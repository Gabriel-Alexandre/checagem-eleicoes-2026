# Correções da revisão r2 (lotes 04, 05 e 06)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. Duas buscas web, as duas só atrás do que contradiria um veredito: uma sobre posição de Flávio sobre a 6x1 antes de maio de 2026 (A031 e A038; nada achado) e outra sobre a origem dos R$ 350 bilhões (A047; achou o Gastômetro do Estadão). A fonte nova foi capturada em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv2` (pedido em `checagens/pedidos-captura/revisao-r2.json`). Todo trecho dos três lotes, novo ou antigo, foi conferido contra o texto capturado por palavra inteira, com a normalização de `ferramentas/conferir-trechos.py`. Nenhuma cor de veredito mudou. Uma checagem (A047) passou a provisória. As notas por checagem estão em `revisao-r2.json`.

## A047 (lote 05), explicação, confiança e marcador de provisório

- **Estava:** INSUSTENTAVEL com confiança média, sem marcador; a explicação tratava o levantamento da Folha (R$ 193,8 bi) como a referência e dizia que o critério "gastou" não correspondia ao que ele mede.
- **Passou a valer:** INSUSTENTAVEL com confiança baixa e a explicação começando por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:". Ela cita o Gastômetro do Estadão (R$ 278,3 bi em "gastos de Lula para se reeleger" em 18/08/2026, com alta prevista), diz que o dito fica 25,8% acima desse valor de agosto (derivação declarada) e que medir a fala de 16/10 por ele seria anacronismo, e diz o que falta: o valor do painel mais perto de 16/10.
- **Por quê:** pergunta 4 e regra das travas do caso de 15/10 (a A155 escapou do mesmo jeito). A busca da checagem não achou o levantamento cujo conceito é o da frase, então o veredito era provisório de fato, sem o marcador. A fala usa o vocabulário do Gastômetro ("gastou", "para tentar se reeleger"); fechar o veredito com o valor de agosto seria o anacronismo da A180 do caso de 15/10.

## A047 (lote 05), resumo

- **Estava:** "Não há fonte para R$ 350 bi; o levantamento da Folha somou R$ 193,8 bi em medidas, a maior parte crédito"
- **Passou a valer:** "O Gastômetro do Estadão somava R$ 278,3 bi em 18 de agosto, com alta prevista; o valor de outubro não foi conferido"
- **Por quê:** pergunta 8: lido sozinho, o card antigo dava a impressão de que a referência é R$ 193,8 bi, quando há um painel do mesmo conceito, maior e em alta. E pergunta 7: "a maior parte crédito" falava do valor, e o trecho só diz que 11 das 20 medidas são majoritariamente crédito.

## A047 (lote 05), ressalva, número apurado e data de referência

- **Estava:** ressalva vazia; `numero_apurado` só com os R$ 193,8 bi da Folha; data "levantamento de 17/09/2026".
- **Passou a valer:** ressalva "A Folha somou R$ 193,8 bi em 20 medidas até 17 de setembro, 11 delas sobretudo linhas de crédito"; `numero_apurado` com os dois levantamentos e as datas; data de referência com as duas datas e a nota de que o valor na data da fala não foi conferido.
- **Por quê:** o dado da Folha continua útil e vai para a ressalva com lastro; a data da fala precisa estar dita (METODOLOGIA §5).

## A047 (lote 05), fontes

- **Estava:** 3 fontes; o trecho do Bahia Notícias parava nas nove medidas com impacto primário.
- **Passou a valer:** 4 fontes. Entrou TNH1, "Lula já gastou R$ 278,3 bilhões para tentar se manter na Presidência" (18/08/2026, reprodução de reportagem do Estadão, captura rv2 `62d5506e8598`), N4. O trecho do Bahia Notícias ganhou "[...] As outras 11 se referem majoritariamente a linhas de crédito com juros mais baixos do que os de mercado".
- **Por quê:** dar trecho ao novo resumo e à nova ressalva (regra 6). ⚠️ O TNH1 reproduz o Estadão; a fonte primária (o Gastômetro) não foi capturada, e é o que a rodada 2 precisa buscar.

## A038 (lote 04), divergência entre fontes

- **Estava:** nenhuma.
- **Passou a valer:** "O título da matéria do Jornal Opção diz que Flávio 'defende fim da escala 6×1', mas o corpo da mesma matéria diz que ele criticou a proposta e traz a frase citada no trecho, contra a PEC. O título não descreve a fala relatada, e o veredito se apoia no corpo."
- **Por quê:** quem abre a fonte lê no título o contrário do que o trecho prova; divergência aparente não pode ficar calada (`checar-alegacao`, campo `divergencia_entre_fontes`). Conferido no texto capturado (p04-r4 `5b2360370e58`).

## A041 (lote 05), fonte do Senado e explicação

- **Estava:** o trecho da página da PEC 12/2026 só tinha título e situação; a explicação dizia "apresentada no Senado em 28/05/2026 [...] com assinatura de Flávio Bolsonaro entre os coautores".
- **Passou a valer:** o trecho inclui "Senador Rogerio Marinho (PL/RN) , e outros [...] Senador Flávio Bolsonaro (PL/RJ)"; a explicação diz "com Flávio Bolsonaro entre os coautores e na CCJ do Senado desde 28/05/2026".
- **Por quê:** pergunta 3: a coautoria não tinha trecho, e a página capturada (p05-r2 `30838a092f93`) mostra 28/05/2026 como data do último local, não como data de apresentação.

## A046 (lote 05), explicação

- **Estava:** "O Jornal de Brasília e o SBT News registram a apresentação e o conteúdo."
- **Passou a valer:** "O Jornal de Brasília (Estadão Conteúdo) registra a apresentação e o conteúdo."
- **Por quê:** o SBT News não está entre as fontes desta checagem (está na A050); a explicação citava fonte que o arquivo não tem.
