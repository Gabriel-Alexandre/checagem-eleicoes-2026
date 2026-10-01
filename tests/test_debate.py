"""O braço de debate: métricas por falante, lotes de extração e checagem, e derivação de recorte.

Sem vídeo e sem rede. Os casos reais do repositório servem de regressão para as métricas; o resto
roda sobre um caso sintético de quatro candidatos num diretório temporário.
"""

from __future__ import annotations

import json
import sys
from importlib import import_module
from pathlib import Path

import pytest

from checagem import config as cfg
from checagem import metricas
from checagem.util import ErroDeExecucao

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ferramentas"))
lotes = import_module("lotes-de-debate")
derivar = import_module("derivar-recorte")


# ─────────────────────────────────────────────────────────────────────
# Caso sintético
# ─────────────────────────────────────────────────────────────────────

CANDIDATOS = ["Ana Souza", "Bruno Lima", "Carla Dias", "Diego Reis"]


def _meta():
    return {
        "slug": "2026-10-01-debate-teste", "titulo": "Debate de teste", "data_do_evento": "2026-10-01",
        "veiculo": "TV", "formato": "debate", "duracao_s": 1200,
        "falantes": [{"nome": "Mediador Um", "papel": "entrevistador"}]
        + [{"nome": n, "papel": "entrevistado"} for n in CANDIDATOS],
    }


def _transcricao():
    """20 min: o mediador pergunta, cada candidato responde 60 s, quatro rodadas."""
    segs, t = [], 0.0
    for r in range(4):
        for i, nome in enumerate(CANDIDATOS):
            segs.append({"inicio_s": t, "fim_s": t + 20, "texto": f"Pergunta da rodada {r} numero {i} sobre o assunto", "falante": "Mediador Um", "papel": "entrevistador"})
            t += 20
            segs.append({"inicio_s": t, "fim_s": t + 50, "texto": f"Resposta {nome} rodada {r} com o dado {r}{i}{r}{i}", "falante": nome, "papel": "entrevistado"})
            t += 50
    return {"segmentos": segs}


def _alegacoes(transcricao):
    alegs = []
    for i, s in enumerate(transcricao["segmentos"]):
        if s["falante"] == "Mediador Um" and i % 4:
            continue
        alegs.append({
            "id": f"A{len(alegs) + 1:03d}", "inicio_s": s["inicio_s"], "fim_s": s["fim_s"], "falante": s["falante"],
            "papel": s["papel"], "frase": s["texto"], "afirmacao": "a afirmacao isolada " + s["texto"],
            "tipo": "numero", "checavel": True, "assunto": "economia" if i % 3 else "saude",
        })
    return alegs


@pytest.fixture
def caso(tmp_path, monkeypatch):
    monkeypatch.setattr(cfg, "CASOS", tmp_path / "casos")
    monkeypatch.setattr(lotes, "RAIZ", tmp_path)
    slug = "2026-10-01-debate-teste"
    pasta = tmp_path / "casos" / slug
    (pasta / "transcricao").mkdir(parents=True)
    (pasta / "alegacoes").mkdir()
    (pasta / "checagens").mkdir()
    (pasta / "CASO.json").write_text(json.dumps(_meta()), encoding="utf-8")
    t = _transcricao()
    (pasta / "transcricao" / "transcricao.json").write_text(json.dumps(t), encoding="utf-8")
    return slug, pasta, t


def _checagem(aid, veredito="VERDADEIRO"):
    return {"id": aid, "veredito": veredito, "resumo": "resumo curto da checagem", "explicacao": "x" * 50,
            "fontes": [], "confianca": "alta"}


# ─────────────────────────────────────────────────────────────────────
# Métricas
# ─────────────────────────────────────────────────────────────────────


