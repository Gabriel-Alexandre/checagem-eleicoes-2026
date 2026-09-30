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
| 30/set/2026 | **peça checada (troca de mídia)** | clipe vertical do g1 no Facebook, 540x960, 5min43s, sha256 `ae35ff24…`, com faixas desfocadas nas laterais | íntegra horizontal da sabatina, 1920x886 com faixas pretas, 44min18s, sha256 `a7006047…`, com o bloco recortado (34:02 a 39:40) e as faixas cortadas | Pedido do autor: usar a íntegra como referência, cortar as faixas pretas e recortar só o bloco checado. O clipe do g1 tinha sido o único arquivo obtido sem contornar trava de acesso; agora o autor forneceu a íntegra. Ver `CASO.json`, `procedencia`. |
| 30/set/2026 | **relógio de todos os tempos** | tempos do clipe (0:00 a 5:38) | tempos da sabatina inteira (34:02 a 39:40): deslocamento de **+2042,36 s**, medido pelo fim de 58 segmentos de texto idêntico, com desvio máximo de 0,08 s | Alegações, turnos de falante e correções de transcrição foram levados por `ferramentas/migrar-tempos.py`. O texto de cada alegação, o resumo, o veredito e as fontes **não mudaram**: 20 das 21 citações continuam literais. O card mostra agora o minuto da sabatina inteira (por exemplo, 34:56 no lugar de 00:54). |
| 30/set/2026 | `A018`, só a citação | "que evitariam que os aposentados do INSS tenham sido roubados como foram roubados nesse atual governo." | "que evitariam que os aposentados do INSS [...] como foram roubados nesse atual governo." | A transcrição da mídia nova e as passadas de conferência escrevem quatro formas diferentes do verbo ('tenham', 'tiverem', 'tinham', 'tivessem' no Poder360), e o áudio não decide entre elas. A citação sai só do que é certo, com `[...]`. O veredito `VERDADEIRO` e o resumo não mudaram. |
| 30/set/2026 | transcrição do bloco (8 correções) | 5 correções sobre a transcrição do clipe (`Otrali`, `a maior juro`, três `Tralho`/`Tralha`) | 8 correções sobre a transcrição nova, ver [`transcricao/CORRECOES_DE_TRANSCRICAO.md`](transcricao/CORRECOES_DE_TRANSCRICAO.md): 4 nomes de entrevistador, `pra lua` por `para a lua`, **`1922` por `2022`** e duas do fim do bloco, onde o motor puxou uma frase da pergunta seguinte ('Então, quero ouvir o senhor, candidato'), que faria um entrevistador falar dentro do último turno de Flávio | Com o áudio de outra codificação o motor errou onde antes acertava (o ano) e acertou onde antes errava (`a maior juro`). Cada correção está com as passadas e a referência que a sustentam, e a que fica sem conferência no áudio (`2022`) está marcada. |
| 30/set/2026 | limite de turno em 35:32 | Tralli falava a partir de 35:31,8, depois de "500 bilhões de reais" | Tralli fala a partir de 35:32,5, o começo da pergunta dele | A transcrição nova traz "Meio trilhão de reais..." (0,6 s) nesse vão; o quadro é o close em Flávio até 35:33. Ver `NOTA_DE_ATRIBUICAO.md` §3. |
| 30/set/2026 | vídeo (cards e enquadramento) | cards a 94% de opacidade, corte seco, canto esquerdo do card com uma quina reta, imagem vertical sobre fundo desfocado | cards opacos (nada do vídeo por baixo do texto), entrada com fade de 8 quadros, canto arredondado, imagem horizontal sem faixas pretas | Padrões do editor de vídeos longos de 29/set (V31, V33, V35) propagados ao pipeline. Nenhum veredito mudou por isso. |
| 30/set/2026 | conferência de atualidade dos dados | (dados consultados até 27/set) | **nenhum veredito muda.** Ver a seção abaixo | Pedido do autor: reconferir o que pudesse ter saído depois da checagem. |

---

## Revisão

As 21 checagens passaram pela revisão adversarial por IA ([`skills/revisar-checagem.md`](../../skills/revisar-checagem.md)), uma passada separada que tenta derrubar cada veredito com a régua da METODOLOGIA. A nota de cada uma está no campo `revisao_ia` de [`checagens/checagens-bloco-economia.json`](checagens/checagens-bloco-economia.json) e no relatório. Resultado: 16 mantidas, 5 alteradas (as linhas acima).

Pontos que continuam em aberto, e que a revisão deixou escritos na explicação de cada card:

- `A005`: o relatório da MoneYou e duas reportagens do mesmo dia divergem sobre a posição do Brasil; vale o documento de origem.
- `A010`: "perdendo o poder de compra" admite duas leituras (12 meses ou dentro do ano); o veredito cobre as duas.
- `A011` e `A014`: sem comprovação porque não há registro oficial conferível.

---

## Conferência de atualidade dos dados (30/set/2026)

Os vereditos são sobre o que foi dito em 28/ago, com o dado que existia então. Três dias depois da checagem, foi conferido o que saiu de novo nas séries que mudam, para o vídeo não afirmar como atual o que já não é. **Nenhum veredito muda.**

| Alegação | Dado no card | O que saiu depois | Efeito |
|---|---|---|---|
| `A002` dívida bruta | 81,95% do PIB em jun/2026 | julho de 2026: **82,56%** (SGS 13762, nota do BC de 31/08: 82,5%). A trajetória de alta se confirma | nenhum: "último dado antes da entrevista" segue certo |
| `A004` Selic em 14% | 14% desde o Copom de 5/ago | o Copom de 16/set cortou para **13,75%**, em vigor desde 17/09 (SGS 432) | nenhum: a fala era do dia 28/ago e o card diz "desde o corte de 5 de agosto" |
| `A005` maior juro real | 9,30% em 05/ago, 1º lugar, Rússia em 2º | o levantamento MoneYou/Lev de 16/set dá **8,45%** com a Selic a 13,75%, ainda em 1º, Rússia em 2º com 6,79% | nenhum: a posição confere e a ressalva (14% é a nominal) segue |
| `A007` juros de "um trilhão" | R$ 1,16 tri em 12 meses até junho | até julho, R$ 1.150,5 bi (8,67% do PIB), nota de 31/08, **já citada na explicação** | nenhum: o desvio vai de 14% para 13%, acima da régua de 10% |
| `A010` salário mínimo | ganho real de 2,6% em 12 meses; perda de 3,5% desde janeiro | INPC de agosto: 12 meses até agosto dão 4,0% e o ganho real vai a **2,7%**; a perda desde janeiro fica em 3,1% | nenhum: as duas leituras do veredito seguem |
| `A011` equipe econômica | 9 nomes | a lista do Poder360 segue com 9 nomes | nenhum |
| `A003`, `A014` | 36 medidas; ~4,4 mil cargos | nenhum levantamento mais recente encontrado | nenhum |
| `A021` sensibilidade | R$ 60,6 a 66,1 bi (nota de 31/07) | a nota de 31/08 traz a tabela de elasticidades como imagem, que a extração de texto não lê; a reportagem do JB (R$ 68,9 bi) já era fonte do card | **aberto**: ninguém leu o número novo do BC. É o único item da lista que ficou sem conferência |

⛔ Estes números **não** entram no card nem no resumo: o vídeo mostra o dado da data da fala. Eles estão aqui para quem ler o relatório em outra data.

---

## Contestações recebidas

Nenhuma até 30/set/2026.
