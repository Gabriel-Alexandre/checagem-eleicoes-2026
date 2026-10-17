"""Mede o começo e o fim de cada alegação PALAVRA POR PALAVRA, antes de qualquer veredito.

    python ferramentas/medir-tempo-das-alegacoes.py <slug> [--recorte sabatina-completa] \\
        [--margem 3.0] [--aplicar] [--so A012,A013]

🔑 Por que existe (validação final do caso de 15/out/2026, `CORRECOES.md` §5 item 4): o tempo de
uma alegação vinha do SEGMENTO da transcrição, que é a frase inteira. Uma alegação dita no meio do
segmento herdava o começo dele, e o card entrava antes da fala (A075: card em 16:03, fala em 16:09;
até 4,4 s de erro). Lá a medida foi feita à mão; aqui ela virou ferramenta, com teste.

Como mede, para cada alegação:

1. acha o segmento (ou os segmentos) da transcrição onde a `frase` está: é a FRASE DE ORIGEM;
2. transcreve de novo, com whisper.cpp palavra por palavra (`-ml 1 -sow`), uma janela que vai de
   `--margem` segundos antes a `--margem` segundos depois da frase de origem;
3. alinha as primeiras palavras da `frase` (e as últimas, para o fim) com as palavras da janela, por
   TRECHOS DE PELO MENOS DUAS PALAVRAS seguidas (uma palavra solta casa em qualquer lugar);
4. ⛔ só aceita o ponto medido quando ele cai DENTRO da frase de origem (com 0,3 s de folga): fora
   dela, o alinhamento pegou a palavra repetida em outra frase, e a medida é recusada com o motivo.

Com `--aplicar`, os tempos aceitos vão para o arquivo de alegações do recorte (e só para ele), e a
ordem cronológica dos ids é conferida: um ajuste que deixaria um id começar antes do anterior é
recusado e listado. Sem `--aplicar`, nada é escrito: o relatório sai em
`alegacoes/TEMPOS_MEDIDOS.json` e na tela.

⛔ Roda antes da checagem: ela não lê `checagens/` e não sabe veredito nenhum.
"""

from __future__ import annotations

import argparse
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unicodedata
from datetime import date
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

RAIZ = Path(__file__).resolve().parents[1]
FOLGA_S = 0.3        # tolerância para "dentro da frase de origem"
MIN_PALAVRAS = 2     # trecho mínimo de alinhamento


# ── funções puras (testadas em tests/test_tempo_e_bordas.py) ────────────────────────────────

def normalizar(palavra: str) -> str:
    """minúsculas, sem acento e sem pontuação: 'Trilhão,' -> 'trilhao'."""
    s = unicodedata.normalize("NFKD", palavra.lower())
    s = "".join(c for c in s if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9%]", "", s)


def tokens(texto: str) -> list[str]:
    return [t for t in (normalizar(p) for p in texto.split()) if t]


def partes_da_frase(frase: str) -> tuple[list[str], list[str]]:
    """As palavras do começo e do fim da frase; `[...]` separa as partes de uma citação cortada."""
    pedacos = [p for p in re.split(r"\[\s*\.\.\.\s*\]|\[…\]", frase) if tokens(p)]
    if not pedacos:
        return [], []
    return tokens(pedacos[0]), tokens(pedacos[-1])


