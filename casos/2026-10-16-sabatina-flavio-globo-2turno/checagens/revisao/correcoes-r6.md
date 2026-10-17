# Correções da revisão r6 (lotes 15, 16 e 17)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A141 a A170. Uma chamada de busca web, atrás do que contradiria um veredito: a atuação de Flávio Bolsonaro pelo PL 3.723/2019 no Senado (A163). Não achou nada que mude o veredito. Três páginas novas foram capturadas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv6` (pedido em `checagens/pedidos-captura/revisao-r6.json`), sem busca: são os PDFs do MapBiomas Fogo (Coleção 5) linkados na página do Monitor do Fogo, que já estava capturada na pasta p16-r10. Uma fonte já capturada no caso de 15/out (página de notícias da PF, pasta `capturas/2026-10-15-sabatina-lula-globo-2turno-p06`) entrou na A167. Todos os 104 trechos dos três lotes, os antigos e os novos, foram conferidos por palavra inteira contra o texto capturado da URL (normalização de `ferramentas/conferir-trechos.py`): todos achados. Os três lotes validam contra `esquemas/checagens.schema.json`, e a conferência de número e ano do validador não acusa aviso.

**Nenhum veredito mudou.** Uma checagem passou a provisória (A142). As notas por checagem estão em `revisao-r6.json`.

## A142 (lote 15), explicação, confiança e resumo

- **Estava:** confiança média; explicação sem marcador, terminando em "Nesta rodada foi feita uma busca dirigida à frase do ranking; Europol e relatórios de apreensão nos portos europeus por origem não foram consultados."; resumo "A ONU lista Santos entre os principais portos de saída de cocaína, mas nenhuma fonte o põe em 2º lugar no mundo".
- **Passou a valer:** explicação começando por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e terminando com o que falta (Europol/EMCDDA, apreensões europeias por porto de origem, World Drug Report posterior a 2022); confiança baixa; resumo "A ONU lista Santos entre os principais portos de saída de cocaína; não foi achada fonte que o ponha em 2º no mundo". Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a própria explicação declarava que fontes pedidas no `o_que_conferir` não foram consultadas, e o relatório do UNODC usado é de 2022. É provisório de fato sem o marcador, o caso da A155 de 15/out. "Nenhuma fonte" afirmava uma ausência que a busca não provou (padrão "não foi achado" dos provisórios).

## A144 (lote 15), resumo, explicação, divergência e prova

- **Estava:** resumo "Fontes mostram orçamento nominal maior e mais investimento em 2023, mas cortes no custeio; falta a série real"; explicação "a fatia de investimento subiu de 6,8% em 2022 para 7,4% no ano seguinte"; divergência "o orçamento nominal das Forças e a fatia de investimento subiram em 2023"; prova do Congresso em Foco "no início do governo".
- **Passou a valer:** resumo "Fontes mostram orçamento nominal maior em 2023 e mais investimento em 2024, mas cortes no custeio; falta a série real"; a explicação diz 7,4% em 2024 e que a reportagem é de 16/02/2025 e fala do ano anterior; divergência e prova ajustadas.
- **Por quê:** o texto capturado do Congresso em Foco (p15) é de 16/2/2025 e diz "No ano passado": o 7,4% é de 2024. Ano errado na tela (pergunta 7). A checagem segue provisória, com marcador e confiança baixa.

## A156 (lote 16), número apurado

- **Estava:** "286.270 registros em 2025 (taxa de 261,7 por 100 mil mulheres)".
- **Passou a valer:** "286.270 registros em 2025 (taxa de 261,7 por cem mil mulheres)".
- **Por quê:** o validador avisava que o "100" não está em trecho nenhum. É a unidade da taxa, não um dado; escrito por extenso, o aviso some sem mudar o sentido.

## A157 (lote 16), fontes, resumo, número apurado, data de referência e explicação

- **Estava:** só imprensa (Diário do Comércio, Extra Classe, Revista Oeste, IHU), com o relatório do MapBiomas não capturado; resumo "Segundo o MapBiomas, a Amazônia teve 15,6 milhões de hectares queimados em 2024, a maior área da série"; dado da coleção publicada em 2025.
- **Passou a valer:** entrou como N2 a ficha técnica do MapBiomas Fogo, Coleção 5 (versão 15/07/2026, captura rv6 `966d4c254781`), com o trecho "Exatamente um ano após a maior área queimada (15,8Mha)"; resumo "Segundo o MapBiomas, a Amazônia teve 15,8 milhões de hectares queimados em 2024, a maior área da série"; número apurado e data de referência na Coleção 5; a explicação registra os dois valores (15,6 na coleção anterior, 15,8 na atual). Veredito `VERDADEIRO` mantido.
- **Por quê:** METODOLOGIA §3.1, regras 1 e 2 (série histórica sem N1 ou N2, imprensa reproduzindo primária não conferida) e pergunta 5 (o dado vigente na data da fala é o da Coleção 5, publicada em julho de 2026).

