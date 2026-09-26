"""Baixa a peça de um caso e registra POR QUAL CAMINHO ela chegou.

    python ferramentas/baixar-peca.py <pedido.json> <destino.mp4>

O pedido (`casos/<slug>/fonte/PEDIDO_NUVEM.json`) traz a `url` principal e, opcionalmente,
`alternativas`: outras publicações da MESMA peça (a cópia oficial do veículo, por exemplo).

A ordem das tentativas é:

  1. yt-dlp direto na URL principal;
  2. se ela é do YouTube e o YouTube recusa (o que acontece em IP de datacenter, com a mensagem
     "Sign in to confirm you're not a bot"), espelhos públicos do mesmo vídeo (Invidious e
     Piped), que servem os MESMOS fluxos do YouTube pelo mesmo identificador;
  3. yt-dlp em cada URL de `alternativas`.

🔴 O caminho que funcionou vai para `origem-download.json`, ao lado do vídeo. Isto não é
detalhe técnico: é procedência. Uma cópia de outro canal, ou a do próprio veículo, pode ter
começo e fim diferentes, e isso desloca todos os tempos do caso. O `CASO.json` declara qual
arquivo foi checado, e o `sha256` amarra a checagem a ele.
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import urllib.request
from pathlib import Path

INVIDIOUS = [
    "https://inv.nadeko.net", "https://invidious.nerdvpn.de", "https://yewtu.be",
    "https://invidious.f5.si", "https://iv.melmac.space", "https://inv.tux.pizza",
    "https://invidious.privacyredirect.com", "https://invidious.materialio.us",
    "https://yt.artemislena.eu", "https://invidious.protokolla.fi", "https://iv.ggtyler.dev",
    "https://invidious.jing.rocks", "https://invidious.lunar.icu",
]
PIPED = [
    "https://pipedapi.kavin.rocks", "https://pipedapi.adminforge.de", "https://api.piped.yt",
    "https://pipedapi.r4fo.com", "https://pipedapi.leptons.xyz",
]
AGENTE = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0 Safari/537.36"


def _id_youtube(url: str) -> str | None:
    m = re.search(r"(?:v=|youtu\.be/|/shorts/|/live/)([A-Za-z0-9_-]{11})", url)
    return m.group(1) if m else None


def _json(url: str, tempo: int = 30):
    req = urllib.request.Request(url, headers={"User-Agent": AGENTE})
    with urllib.request.urlopen(req, timeout=tempo) as r:  # noqa: S310
        return json.loads(r.read().decode("utf-8"))


def _baixar_arquivo(url: str, destino: Path) -> bool:
    r = subprocess.run(["curl", "-fL", "--retry", "3", "-A", AGENTE, "-o", str(destino), url])
    return r.returncode == 0 and destino.exists() and destino.stat().st_size > 1_000_000


def _juntar(video: Path, audio: Path, destino: Path) -> bool:
    r = subprocess.run(["ffmpeg", "-v", "error", "-i", str(video), "-i", str(audio),
                        "-c", "copy", "-map", "0:v:0", "-map", "1:a:0", "-y", str(destino)])
    return r.returncode == 0


def _duracao(caminho: Path) -> float:
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of",
                        "default=nw=1:nk=1", str(caminho)], capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return 0.0


def _yt_dlp(url: str, destino: Path) -> bool:
    for cliente in ("", "youtube:player_client=web", "youtube:player_client=tv_simply,web_safari",
                    "youtube:player_client=mweb", "youtube:player_client=web_embedded"):
        extra = ["--extractor-args", cliente] if cliente else []
        r = subprocess.run([
            "yt-dlp", "--no-playlist", *extra,
            "-f", "bv*[height<=1080][ext=mp4]+ba[ext=m4a]/bv*[height<=1080]+ba/b[height<=1080]/b",
            "--merge-output-format", "mp4", "-o", str(destino), url,
        ])
        if r.returncode == 0 and destino.exists():
            return True
        if "youtube" not in url and "youtu.be" not in url:
            break
    return False


def _invidious(vid: str, destino: Path) -> tuple[bool, str, dict]:
    tmp = destino.parent
    for base in INVIDIOUS:
        try:
            meta = _json(f"{base}/api/v1/videos/{vid}")
        except Exception as e:
            print(f"  invidious {base}: {e}")
            continue
        fmts = meta.get("adaptiveFormats", [])
        videos = [f for f in fmts if f.get("type", "").startswith("video/mp4")
                  and int(re.sub(r"\D", "", f.get("resolution", "0") or "0") or 0) <= 1080]
        audios = [f for f in fmts if f.get("type", "").startswith("audio/mp4")]
        videos.sort(key=lambda f: int(re.sub(r"\D", "", f.get("resolution", "0") or "0") or 0), reverse=True)
        audios.sort(key=lambda f: int(f.get("bitrate", 0) or 0), reverse=True)
        for v in videos[:2]:
            for a in audios[:1]:
                vurl = f"{base}/latest_version?id={vid}&itag={v['itag']}&local=true"
                aurl = f"{base}/latest_version?id={vid}&itag={a['itag']}&local=true"
                if (_baixar_arquivo(vurl, tmp / "_v.mp4") and _baixar_arquivo(aurl, tmp / "_a.m4a")
                        and _juntar(tmp / "_v.mp4", tmp / "_a.m4a", destino)):
                    return True, f"invidious {base} itag {v['itag']}+{a['itag']}", meta
    return False, "", {}


def _piped(vid: str, destino: Path) -> tuple[bool, str, dict]:
    tmp = destino.parent
    for base in PIPED:
        try:
            meta = _json(f"{base}/streams/{vid}")
        except Exception as e:
            print(f"  piped {base}: {e}")
            continue
        videos = [s for s in meta.get("videoStreams", []) if s.get("videoOnly")
                  and "mp4" in (s.get("mimeType") or "") and (s.get("height") or 0) <= 1080]
        audios = [s for s in meta.get("audioStreams", []) if "mp4" in (s.get("mimeType") or "")]
        videos.sort(key=lambda s: s.get("height") or 0, reverse=True)
        audios.sort(key=lambda s: s.get("bitrate") or 0, reverse=True)
        for v in videos[:2]:
            for a in audios[:1]:
                if (_baixar_arquivo(v["url"], tmp / "_v.mp4") and _baixar_arquivo(a["url"], tmp / "_a.m4a")
                        and _juntar(tmp / "_v.mp4", tmp / "_a.m4a", destino)):
                    return True, f"piped {base} {v.get('quality')}", meta
    return False, "", {}


def main() -> int:
    pedido = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    destino = Path(sys.argv[2])
    destino.parent.mkdir(parents=True, exist_ok=True)
    url = pedido["url"]
    registro: dict = {"url_pedida": url, "tentativas": []}

    ok, caminho, meta = _yt_dlp(url, destino), "yt-dlp", {}
    registro["tentativas"].append({"caminho": "yt-dlp", "url": url, "ok": ok})
    vid = _id_youtube(url)
    if not ok and vid:
        ok, caminho, meta = _invidious(vid, destino)
        registro["tentativas"].append({"caminho": "invidious", "ok": ok, "detalhe": caminho})
        if not ok:
            ok, caminho, meta = _piped(vid, destino)
            registro["tentativas"].append({"caminho": "piped", "ok": ok, "detalhe": caminho})
    if ok:
        registro["url_obtida"] = url
    for alt in pedido.get("alternativas", []) if not ok else []:
        ok = _yt_dlp(alt, destino)
        registro["tentativas"].append({"caminho": "yt-dlp", "url": alt, "ok": ok})
        if ok:
            caminho, registro["url_obtida"] = "yt-dlp", alt
            break

    # 🔴 Um arquivo que baixou não é, por isso, a peça. A cópia "oficial" que chegou na primeira
    # tentativa deste caso era um corte vertical de 2min44s. Abaixo da duração mínima do pedido,
    # o arquivo é descartado e registrado como tal, e a próxima alternativa é tentada.
    minima = float(pedido.get("duracao_minima_s", 0))
    while ok and minima and _duracao(destino) < minima:
        registro["tentativas"][-1]["descartado"] = (
            f"duração {_duracao(destino):.0f}s abaixo da mínima de {minima:.0f}s: não é a íntegra")
        destino.unlink()
        ok = False
        restantes = [u for u in pedido.get("alternativas", [])
                     if u not in [t.get("url") for t in registro["tentativas"]]]
        for alt in restantes:
            ok = _yt_dlp(alt, destino)
            registro["tentativas"].append({"caminho": "yt-dlp", "url": alt, "ok": ok})
            if ok:
                caminho, registro["url_obtida"] = "yt-dlp", alt
                break

    registro["ok"] = ok
    registro["caminho"] = caminho if ok else None
    if meta:
        registro["metadados_do_espelho"] = {k: meta.get(k) for k in (
            "title", "author", "uploader", "published", "uploadDate", "lengthSeconds", "duration",
            "description") if k in meta}
    destino.with_name("origem-download.json").write_text(
        json.dumps(registro, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(json.dumps({k: v for k, v in registro.items() if k != "metadados_do_espelho"}, ensure_ascii=False, indent=2))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
