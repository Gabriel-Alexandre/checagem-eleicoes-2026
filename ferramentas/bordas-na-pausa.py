"""Leva as bordas de cada corte para a PAUSA da voz, e prova com a medida.

    python ferramentas/bordas-na-pausa.py <slug> [--recorte sabatina-completa] \\
        [--busca 0.8] [--limiar 12] [--conferir] [--so-medir]

🔑 Por que existe (validação final do caso de 15/out/2026, `CORRECOES.md` §5 item 3): três cortes
terminavam no COMEÇO da palavra seguinte ("e o Castro", "e aí emprestei", "mas, segundo") e um
começava com voz, porque a borda vinha da borda do segmento da transcrição. Lá a borda foi levada à
pausa à mão; aqui virou ferramenta, com teste.

Para cada corte escolhido em `recortes/SUGESTAO_DE_CORTES.json` (campo `escolhidos`):

1. mede o nível da FALA do próprio corte: a mediana, em dB, das janelas de 40 ms dentro dele;
2. mede o primeiro e o último 40 ms do corte. Borda boa é a que fica pelo menos `--limiar` dB
   (12, como no caso de 15/out) abaixo da fala;
3. se a borda não está boa, procura a janela de 40 ms mais silenciosa a até `--busca` segundos dela,
   ⛔ sem nunca cortar uma alegação do corte (o começo não passa do começo da primeira alegação, o fim
   não volta antes do fim da última), e leva a borda para lá;
4. com `--conferir`, transcreve a janela final com whisper.cpp e imprime o texto, para ler que a fala
   fica inteira e nada da palavra seguinte entra.

Saída: `recortes/BORDAS_NA_PAUSA.json` (antes, depois, dB de cada borda, o nível da fala) e a tela.
`--so-medir` só mede as bordas que já estão lá (é o que a validação final roda nos cortes prontos):
as de `recortes/RECORTES.json`, isto é, as do corte entregue; sem ele, as da sugestão.
"""

from __future__ import annotations

import argparse
import json
import math
import shutil
import subprocess
import sys
import tempfile
import wave
from array import array
from datetime import date
from pathlib import Path
from statistics import median

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[1]
JANELA_S = 0.040
PASSO_S = 0.005


# ── funções puras (testadas em tests/test_tempo_e_bordas.py) ────────────────────────────────

def rms_db(amostras) -> float:
    """Nível RMS em dB relativo ao fundo de escala de 16 bits; silêncio digital dá -120."""
    if len(amostras) == 0:
        return -120.0
    q = sum(float(x) * float(x) for x in amostras) / len(amostras)
    return 10 * math.log10(q / (32768.0 ** 2)) if q > 0 else -120.0


def nivel_em(amostras, taxa: int, t0: float, inicio_buffer: float, janela: float = JANELA_S) -> float:
    """dB da janela [t0, t0+janela] dentro de um buffer que começa em `inicio_buffer` segundos."""
    i = int(round((t0 - inicio_buffer) * taxa))
    n = int(round(janela * taxa))
    if i < 0 or i + n > len(amostras):
        return 0.0   # janela fora do buffer: conta como fala, para nunca ser escolhida como pausa
    return rms_db(amostras[i:i + n])


def nivel_da_fala(amostras, taxa: int, inicio_buffer: float, ini: float, fim: float) -> float:
    """Mediana dos dB das janelas de 40 ms entre `ini` e `fim` (o nível típico de fala do corte)."""
    vals, t = [], ini
    while t + JANELA_S <= fim:
        vals.append(nivel_em(amostras, taxa, t, inicio_buffer))
        t += JANELA_S
    return median(vals) if vals else -120.0


def pausa_mais_funda(amostras, taxa: int, inicio_buffer: float, de: float, ate: float,
                     perto_de: float) -> tuple[float, float]:
    """O começo da janela de 40 ms mais silenciosa em [de, ate]; empate vai para a mais perto."""
    melhor, t = None, de
    while t <= ate + 1e-9:
        db = nivel_em(amostras, taxa, t, inicio_buffer)
        chave = (round(db, 1), abs(t - perto_de))
        if melhor is None or chave < melhor[0]:
            melhor = (chave, t, db)
        t += PASSO_S
    return melhor[1], melhor[2]