def test_metricas_contam_por_falante_na_ordem_da_primeira_fala(caso):
    _, _, t = caso
    alegs = _alegacoes(t)
    vs = ["VERDADEIRO", "FALSO", "IMPRECISO", "INSUSTENTAVEL"]
    checagens = {"checagens": [_checagem(a["id"], vs[i % 4]) for i, a in enumerate(alegs)]}
    m = metricas.calcular(_meta(), t, {"alegacoes": alegs}, checagens)
    assert m["geral"]["alegacoes"] == len(alegs)
    assert sum(m["geral"]["por_veredito"].values()) == len(alegs)
    # a ordem é a da primeira fala: o mediador abre, depois cada candidato como foi respondendo
    assert [f["nome"] for f in m["por_falante"]] == ["Mediador Um", *CANDIDATOS]
    assert sum(f["alegacoes"] for f in m["por_falante"]) == len(alegs)


def test_metricas_nunca_ordenam_por_resultado(caso):
    """A ordem não pode mudar quando os vereditos mudam: ordenar por falsidade viraria ranking."""
    _, _, t = caso
    alegs = _alegacoes(t)
    todos_falsos = {"checagens": [_checagem(a["id"], "FALSO") for a in alegs]}
    todos_ok = {"checagens": [_checagem(a["id"], "VERDADEIRO") for a in alegs]}
    a = metricas.calcular(_meta(), t, {"alegacoes": alegs}, todos_falsos)
    b = metricas.calcular(_meta(), t, {"alegacoes": alegs}, todos_ok)
    assert [f["nome"] for f in a["por_falante"]] == [f["nome"] for f in b["por_falante"]]


def test_percentual_e_dos_checaveis_e_nao_checavel_fica_fora(caso):
    _, _, t = caso
    alegs = _alegacoes(t)[:4]
    alegs[0].update({"tipo": "opiniao", "checavel": False})
    checagens = {"checagens": [_checagem(alegs[0]["id"], "NAO_CHECAVEL")]
                 + [_checagem(a["id"], "VERDADEIRO" if i % 2 else "FALSO") for i, a in enumerate(alegs[1:])]}
    m = metricas.calcular(_meta(), t, {"alegacoes": alegs}, checagens)
    assert m["geral"]["checaveis"] == 3 and m["geral"]["nao_checaveis"] == 1
    assert m["geral"]["percentual_dos_checaveis"]["FALSO"] == pytest.approx(66.7, abs=0.1)


def test_metricas_recusam_peca_com_alegacao_sem_checagem(caso):
    _, _, t = caso
    alegs = _alegacoes(t)
    with pytest.raises(ErroDeExecucao, match="sem checagem"):
        metricas.calcular(_meta(), t, {"alegacoes": alegs}, {"checagens": [_checagem(alegs[0]["id"])]})


def test_markdown_traz_as_ressalvas_e_o_aviso_de_assimetria(caso):
    _, _, t = caso
    alegs = [a for a in _alegacoes(t) if a["falante"] != "Diego Reis"]
    m = metricas.calcular(_meta(), t, {"alegacoes": alegs}, {"checagens": [_checagem(a["id"]) for a in alegs]})
    texto = metricas.para_markdown(m)
    assert "Ressalvas (valem sempre)" in texto
    assert "não serve para dizer quem mente mais" in texto
    assert any("Diego Reis" in a for a in m["avisos"]), "candidato sem alegação checável tem que aparecer"


def test_tempo_de_fala_respeita_a_cobertura(caso):
    _, _, t = caso
    alegs = _alegacoes(t)[:3]
    doc = {"alegacoes": alegs, "cobertura": {"inicio_s": 0, "fim_s": 140}}
    m = metricas.calcular(_meta(), t, doc, {"checagens": [_checagem(a["id"]) for a in alegs]})
    assert sum(f["fala_s"] for f in m["por_falante"]) == pytest.approx(140, abs=0.1)


ALVOS_REAIS = [
    (c.name, r.stem[len("alegacoes-"):])
    for c in sorted(cfg.CASOS.glob("*")) if (c / "CASO.json").exists()
    for r in sorted((c / "alegacoes").glob("alegacoes-*.json"))
    if (c / "checagens" / f"checagens-{r.stem[len('alegacoes-'):]}.json").exists()
] if cfg.CASOS.exists() else []


