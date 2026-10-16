# Considerações da IA · sabatina de Lula na TV Globo, 2º turno (15/out/2026)

**Caso:** `2026-10-15-sabatina-lula-globo-2turno` · **escrito em:** 16/out/2026, por IA, no PASSO 6 da skill [`consideracoes-do-debate`](../../../skills/consideracoes-do-debate.md).
**Base:** os seis critérios de [`CRITERIOS.md`](CRITERIOS.md), registrados às 10h de 15/out, antes da sabatina (nenhum critério novo, nenhum adendo); a [passada A](passada-a.md) (com os nomes); a [passada B](passada-b.md) (espelho, feita por outro agente sem ver a A, sobre uma cópia com os nomes trocados); e as métricas finais da checagem, [`metricas/METRICAS_sabatina-completa.md`](../metricas/METRICAS_sabatina-completa.md) e `metricas-sabatina-completa.json`, depois da revisão adversarial e com o validador aprovado sem erro.

⛔ **Isto não é checagem.** É a leitura de uma IA sobre como a entrevista foi usada, pedida pelo autor, separada dos arquivos da checagem. Sem soma de critérios, sem nota, sem recomendação de voto, sem leitura de intenção e sem adjetivo sobre pessoa. Se for para o vídeo, o vídeo diz que é leitura de IA.

⚠️ **Sobre a transcrição.** As duas passadas citam o campo `revisao_humana: true` de `transcricao/transcricao.json`. Esse campo é preenchido automaticamente pelo script de correção (14 correções aplicadas); **nenhuma pessoa ouviu o áudio** para revisar a transcrição. As citações abaixo são literais e carregam os erros dela (*"Lili"*, *"Sou cogita"*, *"bulanças"*, *"a filha é muito tempo"*). As viradas de falante foram refeitas pela IA lendo o texto e olhando quadros do vídeo (`transcricao/falantes.json`).

---

## 1 · O que foi a sabatina

Entrevista de Luiz Inácio Lula da Silva (PT, candidato à reeleição) à TV Globo, conduzida por Renata Lo Prete, na noite de 15/out/2026, dez dias antes do 2º turno de 25/out. A peça tem 47:47 de arquivo e **42:32 de sabatina** sem o intervalo comercial (29:09 a 31:25), a vinheta e o áudio posterior, que ficaram fora de todas as contas. Onze blocos por tema (`metricas/blocos.json`): responsabilidade pelo cenário da eleição, Congresso e governabilidade, Estados Unidos e tarifas, segurança pública, Supremo e caso Master com a Polícia Federal, Bolsa Família e orçamento, endividamento, juros e dívida pública, energia elétrica, saúde, e considerações finais. A sabatina de Flávio Bolsonaro, na mesma emissora e com a mesma entrevistadora, está marcada para 16/out, e o `CRITERIOS.md` diz que a mesma régua vale para ela.

---

## 2 · Critério a critério

As duas passadas foram feitas sem uma ver a outra. Onde a contagem diverge, a causa está escrita. Quando a diferença vem de **regra de leitura** (o que conta como pergunta, como proposta, como termo técnico), este texto não escolhe qual das duas acertou: as duas regras estão declaradas nas passadas e as duas são defensáveis.

### C1 · Respondeu o que foi perguntado

*Indicador:* nos primeiros 30 segundos, a resposta trata do assunto perguntado (`respondeu` · `respondeu em parte` · `tratou de outro assunto`).

| | Passada A | Passada B |
|---|---|---|
| perguntas contadas | **21** | **23** |
| respondeu | 12 | 12 |
| respondeu em parte | 9 | 11 |
| tratou de outro assunto | **0** | **0** |

**Onde concordam.** Nenhuma resposta foi para outro assunto. Das 21 perguntas que as duas contaram, 19 receberam a mesma classificação, inclusive as de fronteira: a maioridade penal (duas vezes `em parte`, depois `respondeu`), a permanência do diretor da PF (duas vezes `em parte`), o aviso da PF sobre Vorcaro (`em parte`), a dívida pública e a energia (`em parte`, com a resposta ao ponto pedido chegando depois dos 30 s).

