---
name: checar-sabatina-completa
description: Orquestra a checagem de uma sabatina INTEIRA (um candidato, uma ou duas jornalistas, 80 a 150 alegações) quando o autor entrega a gravação. Roda do arquivo até as métricas fechadas, o relatório da peça e os 5 a 6 cortes curtos renderizados: procedência, transcrição, rascunho de turnos por enquadramento, turnos conferidos, extração em lotes de internet fechada, sugestão de cortes antes dos vereditos, checagem em lotes, captura de fontes, revisão adversarial, validação, métricas, relatório, cortes, ESTADO e commit. Não escreve as considerações da IA (consideracoes-do-debate) e não edita o vídeo longo.
---

# checar-sabatina-completa

Dono da operação: [`docs/PECA_INTEIRA.md`](../docs/PECA_INTEIRA.md). Esta skill é a **ordem de execução**, os **prompts de cada agente** e a **lista de conferência**. As skills de julgamento continuam sendo [`extrair-alegacoes`](extrair-alegacoes.md), [`checar-alegacao`](checar-alegacao.md) e [`revisar-checagem`](revisar-checagem.md): **os agentes dos lotes seguem essas três, sem versão resumida delas**.

Frase que dispara: *"chegou a sabatina"*, *"aqui está a gravação, executa"*, *"checa a sabatina inteira"*.

## 🔴 As travas

1. ⛔ **A mesma régua para a jornalista e para o candidato.** Pergunta que afirma fato é alegação.
2. ⛔ **Extração de internet fechada, em todos os lotes**, antes de qualquer checagem. Agente de extração que pesquisou: o lote se refaz.
3. ⛔ **Os cortes são sugeridos e commitados ANTES do primeiro veredito** (`sugerir-cortes.py`, que não abre `checagens/`). O horário do commit é a prova.
4. ⛔ **Nenhuma alegação é descartada para o vídeo ficar mais bonito**: o que não vira corte continua na checagem, nas métricas e no relatório.
5. ⛔ **Corte curto**: 15 s recomendados, 30 s no máximo, 120 s somados, 60 s entre um e outro (`config.py`). Mais que isso só com o motivo dele.
6. ⛔ **"Mentiu", "mentira", ranking e placar não entram em arquivo nenhum.** Ele fala "mentira" no pedido; o repositório escreve `FALSO` e explica a diferença (`METODOLOGIA.md` §8).
7. ⛔ **Commit e push**: só com a confirmação dele no chat. O pedido de 15/out já autoriza commit e push ao fim desta execução.

## A ordem, com o tempo esperado

| # | Etapa | Quem | Comando ou prompt | Tempo |
|---|---|---|---|---|
| 0 | Procedência | a IA, com ele | copiar o arquivo para `fonte/` (⛔ nunca mover o original dele); preencher `procedencia` no `CASO.json` (de onde veio, se é íntegra, a duração esperada: a Globo anunciou 45 min); `midia registrar`; `midia audio`; `midia faixas` | 2 min |
| 1 | Transcrição + planos, em paralelo | script | `python -m checagem transcrever <slug>` em segundo plano; ao mesmo tempo `python ferramentas/rascunho-de-turnos.py planos <slug>` | 15 min |
| 2 | Conferência da transcrição | a IA | ler a transcrição inteira procurando nome próprio, número, ano e sigla trocados; correções por `corrigir-transcricao.py`, com a conferência registrada. Se houver transcrição publicada (g1, Poder360), `comparar-transcricao.py --so-relevantes` | 15 min |
| 3 | Turnos | a IA, olhando o vídeo | rotular `planos-rotulos.json` pela `folha-de-planos.jpg` (close do candidato, close da jornalista, `ambiguo` para plano aberto e contraplano); `rascunho-de-turnos.py turnos ... --vt INI-FIM --folha`; abrir a `folha-de-turnos.jpg` e o `RASCUNHO_DE_TURNOS.md`; **conferir todo turno da jornalista e o começo de cada resposta** (é onde o método erra: 71% da fala de jornalista no ensaio); escrever `falantes.json` com o `metodo`; `python -m checagem falantes <slug>`; o tempo por falante impresso tem que ser plausível | 20 min |
| 4 | Blocos | a IA | `metricas/blocos.json`: um bloco por tema perguntado (a virada é a pergunta nova da jornalista), com `id`, `titulo`, `inicio_s`, `fim_s` | 5 min |
| 5 | Lotes de extração | script | `python ferramentas/lotes-de-debate.py extracao-dividir <slug> --minutos 8` (6 lotes para 45 min) | 1 min |
| 6 | **Extração, um agente por lote, em paralelo** | agentes | prompt abaixo | 15 min |
| 7 | Junção | script | `extracao-juntar <slug>`. Se recusar, o conserto é no lote, nunca no script. Ler as `exclusoes`: a jornalista e o candidato com motivos parecidos | 5 min |
| 8 | **Sugestão de cortes, e commit** | script + a IA | `python ferramentas/sugerir-cortes.py <slug>`; ler o `SUGESTAO_DE_CORTES.md`; se vierem menos de 5, `--max 20` (até 30) ou `--min 6`; **commit** de alegações + sugestão antes da etapa 9 | 5 min |
| 9 | Lotes de checagem | script | `checagem-dividir <slug> --tamanho 10` | 1 min |
| 10 | **Checagem, um agente por pedido, em paralelo** | agentes | prompt abaixo; cada agente devolve também as URLs que usou | 40 a 60 min |
| 11 | Junção e fontes | script | `checagem-juntar`; montar `checagens/PEDIDO_CAPTURA.json` com todas as URLs; `capturar-fontes.py`; `conferir-trechos.py --recorte sabatina-completa --capturas capturas/<slug>`; trecho não encontrado volta para o agente daquela alegação | 15 min |
| 12 | **Revisão adversarial** | um agente que **não** checou | prompt abaixo; `registrar-revisao.py --recorte sabatina-completa --ia --notas revisao.json`; veredito alterado vai para `CORRECOES.md` com antes e depois | 30 min |
| 13 | Porta, métricas, relatório | script | `validar --recorte sabatina-completa` (0 erros, avisos lidos); `metricas --recorte sabatina-completa --blocos ...`; `relatorio --recorte sabatina-completa` | 5 min |
| 14 | Cortes | a IA | para cada corte da sugestão: `midia recortar` (com `--cortar-faixas` se a etapa 0 achou faixa), `derivar-recorte.py`, `overlay`, `renderizar`, `validar --recorte corte-NN`; olhar 2 quadros de cada corte (card legível, nada sobre nada, sem borda preta); anotar o congelamento final de cada um | 15 min |
| 15 | Entrega | a IA | copiar os cortes renderizados para `C:/Users/Gabriel/Videos/youtube/video-longo/video-9/cortes-checados/`; atualizar `ESTADO.md` e `CHANGELOG.md`; commit e push | 10 min |
| 16 | Considerações | a IA | skill `consideracoes-do-debate`, com o `CRITERIOS.md` do caso | 30 min |

