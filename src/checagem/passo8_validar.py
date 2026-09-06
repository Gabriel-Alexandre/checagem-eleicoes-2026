"""PASSO 8 — validar.

Esta é a porta. Ela sai com código 1 se achar erro, e é por isso que ela existe:
documento de metodologia que ninguém executa vira enfeite em três semanas.

O que ela confere, e por quê:

  · **A citação existe mesmo na transcrição.** É a trava mais importante do repositório.
    Um modelo de linguagem parafraseia sem perceber, e uma aspa parafraseada num vídeo de
    checagem é exatamente o defeito que o projeto diz combater.
  · **Todo número do veredito tem lastro num trecho de fonte.** METODOLOGIA §3.1 regra 6.
  · **Duas fontes independentes**, e fonte forte quando a alegação é numérica.
  · **Nenhuma alegação sem checagem.** Deixar alegação sem veredito é escolher o que mostrar
    depois de saber o resultado.
  · **Os dois lados da mesa.** Se só o entrevistado foi checado, isso aparece como aviso alto.
  · **Nenhuma cartela sobreposta** e nenhuma fora do vídeo.
"""

from __future__ import annotations

import argparse
import re
import unicodedata
from datetime import date
from pathlib import Path

from . import config as cfg
from .util import hms, ler_json, ms


class Relatorio:
    def __init__(self) -> None:
        self.erros: list[str] = []
        self.avisos: list[str] = []
        self.notas: list[str] = []

    def erro(self, msg: str) -> None:
        self.erros.append(msg)

    def aviso(self, msg: str) -> None:
        self.avisos.append(msg)

    def nota(self, msg: str) -> None:
        self.notas.append(msg)

    def imprimir(self) -> int:
        for n in self.notas:
            print(f"  · {n}")
        for a in self.avisos:
            print(f"  \033[33m⚠\033[0m {a}")
        for e in self.erros:
            print(f"  \033[31m✗\033[0m {e}")
        print()
        if self.erros:
            print(f"\033[31m✗ REPROVADO — {len(self.erros)} erro(s), {len(self.avisos)} aviso(s)\033[0m")
            return 1
        print(f"\033[32m✓ APROVADO — 0 erros, {len(self.avisos)} aviso(s)\033[0m")
        return 0


# ─────────────────────────────────────────────────────────────────────


