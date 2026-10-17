# CORREÇÕES · sabatina de Flávio Bolsonaro na TV Globo, 2º turno (16/out/2026)

Registro de tudo o que mudou na checagem DEPOIS do primeiro veredito, antes de qualquer publicação. ⛔ Veredito não se edita em silêncio (METODOLOGIA §7). Cada passada foi feita por um agente de IA que não escreveu a checagem que revisou. O modelo deste arquivo é o `CORRECOES.md` do caso de Lula de 15/out (`casos/2026-10-15-sabatina-lula-globo-2turno/`), com a mesma régua.

## 1. O limite de buscas web e a rodada 2 (17/out)

A checagem das 207 alegações rodou em três ondas de 7 agentes, cada um com no máximo 7 buscas web, dentro do limite de 200 buscas por turno somadas entre todos os agentes (a lição da §1 do caso de 15/out, em que 15 agentes ao mesmo tempo esgotaram a busca). Onde a busca não foi exaustiva, o veredito saiu INSUSTENTAVEL com confiança baixa e a explicação começando por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:". Saíram 23 assim da rodada 1, e os revisores marcaram mais 4 que eram provisórios de fato e não tinham o marcador (A015, A047, A095, A142; o caso da A155 de 15/out). Na rodada 2, com busca, outros 4 agentes refizeram os 27, e um quinto revisou a rodada 2. Ficaram duas (A113 e A161), refeitas numa rodada 3 com as últimas 7 buscas do turno e revisadas por outro agente: A161 VERDADEIRO, A113 IMPRECISO. Nenhuma ficou provisória.

| id | rodada 1 | rodada 2 | depois da revisão da rodada 2 e da coerência (atual) |
|---|---|---|---|
| A008 | INSUSTENTAVEL (provisório) | IMPRECISO | IMPRECISO |
| A009 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A010 | INSUSTENTAVEL (provisório) | IMPRECISO | IMPRECISO |
| A015 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A020 | INSUSTENTAVEL (provisório) | IMPRECISO | IMPRECISO |
| A023 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A047 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A062 | INSUSTENTAVEL (provisório) | IMPRECISO | INSUSTENTAVEL |
| A071 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A072 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A086 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A095 | VERDADEIRO (provisório) | VERDADEIRO | VERDADEIRO |
| A113 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | IMPRECISO |
| A142 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A144 | INSUSTENTAVEL (provisório) | IMPRECISO | IMPRECISO |
| A151 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A152 | INSUSTENTAVEL (provisório) | IMPRECISO | IMPRECISO |
| A153 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A161 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | VERDADEIRO |
| A162 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |
| A173 | INSUSTENTAVEL (provisório) | VERDADEIRO | INSUSTENTAVEL |
| A174 | INSUSTENTAVEL (provisório) | VERDADEIRO | INSUSTENTAVEL |
| A191 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A194 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | IMPRECISO |
| A199 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A200 | INSUSTENTAVEL (provisório) | VERDADEIRO | VERDADEIRO |
| A201 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | INSUSTENTAVEL |

Na coluna da rodada 2, "(provisório)" marca as duas que só se resolveram na rodada 3. Nenhuma checagem do caso segue provisória.

## 2. A revisão adversarial, lote a lote, a rodada 2 e a coerência entre lotes e entre casos

**Os vereditos que a revisão mudou** (fora os provisórios da §1, que têm tabela própria). A A138 foi de INSUSTENTAVEL a VERDADEIRO na revisão r5 e voltou a INSUSTENTAVEL na coerência, pela regra 1 da §3.1; as duas passagens estão abaixo.

| id | quem fala | rodada 1 | depois da revisão (atual) | onde está o porquê |
|---|---|---|---|---|
| A078 | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL | correcoes-coerencia |
| A085 | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL | correcoes-coerencia |
| A114 | Flávio Bolsonaro | IMPRECISO | INSUSTENTAVEL | correcoes-coerencia |

🔧 **Um incidente, corrigido:** às 14h15 o agente da rodada 2 parte 3, que só devia mexer nos lotes 15 a 17, regravou os lotes 07 a 12 a partir de uma cópia antiga. O revisor da rodada 2 percebeu e restaurou os seis ids da parte 2; a IA que conduz o caso conferiu, id a id, cada lote contra o histórico do git e achou a revisão r4 do lote 11 perdida (A101 a A110 tinham voltado à rodada 1), restaurada do commit `b57c27b`. Nenhuma outra edição de revisão faltou nos 21 lotes, e os agentes seguintes receberam a instrução de ler o lote do disco imediatamente antes de gravar e conferir o `git diff --stat` no fim.

As notas completas estão no campo `revisao_ia` de cada checagem. As mudanças, uma por uma, com o antes e o depois:

### checagens/revisao/correcoes-r1.md

#### Correções da revisão r1 (lotes 01, 02 e 03)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, `docs/METODOLOGIA.md` §2, §3 e §5 e `.cursor/rules/etica-e-risco.mdc`. Duas buscas web, as duas atrás do que contradiria um veredito: os juros nominais só do governo central (A003) e uma fonte para os R$ 36 bilhões de prejuízo das estatais (A019). Nenhuma achou o dado. A captura feita nessa procura (`capturas/2026-10-16-sabatina-flavio-globo-2turno-rv1`, pedido em `checagens/pedidos-captura/revisao-r1.json`: a nota do BC de 30/09 na cópia do Poder360 e o Raio X da Dívida de agosto da Câmara) não entrou como fonte, porque nenhuma das duas separa o governo central. Toda fonte nova abaixo já estava capturada. Os 95 trechos dos três lotes, depois das mudanças, foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py`, por palavra inteira (95 de 95 achados); os três lotes validam contra `esquemas/checagens.schema.json`; números, anos e termos de intenção de `resumo`, `ressalva` e `numero_apurado` foram conferidos com `numeros_de()`, `anos_de()` e `_tem_intencao()` do validador (nenhum aviso). Nenhum veredito mudou. Uma checagem (A015) foi marcada como provisória. As notas por checagem estão em `revisao-r1.json`.

##### A002 (lote 01), explicação

- **Estava:** "o coordenador da campanha, Rogério Marinho, disse que uma vitória de Flávio levaria a Selic a 12% ou 13% (EQI)"
- **Passou a valer:** "o coordenador da campanha, Rogério Marinho, disse que uma eventual vitória de Flávio poderia levar a Selic à faixa de 12% a 13% ao ano (EQI)"
- **Por quê:** o trecho do EQI diz "poderia levar a taxa básica de juros para a faixa de 12% a 13% ao ano"; a explicação transformava a hipótese em afirmação (pergunta 3).

##### A015 (lote 02), explicação e confiança

- **Estava:** explicação sem o marcador de provisório, terminando em "A busca nesta rodada foi limitada a duas consultas sobre o tema."; confiança `media`.
- **Passou a valer:** a explicação começa por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e termina com o que falta ("procurar declarações nominais de economistas ligados à campanha ou que declararam apoio ao candidato sobre o ajuste de R$ 200 bilhões sem mexer nas despesas obrigatórias, e algum levantamento de opinião de economistas que permita falar ou não em consenso"); confiança `baixa`.
- **Por quê:** a árvore do §2.1 só dá INSUSTENTAVEL depois de busca exaustiva, e a própria checagem declarava duas consultas. É o defeito da A155 do caso de 15/out, provisória sem marcador que escapou da rodada 2. Veredito, resumo e fontes sem mudança; a rodada 2 refaz.

##### A016 (lote 02), resumo

- **Estava:** "A coordenadora econômica de Flávio falou em ajuste de 1,5% do PIB, cerca de R$ 190 bi; a campanha fala em R$ 200 bi"
- **Passou a valer:** "A coordenadora econômica falou em ajuste de 1,5% do PIB, cerca de R$ 190 bi; o discurso da campanha é de R$ 200 bi"
- **Por quê:** "a campanha fala em R$ 200 bi" contradizia a ressalva ("a campanha evita cravar o valor"). O SBT, no trecho, diz que integrantes da campanha "evitam cravar o tamanho do ajuste", mas "o discurso é de um corte em torno de R$ 200 bilhões" (perguntas 7 e 8).

##### A016 (lote 02), ressalva

- **Estava:** "A campanha evita cravar o valor; a coordenadora falou em 1,5% do PIB, cerca de R$ 190 bilhões"
- **Passou a valer:** "Integrantes da campanha evitam cravar o valor, e ainda não há plano completo com os gastos a cortar"
- **Por quê:** a ressalva repetia o dado do resumo e deixava de fora o que limita o VERDADEIRO: o valor não foi cravado (SBT) e não há plano completo com a discriminação dos gastos (Poder360), ambos com trecho (pergunta 8).

##### A018 (lote 02), trecho e prova da fonte Money Times

- **Estava:** trecho "As estatais federais registraram superávits sucessivos, como o saldo positivo de R$ 2,5 bilhões em 2021 e de R$ 4,8 bilhões em 2022."
- **Passou a valer:** o trecho começa com "Vale lembrar que a série do Banco Central não considera a Petrobras, a Eletrobras, nem as empresas do setor financeiro (os bancos públicos).", seguido de `[...]` e do trecho antigo (captura p02-r2 `547a05b233f7`); a prova cita a exclusão.
- **Por quê:** a explicação afirma que "a imprensa registra que os bancos públicos também ficam fora" da série, e nenhum trecho da A018 dizia isso (pergunta 3).

##### A019 (lote 02), trecho e prova da fonte Money Times

- **Estava:** trecho só com o déficit de R$ 5,93 bilhões de janeiro a abril de 2026.
- **Passou a valer:** o trecho ganhou, depois de `[...]`, a frase "Vale lembrar que a série do Banco Central não considera a Petrobras, a Eletrobras, nem as empresas do setor financeiro (os bancos públicos)." (mesma captura `547a05b233f7`); a prova cita a exclusão.
- **Por quê:** a ressalva, que vai para a tela, diz "sem Petrobras e bancos públicos", e nenhum trecho da A019 trazia os bancos públicos (perguntas 3 e 7).

##### A021 (lote 03), fontes

- **Estava:** 3 fontes (Lista de Alto Risco do TCU, acórdão do levantamento na SPU, InfoMoney). A `divergencia_entre_fontes` cita "cerca de 742 mil no levantamento do Acórdão 160/2024", número sem trecho nesta checagem.
- **Passou a valer:** 4 fontes. Entrou TCU, "Gestão do patrimônio imobiliário federal gerido pela SPU é ineficiente, diz TCU" (já capturada e usada na A022, `058953b1e507`), com o trecho "A SPU é responsável pela gestão de cerca de 742 mil imóveis, avaliados em, aproximadamente, R$ 1,35 trilhão."
- **Por quê:** METODOLOGIA §3.1, regra 6; a divergência registrada precisava de trecho na própria checagem (pergunta 3). Veredito, resumo e ressalva sem mudança.

##### A026 (lote 03), resumo

- **Estava:** "No orçamento de 2027, a Previdência leva R$ 1.215,1 bi de R$ 2.830,1 bi; saúde e educação têm pisos próprios"
- **Passou a valer:** "No projeto de orçamento de 2027, a Previdência leva R$ 1.215,1 bi de R$ 2.830,1 bi; saúde e educação têm pisos próprios"
- **Por quê:** os valores são do PLOA 2027, projeto enviado em agosto e não aprovado na data da fala; "orçamento de 2027" lia como lei aprovada (perguntas 5 e 8).

##### A027 (lote 03), resumo

- **Estava:** "A Petrobras fala em produzir em cerca de sete anos; a perfuração exploratória já começou em 2025"
- **Passou a valer:** "A Petrobras fala em produzir em cerca de sete anos; a perfuração exploratória foi licenciada em 2025"
- **Por quê:** nenhum trecho dá a data do início da perfuração. O InfoAmazonia dá a licença do Ibama em 20/10/2025, a Exame diz que a licença permite perfuração imediata e o InfoMoney registra o poço em perfuração em agosto de 2026; "começou em 2025" é provável, mas não está escrito em fonte (pergunta 7). Veredito sem mudança.

##### Registrado sem mudança nos lotes

- **A003:** o melhor argumento contra o IMPRECISO é de recorte: a frase fala de "o governo", e a conta divide os juros do setor público consolidado (R$ 1.182,2 bi) pelas dotações federais de saúde e educação (R$ 505 bi). O veredito só continua IMPRECISO se os juros do governo central passarem de cerca de R$ 1.122 bi (2,22 vezes 505). A busca da revisão não achou esse número. Fica IMPRECISO pela mesma medida de juros usada na A007 do caso de 28/08 contra o candidato, e a explicação já declara a lacuna. Pergunta para a passada de coerência.
- **A011:** 7 contra 7,75 dá 9,7% sobre o apurado e 10,7% sobre o dito. Fica VERDADEIRO pela base usada no projeto (o apurado) e pelo mesmo veredito na A006 de 28/08; a A033 do caso de 15/out mediu sobre o dito. Pergunta para a passada de coerência.
- **A025 e A027:** os dois lados usam "exploração" no sentido comum de extração; a checagem seguiu o critério escrito antes da busca (exploração técnica contra produção) e deu IMPRECISO aos dois. Se o autor preferir a leitura comum, as duas mudam juntas.
- **A020:** provisória. O total que falta já está capturado na A021 (cerca de 761 mil imóveis, TCU). Hoje o resumo da A020 cita 655 mil de 2018 e o da A021 cita 761 mil; a rodada 2 deve alinhar os dois cards.
- **A008, A009, A010, A020, A023:** provisórias com o marcador exato e confiança baixa; o que falta está anotado em `revisao-r1.json`.

