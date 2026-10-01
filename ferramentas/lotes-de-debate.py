"""Divide e junta o trabalho de uma peça LONGA, para ele poder rodar em paralelo sem perder a trava.

Um debate de ~2 h com quatro candidatos passa de 200 alegações. Extrair e checar isso numa passada
só estoura o contexto de qualquer agente, e o resultado vira superficial no fim da peça. A saída é
cortar o trabalho em **lotes independentes** e juntar depois, com as travas do projeto intactas:

    1. extracao-dividir   transcrição (já com falantes) -> lotes de ~8 min, cortados em virada de turno
       (cada lote é extraído por um agente, de internet FECHADA, seguindo skills/extrair-alegacoes.md)
    2. extracao-juntar    junta os lotes, tira duplicata da sobreposição, renumera A001.. e prova
       que a varredura cobriu a peça inteira, sem buraco
    3. checagem-dividir   corta as alegações já numeradas em pedidos de ~10 (cada um com seu agente,
       seguindo skills/checar-alegacao.md)
    4. checagem-juntar    junta, acusa alegação sem checagem, id duplicado e id inventado
    5. status             o que já voltou e o que falta

    python ferramentas/lotes-de-debate.py extracao-dividir <slug> [--minutos 8] [--contexto-s 45]
    python ferramentas/lotes-de-debate.py extracao-juntar  <slug> --recorte debate-completo
    python ferramentas/lotes-de-debate.py checagem-dividir <slug> --recorte debate-completo [--tamanho 10]
    python ferramentas/lotes-de-debate.py checagem-juntar  <slug> --recorte debate-completo
    python ferramentas/lotes-de-debate.py status           <slug> --recorte debate-completo

🔴 O que este script NÃO faz: julgar. Ele corta, junta e confere contagem. Quem extrai e checa é
um agente seguindo as skills, e a revisão adversarial (skills/revisar-checagem.md) roda DEPOIS da
junção, sobre o conjunto, por quem não escreveu a checagem.

⚠️ A junção é a parte delicada: lote que escolhe alegação "por conta" é o defeito que a trava de
cobertura existe para pegar. Por isso cada lote declara a janela que varreu, e o script recusa
alegação fora dela e janela com buraco entre uma e outra.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from datetime import date
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from checagem import config as cfg  # noqa: E402

TOLERANCIA_S = 0.5


def _ler(caminho: Path):
    return json.loads(caminho.read_text(encoding="utf-8"))


def _escrever(caminho: Path, dados) -> None:
    caminho.parent.mkdir(parents=True, exist_ok=True)
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def _rel(caminho: Path) -> str:
    try:
        return caminho.relative_to(RAIZ).as_posix()
    except ValueError:
        return caminho.as_posix()


def _mmss(s: float) -> str:
    s = int(s)
    return f"{s // 3600:02d}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def _norm(t: str) -> str:
    t = unicodedata.normalize("NFKD", t.lower())
    t = "".join(c for c in t if not unicodedata.combining(c))
    return re.sub(r"\s+", " ", re.sub(r"[^a-z0-9 ]+", " ", t)).strip()


# ─────────────────────────────────────────────────────────────────────
# 1. extração: dividir
# ─────────────────────────────────────────────────────────────────────

CABECALHO_DO_LOTE = """\
LOTE {n:02d} de {total:02d} · janela a EXTRAIR: {ini} a {fim} ({ini_s:.1f} s a {fim_s:.1f} s)

⛔ INTERNET FECHADA. Não pesquise nada, nem para "entender melhor" uma frase. Quem já sabe a resposta
   escolhe as perguntas (skills/extrair-alegacoes.md, trava 2).
⛔ NENHUM veredito. O arquivo de saída não tem esse campo.
⛔ Extraia SÓ da janela acima. As linhas marcadas (contexto) existem para a frase não ser lida fora
   de contexto, e NÃO viram alegação.
⛔ Mesma régua para todos os falantes: candidato, mediador, e a pergunta que um candidato faz ao outro
   (ela afirma fato e entra). Nada de pular quem "fala difícil".

