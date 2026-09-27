# Correções deste caso

**Caso:** `2026-08-28-sabatina-flavio-globo-economia`

Toda mudança em veredito, resumo, fonte ou número **depois** de o material ter sido dado por pronto entra aqui, com data, o que estava escrito, o que passou a valer e o que motivou a mudança.

> 🔴 **Veredito não se edita em silêncio.**

Correções de **reconhecimento de fala** ficam em [`transcricao/CORRECOES_DE_TRANSCRICAO.md`](transcricao/CORRECOES_DE_TRANSCRICAO.md).

---

## Como contestar

Abra uma **issue** no repositório com a fonte que sustenta a contestação. A resposta é dada com fonte. Contestação procedente vira uma entrada nesta tabela e correção no relatório e, quando possível, no vídeo. ⛔ Nada é apagado.

---

## Registro

| Data | Item | Estava | Passou a ser | Por quê |
|---|---|---|---|---|
| 27/set/2026 | abertura do registro | (nada) | caso dado por pronto para a revisão adversarial | 21 checagens, 55 trechos conferidos contra a página capturada, validador em 0 erros. |
| 27/set/2026 | `A005`, durante a checagem | rascunho baseado em InfoMoney e BP Money: Brasil em 2º no ranking de juros reais | Brasil em 1º, pelo relatório primário da MoneYou de 05/08/2026 | O cruzamento com o documento de origem contradisse as duas reportagens do mesmo dia. Vale a primária; a divergência está no campo `divergencia_entre_fontes`. |
| 27/set/2026 | `A005`, revisão adversarial por IA | `VERDADEIRO`, com a ressalva "Os 14% são a Selic nominal; o juro real do Brasil, que é o do ranking, era 9,30%" | `IMPRECISO`: "O Brasil era o 1º em juro real (9,30%), à frente da Rússia; mas 14% é a Selic nominal, e não o juro real" | A fala diz "14% é o maior juro real do mundo". A posição no ranking confere, mas a régua do §2.2 da METODOLOGIA manda `IMPRECISO` para "nominal por real", e o erro estava só na ressalva. |
| 27/set/2026 | `A007`, revisão adversarial por IA | `VERDADEIRO`, "Os juros do setor público somaram R$ 1,16 trilhão em 12 meses até junho, dado divulgado antes da entrevista", tratado como arredondamento | `IMPRECISO`: "Os juros do setor público somaram R$ 1,16 trilhão em 12 meses até junho: a fala ficou 14% abaixo do valor" | O desvio de 14% passa da régua de 10% do §2.2, que não abre exceção para desvio contra o argumento de quem fala. É a mesma régua aplicada a `A021`. |
| 27/set/2026 | `A012`, revisão adversarial por IA | `VERDADEIRO`, "O déficit primário do governo central somou R$ 335 bi de 2023 a 2025; 'dívida primária' não existe como conceito" | `IMPRECISO`: "O valor bate com o déficit primário de 2023 a 2025 (R$ 335 bi), mas 'dívida primária' não existe: déficit não é dívida" | O card dizia que o conceito da fala não existe e, ao mesmo tempo, dava `VERDADEIRO`. Conceito errado é `IMPRECISO` pela régua do §2.2. |
| 27/set/2026 | `A017`, revisão adversarial por IA (só o resumo) | "O PT se opôs à MP 871: 253 emendas, obstrução e voto contra, com parte das emendas afrouxando controles" | "O PT se opôs à MP 871: 253 emendas, obstrução anunciada e fora do acordo que destravou a votação" | "Voto contra" não está em nenhuma fonte capturada; a CNN registra que o tema "não foi objeto de votação nominal". O veredito `VERDADEIRO` não mudou. |
| 27/set/2026 | `A020`, revisão adversarial por IA | `VERDADEIRO`, com a ressalva "Os gastos estão no orçamento, mas fora do cálculo da meta e do limite de despesas" | `IMPRECISO`: "A IFI estima R$ 147,7 bi fora dos limites fiscais de 2023 a 2026, mas esses gastos estão no orçamento, não fora dele" | A prática existe, mas "fora do orçamento" troca o conceito. Pela mesma régua aplicada a `A012`. |
| 27/set/2026 | vídeo | trecho até 05:43, com a cartela de divulgação do g1 no fim e a cartela de encerramento do projeto | trecho até 05:38, terminando com a fala | A cartela do g1 não é parte da entrevista, e o autor do projeto pediu que o vídeo termine junto com a fala. Nenhum veredito mudou por isso. |

---

## Revisão

As 21 checagens passaram pela revisão adversarial por IA ([`skills/revisar-checagem.md`](../../skills/revisar-checagem.md)), uma passada separada que tenta derrubar cada veredito com a régua da METODOLOGIA. A nota de cada uma está no campo `revisao_ia` de [`checagens/checagens-bloco-economia.json`](checagens/checagens-bloco-economia.json) e no relatório. Resultado: 16 mantidas, 5 alteradas (as linhas acima).

Pontos que continuam em aberto, e que a revisão deixou escritos na explicação de cada card:

- `A005`: o relatório da MoneYou e duas reportagens do mesmo dia divergem sobre a posição do Brasil; vale o documento de origem.
- `A010`: "perdendo o poder de compra" admite duas leituras (12 meses ou dentro do ano); o veredito cobre as duas.
- `A011` e `A014`: sem comprovação porque não há registro oficial conferível.

---

## Contestações recebidas

Nenhuma até 27/set/2026.
