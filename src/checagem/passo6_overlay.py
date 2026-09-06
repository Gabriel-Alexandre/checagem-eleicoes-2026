"""PASSO 6 — montar o overlay.

Entrada:  alegacoes/alegacoes.json + checagens/checagens.json + CASO.json
Saída:    overlay/cartelas/*.png  (1920x1080 RGBA, um por card)
          overlay/plano.json      (quando cada cartela entra e sai)

🔑 A decisão de desenho que faz o resto ficar simples: **cada cartela é um quadro inteiro**
de 1920x1080 transparente, já com a moldura colorida e a tarja inferior desenhadas no lugar.
O ffmpeg então faz UM `overlay` em 0:0 por cartela, com `enable=between(t,a,b)`.

A alternativa — desenhar a moldura com quatro `drawbox` e a tarja com `drawtext` — dá quatro
filtros por card, texto sem quebra de linha de verdade e nenhum controle de acento. Este
projeto já tentou; o Pillow ganha em tudo que importa aqui.

⚠️ Corte seco, sem fade. É deliberado: fade exige entrada de vídeo em laço por cartela, o
grafo de filtro cresce por um ganho estético que, num card de checagem, ninguém sente falta.
Quem quiser fade tem o `--fade`, que paga esse custo.
"""

from __future__ import annotations

import argparse
from datetime import date
from pathlib import Path

from PIL import Image, ImageDraw

from . import config as cfg
from . import tipografia as tipo
from .util import (
    ErroDeExecucao,
    aviso,
    escrever_json,
    hex_para_rgb,
    info,
    ler_json,
    ms,
    ok,
    passo,
)

# ─────────────────────────────────────────────────────────────────────
# Desenho
# ─────────────────────────────────────────────────────────────────────


def _rgba(cor: str, alfa: int = 255) -> tuple[int, int, int, int]:
    r, g, b = hex_para_rgb(cor)
    return (r, g, b, alfa)


def _moldura(d: ImageDraw.ImageDraw, cor: str) -> None:
    """A cor do veredito em volta do quadro inteiro, com um degrau interno escuro
    para a moldura não sumir sobre cenário claro."""
    e = cfg.MOLDURA_ESPESSURA
    d.rectangle([0, 0, cfg.LARGURA - 1, cfg.ALTURA - 1], outline=_rgba(cor, 255), width=e)
    d.rectangle(
        [e, e, cfg.LARGURA - 1 - e, cfg.ALTURA - 1 - e],
        outline=(0, 0, 0, 90), width=2,
    )


def _selo(d: ImageDraw.ImageDraw) -> None:
    """Marca permanente no canto superior direito. Quem vê um corte do vídeo em outra
    plataforma precisa saber que aquilo tem metodologia escrita atrás."""
    f1 = tipo.fonte(24, "Bold")
    f2 = tipo.fonte(19, "Regular")
    larg = int(max(tipo.largura(cfg.SELO_TEXTO, f1), tipo.largura(cfg.SELO_SUBTEXTO, f2))) + 44
    alt = 78
    x = cfg.LARGURA - cfg.CARD_MARGEM_X - larg
    y = 42
    d.rounded_rectangle([x, y, x + larg, y + alt], radius=12, fill=(13, 16, 22, 200))
    d.text((x + 22, y + 16), cfg.SELO_TEXTO, font=f1, fill=cfg.COR_TEXTO)
    d.text((x + 22, y + 46), cfg.SELO_SUBTEXTO, font=f2, fill=cfg.COR_TEXTO_FRACO)


def desenhar_selo() -> Image.Image:
    """A marca permanente, sozinha num quadro inteiro.

    🔴 Ela é uma CAMADA À PARTE, e não parte da cartela, porque precisa estar na tela também
    nos intervalos entre um card e outro. Quando era desenhada dentro da cartela, sumia nos
    trechos sem checagem — e é justamente num corte desses que alguém pode republicar o vídeo
    sem a indicação de quem checou e onde estão as fontes.
    """
    img = Image.new("RGBA", (cfg.LARGURA, cfg.ALTURA), (0, 0, 0, 0))
    _selo(ImageDraw.Draw(img))
    return img


