# Correções da passada de coerência entre lotes

Passada separada, em 17/10/2026, depois das revisões r1 a r7 (lote a lote) e da rodada 2, seguindo `skills/revisar-checagem.md` (pergunta 6: a mesma régua nos dois lados da mesa, entre lotes e entre casos), `docs/METODOLOGIA.md` §2 e §3 e `.cursor/rules/etica-e-risco.mdc`. O revisor não checou nem revisou nenhum lote deste caso antes. Comparação feita com o caso de Lula de 15/out (`checagens-sabatina-completa.json`) e com os dois casos de Flávio de 28/ago. **Sem busca web** (zero de duas) e **sem fonte nova**: nenhum trecho entrou ou mudou, e o validador confere 735 de 735 trechos na página capturada. As 57 fontes com data de consulta de 16/out (aviso "consultada antes da extração") têm captura com a mesma data. A113 e A161 seguem provisórias e não foram tocadas.

Depois da junção, o validador reprova só por A113 e A161 (confiança baixa sem revisão registrada, que some com o registro). Os erros de A114 e A138 e os avisos de A016, A047, A078, A085, A097 e A179 foram resolvidos nos lotes. Os lotes mexidos (02, 04, 05, 07, 08, 09, 10, 11, 12, 14, 18, 19, 20, 21) passam no `esquemas/checagens.schema.json`.

**Mudaram cinco vereditos:** A078, A085, A114 e A138 passaram a `INSUSTENTAVEL` pela regra 1 da §3.1, a mesma régua para os dois lados; A194 passou de `INSUSTENTAVEL` a `IMPRECISO`. Mudaram ainda a confiança de nove checagens, o texto de A094 e o formato de seis campos que o validador acusava. As notas por checagem, inclusive dos pares examinados e mantidos, estão em `revisao-coerencia.json`.

## A114 (lote 12), veredito, resumo, número apurado e explicação · par A113, A037; A018 e A040 do caso de 15/out

- **Estava:** `IMPRECISO`; resumo "Em maio de 2020 o novo diretor da PF trocou seis superintendentes num só ato, entre eles o do Rio, o mais questionado"; quatro fontes N4. O validador dava erro: tipo `comparacao` sem fonte N1 ou N2.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Imprensa registra seis superintendentes da PF trocados num só ato em maio de 2020; o Diário Oficial não foi conferido"; a explicação diz que a leitura das fontes aponta IMPRECISO, mas que falta o Diário Oficial de 25/05/2020, e que não é FALSO porque nada inverte a comparação.
- **Por quê:** número só com imprensa, sem a primária capturada. É a régua da A113 (as 27 trocas atribuídas a Lula, `INSUSTENTAVEL` pelo mesmo motivo), da A037 e das A018 e A040 do caso de 15/out. Não havia N1 ou N2 já capturada: a varredura das capturas dos dois casos não achou o Diário Oficial de 2020.

## A138 (lote 14), veredito, resumo, ressalva, número apurado e explicação · par A078, A114

- **Estava:** `VERDADEIRO`, desde a revisão r5; resumo "Eduardo esteve com o presidente do Parlamento de Israel em maio de 2016; os contatos com a direita dos EUA vêm de 2018"; cinco fontes N4. O validador dava erro: tipo `serie_historica` sem fonte N1 ou N2.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Times of Israel e Folha registram visita de Eduardo a Israel em maio de 2016; não há registro oficial conferido"; ressalva "Os contatos com a direita dos EUA começam em 2018; a viagem de 2016 só aparece em reportagens"; a explicação diz que a leitura das reportagens daria VERDADEIRO, que nada contradiz o prazo e que falta o registro oficial da viagem (missão da Câmara ou agenda do Knesset).
- **Por quê:** a alegação é numérica e todas as fontes são imprensa; nenhuma N1 ou N2 sobre a viagem de 2016 estava capturada (varredura das capturas dos quatro casos). A mesma régua foi aplicada à A078 da entrevistadora, para não deixar um lado da mesa com régua mais dura.

## A078 (lote 08), veredito, resumo, número apurado e explicação · par A138

