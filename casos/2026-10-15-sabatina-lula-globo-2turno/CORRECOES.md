# CORREÇÕES · sabatina de Lula na TV Globo, 2º turno (15/out/2026)

Registro de tudo o que mudou na checagem DEPOIS do primeiro veredito, antes de qualquer publicação. ⛔ Veredito não se edita em silêncio (METODOLOGIA §7). Cada passada foi feita por um agente de IA que não escreveu a checagem que revisou.

## 1. A busca web acabou na primeira rodada (16/out, ~02h)

A checagem das 193 alegações rodou em 15 agentes em paralelo, que dividiam um limite de 200 buscas web por turno. O limite acabou no meio do trabalho. Onde a busca não foi exaustiva, o veredito saiu INSUSTENTAVEL com confiança baixa e a explicação começando por "Busca interrompida pelo limite...", para não fingir uma busca que não houve. Foram 34 assim. Na rodada 2 (16/out, manhã), com a busca de volta, as 34 foram refeitas por outros 4 agentes e revisadas por um quinto. Nenhuma ficou provisória.

| id | rodada 1 | rodada 2 (final) |
|---|---|---|
| A016 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A017 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A028 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A029 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A032 | VERDADEIRO (provisório) | VERDADEIRO |
| A034 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A037 | INSUSTENTAVEL (provisório) | IMPRECISO |
| A038 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A039 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A063 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A080 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A085 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A086 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A092 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A093 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A099 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A100 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A101 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A103 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A126 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A153 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A157 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A158 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A161 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A163 | INSUSTENTAVEL (provisório) | IMPRECISO |
| A165 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A169 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A174 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A178 | INSUSTENTAVEL (provisório) | IMPRECISO |
| A179 | INSUSTENTAVEL (provisório) | VERDADEIRO |
| A180 | INSUSTENTAVEL (provisório) | IMPRECISO |
| A182 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A187 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL |
| A192 | INSUSTENTAVEL (provisório) | IMPRECISO |

## 2. A revisão adversarial, lote a lote, e a de coerência entre lotes

As notas completas estão no campo `revisao_ia` de cada checagem. As mudanças, uma por uma, com o antes e o depois:

### revisao\correcoes-r1.md

#### Correções da revisão r1 (lotes 01 e 02)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p01` e `-p02`, e cada trecho novo foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Nenhum veredito mudou. As notas por checagem estão em `revisao-r1.json`.

#### A003 (lote 01), explicação

- **Estava:** "a avaliação 'ruim ou péssimo' nunca chegou à maioria nas rodadas lidas: 40% e 41% no Datafolha"; série do Datafolha sem a rodada de 20 e 21 de maio; Quaest de 14 de agosto (48% e 46%) e de 2 de setembro (48% e 45%) sem trecho em fonte nenhuma; "em julho e agosto a aprovação ficou numericamente à frente".
- **Passou a valer:** "ruim ou péssimo" de 38% a 42% no Datafolha; a série inclui o empate de 20 e 21 de maio (48% e 48%) e a rodada Quaest de 50% e 44% citada no trecho de 28/09; "em julho e no início de agosto a aprovação ficou numericamente à frente nos dois institutos".
- **Por quê:** METODOLOGIA §3.1, regra 6 (número sem trecho) e pergunta 7 do roteiro. O 40% e 41% omitia o 42% que já estava no trecho do DGABC; o empate de maio estava numa página capturada e não usada; em 14 de agosto a Quaest já tinha a desaprovação à frente, então "julho e agosto" esticava o dado.

#### A003 (lote 01), fontes

- **Estava:** 9 fontes.
- **Passou a valer:** 11 fontes. Entraram Congresso em Foco, "Datafolha: rejeição a Lula cai, e aprovação encurta distância" (23/05/2026, captura p01 `fdf1e7c88b91`), e Diario de Pernambuco (Estadão Conteúdo), "Quaest: 48% desaprovam o governo Lula e 45% aprovam" (02/09/2026, captura p01 `4225091c34ba`).
- **Por quê:** dar trecho aos números da explicação que não tinham (pergunta 3 e regra 6).

#### A003 (lote 01), ressalva

- **Estava:** "Em julho e agosto a aprovação ficou numericamente à frente, e várias diferenças estavam na margem de 2 pontos"
- **Passou a valer:** "Houve empate em maio, a aprovação ficou à frente em julho e no início de agosto, e várias diferenças estavam na margem de 2 pontos"
- **Por quê:** a ressalva vai para a tela; o empate de maio pesa a favor do IMPRECISO e faltava, e "agosto" inteiro não confere (pergunta 8).

#### A011 (lote 01), fontes

- **Estava:** InfoMoney (N4), O Povo (N4) e Aos Fatos (N3); nenhuma N1 ou N2.
- **Passou a valer:** entrou Senado Federal (Presidência do Senado), "Congresso Nacional promulga PEC da Transição que garante a manutenção de R$ 600 a famílias carentes" (22/12/2022, captura p01 `f18364979177`), como N1, com o trecho que diz que a emenda "impediu a redução, já no próximo mês de janeiro, do valor pago" e abriu R$ 70 bilhões para o Bolsa Família.
- **Por quê:** METODOLOGIA §3.1, regra 1: o card traz valores e não havia fonte N1 ou N2. A fonte oficial confirma o ponto que decide o veredito (havia programa no orçamento, faltava verba para os R$ 600).

#### A011 (lote 01), explicação

- **Estava:** "O PLOA em si não foi capturado; os números vêm de três reportagens que leram o projeto, com os mesmos valores."
- **Passou a valer:** "O PLOA em si não foi capturado; os valores do projeto vêm de duas reportagens independentes que o leram, com os mesmos números, e o registro oficial do Senado na promulgação da PEC da Transição confirma o ponto central: a emenda garantiu os R$ 600 e, nas palavras do presidente do Congresso, impediu a redução do valor pago já em janeiro."
- **Por quê:** só duas das três reportagens trazem os valores do projeto (o Aos Fatos não traz R$ 105,7 bi nem R$ 405), e a explicação passa a citar a fonte N1 nova.

#### A014 (lote 02), resumo

- **Estava:** "Tebet, do MDB, apoiou em 2022 e foi ministra; PSDB e Cidadania também apoiaram e ficaram sem ministério"
- **Passou a valer:** "Tebet, do MDB, apoiou em 2022 e foi ministra; o Cidadania e quadros do PSDB também apoiaram e ficaram sem ministério"
- **Por quê:** o trecho do Mais Goiás diz que o PSDB liberou os filiados e que quem apoiou foram quadros como Serra e FHC. O card dizia que o partido apoiou, o que a fonte não sustenta (perguntas 7 e 8).

#### A014 (lote 02), fontes

- **Estava:** 6 fontes, nenhuma com a permanência de Tebet no ministério até 2026, que a explicação afirma ("foi ministra do Planejamento de 2023 até sair para disputar a eleição de 2026").
- **Passou a valer:** entrou Poder360, "Simone Tebet confirma saída do governo até 30 de março" (30/01/2026, captura p02 `afef4debdb40`).
- **Por quê:** pergunta 3; o fato que mais pesa contra a frase da entrevistadora precisava de trecho.

#### A018 (lote 02), trecho da fonte Aos Fatos

- **Estava:** o segundo pedaço do trecho começava em "Segundo a secretaria, a taxa de aprovação seria de 94%".
- **Passou a valer:** o pedaço começa em "Em resposta ao levantamento feito pela Folha de S.Paulo, em janeiro, a Secretaria de Relações Institucionais alegou ser equivocado considerar que houve aprovação de apenas 15% das MPs no primeiro biênio de governo.", e a `prova` cita os 15%.
- **Por quê:** a `divergencia_entre_fontes` cita "15% a 23%" e o 15% não estava em trecho nenhum (regra 6). A frase está na mesma página capturada (p02 `02fb36f61265`).

#### A025 (lote 02), trecho da fonte Expreso (Agencia EFE)

- **Estava:** só a frase de Alckmin sobre a "buena química".
- **Passou a valer:** o trecho começa com "Tensión diplomática: Washington expulsó a un policía brasileño en Miami; Brasil respondió retirando credenciales a un agente de EE. UU. Conflicto Bolsonaro: La relación se tensó por la denegación de visado a un consejero de Trump para visitar al expresidente preso.", e a `prova` cita os dois atritos.
- **Por quê:** a ressalva, que vai para a tela, cita a expulsão de agente e a negação de visto, e nenhum trecho trazia esses fatos (perguntas 3 e 7). A frase está na mesma página capturada (p02 `17f80feaafbf`).

### revisao\correcoes-r2.md

#### Correções da revisão r2 (lotes 04 e 05)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: a fonte nova abaixo já estava capturada em `capturas/2026-10-15-sabatina-lula-globo-2turno-p05`, e o trecho foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Nenhum veredito mudou. As notas por checagem (A040 a A065) estão em `revisao-r2.json`.

#### A042 (lote 04), explicação

- **Estava:** "o governo já acionou o rito da lei (consultas e análise na Camex), em 2025 e em 2026; o que não houve foi a retaliação."
- **Passou a valer:** "o governo já acionou o rito da lei, com a abertura formal do processo em 13 de agosto de 2026; o que não houve foi a retaliação."
- **Por quê:** METODOLOGIA §1 (nenhum veredito nasce da memória do modelo) e pergunta 7 do roteiro. Nenhum trecho das cinco fontes registra acionamento da lei em 2025, nem consultas na Camex; a abertura de 13/08/2026 tem lastro no trecho da Band. Veredito, resumo e ressalva sem mudança.

#### A057 (lote 05), fontes

- **Estava:** 3 fontes (Diário do Nordeste, Gazeta do Povo, Poder360). O campo `divergencia_entre_fontes` citava o Congresso em Foco ("diz que foi em abril"), que não estava na lista.
- **Passou a valer:** 4 fontes. Entrou Congresso em Foco (N4), "Ex-ministro de Lula, Camilo Santana assume liderança do PT no Senado" (captura p05 `0264a4417ba2`), com o trecho "Camilo Santana já ocupava a vice-liderança desde abril, quando retomou seu mandato no Senado. O parlamentar estava afastado para comando do Ministério da Educação desde 2023."
- **Por quê:** pergunta 3 do roteiro. A divergência registrada não tinha trecho de fonte; agora as duas datas (junho no Poder360, abril no Congresso em Foco) estão nas fontes, e o novo trecho confirma também que ele foi ministro da Educação. Veredito, resumo e ressalva sem mudança.

#### Registrado sem mudança no lote

- **A042, arquivo de alegações:** a `afirmacao` ("O governo Lula não acionou a lei da reciprocidade contra os Estados Unidos") é mais larga que a frase, que trata de aplicar a retaliação. A checagem avaliou a frase no contexto, e o card está certo; o ajuste da `afirmacao` é da extração, fora dos lotes.
- **A063:** checagem provisória. Ao refazer, a régua de "bastante" deve ser a mesma da A053 (ocasiões distintas bastaram lá), além da contagem comparada que o critério previa.
- **A064:** fica INSUSTENTAVEL por simetria com A074 e A076 (falas de Lula sobre ministros e pessoas citadas no caso Master, também INSUSTENTAVEL pela ética §5). Se o autor decidir que a existência de suspeitas é fato concluído, as três mudam juntas.

### revisao\correcoes-r3.md

#### Correções da revisão r3 (lotes 06 e 07)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`, `docs/METODOLOGIA.md` §2 a §5 e `.cursor/rules/etica-e-risco.mdc`. Sem busca web nesta rodada e sem captura nova: toda fonte que entrou abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p06`, `-p07` e `-p08`, e os 84 trechos dos dois lotes, depois das mudanças, foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py` (84 de 84 achados). Números e anos de `resumo` e `ressalva` foram conferidos com as funções `numeros_de()` e `anos_de()` do validador (nenhum aviso). Três vereditos mudaram (A081, A088, A089). As notas por checagem estão em `revisao-r3.json`.

