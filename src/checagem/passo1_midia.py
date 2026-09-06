"""PASSO 1 — preparar a mídia.

Três coisas, todas determinísticas:

  registrar   mede e assina o arquivo de origem (sha256, duração, resolução, fps)
  audio       extrai a faixa de áudio em 16 kHz mono, que é o que o whisper.cpp quer
  recortar    corta um trecho, mantendo o tempo absoluto anotado

🔴 O recorte guarda `origem_inicio_s`. Sem isso, um card checado num recorte de 5 min
não sabe voltar para o minuto certo da peça inteira, e a transcrição do recorte vira
uma segunda verdade que ninguém consegue casar com a primeira.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from . import config as cfg
from .util import (
    ErroDeExecucao,
    escrever_json,
    exigir_binario,
    hms,
    info,
    ler_json,
    ok,
    passo,
    rodar,
    sha256_do_arquivo,
    sondar,
)


def _video_de_origem(caso: Path) -> Path:
    pasta = caso / "fonte"
    videos = sorted(
        p for p in pasta.glob("*")
        if p.suffix.lower() in {".mp4", ".mkv", ".mov", ".webm"}
    )
    if not videos:
        raise ErroDeExecucao(
            f"nenhum vídeo em {pasta}.\n"
            "  O arquivo de origem não entra no git (ver .gitignore): quem clona o repositório\n"
            "  baixa a peça pela url_oficial registrada em CASO.json e a põe aqui com o mesmo nome."
        )
    if len(videos) > 1:
        raise ErroDeExecucao(f"mais de um vídeo em {pasta}: {[v.name for v in videos]}")
    return videos[0]


# ─────────────────────────────────────────────────────────────────────


def registrar(slug: str) -> dict:
    """Mede e assina o arquivo de origem. Escreve fonte/MIDIA.json."""
    caso = cfg.pasta_do_caso(slug)
    video = _video_de_origem(caso)

    passo(f"PASSO 1 · registrar mídia — {video.name}")
    dados = sondar(video)
    info(f"{dados['largura']}x{dados['altura']} · {dados['fps']} fps · {hms(dados['duracao_s'])}")
    info("calculando sha256 (é o que prova que a checagem fala deste arquivo)...")
    assinatura = sha256_do_arquivo(video)

    manifesto = {
        "arquivo": video.name,
        "sha256": assinatura,
        "bytes": dados["bytes"],
        "duracao_s": round(dados["duracao_s"], 3),
        "largura": dados["largura"],
        "altura": dados["altura"],
        "fps": dados["fps"],
        "codec_video": dados["codec_video"],
        "codec_audio": dados["codec_audio"],
        "registrado_em": date.today().isoformat(),
    }
    escrever_json(caso / "fonte" / "MIDIA.json", manifesto)
    ok(f"sha256 {assinatura[:16]}… gravado em fonte/MIDIA.json")

    caminho_caso = caso / "CASO.json"
    if caminho_caso.exists():
        meta = ler_json(caminho_caso)
        meta["duracao_s"] = manifesto["duracao_s"]
        meta["midia"] = {
            k: manifesto[k]
            for k in ("arquivo", "sha256", "bytes", "largura", "altura", "fps",
                      "codec_video", "codec_audio")
        }
        escrever_json(caminho_caso, meta)
        ok("bloco `midia` do CASO.json sincronizado")
    return manifesto


# ─────────────────────────────────────────────────────────────────────


def extrair_audio(slug: str, *, recorte: str | None = None) -> Path:
    """Extrai WAV 16 kHz mono PCM — o formato nativo do whisper.cpp."""
    exigir_binario("ffmpeg", "scoop install ffmpeg · apt install ffmpeg · brew install ffmpeg")
    caso = cfg.pasta_do_caso(slug)

    if recorte:
        entrada = caso / "recortes" / f"{recorte}.mp4"
        saida = caso / "recortes" / f"{recorte}.wav"
    else:
        entrada = _video_de_origem(caso)
        saida = caso / "fonte" / f"{entrada.stem}.wav"

    if not entrada.exists():
        raise ErroDeExecucao(f"não encontrei {entrada}")

    passo(f"PASSO 1 · extrair áudio — {entrada.name}")
    rodar([
        "ffmpeg", "-v", "error", "-i", str(entrada),
        "-vn", "-ac", "1", "-ar", "16000", "-c:a", "pcm_s16le",
        "-y", str(saida),
    ])
    ok(f"{saida.relative_to(cfg.RAIZ)} · {saida.stat().st_size / 1e6:.1f} MB")
    return saida


# ─────────────────────────────────────────────────────────────────────


def recortar(slug: str, identificador: str, inicio_s: float, duracao_s: float,
             *, motivo: str = "") -> Path:
    """Corta um trecho do vídeo de origem, sem reencodar o que não precisa.

    O corte é reencodado no vídeo (para o primeiro frame ser exato) e copiado no áudio.
    Corte por cópia de fluxo cai no keyframe anterior, e aí o tempo do card erra.
    """
    exigir_binario("ffmpeg", "scoop install ffmpeg")
    caso = cfg.pasta_do_caso(slug)
    origem = _video_de_origem(caso)
    saida = caso / "recortes" / f"{identificador}.mp4"
    saida.parent.mkdir(parents=True, exist_ok=True)

    passo(f"PASSO 1 · recortar — {identificador} · {hms(inicio_s)} + {duracao_s:.0f}s")
    rodar([
        "ffmpeg", "-v", "error",
        "-ss", f"{inicio_s:.3f}", "-i", str(origem), "-t", f"{duracao_s:.3f}",
        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
        "-pix_fmt", "yuv420p", "-c:a", "aac", "-b:a", "192k",
        "-movflags", "+faststart", "-y", str(saida),
    ])
    medido = sondar(saida)

    registro = {
        "id": identificador,
        "arquivo": saida.name,
        "origem": origem.name,
        "origem_inicio_s": round(inicio_s, 3),
        "duracao_s": round(medido["duracao_s"], 3),
        "largura": medido["largura"],
        "altura": medido["altura"],
        "fps": medido["fps"],
        "motivo": motivo,
        "criado_em": date.today().isoformat(),
    }

    indice_path = caso / "recortes" / "RECORTES.json"
    indice = ler_json(indice_path) if indice_path.exists() else {"caso": slug, "recortes": []}
    indice["recortes"] = [r for r in indice["recortes"] if r["id"] != identificador]
    indice["recortes"].append(registro)
    indice["recortes"].sort(key=lambda r: r["origem_inicio_s"])
    escrever_json(indice_path, indice)

    ok(f"{saida.name} · {medido['largura']}x{medido['altura']} · {medido['duracao_s']:.2f}s")
    info(f"tempo absoluto do trecho na peça: {hms(inicio_s)} → {hms(inicio_s + medido['duracao_s'])}")
    return saida


# ─────────────────────────────────────────────────────────────────────


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem midia", description="PASSO 1 — preparar a mídia")
    p.add_argument("slug")
    sub = p.add_subparsers(dest="acao", required=True)
    sub.add_parser("registrar")
    a = sub.add_parser("audio")
    a.add_argument("--recorte", default=None)
    c = sub.add_parser("recortar")
    c.add_argument("id")
    c.add_argument("--inicio", type=float, required=True, help="segundos, na peça inteira")
    c.add_argument("--duracao", type=float, required=True, help="segundos")
    c.add_argument("--motivo", default="")

    args = p.parse_args(argv)
    if args.acao == "registrar":
        registrar(args.slug)
    elif args.acao == "audio":
        extrair_audio(args.slug, recorte=args.recorte)
    else:
        recortar(args.slug, args.id, args.inicio, args.duracao, motivo=args.motivo)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