- **Estava:** `VERDADEIRO`; resumo "PF e Intercept registram o fundo sem atividade por quase quatro anos, até a 1ª remessa para o filme em 2025"; número apurado com "24/11/2020" (aviso do validador: "24" e "11" fora de trecho).
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Intercept e relatório da PF falam em quase quatro anos sem atividade; o registro do fundo não foi conferido"; número apurado "quase quatro anos sem atividade pública (registro em novembro de 2020; primeira remessa em 13/02/2025), segundo o Intercept e o relatório da PF"; ressalva mantida.
- **Por quê:** é o par da A138 do lado da entrevistadora: um prazo em anos sustentado só por imprensa. Aqui a fonte é ainda mais fraca, porque o relatório da PF reproduzido por O Povo e TVT News cita a própria reportagem do Intercept, e as três fontes têm, para o prazo, uma origem só (regra 3 da §3.1). Com a A138 em `INSUSTENTAVEL` e esta em `VERDADEIRO`, o mesmo tipo de afirmação teria réguas diferentes dos dois lados da mesa. Ver "Para o autor", item 1.

## A085 (lote 09), veredito, resumo, número apurado e explicação · par A090, A173, A174; A126 do caso de 15/out

- **Estava:** `VERDADEIRO`; resumo "Perícia contratada pela produtora Go Up declarou custo de US$ 13,3 milhões, pouco mais de R$ 75 milhões"; número apurado começando por "US$ 13,3 milhões" (aviso do validador: unidade diferente da do número dito); a explicação invocava a regra 2 da §3.1 sem a primária conferida.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão US$ 13,3 milhões, pouco mais de R$ 75 milhões, no laudo da produtora; o laudo não é público"; número apurado "R$ 75,1 milhões no Correio da Manhã; US$ 13,3 milhões, pouco mais de R$ 75 milhões, no Metrópoles (via A Tarde); laudo não conferido"; ressalva mantida. A A086, que cita o valor numa conta lateral, passou a dizer "atribuído à perícia pelas reportagens".
- **Por quê:** é afirmação de valor, e o laudo, anexado a inquérito, não foi conferido; a regra 2 só aceita imprensa no lugar da primária conferida, e a revisão r3 já apontava isso. A A090 do candidato, na mesma situação (valores de mensagens de Vorcaro lidas pela imprensa num inquérito não público), ficou `INSUSTENTAVEL` "e não IMPRECISO, que exigiria fonte N1 ou N2", e a r3 registrou que pela régua da A085 ela seria IMPRECISO. As A173 e A174 da própria entrevistadora (percentuais da Quaest só em reportagens) e a A126 do caso de 15/out (estudo da FGV só na imprensa) também são `INSUSTENTAVEL`. A diferença de tipo na extração (atribuição contra valor monetário) não muda a regra 1, que vale para afirmação que envolve valor.

## A194 (lote 20), veredito e explicação · par A192; A089, A098 e A110 do caso de 15/out

- **Estava:** `INSUSTENTAVEL`, pela §5 de etica-e-risco (fato em apuração).
- **Passou a valer:** `IMPRECISO`; resumo e ressalva mantidos ("Bacellar segue preso desde março por suspeita de vazar operação contra o CV; a PF o descreve como líder político"); a explicação diz que o veredito trata dos atos formais (a prisão e o relatório da PF), não do mérito, que segue em apuração.
- **Por quê:** a A192, da mesma entrevistadora e do mesmo bloco, descreve as suspeitas de uma representação formal da PF e teve veredito sobre o enunciado (`VERDADEIRO`); as A089, A098 e A110 de 15/out fizeram o mesmo com a existência e a data de inquéritos. Pela mesma régua, a frase da A194 tem os dois atos documentados (ele está preso; a PF o descreve como líder do núcleo político), mas liga a prisão ao motivo errado: o fundamento formal é o vazamento. É o "certo, com recorte errado" do §2.2. A A196 (Castro "enrolado", igual à A076 de 15/out, "implicado") e a A082 seguem `INSUSTENTAVEL` porque qualificam o envolvimento, que é o mérito.

## A094 (lote 10), resumo, ressalva e explicação · par A095, A084, A093

