"""PASSO 7 — renderizar o vídeo anotado.

Um `overlay` por cartela, encadeado, cada um com `enable='between(t,entra,sai)'`.
Como cada cartela já é um quadro inteiro de 1920x1080 com moldura e tarja desenhadas
(PASSO 6), o grafo de filtro é uma linha por card e nada mais.

🔴 Duas travas que existem por motivo, não por gosto:

  1. **O grafo vai para um arquivo.** Uma sabatina de 45 min produz mais de cem cartelas, e a
     linha de comando do Windows estoura em 32 KB. ⚠️ Qual opção passa esse arquivo **depende
     da versão do ffmpeg** — ver `_opcao_de_script`.
  2. **O áudio é copiado, nunca reencodado.** O vídeo existe para ser conferido contra a
     peça original: reencodar áudio muda o arquivo sem necessidade nenhuma.
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path

from . import config as cfg
from .util import (
    ErroDeExecucao,
    aviso,
    exigir_binario,
    hms,
    info,
    ler_json,
    ok,
    passo,
    rodar,
    sondar,
)


def _opcao_de_script(script: Path) -> list[str]:
    """Como passar o grafo de filtro por arquivo, que muda com a versão do ffmpeg.

    Até a série 7 era `-filter_complex_script <arquivo>`. Na 8 essa opção **foi removida** e
    substituída pela sintaxe genérica `-/<opção> <arquivo>`, que lê o valor de qualquer opção
    de um arquivo. Com o ffmpeg 9 instalado, a forma antiga morre com
    "Unrecognized option 'filter_complex_script'" — que foi exatamente como este projeto
    descobriu a mudança.

    ⛔ Não dá para simplesmente passar o grafo na linha de comando: uma peça de 45 minutos
    produz mais de cem cartelas, e o comando estoura o limite de 32 KB do Windows.
    """
    r = rodar(["ffmpeg", "-hide_banner", "-version"], silencioso=True)
    primeira = (r.stdout or "").splitlines()[0] if r.stdout else ""
    m = re.search(r"ffmpeg version n?(\d+)", primeira)
    maior = int(m.group(1)) if m else 0
    if maior >= 8:
        return ["-/filter_complex", str(script)]
    return ["-filter_complex_script", str(script)]


def _nivel_de_audio(caminho: Path) -> float | None:
    """Volume médio da faixa, em dB. É a prova de que não entrou silêncio no lugar do áudio.

    ⚠️ Precisa de `-v info`: o `volumedetect` escreve o resultado em nível informativo, e com
    `-v error` a medição sai vazia sem dar erro nenhum — que é o pior tipo de falha, a que
    parece sucesso.
    """
    r = rodar(["ffmpeg", "-hide_banner", "-nostats", "-v", "info",
               "-i", str(caminho), "-af", "volumedetect", "-f", "null", "-"],
              silencioso=True)
    m = re.search(r"mean_volume:\s*(-?[\d.]+) dB", (r.stderr or "") + (r.stdout or ""))
    return float(m.group(1)) if m else None


def _grafo(plano: dict, com_legenda: bool) -> tuple[list[str], str]:
    """Devolve (linhas do filtro, rótulo da saída de vídeo)."""
    linhas: list[str] = []
    atual = "0:v"
    indice = 1

    entradas: list[dict] = []
    if plano.get("selo"):
        entradas.append(plano["selo"])
    if com_legenda and plano.get("legenda"):
        entradas.append({"arquivo": plano["legenda"]["arquivo"],
                         "entra_s": plano["legenda"]["entra_s"],
                         "sai_s": plano["legenda"]["sai_s"]})
    entradas.extend(plano["cartelas"])

    for e in entradas:
        rotulo = f"v{indice}"
        linhas.append(
            f"[{atual}][{indice}:v]overlay=0:0:eof_action=repeat:"
            f"enable='between(t,{e['entra_s']:.3f},{e['sai_s']:.3f})'[{rotulo}]"
        )
        atual = rotulo
        indice += 1

    if not linhas:
        raise ErroDeExecucao("o plano não tem nenhuma cartela para sobrepor")
    return linhas, atual


def renderizar(slug: str, *, recorte: str | None = None, crf: int = 16,
               preset: str = "slow", com_legenda: bool = True,
               sufixo: str = "") -> Path:
    exigir_binario("ffmpeg", "scoop install ffmpeg · apt install ffmpeg · brew install ffmpeg")
    caso = cfg.pasta_do_caso(slug)
    nome_plano = f"plano-{recorte}.json" if recorte else "plano.json"
    plano = ler_json(caso / "overlay" / nome_plano)

    entrada = caso / plano["alvo"]
    if not entrada.exists():
        raise ErroDeExecucao(f"o vídeo de entrada não está aqui: {entrada}")

    medido = sondar(entrada)
    if (medido["largura"], medido["altura"]) != (plano["largura"], plano["altura"]):
        raise ErroDeExecucao(
            f"o vídeo é {medido['largura']}x{medido['altura']} e as cartelas foram desenhadas "
            f"para {plano['largura']}x{plano['altura']}.\n"
            "  As cartelas são quadros inteiros: resolução diferente desalinha tudo."
        )

    base = f"{slug}-checado" + (f"-{recorte}" if recorte else "") + sufixo
    saida = caso / "render" / f"{base}.mp4"
    saida.parent.mkdir(parents=True, exist_ok=True)

    linhas, rotulo = _grafo(plano, com_legenda)
    script = caso / "render" / f"_filtro-{base}.txt"
    script.write_text(";\n".join(linhas) + "\n", encoding="utf-8", newline="\n")

    entradas_png: list[str] = []
    if plano.get("selo"):
        entradas_png.append(str(caso / plano["selo"]["arquivo"]))
    if com_legenda and plano.get("legenda"):
        entradas_png.append(str(caso / plano["legenda"]["arquivo"]))
    entradas_png.extend(str(caso / c["arquivo"]) for c in plano["cartelas"])

    faltando = [p for p in entradas_png if not Path(p).exists()]
    if faltando:
        raise ErroDeExecucao(f"cartela ausente: {faltando[0]} — rode o PASSO 6 de novo")

    passo(f"PASSO 7 · renderizar — {len(entradas_png)} sobreposições sobre {entrada.name}")
    info(f"{medido['largura']}x{medido['altura']} · {medido['fps']} fps · {hms(medido['duracao_s'])}")
    info(f"libx264 crf {crf} preset {preset} · áudio copiado sem reencodar")

    cmd = ["ffmpeg", "-v", "error", "-stats", "-i", str(entrada)]
    for p in entradas_png:
        cmd += ["-i", p]
    cmd += [
        *_opcao_de_script(script),
        "-map", f"[{rotulo}]", "-map", "0:a?",
        "-c:v", "libx264", "-preset", preset, "-crf", str(crf),
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.2",
        "-c:a", "copy", "-movflags", "+faststart",
        "-y", str(saida),
    ]
    rodar(cmd)

    final = sondar(saida)
    ok(f"{saida.relative_to(cfg.RAIZ)} · {saida.stat().st_size / 1e6:.1f} MB")
    info(f"{final['largura']}x{final['altura']} · {final['fps']} fps · {hms(final['duracao_s'])}")

    desvio = abs(final["duracao_s"] - medido["duracao_s"])
    if desvio > 0.15:
        aviso(f"a duração saiu {desvio:.2f}s diferente da entrada")
    else:
        ok(f"duração casa com a entrada (desvio {desvio * 1000:.0f} ms)")
    if final["codec_audio"] is None:
        aviso("o vídeo saiu SEM faixa de áudio")
    else:
        nivel = _nivel_de_audio(saida)
        if nivel is None:
            aviso("não foi possível medir o nível do áudio")
        elif nivel < -60:
            aviso(f"o áudio está em {nivel:.1f} dB — isso é silêncio, não fala")
        else:
            ok(f"áudio presente e audível · volume médio {nivel:.1f} dB")
    script.unlink(missing_ok=True)
    return saida


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem renderizar", description="PASSO 7 — renderizar")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    p.add_argument("--crf", type=int, default=16)
    p.add_argument("--preset", default="slow")
    p.add_argument("--sem-legenda", action="store_true")
    p.add_argument("--sufixo", default="")
    args = p.parse_args(argv)
    renderizar(args.slug, recorte=args.recorte, crf=args.crf, preset=args.preset,
               com_legenda=not args.sem_legenda, sufixo=args.sufixo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
