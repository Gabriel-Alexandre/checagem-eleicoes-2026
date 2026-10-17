# Considerações da IA · sabatina de Flávio Bolsonaro na TV Globo, 2º turno (16/out/2026)

**Caso:** `2026-10-16-sabatina-flavio-globo-2turno` · **escrito em:** 17/out/2026, por IA, no PASSO 6 da skill [`consideracoes-do-debate`](../../../skills/consideracoes-do-debate.md).
**Base:** os seis critérios de [`CRITERIOS.md`](CRITERIOS.md), registrados às 10h de 15/out, antes das duas sabatinas, e copiados sem mudança para este caso ([`ORIGEM_DOS_CRITERIOS.md`](../ORIGEM_DOS_CRITERIOS.md); nenhum critério novo, nenhum adendo); a [passada A](passada-a.md) (com os nomes); a [passada B](passada-b.md) (espelho, feita por outro agente sem ver a A); a [percepção pública](percepcao-publica.md), levantada em 17/out; e as métricas finais da checagem, [`metricas/METRICAS_sabatina-completa.md`](../metricas/METRICAS_sabatina-completa.md) e `metricas-sabatina-completa.json`, depois da revisão adversarial e da auditoria final de 17/out.

⛔ **Isto não é checagem.** É a leitura de uma IA sobre como a entrevista foi usada, pedida pelo autor, separada dos arquivos da checagem. Sem soma de critérios, sem nota, sem placar, sem recomendação de voto, sem leitura de intenção e sem adjetivo sobre pessoa. Se for para o vídeo, o vídeo diz que é leitura de IA.

⚠️ **Sobre a transcrição.** As duas passadas citam o campo `revisao_humana: true` de `transcricao/transcricao.json`. Esse campo é preenchido automaticamente pelo script de correção (22 correções aplicadas, registradas em `transcricao/CORRECOES_DE_TRANSCRICAO.md`); **nenhuma pessoa ouviu o áudio** para revisar a transcrição. As citações abaixo são literais e carregam os erros dela (*"Renato"* no lugar do nome da entrevistadora, *"Podemos votar para seis por um?"*, *"os RODs do petróleo"*). As viradas de falante foram feitas à mão pela IA, lendo o texto e olhando quadros do vídeo: 91 turnos, em `transcricao/falantes.json`.

---

## 1 · O que foi a sabatina

Entrevista de Flávio Bolsonaro (PL, senador e candidato no 2º turno) à TV Globo, conduzida por Renata Lo Prete, na noite de 16/out/2026, depois do Jornal Nacional, nove dias antes do 2º turno de 25/out. No ar, foi anunciada com 40 minutos, dois blocos e as considerações finais. O arquivo tem 42min48s e começa na primeira palavra da entrevista. O intervalo comercial foi tirado na origem: a emenda de 32:22 a 32:24 é só vinheta, sem fala, então o minuto citado aqui é o minuto do arquivo e nada da entrevista ficou de fora. A fala transcrita soma 39:09.

Quinze blocos por tema (`metricas/blocos.json`): ajuste fiscal, juros e salário mínimo; fim da escala 6x1; reeleição e tamanho do mandato; reforma do Judiciário, Moraes e Nunes Marques; caso Master e o dinheiro de Vorcaro para o filme; Polícia Federal e a reunião ministerial de 2020; Jair Bolsonaro, condenação e cargo no governo; Eduardo Bolsonaro e o Itamaraty; Forças Armadas e narcotráfico; 8 de janeiro; respeito ao resultado das urnas; armas e segurança pública; Rio de Janeiro, aliados presos e investigados; saúde e o ministro anunciado; e considerações finais.

A sabatina de Lula, na mesma emissora e com a mesma entrevistadora, foi em 15/out. Os seis critérios e a régua são os mesmos nas duas. As perguntas, os temas e o tempo foram outros, e este documento não compara os resultados.

---

## 2 · Critério a critério

As duas passadas foram feitas sem uma ver a outra. Onde a contagem diverge, a causa está escrita. Quando a diferença vem de **regra de leitura** (o que conta como pergunta, como proposta, como termo técnico), este texto não escolhe qual das duas acertou: as duas regras estão declaradas nas passadas e as duas são defensáveis.

### C1 · Respondeu o que foi perguntado

*Indicador:* nos primeiros 30 segundos, a resposta trata do assunto perguntado (`respondeu` · `respondeu em parte` · `tratou de outro assunto`).

| | Passada A | Passada B |
|---|---|---|
| perguntas contadas | **32** | **30** |
| respondeu | 20 | 17 |
| respondeu em parte | 6 | 9 |
| tratou de outro assunto | **6** | **4** |

**Onde concordam.** Das 30 perguntas que as duas contaram, 26 receberam a mesma classificação. Nas duas, quatro respostas foram para outro assunto: a da mudança de posição sobre a escala 6x1, a primeira sobre a troca do ministro pelo pai, e as duas primeiras sobre a retirada da marcação das cápsulas de munição. Nas duas, ficaram `em parte` a reforma do Judiciário, Nunes Marques, a diferença entre os 134 milhões pedidos e os 75 do custo do filme, a segunda pergunta sobre cargo para o pai e a de armas e Estatuto do Desarmamento. As três perguntas de abertura (mínimo, aposentadorias, pisos de saúde e educação), a do respeito ao resultado das urnas e a de Eduardo como chanceler ficaram `respondeu` nas duas.