#### A072 (lote 06), ressalva

- **Estava:** "A vista suspende o julgamento por até 90 dias; vencido o prazo, o caso é liberado automaticamente"
- **Passou a valer:** "A vista suspende o julgamento por 90 dias, prorrogáveis uma vez; vencido o prazo, o caso é liberado automaticamente"
- **Por quê:** o § 4º do art. 134 do Regimento Interno do STF suspende o prazo no recesso e permite prorrogá-lo uma vez por igual período. "Por até 90 dias" prometia um teto que não existe e contradizia a ressalva da A078, que vai no mesmo vídeo (perguntas 6 e 8).

#### A072 (lote 06), explicação e fonte

- **Estava:** "pelo Regimento Interno do STF a vista tem prazo de 90 dias, e vencido o prazo os autos são liberados automaticamente"; trecho do Regimento com o caput do art. 134 e o § 5º.
- **Passou a valer:** "pelo Regimento Interno do STF a vista tem prazo de 90 dias, que fica suspenso no recesso e pode ser prorrogado uma vez por igual período, e vencido o prazo os autos são liberados automaticamente"; o trecho do Regimento (captura p06 `e27b39c8c544`) ganhou o § 4º, com `[...]` antes do § 5º, porque entre os dois há a nota da Emenda Regimental 54.
- **Por quê:** dar lastro à ressalva nova (pergunta 3).

#### A073 (lote 06), resumo

- **Estava:** "O relatório da PF se concentrou em Moraes, mas o STF não apurou quais ministros são citados nem em que condição"
- **Passou a valer:** "O relatório da PF dedicou 181 de 218 páginas a Moraes, mas nenhuma fonte compara o envolvimento de cada ministro"
- **Por quê:** "o STF não apurou" atribuía ao tribunal o argumento de um voto, o de Gilmar Mendes numa questão de ordem que, pelo Poder360 capturado, estava 4 a 3 contra quando Dino pediu vista. O card passa a dizer o dado (181 de 218, no trecho do Movimento Econômico) e o que falta para o ranking, sem tomar a posição de um dos lados do plenário (perguntas 7 e 8). O veredito INSUSTENTAVEL não muda.

#### A073 (lote 06), explicação e prova da fonte

- **Estava:** "Mas o próprio voto de Gilmar Mendes na questão de ordem de 15/09 diz [...]"; prova: "Documento do STF: a apuração mirou Moraes, mas não há certificação de quais ministros são citados nem em que condição, o que impede o ranking."
- **Passou a valer:** a explicação diz que o voto "é a posição de um ministro numa proposta que não foi aprovada até a data da fala, e não uma conclusão do tribunal", e registra que a mesma régua valeu para as falas do entrevistado sobre Toffoli, Mendonça e Castro; a prova trata o documento como voto de um ministro.
- **Por quê:** pergunta 4 (a fonte prova o que o dono dela disse, não o fato) e pergunta 6 (simetria declarada).

#### A077 (lote 06), ressalva

- **Estava:** "O presidente nomeia ministros, com aval do Senado, e pode conceder indulto; nenhum dos dois muda decisão"
- **Passou a valer:** "O governo pode recorrer pela AGU, como fez em setembro, mas quem decide o recurso é o próprio STF"
- **Por quê:** o melhor argumento contra a frase do entrevistado é que o governo contestou, em setembro, a decisão de Mendonça que afastou o diretor-geral da PF, e o presidente do STF a suspendeu. A ressalva antiga falava de dois poderes que não vêm ao caso e omitia o caminho que existe e foi usado (pergunta 8). O veredito VERDADEIRO não muda: recorrer é pedir ao Judiciário, não interferir na decisão.

#### A077 (lote 06), fontes e explicação

- **Estava:** 3 fontes (Constituição, Regimento do STF, Poder360); explicação sem o recurso da AGU.
- **Passou a valer:** 4 fontes. Entrou O Povo, "Fachin suspende decisões de Mendonça e Dino e mantém Andrei Rodrigues na chefia da PF" (09/09/2026, captura p07 `f8d435ff6b76`), com o trecho do recurso da AGU e da suspensão; a explicação traz o argumento e por que ele não derruba o veredito.
- **Por quê:** lastro da ressalva nova (pergunta 3).

#### A081 (lote 07), veredito

- **Estava:** `INSUSTENTAVEL`
- **Passou a valer:** `IMPRECISO`
- **Por quê:** a transcrição de 27/08 já usada como fonte (Aos Fatos, captura p07 `9ef3ea4cdf53`, conferida contra a transcrição deste repositório em `casos/2026-08-27-sabatina-lula-globo`) traz, no bloco do INSS, "todos eles que foram citados [...] o caminho é um só. É o caminho da apuração, da investigação, ou da inocência, ou da condenação", e, no bloco do Master, que se Jaques Wagner cometeu desvio "vai pagar o preço". O núcleo do que Lula diz ter repetido (apurar e punir quem errou) está na entrevista anterior da Globo; a árvore do §2.1 reserva INSUSTENTAVEL para quando as fontes não sustentam. O que não está é a frase de que a sociedade não aceitaria, e no bloco do Master a ênfase foi a presunção de inocência: essência certa, enquadramento e assunto não.

#### A081 (lote 07), resumo, ressalva, explicação e fonte

- **Estava:** resumo "Na entrevista à Globo de agosto, sobre o Master, Lula falou em apuração e presunção de inocência, não nessa frase"; ressalva "Ideia parecida aparece em entrevistas de setembro à Rádio Tupi e a um podcast, fora da Globo"; trecho do Aos Fatos só com o bloco do Master.
- **Passou a valer:** resumo "Na Globo, em agosto, Lula defendeu apuração e condenação de quem errou, mas sem dizer que a sociedade não aceitaria"; ressalva "A fala de agosto sobre apuração foi no bloco do INSS; sobre o Master, ele destacou a presunção de inocência"; trecho do Aos Fatos com o bloco do INSS e o do Master, separados por `[...]`; explicação refeita.
- **Por quê:** acompanhar o veredito novo (perguntas 6, 7 e 8).

#### A084 (lote 07), resumo

- **Estava:** "Há reportagens sobre dinheiro do Master, festas e um encontro pago com ministros; 'orgia' não aparece nas fontes"
- **Passou a valer:** "Reportagens citam contrato do Master, festa paga por Vorcaro e suposto encontro com acompanhante; 'orgia' só vem de Lula"
- **Por quê:** "um encontro pago com ministros" lia como encontro de ministros pago por Vorcaro, que não é o que o Diario de Pernambuco registra (reportagem sobre um ministro e uma acompanhante); "festas" no plural não tem lastro (as fontes trazem a degustação de Londres); e "'orgia' não aparece nas fontes" era inexato, porque a palavra aparece, na boca do próprio Lula, na reportagem da Rádio Tupi capturada (perguntas 7 e 8). O veredito INSUSTENTAVEL não muda.

#### A084 (lote 07), ressalva

- **Estava:** "Os casos seguem em apuração e nenhum ministro foi denunciado formalmente"
- **Passou a valer:** "Os relatos seguem em apuração, sem conclusão até a data da fala"
- **Por quê:** "nenhum ministro foi denunciado formalmente" não está em trecho nenhum; a Gazeta só diz que nenhum participante da degustação era investigado (pergunta 7).

#### A087 (lote 07), data de referência

- **Estava:** "evento em Londres de 24 a 26/04/2024"
- **Passou a valer:** "degustação de 25/04/2024, durante fórum em Londres em abril de 2024"
- **Por quê:** o dia 24 não está em trecho nenhum; a Gazeta dá 25/04/2024 para a degustação e o Poder360 dá 26 de abril para o painel de Andrei (pergunta 7). O veredito VERDADEIRO não muda.

#### A088 (lote 07), veredito e confiança

- **Estava:** `INSUSTENTAVEL`, confiança baixa (provisório, "uma fonte só").
- **Passou a valer:** `VERDADEIRO`, confiança média.
- **Por quê:** a segunda fonte existia no caso. O SBT News, "Exclusivo: Banco Central recebeu alerta da PF sobre Master em 2024, mas disse não ter encontrado ilegalidades" (19/03/2026, captura p08 `a83e4caff0b7`, já usada nas checagens A097 e A098), registra que o BC conhecia suspeitas sobre o Master desde 2023 e as analisou com seus departamentos de supervisão. Com o LetsMoney (apuração do Valor: ofícios do Departamento de Supervisão desde 2021 e um ciclo de supervisão sobre irregularidades em crédito e precatórios em 2021 e 2022), são duas fontes independentes que datam a atuação do BC antes de abril de 2024 (pergunta 4).

#### A088 (lote 07), resumo, ressalva, explicação e fontes

- **Estava:** resumo "Uma reportagem registra ofícios do BC ao Master desde 2021; não achamos segunda fonte que confirme a data"; ressalva "O termo de comparecimento do BC contra o Master foi preparado em maio de 2024, depois da festa"; 2 fontes.
- **Passou a valer:** resumo "Ofícios do BC cobravam correções do Master desde 2021, e o BC analisou suspeitas sobre o banco em 2023"; ressalva "Eram ofícios de supervisão; o termo de comparecimento, ação mais dura, só foi preparado em maio de 2024"; 3 fontes (entrou o SBT News, com o trecho da resposta do BC; o trecho do LetsMoney ganhou a linha da tabela de 2021 e 2022); explicação refeita, com o que o SBT diz contra (o BC concluiu então não abrir procedimento específico).
- **Por quê:** num card INSUSTENTAVEL, a ressalva antiga lia como desmentido da entrevistadora, quando a única fonte capturada a sustentava (pergunta 8). A mesma informação passa a ser o "certo, mas" de um VERDADEIRO.

#### A089 (lote 07), veredito e confiança

- **Estava:** `INSUSTENTAVEL`, confiança baixa (provisório).
- **Passou a valer:** `VERDADEIRO`, confiança média.
- **Por quê:** a explicação dizia que nenhuma fonte capturada citava inquérito da PF em São Paulo sobre o Master antes de abril de 2024, mas o SBT News capturado na p08 registra que a Delegacia de Repressão a Crimes Financeiros da PF em São Paulo "havia aberto desde 2023 dois inquéritos sobre o Master". A checagem A098, sobre o mesmo ponto retomado pela entrevistadora minutos depois, já tinha VERDADEIRO com o SBT News e a CNN Brasil: o mesmo vídeo teria dois cards opostos sobre o mesmo fato (pergunta 6). Confiança média porque a data anterior à festa vem só do documento obtido pelo SBT News; a CNN confirma investigação em 2024, sem mês.

#### A089 (lote 07), resumo, ressalva, explicação e fontes

- **Estava:** resumo "As fontes datam o inquérito da PF sobre o Master da venda ao BRB, barrada em 2025; nada de inquérito em SP antes"; sem ressalva; 2 fontes (Jovem Pan, Gazeta do Povo).
- **Passou a valer:** resumo "Ofício obtido pelo SBT News registra dois inquéritos da PF de São Paulo sobre o Master abertos desde 2023"; ressalva "A data de 2023 consta de documento obtido pelo SBT News; o mérito dos inquéritos segue em apuração"; 4 fontes (entraram SBT News e CNN Brasil, com os mesmos trechos da A098, capturas p08; Jovem Pan e Gazeta ficam, com a prova dizendo que tratam do inquérito posterior); explicação refeita.
- **Por quê:** "nada de inquérito em SP antes" era contradito por fonte do próprio caso (perguntas 3, 4 e 8).