### checagens/revisao/correcoes-r2.md

#### Correções da revisão r2 (lotes 04, 05 e 06)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. Duas buscas web, as duas só atrás do que contradiria um veredito: uma sobre posição de Flávio sobre a 6x1 antes de maio de 2026 (A031 e A038; nada achado) e outra sobre a origem dos R$ 350 bilhões (A047; achou o Gastômetro do Estadão). A fonte nova foi capturada em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv2` (pedido em `checagens/pedidos-captura/revisao-r2.json`). Todo trecho dos três lotes, novo ou antigo, foi conferido contra o texto capturado por palavra inteira, com a normalização de `ferramentas/conferir-trechos.py`. Nenhuma cor de veredito mudou. Uma checagem (A047) passou a provisória. As notas por checagem estão em `revisao-r2.json`.

##### A047 (lote 05), explicação, confiança e marcador de provisório

- **Estava:** INSUSTENTAVEL com confiança média, sem marcador; a explicação tratava o levantamento da Folha (R$ 193,8 bi) como a referência e dizia que o critério "gastou" não correspondia ao que ele mede.
- **Passou a valer:** INSUSTENTAVEL com confiança baixa e a explicação começando por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:". Ela cita o Gastômetro do Estadão (R$ 278,3 bi em "gastos de Lula para se reeleger" em 18/08/2026, com alta prevista), diz que o dito fica 25,8% acima desse valor de agosto (derivação declarada) e que medir a fala de 16/10 por ele seria anacronismo, e diz o que falta: o valor do painel mais perto de 16/10.
- **Por quê:** pergunta 4 e regra das travas do caso de 15/10 (a A155 escapou do mesmo jeito). A busca da checagem não achou o levantamento cujo conceito é o da frase, então o veredito era provisório de fato, sem o marcador. A fala usa o vocabulário do Gastômetro ("gastou", "para tentar se reeleger"); fechar o veredito com o valor de agosto seria o anacronismo da A180 do caso de 15/10.

##### A047 (lote 05), resumo

- **Estava:** "Não há fonte para R$ 350 bi; o levantamento da Folha somou R$ 193,8 bi em medidas, a maior parte crédito"
- **Passou a valer:** "O Gastômetro do Estadão somava R$ 278,3 bi em 18 de agosto, com alta prevista; o valor de outubro não foi conferido"
- **Por quê:** pergunta 8: lido sozinho, o card antigo dava a impressão de que a referência é R$ 193,8 bi, quando há um painel do mesmo conceito, maior e em alta. E pergunta 7: "a maior parte crédito" falava do valor, e o trecho só diz que 11 das 20 medidas são majoritariamente crédito.

##### A047 (lote 05), ressalva, número apurado e data de referência

- **Estava:** ressalva vazia; `numero_apurado` só com os R$ 193,8 bi da Folha; data "levantamento de 17/09/2026".
- **Passou a valer:** ressalva "A Folha somou R$ 193,8 bi em 20 medidas até 17 de setembro, 11 delas sobretudo linhas de crédito"; `numero_apurado` com os dois levantamentos e as datas; data de referência com as duas datas e a nota de que o valor na data da fala não foi conferido.
- **Por quê:** o dado da Folha continua útil e vai para a ressalva com lastro; a data da fala precisa estar dita (METODOLOGIA §5).

##### A047 (lote 05), fontes

- **Estava:** 3 fontes; o trecho do Bahia Notícias parava nas nove medidas com impacto primário.
- **Passou a valer:** 4 fontes. Entrou TNH1, "Lula já gastou R$ 278,3 bilhões para tentar se manter na Presidência" (18/08/2026, reprodução de reportagem do Estadão, captura rv2 `62d5506e8598`), N4. O trecho do Bahia Notícias ganhou "[...] As outras 11 se referem majoritariamente a linhas de crédito com juros mais baixos do que os de mercado".
- **Por quê:** dar trecho ao novo resumo e à nova ressalva (regra 6). ⚠️ O TNH1 reproduz o Estadão; a fonte primária (o Gastômetro) não foi capturada, e é o que a rodada 2 precisa buscar.

##### A038 (lote 04), divergência entre fontes

- **Estava:** nenhuma.
- **Passou a valer:** "O título da matéria do Jornal Opção diz que Flávio 'defende fim da escala 6×1', mas o corpo da mesma matéria diz que ele criticou a proposta e traz a frase citada no trecho, contra a PEC. O título não descreve a fala relatada, e o veredito se apoia no corpo."
- **Por quê:** quem abre a fonte lê no título o contrário do que o trecho prova; divergência aparente não pode ficar calada (`checar-alegacao`, campo `divergencia_entre_fontes`). Conferido no texto capturado (p04-r4 `5b2360370e58`).

##### A041 (lote 05), fonte do Senado e explicação

- **Estava:** o trecho da página da PEC 12/2026 só tinha título e situação; a explicação dizia "apresentada no Senado em 28/05/2026 [...] com assinatura de Flávio Bolsonaro entre os coautores".
- **Passou a valer:** o trecho inclui "Senador Rogerio Marinho (PL/RN) , e outros [...] Senador Flávio Bolsonaro (PL/RJ)"; a explicação diz "com Flávio Bolsonaro entre os coautores e na CCJ do Senado desde 28/05/2026".
- **Por quê:** pergunta 3: a coautoria não tinha trecho, e a página capturada (p05-r2 `30838a092f93`) mostra 28/05/2026 como data do último local, não como data de apresentação.

##### A046 (lote 05), explicação

- **Estava:** "O Jornal de Brasília e o SBT News registram a apresentação e o conteúdo."
- **Passou a valer:** "O Jornal de Brasília (Estadão Conteúdo) registra a apresentação e o conteúdo."
- **Por quê:** o SBT News não está entre as fontes desta checagem (está na A050); a explicação citava fonte que o arquivo não tem.

### checagens/revisao/correcoes-r3.md

#### Correções da revisão r3 (lotes 07, 08 e 09, A061 a A090)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. O revisor não checou nenhuma destas alegações. **Nenhum veredito mudou.** As mudanças são de confiança, resumo, explicação, data de referência, número apurado e fontes. Toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-16-sabatina-flavio-globo-2turno-p07-r2` e `-p08-r2`. Os 113 trechos dos três lotes, antigos e novos, foram conferidos contra o texto capturado, por palavra inteira, com a normalização de `ferramentas/conferir-trechos.py`, e todos foram encontrados. Os três lotes passam no `esquemas/checagens.schema.json`. Houve uma busca web, atrás do que contradiria a A090 (fonte com os 160 milhões ou com o contrato de Huck), e ela não achou nenhuma. As notas por checagem estão em `revisao-r3.json`.

Provisórios conferidos, com o marcador exato e a confiança baixa: A062, A071, A072 e A086. Não foram refeitos.

##### A063 (lote 07), confiança

- **Estava:** `alta`.
- **Passou a valer:** `media`.
- **Por quê:** as quatro fontes são N4, e a parte "não só a investigação" exige interpretação (o pedido formal à PGR e ao STF aparece como iniciativa da liderança da oposição). Pela skill `checar-alegacao`, `alta` é para N1 direta e inequívoca. O veredito `VERDADEIRO` fica: o essencial é a defesa do impeachment.

##### A067 (lote 07), resumo

- **Estava:** "Mensagens ligam o filho de Nunes Marques a R$ 500 mil por mês via consultoria; ele admite R$ 281,6 mil e nega o resto"
- **Passou a valer:** "Mensagens ligam filho de Nunes Marques a R$ 500 mil mensais; ele diz que recebeu R$ 281,6 mil da consultoria por serviço"
- **Por quê:** "admite R$ 281,6 mil e nega o resto" podia ser lido como confissão de parte de um pagamento de Vorcaro. O trecho do Times Brasil diz que a assessoria do advogado afirma que ele recebeu R$ 281,6 mil da Consult por serviços prestados à própria empresa (pergunta 8).

##### A070 (lote 07), fontes

- **Estava:** 6 fontes; a `divergencia_entre_fontes` citava o Jornal de Brasília ("o encontro resultou de apelos de líderes do PT e do ministro de Relações Institucionais") sem fonte nem trecho.
- **Passou a valer:** 7 fontes. Entrou Jornal de Brasília, "Lula tem encontro Alcolumbre, em gesto de aproximação três meses após rejeição de Messias" (captura p07-r2 `a00f3d530923`), com o trecho dos apelos de Camilo Santana, Teresa Leitão e José Guimarães e o de que o encontro foi na casa de Moraes, com Zanin.
- **Por quê:** pergunta 3; a divergência é parte da checagem e precisava de lastro. O veredito `VERDADEIRO` com ressalva fica.

##### A087 (lote 09), resumo

- **Estava:** "Negociação previa US$ 24 milhões; repasse foi de US$ 10,6 milhões, com parcelas atrasadas cobradas por Flávio"
- **Passou a valer:** "Negociação previa US$ 24 milhões; os repasses documentados somam US$ 12,3 milhões, e Flávio cobrou parcelas atrasadas"
- **Por quê:** pergunta 5 (anacronismo). US$ 10,6 milhões é o total repassado até maio de 2025. Na data da fala, o Coaf, segundo o Poder360 com a piauí (01/09/2026), somava 7 parcelas e US$ 12,3 milhões, contando a de US$ 1,6 milhão de 16/09/2025. O lote 08 (A071) já usava esse total.

##### A087 (lote 09), número apurado, data de referência, explicação e fontes

- **Estava:** `numero_apurado` "US$ 10,6 milhões repassados de US$ 24 milhões negociados"; `data_de_referencia` "repasses de fevereiro a maio de 2025"; explicação "o repassado foi US$ 10,6 milhões, cerca de R$ 61 milhões, de fevereiro a maio de 2025"; 3 fontes.
- **Passou a valer:** `numero_apurado` "US$ 12,3 milhões repassados em 7 parcelas (US$ 10,6 milhões até maio de 2025), de US$ 24 milhões negociados"; `data_de_referencia` "repasses de fevereiro a setembro de 2025, somados pelo Coaf e noticiados em 01/09/2026"; a explicação dá os dois totais e diz que o pago é cerca de metade do combinado; entrou Poder360, "Filme Dark Horse recebeu R$ 65 milhões de Daniel Vorcaro" (captura p08-r2 `063167ccf3af`), com o trecho da parcela de setembro e do total de US$ 12,3 milhões.
- **Por quê:** o mesmo da entrada anterior. O veredito `VERDADEIRO` fica: com US$ 12,3 milhões de US$ 24 milhões, o contrato continua não cumprido.

##### A088 (lote 09), explicação e fontes

- **Estava:** "o fundo usado na captação enviou US$ 13,3 milhões, acima dos US$ 10,6 milhões atribuídos a Vorcaro"; 4 fontes.
- **Passou a valer:** "enviou US$ 13,3 milhões, acima dos US$ 12,3 milhões que o Coaf atribui a Vorcaro em 7 parcelas (Poder360, com a piauí)"; entrou a mesma fonte do Poder360 (captura p08-r2 `063167ccf3af`).
- **Por quê:** pergunta 5; a comparação usava o total de maio de 2025. Com o total vigente na data da fala a diferença diminui, mas o fundo ainda mandou ao filme mais do que Vorcaro pôs nele, e o veredito `VERDADEIRO` fica.

##### Registrado sem mudança no lote

- **A080:** a explicação cita Folha Vitória e Diario de Pernambuco, que não estão entre as fontes da checagem; o que eles sustentariam já está nos trechos da TVT News e do InfoMoney.
- **A086:** provisório; o `numero_apurado` usa os US$ 10,6 milhões de maio de 2025, e a rodada 2 deve usar o total de US$ 12,3 milhões e sair com o mesmo veredito da A072, que é a mesma afirmação.
- **A089:** a transcrição em 1112,6 s registra "um dinheiro totalmente ilícito", provável erro do motor por "lícito"; a frase não foi extraída, mas merece ser ouvida.

### checagens/revisao/correcoes-r4.md

#### Correções da revisão r4 (lotes 10, 11 e 12)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. Duas buscas web, as duas atrás do que contradiria um veredito: uma sobre prisão ou processo de Vaccari por fraude em fundos de pensão (A101), outra sobre manifestação da PF, entre 9 e 16/out, que confirmasse o relato atribuído a Vorcaro (A103 e A104). A segunda não achou nada que mudasse os vereditos. A primeira achou a denúncia da Operação Greenfield, capturada em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv4` (pedido em `checagens/pedidos-captura/revisao-r4.json`). Os outros trechos novos já estavam capturados (p10 e p11/p12). Todo trecho dos três lotes, novo e antigo, foi conferido por palavra inteira contra o texto capturado da sua URL, com a normalização de `ferramentas/conferir-trechos.py` (113 de 113), e os três lotes validam contra `esquemas/checagens.schema.json`. Nenhum veredito mudou de cor; um passou a provisório (A095). As notas por checagem estão em `revisao-r4.json`.

##### A094 (lote 10), explicação