**Onde divergem, e por quê.**
- **Número de perguntas (32 × 30): critério de contagem.** A A contou como perguntas refeitas a confirmação sobre Eduardo de [27:02] (P18b, `respondeu`) e a volta à marcação das munições de [35:34] (P22c, `em parte`); a B leu as duas como afirmações da entrevistadora, sem pergunta.
- **Quatro classificações: regra de leitura.** A regra da B põe em `em parte` a resposta que, na janela, traz só a premissa da própria pergunta, contestada ou comentada. Por isso, na pergunta sobre levar ao eleitor as informações do fundo [16:32] e na de cobrar atitude republicana na PF [22:20], a A deu `respondeu` (contestou a premissa) e a B deu `em parte`; na primeira pergunta sobre cargo para o pai [23:33] e na exigência aos comandantes [27:39], a A deu `tratou de outro assunto` e a B deu `em parte`.

Com essas seis diferenças, as contagens se reconciliam número a número (20, 6 e 6 na A viram 17, 9 e 4 na B). Por isso `respondeu` fica **entre 17 e 20** e `tratou de outro assunto` **entre 4 e 6**, conforme a regra.

**Exemplos.** Atendido: a A usou [08:58] *"Se o senhor chegar à presidência, vai se empenhar para reverter o fim da escala 6x1?"* → [09:03] *"Não vou, Renata."*; a B, [31:22] *"se o senhor perder candidato, o senhor vai respeitar o resultado das urnas?"* → [31:29] *"Independente de qual for o resultado, eu vou respeitar."* Não atendido, o mesmo trecho nas duas: a A usou [33:54] *"Em que retirar a marcação das cápsulas, das balas, ajudaria a combater o crime organizado"* com [34:09] *"o que a gente tem que trabalhar aqui é pra acabar com a impunidade de verdade."*; a B, [33:51] *"Deixa eu tentar ouvi-lo sobre o mérito da proposta."* → [34:08] *"o que a gente tem que trabalhar aqui é pra acabar com a impunidade de verdade."*, com a medida voltando em [35:39], fora da janela, como *"Eu acho que isso é uma coisa muito menor"*.

### C2 · Especificidade das propostas

*Indicador:* proposta contada como específica se traz pelo menos dois de: meta ou número, prazo, mecanismo, origem do recurso, responsável.

| | Passada A | Passada B |
|---|---|---|
| propostas contadas | **24** | **22** |
| com dois ou mais elementos | **8** (33%) | **9** (41%) |
| com um ou nenhum | 16 | 13 |
| com os cinco elementos | 0 | 0 |

**Onde concordam.** Nenhuma proposta trouxe os cinco elementos; a mais completa nas duas tem três. O prazo apareceu numa só, nas duas: a reunião com os comandantes para declarar guerra ao narcotráfico *"a partir de janeiro"*. As duas classificam igual, com dois ou mais elementos, os imóveis da União num fundo securitizado, a securitização da dívida ativa, a creche com voucher pago pelo governo, a PEC do fim da reeleição, a guerra ao narcotráfico, a Marinha no Porto de Santos, as câmeras com inteligência artificial e a cirurgia em vaga ociosa da rede privada. E com menos de dois: cortar 10 ministérios, corrupção e gestão com inteligência artificial, devolver o poder de compra, os penduricalhos do Judiciário, declarar facções como narcoterroristas, o Escudo das Américas, Forças Armadas valorizadas, legislação penal mais dura, melhorar o Estatuto do Desarmamento, o SUS com padrão Einstein, telemedicina e o Prontuário Único Eletrônico.

**Onde divergem, e por quê.**
- **Total (24 × 22): recorte de "proposta", regra de leitura.** A A contou o *"Sim."* ao reajuste do mínimo acima da inflação [01:19] (um elemento) e o Bolsa Família de [38:02], *"Eu vou lembrar de você todos os dias do meu governo."* (nenhum); a B deixou fora o sim ou não a proposta posta pela entrevistadora e os compromissos de manter, e não listou o segundo. (+2 na A, as duas com menos de dois.)
- **Específicas (8 × 9): um caso de classificação.** A margem equatorial [04:50]: a A leu só o número (*"mais de 100 bilhões"*); a B leu número e mecanismo (explorar o petróleo). A própria A anotou que essa proposta podia ganhar mecanismo.
- **Os compromissos do fim:** a A juntou numa linha os três compromissos finais [41:57]; a B separou *"devolver a segurança"* e deixou fora o de não prometer o que não pode cumprir. A contagem fica igual, uma linha de um lado e uma do outro, as duas sem elemento.
- **A declaração de facções como narcoterroristas:** a A não leu mecanismo, a B leu. Não muda o resultado (menos de dois nas duas).

Com essas diferenças, as contagens se reconciliam (24 → 22 no total, 8 → 9 nas específicas). A regra de origem do recurso que a A marcou como sujeita a divergência (*"o governo vai bancar"*, na creche) foi aplicada igual pela B.

**Exemplos.** Atendido, o mesmo nas duas: a A usou [27:58] *"Um dos meus primeiros atos como presidente da república vai ser juntar os comandantes do Exército, Marinha Aeronáutica, os chefes das polícias estaduais."* com [28:11] *"vamos declarar guerra ao narcotráfico aqui no Brasil a partir de janeiro do ano que vem."*; a B, [27:58] *"Um dos meus primeiros atos"* e [28:11] *"vamos declarar guerra ao narcotráfico aqui no Brasil a partir de janeiro do ano que vem."* Não atendido: a A usou [37:21] *"Mas é importante falar, ele tem que ser melhorado."*, sobre o Estatuto do Desarmamento; a B, [05:24] *"combatendo a corrupção e fazendo uma gestão com inteligência artificial, que é o que eu vou propor."*

