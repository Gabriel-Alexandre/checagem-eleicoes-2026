# Nota de atribuição de falante

**Caso:** `2026-08-28-sabatina-flavio-globo-economia` · **Escrito em:** 27/set/2026 · 🔧 **refeito em 30/set/2026**, quando a peça checada passou do clipe vertical do g1 para a íntegra horizontal (ver [`../CORRECOES.md`](../CORRECOES.md))

Atribuir uma frase à pessoa errada é o pior erro possível neste projeto. Esta nota justifica cada turno do [`falantes.json`](falantes.json).

🔑 **Os tempos abaixo são da peça inteira** (a sabatina de 44min18s), não do recorte. O bloco começa em 34:02 e termina em 39:40. Na versão de 27/set eles eram do clipe do g1 (0:00 a 5:38); para converter, some 34:02,3.

---

## 1. Quem está no trecho

| Pessoa | Papel | Tempo de fala | Participação |
|---|---|---|---|
| Flávio Bolsonaro | entrevistado | 00:04:05 | 77,0% |
| César Tralli | entrevistador | 00:00:37 | 11,7% |
| Renata Vasconcellos | entrevistadora | 00:00:36 | 11,3% |

## 2. Os turnos, e a evidência de cada um

Três evidências independentes foram cruzadas: a **imagem** (em 30/set, um quadro dentro de cada turno, tirado do recorte novo: quem fala em plano aberto ou em close), o **áudio** (a quem a resposta se dirige) e a **transcrição do Poder360**, que identifica quem perguntou. A íntegra ajuda porque mostra o plano aberto do estúdio toda vez que um entrevistador fala e o close em Flávio quando ele responde.

| Turno | Falante | Evidência |
|---|---|---|
| 34:02 a 34:32 | César Tralli | plano aberto do estúdio no começo e close no entrevistador de óculos; a resposta começa com "Ô Tralli"; o Poder360 atribui a pergunta a ele |
| 34:32 a 35:32 | Flávio Bolsonaro | close no entrevistado; cartela "FLÁVIO BOLSONARO, candidato do PL" |
| 35:32 a 35:36 | César Tralli | "Para que patamar da dívida pública..." é a réplica de Tralli no Poder360; plano aberto do estúdio |
| 35:36 a 36:14 | Flávio Bolsonaro | close no entrevistado |
| 36:14 a 36:18 | Renata Vasconcellos | plano aberto com a entrevistadora gesticulando; em seguida ela aparece em close. ⚠️ É a única frase atribuída só pela imagem e pela continuidade: o Poder360 não transcreve esta interrupção. Nenhuma alegação sai dela |
| 36:18 a 36:19 | Flávio Bolsonaro | "Sim, eu estou explicando aqui" |
| 36:19 a 36:46 | Renata Vasconcellos | close na entrevistadora; o Poder360 atribui a pergunta do salário mínimo a ela; a resposta começa com "Renata" |
| 36:46 a 37:45 | Flávio Bolsonaro | close no entrevistado |
| 37:45 a 37:51 | César Tralli | plano aberto com o entrevistador gesticulando; o Poder360 atribui a pergunta sobre aposentadorias a ele; a resposta começa com "Tralli" |
| 37:51 a 38:47 | Flávio Bolsonaro | close no entrevistado |
| 38:47 a 38:54 | Renata Vasconcellos | o Poder360 atribui a ela a pergunta sobre desautorizar o coordenador de campanha; plano aberto |
| 38:54 a 39:40 | Flávio Bolsonaro | close no entrevistado até o fim do bloco (39:40,4) |

## 3. O que esta nota não resolve

- 🔧 **O limite entre 35:31 e 35:32 mudou na troca de mídia.** A transcrição nova traz "Meio trilhão de reais..." (0,6 s) entre "500 bilhões de reais" e a pergunta de Tralli. Ela vem de duas das quatro janelas isoladas e não da segunda passada completa, que não a tem, nem da transcrição do clipe. O limite foi posto no começo da pergunta de Tralli (35:32,5), porque o quadro nesse instante é o close em Flávio, que só cai no plano aberto em 35:33. Se a frase existe, é dele. Nenhuma alegação sai dela.
- 🔧 **Uma interjeição de Renata não está na transcrição principal.** Em 37:29, no meio da resposta de Flávio, a segunda passada com prompt e o Poder360 registram "Para que patamar o senhor pretende trazê-la?" (2 s). A passada principal a engoliu dentro de "Eu vou cortar ministérios", que é de Flávio. É uma pergunta sem fato embutido, então não gera alegação, e o segmento fica atribuído a Flávio como está.
- O entrevistado chama a entrevistadora de "Renato" duas vezes (38:20 e 38:40). Todas as passadas ouvem "Renato"; ficou como está, declarado em [`correcoes.json`](correcoes.json).
- O nome do entrevistador saiu errado em quatro pontos (Trale, Tralho) e foi corrigido pela atribuição, como declarado em [`CORRECOES_DE_TRANSCRICAO.md`](CORRECOES_DE_TRANSCRICAO.md). Em duas das quatro janelas nenhuma passada escreve "Tralli": a correção se apoia no turno, não no motor.
- Os quadros de referência desta nota foram tirados do recorte e não entram no git.
