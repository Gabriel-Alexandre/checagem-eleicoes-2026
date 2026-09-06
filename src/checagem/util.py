"""Utilidades compartilhadas: hash, ffprobe, tempo, JSON e saída de terminal."""

from __future__ import annotations

import hashlib
import json
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Any


class ErroDeExecucao(RuntimeError):
    """Erro previsto do pipeline. A CLI transforma em mensagem, não em stack trace."""


# ─────────────────────────────────────────────────────────────────────
# Terminal
# ─────────────────────────────────────────────────────────────────────


def passo(texto: str) -> None:
    print(f"\n\033[1m▶ {texto}\033[0m", flush=True)


def ok(texto: str) -> None:
    print(f"  \033[32m✓\033[0m {texto}", flush=True)


def aviso(texto: str) -> None:
    print(f"  \033[33m⚠\033[0m {texto}", flush=True)


def erro(texto: str) -> None:
    print(f"  \033[31m✗\033[0m {texto}", file=sys.stderr, flush=True)


def info(texto: str) -> None:
    print(f"  · {texto}", flush=True)


# ─────────────────────────────────────────────────────────────────────
# Processos externos
# ─────────────────────────────────────────────────────────────────────


def exigir_binario(nome: str, como_instalar: str) -> str:
    caminho = shutil.which(nome)
    if not caminho:
        raise ErroDeExecucao(
            f"'{nome}' não está no PATH. Instale com: {como_instalar}\n"
            "  No Windows com scoop, os shims podem não estar no PATH do shell:\n"
            '    export PATH="$HOME/scoop/shims:$PATH"'
        )
    return caminho


def rodar(cmd: list[str], *, silencioso: bool = False) -> subprocess.CompletedProcess[str]:
    r = subprocess.run(cmd, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if r.returncode != 0 and not silencioso:
        raise ErroDeExecucao(
            f"comando falhou ({r.returncode}): {' '.join(cmd[:6])} ...\n{(r.stderr or '')[-2000:]}"
        )
    return r


# ─────────────────────────────────────────────────────────────────────
# Mídia
# ─────────────────────────────────────────────────────────────────────


def sha256_do_arquivo(caminho: Path) -> str:
    h = hashlib.sha256()
    with caminho.open("rb") as f:
        for bloco in iter(lambda: f.read(1024 * 1024), b""):
            h.update(bloco)
    return h.hexdigest()


def sondar(caminho: Path) -> dict[str, Any]:
    """ffprobe -> dicionário com o que o projeto precisa saber do arquivo."""
    exigir_binario("ffprobe", "scoop install ffmpeg (Windows) · apt install ffmpeg · brew install ffmpeg")
    r = rodar([
        "ffprobe", "-v", "error", "-print_format", "json",
        "-show_format", "-show_streams", str(caminho),
    ])
    dados = json.loads(r.stdout)
    video = next((s for s in dados["streams"] if s["codec_type"] == "video"), None)
    audio = next((s for s in dados["streams"] if s["codec_type"] == "audio"), None)
    if video is None:
        raise ErroDeExecucao(f"{caminho.name} não tem faixa de vídeo")
    return {
        "duracao_s": float(dados["format"]["duration"]),
        "bytes": int(dados["format"]["size"]),
        "largura": int(video["width"]),
        "altura": int(video["height"]),
        "fps": _fracao(video.get("r_frame_rate", "0/1")),
        "codec_video": video.get("codec_name", "?"),
        "codec_audio": (audio or {}).get("codec_name"),
        "audio_sample_rate": int((audio or {}).get("sample_rate", 0)) or None,
        "audio_canais": (audio or {}).get("channels"),
    }


def _fracao(texto: str) -> float:
    if "/" in texto:
        a, b = texto.split("/", 1)
        return round(float(a) / float(b), 4) if float(b) else 0.0
    return float(texto)


# ─────────────────────────────────────────────────────────────────────
# Tempo
# ─────────────────────────────────────────────────────────────────────


def hms(segundos: float) -> str:
    """3661.5 -> '01:01:01'. Usado no card e no relatório."""
    s = int(round(segundos))
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def ms(segundos: float) -> str:
    """3661.5 -> '61:01'. Formato curto para vídeos de menos de uma hora."""
    s = int(round(segundos))
    return f"{s // 60:02d}:{s % 60:02d}"


# ─────────────────────────────────────────────────────────────────────
# JSON
# ─────────────────────────────────────────────────────────────────────


def ler_json(caminho: Path) -> Any:
    if not caminho.exists():
        raise ErroDeExecucao(f"arquivo não encontrado: {caminho}")
    with caminho.open(encoding="utf-8") as f:
        return json.load(f)


def escrever_json(caminho: Path, dados: Any) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    with caminho.open("w", encoding="utf-8", newline="\n") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)
        f.write("\n")


def hex_para_rgb(cor: str) -> tuple[int, int, int]:
    cor = cor.lstrip("#")
    return tuple(int(cor[i:i + 2], 16) for i in (0, 2, 4))  # type: ignore[return-value]
