# checagem-eleicoes-2026

**Um pipeline aberto que pega o vídeo de uma sabatina ou debate, transcreve, separa tudo que foi
afirmado como fato, confere alegação por alegação em fontes públicas e devolve o mesmo vídeo com
o veredito e as fontes queimados na imagem.**

Vale para os dois lados da mesa: o que o candidato afirma e o que o jornalista afirma dentro da
pergunta passam pelo mesmo funil.

```
🟢 VERDADEIRO      confere com as fontes primárias
🟡 IMPRECISO       essência certa, número ou recorte errado
🟠 SEM COMPROVAÇÃO afirmado como fato, sem lastro nas fontes
🔴 FALSO           as fontes contradizem o que foi dito
⚪ NÃO CHECÁVEL    opinião, promessa ou previsão
```

Cada card no vídeo traz a citação literal, o veredito, o dado apurado e as instituições
consultadas. O caminho inteiro — de que segundo saiu a frase, que fonte foi aberta, em que dia,
com que trecho copiado — fica no repositório, em texto, para qualquer pessoa refazer.

---

## Por que isto existe

Debate eleitoral produz afirmação factual em volume que ninguém confere em tempo real. Quando a
checagem sai, dois dias depois, ela chega a outro público e sem o vídeo.

Este projeto testa uma hipótese específica: **com transcrição local, busca em fonte pública e um
protocolo escrito, dá para produzir checagem rastreável em cima do próprio vídeo, e abrir o
processo inteiro para quem quiser contestar.**

⚠️ **Não é** apuração jornalística: não entrevista ninguém e não obtém documento inédito. Ele
confere o que foi dito contra o que já está publicado.
⛔ **Não** recomenda voto, ⛔ não mede intenção e ⛔ não soma placar de "quem mentiu mais" como
conclusão. Ver [`docs/METODOLOGIA.md` §8](docs/METODOLOGIA.md).

---

## As cinco travas que sustentam o resultado

1. ⛔ **Nenhum fato sai da memória do modelo.** Todo número tem URL, data de consulta e trecho
   copiado. O validador reprova o que não tiver.
2. ⛔ **Duas fontes independentes**, no mínimo, e pelo menos uma primária ou institucional quando
   a alegação é numérica.
3. ⛔ **Extração antes de checagem**, em arquivos separados, com a internet fechada na primeira.
   Quem já sabe a resposta escolhe as perguntas.
4. ⛔ **A citação tem que existir na transcrição.** O validador compara texto normalizado e reprova
   aspa parafraseada. É a trava mais importante do repositório.
5. ⛔ **A IA não publica.** Uma pessoa lê os cards e as fontes antes de qualquer coisa ir ao ar.

---

## Como rodar

### Pré-requisitos

| | Como instalar |
|---|---|
| Python 3.10+ | python.org |
| **ffmpeg / ffprobe** | `scoop install ffmpeg` · `apt install ffmpeg` · `brew install ffmpeg` |
| **whisper.cpp** (`whisper-cli`) | `scoop install whisper-cpp` · `brew install whisper-cpp` · ou compile |
| um agente de IA com busca na web | Claude Code, Cursor, ou você mesmo, à mão |

```bash
git clone https://github.com/Gabriel-Alexandre/checagem-eleicoes-2026
cd checagem-eleicoes-2026
pip install -r requirements.txt
python -m checagem ativos baixar-fontes
```

### O pipeline, passo a passo

```bash
SLUG=2026-08-27-sabatina-lula-globo

# PASSO 1 · assinar e preparar a mídia
python -m checagem midia $SLUG registrar
python -m checagem midia $SLUG audio
python -m checagem midia $SLUG recortar bloco-x --inicio 1200 --duracao 300 --motivo "..."

# PASSO 2 e 3 · transcrever e atribuir falante
python -m checagem transcrever $SLUG
python -m checagem falantes $SLUG

# PASSO 4 e 5 · a IA lê skills/extrair-alegacoes.md e skills/checar-alegacao.md
#               (não há comando: isto é julgamento, não script)

# PASSO 6, 7 e 8 · desenhar, renderizar, validar
python -m checagem overlay     $SLUG --recorte bloco-x
python -m checagem renderizar  $SLUG --recorte bloco-x
python -m checagem validar     $SLUG --recorte bloco-x
python -m checagem relatorio   $SLUG --recorte bloco-x
```

