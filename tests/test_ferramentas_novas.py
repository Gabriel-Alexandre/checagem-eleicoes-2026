"""As peças novas da 0.2.0 que não dependem de caso: enquadramento, conferência de trecho,
data legível e o subtítulo da legenda.
"""

from __future__ import annotations

import sys
from importlib import import_module
from pathlib import Path

from checagem import config as cfg
from checagem.passo1_midia import _filtro_de_enquadramento
from checagem.passo8_validar import valores_de
from checagem.util import data_legivel

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ferramentas"))
ct = import_module("conferir-trechos")


# ─────────────────────────────────────────────────────────────────────
# Enquadramento
# ─────────────────────────────────────────────────────────────────────


def test_video_ja_no_quadro_nao_e_mexido():
    assert _filtro_de_enquadramento(cfg.LARGURA, cfg.ALTURA) is None


def test_video_vertical_entra_inteiro_sem_corte():
    """A imagem original é escalada para caber na altura, nunca cortada: o corte só vale para
    o fundo desfocado, que é cópia."""
    f = _filtro_de_enquadramento(720, 1280)
    assert f is not None
    frente = f.split("[frente]scale")[1].split("[frente2]")[0]
    assert "force_original_aspect_ratio=decrease" in frente
    assert "crop" not in frente


# ─────────────────────────────────────────────────────────────────────
# Conferência de trecho contra a captura
# ─────────────────────────────────────────────────────────────────────


PAGINA = ("Em 2022, o Produto Interno Bruto (PIB) atingiu R$ 10,1 trilhões, crescimento de 3,0% ante 2021. "
          "Outro parágrafo qualquer. O resultado foi puxado pelos serviços.")


def test_trecho_literal_e_encontrado():
    assert ct.conferir("o Produto Interno Bruto (PIB) atingiu R$ 10,1 trilhões", PAGINA, "text/html")


def test_trecho_reescrito_nao_e_encontrado():
    """O defeito que a auditoria de 26/set achou no caso publicado: trecho reescrito em vez de
    copiado ("do PIB" onde a página diz "do Produto Interno Bruto (PIB)")."""
    assert not ct.conferir("o PIB atingiu R$ 10,1 trilhões", PAGINA, "text/html")


def test_corte_interno_confere_pedaco_a_pedaco():
    assert ct.conferir("crescimento de 3,0% ante 2021 [...] puxado pelos serviços", PAGINA, "text/html")


def test_json_confere_por_numero():
    api = '[{"data":"01/12/2022","valor":"71.68"},{"data":"01/06/2026","valor":"81.95"}]'
    assert ct.conferir('{"data":"01/06/2026","valor":"81.95"}', api, "application/json")
    assert not ct.conferir('{"data":"01/06/2026","valor":"81.93"}', api, "application/json")


def test_valor_revisto_e_distinguido_de_trecho_inventado():
    """81,93 virou 81,95 depois da consulta: é revisão da fonte, e a metodologia manda
    registrar as duas datas, não trocar o veredito. 60,00 no lugar de 81,95 não é revisão."""
    api = '[{"data":"01/06/2026","valor":"81.95"}]'
    assert ct.revisto('{"valor":"81.93"}', api)
    assert not ct.revisto('{"valor":"60.00"}', api)


# ─────────────────────────────────────────────────────────────────────
# Texto de tela
# ─────────────────────────────────────────────────────────────────────


def test_data_legivel():
    assert data_legivel("2026-08-27") == "27/ago/2026"
    assert data_legivel("não é data") == "não é data"


def test_subtitulo_nao_repete_o_veiculo():
    from checagem.passo6_overlay import subtitulo_da_legenda
    meta = {"titulo": "Sabatina de Fulano na TV Globo", "veiculo": "TV Globo", "data_do_evento": "2026-08-28"}
    assert subtitulo_da_legenda(meta) == "Sabatina de Fulano na TV Globo · 28/ago/2026"
    meta["titulo"] = "Sabatina de Fulano"
    assert subtitulo_da_legenda(meta) == "Sabatina de Fulano · TV Globo · 28/ago/2026"


def test_valores_de_le_formato_brasileiro():
    assert valores_de("R$ 10,81 trilhões") == [10.81]
    assert valores_de("1.234,5 e 94") == [1234.5, 94.0]


# ─────────────────────────────────────────────────────────────────────
# Fila de cards: tempo de leitura e congelamento final
# ─────────────────────────────────────────────────────────────────────


def test_tempo_de_leitura_cresce_com_o_texto_e_tem_piso_e_teto():
    from checagem.passo6_overlay import tempo_de_leitura
    curto = tempo_de_leitura({"resumo": "Confere com o STF", "ressalva": None})
    longo = tempo_de_leitura({"resumo": " ".join(["palavra"] * 20), "ressalva": " ".join(["x"] * 15)})
    assert curto == cfg.CARD_DURACAO_MIN_S
    assert cfg.CARD_DURACAO_MIN_S < longo <= cfg.CARD_DURACAO_MAX_S


def test_fila_nao_deixa_card_com_menos_que_o_tempo_de_leitura():
    """🔧 O defeito do caso Flávio: cinco alegações em 20s no fim do trecho saíam com 3s cada.
    Agora a fila corre para o congelamento final, e cada card fica o tempo de leitura."""
    from checagem.passo6_overlay import _janelas
    itens = [{"id": f"A{i:03d}", "inicio_s": 90.0 + i, "fim_s": 95.0 + i, "leitura_s": 7.0}
             for i in range(5)]
    janelas = _janelas(itens, 100.0 + cfg.CONGELAMENTO_MAX_S)
    assert all(j["sai_s"] - j["entra_s"] >= 7.0 - 0.001 for j in janelas)
    assert all(b["entra_s"] >= a["sai_s"] for a, b in zip(janelas, janelas[1:], strict=False))
    assert janelas[-1]["sai_s"] > 100.0          # passou do trecho: vira congelamento


def test_card_de_frase_longa_nao_segura_a_fila():
    from checagem.passo6_overlay import _janelas
    itens = [{"id": "A001", "inicio_s": 10.0, "fim_s": 30.0, "leitura_s": 5.0},
             {"id": "A002", "inicio_s": 12.0, "fim_s": 14.0, "leitura_s": 5.0}]
    a, b = _janelas(itens, 100.0)
    assert a["sai_s"] - a["entra_s"] == 5.0
    assert b["entra_s"] < 16.0
