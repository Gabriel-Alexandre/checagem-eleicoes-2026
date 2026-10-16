# Correções da revisão r5 (lotes 10 e 11)

Revisão adversarial por IA, em passada separada, das checagens A118 a A143. Cada entrada abaixo é uma mudança aplicada no arquivo do lote. A busca web estava esgotada nesta rodada; a revisão usou as capturas do caso e uma captura nova, de fonte oficial por URL direta, em `capturas/2026-10-15-sabatina-lula-globo-2turno-rev` (pedido em `checagens/pedidos-captura/pedido-rev-r5.json`).

## A126 (lote 10): veredito

- **Estava:** `VERDADEIRO`, confiança média, resumo "Levantamento do FGV Ibre: 24,9% se endividaram ou usaram reservas para pagar despesas básicas em setembro de 2026".
- **Passou a valer:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "Os 24,9% do FGV Ibre vêm de uma só reportagem, do Estadão; a pesquisa original não foi capturada". Explicação reescrita no padrão de veredito provisório ("Busca interrompida pelo limite de buscas da rodada de 16/out"), ressalva e `numero_apurado` atribuindo o número ao Estadão.
- **Por quê:** é número, e a METODOLOGIA §3.1 exige fonte N1 ou N2, ou duas N3/N4 que citem a primária já conferida. As cinco páginas capturadas (Estadão, 40graus, SP Diário, Aciara, Blog do Itamar) saíram em 11/10 e quatro reproduzem o Estadão, como a própria checagem já dizia. A divulgação do FGV Ibre não foi capturada, e a tentativa da revisão na página da Sondagem do Consumidor (`portalibre.fgv.br/sondagem-do-consumidor`) teve a conexão recusada. Na mesma rodada, falas do candidato com a fonte primária faltando receberam `INSUSTENTAVEL` provisório (A016, por exemplo); manter `VERDADEIRO` aqui seria régua diferente para a jornalista. Nada contradiz o número, por isso não é `FALSO`.

## A119 (lote 10): fonte, explicação e ressalva

- **Estava:** a explicação dizia que o IPCA "não é o índice do ato e não foi usado"; ressalva "A reposição vai até agosto de 2026 e usa o INPC; a inflação de setembro em diante fica para a próxima correção."
- **Passou a valer:** fonte nova do IBGE (SIDRA, tabela 1737, IPCA número-índice, capturada na revisão), com derivações de 16,3% (7633,23 / 6563,07) e de 15,2% (alta do piso, 691 / 600). A explicação diz que pelo IPCA a inflação do período foi 16,3% e que, por essa régua, o piso fica pouco abaixo da reposição integral. Ressalva: "A reposição usa o INPC até agosto de 2026; pelo IPCA, a inflação do mesmo período foi de 16,3%."
- **Por quê:** o melhor argumento contra "vai dar tudo o que a gente não deu" é o índice. Conferido, o IPCA do período é maior que o INPC do decreto, e nenhum componente reajustado chega a 16,3%. A diferença (cerca de 1% no valor do piso) fica abaixo da régua de 10% do §2.2, então o veredito fica, mas o espectador precisa ver a ressalva.

## A122 (lote 10): resumo e fonte

- **Estava:** resumo "Governo diz que o reajuste cabe remanejando gastos; a IFI vê pressão e o MP no TCU questionou a previsão orçamentária"; os custos de R$ 5,8 bilhões e R$ 22 bilhões da explicação não estavam em trecho nenhum.
- **Passou a valer:** resumo "Governo diz que o reajuste cabe remanejando gastos; a instituição fiscal do Senado contesta e o TCU não decidiu"; o trecho do Poder360 passou a incluir a frase capturada com os dois custos.
- **Por quê:** no mesmo bloco, "MP" é medida provisória (A132 a A139), e "MP no TCU" se lê errado em cinco segundos; "IFI" é sigla de especialista (escrita-de-card §1). O card de `INSUSTENTAVEL` precisa mostrar o que ficou em aberto, e a decisão pendente do TCU faz isso. Número da explicação sem trecho fere a regra 6 da §3.1.

## A129 (lote 10): explicação