⚠️ As duas marcaram como leitura incerta *"os RODs do petróleo"* [04:50]. Nas duas, os itens de receita do ajuste fiscal foram contados como proposta, com o valor como número.

### C3 · O que foi dito como fato e se sustentou

Está na **seção 3**, preenchido só com as métricas finais da checagem. As passadas copiaram as métricas antes da auditoria final, com duas alegações ainda provisórias; os números delas para o C3 ficam superados pelos da seção 3.

### C4 · Uso do tempo

*Indicador:* parcela do tempo de fala; vezes em que a entrevistadora retomou a palavra antes de a resposta terminar; vezes em que o candidato falou por cima da pergunta.

| | Passada A | Passada B |
|---|---|---|
| tempo de fala de Flávio Bolsonaro (soma de segmentos) | 1.500,5 s · **63,9%** | 1.500,5 s · **63,9%** |
| tempo de fala de Renata Lo Prete | 848,6 s · **36,1%** | 848,6 s · **36,1%** |
| pelo método de turnos (com pausas) | não fez | 64,3% · 35,7% |
| entrevistadora entra com a frase dele cortada | **0** | **0** |
| candidato começa com a frase dela cortada | **2** ([16:03], [35:22]) | **1** ([16:03]) |
| sobreposição verificada no vídeo (fala curta dela dentro da resposta dele) | não usou | **1** ([35:22]) |
| candidato toma a palavra no meio de um turno dela, depois de frase completa | **2** ([16:11], [21:24]) | **2** ([16:11], [21:24]) |
| retomadas da entrevistadora depois de frase completa | 20, listadas; 8 se declaram volta à pergunta | 9 retomadas da mesma pergunta, contadas no C1 |
| candidato segue falando depois de *"Mas vamos para a próxima pergunta."* [37:18] | 1 | registrado, fora da contagem |

**Onde concordam.** O tempo é o mesmo nas duas: perto de dois terços para o entrevistado, e por bloco a mesma forma (a maior parcela dele nas considerações finais, 88%; a da entrevistadora maior nos blocos do Rio de Janeiro e da Polícia Federal, e perto da metade no do caso Master). Nenhuma das duas achou vez em que a entrevistadora entrou com a frase do candidato cortada. As duas acharam a mesma virada com a frase dela cortada em [16:03] e as mesmas duas tomadas de palavra no meio de um turno dela. As duas lembram que o tempo dela inclui abertura, chamada e volta do intervalo e encerramento.

**Onde divergem, e por quê (fonte e regra do sinal).**
- **O trecho de [35:22]:** a A leu só o texto, onde nenhum segmento se sobrepõe, e contou *"Candidato..."* como frase dela cortada pelo candidato; a B usou a sobreposição declarada em `falantes.json`, conferida pela IA nos quadros do vídeo, e leu como fala curta dela dentro da resposta dele, que segue. É o mesmo episódio lido em sentidos opostos.
- **As retomadas depois de frase completa:** a A listou 20, dizendo que pelo texto não dá para saber se a resposta tinha terminado; a B contou no C1 só as retomadas da mesma pergunta, pelas palavras dela. As duas listas têm em comum [06:57], [07:43], [24:41], [31:04], [33:51] e [35:34].

Por isso o total de vezes em que o candidato começou com a frase da entrevistadora pela metade fica **entre 1 e 2, conforme a fonte**. Sobreposição real de áudio fora de [35:22] não é observável nesta transcrição (as duas registram).

**Exemplos.** Atendido: a A usou a resposta corrida de [40:03] a [41:15] sobre saúde, até [41:10] *"Então é assim que eu vou fazer o Brasil sem filas"*, seguida de [41:16] *"O tempo acabou"*; a B, [09:14] *"Então, da minha parte, nenhum questionamento com relação a isso."* → [09:18] *"Agora, eu vou para um assunto de que o senhor tem falado bastante, que é o tamanho do mandato presidencial."* Não atendido, um de cada lado (B): [16:03] *"gerido por um amigo do seu..."* → [16:04] *"Não, não é um fundo imobiliário, Renata."*; e [35:22] *"Candidato..."* → [35:23] *"Alguém que der um tiro,"*, com a resposta seguindo até [35:33].

### C5 · Tratou do dado da pergunta

*Indicador:* quando a pergunta trouxe um número ou fato, a resposta tratou dele, contestou com outro dado, ou não tratou.

| Passada A (unidade: **pergunta**) | | Passada B (unidade: **cada fato**) | |
|---|---|---|---|
| perguntas com dado ou fato | **19** | fatos contados | **34** |
| tratou | 7 | tratou | 13 |
| contestou ou contrapôs com outro dado ou fato | 4 | contestou com outro dado | 6 |
| tratou em parte | 5 | contestou sem dado | 2 |
| não tratou | 3 | não tratou | 12 |
| | | não se aplica (a entrevistadora encerrou o ponto) | 1 |

**Os denominadores (19 e 34) não se comparam: a unidade é diferente.** A A classificou cada pergunta inteira e tem `em parte` para a pergunta com vários fatos em que só alguns foram tratados; a B separou cada fato da pergunta e não tem `em parte`. É divergência de regra de contagem, as duas declaradas.