> 🔴 **Não existe comando "faz tudo", de propósito.** Os passos 4 e 5 são julgamento, e o 8 termina
> em revisão humana. Um botão de "roda sozinho" daria a impressão de que existe checagem automática
> de ponta a ponta aqui. Não existe.

Passo a passo detalhado, com o que conferir em cada etapa: [`docs/REPLICAR.md`](docs/REPLICAR.md).

---

## O que tem aqui

| Onde | O quê |
|---|---|
| [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) | 🔴 **o documento mais importante.** Vereditos, árvore de decisão, hierarquia de fontes, as armadilhas de enquadramento |
| [`docs/FONTES_BRASIL.md`](docs/FONTES_BRASIL.md) | onde mora cada dado público brasileiro, e as três armadilhas de cada área |
| [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) | cada decisão técnica e o que ela estava segurando |
| [`docs/IDENTIDADE_VISUAL.md`](docs/IDENTIDADE_VISUAL.md) | a tela: cores, tarja, moldura, tempo de leitura |
| [`docs/REPLICAR.md`](docs/REPLICAR.md) | do zero ao vídeo pronto, com o que conferir em cada passo |
| [`skills/`](skills/) | o que a IA executa em cada etapa, em texto |
| [`.cursor/rules/`](.cursor/rules/) | as regras sempre ativas (Cursor carrega sozinho; no Claude Code, ver [`CLAUDE.md`](CLAUDE.md)) |
| [`esquemas/`](esquemas/) | os contratos de dados, em JSON Schema |
| [`src/checagem/`](src/checagem/) | o pipeline, um módulo por passo |
| [`casos/`](casos/) | um caso por peça checada, com transcrição, alegações, checagens e relatório |
| [`ESTADO.md`](ESTADO.md) | onde o trabalho parou e o comando para retomar |

---

## Casos

| Caso | Peça | Estado |
|---|---|---|
| [`2026-08-27-sabatina-lula-globo`](casos/2026-08-27-sabatina-lula-globo/) | Sabatina de Luiz Inácio Lula da Silva na TV Globo, 27/ago/2026, 44min33s | prova de conceito rodada num recorte |

---

## Direito de resposta e correção

Qualquer pessoa citada — ou qualquer pessoa, ponto — pode contestar um veredito abrindo uma
**issue** com a fonte que sustenta a contestação. A resposta é dada com fonte, não com opinião.

Contestação procedente vira entrada em `casos/<slug>/CORRECOES.md`, com data, o que estava escrito,
o que passou a valer e o que motivou a mudança, e o relatório é corrigido. ⛔ **Nada é apagado em
silêncio.** Veredito que muda porque a evidência mudou é o processo funcionando.

---

## Limites conhecidos

- **A transcrição erra**, principalmente em nome próprio e número falado. O passo 2 manda conferir,
  e o que for corrigido fica registrado com o antes e o depois.
- **O falante é atribuído à mão.** É a decisão certa (ver [`ARQUITETURA §3`](docs/ARQUITETURA.md)),
  mas depende de alguém escrever os turnos com atenção.
- **Nem toda afirmação é igualmente checável.** Economia tem série pública; segurança tem defasagem
  de um ano; promessa não tem fonte. Isso pode produzir mais `SEM COMPROVAÇÃO` de um lado só porque
  aquele lado falou de assunto com fonte pior — e quando acontece, vai escrito no relatório.
- **O veredito vale para a data da fala.** Dado revisto depois entra como ressalva, ⛔ nunca como
  "falso porque hoje é outro número".
- **Um agente de IA erra.** Por isso o validador é uma porta que reprova, e por isso a publicação é
  decisão humana.

---

## Licença

- **Código** (`src/`, `tests/`, `esquemas/`): [MIT](LICENSE).
- **Documentação, metodologia, skills e relatórios de caso**:
  [CC BY 4.0](LICENSE-CONTEUDO) — use, adapte e publique, citando a origem.
- **Vídeo de origem**: não é distribuído por este repositório. Ele pertence a quem o produziu; o
  repositório guarda apenas o `sha256`, a transcrição e a checagem. O uso de trechos para checagem
  se apoia em citação para fins de crítica e informação.
- **Fonte Inter**: [SIL Open Font License](ativos/fontes/OFL.txt), baixada por script.