def nova_borda(amostras, taxa, inicio_buffer, *, borda: float, lado: str, fala_db: float,
               limiar: float, busca: float, trava: float) -> dict:
    """Decide a borda de um lado ('inicio' ou 'fim'), respeitando a `trava` (a alegação mais externa)."""
    t_janela = borda if lado == "inicio" else borda - JANELA_S
    db = nivel_em(amostras, taxa, t_janela, inicio_buffer)
    r = {"antes": round(borda, 2), "antes_db_abaixo_da_fala": round(fala_db - db, 1)}
    if fala_db - db >= limiar:
        r.update(depois=round(borda, 2), depois_db_abaixo_da_fala=round(fala_db - db, 1), movida=False)
        return r
    if lado == "inicio":
        de, ate = borda - busca, min(borda + busca, trava) - JANELA_S
        t, db2 = pausa_mais_funda(amostras, taxa, inicio_buffer, de, ate, borda)
        nova = t
    else:
        de, ate = max(borda - busca, trava), borda + busca - JANELA_S
        t, db2 = pausa_mais_funda(amostras, taxa, inicio_buffer, de, ate, borda - JANELA_S)
        nova = t + JANELA_S
    r.update(depois=round(nova, 2), depois_db_abaixo_da_fala=round(fala_db - db2, 1), movida=True)
    return r


# ── execução ───────────────────────────────────────────────────────────────────────────────

def ler_trecho(wav: Path, ini: float, fim: float) -> tuple[array, int]:
    with wave.open(str(wav), "rb") as w:
        if w.getsampwidth() != 2:
            raise SystemExit("o WAV do caso tem que ser PCM de 16 bits (python -m checagem midia <slug> audio)")
        taxa, canais = w.getframerate(), w.getnchannels()
        w.setpos(max(0, int(ini * taxa)))
        bruto = w.readframes(int((fim - ini) * taxa))
    a = array("h", bruto)
    if canais > 1:
        a = array("h", a[::canais])
    return a, taxa


def transcrever(wav: Path, ini: float, fim: float) -> str:
    modelo = Path.home() / ".cache" / "whisper-models" / "ggml-large-v3-turbo.bin"
    d = Path(tempfile.mkdtemp(prefix="borda-"))
    try:
        j = d / "j.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ini:.3f}", "-t", f"{fim - ini:.3f}",
                        "-i", str(wav), "-ar", "16000", "-ac", "1", str(j)], check=True)
        subprocess.run(["whisper-cli", "-m", str(modelo), "-f", str(j), "-l", "pt", "-bs", "5",
                        "-oj", "-of", str(d / "o"), "-np"], check=True, capture_output=True)
        dados = json.loads((d / "o.json").read_text(encoding="utf-8"))
        return " ".join(s["text"].strip() for s in dados["transcription"])
    finally:
        shutil.rmtree(d, ignore_errors=True)


