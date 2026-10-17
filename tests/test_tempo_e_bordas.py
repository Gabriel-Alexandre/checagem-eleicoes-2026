"""As duas ferramentas que nasceram da validação final do caso de 15/out/2026 (CORRECOES.md §5):
o tempo de cada alegação medido palavra por palavra e as bordas dos cortes na pausa da voz.
Só as partes puras: o alinhamento, a regra de aceitar dentro da frase de origem, a ordem dos ids,
o nível em dB e a busca da pausa, sem whisper e sem arquivo de áudio.
"""

from __future__ import annotations

import math
import sys
from array import array
from importlib import import_module
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ferramentas"))
mt = import_module("medir-tempo-das-alegacoes")
bp = import_module("bordas-na-pausa")


# ─────────────────────────────────────────────────────────────────────
# Tempo da alegação, palavra por palavra
# ─────────────────────────────────────────────────────────────────────

PALAVRAS = [  # (palavra, começo, fim), como o whisper.cpp devolve com -ml 1 -sow
    ("Olha,", 10.0, 10.3), ("eu", 10.3, 10.4), ("acho", 10.4, 10.7), ("que", 10.7, 10.8),
    ("o", 10.8, 10.9), ("André", 16.0, 16.3), ("Mendonça", 16.3, 16.8), ("também", 16.8, 17.1),
    ("está", 17.1, 17.3), ("implicado.", 17.3, 17.9),
]


def test_normalizar_tira_acento_e_pontuacao():
    assert mt.normalizar("Trilhão,") == "trilhao"
    assert mt.normalizar("4,5%") == "45%"
    assert mt.tokens("O  André, também!") == ["o", "andre", "tambem"]


def test_a_alegacao_no_meio_da_frase_ganha_o_tempo_da_palavra():
    """O caso da A075: a frase de origem começa 6 s antes da alegação."""
    comeco, fim = mt.partes_da_frase("André Mendonça também está implicado")
    t, n, desloc = mt.alinhar(PALAVRAS, comeco)
    assert (t, n, desloc) == (16.0, 5, 0)       # e não 10,0, o começo do segmento
    t_fim, n_fim, _ = mt.alinhar(PALAVRAS, fim, do_fim=True)
    assert (t_fim, n_fim) == (17.9, 5)


def test_palavra_que_o_motor_comeu_desloca_o_alinhamento():
    t, n, desloc = mt.alinhar(PALAVRAS, ["ministro", "andre", "mendonca", "tambem"])
    assert (t, desloc) == (16.0, 1) and n == 3


def test_a075_de_15_out_nao_cai_no_trecho_repetido_da_frase_anterior():
    """A passada palavra por palavra escreveu 'Mendoza'; o trecho mais longo que casava era
    'também está implicado', dito antes sobre Toffoli. O começo certo é o 'o André' (1018,94 s)."""
    falas = ("o@1016.28 Toffoli@1016.33 também@1016.70 está@1016.96 implicado,@1017.12 o@1018.94 "
             "André@1018.99 Mendoza@1019.24 também@1019.57 está@1019.86 implicado@1020.05 e@1020.53")
    pal = []
    for item in falas.split():
        w, t = item.split("@")
        pal.append((w, float(t), float(t) + 0.2))
    comeco, _ = mt.partes_da_frase("o André Mendonça também está implicado")
    t, n, desloc = mt.alinhar(pal, comeco, perto_de=1018.9)
    assert (t, desloc) == (1018.94, 0)


def test_uma_palavra_sozinha_nao_basta_para_alinhar():
    assert mt.alinhar(PALAVRAS, ["mendonca", "xyz"]) is None
    assert mt.alinhar(PALAVRAS, ["mendonca"]) is None


def test_citacao_com_corte_usa_a_primeira_e_a_ultima_parte():
    comeco, fim = mt.partes_da_frase("nós precisamos [...] o Farmácia Popular voltar a funcionar")
    assert comeco == ["nos", "precisamos"]
    assert fim[-2:] == ["a", "funcionar"]


def test_ponto_fora_da_frase_de_origem_e_recusado():
    assert mt.dentro(16.0, 10.0, 18.0)
    assert mt.dentro(9.8, 10.0, 18.0)          # 0,3 s de folga
    assert not mt.dentro(25.0, 10.0, 18.0)


def test_frase_de_origem_junta_os_segmentos_que_a_alegacao_toca():
    segs = [{"inicio_s": 0.0, "fim_s": 9.9}, {"inicio_s": 10.0, "fim_s": 14.0},
            {"inicio_s": 14.0, "fim_s": 18.0}, {"inicio_s": 18.0, "fim_s": 22.0}]
    assert mt.frase_de_origem(segs, "", 12.0, 15.0) == (10.0, 18.0)


def test_ordem_cronologica_acusa_o_id_que_volta_no_tempo():
    assert mt.ordem_cronologica([("A001", 1.0), ("A002", 3.0), ("A003", 2.5), ("A004", 4.0)]) == ["A003"]
    assert mt.ordem_cronologica([("A001", 1.0), ("A002", 1.0)]) == []