**Onde concordam, no mesmo fato.** Sem tratar o dado, nas duas: as propostas de reforma do Judiciário do plano registrado no TSE ([12:26]), a pergunta sobre o ministro Nunes Marques e as mensagens apreendidas ([14:18]) e o efeito da retirada da marcação na investigação de crimes ([32:55]). Tratado, nas duas: a extensão do mandato de 4 para 5 anos ([09:23]), os aliados que vão tentar aprovar a proposta original do PL ([08:43]), as movimentações para anular a condenação do pai ([23:19]), os fatos do 8 de janeiro ([29:21]) e as prisões de aliados no Rio ([38:17]). Contestado com outro dado ou fato, nas duas: os economistas sobre os 200 bilhões ([03:14]), a troca do ministro pelo pai ([22:01]) e a pesquisa Quaest sobre limitar o acesso a armas ([35:46]).

**Onde divergem, no mesmo fato (leitura de categoria, não de contagem).**

| Fato | Passada A | Passada B |
|---|---|---|
| juros da dívida quase o dobro de saúde e educação [00:49] | tratou em parte, com outro dado | não tratou (trouxe outros números sobre juros) |
| *"eleitoreira"* e *"oportunista"* [06:00] | tratou (a pergunta, sobre a mudança de posição; as duas palavras não aparecem) | não tratou (o fato seguinte, a mudança de posição, tratou) |
| a perícia da produtora: o filme custou 75 milhões [18:10] | tratou em parte | tratou |
| afastamento das Forças Armadas da política [27:12] | tratou em parte (contestou o enquadramento, sem dado) | contestou, sem dado |
| crítica do ministro anunciado à demora das vacinas [39:38] | tratou em parte (a pergunta, sobre o futuro, foi tratada) | não tratou (a pergunta, em [39:54], pede o futuro) |

Este texto não escolhe entre as leituras da tabela: em todas a pergunta é se *trazer outro número*, *contestar o enquadramento* ou *responder à pergunta sem tocar no fato do preâmbulo* conta como tratar o dado, e o indicador escrito antes não decide isso. A B registra ainda que, na atuação pelo projeto que retira a marcação ([32:41]), contou `não tratou`, e que outra leitura, defensável, contaria `tratou`.

**Exemplos.** Atendido: a A usou [38:49] *"Essas revelações sobre políticos com os quais o senhor conviveu de perto, surpreenderam o senhor?"* → [38:56] *"Surpreenderam e eu acho que as pessoas têm o direito de se defenderem"*; a B, [18:10] *"A perícia da própria produtora disse que o filme custou 75 milhões de reais e o senhor pediu 134 ao Vorcaro."* → [18:22] *"era um contrato que não foi cumprido"* (é um dos fatos da tabela acima: a A o pôs em `em parte`). Não atendido: a A usou [32:55] *"a eliminação desse registro compromete tanto a investigação de autoria de crimes quanto a possibilidade de descobrir como é que armas legais vão parar na mão do crime organizado."*, com a resposta de [33:10] a [33:51] e, na terceira vez, [35:39] *"Eu acho que isso é uma coisa muito menor"*; a B, [14:13] *"Daí eu pergunto, mas e o ministro Cássio Nunes Marques?"* → [14:31] *"Tem que estar abaixo da lei."*, com o nome sem voltar na resposta, que segue até [15:34].

Se a contestação estava certa é o C3, e não entra aqui.

### C6 · Clareza para quem assiste

*Indicador:* termos técnicos e siglas sem explicação, por resposta; respostas cuja mensagem principal cabe numa frase da própria fala.

| | Passada A | Passada B |
|---|---|---|
| respostas | 21 | 21 |
| termos sem explicação | **20** (5 de uso corrente, 1 trazido pela pergunta, marcados) | **11**, em 9 respostas (+ 2 referências a episódios sem explicação) |
| termos explicados na própria fala | citados na tabela | 14 |
| mensagem principal numa frase da própria fala | **19 de 21** | **21 de 21** |

**Onde concordam.** Oito termos aparecem sem explicação nas duas: boletim Focus, *gap*, securitizado, MBA, se declarar suspeito, fundos podres, aval da União e CACs. Três deles estão nas respostas sobre o ajuste fiscal. *"Golpe da Disney"* também ficou sem explicação nas duas (a A contou como termo, a B como referência a episódio). Nas duas, Magnitsky, *voucher*, faixa azul, telemedicina, Prontuário Único Eletrônico, Escudo das Américas e Tríplice Fronteira vêm explicados na própria fala.

**Onde divergem, e por quê.**
- **20 × 11 termos: regra de contagem.** A A contou as siglas de uso corrente (PCC três vezes, MST, SUS), o termo que a entrevistadora usou antes (*"ajuste fiscal"*) e a repetição de um termo em outra resposta (*"narcoterroristas"*), marcando cada caso; a B tirou os três tipos. A A contou *"os RODs do petróleo"*, que a B deixou fora por leitura incerta, e *"golpe da Disney"*, que a B pôs na coluna de referências. Tirando esses, sobram 11 na A.
- **Leitura diferente nos termos restantes (julgamento):** *"PEC"* e *"penduricalhos"* a A deu como explicados (pelo conteúdo dito junto e por *"privilégios"*), a B como sem explicação; *"cargos em comissão"* a B contou e a A deixou fora; *"carreira de Estado"*, *"narcoterroristas"* e *"nuvem"* a A contou e a B não listou. Três de cada lado, e por isso os dois totais restantes ficam em 11.
- **Mensagem numa frase (19 × 21):** na resposta sobre o 8 de janeiro e na de armas e Estatuto, a A não achou frase que juntasse os fios; a B usou [29:43] *"Dentro da lei, conforme na proporção dos crimes que eles cometeram,"* e [37:30] *"O problema está nas armas na mão das pessoas erradas."*, e anotou que, na primeira, o resto da fala vai para outro assunto. As duas passadas marcaram esta metade do C6 como a leitura mais sujeita a juízo; este texto não decide.

