# Nota de atribuição de falante

**Caso:** `2026-08-27-sabatina-lula-globo` · **Escrito em:** 05/set/2026

Este documento existe porque atribuir uma frase à pessoa errada é o pior erro possível neste projeto — pior do que errar um veredito, porque coloca na boca de alguém algo que a pessoa não disse. Então a atribuição não é só aplicada: ela é **justificada, uma decisão de cada vez**, e o que não pôde ser provado está marcado como tal.

O arquivo aplicado é [`falantes.json`](falantes.json), com **110 turnos** cobrindo os 2.655 segundos da peça. Ele é escrito à mão e aplicado por `python -m checagem falantes`.

---

## 1. Quem está na peça

| Pessoa | Papel | Tempo de fala | Participação |
|---|---|---|---|
| Lula | entrevistado | 00:29:54 | 68,4% |
| César Tralli | entrevistador | 00:06:53 | 15,8% |
| Renata Vasconcellos | entrevistadora | 00:06:04 | 13,9% |
| Narração (VT) | narração | 00:00:52 | 2,0% |

✅ **Os 68,4% do entrevistado caem dentro da faixa esperada** para uma sabatina (55% a 75%), e os dois entrevistadores ficam praticamente empatados, o que é o desenho anunciado no ar. Números muito fora disso quase sempre indicam turno mal escrito, e é por isso que o script os imprime.

---

## 2. Como cada bloco foi decidido

Duas evidências foram usadas, nesta ordem de força:

**(a) A pessoa é chamada pelo nome na resposta.** É a evidência mais forte, porque vem do próprio áudio da peça. Ex.: em 15:25 Lula responde *"Renata, nem os contratos foram suspensos pelo Lupi"*, o que identifica quem fez a pergunta de 14:52.

**(b) Um quadro do vídeo no meio do bloco de pergunta.** Sampleado de 5 a 8 segundos **depois** do início do turno, porque o diretor costuma segurar o entrevistado na tela durante a primeira frase da pergunta.

| Bloco | Início | Atribuído a | Evidência |
|---|---|---|---|
| Abertura e critério de convite | 00:00 | César Tralli | quadro em 00:08, 00:20 e 00:45, plano fechado |
| Retrospectiva da trajetória | 00:57 | Narração (VT) | quadros em 01:00 e 01:30 são imagens de arquivo, não o estúdio |
| Cumprimento e inquéritos da PF | 01:53 | César Tralli | quadro em 02:03, plano fechado |
| Mensagens da lobista | 04:17 | César Tralli | quadro em 04:17, plano fechado |
| Reunião no Ministério da Saúde | 06:05 | César Tralli | quadro em 06:11, parcial |
| Cargo oferecido à lobista | 07:47 | Renata Vasconcellos | quadro em 07:53, plano fechado |
| Chefe de gabinete | 08:52 | Renata Vasconcellos | quadro em 08:58, plano fechado |
| Despesas pagas ao chefe de gabinete | 10:44 | Renata Vasconcellos | quadro em 10:50, plano fechado |
| Escândalo do INSS | 13:11 | Renata Vasconcellos | quadro em 14:58 + *"Renata, nem os contratos"* em 15:25 |
| Palanque com o ex-ministro | 16:33 | Renata Vasconcellos | *"vamos aguardar, Renata"* em 17:24 |
| Retratação editorial e Previdência | 18:38 | César Tralli | quadro em 18:56, plano fechado |
| Fila do INSS | 18:56 | César Tralli | quadro em 18:56 + *"você não pode deixar de dizer, Tralli"* em 19:44 |
| Banco Master e Jacques Wagner | 20:26 | Renata Vasconcellos | *"se um dia, Renata, você for acusada"* em 21:42 |
| **Contas públicas e dívida** | **22:32** | **Renata Vasconcellos** | *"E, Renata, eu pensei…"* em 23:18 e *"deixa eu falar uma coisa, Renata"* em 26:14 |
| Ministro da Fazenda e gastos | 27:24 | César Tralli | quadro em 27:30 + *"sabe o que acontece, Sr. Tralli?"* em 30:22 |
| Estatais e Correios | 31:09 | César Tralli | quadro em 31:40, plano fechado |
| Volta do intervalo | 33:06 | César Tralli | quadro em 33:06 |
| Educação | 33:14 | Renata Vasconcellos | quadro em 33:20 + *"deixa eu te dizer uma coisa, Renata"* em 33:50 |
| Formação de professores | 36:04 | Renata Vasconcellos | *"Renata, quem criou a Olimpíada…"* em 36:37 |
| Segurança pública | 37:22 | César Tralli | quadro em 37:35 |
| Bahia | 39:11 | César Tralli | quadro em 39:17 |
| Encerramento | 42:28 | César Tralli | quadro em 42:34 |

🔑 **O bloco que gerou o recorte checado (22:32) tem a evidência mais forte da peça**: o entrevistado chama a entrevistadora pelo nome **duas vezes** dentro da própria resposta.

---

## 3. O que NÃO foi possível provar

⬜ **A voz da retrospectiva (00:57 a 01:51).** É uma narração em off sobre imagens de arquivo. Não há quadro do estúdio nesse intervalo e ninguém é chamado pelo nome. Ela está declarada em `CASO.json` como **"Narração (VT)"**, com papel `narracao`, e ⛔ **não foi atribuída a nenhuma das duas pessoas da bancada**. O repositório não atribui o que não consegue provar.

⚠️ **Nenhuma alegação foi extraída desse trecho**, então a indefinição não afeta veredito nenhum.

---

## 4. 🧪 O método que foi tentado e reprovado

A hipótese era separar os dois entrevistadores pela **frequência fundamental da voz** — um homem e uma mulher deveriam cair em faixas distintas. A ferramenta [`ferramentas/medir-tom.py`](../../../ferramentas/medir-tom.py) foi escrita para isso e rodada sobre os 709 segmentos.

**Não funcionou.** A medição devolveu mediana de 186 Hz para a peça inteira e classificou 75% dos segmentos como "voz aguda", o que é impossível numa peça em que o entrevistado, de voz grave, fala 68% do tempo. Trechos de fala reconhecidamente masculina mediram 192 a 202 Hz, e trechos femininos mediram 127 a 186 Hz: **as faixas se sobrepõem e a medida não separa nada.**

**Causa:** áudio de televisão é comprimido e filtrado. O fundamental fica atenuado, o estimador engancha num harmônico e erra a oitava. A correção de sub-harmônico foi implementada e testada, e não resolveu.

A ferramenta ficou no repositório por dois motivos: o método é válido em áudio limpo, e ela **avisa quando não separa** em vez de devolver um resultado com cara de certeza. ⛔ Mas não conte com ela em áudio de TV — a decisão aqui foi feita com nome citado e quadro de vídeo, que é o que consta na tabela acima.