def _badge(d: ImageDraw.ImageDraw, x: int, y: int, veredito: cfg.Veredito) -> int:
    """Desenha a pastilha do veredito. Devolve o x onde ela termina."""
    f = tipo.fonte(cfg.TAM_BADGE, "Bold")
    texto = veredito.rotulo
    pad_x, alt = 20, 46
    larg = int(tipo.largura(texto, f)) + 2 * pad_x
    d.rounded_rectangle([x, y, x + larg, y + alt], radius=9, fill=_rgba(veredito.cor))
    d.text((x + pad_x, y + 9), texto, font=f, fill=veredito.cor_texto)
    return x + larg


def _fontes_em_uma_linha(fontes: list[dict]) -> str:
    if not fontes:
        return ""
    nomes: list[str] = []
    for f in fontes:
        nome = f["instituicao"]
        if nome not in nomes:
            nomes.append(nome)
    linha = "FONTES: " + " · ".join(nomes[:4])
    if len(nomes) > 4:
        linha += f"  (+{len(nomes) - 4})"
    # Duas fontes da mesma instituição colapsariam em um nome só, e o card passaria a
    # impressão de ter uma fonte quando tem duas. O número desfaz isso.
    if len(fontes) > len(nomes):
        linha += f"  ({len(fontes)} documentos)"
    return linha


