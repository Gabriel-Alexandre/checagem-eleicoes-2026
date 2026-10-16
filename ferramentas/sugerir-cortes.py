"""Sugere os CORTES CURTOS de uma peça checada inteira, pelo critério declarado ANTES dos vereditos.

    python ferramentas/sugerir-cortes.py <slug> [--recorte sabatina-completa] [--quantos 6] \\
        [--max 20] [--min 8] [--fixar 1234.5-1252.0 "motivo dele"]

Roda **depois da extração (PASSO 4) e antes da checagem (PASSO 5)**. Lê só a transcrição com
falantes e as alegações; ⛔ não abre `checagens/` em momento nenhum, e é isso que deixa provar que
o corte não foi escolhido "porque ali tem um FALSO" (etica-e-risco §1, docs/DEBATES.md §5).

O critério é o de `recortes/SELECAO_DE_CORTES.md` do caso, registrado antes do evento. Em resumo,
cada janela candidata (começa e termina em borda de segmento, contém as alegações inteiras, dura
entre `--min` e `--max` segundos) ganha pontos por:

  · FATO      alegações checáveis dentro dela (dado duro pesa 1,0; evento, norma, data e atribuição 0,8)
  · CONFRONTO o jornalista afirma fato e o entrevistado responde com fato na mesma janela (+1,0;
              +1,5 se for o mesmo assunto)
  · TROCA     viradas de turno entre jornalista e entrevistado (+0,4 cada, até 3): é o sinal
              observável de "momento quente", sem ler tom, intenção nem resultado
  · DENSIDADE desempate: alegações checáveis por segundo

Toda janela precisa de pelo menos UMA alegação checável do entrevistado (ensaio de 15/out: sem essa
regra, o corte mais denso era só a pergunta da jornalista, sem a resposta). A escolha final, gulosa
pela pontuação, obedece: no máximo `--quantos` cortes, `CORTES_INTERVALO_MIN_S`
entre um e outro (não são continuação), soma até `CORTES_TOTAL_MAX_S`, e **um assunto por corte** na
primeira passada (variedade); só depois repete assunto para completar.

`--fixar` é a porta para o trecho que ELE quer por ser polêmico ou importante: entra na frente, com
o motivo dele escrito, e o relatório mostra que veio de fora do critério.

Saída: `recortes/SUGESTAO_DE_CORTES.json` e `.md`, com os comandos prontos de `midia recortar` e
`derivar-recorte.py` para cada corte.
"""

from __future__ import annotations

import argparse
import json
import sys
from collections import Counter
from datetime import datetime
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))
if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

from checagem import config as cfg  # noqa: E402

PESO_DADO_DURO = 1.0
PESO_FATO = 0.8
DADO_DURO = {"numero", "serie_historica", "valor_monetario", "comparacao", "ranking"}
BONUS_CONFRONTO = 1.0
BONUS_MESMO_ASSUNTO = 0.5
BONUS_TROCA = 0.4
TROCAS_MAX = 3
FOLGA_S = 0.25
TOL = 0.05


def _mmss(s: float) -> str:
    s = int(round(s))
    return f"{s // 60:02d}:{s % 60:02d}" if s < 3600 else f"{s // 3600}:{(s % 3600) // 60:02d}:{s % 60:02d}"


def _peso(a: dict) -> float:
    if not a.get("checavel", True):
        return 0.0
    return PESO_DADO_DURO if a["tipo"] in DADO_DURO else PESO_FATO


