"""MÉTRICAS — o que a checagem de uma peça inteira diz, em números, com o denominador sempre junto.

Existe por causa do debate (outubro/2026): com quatro candidatos e centenas de alegações, o autor
quer falar os resultados **gerais** e **por candidato**. Este módulo só **calcula**. Ele lê o que o
validador já aprovou (alegações, checagens, transcrição com falante) e escreve:

    casos/<slug>/metricas/metricas-<recorte>.json     · para a máquina (e para o roteiro)
    casos/<slug>/metricas/METRICAS_<recorte>.md       · para a pessoa, com as ressalvas escritas

🔴 O que este módulo NÃO faz, de propósito (docs/METODOLOGIA.md §8 e .cursor/rules/etica-e-risco.mdc §2):

  · não gera nota, índice, placar nem ordem de "quem foi pior";
  · não soma `FALSO` com `IMPRECISO` numa palavra só;
  · não ordena candidato por resultado: a ordem é a da **primeira fala**;
  · não diz de quem é a culpa de uma assimetria: ele **mostra** a assimetria (tempo de fala, quantas
    alegações eram checáveis, de que assunto), que é o que etica-e-risco §3 manda escrever.

A contagem é **dado do caso**. O que ela quer dizer é decisão de quem publica.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from collections import Counter
from datetime import date
from typing import Any

from . import config as cfg
from .util import ErroDeExecucao, escrever_json, hms, ler_json, ok, passo

ORDEM_DOS_VEREDITOS = ("VERDADEIRO", "IMPRECISO", "INSUSTENTAVEL", "FALSO", "NAO_CHECAVEL")

# O texto que vai em TODO relatório de métricas. Não é enfeite: é a §3 do etica-e-risco.
RESSALVAS_FIXAS = (
    "A contagem é dado **deste** evento, com o denominador à vista. Ela não é nota nem placar, e "
    "não serve para dizer quem mente mais ou quem se saiu melhor.",
    "Quem fala mais tempo, ou é perguntado sobre assunto com fonte pública melhor (economia tem "
    "série oficial; promessa e opinião não têm), tem mais alegações checáveis. Um percentual "
    "menor de `VERDADEIRO` pode vir só disso: leia o tempo de fala e o assunto antes de comparar.",
    "`INSUSTENTAVEL` (SEM COMPROVAÇÃO) quer dizer que **a busca não achou fonte que sustente**, e "
    "não que alguém provou o contrário. É diferente de `FALSO`.",
    "Alegação **não checável** (opinião, promessa, previsão) não entra nos percentuais, mas entra "
    "na contagem de alegações, porque o autor decide o que é fato pela metodologia, não pelo resultado.",
)


def _slug_de(nome: str) -> str:
    t = unicodedata.normalize("NFKD", nome.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]+", "-", t).strip("-")


def _por_veredito(vereditos: list[str]) -> dict[str, int]:
    c = Counter(vereditos)
    return {v: c.get(v, 0) for v in ORDEM_DOS_VEREDITOS}


def _percentuais(contagem: dict[str, int]) -> dict[str, float | None]:
    """Percentual de cada veredito sobre as alegações CHECÁVEIS (não checável fica de fora)."""
    base = sum(n for v, n in contagem.items() if v != "NAO_CHECAVEL")
    if not base:
        return {v: None for v in ORDEM_DOS_VEREDITOS if v != "NAO_CHECAVEL"}
    return {v: round(100 * contagem[v] / base, 1) for v in ORDEM_DOS_VEREDITOS if v != "NAO_CHECAVEL"}


def calcular(
    meta: dict[str, Any],
    transcricao: dict[str, Any],
    alegacoes_doc: dict[str, Any],
    checagens_doc: dict[str, Any],
    *,
    recorte: str | None = None,
) -> dict[str, Any]:
    """Função pura: recebe os quatro documentos e devolve o dicionário de métricas."""
    alegacoes = alegacoes_doc["alegacoes"]
    checagem_de = {c["id"]: c for c in checagens_doc["checagens"]}
    sem_checagem = [a["id"] for a in alegacoes if a["id"] not in checagem_de]
    if sem_checagem:
        raise ErroDeExecucao(
            f"{len(sem_checagem)} alegações sem checagem ({', '.join(sem_checagem[:6])}…): "
            "métrica de peça incompleta é o defeito de escolher o que mostrar. Feche as checagens antes."
        )

    papel_de = {f["nome"]: f["papel"] for f in meta["falantes"]}
    partido_de = {f["nome"]: f.get("cargo_ou_partido") for f in meta["falantes"]}

    # Tempo de fala por falante e ordem da primeira fala.
    fala_s: dict[str, float] = {}
    primeira: dict[str, float] = {}
    for s in transcricao["segmentos"]:
        quem = s.get("falante")
        if not quem:
            continue
        fala_s[quem] = fala_s.get(quem, 0.0) + max(0.0, s["fim_s"] - s["inicio_s"])
        primeira.setdefault(quem, s["inicio_s"])
    cobertura = alegacoes_doc.get("cobertura") or {"inicio_s": 0.0, "fim_s": float(meta.get("duracao_s", 0))}
    janela_s = max(0.0, cobertura["fim_s"] - cobertura["inicio_s"])

    # Só conta o tempo de fala dentro da janela coberta pela extração.
    if alegacoes_doc.get("cobertura"):
        fala_s = {}
        for s in transcricao["segmentos"]:
            quem = s.get("falante")
            if not quem:
                continue
            ini, fim = max(s["inicio_s"], cobertura["inicio_s"]), min(s["fim_s"], cobertura["fim_s"])
            if fim > ini:
                fala_s[quem] = fala_s.get(quem, 0.0) + (fim - ini)

    def bloco(lista: list[dict]) -> dict[str, Any]:
        vs = [checagem_de[a["id"]]["veredito"] for a in lista]
        cont = _por_veredito(vs)
        checaveis = sum(n for v, n in cont.items() if v != "NAO_CHECAVEL")
        return {
            "alegacoes": len(lista),
            "checaveis": checaveis,
            "nao_checaveis": cont["NAO_CHECAVEL"],
            "por_veredito": cont,
            "percentual_dos_checaveis": _percentuais(cont),
        }

    geral = bloco(alegacoes)
    geral["por_papel"] = {
        papel: bloco([a for a in alegacoes if a["papel"] == papel])
        for papel in sorted({a["papel"] for a in alegacoes})
    }
    geral["janela_s"] = round(janela_s, 1)

    # Por falante, na ordem da primeira fala. ⛔ Nunca ordenar por resultado.
    nomes = sorted(
        {a["falante"] for a in alegacoes} | set(fala_s),
        key=lambda n: (primeira.get(n, 1e12), n),
    )
    por_falante = []
    for nome in nomes:
        suas = [a for a in alegacoes if a["falante"] == nome]
        b = bloco(suas)
        minutos = fala_s.get(nome, 0.0) / 60
        b.update({
            "nome": nome,
            "chave": _slug_de(nome),
            "papel": papel_de.get(nome),
            "cargo_ou_partido": partido_de.get(nome),
            "fala_s": round(fala_s.get(nome, 0.0), 1),
            "fala_hms": hms(fala_s.get(nome, 0.0)),
            "alegacoes_por_minuto_de_fala": round(len(suas) / minutos, 2) if minutos >= 0.5 else None,
            "assuntos": dict(Counter(a["assunto"] for a in suas).most_common()),
            "tipos": dict(Counter(a["tipo"] for a in suas).most_common()),
        })
        por_falante.append(b)

    por_assunto = []
    for assunto, _ in Counter(a["assunto"] for a in alegacoes).most_common():
        lista = [a for a in alegacoes if a["assunto"] == assunto]
        b = bloco(lista)
        b["assunto"] = assunto
        b["por_falante"] = dict(Counter(a["falante"] for a in lista).most_common())
        por_assunto.append(b)

    revisoes = Counter(
        (c.get("revisao_ia") or {}).get("decisao", "sem_revisao") for c in checagem_de.values()
    )
    confianca = Counter(c["confianca"] for c in checagem_de.values())
    fontes = [f for c in checagem_de.values() for f in c.get("fontes", [])]

    avisos: list[str] = []
    candidatos = [f for f in por_falante if f["papel"] == "entrevistado"]
    if len(candidatos) >= 2:
        cs = [f["checaveis"] for f in candidatos]
        if min(cs) and max(cs) / min(cs) >= 1.5:
            avisos.append(
                f"os candidatos têm quantidades de alegações checáveis bem diferentes "
                f"({min(cs)} a {max(cs)}): compare percentuais, nunca contagens brutas."
            )
        ts = [f["fala_s"] for f in candidatos if f["fala_s"]]
        if ts and max(ts) / min(ts) >= 1.3:
            avisos.append(
                f"o tempo de fala dos candidatos difere em {round(100 * (max(ts) / min(ts) - 1))}% "
                f"(de {hms(min(ts))} a {hms(max(ts))}): leia `alegacoes_por_minuto_de_fala`."
            )
        sem = [f["nome"] for f in candidatos if f["checaveis"] == 0]
        if sem:
            avisos.append(f"sem nenhuma alegação checável: {', '.join(sem)}. Isso fica visível, não escondido.")
    if revisoes.get("sem_revisao"):
        avisos.append(f"{revisoes['sem_revisao']} checagens ainda sem `revisao_ia`: o resultado não está fechado.")

    return {
        "caso": meta["slug"],
        "recorte": recorte,
        "gerado_em": date.today().isoformat(),
        "formato": meta["formato"],
        "cobertura": cobertura,
        "geral": geral,
        "por_falante": por_falante,
        "por_assunto": por_assunto,
        "revisao_ia": dict(revisoes),
        "confianca": dict(confianca),
        "fontes": {
            "citacoes": len(fontes),
            "urls_distintas": len({f["url"] for f in fontes}),
            "instituicoes": len({f["instituicao"] for f in fontes}),
        },
        "avisos": avisos,
        "ressalvas": list(RESSALVAS_FIXAS),
    }


# ─────────────────────────────────────────────────────────────────────
# Relatório em texto
# ─────────────────────────────────────────────────────────────────────

ROTULO = {v: cfg.VEREDITOS[v].rotulo for v in ORDEM_DOS_VEREDITOS}


def _linha_de_veredito(b: dict[str, Any]) -> str:
    c = b["por_veredito"]
    return " · ".join(f"{c[v]} {ROTULO[v].lower()}" for v in ORDEM_DOS_VEREDITOS)


def para_markdown(m: dict[str, Any]) -> str:
    g = m["geral"]
    out = [
        f"# Métricas · {m['caso']}" + (f" · {m['recorte']}" if m["recorte"] else ""),
        "",
        f"Gerado em {m['gerado_em']} por `python -m checagem metricas`. ⚠️ **Leia as ressalvas no fim antes de citar qualquer número.**",
        "",
        "## Geral",
        "",
        f"**{g['alegacoes']} alegações** em {hms(g['janela_s'])} de peça: {g['checaveis']} checáveis e {g['nao_checaveis']} não checáveis.",
        "",
        "| Veredito | Alegações | % dos checáveis |",
        "|---|---:|---:|",
    ]
    for v in ORDEM_DOS_VEREDITOS:
        p = g["percentual_dos_checaveis"].get(v)
        out.append(f"| {ROTULO[v]} | {g['por_veredito'][v]} | {'·' if p is None else f'{p}%'} |")
    out += ["", "**Por papel:**", ""]
    for papel, b in g["por_papel"].items():
        out.append(f"- {papel}: {b['alegacoes']} alegações ({_linha_de_veredito(b)})")

    out += ["", "## Por falante (na ordem da primeira fala, nunca por resultado)", "",
            "| Falante | Fala | Alegações | Checáveis | Verdadeiro | Impreciso | Sem comprovação | Falso | Não checável | Alegações por min de fala |",
            "|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|"]
    for f in m["por_falante"]:
        c = f["por_veredito"]
        apm = f["alegacoes_por_minuto_de_fala"]
        out.append(
            f"| {f['nome']} | {f['fala_hms']} | {f['alegacoes']} | {f['checaveis']} | {c['VERDADEIRO']} | "
            f"{c['IMPRECISO']} | {c['INSUSTENTAVEL']} | {c['FALSO']} | {c['NAO_CHECAVEL']} | {'·' if apm is None else apm} |"
        )
    out += ["", "### Percentual dos checáveis, por falante", "",
            "| Falante | Checáveis | % verdadeiro | % impreciso | % sem comprovação | % falso |", "|---|---:|---:|---:|---:|---:|"]
    for f in m["por_falante"]:
        p = f["percentual_dos_checaveis"]

        def fmt(v: float | None) -> str:
            return "·" if v is None else f"{v}%"

        out.append(
            f"| {f['nome']} | {f['checaveis']} | {fmt(p['VERDADEIRO'])} | {fmt(p['IMPRECISO'])} | "
            f"{fmt(p['INSUSTENTAVEL'])} | {fmt(p['FALSO'])} |"
        )

    out += ["", "## Por assunto", "", "| Assunto | Alegações | Checáveis | Verdadeiro | Impreciso | Sem comprovação | Falso |",
            "|---|---:|---:|---:|---:|---:|---:|"]
    for a in m["por_assunto"]:
        c = a["por_veredito"]
        out.append(f"| {a['assunto']} | {a['alegacoes']} | {a['checaveis']} | {c['VERDADEIRO']} | {c['IMPRECISO']} | {c['INSUSTENTAVEL']} | {c['FALSO']} |")

    out += ["", "## Como o trabalho foi conferido", "",
            f"- Revisão adversarial por IA: {', '.join(f'{k} {v}' for k, v in m['revisao_ia'].items())}",
            f"- Confiança: {', '.join(f'{k} {v}' for k, v in m['confianca'].items())}",
            f"- Fontes: {m['fontes']['citacoes']} citações, {m['fontes']['urls_distintas']} URLs, {m['fontes']['instituicoes']} instituições"]
    if m["avisos"]:
        out += ["", "## ⚠️ Avisos desta rodada", ""] + [f"- {a}" for a in m["avisos"]]
    out += ["", "## Ressalvas (valem sempre)", ""] + [f"{i}. {r}" for i, r in enumerate(m["ressalvas"], 1)]
    return "\n".join(out) + "\n"


# ─────────────────────────────────────────────────────────────────────


def gerar(slug: str, *, recorte: str | None = None) -> dict[str, Any]:
    caso = cfg.pasta_do_caso(slug)
    meta = ler_json(caso / "CASO.json")
    nome_t = f"transcricao-{recorte}.json" if recorte else "transcricao.json"
    caminho_t = caso / "transcricao" / nome_t
    if not caminho_t.exists():
        caminho_t = caso / "transcricao" / "transcricao.json"
    transcricao = ler_json(caminho_t)
    alegacoes = ler_json(caso / "alegacoes" / (f"alegacoes-{recorte}.json" if recorte else "alegacoes.json"))
    checagens = ler_json(caso / "checagens" / (f"checagens-{recorte}.json" if recorte else "checagens.json"))

    passo(f"MÉTRICAS · {slug}{' · ' + recorte if recorte else ''}")
    m = calcular(meta, transcricao, alegacoes, checagens, recorte=recorte)

    pasta = caso / "metricas"
    pasta.mkdir(exist_ok=True)
    rotulo = recorte or "completo"
    escrever_json(pasta / f"metricas-{rotulo}.json", m)
    (pasta / f"METRICAS_{rotulo}.md").write_text(para_markdown(m), encoding="utf-8")
    ok(f"{m['geral']['alegacoes']} alegações · {len(m['por_falante'])} falantes · "
       f"casos/{slug}/metricas/METRICAS_{rotulo}.md")
    for a in m["avisos"]:
        print(f"  \033[33m⚠\033[0m {a}")
    return m


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem metricas", description="métricas gerais e por falante")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    args = p.parse_args(argv)
    gerar(args.slug, recorte=args.recorte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