- **Estava:** "O Povo e o Correio da Manhã registram o relato de cerca de R$ 30 milhões em espécie ao Instituto Lula (o valor aparece no relato e nos documentos citados pela revista, não no trecho transcrito do áudio)."
- **Passou a valer:** "(O Povo atribui o valor à própria gravação; o trecho do áudio transcrito pelo SBT News não traz o número)"
- **Por quê:** pergunta 3. O trecho do O Povo, que é fonte da própria checagem, começa por "Na gravação, Vorcaro alega ter negociado [...] um repasse de aproximadamente R$ 30 milhões"; a explicação dizia o contrário do trecho. O veredito não muda: a autenticidade do áudio e o pagamento seguem em apuração (etica-e-risco §5).

##### A095 (lote 10), explicação e confiança

- **Estava:** VERDADEIRO, confiança "media", explicação sem marcador, dizendo que as regras comerciais de transparência para patrocínio "não foram localizadas em documento público dentro do limite de buscas".
- **Passou a valer:** a explicação começa por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e termina dizendo o que falta; confiança "baixa". O veredito (VERDADEIRO) fica até a rodada 2.
- **Por quê:** é um provisório de fato sem o marcador, como a A155 do caso de 15/out. A frase tem duas normas (transparência na compra de patrocínio e separação da linha editorial); só a segunda tem fonte, e a busca da primeira parou no limite. E a `citacao_card` mostra justamente a primeira ("obedecem a regras de transparência"), então o card verde ficava apoiado na metade não buscada (pergunta 8). As duas fontes são documentos do próprio Grupo Globo, o que a explicação já declarava.

##### A098 (lote 10), resumo

- **Estava:** "A PF já tinha inquéritos sobre o Master e o BC o advertiu em novembro de 2024, antes do acordo; o caso segue em apuração"
- **Passou a valer:** "A PF já tinha inquéritos sobre o Master e o BC o convocou em novembro de 2024, antes do acordo; o caso segue em apuração"
- **Por quê:** pergunta 7. Os trechos falam em "termo de compromisso" e em convocação "para um termo de comparecimento"; "advertência" é nome de sanção administrativa do BC, que nenhuma fonte diz ter sido aplicada. A `prova` da fonte Finsiders ("advertência formal") foi corrigida do mesmo jeito.

##### A101 (lote 11), fontes

- **Estava:** 4 fontes, todas sobre a Lava Jato e a CPI de 2016.
- **Passou a valer:** 5 fontes. Entrou Estado de Minas (com Agência Brasil), "Vaccari e mais 13 ex-diretores da Funcef se tornam réus na Operação Greenfield" (29/05/2017, captura rv4 `b9986c6a1804`): a Justiça Federal do DF aceitou a denúncia da Greenfield que tornou Vaccari réu por crimes contra o sistema financeiro e gestão fraudulenta ligados à Funcef.
- **Por quê:** a busca da revisão, feita para tentar derrubar o IMPRECISO, achou que a ligação de Vaccari com fraude em fundo de pensão é mais forte do que o card dizia: não só citação em CPI, mas ação penal. Não muda o veredito, porque a prisão continua sendo da Lava Jato e nenhuma fonte registra prisão pela Greenfield.

##### A101 (lote 11), ressalva

- **Estava:** "A prisão existiu, mas pela Lava Jato; fundos de pensão aparecem só em citações na CPI de 2016"
- **Passou a valer:** "A prisão foi pela Lava Jato; por fraude na Funcef, fundo de pensão da Caixa, ele virou réu em 2017 na Operação Greenfield"
- **Por quê:** perguntas 7 e 8. A ressalva vai para a tela e diminuía, contra o candidato, o que existe no registro. O ano 2017 está no trecho novo.

##### A101 (lote 11), explicação e data de referência

- **Estava:** "[...] sem prisão por isso. Nas buscas feitas não apareceu prisão de Vaccari por fraude em fundos de pensão." · data: "prisão de abril de 2015 (Lava Jato); CPI dos Fundos de Pensão de 2016"
- **Passou a valer:** a explicação acrescenta a denúncia aceita da Greenfield (maio de 2017) e diz que a acusação de fraude em fundo de pensão existe como ação penal, não como motivo de prisão · data: acrescenta "denúncia da Greenfield aceita em maio de 2017".
- **Por quê:** a mesma da fonte nova.

##### A102 (lote 11), resumo

- **Estava:** "Os 10% são relato de Vorcaro em delação rejeitada, sem prova; R$ 1 bi seria a comissão, não o valor a investir"
- **Passou a valer:** "Os 10% são relato de Vorcaro em delação rejeitada, sem comprovação; R$ 1 bi seria a comissão, não o valor a investir"
- **Por quê:** pergunta 7. A própria checagem registra a divergência (a Veja diz que mensagens ajudam a corroborar o relato; a PGR não viu prova dos pagamentos). "Sem prova" afirma ausência; "sem comprovação" diz o que está documentado, e é a forma usada na A099.

##### A103 e A104 (lote 11), trecho e prova da fonte TNH1

- **Estava:** o trecho do TNH1 só trazia o parágrafo dos 10% e do R$ 1 bilhão.
- **Passou a valer:** o trecho acrescenta, com `[...]`, "Mensagens encontradas pela Polícia Federal no celular de Vorcaro ajudaram a corroborar o relato de Vorcaro." e "Mensagens no celular mostram que o banqueiro foi pessoalmente ao Postalis, em Brasília, se reunir com a cúpula do fundo e também conseguiu reuniões com Petros e Previ" (mesma página, captura p10 `c2d9587bedcb`); a `prova` diz que é a leitura da revista, não manifestação da PF.
- **Por quê:** pergunta 3. A ressalva da A104 (texto de tela) e a explicação da A103 citam essas mensagens, e nenhum trecho as trazia.

##### A103 (lote 11), explicação

- **Estava:** "A própria Veja (reproduzida no TNH1) só diz que mensagens obtidas pela PF registram contatos para reuniões com dirigentes de fundos, o que é diferente de a PF confirmar a oferta e a propina atribuídas a Vaccari."
- **Passou a valer:** a explicação passa a expor o melhor argumento a favor da frase (segundo a Veja, mensagens achadas pela PF "ajudaram a corroborar o relato") e diz por que ele não muda o FALSO: é a leitura da revista sobre material apreendido, as mensagens descritas tratam de contatos com dirigentes de fundos e não da oferta e da propina atribuídas a Vaccari, e a única manifestação da PF é a nota que nega ter o relato.
- **Por quê:** a explicação dizia que a Veja "só" falava de contatos, o que encolhia o texto da revista. Um FALSO contra o candidato precisa mostrar o argumento contrário mais forte.

##### A106 (lote 11), ressalva e explicação

- **Estava:** ressalva nula; "A apresentadora suprimiu o palavrão e encurtou a frase, sem mudar o sentido".
- **Passou a valer:** ressalva "Na transcrição, a frase é sobre trocar alguém da segurança na ponta da linha; a citação omitiu da segurança"; a explicação registra a troca de "esperar" por "deixar" e a omissão de "da segurança", e mantém o VERDADEIRO porque a sequência citada (troca o chefe, troca o ministro) está literal na transcrição.
- **Por quê:** perguntas 1 e 6, com a mesma régua da citação aplicada aos dois lados da mesa. A palavra omitida é a que sustenta a leitura de que a fala tratava da segurança pessoal e não da PF; o espectador precisa saber que ela existe. Está no trecho do Poder360.

##### A107 (lote 11), explicação

- **Estava:** "A data exata da saída não entra no card porque o Diário do Nordeste traz 23 de abril e não foi capturada uma segunda fonte com a data."
- **Passou a valer:** "A data exata da saída não entra no card: o Diário do Nordeste traz 23 de abril, e as fontes da A116 situam o pedido de demissão na manhã de 23 (A Gazeta, com Folhapress) e o anúncio em 24 de abril de 2020 (InfoMoney, Poder360)."
- **Por quê:** a frase antiga deixou de ser verdadeira dentro do próprio caso: a A116 (lote 12) tem as datas com trecho capturado (p12).

##### A110 (lote 11), fontes, explicação e data de referência

- **Estava:** 4 fontes; "Se a referência for à troca de 2020, não foi achada justificativa de maus resultados, e Moro disse que nenhuma razão aceitável lhe foi apresentada." · data "agosto de 2019".
- **Passou a valer:** entrou Metrópoles, "Tácio Muzzi é nomeado superintendente da Polícia Federal no Rio de Janeiro" (26/05/2020, captura p11/p12 `3863fe826c55`), com o trecho de que o superintendente que saiu, Carlos Henrique Oliveira, foi confirmado diretor-executivo, "segundo cargo mais importante da corporação"; a explicação usa esse dado para a troca de 2020 · data "agosto de 2019 e maio de 2020".
- **Por quê:** a frase do candidato fala "na época", no contexto da reunião de 2020, e para 2020 o FALSO se apoiava só na palavra de Moro, parte na disputa. A promoção do superintendente que saiu contradiz "maus resultados" por um registro de fato, e a fonte já estava capturada (é da A109).

### checagens/revisao/correcoes-r5.md

#### Correções da revisão r5 (lotes 13 e 14)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A121 a A140. Duas chamadas de busca web, as duas atrás do que contradiria um veredito: uma para a A138 (contatos de Eduardo Bolsonaro com conservadores estrangeiros antes de outubro de 2016) e uma para a A133 (difusão vermelha ou proibição de viagem). A da A138 achou o que muda o veredito; as duas páginas novas foram capturadas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv5` (pedido em `checagens/pedidos-captura/revisao-r5.json`). A da A133 não achou nada que contradissesse o veredito, e nada dela entrou no caso. Os dois lotes validam contra `esquemas/checagens.schema.json` e os 86 pedaços de trecho, antigos e novos, aparecem por palavra inteira no texto capturado da sua URL, com a normalização de `ferramentas/conferir-trechos.py`. Um veredito mudou. As notas por checagem estão em `revisao-r5.json`.

##### A138 (lote 14), veredito

- **Estava:** INSUSTENTAVEL, confiança média.
- **Passou a valer:** VERDADEIRO, confiança média.
- **Por quê:** a explicação original dizia que a busca não tinha olhado 2015 e 2016 e que isso "poderia mudar o veredito", então a busca não era exaustiva (METODOLOGIA §2.1). A busca da revisão achou o registro: em maio de 2016 Eduardo foi a Israel em visita parlamentar (Times of Israel), e a comitiva se reuniu com o presidente do Knesset (reportagem da Folha reproduzida pelo ABC do ABC). De maio de 2016 a outubro de 2026 passam pouco mais de 10 anos, o que confere com "mais de 10 anos". Confiança média porque o registro de 2016 é uma visita de comitiva e o "vários líderes conservadores" se apoia sobretudo na rede americana posterior.

##### A138 (lote 14), resumo

- **Estava:** "Os contatos de Eduardo com conservadores estrangeiros registrados nas fontes começam em 2017 e 2018"
- **Passou a valer:** "Eduardo esteve com o presidente do Parlamento de Israel em maio de 2016; os contatos com a direita dos EUA vêm de 2018"
- **Por quê:** o resumo antigo ficou contradito por duas fontes capturadas (pergunta 8). O novo traz as duas datas com trecho.

##### A138 (lote 14), ressalva, numero_apurado, data_de_referencia, divergencia_entre_fontes e explicação

- **Estava:** ressalva vazia; `numero_apurado` "registros a partir de 2017 e 2018"; `data_de_referencia` "contatos documentados de 2017 e 2018 em diante"; divergência só entre Agora RN e Agência Pública; explicação com "Nenhuma fonte mostra contato anterior a 2016".
- **Passou a valer:** ressalva "O registro de 2016 é uma visita de comitiva ao Parlamento de Israel; a rede com a direita dos EUA começa em 2018"; `numero_apurado` "primeiro contato registrado em maio de 2016"; `data_de_referencia` "visita a Israel em maio de 2016; contatos nos EUA a partir de 2018"; divergência acrescida da diferença de partido da comitiva de 2016 (Partido Social Liberal no Times of Israel, PSC na Folha), que não muda o veredito; explicação refeita com a viagem de 2016, a rede americana a partir de 2018 e o registro de que o veredito mudou nesta revisão.
- **Por quê:** acompanhar o veredito novo e deixar na tela o limite do registro de 2016 (perguntas 7 e 8).

##### A138 (lote 14), fontes

- **Estava:** 3 fontes (Agora RN, Agência Pública, IHU).
- **Passou a valer:** 5 fontes. Entraram The Times of Israel, "Brazil's other Bolsonaro sees elusive embassy move as start of pro-Israel shift" (captura rv5 `9b58ec27364b`), com o trecho da visita parlamentar de maio de 2016, e ABC do ABC (reportagem da Folha de S.Paulo), "Bolsonaro mirou evangélicos e versão 'amigo de Israel' quando se batizou no Jordão" (18/10/2023, captura rv5 `128504235d5d`), com o trecho da viagem de 2016 com os filhos e do encontro com o presidente do Knesset.
- **Por quê:** dar trecho ao fato que muda o veredito, com duas apurações independentes (pergunta 3 e regra 1 da §3.1).

##### A140 (lote 14), resumo

- **Estava:** "O STF condenou generais, um almirante e outros oficiais pela trama golpista, em decisões já definitivas"
- **Passou a valer:** "O STF condenou generais e um almirante no núcleo central da trama golpista, em decisão já definitiva"
- **Por quê:** o trânsito em julgado que está nas fontes (STF, 25/11/2025) é o do núcleo central, e a Agência Brasil de janeiro de 2026 (capturada na p13) registra que os demais núcleos ainda estavam em fase de recurso. "Outros oficiais [...] em decisões já definitivas" punha no card condenações sem trânsito registrado (perguntas 7 e 8). O veredito não muda.

