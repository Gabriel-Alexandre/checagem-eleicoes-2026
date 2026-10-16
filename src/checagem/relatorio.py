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
from .util import data_legivel, hms, ler_json, ok, passo

EMOJI = {
    "VERDADEIRO": "🟢",
    "IMPRECISO": "🟡",
    "INSUSTENTAVEL": "🟠",
    "FALSO": "🔴",
    "NAO_CHECAVEL": "⚪",
}


def _registro_do_recorte(caso: Path, recorte: str | None) -> dict | None:
    """A entrada do recorte em RECORTES.json, ou None (peça inteira, sem vídeo)."""
    if not recorte or not (caso / "recortes" / "RECORTES.json").exists():
        return None
    return next((r for r in ler_json(caso / "recortes" / "RECORTES.json")["recortes"] if r["id"] == recorte), None)


def _secao_da_peca_inteira(add, caso: Path, slug: str, recorte: str) -> None:
    """Métricas por falante e os cortes que viraram vídeo, quando a checagem é da peça inteira."""
    m_path = caso / "metricas" / f"metricas-{recorte}.json"
    if m_path.exists():
        m = ler_json(m_path)
        add("## Por falante")
        add("")
        add(f"Detalhe completo, com assunto e bloco: [`metricas/METRICAS_{recorte}.md`](metricas/METRICAS_{recorte}.md). "
            "Ordem da primeira fala, nunca por resultado.")
        add("")
        add("| Falante | Papel | Fala | Alegações | Checáveis | 🟢 | 🟡 | 🟠 | 🔴 | ⚪ |")
        add("|---|---|---:|---:|---:|---:|---:|---:|---:|---:|")
        for f in m["por_falante"]:
            c = f["por_veredito"]
            add(f"| {f['nome']} | {f['papel']} | {f['fala_hms']} | {f['alegacoes']} | {f['checaveis']} | "
                f"{c['VERDADEIRO']} | {c['IMPRECISO']} | {c['INSUSTENTAVEL']} | {c['FALSO']} | {c['NAO_CHECAVEL']} |")
        add("")
        for a in m.get("avisos", []):
            add(f"- ⚠️ {a}")
        if m.get("avisos"):
            add("")
    else:
        add(f"> ⚠️ Métricas ainda não geradas: `python -m checagem metricas {slug} --recorte {recorte}`.")
        add("")
    cortes = sorted((caso / "alegacoes").glob("alegacoes-corte-*.json"))
    if cortes:
        indice = {r["id"]: r for r in ler_json(caso / "recortes" / "RECORTES.json")["recortes"]}             if (caso / "recortes" / "RECORTES.json").exists() else {}
        add("## Os cortes que viraram vídeo")
        add("")
        add("Cada corte herda as checagens desta peça, com os mesmos ids. O critério de escolha foi "
            "registrado antes dos vereditos ([`recortes/SELECAO_DE_CORTES.md`](recortes/SELECAO_DE_CORTES.md)).")
        add("")
        add("| Corte | Janela | Alegações | Por que este trecho |")
        add("|---|---|---|---|")
        for arq in cortes:
            d = ler_json(arq)
            rid = arq.stem[len("alegacoes-"):]
            cob = d["cobertura"]
            motivo = (indice.get(rid) or {}).get("motivo") or "não registrado"
            if d.get("fora_do_limite_de_tamanho"):
                motivo += " · ⚠️ fora do limite de tamanho: " + d["fora_do_limite_de_tamanho"]["motivo"]
            add(f"| `{rid}` | {hms(cob['inicio_s'])} a {hms(cob['fim_s'])} ({cob['fim_s'] - cob['inicio_s']:.0f} s) | "
                f"{', '.join(x['id'] for x in d['alegacoes'])} | {motivo} |")
        add("")


