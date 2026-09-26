"""Confere cada `trecho` de fonte contra a página capturada, e grava o recibo em CAPTURAS.json.

    python ferramentas/conferir-trechos.py <slug> --recorte ID --capturas <pasta> [<pasta> ...]

As pastas são as saídas de `capturar-fontes.py` (uma por rodada); a mais recente de cada URL
ganha. Para cada fonte citada nas checagens do recorte:

  · página HTML ou PDF: o trecho, normalizado, tem que existir no texto capturado. Corte interno
    marcado com `[...]` é conferido pedaço a pedaço, como a citação da fala;
  · resposta JSON de API (Banco Central, FMI): o trecho é um recorte de uma série, e a ordem dos
    elementos não é contínua. Aí a conferência é por número: todo número do trecho tem que estar
    na resposta capturada.

🔑 É a trava da citação (a fala tem que existir na transcrição) aplicada ao outro lado: a fonte
tem que existir na página. "Trecho copiado" deixa de ser uma promessa e vira um fato conferido.

O resultado vai para `casos/<slug>/checagens/CAPTURAS.json`, que ENTRA no git: URL, hora da
captura, sha256 do bruto e, para cada checagem que cita a URL, se o trecho foi encontrado.
O texto das páginas não entra.

⚠️ Trecho não encontrado não prova erro: a página pode ter mudado depois da consulta, ou o
trecho pode ter sido montado de dois lugares da mesma página sem o `[...]`. Prova que precisa
de uma leitura, e o validador avisa.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", (t or "").lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


def _numeros(t: str) -> set[str]:
    return {re.sub(r"[.,]", "", n).lstrip("0") or "0"
            for n in re.findall(r"-?\d[\d.,]*\d|\d", t or "")}


def _carregar(pastas: list[Path]) -> dict[str, dict]:
    """URL -> {registro, texto}, a rodada mais nova ganhando."""
    achado: dict[str, dict] = {}
    for pasta in pastas:
        manifesto = pasta / "capturas.json"
        if not manifesto.exists():
            continue
        for c in json.loads(manifesto.read_text(encoding="utf-8"))["capturas"]:
            # Página de erro (403 de um portal que recusa robô) não é captura da fonte: é
            # captura da recusa. Conta como "sem captura", nunca como "trecho não encontrado".
            if not c.get("sha256") or (c.get("status") != 200 and c.get("caracteres_de_texto", 0) < 2000):
                continue
            atual = achado.get(c["url"])
            if atual and atual["registro"]["capturada_em"] >= c["capturada_em"]:
                continue
            arq = pasta / "texto" / f"{c['id']}.txt"
            texto = arq.read_text(encoding="utf-8", errors="replace") if arq.exists() else ""
            achado[c["url"]] = {"registro": c, "texto": texto}
    return achado


def conferir(trecho: str, texto: str, tipo: str) -> bool:
    if "json" in (tipo or ""):
        return _numeros(trecho) <= _numeros(texto)
    alvo = _norm(texto)
    return all(_norm(p) in alvo for p in trecho.split("[...]") if _norm(p))


def main() -> int:
    p = argparse.ArgumentParser(description="confere trechos de fonte contra as capturas")
    p.add_argument("slug")
    p.add_argument("--recorte", required=True)
    p.add_argument("--capturas", nargs="+", required=True)
    a = p.parse_args()

    caso = RAIZ / "casos" / a.slug
    checagens = json.loads((caso / "checagens" / f"checagens-{a.recorte}.json").read_text(encoding="utf-8"))
    capturas = _carregar([Path(x) for x in a.capturas])

    destino = caso / "checagens" / "CAPTURAS.json"
    anterior = json.loads(destino.read_text(encoding="utf-8")) if destino.exists() else {}
    por_url: dict[str, dict] = {c["url"]: c for c in anterior.get("capturas", [])}

    ok = falhou = sem = 0
    for c in checagens["checagens"]:
        for f in c.get("fontes", []):
            cap = capturas.get(f["url"])
            if not cap:
                sem += 1
                print(f"  ·  {c['id']} sem captura: {f['url'][:90]}")
                continue
            reg = cap["registro"]
            entrada = por_url.setdefault(f["url"], {})
            entrada.update({k: reg[k] for k in ("url", "capturada_em", "status", "tipo", "caminho", "bytes", "sha256")})
            entrada.setdefault("trechos", {})
            achou = conferir(f["trecho"], cap["texto"], reg.get("tipo", ""))
            entrada["trechos"][c["id"]] = "encontrado" if achou else "não encontrado"
            if achou:
                ok += 1
            else:
                falhou += 1
                print(f"  ✗  {c['id']} trecho NÃO encontrado na captura de {f['url'][:80]}")

    saida = {"caso": a.slug,
             "nota": ("Recibo das capturas das fontes: sha256 do que foi lido e se cada trecho citado foi "
                      "encontrado na página capturada. O texto das páginas não entra no git."),
             "capturas": sorted(por_url.values(), key=lambda x: x["url"])}
    destino.write_text(json.dumps(saida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\n{ok} trechos encontrados · {falhou} não encontrados · {sem} fontes sem captura")
    print(f"recibo em {destino.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