##### A140 (lote 14), explicação

- **Estava:** sem dizer de qual núcleo é o trânsito em julgado que o resumo afirma.
- **Passou a valer:** acrescida da frase "O resumo fala só do núcleo central, porque é dele o trânsito em julgado registrado; o tenente-coronel Mauro Cid, réu-colaborador, e os oficiais das demais ações não entram no resumo."
- **Por quê:** amarrar o resumo novo ao que a fonte diz.

### checagens/revisao/correcoes-r6.md

#### Correções da revisão r6 (lotes 15, 16 e 17)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A141 a A170. Uma chamada de busca web, atrás do que contradiria um veredito: a atuação de Flávio Bolsonaro pelo PL 3.723/2019 no Senado (A163). Não achou nada que mude o veredito. Três páginas novas foram capturadas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv6` (pedido em `checagens/pedidos-captura/revisao-r6.json`), sem busca: são os PDFs do MapBiomas Fogo (Coleção 5) linkados na página do Monitor do Fogo, que já estava capturada na pasta p16-r10. Uma fonte já capturada no caso de 15/out (página de notícias da PF, pasta `capturas/2026-10-15-sabatina-lula-globo-2turno-p06`) entrou na A167. Todos os 104 trechos dos três lotes, os antigos e os novos, foram conferidos por palavra inteira contra o texto capturado da URL (normalização de `ferramentas/conferir-trechos.py`): todos achados. Os três lotes validam contra `esquemas/checagens.schema.json`, e a conferência de número e ano do validador não acusa aviso.

**Nenhum veredito mudou.** Uma checagem passou a provisória (A142). As notas por checagem estão em `revisao-r6.json`.

##### A142 (lote 15), explicação, confiança e resumo

- **Estava:** confiança média; explicação sem marcador, terminando em "Nesta rodada foi feita uma busca dirigida à frase do ranking; Europol e relatórios de apreensão nos portos europeus por origem não foram consultados."; resumo "A ONU lista Santos entre os principais portos de saída de cocaína, mas nenhuma fonte o põe em 2º lugar no mundo".
- **Passou a valer:** explicação começando por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e terminando com o que falta (Europol/EMCDDA, apreensões europeias por porto de origem, World Drug Report posterior a 2022); confiança baixa; resumo "A ONU lista Santos entre os principais portos de saída de cocaína; não foi achada fonte que o ponha em 2º no mundo". Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a própria explicação declarava que fontes pedidas no `o_que_conferir` não foram consultadas, e o relatório do UNODC usado é de 2022. É provisório de fato sem o marcador, o caso da A155 de 15/out. "Nenhuma fonte" afirmava uma ausência que a busca não provou (padrão "não foi achado" dos provisórios).

##### A144 (lote 15), resumo, explicação, divergência e prova

- **Estava:** resumo "Fontes mostram orçamento nominal maior e mais investimento em 2023, mas cortes no custeio; falta a série real"; explicação "a fatia de investimento subiu de 6,8% em 2022 para 7,4% no ano seguinte"; divergência "o orçamento nominal das Forças e a fatia de investimento subiram em 2023"; prova do Congresso em Foco "no início do governo".
- **Passou a valer:** resumo "Fontes mostram orçamento nominal maior em 2023 e mais investimento em 2024, mas cortes no custeio; falta a série real"; a explicação diz 7,4% em 2024 e que a reportagem é de 16/02/2025 e fala do ano anterior; divergência e prova ajustadas.
- **Por quê:** o texto capturado do Congresso em Foco (p15) é de 16/2/2025 e diz "No ano passado": o 7,4% é de 2024. Ano errado na tela (pergunta 7). A checagem segue provisória, com marcador e confiança baixa.

##### A156 (lote 16), número apurado

- **Estava:** "286.270 registros em 2025 (taxa de 261,7 por 100 mil mulheres)".
- **Passou a valer:** "286.270 registros em 2025 (taxa de 261,7 por cem mil mulheres)".
- **Por quê:** o validador avisava que o "100" não está em trecho nenhum. É a unidade da taxa, não um dado; escrito por extenso, o aviso some sem mudar o sentido.

##### A157 (lote 16), fontes, resumo, número apurado, data de referência e explicação

- **Estava:** só imprensa (Diário do Comércio, Extra Classe, Revista Oeste, IHU), com o relatório do MapBiomas não capturado; resumo "Segundo o MapBiomas, a Amazônia teve 15,6 milhões de hectares queimados em 2024, a maior área da série"; dado da coleção publicada em 2025.
- **Passou a valer:** entrou como N2 a ficha técnica do MapBiomas Fogo, Coleção 5 (versão 15/07/2026, captura rv6 `966d4c254781`), com o trecho "Exatamente um ano após a maior área queimada (15,8Mha)"; resumo "Segundo o MapBiomas, a Amazônia teve 15,8 milhões de hectares queimados em 2024, a maior área da série"; número apurado e data de referência na Coleção 5; a explicação registra os dois valores (15,6 na coleção anterior, 15,8 na atual). Veredito `VERDADEIRO` mantido.
- **Por quê:** METODOLOGIA §3.1, regras 1 e 2 (série histórica sem N1 ou N2, imprensa reproduzindo primária não conferida) e pergunta 5 (o dado vigente na data da fala é o da Coleção 5, publicada em julho de 2026).

##### A158 (lote 16), fontes, resumo, ressalva, número apurado, derivação, data de referência e explicação

- **Estava:** só imprensa (Diário do Comércio, Extra Classe); resumo "Em 2024 o fogo atingiu 30 milhões de hectares no país, a segunda maior área em 40 anos; o recorde foi na Amazônia"; ressalva "A área de 2024 ficou 62% acima da média histórica".
- **Passou a valer:** entrou como N2 o Relatório Anual do Fogo 2025 do MapBiomas, Coleção 5 (17/07/2026, captura rv6 `e5e53a2af2c6`), com o trecho "O maior registro ocorreu em 2007, com cerca de 30,7 milhões de hectares, seguido por [...] 2024, com 30,2 milhões de hectares"; resumo "O fogo atingiu 30,2 milhões de hectares no país em 2024, a 2ª maior área desde 1985, atrás de 2007, segundo o MapBiomas"; ressalva "Na Amazônia, 2024 teve a maior área queimada da série; no país, ficou 1,6% abaixo de 2007", com a derivação "30,7 menos 30,2, dividido por 30,7"; explicação refeita na Coleção 5. Veredito `IMPRECISO` mantido.
- **Por quê:** as mesmas regras da A157. A ressalva antiga (62% acima da média) era da coleção anterior; a nova diz ao espectador o tamanho real do erro (segundo lugar por 1,6%) e onde o recorde vale, para o card não parecer mais duro do que o dado (pergunta 8).

##### A159 (lote 16), trecho do Anuário e explicação

- **Estava:** o trecho do Anuário pulava, com `[...]`, a frase do crescimento dos estelionatos; a explicação dizia "alta de mais de 400% desde 2018" e "roubos caíram".
- **Passou a valer:** o trecho inclui "O crescimento superior a 400% desde 2018 evidencia uma profunda transformação das dinâmicas", cópia do mesmo parágrafo capturado (p16-r6); "roubos caíram" saiu da explicação, que fica com "o total de ocorrências patrimoniais segue em queda".
- **Por quê:** METODOLOGIA §3.1, regra 6: o 400% não estava em trecho. A queda dos roubos não está escrita no Anuário capturado, que diz que o total de ocorrências cai e que os furtos passaram a superar os roubos.

##### A160 (lote 16), explicação

- **Estava:** "reportagens da Gazeta do Povo e do Metrópoles que reproduzem a divulgação de 6/8".
- **Passou a valer:** "a reportagem da Gazeta do Povo, que reproduz a divulgação de 6/8".
- **Por quê:** não há fonte do Metrópoles na checagem nem captura dela; a explicação citava uma fonte que o arquivo não tem (pergunta 3).

##### A167 (lote 17), fontes e explicação

- **Estava:** três reportagens (O Liberal, Diário do Pará, Bahia Notícias) do mesmo balanço oficial da PF e da PRF de fevereiro de 2026, apresentadas como apoio independente.
- **Passou a valer:** entrou como N1 a página de notícias da Polícia Federal (captura de 16/10/2026, caso de 15/out, pasta p06), com o trecho "PF e BPFRON apreendem mais de 500 kg de maconha no Paraná [...] PF apreende quatro pistolas ocultas em caixas de som em Cascavel/PR"; a explicação declara que as três reportagens reproduzem o mesmo balanço e contam como uma fonte (regra 2 da §3.1). Veredito `FALSO` mantido.
- **Por quê:** METODOLOGIA §3.1, regras 2 e 3. Sem a fonte nova, o `FALSO` se apoiava numa só fonte de fato. A página da PF é registro primário, independente do balanço, de fiscalização na véspera da fala.

##### Para a passada de coerência, sem mudança feita

- **Régua de ranking (A158 e A142):** a A158 ficou `IMPRECISO` com 2024 a 1,6% de 2007, porque a frase afirma uma posição. Conferir se outro "o maior", "o segundo" ou "recorde" dos dois casos foi tratado do mesmo jeito quando a diferença é pequena.
- **Recordista por métrica (A155, A157, A159, A160):** A157 é `VERDADEIRO` com uma de duas métricas (área sim, focos não); A155 e A159 são `IMPRECISO` porque o recorde vale para um recorte e o total cai. A diferença declarada é total contra recorte, não métrica contra métrica. Conferir se a distinção se sustenta lida pelo espectador.
- **Frase absoluta (A166 e A167):** A167 ("não fiscaliza") é `FALSO` pela leitura literal; A166 ("não compraram arma em loja") é `VERDADEIRO` lida no contexto, com fontes só da PM do Rio e sem os estudos de desvio de armas de CAC que o `o_que_conferir` pedia. Conferir se a mesma régua de literalidade vale para as duas e para as frases absolutas de Lula no caso de 15/out.
- **Só imprensa reproduzindo primária não capturada:** A143, A145 a A150 (eventos sem número) e A166 seguem sem N1 ou N2, aceitas pela regra das redações independentes, como A032 e A140 no caso de 15/out.

### checagens/revisao/correcoes-r7.md

#### Correções da revisão r7 (lotes 18, 19, 20 e 21)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A171 a A207. O revisor não checou nenhuma delas. Foi feita **uma** busca web, atrás do que contradiria um veredito (A180, emissões de CRs de CACs); ela não contradisse e nada dela entrou. As duas fontes novas abaixo já estavam capturadas: `capturas/2026-10-16-sabatina-flavio-globo-2turno-p20` (Gazeta do Povo, `46c2805812fb`) e `capturas/2026-10-15-sabatina-lula-globo-2turno-p06` (Poder360, já usado na A189), e cada trecho, novo ou antigo, foi conferido por palavra inteira contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py`: todos achados. Os quatro lotes validam contra `esquemas/checagens.schema.json`. **Nenhum veredito mudou.** As notas por checagem estão em `revisao-r7.json`.

##### A185 (lote 19), explicação e derivação

- **Estava:** "desvio de cerca de 7% sobre quatro anos, abaixo dos 10% da régua"; derivação "44,5 meses contra 48, desvio de cerca de 7%".
- **Passou a valer:** "desvio de cerca de 8% medido sobre o período apurado (3,5 meses sobre 44,5), abaixo dos 10% da régua"; derivação "44,5 meses contra 48 ditos, desvio de cerca de 8% medido sobre o apurado (3,5 dividido por 44,5)".
- **Por quê:** pergunta 6. As contas de desvio deste caso (A011, A012, A022, A097, A120, A179) e do caso de 15/out (correção da A046 na coerência) medem sobre o valor apurado; esta media sobre o número dito. Pelas duas bases o desvio fica abaixo de 10%, e o veredito `VERDADEIRO` não muda.

##### A187 (lote 19), explicação e derivação

- **Estava:** "607,88 dividido por 189 dá cerca de 3,2 vezes: 'triplicou' confere em termos nominais", sem a conta da régua.
- **Passou a valer:** "607,88 dividido por 189 dá cerca de 3,2 vezes; 'o triplo' contra 3,2 vezes é desvio de cerca de 7% sobre o apurado, e 600 contra 607,88, de cerca de 1%, os dois abaixo da régua de 10% do §2.2"; nova derivação "cerca de 7%" (de "607,88 dividido por 189, contra o triplo dito").
- **Por quê:** pergunta 6. O VERDADEIRO dependia da régua de 10% e ela não estava escrita. O veredito não muda.

##### A192 (lote 20), fontes e explicação

- **Estava:** duas fontes (SBT News e Times Brasil), que reproduzem o mesmo documento da PF, não capturado.
- **Passou a valer:** entrou o Poder360, "Saiba quem é Márcio Canella, preso em operação contra lavagem de dinheiro" (15/10/2026), com o trecho "A ação mira uma organização criminosa suspeita de usar postos de combustíveis na Região Metropolitana do Rio para lavar dinheiro."; a explicação registra que é apuração própria do dia da prisão, a mesma fonte da A189.
- **Por quê:** pergunta 4 e regra 2 da §3.1: as duas fontes antigas remontam à mesma peça não capturada. A nova confirma o objeto da operação sem depender dela. O veredito `VERDADEIRO` (conteúdo da suspeita, não culpa) segue a régua da A110 do caso de 15/out e da A112 deste caso.

##### A193 (lote 20), fontes e explicação

