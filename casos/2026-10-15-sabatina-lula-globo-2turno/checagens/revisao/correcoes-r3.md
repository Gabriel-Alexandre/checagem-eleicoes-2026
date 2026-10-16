# Correções da revisão r3 (lotes 06 e 07)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`, `docs/METODOLOGIA.md` §2 a §5 e `.cursor/rules/etica-e-risco.mdc`. Sem busca web nesta rodada e sem captura nova: toda fonte que entrou abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p06`, `-p07` e `-p08`, e os 84 trechos dos dois lotes, depois das mudanças, foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py` (84 de 84 achados). Números e anos de `resumo` e `ressalva` foram conferidos com as funções `numeros_de()` e `anos_de()` do validador (nenhum aviso). Três vereditos mudaram (A081, A088, A089). As notas por checagem estão em `revisao-r3.json`.

## A072 (lote 06), ressalva

- **Estava:** "A vista suspende o julgamento por até 90 dias; vencido o prazo, o caso é liberado automaticamente"
- **Passou a valer:** "A vista suspende o julgamento por 90 dias, prorrogáveis uma vez; vencido o prazo, o caso é liberado automaticamente"
- **Por quê:** o § 4º do art. 134 do Regimento Interno do STF suspende o prazo no recesso e permite prorrogá-lo uma vez por igual período. "Por até 90 dias" prometia um teto que não existe e contradizia a ressalva da A078, que vai no mesmo vídeo (perguntas 6 e 8).

## A072 (lote 06), explicação e fonte

- **Estava:** "pelo Regimento Interno do STF a vista tem prazo de 90 dias, e vencido o prazo os autos são liberados automaticamente"; trecho do Regimento com o caput do art. 134 e o § 5º.
- **Passou a valer:** "pelo Regimento Interno do STF a vista tem prazo de 90 dias, que fica suspenso no recesso e pode ser prorrogado uma vez por igual período, e vencido o prazo os autos são liberados automaticamente"; o trecho do Regimento (captura p06 `e27b39c8c544`) ganhou o § 4º, com `[...]` antes do § 5º, porque entre os dois há a nota da Emenda Regimental 54.
- **Por quê:** dar lastro à ressalva nova (pergunta 3).

## A073 (lote 06), resumo

- **Estava:** "O relatório da PF se concentrou em Moraes, mas o STF não apurou quais ministros são citados nem em que condição"
- **Passou a valer:** "O relatório da PF dedicou 181 de 218 páginas a Moraes, mas nenhuma fonte compara o envolvimento de cada ministro"
- **Por quê:** "o STF não apurou" atribuía ao tribunal o argumento de um voto, o de Gilmar Mendes numa questão de ordem que, pelo Poder360 capturado, estava 4 a 3 contra quando Dino pediu vista. O card passa a dizer o dado (181 de 218, no trecho do Movimento Econômico) e o que falta para o ranking, sem tomar a posição de um dos lados do plenário (perguntas 7 e 8). O veredito INSUSTENTAVEL não muda.

## A073 (lote 06), explicação e prova da fonte

- **Estava:** "Mas o próprio voto de Gilmar Mendes na questão de ordem de 15/09 diz [...]"; prova: "Documento do STF: a apuração mirou Moraes, mas não há certificação de quais ministros são citados nem em que condição, o que impede o ranking."
- **Passou a valer:** a explicação diz que o voto "é a posição de um ministro numa proposta que não foi aprovada até a data da fala, e não uma conclusão do tribunal", e registra que a mesma régua valeu para as falas do entrevistado sobre Toffoli, Mendonça e Castro; a prova trata o documento como voto de um ministro.
- **Por quê:** pergunta 4 (a fonte prova o que o dono dela disse, não o fato) e pergunta 6 (simetria declarada).

## A077 (lote 06), ressalva

- **Estava:** "O presidente nomeia ministros, com aval do Senado, e pode conceder indulto; nenhum dos dois muda decisão"
- **Passou a valer:** "O governo pode recorrer pela AGU, como fez em setembro, mas quem decide o recurso é o próprio STF"
- **Por quê:** o melhor argumento contra a frase do entrevistado é que o governo contestou, em setembro, a decisão de Mendonça que afastou o diretor-geral da PF, e o presidente do STF a suspendeu. A ressalva antiga falava de dois poderes que não vêm ao caso e omitia o caminho que existe e foi usado (pergunta 8). O veredito VERDADEIRO não muda: recorrer é pedir ao Judiciário, não interferir na decisão.

