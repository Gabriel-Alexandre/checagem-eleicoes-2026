"""Faz um RASCUNHO dos turnos (quem fala quando) e as folhas de quadros para conferir no vídeo.

Para a sabatina inteira (15/out/2026): 45 min, uma jornalista e um candidato, às vezes um VT. O
PASSO 3 continua manual de propósito (passo3_falantes.py): atribuir frase à pessoa errada é o pior
erro do projeto. Este script **não escreve `falantes.json`**. Ele junta pistas medidas e entrega um
rascunho para ser conferido, turno a turno, no vídeo. Dois passos:

    # 1. agrupa os ENQUADRAMENTOS do vídeo (a emissora mostra quem fala) e desenha a folha dos grupos
    python ferramentas/rascunho-de-turnos.py planos <slug> [--grupos 16]
    #    olhe transcricao/folha-de-planos.jpg e escreva transcricao/planos-rotulos.json:
    #    {"0": "Lula", "3": "Renata Lo Prete", "5": "ambiguo", ...}   (plano aberto = "ambiguo")

    # 2. junta plano + texto (+ VT declarado) em turnos, e desenha a folha dos turnos
    python ferramentas/rascunho-de-turnos.py turnos <slug> --pergunta "Renata Lo Prete" --responde "Lula" \\
        [--vt 56.7-112.7] [--folha]

As pistas, na ordem de peso:
  1. o **plano** do segmento (o grupo de enquadramento de mais quadros dentro dele), quando o grupo foi
     rotulado com um nome. Medido no caso de 27/ago: os closes do candidato saem em grupos 95% puros;
     o plano aberto mistura todo mundo e fica "ambiguo";
  2. o **texto**: frase que termina em "?" ou começa com "presidente", "candidato" ou "o senhor" puxa
     para quem pergunta; o nome de quem pergunta dito pelo outro ("Renata, ...") puxa para quem responde;
  3. sem pista, o segmento fica com o falante do anterior (turno dura mais que um segmento), e o turno
     que nasceu sem nenhuma pista sai marcado como dúvida.

⚠️ **O tom de voz não serve para Lula.** Medido em 27/ago (`medir-tom.py`): mediana de 192 Hz para
Lula e 188 Hz para Renata Vasconcellos. A opção `--tom` existe para outra mesa, nunca como padrão.

📏 Medida do método no ensaio de 15/out sobre a sabatina de 27/ago (dois jornalistas, VT declarado,
16 grupos rotulados no olho pela folha, sem olhar a resposta), contra o falantes.json escrito à mão:
**89% do tempo de fala no lado certo da mesa**; **96,5% da fala de Lula** atribuída a Lula, mas só
**71% da fala dos jornalistas** atribuída a jornalista. O erro que sobra é a pergunta feita em plano
aberto ou de costas, que herda o falante da resposta anterior. Por isso a revisão olha **todo turno
de jornalista** e o começo de cada resposta, e o rascunho NÃO é o falantes.json.

Saída: `transcricao/falantes.rascunho.json` (formato do falantes.json, com `confianca` e `pistas`),
`transcricao/RASCUNHO_DE_TURNOS.md` e, com `--folha`, `transcricao/folha-de-turnos.jpg`.

🔴 Depois de conferir: copie para `falantes.json` (corrigindo o que a folha e o áudio desmentiram),
escreva o método em `metodo` e rode `python -m checagem falantes <slug>`.
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import unicodedata
from collections import Counter
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from checagem import config as cfg  # noqa: E402

VOCATIVOS = ("presidente", "candidato", "o senhor", "senhor", "ex-presidente")
FPS_PLANOS = 2
MINI = (32, 18)


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    return "".join(c for c in t if not unicodedata.combining(c))


def _mmss(s: float) -> str:
    s = int(s)
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def _video(caso: Path) -> Path:
    v = next((p for p in sorted((caso / "fonte").glob("*"))
              if p.suffix.lower() in (".mp4", ".mkv", ".mov", ".webm")), None)
    if not v:
        sys.exit("✗ sem vídeo em fonte/")
    return v


def _fonte(tamanho: int):
    from PIL import ImageFont
    try:
        return ImageFont.truetype(str(cfg.FONTE_SANS), tamanho)
    except OSError:
        return ImageFont.load_default()


def _quadro(video: Path, t: float, w: int, h: int, tmp: Path):
    from PIL import Image
    subprocess.run(["ffmpeg", "-v", "error", "-ss", f"{t:.2f}", "-i", str(video), "-frames:v", "1",
                    "-vf", f"scale={w}:{h}", "-y", str(tmp)], check=False)
    return Image.open(tmp).convert("RGB") if tmp.exists() else None


# ─────────────────────────────────────────────────────────────────────
# 1. planos
# ─────────────────────────────────────────────────────────────────────


def kmeans(X, k: int, semente: int = 0, voltas: int = 30):
    import numpy as np
    rng = np.random.default_rng(semente)
    C = X[rng.choice(len(X), k, replace=False)].copy()
    for _ in range(voltas):
        rot = ((X[:, None, :] - C[None]) ** 2).sum(-1).argmin(1)
        for j in range(k):
            if (rot == j).any():
                C[j] = X[rot == j].mean(0)
    return rot, C


def planos(slug: str, grupos: int) -> int:
    import numpy as np
    from PIL import Image, ImageDraw

    caso = cfg.pasta_do_caso(slug)
    video = _video(caso)
    print(f"lendo {video.name} a {FPS_PLANOS} quadros/s em {MINI[0]}x{MINI[1]} (um minuto para 45 min de vídeo)...")
    bruto = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-vf",
                            f"fps={FPS_PLANOS},scale={MINI[0]}:{MINI[1]}", "-f", "rawvideo", "-pix_fmt", "rgb24", "-"],
                           capture_output=True, check=True).stdout
    X = np.frombuffer(bruto, dtype=np.uint8).reshape(-1, MINI[0] * MINI[1] * 3).astype("float32") / 255
    rot, C = kmeans(X, grupos)
    (caso / "transcricao").mkdir(exist_ok=True)
    (caso / "transcricao" / "planos.json").write_text(json.dumps(
        {"caso": slug, "fps": FPS_PLANOS, "grupos": grupos, "semente": 0, "rotulo_por_quadro": rot.tolist()}) + "\n",
        encoding="utf-8", newline="\n")
    # folha: 4 quadros por grupo (os mais perto do centro), uma linha por grupo
    w, h, n = 320, 180, 4
    folha = Image.new("RGB", (n * w + 220, grupos * (h + 8)), (14, 14, 14))
    d = ImageDraw.Draw(folha)
    tmp = caso / "transcricao" / "_quadro.jpg"
    for g in range(grupos):
        idx = np.where(rot == g)[0]
        y = g * (h + 8)
        d.text((10, y + 10), f"plano {g}", font=_fonte(30), fill=(255, 220, 90))
        d.text((10, y + 52), f"{len(idx) / FPS_PLANOS / 60:.1f} min", font=_fonte(24), fill=(220, 220, 220))
        if not len(idx):
            continue
        perto = idx[((X[idx] - C[g]) ** 2).sum(1).argsort()]
        escolha = [perto[int(i * (len(perto) - 1) / max(1, n - 1))] for i in range(n)] if len(perto) >= n else list(perto)
        for j, q in enumerate(sorted(escolha)):
            im = _quadro(video, q / FPS_PLANOS, w, h, tmp)
            if im:
                folha.paste(im, (220 + j * w, y))
                d.text((226 + j * w, y + h - 26), _mmss(q / FPS_PLANOS), font=_fonte(20), fill=(255, 255, 255))
    tmp.unlink(missing_ok=True)
    folha.save(caso / "transcricao" / "folha-de-planos.jpg", quality=82)
    exemplo = {str(g): "NOME ou ambiguo" for g in range(grupos)}
    alvo = caso / "transcricao" / "planos-rotulos.json"
    if not alvo.exists():
        alvo.write_text(json.dumps(exemplo, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(f"✓ {grupos} grupos de enquadramento · folha em casos/{slug}/transcricao/folha-de-planos.jpg")
    print(f"  próximo: rotule cada grupo em casos/{slug}/transcricao/planos-rotulos.json (nome de quem aparece "
          "em close, ou \"ambiguo\" para plano aberto), depois rode o subcomando `turnos`")
    return 0


# ─────────────────────────────────────────────────────────────────────
# 2. turnos
# ─────────────────────────────────────────────────────────────────────


def plano_de_cada_segmento(segs: list[dict], rotulo_por_quadro: list[int], fps: int) -> list[int | None]:
    saida = []
    for s in segs:
        a = int(s["inicio_s"] * fps)
        b = max(a + 1, int(s["fim_s"] * fps))
        c = Counter(rotulo_por_quadro[a:b]).most_common(1)
        saida.append(c[0][0] if c else None)
    return saida


def votar(seg: dict, nome_do_plano: str | None, pergunta: str, responde: str, nome_curto: str,
          tom: str | None = None) -> tuple[str | None, list[str]]:
    """(falante, pistas) de UM segmento; None quando nenhuma pista decide."""
    pistas = []
    if nome_do_plano:  # qualquer falante declarado com close próprio (um segundo jornalista, por exemplo)
        pistas.append("plano")
        return nome_do_plano, pistas
    texto = _norm(seg["texto"]).strip()
    pontos = {pergunta: 0.0, responde: 0.0}
    if tom in ("AGUDA", "GRAVE"):
        pontos[pergunta if tom == "AGUDA" else responde] += 1
        pistas.append(f"tom {tom.lower()}")
    if seg["texto"].rstrip().endswith("?"):
        pontos[pergunta] += 1
        pistas.append("pergunta")
    if any(re.match(rf"^\W*{re.escape(v)}\b", texto) for v in VOCATIVOS):
        pontos[pergunta] += 0.5
        pistas.append("vocativo")
    if nome_curto and re.search(rf"\b{re.escape(nome_curto)}\b", texto):
        pontos[responde] += 1
        pistas.append(f"chama '{nome_curto}'")
    if pontos[pergunta] == pontos[responde]:
        return None, pistas
    return max(pontos, key=pontos.get), pistas


def montar_turnos(segs: list[dict], nomes_de_plano: list[str | None], pergunta: str, responde: str,
                  vts: list[tuple[float, float]], tons: list[str | None] | None = None) -> list[dict]:
    nome_curto = _norm(pergunta.split()[0])
    rotulos: list[tuple[str | None, list[str]]] = []
    for i, s in enumerate(segs):
        meio = (s["inicio_s"] + s["fim_s"]) / 2
        if any(a <= meio < b for a, b in vts):
            rotulos.append(("Narração (VT)", ["VT declarado"]))
        else:
            rotulos.append(votar(s, nomes_de_plano[i], pergunta, responde, nome_curto, tons[i] if tons else None))
    falantes: list[str] = []
    for i, (f, _) in enumerate(rotulos):
        falantes.append(f or (falantes[i - 1] if i else pergunta))
    turnos: list[dict] = []
    for s, f, (rot, pistas) in zip(segs, falantes, rotulos, strict=True):
        if turnos and turnos[-1]["falante"] == f:
            t = turnos[-1]
            t["fim_s"] = s["fim_s"]
            t["segmentos"] += 1
            t["sem_pista"] += rot is None
            t["pistas"] = sorted(set(t["pistas"]) | set(pistas))
        else:
            turnos.append({"inicio_s": s["inicio_s"], "fim_s": s["fim_s"], "falante": f, "segmentos": 1,
                           "sem_pista": int(rot is None), "pistas": sorted(set(pistas)),
                           "nasceu_sem_pista": rot is None, "comeco": s["texto"].strip()[:90]})
    for x, y in zip(turnos, turnos[1:], strict=False):
        x["fim_s"] = y["inicio_s"]
    for t in turnos:
        curto = t["fim_s"] - t["inicio_s"] < 3.0 and t["segmentos"] == 1
        t["confianca"] = "duvida" if (curto or t["nasceu_sem_pista"] or t["sem_pista"] == t["segmentos"]) else "rascunho"
    return turnos


def folha_de_turnos(caso: Path, turnos: list[dict], destino: Path) -> None:
    from PIL import Image, ImageDraw
    video = _video(caso)
    lw, lh, cols = 384, 216, 6
    linhas = (len(turnos) + cols - 1) // cols
    grade = Image.new("RGB", (cols * lw, linhas * (lh + 46)), (12, 12, 12))
    d = ImageDraw.Draw(grade)
    tmp = destino.parent / "_quadro.jpg"
    for n, t in enumerate(turnos):
        # quadro 1 s depois do começo: é a primeira frase do turno que mais erra
        im = _quadro(video, min(t["inicio_s"] + 1.0, (t["inicio_s"] + t["fim_s"]) / 2), lw, lh, tmp)
        x, y = (n % cols) * lw, (n // cols) * (lh + 46)
        if im:
            grade.paste(im, (x, y))
        cor = (255, 200, 60) if t["confianca"] == "duvida" else (235, 235, 235)
        d.text((x + 6, y + lh + 3), f"{n + 1:02d} {_mmss(t['inicio_s'])} {t['falante']}"[:40], font=_fonte(18), fill=cor)
        d.text((x + 6, y + lh + 24), t["comeco"][:44], font=_fonte(16), fill=(150, 150, 150))
    tmp.unlink(missing_ok=True)
    grade.save(destino, quality=82)
    print(f"✓ folha de turnos → {destino.name}")


def turnos_cmd(a) -> int:
    caso = cfg.pasta_do_caso(a.slug)
    meta = json.loads((caso / "CASO.json").read_text(encoding="utf-8"))
    declarados = {f["nome"]: f["papel"] for f in meta["falantes"]}
    for nome in (a.pergunta, a.responde) + (("Narração (VT)",) if a.vt else ()):
        if nome not in declarados:
            print(f"✗ '{nome}' não está declarado no CASO.json")
            return 1
    segs = json.loads((caso / "transcricao" / "transcricao.json").read_text(encoding="utf-8"))["segmentos"]
    nomes_de_plano: list[str | None] = [None] * len(segs)
    p_planos, p_rot = caso / "transcricao" / "planos.json", caso / "transcricao" / "planos-rotulos.json"
    if p_planos.exists() and p_rot.exists():
        planos_doc = json.loads(p_planos.read_text(encoding="utf-8"))
        rotulos = json.loads(p_rot.read_text(encoding="utf-8"))
        ruins = {v for v in rotulos.values() if v not in declarados and v != "ambiguo"}
        if ruins:
            print(f"✗ planos-rotulos.json tem nome que não está no CASO.json (ou não foi preenchido): {sorted(ruins)}")
            return 1
        grupos = plano_de_cada_segmento(segs, planos_doc["rotulo_por_quadro"], planos_doc["fps"])
        nomes_de_plano = [rotulos.get(str(g)) if g is not None else None for g in grupos]
        nomes_de_plano = [None if n == "ambiguo" else n for n in nomes_de_plano]
    else:
        print("⚠ sem planos rotulados: o rascunho vai só pelo texto, e vai errar mais. Rode o subcomando `planos`.")
    tons = None
    if a.tom:
        marcas = {}
        for linha in Path(a.tom).read_text(encoding="utf-8").splitlines()[1:]:
            partes = linha.split("\t")
            if len(partes) >= 4:
                marcas[round(float(partes[1]), 2)] = partes[3]
        tons = [marcas.get(round(s["inicio_s"], 2)) for s in segs]
    vts = [tuple(float(x) for x in v.split("-")) for v in a.vt]
    turnos = montar_turnos(segs, nomes_de_plano, a.pergunta, a.responde, vts, tons)

    saida = {"caso": a.slug,
             "metodo": "RASCUNHO de ferramentas/rascunho-de-turnos.py (plano + texto + VT declarado). "
                       "⛔ Não é o falantes.json: conferir cada turno no vídeo antes de copiar.",
             "turnos": [{k: t[k] for k in ("inicio_s", "fim_s", "falante", "confianca", "pistas")} for t in turnos]}
    (caso / "transcricao" / "falantes.rascunho.json").write_text(
        json.dumps(saida, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    tempo: dict[str, float] = {}
    for t in turnos:
        tempo[t["falante"]] = tempo.get(t["falante"], 0.0) + t["fim_s"] - t["inicio_s"]
    L = [f"# Rascunho de turnos · {a.slug}", "",
         "⛔ **Rascunho.** Confira cada turno no vídeo (a folha de turnos ajuda) antes de copiar para `falantes.json`. "
         "O erro mais comum do método é a **primeira frase da resposta** ficar com quem perguntou.", "",
         "Tempo por falante no rascunho: " + " · ".join(f"{k} {_mmss(v)}" for k, v in tempo.items()), "",
         "| # | Início | Fim | Falante | Confiança | Pistas | Começa com |", "|---:|---|---|---|---|---|---|"]
    for n, t in enumerate(turnos, 1):
        L.append(f"| {n} | {_mmss(t['inicio_s'])} | {_mmss(t['fim_s'])} | {t['falante']} | "
                 f"{'⚠️ dúvida' if t['confianca'] == 'duvida' else 'rascunho'} | {', '.join(t['pistas']) or '·'} | {t['comeco']} |")
    (caso / "transcricao" / "RASCUNHO_DE_TURNOS.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    duvidas = sum(t["confianca"] == "duvida" for t in turnos)
    print(f"✓ {len(turnos)} turnos no rascunho ({duvidas} em dúvida) → casos/{a.slug}/transcricao/RASCUNHO_DE_TURNOS.md")
    if a.folha:
        folha_de_turnos(caso, turnos, caso / "transcricao" / "folha-de-turnos.jpg")
    return 0


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    pl = sub.add_parser("planos")
    pl.add_argument("slug")
    pl.add_argument("--grupos", type=int, default=16)
    tu = sub.add_parser("turnos")
    tu.add_argument("slug")
    tu.add_argument("--pergunta", required=True, help="quem pergunta (o jornalista)")
    tu.add_argument("--responde", required=True, help="quem responde (o candidato)")
    tu.add_argument("--vt", action="append", default=[], metavar="INICIO-FIM")
    tu.add_argument("--tom", default=None, help="TSV do medir-tom.py (⚠️ não serve para Lula)")
    tu.add_argument("--folha", action="store_true")
    a = p.parse_args()
    return planos(a.slug, a.grupos) if a.cmd == "planos" else turnos_cmd(a)


if __name__ == "__main__":
    raise SystemExit(main())
