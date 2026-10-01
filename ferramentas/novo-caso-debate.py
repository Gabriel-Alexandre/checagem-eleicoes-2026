"""Abre a pasta de um caso de DEBATE, com os falantes já declarados e a mídia por registrar.

    python ferramentas/novo-caso-debate.py <slug> --titulo "..." --data AAAA-MM-DD --veiculo "TV Globo" \\
        --mediador "César Tralli" --candidato "Nome (PARTIDO)" --candidato "Nome (PARTIDO)" ...

Depois que o vídeo existir:

    python -m checagem midia <slug> registrar        # assina o arquivo e completa o bloco `midia` do CASO.json
    python -m checagem midia <slug> audio
    python -m checagem transcrever <slug>
    # escrever transcricao/falantes.json (turnos) e rodar: python -m checagem falantes <slug>

O CASO.json nasce com `midia` zerada: é o `registrar` que a preenche. ⛔ Não registre o arquivo errado
só para o validador passar: a procedência (`procedencia`) é o que torna a checagem conferível.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from checagem import config as cfg  # noqa: E402


def _nome_e_partido(texto: str) -> tuple[str, str | None]:
    m = re.match(r"^(.*?)\s*\((.+)\)\s*$", texto)
    return (m.group(1).strip(), m.group(2).strip()) if m else (texto.strip(), None)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug")
    p.add_argument("--titulo", required=True)
    p.add_argument("--data", required=True)
    p.add_argument("--veiculo", required=True)
    p.add_argument("--programa", default=None)
    p.add_argument("--mediador", action="append", default=[], help="repita para mais de um")
    p.add_argument("--candidato", action="append", default=[], help='"Nome (PARTIDO)"; repita')
    p.add_argument("--ausente", action="append", default=[], help='candidato que não foi, para o registro')
    p.add_argument("--url-oficial", default=None)
    a = p.parse_args()

    if not re.match(r"^\d{4}-\d{2}-\d{2}-[a-z0-9-]+$", a.slug):
        sys.exit("slug no formato AAAA-MM-DD-nome-em-kebab")
    pasta = cfg.pasta_do_caso(a.slug)
    if (pasta / "CASO.json").exists():
        sys.exit(f"{pasta} já tem CASO.json: não sobrescrevo")

    falantes = [{"nome": n, "papel": "entrevistador", "cargo_ou_partido": a.veiculo,
                 "descricao": "Mediação do debate."} for n in a.mediador]
    for c in a.candidato:
        nome, partido = _nome_e_partido(c)
        falantes.append({"nome": nome, "papel": "entrevistado", "cargo_ou_partido": partido,
                         "descricao": "Candidato à Presidência da República, debatedor."})
    obs = ("Debate com mais de um candidato: o papel `entrevistado` vale para cada debatedor. "
           "A pergunta que um candidato faz a outro afirma fato e entra na checagem, com o autor dela.")
    if a.ausente:
        obs += " Ausentes: " + ", ".join(a.ausente) + " (não são falantes)."
    meta = {
        "slug": a.slug, "titulo": a.titulo, "data_do_evento": a.data, "veiculo": a.veiculo,
        "programa": a.programa, "formato": "debate",
        "eleicao": "Eleições gerais 2026, Presidência da República",
        "duracao_s": 1,
        "falantes": falantes,
        "midia": {"arquivo": "a-registrar.mp4", "sha256": "0" * 64, "bytes": 0, "largura": 1920,
                  "altura": 1080, "fps": 30},
        "procedencia": {"como_foi_obtido": "A PREENCHER antes de qualquer transcrição (PASSO 0).",
                        "url_oficial": a.url_oficial, "integralidade": "desconhecido", "observacoes": obs},
    }
    for sub in ("fonte", "transcricao", "alegacoes", "checagens", "recortes"):
        (pasta / sub).mkdir(parents=True, exist_ok=True)
    (pasta / "CASO.json").write_text(json.dumps(meta, ensure_ascii=False, indent=2) + "\n",
                                     encoding="utf-8", newline="\n")
    print(f"✓ {pasta.relative_to(RAIZ)} · {len(falantes)} falantes · próximo: preencher a procedência e registrar a mídia")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
