# Correções da revisão r6 (lotes 12 e 13)

Revisão adversarial por IA, em passada separada, das checagens A144 a A169. Cada entrada abaixo é uma mudança aplicada no arquivo do lote. A busca web estava esgotada nesta rodada; a revisão usou as capturas do caso e três capturas novas, de fonte oficial por URL direta, em `capturas/2026-10-15-sabatina-lula-globo-2turno-rev` (pedido em `checagens/pedidos-captura/pedido-rev-r6.json`): a posição do Brasil no FMI em 30/11/2003, o relatório da FAO de 2014 (The State of Food Insecurity in the World 2014) e a série do Banco Mundial de renováveis no consumo final de energia, todos os países, 2020.

## A154 (lote 12): veredito

- **Estava:** `VERDADEIRO`, ressalva "A alta apurada até agosto de 2026 foi de 11,19 pontos; até junho, era de 10,2". A explicação tratava o desvio como "cerca de 10%, no limite da régua".
- **Passou a valer:** `IMPRECISO`. Ressalva "A diferença é para menos: a alta apurada é maior que a dita; até junho, era de 10,2 pontos". Explicação reescrita com o desvio medido (10,6%) e derivação nova (`82.87 menos 71.68 menos 10, dividido por 82.87 menos 71.68`).
- **Por quê:** os 10 pontos ditos pela entrevistadora ficam 1,19 abaixo da alta apurada de 11,19, desvio de 10,6% sobre o valor apurado, que é a base da conta do §2.2 (o exemplo "94 contra 92,4"). A régua diz "desvio ≥ 10% no valor: IMPRECISO" e não distingue o sentido: foi o critério aplicado ao "um trilhão de reais" de Flávio Bolsonaro em 28/ago (A007 daquele caso, 14% para menos, `IMPRECISO` depois de revisão) e, neste caso, ao "dobro da inflação" da mesma entrevistadora (A166) e às posições de ranking do candidato (A144, A151). Manter `VERDADEIRO` a 10,6% seria régua mais frouxa para um dos lados da mesa.

## A156 (lote 12): veredito

- **Estava:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "As fontes capturadas citam Lurian e Marcos Cláudio como filhos de Lula, mas nenhuma diz quantos filhos ele tem". A explicação dizia que a biografia oficial da Presidência "conta a família de origem dele [...] mas não fala dos filhos".
- **Passou a valer:** `VERDADEIRO`, confiança média, resumo "A biografia oficial da Presidência diz que Lula tem cinco filhos, quatro deles com Marisa Letícia". O trecho da fonte N1 passou a ser a frase da própria biografia: "Marisa Letícia Lula da Silva, mãe de quatro dos seus cinco filhos". `numero_apurado` e `data_de_referencia` reescritos; as duas reportagens do Poder360 ficam como apoio.
- **Por quê:** a frase com o total está na página já capturada (`capturas/...-p12/texto/06c2b86c5a3b.txt`, a mesma URL que a checagem citava). A leitura de que a biografia não falava dos filhos estava errada. Confiança média porque só a fonte oficial dá a soma; as reportagens confirmam filhos nomeados.

## A153 (lote 12): veredito

- **Estava:** `VERDADEIRO`, confiança média, resumo "Fraga, Malan e Bacha, que votaram em Lula, escreveram que os pobres sofrem mais se o governo perde crédito fiscal".
- **Passou a valer:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "A crítica de Fraga, Malan e Bacha, que votaram em Lula, só aparece no Poder360; a carta original não foi capturada". Explicação no padrão de veredito provisório. Ressalva mantida.
- **Por quê:** as quatro fontes são N4 do mesmo veículo, e a carta (publicada na Folha de S.Paulo), que é a primária, não foi capturada. A METODOLOGIA §3.1, regra 2, só aceita N3/N4 quando citam a primária e ela foi conferida. Neste caso a mesma falta levou a `INSUSTENTAVEL` provisório falas do candidato (A016) e outro número da entrevistadora (A126, na revisão r5); manter `VERDADEIRO` aqui seria régua diferente. Nada contradiz a pergunta, por isso não é `FALSO`. Para virar `VERDADEIRO` falta capturar a carta e uma segunda redação.

