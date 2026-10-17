# Correções da revisão r5 (lotes 13 e 14)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A121 a A140. Duas chamadas de busca web, as duas atrás do que contradiria um veredito: uma para a A138 (contatos de Eduardo Bolsonaro com conservadores estrangeiros antes de outubro de 2016) e uma para a A133 (difusão vermelha ou proibição de viagem). A da A138 achou o que muda o veredito; as duas páginas novas foram capturadas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv5` (pedido em `checagens/pedidos-captura/revisao-r5.json`). A da A133 não achou nada que contradissesse o veredito, e nada dela entrou no caso. Os dois lotes validam contra `esquemas/checagens.schema.json` e os 86 pedaços de trecho, antigos e novos, aparecem por palavra inteira no texto capturado da sua URL, com a normalização de `ferramentas/conferir-trechos.py`. Um veredito mudou. As notas por checagem estão em `revisao-r5.json`.

## A138 (lote 14), veredito

- **Estava:** INSUSTENTAVEL, confiança média.
- **Passou a valer:** VERDADEIRO, confiança média.
- **Por quê:** a explicação original dizia que a busca não tinha olhado 2015 e 2016 e que isso "poderia mudar o veredito", então a busca não era exaustiva (METODOLOGIA §2.1). A busca da revisão achou o registro: em maio de 2016 Eduardo foi a Israel em visita parlamentar (Times of Israel), e a comitiva se reuniu com o presidente do Knesset (reportagem da Folha reproduzida pelo ABC do ABC). De maio de 2016 a outubro de 2026 passam pouco mais de 10 anos, o que confere com "mais de 10 anos". Confiança média porque o registro de 2016 é uma visita de comitiva e o "vários líderes conservadores" se apoia sobretudo na rede americana posterior.

## A138 (lote 14), resumo

- **Estava:** "Os contatos de Eduardo com conservadores estrangeiros registrados nas fontes começam em 2017 e 2018"
- **Passou a valer:** "Eduardo esteve com o presidente do Parlamento de Israel em maio de 2016; os contatos com a direita dos EUA vêm de 2018"
- **Por quê:** o resumo antigo ficou contradito por duas fontes capturadas (pergunta 8). O novo traz as duas datas com trecho.

## A138 (lote 14), ressalva, numero_apurado, data_de_referencia, divergencia_entre_fontes e explicação

- **Estava:** ressalva vazia; `numero_apurado` "registros a partir de 2017 e 2018"; `data_de_referencia` "contatos documentados de 2017 e 2018 em diante"; divergência só entre Agora RN e Agência Pública; explicação com "Nenhuma fonte mostra contato anterior a 2016".
- **Passou a valer:** ressalva "O registro de 2016 é uma visita de comitiva ao Parlamento de Israel; a rede com a direita dos EUA começa em 2018"; `numero_apurado` "primeiro contato registrado em maio de 2016"; `data_de_referencia` "visita a Israel em maio de 2016; contatos nos EUA a partir de 2018"; divergência acrescida da diferença de partido da comitiva de 2016 (Partido Social Liberal no Times of Israel, PSC na Folha), que não muda o veredito; explicação refeita com a viagem de 2016, a rede americana a partir de 2018 e o registro de que o veredito mudou nesta revisão.
- **Por quê:** acompanhar o veredito novo e deixar na tela o limite do registro de 2016 (perguntas 7 e 8).

## A138 (lote 14), fontes

- **Estava:** 3 fontes (Agora RN, Agência Pública, IHU).
- **Passou a valer:** 5 fontes. Entraram The Times of Israel, "Brazil's other Bolsonaro sees elusive embassy move as start of pro-Israel shift" (captura rv5 `9b58ec27364b`), com o trecho da visita parlamentar de maio de 2016, e ABC do ABC (reportagem da Folha de S.Paulo), "Bolsonaro mirou evangélicos e versão 'amigo de Israel' quando se batizou no Jordão" (18/10/2023, captura rv5 `128504235d5d`), com o trecho da viagem de 2016 com os filhos e do encontro com o presidente do Knesset.
- **Por quê:** dar trecho ao fato que muda o veredito, com duas apurações independentes (pergunta 3 e regra 1 da §3.1).

## A140 (lote 14), resumo

- **Estava:** "O STF condenou generais, um almirante e outros oficiais pela trama golpista, em decisões já definitivas"
- **Passou a valer:** "O STF condenou generais e um almirante no núcleo central da trama golpista, em decisão já definitiva"
- **Por quê:** o trânsito em julgado que está nas fontes (STF, 25/11/2025) é o do núcleo central, e a Agência Brasil de janeiro de 2026 (capturada na p13) registra que os demais núcleos ainda estavam em fase de recurso. "Outros oficiais [...] em decisões já definitivas" punha no card condenações sem trânsito registrado (perguntas 7 e 8). O veredito não muda.

## A140 (lote 14), explicação

- **Estava:** sem dizer de qual núcleo é o trânsito em julgado que o resumo afirma.
- **Passou a valer:** acrescida da frase "O resumo fala só do núcleo central, porque é dele o trânsito em julgado registrado; o tenente-coronel Mauro Cid, réu-colaborador, e os oficiais das demais ações não entram no resumo."
- **Por quê:** amarrar o resumo novo ao que a fonte diz.