# ─────────────────────────────────────────────────────────────────────
# Bordas na pausa da voz
# ─────────────────────────────────────────────────────────────────────

TAXA = 1000  # 1 kHz basta para o teste: 40 ms = 40 amostras


def _sinal(trechos):
    """[(duração_s, amplitude)] -> amostras de um seno de 100 Hz com aquela amplitude."""
    a = array("h")
    for dur, amp in trechos:
        for i in range(int(dur * TAXA)):
            a.append(int(amp * math.sin(2 * math.pi * 100 * i / TAXA)))
    return a


def test_rms_db_de_silencio_e_de_fundo_de_escala():
    assert bp.rms_db(array("h", [0] * 40)) == -120.0
    cheio = _sinal([(0.04, 32767)])
    assert -3.5 < bp.rms_db(cheio) < -2.5        # seno cheio: cerca de -3 dB


def test_borda_na_fala_vai_para_a_pausa_sem_cortar_a_alegacao():
    # 0 a 1 s fala; 1,0 a 1,3 s pausa; 1,3 a 2,0 s fala (a palavra seguinte)
    s = _sinal([(1.0, 8000), (0.3, 30), (0.7, 8000)])
    fala = bp.nivel_da_fala(s, TAXA, 0.0, 0.0, 1.0)
    # a borda caiu no começo da palavra seguinte (1,4 s), e a alegação termina em 0,95 s
    r = bp.nova_borda(s, TAXA, 0.0, borda=1.4, lado="fim", fala_db=fala, limiar=12, busca=0.8, trava=0.95)
    assert r["movida"] and 1.0 <= r["depois"] <= 1.3
    assert r["depois_db_abaixo_da_fala"] >= 12
    assert r["antes_db_abaixo_da_fala"] < 12


def test_borda_ja_na_pausa_nao_se_mexe():
    s = _sinal([(1.0, 8000), (0.3, 30), (0.7, 8000)])
    fala = bp.nivel_da_fala(s, TAXA, 0.0, 0.0, 1.0)
    r = bp.nova_borda(s, TAXA, 0.0, borda=1.2, lado="fim", fala_db=fala, limiar=12, busca=0.8, trava=0.95)
    assert not r["movida"] and r["depois"] == 1.2


def test_o_comeco_nunca_passa_do_comeco_da_primeira_alegacao():
    # pausa só DEPOIS de onde a alegação começa: a busca não pode ir lá
    s = _sinal([(1.0, 8000), (0.3, 30), (0.7, 8000)])
    fala = bp.nivel_da_fala(s, TAXA, 0.0, 0.0, 2.0)
    r = bp.nova_borda(s, TAXA, 0.0, borda=0.5, lado="inicio", fala_db=fala, limiar=12, busca=0.8, trava=0.6)
    assert r["depois"] <= 0.6


def test_a044_volta_quando_o_ajuste_passaria_da_a045():
    """Caso de 15/out: a A044 medida em 531,49 s ficaria depois da A045 (530,6 s), que a contém."""
    t, notas = mt.acertar_ordem([("A043", 520.0), ("A044", 531.49), ("A045", 530.6)], [519.0, 530.6, 530.6])
    assert t == [520.0, 530.6, 530.6] and len(notas) == 1


def test_sem_tempo_antigo_que_sirva_fica_igual_ao_seguinte():
    t, _ = mt.acertar_ordem([("A001", 12.0), ("A002", 11.0)], [11.5, 11.0])
    assert t == [11.0, 11.0]


def test_janelas_que_se_sobrepoem_viram_um_bloco_so():
    assert mt.juntar_janelas([(10, 20), (15, 25), (30, 40), (39, 41)]) == [(10, 25), (30, 41)]


def test_par_de_palavras_repetido_na_janela_nao_alinha():
    """A034 de 16/out: com 'mudou' escrito de outro jeito, só 'o senhor' casava, e ele aparece
    duas vezes na janela. Par ambíguo não vale; o começo fica sem medida (recusado)."""
    pal = [(w, t, t + 0.2) for w, t in [("o", 362.95), ("senhor", 363.21), ("chamou", 363.36),
                                         ("o", 367.03), ("senhor", 367.11), ("mudô", 367.60)]]
    assert mt.alinhar(pal, ["o", "senhor", "mudou", "de"], perto_de=365.4) is None


def test_so_medir_mede_o_corte_entregue_e_nao_a_sugestao(tmp_path):
    """Validação final de 17/out: o --so-medir lia a sugestão e media bordas de antes da pausa."""
    (tmp_path / "recortes").mkdir()
    (tmp_path / "recortes" / "RECORTES.json").write_text(
        '{"recortes": [{"id": "corte-01", "origem_inicio_s": 963.38, "duracao_s": 14.19}, {"id": "x"}]}',
        encoding="utf-8")
    assert bp.bordas_entregues(tmp_path) == {"corte-01": (963.38, 977.57)}
    assert bp.bordas_entregues(tmp_path / "sem-recortes") == {}