- **Estava:** o "originalmente o seu candidato" se apoiava no acordo de Jair Bolsonaro com Bacellar (Jovem Pan, 2025) e na busca de outros nomes por Flávio (Diário do Rio).
- **Passou a valer:** entrou a Gazeta do Povo, "PL define chapa pura no Rio de Janeiro após desembarque de aliados" (04/08/2026), com o trecho "Douglas Ruas assume candidatura após troca no grupo de Flávio Douglas Ruas passou a ser o nome do PL para disputar o governo do Rio depois que Rodrigo Bacellar deixou a corrida eleitoral após ser preso em operações da Polícia Federal."; a explicação cita a "troca no grupo de Flávio".
- **Por quê:** pergunta 3. O melhor argumento contra o card é que o acordo documentado era do pai, não de Flávio; a página, já capturada e não usada, liga Bacellar ao grupo de Flávio. O veredito `VERDADEIRO` e a ressalva não mudam.

##### Provisórios conferidos, sem mudança

A173, A174, A191, A194, A199, A200 e A201: a explicação começa pelo marcador exato ("Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:") e a confiança é baixa. O que falta em cada um está na nota de `revisao-r7.json`. Nenhum veredito provisório sem marcador foi achado nos quatro lotes.

### checagens/revisao/rodada2-parte1.md

#### Rodada 2 · parte 1 (17/out/2026)

Refeitas, com busca, as sete checagens que saíram da rodada 1 com o marcador "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:". Quem fez esta parte não tinha checado essas alegações. O marcador saiu do início da explicação, e cada explicação diz agora que foi refeita na rodada 2 de 17/out/2026.

- Buscas web usadas: 9 (limite da parte: 9).
- Captura: pedido em `checagens/pedidos-captura/rodada2-parte1.json`, saída em `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2parte1` (26 URLs, todas com status 200). Os trechos das fontes que já vinham da rodada 1 saem das pastas de captura deste caso (TCU e PGFN em `-p03` e `-p03-r2`, Gastômetro de agosto em `-rv2`) e, para o Agora RN, de `capturas/2026-10-15-sabatina-lula-globo-2turno-p13`.
- Conferência: os quatro lotes editados (01, 02, 03 e 05) validam contra `esquemas/checagens.schema.json`; cada `trecho` foi achado, por palavra inteira e com espaços normalizados, no texto capturado da própria URL; todo número do `resumo`, da `ressalva` e do `numero_apurado` está num trecho, numa derivação ou na data de referência.
- Nenhuma ficou provisória.

| id | rodada 1 | rodada 2 | por quê |
|---|---|---|---|
| A008 | INSUSTENTAVEL (provisório) | IMPRECISO | Achado o vídeo de Lula "Se o Flávio vence, você perde", que ligava a vitória de Flávio a perdas na aposentadoria e no reajuste (retirado por decisão liminar do TSE de 8/out; Investidor10, Mais Goiás, A Crítica), e o vídeo dos deputados aliados Janones e Lindbergh sobre "reduzir o valor da aposentadoria" (íntegra da decisão do TSE). A essência confere; "acabaria com as aposentadorias" amplia o registrado (perdas e fim do reajuste real). Confiança média. |
| A009 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | As quatro decisões do TSE de 8/out sobre peças de Lula, Janja e aliados não tratam de servidores; BBC/A Gazeta e IstoÉ registram que a atribuição sobre concursos circulou "nas redes sociais", sem autor. Busca concluída, confiança de baixa para média. |
| A010 | INSUSTENTAVEL (provisório) | IMPRECISO | Achado vídeo dos deputados Janones (Rede) e Lindbergh Farias (PT) atribuindo a Flávio a privatização da Petrobras, retirado pelo TSE (íntegra da decisão, Poder360, Investidor10). O autor é aliado, não Lula nem a campanha, e Banco do Brasil e Caixa não aparecem com autor. Confiança média. |
| A015 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Procurados de novo declarações nominais de economistas apoiadores e um levantamento de opinião: nenhum dos dois achado. Acrescentado que a própria equipe do candidato estudou mexer em aposentadorias, BPC e pisos (Folha, no Diario de Pernambuco). Mesma régua da A155 do caso de 15/out. Confiança de baixa para média. |
| A020 | INSUSTENTAVEL (provisório) | IMPRECISO | O total da União é de cerca de 761 mil imóveis (TCU, Lista de Alto Risco), o mesmo da A021, como pedia a revisão r1. "Mais de 30 mil" lido com rigor fica cerca de 25 vezes abaixo: régua de 10% do §2.2. Saíram as cifras de 2018. Confiança média. |
| A023 | INSUSTENTAVEL (provisório) | VERDADEIRO | Achado o estoque oficial: R$ 3 trilhões em 2024 (PGFN em Números 2025), confirmado de forma independente pela análise do JOTA sobre a LDO ("praticamente R$ 3 trilhões"). A edição de 2026 não traz o estoque, então este é o último publicado na data da fala. O R$ 2,1 trilhões da rodada 1 é a parcela em cobrança. Ressalva: R$ 1 trilhão negociado, garantido ou suspenso, e só 6,6% de maior chance de recuperação. Confiança média. |
| A047 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Achado o Gastômetro do Estadão mais perto da fala: R$ 354 bi em 14/10 (desvio de 1,1%). Fica INSUSTENTAVEL, agora como veredito final: o próprio painel soma crédito, subsídio e renúncia e "não representa apenas dinheiro já desembolsado", e a soma é de um jornal, sem fonte N1 ou N2 (§3.1, regra 1); a Folha, com outro critério, dava R$ 193,8 bi. Confiança de baixa para média. |

### checagens/revisao/rodada2-parte2.md

#### Rodada 2, parte 2 (17/out/2026)

Refeitos, com busca, os vereditos provisórios A062 (lote 07), A071 e A072 (lote 08), A086 (lote 09), A095 (lote 10) e A113 (lote 12). Nove chamadas de WebSearch/WebFetch, o limite desta parte. Capturas novas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2parte2` (pedido `checagens/pedidos-captura/rodada2-parte2.json`) e `-r2parte2-r2` (pedido `rodada2-parte2-r2.json`, só o decreto do Planalto, que não abriu). Todos os trechos dos seis ids foram conferidos por palavra inteira contra o texto capturado da sua URL, com a função de `ferramentas/conferir-trechos.py`, e os cinco lotes validam contra `esquemas/checagens.schema.json`.

| id | rodada 1 | rodada 2 | por quê |
|---|---|---|---|
| A086 | INSUSTENTAVEL (provisório) | VERDADEIRO | Faltava fonte N1. O acordo é em dólares (US$ 24 milhões, US$ 23,9 milhões na planilha; reportagem original do Intercept, capturada) e a conversão, que é a parte divergente, foi refeita com o dólar do Banco Central (N1): R$ 145,1 milhões em 21/01/2025, R$ 134,0 milhões na média de 2025, R$ 122,0 milhões no dia da fala. O "134" fica a menos de 10% de todas (7,6% contra a de janeiro de 2025). Nota do revisor r3 atendida: o valor repassado não aparece mais com os US$ 10,6 milhões de maio de 2025. Mesmo veredito, mesmas fontes e mesma régua da A072. |
| A072 | INSUSTENTAVEL (provisório) | VERDADEIRO | Mesma afirmação da A086 ("134 que o senhor pediu"), mesmo texto de tela, mesmas fontes e derivações. |
| A071 | INSUSTENTAVEL (provisório) | VERDADEIRO | Os sete repasses documentados na data da fala (seis da planilha do Intercept, com datas e valores, e o de 16/09/2025 do relatório do Coaf obtido pela piauí) somam US$ 12,3 milhões; convertidos pelo dólar do Banco Central de cada data, R$ 69,8 milhões. A mesma conta até maio dá R$ 61,0 milhões, o valor publicado pelo Intercept, o que confirma o método. "Quase 70" fica a 0,3%. Os R$ 65 milhões da imprensa ("mais de 65" na piauí) usaram outra cotação; vão na ressalva e na divergência. |
| A062 | INSUSTENTAVEL (provisório) | IMPRECISO | Achada a fonte N2: estudo do Movimento Pessoas à Frente e da República.org, R$ 20,01 bilhões pagos acima do teto em 12 meses (ago/2024 a jul/2025), nos três Poderes; ainda a referência em maio de 2026 (nota da Coalizão de Combate aos Supersalários). Nenhuma fonte dá R$ 24 bilhões (busca pela frase exata). Não há conta posterior às regras do STF de 25/03/2026. Desvio de 20%, acima da régua de 10% (e no limite de 20% que valeria até para estimativa com intervalo). |
| A095 | VERDADEIRO (provisório, marcador do revisor r4) | VERDADEIRO | A metade que faltava (regras de transparência na compra de patrocínio) agora tem fonte: Lei 4.680/1965 (N1, preços de tabela), Normas-Padrão do CENP (N2, lista de preços única e pública) e Meio & Mensagem (obrigação legal de lista única e pública para todo veículo). A ressalva da tela diz que a lista da própria Globo não foi consultada e que o card não avalia o cumprimento na prática. Confiança passou de baixa a média. A `citacao_card` não foi mexida (é campo da alegação). |
| A113 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL (continua provisório) | Cinco buscas ("26 das 27 superintendências", a exceção do Rio Grande do Sul, as "39 trocas", notas de apoio de 2026, Diário Oficial de 18/01/2023) não acharam o levantamento original nem o Diário Oficial; o Conjur recusou o robô de novo (403). Sem fonte N1 ou N2, o veredito amarelo (a tendência, contra os 18 documentados) não pode sair. Marcador exato mantido, confiança baixa, explicação atualizada com o que esta rodada fez e o que falta. |

Buscas usadas: nove (Dark Horse 1; penduricalhos 2; superintendências da PF 5; patrocínio e lista de preços 1). A captura de URLs conhecidas (Banco Central, Planalto, páginas citadas por páginas já capturadas) não contou como busca.

### checagens/revisao/rodada2-parte3.md

#### Rodada 2 · parte 3 (17/out/2026)

Refeitas, com busca, as sete checagens que saíram da rodada 1 com o marcador "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" (A161 e A162 do lote 17, que estão num corte do vídeo, primeiro; depois A151, A152 e A153 do lote 16 e A142 e A144 do lote 15). Quem fez esta parte não tinha checado essas alegações. Nas seis que fecharam, o marcador saiu do início da explicação, e a explicação diz que a checagem foi refeita na rodada 2 de 17/out/2026. A A161 continua provisória, com o marcador exato.

- Buscas web usadas: 10 (limite da parte: 10). A161: 3; A162: 2; A151: 1; A152 e A153: 1; A142: 1; A144: 1.
- Captura: pedidos em `checagens/pedidos-captura/rodada2-parte3.json` e `-r2` a `-r6`, saídas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2parte3` e `-r2` a `-r6`. As fontes que já vinham da rodada 1 saem das pastas `-p15`, `-p16`, `-p16-r2`, `-p17`, `-p17-r2` e `-p17-r3`.
- Conferência: os lotes 15, 16 e 17 validam contra `esquemas/checagens.schema.json`; cada `trecho` foi achado, por palavra inteira e com espaços normalizados (pedaço a pedaço quando há `[...]`, por número nas respostas JSON do IBGE e do Banco Mundial), no texto capturado da própria URL; todo número do `resumo`, da `ressalva` e do `numero_apurado` está num trecho, numa derivação, na fala ou na data de referência.
- Continua provisória: A161 (ver abaixo).

| id | rodada 1 | rodada 2 | por quê |
|---|---|---|---|
| A161 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL (provisório) | Conferidos os quatro quadrimestres de 2024 e 2025 (854.150, 830.525, 973.330 e 942.049 fechamentos): sobem nos dois anos, e no 2º quadrimestre cada ano do governo atual é o maior da série desde 2014; no 1º quadrimestre o pico é 2018 (cancelamento em massa de MEIs). Os boletins anuais de 2024 e 2025 (3º quadrimestre) e o do 1º quadrimestre de 2026, que diriam se há recorde no ano, não foram achados: 404 no gov.br em cerca de 40 endereços tentados, sem cópia no Poder360, e três buscas sem o total anual. Corrigida a leitura do Diário do Comércio ("queda de 13,4%"), que contradiz a base de 2024 (alta de cerca de 14%, divergência declarada). Confiança baixa, marcador mantido. |
| A162 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Capturada a base do país parceiro (informe oficial do MIC de dez/2025, Infonegocios e Última Hora). O recorde que existe é de programas de maquila aprovados em 2024 (36, o maior desde a criação do regime), de todas as origens; não há série por origem, e o único corte por período de empresas brasileiras (Poder360: 40 a partir de 2023, 26 em 2021 e 2022) não mostra pico. Programa não é empresa nova, e as empresas não "deixam" o Brasil (Aos Fatos; CNIME). Confiança média. |
| A151 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Abertas as 91 portarias de 2026 da lista da Senatran que faltavam (além das já abertas na p16-r4): nenhuma trata da Faixa Azul de São Paulo, nem renovação nem negativa; a busca só achou a prorrogação de 2025. O documentado é que o governo atual autorizou e prorrogou a Faixa Azul até 31/03/2026; a situação na data da fala segue sem registro. Confiança média. |
| A152 | INSUSTENTAVEL (provisório) | IMPRECISO | Achado o pedido: operação de US$ 205,3 milhões com o BID para o Avança Saúde II. Ficou parado na Casa Civil desde abril de 2026 (Folha de Pernambuco; Diário do Transporte, com documentos do SEI), com o governo dizendo que seguia o trâmite regular; a Presidência enviou ao Senado em 12/08 (MSF 41/2026), o Senado autorizou em 13/08 (PRS 35/2026) e a Fazenda assinou a garantia em 25/08/2026, antes da fala. A demora confere; "negou"/"não dava" não. Confiança média. |
| A153 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | A Prefeitura pediu liminar ao STJ contra a Fazenda em 25/08/2026, e a garantia foi assinada horas depois, pela própria Fazenda, sem decisão judicial registrada (Diário do Transporte). A ação existiu; o "teve que" (que a Justiça foi o que liberou o dinheiro) não se sustenta, e é ação sem decisão definitiva (etica-e-risco §5). Segunda fonte independente sobre o pedido ao STJ não foi achada, o que está declarado. Confiança média. |
| A142 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Consultada a análise conjunta EMCDDA (EUDA) e Europol sobre o mercado de cocaína, que o critério pedia: Brasil, Equador e Colômbia são os principais países de saída para a Europa, sem ranking de portos. A página do World Drug Report 2025 não traz ranking de portos, e a busca dirigida não achou fonte que ponha Santos em segundo nem em outra posição. Confiança média. |
| A144 | INSUSTENTAVEL (provisório) | IMPRECISO | Achada a série oficial do Ministério da Defesa (empenhado de 2017 a 2025, versão de 30/09/2026) e deflacionada pelo IPCA (IBGE): queda real de 4,2% de 2022 a 2025, contra 11,6% de 2019 a 2022; em proporção do PIB (Banco Mundial/SIPRI), 1,05% em 2022, 0,99% e 0,96% em 2023 e 2024, e 1,05% em 2025. Redução pequena no governo atual, com a maior parte antes dele: período errado (régua do §2.2). Capacidade não medida. Confiança média. |