**Onde divergem, e por quê.**
- **Número de perguntas (21 × 23): critério de contagem.** A B contou como pergunta as duas de seguimento curtas, *"Não foi convincente?"* [20:49] e *"O senhor não sabia?"* [27:14]; a A as tratou como parte da pergunta em curso. As duas contaram as perguntas refeitas como novas. A passada A registra que a cobertura de imprensa falou em cerca de 25 perguntas, sem fonte anotada; o número fica fora.
- **Duas classificações (P1 e P2 da A): regra de leitura.** Na pergunta sobre responsabilidade e o que faria diferente [01:53], e na de governar sem frente ampla com um Congresso mais hostil [03:53], a A deu `respondeu` e a B deu `em parte`. A regra da B põe em `em parte` a resposta que, na janela, traz só uma das partes de uma pergunta múltipla ou só a contestação da premissa; a A contou a contestação da premissa como resposta. Somadas as duas seguidas que a B contou como `respondeu`, os totais de `respondeu` coincidem em 12 por caminhos diferentes.

**Exemplos (os mesmos nas duas passadas).** Atendido: [14:08] *"Então, só para a gente deixar bem claro, o senhor é a favor de reduzir para 16?"* → [14:11] *"Eu sou favorável a reduzir para 16, mas não discutindo nessa PEC."* Não atendido: a A usou o aviso da PF, [22:10] *"Não era o caso da PF ter avisado o senhor sobre o que pesava contra Daniel Vorcaro no momento em que o senhor recebe ele no Planalto?"*, com a resposta [22:19] a [23:27] sem voltar ao aviso; a B usou a permanência de Andrei Rodrigues, [20:18] *"O senhor, se reeleito, vai manter Andrei Rodrigues no comando da Polícia Federal?"*, repetida em [21:10], com [21:21] *"Eu não vou dizer aqui que eu vou escolher quem que vai ficar, quem que vai sair."*

### C2 · Especificidade das propostas

*Indicador:* proposta contada como específica se traz pelo menos dois de: meta ou número, prazo, mecanismo, origem do recurso, responsável.

| | Passada A | Passada B |
|---|---|---|
| propostas contadas | **27** | **24** |
| com dois ou mais elementos | **12** (44%) | **10** (42%) |
| com um ou nenhum | 15 | 14 |
| com os cinco elementos | 0 | 0 |

**Onde concordam.** Nenhuma proposta trouxe os cinco elementos. O prazo é o elemento mais raro nas duas, e os prazos ditos são deste ano (*"ainda esse ano"*, *"esse ano"*), não de um novo mandato. As duas classificam igual os presídios, o Desenrola com leilão de dívida, o estudo de anistia da dívida de MEI, o aval de R$ 5 mil, os data centers, as carretas de exame e a reforma do Judiciário (com dois ou mais), e *"libertar os territórios"*, economia verde, câncer, Brasil Sorridente e Farmácia Popular, escala 6 por 1 e transporte gratuito (com menos de dois).

**Onde divergem, e por quê (o recorte de "proposta", todas de regra de leitura).**
- A **A separou** a PEC da segurança e a criação do ministério (duas propostas, as duas com dois elementos); a **B juntou** numa só. (+1 na A, nas duas colunas.)
- A **A incluiu** a previsão *"o ano que vem, vamos ter economia entre as 8ª economia do mundo"* [36:15], marcada como previsão; a regra da B só conta ação. (+1 na A, nas duas colunas.)
- A **A incluiu** *"não gastar, não cortar dinheiro dos pobres"* [39:03] e o uso da dívida para *"ativo produtivo"* [38:36]; a B não os listou como proposta. (+2 no total da A.)
- A **B separou** o convênio com hospitais pago com a dívida deles com o Estado [43:43] e as 16 milhões de cirurgias eletivas deste ano [43:59]; a **A juntou** numa proposta com quatro elementos. (+1 na B, nas duas colunas.)
- **Os médicos** [42:20]: a A leu número e mecanismo (contratação) e contou dois; a B leu só o número. Divergência de classificação no mesmo trecho, que a transcrição deixa sem unidade (*"16 mil para ir para 28 médicos"*).
- **"A União vai comprar essa dívida"**: a A contou a União como responsável; a B, como origem do recurso. Não muda o resultado da proposta.