def normalizar(texto: str) -> str:
    """Para comparar citação com transcrição: sem acento, sem pontuação, minúsculo,
    espaço colapsado. ⚠️ Não é para exibir nada — só para conferir se a frase existe."""
    t = unicodedata.normalize("NFKD", texto.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    t = re.sub(r"[^a-z0-9 ]+", " ", t)
    return re.sub(r"\s+", " ", t).strip()


# Um dígito precedido de letra é nome, não quantidade: "G20", "PL2", "IPCA15".
NUMERO = re.compile(r"(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ])\d[\d.,]*")


def numeros_de(texto: str) -> set[str]:
    """As QUANTIDADES de um texto, normalizadas para comparação.

    Ficam de fora, de propósito:

    · **número de um dígito só** — aparece em qualquer lugar e só produziria ruído;
    · **ano plausível (1900 a 2099)** — porque esta checagem existe para pegar quantidade
      inventada, e ano é data. Data já é conferida pelo campo `data_de_referencia` e pela
      própria fonte. ⚠️ O preço disso é real e está registrado: um ano errado dentro de um
      resumo (por exemplo "a maior taxa desde 1986") NÃO é pego aqui, e depende da revisão
      humana do PASSO 8. Aconteceu na primeira rodada deste repositório.
    """
    achados = set()
    for bruto in NUMERO.findall(texto or ""):
        limpo = bruto.strip(".,")
        so_digitos = limpo.replace(".", "").replace(",", "")
        if len(so_digitos) < 2:
            continue
        if len(so_digitos) == 4 and limpo == so_digitos and 1900 <= int(so_digitos) <= 2099:
            continue
        achados.add(so_digitos)
    return achados


# ─────────────────────────────────────────────────────────────────────


def _validar_esquema(dados: dict, esquema: Path, rel: Relatorio, rotulo: str) -> None:
    try:
        import jsonschema
    except ImportError:
        rel.aviso("jsonschema não instalado: a validação de esquema foi pulada "
                  "(pip install jsonschema)")
        return
    try:
        jsonschema.validate(dados, ler_json(esquema))
    except jsonschema.ValidationError as e:  # type: ignore[attr-defined]
        caminho = "/".join(str(p) for p in e.absolute_path)
        rel.erro(f"{rotulo}: esquema — em '{caminho or 'raiz'}': {e.message}")


def validar(slug: str, *, recorte: str | None = None) -> int:
    caso = cfg.pasta_do_caso(slug)
    rel = Relatorio()
    print(f"\n\033[1m▶ PASSO 8 · validar — {slug}{' · recorte ' + recorte if recorte else ''}\033[0m\n")

    # ── 1. CASO.json ────────────────────────────────────────────────
    meta = ler_json(caso / "CASO.json")
    _validar_esquema(meta, cfg.ESQUEMAS / "caso.schema.json", rel, "CASO.json")
    nomes_declarados = {f["nome"] for f in meta["falantes"]}
    papel_de = {f["nome"]: f["papel"] for f in meta["falantes"]}

    video = caso / "fonte" / meta["midia"]["arquivo"]
    if video.exists():
        manifesto = caso / "fonte" / "MIDIA.json"
        if manifesto.exists():
            m = ler_json(manifesto)
            if m["sha256"] != meta["midia"]["sha256"]:
                rel.erro("o sha256 do CASO.json não bate com o de fonte/MIDIA.json")
            else:
                rel.nota(f"mídia assinada · sha256 {m['sha256'][:16]}…")
    else:
        rel.nota("o vídeo de origem não está na cópia local (esperado: ele não entra no git)")

    # ── 2. transcrição ──────────────────────────────────────────────
    # Um recorte PODE ter transcrição própria, mas normalmente não tem: os tempos da
    # transcrição da peça inteira já são absolutos, então a checagem de um trecho se faz
    # contra ela. Ver docs/ARQUITETURA.md §9.
    caminho_t = caso / "transcricao" / f"transcricao-{recorte}.json" if recorte else None
    if caminho_t is None or not caminho_t.exists():
        caminho_t = caso / "transcricao" / "transcricao.json"
    transcricao = ler_json(caminho_t)
    rel.nota(f"transcrição usada: {caminho_t.name}")
    segmentos = transcricao["segmentos"]
    if not segmentos:
        rel.erro("a transcrição está vazia")
        return rel.imprimir()

    for a, b in zip(segmentos, segmentos[1:], strict=False):
        if b["inicio_s"] < a["inicio_s"] - 0.001:
            rel.erro(f"transcrição fora de ordem em {hms(b['inicio_s'])}")
            break
    sem_falante = [s for s in segmentos if not s.get("falante")]
    if sem_falante:
        rel.erro(f"{len(sem_falante)} segmentos sem falante — rode o PASSO 3")
    desconhecidos = {s.get("falante") for s in segmentos} - nomes_declarados - {None}
    if desconhecidos:
        rel.erro(f"falantes na transcrição que não estão no CASO.json: {sorted(desconhecidos)}")

    texto_normalizado = normalizar(" ".join(s["texto"] for s in segmentos))
    rel.nota(f"transcrição · {len(segmentos)} segmentos · "
             f"{sum(len(s['texto'].split()) for s in segmentos)} palavras")

    # ── 3. alegações ────────────────────────────────────────────────
    nome_a = f"alegacoes-{recorte}.json" if recorte else "alegacoes.json"
    alegacoes_doc = ler_json(caso / "alegacoes" / nome_a)
    _validar_esquema(alegacoes_doc, cfg.ESQUEMAS / "alegacoes.schema.json", rel, "alegacoes")
    alegacoes = alegacoes_doc["alegacoes"]

    duracao = float(meta["duracao_s"])
    vistos: set[str] = set()
    anterior = -1.0
    for a in alegacoes:
        aid = a["id"]
        if aid in vistos:
            rel.erro(f"{aid}: id repetido")
        vistos.add(aid)

        if a["inicio_s"] < anterior - 0.001:
            rel.erro(f"{aid}: fora de ordem cronológica (começa em {hms(a['inicio_s'])})")
        anterior = a["inicio_s"]

        if a["fim_s"] <= a["inicio_s"]:
            rel.erro(f"{aid}: fim_s não é maior que inicio_s")
        if a["fim_s"] > duracao + 1:
            rel.erro(f"{aid}: termina em {hms(a['fim_s'])}, fora da peça ({hms(duracao)})")

        if a["falante"] not in nomes_declarados:
            rel.erro(f"{aid}: falante '{a['falante']}' não está no CASO.json")
        elif papel_de[a["falante"]] != a["papel"]:
            rel.erro(f"{aid}: papel '{a['papel']}' contradiz o CASO.json "
                     f"('{papel_de[a['falante']]}')")

        # 🔴 a trava da citação
        partes = [p for p in a["frase"].split("[...]") if normalizar(p)]
        for parte in partes:
            if normalizar(parte) not in texto_normalizado:
                rel.erro(
                    f"{aid}: a citação NÃO existe na transcrição — "
                    f'"{parte.strip()[:70]}…"'
                )
                break

        if a["checavel"] and a["tipo"] in cfg.TIPOS_NAO_CHECAVEIS:
            rel.erro(f"{aid}: marcada como checável, mas o tipo é '{a['tipo']}'")
        if not a["checavel"] and a["tipo"] not in cfg.TIPOS_NAO_CHECAVEIS:
            rel.erro(f"{aid}: marcada como não checável, mas o tipo é '{a['tipo']}'")

    # ── 4. checagens ────────────────────────────────────────────────
    nome_c = f"checagens-{recorte}.json" if recorte else "checagens.json"
    checagens_doc = ler_json(caso / "checagens" / nome_c)
    _validar_esquema(checagens_doc, cfg.ESQUEMAS / "checagens.schema.json", rel, "checagens")
    checagens = {c["id"]: c for c in checagens_doc["checagens"]}

    sem_checagem = [a["id"] for a in alegacoes if a["id"] not in checagens]
    if sem_checagem:
        rel.erro(f"{len(sem_checagem)} alegações sem checagem: {sem_checagem[:8]}")
    orfas = set(checagens) - vistos
    if orfas:
        rel.erro(f"checagens sem alegação correspondente: {sorted(orfas)[:8]}")

    hoje = date.today()
    por_veredito: dict[str, int] = {}
    for a in alegacoes:
        c = checagens.get(a["id"])
        if c is None:
            continue
        aid, v = a["id"], c["veredito"]
        por_veredito[v] = por_veredito.get(v, 0) + 1
        veredito = cfg.VEREDITOS[v]

        if not a["checavel"] and v != "NAO_CHECAVEL":
            rel.erro(f"{aid}: alegação não checável recebeu veredito '{v}'")
        if a["checavel"] and v == "NAO_CHECAVEL":
            rel.erro(f"{aid}: alegação checável recebeu NAO_CHECAVEL — "
                     "se não deu para checar, o veredito é INSUSTENTAVEL, com a busca descrita")

        fontes = c.get("fontes", [])
        if len(fontes) < veredito.exige_fontes:
            rel.erro(f"{aid} [{v}]: {len(fontes)} fonte(s), o mínimo é {veredito.exige_fontes}")

        urls = [f["url"] for f in fontes]
        if len(set(urls)) != len(urls):
            rel.erro(f"{aid}: a mesma URL aparece duas vezes — não são duas fontes")

        exige_forte = (v != "NAO_CHECAVEL"
                       and a["tipo"] in cfg.TIPOS_QUE_EXIGEM_FONTE_FORTE)
        if exige_forte and not any(f["nivel"] in cfg.NIVEIS_FORTES for f in fontes):
            rel.erro(f"{aid} [{a['tipo']}]: nenhuma fonte N1 ou N2 "
                     "(METODOLOGIA §3.1 regra 1)")

        for f in fontes:
            try:
                consultada = date.fromisoformat(f["consultada_em"])
                if consultada > hoje:
                    rel.erro(f"{aid}: fonte consultada no futuro ({f['consultada_em']})")
            except ValueError:
                rel.erro(f"{aid}: data de consulta inválida '{f['consultada_em']}'")
            if not f["url"].startswith("http"):
                rel.erro(f"{aid}: URL inválida '{f['url'][:60]}'")

        # 🔴 lastro numérico — METODOLOGIA §3.1 regra 6
        if v != "NAO_CHECAVEL":
            texto_trechos = " ".join(f["trecho"] for f in fontes)
            trechos = normalizar(texto_trechos)
            numeros_trechos = numeros_de(texto_trechos)

            # Número derivado por cálculo (subtração, conversão de unidade, arredondamento)
            # não está literalmente em trecho nenhum — e ainda assim tem lastro. A saída NÃO
            # é abrir exceção: é obrigar quem derivou a declarar a conta, e conferir que as
            # PARCELAS da conta estão nos trechos. Ver docs/METODOLOGIA.md §3.1.
            derivados: set[str] = set()
            for d in c.get("derivacoes", []):
                parcelas = numeros_de(d.get("de", ""))
                faltando = [
                    n for n in parcelas
                    if n not in numeros_trechos and n not in trechos.replace(" ", "")
                ]
                if faltando:
                    rel.erro(f"{aid}: a derivação de '{d.get('valor')}' usa {faltando} "
                             "que não está em nenhum trecho de fonte")
                else:
                    derivados |= numeros_de(d.get("valor", ""))

            # Número que a própria pessoa falou e que o card repete não precisa de fonte:
            # a fonte dele é a transcrição, que o bloco 3 já conferiu palavra por palavra.
            ditos = numeros_de(c.get("numero_dito") or "") | numeros_de(a["frase"])

            for campo in ("numero_apurado", "resumo"):
                for n in numeros_de(c.get(campo) or ""):
                    if (n not in numeros_trechos and n not in derivados and n not in ditos
                            and n not in trechos.replace(" ", "")):
                        rel.aviso(f"{aid}: o número '{n}' aparece em {campo} mas não em "
                                  "nenhum trecho de fonte nem em derivação declarada")

        if c.get("confianca") == "baixa" and not c.get("revisao_humana"):
            rel.erro(f"{aid}: confiança baixa sem revisão humana registrada")
        if v in ("FALSO", "INSUSTENTAVEL") and len(c.get("explicacao", "")) < 120:
            rel.aviso(f"{aid} [{v}]: explicação curta para um veredito pesado")

    # ── 5. os dois lados da mesa ────────────────────────────────────
    por_papel: dict[str, int] = {}
    for a in alegacoes:
        por_papel[a["papel"]] = por_papel.get(a["papel"], 0) + 1
    rel.nota("alegações por papel: " + " · ".join(f"{k} {n}" for k, n in sorted(por_papel.items())))
    rel.nota("vereditos: " + " · ".join(
        f"{cfg.VEREDITOS[k].rotulo} {n}" for k, n in sorted(por_veredito.items())))
    if len(alegacoes) >= 10 and por_papel.get("entrevistador", 0) == 0:
        rel.aviso("nenhuma alegação de entrevistador em 10+ alegações — "
                  "a pergunta também afirma fato (METODOLOGIA §4.1)")

    # ── 6. plano de overlay ─────────────────────────────────────────
    nome_p = f"plano-{recorte}.json" if recorte else "plano.json"
    caminho_plano = caso / "overlay" / nome_p
    if caminho_plano.exists():
        plano = ler_json(caminho_plano)
        cartelas = sorted(plano["cartelas"], key=lambda c: c["entra_s"])
        for x, y in zip(cartelas, cartelas[1:], strict=False):
            if y["entra_s"] < x["sai_s"] - 0.001:
                rel.erro(f"cartelas sobrepostas: {x['id']} sai em {x['sai_s']:.2f}s e "
                         f"{y['id']} entra em {y['entra_s']:.2f}s")
        for c in cartelas:
            arq = caso / c["arquivo"]
            if not arq.exists():
                rel.erro(f"cartela ausente: {c['arquivo']}")
            dur = c["sai_s"] - c["entra_s"]
            if dur < cfg.CARD_DURACAO_MIN_S - 0.001:
                rel.aviso(f"{c['id']} fica {dur:.1f}s na tela (piso {cfg.CARD_DURACAO_MIN_S}s)")
            if c["sai_s"] > plano["duracao_s"] + 0.5:
                rel.erro(f"{c['id']} sai depois do fim do vídeo")
            if c.get("atraso_do_fim_s", 0) > cfg.ATRASO_MAX_S:
                rel.aviso(f"{c['id']} só entra {c['atraso_do_fim_s']:.1f}s depois de a frase "
                          f"acabar (teto {cfg.ATRASO_MAX_S}s)")
        rel.nota(f"plano de overlay · {len(cartelas)} cartelas · {ms(plano['duracao_s'])}")
    else:
        rel.nota("ainda não há plano de overlay (PASSO 6 não rodou)")

    return rel.imprimir()


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem validar", description="PASSO 8 — validar")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    args = p.parse_args(argv)
    return validar(args.slug, recorte=args.recorte)


if __name__ == "__main__":
    raise SystemExit(main())