def bordas_entregues(caso: Path) -> dict[str, tuple[float, float]]:
    """As bordas dos cortes como foram recortados (`recortes/RECORTES.json`), não as da sugestão.

    🔑 Validação final de 17/out: o `--so-medir` lia a SUGESTAO_DE_CORTES.json, e media as bordas de
    antes da pausa, não as do corte entregue."""
    arq = caso / "recortes" / "RECORTES.json"
    if not arq.exists():
        return {}
    dados = json.loads(arq.read_text(encoding="utf-8"))
    return {r["id"]: (r["origem_inicio_s"], round(r["origem_inicio_s"] + r["duracao_s"], 2))
            for r in dados.get("recortes", []) if "origem_inicio_s" in r and "duracao_s" in r}


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("slug")
    p.add_argument("--recorte", default="sabatina-completa")
    p.add_argument("--busca", type=float, default=0.8)
    p.add_argument("--limiar", type=float, default=12.0)
    p.add_argument("--conferir", action="store_true")
    p.add_argument("--so-medir", action="store_true")
    a = p.parse_args()

    caso = RAIZ / "casos" / a.slug
    wav = next((caso / "fonte").glob("*.wav"))
    sug = json.loads((caso / "recortes" / "SUGESTAO_DE_CORTES.json").read_text(encoding="utf-8"))
    aleg = json.loads((caso / "alegacoes" / f"alegacoes-{a.recorte}.json").read_text(encoding="utf-8"))
    por_id = {x["id"]: x for x in aleg["alegacoes"]}

    entregues = bordas_entregues(caso) if a.so_medir else {}
    saida = []
    for c in sug["escolhidos"]:
        ini, fim = entregues.get(c["id"], (c["inicio_s"], c["fim_s"]))
        ids = c.get("ids") or [x["id"] for x in aleg["alegacoes"] if x["inicio_s"] >= ini - 0.05 and x["fim_s"] <= fim + 0.05]
        primeira = min(por_id[i]["inicio_s"] for i in ids)
        ultima = max(por_id[i]["fim_s"] for i in ids)
        b0 = ini - a.busca - 0.5
        amostras, taxa = ler_trecho(wav, b0, fim + a.busca + 0.5)
        fala = nivel_da_fala(amostras, taxa, b0, ini, fim)
        if a.so_medir:
            r_i = {"borda": ini, "db_abaixo_da_fala": round(fala - nivel_em(amostras, taxa, ini, b0), 1)}
            r_f = {"borda": fim, "db_abaixo_da_fala": round(fala - nivel_em(amostras, taxa, fim - JANELA_S, b0), 1)}
        else:
            r_i = nova_borda(amostras, taxa, b0, borda=ini, lado="inicio", fala_db=fala, limiar=a.limiar,
                             busca=a.busca, trava=primeira)
            r_f = nova_borda(amostras, taxa, b0, borda=fim, lado="fim", fala_db=fala, limiar=a.limiar,
                             busca=a.busca, trava=ultima)
        item = {"corte": c["id"], "fala_db": round(fala, 1), "alegacoes": ids, "inicio": r_i, "fim": r_f}
        if a.conferir:
            i2 = r_i.get("depois", r_i.get("borda"))
            f2 = r_f.get("depois", r_f.get("borda"))
            item["texto_da_janela"] = transcrever(wav, i2, f2)
        saida.append(item)
        if a.so_medir:
            print(f"{c['id']}  fala {fala:6.1f} dB · início {ini:8.2f} ({r_i['db_abaixo_da_fala']:5.1f} dB abaixo)"
                  f" · fim {fim:8.2f} ({r_f['db_abaixo_da_fala']:5.1f} dB abaixo)")
        else:
            print(f"{c['id']}  fala {fala:6.1f} dB · início {r_i['antes']:8.2f}->{r_i['depois']:8.2f}"
                  f" ({r_i['antes_db_abaixo_da_fala']:5.1f}->{r_i['depois_db_abaixo_da_fala']:5.1f} dB abaixo)"
                  f" · fim {r_f['antes']:8.2f}->{r_f['depois']:8.2f}"
                  f" ({r_f['antes_db_abaixo_da_fala']:5.1f}->{r_f['depois_db_abaixo_da_fala']:5.1f} dB abaixo)")
        if a.conferir:
            print(f"     «{item['texto_da_janela']}»")

    if not a.so_medir:
        destino = caso / "recortes" / "BORDAS_NA_PAUSA.json"
        destino.write_text(json.dumps({"caso": a.slug, "gerado_em": str(date.today()),
                                       "metodo": f"janelas de {int(JANELA_S * 1000)} ms; borda boa a {a.limiar} dB "
                                                 f"ou mais abaixo da mediana da fala do corte; busca de {a.busca} s "
                                                 "sem cortar alegação",
                                       "cortes": saida}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        ruins = [s["corte"] for s in saida for lado in ("inicio", "fim")
                 if s[lado]["depois_db_abaixo_da_fala"] < a.limiar]
        print(f"\n✓ {destino.relative_to(RAIZ)}" + (f" · ⚠ ainda sem pausa funda: {sorted(set(ruins))}" if ruins else
                                                   " · todas as bordas na pausa"))
    return 0


if __name__ == "__main__":
    sys.exit(main())
