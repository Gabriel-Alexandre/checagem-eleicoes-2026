"""Leva o que já foi escrito de uma mídia para outra, quando a peça do caso é trocada.

    python ferramentas/migrar-tempos.py <slug> --recorte ID --antiga <transcricao-antiga.json>
                                        [--aplicar]

Acontece quando o arquivo checado é substituído por outro da MESMA fala (o clipe vertical do g1 pela
íntegra horizontal, por exemplo). As alegações, os turnos de falante e as correções de transcrição
estão escritos no tempo da mídia antiga; a nova tem outro relógio. Refazer tudo à mão é o tipo de
trabalho em que se erra um segundo e o card aparece na frase errada.

O que o script faz, e só isto:

  1. mede o deslocamento entre as duas mídias pelo FIM dos segmentos: cada segmento antigo com 5
     palavras ou mais é casado com o segmento novo de texto idêntico (sem acento, sem pontuação), e o
     deslocamento é a mediana das diferenças entre os fins. 🔴 Não se mede pelo começo: o motor
     acha o começo de cada segmento onde a fala começa depois do silêncio, e ele varia até 0,8 s
     entre duas passadas sobre o MESMO áudio, enquanto o fim é estável (medido: ±0,04 s nos 58
     casamentos do caso Flávio). Mídia diferente de verdade daria fim que anda, e aí o script recusa;
  2. leva cada `fim_s` de alegação e cada limite de turno para o tempo novo somando o deslocamento
     e colando no fim de segmento novo mais próximo (tolerância de 0,35 s; sem par, fica o tempo
     somado e o relatório marca). O `inicio_s` leva o mesmo deslocamento e cola no começo de segmento
     novo mais próximo (tolerância de 1,0 s, porque o começo é o lado instável);
  3. reconfere cada correção de transcrição contra o texto novo: se o motor já acertou, a correção
     sai (e o motivo fica escrito); se o texto novo é outro, ela NÃO é migrada e fica listada: o motor errou de outro jeito, e a
     conferência (segunda passada, referência publicada) tem que ser refeita na mídia nova.

⛔ Ele NÃO muda `frase`, `resumo`, veredito nem fonte. Se uma citação deixou de existir na transcrição
nova, quem reprova é o validador (PASSO 8), e o conserto é por `corrigir-transcricao.py`, com registro.

Sem `--aplicar` ele só escreve o relatório na tela.
"""

from __future__ import annotations

import argparse
import difflib
import json
import statistics
import sys
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(RAIZ / "src"))

from checagem.passo8_validar import normalizar  # noqa: E402

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

TOLERANCIA_INICIO_S = 1.0
DISPERSAO_MAX_S = 0.15
TOLERANCIA_FIM_S = 0.35


def _ler(caminho: Path):
    return json.loads(caminho.read_text(encoding="utf-8"))


def _escrever(caminho: Path, dados) -> None:
    caminho.write_text(json.dumps(dados, ensure_ascii=False, indent=2) + "\n",
                       encoding="utf-8", newline="\n")


def medir_deslocamento(antigos: list[dict], novos: list[dict]) -> tuple[float, list[float]]:
    por_texto: dict[str, list[dict]] = {}
    for s in novos:
        por_texto.setdefault(normalizar(s["texto"]), []).append(s)
    diferencas: list[float] = []
    for a in antigos:
        chave = normalizar(a["texto"])
        if len(chave.split()) < 5:
            continue
        candidatos = por_texto.get(chave, [])
        if len(candidatos) == 1:
            diferencas.append(candidatos[0]["fim_s"] - a["fim_s"])
    if len(diferencas) < 10:
        raise SystemExit(f"só {len(diferencas)} segmentos casaram por texto idêntico: "
                         "não dá para medir o deslocamento com segurança")
    return statistics.median(diferencas), diferencas


def colar(t: float, limites: list[float], tolerancia: float) -> tuple[float, bool]:
    """(tempo colado no limite mais próximo, achou par). Sem limite perto, devolve o tempo cru."""
    melhor = min(limites, key=lambda x: abs(x - t))
    return (melhor, True) if abs(melhor - t) <= tolerancia else (round(t, 3), False)


