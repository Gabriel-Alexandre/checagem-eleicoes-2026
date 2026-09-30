"""PASSO 1 — preparar a mídia.

Três coisas, todas determinísticas:

  registrar   mede e assina o arquivo de origem (sha256, duração, resolução, fps)
  audio       extrai a faixa de áudio em 16 kHz mono, que é o que o whisper.cpp quer
  faixas      mede as faixas pretas do vídeo (a imagem útil)
  recortar    corta um trecho, mantendo o tempo absoluto anotado; com `--cortar-faixas`,
              tira as faixas pretas e leva a imagem a 1920x1080

🔴 O recorte guarda `origem_inicio_s`. Sem isso, um card checado num recorte de 5 min
não sabe voltar para o minuto certo da peça inteira, e a transcrição do recorte vira
uma segunda verdade que ninguém consegue casar com a primeira.
"""

from __future__ import annotations

import argparse
import re
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


def _filtro_de_enquadramento(largura: int, altura: int) -> str | None:
    """Filtro que põe um vídeo de outra proporção dentro do quadro de 1920x1080.

    🔴 A imagem original NÃO é cortada nem deformada: ela é escalada para caber inteira na
    altura e centralizada. O espaço que sobra ao lado é preenchido por uma cópia desfocada e
    escurecida do próprio vídeo, e não por barra preta, para o espectador não confundir a borda
    com parte da imagem. Existe porque a peça oficial pode vir vertical (corte de rede social) e
    as cartelas são quadros inteiros de 1920x1080.
    """
    if (largura, altura) == (cfg.LARGURA, cfg.ALTURA):
        return None
    W, H = cfg.LARGURA, cfg.ALTURA
    return (f"[0:v]split=2[fundo][frente];"
            f"[fundo]scale={W}:{H}:force_original_aspect_ratio=increase,crop={W}:{H},"
            f"boxblur=40:4,eq=brightness=-0.18[fundo2];"
            f"[frente]scale=-2:{H}:force_original_aspect_ratio=decrease[frente2];"
            f"[fundo2][frente2]overlay=(W-w)/2:(H-h)/2,setsar=1,format=yuv420p[v]")


# ─────────────────────────────────────────────────────────────────────
# Faixas pretas
# ─────────────────────────────────────────────────────────────────────

# A borda entre a faixa preta e a imagem é mole: a compressão espalha 3 a 4 colunas de cinza.
# Sem uma margem para dentro, sobra uma linha escura no quadro final, e é justo o que o
# espectador vê como "faixa preta". Medido na sabatina de Flávio: a coluna 172 tem luma 33.
MARGEM_DA_BORDA_PX = 4
AMOSTRAS_DE_FAIXA = 24


