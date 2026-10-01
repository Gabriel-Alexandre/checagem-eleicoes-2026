"""Deriva as alegações e checagens de um RECORTE de vídeo a partir da checagem da peça inteira.

No debate, a validação roda sobre a peça toda (recorte `debate-completo`, sem vídeo renderizado) e
só alguns trechos viram vídeo com cartela. Em vez de checar de novo, o recorte do vídeo **herda** as
checagens da peça inteira, com os mesmos ids:

    python ferramentas/derivar-recorte.py <slug> --de debate-completo --para corte-01 \\
        --inicio 1234.5 --fim 1410.0

    1. python -m checagem midia <slug> recortar corte-01 --inicio 1234.5 --duracao 175.5 --motivo "..."
    2. python ferramentas/derivar-recorte.py ...          (este script)
    3. python -m checagem overlay <slug> --recorte corte-01
       python -m checagem renderizar <slug> --recorte corte-01
       python -m checagem validar <slug> --recorte corte-01

🔴 O trecho tem que ser CONTÍNUO e conter a alegação inteira (etica-e-risco §4). Alegação que
atravessa a borda do trecho derruba o script: mexa na borda, não na alegação. ⛔ A escolha do
trecho vem dos critérios declarados ANTES dos vereditos (docs/DEBATES.md §5), e o `--motivo` do
recorte diz qual foi.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from checagem import config as cfg  # noqa: E402


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug")
    p.add_argument("--de", default="debate-completo")
    p.add_argument("--para", required=True)
    p.add_argument("--inicio", type=float, required=True, help="início absoluto do trecho, em segundos")
    p.add_argument("--fim", type=float, required=True, help="fim absoluto do trecho, em segundos")
    args = p.parse_args()

    caso = cfg.pasta_do_caso(args.slug)
    a = json.loads((caso / "alegacoes" / f"alegacoes-{args.de}.json").read_text(encoding="utf-8"))
    c = json.loads((caso / "checagens" / f"checagens-{args.de}.json").read_text(encoding="utf-8"))
    if args.fim <= args.inicio:
        print("✗ --fim tem que ser maior que --inicio")
        return 1

    dentro, cortadas = [], []
    for al in a["alegacoes"]:
        if al["fim_s"] <= args.inicio + 0.05 or al["inicio_s"] >= args.fim - 0.05:
            continue
        if al["inicio_s"] < args.inicio - 0.05 or al["fim_s"] > args.fim + 0.05:
            cortadas.append(al["id"])
        else:
            dentro.append(al)
    if cortadas:
        print(f"✗ alegações que atravessam a borda do trecho: {', '.join(cortadas)}. "
              "Mexa na borda (use uma pausa entre falas), nunca na alegação.")
        return 1
    if not dentro:
        print("✗ nenhuma alegação dentro do trecho")
        return 1

    ids = {x["id"] for x in dentro}
    doc_a = {k: v for k, v in a.items() if k not in ("alegacoes", "exclusoes", "cobertura", "recorte")}
    doc_a.update({
        "gerado_em": date.today().isoformat(), "recorte": args.para,
        "cobertura": {"inicio_s": args.inicio, "fim_s": args.fim},
        "alegacoes": dentro,
    })
    exc = [e for e in a.get("exclusoes", []) if args.inicio <= e["inicio_s"] <= args.fim]
    if exc:
        doc_a["exclusoes"] = exc
    doc_c = {k: v for k, v in c.items() if k != "checagens"}
    doc_c["fonte_alegacoes"] = f"casos/{args.slug}/alegacoes/alegacoes-{args.para}.json"
    doc_c["checagens"] = [x for x in c["checagens"] if x["id"] in ids]

    (caso / "alegacoes" / f"alegacoes-{args.para}.json").write_text(
        json.dumps(doc_a, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    (caso / "checagens" / f"checagens-{args.para}.json").write_text(
        json.dumps(doc_c, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    por = {}
    for al in dentro:
        por[al["falante"]] = por.get(al["falante"], 0) + 1
    print(f"✓ {len(dentro)} alegações em {args.para}: " + " · ".join(f"{k} {v}" for k, v in por.items()))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
