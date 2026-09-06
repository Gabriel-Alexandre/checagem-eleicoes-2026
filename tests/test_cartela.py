"""O desenho da cartela.

⚠️ Precisa das fontes, que não entram no git. Rode antes:
    python -m checagem ativos baixar-fontes
"""

from __future__ import annotations

import json

import pytest

from checagem import config as cfg

pytestmark = pytest.mark.skipif(
    not cfg.FONTE_SANS.exists(),
    reason="fontes não baixadas: python -m checagem ativos baixar-fontes",
)


@pytest.fixture(scope="module")
def desenho():
    from checagem import tipografia as tipo
    from checagem.passo6_overlay import _fontes_em_uma_linha
    f = tipo.fonte(cfg.TAM_FONTES, "Medium")
    largura = cfg.CARD_LARGURA - cfg.CARD_BARRA - 2 * cfg.CARD_PADDING_X
    return _fontes_em_uma_linha, f, largura, tipo


def fonte_falsa(instituicao):
    return {"nivel": "N1", "instituicao": instituicao, "titulo": "t",
            "url": "https://exemplo", "consultada_em": "2026-01-01",
            "trecho": "x" * 30, "prova": "y" * 20}


def test_linha_de_fontes_nunca_estoura_a_caixa(desenho):
    """🔴 O defeito real: 'US Department of the Treasury / Federal Reserve Bank of St. Louis'
    somado a um segundo nome dava 1802px numa caixa de 1710px. Nenhum validador pegou."""
    montar, f, largura, tipo = desenho
    casos = [
        [fonte_falsa("IBGE")],
        [fonte_falsa("IBGE"), fonte_falsa("IBGE")],
        [fonte_falsa("US Department of the Treasury / Federal Reserve Bank of St. Louis"),
         fonte_falsa("Federal Reserve Bank of St. Louis (fonte: US Office of Management and Budget)")],
        [fonte_falsa("Instituição com um nome absurdamente longo " * 6)],
        [fonte_falsa(f"Instituição {i}") for i in range(12)],
    ]
    for fontes in casos:
        linha = montar(fontes, f, largura)
        assert tipo.largura(linha, f) <= largura, linha


def test_duas_fontes_da_mesma_casa_mostram_a_contagem(desenho):
    """Sem isso, o card diria 'FONTES: IBGE' tendo dois documentos do IBGE, e passaria a
    impressão de uma fonte só."""
    montar, f, largura, _ = desenho
    linha = montar([fonte_falsa("IBGE"), fonte_falsa("IBGE")], f, largura)
    assert "2 documentos" in linha


def test_sem_fontes_a_linha_e_vazia(desenho):
    montar, f, largura, _ = desenho
    assert montar([], f, largura) == ""


def test_as_fontes_do_caso_publicado_cabem(desenho):
    montar, f, largura, tipo = desenho
    caminho = cfg.CASOS / "2026-08-27-sabatina-lula-globo" / "checagens" / \
        "checagens-bloco-contas-publicas.json"
    if not caminho.exists():
        pytest.skip("o caso de exemplo não está aqui")
    for c in json.loads(caminho.read_text(encoding="utf-8"))["checagens"]:
        linha = montar(c.get("fontes", []), f, largura)
        assert tipo.largura(linha, f) <= largura, f"{c['id']}: {linha}"


def test_toda_cor_de_veredito_tem_rotulo_proprio():
    """Verde e vermelho não podem ser a única diferença: cerca de 8% dos homens têm alguma
    deficiência de visão de cor. O badge sempre traz a palavra."""
    rotulos = [v.rotulo for v in cfg.VEREDITOS.values()]
    assert len(set(rotulos)) == len(rotulos)
    assert all(r.strip() for r in rotulos)


def test_cada_veredito_tem_cor_distinta():
    cores = [v.cor for v in cfg.VEREDITOS.values()]
    assert len(set(cores)) == len(cores)