**Exemplos.** Atendido, o mesmo nas duas: [26:17] *"O Alexandre de Moraes toma uma Magnitsky que é uma punição do governo americano com base na lei americana"*. Não atendido: a A usou [04:21] *"Isso pode ser colocado num fundo, pode ser securitizado"*; a B, [36:26] *"onde houve um recorde, inclusive, de emissões de certificáveis dos CACs, a taxa de homicídio caiu 17%"*.

---

## 3 · C3 · O que foi dito como fato e se sustentou

*Fonte:* só as métricas finais da checagem (`metricas/`), depois da revisão adversarial e da auditoria final de 17/out (143 vereditos mantidos, 64 alterados, contando a auditoria final). As passadas não fizeram este critério: copiaram as métricas de antes da auditoria, com a A113 e a A161 provisórias. Na versão final, a A113 ficou `IMPRECISO` e a A161 `VERDADEIRO`, e outros vereditos mudaram na auditoria; os números abaixo substituem os das passadas.

**207 afirmações de fato** foram conferidas na sabatina. **206 eram checáveis**; uma, do candidato, no bloco de armas e segurança pública, ficou `NÃO CHECÁVEL` e não entra no denominador dos percentuais, como faz o arquivo de métricas.

| Lado da mesa | Tempo de fala | Afirmações | Checáveis (denominador) | Verdadeiro | Impreciso | Sem comprovação | Falso | Não checável | Por minuto de fala |
|---|---|---:|---:|---:|---:|---:|---:|---:|---:|
| Flávio Bolsonaro (entrevistado) | 25:00 | 124 | **123** | 66 · 53,7% | 23 · 18,7% | 25 · 20,3% | 9 · 7,3% | 1 | 4,96 |
| Renata Lo Prete (entrevistadora) | 14:09 | 83 | **83** | 65 · 78,3% | 3 · 3,6% | 15 · 18,1% | 0 · 0,0% | 0 | 5,87 |
| total | 39:09 de fala (42:47 de peça) | 207 | **206** | 131 · 63,6% | 26 · 12,6% | 40 · 19,4% | 9 · 4,4% | 1 | |

As nove afirmações classificadas como `FALSO` estão nos blocos de ajuste fiscal (uma), reforma do Judiciário (uma), caso Master (duas), Jair Bolsonaro e a condenação (uma) e armas e segurança pública (quatro).

O bloco do caso Master tem 17 das 40 classificadas como `SEM COMPROVAÇÃO`, de 33 alegações no bloco, somando os dois lados da mesa. Parte delas são valores que só aparecem na imprensa sobre material de investigação não público, com a investigação da Polícia Federal em curso e sob sigilo; a checagem registra que nada ali diz que o valor é falso.

🔴 **Os dois lados da mesa não se comparam direto.** Quem responde fala mais e afirma mais (124 contra 83, em 25:00 contra 14:09; a entrevistadora fez mais afirmações por minuto de fala), e as afirmações da entrevistadora são, na maior parte, o contexto das perguntas. Um percentual menor de `VERDADEIRO` pode vir só do tempo de fala e do assunto. `SEM COMPROVAÇÃO` quer dizer que a busca não achou fonte que sustente, e não que alguém provou o contrário.

⛔ **Nada disso é placar**, nem nota, nem medida de quem diz mais verdade. `FALSO` e `IMPRECISO` não se somam: são vereditos diferentes, e somá-los é a conta que a metodologia proíbe.

---

## 4 · Percepção pública

*Fonte:* [`percepcao-publica.md`](percepcao-publica.md), levantado em 17/out/2026 com dez buscas (duas recusadas pela ferramenta por domínio bloqueado) e vinte páginas capturadas, com cada trecho conferido por script contra o texto capturado (40 de 40 achados). As passadas A e B não fizeram esta parte.

**Pesquisa de opinião sobre a reação à sabatina: ainda não existe.** Até 17/out, nenhum instituto (Datafolha, Quaest, AtlasIntel, Paraná Pesquisas ou outro) publicou levantamento que pergunte ao eleitor como ele avaliou esta entrevista. Ficaram fora, com o motivo: uma pesquisa Quaest em campo de 17 a 20/out, noticiada de segunda mão pela NC News, que é de intenção de voto e mede o cenário, não a reação; as pesquisas de intenção de voto do 2º turno que aparecem nas páginas; e a audiência de 21 pontos, atribuída pelo Portal Área VIP a uma coluna da Folha de S.Paulo não aberta, que mede quem assistiu, não o que achou.

**Análises de veículos, originais e atribuídas (como o arquivo registrou):**