## A077 (lote 06), fontes e explicação

- **Estava:** 3 fontes (Constituição, Regimento do STF, Poder360); explicação sem o recurso da AGU.
- **Passou a valer:** 4 fontes. Entrou O Povo, "Fachin suspende decisões de Mendonça e Dino e mantém Andrei Rodrigues na chefia da PF" (09/09/2026, captura p07 `f8d435ff6b76`), com o trecho do recurso da AGU e da suspensão; a explicação traz o argumento e por que ele não derruba o veredito.
- **Por quê:** lastro da ressalva nova (pergunta 3).

## A081 (lote 07), veredito

- **Estava:** `INSUSTENTAVEL`
- **Passou a valer:** `IMPRECISO`
- **Por quê:** a transcrição de 27/08 já usada como fonte (Aos Fatos, captura p07 `9ef3ea4cdf53`, conferida contra a transcrição deste repositório em `casos/2026-08-27-sabatina-lula-globo`) traz, no bloco do INSS, "todos eles que foram citados [...] o caminho é um só. É o caminho da apuração, da investigação, ou da inocência, ou da condenação", e, no bloco do Master, que se Jaques Wagner cometeu desvio "vai pagar o preço". O núcleo do que Lula diz ter repetido (apurar e punir quem errou) está na entrevista anterior da Globo; a árvore do §2.1 reserva INSUSTENTAVEL para quando as fontes não sustentam. O que não está é a frase de que a sociedade não aceitaria, e no bloco do Master a ênfase foi a presunção de inocência: essência certa, enquadramento e assunto não.

## A081 (lote 07), resumo, ressalva, explicação e fonte

- **Estava:** resumo "Na entrevista à Globo de agosto, sobre o Master, Lula falou em apuração e presunção de inocência, não nessa frase"; ressalva "Ideia parecida aparece em entrevistas de setembro à Rádio Tupi e a um podcast, fora da Globo"; trecho do Aos Fatos só com o bloco do Master.
- **Passou a valer:** resumo "Na Globo, em agosto, Lula defendeu apuração e condenação de quem errou, mas sem dizer que a sociedade não aceitaria"; ressalva "A fala de agosto sobre apuração foi no bloco do INSS; sobre o Master, ele destacou a presunção de inocência"; trecho do Aos Fatos com o bloco do INSS e o do Master, separados por `[...]`; explicação refeita.
- **Por quê:** acompanhar o veredito novo (perguntas 6, 7 e 8).

## A084 (lote 07), resumo

- **Estava:** "Há reportagens sobre dinheiro do Master, festas e um encontro pago com ministros; 'orgia' não aparece nas fontes"
- **Passou a valer:** "Reportagens citam contrato do Master, festa paga por Vorcaro e suposto encontro com acompanhante; 'orgia' só vem de Lula"
- **Por quê:** "um encontro pago com ministros" lia como encontro de ministros pago por Vorcaro, que não é o que o Diario de Pernambuco registra (reportagem sobre um ministro e uma acompanhante); "festas" no plural não tem lastro (as fontes trazem a degustação de Londres); e "'orgia' não aparece nas fontes" era inexato, porque a palavra aparece, na boca do próprio Lula, na reportagem da Rádio Tupi capturada (perguntas 7 e 8). O veredito INSUSTENTAVEL não muda.

## A084 (lote 07), ressalva

- **Estava:** "Os casos seguem em apuração e nenhum ministro foi denunciado formalmente"
- **Passou a valer:** "Os relatos seguem em apuração, sem conclusão até a data da fala"
- **Por quê:** "nenhum ministro foi denunciado formalmente" não está em trecho nenhum; a Gazeta só diz que nenhum participante da degustação era investigado (pergunta 7).

## A087 (lote 07), data de referência