- **Estava:** resumo "Áudio publicado pela Veja cita os dois filmes e relato de R$ 30 milhões; autenticidade e pagamento sem confirmação"; ressalva "A fala sobre os filmes consta do áudio publicado; o pagamento e a legalidade do patrocínio ao Dark Horse seguem em apuração"; a explicação apoiava o `INSUSTENTAVEL` em três frentes, duas delas sobre a verdade do conteúdo (pagamento, legalidade).
- **Passou a valer:** resumo "Áudio publicado diz que o filme de Lula foi por fora e o de Flávio, patrocínio; valor e autenticidade sem confirmação"; ressalva "Os R$ 30 milhões não estão no trecho transcrito do áudio; a nota oficial da defesa não reconhece o material"; a explicação checa o que o áudio diz e a autoria. Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a frase é atribuição ("o que ele fala nesse áudio"). A A095, da entrevistadora, foi checada como norma, e não como cumprimento da norma; a A093 trata "só do que a defesa declarou"; a A084, sobre o mesmo valor, se apoia na divergência entre O Povo e Estadão sobre o valor estar na gravação. A A094 julgava também o conteúdo do áudio. Agora as quatro usam o mesmo critério: checa-se o que foi dito no registro citado, não se o que ele diz é verdade.

## A040, A045, A065, A106, A108, A189, A195, A198 (entrevistadora) e A202 (candidato), confiança

- **Estava:** confiança alta, com todas as fontes N4.
- **Passou a valer:** confiança média. Vereditos mantidos.
- **Por quê:** o esquema e a skill `checar-alegacao` definem alta como "fonte N1 direta e inequívoca"; o resto do caso segue isso. Para comparar: a A071 de 15/out (Dino indicado por Lula) tem fonte N1 (Planalto), e a A065 daqui (Nunes Marques indicado por Bolsonaro) só imprensa. O caso de 15/out tem 17 checagens com confiança alta sem N1 (ver "Para o autor").

## A016 (lote 02), número apurado e ressalva · aviso do validador

- **Estava:** número apurado "1,5% do PIB, cerca de R$ 190 bilhões (Daniella Marques); ..." e ressalva "Integrantes da campanha evitam cravar o valor, e ainda não há plano completo com os gastos a cortar".
- **Passou a valer:** número apurado "R$ 190 bilhões, cerca de 1,5% do PIB (Daniella Marques); discurso de corte em torno de R$ 200 bilhões"; ressalva "A coordenadora falou em cerca de R$ 190 bi; a campanha evita cravar o valor e não tem plano completo de cortes".
- **Por quê:** o validador comparava 200 com 1,5 e acusava 13.233% de desvio; com o valor em reais na frente, compara 200 com 190 (5%), e a ressalva de um `VERDADEIRO` arredondado tem que mostrar o valor apurado (§2.2). A A016 trata de falas públicas da campanha, cujo registro é a própria fala relatada pela imprensa; por isso não recebeu a régua da A085, que trata de documento não público.

## A097 (lote 10) e A179 (lote 18), ressalva · aviso do validador

- **A097, estava:** "Com as administradoras de consórcio, o total chega a 1.785; com os bancos de câmbio, a 171 bancos". **Passou a valer:** "Sem as administradoras de consórcio, 1.654 instituições e 167 bancos; com elas, 1.785, e com os de câmbio, 171 bancos".
- **A179, estava:** "Pelos dados de saúde, os homicídios caíram 21%, com alerta de subnotificação em 2019". **Passou a valer:** "Queda exata de 17,8% na taxa de mortes violentas; nos dados de saúde, 21%, com alerta de subnotificação em 2019".
- **Por quê:** `VERDADEIRO` com número arredondado tem que trazer o valor apurado na ressalva (§2.2); as duas mostravam só o recorte alternativo.

## A047 (lote 05), número apurado · aviso do validador

- **Estava:** "... no levantamento da Folha até 17/09/2026". **Passou a valer:** "... até 17 de setembro de 2026".
- **Por quê:** o "09" da data aparecia ao validador como número sem trecho; a data está nas fontes e na data de referência.

## Mantidos depois de comparados (resumo; o detalhe está no JSON)