### revisao\correcoes-r4.md

#### Correções da revisão r4 (lotes 08 e 09)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p07` e `-p09`, e cada trecho novo foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Um veredito mudou (A104). As notas por checagem estão em `revisao-r4.json`. O lote 09 não foi alterado.

#### A104 (lote 08), veredito

- **Estava:** `INSUSTENTAVEL` (provisório, "busca interrompida pelo limite de buscas"), com a explicação "Nenhuma fonte capturada sustenta a posição atribuída, e nenhuma a contradiz".
- **Passou a valer:** `VERDADEIRO`, confiança baixa (a mesma de antes).
- **Por quê:** a captura p07 `2c258b0dcb7e` (A Crítica de Campo Grande, entrevista de Haddad ao podcast 3 Irmãos, publicada em 6 de junho) traz Haddad dizendo que o Banco Central era o órgão responsável por acompanhar e agir diante das irregularidades do Master, que quem supervisiona banco é o Banco Central, e que o caso foi levado ao conhecimento do Procurador-Geral da República e da Polícia Federal. É a posição que Lula atribui a ele no contexto da fala ("o Banco Central vai investigar tecnicamente [...] foi assim que eu pedi para ele comunicar ao Procurador-Geral da República, foi assim que o Haddad se posicionou"). Com o agradecimento público de Galípolo ao apoio de Haddad (Finsiders, 09/02/2026), são duas fontes. Pergunta 3 e pergunta 6: a mesma régua deu `VERDADEIRO` com ressalva para Galípolo em A102, onde a expressão literal também não aparece.

#### A104 (lote 08), resumo, ressalva, explicação e data de referência

- **Estava:** resumo "As fontes achadas não trazem Haddad dizendo que o caso Master seria tratado de forma técnica"; ressalva nula; data de referência "declarações de 2026".
- **Passou a valer:** resumo "Haddad disse que cabia ao Banco Central agir no caso Master e que o caso foi levado à Procuradoria-Geral e à PF"; ressalva "Haddad fala do dever do Banco Central e do envio à Procuradoria-Geral e à PF; a expressão sem critério político não aparece"; data de referência "entrevista publicada em 6 de junho de 2026; agradecimento de Galípolo em 9 de fevereiro de 2026"; explicação reescrita com o que a entrevista diz, a ressalva da expressão literal e o registro de que, na mesma entrevista, Haddad associou o caso à gestão anterior do BC (avaliação dele, fora do veredito).
- **Por quê:** acompanhar o veredito novo (perguntas 7 e 8).

#### A104 (lote 08), fontes

- **Estava:** Jornal Grande Bahia (Haddad e Dirceu defendem Jaques Wagner, junho de 2026) e Finsiders (Galípolo agradece o apoio de Haddad).
- **Passou a valer:** A Crítica de Campo Grande (captura p07 `2c258b0dcb7e`, trecho com três pedaços marcados por `[...]`) e Finsiders, com a coluna `prova` reescrita ("Em outra ocasião, o presidente do BC registra o apoio de Haddad à atuação do BC no caso"). O Jornal Grande Bahia saiu.
- **Por quê:** a matéria sobre Jaques Wagner trata de outro ponto e não prova nada sobre a alegação (pergunta 3); a fonte que prova estava capturada e não tinha sido usada.

#### A103 (lote 08), explicação e data de referência

- **Estava:** "nenhuma fonte capturada registra pedido de Lula, nem especifica o Procurador-Geral como destinatário"; data de referência "comunicações do BC em 2025".
- **Passou a valer:** a explicação registra que Haddad, na entrevista de junho de 2026 (captura p07), diz que o caso foi levado ao conhecimento do Procurador-Geral da República e da PF, sem dizer por quem nem a pedido de quem; que o BC teve certeza da falta de lastro em 27 de junho de 2025 e comunicou o MPF e a PF em julho (Poder360, captura p09); e que Galípolo, perguntado na CPI se recebeu comando do Planalto depois da reunião com Vorcaro, descreveu a orientação de ser técnico, sem citar pedido para comunicar a PGR. Data de referência: "comunicações ao Ministério Público e à PF entre o fim de 2024 e setembro de 2025". O veredito continua `INSUSTENTAVEL`.
- **Por quê:** a frase "nem especifica o Procurador-Geral como destinatário" ficou errada diante de uma captura que já estava no caso (pergunta 3), e o depoimento de Galípolo à CPI é o registro mais próximo do pedido que Lula descreve e não o menciona.

#### A103 (lote 08), fontes

- **Estava:** Revista Oeste e Finsiders.
- **Passou a valer:** mais duas, Poder360, "Lula disse para eu ser técnico após reunião com Vorcaro, diz Galípolo" (08/04/2026, captura p09 `9da28aea89bf`), e A Crítica de Campo Grande (captura p07 `2c258b0dcb7e`).
- **Por quê:** dar trecho ao que a explicação nova afirma (regra 6 do §3.1).

#### A103 (lote 08), resumo

- **Estava:** "O BC comunicou fatos do Master ao Ministério Público, mas não há registro de que foi a pedido de Lula"
- **Passou a valer:** "O BC comunicou o caso Master ao Ministério Público e à PF; as fontes não registram que foi a pedido de Lula"
- **Por quê:** "não há registro" afirma ausência absoluta numa rodada de busca limitada; o card passa a dizer o que as fontes mostram (perguntas 7 e 8).

#### A099 (lote 08), resumo

- **Estava:** "As fontes consultadas não registram o pedido; a visita de Silvio Santos a Lula em 2010 foi sobre o Teleton"
- **Passou a valer:** "As fontes não registram Silvio Santos procurando Lula no caso PanAmericano; a visita de 2010 foi antes, sobre o Teleton"
- **Por quê:** lido sozinho, o resumo antigo sugeria que a visita citada por Lula tinha sido sobre outra coisa, o que é impressão de `FALSO` num card `INSUSTENTAVEL`. A visita registrada foi em setembro de 2010, antes do rombo de novembro, e o card agora diz isso (pergunta 8).

#### A101 (lote 08), resumo e explicação

- **Estava:** resumo "O banco de Macedo é o Digimais, em crise desde 2024; as fontes não registram pedido dele a Lula"; explicação "Metrópoles e Estadão descrevem a crise do banco desde 2024, com inadimplência, aportes do próprio Macedo e tentativas de venda sob supervisão do BC."
- **Passou a valer:** resumo "O banco de Edir Macedo é o Digimais, com crise apontada em 2024 e 2025; as fontes não registram o banco procurando Lula"; explicação "Metrópoles e Estadão descrevem a crise do banco, com relatórios de 2024 e 2025 apontando inadimplência alta depois da pandemia, aportes do próprio Macedo e o banco à venda há mais de um ano."
- **Por quê:** "desde 2024" não tem lastro: o Metrópoles diz que a situação "não é boa há um bom tempo" e cita relatórios de 2024 e 2025 sobre inadimplência pós-pandemia, e o Estadão fala em "à venda há mais de um ano"; "sob supervisão do BC" não está em trecho nenhum. "pedido dele" era ambíguo entre Macedo e o banco (pergunta 7).

### revisao\correcoes-r5.md

#### Correções da revisão r5 (lotes 10 e 11)

Revisão adversarial por IA, em passada separada, das checagens A118 a A143. Cada entrada abaixo é uma mudança aplicada no arquivo do lote. A busca web estava esgotada nesta rodada; a revisão usou as capturas do caso e uma captura nova, de fonte oficial por URL direta, em `capturas/2026-10-15-sabatina-lula-globo-2turno-rev` (pedido em `checagens/pedidos-captura/pedido-rev-r5.json`).

#### A126 (lote 10): veredito

- **Estava:** `VERDADEIRO`, confiança média, resumo "Levantamento do FGV Ibre: 24,9% se endividaram ou usaram reservas para pagar despesas básicas em setembro de 2026".
- **Passou a valer:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "Os 24,9% do FGV Ibre vêm de uma só reportagem, do Estadão; a pesquisa original não foi capturada". Explicação reescrita no padrão de veredito provisório ("Busca interrompida pelo limite de buscas da rodada de 16/out"), ressalva e `numero_apurado` atribuindo o número ao Estadão.
- **Por quê:** é número, e a METODOLOGIA §3.1 exige fonte N1 ou N2, ou duas N3/N4 que citem a primária já conferida. As cinco páginas capturadas (Estadão, 40graus, SP Diário, Aciara, Blog do Itamar) saíram em 11/10 e quatro reproduzem o Estadão, como a própria checagem já dizia. A divulgação do FGV Ibre não foi capturada, e a tentativa da revisão na página da Sondagem do Consumidor (`portalibre.fgv.br/sondagem-do-consumidor`) teve a conexão recusada. Na mesma rodada, falas do candidato com a fonte primária faltando receberam `INSUSTENTAVEL` provisório (A016, por exemplo); manter `VERDADEIRO` aqui seria régua diferente para a jornalista. Nada contradiz o número, por isso não é `FALSO`.

#### A119 (lote 10): fonte, explicação e ressalva

- **Estava:** a explicação dizia que o IPCA "não é o índice do ato e não foi usado"; ressalva "A reposição vai até agosto de 2026 e usa o INPC; a inflação de setembro em diante fica para a próxima correção."
- **Passou a valer:** fonte nova do IBGE (SIDRA, tabela 1737, IPCA número-índice, capturada na revisão), com derivações de 16,3% (7633,23 / 6563,07) e de 15,2% (alta do piso, 691 / 600). A explicação diz que pelo IPCA a inflação do período foi 16,3% e que, por essa régua, o piso fica pouco abaixo da reposição integral. Ressalva: "A reposição usa o INPC até agosto de 2026; pelo IPCA, a inflação do mesmo período foi de 16,3%."
- **Por quê:** o melhor argumento contra "vai dar tudo o que a gente não deu" é o índice. Conferido, o IPCA do período é maior que o INPC do decreto, e nenhum componente reajustado chega a 16,3%. A diferença (cerca de 1% no valor do piso) fica abaixo da régua de 10% do §2.2, então o veredito fica, mas o espectador precisa ver a ressalva.

#### A122 (lote 10): resumo e fonte

- **Estava:** resumo "Governo diz que o reajuste cabe remanejando gastos; a IFI vê pressão e o MP no TCU questionou a previsão orçamentária"; os custos de R$ 5,8 bilhões e R$ 22 bilhões da explicação não estavam em trecho nenhum.
- **Passou a valer:** resumo "Governo diz que o reajuste cabe remanejando gastos; a instituição fiscal do Senado contesta e o TCU não decidiu"; o trecho do Poder360 passou a incluir a frase capturada com os dois custos.
- **Por quê:** no mesmo bloco, "MP" é medida provisória (A132 a A139), e "MP no TCU" se lê errado em cinco segundos; "IFI" é sigla de especialista (escrita-de-card §1). O card de `INSUSTENTAVEL` precisa mostrar o que ficou em aberto, e a decisão pendente do TCU faz isso. Número da explicação sem trecho fere a regra 6 da §3.1.

#### A129 (lote 10): explicação

- **Estava:** "O logo depois é impreciso para a primeira fase: a alta começou cerca de sete meses depois do fim", com veredito `VERDADEIRO`.
- **Passou a valer:** a explicação diz que o tempo vai na ressalva, que na segunda fase o índice subiu durante o programa, que a série capturada ainda não mostra o mês seguinte ao fim da segunda fase, e por que a distância no tempo não rebaixa o veredito.
- **Por quê:** a palavra "impreciso" com veredito `VERDADEIRO` era contradição interna do card, e a explicação deixava de dizer que o "depois" da segunda fase ainda não é observável.