Total esperado: **3 a 4 horas** depois de o arquivo chegar, a maior parte nos agentes de checagem.

## Prompt do agente de extração (um por lote)

```
Você extrai alegações de UM lote da sabatina <slug>. Leia, nesta ordem: skills/extrair-alegacoes.md inteira,
docs/METODOLOGIA.md §4 e o seu lote (casos/<slug>/lotes/extracao/lote-NN.txt).
INTERNET FECHADA: não pesquise nada. NENHUM veredito. Extraia só da janela do lote; as linhas marcadas (contexto)
não viram alegação. Mesma régua para a jornalista e para o candidato: a pergunta que afirma fato entra.
Frase é cópia literal da transcrição. `assunto` em kebab-case, escolhido da lista de assuntos que já existe nos
casos do repositório quando couber (economia, contas-publicas, inss, seguranca-publica, saude, educacao, justica,
politica, meio-ambiente, relacoes-exteriores...). Escreva o arquivo indicado no cabeçalho do lote, com `cobertura`
igual à janela, ids locais A001.. e `exclusoes` com motivo para o que atravessou o filtro e não virou alegação.
Não leia outros lotes.
```

## Prompt do agente de checagem (um por pedido)

```
Você checa as alegações do pedido casos/<slug>/lotes/checagem/pedido-NN.json. Leia skills/checar-alegacao.md
inteira, docs/METODOLOGIA.md §2, §3 e §5, docs/FONTES_BRASIL.md e .cursor/rules/etica-e-risco.mdc. Nenhum fato da
memória: URL consultada, trecho copiado da página, duas fontes independentes (a mesma matéria republicada é uma).
Fato em apuração é INSUSTENTAVEL ou NAO_CHECAVEL, nunca FALSO. O dado vale para a data da FALA (15/out/2026), não
para o que saiu depois. O `resumo` fala do enunciado, nunca da intenção, cabe em duas linhas, sem travessão.
Escreva o arquivo indicado no cabeçalho do pedido e, no fim da resposta, a lista das URLs que você usou.
Não veja outros pedidos.
```

## Prompt do agente de revisão

```
Você NÃO checou nenhuma destas alegações. Siga skills/revisar-checagem.md e tente DERRUBAR cada veredito de
casos/<slug>/checagens/checagens-sabatina-completa.json. Além disso, na ordem cronológica: (1) alegação da
jornalista e do candidato sobre o mesmo dado receberam o mesmo critério (arredondamento, nominal x real, data de
referência, exigência de fonte forte)? (2) a mesma afirmação repetida pelo candidato em dois momentos recebeu o
mesmo veredito? Liste cada divergência com os ids. Saída: revisao.json no formato de
ferramentas/registrar-revisao.py --ia.
```

## Antes de dar por fechado

- [ ] `procedencia` preenchida antes da transcrição; `integralidade` declarada
- [ ] `falantes.json` com `metodo` escrito e o tempo por falante plausível
- [ ] `SUGESTAO_DE_CORTES.md` commitado **antes** do commit das checagens (confira `git log`)
- [ ] `validar --recorte sabatina-completa`: 0 erros; todos os avisos lidos
- [ ] 100% das checagens com `revisao_ia`; mudanças de veredito em `CORRECOES.md`
- [ ] `metricas` rodada **depois** da revisão; os dois lados da mesa no `METRICAS_*.md`
- [ ] `RELATORIO_SABATINA_COMPLETA.md` gerado, com a seção por falante e a lista de cortes
- [ ] cada corte: `validar --recorte corte-NN` aprovado, 2 quadros olhados, congelamento anotado
- [ ] soma dos cortes ≤ 120 s; nenhum corte colado no outro
- [ ] ⛔ nenhuma frase de "mentiu", ranking por falsidade ou recomendação de voto em arquivo do repositório
- [ ] `ESTADO.md` diz onde parou e o que é decisão dele
