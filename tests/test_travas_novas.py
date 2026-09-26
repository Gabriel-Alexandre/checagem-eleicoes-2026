"""As travas acrescentadas na versão 0.2.0, cada uma provada sobre uma cópia do caso real.

Cada teste pega o caso publicado, que passa no validador, estraga UMA coisa e confere que a
porta fecha. É o jeito mais honesto de provar uma trava: mostrar o defeito que ela pega.
"""

from __future__ import annotations

import json
import shutil

import pytest

from checagem import config as cfg
from checagem.passo8_validar import anos_de, validar

SLUG = "2026-08-27-sabatina-lula-globo"
RECORTE = "bloco-contas-publicas"

pytestmark = pytest.mark.skipif(not (cfg.CASOS / SLUG).exists(), reason="caso de exemplo ausente")


@pytest.fixture
def caso(tmp_path, monkeypatch):
    """Uma cópia do caso real num diretório temporário, sem cartelas desenhadas."""
    destino = tmp_path / SLUG
    shutil.copytree(cfg.CASOS / SLUG, destino,
                    ignore=shutil.ignore_patterns("cartelas*", "render", "*.mp4", "*.wav"))
    monkeypatch.setattr(cfg, "CASOS", tmp_path)
    return destino


def ler(caso, rel):
    return json.loads((caso / rel).read_text(encoding="utf-8"))


def gravar(caso, rel, dados):
    (caso / rel).write_text(json.dumps(dados, ensure_ascii=False, indent=2), encoding="utf-8")


def checagens(caso):
    return ler(caso, f"checagens/checagens-{RECORTE}.json")


def alegacoes(caso):
    return ler(caso, f"alegacoes/alegacoes-{RECORTE}.json")


# ─────────────────────────────────────────────────────────────────────


def test_clone_limpo_sem_cartelas_passa(caso, capsys):
    """🔧 O defeito que deixou a CI vermelha desde o primeiro commit: num clone limpo as
    cartelas não existem (são derivadas e fora do git), e a porta fechava para todo mundo."""
    assert validar(SLUG, recorte=RECORTE) == 0
    assert "cartelas ainda não desenhadas" in capsys.readouterr().out


def test_pasta_de_cartelas_incompleta_reprova(caso):
    pasta = caso / "overlay" / f"cartelas-{RECORTE}"
    pasta.mkdir()
    (pasta / "A001.png").write_bytes(b"x")
    assert validar(SLUG, recorte=RECORTE) == 1


def test_plano_com_veredito_velho_reprova(caso, capsys):
    """Um veredito mudado depois do PASSO 6 deixaria a moldura com a cor antiga no vídeo."""
    dados = checagens(caso)
    alvo = next(c for c in dados["checagens"] if c["veredito"] == "VERDADEIRO")
    alvo["veredito"] = "IMPRECISO"
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1
    assert "cor errada" in capsys.readouterr().out


def test_travessao_no_resumo_reprova(caso):
    dados = checagens(caso)
    dados["checagens"][0]["resumo"] = "A dívida passou de R$ 10 trilhões — segundo o Banco Central"
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1


def test_leitura_de_intencao_na_ressalva_reprova(caso):
    dados = checagens(caso)
    dados["checagens"][0]["ressalva"] = "O candidato sabia que o número era outro."
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1


def test_numero_sem_data_de_referencia_reprova(caso):
    dados = checagens(caso)
    dados["checagens"][0]["data_de_referencia"] = None      # A001 é valor_monetario
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1


def test_alegacao_fora_da_cobertura_reprova(caso):
    """A cobertura prova que a varredura não escolheu trechos. Alegação fora dela é pesca."""
    dados = alegacoes(caso)
    dados["cobertura"]["inicio_s"] = dados["alegacoes"][1]["inicio_s"]
    gravar(caso, f"alegacoes/alegacoes-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1


def test_citacao_card_parafraseada_reprova(caso):
    dados = alegacoes(caso)
    dados["alegacoes"][0]["citacao_card"] = "a dívida no seu governo passou de 10 trilhões"
    gravar(caso, f"alegacoes/alegacoes-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 1


def test_citacao_card_literal_passa(caso):
    dados = alegacoes(caso)
    dados["alegacoes"][0]["citacao_card"] = "a dívida pública no seu governo ultrapassou os 10 trilhões"
    gravar(caso, f"alegacoes/alegacoes-{RECORTE}.json", dados)
    assert validar(SLUG, recorte=RECORTE) == 0


def test_ano_inventado_no_resumo_vira_aviso(caso, capsys):
    """🔧 O conserto do "desde 1986": ano na tela também precisa de lastro."""
    dados = checagens(caso)
    alvo = next(c for c in dados["checagens"] if c["id"] == "A011")
    alvo["resumo"] = "O IBGE fechou 2010 com 7,5%, a maior taxa desde 1986"
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    validar(SLUG, recorte=RECORTE)
    assert "o ano 1986 aparece em resumo" in capsys.readouterr().out


def test_numero_na_ressalva_sem_lastro_vira_aviso(caso, capsys):
    dados = checagens(caso)
    dados["checagens"][0]["ressalva"] = "No conceito do Tesouro, o estoque era R$ 7,77 trilhões."
    gravar(caso, f"checagens/checagens-{RECORTE}.json", dados)
    validar(SLUG, recorte=RECORTE)
    assert "'777' aparece em ressalva" in capsys.readouterr().out


# ─────────────────────────────────────────────────────────────────────


def test_anos_de_pega_ano_e_ignora_valor():
    assert anos_de("a maior taxa desde 1986") == {"1986"}
    assert anos_de("entre 2003 e 2010") == {"2003", "2010"}
    assert anos_de("R$ 1.986,50") == set()
    assert anos_de("G2023") == set()
