# Correções da revisão r1 (lotes 01 e 02)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p01` e `-p02`, e cada trecho novo foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Nenhum veredito mudou. As notas por checagem estão em `revisao-r1.json`.

## A003 (lote 01), explicação

- **Estava:** "a avaliação 'ruim ou péssimo' nunca chegou à maioria nas rodadas lidas: 40% e 41% no Datafolha"; série do Datafolha sem a rodada de 20 e 21 de maio; Quaest de 14 de agosto (48% e 46%) e de 2 de setembro (48% e 45%) sem trecho em fonte nenhuma; "em julho e agosto a aprovação ficou numericamente à frente".
- **Passou a valer:** "ruim ou péssimo" de 38% a 42% no Datafolha; a série inclui o empate de 20 e 21 de maio (48% e 48%) e a rodada Quaest de 50% e 44% citada no trecho de 28/09; "em julho e no início de agosto a aprovação ficou numericamente à frente nos dois institutos".
- **Por quê:** METODOLOGIA §3.1, regra 6 (número sem trecho) e pergunta 7 do roteiro. O 40% e 41% omitia o 42% que já estava no trecho do DGABC; o empate de maio estava numa página capturada e não usada; em 14 de agosto a Quaest já tinha a desaprovação à frente, então "julho e agosto" esticava o dado.

## A003 (lote 01), fontes

- **Estava:** 9 fontes.
- **Passou a valer:** 11 fontes. Entraram Congresso em Foco, "Datafolha: rejeição a Lula cai, e aprovação encurta distância" (23/05/2026, captura p01 `fdf1e7c88b91`), e Diario de Pernambuco (Estadão Conteúdo), "Quaest: 48% desaprovam o governo Lula e 45% aprovam" (02/09/2026, captura p01 `4225091c34ba`).
- **Por quê:** dar trecho aos números da explicação que não tinham (pergunta 3 e regra 6).

## A003 (lote 01), ressalva

- **Estava:** "Em julho e agosto a aprovação ficou numericamente à frente, e várias diferenças estavam na margem de 2 pontos"
- **Passou a valer:** "Houve empate em maio, a aprovação ficou à frente em julho e no início de agosto, e várias diferenças estavam na margem de 2 pontos"
- **Por quê:** a ressalva vai para a tela; o empate de maio pesa a favor do IMPRECISO e faltava, e "agosto" inteiro não confere (pergunta 8).

## A011 (lote 01), fontes

- **Estava:** InfoMoney (N4), O Povo (N4) e Aos Fatos (N3); nenhuma N1 ou N2.
- **Passou a valer:** entrou Senado Federal (Presidência do Senado), "Congresso Nacional promulga PEC da Transição que garante a manutenção de R$ 600 a famílias carentes" (22/12/2022, captura p01 `f18364979177`), como N1, com o trecho que diz que a emenda "impediu a redução, já no próximo mês de janeiro, do valor pago" e abriu R$ 70 bilhões para o Bolsa Família.
- **Por quê:** METODOLOGIA §3.1, regra 1: o card traz valores e não havia fonte N1 ou N2. A fonte oficial confirma o ponto que decide o veredito (havia programa no orçamento, faltava verba para os R$ 600).

## A011 (lote 01), explicação

- **Estava:** "O PLOA em si não foi capturado; os números vêm de três reportagens que leram o projeto, com os mesmos valores."
- **Passou a valer:** "O PLOA em si não foi capturado; os valores do projeto vêm de duas reportagens independentes que o leram, com os mesmos números, e o registro oficial do Senado na promulgação da PEC da Transição confirma o ponto central: a emenda garantiu os R$ 600 e, nas palavras do presidente do Congresso, impediu a redução do valor pago já em janeiro."
- **Por quê:** só duas das três reportagens trazem os valores do projeto (o Aos Fatos não traz R$ 105,7 bi nem R$ 405), e a explicação passa a citar a fonte N1 nova.

## A014 (lote 02), resumo

- **Estava:** "Tebet, do MDB, apoiou em 2022 e foi ministra; PSDB e Cidadania também apoiaram e ficaram sem ministério"
- **Passou a valer:** "Tebet, do MDB, apoiou em 2022 e foi ministra; o Cidadania e quadros do PSDB também apoiaram e ficaram sem ministério"
- **Por quê:** o trecho do Mais Goiás diz que o PSDB liberou os filiados e que quem apoiou foram quadros como Serra e FHC. O card dizia que o partido apoiou, o que a fonte não sustenta (perguntas 7 e 8).

## A014 (lote 02), fontes

- **Estava:** 6 fontes, nenhuma com a permanência de Tebet no ministério até 2026, que a explicação afirma ("foi ministra do Planejamento de 2023 até sair para disputar a eleição de 2026").
- **Passou a valer:** entrou Poder360, "Simone Tebet confirma saída do governo até 30 de março" (30/01/2026, captura p02 `afef4debdb40`).
- **Por quê:** pergunta 3; o fato que mais pesa contra a frase da entrevistadora precisava de trecho.

## A018 (lote 02), trecho da fonte Aos Fatos

- **Estava:** o segundo pedaço do trecho começava em "Segundo a secretaria, a taxa de aprovação seria de 94%".
- **Passou a valer:** o pedaço começa em "Em resposta ao levantamento feito pela Folha de S.Paulo, em janeiro, a Secretaria de Relações Institucionais alegou ser equivocado considerar que houve aprovação de apenas 15% das MPs no primeiro biênio de governo.", e a `prova` cita os 15%.
- **Por quê:** a `divergencia_entre_fontes` cita "15% a 23%" e o 15% não estava em trecho nenhum (regra 6). A frase está na mesma página capturada (p02 `02fb36f61265`).

## A025 (lote 02), trecho da fonte Expreso (Agencia EFE)

- **Estava:** só a frase de Alckmin sobre a "buena química".
- **Passou a valer:** o trecho começa com "Tensión diplomática: Washington expulsó a un policía brasileño en Miami; Brasil respondió retirando credenciales a un agente de EE. UU. Conflicto Bolsonaro: La relación se tensó por la denegación de visado a un consejero de Trump para visitar al expresidente preso.", e a `prova` cita os dois atritos.
- **Por quê:** a ressalva, que vai para a tela, cita a expulsão de agente e a negação de visto, e nenhum trecho trazia esses fatos (perguntas 3 e 7). A frase está na mesma página capturada (p02 `17f80feaafbf`).
