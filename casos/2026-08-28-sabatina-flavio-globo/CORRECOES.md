# Correções deste caso

**Caso:** `2026-08-28-sabatina-flavio-globo`

Toda mudança em veredito, resumo, fonte ou número **depois** de o material ter sido dado por pronto entra aqui, com data, o que estava escrito, o que passou a valer e o que motivou a mudança.

> 🔴 **Veredito não se edita em silêncio.** Um veredito que muda porque a evidência mudou é o processo funcionando; um veredito que muda sem registro é o processo quebrado.

Correções de **reconhecimento de fala** ficam em outro arquivo, porque são de outra natureza: [`transcricao/CORRECOES_DE_TRANSCRICAO.md`](transcricao/CORRECOES_DE_TRANSCRICAO.md).

---

## Como contestar

Abra uma **issue** no repositório com a fonte que sustenta a contestação. A resposta é dada com fonte, não com opinião. Contestação procedente vira uma entrada nesta tabela e correção no relatório e, quando possível, no vídeo. ⛔ Nada é apagado.

---

## Registro

| Data | Item | Estava | Passou a ser | Por quê |
|---|---|---|---|---|
| 27/set/2026 | abertura do registro | (nada) | caso dado por pronto para a revisão adversarial | 19 checagens, 48 trechos conferidos contra a página capturada, validador em 0 erros e 0 avisos. Nenhuma correção posterior até esta data. |
| 27/set/2026 | `A004`, `A005` e `A006` (extração) | três juízos de valor ("atacar a democracia", "farsa", "julgado pelos inimigos") extraídos como alegações e mostrados como cards NÃO CHECÁVEL | mantidos no arquivo, com este registro de que não deveriam ter entrado | A METODOLOGIA §4.2 diz que juízo de valor **não entra** como alegação; só a parte factual dele vira alegação separada, e os fatos destas frases já estavam checados em A001 a A003, A007 e A015 a A019. O erro foi apontado pelo autor do projeto ao ver o vídeo ("muitas partes focaram em juízo de valor"). Nenhum veredito mudou. O caso principal da sabatina de Flávio Bolsonaro passou a ser o bloco de economia (`casos/2026-08-28-sabatina-flavio-globo-economia`), escolhido por tema antes da checagem; este trecho fica no repositório como registro. |
| 27/set/2026 | vídeo | trecho com a cartela de divulgação do g1 no fim e a cartela de encerramento do projeto | trecho cortado em 02:38,9, terminando com a fala | A cartela do g1 não é parte da entrevista, e o autor do projeto pediu que o vídeo termine junto com a fala. Nenhum veredito mudou por isso. |
| 18/out/2026 | `A009` | `FALSO` ("Houve armas: facas, porretes e estilingues nos processos, e armas levadas do GSI, parte recuperada pela PM") | `IMPRECISO` ("Não houve arma de fogo apreendida com manifestantes, mas os processos citam facas e porretes, e levaram armas do GSI"), ressalva sobre as duas versões oficiais das armas do GSI | Revisão adversarial pendente deste caso, feita na auditoria de coerência de 18/out do caso `2026-10-16-sabatina-flavio-globo-2turno` (`CORRECOES.md` §6 de lá), onde a mesma frase é a A123. O *"E armada?"* da própria fala aponta para arma de fogo; nessa leitura a Gazeta do Povo confirma que nenhuma foi apreendida com os manifestantes, e o que contradiz são as armas do GSI, com duas versões oficiais sobre a letalidade, o que não chega às duas fontes independentes de um `FALSO`. O absoluto segue errado pelas armas brancas dos processos: `IMPRECISO` (METODOLOGIA §2.2). Plano de overlay refeito; ⚠️ o vídeo do trecho precisa ser renderizado de novo por quem tem a mídia. |

---

## Pontos para a revisão adversarial

A revisão deste trecho é por IA ([`skills/revisar-checagem.md`](../../skills/revisar-checagem.md)), numa passada separada, e ainda não foi registrada: o caso principal passou a ser o bloco de economia. Quando for feita, deve olhar em especial:

- ~~`A009`~~ ✅ revista em 18/out (registro acima): passou a `IMPRECISO`;
- `A013` (`FALSO`, confiança média): aplicação de norma a um caso, apoiada numa decisão definitiva, com um voto divergente;
- `A017` e `A018` (`VERDADEIRO` com ressalva, confiança média): andamento atual da queixa-crime não encontrado; a frase de Dino vem de um veículo que reproduz a entrevista;
- a atribuição da pergunta a César Tralli, que diverge da transcrição do Poder360 ([`transcricao/NOTA_DE_ATRIBUICAO.md`](transcricao/NOTA_DE_ATRIBUICAO.md)).

---

## Contestações recebidas

Nenhuma até 27/set/2026.