Saída: {saida}
  · ids locais A001, A002... na ordem da fala (o script renumera depois)
  · `cobertura`: {{"inicio_s": {ini_s:.1f}, "fim_s": {fim_s:.1f}}}
  · `exclusoes` para o que atravessou o filtro e não virou alegação, com motivo
  · `frase` é cópia LITERAL da transcrição (o validador confere palavra inteira)

────────────────────────────────────────────────────────────────────────────
"""


def _turnos(segmentos: list[dict]) -> list[int]:
    """Índices dos segmentos que começam um turno novo (o falante mudou)."""
    idx = []
    for i, s in enumerate(segmentos):
        if i == 0 or s.get("falante") != segmentos[i - 1].get("falante"):
            idx.append(i)
    return idx


def dividir_extracao(slug: str, minutos: float, contexto_s: float) -> None:
    caso = cfg.pasta_do_caso(slug)
    transcricao = _ler(caso / "transcricao" / "transcricao.json")
    segs = transcricao["segmentos"]
    if any(not s.get("falante") for s in segs):
        sys.exit("há segmentos sem falante: rode o PASSO 3 (python -m checagem falantes) antes de dividir.")
    alvo = minutos * 60
    inicios_de_turno = set(_turnos(segs))

    # Fecha o lote quando passou do alvo E o próximo segmento abre um turno (nunca no meio de uma
    # resposta). Se o turno é longo demais, fecha em 1,6x o alvo no fim de qualquer segmento.
    lotes: list[tuple[int, int]] = []
    ini = 0
    for i in range(1, len(segs) + 1):
        if i == len(segs):
            lotes.append((ini, i))
            break
        dur = segs[i]["inicio_s"] - segs[ini]["inicio_s"]
        if (dur >= alvo and i in inicios_de_turno) or dur >= alvo * 1.6:
            lotes.append((ini, i))
            ini = i

    pasta = caso / "lotes" / "extracao"
    pasta.mkdir(parents=True, exist_ok=True)
    saida_pasta = caso / "alegacoes" / "lotes"
    indice = []
    for n, (a, b) in enumerate(lotes, 1):
        janela = segs[a:b]
        ini_s, fim_s = janela[0]["inicio_s"], janela[-1]["fim_s"]
        antes = [s for s in segs[:a] if s["fim_s"] >= ini_s - contexto_s]
        saida = saida_pasta / f"alegacoes-lote-{n:02d}.json"
        linhas = [CABECALHO_DO_LOTE.format(
            n=n, total=len(lotes), ini=_mmss(ini_s), fim=_mmss(fim_s), ini_s=ini_s, fim_s=fim_s,
            saida=_rel(saida))]
        for s in antes:
            linhas.append(f"(contexto, NÃO extrair) [{_mmss(s['inicio_s'])} · {s['inicio_s']:.1f}s] {s['falante']}: {s['texto'].strip()}")
        if antes:
            linhas.append("─── a janela começa aqui ───")
        for s in janela:
            linhas.append(f"[{_mmss(s['inicio_s'])} · {s['inicio_s']:.1f}s → {s['fim_s']:.1f}s] {s['falante']}: {s['texto'].strip()}")
        (pasta / f"lote-{n:02d}.txt").write_text("\n".join(linhas) + "\n", encoding="utf-8", newline="\n")
        indice.append({
            "n": n, "inicio_s": round(ini_s, 2), "fim_s": round(fim_s, 2),
            "segmentos": len(janela), "palavras": sum(len(s["texto"].split()) for s in janela),
            "entrada": _rel(pasta / f"lote-{n:02d}.txt"),
            "saida": _rel(saida),
        })
    _escrever(pasta / "lotes.json", {"caso": slug, "gerado_em": date.today().isoformat(),
                                    "minutos_alvo": minutos, "contexto_s": contexto_s, "lotes": indice})
    print(f"{len(indice)} lotes de extração em {_rel(pasta)} "
          f"({min(i['palavras'] for i in indice)} a {max(i['palavras'] for i in indice)} palavras cada)")


# ─────────────────────────────────────────────────────────────────────
# 2. extração: juntar
# ─────────────────────────────────────────────────────────────────────


def juntar_extracao(slug: str, recorte: str) -> int:
    caso = cfg.pasta_do_caso(slug)
    indice = _ler(caso / "lotes" / "extracao" / "lotes.json")["lotes"]
    meta = _ler(caso / "CASO.json")
    erros: list[str] = []
    todas: list[tuple[int, dict]] = []
    exclusoes: list[dict] = []
    faltam = []
    for lote in indice:
        caminho = RAIZ / lote["saida"]
        if not caminho.exists():
            faltam.append(lote["n"])
            continue
        doc = _ler(caminho)
        cob = doc.get("cobertura") or {}
        if abs(cob.get("inicio_s", -1) - lote["inicio_s"]) > 1 or abs(cob.get("fim_s", -1) - lote["fim_s"]) > 1:
            erros.append(f"lote {lote['n']:02d}: a cobertura declarada {cob} não é a janela pedida "
                         f"({lote['inicio_s']} a {lote['fim_s']}): a varredura não cobriu o que devia")
        for a in doc["alegacoes"]:
            if "veredito" in a:
                erros.append(f"lote {lote['n']:02d} {a.get('id')}: veredito na extração (PASSO 4 não tem veredito)")
            if not (lote["inicio_s"] - TOLERANCIA_S <= a["inicio_s"] <= lote["fim_s"] + TOLERANCIA_S):
                erros.append(f"lote {lote['n']:02d} {a['id']}: começa em {a['inicio_s']}, fora da janela do lote")
                continue
            todas.append((lote["n"], a))
        for e in doc.get("exclusoes", []):
            if lote["inicio_s"] - TOLERANCIA_S <= e["inicio_s"] <= lote["fim_s"] + TOLERANCIA_S:
                exclusoes.append(e)
    if faltam:
        print(f"✗ faltam os lotes {faltam}: sem eles a varredura tem buraco e o resultado seria "
              "escolher o que mostrar.")
        return 1

    # Duplicata exata (mesma frase do mesmo falante): só acontece em borda de lote.
    todas.sort(key=lambda t: (t[1]["inicio_s"], t[0]))
    vistas: set[tuple[str, str]] = set()
    finais: list[dict] = []
    mapa = []
    for n, a in todas:
        chave = (a["falante"], _norm(a["frase"]))
        if chave in vistas:
            continue
        vistas.add(chave)
        novo = dict(a)
        novo["id"] = f"A{len(finais) + 1:03d}"
        finais.append(novo)
        mapa.append({"final": novo["id"], "lote": n, "id_local": a["id"]})
    if len(finais) > 999:
        erros.append(f"{len(finais)} alegações: o formato A### vai até A999. Divida a peça em dois recortes.")

    ini = min(x["inicio_s"] for x in indice)
    fim = max(x["fim_s"] for x in indice)
    # buraco entre janelas
    for x, y in zip(indice, indice[1:], strict=False):
        if y["inicio_s"] - x["fim_s"] > 2.0:
            erros.append(f"buraco de {y['inicio_s'] - x['fim_s']:.1f}s entre os lotes {x['n']:02d} e {y['n']:02d}")

    doc = {
        "caso": slug, "gerado_em": date.today().isoformat(),
        "fonte_transcricao": f"casos/{slug}/transcricao/transcricao.json",
        "recorte": recorte, "cobertura": {"inicio_s": ini, "fim_s": fim},
        "alegacoes": finais,
    }
    if exclusoes:
        doc["exclusoes"] = sorted(exclusoes, key=lambda e: e["inicio_s"])
    try:
        import jsonschema
        jsonschema.validate(doc, _ler(cfg.ESQUEMAS / "alegacoes.schema.json"))
    except ImportError:
        print("⚠ jsonschema não instalado: esquema não conferido")
    except jsonschema.ValidationError as e:  # type: ignore[attr-defined]
        erros.append(f"esquema: em '{'/'.join(map(str, e.absolute_path))}': {e.message}")
    if erros:
        print("✗ a junção NÃO foi gravada:")
        for e in erros:
            print(f"  - {e}")
        return 1
    _escrever(caso / "alegacoes" / f"alegacoes-{recorte}.json", doc)
    _escrever(caso / "alegacoes" / "lotes" / "mapa-de-ids.json", mapa)
    duracao = float(meta.get("duracao_s") or fim)
    por_falante: dict[str, int] = {}
    for a in finais:
        por_falante[a["falante"]] = por_falante.get(a["falante"], 0) + 1
    print(f"✓ {len(finais)} alegações em {_mmss(ini)}–{_mmss(fim)} ({len(finais) / (duracao / 60):.1f} por minuto) · "
          + " · ".join(f"{k} {v}" for k, v in por_falante.items()))
    print(f"  → casos/{slug}/alegacoes/alegacoes-{recorte}.json")
    return 0


# ─────────────────────────────────────────────────────────────────────
# 3. checagem: dividir e juntar
# ─────────────────────────────────────────────────────────────────────

CABECALHO_DA_CHECAGEM = """\
PEDIDO DE CHECAGEM {n:02d} de {total:02d} · alegações {primeira} a {ultima}

