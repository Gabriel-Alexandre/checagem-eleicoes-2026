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
  · **O plano de overlay está em dia com as checagens.** Um veredito mudado depois do PASSO 6
    deixaria a moldura com a cor antiga no vídeo.
  · **O texto da tela obedece às regras de escrita**: sem travessão, sem leitura de intenção.
  · **Ano também precisa de lastro.** Ver `anos_de()`: é o conserto do "desde 1986".
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


ANO = re.compile(r"(?<![0-9A-Za-zÀ-ÖØ-öø-ÿ.,])(19\d{2}|20\d{2})(?![0-9A-Za-z]|[.,]\d)")


def anos_de(texto: str) -> set[str]:
    """Os ANOS de um texto: os números que `numeros_de()` deixa de fora de propósito.

    🔧 Existe por causa de um defeito real. "A maior taxa desde 1986" entrou num resumo da
    primeira rodada escrito de memória, e `numeros_de()` não pegou porque trata ano como data.
    Ano que aparece na tela, porém, também é afirmação: ou está num trecho de fonte, ou na
    própria fala, ou na `data_de_referencia`. O validador cobra isso como AVISO, não como erro,
    porque ano aparece em lugar legítimo demais para reprovar sem uma leitura (METODOLOGIA §3.1).
    """
    return set(ANO.findall(texto or ""))


def valores_de(texto: str) -> list[float]:
    """Os números de um texto como QUANTIDADE, no formato brasileiro: '10,81' -> 10.81,
    '1.234,5' -> 1234.5. Serve para comparar o dito com o apurado com tolerância."""
    saida = []
    for bruto in NUMERO.findall(texto or ""):
        limpo = bruto.strip(".,")
        if "," in limpo:
            limpo = limpo.replace(".", "").replace(",", ".")
        elif limpo.count(".") >= 1 and all(len(p) == 3 for p in limpo.split(".")[1:]):
            limpo = limpo.replace(".", "")
        try:
            saida.append(float(limpo))
        except ValueError:
            continue
    return saida


def _tem_intencao(texto: str) -> list[str]:
    baixo = (texto or "").lower()
    return [t for t in cfg.TERMOS_DE_INTENCAO if re.search(rf"(?<![a-zà-ÿ]){re.escape(t)}(?![a-zà-ÿ])", baixo)]


