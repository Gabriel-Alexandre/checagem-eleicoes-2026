"""Constantes do projeto.

⛔ Este é o único lugar onde cor, fonte, medida de tela e nome de arquivo se definem.
Número mágico espalhado pelo código é como duas réguas: mais cedo ou mais tarde elas divergem.

Dono da doutrina que estas constantes implementam:
  - vereditos e cores ......... docs/METODOLOGIA.md §2
  - desenho do card ........... docs/IDENTIDADE_VISUAL.md
"""

from __future__ import annotations

import sys
from dataclasses import dataclass
from pathlib import Path

# O console do Windows nasce em cp1252 e morre num print de emoji.
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")
if hasattr(sys.stderr, "reconfigure"):
    sys.stderr.reconfigure(encoding="utf-8")


# ─────────────────────────────────────────────────────────────────────
# Caminhos
# ─────────────────────────────────────────────────────────────────────

RAIZ = Path(__file__).resolve().parents[2]
CASOS = RAIZ / "casos"
ESQUEMAS = RAIZ / "esquemas"
ATIVOS = RAIZ / "ativos"
FONTES_DIR = ATIVOS / "fontes"

FONTE_SANS = FONTES_DIR / "Inter-VariableFont.ttf"
FONTE_SANS_ITALICO = FONTES_DIR / "Inter-Italic-VariableFont.ttf"


def pasta_do_caso(slug: str) -> Path:
    return CASOS / slug


# ─────────────────────────────────────────────────────────────────────
# Vereditos — docs/METODOLOGIA.md §2
# ─────────────────────────────────────────────────────────────────────


@dataclass(frozen=True)
class Veredito:
    chave: str
    rotulo: str          # o que aparece no badge do card
    cor: str             # hex, cor da moldura e do badge
    cor_texto: str       # cor do texto dentro do badge
    familia: str         # verde | amarelo | laranja | vermelho | cinza
    exige_fontes: int    # mínimo de fontes para o veredito ser válido


VEREDITOS: dict[str, Veredito] = {
    "VERDADEIRO": Veredito(
        "VERDADEIRO", "VERDADEIRO", "#12A150", "#FFFFFF", "verde", 2
    ),
    "IMPRECISO": Veredito(
        "IMPRECISO", "IMPRECISO", "#E5A50A", "#1A1200", "amarelo", 2
    ),
    "INSUSTENTAVEL": Veredito(
        "INSUSTENTAVEL", "SEM COMPROVAÇÃO", "#E8590C", "#FFFFFF", "laranja", 2
    ),
    "FALSO": Veredito(
        "FALSO", "FALSO", "#D62828", "#FFFFFF", "vermelho", 2
    ),
    "NAO_CHECAVEL": Veredito(
        "NAO_CHECAVEL", "NÃO CHECÁVEL", "#6B7280", "#FFFFFF", "cinza", 0
    ),
}

# Vereditos que uma alegação marcada como `checavel: false` pode receber.
VEREDITOS_DE_NAO_CHECAVEL = {"NAO_CHECAVEL"}

TIPOS_NAO_CHECAVEIS = {
    "opiniao",
    "promessa",
    "previsao",
    "juizo_de_valor",
    "hipotese",
}

NIVEIS_DE_FONTE = ("N1", "N2", "N3", "N4")
NIVEIS_FORTES = ("N1", "N2")

# Tipos que exigem pelo menos uma fonte N1 ou N2 (METODOLOGIA §3.1 regra 1).
TIPOS_QUE_EXIGEM_FONTE_FORTE = {
    "numero",
    "serie_historica",
    "valor_monetario",
    "ranking",
    "comparacao",
}


# ─────────────────────────────────────────────────────────────────────
# Tela — docs/IDENTIDADE_VISUAL.md
# ─────────────────────────────────────────────────────────────────────

LARGURA = 1920
ALTURA = 1080
FPS_SAIDA = 30

# Moldura: a cor do veredito em volta do quadro inteiro.
MOLDURA_ESPESSURA = 10

# Card inferior.
CARD_MARGEM_X = 64
CARD_MARGEM_INFERIOR = 56
CARD_LARGURA = LARGURA - 2 * CARD_MARGEM_X          # 1792
CARD_RAIO = 22
CARD_BARRA = 14                                      # faixa colorida à esquerda
CARD_PADDING_X = 34
CARD_PADDING_Y = 26
CARD_FUNDO = (13, 16, 22, 240)
CARD_BORDA = (255, 255, 255, 36)

COR_TEXTO = "#F5F7FA"
COR_TEXTO_FRACO = "#A8B0BD"
COR_CITACAO = "#D5DBE5"

TAM_BADGE = 30
TAM_META = 25
TAM_CITACAO = 33
TAM_RESUMO = 40
TAM_FONTES = 24

# Selo permanente no canto superior direito.
SELO_TEXTO = "CHECAGEM ABERTA"
SELO_SUBTEXTO = "metodologia e fontes no repositório"

# ─────────────────────────────────────────────────────────────────────
# Tempo de tela
# ─────────────────────────────────────────────────────────────────────

# Quanto o card continua depois de a frase acabar, para dar tempo de ler.
PERMANENCIA_S = 4.0
# Piso e teto de duração de um card.
CARD_DURACAO_MIN_S = 3.0
CARD_DURACAO_MAX_S = 14.0
# Folga entre um card e o próximo, para não haver dois na tela.
FOLGA_ENTRE_CARDS_S = 0.20
# Quanto uma cartela pode entrar DEPOIS DE A FRASE ACABAR, quando a fila empurra.
# Acima disso o espectador já não liga o card à fala, e o PASSO 6 avisa.
ATRASO_MAX_S = 12.0
# Fade de entrada e saída do card.
FADE_S = 0.25

# Cartela de legenda no começo do vídeo.
LEGENDA_DURACAO_S = 7.0
