"""A sabatina checada inteira (15/out/2026): caso novo, métricas dos dois lados da mesa, cortes curtos
com teto de tamanho, sugestão de cortes que não lê veredito e relatório da peça inteira.

Sem vídeo e sem rede: um caso sintético de sabatina num diretório temporário.
"""

from __future__ import annotations

import json
import sys
from importlib import import_module
from pathlib import Path

import pytest

from checagem import config as cfg
from checagem import metricas, relatorio

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ferramentas"))
derivar = import_module("derivar-recorte")
sugerir = import_module("sugerir-cortes")
novo_caso = import_module("novo-caso-debate")

SLUG = "2026-10-15-sabatina-teste"
RECORTE = "sabatina-completa"


def _meta():
    return {
        "slug": SLUG, "titulo": "Sabatina de teste", "data_do_evento": "2026-10-15", "veiculo": "TV",
        "formato": "sabatina", "duracao_s": 1200,
        "falantes": [{"nome": "Jornalista Um", "papel": "entrevistador", "cargo_ou_partido": "TV"},
                     {"nome": "Candidato Um", "papel": "entrevistado", "cargo_ou_partido": "PX"}],
        "midia": {"arquivo": "x.mp4", "sha256": "0" * 64, "bytes": 0, "largura": 1920, "altura": 1080, "fps": 30},
        "procedencia": {"como_foi_obtido": "teste", "url_oficial": None, "integralidade": "integral"},
    }


ASSUNTOS = ["economia", "saude", "seguranca-publica", "educacao", "inss", "meio-ambiente", "politica",
            "justica", "habitacao", "energia"]


def _transcricao():
    """20 min: a jornalista pergunta (8 s, afirmando um dado), o candidato responde em 4 frases de 6 s
    e uma de 4 s (promessa). Vinte rodadas de 60 s, um assunto por rodada."""
    segs, t = [], 0.0
    for r in range(20):
        segs.append({"inicio_s": t, "fim_s": t + 8, "texto": f"Pergunta {r} com o dado {r}{r}",
                     "falante": "Jornalista Um", "papel": "entrevistador"})
        t += 8
        for k in range(4):
            segs.append({"inicio_s": t, "fim_s": t + 6, "texto": f"Resposta {r} frase {k} com o numero {r}{k}",
                         "falante": "Candidato Um", "papel": "entrevistado"})
            t += 6
        segs.append({"inicio_s": t, "fim_s": t + 4, "texto": f"Prometo fazer {r}", "falante": "Candidato Um",
                     "papel": "entrevistado"})
        t += 4
        t += 24  # resto da rodada, fala sem alegação
        segs.append({"inicio_s": t - 24, "fim_s": t, "texto": f"Comentário {r} sem fato nenhum",
                     "falante": "Candidato Um", "papel": "entrevistado"})
    return {"segmentos": segs}