@pytest.mark.parametrize("slug,recorte", ALVOS_REAIS)
def test_metricas_nos_casos_reais_batem_com_as_checagens(slug, recorte):
    caso_ = cfg.pasta_do_caso(slug)
    meta = json.loads((caso_ / "CASO.json").read_text(encoding="utf-8"))
    nome_t = caso_ / "transcricao" / f"transcricao-{recorte}.json"
    if not nome_t.exists():
        nome_t = caso_ / "transcricao" / "transcricao.json"
    t = json.loads(nome_t.read_text(encoding="utf-8"))
    a = json.loads((caso_ / "alegacoes" / f"alegacoes-{recorte}.json").read_text(encoding="utf-8"))
    c = json.loads((caso_ / "checagens" / f"checagens-{recorte}.json").read_text(encoding="utf-8"))
    m = metricas.calcular(meta, t, a, c, recorte=recorte)
    assert m["geral"]["alegacoes"] == len(a["alegacoes"])
    for v in metricas.ORDEM_DOS_VEREDITOS:
        assert m["geral"]["por_veredito"][v] == sum(1 for x in c["checagens"] if x["veredito"] == v)
    assert sum(f["alegacoes"] for f in m["por_falante"]) == len(a["alegacoes"])


# ─────────────────────────────────────────────────────────────────────
# Lotes
# ─────────────────────────────────────────────────────────────────────


def _responder_lote(pasta: Path, indice, *, pular=None):
    """Faz o papel do agente: uma alegação por segmento de candidato dentro da janela."""
    t = json.loads((pasta / "transcricao" / "transcricao.json").read_text(encoding="utf-8"))
    for lote in indice:
        if lote["n"] == pular:
            continue
        alegs = []
        for s in t["segmentos"]:
            if s["papel"] == "entrevistado" and lote["inicio_s"] - 0.5 <= s["inicio_s"] <= lote["fim_s"] + 0.5:
                alegs.append({"id": f"A{len(alegs) + 1:03d}", "inicio_s": s["inicio_s"], "fim_s": s["fim_s"],
                              "falante": s["falante"], "papel": s["papel"], "frase": s["texto"],
                              "afirmacao": "a afirmacao isolada " + s["texto"], "tipo": "numero",
                              "checavel": True, "assunto": "economia"})
        saida = Path(lote["saida"])
        saida = saida if saida.is_absolute() else pasta.parents[1] / saida
        saida.parent.mkdir(parents=True, exist_ok=True)
        saida.write_text(json.dumps({"caso": pasta.name, "gerado_em": "2026-10-01", "fonte_transcricao": "x",
                                     "cobertura": {"inicio_s": lote["inicio_s"], "fim_s": lote["fim_s"]},
                                     "alegacoes": alegs}), encoding="utf-8")


def test_divisao_corta_so_em_virada_de_turno_e_cobre_tudo(caso):
    slug, pasta, t = caso
    lotes.dividir_extracao(slug, minutos=5, contexto_s=30)
    indice = json.loads((pasta / "lotes" / "extracao" / "lotes.json").read_text(encoding="utf-8"))["lotes"]
    assert len(indice) >= 3
    inicios_de_turno = {s["inicio_s"] for i, s in enumerate(t["segmentos"])
                        if i == 0 or s["falante"] != t["segmentos"][i - 1]["falante"]}
    for lote in indice:
        assert lote["inicio_s"] in inicios_de_turno
    for x, y in zip(indice, indice[1:], strict=False):
        assert y["inicio_s"] == pytest.approx(x["fim_s"], abs=0.01), "buraco entre lotes"
    assert indice[0]["inicio_s"] == 0 and indice[-1]["fim_s"] == pytest.approx(t["segmentos"][-1]["fim_s"])
    texto = (pasta / "lotes" / "extracao" / "lote-02.txt").read_text(encoding="utf-8")
    assert "INTERNET FECHADA" in texto and "contexto, NÃO extrair" in texto