def caixa_sem_faixas(largura: int, altura: int, x1: int, x2: int, y1: int, y2: int,
                     *, margem: int = MARGEM_DA_BORDA_PX) -> dict[str, int]:
    """A maior caixa 16:9 que fica inteira dentro da imagem, sem nenhum pixel de faixa.

    `x1..x2` e `y1..y2` são a menor e a maior coluna e linha com conteúdo, somadas sobre várias
    amostras (uma cena escura sozinha subestimaria a imagem). A margem só se aplica no lado em
    que existe faixa: a borda do próprio arquivo não é mole.
    """
    esq = margem if x1 > 0 else 0
    dir_ = margem if x2 < largura - 1 else 0
    topo = margem if y1 > 0 else 0
    base = margem if y2 < altura - 1 else 0
    x, y = x1 + esq, y1 + topo
    w, h = (x2 - dir_) - x + 1, (y2 - base) - y + 1
    # 16:9 exato, centrado e par (yuv420p exige dimensão par)
    if w * 9 > h * 16:
        novo_w = (h * 16 // 9) // 2 * 2
        x += (w - novo_w) // 2
        w = novo_w
    else:
        novo_h = (w * 9 // 16) // 2 * 2
        y += (h - novo_h) // 2
        h = novo_h
    return {"x": x // 2 * 2, "y": y // 2 * 2, "w": w, "h": h}


def medir_faixas(video: Path, amostras: int = AMOSTRAS_DE_FAIXA) -> dict:
    """Mede a imagem útil com `cropdetect` em várias cenas e devolve a caixa segura."""
    exigir_binario("ffmpeg", "scoop install ffmpeg")
    dados = sondar(video)
    duracao = dados["duracao_s"]
    x1 = y1 = 10**9
    x2 = y2 = -1
    for i in range(amostras):
        ponto = duracao * (i + 0.5) / amostras
        r = rodar(["ffmpeg", "-hide_banner", "-ss", f"{ponto:.2f}", "-i", str(video), "-t", "2",
                   "-vf", "cropdetect=limit=24:round=2:reset=0", "-an", "-f", "null", "-"],
                  silencioso=True)
        achados = re.findall(r"x1:(\d+) x2:(\d+) y1:(\d+) y2:(\d+)", r.stderr or "")
        if not achados:
            continue
        a, b, c, d = (int(v) for v in achados[-1])
        x1, x2, y1, y2 = min(x1, a), max(x2, b), min(y1, c), max(y2, d)
    if x2 < 0:
        raise ErroDeExecucao(f"não consegui medir as faixas de {video.name}")
    return {
        "original": f"{dados['largura']}x{dados['altura']}",
        "conteudo": {"x1": x1, "x2": x2, "y1": y1, "y2": y2},
        "margem_px": MARGEM_DA_BORDA_PX,
        "amostras": amostras,
        "corte": caixa_sem_faixas(dados["largura"], dados["altura"], x1, x2, y1, y2),
    }


def _filtro_de_faixas(corte: dict[str, int]) -> str:
    """Corta a caixa útil e leva a imagem a 1920x1080. A proporção da caixa já é 16:9."""
    return (f"crop={corte['w']}:{corte['h']}:{corte['x']}:{corte['y']},"
            f"scale={cfg.LARGURA}:{cfg.ALTURA}:flags=lanczos,setsar=1,format=yuv420p")


def recortar(slug: str, identificador: str, inicio_s: float, duracao_s: float,
             *, motivo: str = "", enquadrar: bool = False,
             cortar_faixas: bool = False) -> Path:
    """Corta um trecho do vídeo de origem, sem reencodar o que não precisa.

    O corte é reencodado no vídeo (para o primeiro frame ser exato) e copiado no áudio.
    Corte por cópia de fluxo cai no keyframe anterior, e aí o tempo do card erra.

    Com `enquadrar`, um vídeo que não é 1920x1080 é posto dentro desse quadro (ver
    `_filtro_de_enquadramento`), e o registro do recorte guarda como foi feito.

    Com `cortar_faixas`, as faixas pretas do arquivo são medidas (`medir_faixas`) e cortadas, e a
    imagem útil, que é 16:9, vai a 1920x1080 sem deformar. É o caminho de uma peça horizontal
    que veio com barras: a moldura e o card ficam sobre a imagem, não sobre o preto.
    """
    exigir_binario("ffmpeg", "scoop install ffmpeg")
    if enquadrar and cortar_faixas:
        raise ErroDeExecucao("--enquadrar e --cortar-faixas são caminhos diferentes: escolha um")
    caso = cfg.pasta_do_caso(slug)
    origem = _video_de_origem(caso)
    saida = caso / "recortes" / f"{identificador}.mp4"
    saida.parent.mkdir(parents=True, exist_ok=True)

    passo(f"PASSO 1 · recortar · {identificador} · {hms(inicio_s)} + {duracao_s:.0f}s")
    original = sondar(origem)
    faixas = medir_faixas(origem) if cortar_faixas else None
    filtro = _filtro_de_enquadramento(original["largura"], original["altura"]) if enquadrar else None
    if filtro:
        info(f"enquadrando {original['largura']}x{original['altura']} em {cfg.LARGURA}x{cfg.ALTURA}, "
             "sem cortar a imagem original")
    if faixas:
        c = faixas["corte"]
        info(f"faixas pretas: imagem útil {c['w']}x{c['h']} em x={c['x']} y={c['y']} "
             f"(margem de {faixas['margem_px']}px para dentro da borda mole)")
    rodar([
        "ffmpeg", "-v", "error",
        "-ss", f"{inicio_s:.3f}", "-i", str(origem), "-t", f"{duracao_s:.3f}",
        *(["-filter_complex", filtro, "-map", "[v]", "-map", "0:a?"] if filtro else []),
        *(["-vf", _filtro_de_faixas(faixas["corte"])] if faixas else []),
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
    if filtro:
        registro["enquadramento"] = {
            "original": f"{original['largura']}x{original['altura']}",
            "como": "imagem inteira centralizada na altura, sem corte nem deformação; laterais com "
                    "cópia desfocada e escurecida do próprio vídeo",
            "filtro": filtro,
        }
    if faixas:
        registro["enquadramento"] = {
            "original": faixas["original"],
            "como": "faixas pretas cortadas (medidas por cropdetect em várias cenas, com margem "
                    "para dentro da borda mole) e a imagem útil, 16:9, escalada a 1920x1080 sem "
                    "deformar; nenhum pixel de faixa fica no quadro",
            "corte": faixas["corte"],
            "conteudo_medido": faixas["conteudo"],
            "filtro": _filtro_de_faixas(faixas["corte"]),
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
    sub.add_parser("faixas", help="mede as faixas pretas e mostra a caixa de corte")
    a = sub.add_parser("audio")
    a.add_argument("--recorte", default=None)
    c = sub.add_parser("recortar")
    c.add_argument("id")
    c.add_argument("--inicio", type=float, required=True, help="segundos, na peça inteira")
    c.add_argument("--duracao", type=float, required=True, help="segundos")
    c.add_argument("--motivo", default="")
    c.add_argument("--enquadrar", action="store_true",
                   help="põe vídeo de outra proporção (vertical, por exemplo) dentro de 1920x1080")

    c.add_argument("--cortar-faixas", action="store_true",
                   help="mede e corta as faixas pretas, e leva a imagem útil a 1920x1080")

    args = p.parse_args(argv)
    if args.acao == "registrar":
        registrar(args.slug)
    elif args.acao == "faixas":
        f = medir_faixas(_video_de_origem(cfg.pasta_do_caso(args.slug)))
        passo(f"PASSO 1 · faixas pretas: {f['original']}")
        info(f"conteúdo em x {f['conteudo']['x1']}..{f['conteudo']['x2']} · "
             f"y {f['conteudo']['y1']}..{f['conteudo']['y2']} ({f['amostras']} amostras)")
        ok(f"caixa de corte {f['corte']}")
    elif args.acao == "audio":
        extrair_audio(args.slug, recorte=args.recorte)
    else:
        recortar(args.slug, args.id, args.inicio, args.duracao, motivo=args.motivo,
                 enquadrar=args.enquadrar, cortar_faixas=args.cortar_faixas)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
