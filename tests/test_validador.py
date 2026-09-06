"""As travas do validador, que são a doutrina escrita em código.

⛔ Se um destes testes precisar ser afrouxado para um caso passar, o problema é o caso.
"""

from __future__ import annotations

from checagem.passo8_validar import normalizar, numeros_de

# ─────────────────────────────────────────────────────────────────────
# A trava da citação
# ─────────────────────────────────────────────────────────────────────


def test_citacao_literal_e_encontrada_na_transcricao():
    transcricao = normalizar("Eu herdei esse governo em janeiro de 2023 com déficit fiscal de 2,8%.")
    citacao = normalizar("Eu herdei esse governo em janeiro de 2023 com déficit fiscal de 2,8%.")
    assert citacao in transcricao


def test_citacao_parafraseada_e_recusada():
    """🔴 A trava mais importante do repositório. Um modelo de linguagem parafraseia sem
    perceber, e aspa parafraseada num vídeo de checagem é o defeito que o projeto combate."""
    transcricao = normalizar("Eu herdei esse governo em janeiro de 2023 com déficit fiscal de 2,8%.")
    parafrase = normalizar("Herdei o governo em 2023 com um déficit fiscal de 2,8%.")
    assert parafrase not in transcricao


def test_normalizar_ignora_acento_e_pontuacao_mas_nao_palavra():
    assert normalizar("déficit, fiscal!") == normalizar("deficit fiscal")
    assert normalizar("superávit") != normalizar("deficit")


def test_corte_interno_marcado_confere_pedaco_a_pedaco():
    """Uma citação com [...] é conferida por partes: cada pedaço tem que existir."""
    transcricao = normalizar(
        "Você se esquece que eu deixei esse país crescendo 7,5% e quando eu voltei ele estava "
        "crescendo 1%, ele só cresceu 3%, sabe, em 2023, 2024, 2025."
    )
    frase = "Você se esquece que eu deixei esse país crescendo 7,5% e quando eu voltei ele estava [...] crescendo 1%"
    for parte in frase.split("[...]"):
        assert normalizar(parte) in transcricao


# ─────────────────────────────────────────────────────────────────────
# O lastro numérico
# ─────────────────────────────────────────────────────────────────────


def test_numeros_de_pega_quantidade():
    assert "1025" in numeros_de("alta de 10,25 pontos percentuais")
    assert "8193" in numeros_de("chegou a 81,93% do PIB")


def test_numeros_de_ignora_um_digito():
    assert numeros_de("cresceu 3% no ano") == set()


def test_numeros_de_ignora_ano():
    """Ano é data, não quantidade. Data se confere pelo campo data_de_referencia e pela
    própria fonte; incluí-la aqui só produziria ruído."""
    assert numeros_de("em 2023 e em 2024") == set()
    assert numeros_de("desde 1986") == set()


def test_numeros_de_ignora_digito_colado_em_letra():
    """'G20' é nome de grupo, não quantidade. 'PL2' e 'IPCA15' também."""
    assert numeros_de("os países do G20") == set()
    assert numeros_de("o IPCA15 de julho") == set()


def test_numeros_de_pega_ano_quando_ele_faz_parte_de_um_valor():
    """1986 sozinho é ano; 1.986,5 é quantidade."""
    assert numeros_de("R$ 1.986,50") == {"198650"}