### checagens/revisao/rodada2-parte4.md

#### Rodada 2 · parte 4 (17/out/2026)

Refeitas, com busca, as sete checagens que saíram da rodada 1 com o marcador "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" (A173 e A174 no lote 18; A191, A194, A199 e A200 no lote 20; A201 no lote 21). Quem fez esta parte não tinha checado essas alegações. O marcador saiu do início da explicação, e cada explicação diz agora que foi refeita na rodada 2 de 17/out/2026. O que faltava em cada uma foi tirado da explicação provisória e da nota do revisor r7 (`revisao-r7.json`).

- Buscas web usadas: 9 (limite da parte: 9).
- Captura: pedidos em `checagens/pedidos-captura/rodada2-parte4.json` e `rodada2-parte4-r2.json` a `-r5.json`, saídas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2parte4` e `-r2parte4-r2` a `-r2parte4-r5` (28 URLs; só a do Midiamax veio com erro 520 e não foi usada; a captura do site da Quaest, em `-r2parte4-r4`, não trouxe o relatório). Os trechos que já vinham da rodada 1 saem das pastas `-p20` e `-p21` deste caso.
- Conferência: os três lotes editados (18, 20 e 21) validam contra `esquemas/checagens.schema.json`; cada `trecho` foi achado, por palavra inteira e com espaços normalizados, no texto capturado da própria URL; todo número do `resumo`, da `ressalva` e do `numero_apurado` está num trecho, numa derivação, na frase ou na data de referência.
- Nenhuma ficou provisória. Todas saem com confiança média.

| id | rodada 1 | rodada 2 | por quê |
|---|---|---|---|
| A173 | INSUSTENTAVEL (provisório) | VERDADEIRO | A pesquisa é a Pesquisa Nacional de Segurança e Tecnologia, da Quaest com a Pax (12 a 15/09), não a eleitoral. Numa bateria sobre medidas efetivas para melhorar a segurança pública, restringir o acesso da população a armas teve 58% de aprovação e 39% de reprovação (Exame, Agenda do Poder, Brasil em Folhas). As reportagens reproduzem o mesmo relatório, não localizado no site da Quaest (regra 2 da §3.1 declarada); mesma régua da A043 do caso de 15/out. |
| A174 | INSUSTENTAVEL (provisório) | VERDADEIRO | Na mesma pergunta, 62% entre as mulheres, 58% no total e 55% entre os homens (Exame, Brasil em Folhas); margem de 3 pontos por sexo (Metrópoles). A diferença para o total, 4 pontos (derivação), passa da margem do recorte. |
| A191 | INSUSTENTAVEL (provisório) | VERDADEIRO | Achados os vídeos: o Poder360 registra vídeo de apoio publicado por Flávio com Canella no Instagram em 22/04/2026, e o Estadão Conteúdo (no O Liberal) diz que Flávio "chegou a gravar vídeos" chamando Canella de "competente" e "amigo" na pré-candidatura ao Senado. |
| A194 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Achado o que faltava sobre a data da fala: a cobertura de 16 e 17/out (SBT News, Agenda do Poder) trata Bacellar como aliado preso, e não há notícia de soltura. Fica INSUSTENTAVEL como veredito final: a ordem de prisão de março cita vazamento para atrapalhar operação contra o CV, e a denúncia da PGR é por obstrução; "liderança do núcleo político" é a caracterização do relatório da PF; é apuração sem julgamento, com a defesa negando (etica-e-risco §5). Confiança de baixa para média. |
| A199 | INSUSTENTAVEL (provisório) | VERDADEIRO | Segunda fonte independente: a Folha (Folhapress, no Bahia Notícias, 13/10) diz que Flávio já tinha anunciado Lottenberg e estudava divulgar mais dois ou três ministros antes do 2º turno. Com o BP Money ("primeiro nome anunciado") e o anúncio de 28/08 (A198), a precedência se sustenta. |
| A200 | INSUSTENTAVEL (provisório) | VERDADEIRO | Achadas falas de 2021 sobre a compra: ao Correio Braziliense (junho), "a tal da diplomacia da vacina aconteceu tarde" e veio "com muito negacionismo", com falta de compromisso na "busca das vacinas"; à Jovem Pan, vacinação "lenta" (janeiro) e atrasada pela "obtenção de novas doses" (abril). Ressalva: ele nem sempre nomeia o governo federal na frase. |
| A201 | INSUSTENTAVEL (provisório) | INSUSTENTAVEL | Mais duas buscas dirigidas e oito páginas capturadas não acharam a citação entre aspas nem o veículo e a data da entrevista; a Gazeta do Povo repete o teor na cobertura da sabatina, sem citar fonte, e não foi contada. O teor (crítica à demora da vacinação) está documentado e foi para a A200. Fica INSUSTENTAVEL como veredito final, porque a busca na web aberta foi esgotada; a entrevista pode estar em acervo fechado (Globo, Folha, Estadão). Confiança de baixa para média. |

### checagens/revisao/correcoes-rodada2.md

#### Correções da revisão adversarial da rodada 2

Revisão adversarial por IA, em passada separada, feita em 17/out/2026 sobre as 27 checagens que a rodada 2 refez com busca (partes 1 a 4). O revisor não checou nenhuma delas. Não fez nenhuma busca web: as mudanças saem só das capturas já feitas, da régua da METODOLOGIA e do validador. Três vereditos mudaram (A062, A173 e A174, os três para INSUSTENTAVEL), e um trecho foi completado sem mudar o veredito (A153). As notas de cada id estão em `revisao-rodada2.json`.

##### Antes da revisão: os lotes 07 a 12 tinham voltado ao estado provisório

- **O que foi achado:** às 14:15:55 de 17/out, um mesmo processo regravou os lotes 07 a 12 e 15 a 17 (diferença de milissegundos entre os arquivos). Os lotes 15 a 17 saíram com a parte 3, mas os lotes 07 a 12 voltaram ao texto da rodada 1: A062, A071, A072, A086 e A113 com o marcador de provisório, e A095 com o marcador do revisor r4. A parte 2 tinha gravado os lotes por volta de 13:53 e o `checagens-sabatina-completa.json` às 13:54, e só ele guardava a versão da parte 2.
- **O que foi feito:** as seis checagens da parte 2 foram copiadas do `checagens-sabatina-completa.json` de 13:54 de volta para os lotes 07, 08, 09, 10 e 12. As outras checagens desses lotes já eram iguais às do arquivo consolidado. Cópia dos lotes antes da restauração e do consolidado de 13:54 ficaram no scratchpad do revisor.
- **Depois das correções abaixo,** o `checagens-sabatina-completa.json` foi remontado a partir dos lotes com `ferramentas/lotes-de-debate.py checagem-juntar` (207 checagens). Antes disso ele não tinha as partes 3 e 4.

##### A062 (lote 07)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`, `derivacoes` (o `como`), e o `trecho` e a `prova` da fonte N2 (estudo do Movimento Pessoas à Frente e da República.org)
- **Estava:** `IMPRECISO`; resumo "Estudo estima R$ 20 bilhões por ano pagos acima do teto nos três Poderes; o número dito fica 20% acima"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Estudo estima ao menos R$ 20 bi por ano pagos acima do teto nos três Poderes; R$ 24 bi não aparece em fonte"; ressalva "O estudo trata os R$ 20 bi como piso e cobre agosto de 2024 a julho de 2025, antes das regras do STF de março de 2026"
- **Por quê:** o IMPRECISO media os R$ 24 bilhões contra os R$ 20 bilhões como se fossem o total, mas a própria fonte N2 diz que o gasto com supersalários "é de pelo menos 8 bilhões de dólares ao ano" (o equivalente aos cerca de R$ 20 bilhões), que o estudo "aborda um subgrupo do universo de servidores" e que é "difícil dimensionar a subnotificação"; a Itatiaia e a Coalizão, que o reproduzem, escrevem "ao menos R$ 20 bilhões". Desvio de 20% sobre um piso não prova erro: é a leitura de piso aplicada a "mais de 15 milhões" na A192 do caso 2026-10-15-sabatina-lula-globo-2turno (perguntas 4 e 6: a primária ganha das secundárias, que tratam o valor como total). Sem fonte para os 24 e sem fonte que os contradiga, a régua do §2.2 dá INSUSTENTAVEL ("número que não existe em fonte nenhuma"). Os trechos novos foram conferidos no texto capturado em `-r2parte2`.

##### A173 (lote 18)

- **Campos:** `veredito`, `resumo`, `ressalva`, `numero_apurado`, `explicacao`
- **Estava:** `VERDADEIRO`; resumo "Na Quaest com a Pax de setembro, 58% apoiam restringir o acesso a armas como medida para a segurança; 39% rejeitam"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão 58% a favor de restringir armas na Quaest com a Pax de setembro; o relatório do instituto não foi achado"; ressalva "É a pesquisa da Quaest com a Pax, não a eleitoral; os 58% a favor e os 39% contra vêm só de reportagens"
- **Por quê:** as quatro fontes são reportagens (N4) que reproduzem o mesmo relatório da Quaest, e a própria checagem diz que o relatório não foi localizado. A regra 2 da §3.1 só aceita fontes N3/N4 quando a primária que citam foi conferida, e a regra 1 pede N1 ou N2 para afirmação com número ("a maioria"). O precedente citado pela rodada 2, a A043 do caso de 15/out, tinha o Datafolha como fonte N2; todas as outras checagens de pesquisa com veredito colorido nos dois casos de outubro (A003, A046, A052 e A174 de 15/out; A039 e A197 deste caso) têm o relatório do instituto. E é a régua aplicada ao candidato neste caso: número reproduzido só por imprensa, sem N1 ou N2, ficou INSUSTENTAVEL (A047, A113) (pergunta 6). Nada contradiz a frase: se o relatório da Pesquisa Nacional de Segurança e Tecnologia for capturado e confirmar a pergunta e o percentual, o veredito volta a VERDADEIRO.

##### A174 (lote 18)

- **Campos:** `veredito`, `resumo`, `numero_apurado`, `explicacao`
- **Estava:** `VERDADEIRO`; resumo "Entre as mulheres, 62% apoiam restringir o acesso a armas, contra 58% no total e 55% entre os homens"
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão 62% entre as mulheres, contra 58% no total, na Quaest com a Pax; o relatório do instituto não foi achado"
- **Por quê:** o mesmo motivo da A173, e mais um: a alegação é do tipo `comparacao`, e o validador (`passo8_validar`, regra 1 da §3.1) reprova veredito colorido desse tipo sem fonte N1 ou N2. Com VERDADEIRO a validação do caso tinha um erro a mais; com INSUSTENTAVEL fica o aviso de que a explicação diz o que faltou, e ela diz (o relatório da Quaest). Ressalva da margem de 3 pontos mantida.

##### A153 (lote 16)

- **Campos:** `trecho` e `prova` da fonte Diário do Transporte
- **Estava:** trecho sem a data; o resumo diz "em 25 de agosto", e o validador avisava que o número 25 não estava em trecho nenhum desta checagem
- **Passou a valer:** o trecho começa por "o Governo Federal autorizou na noite desta terça-feira, 25 de agosto de 2026, a concessão das garantias da União [...]", texto da mesma página, já usado na A152 e conferido na captura `-r2parte3-r2`
- **Por quê:** número de tela precisa de trecho (regra 6 da §3.1). O veredito não muda.

### checagens/revisao/correcoes-coerencia.md

#### Correções da passada de coerência entre lotes

