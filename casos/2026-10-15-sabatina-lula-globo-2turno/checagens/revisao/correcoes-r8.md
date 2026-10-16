# Correções da revisão r8 (lote 03, A027 a A039)

Revisão adversarial por IA, passada separada, em 16/out/2026. Nenhum veredito mudou nesta rodada. As mudanças são de resumo, explicação, ressalva, data de referência, derivações e fontes. Todo trecho novo ou alterado foi conferido contra o texto capturado e encontrado. Nenhuma busca web foi feita.

🆕 **Captura nova da revisão** (`capturas/2026-10-15-sabatina-lula-globo-2turno-rev`, caminho `api-post`): duas consultas POST à API pública do Comex Stat com outubro a dezembro de 2024 e de 2025 para os cinco países da fala (exportação `80fc9bb8be26`, importação `bc559f37e260`). Junto com as consultas de janeiro a setembro da rodada p03 (`14f263ecc686` e `b962fcafb544`), elas dão os 12 meses até setembro. É a mesma base do MDIC, e por isso **não** conta como a segunda fonte independente que falta em A037 a A039.

## A027 (Renata Lo Prete, clara preferência do governo americano)

- **Campos:** `resumo`, `explicacao`, trechos e prova das três fontes, título da Folha de Pernambuco
- **Estava:** resumo "Trump elogiou a votação de Flávio, mas não declarou apoio; fonte do governo dos EUA nega preferência eleitoral"; a fonte do Estadão (via Folha de Pernambuco) sem data no título e com o trecho só da parte que nega preferência
- **Passou a valer:** resumo "Trump elogiou a votação de Flávio e o recebeu na Casa Branca, mas nem ele nem o governo dos EUA declararam apoio"; a Folha de Pernambuco ganha a data de publicação (03/06/2026, lida no `datePublished` da página capturada) e o trecho passa a trazer os dois lados da mesma fonte (o entorno de Trump vê Flávio como "aliado natural", o encontro na Casa Branca, e a frase de que as reuniões não refletem preferência eleitoral); o BP Money ganha o trecho em que o governo americano "evita anunciar apoio oficial a um dos candidatos"; a AFP ganha o trecho das tarifas e sanções após a condenação de Jair Bolsonaro, que a explicação já citava sem lastro
- **Por quê:** o resumo punha na tela, como contraprova da pergunta, a fala de uma fonte anônima publicada quatro meses antes da sabatina, e cortava a parte da mesma fonte que vai na direção da jornalista (pergunta 8, e mesma régua para a mesa: o card puxava para um lado). O fato que as fontes sustentam é a ausência de apoio declarado, de Trump e do governo americano, e é ele que o resumo passa a dizer. "Tarifas e sanções" estava na explicação sem trecho (pergunta 7). O veredito `INSUSTENTAVEL` fica: há sinais nas duas direções e falta a manifestação que a frase afirma.

## A029 (Lula, nunca procurou os partidos)

- **Campos:** `resumo`, `explicacao`, trecho e prova da fonte Poder360 sobre a reunião
- **Estava:** resumo "Lula convocou senadores do MDB ao Alvorada em 14 de outubro; não há registro do que foi pedido na reunião"; explicação dizia que os senadores eram "os mesmos que declararam apoio a ele no 2º turno"
- **Passou a valer:** resumo "Lula reuniu senadores do MDB em 14 de outubro, durante a votação do fim da escala 6 X 1; não foi achado o que se tratou"; explicação diz que a reunião foi durante a votação da PEC e que, naquele momento, 10 dos 27 diretórios apoiavam Lula e 17 Flávio; o trecho passa a incluir a frase sobre o Alvorada e a votação da PEC
- **Por quê:** a reportagem não diz que os senadores convocados são os mesmos que declararam apoio a Lula (pergunta 3 e 7); diz que o encontro aconteceu durante a votação da PEC do fim da escala 6 X 1, contexto que o card omitia e que muda a leitura em cinco segundos (pergunta 8). "Não há registro" afirma uma ausência que a busca interrompida não provou; "não foi achado" é o padrão dos cards provisórios do caso (r7, A174 e A182). Veredito provisório mantido.

## A031 (Lula, as duas maiores democracias do Ocidente)

