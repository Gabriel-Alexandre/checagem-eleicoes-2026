"""Relatório do caso — o que o vídeo não cabe.

O card na tela tem duas linhas. A explicação, a divergência entre fontes, o trecho copiado de
cada fonte e a data de consulta vivem aqui. É este arquivo que sustenta a frase "a fonte está
no repositório", e é ele que um terceiro lê para refazer o caminho.

⛔ O relatório NÃO conclui nada sobre a pessoa. Ele lista alegações, vereditos e fontes, e traz
a contagem como dado do caso. Ver docs/METODOLOGIA.md §8.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from . import config as cfg
from .util import hms, ler_json, ok, passo

EMOJI = {
    "VERDADEIRO": "🟢",
    "IMPRECISO": "🟡",
    "INSUSTENTAVEL": "🟠",
    "FALSO": "🔴",
    "NAO_CHECAVEL": "⚪",
}


def gerar(slug: str, *, recorte: str | None = None) -> Path:
    caso = cfg.pasta_do_caso(slug)
    meta = ler_json(caso / "CASO.json")
    sufixo = f"-{recorte}" if recorte else ""
    alegacoes = ler_json(caso / "alegacoes" / f"alegacoes{sufixo}.json")["alegacoes"]
    checagens = {c["id"]: c for c in ler_json(caso / "checagens" / f"checagens{sufixo}.json")["checagens"]}

    passo(f"relatório — {slug}{sufixo}")
    L: list[str] = []
    add = L.append

    add(f"# Checagem — {meta['titulo']}")
    add("")
    add(f"**Peça:** {meta['veiculo']}"
        + (f" · {meta['programa']}" if meta.get("programa") else "")
        + f" · {meta['formato']} · {meta['data_do_evento']}  ")
    add(f"**Duração:** {hms(float(meta['duracao_s']))}  ")
    if recorte:
        indice = ler_json(caso / "recortes" / "RECORTES.json")
        reg = next(r for r in indice["recortes"] if r["id"] == recorte)
        add(f"**Trecho checado:** `{recorte}` — {hms(reg['origem_inicio_s'])} a "
            f"{hms(reg['origem_inicio_s'] + reg['duracao_s'])} da peça  ")
        add(f"**Por que este trecho:** {reg.get('motivo') or 'não registrado'}  ")
    add(f"**Relatório gerado em:** {date.today().isoformat()}  ")
    add("**Metodologia:** [`docs/METODOLOGIA.md`](../../docs/METODOLOGIA.md)  ")
    add(f"**Assinatura da mídia (sha256):** `{meta['midia']['sha256']}`")
    add("")
    add("> ⚠️ Este relatório afere **enunciados**, não pessoas. Ele não mede intenção, não avalia "
        "governo e não recomenda voto. A contagem abaixo é um dado deste trecho, não um veredito "
        "sobre quem falou. Ver [`METODOLOGIA §8`](../../docs/METODOLOGIA.md).")
    add("")

    # ── quem falou ──
    add("## Quem está na peça")
    add("")
    add("| Pessoa | Papel | |")
    add("|---|---|---|")
    for f in meta["falantes"]:
        add(f"| {f['nome']} | {f['papel']} | {f.get('cargo_ou_partido') or ''} |")
    add("")

    # ── placar ──
    contagem: dict[str, int] = {}
    por_papel: dict[str, dict[str, int]] = {}
    for a in alegacoes:
        c = checagens[a["id"]]
        contagem[c["veredito"]] = contagem.get(c["veredito"], 0) + 1
        por_papel.setdefault(a["papel"], {})
        por_papel[a["papel"]][c["veredito"]] = por_papel[a["papel"]].get(c["veredito"], 0) + 1

    add("## Contagem")
    add("")
    add(f"**{len(alegacoes)} alegações** extraídas e checadas.")
    add("")
    ordem = ["VERDADEIRO", "IMPRECISO", "INSUSTENTAVEL", "FALSO", "NAO_CHECAVEL"]
    add("| Veredito | Total | " + " | ".join(sorted(por_papel)) + " |")
    add("|---|---:|" + "---:|" * len(por_papel))
    for v in ordem:
        if v not in contagem:
            continue
        linha = f"| {EMOJI[v]} {cfg.VEREDITOS[v].rotulo} | {contagem[v]} |"
        for papel in sorted(por_papel):
            linha += f" {por_papel[papel].get(v, 0)} |"
        add(linha)
    add("")

    # ── as alegações ──
    add("## Alegação por alegação")
    add("")
    for a in alegacoes:
        c = checagens[a["id"]]
        v = cfg.VEREDITOS[c["veredito"]]
        add(f"### {a['id']} · {EMOJI[c['veredito']]} {v.rotulo} — {hms(a['inicio_s'])}")
        add("")
        add(f"**{a['falante']}** ({a['papel']}) · assunto: `{a['assunto']}` · tipo: `{a['tipo']}`")
        add("")
        add(f"> \"{a['frase']}\"")
        add("")
        add(f"**Afirmação isolada:** {a['afirmacao']}")
        add("")
        if a.get("contexto"):
            add(f"**Contexto:** {a['contexto']}")
            add("")
        add(f"**Resumo (o que aparece no vídeo):** {c['resumo']}")
        add("")
        if c.get("numero_dito") or c.get("numero_apurado"):
            add("| | |")
            add("|---|---|")
            add(f"| Dito | {c.get('numero_dito') or '—'} |")
            add(f"| Apurado | {c.get('numero_apurado') or '—'} |")
            if c.get("data_de_referencia"):
                add(f"| Data de referência | {c['data_de_referencia']} |")
            add("")
        add(f"**Análise:** {c['explicacao']}")
        add("")
        if c.get("ressalva"):
            add(f"**Ressalva:** {c['ressalva']}")
            add("")
        if c.get("divergencia_entre_fontes"):
            add(f"**⚠️ Divergência entre fontes:** {c['divergencia_entre_fontes']}")
            add("")
        add(f"**Confiança:** {c['confianca']}")
        add("")
        if c.get("revisao_humana"):
            r = c["revisao_humana"]
            add(f"**Revisão humana:** {r['revisor']} em {r['data']} — {r['decisao']}"
                + (f". {r.get('nota')}" if r.get("nota") else ""))
            add("")
        if c.get("derivacoes"):
            add("**Números derivados por cálculo:**")
            add("")
            add("| Valor | De | Como |")
            add("|---|---|---|")
            for d in c["derivacoes"]:
                add(f"| {d['valor']} | `{d['de']}` | {d['como']} |")
            add("")
        if c.get("fontes"):
            add("**Fontes:**")
            add("")
            for i, f in enumerate(c["fontes"], 1):
                add(f"{i}. `{f['nivel']}` **{f['instituicao']}** — [{f['titulo']}]({f['url']}) "
                    f"· consultada em {f['consultada_em']}")
                add(f"   > {f['trecho']}")
                add("")
                add(f"   *O que prova:* {f['prova']}")
                add("")
        else:
            add("*Sem fontes: alegação classificada como não checável.*")
            add("")
        add("---")
        add("")

    exclusoes = ler_json(caso / "alegacoes" / f"alegacoes{sufixo}.json").get("exclusoes", [])
    if exclusoes:
        add("## Frases que ficaram de fora, e por quê")
        add("")
        add("Estas frases passaram pelo filtro de \"isto afirma um fato\" e ainda assim não "
            "viraram alegação. Elas estão aqui para que a varredura seja auditável: sem este "
            "registro, uma frase deixada de fora seria indistinguível de uma frase não vista.")
        add("")
        for e in exclusoes:
            add(f"### {hms(e['inicio_s'])} · {e.get('falante', '—')}")
            add("")
            add(f"> \"{e['frase']}\"")
            add("")
            add(f"**Por que ficou de fora:** {e['motivo']}")
            add("")
        add("---")
        add("")

    add("## Como refazer esta checagem")
    add("")
    add("```bash")
    add(f"python -m checagem midia {slug} registrar")
    add(f"python -m checagem midia {slug} audio")
    add(f"python -m checagem transcrever {slug}")
    add(f"python -m checagem falantes {slug}")
    add(f"python -m checagem validar {slug}" + (f" --recorte {recorte}" if recorte else ""))
    add("```")
    add("")
    add("Os passos de extração e de checagem são feitos por IA seguindo as skills em "
        "[`skills/`](../../skills/). O que está neste relatório é a saída delas, com as fontes "
        "que qualquer pessoa pode abrir e conferir.")
    add("")

    destino = caso / f"RELATORIO{sufixo.upper().replace('-', '_')}.md"
    destino.write_text("\n".join(L), encoding="utf-8", newline="\n")
    ok(f"{destino.relative_to(cfg.RAIZ)} · {len(alegacoes)} alegações")
    return destino


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem relatorio")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    args = p.parse_args(argv)
    gerar(args.slug, recorte=args.recorte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