## A145 (lote 12): resumo, fonte e explicação

- **Estava:** resumo "Na posse, o Brasil devia ao FMI 15,3 bilhões de DES; a dívida só passou de US$ 30 bi em 2003, com pico de US$ 33,7 bi". O saldo de 2003 só tinha a reportagem de 2005 como fonte.
- **Passou a valer:** resumo "Na posse, o Brasil devia ao FMI cerca de US$ 20 bi; a dívida só passou de US$ 30 bi em 2003, com pico de US$ 33,7 bi" (o valor em dólar já era derivação declarada). Fonte nova N2: posição do Brasil no FMI em 30/11/2003 (saldo de 23.358,59 milhões de DES; 17.199,64 milhões sacados do acordo de 2002). A explicação cita essa posição.
- **Por quê:** lido em cinco segundos, o card punha "15,3 bilhões de DES" ao lado de "30 bilhões de dólares", e quem não sabe o que é DES compara os dois números e vê a fala com o dobro do valor; em dólar o saldo da posse é cerca de US$ 20 bilhões. O veredito não muda.

## A149 (lote 12): fonte, explicação e derivação

- **Estava:** o pico de US$ 33,7 bilhões vinha só da reportagem de 2005 (N4), e a explicação dizia que os 30 bilhões ficam entre o pago em 2005 e o pico.
- **Passou a valer:** fonte nova N2 (posição do Brasil no FMI em 30/11/2003, 23.358,59 milhões de DES) e derivação "cerca de US$ 30,7 bilhões" (`23,358.59 vezes 30 dividido por 22,821.12`, pela equivalência da carta de intenção de 2002). A explicação diz que o acordo de 2002 estava em grande parte sacado (17.199,64 de 22.821,12 milhões de DES).
- **Por quê:** o melhor argumento contra o `VERDADEIRO` é que o pico de US$ 33,7 bilhões fica 11% acima dos 30 ditos. A fonte primária mostra que, pela mesma equivalência que a fala e o acordo usavam, o saldo no pico era de cerca de US$ 30,7 bilhões, e que a dívida quitada era em grande parte o próprio acordo de 30 bilhões. O veredito fica de pé, agora com a primária.

## A148 (lote 12): explicação

- **Estava:** "estoque final (US$ 288,6 bilhões, 6% acima) e o acréscimo do período (US$ 250,8 bilhões, 7% abaixo)".
- **Passou a valer:** "do qual o dito fica 6,4% abaixo" e "do qual o dito fica 7,7% acima", medidos sobre o valor apurado.
- **Por quê:** os dois desvios estavam calculados com bases diferentes (um sobre o apurado, outro sobre o dito). Medidos como manda o §2.2, ficam em 6,4% e 7,7%, ainda abaixo de 10%. O veredito não muda.

## A158 (lote 13): resumo

- **Estava:** "Os verbetes do CPDOC registram divergência entre Mantega e Meirelles, não brigas de Lula com os dois".
- **Passou a valer:** "Nenhuma fonte achada registra brigas de Lula com Mantega e Meirelles; o CPDOC registra divergência entre os dois".
- **Por quê:** lido sozinho, "não brigas de Lula com os dois" soa como se a fonte dissesse que as brigas não aconteceram. O verbete biográfico só não as registra. O card de `INSUSTENTAVEL` tem que dizer o que faltou, não sugerir desmentido.

## A159 (lote 13): fontes e explicação