def alinhar(palavras: list[tuple[str, float, float]], alvo: list[str], *, do_fim: bool = False,
            minimo: int = MIN_PALAVRAS, maximo: int = 6, perto_de: float | None = None) -> tuple[float, int, int] | None:
    """Procura, nas palavras medidas, um trecho seguido igual ao começo (ou ao fim) do alvo.

    Candidatos: todo trecho de `minimo` a `maximo` palavras do alvo, começando na palavra 0 do alvo ou
    deslocado em até três palavras (o motor às vezes come ou troca a primeira palavra). A escolha é,
    nesta ordem: o MENOR deslocamento (o trecho que começa na primeira palavra do alvo ganha), o
    trecho mais longo e, no empate, o mais perto de `perto_de` (o tempo que a alegação já tinha).

    🔧 17/out/2026: a primeira versão pegava o trecho mais longo em qualquer deslocamento e a
    primeira ocorrência dele. Na A075 do caso de 15/out ("o André Mendonça também está implicado",
    com "Mendoza" na passada palavra por palavra), o trecho mais longo era "também está implicado",
    que aparece antes em "o Toffoli também está implicado": a medida saía 2,2 s cedo, ainda dentro
    da frase de origem. Com o deslocamento primeiro, "o André" vence e a medida cai em 1018,94 s.

    Devolve o tempo medido do começo (ou do fim) do alvo, quantas palavras casaram e o deslocamento;
    `None` se nada com `minimo` palavras casou. 🔧 Um trecho de só DUAS palavras só vale se aparecer
    uma vez na janela: na A034 do caso de 16/out, "o senhor" aparecia quatro vezes e a medida caiu na
    frase anterior. Com deslocamento, o tempo é o da primeira palavra
    casada (não se inventa o tempo da palavra que o motor não escreveu igual).
    """
    norm = [normalizar(p[0]) for p in palavras]
    seq = list(reversed(alvo)) if do_fim else list(alvo)
    lista = list(reversed(norm)) if do_fim else norm
    tempos = [p[2] for p in reversed(palavras)] if do_fim else [p[1] for p in palavras]
    melhor = None
    for desloc in range(0, min(4, max(1, len(seq) - minimo + 1))):
        for tamanho in range(min(maximo, len(seq) - desloc), minimo - 1, -1):
            trecho = seq[desloc:desloc + tamanho]
            achados = [i for i in range(len(lista) - tamanho + 1) if lista[i:i + tamanho] == trecho]
            if tamanho < 3 and len(achados) > 1:
                continue   # par de palavras repetido na janela ("o senhor"): ambíguo, não alinha
            for i in achados:
                dist = abs(tempos[i] - perto_de) if perto_de is not None else i
                chave = (desloc, -tamanho, dist)
                if melhor is None or chave < melhor[0]:
                    melhor = (chave, tempos[i], tamanho, desloc)
        if melhor is not None:
            break
    return None if melhor is None else (melhor[1], melhor[2], melhor[3])


def dentro(t: float, ini: float, fim: float, folga: float = FOLGA_S) -> bool:
    return ini - folga <= t <= fim + folga


def frase_de_origem(segmentos: list[dict], frase: str, ini: float, fim: float) -> tuple[float, float]:
    """O intervalo dos segmentos que contêm a alegação (os que se sobrepõem a [ini, fim])."""
    toc = [s for s in segmentos if s["fim_s"] > ini - 0.05 and s["inicio_s"] < fim + 0.05]
    if not toc:
        return ini, fim
    return min(s["inicio_s"] for s in toc), max(s["fim_s"] for s in toc)


def ordem_cronologica(itens: list[tuple[str, float]]) -> list[str]:
    """Ids que começariam antes do anterior (a ordem dos ids tem que ser a da fala)."""
    ruins, ultimo = [], float("-inf")
    for ident, t in itens:
        if t < ultimo - 1e-6:
            ruins.append(ident)
        else:
            ultimo = t
    return ruins


def acertar_ordem(novos: list[tuple[str, float]], antigos: list[float]) -> tuple[list[float], list[str]]:
    """Garante começos em ordem não decrescente depois dos ajustes, sem mexer na ordem dos ids.

    Quando o começo medido de um id fica DEPOIS do começo do id seguinte (no caso de 15/out, a A044
    medida em 531,5 s e a A045, que a contém, começando em 530,6 s), o id anterior volta ao tempo
    que tinha, se isso basta; se não basta, fica com o mesmo começo do seguinte (a solução da A044
    em 16/out). Devolve os começos finais e as notas do que foi feito.
    """
    t = [x for _, x in novos]
    notas = []
    for k in range(len(t) - 1, 0, -1):
        if t[k - 1] > t[k] + 1e-6:
            ident = novos[k - 1][0]
            if antigos[k - 1] <= t[k] + 1e-6:
                notas.append(f"{ident}: o começo medido ({t[k - 1]}) ficava depois do de {novos[k][0]} ({t[k]}); voltou a {antigos[k - 1]}")
                t[k - 1] = antigos[k - 1]
            else:
                notas.append(f"{ident}: o começo medido ({t[k - 1]}) ficava depois do de {novos[k][0]} ({t[k]}); ficou igual a ele")
                t[k - 1] = t[k]
    return t, notas


