"""CLI — uma porta só para os oito passos.

    python -m checagem <comando> [args]

⛔ Não há um comando "fazer tudo". Os passos 4 e 5 (extrair alegações e checar) são feitos por
uma IA seguindo as skills, e o passo 8 é uma revisão humana. Um botão de "roda sozinho" daria a
impressão de que existe checagem automática de ponta a ponta neste repositório. Não existe, e
fingir que existe é o oposto do que o projeto defende.
"""

from __future__ import annotations

import sys

from . import config as cfg  # noqa: F401  (reconfigura o stdout para UTF-8)
from .util import ErroDeExecucao, erro

AJUDA = """
checagem — pipeline de checagem de fatos em vídeo

  midia <slug> registrar                    PASSO 1 · assina e mede o vídeo de origem
  midia <slug> audio [--recorte ID]         PASSO 1 · extrai WAV 16 kHz mono
  midia <slug> recortar ID --inicio S --duracao S [--motivo "..."]
                                            PASSO 1 · corta um trecho

  transcrever <slug> [--recorte ID] [--modelo M] [--threads N]
                                            PASSO 2 · whisper.cpp local
  falantes <slug> [--recorte ID]            PASSO 3 · aplica transcricao/falantes.json

  ── PASSO 4 e 5 são feitos pela IA, seguindo skills/extrair-alegacoes.md
     e skills/checar-alegacao.md. Não há comando: eles são julgamento, não script. ──

  overlay <slug> [--recorte ID]             PASSO 6 · desenha as cartelas
  renderizar <slug> [--recorte ID]          PASSO 7 · queima o overlay no vídeo
  validar <slug> [--recorte ID]             PASSO 8 · a porta (sai 1 se achar erro)

  relatorio <slug> [--recorte ID]           gera o RELATORIO.md do caso
  ativos baixar-fontes                      baixa a Inter (OFL)

Documentação: docs/METODOLOGIA.md · docs/REPLICAR.md · ESTADO.md
"""


def main(argv: list[str] | None = None) -> int:
    argv = list(sys.argv[1:] if argv is None else argv)
    if not argv or argv[0] in ("-h", "--help", "ajuda"):
        print(AJUDA)
        return 0

    comando, resto = argv[0], argv[1:]
    try:
        if comando == "midia":
            from .passo1_midia import main as m
            # a subação vem depois do slug: midia <slug> <acao>
            return m(resto)
        if comando == "transcrever":
            from .passo2_transcrever import main as m
            return m(resto)
        if comando == "falantes":
            from .passo3_falantes import main as m
            return m(resto)
        if comando == "overlay":
            from .passo6_overlay import main as m
            return m(resto)
        if comando == "renderizar":
            from .passo7_renderizar import main as m
            return m(resto)
        if comando == "validar":
            from .passo8_validar import main as m
            return m(resto)
        if comando == "relatorio":
            from .relatorio import main as m
            return m(resto)
        if comando == "ativos":
            from .ativos import main as m
            return m(resto)
    except ErroDeExecucao as e:
        erro(str(e))
        return 1
    except KeyboardInterrupt:
        erro("interrompido")
        return 130

    erro(f"comando desconhecido: {comando}")
    print(AJUDA)
    return 2


if __name__ == "__main__":
    raise SystemExit(main())
