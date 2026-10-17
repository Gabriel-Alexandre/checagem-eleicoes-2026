"""Segunda passada em lote: cada janela suspeita (de t-3 a t+5 s) é recortada do WAV, as janelas são postas
em fila com 2 s de silêncio entre elas, e o whisper.cpp (large-v3-turbo, feixe 8, -mc 0: sem texto anterior
como contexto) transcreve a fila numa chamada só, sem e com prompt. Cada trecho volta para a janela dele
pelo tempo. Grava JSON com as duas leituras por janela.

uso: python passada_concatenada.py SAIDA.json t1 t2 ...
"""
import json, struct, subprocess, sys, tempfile, wave
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
WAV = Path(r"C:\Users\Gabriel\Downloads\repositorios\checagem-eleicoes-2026\casos\2026-10-16-sabatina-flavio-globo-2turno\fonte\sabatina-flavio-globo-2026-10-16.wav")
MODELO = Path.home() / ".cache" / "whisper-models" / "ggml-large-v3-turbo.bin"
PROMPT = ("Sabatina da TV Globo com Renata Lo Prete e o candidato Flávio Bolsonaro, do PL. Nomes citados: Lula, Jair Bolsonaro, "
          "Daniel Vorcaro, Banco Master, Kassio Nunes Marques, Alexandre de Moraes, João Vaccari Neto, Andrei Rodrigues, Davi Alcolumbre, "
          "Sérgio Moro, Eduardo Bolsonaro, Magnitsky, Flávio Dino, Zanin, Ricardo Nunes, Márcio Canella, Rodrigo Bacellar, Cláudio Castro, "
          "Claudio Lottenberg, Albert Einstein, Quaest, CACs, PEC, Petrobras, margem equatorial, royalties, rachadinhas, Luciano Huck.")
ANTES, DEPOIS, PAUSA = 3.0, 5.0, 2.0

def main():
    saida, tempos = sys.argv[1], [float(x) for x in sys.argv[2:]]
    d = Path(tempfile.mkdtemp())
    with wave.open(str(WAV), "rb") as w:
        taxa, larg, can = w.getframerate(), w.getsampwidth(), w.getnchannels()
        fila, mapa, pos = bytearray(), [], 0.0
        silencio = b"\x00" * int(PAUSA * taxa) * larg * can
        for t in tempos:
            ini = max(0.0, t - ANTES)
            w.setpos(int(ini * taxa))
            bruto = w.readframes(int((ANTES + DEPOIS) * taxa))
            dur = len(bruto) / (taxa * larg * can)
            mapa.append((t, ini, pos, pos + dur))
            fila += bruto + silencio
            pos += dur + PAUSA
    arq = d / "fila.wav"
    with wave.open(str(arq), "wb") as o:
        o.setnchannels(can); o.setsampwidth(larg); o.setframerate(taxa); o.writeframes(bytes(fila))
    leituras = {}
    for nome, prompt in (("sem_prompt", None), ("com_prompt", PROMPT)):
        cmd = ["whisper-cli", "-m", str(MODELO), "-f", str(arq), "-l", "pt", "-bs", "8", "-bo", "8", 
               "-oj", "-of", str(d / nome), "-np", "-t", "12"]
        if prompt:
            cmd += ["--prompt", prompt]
        subprocess.run(cmd, check=True, capture_output=True)
        segs = json.load(open(d / f"{nome}.json", encoding="utf-8"))["transcription"]
        leituras[nome] = [(s["offsets"]["from"] / 1000, s["offsets"]["to"] / 1000, s["text"].strip()) for s in segs]
        print("passada pronta:", nome, flush=True)
    res = {}
    for t, ini, a, b in mapa:
        item = {"janela_no_arquivo": [round(ini, 2), round(ini + ANTES + DEPOIS, 2)]}
        for nome, segs in leituras.items():
            item[nome] = " ".join(x for (s0, s1, x) in segs if (s0 + s1) / 2 >= a - 0.2 and (s0 + s1) / 2 < b + 0.2)
        res[str(t)] = item
        print(f"== {t}\n  sem: {item['sem_prompt']}\n  com: {item['com_prompt']}")
    json.dump({"metodo": __doc__.strip().split("\n\n")[0], "janelas": res}, open(saida, "w", encoding="utf-8"), ensure_ascii=False, indent=1)

main()
