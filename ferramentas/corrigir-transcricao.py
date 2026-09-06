"""Aplica correções de reconhecimento na transcrição, deixando rastro.

> 🔴 **A transcrição é a evidência do que foi dito.** Corrigir é obrigatório quando o motor
> errou — mas corrigir em silêncio destrói o valor dela. Este script existe para que toda
> correção tenha antes, depois, motivo e como foi conferida, num arquivo versionado.

Entrada: `casos/<slug>/transcricao/correcoes.json`

    {
      "correcoes": [
        {
          "inicio_s": 1443.32,
          "de": "Quando eu votei à presidência da República.",
          "para": "Quando eu voltei à presidência da República.",
          "motivo": "erro de reconhecimento: 'votei' por 'voltei'",
          "conferido_como": "2ª passada do whisper.cpp na janela isolada 24:55-25:11, com prompt de contexto"
        }
      ]
    }

Saída: `transcricao.json` atualizado + `CORRECOES_DE_TRANSCRICAO.md` reescrito.

⛔ O script recusa a correção se o texto `de` não bater exatamente com o que está no segmento.
Correção que não bate é correção aplicada duas vezes, ou aplicada no segmento errado.

Uso:
    python ferramentas/corrigir-transcricao.py <slug> [--recorte ID] [--conferir]
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[1]


def hms(s: float) -> str:
    n = int(round(s))
    return f"{n // 3600:02d}:{(n % 3600) // 60:02d}:{n % 60:02d}"


def main() -> int:
    p = argparse.ArgumentParser(description="Aplica correções de transcrição com registro")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    p.add_argument("--conferir", action="store_true", help="só verifica, não escreve nada")
    args = p.parse_args()

    caso = RAIZ / "casos" / args.slug
    nome = f"transcricao-{args.recorte}" if args.recorte else "transcricao"
    alvo = caso / "transcricao" / f"{nome}.json"
    fonte = caso / "transcricao" / "correcoes.json"

    if not fonte.exists():
        print(f"não há {fonte.relative_to(RAIZ)} — nada a corrigir")
        return 0

    transcricao = json.loads(alvo.read_text(encoding="utf-8"))
    correcoes = json.loads(fonte.read_text(encoding="utf-8"))["correcoes"]
    por_inicio = {round(s["inicio_s"], 2): s for s in transcricao["segmentos"]}

    aplicadas, ja_feitas, erros = [], [], []
    for c in correcoes:
        seg = por_inicio.get(round(float(c["inicio_s"]), 2))
        if seg is None:
            erros.append(f"{hms(c['inicio_s'])}: não há segmento começando neste tempo")
            continue
        if seg["texto"] == c["para"]:
            ja_feitas.append(c)
            continue
        if seg["texto"] != c["de"]:
            erros.append(
                f"{hms(c['inicio_s'])}: o segmento diz\n      {seg['texto']!r}\n"
                f"    e a correção esperava\n      {c['de']!r}"
            )
            continue
        if not args.conferir:
            seg["texto"] = c["para"]
        aplicadas.append(c)

    for e in erros:
        print(f"  ✗ {e}")
    if erros:
        print(f"\n✗ {len(erros)} correção(ões) não batem com a transcrição. Nada foi escrito.")
        return 1

    print(f"  ✓ {len(aplicadas)} aplicada(s) · {len(ja_feitas)} já estavam aplicadas")
    if args.conferir:
        return 0

    transcricao["revisao_humana"] = True
    transcricao["correcoes_aplicadas"] = len(correcoes)
    alvo.write_text(json.dumps(transcricao, ensure_ascii=False, indent=2) + "\n",
                    encoding="utf-8", newline="\n")

    L = [
        "# Correções de transcrição",
        "",
        f"**Caso:** `{args.slug}`" + (f" · recorte `{args.recorte}`" if args.recorte else ""),
        f"**Atualizado em:** {date.today().isoformat()}",
        "",
        "A transcrição é gerada por `whisper.cpp` e **erra**, principalmente em nome próprio, "
        "número falado e palavra de contexto técnico. Corrigir é obrigatório; corrigir em silêncio, "
        "não. Toda alteração está abaixo, com o que estava, o que passou a valer e como foi conferida.",
        "",
        "⛔ Nada aqui muda o **sentido** de uma fala. Se uma correção mudasse o sentido, ela não "
        "seria correção: seria edição, e o caso teria que ser refeito.",
        "",
        "| Tempo | Estava | Passou a ser | Como foi conferida |",
        "|---|---|---|---|",
    ]
    for c in sorted(correcoes, key=lambda x: x["inicio_s"]):
        L.append(
            f"| `{hms(c['inicio_s'])}` | {c['de']} | **{c['para']}** | {c['conferido_como']} |"
        )
    L += ["", f"**Total:** {len(correcoes)} correções.", ""]

    destino = caso / "transcricao" / "CORRECOES_DE_TRANSCRICAO.md"
    destino.write_text("\n".join(L), encoding="utf-8", newline="\n")
    print(f"  ✓ {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