Com essas cinco diferenças, as contagens se reconciliam número a número (27 → 24 no total, 12 → 10 nas específicas).

**Exemplos.** Atendido: a A usou [43:43] *"Nós fizemos um convênio com hospitais particulares que estão pagando parte da dívida que tem com o Estado para atender pelo SUS."* com [44:00] *"Esse ano, vamos fazer 16 milhões de cirurgias eletivas."*; a B usou [12:05] *"Nós vamos financiar 138 presídios em todo o território nacional."* com [12:14] *"em cadeia de segurança máxima financiada pelo governo federal"*. Não atendido: a A usou [45:13] *"De dar transporte gratuito para as pessoas no final de semana"*; a B usou [12:44] *"Ou seja, nós queremos libertar os territórios dos bandidos nesse país."*

⚠️ As duas marcaram como frágeis os trechos que a transcrição cortou: as ambulâncias [43:15] (*"10 mil bulanças se renovaram"*) e a escala 6 por 1 [45:06].

### C3 · O que foi dito como fato e se sustentou

Está na **seção 3**, preenchido só com as métricas finais da checagem. As passadas não fizeram este critério.

### C4 · Uso do tempo

*Indicador:* parcela do tempo de fala; vezes em que a entrevistadora retomou a palavra antes de a resposta terminar; vezes em que o candidato falou por cima da pergunta.

| | Passada A | Passada B |
|---|---|---|
| tempo de fala de Lula (soma de segmentos) | 1.429,0 s · **62,6%** | 1.429,0 s · **62,6%** |
| tempo de fala de Renata Lo Prete | 852,1 s · **37,4%** | 852,1 s · **37,4%** |
| pelo método de turnos (com pausas) | não fez | 63,2% · 36,8% |
| entrevistadora entra com a frase dele cortada | **2** ([13:39], [17:05]) | **2** ([13:39], [17:05]) |
| candidato começa com a frase dela cortada | **4 episódios** ([24:17], [37:04] e [37:09], [43:25], [43:41]) | **2** ([43:25], [43:41]) + **1 trecho de sobreposição** ([37:01] a [37:18]) |
| retomadas depois de frase completa, com o assunto em curso | 14, listadas, sem classificar | não contadas |

**Onde concordam.** O tempo é o mesmo nas duas (perto de dois terços para o entrevistado, e por bloco a mesma forma: a maior parcela dele em EUA, considerações finais e saúde, e a parcela da entrevistadora maior no bloco do Bolsa Família). As duas retomadas da entrevistadora com a frase cortada são as mesmas. As duas lembram que o tempo dela inclui abertura, chamada do intervalo e encerramento.

**Onde divergem, e por quê (fonte e regra do sinal).**
- **O trecho de [37:01] a [37:18]:** a A leu só o texto, onde nenhum segmento se sobrepõe, e contou os dois *"Sou cogita"* como pergunta cortada; a B usou a sobreposição declarada em `falantes.json`, conferida pela IA nos quadros do vídeo, e contou o trecho à parte. É o mesmo episódio contado de dois jeitos.
- **[24:17]** *"O senhor acha que isso?"* → *"Acho, Renata, que nós temos que mudar muitas coisas."*: a A leu a pergunta como cortada; a B, como pergunta terminada.
- **As 14 retomadas de frase completa:** a A listou, dizendo que pelo texto não dá para saber se a resposta tinha terminado; a regra da B não conta virada depois de frase completa.

Por isso o total de vezes em que o candidato começou com a frase da entrevistadora pela metade fica **entre 2 e 4, conforme a regra**. Sobreposição real de áudio fora de [37:01] a [37:18] não é observável nesta transcrição (as duas registram).

**Exemplos.** Atendido: a A usou a resposta corrida de [06:31] a [08:41] sobre os EUA; a B, [14:26] *"Eu acho que a sociedade brasileira inteira, sabe, é favorável à punição de qualquer crime hediondo."* → [14:36] *"Ok, presidente, acho que a sua posição ficou clara."* Não atendido, um de cada lado (B): [13:38] *"O meu pensamento..."* → [13:39] *"O senhor é a favor da redução?"*; e [43:40] *"Mas eu agradeço ao senhor..."* → [43:41] *"Mas veja um milagre"*.