- **Estava:** "O logo depois é impreciso para a primeira fase: a alta começou cerca de sete meses depois do fim", com veredito `VERDADEIRO`.
- **Passou a valer:** a explicação diz que o tempo vai na ressalva, que na segunda fase o índice subiu durante o programa, que a série capturada ainda não mostra o mês seguinte ao fim da segunda fase, e por que a distância no tempo não rebaixa o veredito.
- **Por quê:** a palavra "impreciso" com veredito `VERDADEIRO` era contradição interna do card, e a explicação deixava de dizer que o "depois" da segunda fase ainda não é observável.

## A139 (lote 11): resumo e explicação

- **Estava:** resumo "O custo de até R$ 15 bilhões entra como despesa primária, compensada com corte em outras áreas"; explicação afirmava "o programa não amplia o teto nem fura a regra fiscal" e "a regra fiscal é cumprida".
- **Passou a valer:** resumo "O custo de até R$ 15 bilhões é despesa do orçamento, que o governo diz compensar com corte em outras áreas"; a explicação atribui a compensação ao governo, diz que ela é anunciada para o orçamento do ano que vem e ainda não está em documento capturado, e o fecho passa a "o programa não amplia o limite de despesas, mas usa o espaço dentro dele".
- **Por quê:** a compensação é plano anunciado pelo ministro, não fato registrado; o texto a dava como cumprida. É a mesma cautela aplicada ao A122, onde a palavra do governo sobre espaço fiscal não bastou.

## A135 (lote 11): resumo, explicação e número apurado

- **Estava:** "O governo estima até R$ 150 bilhões em dívidas elegíveis [...]".
- **Passou a valer:** resumo "O governo estima comprar até R$ 150 bilhões em dívidas, gastando até R$ 15 bilhões com deságio mínimo de 90%"; explicação e `numero_apurado` com as palavras da fonte ("possam ser renegociados pelas regras do programa").
- **Por quê:** as fontes dão a capacidade de compra (R$ 15 bilhões a 10% do valor de face), não o estoque de dívidas elegíveis, que nenhuma fonte capturada mede. "Elegíveis" afirmava no card o que não foi conferido.

## A125 (lote 10): resumo

- **Estava:** "A IFI projeta receita líquida R$ 127,9 bi menor que a do projeto de 2027 e déficit de R$ 86,1 bi, não superávit".
- **Passou a valer:** "A instituição fiscal do Senado projeta receita R$ 127,9 bi menor que a do projeto de 2027 e déficit de R$ 86,1 bi".
- **Por quê:** sigla de especialista sem o nome por extenso (escrita-de-card §1). O veredito não muda.

## A138 (lote 11): resumo

- **Estava:** "A PGFN pode comunicar a dívida ativa a cadastros de crédito como a Serasa, o que dificulta obter crédito".
- **Passou a valer:** "A Procuradoria da Fazenda pode comunicar a dívida ativa a cadastros como a Serasa, o que dificulta obter crédito".
- **Por quê:** sigla de especialista sem o nome por extenso. O veredito não muda.

## A118 (lote 10): fonte

- **Estava:** o trecho da Lei 14.601 trazia só R$ 142 e R$ 600, e a explicação citava também R$ 150 e R$ 50.
- **Passou a valer:** o trecho inclui os incisos III e IV, com R$ 150,00 e R$ 50,00, conferidos na mesma página capturada.
- **Por quê:** regra 6 da §3.1: número escrito precisa estar num trecho.

## A123 (lote 10): fonte

- **Estava:** a explicação citava o déficit de R$ 86,1 bilhões projetado pela IFI, sem trecho na checagem.
- **Passou a valer:** o trecho do RAF 116 inclui a frase com os R$ 86,1 bilhões, conferida no PDF capturado.
- **Por quê:** regra 6 da §3.1.

## A137 (lote 11): derivação

- **Estava:** a explicação dizia que o valor falado fica "a 1,2% do valor do documento oficial", sem a conta declarada.
- **Passou a valer:** derivação declarada, (12,86 menos 12,7) dividido por 12,86.
- **Por quê:** número derivado só entra com a conta escrita (§3.1, regra 6).