def main() -> int:
    p = argparse.ArgumentParser(description="leva tempos de uma mídia antiga para a nova")
    p.add_argument("slug")
    p.add_argument("--recorte", required=True)
    p.add_argument("--antiga", required=True, help="transcricao.json da mídia antiga")
    p.add_argument("--aplicar", action="store_true")
    a = p.parse_args()

    caso = RAIZ / "casos" / a.slug
    novos = _ler(caso / "transcricao" / f"transcricao-{a.recorte}.json")["segmentos"]
    antigos = _ler(Path(a.antiga))["segmentos"]
    inicios = [s["inicio_s"] for s in novos]
    fins = [s["fim_s"] for s in novos]

    d, diferencas = medir_deslocamento(antigos, novos)
    disp = max(abs(x - d) for x in diferencas)
    print(f"deslocamento medido pelo fim dos segmentos: {d:+.3f} s  ({len(diferencas)} casados, "
          f"desvio máximo {disp:.3f} s)")
    if disp > DISPERSAO_MAX_S:
        print(f"✗ desvio acima de {DISPERSAO_MAX_S} s: as duas mídias não andam juntas "
              "(corte, velocidade ou fala diferente). Nada foi feito.")
        return 1

    sem_par: list[str] = []

    def novo_inicio(t: float) -> float:
        valor, par = colar(t + d, inicios, TOLERANCIA_INICIO_S)
        if not par:
            sem_par.append(f"início {t:.2f}")
        return valor

    def novo_fim(t: float) -> float:
        valor, par = colar(t + d, fins, TOLERANCIA_FIM_S)
        if not par:
            sem_par.append(f"fim {t:.2f}")
        return valor

    # A cobertura é a janela do recorte na peça nova: o clipe antigo tinha 5 s de cartela do veículo
    # no fim, que o recorte novo não leva, então somar o deslocamento à cobertura antiga passaria do fim.
    reg = next(r for r in _ler(caso / "recortes" / "RECORTES.json")["recortes"] if r["id"] == a.recorte)
    fim_do_recorte = round(reg["origem_inicio_s"] + reg["duracao_s"], 3)

    # ── alegações ──
    pa = caso / "alegacoes" / f"alegacoes-{a.recorte}.json"
    doc = _ler(pa)
    linhas: list[str] = []
    for al in doc["alegacoes"]:
        i0, f0 = al["inicio_s"], al["fim_s"]
        al["inicio_s"], al["fim_s"] = novo_inicio(i0), novo_fim(f0)
        linhas.append(f"{al['id']}  {i0:8.2f} a {f0:8.2f}  →  {al['inicio_s']:8.2f} a {al['fim_s']:8.2f}"
                      f"   (começo {al['inicio_s'] - i0 - d:+.2f} s do deslocamento, fim {al['fim_s'] - f0 - d:+.2f} s)")
    cob = doc.get("cobertura")
    if cob:
        cob["inicio_s"] = round(reg["origem_inicio_s"], 3)
        cob["fim_s"] = fim_do_recorte
    for ex in doc.get("exclusoes", []):
        if "inicio_s" in ex:
            ex["inicio_s"] = round(ex["inicio_s"] + d, 3)

    # ── turnos ──
    pf = caso / "transcricao" / "falantes.json"
    turnos = _ler(pf)
    antigos_t = [dict(x) for x in turnos["turnos"]]
    for n, x in enumerate(turnos["turnos"]):
        anterior = antigos_t[n - 1] if n else None
        colado = anterior and abs(anterior["fim_s"] - antigos_t[n]["inicio_s"]) < 1e-6
        # turno colado ao anterior no arquivo antigo continua colado: um só limite, sem vão nem sobra
        x["inicio_s"] = turnos["turnos"][n - 1]["fim_s"] if colado else novo_inicio(antigos_t[n]["inicio_s"])
        x["fim_s"] = min(novo_fim(antigos_t[n]["fim_s"]), fim_do_recorte)
    turnos["turnos"][0]["inicio_s"] = round(reg["origem_inicio_s"], 3)

    # ── correções ──
    pc = caso / "transcricao" / "correcoes.json"
    corr = _ler(pc)
    mantidas, dispensadas, a_ler = [], [], []
    for c in corr["correcoes"]:
        centro = c["inicio_s"] + d
        perto = [s for s in novos if abs(s["inicio_s"] - centro) <= 3.0]
        seg = max(perto, key=lambda s: difflib.SequenceMatcher(
            None, normalizar(s["texto"]), normalizar(c["de"])).ratio(), default=None)
        if seg is None:
            a_ler.append((c, "nenhum segmento novo perto"))
        elif normalizar(seg["texto"]) == normalizar(c["para"]):
            dispensadas.append((c, seg["texto"]))
        elif seg["texto"] == c["de"]:
            mantidas.append({**c, "inicio_s": seg["inicio_s"]})
        else:
            a_ler.append((c, f"o segmento novo, em {seg['inicio_s']:.2f}, diz {seg['texto']!r}"))

    print("\n".join(linhas))
    print(f"\nturnos: {len(turnos['turnos'])} · sem par pelo fim (usou o limite mais próximo): "
          f"{len(sem_par)}" + (f" -> {sem_par}" if sem_par else ""))
    print(f"correções: {len(mantidas)} mantidas · {len(dispensadas)} dispensadas (o motor já acertou) "
          f"· {len(a_ler)} para ler")
    for c, txt in dispensadas:
        print(f"  dispensada em {c['inicio_s']:.2f}: {c['de']!r} → o motor novo escreveu {txt!r}")
    for c, motivo in a_ler:
        print(f"  ✗ LER {c['inicio_s']:.2f}: {c['de']!r} → {c['para']!r}: {motivo}")

    if not a.aplicar:
        print("\n(sem --aplicar: nada foi escrito)")
        return 0
    _escrever(pa, doc)
    _escrever(pf, turnos)
    corr["correcoes"] = mantidas
    _escrever(pc, corr)
    print("\n✓ alegações e turnos escritos no tempo da mídia nova")
    if a_ler:
        print(f"⚠️ {len(a_ler)} correção(ões) NÃO migradas (o texto novo é outro): reescreva-as em "
              "correcoes.json com o texto novo e a conferência feita na mídia nova.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