- **Campos:** `ressalva`, `explicacao`
- **Estava:** ressalva "Vale tomando Ocidente como Américas e Europa; o México, terceiro mais populoso, é parcialmente livre."; explicação apresentava a classificação do México como parte do argumento
- **Passou a valer:** ressalva "Vale tomando Ocidente como Américas e Europa e democracia como país livre pela Freedom House."; a explicação diz que o resultado não depende da classificação do México, que fica atrás do Brasil de qualquer forma
- **Por quê:** para Brasil e EUA serem as duas maiores democracias basta que os dois sejam democracias e que nenhum outro país do recorte tenha mais gente que o Brasil. O México, com 131 milhões, fica atrás do Brasil livre ou não. A ressalva dava a entender que o veredito dependia do México ser "parcialmente livre" (pergunta 8). As condições que de fato sustentam o veredito são a definição de Ocidente e a de democracia, e é isso que a ressalva passa a dizer.

## A035 (Lula, perdemos 9% com os Estados Unidos)

- **Campos:** `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas
- **Estava:** "os 9% ficam 38% acima da medida mais desfavorável dos dois recortes"; e "Num recorte de 12 meses até setembro, consultado na série mensal do Comex Stat mas não capturado nesta rodada, a queda das exportações passa de 9% e a da corrente de comércio fica abaixo"
- **Passou a valer:** "os 9% ficam 38% acima da queda das exportações e 32% acima da queda da corrente de comércio"; e "Em 12 meses até setembro [...] as exportações caem 11,4% e a corrente de comércio 7,2%; nenhum dos quatro recortes fica a menos de 10% dos 9% ditos", com as derivações de 32%, −11,4% e −7,2% declaradas e as duas capturas de outubro a dezembro como fontes
- **Por quê:** os 38% são medidos contra a queda das exportações (6,5%), que é a **menor** das duas, e não a "mais desfavorável" (a corrente caiu 6,8%) (pergunta 7). O recorte de 12 meses era afirmado sem captura (§3.1, regra 6); a revisão capturou e conferiu: 9 contra 11,4 é desvio de 21%, contra 7,2 é de 25%. A pergunta adversarial (o candidato pode ter usado outro recorte?) fica respondida com número, e o `IMPRECISO` se sustenta em todos.

## A036 (Lula, crescemos 20% com a China)

- **Campos:** `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas
- **Estava:** só o acumulado de janeiro a setembro (12,0% nas exportações, 11,1% na corrente)
- **Passou a valer:** a explicação acrescenta os 12 meses até setembro (16,6% nas exportações, 12,8% na corrente), com derivações e fontes, e diz que os 20% ficam acima de todas as medidas por mais que a margem
- **Por quê:** a mesma pergunta feita em A035 tem que ser feita aqui (pergunta 6, régua igual na mesma resposta). 20 contra 16,6 é desvio de 20%, então o veredito `IMPRECISO` não muda.

## A037, A038 e A039 (Lula, Indonésia 15%, Alemanha 16%, Vietnã 13%)

- **Campos:** `resumo`, `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas em cada
- **Estava:** resumo "No Comex Stat, as exportações à Indonésia [Alemanha, Vietnã] subiram 2,2% [15,8%, 14,1%] até setembro; falta segunda fonte"
- **Passou a valer:**
  - A037: "Pelo Ministério do Desenvolvimento, a exportação à Indonésia subiu 2,2% até setembro, longe do dito; sem segunda fonte"
  - A038: "Pelo Ministério do Desenvolvimento, a exportação à Alemanha subiu 15,8% até setembro, perto do dito; sem segunda fonte"
  - A039: "Pelo Ministério do Desenvolvimento, a exportação ao Vietnã subiu 14,1% até setembro, perto do dito; sem segunda fonte"
  - nas três, a explicação ganha os 12 meses até setembro (Indonésia 0,8% e 2,0%; Alemanha 15,9% e 8,5%; Vietnã 5,5% e 11,9%, exportação e corrente), com derivações e fontes
- **Por quê:** "Comex Stat" é nome de sistema, e a regra de escrita de card pede o nome que o espectador reconhece (escrita-de-card §3). Em A038 e A039 o card é laranja, mas a base oficial dá número perto do dito; sem dizer isso, o card lido sozinho sugeria que o dado contraria a fala (pergunta 8). "Perto do dito" e "longe do dito" deixam a leitura certa sem antecipar o veredito. Os 12 meses respondem, para os três, a mesma pergunta de recorte feita em A035 e A036. O veredito `INSUSTENTAVEL` provisório fica nos três: a captura nova é da mesma base, e a §2.1 e a §3.1 pedem duas fontes independentes, que continuam faltando.