| Fonte | Data | O que registrou | Observação |
|---|---|---|---|
| Terra, Beatriz Araujo | 17/out, 07h18 | dois especialistas ouvidos pelo veículo comparam as duas sabatinas; Doacir Gonçalves de Quadros (UNINTER): *"Flávio Bolsonaro não soube aproveitar esse espaço concedido na entrevista para sobretudo conquistar o voto do eleitor indeciso"*; Adriane Buarque de Holanda (Esfera Lab, ESPM Rio), na paráfrase do veículo: *"Holanda avalia que Flávio Bolsonaro usou muito mais tempo de sua entrevista para atacar Lula enquanto apresentou propostas rasas."* | duas pessoas ouvidas por um veículo, não uma amostra; a comparação entre as sabatinas é deles |
| O Folha de Minas, Redação | 17/out, 08h36 | que a entrevista teve *"respostas que fugiram das perguntas"*, e também que *"Em alguns temas, Flávio respondeu diretamente."* (6x1, aposentadorias, pisos de saúde e educação, mandato único, respeito ao resultado); que o ajuste de R$ 200 bilhões *"permaneceu sem detalhamento suficiente"* | as perguntas que o veículo lista como respondidas diretamente estão entre as classificadas `respondeu` nas duas passadas do C1; parte do texto se apoia em checagens de terceiros, que não são percepção |
| Metrópoles, Blog do Noblat, Ricardo Noblat | 17/out, 04h30 | sobre a resposta a respeito do resultado da eleição: *"Flávio respondeu de maneira pouco convincente"* | coluna de opinião assinada; boa parte do texto trata da trajetória do candidato |
| Revista Fórum, Blog do Rovai, Renato Rovai | 17/out, 10h57 | *"Acho difícil que ele tenha conquistado votos a partir dessa entrevista."* | blog de opinião; o veículo se apresenta como *"é o veículo mais antigo da mídia progressista"* |
| Revista Fórum, Plínio Teodoro | 17/out, 08h03 | contagem própria de 28 menções nominais a Lula e uma contagem do Ranking dos Políticos sobre 26 declarações | métodos diferentes do deste projeto; não substituem o C3 nem o C4 |
| TMC, Redação | 17/out, 11h32 | sobre o trecho do filme: *"cada vez que a jornalista Renata Lo Prete pressionava sobre os valores e a origem do financiamento, ele redirecionava o assunto para outros personagens ligados ao banqueiro Daniel Vorcaro"* | avalia um bloco, não a entrevista inteira |

**Reação de aliados da campanha, noticiada.** O Poder360 (17/out, 00h26) registrou que *"deputados e apoiadores elogiaram as respostas e criticaram a condução da conversa pela jornalista Renata Lo Prete"*, entre eles Nikolas Ferreira (PL-MG): *"Flávio calmo e posturado na sabatina da Globo"*. São aliados políticos, não analistas independentes; entra como reação noticiada, não como análise de veículo.

**Cobertura descritiva, sem avaliação do desempenho:** Gazeta do Povo, Jovem Pan, Poder360, Congresso em Foco, Terra, Metrópoles, Blog do Esmael Morais e Brasil 247. Na Gazeta do Povo e na Jovem Pan, procuradas por estarem na lista de orientações diferentes, as páginas achadas são relato. A Revista Oeste só apareceu com matéria de antes da entrevista.

**De segunda mão, fora como número:** a NC News atribui a colunistas notas de 1 a 5 para os candidatos e frases sobre esta entrevista nos dois sentidos; a publicação original não foi achada, e as notas não entram, pela mesma régua usada na sabatina de 15/out.

Ficaram fora, com o motivo: a TVT News (página de agosto, sobre a sabatina do 1º turno), a Rádio Capital FM (matéria sobre panelaços, com avaliação sem autor identificado), o Brasil em Folhas (data errada da entrevista), uma coluna sobre bastidor anterior à entrevista e as checagens de Lupa, UOL Confere e Aos Fatos (são checagem, não percepção).

⚠️ **A exigência de duas fontes independentes e de orientações diferentes foi cumprida em parte** (§5 do arquivo). Duas fontes independentes: cumprida (Terra, O Folha de Minas, Metrópoles, Revista Fórum e TMC avaliam a entrevista em texto original). Orientações diferentes: só em parte. As avaliações originais vêm de veículos de cobertura geral e de um veículo que se declara progressista; nos veículos procurados do outro lado da lista só apareceu relato; e a leitura favorável aparece como reação de aliados noticiada e como frases de colunistas de segunda mão, não como análise original de veículo.

⚠️ **As seções de percepção das duas sabatinas não se comparam.** A de 15/out foi feita no dia seguinte com seis buscas e achou três fontes; esta, com dez buscas, achou mais material. A diferença vem do método, não do que foi dito. **Esta seção precisa ser refeita** quando houver pesquisa de instituto sobre a reação às sabatinas e quando o original das notas de colunistas for achado; se as duas forem apresentadas lado a lado, a de 15/out tem de ser refeita antes com a mesma régua.

---

## 5 · As duas passadas, onde divergiram, e o teste de troca

**Como foram feitas.** A passada A leu a transcrição com os nomes. A passada B foi feita por outro agente, sem abrir a A, também com os nomes: numa sabatina com um candidato só não houve cópia anonimizada, e o controle do nome é o teste de troca. Nenhuma das duas fez busca na web; a percepção pública foi levantada à parte (seção 4).

**Resumo das divergências.**

| Critério | Divergência | Natureza |
|---|---|---|
| C1 | 32 × 30 perguntas; quatro classificações diferentes | contagem (duas falas da entrevistadora lidas como pergunta refeita ou como afirmação) e regra de leitura (premissa contestada ou comentada) |
| C2 | 24 × 22 propostas; 8 × 9 com dois ou mais elementos | recorte de proposta (o *"Sim."* ao mínimo e o Bolsa Família) e um caso de classificação (margem equatorial) |
| C3 | não se aplica | as duas deixaram para as métricas, e os números delas ficaram superados pela auditoria final |
| C4 | 2 × 1 viradas com a frase dela cortada; [35:22] lido em sentidos opostos | fonte (só texto × `falantes.json`) e regra do sinal |
| C5 | 19 perguntas × 34 fatos; cinco fatos com categoria diferente | unidade de contagem e leitura de categoria |
| C6 | 20 × 11 termos; 19 × 21 mensagens numa frase | regra de contagem (uso corrente, termo da pergunta, repetição, leitura incerta) e julgamento em seis termos e em duas respostas |