- **Estava:** só três reportagens (N4), sem a fonte primária, e a explicação dizia que "as fontes capturadas não dizem quem governava em 2014, então a atribuição pessoal ('eu tinha acabado') não foi conferida".
- **Passou a valer:** duas fontes novas. N2: o relatório da FAO de 2014, capturado na revisão, que registra a queda da subalimentação no Brasil de 10,7% em 2000-02 para abaixo de 5% em 2004-06, com o Fome Zero lançado em 2003. N1: a biografia oficial da Presidência (já capturada), que registra Dilma Rousseff no cargo desde 2011 e reeleita em 2014. A explicação diz que em 2014 governava Dilma, mas que a queda que levou o país abaixo do limite aconteceu no primeiro mandato de Lula.
- **Por quê:** o melhor argumento contra o veredito era a régua do §2.2 para "atribui a um governo o que aconteceu em outro", porque em 2014 Lula não era presidente. A fonte primária derruba esse argumento: a queda medida pela FAO é de 2000-02 a 2004-06. E, pela regra 2 da §3.1, três reportagens sem a primária conferida não bastavam. O veredito fica.

## A161 (lote 13): resumo, fonte e explicação

- **Estava:** resumo "O plano de Flávio não muda a regra do mínimo, e não se achou anúncio dele de reajuste só pela inflação"; o trecho do Imirante começava por "O plano de governo não apresenta mudanças no cálculo dos benefícios previdenciários ou do salário mínimo."
- **Passou a valer:** resumo "Não se achou anúncio de Flávio de reajuste do mínimo só pela inflação; o plano dele não fixa meta para o piso". O trecho do Imirante passou a ser a parte da reportagem sobre Flávio (o cabeçalho da seção e a pergunta da Globo sobre a vinculação, que ficou sem resposta). Explicação corrigida.
- **Por quê:** na página capturada, a frase "O plano de governo não apresenta mudanças no cálculo [...] do salário mínimo" é a última da seção sobre o plano de **Lula**, logo antes do cabeçalho "Flávio Bolsonaro". Ela foi atribuída ao plano errado. O que as fontes dizem do plano de Flávio é que não fixa meta para o piso (NSC Total). O veredito `INSUSTENTAVEL` provisório não muda.

## A167 (lote 13): ressalva, fonte, explicação e derivação

- **Estava:** ressalva "Acima de 80 kWh o desconto passou a zero; antes havia 40% de 31 a 100 kWh"; o trecho da Lei 12.212 trazia só as duas primeiras faixas.
- **Passou a valer:** ressalva "Em kWh gratuitos, o desconto máximo passou de 59,5 para 80, e acima de 80 kWh não há mais desconto". O trecho da Lei 12.212 inclui a terceira faixa (10% de 101 a 220 kWh), e a derivação nova declara a conta (`30 vezes 65% mais (100 menos 30) vezes 40% mais (220 menos 100) vezes 10%`). A explicação diz que o desconto total cresceu em qualquer faixa de consumo.
- **Por quê:** a ressalva antiga, lida sozinha, sugeria perda para quem consome mais de 80 kWh. Somadas as faixas antigas, o desconto máximo equivalia a 59,5 kWh gratuitos, contra 80 na regra nova, então ninguém na Tarifa Social perdeu desconto total. O veredito não muda.

## A168 (lote 13): fonte e explicação

- **Estava:** a terceira fonte era o trecho da Lei 15.235 sobre o desconto de 100% até 80 kWh de **famílias indígenas e quilombolas** custeado pela CDE, e a explicação dizia "A lei custeia pela CDE o desconto de 100% até 80 kWh", como se fosse o desconto geral.
- **Passou a valer:** a terceira fonte passou a ser o art. 11-A que a Lei 15.235 acrescentou à Lei 12.111: o rateio do custo de Angra 1 e Angra 2 entre os consumidores, exceto a Subclasse Residencial Baixa Renda. A explicação diz que a lei manteve o rateio da MP 1.300 e que quem custeia o desconto geral não foi conferido.
- **Por quê:** o trecho antigo não provava o que a coluna `prova` dizia (pergunta 3 do roteiro). E o resumo diz "a lei passa custos a quem está fora da baixa renda", o que só a MP sustentava; conferido na lei de conversão, o rateio continua. O veredito não muda.