def _alegacoes(t):
    alegs = []
    for s in t["segmentos"]:
        if s["texto"].startswith("Comentário"):
            continue
        promessa = s["texto"].startswith("Prometo")
        rodada = int(round(s["inicio_s"] // 60))
        alegs.append({
            "id": f"A{len(alegs) + 1:03d}", "inicio_s": s["inicio_s"], "fim_s": s["fim_s"], "falante": s["falante"],
            "papel": s["papel"], "frase": s["texto"], "afirmacao": "a afirmacao isolada " + s["texto"],
            "tipo": "promessa" if promessa else "numero", "checavel": not promessa,
            "assunto": ASSUNTOS[rodada % len(ASSUNTOS)],
        })
    return alegs


def _checagem(aid, veredito="VERDADEIRO"):
    return {"id": aid, "veredito": veredito, "resumo": "resumo curto da checagem", "explicacao": "x" * 50,
            "fontes": [], "confianca": "alta"}


@pytest.fixture
def caso(tmp_path, monkeypatch):
    monkeypatch.setattr(cfg, "CASOS", tmp_path / "casos")
    monkeypatch.setattr(cfg, "RAIZ", tmp_path)
    pasta = tmp_path / "casos" / SLUG
    for sub in ("transcricao", "alegacoes", "checagens", "recortes"):
        (pasta / sub).mkdir(parents=True)
    (pasta / "CASO.json").write_text(json.dumps(_meta()), encoding="utf-8")
    t = _transcricao()
    (pasta / "transcricao" / "transcricao.json").write_text(json.dumps(t), encoding="utf-8")
    alegs = _alegacoes(t)
    (pasta / "alegacoes" / f"alegacoes-{RECORTE}.json").write_text(json.dumps(
        {"caso": SLUG, "gerado_em": "2026-10-15", "fonte_transcricao": "x", "recorte": RECORTE,
         "cobertura": {"inicio_s": 0.0, "fim_s": 1200.0}, "alegacoes": alegs}), encoding="utf-8")
    return pasta, t, alegs


def _com_checagens(pasta, alegs, vs=("VERDADEIRO", "IMPRECISO", "FALSO", "INSUSTENTAVEL")):
    doc = {"caso": SLUG, "gerado_em": "2026-10-15", "fonte_alegacoes": "x",
           "checagens": [_checagem(a["id"], "NAO_CHECAVEL" if not a["checavel"] else vs[i % len(vs)])
                         for i, a in enumerate(alegs)]}
    (pasta / "checagens" / f"checagens-{RECORTE}.json").write_text(json.dumps(doc), encoding="utf-8")
    return doc


def _rodar(modulo, monkeypatch, *args):
    monkeypatch.setattr("sys.argv", ["x.py", *args])
    return modulo.main()


# ─────────────────────────────────────────────────────────────────────


def test_o_recorte_da_peca_inteira_segue_o_formato():
    assert cfg.recorte_da_peca_inteira("sabatina") == "sabatina-completa"
    assert cfg.recorte_da_peca_inteira("debate") == "debate-completo"
    assert cfg.recorte_da_peca_inteira("entrevista") == "peca-completa"


def test_novo_caso_de_sabatina(tmp_path, monkeypatch):
    monkeypatch.setattr(cfg, "CASOS", tmp_path / "casos")
    monkeypatch.setattr(novo_caso, "RAIZ", tmp_path)
    slug = "2026-10-15-sabatina-nova"
    assert _rodar(novo_caso, monkeypatch, slug, "--formato", "sabatina", "--titulo", "T", "--data", "2026-10-15",
                  "--veiculo", "TV Globo", "--entrevistador", "Renata Lo Prete", "--candidato", "Lula (PT)",
                  "--narracao") == 0
    meta = json.loads((tmp_path / "casos" / slug / "CASO.json").read_text(encoding="utf-8"))
    assert meta["formato"] == "sabatina"
    assert [(f["nome"], f["papel"]) for f in meta["falantes"]] == [
        ("Renata Lo Prete", "entrevistador"), ("Lula", "entrevistado"), ("Narração (VT)", "narracao")]
    assert "sabatina-completa" in meta["procedencia"]["observacoes"]
    assert meta["procedencia"]["integralidade"] == "desconhecido"


def test_metricas_mostram_os_dois_lados_da_mesa(caso):
    pasta, t, alegs = caso
    doc = _com_checagens(pasta, alegs)
    m = metricas.calcular(_meta(), t, {"alegacoes": alegs}, doc)
    r = m["para_roteiro"]
    assert r["C1_NOME"] == "Candidato Um" and r["J1_NOME"] == "Jornalista Um"
    assert r["P_ENTREVISTADO_ALEG"] + r["P_ENTREVISTADOR_ALEG"] == r["N_ALEG"] == len(alegs)
    assert r["P_ENTREVISTADOR_ALEG"] == 20 and r["J1_ALEG"] == 20
    assert r["C1_NC"] == 20 and r["P_ENTREVISTADO_NC"] == 20
    assert r["N_PV"] == m["geral"]["percentual_dos_checaveis"]["VERDADEIRO"]
    assert r["C1_PV"] is not None


def test_derivar_recorte_infere_a_peca_e_aceita_corte_curto(caso, monkeypatch):
    pasta, _, alegs = caso
    _com_checagens(pasta, alegs)
    # rodada 0: pergunta em 0 a 8 e três frases de resposta até 26 s
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-01", "--inicio", "0", "--fim", "26") == 0
    a = json.loads((pasta / "alegacoes" / "alegacoes-corte-01.json").read_text(encoding="utf-8"))
    assert [x["id"] for x in a["alegacoes"]] == ["A001", "A002", "A003", "A004"]
    assert "fora_do_limite_de_tamanho" not in a


def test_derivar_recorte_recusa_corte_longo(caso, monkeypatch, capsys):
    pasta, _, alegs = caso
    _com_checagens(pasta, alegs)
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-01", "--inicio", "0", "--fim", "36") == 1
    assert "o máximo de um corte é 30 s" in capsys.readouterr().out


def test_derivar_recorte_recusa_corte_colado_no_outro(caso, monkeypatch, capsys):
    pasta, _, alegs = caso
    _com_checagens(pasta, alegs)
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-01", "--inicio", "0", "--fim", "26") == 0
    # rodada 1 começa em 60 s: a 34 s do corte-01, menos que os 60 s exigidos
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-02", "--inicio", "60", "--fim", "86") == 1
    assert "não são continuação" in capsys.readouterr().out


def test_derivar_recorte_recusa_soma_acima_do_teto(caso, monkeypatch, capsys):
    pasta, _, alegs = caso
    _com_checagens(pasta, alegs)
    for n in range(6):  # 6 x 26 s = 156 s
        ini = n * 120
        codigo = _rodar(derivar, monkeypatch, SLUG, "--para", f"corte-{n + 1:02d}", "--inicio", str(ini),
                        "--fim", str(ini + 26))
    assert codigo == 1
    assert "somando os cortes" in capsys.readouterr().out


def test_derivar_recorte_mais_longo_so_com_motivo_gravado(caso, monkeypatch):
    pasta, _, alegs = caso
    _com_checagens(pasta, alegs)
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-01", "--inicio", "0", "--fim", "36",
                  "--aceito-mais-longo", "o autor quis a resposta inteira") == 0
    a = json.loads((pasta / "alegacoes" / "alegacoes-corte-01.json").read_text(encoding="utf-8"))
    assert a["fora_do_limite_de_tamanho"]["motivo"] == "o autor quis a resposta inteira"


def test_sugestao_de_cortes_respeita_os_limites_e_nao_le_veredito(caso, monkeypatch):
    pasta, _, alegs = caso
    # checagens ilegíveis: se a ferramenta abrisse o arquivo de vereditos, quebraria aqui
    (pasta / "checagens" / f"checagens-{RECORTE}.json").write_text("isto não é json", encoding="utf-8")
    assert _rodar(sugerir, monkeypatch, SLUG) == 0
    s = json.loads((pasta / "recortes" / "SUGESTAO_DE_CORTES.json").read_text(encoding="utf-8"))
    cortes = s["escolhidos"]
    assert s["leu_checagens"] is False
    assert cfg.CORTES_QUANTIDADE[0] <= len(cortes) <= cfg.CORTES_QUANTIDADE[1]
    assert all(c["duracao_s"] <= cfg.CORTE_RECOMENDADO_S + 0.01 for c in cortes)
    assert s["total_s"] <= cfg.CORTES_TOTAL_MAX_S
    for x, y in zip(cortes, cortes[1:], strict=False):
        assert y["inicio_s"] - x["fim_s"] >= cfg.CORTES_INTERVALO_MIN_S
    assert len({c["assunto"] for c in cortes}) == len(cortes), "um assunto por corte na primeira passada"
    # nenhuma alegação cortada na borda
    for c in cortes:
        for a in alegs:
            dentro = a["inicio_s"] >= c["inicio_s"] - 0.05 and a["fim_s"] <= c["fim_s"] + 0.05
            fora = a["fim_s"] <= c["inicio_s"] + 0.05 or a["inicio_s"] >= c["fim_s"] - 0.05
            assert dentro or fora
    # o confronto (jornalista afirma, candidato responde) pesa
    assert all(c["confronto"] for c in cortes)
    assert "derivar-recorte.py" in (pasta / "recortes" / "SUGESTAO_DE_CORTES.md").read_text(encoding="utf-8")


def test_sugestao_aceita_trecho_fixado_pelo_autor(caso, monkeypatch):
    pasta, _, _ = caso
    assert _rodar(sugerir, monkeypatch, SLUG, "--fixar", "300-326", "o trecho mais comentado da noite") == 0
    s = json.loads((pasta / "recortes" / "SUGESTAO_DE_CORTES.json").read_text(encoding="utf-8"))
    fixo = [c for c in s["escolhidos"] if c.get("fixado_pelo_autor")]
    assert len(fixo) == 1 and fixo[0]["motivo"].startswith("escolha do autor, fora do critério")


def test_relatorio_da_peca_inteira_sem_video(caso, monkeypatch):
    pasta, t, alegs = caso
    doc = _com_checagens(pasta, alegs)
    m = metricas.calcular(_meta(), t, json.loads(
        (pasta / "alegacoes" / f"alegacoes-{RECORTE}.json").read_text(encoding="utf-8")), doc, recorte=RECORTE)
    (pasta / "metricas").mkdir()
    (pasta / "metricas" / f"metricas-{RECORTE}.json").write_text(json.dumps(m), encoding="utf-8")
    assert _rodar(derivar, monkeypatch, SLUG, "--para", "corte-01", "--inicio", "0", "--fim", "26") == 0
    destino = relatorio.gerar(SLUG, recorte=RECORTE)
    texto = destino.read_text(encoding="utf-8")
    assert "a peça inteira (`sabatina-completa`)" in texto
    assert "## Por falante" in texto and "Jornalista Um" in texto
    assert "`corte-01`" in texto
    assert f"python -m checagem metricas {SLUG} --recorte {RECORTE}" in texto
