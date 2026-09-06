"""Ativos do repositório — hoje, só as fontes tipográficas.

A Inter entra como fonte variável (um arquivo, nove pesos) sob licença OFL. Ela não é
commitada: 1,8 MB de binário num repositório de texto envelhece mal e o download é de
uma vez só.
"""

from __future__ import annotations

import argparse
import urllib.request

from . import config as cfg
from .util import ErroDeExecucao, info, ok, passo

FONTES = {
    "Inter-VariableFont.ttf":
        "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter%5Bopsz,wght%5D.ttf",
    "Inter-Italic-VariableFont.ttf":
        "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/Inter-Italic%5Bopsz,wght%5D.ttf",
    "OFL.txt":
        "https://raw.githubusercontent.com/google/fonts/main/ofl/inter/OFL.txt",
}


def baixar_fontes(*, forcar: bool = False) -> None:
    cfg.FONTES_DIR.mkdir(parents=True, exist_ok=True)
    passo("baixando as fontes (Inter, licença OFL)")
    for nome, url in FONTES.items():
        destino = cfg.FONTES_DIR / nome
        if destino.exists() and destino.stat().st_size > 1000 and not forcar:
            info(f"{nome} já está aqui")
            continue
        with urllib.request.urlopen(url) as r:  # noqa: S310
            dados = r.read()
        if len(dados) < 1000:
            raise ErroDeExecucao(f"o download de {nome} veio vazio ou com erro ({len(dados)} bytes)")
        destino.write_bytes(dados)
        ok(f"{nome} · {len(dados) / 1024:.0f} KB")


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem ativos")
    sub = p.add_subparsers(dest="acao", required=True)
    b = sub.add_parser("baixar-fontes")
    b.add_argument("--forcar", action="store_true")
    args = p.parse_args(argv)
    baixar_fontes(forcar=args.forcar)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