def test_juncao_renumera_e_prova_a_cobertura(caso):
    slug, pasta, t = caso
    lotes.dividir_extracao(slug, minutos=5, contexto_s=30)
    indice = json.loads((pasta / "lotes" / "extracao" / "lotes.json").read_text(encoding="utf-8"))["lotes"]
    _responder_lote(pasta, indice)
    assert lotes.juntar_extracao(slug, "debate-completo") == 0
    doc = json.loads((pasta / "alegacoes" / "alegacoes-debate-completo.json").read_text(encoding="utf-8"))
    ids = [a["id"] for a in doc["alegacoes"]]
    assert ids == [f"A{i:03d}" for i in range(1, len(ids) + 1)]
    assert [a["inicio_s"] for a in doc["alegacoes"]] == sorted(a["inicio_s"] for a in doc["alegacoes"])
    assert len(ids) == 16  # quatro rodadas x quatro candidatos, nenhuma duplicada
    assert doc["cobertura"]["fim_s"] == pytest.approx(t["segmentos"][-1]["fim_s"])


def test_juncao_recusa_lote_que_faltou(caso, capsys):
    slug, pasta, _ = caso
    lotes.dividir_extracao(slug, minutos=5, contexto_s=30)
    indice = json.loads((pasta / "lotes" / "extracao" / "lotes.json").read_text(encoding="utf-8"))["lotes"]
    _responder_lote(pasta, indice, pular=2)
    assert lotes.juntar_extracao(slug, "debate-completo") == 1
    assert not (pasta / "alegacoes" / "alegacoes-debate-completo.json").exists()
    assert "faltam os lotes [2]" in capsys.readouterr().out


def test_juncao_recusa_alegacao_fora_da_janela_do_lote(caso, capsys):
    slug, pasta, _ = caso
    lotes.dividir_extracao(slug, minutos=5, contexto_s=30)
    indice = json.loads((pasta / "lotes" / "extracao" / "lotes.json").read_text(encoding="utf-8"))["lotes"]
    _responder_lote(pasta, indice)
    arq = Path(indice[0]["saida"])
    arq = arq if arq.is_absolute() else pasta.parents[1] / arq
    doc = json.loads(arq.read_text(encoding="utf-8"))
    doc["alegacoes"][0]["inicio_s"] = indice[-1]["fim_s"] - 5
    arq.write_text(json.dumps(doc), encoding="utf-8")
    assert lotes.juntar_extracao(slug, "debate-completo") == 1
    assert "fora da janela do lote" in capsys.readouterr().out


def test_juncao_recusa_veredito_na_extracao(caso, capsys):
    slug, pasta, _ = caso
    lotes.dividir_extracao(slug, minutos=5, contexto_s=30)
    indice = json.loads((pasta / "lotes" / "extracao" / "lotes.json").read_text(encoding="utf-8"))["lotes"]
    _responder_lote(pasta, indice)
    arq = Path(indice[1]["saida"])
    arq = arq if arq.is_absolute() else pasta.parents[1] / arq
    doc = json.loads(arq.read_text(encoding="utf-8"))
    doc["alegacoes"][0]["veredito"] = "FALSO"
    arq.write_text(json.dumps(doc), encoding="utf-8")
    assert lotes.juntar_extracao(slug, "debate-completo") == 1
    assert "veredito na extração" in capsys.readouterr().out


