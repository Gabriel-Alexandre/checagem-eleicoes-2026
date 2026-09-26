"""Registra a revisão humana de checagens, com nome, data e decisão.

    python ferramentas/registrar-revisao.py <slug> --recorte ID --revisor "Nome Sobrenome" \\
        [--ids A001 A002 ...] [--decisao mantido|alterado|removido] [--nota "..."]

Sem `--ids`, marca TODAS as checagens do recorte que ainda não têm revisão.

🔴 Quem roda este comando é a PESSOA que leu os cards e as fontes, não a IA. A doutrina diz
que nada vai ao ar sem uma pessoa ter lido (METODOLOGIA §6), e este campo é o registro disso.
⛔ Um agente de IA não preenche `revisao_humana` em nome de ninguém: o validador aceitaria, e é
exatamente por isso que isto é regra escrita e não só código.

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
    p.add_argument("--revisor", required=True)
    p.add_argument("--ids", nargs="*", default=None)
    p.add_argument("--decisao", default="mantido", choices=["mantido", "alterado", "removido"])
    p.add_argument("--nota", default=None)
    a = p.parse_args()

    caminho = RAIZ / "casos" / a.slug / "checagens" / f"checagens-{a.recorte}.json"
    dados = json.loads(caminho.read_text(encoding="utf-8"))
    hoje = date.today().isoformat()
    marcadas = []
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
    print("Agora rode o PASSO 6 de novo: a cartela de encerramento mostra a contagem de revisão.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
