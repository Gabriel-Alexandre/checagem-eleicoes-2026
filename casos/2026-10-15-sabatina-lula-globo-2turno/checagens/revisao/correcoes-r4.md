# Correções da revisão r4 (lotes 08 e 09)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-p07` e `-p09`, e cada trecho novo foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Um veredito mudou (A104). As notas por checagem estão em `revisao-r4.json`. O lote 09 não foi alterado.

## A104 (lote 08), veredito

- **Estava:** `INSUSTENTAVEL` (provisório, "busca interrompida pelo limite de buscas"), com a explicação "Nenhuma fonte capturada sustenta a posição atribuída, e nenhuma a contradiz".
- **Passou a valer:** `VERDADEIRO`, confiança baixa (a mesma de antes).
- **Por quê:** a captura p07 `2c258b0dcb7e` (A Crítica de Campo Grande, entrevista de Haddad ao podcast 3 Irmãos, publicada em 6 de junho) traz Haddad dizendo que o Banco Central era o órgão responsável por acompanhar e agir diante das irregularidades do Master, que quem supervisiona banco é o Banco Central, e que o caso foi levado ao conhecimento do Procurador-Geral da República e da Polícia Federal. É a posição que Lula atribui a ele no contexto da fala ("o Banco Central vai investigar tecnicamente [...] foi assim que eu pedi para ele comunicar ao Procurador-Geral da República, foi assim que o Haddad se posicionou"). Com o agradecimento público de Galípolo ao apoio de Haddad (Finsiders, 09/02/2026), são duas fontes. Pergunta 3 e pergunta 6: a mesma régua deu `VERDADEIRO` com ressalva para Galípolo em A102, onde a expressão literal também não aparece.

## A104 (lote 08), resumo, ressalva, explicação e data de referência

- **Estava:** resumo "As fontes achadas não trazem Haddad dizendo que o caso Master seria tratado de forma técnica"; ressalva nula; data de referência "declarações de 2026".
- **Passou a valer:** resumo "Haddad disse que cabia ao Banco Central agir no caso Master e que o caso foi levado à Procuradoria-Geral e à PF"; ressalva "Haddad fala do dever do Banco Central e do envio à Procuradoria-Geral e à PF; a expressão sem critério político não aparece"; data de referência "entrevista publicada em 6 de junho de 2026; agradecimento de Galípolo em 9 de fevereiro de 2026"; explicação reescrita com o que a entrevista diz, a ressalva da expressão literal e o registro de que, na mesma entrevista, Haddad associou o caso à gestão anterior do BC (avaliação dele, fora do veredito).
- **Por quê:** acompanhar o veredito novo (perguntas 7 e 8).

## A104 (lote 08), fontes

- **Estava:** Jornal Grande Bahia (Haddad e Dirceu defendem Jaques Wagner, junho de 2026) e Finsiders (Galípolo agradece o apoio de Haddad).
- **Passou a valer:** A Crítica de Campo Grande (captura p07 `2c258b0dcb7e`, trecho com três pedaços marcados por `[...]`) e Finsiders, com a coluna `prova` reescrita ("Em outra ocasião, o presidente do BC registra o apoio de Haddad à atuação do BC no caso"). O Jornal Grande Bahia saiu.
- **Por quê:** a matéria sobre Jaques Wagner trata de outro ponto e não prova nada sobre a alegação (pergunta 3); a fonte que prova estava capturada e não tinha sido usada.

## A103 (lote 08), explicação e data de referência

- **Estava:** "nenhuma fonte capturada registra pedido de Lula, nem especifica o Procurador-Geral como destinatário"; data de referência "comunicações do BC em 2025".
- **Passou a valer:** a explicação registra que Haddad, na entrevista de junho de 2026 (captura p07), diz que o caso foi levado ao conhecimento do Procurador-Geral da República e da PF, sem dizer por quem nem a pedido de quem; que o BC teve certeza da falta de lastro em 27 de junho de 2025 e comunicou o MPF e a PF em julho (Poder360, captura p09); e que Galípolo, perguntado na CPI se recebeu comando do Planalto depois da reunião com Vorcaro, descreveu a orientação de ser técnico, sem citar pedido para comunicar a PGR. Data de referência: "comunicações ao Ministério Público e à PF entre o fim de 2024 e setembro de 2025". O veredito continua `INSUSTENTAVEL`.
- **Por quê:** a frase "nem especifica o Procurador-Geral como destinatário" ficou errada diante de uma captura que já estava no caso (pergunta 3), e o depoimento de Galípolo à CPI é o registro mais próximo do pedido que Lula descreve e não o menciona.

## A103 (lote 08), fontes

- **Estava:** Revista Oeste e Finsiders.
- **Passou a valer:** mais duas, Poder360, "Lula disse para eu ser técnico após reunião com Vorcaro, diz Galípolo" (08/04/2026, captura p09 `9da28aea89bf`), e A Crítica de Campo Grande (captura p07 `2c258b0dcb7e`).
- **Por quê:** dar trecho ao que a explicação nova afirma (regra 6 do §3.1).

## A103 (lote 08), resumo

- **Estava:** "O BC comunicou fatos do Master ao Ministério Público, mas não há registro de que foi a pedido de Lula"
- **Passou a valer:** "O BC comunicou o caso Master ao Ministério Público e à PF; as fontes não registram que foi a pedido de Lula"
- **Por quê:** "não há registro" afirma ausência absoluta numa rodada de busca limitada; o card passa a dizer o que as fontes mostram (perguntas 7 e 8).

## A099 (lote 08), resumo

- **Estava:** "As fontes consultadas não registram o pedido; a visita de Silvio Santos a Lula em 2010 foi sobre o Teleton"
- **Passou a valer:** "As fontes não registram Silvio Santos procurando Lula no caso PanAmericano; a visita de 2010 foi antes, sobre o Teleton"
- **Por quê:** lido sozinho, o resumo antigo sugeria que a visita citada por Lula tinha sido sobre outra coisa, o que é impressão de `FALSO` num card `INSUSTENTAVEL`. A visita registrada foi em setembro de 2010, antes do rombo de novembro, e o card agora diz isso (pergunta 8).

## A101 (lote 08), resumo e explicação

- **Estava:** resumo "O banco de Macedo é o Digimais, em crise desde 2024; as fontes não registram pedido dele a Lula"; explicação "Metrópoles e Estadão descrevem a crise do banco desde 2024, com inadimplência, aportes do próprio Macedo e tentativas de venda sob supervisão do BC."
- **Passou a valer:** resumo "O banco de Edir Macedo é o Digimais, com crise apontada em 2024 e 2025; as fontes não registram o banco procurando Lula"; explicação "Metrópoles e Estadão descrevem a crise do banco, com relatórios de 2024 e 2025 apontando inadimplência alta depois da pandemia, aportes do próprio Macedo e o banco à venda há mais de um ano."
- **Por quê:** "desde 2024" não tem lastro: o Metrópoles diz que a situação "não é boa há um bom tempo" e cita relatórios de 2024 e 2025 sobre inadimplência pós-pandemia, e o Estadão fala em "à venda há mais de um ano"; "sob supervisão do BC" não está em trecho nenhum. "pedido dele" era ambíguo entre Macedo e o banco (pergunta 7).