### C5 · Tratou do dado da pergunta

*Indicador:* quando a pergunta trouxe um número ou fato, a resposta tratou dele, contestou com outro dado, ou não tratou.

| Passada A (unidade: **pergunta**) | | Passada B (unidade: **cada fato**) | |
|---|---|---|---|
| perguntas com dado ou fato | **19** | fatos contados | **35** |
| tratou | 5 | tratou | 17 |
| contestou ou contrapôs com outro dado | 4 | contestou com outro dado | 4 |
| tratou em parte | 5 | contestou sem dado | 1 |
| não tratou | 5 | não tratou | 11 |
| | | não se aplica (a entrevistadora encerrou o ponto) | 2 |

**Os denominadores (19 e 35) não se comparam: a unidade é diferente.** A A classificou cada pergunta inteira e criou `em parte` para a pergunta com vários fatos em que só alguns foram tratados; a B separou cada fato da pergunta (uma pergunta pode ter três) e não tem `em parte`. É divergência de regra de contagem, as duas declaradas.

**Onde concordam, no mesmo fato.** Sem tratar o dado, nas duas: a pesquisa Datafolha sobre a designação de facções como terroristas ([09:11]), os quase 80% com medo de roubo na rua do Fórum Brasileiro de Segurança Pública ([11:16]), a palavra *"promiscuidade"* só depois do 1º turno ([15:14]) e os 10 pontos percentuais de alta da dívida pública ([36:47]). Tratado, nas duas: os 17 dias entre o reajuste do Bolsa Família e o 1º turno ([26:59]), a ida de Andrei Rodrigues à festa em Londres ([20:05]) e a proposta de 16 anos ([13:18]).

**Onde divergem, no mesmo fato (leitura de categoria, não de contagem).**

| Fato | Passada A | Passada B |
|---|---|---|
| Congresso eleito mais hostil [03:45] | contestou com outro dado (70 deputados, 99% aprovado) | não tratou (os números foram lidos como resposta à frente ampla, outro fato da mesma pergunta) |
| FGV e 84 milhões negativados [31:50] | contrapôs com outro dado (78%) | não tratou (trouxe outro número) |
| Galípolo e o modelo esgotado [35:07] | tratou, contestando com argumento sem dado | contestou com outro dado ([35:45]-[36:08]) |
| tarifa subiu o dobro da inflação [39:37] | não tratou do número | tratou, atribuindo à privatização |
| orçamento de 31/ago sem correção [27:43] | em parte (a data não aparece) | tratou |

Este texto não escolhe entre as leituras da tabela: em todas a pergunta é se *trazer outro número* ou *explicar a causa* conta como tratar o dado, e o indicador escrito antes não decide isso.

**Exemplos.** Atendido: a A usou [26:59] *"por que o principal programa social do governo só foi reajustado 17 dias antes do primeiro turno?"* → [27:15] *"Eu não sabia, porque é inexplicável, Renata"*; a B, [27:43] *"No dia 31 de agosto, duas semanas antes do anúncio, o seu governo mandou para o Congresso a proposta de orçamento de 2027."* → [28:01] *"Não, aconteceu que eu fiquei sabendo que não tinha sido aumentado o Bolsa Família."* (é um dos fatos da tabela acima: a A o pôs em `em parte`). Não atendido: a A usou o Datafolha, [09:11] *"uma pesquisa de junho do Datafolha, aponta que dois terços, aproximadamente, concorda total ou parcialmente com essa designação"* → [09:31] *"Não, veja, é um ponto que os Estados Unidos não entendem."*; a B, [36:47] *"Por exemplo, o fato da dívida pública ter crescido"* [36:49] *"10 pontos percentuais no seu governo"* → [37:01] *"E você acha que eu não estou preocupado?"*, sem o número voltar.

Se a contestação estava certa é o C3, e não entra aqui.

### C6 · Clareza para quem assiste

