"""Desenha as cartelas e roda o validador em TODOS os casos e recortes do repositório.

    python ferramentas/validar-todos.py [--sem-overlay]

É o que a CI roda. Existe porque a porta só vale se valer para todo caso: a versão anterior
da CI validava um caso escrito à mão no workflow, e um segundo caso entraria sem passar por
ela.

Um "alvo" é cada arquivo `alegacoes/alegacoes[-<recorte>].json` que tem a checagem
correspondente. Alegações sem checagem ainda (caso em andamento, antes do PASSO 5) aparecem
como pendentes, sem reprovar: o validador de cada caso é que diz quando ele está pronto.

Sai com 1 se qualquer alvo reprovar.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from checagem import config as cfg  # noqa: E402
from checagem.passo6_overlay import montar  # noqa: E402
from checagem.passo8_validar import validar  # noqa: E402


def alvos() -> list[tuple[str, str | None]]:
    achados = []
    for caso in sorted(p for p in cfg.CASOS.iterdir() if (p / "CASO.json").exists()):
        for arq in sorted((caso / "alegacoes").glob("alegacoes*.json")):
            recorte = arq.stem[len("alegacoes-"):] if arq.stem != "alegacoes" else None
            checagens = caso / "checagens" / (f"checagens-{recorte}.json" if recorte else "checagens.json")
            if checagens.exists():
                achados.append((caso.name, recorte))
            else:
                print(f"  · pendente: {caso.name} {recorte or ''} (alegações sem checagem ainda)")
    return achados


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("--sem-overlay", action="store_true", help="não redesenha as cartelas")
    args = p.parse_args()

    reprovados = []
    lista = alvos()
    for slug, recorte in lista:
        if not args.sem_overlay:
            montar(slug, recorte=recorte)
        if validar(slug, recorte=recorte) != 0:
            reprovados.append(f"{slug} {recorte or ''}".strip())

    print()
    if reprovados:
        print(f"✗ {len(reprovados)} de {len(lista)} alvos reprovados: {', '.join(reprovados)}")
        return 1
    print(f"✓ {len(lista)} alvos aprovados")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
