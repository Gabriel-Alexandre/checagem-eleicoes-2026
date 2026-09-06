# CLAUDE.md — como operar neste repositório

Este arquivo existe por um motivo específico: as regras deste repo moram em `.cursor/rules/*.mdc`, que o **Cursor carrega sozinho** e o **Claude Code não**. Sem ele, uma sessão no Claude Code trabalharia sem a doutrina.

> ⚠️ **Este arquivo é roteador, não fonte de verdade.** Ele não guarda metodologia, veredito nem estado. Tudo aqui é ponteiro. Se você achar aqui um fato que contradiz o arquivo dono dele, **o dono ganha** e você reporta a divergência.

---

## 1. As cinco regras que valem sobre todas as outras

1. ⛔ **Nenhum fato sai da memória do modelo.** Número, data, valor, citação de lei, decisão judicial: ou tem URL consultada com trecho copiado, ou não entra. Vale inclusive quando você tem certeza.
2. ⛔ **Duas fontes independentes**, no mínimo, para todo veredito que não seja `NAO_CHECAVEL`. Duas matérias com o mesmo parágrafo são **uma** fonte.
3. ⛔ **A régua é a mesma para os dois lados da mesa.** Pergunta de jornalista que afirma fato é alegação.
4. ⛔ **Nunca julgue intenção.** "Tentou esconder", "sabia que", "omitiu de propósito" não entram em lugar nenhum.
5. ⛔ **A IA não publica.** Nada vai ao ar sem uma pessoa ter lido os cards e as fontes.

Doutrina completa: [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).

---

## 2. Leia isto antes de responder qualquer coisa sobre o projeto

| Ordem | Arquivo | O que você tira dele |
|---|---|---|
| 1 | [`ESTADO.md`](ESTADO.md) | onde o trabalho parou, o que falta, o comando para retomar |
| 2 | [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) | os cinco vereditos, a árvore de decisão, a hierarquia de fontes, as armadilhas |
| 3 | [`README.md`](README.md) | o mapa do repositório |
| 4 | [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) | só quando a pergunta for "por que assim e não do outro jeito" |

---

## 3. 🔴 As rules, que você precisa ler à mão

Todas em `.cursor/rules/`. No Cursor elas são `alwaysApply: true`; aqui **você tem que abrir**.

| Rule | Quando é obrigatória |
|---|---|
| [`checagem-fundamentos.mdc`](.cursor/rules/checagem-fundamentos.mdc) | **sempre.** É a doutrina de comportamento |
| [`etica-e-risco.mdc`](.cursor/rules/etica-e-risco.mdc) | **sempre que houver decisão editorial**: escolha de recorte, redação de veredito, qualquer coisa que saia em público |
| [`escrita-de-card.mdc`](.cursor/rules/escrita-de-card.mdc) | qualquer texto que vá para a tela |
| [`organizacao-do-repo.mdc`](.cursor/rules/organizacao-do-repo.mdc) | sempre que criar, mover ou renomear arquivo |

---

## 4. As skills, e qual usar quando

Moram em [`skills/`](skills/) (fonte única) e têm um **espelho** em `.claude/skills/<nome>/SKILL.md`, que é só um ponteiro para tornar a skill invocável aqui.

🔴 **Regra de manutenção: doutrina se edita em `skills/`, nunca no ponteiro.** Skill nova exige criar os **dois** arquivos no mesmo turno.

| Ele disse | Skill |
|---|---|
| "chegou um vídeo novo", "abre um caso" | [`preparar-caso`](skills/preparar-caso.md) — PASSOS 0 a 3 |
| "o que dá para checar aqui?", "extrai as alegações" | [`extrair-alegacoes`](skills/extrair-alegacoes.md) — PASSO 4 |
| "checa isso", "busca as fontes" | [`checar-alegacao`](skills/checar-alegacao.md) — PASSO 5 |
| "monta o vídeo", "gera o relatório" | [`fechar-caso`](skills/fechar-caso.md) — PASSOS 6 a 8 |

⛔ **Não pule da transcrição direto para a checagem.** A extração roda antes, com a internet fechada, e num arquivo separado. Quem já sabe a resposta escolhe as perguntas.

---

## 5. O pipeline, comando a comando

```bash
SLUG=2026-08-27-sabatina-lula-globo
export PATH="$HOME/scoop/shims:$PATH"      # Windows com scoop

python -m checagem midia $SLUG registrar             # PASSO 1 · sha256, duração, resolução
python -m checagem midia $SLUG audio                 # PASSO 1 · WAV 16 kHz mono
python -m checagem midia $SLUG recortar <id> --inicio S --duracao S --motivo "..."
python -m checagem transcrever $SLUG                 # PASSO 2 · whisper.cpp local
python ferramentas/corrigir-transcricao.py $SLUG     # correções, com registro
python -m checagem falantes $SLUG                    # PASSO 3 · aplica falantes.json

#   PASSO 4 e 5 são JULGAMENTO, feitos pelas skills. Não há comando, e isso é de propósito.

python -m checagem overlay    $SLUG --recorte <id>   # PASSO 6 · desenha as cartelas
python -m checagem renderizar $SLUG --recorte <id>   # PASSO 7 · queima no vídeo
python -m checagem validar    $SLUG --recorte <id>   # PASSO 8 · a porta (sai 1 se achar erro)
python -m checagem relatorio  $SLUG --recorte <id>   # o documento público do caso
```

Passo a passo com o que conferir em cada etapa: [`docs/REPLICAR.md`](docs/REPLICAR.md).

---

## 6. Convenções que quebram trabalho se ignoradas

- **`python -m checagem validar` é a porta.** ⛔ Nada é dado por pronto com ele reprovando. Ele **sai com código 1**.
- **Mídia não entra no git**; o manifesto com `sha256` entra. O repositório guarda o que foi dito e a checagem, não o arquivo.
- **Tempo é sempre absoluto na peça inteira**, mesmo dentro de um recorte. É isso que deixa checar num trecho e renderizar na peça toda.
- **Citação é literal.** O validador normaliza a transcrição e procura a frase dentro dela. Aspa parafraseada **reprova o caso**.
- **Número calculado vai em `derivacoes`**, com as parcelas e a conta. ⛔ Não é atalho para número que você não achou: isso é `INSUSTENTAVEL`.
- **Duas entradas com a mesma URL são uma fonte só.** Junte no mesmo `trecho`.
- **Correção de transcrição entra por script**, com antes, depois e como foi conferida. ⛔ Nunca em silêncio.
- **Mudou estado, atualize [`ESTADO.md`](ESTADO.md)** no mesmo turno. Uma sessão nova tem que conseguir continuar lendo só ele.
- **Veredito publicado não se edita em silêncio.** Vai para `casos/<slug>/CORRECOES.md`, com data, o que estava escrito e o que passou a valer.
- ⛔ **Travessão em nome de arquivo, nunca.** Hífen simples.
- ⛔ **Commit e push só com confirmação explícita dele**, mesmo que o prompt diga "commit ao final".

---

## 7. O que este repositório NÃO faz

⛔ Não apura (não entrevista ninguém, não obtém documento inédito) · ⛔ não mede intenção, caráter ou desempenho de governo · ⛔ não recomenda voto · ⛔ não conclui "mentiu N vezes" sobre ninguém, nem no relatório nem em peça de divulgação · ⛔ não substitui as agências de checagem profissionais: usa-as como fonte e aponta para elas.

Ver [`docs/METODOLOGIA.md` §8](docs/METODOLOGIA.md).
