# Correções de transcrição

**Caso:** `2026-08-28-sabatina-flavio-globo`
**Atualizado em:** 2026-09-26

A transcrição é gerada por `whisper.cpp` e **erra**, principalmente em nome próprio, número falado e palavra de contexto técnico. Corrigir é obrigatório; corrigir em silêncio, não. Toda alteração está abaixo, com o que estava, o que passou a valer e como foi conferida.

⛔ Nada aqui muda o **sentido** de uma fala. Se uma correção mudasse o sentido, ela não seria correção: seria edição, e o caso teria que ser refeito.

| Tempo | Estava | Passou a ser | Como foi conferida |
|---|---|---|---|
| `00:01:42` | Não foi encontrada uma arma no 8 de janeiro, Tralho. | **E armada? Não foi encontrada uma arma no 8 de janeiro, Tralli.** | janela 01:34 a 01:46, feixe 8. Sem prompt: 'E armada? Não foi encontrada uma arma no 8 de janeiro?' e, na janela seguinte, 'do tralho?'. Com prompt: 'E armada? Não foi encontrada uma arma no 8 de janeiro, Tralli?'. ⚠️ Só a passada com prompt escreve o nome certo, e o prompt continha o nome: a correção do nome se apoia também na atribuição (NOTA_DE_ATRIBUICAO.md), não só na concordância. |
| `00:02:06` | Ele foi imputado, esse crime é ele, é uma depredação de patrimônio público por | **Ele foi imputado esse crime a ele, é uma depredação de patrimônio público por** | janela 02:05 a 02:18, feixe 8: as duas passadas (sem e com prompt) devolvem 'Ele foi imputado esse crime a ele'; a transcrição do Poder360 tem 'E foi imputado esse crime a ele'. |
| `00:02:14` | Então, claramente, Tralho, isso tudo foi uma farsa que foi armada. | **Então, claramente, Tralli, isso tudo foi uma farsa que foi armada.** | janela 02:05 a 02:18. Com prompt: 'Então, claramente, Tralli, isso tudo foi uma farsa'. Sem prompt, o nome some ('Então, claramente, isso tudo'). Mesma ressalva da primeira correção. |

**Total:** 3 correções.
