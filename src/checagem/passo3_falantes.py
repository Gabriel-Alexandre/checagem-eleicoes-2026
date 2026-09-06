"""PASSO 3 — atribuir falante.

O whisper.cpp não separa vozes. Diarização automática, nas versões que rodam offline hoje,
erra justamente onde dói: na virada de turno, que é onde uma frase muda de dono.

Numa sabatina, porém, o turno é óbvio na leitura — pergunta e resposta se alternam. Então a
atribuição é **escrita à mão** (por uma pessoa, ou por uma IA que leu a transcrição e conferiu
no vídeo) num arquivo de turnos, e este script **aplica** esse arquivo.

🔴 Por que isso é melhor do que um diarizador silencioso: atribuir uma frase à pessoa errada é
o pior erro possível neste projeto — pior do que errar o veredito, porque coloca na boca de
alguém algo que a pessoa não disse. Um arquivo de turnos é auditável linha a linha; um vetor
de embedding não é.

Formato de `transcricao/falantes.json`:

    {
      "caso": "...",
      "turnos": [
        { "inicio_s": 0.0,   "fim_s": 118.4, "falante": "César Tralli" },
        { "inicio_s": 118.4, "fim_s": 190.2, "falante": "Lula" }
      ]
    }

O segmento recebe o falante do turno que contém o seu **ponto médio**. Sobreposição de fala
(um cortando o outro) é resolvida por quem tem mais tempo dentro do segmento.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from . import config as cfg
from .util import (
    ErroDeExecucao,
    aviso,
    escrever_json,
    hms,
    info,
    ler_json,
    ok,
    passo,
)


def _papel_de(slug: str, nome: str) -> str:
    meta = ler_json(cfg.pasta_do_caso(slug) / "CASO.json")
    for f in meta["falantes"]:
        if f["nome"] == nome:
            return f["papel"]
    raise ErroDeExecucao(
        f"o falante '{nome}' aparece em falantes.json mas não em CASO.json.\n"
        "  Todo nome que sai na tela tem que estar declarado no caso, com papel."
    )


def aplicar(slug: str, *, recorte: str | None = None) -> Path:
    caso = cfg.pasta_do_caso(slug)
    nome = f"transcricao-{recorte}" if recorte else "transcricao"
    caminho = caso / "transcricao" / f"{nome}.json"
    turnos_path = caso / "transcricao" / "falantes.json"

    if not turnos_path.exists():
        raise ErroDeExecucao(
            f"não existe {turnos_path.relative_to(cfg.RAIZ)}.\n"
            "  Escreva os turnos lendo a transcrição: numa sabatina a virada é evidente.\n"
            "  Ver o cabeçalho deste arquivo para o formato."
        )

    transcricao = ler_json(caminho)
    turnos = sorted(ler_json(turnos_path)["turnos"], key=lambda t: t["inicio_s"])
    passo(f"PASSO 3 · atribuir falante — {len(turnos)} turnos sobre {len(transcricao['segmentos'])} segmentos")

    # Sobreposição entre turnos é erro de escrita, não ambiguidade a resolver.
    for a, b in zip(turnos, turnos[1:], strict=False):
        if b["inicio_s"] < a["fim_s"] - 0.001:
            raise ErroDeExecucao(
                f"turnos se sobrepõem: '{a['falante']}' até {hms(a['fim_s'])} e "
                f"'{b['falante']}' a partir de {hms(b['inicio_s'])}"
            )

    papeis = {t["falante"]: _papel_de(slug, t["falante"]) for t in turnos}

    sem_dono = 0
    for s in transcricao["segmentos"]:
        meio = (s["inicio_s"] + s["fim_s"]) / 2
        escolhido = None
        melhor_sobreposicao = 0.0
        for t in turnos:
            if t["inicio_s"] <= meio < t["fim_s"]:
                escolhido = t["falante"]
                break
            sobrepoe = min(s["fim_s"], t["fim_s"]) - max(s["inicio_s"], t["inicio_s"])
            if sobrepoe > melhor_sobreposicao:
                melhor_sobreposicao, escolhido = sobrepoe, t["falante"]
        if escolhido is None:
            sem_dono += 1
        s["falante"] = escolhido
        s["papel"] = papeis.get(escolhido)

    if sem_dono:
        aviso(f"{sem_dono} segmentos ficaram sem falante — os turnos não cobrem a peça inteira")
    else:
        ok("todos os segmentos têm falante")

    contagem: dict[str, float] = {}
    for s in transcricao["segmentos"]:
        contagem[s["falante"] or "—"] = contagem.get(s["falante"] or "—", 0.0) + (s["fim_s"] - s["inicio_s"])
    for quem, seg in sorted(contagem.items(), key=lambda kv: -kv[1]):
        info(f"{quem:<28} {hms(seg)}  ({seg / max(1, sum(contagem.values())) * 100:4.1f}%)")

    escrever_json(caminho, transcricao)
    ok(f"{caminho.relative_to(cfg.RAIZ)} atualizado")
    return caminho


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem falantes", description="PASSO 3 — atribuir falante")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    args = p.parse_args(argv)
    aplicar(args.slug, recorte=args.recorte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
