"""Compara a transcrição do caso com uma transcrição publicada por terceiro, e lista onde divergem.

    python ferramentas/comparar-transcricao.py <slug> <referencia.txt> [--inicio S] [--fim S]
                                               [--so-relevantes] [--saida arquivo.md]

A skill `preparar-caso` manda conferir a transcrição contra a publicada pelo veículo ou por
um terceiro (Poder360, por exemplo). Fazer isso lendo dois textos lado a lado é exatamente o
tipo de tarefa em que o olho cansa e pula. Este script alinha as duas sequências de palavras
e devolve cada janela em que elas discordam, com o tempo da nossa transcrição.

🔑 **Relevante** é a divergência que envolve número ou nome próprio, que é onde o
reconhecimento mais erra e onde o erro mais custa: é a palavra que vai para a citação do card.

⚠️ A transcrição de referência NÃO é verdade: jornal edita, tira hesitação, corrige
concordância. Divergência é **suspeita**, não correção. A correção só entra depois de conferida
no áudio (janela isolada, segunda passada), e entra por `corrigir-transcricao.py`, com rastro.
"""

from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
import unicodedata
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def _norm(p: str) -> str:
    t = unicodedata.normalize("NFKD", p.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", t)


def _palavras(texto: str) -> list[str]:
    return [p for p in re.findall(r"[\wÀ-ÿ$%.,/-]+", texto) if _norm(p)]


def _hms(s: float) -> str:
    n = int(round(s))
    return f"{n // 3600:02d}:{(n % 3600) // 60:02d}:{n % 60:02d}"


def _relevante(palavras: list[str]) -> bool:
    return any(re.search(r"\d", p) or (p[:1].isupper() and len(p) > 2) for p in palavras)


def comparar(slug: str, referencia: Path, inicio: float, fim: float) -> list[dict]:
    t = json.loads((RAIZ / "casos" / slug / "transcricao" / "transcricao.json").read_text(encoding="utf-8"))
    nossas: list[tuple[str, float]] = []
    for s in t["segmentos"]:
        if s["fim_s"] < inicio or s["inicio_s"] > fim:
            continue
        for p in _palavras(s["texto"]):
            nossas.append((p, s["inicio_s"]))
    ref = _palavras(referencia.read_text(encoding="utf-8"))

    a = [_norm(p) for p, _ in nossas]
    b = [_norm(p) for p in ref]
    sm = difflib.SequenceMatcher(a=a, b=b, autojunk=False)
    achados = []
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "equal":
            continue
        nos = [p for p, _ in nossas[i1:i2]]
        deles = ref[j1:j2]
        # Diferença grande demais é trecho que a referência não transcreveu (ou nós não), e
        # não erro de palavra: registra, mas não mistura com a suspeita pontual.
        tempo = nossas[min(i1, len(nossas) - 1)][1] if nossas else 0.0
        achados.append({
            "tempo_s": tempo,
            "nossa": " ".join(nos),
            "referencia": " ".join(deles),
            "relevante": _relevante(nos + deles),
            "tamanho": max(len(nos), len(deles)),
        })
    return achados


def main() -> int:
    p = argparse.ArgumentParser(description="compara a transcrição com uma referência publicada")
    p.add_argument("slug")
    p.add_argument("referencia")
    p.add_argument("--inicio", type=float, default=0.0)
    p.add_argument("--fim", type=float, default=10**9)
    p.add_argument("--so-relevantes", action="store_true")
    p.add_argument("--max-tamanho", type=int, default=12,
                   help="divergências maiores que isto são listadas à parte, como lacuna")
    p.add_argument("--saida", default=None)
    a = p.parse_args()

    achados = comparar(a.slug, Path(a.referencia), a.inicio, a.fim)
    pontuais = [x for x in achados if x["tamanho"] <= a.max_tamanho]
    lacunas = [x for x in achados if x["tamanho"] > a.max_tamanho]
    if a.so_relevantes:
        pontuais = [x for x in pontuais if x["relevante"]]

    linhas = [f"# Divergências · {a.slug} contra {Path(a.referencia).name}", "",
              f"{len(pontuais)} divergências pontuais"
              + (" relevantes (número ou nome próprio)" if a.so_relevantes else "")
              + f" · {len(lacunas)} lacunas longas", "",
              "| Tempo | Nossa transcrição | Referência | Relevante |", "|---|---|---|---|"]
    for x in pontuais:
        linhas.append(f"| {_hms(x['tempo_s'])} | {x['nossa'] or '(nada)'} | {x['referencia'] or '(nada)'} | "
                      f"{'sim' if x['relevante'] else ''} |")
    if lacunas:
        linhas += ["", "## Lacunas longas (trecho que só uma das duas tem)", ""]
        for x in lacunas:
            linhas.append(f"- {_hms(x['tempo_s'])} · {x['tamanho']} palavras · nossa: "
                          f"\"{x['nossa'][:120]}\" · referência: \"{x['referencia'][:120]}\"")
    texto = "\n".join(linhas) + "\n"
    if a.saida:
        Path(a.saida).write_text(texto, encoding="utf-8")
    print(texto)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