def desenhar_cartela(*, veredito_chave: str, falante: str, tempo_s: float, id_alegacao: str,
                     frase: str, resumo: str, ressalva: str | None,
                     fontes: list[dict]) -> Image.Image:
    """Um quadro inteiro transparente com a moldura e a tarja já posicionadas."""
    v = cfg.VEREDITOS[veredito_chave]
    img = Image.new("RGBA", (cfg.LARGURA, cfg.ALTURA), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    f_meta = tipo.fonte(cfg.TAM_META, "Medium")
    f_cit = tipo.fonte(cfg.TAM_CITACAO, "Regular", italico=True)
    f_res = tipo.fonte(cfg.TAM_RESUMO, "SemiBold")
    f_rsv = tipo.fonte(cfg.TAM_FONTES + 2, "Medium")
    f_fnt = tipo.fonte(cfg.TAM_FONTES, "Medium")

    largura_texto = cfg.CARD_LARGURA - cfg.CARD_BARRA - 2 * cfg.CARD_PADDING_X

    linhas_cit = tipo.quebrar(f'"{frase}"', f_cit, largura_texto, max_linhas=2)
    linhas_res = tipo.quebrar(resumo, f_res, largura_texto, max_linhas=2)
    linhas_rsv = (tipo.quebrar(f"Ressalva: {ressalva}", f_rsv, largura_texto, max_linhas=2)
                  if ressalva else [])
    linha_fontes = _fontes_em_uma_linha(fontes)

    h_cit = tipo.altura_da_linha(f_cit)
    h_res = tipo.altura_da_linha(f_res)
    h_rsv = tipo.altura_da_linha(f_rsv)
    h_fnt = tipo.altura_da_linha(f_fnt)

    altura_card = (
        cfg.CARD_PADDING_Y
        + 46 + 18                                   # linha do badge
        + len(linhas_cit) * h_cit + 14
        + len(linhas_res) * h_res
        + (len(linhas_rsv) * h_rsv + 8 if linhas_rsv else 0)
        + (h_fnt + 12 if linha_fontes else 0)
        + cfg.CARD_PADDING_Y
    )

    x0 = cfg.CARD_MARGEM_X
    y0 = cfg.ALTURA - cfg.CARD_MARGEM_INFERIOR - altura_card
    x1 = x0 + cfg.CARD_LARGURA
    y1 = y0 + altura_card

    d.rounded_rectangle([x0, y0, x1, y1], radius=cfg.CARD_RAIO,
                        fill=cfg.CARD_FUNDO, outline=cfg.CARD_BORDA, width=2)
    # faixa colorida à esquerda, arredondada só do lado de fora
    d.rounded_rectangle([x0, y0, x0 + cfg.CARD_BARRA + cfg.CARD_RAIO, y1],
                        radius=cfg.CARD_RAIO, fill=_rgba(v.cor))
    d.rectangle([x0 + cfg.CARD_BARRA, y0, x0 + cfg.CARD_BARRA + cfg.CARD_RAIO, y1],
                fill=cfg.CARD_FUNDO)

    tx = x0 + cfg.CARD_BARRA + cfg.CARD_PADDING_X
    ty = y0 + cfg.CARD_PADDING_Y

    fim_badge = _badge(d, tx, ty, v)
    meta = f"{falante}  ·  {ms(tempo_s)}  ·  {id_alegacao}"
    d.text((fim_badge + 20, ty + 12), meta, font=f_meta, fill=cfg.COR_TEXTO_FRACO)
    ty += 46 + 18

    for linha in linhas_cit:
        d.text((tx, ty), linha, font=f_cit, fill=cfg.COR_CITACAO)
        ty += h_cit
    ty += 14

    for linha in linhas_res:
        d.text((tx, ty), linha, font=f_res, fill=cfg.COR_TEXTO)
        ty += h_res

    if linhas_rsv:
        ty += 8
        for linha in linhas_rsv:
            d.text((tx, ty), linha, font=f_rsv, fill=cfg.VEREDITOS["IMPRECISO"].cor)
            ty += h_rsv

    if linha_fontes:
        ty += 12
        d.text((tx, ty), linha_fontes, font=f_fnt, fill=cfg.COR_TEXTO_FRACO)

    _moldura(d, v.cor)
    return img


def desenhar_legenda(titulo: str, subtitulo: str) -> Image.Image:
    """Cartela de abertura: o que cada cor quer dizer. Sem ela, a moldura verde é decoração."""
    img = Image.new("RGBA", (cfg.LARGURA, cfg.ALTURA), (0, 0, 0, 0))
    d = ImageDraw.Draw(img)

    larg, alt = 1280, 566
    x0 = (cfg.LARGURA - larg) // 2
    y0 = (cfg.ALTURA - alt) // 2
    d.rounded_rectangle([x0, y0, x0 + larg, y0 + alt], radius=26,
                        fill=(10, 13, 18, 242), outline=(255, 255, 255, 40), width=2)

    f_tit = tipo.fonte(46, "Bold")
    f_sub = tipo.fonte(26, "Regular")
    f_item = tipo.fonte(30, "SemiBold")
    f_desc = tipo.fonte(24, "Regular")

    d.text((x0 + 56, y0 + 44), titulo, font=f_tit, fill=cfg.COR_TEXTO)
    for i, linha in enumerate(tipo.quebrar(subtitulo, f_sub, larg - 112, max_linhas=2)):
        d.text((x0 + 56, y0 + 106 + i * 34), linha, font=f_sub, fill=cfg.COR_TEXTO_FRACO)

    explicacao = {
        "VERDADEIRO": "confere com as fontes primárias",
        "IMPRECISO": "essência certa, número ou recorte errado",
        "INSUSTENTAVEL": "afirmado como fato, sem lastro nas fontes",
        "FALSO": "as fontes contradizem o que foi dito",
        "NAO_CHECAVEL": "opinião, promessa ou previsão",
    }
    # A coluna da descrição começa depois do rótulo MAIS LARGO, medido na própria fonte.
    # ⛔ Largura fixa aqui já fez "SEM COMPROVAÇÃO" escrever por cima da descrição.
    coluna = int(max(tipo.largura(cfg.VEREDITOS[k].rotulo, f_item) for k in explicacao)) + 46

    y = y0 + 190
    for chave, desc in explicacao.items():
        v = cfg.VEREDITOS[chave]
        d.rounded_rectangle([x0 + 56, y, x0 + 56 + 22, y + 40], radius=6, fill=_rgba(v.cor))
        d.text((x0 + 96, y + 4), v.rotulo, font=f_item, fill=cfg.COR_TEXTO)
        d.text((x0 + 96 + coluna, y + 8), desc, font=f_desc, fill=cfg.COR_TEXTO_FRACO)
        y += 56

    d.text((x0 + 56, y + 18), "Toda checagem tem no mínimo duas fontes independentes, "
           "listadas no repositório.", font=f_desc, fill=cfg.COR_TEXTO_FRACO)
    return img


# ─────────────────────────────────────────────────────────────────────
# Plano de tempo
# ─────────────────────────────────────────────────────────────────────


def _janelas(itens: list[dict], limite_s: float) -> list[dict]:
    """Calcula quando cada cartela entra e sai, sem deixar duas na tela ao mesmo tempo.

    A cartela quer entrar quando a frase começa e ficar até PERMANENCIA_S depois de a frase
    acabar. ⛔ Duas cartelas simultâneas é defeito, não estilo: o espectador não sabe a qual
    frase a moldura se refere.

    🔴 Por que isto é uma FILA e não um recorte. Duas alegações podem sair da **mesma frase** —
    "a dívida disparou 10 pontos, atingiu 82% do PIB" tem dois números que se conferem em séries
    diferentes, e a metodologia manda separá-los (§4.3). Com o mesmo `inicio_s`, cortar a primeira
    cartela no começo da segunda daria duração zero ou negativa. Então cada cartela entra no
    **máximo entre o começo da fala e o fim da cartela anterior**, e o atraso fica registrado no
    plano: card que aparece muito depois da frase que ele cita é defeito, e o validador precisa
    conseguir enxergá-lo.
    """
    itens = sorted(itens, key=lambda a: (a["inicio_s"], a["id"]))
    janelas: list[dict] = []
    cursor = 0.0

    for a in itens:
        entra = max(0.0, a["inicio_s"], cursor)
        natural = a["fim_s"] + cfg.PERMANENCIA_S - entra
        duracao = max(cfg.CARD_DURACAO_MIN_S, min(natural, cfg.CARD_DURACAO_MAX_S))
        sai = min(entra + duracao, limite_s)
        janelas.append({
            "id": a["id"],
            "entra_s": round(entra, 3),
            "sai_s": round(sai, 3),
            # Dois atrasos, e eles medem coisas diferentes.
            # `atraso_s` conta do INÍCIO da fala e serve de auditoria da fila.
            # `atraso_do_fim_s` conta de quando a fala ACABOU, e é o que o espectador sente:
            # um card que entra durante uma frase de 12s não está atrasado, ainda que o
            # primeiro número diga 12. É este segundo que dispara o aviso.
            "atraso_s": round(entra - a["inicio_s"], 3),
            "atraso_do_fim_s": round(max(0.0, entra - a["fim_s"]), 3),
            "curta": (sai - entra) < cfg.CARD_DURACAO_MIN_S - 0.001,
        })
        cursor = sai + cfg.FOLGA_ENTRE_CARDS_S

    return janelas


# ─────────────────────────────────────────────────────────────────────


def montar(slug: str, *, recorte: str | None = None, com_legenda: bool = True) -> Path:
    caso = cfg.pasta_do_caso(slug)
    meta = ler_json(caso / "CASO.json")
    alegacoes = ler_json(caso / "alegacoes" / _nome("alegacoes", recorte))
    checagens = ler_json(caso / "checagens" / _nome("checagens", recorte))

    por_id_checagem = {c["id"]: c for c in checagens["checagens"]}
    faltando = [a["id"] for a in alegacoes["alegacoes"] if a["id"] not in por_id_checagem]
    if faltando:
        raise ErroDeExecucao(
            f"{len(faltando)} alegações sem checagem: {', '.join(faltando[:8])}\n"
            "  Toda alegação extraída tem que receber veredito, inclusive NAO_CHECAVEL.\n"
            "  Deixar alegação sem checagem é escolher o que mostrar depois de saber o resultado."
        )

    if recorte:
        indice = ler_json(caso / "recortes" / "RECORTES.json")
        reg = next(r for r in indice["recortes"] if r["id"] == recorte)
        base_s, limite_s = float(reg["origem_inicio_s"]), float(reg["duracao_s"])
        alvo = f"recortes/{reg['arquivo']}"
    else:
        base_s, limite_s = 0.0, float(meta["duracao_s"])
        alvo = f"fonte/{meta['midia']['arquivo']}"

    passo(f"PASSO 6 · montar overlay — {len(alegacoes['alegacoes'])} cartelas sobre {alvo}")

    saida = caso / "overlay" / ("cartelas" if not recorte else f"cartelas-{recorte}")
    saida.mkdir(parents=True, exist_ok=True)
    for antigo in saida.glob("*.png"):
        antigo.unlink()

    # Tempo relativo ao arquivo que vai ser renderizado.
    relativos = [
        {"id": a["id"], "inicio_s": a["inicio_s"] - base_s, "fim_s": a["fim_s"] - base_s}
        for a in alegacoes["alegacoes"]
    ]
    fora = [r["id"] for r in relativos if r["fim_s"] < 0 or r["inicio_s"] > limite_s]
    if fora:
        aviso(f"{len(fora)} alegações caem fora do trecho renderizado e serão ignoradas: {fora[:5]}")
        relativos = [r for r in relativos if r["id"] not in fora]

    janelas = _janelas(relativos, limite_s)
    por_id_alegacao = {a["id"]: a for a in alegacoes["alegacoes"]}

    itens = []
    contagem: dict[str, int] = {}
    for j in janelas:
        a = por_id_alegacao[j["id"]]
        c = por_id_checagem[j["id"]]
        img = desenhar_cartela(
            veredito_chave=c["veredito"],
            falante=a["falante"],
            tempo_s=a["inicio_s"],
            id_alegacao=a["id"],
            frase=a["frase"],
            resumo=c["resumo"],
            ressalva=c.get("ressalva"),
            fontes=c.get("fontes", []),
        )
        arquivo = saida / f"{a['id']}.png"
        img.save(arquivo, optimize=True)
        contagem[c["veredito"]] = contagem.get(c["veredito"], 0) + 1
        itens.append({
            "id": a["id"],
            "arquivo": str(arquivo.relative_to(caso)).replace("\\", "/"),
            "entra_s": j["entra_s"],
            "sai_s": j["sai_s"],
            "atraso_s": j["atraso_s"],
            "atraso_do_fim_s": j["atraso_do_fim_s"],
            "veredito": c["veredito"],
            "tempo_na_peca_s": a["inicio_s"],
        })
        if j["curta"]:
            aviso(f"{a['id']} fica só {j['sai_s'] - j['entra_s']:.1f}s na tela "
                  f"(piso é {cfg.CARD_DURACAO_MIN_S}s) — o trecho acabou antes")
        if j["atraso_do_fim_s"] > cfg.ATRASO_MAX_S:
            aviso(f"{a['id']} só entra {j['atraso_do_fim_s']:.1f}s depois de a frase acabar "
                  f"(teto é {cfg.ATRASO_MAX_S}s) — há alegações demais empilhadas antes dela")

    caminho_selo = saida / "_selo.png"
    desenhar_selo().save(caminho_selo, optimize=True)

    legenda_arquivo = None
    if com_legenda:
        img = desenhar_legenda(
            "Como ler esta checagem",
            f"{meta['titulo']} · {meta['veiculo']} · {meta['data_do_evento']}",
        )
        p = saida / "_legenda.png"
        img.save(p, optimize=True)
        legenda_arquivo = str(p.relative_to(caso)).replace("\\", "/")

    plano = {
        "caso": slug,
        "recorte": recorte,
        "alvo": alvo,
        "base_s": base_s,
        "duracao_s": limite_s,
        "largura": cfg.LARGURA,
        "altura": cfg.ALTURA,
        "gerado_em": date.today().isoformat(),
        "selo": {
            "arquivo": str(caminho_selo.relative_to(caso)).replace("\\", "/"),
            "entra_s": 0.0,
            "sai_s": round(limite_s, 3),
        },
        "legenda": (
            {"arquivo": legenda_arquivo, "entra_s": 0.5,
             "sai_s": 0.5 + cfg.LEGENDA_DURACAO_S} if legenda_arquivo else None
        ),
        "contagem_por_veredito": contagem,
        "cartelas": itens,
    }
    caminho_plano = caso / "overlay" / _nome("plano", recorte)
    escrever_json(caminho_plano, plano)

    ok(f"{len(itens)} cartelas em {saida.relative_to(cfg.RAIZ)}")
    for k, n in sorted(contagem.items(), key=lambda kv: -kv[1]):
        info(f"{cfg.VEREDITOS[k].rotulo:<18} {n}")
    ok(f"{caminho_plano.relative_to(cfg.RAIZ)}")
    return caminho_plano


def _nome(base: str, recorte: str | None) -> str:
    return f"{base}-{recorte}.json" if recorte else f"{base}.json"


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(prog="checagem overlay", description="PASSO 6 — montar overlay")
    p.add_argument("slug")
    p.add_argument("--recorte", default=None)
    p.add_argument("--sem-legenda", action="store_true")
    args = p.parse_args(argv)
    montar(args.slug, recorte=args.recorte, com_legenda=not args.sem_legenda)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