#### A139 (lote 11): resumo e explicação

- **Estava:** resumo "O custo de até R$ 15 bilhões entra como despesa primária, compensada com corte em outras áreas"; explicação afirmava "o programa não amplia o teto nem fura a regra fiscal" e "a regra fiscal é cumprida".
- **Passou a valer:** resumo "O custo de até R$ 15 bilhões é despesa do orçamento, que o governo diz compensar com corte em outras áreas"; a explicação atribui a compensação ao governo, diz que ela é anunciada para o orçamento do ano que vem e ainda não está em documento capturado, e o fecho passa a "o programa não amplia o limite de despesas, mas usa o espaço dentro dele".
- **Por quê:** a compensação é plano anunciado pelo ministro, não fato registrado; o texto a dava como cumprida. É a mesma cautela aplicada ao A122, onde a palavra do governo sobre espaço fiscal não bastou.

#### A135 (lote 11): resumo, explicação e número apurado

- **Estava:** "O governo estima até R$ 150 bilhões em dívidas elegíveis [...]".
- **Passou a valer:** resumo "O governo estima comprar até R$ 150 bilhões em dívidas, gastando até R$ 15 bilhões com deságio mínimo de 90%"; explicação e `numero_apurado` com as palavras da fonte ("possam ser renegociados pelas regras do programa").
- **Por quê:** as fontes dão a capacidade de compra (R$ 15 bilhões a 10% do valor de face), não o estoque de dívidas elegíveis, que nenhuma fonte capturada mede. "Elegíveis" afirmava no card o que não foi conferido.

#### A125 (lote 10): resumo

- **Estava:** "A IFI projeta receita líquida R$ 127,9 bi menor que a do projeto de 2027 e déficit de R$ 86,1 bi, não superávit".
- **Passou a valer:** "A instituição fiscal do Senado projeta receita R$ 127,9 bi menor que a do projeto de 2027 e déficit de R$ 86,1 bi".
- **Por quê:** sigla de especialista sem o nome por extenso (escrita-de-card §1). O veredito não muda.

#### A138 (lote 11): resumo

- **Estava:** "A PGFN pode comunicar a dívida ativa a cadastros de crédito como a Serasa, o que dificulta obter crédito".
- **Passou a valer:** "A Procuradoria da Fazenda pode comunicar a dívida ativa a cadastros como a Serasa, o que dificulta obter crédito".
- **Por quê:** sigla de especialista sem o nome por extenso. O veredito não muda.

#### A118 (lote 10): fonte

- **Estava:** o trecho da Lei 14.601 trazia só R$ 142 e R$ 600, e a explicação citava também R$ 150 e R$ 50.
- **Passou a valer:** o trecho inclui os incisos III e IV, com R$ 150,00 e R$ 50,00, conferidos na mesma página capturada.
- **Por quê:** regra 6 da §3.1: número escrito precisa estar num trecho.

#### A123 (lote 10): fonte

- **Estava:** a explicação citava o déficit de R$ 86,1 bilhões projetado pela IFI, sem trecho na checagem.
- **Passou a valer:** o trecho do RAF 116 inclui a frase com os R$ 86,1 bilhões, conferida no PDF capturado.
- **Por quê:** regra 6 da §3.1.

#### A137 (lote 11): derivação

- **Estava:** a explicação dizia que o valor falado fica "a 1,2% do valor do documento oficial", sem a conta declarada.
- **Passou a valer:** derivação declarada, (12,86 menos 12,7) dividido por 12,86.
- **Por quê:** número derivado só entra com a conta escrita (§3.1, regra 6).

### revisao\correcoes-r6.md

#### Correções da revisão r6 (lotes 12 e 13)

Revisão adversarial por IA, em passada separada, das checagens A144 a A169. Cada entrada abaixo é uma mudança aplicada no arquivo do lote. A busca web estava esgotada nesta rodada; a revisão usou as capturas do caso e três capturas novas, de fonte oficial por URL direta, em `capturas/2026-10-15-sabatina-lula-globo-2turno-rev` (pedido em `checagens/pedidos-captura/pedido-rev-r6.json`): a posição do Brasil no FMI em 30/11/2003, o relatório da FAO de 2014 (The State of Food Insecurity in the World 2014) e a série do Banco Mundial de renováveis no consumo final de energia, todos os países, 2020.

#### A154 (lote 12): veredito

- **Estava:** `VERDADEIRO`, ressalva "A alta apurada até agosto de 2026 foi de 11,19 pontos; até junho, era de 10,2". A explicação tratava o desvio como "cerca de 10%, no limite da régua".
- **Passou a valer:** `IMPRECISO`. Ressalva "A diferença é para menos: a alta apurada é maior que a dita; até junho, era de 10,2 pontos". Explicação reescrita com o desvio medido (10,6%) e derivação nova (`82.87 menos 71.68 menos 10, dividido por 82.87 menos 71.68`).
- **Por quê:** os 10 pontos ditos pela entrevistadora ficam 1,19 abaixo da alta apurada de 11,19, desvio de 10,6% sobre o valor apurado, que é a base da conta do §2.2 (o exemplo "94 contra 92,4"). A régua diz "desvio ≥ 10% no valor: IMPRECISO" e não distingue o sentido: foi o critério aplicado ao "um trilhão de reais" de Flávio Bolsonaro em 28/ago (A007 daquele caso, 14% para menos, `IMPRECISO` depois de revisão) e, neste caso, ao "dobro da inflação" da mesma entrevistadora (A166) e às posições de ranking do candidato (A144, A151). Manter `VERDADEIRO` a 10,6% seria régua mais frouxa para um dos lados da mesa.

#### A156 (lote 12): veredito

- **Estava:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "As fontes capturadas citam Lurian e Marcos Cláudio como filhos de Lula, mas nenhuma diz quantos filhos ele tem". A explicação dizia que a biografia oficial da Presidência "conta a família de origem dele [...] mas não fala dos filhos".
- **Passou a valer:** `VERDADEIRO`, confiança média, resumo "A biografia oficial da Presidência diz que Lula tem cinco filhos, quatro deles com Marisa Letícia". O trecho da fonte N1 passou a ser a frase da própria biografia: "Marisa Letícia Lula da Silva, mãe de quatro dos seus cinco filhos". `numero_apurado` e `data_de_referencia` reescritos; as duas reportagens do Poder360 ficam como apoio.
- **Por quê:** a frase com o total está na página já capturada (`capturas/...-p12/texto/06c2b86c5a3b.txt`, a mesma URL que a checagem citava). A leitura de que a biografia não falava dos filhos estava errada. Confiança média porque só a fonte oficial dá a soma; as reportagens confirmam filhos nomeados.

#### A153 (lote 12): veredito

- **Estava:** `VERDADEIRO`, confiança média, resumo "Fraga, Malan e Bacha, que votaram em Lula, escreveram que os pobres sofrem mais se o governo perde crédito fiscal".
- **Passou a valer:** `INSUSTENTAVEL` provisório, confiança baixa, resumo "A crítica de Fraga, Malan e Bacha, que votaram em Lula, só aparece no Poder360; a carta original não foi capturada". Explicação no padrão de veredito provisório. Ressalva mantida.
- **Por quê:** as quatro fontes são N4 do mesmo veículo, e a carta (publicada na Folha de S.Paulo), que é a primária, não foi capturada. A METODOLOGIA §3.1, regra 2, só aceita N3/N4 quando citam a primária e ela foi conferida. Neste caso a mesma falta levou a `INSUSTENTAVEL` provisório falas do candidato (A016) e outro número da entrevistadora (A126, na revisão r5); manter `VERDADEIRO` aqui seria régua diferente. Nada contradiz a pergunta, por isso não é `FALSO`. Para virar `VERDADEIRO` falta capturar a carta e uma segunda redação.

#### A145 (lote 12): resumo, fonte e explicação

- **Estava:** resumo "Na posse, o Brasil devia ao FMI 15,3 bilhões de DES; a dívida só passou de US$ 30 bi em 2003, com pico de US$ 33,7 bi". O saldo de 2003 só tinha a reportagem de 2005 como fonte.
- **Passou a valer:** resumo "Na posse, o Brasil devia ao FMI cerca de US$ 20 bi; a dívida só passou de US$ 30 bi em 2003, com pico de US$ 33,7 bi" (o valor em dólar já era derivação declarada). Fonte nova N2: posição do Brasil no FMI em 30/11/2003 (saldo de 23.358,59 milhões de DES; 17.199,64 milhões sacados do acordo de 2002). A explicação cita essa posição.
- **Por quê:** lido em cinco segundos, o card punha "15,3 bilhões de DES" ao lado de "30 bilhões de dólares", e quem não sabe o que é DES compara os dois números e vê a fala com o dobro do valor; em dólar o saldo da posse é cerca de US$ 20 bilhões. O veredito não muda.

#### A149 (lote 12): fonte, explicação e derivação

- **Estava:** o pico de US$ 33,7 bilhões vinha só da reportagem de 2005 (N4), e a explicação dizia que os 30 bilhões ficam entre o pago em 2005 e o pico.
- **Passou a valer:** fonte nova N2 (posição do Brasil no FMI em 30/11/2003, 23.358,59 milhões de DES) e derivação "cerca de US$ 30,7 bilhões" (`23,358.59 vezes 30 dividido por 22,821.12`, pela equivalência da carta de intenção de 2002). A explicação diz que o acordo de 2002 estava em grande parte sacado (17.199,64 de 22.821,12 milhões de DES).
- **Por quê:** o melhor argumento contra o `VERDADEIRO` é que o pico de US$ 33,7 bilhões fica 11% acima dos 30 ditos. A fonte primária mostra que, pela mesma equivalência que a fala e o acordo usavam, o saldo no pico era de cerca de US$ 30,7 bilhões, e que a dívida quitada era em grande parte o próprio acordo de 30 bilhões. O veredito fica de pé, agora com a primária.

#### A148 (lote 12): explicação

- **Estava:** "estoque final (US$ 288,6 bilhões, 6% acima) e o acréscimo do período (US$ 250,8 bilhões, 7% abaixo)".
- **Passou a valer:** "do qual o dito fica 6,4% abaixo" e "do qual o dito fica 7,7% acima", medidos sobre o valor apurado.
- **Por quê:** os dois desvios estavam calculados com bases diferentes (um sobre o apurado, outro sobre o dito). Medidos como manda o §2.2, ficam em 6,4% e 7,7%, ainda abaixo de 10%. O veredito não muda.

#### A158 (lote 13): resumo

- **Estava:** "Os verbetes do CPDOC registram divergência entre Mantega e Meirelles, não brigas de Lula com os dois".
- **Passou a valer:** "Nenhuma fonte achada registra brigas de Lula com Mantega e Meirelles; o CPDOC registra divergência entre os dois".
- **Por quê:** lido sozinho, "não brigas de Lula com os dois" soa como se a fonte dissesse que as brigas não aconteceram. O verbete biográfico só não as registra. O card de `INSUSTENTAVEL` tem que dizer o que faltou, não sugerir desmentido.

#### A159 (lote 13): fontes e explicação

