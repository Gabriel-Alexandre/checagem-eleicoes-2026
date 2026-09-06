"""Confere que todo link interno da documentação aponta para um arquivo que existe.

Documentação que promete um arquivo inexistente é pior do que documentação faltando: ela
manda a pessoa procurar uma coisa que não está lá. Este repositório aponta muito de um
documento para outro, então o risco é real e cresce a cada arquivo novo.

⛔ Não confere link externo (http), de propósito: URL de fonte é conferida na hora da
checagem, com data de consulta, e sair batendo em site de terceiro a cada commit é
comportamento que nenhum servidor merece.

Uso:
    python ferramentas/conferir-links.py          # sai 1 se achar link quebrado
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[1]
IGNORAR = {".git", "node_modules", "__pycache__", ".venv", "venv", ".pytest_cache", ".ruff_cache"}

# [texto](destino) — sem casar imagem inline nem link de referência.
LINK = re.compile(r"\[[^\]]*\]\(\s*<?([^)>\s]+)>?\s*(?:\"[^\"]*\")?\)")


def documentos() -> list[Path]:
    achados = []
    for p in RAIZ.rglob("*"):
        if p.suffix.lower() not in {".md", ".mdc"} or not p.is_file():
            continue
        if any(parte in IGNORAR for parte in p.parts):
            continue
        achados.append(p)
    return sorted(achados)


def quebrados() -> list[tuple[Path, str]]:
    erros: list[tuple[Path, str]] = []
    for doc in documentos():
        texto = doc.read_text(encoding="utf-8", errors="replace")
        for destino in LINK.findall(texto):
            if destino.startswith(("http://", "https://", "mailto:", "#")):
                continue
            alvo = destino.split("#", 1)[0]
            if not alvo:
                continue
            if not (doc.parent / alvo).resolve().exists():
                erros.append((doc, destino))
    return erros


def main() -> int:
    erros = quebrados()
    total = len(documentos())
    for doc, destino in erros:
        rel = doc.relative_to(RAIZ)
        print(f"  ✗ {rel}: link quebrado para '{destino}'")
    if erros:
        print(f"\n✗ {len(erros)} link(s) quebrado(s) em {total} documentos")
        return 1
    print(f"✓ {total} documentos, nenhum link interno quebrado")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
