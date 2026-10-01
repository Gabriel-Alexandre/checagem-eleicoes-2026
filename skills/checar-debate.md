---
name: checar-debate
description: Orquestra a checagem de um debate inteiro (vários candidatos, 150 a 300 alegações) em lotes paralelos sem perder as travas do projeto. Roda do vídeo registrado até as métricas fechadas, passando por transcrição, turnos, extração em lotes de internet fechada, checagem em lotes, junção, revisão adversarial em pares, validação, métricas e derivação dos recortes que viram vídeo. Não escreve as considerações da IA (consideracoes-do-debate) e não monta o vídeo.
---

# checar-debate

Dono da operação: [`docs/DEBATES.md`](../docs/DEBATES.md). Esta skill é a **ordem de execução** e os **prompts de cada agente**. As skills de julgamento continuam sendo [`extrair-alegacoes`](extrair-alegacoes.md), [`checar-alegacao`](checar-alegacao.md) e [`revisar-checagem`](revisar-checagem.md): **os agentes dos lotes seguem essas três, sem versão resumida delas**.

## 🔴 As travas que só existem no debate

1. ⛔ **A mesma régua para os quatro candidatos e o mediador.** A pergunta de um candidato para outro afirma fato e entra.
2. ⛔ **Extração de internet fechada, em todos os lotes**, antes de qualquer lote de checagem começar. Se um agente de extração pesquisar, o lote inteiro se refaz.
3. ⛔ **Nenhum agente vê o resultado de outro lote** durante a extração ou a checagem (a revisão em pares é depois, por outro agente).
4. ⛔ **Nenhuma alegação é descartada para o vídeo ficar mais bonito**; o que não vira vídeo continua na checagem e nas métricas.
5. ⛔ **Recorte de vídeo se escolhe pelo critério declarado antes dos vereditos** (`docs/DEBATES.md` §5).

## A ordem

| # | Etapa | Quem | Comando ou prompt |
|---|---|---|---|
| 0 | Procedência e mídia | a IA | `preparar-caso` PASSOS 0 e 1: preencher `procedencia` do CASO.json; `midia registrar`; `midia audio` |
| 1 | Transcrição | a IA | `python -m checagem transcrever <slug>`; segunda passada nos trechos com nome, número ou ano; correções por script |
| 2 | Turnos | a IA, conferindo o vídeo | `transcricao/falantes.json` (ver `docs/DEBATES.md` §3); `python -m checagem falantes <slug>`. Confira o tempo de fala por falante que o comando imprime: um candidato com 0% é turno errado |
| 3 | Lotes de extração | script | `python ferramentas/lotes-de-debate.py extracao-dividir <slug> --minutos 8` |
| 4 | **Extração, N agentes em paralelo** | um agente por lote | prompt abaixo |
| 5 | Junção | script | `extracao-juntar`. Se recusar, o conserto é no lote, nunca no script |
| 6 | Seleção de cortes (critério declarado) | a IA, com o autor | `recortes/SELECAO_DE_CORTES.md`, **antes** da etapa 7 |
| 7 | Lotes de checagem | script | `checagem-dividir --tamanho 10` |
| 8 | **Checagem, N agentes em paralelo** | um agente por pedido | prompt abaixo |
| 9 | Junção e fontes | script | `checagem-juntar`; `capturar-fontes.py`; `conferir-trechos.py` |
| 10 | **Revisão adversarial em pares** | um agente que **não** checou | `revisar-checagem`, mais a pergunta de pares (`docs/DEBATES.md` §4.1); `registrar-revisao.py --ia` |
| 11 | Porta e métricas | script | `validar --recorte debate-completo`; `metricas --recorte debate-completo` |
| 12 | Derivar e renderizar os cortes | a IA | `midia recortar`, `derivar-recorte.py`, `overlay`, `renderizar`, `validar --recorte corte-NN`, conferência com o olho (`fechar-caso`) |
| 13 | Considerações | a IA | skill `consideracoes-do-debate` |

## Prompt do agente de extração (um por lote)

```
Você extrai alegações de UM lote de um debate presidencial. Leia, nesta ordem: skills/extrair-alegacoes.md inteira,
docs/METODOLOGIA.md §4 e o seu lote (casos/<slug>/lotes/extracao/lote-NN.txt).
INTERNET FECHADA: não pesquise nada. NENHUM veredito. Extraia só da janela do lote; as linhas marcadas (contexto)
não viram alegação. Mesma régua para todos os falantes, incluindo a pergunta que um candidato faz a outro.
Frase é cópia literal. Escreva o arquivo indicado no cabeçalho do lote, com `cobertura` igual à janela, ids locais
A001.. e `exclusoes` com motivo para o que atravessou o filtro e não virou alegação. Não leia outros lotes.
```

## Prompt do agente de checagem (um por pedido)

```
Você checa as alegações do pedido casos/<slug>/lotes/checagem/pedido-NN.json. Leia skills/checar-alegacao.md
inteira, docs/METODOLOGIA.md §2, §3 e §5, e .cursor/rules/etica-e-risco.mdc. Nenhum fato da memória: URL consultada,
trecho copiado, duas fontes independentes (a mesma matéria republicada é uma). Fato em apuração é INSUSTENTAVEL ou
NAO_CHECAVEL, nunca FALSO. Dado vale para a data da FALA. O `resumo` fala do enunciado, nunca da intenção, sem
travessão. Escreva o arquivo indicado no cabeçalho do pedido. Não veja outros pedidos.
```

## Prompt do agente de revisão

```
Você NÃO checou nenhuma destas alegações. Siga skills/revisar-checagem.md e tente DERRUBAR cada veredito. Além disso, na
ordem cronológica, procure PARES de alegações do mesmo tipo e assunto, de falantes diferentes, e confirme que o mesmo
critério foi aplicado (arredondamento, nominal × real, data de referência, exigência de fonte forte). Liste cada
divergência com os dois ids. Saída: revisao.json no formato de ferramentas/registrar-revisao.py --ia.
```

## Antes de dar por fechado

- [ ] `validar --recorte debate-completo`: 0 erros; todos os avisos lidos
- [ ] 100% das checagens com `revisao_ia`; mudanças de veredito em `CORRECOES.md`, com antes e depois
- [ ] `metricas` rodada **depois** da revisão (as métricas anteriores à revisão não valem)
- [ ] a lista de `exclusoes` lida: nenhum candidato com muito mais exclusões que os outros sem motivo
- [ ] a pergunta de pares respondida e registrada
- [ ] `SELECAO_DE_CORTES.md` anterior ao primeiro veredito (confira o histórico do git)
- [ ] ⛔ nenhuma frase de "mentiu", de ranking por falsidade ou de recomendação de voto em arquivo do repositório