- **Estava:** só três reportagens (N4), sem a fonte primária, e a explicação dizia que "as fontes capturadas não dizem quem governava em 2014, então a atribuição pessoal ('eu tinha acabado') não foi conferida".
- **Passou a valer:** duas fontes novas. N2: o relatório da FAO de 2014, capturado na revisão, que registra a queda da subalimentação no Brasil de 10,7% em 2000-02 para abaixo de 5% em 2004-06, com o Fome Zero lançado em 2003. N1: a biografia oficial da Presidência (já capturada), que registra Dilma Rousseff no cargo desde 2011 e reeleita em 2014. A explicação diz que em 2014 governava Dilma, mas que a queda que levou o país abaixo do limite aconteceu no primeiro mandato de Lula.
- **Por quê:** o melhor argumento contra o veredito era a régua do §2.2 para "atribui a um governo o que aconteceu em outro", porque em 2014 Lula não era presidente. A fonte primária derruba esse argumento: a queda medida pela FAO é de 2000-02 a 2004-06. E, pela regra 2 da §3.1, três reportagens sem a primária conferida não bastavam. O veredito fica.

#### A161 (lote 13): resumo, fonte e explicação

- **Estava:** resumo "O plano de Flávio não muda a regra do mínimo, e não se achou anúncio dele de reajuste só pela inflação"; o trecho do Imirante começava por "O plano de governo não apresenta mudanças no cálculo dos benefícios previdenciários ou do salário mínimo."
- **Passou a valer:** resumo "Não se achou anúncio de Flávio de reajuste do mínimo só pela inflação; o plano dele não fixa meta para o piso". O trecho do Imirante passou a ser a parte da reportagem sobre Flávio (o cabeçalho da seção e a pergunta da Globo sobre a vinculação, que ficou sem resposta). Explicação corrigida.
- **Por quê:** na página capturada, a frase "O plano de governo não apresenta mudanças no cálculo [...] do salário mínimo" é a última da seção sobre o plano de **Lula**, logo antes do cabeçalho "Flávio Bolsonaro". Ela foi atribuída ao plano errado. O que as fontes dizem do plano de Flávio é que não fixa meta para o piso (NSC Total). O veredito `INSUSTENTAVEL` provisório não muda.

#### A167 (lote 13): ressalva, fonte, explicação e derivação

- **Estava:** ressalva "Acima de 80 kWh o desconto passou a zero; antes havia 40% de 31 a 100 kWh"; o trecho da Lei 12.212 trazia só as duas primeiras faixas.
- **Passou a valer:** ressalva "Em kWh gratuitos, o desconto máximo passou de 59,5 para 80, e acima de 80 kWh não há mais desconto". O trecho da Lei 12.212 inclui a terceira faixa (10% de 101 a 220 kWh), e a derivação nova declara a conta (`30 vezes 65% mais (100 menos 30) vezes 40% mais (220 menos 100) vezes 10%`). A explicação diz que o desconto total cresceu em qualquer faixa de consumo.
- **Por quê:** a ressalva antiga, lida sozinha, sugeria perda para quem consome mais de 80 kWh. Somadas as faixas antigas, o desconto máximo equivalia a 59,5 kWh gratuitos, contra 80 na regra nova, então ninguém na Tarifa Social perdeu desconto total. O veredito não muda.

#### A168 (lote 13): fonte e explicação

- **Estava:** a terceira fonte era o trecho da Lei 15.235 sobre o desconto de 100% até 80 kWh de **famílias indígenas e quilombolas** custeado pela CDE, e a explicação dizia "A lei custeia pela CDE o desconto de 100% até 80 kWh", como se fosse o desconto geral.
- **Passou a valer:** a terceira fonte passou a ser o art. 11-A que a Lei 15.235 acrescentou à Lei 12.111: o rateio do custo de Angra 1 e Angra 2 entre os consumidores, exceto a Subclasse Residencial Baixa Renda. A explicação diz que a lei manteve o rateio da MP 1.300 e que quem custeia o desconto geral não foi conferido.
- **Por quê:** o trecho antigo não provava o que a coluna `prova` dizia (pergunta 3 do roteiro). E o resumo diz "a lei passa custos a quem está fora da baixa renda", o que só a MP sustentava; conferido na lei de conversão, o rateio continua. O veredito não muda.

### revisao\correcoes-r7.md

#### Correções da revisão r7 (lotes 14 e 15)

Revisão adversarial por IA, passada separada, em 16/out/2026. Nenhum veredito mudou nesta rodada; as mudanças são de resumo, explicação, ressalva, data de referência e fontes. Todo trecho novo ou alterado foi conferido contra o texto capturado (`capturas/2026-10-15-sabatina-lula-globo-2turno-p01`, `-p14` e `-p15`) e encontrado. Nenhuma busca web foi feita.

#### A172 (Lula, mercado livre de energia)

- **Campo:** `resumo`
- **Estava:** "Até a reforma de 2025, residências não podiam ir ao mercado livre, restrito a grandes consumidores"
- **Passou a valer:** "Mercado livre, apontado como mais barato, era restrito a grandes consumidores; residências ainda não podem migrar"
- **Por quê:** "até a reforma de 2025, não podiam" dá a entender que depois da reforma as residências já podiam migrar. Na data da fala elas ainda não podiam: a Lei 15.269 dá até 36 meses (o próprio caso registra isso na A173). O card lido sozinho deixava a impressão errada (pergunta 8). O resumo novo também traz a parte de preço que a fala afirma, com lastro no Times Brasil e no Cenário Energia.

#### A175 (Renata Lo Prete, programa ampliou o atendimento)

- **Campos:** `resumo`, `numero_apurado`, `data_de_referencia` e um trecho da `explicacao`
- **Estava:** resumo "Cirurgias eletivas no SUS foram de 10,8 milhões em 2022 a 14,7 milhões em 2025, e o programa tem parte disso"; número apurado "cirurgias eletivas: 10,8 milhões (2022) para 14,7 milhões (2025)"; data "2022 a 2025; primeiro semestre de 2026"; explicação "No primeiro semestre de 2026, 2,92 milhões de cirurgias..."
- **Passou a valer:** resumo "Cirurgias eletivas no SUS cresceram 42% de 2022 a 2025, e o TCU vê ajuda do programa nessa alta"; número apurado "cirurgias eletivas: 14,9 milhões em 2025, 42% acima de 2022 (balanço do Ministério da Saúde)"; data "2022 a 2025; até julho de 2026"; explicação passa a dar 14,9 milhões e 42% (Diário do Pará) e cita os 14,7 milhões como a primeira divulgação, e "até julho de 2026" no lugar de "no primeiro semestre"
- **Por quê:** os 14,7 milhões são a divulgação de fevereiro; o balanço mais recente antes da fala, já usado na A188 deste mesmo caso, é 14,9 milhões (pergunta 5). Do jeito que estava, dois cards do mesmo vídeo mostrariam números diferentes para 2025. E o trecho da TVT diz "realizadas até julho", não "primeiro semestre".

#### A176 (Renata Lo Prete, a espera não diminuiu significativamente)

- **Campos:** `resumo`, `explicacao`, `divergencia_entre_fontes` e uma fonte nova
- **Estava:** resumo "Não há série nacional de espera; o TCU viu a mediana cair na maioria das cirurgias e um quarto esperar mais"; explicação chamava o achado do TCU de "ambíguo" só pela leitura do Futuro da Saúde; o acórdão, capturado no caso, não era fonte
- **Passou a valer:** resumo "Sem série nacional; TCU vê mediana menor na maioria das cirurgias, um quarto esperando mais e baixa efetividade"; a explicação e a divergência passam a citar a ementa do Acórdão 1622/2026 ("baixa efetividade na redução do tempo de espera") ao lado do achado de mediana em queda; entra como primeira fonte o relatório do acórdão (N1), com os dois lados no trecho
- **Por quê:** a fonte primária estava capturada e não era citada; o achado do TCU chegava só por uma leitura de imprensa (§3.1, regra 2). E o card só trazia o lado que contraria a jornalista: a ementa do mesmo documento vai na direção da pergunta. Com os dois lados, o veredito INSUSTENTAVEL fica de pé (pergunta 6, mesma régua para a mesa) e o card deixa de puxar para um lado só (pergunta 8).

#### A180 (Lula, 16 mil médicos contratados)

- **Campos:** `resumo`, `explicacao`, `data_de_referencia` e o trecho e a prova da fonte Mais Goiás
- **Estava:** resumo "O último dado achado, de junho de 2024, soma 12.051 médicos a mais que em 2022; o de 2026 não foi localizado"; explicação "O dado mais recente capturado é de junho de 2024 [...] com meta de 28 mil"; data "dezembro de 2022 a junho de 2024 (dado de 2026 não localizado)"; trecho do Mais Goiás só com "cerca de 24,9 mil médicos atuando"
- **Passou a valer:** resumo "Em junho de 2024 havia 12.051 médicos a mais que em 2022, e 24,9 mil em maio de 2025; falta o dado de 2026"; explicação diz que o dado mais recente capturado é o da Agência Brasil de maio de 2025; data "dezembro de 2022 a maio de 2025 (dado de 2026 não localizado)"; o trecho do Mais Goiás ganha a data de publicação (22/05/2025) e a meta de 28 mil
- **Por quê:** a reportagem do Mais Goiás (Agência Brasil), já capturada e citada, é de 22/05/2025, então o "último dado achado" não era o de junho de 2024 (perguntas 3 e 5). A meta de 28 mil estava na explicação sem trecho que a sustentasse (§3.1, regra 6). O veredito não muda: ainda não há dado de 2026.

#### A183 (Lula, Farmácia Popular voltar a funcionar)

- **Campos:** `resumo`, `explicacao`, `ressalva`, `data_de_referencia` e duas fontes novas
- **Estava:** resumo "O programa funcionava em 2022, com R$ 2,5 bi, mas passou quase uma década sem credenciar farmácia nova"; ressalva "Os valores de orçamento são nominais e vêm do próprio Ministério da Saúde"; data "2022 (orçamento e situação do programa antes de 2023)"; explicação com o limite declarado de que as três fontes eram comunicados do próprio Ministério da Saúde, sem fonte independente
- **Passou a valer:** resumo "O programa funcionava em 2022, mas estava sem credenciar farmácia nova e o orçamento de 2023 previa corte de 59%"; ressalva "O corte de 59% estava na proposta de orçamento de 2023, não no gasto de 2022"; data "2022 (situação do programa e proposta de orçamento de 2023, de agosto de 2022)"; entram Aos Fatos (N3, corte de 59% no PLOA 2023) e Rádio Senado (relator do orçamento, novembro de 2022: o programa corria risco de parar sem a PEC da Transição), ambas já capturadas na rodada p01 do caso
- **Por quê:** com as três fontes de mesma origem, o veredito não cumpria a independência da §3.1 (regras 1 e 3) e, pela árvore do §2.1, cairia para INSUSTENTAVEL. As duas fontes novas são independentes do Ministério e sustentam a essência que o IMPRECISO afirma (programa funcionando, enfraquecido e sob risco de parar), então o veredito fica, agora com lastro. O resumo passa a mostrar o fato mais próximo do "voltar a funcionar": o corte proposto para o ano em que ele assumiu.

#### A184 (Renata Lo Prete, o Mais Especialistas ampliou o atendimento)

- **Campo:** `resumo`
- **Estava:** "O TCU confirma que o financiamento do programa ajudou a aumentar as cirurgias, em parte pela volta pós-pandemia"
- **Passou a valer:** "O TCU diz que o programa ajudou a aumentar as cirurgias, mas boa parte da alta é recuperação pós-pandemia"
- **Por quê:** o TCU escreve "boa parte desse crescimento reflete a recuperação do SUS após a pandemia"; "em parte" encolhia a ressalva do próprio auditor, e a construção dava a entender que a ajuda do programa vinha da volta pós-pandemia (perguntas 7 e 8).

#### A186 (Lula, hospitais pagando dívida com atendimento ao SUS)