def test_checagem_em_lotes_junta_e_acusa_o_que_falta(caso, capsys):
    slug, pasta, t = caso
    alegs = _alegacoes(t)
    (pasta / "alegacoes" / "alegacoes-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_transcricao": "x", "alegacoes": alegs}), encoding="utf-8")
    lotes.dividir_checagem(slug, "debate-completo", tamanho=5)
    pedidos = json.loads((pasta / "lotes" / "checagem" / "pedidos.json").read_text(encoding="utf-8"))["pedidos"]
    assert sum(len(p["ids"]) for p in pedidos) == len(alegs)
    pasta_c = pasta / "checagens" / "lotes"
    pasta_c.mkdir(parents=True, exist_ok=True)
    for p in pedidos[:-1]:
        (pasta_c / f"checagens-lote-{p['n']:02d}.json").write_text(
            json.dumps({"checagens": [_checagem(i) for i in p["ids"]]}), encoding="utf-8")
    assert lotes.juntar_checagem(slug, "debate-completo") == 1
    assert "sem checagem" in capsys.readouterr().out
    ultimo = pedidos[-1]
    (pasta_c / f"checagens-lote-{ultimo['n']:02d}.json").write_text(
        json.dumps({"checagens": [_checagem(i) for i in ultimo["ids"]]}), encoding="utf-8")
    assert lotes.juntar_checagem(slug, "debate-completo") == 0
    final = json.loads((pasta / "checagens" / "checagens-debate-completo.json").read_text(encoding="utf-8"))
    assert [c["id"] for c in final["checagens"]] == [a["id"] for a in alegs]


def test_checagem_em_lotes_recusa_id_inventado(caso, capsys):
    slug, pasta, t = caso
    alegs = _alegacoes(t)[:3]
    (pasta / "alegacoes" / "alegacoes-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_transcricao": "x", "alegacoes": alegs}), encoding="utf-8")
    pasta_c = pasta / "checagens" / "lotes"
    pasta_c.mkdir(parents=True)
    (pasta_c / "checagens-lote-01.json").write_text(json.dumps(
        {"checagens": [_checagem("A001"), _checagem("A002"), _checagem("A003"), _checagem("A099")]}), encoding="utf-8")
    assert lotes.juntar_checagem(slug, "debate-completo") == 1
    assert "id inventado" in capsys.readouterr().out


# ─────────────────────────────────────────────────────────────────────
# Derivação de recorte
# ─────────────────────────────────────────────────────────────────────


def _derivar(monkeypatch, *args):
    monkeypatch.setattr("sys.argv", ["derivar-recorte.py", *args])
    return derivar.main()


def test_derivar_recorte_herda_as_checagens_com_os_mesmos_ids(caso, monkeypatch):
    slug, pasta, t = caso
    alegs = _alegacoes(t)
    (pasta / "alegacoes" / "alegacoes-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_transcricao": "x", "recorte": "debate-completo",
         "alegacoes": alegs}), encoding="utf-8")
    (pasta / "checagens" / "checagens-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_alegacoes": "x",
         "checagens": [_checagem(a["id"]) for a in alegs]}), encoding="utf-8")
    # um trecho que contém exatamente as alegações da rodada 1 (t = 280 a 560)
    assert _derivar(monkeypatch, slug, "--para", "corte-01", "--inicio", "280", "--fim", "560") == 0
    a = json.loads((pasta / "alegacoes" / "alegacoes-corte-01.json").read_text(encoding="utf-8"))
    c = json.loads((pasta / "checagens" / "checagens-corte-01.json").read_text(encoding="utf-8"))
    assert a["recorte"] == "corte-01" and a["cobertura"] == {"inicio_s": 280.0, "fim_s": 560.0}
    assert [x["id"] for x in c["checagens"]] == [x["id"] for x in a["alegacoes"]]
    assert all(x["inicio_s"] >= 280 - 0.05 and x["fim_s"] <= 560 + 0.05 for x in a["alegacoes"])


def test_derivar_recorte_recusa_alegacao_cortada_na_borda(caso, monkeypatch, capsys):
    slug, pasta, t = caso
    alegs = _alegacoes(t)
    (pasta / "alegacoes" / "alegacoes-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_transcricao": "x", "alegacoes": alegs}), encoding="utf-8")
    (pasta / "checagens" / "checagens-debate-completo.json").write_text(json.dumps(
        {"caso": slug, "gerado_em": "2026-10-01", "fonte_alegacoes": "x",
         "checagens": [_checagem(a["id"]) for a in alegs]}), encoding="utf-8")
    assert _derivar(monkeypatch, slug, "--para", "corte-02", "--inicio", "290", "--fim", "560") == 1
    assert "atravessam a borda" in capsys.readouterr().out