def _avaliar(ini: float, fim: float, segs: list[dict], alegs: list[dict]) -> dict | None:
    """Pontua a janela [ini, fim]. None se alguma alegação atravessa a borda ou se não há fato."""
    dentro = []
    for a in alegs:
        if a["fim_s"] <= ini + TOL or a["inicio_s"] >= fim - TOL:
            continue
        if a["inicio_s"] < ini - TOL or a["fim_s"] > fim + TOL:
            return None
        dentro.append(a)
    checaveis = [a for a in dentro if a.get("checavel", True)]
    if not checaveis:
        return None
    fato = sum(_peso(a) for a in dentro)
    assuntos_j = {a["assunto"] for a in checaveis if a["papel"] == "entrevistador"}
    assuntos_e = {a["assunto"] for a in checaveis if a["papel"] == "entrevistado"}
    if not assuntos_e:
        return None
    mesmo_assunto = sorted(assuntos_j & assuntos_e)
    confronto = sorted(assuntos_j | assuntos_e) if assuntos_j else []
    falas = [s for s in segs if s["fim_s"] > ini + TOL and s["inicio_s"] < fim - TOL
             and s.get("papel") in ("entrevistador", "entrevistado")]
    trocas = sum(1 for x, y in zip(falas, falas[1:], strict=False) if x.get("papel") != y.get("papel"))
    duracao = fim - ini
    pontos = (fato + (BONUS_CONFRONTO if confronto else 0.0) + (BONUS_MESMO_ASSUNTO if mesmo_assunto else 0.0)
              + BONUS_TROCA * min(trocas, TROCAS_MAX))
    if len(checaveis) < 2 and not confronto:
        return None
    assunto = Counter(a["assunto"] for a in checaveis).most_common(1)[0][0]
    return {
        "inicio_s": round(ini, 2), "fim_s": round(fim, 2), "duracao_s": round(duracao, 2),
        "pontos": round(pontos, 2), "densidade": round(len(checaveis) / duracao, 3),
        "fato": round(fato, 2), "confronto": confronto, "mesmo_assunto": mesmo_assunto, "trocas_de_turno": trocas,
        "assunto": assunto, "ids": [a["id"] for a in dentro],
        "checaveis": len(checaveis), "nao_checaveis": len(dentro) - len(checaveis),
        "falantes": list(dict.fromkeys(a["falante"] for a in dentro)),
    }


def candidatas(segs: list[dict], alegs: list[dict], minimo: float, maximo: float) -> list[dict]:
    """Toda janela que começa num segmento e termina noutro, com folga curta nas pontas."""
    saida = []
    for i, si in enumerate(segs):
        ini = max(si["inicio_s"] - FOLGA_S, segs[i - 1]["fim_s"] if i else 0.0)
        for j in range(i, len(segs)):
            fim = segs[j]["fim_s"] + FOLGA_S
            if j + 1 < len(segs):
                fim = min(fim, segs[j + 1]["inicio_s"])
            dur = fim - ini
            if dur > maximo:
                break
            if dur < minimo:
                continue
            av = _avaliar(ini, fim, segs, alegs)
            if av:
                saida.append(av)
    saida.sort(key=lambda c: (-c["pontos"], -c["densidade"], c["inicio_s"]))
    return saida


def escolher(cands: list[dict], quantos: int, fixos: list[dict]) -> list[dict]:
    escolhidos = list(fixos)

    def cabe(c: dict, repetir_assunto: bool) -> bool:
        total = sum(x["duracao_s"] for x in escolhidos) + c["duracao_s"]
        if total > cfg.CORTES_TOTAL_MAX_S + 0.01:
            return False
        for x in escolhidos:
            if max(c["inicio_s"] - x["fim_s"], x["inicio_s"] - c["fim_s"]) < cfg.CORTES_INTERVALO_MIN_S:
                return False
        return repetir_assunto or c["assunto"] not in {x["assunto"] for x in escolhidos}

    for repetir in (False, True):
        for c in cands:
            if len(escolhidos) >= quantos:
                break
            if c not in escolhidos and cabe(c, repetir):
                escolhidos.append(c)
    escolhidos.sort(key=lambda c: c["inicio_s"])
    for n, c in enumerate(escolhidos, 1):
        c["id"] = f"corte-{n:02d}"
    return escolhidos