def gerar(slug: str, *, recorte: str | None = None) -> Path:
    caso = cfg.pasta_do_caso(slug)
    meta = ler_json(caso / "CASO.json")
    sufixo = f"-{recorte}" if recorte else ""
    alegacoes = ler_json(caso / "alegacoes" / f"alegacoes{sufixo}.json")["alegacoes"]
    checagens = {c["id"]: c for c in ler_json(caso / "checagens" / f"checagens{sufixo}.json")["checagens"]}

    passo(f"relatório · {slug}{sufixo}")
    caminho_capturas = caso / "checagens" / "CAPTURAS.json"
    capturas = ({c["url"]: c for c in ler_json(caminho_capturas).get("capturas", [])}
                if caminho_capturas.exists() else {})
    L: list[str] = []
    add = L.append

    add(f"# Checagem: {meta['titulo']}")
    add("")
    add(f"**Peça:** {meta['veiculo']}"
        + (f" · {meta['programa']}" if meta.get("programa") else "")
        + f" · {meta['formato']} · {data_legivel(meta['data_do_evento'])}  ")
    add(f"**Duração:** {hms(float(meta['duracao_s']))}  ")
    reg = _registro_do_recorte(caso, recorte)
    doc_alegacoes = ler_json(caso / "alegacoes" / f"alegacoes{sufixo}.json")
    if recorte and reg:
        add(f"**Trecho checado:** `{recorte}`, de {hms(reg['origem_inicio_s'])} a "
            f"{hms(reg['origem_inicio_s'] + reg['duracao_s'])} da peça  ")
        add(f"**Por que este trecho:** {reg.get('motivo') or 'não registrado'}  ")
        if doc_alegacoes.get("fora_do_limite_de_tamanho"):
            fl = doc_alegacoes["fora_do_limite_de_tamanho"]
            add(f"**⚠️ Fora do limite de tamanho de corte:** {'; '.join(fl['problemas'])}. Motivo: {fl['motivo']}  ")
    elif recorte:
        # 🆕 15/out/2026: a peça checada INTEIRA (debate-completo, sabatina-completa) não tem vídeo
        # renderizado nem entrada em RECORTES.json. O que prova a cobertura é a `cobertura` da extração.
        cob = doc_alegacoes.get("cobertura") or {"inicio_s": 0.0, "fim_s": float(meta["duracao_s"])}
        add(f"**Trecho checado:** a peça inteira (`{recorte}`), de {hms(cob['inicio_s'])} a "
            f"{hms(cob['fim_s'])}, sem escolha de trecho  ")
    if meta.get("inicio_da_entrevista_s"):
        zero = float(meta["inicio_da_entrevista_s"])
        add(f"**Os horários:** neste relatório, os do arquivo de gravação; a entrevista começa em "
            f"{hms(zero)} dele. Nos cards do vídeo, o minuto conta do começo da entrevista "
            f"(horário do arquivo menos {hms(zero)})  ")
    add(f"**Relatório gerado em:** {date.today().isoformat()}  ")
    add("**Metodologia:** [`docs/METODOLOGIA.md`](../../docs/METODOLOGIA.md)  ")
    add(f"**Assinatura da mídia (sha256):** `{meta['midia']['sha256']}`")
    add("")
    proc = meta.get("procedencia", {})
    if proc.get("integralidade") != "integral":
        # etica-e-risco §4: peça que já é recorte de terceiro avisa EM CIMA, antes de tudo.
        add("> 🔴 **Atenção: a peça checada não é a íntegra oficial** "
            f"(integralidade: `{proc.get('integralidade', 'desconhecido')}`). Corte muda contexto, "
            "e o que ficou fora do arquivo não foi visto por esta checagem. Detalhes em "
            "[Procedência](#procedência-da-peça).")
        add("")
    add("> ⚠️ Este relatório afere **enunciados**, não pessoas. Ele não mede intenção, não avalia "
        "governo e não recomenda voto. A contagem abaixo é um dado deste trecho, não um veredito "
        "sobre quem falou. Ver [`METODOLOGIA §8`](../../docs/METODOLOGIA.md).")
    add("")

    # ── procedência ──
    add("## Procedência da peça")
    add("")
    add(f"- **Como foi obtida:** {proc.get('como_foi_obtido') or 'não registrado'}")
    if proc.get("url_oficial"):
        add(f"- **Endereço:** <{proc['url_oficial']}>")
    add(f"- **Integralidade:** `{proc.get('integralidade', 'desconhecido')}`")
    if proc.get("observacoes"):
        add(f"- **Observações:** {proc['observacoes']}")
    add(f"- **Arquivo checado:** `{meta['midia']['arquivo']}` · {meta['midia']['largura']}x"
        f"{meta['midia']['altura']} · sha256 `{meta['midia']['sha256']}`")
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
    # ── o que a contagem é, e o que ela não é ──
    revisadas = sum(1 for a in alegacoes
                    if checagens[a["id"]].get("revisao_ia") or checagens[a["id"]].get("revisao_humana"))
    add("### Como ler esta contagem")
    add("")
    for papel in sorted(por_papel):
        n = sum(por_papel[papel].values())
        add(f"- **{papel}:** {n} de {len(alegacoes)} alegações.")
    add("- Os números acima são **deste trecho** e têm o denominador à vista. ⛔ Eles não são "
        "ranking entre pessoas nem entre candidatos, e não dizem nada sobre intenção.")
    add("- ⚠️ **Nem toda afirmação é igualmente checável.** Economia tem série pública; segurança "
        "tem defasagem; promessa não tem fonte. Um lado pode acumular `SEM COMPROVAÇÃO` só porque "
        "falou de assunto com fonte pior ([`etica-e-risco` §3](../../.cursor/rules/etica-e-risco.mdc)).")
    if revisadas < len(alegacoes):
        add(f"- 🔴 **Revisão registrada em {revisadas} de {len(alegacoes)} checagens.** O caso só "
            "está pronto quando todas passaram pela revisão adversarial "
            "([`skills/revisar-checagem.md`](../../skills/revisar-checagem.md)).")
    else:
        add(f"- **Revisão adversarial registrada nas {len(alegacoes)} checagens**, feita por IA em "
            "passada separada da checagem ([`skills/revisar-checagem.md`](../../skills/revisar-checagem.md)); "
            "o resultado de cada uma está na alegação.")
    add("")

    if recorte and not reg:
        _secao_da_peca_inteira(add, caso, slug, recorte)

    add("## Alegação por alegação")
    add("")
    for a in alegacoes:
        c = checagens[a["id"]]
        v = cfg.VEREDITOS[c["veredito"]]
        add(f"### {a['id']} · {EMOJI[c['veredito']]} {v.rotulo} · {hms(a['inicio_s'])}")
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
            add(f"| Dito | {c.get('numero_dito') or 'não se aplica'} |")
            add(f"| Apurado | {c.get('numero_apurado') or 'não se aplica'} |")
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
        if c.get("revisao_ia"):
            r = c["revisao_ia"]
            add(f"**Revisão por IA:** {r['revisor']} em {r['data']}: {r['decisao']}. {r['nota']}")
            add("")
        if c.get("revisao_humana"):
            r = c["revisao_humana"]
            add(f"**Revisão humana:** {r['revisor']} em {r['data']}: {r['decisao']}"
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
                cap = capturas.get(f["url"])
                assinatura = f" · captura sha256 `{cap['sha256'][:16]}…`" if cap and cap.get("sha256") else ""
                add(f"{i}. `{f['nivel']}` **{f['instituicao']}**: [{f['titulo']}]({f['url']}) "
                    f"· consultada em {f['consultada_em']}{assinatura}")
                add(f"   > {f['trecho']}")
                add("")
                add(f"   *O que prova:* {f['prova']}")
                add("")
        else:
            add("*Sem fontes: alegação classificada como não checável.*")
            add("")
        add("---")
        add("")

    exclusoes = doc_alegacoes.get("exclusoes", [])
    if exclusoes:
        add("## Frases que ficaram de fora, e por quê")
        add("")
        add("Estas frases passaram pelo filtro de \"isto afirma um fato\" e ainda assim não "
            "viraram alegação. Elas estão aqui para que a varredura seja auditável: sem este "
            "registro, uma frase deixada de fora seria indistinguível de uma frase não vista.")
        add("")
        for e in exclusoes:
            add(f"### {hms(e['inicio_s'])} · {e.get('falante', 'falante não atribuído')}")
            add("")
            add(f"> \"{e['frase']}\"")
            add("")
            add(f"**Por que ficou de fora:** {e['motivo']}")
            add("")
        add("---")
        add("")

    add("## Correções e contestação")
    add("")
    add("- Mudanças depois da publicação: [`CORRECOES.md`](CORRECOES.md). ⛔ Nada é apagado em silêncio.")
    if (caso / "transcricao" / "CORRECOES_DE_TRANSCRICAO.md").exists():
        add("- Correções de reconhecimento de fala: "
            "[`transcricao/CORRECOES_DE_TRANSCRICAO.md`](transcricao/CORRECOES_DE_TRANSCRICAO.md).")
    if (caso / "transcricao" / "NOTA_DE_ATRIBUICAO.md").exists():
        add("- Quem falou o quê, decisão por decisão: "
            "[`transcricao/NOTA_DE_ATRIBUICAO.md`](transcricao/NOTA_DE_ATRIBUICAO.md).")
    add("- Discorda de um veredito? Abra uma **issue** com a fonte que sustenta a contestação. "
        "Ver [`CONTRIBUTING.md`](../../CONTRIBUTING.md).")
    add("")

    rec = f" --recorte {recorte}" if recorte else ""
    add("## Como refazer esta checagem")
    add("")
    add("```bash")
    add(f"# ponha o vídeo em casos/{slug}/fonte/ e confira que o sha256 bate com o de CASO.json")
    add(f"python -m checagem midia {slug} registrar")
    add(f"python -m checagem midia {slug} audio")
    add(f"python -m checagem transcrever {slug}")
    add(f"python ferramentas/corrigir-transcricao.py {slug}")
    add(f"python -m checagem falantes {slug}")
    add(f"python -m checagem validar {slug}{rec}")
    if recorte and reg:
        add(f"python -m checagem midia {slug} recortar {recorte} --inicio {reg['origem_inicio_s']} "
            f"--duracao {reg['duracao_s']}")
    if not recorte or reg:
        add(f"python -m checagem overlay {slug}{rec}")
        add(f"python -m checagem renderizar {slug}{rec}")
    else:
        add(f"python -m checagem metricas {slug}{rec}")
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
