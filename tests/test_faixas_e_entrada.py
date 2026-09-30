"""Faixas pretas cortadas e entrada das cartelas com fade (30/set/2026).

Cada teste trava um defeito que o padrão de 29/set apontou: borda preta à mostra no quadro final,
texto do card sobre o vídeo, elemento que entra sem animação.
"""

from __future__ import annotations

from checagem import config as cfg
from checagem.passo1_midia import caixa_sem_faixas
from checagem.passo7_renderizar import _grafo, _linhas_de_som, _sobreposicoes


def test_caixa_da_sabatina_de_flavio_fica_dentro_da_imagem():
    """🔴 O caso real: 1920x886, imagem de x=172 a x=1747 (a borda tem 3 a 4 colunas de cinza).

    A caixa tem que começar depois da borda mole e ser 16:9 exata, para a escala a 1920x1080
    não deformar nada.
    """
    c = caixa_sem_faixas(1920, 886, 172, 1747, 0, 885)
    assert c == {"x": 176, "y": 2, "w": 1568, "h": 882}
    assert c["w"] * 9 == c["h"] * 16
    assert c["x"] > 172 and c["x"] + c["w"] - 1 < 1747


def test_sem_faixa_nao_perde_nenhum_pixel():
    """A borda do próprio arquivo não é mole: sem barra, a margem não se aplica."""
    assert caixa_sem_faixas(1920, 1080, 0, 1919, 0, 1079) == {"x": 0, "y": 0, "w": 1920, "h": 1080}


def test_caixa_e_sempre_par():
    for x1, x2 in ((101, 1180), (99, 1178), (7, 1270)):
        c = caixa_sem_faixas(1280, 720, x1, x2, 0, 719)
        assert all(v % 2 == 0 for v in c.values()), c


def plano(**extra):
    base = {
        "selo": {"arquivo": "overlay/_selo.png", "entra_s": 0.0, "sai_s": 100.0},
        "legenda": {"arquivo": "overlay/_legenda.png", "entra_s": 0.5, "sai_s": 7.5},
        "cartelas": [
            {"id": "A001", "arquivo": "overlay/A001.png", "entra_s": 8.0, "sai_s": 14.0},
            {"id": "A002", "arquivo": "overlay/A002.png", "entra_s": 20.0, "sai_s": 26.0},
        ],
        "congelamento": {"duracao_s": 0.0},
        "encerramento": None,
    }
    base.update(extra)
    return base


def test_cartela_e_legenda_entram_com_fade_e_o_selo_nao():
    linhas, saida = _grafo(plano(), True)
    fades = [ln for ln in linhas if "fade=t=in" in ln]
    assert len(fades) == 3          # legenda + 2 cartelas
    assert all(f"d={cfg.ENTRADA_FADE_S}" in ln and "alpha=1" in ln for ln in fades)
    selo = next(ln for ln in linhas if ln.startswith("[0:v][1:v]overlay"))
    assert "eof_action=repeat" in selo and "fade" not in selo
    assert saida == "v4"


def test_fade_comeca_no_quadro_em_que_a_cartela_entra():
    """O `setpts` desloca a entrada em laço para o segundo certo; sem ele o fade rodaria no zero."""
    linhas, _ = _grafo(plano(), True)
    a001 = next(ln for ln in linhas if ln.startswith("[3:v]format=rgba"))
    assert "setpts=PTS+8.000/TB" in a001
    sobreposicao = next(ln for ln in linhas if "[c3]overlay" in ln)
    assert "between(t,8.000,14.000)" in sobreposicao and "eof_action=pass" in sobreposicao


def test_oito_quadros_a_trinta_por_segundo():
    assert abs(cfg.ENTRADA_FADE_S * cfg.FPS_SAIDA - 8) < 0.02


def test_card_selo_e_legenda_sao_opacos():
    """🔴 Nada do vídeo por baixo do texto: o fundo do card é opaco, não 94%."""
    from checagem.passo6_overlay import desenhar_cartela, desenhar_legenda, desenhar_selo

    assert cfg.CARD_FUNDO[3] == 255
    card = desenhar_cartela(veredito_chave="VERDADEIRO", falante="A", tempo_s=1.0,
                            id_alegacao="A001", frase="uma frase", resumo="um resumo",
                            ressalva=None, fontes=[])
    # um pixel no meio do card, longe de texto: alfa cheio
    y = cfg.ALTURA - cfg.CARD_MARGEM_INFERIOR - 10
    assert card.getpixel((cfg.LARGURA // 2, y))[3] == 255
    selo = desenhar_selo()
    assert selo.getpixel((cfg.LARGURA - cfg.CARD_MARGEM_X - 8, 50))[3] == 255
    legenda = desenhar_legenda("Título", "Sub")
    assert legenda.getpixel((cfg.LARGURA // 2, cfg.ALTURA // 2 + 250))[3] == 255


def test_som_de_entrada_so_nas_cartelas_que_entram():
    linhas, rotulo = _linhas_de_som(plano(), True)
    assert rotulo == "[aout]"
    assert sum("sine=" in ln for ln in linhas) == len(
        [e for e in _sobreposicoes(plano(), True) if e["entra"]])   # 3, não 4: o selo não entra
    assert "normalize=0" in linhas[-1] and "duration=first" in linhas[-1]
    assert any("adelay=8000|8000" in ln for ln in linhas)


def test_canto_esquerdo_do_card_nao_tem_quina_reta():
    """🔧 O corpo escuro era um retângulo de quina reta sobre a faixa colorida, e a quina saía do
    arredondamento como um degrau de alguns pixels. Agora o pixel da quina superior esquerda do
    corpo, fora da curva, é transparente."""
    from checagem.passo6_overlay import desenhar_cartela

    card = desenhar_cartela(veredito_chave="VERDADEIRO", falante="A", tempo_s=1.0,
                            id_alegacao="A001", frase="f", resumo="r", ressalva=None, fontes=[])
    # a caixa é a mais baixa possível: procura a primeira linha com pixel opaco na coluna do corpo
    x_corpo = cfg.CARD_MARGEM_X + cfg.CARD_BARRA + 2
    topo = next(y for y in range(cfg.ALTURA) if card.getpixel((x_corpo, y))[3] == 255)
    x_barra = cfg.CARD_MARGEM_X + 2
    topo_barra = next(y for y in range(cfg.ALTURA) if card.getpixel((x_barra, y))[3] == 255)
    # a faixa é arredondada e o corpo ali é reto (corners só à direita): o corpo não pode
    # começar acima da faixa
    assert topo >= topo_barra - 1