- **Campo:** trecho da fonte Planalto (Lei 15.233/2025)
- **Estava:** trecho sem o § 1º e o § 2º do art. 4º
- **Passou a valer:** o trecho ganha "§ 1º A partir do exercício de 2026, para fruição dos créditos financeiros [...]" e "§ 2º Os créditos financeiros [...] serão limitados anualmente ao valor de R$ 2.000.000.000,00 (dois bilhões de reais)", conferidos na captura p15
- **Por quê:** a explicação cita "a partir de 2026" e o "teto anual de R$ 2 bilhões" sem trecho que os contivesse (§3.1, regra 6). O veredito não muda.

#### A187 (Lula, convênio com todas as Santas Casas)

- **Campo:** `resumo`
- **Estava:** "A adesão das Santas Casas ao programa é voluntária e não há registro de convênio com todas elas"
- **Passou a valer:** "A adesão das Santas Casas ao programa é voluntária, e não foi achado convênio com todas elas"
- **Por quê:** a busca foi interrompida pelo limite e a própria explicação diz que um acordo com a CMB não pôde ser procurado a fundo. "Não há registro" afirma uma ausência que a busca não provou; "não foi achado" é o que a checagem sustenta, e segue o padrão dos outros cards provisórios do caso (A174, A182).

### revisao\correcoes-r8.md

#### Correções da revisão r8 (lote 03, A027 a A039)

Revisão adversarial por IA, passada separada, em 16/out/2026. Nenhum veredito mudou nesta rodada. As mudanças são de resumo, explicação, ressalva, data de referência, derivações e fontes. Todo trecho novo ou alterado foi conferido contra o texto capturado e encontrado. Nenhuma busca web foi feita.

🆕 **Captura nova da revisão** (`capturas/2026-10-15-sabatina-lula-globo-2turno-rev`, caminho `api-post`): duas consultas POST à API pública do Comex Stat com outubro a dezembro de 2024 e de 2025 para os cinco países da fala (exportação `80fc9bb8be26`, importação `bc559f37e260`). Junto com as consultas de janeiro a setembro da rodada p03 (`14f263ecc686` e `b962fcafb544`), elas dão os 12 meses até setembro. É a mesma base do MDIC, e por isso **não** conta como a segunda fonte independente que falta em A037 a A039.

#### A027 (Renata Lo Prete, clara preferência do governo americano)

- **Campos:** `resumo`, `explicacao`, trechos e prova das três fontes, título da Folha de Pernambuco
- **Estava:** resumo "Trump elogiou a votação de Flávio, mas não declarou apoio; fonte do governo dos EUA nega preferência eleitoral"; a fonte do Estadão (via Folha de Pernambuco) sem data no título e com o trecho só da parte que nega preferência
- **Passou a valer:** resumo "Trump elogiou a votação de Flávio e o recebeu na Casa Branca, mas nem ele nem o governo dos EUA declararam apoio"; a Folha de Pernambuco ganha a data de publicação (03/06/2026, lida no `datePublished` da página capturada) e o trecho passa a trazer os dois lados da mesma fonte (o entorno de Trump vê Flávio como "aliado natural", o encontro na Casa Branca, e a frase de que as reuniões não refletem preferência eleitoral); o BP Money ganha o trecho em que o governo americano "evita anunciar apoio oficial a um dos candidatos"; a AFP ganha o trecho das tarifas e sanções após a condenação de Jair Bolsonaro, que a explicação já citava sem lastro
- **Por quê:** o resumo punha na tela, como contraprova da pergunta, a fala de uma fonte anônima publicada quatro meses antes da sabatina, e cortava a parte da mesma fonte que vai na direção da jornalista (pergunta 8, e mesma régua para a mesa: o card puxava para um lado). O fato que as fontes sustentam é a ausência de apoio declarado, de Trump e do governo americano, e é ele que o resumo passa a dizer. "Tarifas e sanções" estava na explicação sem trecho (pergunta 7). O veredito `INSUSTENTAVEL` fica: há sinais nas duas direções e falta a manifestação que a frase afirma.

#### A029 (Lula, nunca procurou os partidos)

- **Campos:** `resumo`, `explicacao`, trecho e prova da fonte Poder360 sobre a reunião
- **Estava:** resumo "Lula convocou senadores do MDB ao Alvorada em 14 de outubro; não há registro do que foi pedido na reunião"; explicação dizia que os senadores eram "os mesmos que declararam apoio a ele no 2º turno"
- **Passou a valer:** resumo "Lula reuniu senadores do MDB em 14 de outubro, durante a votação do fim da escala 6 X 1; não foi achado o que se tratou"; explicação diz que a reunião foi durante a votação da PEC e que, naquele momento, 10 dos 27 diretórios apoiavam Lula e 17 Flávio; o trecho passa a incluir a frase sobre o Alvorada e a votação da PEC
- **Por quê:** a reportagem não diz que os senadores convocados são os mesmos que declararam apoio a Lula (pergunta 3 e 7); diz que o encontro aconteceu durante a votação da PEC do fim da escala 6 X 1, contexto que o card omitia e que muda a leitura em cinco segundos (pergunta 8). "Não há registro" afirma uma ausência que a busca interrompida não provou; "não foi achado" é o padrão dos cards provisórios do caso (r7, A174 e A182). Veredito provisório mantido.

#### A031 (Lula, as duas maiores democracias do Ocidente)

- **Campos:** `ressalva`, `explicacao`
- **Estava:** ressalva "Vale tomando Ocidente como Américas e Europa; o México, terceiro mais populoso, é parcialmente livre."; explicação apresentava a classificação do México como parte do argumento
- **Passou a valer:** ressalva "Vale tomando Ocidente como Américas e Europa e democracia como país livre pela Freedom House."; a explicação diz que o resultado não depende da classificação do México, que fica atrás do Brasil de qualquer forma
- **Por quê:** para Brasil e EUA serem as duas maiores democracias basta que os dois sejam democracias e que nenhum outro país do recorte tenha mais gente que o Brasil. O México, com 131 milhões, fica atrás do Brasil livre ou não. A ressalva dava a entender que o veredito dependia do México ser "parcialmente livre" (pergunta 8). As condições que de fato sustentam o veredito são a definição de Ocidente e a de democracia, e é isso que a ressalva passa a dizer.

#### A035 (Lula, perdemos 9% com os Estados Unidos)

- **Campos:** `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas
- **Estava:** "os 9% ficam 38% acima da medida mais desfavorável dos dois recortes"; e "Num recorte de 12 meses até setembro, consultado na série mensal do Comex Stat mas não capturado nesta rodada, a queda das exportações passa de 9% e a da corrente de comércio fica abaixo"
- **Passou a valer:** "os 9% ficam 38% acima da queda das exportações e 32% acima da queda da corrente de comércio"; e "Em 12 meses até setembro [...] as exportações caem 11,4% e a corrente de comércio 7,2%; nenhum dos quatro recortes fica a menos de 10% dos 9% ditos", com as derivações de 32%, −11,4% e −7,2% declaradas e as duas capturas de outubro a dezembro como fontes
- **Por quê:** os 38% são medidos contra a queda das exportações (6,5%), que é a **menor** das duas, e não a "mais desfavorável" (a corrente caiu 6,8%) (pergunta 7). O recorte de 12 meses era afirmado sem captura (§3.1, regra 6); a revisão capturou e conferiu: 9 contra 11,4 é desvio de 21%, contra 7,2 é de 25%. A pergunta adversarial (o candidato pode ter usado outro recorte?) fica respondida com número, e o `IMPRECISO` se sustenta em todos.

#### A036 (Lula, crescemos 20% com a China)

- **Campos:** `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas
- **Estava:** só o acumulado de janeiro a setembro (12,0% nas exportações, 11,1% na corrente)
- **Passou a valer:** a explicação acrescenta os 12 meses até setembro (16,6% nas exportações, 12,8% na corrente), com derivações e fontes, e diz que os 20% ficam acima de todas as medidas por mais que a margem
- **Por quê:** a mesma pergunta feita em A035 tem que ser feita aqui (pergunta 6, régua igual na mesma resposta). 20 contra 16,6 é desvio de 20%, então o veredito `IMPRECISO` não muda.

#### A037, A038 e A039 (Lula, Indonésia 15%, Alemanha 16%, Vietnã 13%)

- **Campos:** `resumo`, `explicacao`, `derivacoes`, `data_de_referencia`, duas fontes novas em cada
- **Estava:** resumo "No Comex Stat, as exportações à Indonésia [Alemanha, Vietnã] subiram 2,2% [15,8%, 14,1%] até setembro; falta segunda fonte"
- **Passou a valer:**
  - A037: "Pelo Ministério do Desenvolvimento, a exportação à Indonésia subiu 2,2% até setembro, longe do dito; sem segunda fonte"
  - A038: "Pelo Ministério do Desenvolvimento, a exportação à Alemanha subiu 15,8% até setembro, perto do dito; sem segunda fonte"
  - A039: "Pelo Ministério do Desenvolvimento, a exportação ao Vietnã subiu 14,1% até setembro, perto do dito; sem segunda fonte"
  - nas três, a explicação ganha os 12 meses até setembro (Indonésia 0,8% e 2,0%; Alemanha 15,9% e 8,5%; Vietnã 5,5% e 11,9%, exportação e corrente), com derivações e fontes
- **Por quê:** "Comex Stat" é nome de sistema, e a regra de escrita de card pede o nome que o espectador reconhece (escrita-de-card §3). Em A038 e A039 o card é laranja, mas a base oficial dá número perto do dito; sem dizer isso, o card lido sozinho sugeria que o dado contraria a fala (pergunta 8). "Perto do dito" e "longe do dito" deixam a leitura certa sem antecipar o veredito. Os 12 meses respondem, para os três, a mesma pergunta de recorte feita em A035 e A036. O veredito `INSUSTENTAVEL` provisório fica nos três: a captura nova é da mesma base, e a §2.1 e a §3.1 pedem duas fontes independentes, que continuam faltando.

### revisao\correcoes-rodada2.md

#### Correções da revisão adversarial da rodada 2

Revisão adversarial por IA, passada separada, em 16/out/2026, sobre as 34 checagens refeitas na rodada 2 com a busca web de volta. O revisor não checou nenhuma delas. Foram feitas 9 buscas web, todas atrás do que contradiria um veredito. Dois vereditos mudaram (os dois FALSO viraram INSUSTENTAVEL) e uma explicação foi corrigida sem mudar o veredito. As mudanças foram aplicadas em `checagens-sabatina-completa.json` e nos lotes 13, 14 e 15.

🆕 **Captura nova da revisão** (`capturas/2026-10-15-sabatina-lula-globo-2turno-rv2`, pedido em `checagens/pedidos-captura/revisao-rodada2.json`): Poder360 de 08/05/2023 com as declarações da ministra e do secretário da Saúde sobre o Brasil Sorridente (`7776d3215cde`) e Correio Braziliense de 22/04/2026 sobre o estudo da equipe econômica de Flávio Bolsonaro (`e0f4f07ca12e`, a mesma página já estava na captura p13). Os dois trechos novos foram conferidos contra o texto capturado e encontrados. ⚠️ O `CAPTURAS.json` do caso não foi regerado nesta revisão: falta rodar `conferir-trechos.py` incluindo a pasta `-rv2`.

#### A161 (Lula, o adversário anuncia que não tem aumento do mínimo acima da inflação)