def _partes_da_citacao(texto: str) -> list[str]:
    return [p for p in texto.split("[...]") if normalizar(p)]


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
    cobertura = alegacoes_doc.get("cobertura")
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
        # A cobertura é a prova de que a varredura não escolheu trechos. Alegação fora dela
        # quer dizer que alguém foi pescar fora do intervalo que declarou ter varrido.
        if cobertura and (a["inicio_s"] < cobertura["inicio_s"] - 0.5
                          or a["inicio_s"] > cobertura["fim_s"] + 0.5):
            rel.erro(f"{aid}: começa em {hms(a['inicio_s'])}, fora da cobertura declarada "
                     f"({hms(cobertura['inicio_s'])} a {hms(cobertura['fim_s'])})")

        if a["falante"] not in nomes_declarados:
            rel.erro(f"{aid}: falante '{a['falante']}' não está no CASO.json")
        elif papel_de[a["falante"]] != a["papel"]:
            rel.erro(f"{aid}: papel '{a['papel']}' contradiz o CASO.json "
                     f"('{papel_de[a['falante']]}')")

        # 🔴 a trava da citação
        for parte in _partes_da_citacao(a["frase"]):
            if normalizar(parte) not in texto_normalizado:
                rel.erro(
                    f"{aid}: a citação NÃO existe na transcrição — "
                    f'"{parte.strip()[:70]}…"'
                )
                break

        # A citação encurtada para a tela passa pela MESMA trava, e ainda tem que sair da
        # própria frase: encurtar não autoriza trocar de fala.
        if a.get("citacao_card"):
            frase_norm = normalizar(" ".join(_partes_da_citacao(a["frase"])))
            for parte in _partes_da_citacao(a["citacao_card"]):
                if normalizar(parte) not in texto_normalizado:
                    rel.erro(f'{aid}: a citacao_card NÃO existe na transcrição — "{parte.strip()[:70]}…"')
                    break
                if normalizar(parte) not in frase_norm:
                    rel.erro(f"{aid}: a citacao_card não é um trecho da própria `frase`")
                    break

        if a["checavel"] and a["tipo"] in cfg.TIPOS_NAO_CHECAVEIS:
            rel.erro(f"{aid}: marcada como checável, mas o tipo é '{a['tipo']}'")
        if not a["checavel"] and a["tipo"] not in cfg.TIPOS_NAO_CHECAVEIS:
            rel.erro(f"{aid}: marcada como não checável, mas o tipo é '{a['tipo']}'")

    for e in alegacoes_doc.get("exclusoes", []):
        if cobertura and not (cobertura["inicio_s"] - 0.5 <= e["inicio_s"] <= cobertura["fim_s"] + 0.5):
            rel.erro(f"exclusão em {hms(e['inicio_s'])} está fora da cobertura declarada")
        for parte in _partes_da_citacao(e["frase"]):
            if normalizar(parte) not in texto_normalizado:
                rel.aviso(f"exclusão em {hms(e['inicio_s'])}: a frase não está na transcrição "
                          "(aceitável só se o motivo for justamente a transcrição não resolvida)")
                break

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
    try:
        extraido_em = date.fromisoformat(alegacoes_doc["gerado_em"])
    except (KeyError, ValueError):
        extraido_em = None
    capturas_path = caso / "checagens" / "CAPTURAS.json"
    capturas_doc = ler_json(capturas_path) if capturas_path.exists() else None
    urls_capturadas = (
        {c["url"] for c in capturas_doc.get("capturas", []) if c.get("sha256")}
        if capturas_doc else None
    )
    urls_citadas: set[str] = set()
    revisadas = 0
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
        urls_citadas |= {f["url"] for f in fontes}
        if c.get("revisao_humana"):
            revisadas += 1

        # Regras de escrita do que vai para a tela (.cursor/rules/escrita-de-card.mdc).
        for campo in ("resumo", "ressalva"):
            texto = c.get(campo) or ""
            if any(t in texto for t in cfg.TRAVESSOES):
                rel.erro(f"{aid}: travessão em `{campo}` — ele quebra mal em caixa estreita")
            for termo in _tem_intencao(texto):
                rel.erro(f"{aid}: `{campo}` lê intenção ou conclui sobre a pessoa ('{termo}')")
        for termo in _tem_intencao(c.get("explicacao", "")):
            rel.aviso(f"{aid}: a explicação usa '{termo}' — confira se é citação, e não leitura "
                      "de intenção")

        if (v != "NAO_CHECAVEL" and a["tipo"] in ("numero", "serie_historica", "valor_monetario")
                and not (c.get("data_de_referencia") or "").strip()):
            rel.erro(f"{aid} [{a['tipo']}]: sem `data_de_referencia` — um número certo sem data "
                     "vira anacronismo (METODOLOGIA §5)")

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
                if extraido_em and consultada < extraido_em:
                    rel.aviso(f"{aid}: fonte consultada em {f['consultada_em']}, antes da extração "
                              f"({extraido_em.isoformat()}) — a extração vem antes da busca")
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
            # A parcela de uma conta pode vir da fonte OU da própria fala: "94 contra 92,4" é a
            # conta que mede o desvio do número dito, e o 94 tem lastro na transcrição.
            da_fala = numeros_de(a["frase"]) | numeros_de(c.get("numero_dito") or "")
            for d in c.get("derivacoes", []):
                parcelas = numeros_de(d.get("de", ""))
                faltando = [
                    n for n in parcelas
                    if n not in numeros_trechos and n not in trechos.replace(" ", "") and n not in da_fala
                ]
                if faltando:
                    rel.erro(f"{aid}: a derivação de '{d.get('valor')}' usa {faltando} "
                             "que não está em nenhum trecho de fonte")
                else:
                    derivados |= numeros_de(d.get("valor", ""))

            # Número que a própria pessoa falou e que o card repete não precisa de fonte:
            # a fonte dele é a transcrição, que o bloco 3 já conferiu palavra por palavra.
            ditos = numeros_de(c.get("numero_dito") or "") | numeros_de(a["frase"])

            for campo in ("numero_apurado", "resumo", "ressalva"):
                for n in numeros_de(c.get(campo) or ""):
                    if (n not in numeros_trechos and n not in derivados and n not in ditos
                            and n not in trechos.replace(" ", "")):
                        rel.aviso(f"{aid}: o número '{n}' aparece em {campo} mas não em "
                                  "nenhum trecho de fonte nem em derivação declarada")

            # 🔧 O ano, que `numeros_de()` deixa de fora. Ver `anos_de()`.
            anos_com_lastro = (anos_de(texto_trechos) | anos_de(a["frase"])
                               | anos_de(c.get("data_de_referencia") or "")
                               | anos_de(" ".join(d.get("de", "") + " " + d.get("valor", "")
                                                  for d in c.get("derivacoes", []))))
            for campo in ("resumo", "ressalva", "numero_apurado"):
                for ano in sorted(anos_de(c.get(campo) or "") - anos_com_lastro):
                    rel.aviso(f"{aid}: o ano {ano} aparece em {campo} mas não em trecho de fonte, "
                              "na fala nem na data de referência")

        # 🔧 Pego por um espectador (comentário no vídeo publicado, set/2026): "ele disse 94 bi,
        # o card mostra 92,4 bi e marca VERDADEIRO". O veredito estava certo pela régua do §2.2
        # (desvio de 1,7%), mas a própria régua manda o card DIZER o arredondamento, e não dizia.
        # Número dito diferente do apurado, num VERDADEIRO, exige ressalva que traga o número.
        if v == "VERDADEIRO":
            dito_txt = (c.get("numero_dito") or "").lower()
            d_vals, a_vals = valores_de(dito_txt), valores_de(c.get("numero_apurado") or "")
            if d_vals and a_vals and a_vals[0]:
                d, ap = d_vals[0], a_vals[0]
                piso = any(t in dito_txt for t in ("mais de", "acima de", "passou de", "ultrapass"))
                teto = any(t in dito_txt for t in ("menos de", "abaixo de"))
                coerente = (piso and ap >= d) or (teto and ap <= d)
                if not coerente and abs(d - ap) / abs(ap) >= 0.01:
                    na_ressalva = valores_de(c.get("ressalva") or "")
                    if not any(abs(x - ap) / abs(ap) < 0.05 for x in na_ressalva):
                        rel.aviso(f"{aid}: VERDADEIRO com o número dito ({c.get('numero_dito')}) "
                                  f"{abs(d - ap) / abs(ap) * 100:.1f}% longe do apurado, e a ressalva "
                                  "não mostra o valor apurado: o card tem que dizer o arredondamento "
                                  "(METODOLOGIA §2.2)")

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
    rel.nota(f"revisão humana registrada: {revisadas} de {len(checagens)} checagens"
             + (" (a doutrina manda uma pessoa ler antes de publicar)" if revisadas == 0 else ""))
    if urls_capturadas is not None:
        sem_captura = sorted(urls_citadas - urls_capturadas)
        rel.nota(f"capturas assinadas: {len(urls_citadas) - len(sem_captura)} de "
                 f"{len(urls_citadas)} URLs citadas têm sha256 em checagens/CAPTURAS.json")
        for u in sem_captura[:5]:
            rel.aviso(f"URL citada sem captura assinada: {u[:90]}")
        conferidos = [(c["url"], aid, r) for c in capturas_doc["capturas"]
                      for aid, r in (c.get("trechos") or {}).items()]
        achados = sum(1 for _, _, r in conferidos if r == "encontrado")
        rel.nota(f"trechos conferidos contra a página capturada: {achados} de {len(conferidos)} encontrados")
        for url, aid, r in conferidos:
            if r != "encontrado":
                rel.aviso(f"{aid}: o trecho citado não foi encontrado na captura de {url[:80]} — "
                          "a página mudou, ou o trecho não é cópia literal")
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
        legenda = plano.get("legenda")
        if legenda and cartelas and cartelas[0]["entra_s"] < legenda["sai_s"] - 0.001:
            rel.aviso(f"{cartelas[0]['id']} entra em {cartelas[0]['entra_s']:.2f}s, durante a "
                      "legenda de abertura — rode o PASSO 6 de novo")

        # O plano é derivado das checagens. Se elas mudaram depois, o vídeo mostraria o passado.
        base = float(plano.get("base_s", 0.0))
        limite = float(plano["duracao_s"])
        no_trecho = {a["id"] for a in alegacoes
                     if not (a["fim_s"] - base < 0 or a["inicio_s"] - base > limite)}
        no_plano = {c["id"] for c in cartelas}
        if no_trecho - no_plano:
            rel.erro(f"alegações sem cartela no plano: {sorted(no_trecho - no_plano)[:8]} — "
                     "rode o PASSO 6 de novo")
        if no_plano - no_trecho:
            rel.erro(f"cartelas no plano sem alegação: {sorted(no_plano - no_trecho)[:8]}")
        for c in cartelas:
            atual = checagens.get(c["id"], {}).get("veredito")
            if atual and c.get("veredito") != atual:
                rel.erro(f"{c['id']}: o plano diz {c.get('veredito')} e a checagem diz {atual} — "
                         "a moldura sairia com a cor errada; rode o PASSO 6 de novo")

        # As PNGs são derivadas e ficam fora do git: num clone limpo elas simplesmente não
        # existem ainda, e isso não é defeito. Defeito é existir a pasta com cartela faltando.
        pasta = caso / "overlay" / (f"cartelas-{recorte}" if recorte else "cartelas")
        if not pasta.exists():
            rel.nota(f"cartelas ainda não desenhadas nesta cópia (são derivadas, fora do git): "
                     f"python -m checagem overlay {slug}" + (f" --recorte {recorte}" if recorte else ""))
        else:
            for c in cartelas:
                if not (caso / c["arquivo"]).exists():
                    rel.erro(f"cartela ausente: {c['arquivo']}")

        for c in cartelas:
            dur = c["sai_s"] - c["entra_s"]
            if dur < cfg.CARD_DURACAO_MIN_S - 0.001:
                rel.aviso(f"{c['id']} fica {dur:.1f}s na tela (piso {cfg.CARD_DURACAO_MIN_S}s)")
            if c["sai_s"] > plano["duracao_s"] + 0.5:
                rel.erro(f"{c['id']} sai depois do fim do vídeo")
            if c.get("atraso_do_fim_s", 0) > cfg.ATRASO_MAX_S:
                rel.aviso(f"{c['id']} só entra {c['atraso_do_fim_s']:.1f}s depois de a frase "
                          f"acabar (teto {cfg.ATRASO_MAX_S}s)")
            for campo in c.get("cortado_na_tela", []):
                rel.aviso(f"{c['id']}: `{campo}` não cabe em duas linhas e sai cortado na tela"
                          + (" — use `citacao_card`" if campo == "citacao" else ""))
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
