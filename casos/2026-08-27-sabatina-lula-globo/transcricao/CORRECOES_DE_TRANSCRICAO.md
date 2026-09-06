# Correções de transcrição

**Caso:** `2026-08-27-sabatina-lula-globo`
**Atualizado em:** 2026-09-05

A transcrição é gerada por `whisper.cpp` e **erra**, principalmente em nome próprio, número falado e palavra de contexto técnico. Corrigir é obrigatório; corrigir em silêncio, não. Toda alteração está abaixo, com o que estava, o que passou a valer e como foi conferida.

⛔ Nada aqui muda o **sentido** de uma fala. Se uma correção mudasse o sentido, ela não seria correção: seria edição, e o caso teria que ser refeito.

| Tempo | Estava | Passou a ser | Como foi conferida |
|---|---|---|---|
| `00:24:03` | Quando eu votei à presidência da República. | **Quando eu voltei à presidência da República.** | 2ª e 3ª passadas, janela 24:36 a 24:52, concordam em 'voltei' |
| `00:24:10` | Você se esquece que eu deixei esse país crescendo 7,5% e quando eu votei ele estava | **Você se esquece que eu deixei esse país crescendo 7,5% e quando eu voltei ele estava** | 2ª passada no recorte inteiro, com prompt de contexto |
| `00:25:26` | Superar o primário de 0,1%. | **Superávit primário de 0,1%.** | 3ª passada em janela isolada de 11s (25:19 a 25:30), que devolveu 'Superávit primário de 0,1%' com clareza |
| `00:26:03` | Deixou um roubo de 94 bilhões, sabe, de dívida com as pessoas que nós tivemos que pagar. | **Deixou um rombo de 94 bilhões, sabe, de dívida com as pessoas que nós tivemos que pagar.** | 2ª passada no recorte inteiro devolveu 'o rombo deixado pelo outro governo' no segmento anterior e 'rombo' aqui |
| `00:26:59` | Se você consumir com responsabilidade, você vai poder pagar sua dívida e o PEC vai voltar | **Se você consumir com responsabilidade, você vai poder pagar sua dívida e o país vai voltar** | 2ª e 3ª passadas, janela 26:58 a 27:10, concordam em 'o país vai voltar a crescer' |

**Total:** 5 correções.