- **Campos:** `veredito`, `resumo`, `ressalva`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Correio Braziliense, 22/04/2026)
- **Estava:** `FALSO`; resumo "Flávio disse que manterá o reajuste do mínimo e prometeu aumento real a aposentados; não há anúncio do contrário"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Não foi achado anúncio de Flávio contra aumento real do mínimo; jornais relataram estudo da equipe sobre benefícios"; ressalva "Segundo jornais, a equipe estudou corrigir aposentadorias e BPC só pela inflação, não o piso; o candidato nega"
- **Por quê:** FALSO exige que as fontes contradigam o essencial (METODOLOGIA §2). O que estava contra a fala eram declarações e promessas de campanha do próprio candidato, que negam um estudo, mas não são registro de que o estudo não houve. A busca da revisão achou o Correio Braziliense de abril de 2026: a equipe econômica estudava "mudanças na política de valorização do salário mínimo" para que aposentadorias e BPC passassem a ter "apenas reposição inflacionária", num plano "ainda não oficialmente apresentado". Isso dá base parcial à fala (há plano relatado que tira o ganho real de quem recebe benefício atrelado ao mínimo), embora não haja anúncio e o piso dos trabalhadores fique com ganho real. Lido sozinho, o card FALSO deixava a impressão de que a fala não tinha base nenhuma (pergunta 8). Régua igual (pergunta 6): na A029, relato de bastidor negado pelo partido também não fechou FALSO contra Lula.

#### A182 (Lula, fazer o Brasil Sorridente voltar a funcionar)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Poder360, 08/05/2023)
- **Estava:** `FALSO`; resumo "O programa estava em 5,2 mil municípios no relançamento, e as equipes cresceram desde 2019; não tinha parado"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "O programa estava em 5,2 mil municípios em 2023; o governo diz que o credenciamento de equipes estava parado"; ressalva "A paralisação do credenciamento é relato do próprio governo; a série oficial de equipes e de gastos não foi achada"
- **Por quê:** o FALSO se apoiava numa conta de equipes montada com duas fontes de imprensa (26.807 em 2019 e "mais de 33 mil" menos 3.685 em 2023), sem a série oficial, e a própria checagem tinha a leitura branda da alegação ("estava reduzido") e confiança média. A busca da revisão achou o Poder360 de 08/05/2023 com a ministra da Saúde dizendo que o programa "ficou estagnada nos últimos 4 anos" e que o governo anterior "represou o credenciamento de equipes", e o secretário dizendo que encontrou "mais de 3.500 equipes represadas" e que o credenciamento, que libera o repasse, "ficou paralisado". É relato do governo que faz a afirmação e não confirma a fala sozinho, mas tira a contradição direta: a leitura literal (o programa tinha parado) é contradita pelos 5,2 mil municípios; a leitura que o contexto sustenta (estava travado) tem registro a favor e uma conta contra. Sem contradição direta do essencial, não é FALSO (perguntas 3, 4 e 6).

#### A192 (Lula, gás para 17 milhões de pessoas)

- **Campos:** `explicacao`
- **Estava:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima dos 15 milhões. Nas duas leituras o desvio passa de 10%."
- **Passou a valer:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima de 15 milhões; mas o dado do mês é 'mais de 15 milhões' e a meta oficial era 15,5 milhões, e contra a meta o desvio fica no limite da margem de 10%. Por isso o veredito se apoia na leitura em pessoas, que é a unidade dita."
- **Por quê:** "mais de 15 milhões" é piso, não total, e contra a meta de 15,5 milhões (trecho da exposição de motivos da MP 1.313) o desvio na leitura em famílias fica perto de 10%; a explicação afirmava mais do que o dado sustenta (pergunta 7). O veredito `IMPRECISO` não muda: na unidade dita, pessoas, 17 milhões contra cerca de 50 milhões passa muito da margem.

### correcoes-coerencia.md

#### Correções da revisão de coerência entre lotes

Passada separada, em 16/10/2026, depois das revisões r1 a r8 (lote a lote), seguindo `skills/revisar-checagem.md` (pergunta 6: a mesma régua nos dois lados da mesa e entre checagens), `docs/METODOLOGIA.md` §2 e §2.2 e `.cursor/rules/etica-e-risco.mdc`. O revisor não checou nem revisou nenhuma alegação deste caso antes. Sem busca web: toda fonte que entrou abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-*` e já era usada em outra checagem do caso; os trechos das dez checagens tocadas foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py` (todos achados). O validador, depois da junção, não acusa aviso novo de número ou ano; os dois erros novos são A092 e A093 com confiança baixa ainda sem revisão registrada.

**Nenhum veredito mudou.** Mudaram confiança, resumo, ressalva, explicação e fontes de dez checagens. As notas por checagem, inclusive dos pares examinados e mantidos, estão em `revisao-coerencia.json`.

#### A110 (lote 09), resumo, ressalva, explicação e fontes · par A089, A098

- **Estava:** resumo "A PF investigava o Master desde 2024; o contrato da família de Lewandowski com o banco foi até setembro de 2025"; ressalva "As fontes não dão o mês em que a investigação começou e tratam da investigação do banco, que Vorcaro controlava"; três fontes (SBT News da liquidação, Migalhas, Metrópoles).
- **Passou a valer:** resumo "A PF de São Paulo investigava o Master desde 2023; o contrato da família de Lewandowski foi até setembro de 2025"; ressalva "Os inquéritos de 2023 constam de documento obtido pelo SBT News e tratam do Master e de fundos usados por Vorcaro"; entrou a reportagem do SBT News (coluna Nathalia Fruet, captura p08), com o mesmo trecho das checagens A089 e A098; explicação e data de referência refeitas.
- **Por quê:** a entrevistadora fala da investigação da PF três vezes em dois minutos (A089, A098, A110). Nos dois primeiros cards o vídeo diz "abertos desde 2023"; no terceiro dizia "desde 2024" e que as fontes não davam a data. Lidos em sequência, os cards se contradiziam sobre o mesmo fato, e a fonte que resolve já estava no caso.

#### A116 (lote 09), confiança, ressalva, explicação e fontes · par A118

- **Estava:** confiança média; ressalva "As reportagens tratam do piso por família; não foi conferido se algum adicional mudou antes".
- **Passou a valer:** confiança alta; sem ressalva; entraram o Decreto 13.120 e a reportagem do Congresso em Foco, os mesmos da checagem A118.
- **Por quê:** é o mesmo fato (o reajuste de setembro de 2026 foi o primeiro do mandato) dito pela entrevistadora (A116) e pelo candidato (A118). A118 tinha confiança alta com o decreto, que corrige todos os componentes desde março de 2023; A116 tinha confiança média e uma ressalva sobre os adicionais que a fonte de A118 responde. O lado da mesa que acertou o mesmo fato recebia um card mais fraco.

#### A092 e A093 (lote 08), confiança, resumo e explicação · par A085, A103

- **Estava:** A092 com confiança média e resumo "O único registro da bronca a Andrei Rodrigues é a fala do próprio Lula; não há nota oficial sobre ela"; A093 com confiança média e resumo "Não há registro público do alerta ao ministro da Justiça além da fala do próprio Lula na sabatina". Sem o prefixo de provisório. A explicação de A092 terminava com "A busca desta rodada foi limitada e não achou outro relato".
- **Passou a valer:** confiança baixa; explicação começando por "Busca interrompida pelo limite de buscas da rodada de 16/out; veredito provisório, a refazer:"; resumos "Não foi achado registro da bronca a Andrei Rodrigues além da fala do próprio Lula, nem nota oficial sobre ela" e "Não foi achado registro público do alerta ao ministro da Justiça além da fala do próprio Lula na sabatina". Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a regra de provisórios do caso (INSUSTENTAVEL por busca não exaustiva leva confiança baixa e o prefixo) já valia para A085 (as três conversas de Lula com Fachin, mesmo tipo de afirmação) e para A103, e a r4 citou A085 como "mesma régua" sem igualar o tratamento. A092 declarava a busca limitada; A093 é a mesma frase, o mesmo episódio e o mesmo lote. "Não há registro" afirma uma ausência que a busca interrompida não provou; "não foi achado" é o padrão dos cards provisórios (r4 em A103, r8 em A029).

#### A103 (lote 08), explicação

- **Estava:** "... veredito provisório, a refazer. Revisão r4: entraram duas capturas ..."
- **Passou a valer:** "... veredito provisório, a refazer: na revisão r4 entraram duas capturas ..."
- **Por quê:** o prefixo de provisório é o mesmo em todas as checagens do caso, terminado em dois-pontos; esta era a única fora do formato.

#### A065 (lote 05), ressalva, explicação e fontes · par A070, A081, A084, A115

- **Estava:** ressalva "As fontes não medem se Lula evitou o tema antes; a parte checada é o uso da palavra depois do 1º turno".
- **Passou a valer:** ressalva "Em 18 de setembro, antes do 1º turno, Lula já dizia que cinco ministros do STF estavam ligados ao caso Master"; entrou o Diario de Pernambuco de 18/09/2026 (captura p07, já usado em A081 e A084) com o trecho em que Lula diz que cinco ministros estão ligados direta ou indiretamente ao caso e cita Moraes e Toffoli; a explicação registra também as falas de 3 e 9 de setembro (A070). Veredito `VERDADEIRO` mantido, sobre o uso da palavra depois do 1º turno; a demora não é julgada, porque as fontes não datam o começo das suspeitas sobre ministros.
- **Por quê:** a ressalva dizia que as fontes não mediam o que outras checagens do mesmo vídeo mostram. Lido sozinho, o card verde dava a impressão de que Lula não tinha comentado com clareza antes do 1º turno; A070 e A115, mais adiante, mostram falas de setembro sobre o mesmo assunto.

#### A030 (lote 03), ressalva, explicação, fontes e derivação · par A143

- **Estava:** sem ressalva; "os dois tinham 80 anos na data da fala".
- **Passou a valer:** ressalva "Alguns documentos registram o nascimento de Lula em 6 de outubro; por essa data ele teria 81 anos"; entrou a fonte TVT News e a derivação dos 81 anos, as mesmas de A143. Veredito `VERDADEIRO` mantido ("cerca de 80 anos").
- **Por quê:** a idade de Lula aparece duas vezes no vídeo (A030 e A143). A143 trazia a ressalva da data de registro; A030 não. O próprio arquivo do TSE usado em A001 registra 06/10/1945.

#### A006 (lote 01), confiança · par A147

- **Estava:** confiança média.
- **Passou a valer:** confiança alta.
- **Por quê:** A006 e A147 conferem o mesmo ponto (7ª economia em 2010) com as mesmas duas séries do Banco Mundial e do FMI, e A147 tinha confiança alta.

#### A046 (lote 04), explicação · par A035, A148, A154, A190

- **Estava:** "um desvio de cerca de 11,5% sobre o número dito".
- **Passou a valer:** "um desvio de cerca de 13% medido sobre o valor apurado (7,7 sobre 59)".
- **Por quê:** todas as outras contas de desvio do caso medem sobre o valor apurado (A008, A035, A036, A148, A150, A154, A188, A190), e A148 já tinha sido corrigida na r6 por usar bases diferentes. Pelas duas bases o desvio passa de 10%, então o veredito `IMPRECISO` não muda.

#### A163 (lote 13), resumo · par A037, A038, A039, A178

- **Estava:** "Na PIA do IBGE, a compra de energia elétrica foi 1,05% dos custos da indústria em 2023; matérias-primas, 46%".
- **Passou a valer:** "Na PIA do IBGE, energia elétrica foi 1,05% dos custos da indústria em 2023 e matérias-primas, 46%; sem segunda fonte".
- **Por quê:** é provisório pelo mesmo motivo dos cards do candidato com uma base oficial só (A037 a A039, "sem segunda fonte"; A178, "falta uma segunda fonte independente"). Sem isso, o card laranja da entrevistadora, com um dado oficial que aponta contra a frase, não dizia por que não é vermelho.

#### Para o autor, sem mudança feita

