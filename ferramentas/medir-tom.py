"""Mede a frequência fundamental (F0) média de cada segmento da transcrição.

**Para que serve:** ajudar a escrever `transcricao/falantes.json` no PASSO 3.

Numa sabatina com dois entrevistadores de vozes agudas e graves distintas, o tom separa os
turnos de pergunta em segundos — trabalho que, no olho, custa dezenas de quadros extraídos.

> 🔴 **Isto NÃO é diarização, e não decide nada sozinho.** É uma pista, medida e auditável, que
> entra junto com as pistas do texto (quem é chamado pelo nome, quem faz a pergunta, quem
> responde). A atribuição continua sendo escrita à mão e revisada — ver
> [`docs/ARQUITETURA.md` §3](../docs/ARQUITETURA.md).
>
> ⚠️ O tom **não** separa duas pessoas do mesmo registro vocal. Se os dois entrevistadores forem
> ambos graves, esta ferramenta não ajuda, e o script avisa quando a distribuição não tem dois
> grupos separáveis.

Método: autocorrelação por quadro de 40 ms, com janela de Hann, apenas em quadros com energia
acima de um piso. F0 do segmento é a **mediana** dos quadros vozeados, que é robusta a oitava
errada num quadro isolado.

Uso:
    python ferramentas/medir-tom.py <slug> [--recorte ID] [--limite 165]

Requer `numpy` (não é dependência do pipeline; só desta ferramenta).
"""

from __future__ import annotations

import argparse
import json
import sys
import wave
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[1]

F0_MIN, F0_MAX = 70.0, 320.0
QUADRO_S = 0.040
PASSO_S = 0.020
PISO_RMS = 0.012


def ler_wav(caminho: Path) -> tuple[object, int]:
    import numpy as np

    with wave.open(str(caminho), "rb") as w:
        if w.getsampwidth() != 2:
            raise SystemExit(f"{caminho.name}: esperado PCM 16 bits, veio {w.getsampwidth() * 8}")
        canais, taxa, n = w.getnchannels(), w.getframerate(), w.getnframes()
        dados = np.frombuffer(w.readframes(n), dtype="<i2").astype("float32") / 32768.0
    if canais > 1:
        dados = dados.reshape(-1, canais).mean(axis=1)
    return dados, taxa


def f0_do_trecho(sinal, taxa: int) -> float | None:
    """Mediana da F0 dos quadros vozeados. None quando não há quadro vozeado suficiente."""
    import numpy as np

    n_quadro = int(QUADRO_S * taxa)
    n_passo = int(PASSO_S * taxa)
    if len(sinal) < n_quadro * 2:
        return None

    lag_min = int(taxa / F0_MAX)
    lag_max = int(taxa / F0_MIN)
    janela = np.hanning(n_quadro).astype("float32")
    achados: list[float] = []

    for inicio in range(0, len(sinal) - n_quadro, n_passo):
        q = sinal[inicio:inicio + n_quadro]
        rms = float(np.sqrt(np.mean(q * q)))
        if rms < PISO_RMS:
            continue
        q = (q - q.mean()) * janela
        ac = np.correlate(q, q, mode="full")[n_quadro - 1:]
        if ac[0] <= 0:
            continue
        ac = ac / ac[0]
        faixa = ac[lag_min:lag_max]
        if faixa.size == 0:
            continue
        pico = int(np.argmax(faixa)) + lag_min
        # Um pico fraco é ruído, não voz; e sem isso o silêncio vira "F0".
        if ac[pico] < 0.30:
            continue
        achados.append(taxa / pico)

    if len(achados) < 5:
        return None
    return float(np.median(achados))


def main() -> int:
    p = argparse.ArgumentParser(description="Mede F0 por segmento, para ajudar a escrever falantes.json")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    p.add_argument("--limite", type=float, default=165.0,
                   help="Hz acima do qual o segmento é marcado como voz aguda (padrão 165)")
    p.add_argument("--saida", default=None, help="arquivo TSV; padrão é imprimir na tela")
    args = p.parse_args()

    try:
        import numpy  # noqa: F401
    except ImportError:
        raise SystemExit("esta ferramenta precisa de numpy:  pip install numpy") from None

    caso = RAIZ / "casos" / args.slug
    nome = f"transcricao-{args.recorte}" if args.recorte else "transcricao"
    transcricao = json.loads((caso / "transcricao" / f"{nome}.json").read_text(encoding="utf-8"))

    if args.recorte:
        wav = caso / "recortes" / f"{args.recorte}.wav"
        indice = json.loads((caso / "recortes" / "RECORTES.json").read_text(encoding="utf-8"))
        base = float(next(r for r in indice["recortes"] if r["id"] == args.recorte)["origem_inicio_s"])
    else:
        wav = next(iter(sorted((caso / "fonte").glob("*.wav"))), None)
        base = 0.0
    if wav is None or not wav.exists():
        raise SystemExit("não há WAV. Rode:  python -m checagem midia <slug> audio")

    print(f"lendo {wav.name} ...", file=sys.stderr)
    sinal, taxa = ler_wav(wav)

    linhas = ["tempo\tinicio_s\tf0_hz\tvoz\ttexto"]
    medidos: list[float] = []
    for s in transcricao["segmentos"]:
        a = int((s["inicio_s"] - base) * taxa)
        b = int((s["fim_s"] - base) * taxa)
        f0 = f0_do_trecho(sinal[max(0, a):max(0, b)], taxa) if b > a else None
        marca = "?" if f0 is None else ("AGUDA" if f0 >= args.limite else "GRAVE")
        if f0 is not None:
            medidos.append(f0)
        hh = int(s["inicio_s"])
        linhas.append(
            f"{hh // 3600:02d}:{(hh % 3600) // 60:02d}:{hh % 60:02d}\t{s['inicio_s']:.2f}\t"
            f"{'' if f0 is None else f'{f0:.0f}'}\t{marca}\t{s['texto']}"
        )

    saida = "\n".join(linhas)
    if args.saida:
        Path(args.saida).write_text(saida + "\n", encoding="utf-8", newline="\n")
        print(f"escrito em {args.saida}", file=sys.stderr)
    else:
        print(saida)

    if medidos:
        import numpy as np
        arr = np.array(medidos)
        acima = int((arr >= args.limite).sum())
        print(
            f"\n{len(medidos)} segmentos medidos · mediana {np.median(arr):.0f} Hz · "
            f"{acima} agudos ({acima / len(arr) * 100:.0f}%) · {len(arr) - acima} graves",
            file=sys.stderr,
        )
        if acima == 0 or acima == len(arr):
            print("⚠️ tudo caiu de um lado só do limite: o tom NÃO separa as vozes desta peça. "
                  "Não use esta pista aqui.", file=sys.stderr)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