def juntar_janelas(janelas: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Une as janelas que se sobrepõem (alegações vizinhas dividem a mesma fala)."""
    blocos: list[list[float]] = []
    for a, b in sorted(janelas):
        if blocos and a <= blocos[-1][1]:
            blocos[-1][1] = max(blocos[-1][1], b)
        else:
            blocos.append([a, b])
    return [(a, b) for a, b in blocos]


# ── execução ───────────────────────────────────────────────────────────────────────────────

def transcrever_palavras(wav: Path, ini: float, fim: float, modelo: Path) -> list[tuple[str, float, float]]:
    d = Path(tempfile.mkdtemp(prefix="tempo-"))
    try:
        janela = d / "j.wav"
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-ss", f"{ini:.3f}", "-t", f"{fim - ini:.3f}",
                        "-i", str(wav), "-ar", "16000", "-ac", "1", str(janela)], check=True)
        subprocess.run(["whisper-cli", "-m", str(modelo), "-f", str(janela), "-l", "pt", "-bs", "5",
                        "-bo", "5", "-ml", "1", "-sow", "-oj", "-of", str(d / "o"), "-np"],
                       check=True, capture_output=True)
        dados = json.loads((d / "o.json").read_text(encoding="utf-8"))
        saida = []
        for s in dados["transcription"]:
            texto = s["text"].strip()
            if not texto:
                continue
            saida.append((texto, ini + s["offsets"]["from"] / 1000, ini + s["offsets"]["to"] / 1000))
        return saida
    finally:
        shutil.rmtree(d, ignore_errors=True)


def transcrever_em_fila(wav: Path, blocos: list[tuple[float, float]], modelo: Path,
                        pausa: float = 2.0) -> list[tuple[str, float, float]]:
    """Os blocos em fila, com `pausa` de silêncio entre eles, numa chamada só (-ml 1 -sow -mc 0).

    Devolve as palavras no horário do ARQUIVO. `-mc 0` impede que o texto de um bloco sirva de
    contexto para o seguinte; o silêncio entre eles impede que uma palavra atravesse a emenda.
    """
    import wave
    d = Path(tempfile.mkdtemp(prefix="tempo-fila-"))
    try:
        mapa, pos = [], 0.0
        with wave.open(str(wav), "rb") as w:
            taxa, larg, can = w.getframerate(), w.getsampwidth(), w.getnchannels()
            silencio = bytes(1) * int(pausa * taxa) * larg * can
            dados = bytearray()
            for a, b in blocos:
                w.setpos(int(a * taxa))
                bruto = w.readframes(int((b - a) * taxa))
                dur = len(bruto) / (taxa * larg * can)
                mapa.append((pos, pos + dur, a))
                dados += bruto + silencio
                pos += dur + pausa
        arq = d / "fila.wav"
        with wave.open(str(arq), "wb") as o:
            o.setnchannels(can)
            o.setsampwidth(larg)
            o.setframerate(taxa)
            o.writeframes(bytes(dados))
        subprocess.run(["whisper-cli", "-m", str(modelo), "-f", str(arq), "-l", "pt", "-bs", "5", "-bo", "5",
                        "-ml", "1", "-sow", "-mc", "0", "-oj", "-of", str(d / "o"), "-np"],
                       check=True, capture_output=True)
        saida = []
        for seg in json.loads((d / "o.json").read_text(encoding="utf-8"))["transcription"]:
            texto = seg["text"].strip()
            if not texto:
                continue
            t0, t1 = seg["offsets"]["from"] / 1000, seg["offsets"]["to"] / 1000
            for f0, f1, a in mapa:
                if f0 - 0.05 <= t0 < f1 + 0.05:
                    saida.append((texto, a + (t0 - f0), a + (t1 - f0)))
                    break
        return saida
    finally:
        shutil.rmtree(d, ignore_errors=True)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    p.add_argument("slug")
    p.add_argument("--recorte", default="sabatina-completa")
    p.add_argument("--margem", type=float, default=3.0)
    p.add_argument("--aplicar", action="store_true")
    p.add_argument("--so", default=None, help="ids separados por vírgula")
    p.add_argument("--janela-a-janela", action="store_true",
                   help="uma chamada do motor por alegação (lento: o modelo carrega a cada vez); o padrão é a fila")
    a = p.parse_args()

    caso = RAIZ / "casos" / a.slug
    arq_aleg = caso / "alegacoes" / f"alegacoes-{a.recorte}.json"
    aleg = json.loads(arq_aleg.read_text(encoding="utf-8"))
    segs = json.loads((caso / "transcricao" / "transcricao.json").read_text(encoding="utf-8"))["segmentos"]
    wav = next((caso / "fonte").glob("*.wav"))
    modelo = Path.home() / ".cache" / "whisper-models" / "ggml-large-v3-turbo.bin"
    so = set(a.so.split(",")) if a.so else None

    alvo = [al for al in aleg["alegacoes"] if not so or al["id"] in so]
    origens = {al["id"]: frase_de_origem(segs, al["frase"], al["inicio_s"], al["fim_s"]) for al in alvo}
    janelas = {i: (max(0.0, o[0] - a.margem), o[1] + a.margem) for i, o in origens.items()}
    todas = None
    if not a.janela_a_janela:
        blocos = juntar_janelas(list(janelas.values()))
        print(f"fila: {len(blocos)} blocos, {sum(b - x for x, b in blocos) / 60:.1f} min de áudio, uma chamada do motor")
        todas = transcrever_em_fila(wav, blocos, modelo)
    relatorio = []
    for al in alvo:
        o_ini, o_fim = origens[al["id"]]
        j0, j1 = janelas[al["id"]]
        palavras = ([p for p in todas if j0 <= p[1] <= j1] if todas is not None
                    else transcrever_palavras(wav, j0, j1, modelo))
        comeco, final = partes_da_frase(al["frase"])
        r = {"id": al["id"], "antes": [al["inicio_s"], al["fim_s"]], "origem": [o_ini, o_fim]}
        m_ini = alinhar(palavras, comeco, perto_de=al["inicio_s"])
        m_fim = alinhar(palavras, final, do_fim=True, perto_de=al["fim_s"])
        for nome, m in (("inicio", m_ini), ("fim", m_fim)):
            if m is None:
                r[nome] = {"aceito": False, "motivo": "nenhum trecho de duas palavras casou"}
            elif not dentro(m[0], o_ini, o_fim):
                r[nome] = {"aceito": False, "medido": round(m[0], 2), "palavras": m[1], "deslocamento": m[2],
                           "motivo": "o ponto medido cai fora da frase de origem"}
            else:
                r[nome] = {"aceito": True, "medido": round(m[0], 2), "palavras": m[1], "deslocamento": m[2]}
        if r["inicio"].get("aceito") and r["fim"].get("aceito") and r["fim"]["medido"] <= r["inicio"]["medido"]:
            r["inicio"]["aceito"] = r["fim"]["aceito"] = False
            r["inicio"]["motivo"] = r["fim"]["motivo"] = "fim medido antes do começo medido"
        relatorio.append(r)
        ini_txt = r["inicio"].get("medido", "-")
        fim_txt = r["fim"].get("medido", "-")
        print(f"{al['id']}  {al['inicio_s']:8.2f}->{ini_txt!s:>8} {'ok' if r['inicio']['aceito'] else 'recusado'}"
              f"   {al['fim_s']:8.2f}->{fim_txt!s:>8} {'ok' if r['fim']['aceito'] else 'recusado'}")

    destino = caso / "alegacoes" / "TEMPOS_MEDIDOS.json"
    destino.write_text(json.dumps({"caso": a.slug, "recorte": a.recorte, "gerado_em": str(date.today()),
                                   "metodo": "whisper.cpp large-v3-turbo -ml 1 -sow numa janela de "
                                             f"{a.margem} s em volta da frase de origem ("
                                             + ("uma chamada por janela" if a.janela_a_janela else
                                                "janelas sobrepostas unidas, postas em fila com 2 s de silêncio, "
                                                "numa chamada só com -mc 0") + "); alinhamento por "
                                             f"trechos de >= {MIN_PALAVRAS} palavras; aceito só dentro da "
                                             f"frase de origem (folga {FOLGA_S} s)",
                                   "medidas": relatorio}, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    aceitos_i = sum(r["inicio"]["aceito"] for r in relatorio)
    aceitos_f = sum(r["fim"]["aceito"] for r in relatorio)
    print(f"\n✓ {len(relatorio)} medidas · começo aceito em {aceitos_i} · fim aceito em {aceitos_f} · {destino.relative_to(RAIZ)}")

    if a.aplicar:
        por_id = {r["id"]: r for r in relatorio}
        novos = []
        for al in aleg["alegacoes"]:
            r = por_id.get(al["id"])
            ini = r["inicio"]["medido"] if r and r["inicio"]["aceito"] else al["inicio_s"]
            fim = r["fim"]["medido"] if r and r["fim"]["aceito"] else al["fim_s"]
            novos.append((al["id"], ini, fim))
        inicios, notas = acertar_ordem([(i, s) for i, s, _ in novos], [al["inicio_s"] for al in aleg["alegacoes"]])
        for nota in notas:
            print(f"  ⚠ {nota}")
        assert not ordem_cronologica([(i, s) for (i, _, _), s in zip(novos, inicios, strict=True)])
        mudou = 0
        for al, (_ident, _, fim), ini in zip(aleg["alegacoes"], novos, inicios, strict=True):
            if (ini, fim) != (al["inicio_s"], al["fim_s"]):
                al["inicio_s"], al["fim_s"] = ini, fim
                mudou += 1
        arq_aleg.write_text(json.dumps(aleg, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
        print(f"✓ {mudou} alegações com o tempo ajustado em {arq_aleg.relative_to(RAIZ)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
