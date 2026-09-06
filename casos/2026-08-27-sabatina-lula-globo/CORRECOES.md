# Correções deste caso

**Caso:** `2026-08-27-sabatina-lula-globo`

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
| 06/set/2026 | `A011` · resumo | "O IBGE registrou crescimento de 7,5% do PIB em 2010, **a maior taxa desde 1986**" | "O IBGE fechou 2010 com crescimento de 7,5% do PIB, exatamente o número citado" | O trecho "a maior taxa desde 1986" **não tinha fonte nenhuma** entre as duas citadas na checagem. Foi escrito de memória, que é justamente o que a regra 1 da metodologia proíbe. ⚠️ O validador não pegou: ele trata ano como data, não como quantidade, e por isso `1986` passou. Quem pegou foi a revisão humana. A limitação está agora documentada em `docs/METODOLOGIA.md` §3.1 e no docstring de `numeros_de()`. |
| 06/set/2026 | `A007` · fontes | Três fontes, sendo **duas com a mesma URL** do DataMapper do FMI (uma para o Brasil, outra para os demais países do G20) | Duas fontes: uma entrada única do FMI, com o trecho cobrindo Brasil e os demais membros, mais a série do Banco Central | Duas entradas do mesmo endereço são **uma** fonte, não duas (metodologia §3.1, regra 3). O validador reprovou com "a mesma URL aparece duas vezes", e estava certo. |
| 06/set/2026 | `A006` · fonte 1 | Trecho da série do Banco Central abreviado com reticências, mostrando só 2003 e 2010 | Trecho com os oito anos, de 2003 a 2010 | O `numero_apurado` citava "entre 1,94% e 3,74% do PIB", e nenhum dos dois valores aparecia no trecho abreviado. Números sem lastro no trecho citado. |
| 06/set/2026 | `A009` · fontes | Três fontes (2025, 2021 e FGV) | Seis fontes, com os releases do IBGE de 2022, 2023 e 2024 | O `numero_apurado` listava as taxas de cinco anos e só três tinham fonte. |
| 06/set/2026 | `A023` · fonte 1 | Trecho sem a data de publicação da matéria | Trecho começando por "Publicado em 20 de março de 2026 às 06h00." | O `numero_apurado` afirmava a posse em 20 de março e o trecho citado só dizia "nesta quinta-feira, 19". |

---

## Nada foi alterado em

Os **vereditos** dos 23 itens continuam como foram escritos na primeira rodada. As correções acima são de **lastro e de redação**: elas apertam a evidência de vereditos que já eram esses. Nenhuma delas mudou `VERDADEIRO` para `FALSO` nem o contrário.