- **Estava:** "evento em Londres de 24 a 26/04/2024"
- **Passou a valer:** "degustação de 25/04/2024, durante fórum em Londres em abril de 2024"
- **Por quê:** o dia 24 não está em trecho nenhum; a Gazeta dá 25/04/2024 para a degustação e o Poder360 dá 26 de abril para o painel de Andrei (pergunta 7). O veredito VERDADEIRO não muda.

## A088 (lote 07), veredito e confiança

- **Estava:** `INSUSTENTAVEL`, confiança baixa (provisório, "uma fonte só").
- **Passou a valer:** `VERDADEIRO`, confiança média.
- **Por quê:** a segunda fonte existia no caso. O SBT News, "Exclusivo: Banco Central recebeu alerta da PF sobre Master em 2024, mas disse não ter encontrado ilegalidades" (19/03/2026, captura p08 `a83e4caff0b7`, já usada nas checagens A097 e A098), registra que o BC conhecia suspeitas sobre o Master desde 2023 e as analisou com seus departamentos de supervisão. Com o LetsMoney (apuração do Valor: ofícios do Departamento de Supervisão desde 2021 e um ciclo de supervisão sobre irregularidades em crédito e precatórios em 2021 e 2022), são duas fontes independentes que datam a atuação do BC antes de abril de 2024 (pergunta 4).

## A088 (lote 07), resumo, ressalva, explicação e fontes

- **Estava:** resumo "Uma reportagem registra ofícios do BC ao Master desde 2021; não achamos segunda fonte que confirme a data"; ressalva "O termo de comparecimento do BC contra o Master foi preparado em maio de 2024, depois da festa"; 2 fontes.
- **Passou a valer:** resumo "Ofícios do BC cobravam correções do Master desde 2021, e o BC analisou suspeitas sobre o banco em 2023"; ressalva "Eram ofícios de supervisão; o termo de comparecimento, ação mais dura, só foi preparado em maio de 2024"; 3 fontes (entrou o SBT News, com o trecho da resposta do BC; o trecho do LetsMoney ganhou a linha da tabela de 2021 e 2022); explicação refeita, com o que o SBT diz contra (o BC concluiu então não abrir procedimento específico).
- **Por quê:** num card INSUSTENTAVEL, a ressalva antiga lia como desmentido da entrevistadora, quando a única fonte capturada a sustentava (pergunta 8). A mesma informação passa a ser o "certo, mas" de um VERDADEIRO.

## A089 (lote 07), veredito e confiança

- **Estava:** `INSUSTENTAVEL`, confiança baixa (provisório).
- **Passou a valer:** `VERDADEIRO`, confiança média.
- **Por quê:** a explicação dizia que nenhuma fonte capturada citava inquérito da PF em São Paulo sobre o Master antes de abril de 2024, mas o SBT News capturado na p08 registra que a Delegacia de Repressão a Crimes Financeiros da PF em São Paulo "havia aberto desde 2023 dois inquéritos sobre o Master". A checagem A098, sobre o mesmo ponto retomado pela entrevistadora minutos depois, já tinha VERDADEIRO com o SBT News e a CNN Brasil: o mesmo vídeo teria dois cards opostos sobre o mesmo fato (pergunta 6). Confiança média porque a data anterior à festa vem só do documento obtido pelo SBT News; a CNN confirma investigação em 2024, sem mês.

## A089 (lote 07), resumo, ressalva, explicação e fontes

- **Estava:** resumo "As fontes datam o inquérito da PF sobre o Master da venda ao BRB, barrada em 2025; nada de inquérito em SP antes"; sem ressalva; 2 fontes (Jovem Pan, Gazeta do Povo).
- **Passou a valer:** resumo "Ofício obtido pelo SBT News registra dois inquéritos da PF de São Paulo sobre o Master abertos desde 2023"; ressalva "A data de 2023 consta de documento obtido pelo SBT News; o mérito dos inquéritos segue em apuração"; 4 fontes (entraram SBT News e CNN Brasil, com os mesmos trechos da A098, capturas p08; Jovem Pan e Gazeta ficam, com a prova dizendo que tratam do inquérito posterior); explicação refeita.
- **Por quê:** "nada de inquérito em SP antes" era contradito por fonte do próprio caso (perguntas 3, 4 e 8).
