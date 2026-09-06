"""PASSO 2 — transcrever.

Motor: whisper.cpp (`whisper-cli`), rodando local. Duas razões, e as duas são de método:

  1. **Reprodutibilidade.** Mesmo arquivo + mesmo modelo + mesmos parâmetros = mesma saída.
     Uma API que muda de versão sem avisar não serve de base para um veredito citável.
  2. **Procedência.** O `sha256` do modelo vai no cabeçalho da transcrição. Quem quiser refazer
     a checagem sabe exatamente qual modelo produziu aquelas palavras.

⛔ A transcrição NÃO é corrigida por conveniência. Ela é a evidência do que foi dito.
Correção de erro de reconhecimento é permitida e obrigatória — mas vai registrada em
`transcricao/CORRECOES_DE_TRANSCRICAO.md`, com o antes, o depois e quem conferiu no áudio.
"""

from __future__ import annotations

import argparse
import json
import os
import urllib.request
from datetime import date
from pathlib import Path

from . import config as cfg
from .util import (
    ErroDeExecucao,
    escrever_json,
    exigir_binario,
    hms,
    info,
    ler_json,
    ok,
    passo,
    rodar,
    sha256_do_arquivo,
)

MODELO_PADRAO = "large-v3-turbo"
URL_MODELOS = "https://huggingface.co/ggerganov/whisper.cpp/resolve/main/ggml-{nome}.bin"


def pasta_de_modelos() -> Path:
    p = Path(os.environ.get("CHECAGEM_MODELOS", Path.home() / ".cache" / "whisper-models"))
    p.mkdir(parents=True, exist_ok=True)
    return p


def garantir_modelo(nome: str = MODELO_PADRAO) -> Path:
    destino = pasta_de_modelos() / f"ggml-{nome}.bin"
    if destino.exists() and destino.stat().st_size > 10_000_000:
        return destino
    passo(f"baixando modelo whisper '{nome}' (uma vez só)")
    parcial = destino.with_suffix(".bin.part")
    url = URL_MODELOS.format(nome=nome)
    with urllib.request.urlopen(url) as r, parcial.open("wb") as f:  # noqa: S310
        total = int(r.headers.get("Content-Length", 0))
        baixado = 0
        while bloco := r.read(1 << 20):
            f.write(bloco)
            baixado += len(bloco)
            if total:
                print(f"\r  · {baixado / 1e6:.0f} / {total / 1e6:.0f} MB", end="", flush=True)
    print()
    parcial.rename(destino)
    ok(f"{destino}")
    return destino


# ─────────────────────────────────────────────────────────────────────


def _entrada_de_audio(caso: Path, recorte: str | None) -> tuple[Path, float, str | None]:
    """Devolve (wav, deslocamento_em_segundos_na_peca_inteira, id_do_recorte)."""
    if recorte:
        wav = caso / "recortes" / f"{recorte}.wav"
        indice = ler_json(caso / "recortes" / "RECORTES.json")
        reg = next((r for r in indice["recortes"] if r["id"] == recorte), None)
        if reg is None:
            raise ErroDeExecucao(f"recorte '{recorte}' não está em recortes/RECORTES.json")
        return wav, float(reg["origem_inicio_s"]), recorte

    candidatos = sorted((caso / "fonte").glob("*.wav"))
    if not candidatos:
        raise ErroDeExecucao(
            "não há WAV em fonte/. Rode antes:  python -m checagem midia <slug> audio"
        )
    return candidatos[0], 0.0, None


def transcrever(slug: str, *, recorte: str | None = None, modelo: str = MODELO_PADRAO,
                threads: int = 0, idioma: str = "pt", reaproveitar_bruto: bool = False) -> Path:
    caso = cfg.pasta_do_caso(slug)
    wav, deslocamento, id_recorte = _entrada_de_audio(caso, recorte)
    nome_saida = f"transcricao-{id_recorte}" if id_recorte else "transcricao"
    bruto = caso / "transcricao" / f"{nome_saida}.bruto"
    bruto.parent.mkdir(parents=True, exist_ok=True)
    threads = threads or max(2, (os.cpu_count() or 4) - 2)
    parametros = ["-t", str(threads), "-bs", "5", "-bo", "5", "-ml", "0"]

    if reaproveitar_bruto:
        # Renormaliza uma saída de whisper.cpp que já existe, sem gastar CPU de novo.
        # ⚠️ Só é honesto quando os parâmetros abaixo são os que produziram aquele arquivo.
        # O cabeçalho da transcrição registra exatamente isto, então mentir aqui é mentir no
        # dado que serve para outra pessoa refazer o trabalho.
        if not bruto.with_suffix(".bruto.json").exists():
            raise ErroDeExecucao(
                f"--reaproveitar-bruto pedido, mas {bruto.with_suffix('.bruto.json').name} não existe"
            )
        caminho_modelo = garantir_modelo(modelo)
        passo(f"PASSO 2 · renormalizar saída existente — {bruto.with_suffix('.bruto.json').name}")
    else:
        exigir_binario("whisper-cli", "scoop install whisper-cpp · ou compile o whisper.cpp")
        if not wav.exists():
            raise ErroDeExecucao(f"não encontrei {wav}")
        caminho_modelo = garantir_modelo(modelo)
        passo(f"PASSO 2 · transcrever — {wav.name} · modelo {modelo} · {threads} threads")
        info("o whisper.cpp roda a ~3x tempo real nesta máquina; 45 min de áudio levam ~15 min")
        rodar([
            "whisper-cli", "-m", str(caminho_modelo), "-f", str(wav),
            "-l", idioma, *parametros,
            "-oj", "-ojf", "-osrt", "-ovtt", "-otxt",
            "-of", str(bruto), "-np",
        ])

    normalizado = _normalizar(
        bruto.with_suffix(".bruto.json"),
        slug=slug, origem=wav, recorte=id_recorte, deslocamento=deslocamento,
        modelo=caminho_modelo, idioma=idioma, parametros=" ".join(parametros),
    )
    destino = caso / "transcricao" / f"{nome_saida}.json"
    escrever_json(destino, normalizado)

    n = len(normalizado["segmentos"])
    palavras = sum(len(s["texto"].split()) for s in normalizado["segmentos"])
    ok(f"{n} segmentos · {palavras} palavras · {hms(normalizado['duracao_s'])}")
    ok(f"{destino.relative_to(cfg.RAIZ)}")
    return destino


