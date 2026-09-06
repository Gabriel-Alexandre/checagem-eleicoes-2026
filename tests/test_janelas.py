"""O tempo de tela das cartelas.

Cada teste aqui trava um defeito que já aconteceu ou que quebraria o vídeo em silêncio.
"""

from __future__ import annotations

import pytest

from checagem import config as cfg
from checagem.passo6_overlay import _janelas


def alegacao(id_, inicio, fim):
    return {"id": id_, "inicio_s": inicio, "fim_s": fim}


def test_duas_alegacoes_na_mesma_frase_nao_colidem():
    """🔴 O defeito que motivou a fila.

    "a dívida disparou 10 pontos, atingiu 82% do PIB" tem dois números que se conferem em
    séries diferentes, e a metodologia manda separá-los. Com o mesmo intervalo de fala, a
    versão antiga cortava a primeira cartela no começo da segunda e produzia duração zero
    ou negativa.
    """
    js = _janelas([alegacao("A001", 10.0, 16.0), alegacao("A002", 10.0, 16.0)], 300.0)
    assert len(js) == 2
    for j in js:
        assert j["sai_s"] - j["entra_s"] >= cfg.CARD_DURACAO_MIN_S - 1e-6
    assert js[1]["entra_s"] >= js[0]["sai_s"]


def test_nunca_ha_duas_cartelas_na_tela():
    """Duas cartelas simultâneas é defeito, não estilo: não dá para saber a qual frase
    a moldura se refere."""
    itens = [alegacao(f"A{i:03d}", i * 2.0, i * 2.0 + 1.5) for i in range(1, 15)]
    js = _janelas(itens, 600.0)
    for a, b in zip(js, js[1:], strict=False):
        assert b["entra_s"] >= a["sai_s"], f"{a['id']} e {b['id']} se sobrepõem"


def test_folga_entre_cartelas_e_respeitada():
    js = _janelas([alegacao("A001", 0.0, 1.0), alegacao("A002", 0.5, 1.0)], 300.0)
    assert js[1]["entra_s"] - js[0]["sai_s"] == pytest.approx(cfg.FOLGA_ENTRE_CARDS_S)


def test_cartela_nunca_passa_do_fim_do_video():
    js = _janelas([alegacao("A001", 95.0, 99.0)], 100.0)
    assert js[0]["sai_s"] <= 100.0


def test_cartela_espremida_no_fim_e_marcada_como_curta():
    """Quando o vídeo acaba antes do piso de leitura, o card sai curto — e isso precisa
    aparecer, não ser escondido."""
    js = _janelas([alegacao("A001", 99.0, 99.5)], 100.0)
    assert js[0]["curta"] is True


def test_teto_de_duracao():
    """Card parado demais vira ruído e some da atenção."""
    js = _janelas([alegacao("A001", 0.0, 120.0)], 300.0)
    assert js[0]["sai_s"] - js[0]["entra_s"] <= cfg.CARD_DURACAO_MAX_S + 1e-6


def test_atraso_do_fim_e_zero_quando_o_card_entra_durante_a_fala():
    """Os dois atrasos medem coisas diferentes, e é o segundo que importa para o espectador:
    um card que entra durante uma frase longa não está atrasado."""
    js = _janelas([alegacao("A001", 0.0, 30.0)], 300.0)
    assert js[0]["atraso_s"] == 0.0
    assert js[0]["atraso_do_fim_s"] == 0.0


def test_atraso_do_fim_cresce_quando_a_fila_empurra():
    itens = [alegacao("A001", 0.0, 1.0), alegacao("A002", 0.0, 1.0), alegacao("A003", 0.0, 1.0)]
    js = _janelas(itens, 300.0)
    assert js[0]["atraso_do_fim_s"] == 0.0
    assert js[2]["atraso_do_fim_s"] > js[1]["atraso_do_fim_s"] > 0.0


def test_ordem_cronologica_preservada():
    itens = [alegacao("A003", 30.0, 31.0), alegacao("A001", 10.0, 11.0),
             alegacao("A002", 20.0, 21.0)]
    js = _janelas(itens, 300.0)
    assert [j["id"] for j in js] == ["A001", "A002", "A003"]
