"""Baixa os comentários públicos de um vídeo publicado, para a revisão do próprio projeto.

    python ferramentas/baixar-comentarios.py <pedido.json>

Lê `comentarios_de` do pedido e escreve `comentarios_<n>.json` na pasta corrente.

⚠️ Comentário é dado de terceiro. Ele serve para o projeto ouvir o público (contestação,
defeito de leitura na tela, pedido de fonte), e ⛔ não entra no git: o que entra é o que o
projeto decidiu fazer com ele, escrito com as próprias palavras.
"""

from __future__ import annotations

import json
import subprocess
import sys
import urllib.parse
import urllib.request
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from importlib import import_module  # noqa: E402

bp = import_module("baixar-peca")


def _invidious(vid: str) -> list[dict]:
    for base in bp.INVIDIOUS:
        comentarios: list[dict] = []
        cont = None
        try:
            for _ in range(40):
                url = f"{base}/api/v1/comments/{vid}?sort_by=new"
                if cont:
                    url += "&continuation=" + urllib.parse.quote(cont)
                dados = bp._json(url)
                for c in dados.get("comments", []):
                    comentarios.append({"texto": c.get("content"), "curtidas": c.get("likeCount"),
                                        "publicado": c.get("publishedText"),
                                        "respostas": (c.get("replies") or {}).get("replyCount", 0)})
                cont = dados.get("continuation")
                if not cont:
                    break
        except Exception as e:
            print(f"  invidious {base}: {e}")
            if not comentarios:
                continue
        if comentarios:
            return comentarios
    return []


def main() -> int:
    pedido = json.loads(Path(sys.argv[1]).read_text(encoding="utf-8"))
    for i, url in enumerate(pedido.get("comentarios_de", [])):
        saida = Path(f"comentarios_{i}.json")
        r = subprocess.run(["yt-dlp", "--skip-download", "--write-comments", "--write-info-json",
                            "-o", f"comentarios_{i}_ytdlp", url])
        if r.returncode == 0 and Path(f"comentarios_{i}_ytdlp.info.json").exists():
            info = json.loads(Path(f"comentarios_{i}_ytdlp.info.json").read_text(encoding="utf-8"))
            dados = [{"texto": c.get("text"), "curtidas": c.get("like_count")} for c in info.get("comments", [])]
        else:
            vid = bp._id_youtube(url)
            dados = _invidious(vid) if vid else []
        saida.write_text(json.dumps({"url": url, "comentarios": dados}, ensure_ascii=False, indent=2),
                         encoding="utf-8")
        print(f"{url}: {len(dados)} comentários")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
