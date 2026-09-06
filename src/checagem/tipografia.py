"""Tipografia — carregar a Inter variável e quebrar texto por largura real.

⚠️ Quebrar texto por contagem de caracteres é o defeito clássico: "R$ 1.900.000.000,00"
ocupa o dobro de "aaaaaaaaaaaaaaaaaaa" com a mesma contagem. Aqui a quebra é medida em
pixels, com a própria fonte que vai desenhar.
"""

from __future__ import annotations

from functools import lru_cache

from PIL import ImageFont

from . import config as cfg
from .util import ErroDeExecucao


@lru_cache(maxsize=64)
def fonte(tamanho: int, peso: str = "Regular", *, italico: bool = False) -> ImageFont.FreeTypeFont:
    """Carrega a Inter no peso pedido.

    ⚠️ Os nomes das instâncias mudam entre o arquivo reto e o itálico: o reto tem 'Regular' e
    'SemiBold', o itálico tem 'Italic' e 'SemiBold Italic'. Pedir 'Regular' no arquivo itálico
    levanta ValueError, e foi assim que este projeto descobriu a diferença. A tradução é feita
    aqui, num lugar só, para quem chama continuar pedindo o peso pelo nome que conhece.
    """
    caminho = cfg.FONTE_SANS_ITALICO if italico else cfg.FONTE_SANS
    if not caminho.exists():
        raise ErroDeExecucao(
            f"fonte não encontrada: {caminho}\n"
            "  Rode:  python -m checagem ativos baixar-fontes"
        )
    f = ImageFont.truetype(str(caminho), tamanho)

    alvo = peso
    if italico:
        alvo = "Italic" if peso == "Regular" else f"{peso} Italic"

    try:
        disponiveis = [n.decode() for n in f.get_variation_names()]
    except OSError as e:  # Pillow sem suporte a fonte variável
        raise ErroDeExecucao(
            f"esta instalação do Pillow não abre fonte variável: {e}\n"
            "  Atualize com:  pip install -U Pillow"
        ) from e

    if alvo not in disponiveis:
        raise ErroDeExecucao(
            f"peso '{alvo}' não existe em {caminho.name}. Disponíveis: {disponiveis}"
        )
    f.set_variation_by_name(alvo)
    return f


def largura(texto: str, f: ImageFont.FreeTypeFont) -> float:
    return f.getlength(texto)


def quebrar(texto: str, f: ImageFont.FreeTypeFont, largura_max: float,
            *, max_linhas: int | None = None) -> list[str]:
    """Quebra por palavra, medindo em pixels. Corta com reticências se estourar max_linhas."""
    palavras = texto.split()
    linhas: list[str] = []
    atual = ""

    for p in palavras:
        tentativa = f"{atual} {p}".strip()
        if f.getlength(tentativa) <= largura_max or not atual:
            atual = tentativa
        else:
            linhas.append(atual)
            atual = p
    if atual:
        linhas.append(atual)

    if max_linhas is not None and len(linhas) > max_linhas:
        linhas = linhas[:max_linhas]
        ultima = linhas[-1]
        while ultima and f.getlength(ultima + "…") > largura_max:
            ultima = ultima[:-1].rstrip()
        linhas[-1] = ultima + "…"
    return linhas


def altura_da_linha(f: ImageFont.FreeTypeFont, entrelinha: float = 1.30) -> int:
    ascent, descent = f.getmetrics()
    return int(round((ascent + descent) * entrelinha))