*Indicador:* termos técnicos e siglas sem explicação, por resposta; respostas cuja mensagem principal cabe numa frase da própria fala.

| | Passada A | Passada B |
|---|---|---|
| respostas | 19 | 19 |
| termos sem explicação | **22** (2 de uso corrente, 5 trazidos pela pergunta, marcados) | **13**, em 9 respostas (+ 2 nomes de programa sem explicação) |
| termos explicados na própria fala | citados nos exemplos | 8 |
| mensagem principal numa frase da própria fala | **17 de 19** | **18 de 19** |

**Onde concordam.** Onze termos aparecem sem explicação nas duas: superávit comercial, lei da reciprocidade, quarentena, superávit primário (com o *"déficit de 2,8%"* sem dizer de quê), medida provisória, MEI, FMI, crise do subprime, recebíveis, data center e economia verde, criativa e digital. Os blocos de economia concentram a maior parte nas duas. Na resposta sobre energia, nenhuma das duas achou uma frase da própria fala que dissesse qual era a resposta ao plano pedido.

**Onde divergem, e por quê.**
- **22 × 13 termos: regra de contagem.** A A contou o termo que a entrevistadora usou antes (*"crime hediondo"*, *"pedir vista"*, *"espaço fiscal"*, *"cirurgias eletivas"*), siglas de uso corrente (ONU, SUS) e a repetição de um termo em outra resposta (*"MEI"*, *"espaço fiscal"*), marcando cada caso; a B tirou os três tipos. Tirando esses da A, sobram 16.
- **Leitura oposta no mesmo termo (julgamento):** *"PEC da transição"* e *"PEC"* a A deu como explicados pela função dita junto, a B como sem explicação; *"microcrédito"* e *"escala 6 por 1"* a B deu como explicados, a A como sem explicação. A A contou ainda *"problema fiscal"* [35:23].
- **Mensagem numa frase (17 × 18):** a resposta sobre regras de conduta (P11 na A) ficou `não achei` na A e `sim` na B, com [26:08] *"Então, nós temos que aproveitar esse acontecimento para colocar um fim e criar um comportamento ético mais adequado."* As duas passadas marcaram esta metade do C6 como a leitura mais sujeita a juízo; este texto não decide.

**Exemplos.** Atendido: a A usou [10:27] *"aprovamos a lei contra a lei anti-facção, que aumenta a pena dos bandidos"*; a B, [38:08] *"O que faz a economia do Brasil crescer é a chamada microeconomia,"* [38:12] *"é fazer o dinheiro rodar na mão do povo."* Não atendido: a A usou [36:04] *"e aí emprestei 15 bilhões depois da crise do subprime ao FMI."*; a B, [28:19] *"É importante lembrar, Renata, que nós apresentamos um orçamento com superávit primário."*

---

## 3 · C3 · O que foi dito como fato e se sustentou

*Fonte:* só as métricas finais da checagem (`metricas/`), depois da revisão adversarial (108 vereditos mantidos, 85 alterados, contando a auditoria final por amostra) e com o validador aprovado sem erro. As passadas não fizeram este critério.

**193 afirmações de fato** foram conferidas na sabatina, e **todas** eram checáveis (0 não checáveis).

| Lado da mesa | Tempo de fala | Afirmações (denominador) | Verdadeiro | Impreciso | Sem comprovação | Falso | Por minuto de fala |
|---|---|---:|---:|---:|---:|---:|---:|
| Lula (entrevistado) | 23:49 | **119** | 67 · 56,3% | 24 · 20,2% | 25 · 21,0% | 3 · 2,5% | 5,0 |
| Renata Lo Prete (entrevistadora) | 14:12 | **74** | 62 · 83,8% | 6 · 8,1% | 6 · 8,1% | 0 · 0,0% | 5,21 |
| total | 38:01 | **193** | 129 · 66,8% | 30 · 15,5% | 31 · 16,1% | 3 · 1,6% | |

As três afirmações classificadas como `FALSO` estão nos blocos de segurança pública, de Bolsa Família e orçamento, e de juros e dívida pública (uma em cada).