## A158 (lote 16), fontes, resumo, ressalva, número apurado, derivação, data de referência e explicação

- **Estava:** só imprensa (Diário do Comércio, Extra Classe); resumo "Em 2024 o fogo atingiu 30 milhões de hectares no país, a segunda maior área em 40 anos; o recorde foi na Amazônia"; ressalva "A área de 2024 ficou 62% acima da média histórica".
- **Passou a valer:** entrou como N2 o Relatório Anual do Fogo 2025 do MapBiomas, Coleção 5 (17/07/2026, captura rv6 `e5e53a2af2c6`), com o trecho "O maior registro ocorreu em 2007, com cerca de 30,7 milhões de hectares, seguido por [...] 2024, com 30,2 milhões de hectares"; resumo "O fogo atingiu 30,2 milhões de hectares no país em 2024, a 2ª maior área desde 1985, atrás de 2007, segundo o MapBiomas"; ressalva "Na Amazônia, 2024 teve a maior área queimada da série; no país, ficou 1,6% abaixo de 2007", com a derivação "30,7 menos 30,2, dividido por 30,7"; explicação refeita na Coleção 5. Veredito `IMPRECISO` mantido.
- **Por quê:** as mesmas regras da A157. A ressalva antiga (62% acima da média) era da coleção anterior; a nova diz ao espectador o tamanho real do erro (segundo lugar por 1,6%) e onde o recorde vale, para o card não parecer mais duro do que o dado (pergunta 8).

## A159 (lote 16), trecho do Anuário e explicação

- **Estava:** o trecho do Anuário pulava, com `[...]`, a frase do crescimento dos estelionatos; a explicação dizia "alta de mais de 400% desde 2018" e "roubos caíram".
- **Passou a valer:** o trecho inclui "O crescimento superior a 400% desde 2018 evidencia uma profunda transformação das dinâmicas", cópia do mesmo parágrafo capturado (p16-r6); "roubos caíram" saiu da explicação, que fica com "o total de ocorrências patrimoniais segue em queda".
- **Por quê:** METODOLOGIA §3.1, regra 6: o 400% não estava em trecho. A queda dos roubos não está escrita no Anuário capturado, que diz que o total de ocorrências cai e que os furtos passaram a superar os roubos.

## A160 (lote 16), explicação

- **Estava:** "reportagens da Gazeta do Povo e do Metrópoles que reproduzem a divulgação de 6/8".
- **Passou a valer:** "a reportagem da Gazeta do Povo, que reproduz a divulgação de 6/8".
- **Por quê:** não há fonte do Metrópoles na checagem nem captura dela; a explicação citava uma fonte que o arquivo não tem (pergunta 3).

## A167 (lote 17), fontes e explicação

- **Estava:** três reportagens (O Liberal, Diário do Pará, Bahia Notícias) do mesmo balanço oficial da PF e da PRF de fevereiro de 2026, apresentadas como apoio independente.
- **Passou a valer:** entrou como N1 a página de notícias da Polícia Federal (captura de 16/10/2026, caso de 15/out, pasta p06), com o trecho "PF e BPFRON apreendem mais de 500 kg de maconha no Paraná [...] PF apreende quatro pistolas ocultas em caixas de som em Cascavel/PR"; a explicação declara que as três reportagens reproduzem o mesmo balanço e contam como uma fonte (regra 2 da §3.1). Veredito `FALSO` mantido.
- **Por quê:** METODOLOGIA §3.1, regras 2 e 3. Sem a fonte nova, o `FALSO` se apoiava numa só fonte de fato. A página da PF é registro primário, independente do balanço, de fiscalização na véspera da fala.

## Para a passada de coerência, sem mudança feita

- **Régua de ranking (A158 e A142):** a A158 ficou `IMPRECISO` com 2024 a 1,6% de 2007, porque a frase afirma uma posição. Conferir se outro "o maior", "o segundo" ou "recorde" dos dois casos foi tratado do mesmo jeito quando a diferença é pequena.
- **Recordista por métrica (A155, A157, A159, A160):** A157 é `VERDADEIRO` com uma de duas métricas (área sim, focos não); A155 e A159 são `IMPRECISO` porque o recorde vale para um recorte e o total cai. A diferença declarada é total contra recorte, não métrica contra métrica. Conferir se a distinção se sustenta lida pelo espectador.
- **Frase absoluta (A166 e A167):** A167 ("não fiscaliza") é `FALSO` pela leitura literal; A166 ("não compraram arma em loja") é `VERDADEIRO` lida no contexto, com fontes só da PM do Rio e sem os estudos de desvio de armas de CAC que o `o_que_conferir` pedia. Conferir se a mesma régua de literalidade vale para as duas e para as frases absolutas de Lula no caso de 15/out.
- **Só imprensa reproduzindo primária não capturada:** A143, A145 a A150 (eventos sem número) e A166 seguem sem N1 ou N2, aceitas pela regra das redações independentes, como A032 e A140 no caso de 15/out.