Passada separada, em 17/10/2026, depois das revisões r1 a r7 (lote a lote) e da rodada 2, seguindo `skills/revisar-checagem.md` (pergunta 6: a mesma régua nos dois lados da mesa, entre lotes e entre casos), `docs/METODOLOGIA.md` §2 e §3 e `.cursor/rules/etica-e-risco.mdc`. O revisor não checou nem revisou nenhum lote deste caso antes. Comparação feita com o caso de Lula de 15/out (`checagens-sabatina-completa.json`) e com os dois casos de Flávio de 28/ago. **Sem busca web** (zero de duas) e **sem fonte nova**: nenhum trecho entrou ou mudou, e o validador confere 735 de 735 trechos na página capturada. As 57 fontes com data de consulta de 16/out (aviso "consultada antes da extração") têm captura com a mesma data. A113 e A161 seguem provisórias e não foram tocadas.

Depois da junção, o validador reprova só por A113 e A161 (confiança baixa sem revisão registrada, que some com o registro). Os erros de A114 e A138 e os avisos de A016, A047, A078, A085, A097 e A179 foram resolvidos nos lotes. Os lotes mexidos (02, 04, 05, 07, 08, 09, 10, 11, 12, 14, 18, 19, 20, 21) passam no `esquemas/checagens.schema.json`.

**Mudaram cinco vereditos:** A078, A085, A114 e A138 passaram a `INSUSTENTAVEL` pela regra 1 da §3.1, a mesma régua para os dois lados; A194 passou de `INSUSTENTAVEL` a `IMPRECISO`. Mudaram ainda a confiança de nove checagens, o texto de A094 e o formato de seis campos que o validador acusava. As notas por checagem, inclusive dos pares examinados e mantidos, estão em `revisao-coerencia.json`.

##### A114 (lote 12), veredito, resumo, número apurado e explicação · par A113, A037; A018 e A040 do caso de 15/out

- **Estava:** `IMPRECISO`; resumo "Em maio de 2020 o novo diretor da PF trocou seis superintendentes num só ato, entre eles o do Rio, o mais questionado"; quatro fontes N4. O validador dava erro: tipo `comparacao` sem fonte N1 ou N2.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Imprensa registra seis superintendentes da PF trocados num só ato em maio de 2020; o Diário Oficial não foi conferido"; a explicação diz que a leitura das fontes aponta IMPRECISO, mas que falta o Diário Oficial de 25/05/2020, e que não é FALSO porque nada inverte a comparação.
- **Por quê:** número só com imprensa, sem a primária capturada. É a régua da A113 (as 27 trocas atribuídas a Lula, `INSUSTENTAVEL` pelo mesmo motivo), da A037 e das A018 e A040 do caso de 15/out. Não havia N1 ou N2 já capturada: a varredura das capturas dos dois casos não achou o Diário Oficial de 2020.

##### A138 (lote 14), veredito, resumo, ressalva, número apurado e explicação · par A078, A114

- **Estava:** `VERDADEIRO`, desde a revisão r5; resumo "Eduardo esteve com o presidente do Parlamento de Israel em maio de 2016; os contatos com a direita dos EUA vêm de 2018"; cinco fontes N4. O validador dava erro: tipo `serie_historica` sem fonte N1 ou N2.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Times of Israel e Folha registram visita de Eduardo a Israel em maio de 2016; não há registro oficial conferido"; ressalva "Os contatos com a direita dos EUA começam em 2018; a viagem de 2016 só aparece em reportagens"; a explicação diz que a leitura das reportagens daria VERDADEIRO, que nada contradiz o prazo e que falta o registro oficial da viagem (missão da Câmara ou agenda do Knesset).
- **Por quê:** a alegação é numérica e todas as fontes são imprensa; nenhuma N1 ou N2 sobre a viagem de 2016 estava capturada (varredura das capturas dos quatro casos). A mesma régua foi aplicada à A078 da entrevistadora, para não deixar um lado da mesa com régua mais dura.

##### A078 (lote 08), veredito, resumo, número apurado e explicação · par A138

- **Estava:** `VERDADEIRO`; resumo "PF e Intercept registram o fundo sem atividade por quase quatro anos, até a 1ª remessa para o filme em 2025"; número apurado com "24/11/2020" (aviso do validador: "24" e "11" fora de trecho).
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Intercept e relatório da PF falam em quase quatro anos sem atividade; o registro do fundo não foi conferido"; número apurado "quase quatro anos sem atividade pública (registro em novembro de 2020; primeira remessa em 13/02/2025), segundo o Intercept e o relatório da PF"; ressalva mantida.
- **Por quê:** é o par da A138 do lado da entrevistadora: um prazo em anos sustentado só por imprensa. Aqui a fonte é ainda mais fraca, porque o relatório da PF reproduzido por O Povo e TVT News cita a própria reportagem do Intercept, e as três fontes têm, para o prazo, uma origem só (regra 3 da §3.1). Com a A138 em `INSUSTENTAVEL` e esta em `VERDADEIRO`, o mesmo tipo de afirmação teria réguas diferentes dos dois lados da mesa. Ver "Para o autor", item 1.

##### A085 (lote 09), veredito, resumo, número apurado e explicação · par A090, A173, A174; A126 do caso de 15/out

- **Estava:** `VERDADEIRO`; resumo "Perícia contratada pela produtora Go Up declarou custo de US$ 13,3 milhões, pouco mais de R$ 75 milhões"; número apurado começando por "US$ 13,3 milhões" (aviso do validador: unidade diferente da do número dito); a explicação invocava a regra 2 da §3.1 sem a primária conferida.
- **Passou a valer:** `INSUSTENTAVEL`; resumo "Reportagens dão US$ 13,3 milhões, pouco mais de R$ 75 milhões, no laudo da produtora; o laudo não é público"; número apurado "R$ 75,1 milhões no Correio da Manhã; US$ 13,3 milhões, pouco mais de R$ 75 milhões, no Metrópoles (via A Tarde); laudo não conferido"; ressalva mantida. A A086, que cita o valor numa conta lateral, passou a dizer "atribuído à perícia pelas reportagens".
- **Por quê:** é afirmação de valor, e o laudo, anexado a inquérito, não foi conferido; a regra 2 só aceita imprensa no lugar da primária conferida, e a revisão r3 já apontava isso. A A090 do candidato, na mesma situação (valores de mensagens de Vorcaro lidas pela imprensa num inquérito não público), ficou `INSUSTENTAVEL` "e não IMPRECISO, que exigiria fonte N1 ou N2", e a r3 registrou que pela régua da A085 ela seria IMPRECISO. As A173 e A174 da própria entrevistadora (percentuais da Quaest só em reportagens) e a A126 do caso de 15/out (estudo da FGV só na imprensa) também são `INSUSTENTAVEL`. A diferença de tipo na extração (atribuição contra valor monetário) não muda a regra 1, que vale para afirmação que envolve valor.

##### A194 (lote 20), veredito e explicação · par A192; A089, A098 e A110 do caso de 15/out

- **Estava:** `INSUSTENTAVEL`, pela §5 de etica-e-risco (fato em apuração).
- **Passou a valer:** `IMPRECISO`; resumo e ressalva mantidos ("Bacellar segue preso desde março por suspeita de vazar operação contra o CV; a PF o descreve como líder político"); a explicação diz que o veredito trata dos atos formais (a prisão e o relatório da PF), não do mérito, que segue em apuração.
- **Por quê:** a A192, da mesma entrevistadora e do mesmo bloco, descreve as suspeitas de uma representação formal da PF e teve veredito sobre o enunciado (`VERDADEIRO`); as A089, A098 e A110 de 15/out fizeram o mesmo com a existência e a data de inquéritos. Pela mesma régua, a frase da A194 tem os dois atos documentados (ele está preso; a PF o descreve como líder do núcleo político), mas liga a prisão ao motivo errado: o fundamento formal é o vazamento. É o "certo, com recorte errado" do §2.2. A A196 (Castro "enrolado", igual à A076 de 15/out, "implicado") e a A082 seguem `INSUSTENTAVEL` porque qualificam o envolvimento, que é o mérito.

##### A094 (lote 10), resumo, ressalva e explicação · par A095, A084, A093

- **Estava:** resumo "Áudio publicado pela Veja cita os dois filmes e relato de R$ 30 milhões; autenticidade e pagamento sem confirmação"; ressalva "A fala sobre os filmes consta do áudio publicado; o pagamento e a legalidade do patrocínio ao Dark Horse seguem em apuração"; a explicação apoiava o `INSUSTENTAVEL` em três frentes, duas delas sobre a verdade do conteúdo (pagamento, legalidade).
- **Passou a valer:** resumo "Áudio publicado diz que o filme de Lula foi por fora e o de Flávio, patrocínio; valor e autenticidade sem confirmação"; ressalva "Os R$ 30 milhões não estão no trecho transcrito do áudio; a nota oficial da defesa não reconhece o material"; a explicação checa o que o áudio diz e a autoria. Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a frase é atribuição ("o que ele fala nesse áudio"). A A095, da entrevistadora, foi checada como norma, e não como cumprimento da norma; a A093 trata "só do que a defesa declarou"; a A084, sobre o mesmo valor, se apoia na divergência entre O Povo e Estadão sobre o valor estar na gravação. A A094 julgava também o conteúdo do áudio. Agora as quatro usam o mesmo critério: checa-se o que foi dito no registro citado, não se o que ele diz é verdade.

##### A040, A045, A065, A106, A108, A189, A195, A198 (entrevistadora) e A202 (candidato), confiança

- **Estava:** confiança alta, com todas as fontes N4.
- **Passou a valer:** confiança média. Vereditos mantidos.
- **Por quê:** o esquema e a skill `checar-alegacao` definem alta como "fonte N1 direta e inequívoca"; o resto do caso segue isso. Para comparar: a A071 de 15/out (Dino indicado por Lula) tem fonte N1 (Planalto), e a A065 daqui (Nunes Marques indicado por Bolsonaro) só imprensa. O caso de 15/out tem 17 checagens com confiança alta sem N1 (ver "Para o autor").

##### A016 (lote 02), número apurado e ressalva · aviso do validador

- **Estava:** número apurado "1,5% do PIB, cerca de R$ 190 bilhões (Daniella Marques); ..." e ressalva "Integrantes da campanha evitam cravar o valor, e ainda não há plano completo com os gastos a cortar".
- **Passou a valer:** número apurado "R$ 190 bilhões, cerca de 1,5% do PIB (Daniella Marques); discurso de corte em torno de R$ 200 bilhões"; ressalva "A coordenadora falou em cerca de R$ 190 bi; a campanha evita cravar o valor e não tem plano completo de cortes".
- **Por quê:** o validador comparava 200 com 1,5 e acusava 13.233% de desvio; com o valor em reais na frente, compara 200 com 190 (5%), e a ressalva de um `VERDADEIRO` arredondado tem que mostrar o valor apurado (§2.2). A A016 trata de falas públicas da campanha, cujo registro é a própria fala relatada pela imprensa; por isso não recebeu a régua da A085, que trata de documento não público.

##### A097 (lote 10) e A179 (lote 18), ressalva · aviso do validador

- **A097, estava:** "Com as administradoras de consórcio, o total chega a 1.785; com os bancos de câmbio, a 171 bancos". **Passou a valer:** "Sem as administradoras de consórcio, 1.654 instituições e 167 bancos; com elas, 1.785, e com os de câmbio, 171 bancos".
- **A179, estava:** "Pelos dados de saúde, os homicídios caíram 21%, com alerta de subnotificação em 2019". **Passou a valer:** "Queda exata de 17,8% na taxa de mortes violentas; nos dados de saúde, 21%, com alerta de subnotificação em 2019".
- **Por quê:** `VERDADEIRO` com número arredondado tem que trazer o valor apurado na ressalva (§2.2); as duas mostravam só o recorte alternativo.

##### A047 (lote 05), número apurado · aviso do validador

- **Estava:** "... no levantamento da Folha até 17/09/2026". **Passou a valer:** "... até 17 de setembro de 2026".
- **Por quê:** o "09" da data aparecia ao validador como número sem trecho; a data está nas fontes e na data de referência.

##### Mantidos depois de comparados (resumo; o detalhe está no JSON)

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

##### Para o autor, sem mudança feita

1. **Prazo e data só com imprensa.** A A138 virou `INSUSTENTAVEL` porque a extração a marcou como `serie_historica`, e a A078 recebeu a mesma régua para os dois lados da mesa. No caso de 15/out, a A140 (entrevistadora, "um ano e nove meses" de Galípolo no BC, `data_ou_prazo`, só imprensa) ficou `VERDADEIRO` com confiança alta, com o argumento de que "a afirmação é de data". Se o autor decidir que prazo e data ficam fora da regra 1 (que lista número, série histórica, valor e ranking), A138 e A078 voltam juntas a `VERDADEIRO`, e o tipo da A138 nas alegações passa a `data_ou_prazo`; se decidir que entram, a A140 de 15/out precisa da mesma régua. Não editei o outro caso.
2. **Confiança alta sem N1 no caso de 15/out:** A005, A006, A024, A046, A052, A066, A067, A068, A069, A070, A127, A140, A144, A145, A147, A150 e A151. Aqui a régua do esquema foi aplicada; lá, não.
3. **A033 do caso de 15/out** mede o desvio sobre o número dito (10 minutos sobre 90, "cerca de 11%"); sobre o apurado são 12,5%. O veredito não muda, mas é a única conta daquele caso fora da base declarada pela coerência de 15/out.
4. **A064 do caso de 15/out** ("as suspeitas que pairam sobre vários ministros", `INSUSTENTAVEL`): pela régua aplicada aqui (o que está documentado pode ser dito como documentado), a existência das suspeitas noticiadas teria veredito sobre o enunciado. A diferença para a A192 daqui está escrita (peça formal contra o investigado lá não havia), mas a decisão é do autor.
5. **A081 e A089** (e, em parte, A084 e A094) são quase a mesma afirmação e pesam duas vezes na contagem do candidato. É decisão de extração. A r3 também pediu para ouvir o "ilícito" da transcrição em 1112,6 s, perto da A089.
6. **A009 do caso de 28/ago** (`FALSO`, "nenhuma arma") não tem revisão adversarial registrada; a A123 daqui, com o mesmo veredito, tem (r5).
7. O validador acusa **5 URLs citadas sem captura assinada** em `CAPTURAS.json` (Agenda do Poder, duas; Banco Mundial; IBGE/SIDRA; Diário do Transporte). Já estavam antes desta passada e não são dos lotes.

