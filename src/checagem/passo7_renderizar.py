"""PASSO 7 — renderizar o vídeo anotado.

Um `overlay` por cartela, encadeado, cada um com `enable='between(t,entra,sai)'`.
Como cada cartela já é um quadro inteiro de 1920x1080 com moldura e tarja desenhadas
(PASSO 6), o grafo de filtro é uma linha por card e nada mais.

🔴 Duas travas que existem por motivo, não por gosto:

  1. **O grafo vai para um arquivo.** Uma sabatina de 45 min produz mais de cem cartelas, e a
     linha de comando do Windows estoura em 32 KB. ⚠️ Qual opção passa esse arquivo **depende
     da versão do ffmpeg** — ver `_opcao_de_script`.
  2. **O áudio é copiado, nunca reencodado.** O vídeo existe para ser conferido contra a
     peça original: reencodar áudio muda o arquivo sem necessidade nenhuma. A única exceção é
     opt-in, `--som-de-entrada`, que mixa um estalo curto a cada cartela que entra.

🔧 30/set/2026: cada cartela (menos o selo, que já está na tela no primeiro quadro) entra com um
fade de 8 quadros. Para o `fade` ter o que fazer, a cartela vira uma entrada em laço só pela sua
própria vida (`-loop 1 -t`), deslocada no tempo com `setpts`: o custo é de segundos de quadros por
cartela, não de minutos. Ver docs/ARQUITETURA.md §5.
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


def _acrescimo(plano: dict) -> float:
    """Segundos acrescentados ao fim do trecho: congelamento de leitura mais encerramento."""
    return (float((plano.get("congelamento") or {}).get("duracao_s", 0.0))
            + float((plano.get("encerramento") or {}).get("duracao_s", 0.0)))


def _sobreposicoes(plano: dict, com_legenda: bool) -> list[dict]:
    """Tudo que é sobreposto ao vídeo, na ordem das entradas do ffmpeg (depois da 0).

    `entra` marca o que entra animado: é ele que vira entrada em laço com fade (e, opcionalmente,
    som). O selo é permanente e já está no primeiro quadro, então entra seco.
    """
    itens: list[dict] = []
    if plano.get("selo"):
        itens.append({**plano["selo"], "entra": False})
    if com_legenda and plano.get("legenda"):
        itens.append({"arquivo": plano["legenda"]["arquivo"], "entra": True,
                      "entra_s": plano["legenda"]["entra_s"], "sai_s": plano["legenda"]["sai_s"]})
    itens.extend({**c, "entra": True} for c in plano["cartelas"])
    if plano.get("encerramento"):
        itens.append({**plano["encerramento"], "entra": True})
    return itens


def _grafo(plano: dict, com_legenda: bool) -> tuple[list[str], str]:
    """Devolve (linhas do filtro, rótulo da saída de vídeo)."""
    linhas: list[str] = []
    atual = "0:v"

    # A cartela de encerramento vive DEPOIS do fim do trecho, sobre o último quadro congelado.
    # O áudio não é tocado: continua copiado, e simplesmente acaba antes do vídeo.
    # Antes dele, o congelamento de leitura (se a fila de cards passou do fim do trecho).
    extra = _acrescimo(plano)
    if extra > 0:
        linhas.append(f"[0:v]tpad=stop_mode=clone:stop_duration={extra:.3f}[base]")
        atual = "base"

    if not plano["cartelas"]:
        raise ErroDeExecucao("o plano não tem nenhuma cartela para sobrepor")

    for indice, e in enumerate(_sobreposicoes(plano, com_legenda), start=1):
        fonte = f"{indice}:v"
        if e["entra"]:
            fonte = f"c{indice}"
            linhas.append(
                f"[{indice}:v]format=rgba,fade=t=in:st=0:d={cfg.ENTRADA_FADE_S}:alpha=1,"
                f"setpts=PTS+{e['entra_s']:.3f}/TB[{fonte}]"
            )
        rotulo = f"v{indice}"
        linhas.append(
            f"[{atual}][{fonte}]overlay=0:0:eof_action={'pass' if e['entra'] else 'repeat'}:"
            f"enable='between(t,{e['entra_s']:.3f},{e['sai_s']:.3f})'[{rotulo}]"
        )
        atual = rotulo
    return linhas, atual


def _linhas_de_som(plano: dict, com_legenda: bool, canais: int = 2) -> tuple[list[str], str]:
    """Mixa um estalo curto no quadro em que cada cartela começa a entrar.

    Opt-in (`--som-de-entrada`): reencoda o áudio. O estalo é um seno de 880 Hz de 90 ms que cai
    em 80 ms, a -20 dBFS de pico, gerado pelo próprio ffmpeg (nenhum arquivo de terceiros).
    `normalize=0` no `amix`: sem ele, o ffmpeg abaixaria a fala para dar lugar aos estalos. E o
    estalo nasce no mesmo layout de canais da fala (`canais`): forçar estéreo sobre uma fala mono
    baixa a fala 3 dB no upmix, e a fala não pode mudar de nível por causa de um efeito.
    """
    layout = "mono" if canais == 1 else "stereo"
    entradas = [e for e in _sobreposicoes(plano, com_legenda) if e["entra"]]
    linhas: list[str] = [f"[0:a]aresample=48000,aformat=channel_layouts={layout}[fala]"]
    rotulos = ["[fala]"]
    for n, e in enumerate(entradas):
        atraso = max(0, round(e["entra_s"] * 1000))
        linhas.append(
            "sine=frequency=880:duration=0.09:sample_rate=48000,"
            f"afade=t=out:st=0.01:d=0.08,volume=0.1,aformat=channel_layouts={layout},"
            f"adelay={atraso}|{atraso}[som{n}]"
        )
        rotulos.append(f"[som{n}]")
    linhas.append(f"{''.join(rotulos)}amix=inputs={len(rotulos)}:duration=first:normalize=0[aout]")
    return linhas, "[aout]"


def renderizar(slug: str, *, recorte: str | None = None, crf: int = 16,
               preset: str = "slow", com_legenda: bool = True,
               sufixo: str = "", som_de_entrada: bool = False) -> Path:
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
    rotulo_audio = None
    if som_de_entrada:
        linhas_som, rotulo_audio = _linhas_de_som(plano, com_legenda, medido["audio_canais"] or 2)
        linhas += linhas_som
    script = caso / "render" / f"_filtro-{base}.txt"
    script.write_text(";\n".join(linhas) + "\n", encoding="utf-8", newline="\n")

    sobrepostas = _sobreposicoes(plano, com_legenda)
    entradas_png = [str(caso / e["arquivo"]) for e in sobrepostas]
    acrescimo = _acrescimo(plano)

    faltando = [p for p in entradas_png if not Path(p).exists()]
    if faltando:
        raise ErroDeExecucao(f"cartela ausente: {faltando[0]} — rode o PASSO 6 de novo")

    passo(f"PASSO 7 · renderizar — {len(entradas_png)} sobreposições sobre {entrada.name}")
    info(f"{medido['largura']}x{medido['altura']} · {medido['fps']} fps · {hms(medido['duracao_s'])}")
    info(f"libx264 crf {crf} preset {preset} · "
         + ("áudio com o estalo de entrada mixado (aac 192k)" if som_de_entrada
            else "áudio copiado sem reencodar"))

    cmd = ["ffmpeg", "-v", "error", "-stats", "-i", str(entrada)]
    for arquivo, e in zip(entradas_png, sobrepostas, strict=True):
        if e["entra"]:
            # a cartela só existe durante a sua janela; o fade precisa de quadros de verdade
            cmd += ["-loop", "1", "-framerate", str(cfg.FPS_SAIDA),
                    "-t", f"{e['sai_s'] - e['entra_s'] + 0.25:.3f}"]
        cmd += ["-i", arquivo]
    cmd += [
        *_opcao_de_script(script),
        "-map", f"[{rotulo}]", *(["-map", rotulo_audio] if rotulo_audio else ["-map", "0:a?"]),
        "-c:v", "libx264", "-preset", preset, "-crf", str(crf),
        "-pix_fmt", "yuv420p", "-profile:v", "high", "-level", "4.2",
        *(["-c:a", "aac", "-b:a", "192k"] if rotulo_audio else ["-c:a", "copy"]),
        "-movflags", "+faststart",
        "-y", str(saida),
    ]
    rodar(cmd)

    final = sondar(saida)
    ok(f"{saida.relative_to(cfg.RAIZ)} · {saida.stat().st_size / 1e6:.1f} MB")
    info(f"{final['largura']}x{final['altura']} · {final['fps']} fps · {hms(final['duracao_s'])}")

    esperado = medido["duracao_s"] + acrescimo
    desvio = abs(final["duracao_s"] - esperado)
    if desvio > 0.15:
        aviso(f"a duração saiu {desvio:.2f}s diferente do esperado "
              f"({hms(medido['duracao_s'])} da entrada + {acrescimo:.0f}s de congelamento e encerramento)")
    else:
        ok(f"duração casa com a entrada + {acrescimo:.0f}s de congelamento e encerramento "
           f"(desvio {desvio * 1000:.0f} ms)")
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
    p.add_argument("--som-de-entrada", action="store_true",
                   help="mixa um estalo curto a cada cartela que entra (reencoda o áudio)")
    args = p.parse_args(argv)
    renderizar(args.slug, recorte=args.recorte, crf=args.crf, preset=args.preset,
               com_legenda=not args.sem_legenda, sufixo=args.sufixo,
               som_de_entrada=args.som_de_entrada)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
