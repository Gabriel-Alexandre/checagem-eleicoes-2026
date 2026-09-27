"""Registra a revisão de checagens, com revisor, data, decisão e nota.

Revisão por IA (o padrão do projeto desde 27/set/2026), com uma nota por checagem:

    python ferramentas/registrar-revisao.py <slug> --recorte ID --ia --notas revisao.json

    revisao.json: {"revisor": "...", "A001": {"decisao": "mantido", "nota": "...",
                   "verificacoes": ["..."]}, ...}

Revisão humana, quando uma pessoa também ler:

    python ferramentas/registrar-revisao.py <slug> --recorte ID --revisor "Nome Sobrenome" \\
        [--ids A001 A002 ...] [--decisao mantido|alterado|removido] [--nota "..."]

🔴 A revisão por IA é uma passada ADVERSARIAL separada da checagem (skills/revisar-checagem.md):
ela tenta derrubar cada veredito. ⛔ Um agente não preenche `revisao_humana` em nome de ninguém.

`decisao: alterado` é para quando a leitura mudou algo: nesse caso, a mudança em si vai para
`casos/<slug>/CORRECOES.md`, com o antes e o depois.
"""

from __future__ import annotations

import argparse
import json
import sys
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def main() -> int:
    p = argparse.ArgumentParser(description="registra revisão humana nas checagens")
    p.add_argument("slug")
    p.add_argument("--recorte", required=True)
    p.add_argument("--revisor", default=None)
    p.add_argument("--ia", action="store_true", help="registra revisao_ia a partir de --notas")
    p.add_argument("--notas", default=None, help="JSON com a decisão e a nota de cada checagem")
    p.add_argument("--ids", nargs="*", default=None)
    p.add_argument("--decisao", default="mantido", choices=["mantido", "alterado", "removido"])
    p.add_argument("--nota", default=None)
    a = p.parse_args()

    caminho = RAIZ / "casos" / a.slug / "checagens" / f"checagens-{a.recorte}.json"
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    hoje = date.today().isoformat()
    marcadas = []
    if a.ia:
        notas = json.loads(Path(a.notas).read_text(encoding="utf-8"))
        revisor = notas.pop("revisor")
        for c in dados["checagens"]:
            n = notas.get(c["id"])
            if not n:
                continue
            c["revisao_ia"] = {"revisor": revisor, "data": hoje, "decisao": n["decisao"],
                               "nota": n["nota"]}
            if n.get("verificacoes"):
                c["revisao_ia"]["verificacoes"] = n["verificacoes"]
            marcadas.append(c["id"])
        faltando = [c["id"] for c in dados["checagens"] if c["id"] not in marcadas]
        caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"revisão por IA registrada em {len(marcadas)} checagens"
              + (f"; SEM revisão: {' '.join(faltando)}" if faltando else ""))
        return 0
    if not a.revisor:
        p.error("--revisor é obrigatório para revisão humana")
    for c in dados["checagens"]:
        if a.ids is not None and c["id"] not in a.ids:
            continue
        if a.ids is None and c.get("revisao_humana"):
            continue
        c["revisao_humana"] = {"revisor": a.revisor, "data": hoje, "decisao": a.decisao}
        if a.nota:
            c["revisao_humana"]["nota"] = a.nota
        marcadas.append(c["id"])

    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"revisão registrada em {len(marcadas)} checagens: {' '.join(marcadas)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
