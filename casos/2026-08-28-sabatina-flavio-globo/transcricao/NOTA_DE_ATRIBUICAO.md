# Nota de atribuição de falante

**Caso:** `2026-08-28-sabatina-flavio-globo` · **Escrito em:** 26/set/2026

Atribuir uma frase à pessoa errada é o pior erro possível neste projeto. Esta nota justifica cada decisão do [`falantes.json`](falantes.json) e registra uma divergência com a transcrição publicada por terceiro.

---

## 1. Quem está no trecho

| Pessoa | Papel | Tempo de fala | Participação |
|---|---|---|---|
| Flávio Bolsonaro | entrevistado | 00:01:29 | 56,9% |
| César Tralli | entrevistador | 00:01:07 | 43,1% |

O trecho é uma pergunta e uma resposta. Renata Vasconcellos, a outra entrevistadora da série, não fala nele. Os 56,9% do entrevistado ficam dentro da faixa esperada (55% a 75%), no limite de baixo, o que é natural num trecho de uma pergunta longa só.

## 2. As duas decisões, e a evidência de cada uma

| Turno | Atribuído a | Evidência |
|---|---|---|
| 00:00 a 01:08 | César Tralli | (a) **o entrevistado o chama pelo nome duas vezes** na resposta, em 01:42 e em 02:14 ("Tralli"; o reconhecimento de fala escreveu "Tralho", corrigido com registro); (b) os quadros de 00:00 a 01:05 mostram, em plano fechado e fazendo a pergunta, o mesmo entrevistador de óculos, e nenhuma mulher na tela |
| 01:08 ao fim | Flávio Bolsonaro | quadros de 01:10 a 02:35 em plano fechado no entrevistado; a legenda do próprio g1 no começo do vídeo diz "Flávio Bolsonaro responde sobre tentativa de golpe após eleições de 2022"; a resposta começa com "É muito importante a sua pergunta" |
| 02:40 ao fim | (sem fala) | cartela do g1: "Veja a íntegra da entrevista em g1.com.br/eleicoes" |

A virada fica em 68,4 s, onde começa o segmento 16 ("É muito importante a sua pergunta"). O segmento anterior termina a pergunta ("se o senhor for eleito").

## 3. ⚠️ Divergência com a transcrição do Poder360

A transcrição publicada pelo Poder360 ("Leia a íntegra das perguntas da Globo e as respostas de Flávio") atribui esta pergunta ("Ao julgar o caso, o STF identificou 13 atos [...]") a **Renata Vasconcellos**.

A gravação mostra outra coisa, e por duas evidências independentes entre si: a imagem (um entrevistador homem, de óculos, fazendo a pergunta inteira) e o áudio da resposta (o entrevistado se dirige a "Tralli"). O repositório segue a gravação, que é a peça checada.

⛔ A divergência não se resolve em silêncio: ela fica aqui, e a atribuição pode ser contestada por issue, como qualquer veredito.

## 4. O que esta nota não resolve

- O trecho é um recorte feito pelo g1. O que foi dito antes e depois dele não está no arquivo; a transcrição do Poder360 mostra que a conversa sobre o tema continua, com réplica do entrevistador.
- Os quadros de referência foram tirados a cada 5 s pelo runner (`quadros.tar.gz` no release em rascunho), e não entram no git.
