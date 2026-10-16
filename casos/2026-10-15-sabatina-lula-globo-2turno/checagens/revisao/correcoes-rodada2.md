# Correções da revisão adversarial da rodada 2

Revisão adversarial por IA, passada separada, em 16/out/2026, sobre as 34 checagens refeitas na rodada 2 com a busca web de volta. O revisor não checou nenhuma delas. Foram feitas 9 buscas web, todas atrás do que contradiria um veredito. Dois vereditos mudaram (os dois FALSO viraram INSUSTENTAVEL) e uma explicação foi corrigida sem mudar o veredito. As mudanças foram aplicadas em `checagens-sabatina-completa.json` e nos lotes 13, 14 e 15.

🆕 **Captura nova da revisão** (`capturas/2026-10-15-sabatina-lula-globo-2turno-rv2`, pedido em `checagens/pedidos-captura/revisao-rodada2.json`): Poder360 de 08/05/2023 com as declarações da ministra e do secretário da Saúde sobre o Brasil Sorridente (`7776d3215cde`) e Correio Braziliense de 22/04/2026 sobre o estudo da equipe econômica de Flávio Bolsonaro (`e0f4f07ca12e`, a mesma página já estava na captura p13). Os dois trechos novos foram conferidos contra o texto capturado e encontrados. ⚠️ O `CAPTURAS.json` do caso não foi regerado nesta revisão: falta rodar `conferir-trechos.py` incluindo a pasta `-rv2`.

## A161 (Lula, o adversário anuncia que não tem aumento do mínimo acima da inflação)

- **Campos:** `veredito`, `resumo`, `ressalva`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Correio Braziliense, 22/04/2026)
- **Estava:** `FALSO`; resumo "Flávio disse que manterá o reajuste do mínimo e prometeu aumento real a aposentados; não há anúncio do contrário"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Não foi achado anúncio de Flávio contra aumento real do mínimo; jornais relataram estudo da equipe sobre benefícios"; ressalva "Segundo jornais, a equipe estudou corrigir aposentadorias e BPC só pela inflação, não o piso; o candidato nega"
- **Por quê:** FALSO exige que as fontes contradigam o essencial (METODOLOGIA §2). O que estava contra a fala eram declarações e promessas de campanha do próprio candidato, que negam um estudo, mas não são registro de que o estudo não houve. A busca da revisão achou o Correio Braziliense de abril de 2026: a equipe econômica estudava "mudanças na política de valorização do salário mínimo" para que aposentadorias e BPC passassem a ter "apenas reposição inflacionária", num plano "ainda não oficialmente apresentado". Isso dá base parcial à fala (há plano relatado que tira o ganho real de quem recebe benefício atrelado ao mínimo), embora não haja anúncio e o piso dos trabalhadores fique com ganho real. Lido sozinho, o card FALSO deixava a impressão de que a fala não tinha base nenhuma (pergunta 8). Régua igual (pergunta 6): na A029, relato de bastidor negado pelo partido também não fechou FALSO contra Lula.

## A182 (Lula, fazer o Brasil Sorridente voltar a funcionar)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`, `data_de_referencia`, `divergencia_entre_fontes`, uma fonte nova (Poder360, 08/05/2023)
- **Estava:** `FALSO`; resumo "O programa estava em 5,2 mil municípios no relançamento, e as equipes cresceram desde 2019; não tinha parado"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "O programa estava em 5,2 mil municípios em 2023; o governo diz que o credenciamento de equipes estava parado"; ressalva "A paralisação do credenciamento é relato do próprio governo; a série oficial de equipes e de gastos não foi achada"
- **Por quê:** o FALSO se apoiava numa conta de equipes montada com duas fontes de imprensa (26.807 em 2019 e "mais de 33 mil" menos 3.685 em 2023), sem a série oficial, e a própria checagem tinha a leitura branda da alegação ("estava reduzido") e confiança média. A busca da revisão achou o Poder360 de 08/05/2023 com a ministra da Saúde dizendo que o programa "ficou estagnada nos últimos 4 anos" e que o governo anterior "represou o credenciamento de equipes", e o secretário dizendo que encontrou "mais de 3.500 equipes represadas" e que o credenciamento, que libera o repasse, "ficou paralisado". É relato do governo que faz a afirmação e não confirma a fala sozinho, mas tira a contradição direta: a leitura literal (o programa tinha parado) é contradita pelos 5,2 mil municípios; a leitura que o contexto sustenta (estava travado) tem registro a favor e uma conta contra. Sem contradição direta do essencial, não é FALSO (perguntas 3, 4 e 6).

## A192 (Lula, gás para 17 milhões de pessoas)

- **Campos:** `explicacao`
- **Estava:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima dos 15 milhões. Nas duas leituras o desvio passa de 10%."
- **Passou a valer:** "Se a fala quis dizer famílias, 17 milhões fica 13,3% acima de 15 milhões; mas o dado do mês é 'mais de 15 milhões' e a meta oficial era 15,5 milhões, e contra a meta o desvio fica no limite da margem de 10%. Por isso o veredito se apoia na leitura em pessoas, que é a unidade dita."
- **Por quê:** "mais de 15 milhões" é piso, não total, e contra a meta de 15,5 milhões (trecho da exposição de motivos da MP 1.313) o desvio na leitura em famílias fica perto de 10%; a explicação afirmava mais do que o dado sustenta (pergunta 7). O veredito `IMPRECISO` não muda: na unidade dita, pessoas, 17 milhões contra cerca de 50 milhões passa muito da margem.