def _motivo(c: dict) -> str:
    if c.get("fixado_pelo_autor"):
        return f"escolha do autor, fora do critério: {c['fixado_pelo_autor']}"
    partes = [f"critério pré-registrado (recortes/SELECAO_DE_CORTES.md): {c['checaveis']} alegações "
              f"checáveis em {c['duracao_s']:.0f} s, assunto {c['assunto']}"]
    if c["confronto"]:
        partes.append(f"confronto jornalista x entrevistado em {', '.join(c['confronto'])}")
    if c["trocas_de_turno"]:
        partes.append(f"{c['trocas_de_turno']} troca{'s' if c['trocas_de_turno'] > 1 else ''} de turno")
    return "; ".join(partes)


def main() -> int:
    p = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    p.add_argument("slug")
    p.add_argument("--recorte", default=None, help="padrão: o recorte da peça inteira do formato do caso")
    p.add_argument("--quantos", type=int, default=cfg.CORTES_QUANTIDADE[1])
    p.add_argument("--max", type=float, default=cfg.CORTE_RECOMENDADO_S, help="duração máxima de cada corte")
    p.add_argument("--min", type=float, default=8.0, help="duração mínima de cada corte")
    p.add_argument("--fixar", nargs=2, action="append", default=[], metavar=("INICIO-FIM", "MOTIVO"),
                   help="trecho que o autor quer de qualquer jeito, com o motivo dele")
    p.add_argument("--mostrar", type=int, default=15, help="quantas candidatas listar no relatório")
    p.add_argument("--caixa", default=None, metavar="X,Y,W,H",
                   help="caixa declarada no CASO.json (imagem dentro de moldura); vai nos comandos de recorte")
    a = p.parse_args()
    a.recorte = a.recorte or cfg.recorte_da_peca_inteira_do_caso(a.slug)
    if a.max > cfg.CORTE_MAX_S:
        print(f"✗ --max {a.max:.0f} s passa do teto de um corte ({cfg.CORTE_MAX_S:.0f} s, config.CORTE_MAX_S)")
        return 1

    caso = cfg.pasta_do_caso(a.slug)
    segs = json.loads((caso / "transcricao" / "transcricao.json").read_text(encoding="utf-8"))["segmentos"]
    if any(not s.get("falante") for s in segs):
        print("✗ há segmentos sem falante: rode o PASSO 3 antes (o critério usa o papel de quem fala)")
        return 1
    doc = json.loads((caso / "alegacoes" / f"alegacoes-{a.recorte}.json").read_text(encoding="utf-8"))
    alegs = doc["alegacoes"]

    fixos = []
    for janela, motivo in a.fixar:
        ini, fim = (float(x) for x in janela.split("-"))
        av = _avaliar(ini, fim, segs, alegs)
        if av is None:
            print(f"✗ --fixar {janela}: alguma alegação atravessa a borda, ou não há alegação checável")
            return 1
        if av["duracao_s"] > cfg.CORTE_MAX_S + 0.01:
            print(f"✗ --fixar {janela}: {av['duracao_s']:.1f} s passa do teto de {cfg.CORTE_MAX_S:.0f} s")
            return 1
        av["fixado_pelo_autor"] = motivo
        fixos.append(av)

    cands = candidatas(segs, alegs, a.min, a.max)
    escolhidos = escolher(cands, a.quantos, fixos)
    for c in escolhidos:
        c["motivo"] = _motivo(c)
    total = sum(c["duracao_s"] for c in escolhidos)
    agora = datetime.now().astimezone().isoformat(timespec="minutes")
    saida = {
        "caso": a.slug, "recorte_de_origem": a.recorte, "gerado_em": agora,
        "leu_checagens": False,
        "parametros": {"quantos": a.quantos, "min_s": a.min, "max_s": a.max,
                       "intervalo_min_s": cfg.CORTES_INTERVALO_MIN_S, "total_max_s": cfg.CORTES_TOTAL_MAX_S},
        "escolhidos": escolhidos, "total_s": round(total, 2),
        "candidatas": cands[: a.mostrar], "candidatas_avaliadas": len(cands),
    }
    pasta = caso / "recortes"
    pasta.mkdir(exist_ok=True)
    (pasta / "SUGESTAO_DE_CORTES.json").write_text(json.dumps(saida, ensure_ascii=False, indent=2) + "\n",
                                                  encoding="utf-8", newline="\n")
    texto_de = {x["id"]: x for x in alegs}
    L = [f"# Sugestão de cortes · {a.slug}", "",
         f"Gerado em {agora} por `ferramentas/sugerir-cortes.py`, **sem ler nenhuma checagem** (o arquivo de "
         "vereditos não é aberto). Critério: `recortes/SELECAO_DE_CORTES.md`. ⚠️ É sugestão: a decisão de "
         "quais cortes saem, e em que ordem aparecem no vídeo, é dele.", "",
         f"**{len(escolhidos)} cortes**, {total:.1f} s de trecho da emissora no total "
         f"(teto {cfg.CORTES_TOTAL_MAX_S:.0f} s; cada um até {a.max:.0f} s; {cfg.CORTES_INTERVALO_MIN_S:.0f} s "
         f"entre um e outro). {len(cands)} janelas avaliadas.", ""]
    if len(escolhidos) < cfg.CORTES_QUANTIDADE[0]:
        L += [f"> ⚠️ Só {len(escolhidos)} cortes cabem no critério (ele pediu {cfg.CORTES_QUANTIDADE[0]} a "
              f"{cfg.CORTES_QUANTIDADE[1]}). Rode de novo com `--max` maior (até {cfg.CORTE_MAX_S:.0f} s) ou "
              "`--min` menor, ou fixe um trecho com `--fixar`.", ""]
    for c in escolhidos:
        L += [f"## {c['id']} · {_mmss(c['inicio_s'])} a {_mmss(c['fim_s'])} · {c['duracao_s']:.1f} s · `{c['assunto']}`", "",
              f"**Por quê:** {c['motivo']}  ",
              f"**Pontos:** {c['pontos']} (fato {c['fato']}, confronto {'sim' if c['confronto'] else 'não'}, "
              f"{c['trocas_de_turno']} trocas)  ", ""]
        for i in c["ids"]:
            x = texto_de[i]
            L.append(f"- `{i}` {x['falante']}: \"{x['frase']}\"")
        L += ["", "```bash",
              f"python -m checagem midia {a.slug} recortar {c['id']} --inicio {c['inicio_s']} "
              f"--duracao {c['duracao_s']} --motivo \"{c['motivo']}\""
              + (f" --caixa {a.caixa}" if a.caixa else ""),
              f"python ferramentas/derivar-recorte.py {a.slug} --de {a.recorte} --para {c['id']} "
              f"--inicio {c['inicio_s']} --fim {c['fim_s']}",
              "```", ""]
    L += ["## As outras candidatas (as de maior pontuação)", "",
          "| Janela | Duração | Pontos | Checáveis | Confronto | Trocas | Assunto |", "|---|---:|---:|---:|---|---:|---|"]
    for c in cands[: a.mostrar]:
        L.append(f"| {_mmss(c['inicio_s'])} a {_mmss(c['fim_s'])} | {c['duracao_s']:.1f} s | {c['pontos']} | "
                 f"{c['checaveis']} | {', '.join(c['confronto']) or '·'} | {c['trocas_de_turno']} | {c['assunto']} |")
    (pasta / "SUGESTAO_DE_CORTES.md").write_text("\n".join(L) + "\n", encoding="utf-8", newline="\n")
    print(f"✓ {len(escolhidos)} cortes sugeridos, {total:.1f} s no total → casos/{a.slug}/recortes/SUGESTAO_DE_CORTES.md")
    for c in escolhidos:
        print(f"  {c['id']}  {_mmss(c['inicio_s'])}–{_mmss(c['fim_s'])}  {c['duracao_s']:5.1f} s  "
              f"{c['checaveis']} checáveis  {c['assunto']}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