- **A010 contra a A161 de 15/out:** quando há fala pública do campo do adversário que confere em parte (aliados, só Petrobras), `IMPRECISO` (A008, A010); quando não há fala pública nenhuma, `INSUSTENTAVEL` (A009 aqui, A161 lá, que tinha só estudo interno relatado). Mesma régua.
- **A071 contra A072 e A086:** objetos diferentes. Dinheiro já transferido converte-se pelo dólar de cada repasse (datas conhecidas); valor negociado, sem data de pagamento, pela média do ano com a faixa das conversões na ressalva. Os desvios das três medem sobre o apurado.
- **A036 contra A037 (e A013 e A014 de 28/ago):** a diferença vem da fonte: o decreto de 2019 é N1 e o número confere com categoria trocada (`IMPRECISO`); para os 22.500 não há N1 nem fonte nenhuma com o número, e o apurado da imprensa é cinco vezes menor (`INSUSTENTAVEL`). Mesmos vereditos de 28/ago.
- **A031 ("desde o início", entrevistadora) e A038 ("sempre", candidato):** os dois `VERDADEIRO` com ressalva de que não há registro anterior a maio de 2026. Mesma régua.
- **A081 e A089:** quase a mesma afirmação, mesmo veredito e mesmo critério. Contam duas vezes do lado do candidato (ver "Para o autor").
- **A181 (`IMPRECISO`) contra A182 (`FALSO`):** a A181 acerta o fato (o direito à legítima defesa existe, no Código Penal) e erra o lugar (a Constituição); a A182 é contradita no essencial pelo texto vigente do Estatuto e do decreto. Réguas coerentes.
- **A192 contra a A064 de 15/out:** a A192 descreve o conteúdo de representação formal da PF que embasou prisão; a A064 de 15/out falava de suspeitas difusas sobre ministros, sem peça formal contra eles. Mantido aqui; ver "Para o autor".
- **A123 (`FALSO`, "nenhuma arma"):** teve revisão adversarial própria na r5 deste caso, que testou a leitura "arma de fogo" e a manteve na ressalva; a A009 de 28/ago tem o mesmo veredito e as mesmas fontes.
- **Base do desvio:** todas as contas de desvio deste caso medem sobre o valor apurado (A003, A011, A012, A013, A014, A017, A018, A019, A022, A047, A062, A071, A072, A086, A097, A120, A124, A179, A185, A187). Na A011, 7 contra 7,75 dá 9,7% sobre o apurado (`VERDADEIRO`, como a A006 de 28/ago).
- **"Quase" e "mais de":** "quase" lido com rigor nos dois lados (A003 da entrevistadora e A014 do candidato, `IMPRECISO` com o erro para menos; A071, A097 e A023 dentro da régua); "mais de" lido com rigor na A020.

## Para o autor, sem mudança feita

1. **Prazo e data só com imprensa.** A A138 virou `INSUSTENTAVEL` porque a extração a marcou como `serie_historica`, e a A078 recebeu a mesma régua para os dois lados da mesa. No caso de 15/out, a A140 (entrevistadora, "um ano e nove meses" de Galípolo no BC, `data_ou_prazo`, só imprensa) ficou `VERDADEIRO` com confiança alta, com o argumento de que "a afirmação é de data". Se o autor decidir que prazo e data ficam fora da regra 1 (que lista número, série histórica, valor e ranking), A138 e A078 voltam juntas a `VERDADEIRO`, e o tipo da A138 nas alegações passa a `data_ou_prazo`; se decidir que entram, a A140 de 15/out precisa da mesma régua. Não editei o outro caso.
2. **Confiança alta sem N1 no caso de 15/out:** A005, A006, A024, A046, A052, A066, A067, A068, A069, A070, A127, A140, A144, A145, A147, A150 e A151. Aqui a régua do esquema foi aplicada; lá, não.
3. **A033 do caso de 15/out** mede o desvio sobre o número dito (10 minutos sobre 90, "cerca de 11%"); sobre o apurado são 12,5%. O veredito não muda, mas é a única conta daquele caso fora da base declarada pela coerência de 15/out.
4. **A064 do caso de 15/out** ("as suspeitas que pairam sobre vários ministros", `INSUSTENTAVEL`): pela régua aplicada aqui (o que está documentado pode ser dito como documentado), a existência das suspeitas noticiadas teria veredito sobre o enunciado. A diferença para a A192 daqui está escrita (peça formal contra o investigado lá não havia), mas a decisão é do autor.
5. **A081 e A089** (e, em parte, A084 e A094) são quase a mesma afirmação e pesam duas vezes na contagem do candidato. É decisão de extração. A r3 também pediu para ouvir o "ilícito" da transcrição em 1112,6 s, perto da A089.
6. **A009 do caso de 28/ago** (`FALSO`, "nenhuma arma") não tem revisão adversarial registrada; a A123 daqui, com o mesmo veredito, tem (r5).
7. O validador acusa **5 URLs citadas sem captura assinada** em `CAPTURAS.json` (Agenda do Poder, duas; Banco Mundial; IBGE/SIDRA; Diário do Transporte). Já estavam antes desta passada e não são dos lotes.