🔴 **Os dois lados da mesa não se comparam direto.** Quem responde fala mais e afirma mais (119 contra 74, em 23:49 contra 14:12, com densidade parecida por minuto), e as afirmações da entrevistadora são, na maior parte, o contexto das perguntas. Um percentual menor de `VERDADEIRO` pode vir só do tempo de fala e do assunto (economia tem série oficial; promessa e opinião não têm). `SEM COMPROVAÇÃO` quer dizer que a busca não achou fonte que sustente, e não que alguém provou o contrário.

⛔ **Nada disso é placar**, nem nota, nem medida de quem diz mais verdade. `FALSO` e `IMPRECISO` não se somam: são vereditos diferentes, e somá-los é a conta que a metodologia proíbe.

---

## 4 · Percepção pública

*Fonte:* seção 6 da passada A, buscas feitas em 16/out/2026 (seis buscas, o limite combinado). A passada B não fez esta parte.

**Pesquisa de opinião sobre a sabatina: ainda não existe.** Até a data das buscas, nenhum instituto (Datafolha, Quaest, AtlasIntel ou outro) publicou pesquisa sobre a avaliação desta entrevista. As pesquisas de intenção de voto do 2º turno do mesmo dia não medem a sabatina e não entram.

**Análises de veículos, atribuídas (como a passada A registrou):**

| Fonte | Data | O que registrou | Observação |
|---|---|---|---|
| TMC, Arthur Farias | 15/out, 23h19 | que, sobre o Bolsa Família, *"Detalhes sobre o montante, o cronograma e a modalidade dessa recomposição não foram apresentados."* | coincide com a proposta do Bolsa Família ter zero ou um elemento no C2 |
| O Repórter, Redação | 16/out, 02h14 | que José Roberto de Toledo (UOL) considerou a declaração sobre o Bolsa Família *"o momento mais problemático da entrevista para o candidato"* e que Merval Pereira (GloboNews) avaliou favoravelmente o desempenho de Lula | ⚠️ **de segunda mão**: os comentários originais não foram abertos; boa parte da matéria avalia a entrevistadora, e o próprio veículo diz que as avaliações não medem impacto eleitoral |
| Revista Fórum, Raony Salvador | 15/out, 22h03 | relato das falas sobre o Bolsa Família, sem avaliação de desempenho | o veículo se apresenta como *"o veículo mais antigo da mídia progressista"* |

Ficaram fora, com o motivo: a nota média de colunistas de O Globo citada pelo Maranhão Hoje (o original não foi achado); uma página da TVT News que é de 28/ago e trata da sabatina do 1º turno; a checagem ao vivo da Lupa (é checagem, não percepção).

⚠️ **A exigência de orientações diferentes não foi cumprida.** A passada A não achou, dentro do limite, análise de veículo identificado com a direita ou com a campanha adversária. O que existe é cobertura geral, um veículo que se declara progressista e um resumo de segunda mão. **Esta seção precisa ser refeita quando houver pesquisa de instituto e análises originais dos dois lados.**

---

## 5 · As duas passadas, onde divergiram, e o teste de troca

**Como foram feitas.** A passada A leu a transcrição com os nomes. A passada B foi feita por outro agente, sem abrir a A, sobre uma cópia em que um script trocou candidato, entrevistadora, partido e vocativos por rótulos; ela mesma declara que a troca reduziu o efeito do nome sem eliminá-lo, porque o conteúdo (*"quarto mandato"*, o adversário, o PL) continua dizendo de quem se trata. A A fez também a percepção pública; a B fez o teste de troca completo.

**Resumo das divergências.**

| Critério | Divergência | Natureza |
|---|---|---|
| C1 | 21 × 23 perguntas; P1 e P2 `respondeu` (A) × `em parte` (B) | contagem (perguntas de seguimento) e regra de leitura (contestação de premissa) |
| C2 | 27 × 24 propostas; 12 × 10 com dois ou mais elementos | recorte de proposta (separar ou juntar, incluir previsão e frase genérica) e um caso de classificação (médicos) |
| C3 | não se aplica | as duas deixaram para as métricas |
| C4 | 4 × 2 episódios do candidato com a frase dela cortada; sobreposição de [37:01] a [37:18] contada de dois jeitos | fonte (só texto × `falantes.json`) e regra do sinal |
| C5 | 19 perguntas × 35 fatos; cinco fatos com categoria diferente | unidade de contagem e leitura de categoria |
| C6 | 22 × 13 termos; 17 × 18 mensagens numa frase | regra de contagem (termo da pergunta, de uso corrente, repetido) e julgamento em quatro termos e numa resposta |

