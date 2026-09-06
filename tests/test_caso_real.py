"""Regressão contra o caso que está no repositório.

Este é o teste com mais dentes do projeto: ele roda o validador de verdade sobre os arquivos
de verdade. Se alguém mexer numa regra e o caso publicado parar de passar, isto acusa.

⚠️ Ele NÃO precisa do vídeo nem do áudio, que não entram no git. Roda em qualquer clone.
"""

from __future__ import annotations

import json

import pytest

from checagem import config as cfg
from checagem.passo8_validar import numeros_de, validar

SLUG = "2026-08-27-sabatina-lula-globo"
RECORTE = "bloco-contas-publicas"
CASO = cfg.CASOS / SLUG

pytestmark = pytest.mark.skipif(not CASO.exists(), reason="o caso de exemplo não está aqui")


def ler(caminho):
    return json.loads((CASO / caminho).read_text(encoding="utf-8"))


def test_o_caso_publicado_passa_no_validador(capsys):
    assert validar(SLUG, recorte=RECORTE) == 0


def test_toda_alegacao_tem_exatamente_uma_checagem():
    alegacoes = ler(f"alegacoes/alegacoes-{RECORTE}.json")["alegacoes"]
    checagens = ler(f"checagens/checagens-{RECORTE}.json")["checagens"]
    assert [a["id"] for a in alegacoes] == [c["id"] for c in checagens]


def test_os_dois_lados_da_mesa_foram_checados():
    """⛔ Um caso só com o entrevistado checado é caso incompleto. A pergunta que afirma
    fato entra pelo mesmo funil."""
    alegacoes = ler(f"alegacoes/alegacoes-{RECORTE}.json")["alegacoes"]
    papeis = {a["papel"] for a in alegacoes}
    assert "entrevistado" in papeis
    assert "entrevistador" in papeis


def test_veredito_com_fonte_tem_no_minimo_duas_urls_distintas():
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        if c["veredito"] == "NAO_CHECAVEL":
            assert c["fontes"] == []
            continue
        urls = [f["url"] for f in c["fontes"]]
        assert len(urls) >= 2, c["id"]
        assert len(set(urls)) == len(urls), f"{c['id']}: URL repetida"


def test_alegacao_numerica_tem_fonte_primaria_ou_institucional():
    alegacoes = {a["id"]: a for a in ler(f"alegacoes/alegacoes-{RECORTE}.json")["alegacoes"]}
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        if c["veredito"] == "NAO_CHECAVEL":
            continue
        if alegacoes[c["id"]]["tipo"] in cfg.TIPOS_QUE_EXIGEM_FONTE_FORTE:
            assert any(f["nivel"] in cfg.NIVEIS_FORTES for f in c["fontes"]), c["id"]


def test_nenhum_resumo_fala_de_intencao():
    """⛔ O card fala do enunciado, nunca do motivo. Ver .cursor/rules/escrita-de-card.mdc."""
    proibidas = ("tentou esconder", "quis passar", "sabia que", "omitiu de propósito",
                 "de propósito", "mentiu", "mentira")
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        baixo = c["resumo"].lower()
        for termo in proibidas:
            assert termo not in baixo, f"{c['id']}: '{termo}' no resumo"


def test_nenhum_resumo_usa_travessao():
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        assert "—" not in c["resumo"], c["id"]


def test_resumo_cabe_no_card():
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        assert 8 <= len(c["resumo"]) <= 120, c["id"]


def test_derivacoes_tem_as_parcelas_nos_trechos():
    """A exceção declarada da regra 6 só vale se as parcelas da conta estiverem nas fontes."""
    for c in ler(f"checagens/checagens-{RECORTE}.json")["checagens"]:
        if not c.get("derivacoes"):
            continue
        trechos = " ".join(f["trecho"] for f in c["fontes"])
        nos_trechos = numeros_de(trechos)
        achatado = trechos.replace(" ", "").replace(",", "").replace(".", "")
        for d in c["derivacoes"]:
            for n in numeros_de(d["de"]):
                assert n in nos_trechos or n in achatado, f"{c['id']}: parcela {n} sem lastro"


def test_o_recorte_guarda_o_tempo_absoluto():
    """Sem origem_inicio_s, um card checado num trecho não sabe voltar ao minuto certo
    da peça inteira."""
    reg = next(r for r in ler("recortes/RECORTES.json")["recortes"] if r["id"] == RECORTE)
    assert reg["origem_inicio_s"] > 0
    assert reg["motivo"].strip()


def test_o_motivo_do_recorte_esta_escrito():
    """⛔ A escolha do trecho não pode ser feita pelo resultado, e o motivo sai no relatório
    exatamente para poder ser contestado."""
    reg = next(r for r in ler("recortes/RECORTES.json")["recortes"] if r["id"] == RECORTE)
    assert len(reg["motivo"]) > 40