**O que as duas acharam igual**, apesar das regras diferentes: quatro respostas para outro assunto nas mesmas perguntas, entre elas as duas primeiras sobre a marcação das cápsulas; nenhuma proposta com os cinco elementos e o prazo numa só; o tempo de fala; nenhuma retomada da entrevistadora com a frase dele cortada; a virada de [16:03] e as duas tomadas de palavra no meio de um turno dela; os três dados da pergunta que ficaram sem tratamento nas duas leituras (plano do TSE, Nunes Marques, efeito na investigação); oito termos sem explicação e Magnitsky explicada.

**O teste de troca** (regra 3 do `CRITERIOS.md`: cada frase relida com o nome do outro candidato do 2º turno, Lula, no lugar; fica só a que continua justa).
- **Na passada B**, nove frases do rascunho não passaram: **cinco foram reescritas** (*"o candidato não respondeu, como a própria entrevistadora registrou"*, *"a entrevistadora precisou voltar à pergunta nove vezes"*, *"ele falou por cima da entrevistadora três vezes"*, *"ele minimizou os ataques"*, *"o candidato evitou falar de Nunes Marques"*) e **quatro foram tiradas** (*"usou boa parte das respostas para atacar o adversário"*, *"as propostas mais detalhadas foram as de receita do ajuste fiscal"*, *"boa parte do que ele afirmou como fato não se sustentou"*, *"trouxe números sem fonte"*), por leitura de intenção, juízo sem indicador, ranking que o critério não tem, soma de vereditos ou veredito sem checagem. Passaram as tabelas, as regras e as citações, e a frase de que o candidato teve perto de dois terços do tempo.
- **Na passada A**, o teste foi aplicado às linhas de contagem e aos exemplos, que são só número e citação; a A registra que o teste completo era da passada espelho.
- **Neste documento**, o teste foi aplicado a todas as frases das seções 1 a 7. Seis frases do rascunho não passaram: *"Flávio ocupou quase dois terços da entrevista"* virou a parcela medida com a frase de que este é o desenho de uma sabatina (*"ocupou"* sugere intenção); *"deixou sem resposta a pergunta sobre as cápsulas"* virou *"as duas leituras dizem que as duas primeiras respostas foram para outro assunto"* (*"deixou"* sugere escolha, e o C1 mede só a janela de 30 segundos); *"a entrevistadora teve de refazer a pergunta três vezes"* virou *"a pergunta veio três vezes"* (*"teve de"* põe a causa num lado); *"errou nove vezes"* virou *"nove foram classificadas como falsas"*; no texto da forma B, *"falou mais do adversário do que de propostas"* saiu (nenhum critério mede isso, e a contagem de menções é de terceiro, com outro método); e, no texto da forma C, *"a maior parte das análises foi negativa"* saiu (somar opiniões não vira percepção medida). As tabelas e as citações passaram sem mudança e valem do mesmo jeito para a sabatina de 15/out.

---

## 6 · O que não pode ser afirmado a partir disto

- quem convenceu quem, ou se a sabatina mudou algum voto;
- quem vai ser eleito em 25/out;
- quem governaria melhor, ou se alguma proposta é boa, viável ou barata (o C2 mede só se ela veio com elementos);
- que uma resposta `em parte` ou `tratou de outro assunto`, ou um dado `não tratado`, foi uma esquiva: os critérios medem o que foi dito, não por quê;
- a intenção de qualquer pessoa, do candidato ao responder ou da entrevistadora ao perguntar e retomar a palavra;
- que o percentual de `VERDADEIRO` de um lado da mesa é melhor ou pior que o do outro, ou que `FALSO` e `IMPRECISO` somados dizem alguma coisa;
- que um fato ainda em apuração (inquérito ou processo sem decisão) é verdadeiro ou falso: nesses casos o que existe é `SEM COMPROVAÇÃO`, com a investigação em curso;
- que as contagens de terceiros citadas na seção 4 (menções ao adversário, declarações falsas ou imprecisas) confirmam ou contradizem o C3 ou o C4: os métodos são outros;
- o que o público achou da entrevista, enquanto não houver pesquisa de instituto;
- qualquer comparação de placar com a sabatina de Lula de 15/out: os critérios são os mesmos, mas as perguntas, os temas e o tempo foram diferentes, e os resultados das duas não se comparam como placar.

---

## 7 · Texto-base para a fala do vídeo

🔑 **A escolha da forma é do autor.** A IA entrega as três e não escolhe. Os riscos (skill §5 e `CRITERIOS.md`):

| Forma | Risco |
|---|---|
| **A · critério a critério** | o menor: cada frase tem indicador e exemplo |
| **B · síntese que nomeia** | 🔴 **o maior.** É a frase que o projeto diz que não faz: para juntar seis critérios numa frase alguém escolhe quais entram e com que peso, e a IA não escolhe pesos. Numa sabatina, ainda é a frase mais fácil de recortar e usar como propaganda, contra ou a favor, sem o resto do texto |
| **C · só a percepção medida** | menor, mas nenhuma pesquisa mediu a reação até 17/out; as análises originais achadas são de cobertura geral e de um veículo que se declara progressista, e a leitura favorável aparece só como reação de aliados da campanha. Se for dita junto com a forma C da sabatina de 15/out, aquela tem de ser refeita antes com a mesma régua |