- **A032** segue com o erro do validador "nenhuma fonte N1 ou N2" (já estava antes desta passada). A comparação entre lotes não pede mudança: contagem de encontros públicos com data, confirmada por redações independentes, recebeu o mesmo tratamento que a contagem de tempo da entrevistadora em A140 (só imprensa, `VERDADEIRO`). É diferente de A017 (composição partidária do Senado, que tem registro oficial e ficou provisória). Fica para o autor decidir entre aceitar o aviso como exceção declarada ou buscar fonte oficial dos três encontros.
- **A026** tem, dentro da própria checagem, "agosto de 2025" no resumo e "julho de 2025" no número apurado para a mesma tarifa de 40% (ordem de 30/07, vigência em 06/08). Não é divergência entre lotes e não foi tocada.

### correcoes-rodada2.md

#### Correções da revisão adversarial da rodada 2

Revisão adversarial por IA, passada separada, em 16/out/2026, sobre as 34 checagens refeitas na rodada 2 com a busca web de volta. O revisor não checou nenhuma delas. Foram feitas 9 buscas web, todas atrás do que contradiria um veredito. Dois vereditos mudaram (os dois FALSO viraram INSUSTENTAVEL) e uma explicação foi corrigida sem mudar o veredito. As mudanças foram aplicadas em `checagens-sabatina-completa.json` e nos lotes 13, 14 e 15.

🆕 **Captura nova da revisão** (`capturas/2026-10-15-sabatina-lula-globo-2turno-rv2`, pedido em `checagens/pedidos-captura/revisao-rodada2.json`): Poder360 de 08/05/2023 com as declarações da ministra e do secretário da Saúde sobre o Brasil Sorridente (`7776d3215cde`) e Correio Braziliense de 22/04/2026 sobre o estudo da equipe econômica de Flávio Bolsonaro (`e0f4f07ca12e`, a mesma página já estava na captura p13). Os dois trechos novos foram conferidos contra o texto capturado e encontrados. ⚠️ O `CAPTURAS.json` do caso não foi regerado nesta revisão: falta rodar `conferir-trechos.py` incluindo a pasta `-rv2`.

#### A161 (Lula, o adversário anuncia que não tem aumento do mínimo acima da inflação)

- **Campos:** `veredito`, `resumo`, `ressalva`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Correio Braziliense, 22/04/2026)
- **Estava:** `FALSO`; resumo "Flávio disse que manterá o reajuste do mínimo e prometeu aumento real a aposentados; não há anúncio do contrário"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Não foi achado anúncio de Flávio contra aumento real do mínimo; jornais relataram estudo da equipe sobre benefícios"; ressalva "Segundo jornais, a equipe estudou corrigir aposentadorias e BPC só pela inflação, não o piso; o candidato nega"
- **Por quê:** FALSO exige que as fontes contradigam o essencial (METODOLOGIA §2). O que estava contra a fala eram declarações e promessas de campanha do próprio candidato, que negam um estudo, mas não são registro de que o estudo não houve. A busca da revisão achou o Correio Braziliense de abril de 2026: a equipe econômica estudava "mudanças na política de valorização do salário mínimo" para que aposentadorias e BPC passassem a ter "apenas reposição inflacionária", num plano "ainda não oficialmente apresentado". Isso dá base parcial à fala (há plano relatado que tira o ganho real de quem recebe benefício atrelado ao mínimo), embora não haja anúncio e o piso dos trabalhadores fique com ganho real. Lido sozinho, o card FALSO deixava a impressão de que a fala não tinha base nenhuma (pergunta 8). Régua igual (pergunta 6): na A029, relato de bastidor negado pelo partido também não fechou FALSO contra Lula.

#### A182 (Lula, fazer o Brasil Sorridente voltar a funcionar)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Poder360, 08/05/2023)
- **Estava:** `FALSO`; resumo "O programa estava em 5,2 mil municípios no relançamento, e as equipes cresceram desde 2019; não tinha parado"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "O programa estava em 5,2 mil municípios em 2023; o governo diz que o credenciamento de equipes estava parado"; ressalva "A paralisação do credenciamento é relato do próprio governo; a série oficial de equipes e de gastos não foi achada"
- **Por quê:** o FALSO se apoiava numa conta de equipes montada com duas fontes de imprensa (26.807 em 2019 e "mais de 33 mil" menos 3.685 em 2023), sem a série oficial, e a própria checagem tinha a leitura branda da alegação ("estava reduzido") e confiança média. A busca da revisão achou o Poder360 de 08/05/2023 com a ministra da Saúde dizendo que o programa "ficou estagnada nos últimos 4 anos" e que o governo anterior "represou o credenciamento de equipes", e o secretário dizendo que encontrou "mais de 3.500 equipes represadas" e que o credenciamento, que libera o repasse, "ficou paralisado". É relato do governo que faz a afirmação e não confirma a fala sozinho, mas tira a contradição direta: a leitura literal (o programa tinha parado) é contradita pelos 5,2 mil municípios; a leitura que o contexto sustenta (estava travado) tem registro a favor e uma conta contra. Sem contradição direta do essencial, não é FALSO (perguntas 3, 4 e 6).

#### A192 (Lula, gás para 17 milhões de pessoas)

- **Campos:** `explicacao`
- **Estava:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima dos 15 milhões. Nas duas leituras o desvio passa de 10%."
- **Passou a valer:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima de 15 milhões; mas o dado do mês é 'mais de 15 milhões' e a meta oficial era 15,5 milhões, e contra a meta o desvio fica no limite da margem de 10%. Por isso o veredito se apoia na leitura em pessoas, que é a unidade dita."
- **Por quê:** "mais de 15 milhões" é piso, não total, e contra a meta de 15,5 milhões (trecho da exposição de motivos da MP 1.313) o desvio na leitura em famílias fica perto de 10%; a explicação afirmava mais do que o dado sustenta (pergunta 7). O veredito `IMPRECISO` não muda: na unidade dita, pessoas, 17 milhões contra cerca de 50 milhões passa muito da margem.

### correcoes-validacao.md

#### Correções da validação final (16/out/2026)

Achadas pelo validador e pela releitura depois da revisão adversarial, antes de qualquer publicação. Nenhum veredito mudou.

- **A059:** o trecho do Estado de Minas começava no meio de uma palavra ("o presidente", recortado de "pelo presidente"), e a conferência por palavra inteira não o achava na captura. O trecho passou a começar em "anúncio feito neste domingo (31) pelo presidente", cópia literal da mesma página.
- **A026:** o `numero_apurado` datava a tarifa de 40% em "julho de 2025" e o resumo em "agosto de 2025". As duas datas estão na fonte (ordem executiva de 30/07/2025, em vigor em 06/08/2025); o `numero_apurado` passou a dizer as duas, por extenso (30 de julho, 6 de agosto), como estão no trecho.
- **A191:** o validador avisou que a ressalva não mostrava o valor apurado. A ressalva passou a dizer as duas faixas (80 kWh na tarifa social, 120 kWh com isenção só da CDE), e o `numero_apurado` deixou de dizer "desconto de 100%" (que o validador comparava com os 80 kWh) e passou a dizer as duas faixas.

## 3. Transcrição

As 14 correções da transcrição estão em `transcricao/CORRECOES_DE_TRANSCRICAO.md`. ⚠️ O campo `revisao_humana: true` de `transcricao/transcricao.json` é marcado sozinho pelo `ferramentas/corrigir-transcricao.py` quando aplica correções; nesta transcrição as correções foram conferidas pela IA, por passadas isoladas do motor, e **nenhuma pessoa ouviu o áudio**.

## 4. A auditoria final por amostra (16/out, manhã)

Depois da validação, um agente de IA que não extraiu, não checou e não revisou nada deste caso auditou 44 checagens: as 3 `FALSO`, uma amostra sorteada dos outros vereditos (semente e script em `checagens/revisao/AUDITORIA_FINAL.md`) e todas as dos 6 cortes. Fez 8 buscas web, só atrás do que contradiria um veredito. Achou 5 problemas, e a correção foi feita em seguida, nos lotes, com nova junção, registro da revisão (`revisao.json`, nota "Auditoria final" no começo de cada uma), conferência de trechos (704 de 704) e validador com 0 erros. O antes e depois está em `checagens/revisao/auditoria-final-antes-depois.json`.

| Id | Quem fala | Antes | Depois | Por quê |
|---|---|---|---|---|
| A149 (corte-04) | Lula | VERDADEIRO | IMPRECISO | a conversão do saldo do FMI de nov/2003 usava a equivalência de agosto de 2002 (cerca de US$ 30,7 bilhões); pela cotação do próprio FMI de 28/11/2003 (capturada) dá cerca de US$ 33,8 bilhões, 11% acima dos 30 ditos, e o pago em 2005 fica 29% abaixo. É a régua da A154 (Renata, 10,6%) aplicada ao candidato |
| A039 (corte-02) | Lula | INSUSTENTAVEL | VERDADEIRO | a segunda fonte existia: a VNA publicou, pela embaixada do Vietnã, alta de 16,6% nas exportações do Brasil no 1º semestre; com os 14,1% do Comex Stat até setembro, o dito fica a cerca de 8% do apurado, a régua da A038 |
| A155 | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL | era provisório de uma busca interrompida, sem o marcador, e a rodada 2 não passou por ele; a busca da auditoria não achou levantamento do que pensa "boa parte dos economistas". É a régua da A157 e da A158 (Lula) aplicada à jornalista |
| A180 | Lula | IMPRECISO | INSUSTENTAVEL | julgava uma fala de out/2026 com dado de nov/2024 (anacronismo, METODOLOGIA §5); lida como entradas, a frase não é contradita, e não há balanço de 2026 |
| A036 (corte-02) | Lula | IMPRECISO | IMPRECISO | o veredito fica; entrou na ressalva o melhor argumento a favor da fala (22% no 1º semestre, pelo CEBC), que não se sustenta até setembro, como o recorte de janeiro a maio da A037, e a explicação declara que Poder360 e CEBC usam a mesma base (regra 2 da §3.1). A China não tinha 2026 no UN Comtrade |
| A064 e A074 (corte-03) | Renata Lo Prete e Lula | INSUSTENTAVEL | INSUSTENTAVEL | o auditor sugeriu VERDADEIRO com ressalva. Mantidos: as duas frases tocam fato em apuração, e `etica-e-risco.mdc` §5 manda INSUSTENTAVEL; o resumo de cada uma diz o que está documentado e que a apuração não concluiu, a mesma régua nos dois lados da mesa |

**Novas capturas:** `capturas/2026-10-15-sabatina-lula-globo-2turno-aud` (cotações do DES do FMI de novembro de 2003 e a matéria da VNA; a página de cotações de dezembro de 2002 veio sem a tabela e não entrou como fonte) e `-aud2` (Caixin, com o relatório do CEBC). Pedidos em `checagens/pedidos-captura/auditoria-final*.json`.

**O que mudou no resultado:** 129 verdadeiro, 30 impreciso, 31 sem comprovação, 3 falso. Do lado de Lula os números não mudaram (67 · 24 · 25 · 3: uma subida e uma descida em cada veredito); do lado da entrevistadora, 62 · 6 · 6 · 0. Métricas, relatório e considerações refeitos; corte-02 e corte-04 renderizados, validados e copiados de novo para a pasta de entrega.

**A A145** usa a mesma equivalência de 2002 para o saldo da posse. O auditor, com a cotação do FMI de 31/12/2002, chegou a perto de US$ 20,8 bilhões; essa página veio sem a tabela na captura e o número não entrou no caso. O resumo ("cerca de US$ 20 bi") continua de pé nas duas contas, e a A145 não mudou.