**O que as duas acharam igual**, apesar das regras diferentes: nenhuma resposta para outro assunto; perto de 40% das propostas com dois ou mais elementos e nenhuma com os cinco; o tempo de fala; as duas retomadas da entrevistadora com a frase cortada; os quatro dados da pergunta que ficaram sem tratamento nas duas leituras (Datafolha, 80% de medo de roubo, *"promiscuidade"*, 10 pontos da dívida); onze termos sem explicação; a resposta sobre energia sem frase que a resuma.

**O teste de troca** (regra 3 do `CRITERIOS.md`: cada frase relida com o nome do outro candidato do 2º turno no lugar; fica só a que continua justa).
- **Na passada B**, sete frases do rascunho não passaram e foram reescritas ou tiradas: *"respondeu com a defesa dos indicados"*, *"as respostas mais específicas vieram quando o tema era o programa do próprio governo"*, *"a entrevistadora precisou repetir"*, *"recorreu a números de 2003 a 2010"*, *"a resposta sobre energia foi dispersa"*, *"ele dominou o tempo da entrevista"* e *"respostas cheias de números"* (leitura de intenção, adjetivo, ou generalização que só cabe a quem governa).
- **Na passada A**, o teste foi aplicado às frases de contagem e aos exemplos, que são só número e citação.
- **Neste documento**, o teste foi aplicado a todas as frases das seções 1 a 7. Quatro frases do rascunho não passaram: *"Lula ocupou a maior parte da entrevista"* virou a parcela medida com a frase de que este é o desenho de uma sabatina (*"ocupou"* sugere intenção); *"deixou sem resposta os números da pergunta"* virou *"as duas leituras concordam em casos em que a resposta não falou daquele número"* (*"deixou"* sugere escolha); *"errou três vezes"* virou *"três foram classificadas como falsas"*; e, no texto da forma B, *"usou a entrevista para defender o governo"* saiu (leitura de intenção). As tabelas e as citações passaram sem mudança e valem do mesmo jeito para a sabatina de 16/out.

---

## 6 · O que não pode ser afirmado a partir disto

- quem convenceu quem, ou se a sabatina mudou algum voto;
- quem vai ser eleito em 25/out;
- quem governaria melhor, ou se alguma proposta é boa, viável ou barata (o C2 mede só se ela veio com elementos);
- que uma resposta `em parte` ou um dado `não tratado` foi uma esquiva: os critérios medem o que foi dito, não por quê;
- a intenção de qualquer pessoa, do candidato ao responder ou da entrevistadora ao perguntar e retomar a palavra;
- que o percentual de `VERDADEIRO` de um lado da mesa é melhor ou pior que o do outro, ou que `FALSO` e `IMPRECISO` somados dizem alguma coisa;
- o que o público achou da entrevista, enquanto não houver pesquisa de instituto;
- qualquer comparação com a sabatina de Flávio Bolsonaro de 16/out antes de ela ser lida pelos mesmos seis critérios, com as diferenças declaradas (perguntas, temas e tempo diferentes).

---

## 7 · Texto-base para a fala do vídeo

🔑 **A escolha da forma é do autor.** A IA entrega as três e não escolhe. Os riscos (skill §5 e `CRITERIOS.md`):

| Forma | Risco |
|---|---|
| **A · critério a critério** | o menor: cada frase tem indicador e exemplo |
| **B · síntese que nomeia** | 🔴 **o maior.** É a frase que o projeto diz que não faz: para juntar seis critérios numa frase alguém escolhe quais entram e com que peso, e a IA não escolhe pesos. Numa sabatina, ainda é a frase mais fácil de recortar e usar como propaganda, contra ou a favor, sem o resto do texto |
| **C · só a percepção medida** | menor, mas hoje não existe pesquisa de instituto, e as análises achadas são de segunda mão e sem os dois lados |