Os três textos usam porcentagem redonda e as contagens em que as duas passadas concordam; onde elas divergem, a fala dá a faixa.

### Forma A · critério a critério

> Os critérios foram escritos antes das sabatinas, e a IA leu a entrevista inteira com eles em duas leituras separadas, uma sem ver a outra. O que vem agora é a leitura da IA, e ela não soma os critérios nem dá nota.
>
> O primeiro critério olha se a resposta falou do assunto da pergunta logo no começo. Uma leitura contou 32 perguntas e a outra contou 30. Nas duas, mais da metade teve resposta direta, e de quatro a seis respostas foram para outro assunto nos primeiros 30 segundos, conforme a regra usada. A pergunta sobre tirar a marcação das cápsulas de munição veio três vezes, e as duas leituras dizem que as duas primeiras respostas foram para outro assunto.
>
> O segundo critério olha as propostas. A IA contou quantas vinham com pelo menos duas coisas entre meta, prazo, jeito de fazer, de onde sai o dinheiro e quem faz. Deu entre um terço e 40% das propostas. Só uma trouxe prazo: reunir os comandantes e declarar guerra ao narcotráfico a partir de janeiro.
>
> O terceiro critério vem da checagem. Flávio fez 124 afirmações de fato, e 123 deu para conferir. Delas, 66 se confirmaram, pouco mais da metade. Perto de 20% estavam imprecisas, outros 20% ficaram sem fonte que sustentasse, e nove foram classificadas como falsas. A entrevistadora fez 83 afirmações nas perguntas, e 65 se confirmaram. Esses números ficam lado a lado, sem comparação direta, porque quem responde fala mais e afirma mais, e eles não viram placar.
>
> No tempo, Flávio ficou com perto de dois terços da fala, que é o desenho de uma sabatina. Nenhuma das leituras achou vez em que a entrevistadora entrou com a frase dele cortada. Ele começou a falar com a frase dela pela metade uma ou duas vezes, conforme a fonte usada para contar.
>
> Quando a pergunta trazia um número ou um fato, a IA olhou se a resposta falava daquilo. As duas leituras concordam em três casos em que a resposta não falou: as propostas de reforma do Judiciário do plano de governo, a pergunta sobre o ministro Nunes Marques e o efeito de tirar a marcação das cápsulas na investigação de crimes. E concordam em casos em que falou, como os fatos do 8 de janeiro.
>
> O último critério é a clareza para quem assiste. As duas leituras acharam oito termos usados sem explicação, como securitizado, boletim Focus e CACs. E acharam termo explicado na hora, como a Magnitsky, que ele disse ser uma punição do governo americano.
>
> Nada disso diz quem convenceu quem, quem vai ganhar no dia 25 ou quem governaria melhor. Os mesmos seis critérios foram usados na sabatina de Lula, no dia 15, e esta leitura não compara os resultados das duas.

### Forma B · síntese que nomeia

> Juntando os seis critérios numa frase, e essa frase é uma escolha da IA sobre o que entra: Flávio deu resposta direta a mais da metade das perguntas, e de quatro a seis respostas foram para outro assunto no começo; entre um terço e 40% das propostas vieram com pelo menos dois detalhes, como meta, prazo ou jeito de fazer; e pouco mais da metade do que disse como fato se confirmou na checagem. Isso descreve como a entrevista foi usada, e não diz quem convenceu ninguém nem quem vai ganhar.

### Forma C · só a percepção medida

> Até o dia 17 de outubro, quando a IA fez a busca, nenhum instituto de pesquisa tinha medido o que o público achou da sabatina. Uma pesquisa da Quaest estava em campo, mas é de intenção de voto. O que existe são análises e comentários. No Terra, o especialista Doacir Quadros, da Uninter, disse que o candidato não aproveitou a entrevista para conquistar o eleitor indeciso. Numa coluna no Metrópoles, Ricardo Noblat escreveu que a resposta sobre o resultado da eleição foi pouco convincente. O Poder360 registrou elogios de aliados da campanha, como o deputado Nikolas Ferreira. A IA procurou veículos de orientações diferentes e, em alguns deles, só achou relato, sem avaliação. Por isso essa parte fica incompleta até sair pesquisa.

---

## 8 · Conferência do texto-base

Detector de cara de IA do repositório do canal (`referencias-conteudo/roteiros/scripts/detectar-cara-de-ia.py`), rodado em 17/out/2026 sobre um arquivo temporário só com as falas das três formas da seção 7 (sem o sinal de citação, o mesmo conteúdo que o modo `--falas` leria): **671 palavras, 0 ocorrências, 0,0 por mil palavras** (meta: abaixo de 3). O detector listou à parte, fora da taxa, 25 números por extenso, que aqui são contagens ditas em voz alta (duas leituras, seis critérios) e ficam como estão. O detector aponta candidatos; a leitura em voz alta é do autor.

Travessão: `grep -c` por travessão e meia-risca neste arquivo dá **0**.

Citações: os trechos entre aspas e em itálico do documento foram conferidos por script contra a passada A, a passada B e o arquivo de percepção (normalizando caixa e pontuação): 95 trechos, 84 achados; os 11 restantes são as frases do rascunho deste documento citadas no teste de troca (seção 5), que não vêm de fonte.