### checagens/revisao/rodada2-rodada3.md

#### Rodada 2, terceira tentativa (parte rodada3, 17/out/2026)

Refeitas, com busca, as duas checagens que seguiam provisórias depois da rodada 1 e da rodada 2 (partes 2 e 3): A161 (lote 17, corte 04), primeiro, e A113 (lote 12). As duas fecharam: o marcador saiu do início da explicação, a explicação diz que a checagem foi refeita na rodada 2 de 17/out/2026 (terceira tentativa) e a confiança passou de baixa a média.

- Buscas usadas: 7 (limite: 7). A161: 4 WebSearch. A113: 1 WebSearch e 2 consultas à busca do próprio Diário Oficial (in.gov.br/consulta), capturadas por `capturar-fontes.py` e contadas aqui como busca, por serem consulta a buscador.
- Captura: pedidos `checagens/pedidos-captura/rodada3.json` e `rodada3-r2.json` a `rodada3-r8.json`; saídas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2rodada3` e `-r2rodada3-r2` a `-r2rodada3-r8`. As fontes que já vinham das rodadas anteriores saem das pastas `-p12`, `-p17`, `-p17-r3`, `-r2parte3-r4`.
- Conferência: os lotes 12 e 17 validam contra `esquemas/checagens.schema.json`; cada `trecho` foi achado, por palavra inteira e com espaços normalizados (pedaço a pedaço quando há `[...]`), no texto capturado da própria URL, com a função `conferir` de `ferramentas/conferir-trechos.py`; todo número e ano do `resumo`, da `ressalva` e do `numero_apurado` está num trecho, numa derivação, na fala ou na data de referência; as parcelas das derivações estão nos trechos. Só A161 e A113 mudaram nos lotes (comparado com o HEAD).
- Rótulos de gráfico (2,44 e 2,43 milhões no boletim de 2024; 2,42 milhões no de 2020) foram lidos na página renderizada do PDF e estão no texto capturado como rótulos soltos; a atribuição de cada rótulo ao ano é leitura do gráfico, declarada na explicação.

| id | rodada 1 | rodada 2 | por quê |
|---|---|---|---|
| A161 | INSUSTENTAVEL (provisório) | VERDADEIRO | Achado o boletim anual de 2024 do Mapa de Empresas, com nome de arquivo diferente dos cerca de 40 tentados antes (`boletim-do-mapa-de-empresas-3o-quad-2024.pdf`, apontado por um repositório público que reúne a série): 2.436.190 empresas fechadas em 2024, o maior número da série de 2010 a 2024, acima de 2018 (2,43 milhões, cancelamento em massa de MEIs). Fonte independente: Sebrae com a base de CNPJ da Receita, 2.395.523 pequenos negócios baixados em 2024, o maior de 2019 a 2024. 2025 até agosto está 13,7% acima do mesmo período de 2024, e o total anual de 2025 não foi achado; qualquer que seja, o recorde fica no governo atual. Ressalva: número absoluto, com MEI e baixas de ofício, e saldo positivo de 1.818.713 em 2024. Confiança média (margem pequena sobre 2018, lida em rótulo de gráfico). |
| A113 | INSUSTENTAVEL (provisório) | VERDADEIRO | Diário Oficial (N1): 18 superintendências trocadas no ato de 18/01/2023, mais Distrito Federal, Bahia e Roraima até 07/03/2023, 21 no total (o número do Portal Tela para os três primeiros meses). O Rio Grande do Sul, que o Portal Tela dava como única exceção (26 das 27 até junho de 2025), também trocou: Thiago Machado Delabary no cargo em abril de 2024, dispensa de Aldronei Antonio Pacheco Rodrigues e designação de Alessandro Maciel Lopes em 12/11/2025. A conta chega a 27 na gestão Andrei, antes da fala; a frase não diz "no início", e a ressalva diz que foi em etapas. Limite declarado: Acre, Amapá, Ceará, Espírito Santo e Piauí só entram pela fonte única do Portal Tela. Confiança média. A A114 (que usa os 18 de janeiro de 2023) segue coerente. |

### checagens/revisao/correcoes-rodada3.md

#### Correções da revisão adversarial da rodada 3 (17/out/2026)

Passada separada sobre as duas checagens fechadas na rodada 2, parte rodada3 (`rodada2-rodada3.md`): A161 (lote 17, corte 04) e A113 (lote 12). O revisor não checou essas alegações antes. Sem busca web (zero chamadas) e sem fonte nova: só o que está nas pastas `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2rodada3*` e nas capturas das rodadas anteriores. Depois das mudanças, os lotes 12 e 17 validam contra `esquemas/checagens.schema.json`. Todos os trechos das duas checagens (8 da A161, 11 da A113) foram achados no texto capturado da própria URL com a função `conferir` de `ferramentas/conferir-trechos.py`. Número e ano do resumo, da ressalva e do `numero_apurado` têm lastro, as parcelas das derivações estão nos trechos ou na fala, e não há travessão nem leitura de intenção. Os arquivos juntados (`checagens-sabatina-completa.json`, `checagens-corte-04.json`) não foram regerados aqui.

##### A113 · Estava · Passou a valer · Por quê

- **Estava:** VERDADEIRO. Resumo: "As 27 superintendências da PF trocaram de chefe no governo atual, em etapas: 21 até março de 2023 e o RS em 2025". Confiança média.
- **Passou a valer:** IMPRECISO. Resumo: "O Diário Oficial registra 21 das 27 superintendências da PF trocadas até março de 2023, não as 27". Ressalva: "Até 2025 o Diário Oficial soma 22 trocas; outras cinco só aparecem numa fonte de imprensa, sem ato conferido". O número apurado, a explicação, a divergência e as derivações também mudaram: entram 22 = 21 mais 1, o desvio de 22% e o de 19%. Confiança média.
- **Por quê:** o Diário Oficial (N1) documenta 22 trocas: 18 no ato de 18/01/2023, mais Distrito Federal, Bahia e Roraima até 07/03/2023, mais o Rio Grande do Sul em 12/11/2025. Isso foi conferido de novo nas capturas `-r2rodada3-r6` e `-r8`, estado por estado. As outras cinco (Acre, Amapá, Ceará, Espírito Santo e Piauí) só entram pelo Portal Tela, que é fonte única e de imprensa, e o texto vem marcado na página como "Gerado por Telinha" e revisado pela redação. A matéria não cita ato oficial, e o próprio Diário Oficial desmente a "única exceção" do Rio Grande do Sul que ela aponta. Pelas regras 1 a 3 da §3.1, ela não fecha o número 27.
  - **O recorte de tempo:** a frase vem logo depois de "a primeira coisa que o meu adversário fez quando sentou na cadeira [...] foi botar o amigo dele, Andrei", e a extração, feita antes da checagem, leu "no início do governo Lula". Nessa leitura, o registro dá 21, não 27 (desvio de 22%). A rodada 2 adotou a leitura da gestão inteira depois de ver o resultado (§5). Mesmo nessa leitura, o documentado chega a 22 (desvio de 19%), e a troca do Rio Grande do Sul é de quase três anos depois da posse.
  - **A régua:** nas duas leituras, o desvio passa de 10% (§2.2), e o essencial confere: houve troca em massa no início da gestão Andrei, muito acima de "um". É a régua da A036 (o registro oficial confirma a ordem de grandeza e corrige o número).
  - **Por que não INSUSTENTAVEL:** a A114 e a A037 ficaram INSUSTENTAVEL porque só tinham imprensa. Aqui há N1 para o essencial e para o número apurado.
  - **Por que não FALSO:** nada inverte a frase, e as cinco superintendências sem ato conferido podem ter sido trocadas.
  - **O que falta:** com os atos dessas cinco no Diário Oficial, a leitura da gestão inteira daria 27.
- **Pendente fora do escopo desta passada:** a explicação da A114 ainda diz "a mesma régua da A113 (as 27 trocas atribuídas a Lula, só com imprensa)". Isso descreve a A113 da rodada 1 e precisa ser atualizado por quem puder editar a A114. O veredito da A114 não muda.

##### A161 · Estava · Passou a valer · Por quê

- **Estava:** VERDADEIRO, com confiança média e o mesmo resumo e a mesma ressalva.
- **Passou a valer:** continua VERDADEIRO, sem mudança no resumo, na ressalva, nas fontes nem na confiança. Entram duas frases na explicação e uma na divergência:
  - **Na explicação:** os rótulos do gráfico são arredondados, não truncados, porque o próprio 2024 (2.436.190) aparece como 2,44 milhões. Logo, os 2,43 milhões de 2018 ficam abaixo de 2.435.000. A atribuição dos rótulos aos anos foi conferida de novo na página renderizada.
  - **Na divergência:** o boletim do 2º quadrimestre de 2025 dá percentuais (queda de 4,5% sobre o quadrimestre anterior, alta de 12,9% sobre 2024) que não fecham com 973.330 e 830.525. Isso mostra que a série é revista a cada edição, sem mudar a conclusão.
- **Por quê:**
  - **O ataque principal:** o valor de 2018 é um rótulo de gráfico. O rótulo "2,43Mi" está no texto capturado do PDF (o trecho existe, regra 5). A ligação entre o rótulo e o ano 2018 foi conferida aqui, renderizando as páginas dos dois boletins: no gráfico de 2014 a 2024, a linha de fechadas marca 2,43 em 2018 e 2,44 em 2024, e no de 2010 a 2020, 2,42 em 2018.
  - **O furo que havia:** a explicação dizia que 2.436.190 "fica acima de qualquer valor que arredonde para 2,43 milhões", mas não mostrava que o gráfico arredonda. Se os rótulos fossem truncados, 2018 poderia chegar a 2.439.999 e passar 2024. O rótulo do próprio 2024 (2,44 para 2.436.190) prova que o gráfico arredonda, e a ordem entre 2024 e 2018 sai do mesmo gráfico, na mesma revisão da série. A frase entrou na explicação.
  - **As fontes:** o Sebrae (N2, independente) cobre só de 2019 a 2024. Para o pico de 2018 a fonte é uma só, o Mapa de Empresas, em duas edições. A regra 1 fica atendida para a alegação (N1 mais N2 independentes, as duas com 2024 no topo do que cobrem), e a comparação com 2018 está no registro primário.
  - **A margem e a ressalva:** a margem é pequena e o resumo mostra os dois números (2.436.190 contra 2,43 milhões), então o card não esconde o quase empate. A ressalva cobre o número absoluto, o MEI, as baixas de ofício e o saldo positivo.
  - **O ano de 2025:** janeiro a agosto de 2025 está acima do mesmo período de 2024 mesmo com as revisões da série. Se o total de 2025 tiver passado o de 2024, o recorde continua no governo atual.

##### A114 (lote 12), explicação · par A113

- **Estava:** "passou a INSUSTENTAVEL pela mesma régua da A113 (as 27 trocas atribuídas a Lula, só com imprensa), [...]"
- **Passou a valer:** a explicação diz que a A113 ganhou o Diário Oficial na rodada 3 e passou a IMPRECISO, e que a parte de 2020 desta comparação continua sem fonte N1 ou N2; o veredito da A114 não muda.
- **Por quê:** o revisor da rodada 3 apontou que a explicação descrevia a A113 de antes da rodada 3. Feito pela IA que conduz o caso.


## 3. Transcrição

As 22 correções da transcrição estão em `transcricao/CORRECOES_DE_TRANSCRICAO.md`, e as três leituras alternativas que as sustentam, em `transcricao/leituras-alternativas/`. Todos os números conferidos saíram iguais na segunda leitura. As leituras que não se resolveram (entre elas *"um dinheiro totalmente ilícito"*, em 18:32, que as quatro leituras escrevem assim e o contexto pede *"lícito"*) estão listadas em `transcricao/correcoes.json`, campo `como_foram_conferidas`, e não vão para a tela sem `[...]`.

⚠️ O campo `revisao_humana: true` de `transcricao/transcricao.json` é marcado sozinho pelo `ferramentas/corrigir-transcricao.py` quando aplica correções; nesta transcrição as correções foram conferidas pela IA, por passadas do motor em janelas isoladas, e **nenhuma pessoa ouviu o áudio**.

🔧 Uma coisa do método que vale registrar: a 2ª leitura usou `-mc 0` (nenhum texto anterior como contexto) e, com isso, o whisper.cpp também descartou o prompt; as duas versões dela (sem e com prompt) saíram iguais. Ela foi tratada como uma leitura sem prompt, e a 3ª leitura, sem o `-mc 0`, é a que tem prompt.