Os três textos usam porcentagem redonda e as contagens em que as duas passadas concordam; onde elas divergem, a fala dá a faixa.

### Forma A · critério a critério

> Os critérios foram escritos antes da sabatina, e a IA leu a entrevista inteira com eles em duas leituras separadas, uma sem ver a outra. O que vem agora é a leitura da IA, e ela não soma os critérios nem dá nota.
>
> O primeiro critério olha se a resposta falou do assunto da pergunta logo no começo. Lula falou do assunto em todas as perguntas, e em quase metade delas falou só de uma parte. Sobre manter o diretor da Polícia Federal, a pergunta veio duas vezes, e a resposta foi que ele não ia dizer ali quem fica e quem sai.
>
> O segundo critério olha as propostas. A IA contou quantas vinham com pelo menos duas coisas entre meta, prazo, jeito de fazer, de onde sai o dinheiro e quem faz. Deu perto de 40% das propostas, e o prazo quase não apareceu.
>
> O terceiro critério vem da checagem. Das 119 frases de Lula que foram conferidas, 67 se confirmaram. Uns 20% estavam imprecisos, outros 20% ficaram sem fonte que sustentasse, e três foram classificadas como falsas. A entrevistadora fez 74 afirmações nas perguntas, e 62 se confirmaram. Esses números ficam lado a lado, sem comparação direta, porque quem responde fala mais e afirma mais, e eles não viram placar.
>
> No tempo, Lula ficou com uns 60% da fala, que é o desenho de uma sabatina. Em duas vezes a entrevistadora entrou com a frase dele cortada, e ele começou a falar com a frase dela pela metade entre duas e quatro vezes, conforme a regra usada para contar.
>
> Quando a pergunta trazia um número ou um fato, a IA olhou se a resposta falava daquilo. As duas leituras concordam em quatro casos em que a resposta não falou, entre eles a pesquisa do Datafolha sobre as facções e o dado de que a dívida pública subiu 10 pontos. E concordam em casos em que falou, como o Bolsa Família reajustado 17 dias antes do primeiro turno.
>
> O último critério é a clareza para quem assiste. As duas leituras acharam onze termos usados sem explicação, quase todos de economia, como superávit primário e recebíveis. Na resposta sobre a conta de luz, nenhuma das duas achou uma frase dele que resumisse a resposta.
>
> Nada disso diz quem convenceu quem, quem vai ganhar no dia 25 ou quem governaria melhor. Os mesmos seis critérios valem para a sabatina de Flávio Bolsonaro.

### Forma B · síntese que nomeia

> Juntando os seis critérios numa frase, e essa frase é uma escolha da IA sobre o que entra: Lula falou do assunto em todas as perguntas, em quase metade só de uma parte, perto de 40% das propostas vieram com pelo menos dois detalhes, como meta, prazo ou jeito de fazer, e mais da metade do que disse como fato se confirmou na checagem. Isso descreve como a entrevista foi usada, e não diz quem convenceu ninguém nem quem vai ganhar.

### Forma C · só a percepção medida

> Até o dia 16 de outubro, quando a IA fez a busca, nenhum instituto de pesquisa tinha medido o que o público achou da sabatina. O que existe são comentários de analistas. Segundo um resumo publicado pelo site O Repórter, José Roberto de Toledo, do UOL, apontou a fala sobre o Bolsa Família como o momento mais difícil da entrevista para o candidato, e Merval Pereira, da GloboNews, avaliou bem o desempenho de Lula. A IA procurou e não achou análise dos dois lados da disputa, então essa parte fica incompleta até sair pesquisa.

---

## 8 · Conferência do texto-base

Detector de cara de IA do repositório do canal (`referencias-conteudo/roteiros/scripts/detectar-cara-de-ia.py`), rodado em 16/out/2026 sobre um arquivo temporário só com as falas das três formas da seção 7 (`--falas`): **576 palavras, 0 ocorrências, 0,0 por mil palavras** (meta: abaixo de 3). O detector aponta candidatos; a leitura em voz alta é do autor.
