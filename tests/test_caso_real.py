"""Regressão contra os casos que estão no repositório.

Este é o teste com mais dentes do projeto: ele roda o validador de verdade sobre os arquivos
de verdade. Se alguém mexer numa regra e um caso publicado parar de passar, isto acusa.

🔧 Até a 0.1.1 ele olhava um caso escrito à mão aqui. Agora descobre sozinho todo par
alegações + checagens em `casos/`, e cada teste roda uma vez por caso: um caso novo entra
na regressão sem ninguém precisar lembrar de acrescentá-lo.

⚠️ Ele NÃO precisa do vídeo nem do áudio, que não entram no git. Roda em qualquer clone.
"""

from __future__ import annotations

import json

import pytest

from checagem import config as cfg
from checagem.passo8_validar import numeros_de, validar


def _alvos():
    achados = []
    for caso in sorted(p for p in cfg.CASOS.iterdir() if (p / "CASO.json").exists()):
        for arq in sorted((caso / "alegacoes").glob("alegacoes-*.json")):
            recorte = arq.stem[len("alegacoes-"):]
            if (caso / "checagens" / f"checagens-{recorte}.json").exists():
                achados.append(pytest.param((caso.name, recorte), id=f"{caso.name}:{recorte}"))
    return achados


ALVOS = _alvos()
pytestmark = pytest.mark.skipif(not ALVOS, reason="nenhum caso com checagem no repositório")


@pytest.fixture(params=ALVOS)
def alvo(request):
    return request.param


def ler(slug, caminho):
    return json.loads((cfg.CASOS / slug / caminho).read_text(encoding="utf-8"))


def test_o_caso_publicado_passa_no_validador(alvo, capsys):
    slug, recorte = alvo
    assert validar(slug, recorte=recorte) == 0


def test_toda_alegacao_tem_exatamente_uma_checagem(alvo):
    slug, recorte = alvo
    alegacoes = ler(slug, f"alegacoes/alegacoes-{recorte}.json")["alegacoes"]
    checagens = ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]
    assert [a["id"] for a in alegacoes] == [c["id"] for c in checagens]


def test_os_dois_lados_da_mesa_foram_checados(alvo):
    slug, recorte = alvo
    """⛔ Um caso só com o entrevistado checado é caso incompleto. A pergunta que afirma
    fato entra pelo mesmo funil."""
    alegacoes = ler(slug, f"alegacoes/alegacoes-{recorte}.json")["alegacoes"]
    papeis = {a["papel"] for a in alegacoes}
    assert "entrevistado" in papeis
    assert "entrevistador" in papeis


def test_veredito_com_fonte_tem_no_minimo_duas_urls_distintas(alvo):
    slug, recorte = alvo
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        if c["veredito"] == "NAO_CHECAVEL":
            assert c["fontes"] == []
            continue
        urls = [f["url"] for f in c["fontes"]]
        assert len(urls) >= 2, c["id"]
        assert len(set(urls)) == len(urls), f"{c['id']}: URL repetida"


def test_alegacao_numerica_tem_fonte_primaria_ou_institucional(alvo):
    slug, recorte = alvo
    alegacoes = {a["id"]: a for a in ler(slug, f"alegacoes/alegacoes-{recorte}.json")["alegacoes"]}
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        if c["veredito"] == "NAO_CHECAVEL":
            continue
        if alegacoes[c["id"]]["tipo"] in cfg.TIPOS_QUE_EXIGEM_FONTE_FORTE:
            assert any(f["nivel"] in cfg.NIVEIS_FORTES for f in c["fontes"]), c["id"]


def test_nenhum_resumo_fala_de_intencao(alvo):
    slug, recorte = alvo
    """⛔ O card fala do enunciado, nunca do motivo. Ver .cursor/rules/escrita-de-card.mdc."""
    proibidas = cfg.TERMOS_DE_INTENCAO
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        baixo = c["resumo"].lower()
        for termo in proibidas:
            assert termo not in baixo, f"{c['id']}: '{termo}' no resumo"


def test_nenhum_resumo_usa_travessao(alvo):
    slug, recorte = alvo
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        assert "—" not in c["resumo"], c["id"]


def test_resumo_cabe_no_card(alvo):
    slug, recorte = alvo
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        assert 8 <= len(c["resumo"]) <= 120, c["id"]


def test_derivacoes_tem_as_parcelas_nos_trechos(alvo):
    """A exceção declarada da regra 6 só vale se as parcelas da conta estiverem nas fontes, ou
    na própria fala (o número dito, na conta que mede o desvio dele)."""
    slug, recorte = alvo
    alegacoes = {a["id"]: a for a in ler(slug, f"alegacoes/alegacoes-{recorte}.json")["alegacoes"]}
    for c in ler(slug, f"checagens/checagens-{recorte}.json")["checagens"]:
        if not c.get("derivacoes"):
            continue
        trechos = " ".join(f["trecho"] for f in c["fontes"])
        nos_trechos = numeros_de(trechos)
        achatado = trechos.replace(" ", "").replace(",", "").replace(".", "")
        da_fala = numeros_de(alegacoes[c["id"]]["frase"]) | numeros_de(c.get("numero_dito") or "")
        for d in c["derivacoes"]:
            for n in numeros_de(d["de"]):
                assert n in nos_trechos or n in achatado or n in da_fala, f"{c['id']}: parcela {n} sem lastro"

def test_o_recorte_guarda_o_tempo_absoluto(alvo):
    slug, recorte = alvo
    """Sem origem_inicio_s, um card checado num trecho não sabe voltar ao minuto certo
    da peça inteira."""
    reg = next(r for r in ler(slug, "recortes/RECORTES.json")["recortes"] if r["id"] == recorte)
    assert reg["origem_inicio_s"] > 0
    assert reg["motivo"].strip()


def test_o_motivo_do_recorte_esta_escrito(alvo):
    slug, recorte = alvo
    """⛔ A escolha do trecho não pode ser feita pelo resultado, e o motivo sai no relatório
    exatamente para poder ser contestado."""
    reg = next(r for r in ler(slug, "recortes/RECORTES.json")["recortes"] if r["id"] == recorte)
    assert len(reg["motivo"]) > 40