def _normalizar(bruto_json: Path, *, slug: str, origem: Path, recorte: str | None,
                deslocamento: float, modelo: Path, idioma: str, parametros: str) -> dict:
    """whisper.cpp -> o formato do projeto.

    O tempo gravado é SEMPRE o tempo na peça inteira. Um recorte que começa em 12:00
    tem o primeiro segmento em 720s, não em 0s. É isso que permite checar num recorte
    e montar o overlay na peça inteira sem recalcular nada.
    """
    with bruto_json.open(encoding="utf-8") as f:
        dados = json.load(f)

    segmentos = []
    for i, item in enumerate(dados.get("transcription", [])):
        inicio = item["offsets"]["from"] / 1000.0 + deslocamento
        fim = item["offsets"]["to"] / 1000.0 + deslocamento
        texto = item["text"].strip()
        if not texto:
            continue
        segmentos.append({
            "i": i,
            "inicio_s": round(inicio, 3),
            "fim_s": round(fim, 3),
            "texto": texto,
            "falante": None,
        })

    return {
        "caso": slug,
        "origem": origem.name,
        "recorte": recorte,
        "deslocamento_s": round(deslocamento, 3),
        "motor": "whisper.cpp",
        "modelo": modelo.name,
        "modelo_sha256": sha256_do_arquivo(modelo),
        "idioma": idioma,
        "parametros": parametros,
        "gerado_em": date.today().isoformat(),
        "revisao_humana": False,
        "duracao_s": round(segmentos[-1]["fim_s"] - deslocamento, 3) if segmentos else 0.0,
        "segmentos": segmentos,
    }


# ─────────────────────────────────────────────────────────────────────


def exportar_texto(slug: str, *, recorte: str | None = None) -> Path:
    """Escreve a versão legível, com tempo na margem. É por este arquivo que a IA lê a peça."""
    caso = cfg.pasta_do_caso(slug)
    nome = f"transcricao-{recorte}" if recorte else "transcricao"
    dados = ler_json(caso / "transcricao" / f"{nome}.json")
    destino = caso / "transcricao" / f"{nome}.txt"

    linhas = [
        f"# {slug} — transcrição{' · recorte ' + recorte if recorte else ''}",
        f"# motor {dados['motor']} · modelo {dados['modelo']} · idioma {dados['idioma']}",
        f"# tempos em HH:MM:SS na peça inteira · gerado em {dados['gerado_em']}",
        "",
    ]
    falante_atual = object()
    for s in dados["segmentos"]:
        if s["falante"] != falante_atual:
            falante_atual = s["falante"]
            linhas.append("")
            linhas.append(f"[{falante_atual or 'FALANTE NÃO ATRIBUÍDO'}]")
        linhas.append(f"{hms(s['inicio_s'])}  {s['texto']}")

    destino.write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")
    ok(f"{destino.relative_to(cfg.RAIZ)}")
    return destino


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem transcrever", description="PASSO 2 — transcrever")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    p.add_argument("--modelo", default=MODELO_PADRAO)
    p.add_argument("--threads", type=int, default=0)
    p.add_argument("--idioma", default="pt")
    p.add_argument("--so-texto", action="store_true", help="só regera o .txt legível")
    p.add_argument("--reaproveitar-bruto", action="store_true",
                   help="renormaliza um .bruto.json de whisper.cpp que já existe, sem rodar de novo")
    args = p.parse_args(argv)

    if not args.so_texto:
        transcrever(args.slug, recorte=args.recorte, modelo=args.modelo,
                    threads=args.threads, idioma=args.idioma,
                    reaproveitar_bruto=args.reaproveitar_bruto)
    exportar_texto(args.slug, recorte=args.recorte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