Siga skills/checar-alegacao.md do começo ao fim, uma alegação por vez.
⛔ Nenhum fato da memória do modelo: URL consultada, trecho copiado, no mínimo duas fontes independentes.
⛔ A mesma régua para todos. Alegação não checável passa direto (veredito NAO_CHECAVEL, sem fonte).
⛔ Fato em apuração (inquérito aberto, processo sem trânsito, dado com revisão pendente): o veredito é
   INSUSTENTAVEL ou NAO_CHECAVEL, nunca FALSO (etica-e-risco §5).
⛔ Nunca leia intenção. O `resumo` fala do enunciado, cabe em duas linhas, sem travessão.

Saída: {saida}
  {{"checagens": [ {{"id": "A001", "veredito": ..., "resumo": ..., "explicacao": ..., "fontes": [...],
                      "confianca": ...}}, ... ]}}   (esquema: esquemas/checagens.schema.json)

Alegações deste pedido:
────────────────────────────────────────────────────────────────────────────
"""


def dividir_checagem(slug: str, recorte: str, tamanho: int) -> None:
    caso = cfg.pasta_do_caso(slug)
    doc = _ler(caso / "alegacoes" / f"alegacoes-{recorte}.json")
    alegs = doc["alegacoes"]
    # Corte por ordem cronológica: o debate muda de assunto a cada bloco, então alegações vizinhas
    # tendem a dividir a mesma fonte (quem abre o IBGE uma vez checa várias).
    pedidos = [alegs[i:i + tamanho] for i in range(0, len(alegs), tamanho)]
    pasta = caso / "lotes" / "checagem"
    for n, grupo in enumerate(pedidos, 1):
        saida = caso / "checagens" / "lotes" / f"checagens-lote-{n:02d}.json"
        cab = CABECALHO_DA_CHECAGEM.format(
            n=n, total=len(pedidos), primeira=grupo[0]["id"], ultima=grupo[-1]["id"],
            saida=_rel(saida))
        corpo = json.dumps({"alegacoes": grupo}, ensure_ascii=False, indent=2)
        (pasta / f"pedido-{n:02d}.json").parent.mkdir(parents=True, exist_ok=True)
        (pasta / f"pedido-{n:02d}.json").write_text(cab + corpo + "\n", encoding="utf-8", newline="\n")
    _escrever(pasta / "pedidos.json", {
        "caso": slug, "recorte": recorte, "gerado_em": date.today().isoformat(),
        "pedidos": [{"n": n, "ids": [a["id"] for a in g]} for n, g in enumerate(pedidos, 1)]})
    print(f"{len(pedidos)} pedidos de checagem ({tamanho} alegações cada) em {_rel(pasta)}")


def juntar_checagem(slug: str, recorte: str) -> int:
    caso = cfg.pasta_do_caso(slug)
    alegs = _ler(caso / "alegacoes" / f"alegacoes-{recorte}.json")["alegacoes"]
    ids = [a["id"] for a in alegs]
    pasta = caso / "checagens" / "lotes"
    arquivos = sorted(pasta.glob("checagens-lote-*.json"))
    vistas: dict[str, dict] = {}
    erros = []
    for arq in arquivos:
        for c in _ler(arq)["checagens"]:
            if c["id"] not in ids:
                erros.append(f"{arq.name}: {c['id']} não existe nas alegações (id inventado)")
            elif c["id"] in vistas:
                erros.append(f"{arq.name}: {c['id']} checada duas vezes")
            else:
                vistas[c["id"]] = c
    falta = [i for i in ids if i not in vistas]
    if falta:
        erros.append(f"{len(falta)} alegações sem checagem: {', '.join(falta[:12])}{'…' if len(falta) > 12 else ''}")
    if erros:
        print("✗ a junção NÃO foi gravada:")
        for e in erros:
            print(f"  - {e}")
        return 1
    doc = {"caso": slug, "gerado_em": date.today().isoformat(),
           "fonte_alegacoes": f"casos/{slug}/alegacoes/alegacoes-{recorte}.json",
           "checagens": [vistas[i] for i in ids]}
    _escrever(caso / "checagens" / f"checagens-{recorte}.json", doc)
    print(f"✓ {len(ids)} checagens → casos/{slug}/checagens/checagens-{recorte}.json")
    print("  próximo: revisão adversarial separada (skills/revisar-checagem.md), depois "
          f"python -m checagem validar {slug} --recorte {recorte}")
    return 0


# ─────────────────────────────────────────────────────────────────────


def status(slug: str, recorte: str) -> None:
    caso = cfg.pasta_do_caso(slug)
    idx = caso / "lotes" / "extracao" / "lotes.json"
    if idx.exists():
        lotes = _ler(idx)["lotes"]
        feitos = [x["n"] for x in lotes if (RAIZ / x["saida"]).exists()]
        print(f"extração: {len(feitos)} de {len(lotes)} lotes devolvidos; faltam {[x['n'] for x in lotes if x['n'] not in feitos] or 'nenhum'}")
    ped = caso / "lotes" / "checagem" / "pedidos.json"
    if ped.exists():
        pedidos = _ler(ped)["pedidos"]
        arq = {int(re.search(r"(\d+)", p.stem.split("lote-")[-1]).group(1)) for p in (caso / "checagens" / "lotes").glob("checagens-lote-*.json")} \
            if (caso / "checagens" / "lotes").exists() else set()
        print(f"checagem: {len(arq)} de {len(pedidos)} pedidos devolvidos; faltam {[p['n'] for p in pedidos if p['n'] not in arq] or 'nenhum'}")
    for rotulo, p in (("alegações juntas", caso / "alegacoes" / f"alegacoes-{recorte}.json"),
                      ("checagens juntas", caso / "checagens" / f"checagens-{recorte}.json")):
        print(f"{rotulo}: {'sim' if p.exists() else 'ainda não'}")


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    sub = p.add_subparsers(dest="cmd", required=True)
    a = sub.add_parser("extracao-dividir")
    a.add_argument("slug")
    a.add_argument("--minutos", type=float, default=8.0)
    a.add_argument("--contexto-s", type=float, default=45.0)
    for nome in ("extracao-juntar", "checagem-juntar", "status"):
        s = sub.add_parser(nome)
        s.add_argument("slug")
        s.add_argument("--recorte", default="debate-completo")
    c = sub.add_parser("checagem-dividir")
    c.add_argument("slug")
    c.add_argument("--recorte", default="debate-completo")
    c.add_argument("--tamanho", type=int, default=10)
    args = p.parse_args()
    if args.cmd == "extracao-dividir":
        dividir_extracao(args.slug, args.minutos, args.contexto_s)
    elif args.cmd == "extracao-juntar":
        return juntar_extracao(args.slug, args.recorte)
    elif args.cmd == "checagem-dividir":
        dividir_checagem(args.slug, args.recorte, args.tamanho)
    elif args.cmd == "checagem-juntar":
        return juntar_checagem(args.slug, args.recorte)
    else:
        status(args.slug, args.recorte)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
