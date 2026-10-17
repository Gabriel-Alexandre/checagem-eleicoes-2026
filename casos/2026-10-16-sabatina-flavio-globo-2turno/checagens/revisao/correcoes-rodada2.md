# Correções da revisão adversarial da rodada 2

Revisão adversarial por IA, em passada separada, feita em 17/out/2026 sobre as 27 checagens que a rodada 2 refez com busca (partes 1 a 4). O revisor não checou nenhuma delas. Não fez nenhuma busca web: as mudanças saem só das capturas já feitas, da régua da METODOLOGIA e do validador. Três vereditos mudaram (A062, A173 e A174, os três para INSUSTENTAVEL), e um trecho foi completado sem mudar o veredito (A153). As notas de cada id estão em `revisao-rodada2.json`.

## Antes da revisão: os lotes 07 a 12 tinham voltado ao estado provisório

- **O que foi achado:** às 14:15:55 de 17/out, um mesmo processo regravou os lotes 07 a 12 e 15 a 17 (diferença de milissegundos entre os arquivos). Os lotes 15 a 17 saíram com a parte 3, mas os lotes 07 a 12 voltaram ao texto da rodada 1: A062, A071, A072, A086 e A113 com o marcador de provisório, e A095 com o marcador do revisor r4. A parte 2 tinha gravado os lotes por volta de 13:53 e o `checagens-sabatina-completa.json` às 13:54, e só ele guardava a versão da parte 2.
- **O que foi feito:** as seis checagens da parte 2 foram copiadas do `checagens-sabatina-completa.json` de 13:54 de volta para os lotes 07, 08, 09, 10 e 12. As outras checagens desses lotes já eram iguais às do arquivo consolidado. Cópia dos lotes antes da restauração e do consolidado de 13:54 ficaram no scratchpad do revisor.
- **Depois das correções abaixo,** o `checagens-sabatina-completa.json` foi remontado a partir dos lotes com `ferramentas/lotes-de-debate.py checagem-juntar` (207 checagens). Antes disso ele não tinha as partes 3 e 4.

## A062 (lote 07)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`, `derivacoes` (o `como`), e o `trecho` e a `prova` da fonte N2 (estudo do Movimento Pessoas à Frente e da República.org)
- **Estava:** `IMPRECISO`; resumo "Estudo estima R$ 20 bilhões por ano pagos acima do teto nos três Poderes; o número dito fica 20% acima"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Estudo estima ao menos R$ 20 bi por ano pagos acima do teto nos três Poderes; R$ 24 bi não aparece em fonte"; ressalva "O estudo trata os R$ 20 bi como piso e cobre agosto de 2024 a julho de 2025, antes das regras do STF de março de 2026"
- **Por quê:** o IMPRECISO media os R$ 24 bilhões contra os R$ 20 bilhões como se fossem o total, mas a própria fonte N2 diz que o gasto com supersalários "é de pelo menos 8 bilhões de dólares ao ano" (o equivalente aos cerca de R$ 20 bilhões), que o estudo "aborda um subgrupo do universo de servidores" e que é "difícil dimensionar a subnotificação"; a Itatiaia e a Coalizão, que o reproduzem, escrevem "ao menos R$ 20 bilhões". Desvio de 20% sobre um piso não prova erro: é a leitura de piso aplicada a "mais de 15 milhões" na A192 do caso 2026-10-15-sabatina-lula-globo-2turno (perguntas 4 e 6: a primária ganha das secundárias, que tratam o valor como total). Sem fonte para os 24 e sem fonte que os contradiga, a régua do §2.2 dá INSUSTENTAVEL ("número que não existe em fonte nenhuma"). Os trechos novos foram conferidos no texto capturado em `-r2parte2`.

## A173 (lote 18)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`
- **Estava:** `VERDADEIRO`; resumo "Na Quaest com a Pax de setembro, 58% apoiam restringir o acesso a armas como medida para a segurança; 39% rejeitam"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão 58% a favor de restringir armas na Quaest com a Pax de setembro; o relatório do instituto não foi achado"; ressalva "É a pesquisa da Quaest com a Pax, não a eleitoral; os 58% a favor e os 39% contra vêm só de reportagens"
- **Por quê:** as quatro fontes são reportagens (N4) que reproduzem o mesmo relatório da Quaest, e a própria checagem diz que o relatório não foi localizado. A regra 2 da §3.1 só aceita fontes N3/N4 quando a primária que citam foi conferida, e a regra 1 pede N1 ou N2 para afirmação com número ("a maioria"). O precedente citado pela rodada 2, a A043 do caso de 15/out, tinha o Datafolha como fonte N2; todas as outras checagens de pesquisa com veredito colorido nos dois casos de outubro (A003, A046, A052 e A174 de 15/out; A039 e A197 deste caso) têm o relatório do instituto. E é a régua aplicada ao candidato neste caso: número reproduzido só por imprensa, sem N1 ou N2, ficou INSUSTENTAVEL (A047, A113) (pergunta 6). Nada contradiz a frase: se o relatório da Pesquisa Nacional de Segurança e Tecnologia for capturado e confirmar a pergunta e o percentual, o veredito volta a VERDADEIRO.

## A174 (lote 18)

- **Campos:** `veredito`, `resumo`, `numero_apurado`, `explicacao`
- **Estava:** `VERDADEIRO`; resumo "Entre as mulheres, 62% apoiam restringir o acesso a armas, contra 58% no total e 55% entre os homens"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão 62% entre as mulheres, contra 58% no total, na Quaest com a Pax; o relatório do instituto não foi achado"
- **Por quê:** o mesmo motivo da A173, e mais um: a alegação é do tipo `comparacao`, e o validador (`passo8_validar`, regra 1 da §3.1) reprova veredito colorido desse tipo sem fonte N1 ou N2. Com VERDADEIRO a validação do caso tinha um erro a mais; com INSUSTENTAVEL fica o aviso de que a explicação diz o que faltou, e ela diz (o relatório da Quaest). Ressalva da margem de 3 pontos mantida.

## A153 (lote 16)

- **Campos:** `trecho` e `prova` da fonte Diário do Transporte
- **Estava:** trecho sem a data; o resumo diz "em 25 de agosto", e o validador avisava que o número 25 não estava em trecho nenhum desta checagem
- **Passou a valer:** o trecho começa por "o Governo Federal autorizou na noite desta terça-feira, 25 de agosto de 2026, a concessão das garantias da União [...]", texto da mesma página, já usado na A152 e conferido na captura `-r2parte3-r2`
- **Por quê:** número de tela precisa de trecho (regra 6 da §3.1). O veredito não muda.
