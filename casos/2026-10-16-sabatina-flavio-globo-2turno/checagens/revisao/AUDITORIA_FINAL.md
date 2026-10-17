# Auditoria final: caso 2026-10-16-sabatina-flavio-globo-2turno

**Data:** 17/10/2026 · **Auditor:** Claude (auditor final, sem participação na extração, na checagem nem nas revisões deste caso) · **Base auditada:** `checagens/checagens-sabatina-completa.json` (207 checagens: 134 VERDADEIRO, 27 IMPRECISO, 35 INSUSTENTAVEL, 11 FALSO, 0 NAO_CHECAVEL) · **Régua:** `docs/METODOLOGIA.md` §2 a §5, `.cursor/rules/etica-e-risco.mdc`, `skills/revisar-checagem.md`, e os casos de 15/out (`2026-10-15-sabatina-lula-globo-2turno`) e 28/ago (`2026-08-28-sabatina-flavio-globo`).

Nada foi corrigido nos arquivos do caso (lotes, juntado, alegações, cortes). Este documento só registra o que foi conferido e o que foi achado. Os únicos arquivos novos fora deste documento são o pedido de captura `checagens/pedidos-captura/auditoria-final.json` e a pasta `capturas/2026-10-16-sabatina-flavio-globo-2turno-aud/`, gerados pelo processo do repositório. A decisão sobre cada achado é do autor do projeto.

---

## 1. A amostra

**Como foi sorteada.** Script em Python, `random.Random(16102026)`. Os ids de cada veredito foram ordenados e sorteados nesta ordem, com o mesmo gerador: todas as FALSO; 6 IMPRECISO; 8 INSUSTENTAVEL; 8 VERDADEIRO. Depois foram somados todos os ids dos 6 cortes em `recortes/SUGESTAO_DE_CORTES.json` (campo `escolhidos`). Refazer, da pasta do caso:

```python
import json, random
ch = json.load(open("checagens/checagens-sabatina-completa.json", encoding="utf-8"))["checagens"]
por = {}
for c in ch: por.setdefault(c["veredito"], []).append(c["id"])
for v in por: por[v].sort()
rng = random.Random(16102026)
falso = por["FALSO"]
imp = sorted(rng.sample(por["IMPRECISO"], 6))
ins = sorted(rng.sample(por["INSUSTENTAVEL"], 8))
ver = sorted(rng.sample(por["VERDADEIRO"], 8))
cortes = {e["id"]: e["ids"] for e in json.load(open("recortes/SUGESTAO_DE_CORTES.json", encoding="utf-8"))["escolhidos"]}
```

| Grupo | Ids |
|---|---|
| FALSO (todas, 11) | A024, A069, A100, A103, A110, A123, A165, A167, A182, A183, A184 |
| IMPRECISO (6) | A036, A074, A144, A159, A181, A194 |
| INSUSTENTAVEL (8) | A037, A047, A081, A085, A173, A174, A196, A201 |
| VERDADEIRO (8) | A005, A039, A096, A128, A139, A175, A188, A191 |
| corte-01 | A075, A076, A077, A078 |
| corte-02 | A085, A086, A087 |
| corte-03 | A131, A132 |
| corte-04 | A158, A159, A160, A161, A162 |
| corte-05 | A185, A186, A187, A188 |
| corte-06 | A202, A203, A204 |

**Total: 51 checagens distintas** (33 do sorteio mais 21 dos cortes, menos A085, A159 e A188, que caíram no sorteio e também estão em corte). Por falante: 35 de Flávio Bolsonaro, 16 de Renata Lo Prete.

## 2. O que foi conferido em cada uma

Para as 51, nesta ordem:

1. **Frase e falante:** a `frase` contra `transcricao/transcricao.json`, no intervalo da alegação, com o falante do segmento, e a leitura de cerca de 12 s antes e 8 s depois para ver se a `afirmacao` e o card mudam o sentido. **Todas as 51 frases estão na transcrição, com o falante certo.**
2. **Trechos:** cada `trecho` (partido nos `[...]`) procurado por script no texto capturado (`capturas/<caso>-*/texto/<id>.txt`, achado pela URL nos `capturas.json` das pastas de 15 e 16/out) e cruzado com o manifesto `checagens/CAPTURAS.json`. Os 2 casos que o script marcou como parciais (A144, IBGE/SIDRA; A086, Banco Central SGS) foram conferidos à mão: diferença só de formatação do JSON (chave em maiúscula e espaços); os valores e as datas estão na captura. **Todos os trechos da amostra estão nas capturas.** Depois, leitura de cada trecho contra a coluna `prova`.
3. **Independência das fontes** (§3.1, regras 1 a 3) e N1/N2 quando há número.
4. **Árvore do §2.1 e régua de 10% do §2.2**, com as contas refeitas por script: A047 (354 contra 350: 1,1%), A086 (média de 2025 do SGS = 5,5855, 252 cotações; 24 × 5,5855 = 134,05; 24 × 6,0440 = 145,06; 24 × 5,0826 = 121,98; desvios de 2,3%, 7,6% e 9,8%), A144 (queda real de 4,2% de 2022 a 2025 e de 11,6% de 2019 a 2022, conferidas), A158 (1,6%), A185 (3,5 meses sobre 44,5: 7,9%), A186 (4/10/2026 é domingo; 17 dias), A187 (607,88 / 189 = 3,22; desvio de 6,7%). Comparação com checagens irmãs do mesmo caso nos dois lados da mesa e com 15/out e 28/ago.
5. **Ética §5** (fato em apuração nunca VERDADEIRO nem FALSO), leitura de intenção, travessão, adjetivo no resumo e na ressalva.
6. **Arquivos de corte:** veredito, resumo, ressalva, número apurado, explicação e fontes dos 21 itens em `checagens-corte-0N.json` são idênticos aos da completa (conferido por script). Cartela renderizada conferida: `overlay/cartelas-corte-03/A131.png`.
7. **Busca web: 9 chamadas (7 WebSearch, 2 WebFetch), só atrás do que contradiria um veredito:** base do "armada" na condenação de Bolsonaro (A123, 1 busca e 1 leitura); decisão de Moraes sobre armas apreendidas (A123, 1 busca); margem equatorial no plano de 2022 (A024); Vaccari no Instituto Lula (A100); a citação de Lottenberg (A201); entrevista de Eduardo ao SBT News (A131, 1 busca e 1 leitura, que caiu numa entrevista de dez/2025 e não serviu); motivo declarado por Bolsonaro para a troca na PF do Rio (A110). Cinco páginas foram capturadas pelo processo do repositório (`capturas/2026-10-16-sabatina-flavio-globo-2turno-aud`, ver §5).

---

## 3. ACHADOS

| # | Id | Quem fala | Veredito atual | O que se propõe | Por quê, em uma linha |
|---|---|---|---|---|---|
| 1 | A131 (corte-03, na tela) | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL (ou IMPRECISO, se aparecer segunda fonte independente) | uma única origem (Estadão Conteúdo) para a fala, e a própria ressalva diz o contrário do essencial |
| 2 | A039 | Flávio Bolsonaro | VERDADEIRO | ler o número na primária capturada; sem isso, INSUSTENTAVEL | mesma situação de prova da A173 e A174 (Renata), que ficaram INSUSTENTAVEL |
| 3 | A110 | Flávio Bolsonaro | FALSO | INSUSTENTAVEL | o motivo da troca está em disputa entre versões oficiais; o próprio Bolsonaro, em depoimento, deu motivo de gestão |
| 4 | A085 e A086 (+ A072) (corte-02, na tela) | Renata Lo Prete | INSUSTENTAVEL e VERDADEIRO | mesmo veredito para as duas (a régua escolhida pelo autor) | mesma situação de prova, vereditos opostos lado a lado no mesmo corte |
| 5 | A074 | Renata Lo Prete | IMPRECISO | VERDADEIRO com ressalva | o rótulo "fundo imobiliário" é o objeto registrado do fundo; o próprio resumo confirma |
| 6 | A183 | Flávio Bolsonaro | FALSO | NAO_CHECAVEL com justificativa, ou fundir na A184 | lê ao pé da letra um "autoriza" cuja causa dita na mesma frase é a falta de fiscalização, já checada na A184 |
| 7 | A123 | Flávio Bolsonaro | FALSO | mantém FALSO; acrescentar a fonte que resolve a leitura "arma de fogo" | a revisão chamou de "forte" a leitura de arma de fogo, e o arquivo não tem a prova que a responde |

### Achado 1 · A131 (corte-03, vai para a tela) · VERDADEIRO com uma fonte só, e a ressalva contradiz o essencial

**A frase** (Renata, 1548 s): "porque dias atrás ele deu uma entrevista dizendo que quem vai decidir isso é o pai de vocês". O "isso" é se Eduardo será chanceler (pergunta anterior: "Eduardo será chanceler?").

**O problema.** (a) As duas fontes que trazem a fala de Eduardo (Diário do Grande ABC e Times Brasil) são o mesmo texto do Estadão Conteúdo, o que a própria explicação declara ("as duas matérias que trazem a fala vêm do mesmo serviço de agência"); a terceira (Correio da Manhã) só confirma que o cargo estava em discussão, não a fala. Pela regra 3 da §3.1 é uma fonte; pela árvore do §2.1, sem duas independentes, INSUSTENTAVEL. A busca desta auditoria achou a mesma fala em O Povo, O Liberal, Jornal do Comércio, Midiamax e Muita Informação, todas do mesmo serviço; a entrevista original do SBT News não foi achada. (b) No conteúdo, a fala literal é geral ("As nomeações de ministros vão passar pelo presidente Jair Bolsonaro", trecho do DGABC), e sobre a própria ida ao ministério, que é o "isso" da pergunta, Eduardo disse o contrário: "se for da vontade de Flávio me ter em um Ministério, estou à disposição" (trecho do Times Brasil, já capturado na p14). A cartela renderizada mostra o selo verde com a ressalva "Sobre a própria ida ao Itamaraty, Eduardo disse que depende da vontade de Flávio": cor e ressalva apontam para lados opostos.

**A régua dos dois lados.** A A201 (Renata, citação de Lottenberg sem a entrevista original) e a A138 (Flávio, prazo só com imprensa) ficaram INSUSTENTAVEL por falta de fonte; a A131 é atribuição de fala com uma origem só.

**O que deveria mudar.** INSUSTENTAVEL, com o resumo dizendo o que a agência registrou (nomeações passam por Jair; sobre a própria indicação, a vontade de Flávio). Se o autor achar uma segunda apuração independente da fala (o vídeo do SBT News de 10/10/2026), o veredito pela árvore passa a IMPRECISO: a parte geral confere, a parte específica ("isso", a chancelaria) está trocada. Em nenhum dos dois casos fica verde. Regerar a cartela e o render do corte-03.

### Achado 2 · A039 · "grande maioria" de Flávio com prova igual à da "maioria" de Renata, e vereditos opostos

**A frase** (Flávio, 470 s): "Como eu ouvi da grande maioria dos trabalhadores, que eles estavam favoráveis ao fim da escala seis por um". VERDADEIRO.

**O problema.** A fonte marcada como N2 (PDF da Genial/Quaest, captura p04-r5) tem no trecho só a especificação técnica ("PESQUISA REGISTRADA SOB O NÚMERO BR-03598/2026"); a explicação admite que "os percentuais estão em gráficos sem texto, e por isso o número vem do Poder360". Conferi o PDF bruto (`capturas/2026-10-16-sabatina-flavio-globo-2turno-p04-r5/bruto/6089a208e39f.pdf`): a pergunta "Você é a favor ou contra o fim da escala 6x1?" está na página 18, e o número não é extraível como texto nem como imagem embutida (a imagem da página é só o fundo). Os 68%, 69% e 71% vêm de Poder360, CartaCapital e Times Brasil (N4). A primária, portanto, não foi conferida no número, e a regra 2 da §3.1 não se cumpre.

**A régua dos dois lados.** A A173 (Renata, "a maioria dos brasileiros considera que limitar o acesso melhora a segurança", Quaest com a Pax) foi rebaixada de VERDADEIRO a INSUSTENTAVEL na revisão da rodada 2 exatamente por isso: "fontes de imprensa só bastam quando a primária que citam foi conferida, e aqui não foi; e a afirmação é sobre um número ('a maioria'), que pela regra 1 pede fonte N1 ou N2"; a A174 seguiu a mesma régua. A explicação da A173 afirma que "todas as outras checagens de pesquisa deste caso [...] que saíram com veredito colorido têm o relatório do instituto": a A039 tem o relatório, mas não o número lido nele. Hoje a régua favorece o candidato. A diferença real a favor da A039 (dois institutos, Quaest e Datafolha) não muda o ponto, porque o Datafolha também entra só pela reprodução do Times Brasil.

**O que deveria mudar.** Renderizar a página 18 do PDF já capturado e registrar o percentual lido (como se fez na A161 com os rótulos do gráfico do Mapa de Empresas). Se o número estiver lá, a A039 fica VERDADEIRO com a N2 de fato conferida, e a frase da explicação da A173 passa a ser verdadeira. Se não for possível, INSUSTENTAVEL, pela régua da A173.

### Achado 3 · A110 · FALSO para um motivo que as fontes oficiais disputam entre si

**A frase** (Flávio, 1347 s): "ele trocou o superintendente do Rio de Janeiro na época, se não me engano, porque estava apresentando maus resultados". FALSO.

**O problema.** A frase afirma o motivo de uma troca. O arquivo opõe a ela a nota da PF de 2019 ("não guardando qualquer relação com o desempenho do atual ocupante do cargo"), o recuo de Bolsonaro no dia seguinte, a fala de Moro (parte na disputa) e, para 2020, a promoção do superintendente que saiu (indício, não contradição: a explicação diz que "não combina"). Mas há o registro do próprio autor da troca, em depoimento à PF no inquérito que apurou exatamente isso, dando motivo de gestão: "Que sugeriu a mudança porque o Estado do Rio de Janeiro é muito complicado e entendia que necessitava de um dirigente da Polícia Federal local com maior liberdade de trabalho", e, sobre Ricardo Saadi, que ele "não tinha a completa independência para tomar as medidas necessárias para melhorar a gestão local" (Poder360, 4/nov/2021, capturado nesta auditoria, `capturas/2026-10-16-sabatina-flavio-globo-2turno-aud`, id a5dd69760514; o mesmo depoimento está em 74407be6f6ca). Há, portanto, duas versões oficiais do motivo (a da PF e a do presidente), e nenhuma fonte mede desempenho da superintendência. "Maus resultados" não é exatamente "melhorar a gestão", mas a distância entre os dois é de ornamento, e o que a nota da PF contradiz é a versão do presidente, não um dado.

**A régua.** O §2.1 manda FALSO quando as fontes contradizem o essencial; aqui elas divergem entre si sobre um estado mental de terceiro, e o veredito escolhe uma versão. É a situação que o caso trata como INSUSTENTAVEL em outras falas sobre motivo e envolvimento (A081, A089, A196).

**O que deveria mudar.** INSUSTENTAVEL, com o resumo dizendo que a PF negou relação com desempenho em 2019 e que Bolsonaro, em depoimento de 2021, atribuiu a troca à necessidade de melhorar a gestão local; registrar a divergência em `divergencia_entre_fontes`. As duas páginas novas são uma fonte só (mesmo veículo, mesmo depoimento) e entram como registro da versão do presidente.

### Achado 4 · A085 e A086 (corte-02, vão para a tela), com a A072 · mesma prova, cores opostas no mesmo corte

**As frases** (Renata, 1090 a 1096 s, uma pergunta só): "A perícia da própria produtora disse que o filme custou 75 milhões de reais" (A085, INSUSTENTAVEL) "e o senhor pediu 134 ao Vorcaro" (A086, VERDADEIRO; A072 é a mesma afirmação, também VERDADEIRO).

**O problema.** A A085 ficou laranja porque "o laudo, anexado a inquérito, não é público e não foi conferido" e a regra 1 pede N1/N2 para valor. A A086 está na mesma situação no essencial: o valor de US$ 24 milhões vem só da imprensa sobre material de investigação não público (Intercept, com as mensagens; Correio da Manhã; O Povo e TVT News com o relatório da PF). A única N1 da A086 é a série de câmbio do Banco Central, que prova a conversão, não o pedido. Nas duas há confirmação pela parte interessada: na A086, "Flávio Bolsonaro admitiu ter tido uma conversa com Daniel Vorcaro [...] para que ele repassasse US$ 24 milhões" (Correio da Manhã, p08); na A085, o valor é "informação revelada pela Go Up Entertainment, produtora do filme" (A Tarde, p09). Uma checagem pode ser verde e a outra laranja só pelo artifício de pôr uma N1 de câmbio numa delas (a A085 também tem valor em dólar, US$ 13,3 milhões, convertível pela mesma série). No vídeo, o espectador vê a mesma pergunta da mesma jornalista com um número verde e outro laranja.

**O que deveria mudar.** Decidir uma régua e aplicá-la às três (A072, A085, A086). Pela letra da regra 1 da §3.1, a saída coerente com A078, A090, A138, A173 e A174 é INSUSTENTAVEL para A072 e A086, com o resumo atual (que diz o que as reportagens trazem). Se o autor entender que a confirmação pública pela parte que negociou ou encomendou o documento vale como primária para um valor não público, isso vira regra escrita na metodologia, e a A085 vai a VERDADEIRO com a ressalva que já tem (laudo encomendado, sem notas fiscais). Regerar as cartelas do corte-02.

### Achado 5 · A074 · IMPRECISO para um rótulo que o registro confirma

**A frase** (Renata, 960 s): "foi parar num fundo nos Estados Unidos, um fundo imobiliário". IMPRECISO.

**O problema.** As fontes confirmam o rótulo: o Havengate Development Fund "foi criado originalmente para vender a investidores [...] um projeto imobiliário de 21,1 milhões de dólares no Texas" (Intercept, com os registros) e, segundo o relatório da PF, "havia sido criado originalmente, em 2020, para um empreendimento imobiliário" (TVT News). O IMPRECISO pune uma implicação que a frase não faz ("sugere que o dinheiro foi para negócio imobiliário"); a revisão r3 já anotou que "o veredito pune uma implicação". O resumo do card ("O fundo nasceu para um projeto imobiliário que não saiu do papel e nunca teve terreno; depois recebeu verba do filme") confirma a jornalista, com cor amarela. Comparação: a A036 (Flávio, IMPRECISO) troca a categoria de fato ("cargos em comissão" para um total que inclui funções e gratificações); a A074 usa a categoria registrada do fundo.

**O que deveria mudar.** VERDADEIRO, com ressalva: o fundo nunca teve imóvel e, desde fevereiro de 2025, a única atividade conhecida é receber o dinheiro do filme. A A075 (Flávio, "não é um fundo imobiliário [...] faz só a gestão do filme") continua INSUSTENTAVEL pelo motivo que já tem (a segunda metade está em apuração). Achado de menor gravidade: é escolha de leitura, mas hoje a cor contradiz o texto do próprio card.

### Achado 6 · A183 · o "autoriza" lido ao pé da letra, e a mesma ideia contada como dois FALSO

**A frase** (Flávio, 2245 a 2250 s, uma oração só): "e autoriza os marginais a comprarem armas de guerra porque não tem fiscalização nenhuma". A extração separou "autoriza os marginais a comprarem armas de guerra" (A183, FALSO, pelo texto da Lei 10.826) de "porque não tem fiscalização nenhuma" (A184, FALSO, pelas apreensões).

**O problema.** A própria frase dá a causa da "autorização": a falta de fiscalização. Nenhuma leitura razoável entende que a lei permite legalmente a compra por criminosos; a revisão r7 registrou o argumento ("a frase quer dizer que o crime se arma porque a lei não funciona") e o derrubou pela leitura literal. O conteúdo factual da oração é o da A184, que já é FALSO. O resultado é a mesma afirmação contada duas vezes como FALSO contra o candidato, e um card que refuta o que ninguém afirmou. A revisão já apontou dupla contagem do mesmo tipo em favor do candidato (A081 e A089); aqui é contra.

**O que deveria mudar.** Ou NAO_CHECAVEL, com a justificativa escrita de que "autoriza" é figura cuja parte checável está na A184 (§2, aviso do `NAO_CHECAVEL`), ou fundir A183 na A184, com o intervalo das duas. Se o autor mantiver o FALSO, registrar no relatório que A183 e A184 são uma oração só. Achado de menor gravidade.

### Achado 7 · A123 · FALSO de pé, mas sem no arquivo a prova da leitura que a revisão chamou de forte

**A frase** (Flávio, 1430 s): "Ele foi condenado por organização criminosa armada e não foi encontrado uma arma em lugar nenhum". FALSO.

**O problema.** A revisão r5 diz que a leitura "arma de fogo" é "forte" (é o que a qualificadora mira, a Gazeta do Povo diz que nenhuma arma de fogo foi apreendida com os manifestantes, o Planalto disse que as armas do GSI não eram letais, e o agravante citado pela CNN vem de um plano). As fontes do arquivo respondem a essa leitura só com facas, porretes e armas do GSI de letalidade disputada. A busca desta auditoria, feita para derrubar o FALSO, achou o contrário: decisão de Moraes, assinada em 28/08/2026 e publicada em 01/09/2026 (antes da fala), que manda destruir sete armas de fogo apreendidas de Bolsonaro como instrumentos do crime: "Nessa perspectiva, os armamentos apreendidos, empregados ou destinados à atuação da associação criminosa armada qualificam-se como instrumentos do crime e sujeitam-se ao confisco como efeito da condenação" (Congresso em Foco, id 9117659250bc; o mesmo trecho está na Gazeta do Povo, id 316f08de46d5, e no A Crítica, id 421eec8c7c48, capturados em `capturas/2026-10-16-sabatina-flavio-globo-2turno-aud`). É registro judicial, sobre a condenação definitiva, de armas de fogo ligadas pelo STF à organização armada: contradiz o "em lugar nenhum" também na leitura estrita.

**Nuance a declarar.** A Gazeta do Povo diz que as armas "foram apreendidas após o episódio envolvendo um de seus agentes de segurança", isto é, não no curso da investigação do golpe; o que as liga à organização é a qualificação da decisão ("empregados ou destinados").

**O que deveria mudar.** Veredito mantido. Acrescentar a decisão (as duas reportagens, de linhas editoriais diferentes, citam o mesmo texto da decisão; pela regra 2, se o autor conseguir a decisão no portal do STF, ela vira a N1) e a nuance acima à explicação; a ressalva pode continuar com a Gazeta. A A148 (Renata, armas levadas do GSI, VERDADEIRO) não muda.

---

## 4. Uma linha por checagem auditada

| Id | Falante | Veredito | Resultado | Nota |
|---|---|---|---|---|
| A005 | Renata | VERDADEIRO | mantém | Lei 14.663 e Lei 15.077 (N1) dão ganho real com piso e teto; exceção do PIB negativo na ressalva |
| A024 | Flávio | FALSO | mantém | plano de 2022 lido por inteiro, sem margem equatorial; busca não achou o contrário. Ponto contra que a explicação poderia citar: o Plano Estratégico 2022-2026 da Petrobras, ainda no governo Bolsonaro, previa poços na margem equatorial; o FALSO depende de ler "proposta de governo" como o plano registrado, que é a leitura natural no contexto |
| A036 | Flávio | IMPRECISO | mantém | 21 mil no Decreto 9.725 somam cargos, funções e gratificações; mesma régua da A013 de 28/ago |
| A037 | Flávio | INSUSTENTAVEL | mantém | 22.500 não existe em fonte; apurado da imprensa (4,4 mil) sem a primária, igual à A014 de 28/ago e à régua aplicada a Renata |
| A039 | Flávio | VERDADEIRO | **Achado 2** | número só na imprensa; PDF da Quaest sem o número lido |
| A047 | Flávio | INSUSTENTAVEL | mantém | Gastômetro (R$ 354 bi, 1,1%) é soma de jornal, sem N1/N2, e o painel diz que não é só dinheiro desembolsado; mesma régua das A173 e A174 |
| A069 | Flávio | FALSO | mantém | arts. 44 a 48 da Lei 1.079 preveem deliberação e arquivamento; igual à A077 de 15/out. Observação: a decisão da ADPF 1.259, marcada N1, está hospedada em site de terceiro (correiosabia.com.br) |
| A074 | Renata | IMPRECISO | **Achado 5** | rótulo confirmado pelo registro do fundo |
| A075 | Flávio | INSUSTENTAVEL | mantém | "só a gestão do filme" é o que a PF rastreia (pedido aos EUA em 9/10); ética §5 |
| A076 | Renata | VERDADEIRO | mantém | Calixto no registro do Texas e descrito como amigo de Eduardo por BBC e piauí; Flávio não negou na sabatina |
| A077 | Flávio | VERDADEIRO | mantém, com observação | a `afirmacao` encolhe a frase ("experiente nisso" vira "é advogado"); a ressalva leva o registro de gestora abandonado em 2021. O resumo ("especialista em imigração") pode ganhar o "visto EB-5, modalidade [...] a estrangeiros que invistam", que está no mesmo trecho da BBC e liga a especialidade a fundos |
| A078 | Renata | INSUSTENTAVEL | mantém | prazo só com imprensa e uma origem (o relatório da PF cita o Intercept); mesma régua da A138 do candidato |
| A081 | Flávio | INSUSTENTAVEL | mantém | ausência de verba pública é objeto de inquérito; ética §5. Dupla contagem com a A089 já registrada pela revisão |
| A085 | Renata | INSUSTENTAVEL | **Achado 4** | mesma prova da A086 |
| A086 | Renata | VERDADEIRO | **Achado 4** | contas de câmbio refeitas e corretas; a N1 só cobre a conversão |
| A087 | Flávio | VERDADEIRO | mantém | US$ 12,3 mi pagos de US$ 24 mi; cobrança de parcelas atrasadas pelo próprio Flávio |
| A096 | Renata | VERDADEIRO | mantém | comunicado da Globo (15/10) e Poder360; datas batem com a fala de 16/10 |
| A100 | Flávio | FALSO | mantém | página oficial do instituto (triênio 2023/2026) sem Vaccari; busca não achou cargo dele no instituto |
| A103 | Flávio | FALSO | mantém, com observação | a nota da PF de 9/10 nega ter o relato e diz que a apuração começava; o FALSO é sobre a posição da PF, não sobre o mérito. Observação: as quatro fontes são N4 e a nota só entra pela "íntegra" do Congresso em Foco; capturar a nota no gov.br/pf fecharia a regra 2 |
| A110 | Flávio | FALSO | **Achado 3** | motivo em disputa entre versões oficiais |
| A123 | Flávio | FALSO | **Achado 7** (mantém) | falta no arquivo a decisão que responde à leitura "arma de fogo" |
| A128 | Flávio | VERDADEIRO | mantém | indicação por Lula e 58 a 18 no Senado (Agência Senado, N1) |
| A131 | Renata | VERDADEIRO | **Achado 1** | uma origem só; ressalva contradiz o essencial |
| A132 | Flávio | VERDADEIRO | mantém | mora nos EUA desde 2025 e atua de lá contra o STF; "arbitrariedades" separado como juízo |
| A139 | Renata | VERDADEIRO | mantém, com observação | medidas de despolitização documentadas; "processo de afastamento" é caracterização. Observação: o 61 para 17 do resumo vem só da Revista Sociedade Militar (site de nicho, "com dados do Estadão"); a contagem tem origem no TSE e poderia vir de lá |
| A144 | Flávio | IMPRECISO | mantém | queda real de 4,2% de 2022 a 2025 contra 11,6% de 2019 a 2022 (contas conferidas); "sucateadas" fica sem sustentação, a redução existe. Leitura no limite do juízo, mas coerente com A155 e A159 |
| A158 | Flávio | IMPRECISO | mantém | 2024 é o 2º no país (30,2 contra 30,7 mi ha), recorde só na Amazônia; posição errada, não valor. Coerente com a A161 (recorde por margem pequena, mas 1º) |
| A159 | Flávio | IMPRECISO | mantém | MVI na menor taxa desde 2012, recordes só em tipos específicos; recorte que inverte a tendência (§2.2) |
| A160 | Flávio | VERDADEIRO | mantém | Peic de jul/2026, 82,0%, recorde; mesma régua da A130 de 15/out; ressalva com a inadimplência |
| A161 | Flávio | VERDADEIRO | mantém | 2.436.190 fechamentos em 2024 contra 2,43 mi em 2018 (rótulo arredondado, argumento conferido); Sebrae como segunda fonte; resumo mostra o quase empate |
| A162 | Flávio | INSUSTENTAVEL | mantém | recorde de programas de maquila é de todas as origens; sem série de brasileiras; Aos Fatos: empresas não deixam o Brasil |
| A165 | Flávio | FALSO | mantém | PF e PRF, ouvidas pelo Comprova, fizeram a segurança de Dino na Maré |
| A167 | Flávio | FALSO | mantém | "não fiscaliza" absoluto contra operações e apreensões de 2025 e da véspera (página da PF, N1); regra 2 declarada para as três reproduções do balanço |
| A173 | Renata | INSUSTENTAVEL | mantém | relatório da Quaest/Pax não achado; ver Achado 2 sobre a A039 |
| A174 | Renata | INSUSTENTAVEL | mantém | mesma régua da A173 |
| A175 | Renata | VERDADEIRO | mantém | PDL 193/2023 de Flávio (Agência Senado) e Pollon na equipe; nuance de Pollon na ressalva |
| A181 | Flávio | IMPRECISO | mantém | a Constituição não traz "legítima defesa" (PEC 100/2019 não aprovada); o direito existe no Código Penal: lugar errado |
| A182 | Flávio | FALSO | mantém | Lei 10.826 e Decreto 11.615 preveem arma para defesa pessoal; o porte restrito vai na ressalva |
| A183 | Flávio | FALSO | **Achado 6** | leitura literal de "autoriza"; mesma oração da A184 |
| A184 | Flávio | FALSO | mantém | Sinarm, Exército e apreensões de fuzis em 2025; "nenhuma" absoluto |
| A185 | Flávio | VERDADEIRO | mantém | 44,5 meses contra 48 ditos, 7,9% sobre o apurado; leitura dos adicionais igual à de 15/out |
| A186 | Flávio | VERDADEIRO | mantém | 17/9 a 4/10/2026 (domingo) são 17 dias |
| A187 | Flávio | VERDADEIRO | mantém | 189 para 607,88 (3,2 vezes, desvio de 6,7%); caráter temporário e conta nominal na ressalva |
| A188 | Flávio | VERDADEIRO | mantém | R$ 189 (Agência Câmara) e "em torno de R$ 190" (FGV/IBRE, N2). Observação: Agência Câmara marcada N1 é agência de notícias; a N2 sustenta |
| A191 | Renata | VERDADEIRO | mantém | vídeo de 22/04/2026 (Poder360) e "chegou a gravar vídeos" (Estadão Conteúdo), apurações independentes |
| A194 | Renata | IMPRECISO | mantém | prisão documentada com fundamento formal diferente (vazamento e obstrução) da caracterização da PF (liderança do núcleo político); descreve atos formais, sem afirmar culpa |
| A196 | Renata | INSUSTENTAVEL | mantém | "enrolado" qualifica envolvimento em apuração; mesmo veredito da A076 de 15/out (que seguiu INSUSTENTAVEL depois da auditoria daquele caso) |
| A201 | Renata | INSUSTENTAVEL | mantém | a citação entre aspas não foi achada; a busca desta auditoria também não a achou |
| A202 | Flávio | VERDADEIRO | mantém | presidente da mantenedora de 2001 a 2016, três fontes |
| A203 | Flávio | VERDADEIRO | mantém | 1º do Brasil no ranking Newsweek/Statista 2026 (N2); "melhor" ancorado no ranking, ressalva sobre outros rankings |
| A204 | Flávio | VERDADEIRO | mantém | 16º do mundo, nenhum latino-americano acima |

**Conferências que passaram em toda a amostra:** todas as frases estão na transcrição com o falante certo; todos os trechos estão nas capturas; os arquivos de corte batem com a completa; nenhuma checagem da amostra está marcada como provisória nem com confiança baixa; nenhum resumo ou ressalva da amostra tem leitura de intenção, adjetivo sobre a pessoa ou travessão; todas as checagens que tocam fato em apuração (A075, A081, A103, A194, A196) declaram a ética §5, e nenhuma delas tem VERDADEIRO ou FALSO sobre o mérito da apuração.

**Sobre a régua entre os lados da mesa.** Fora dos achados 2 e 4, a régua é a mesma: número sem N1/N2 deu INSUSTENTAVEL para os dois lados (A037, A047, A090, A138 do candidato; A078, A085, A173, A174 da jornalista), e a régua de 10% foi medida sobre o apurado nos dois lados. As 11 FALSO são todas de Flávio; das sorteadas, A100, A165, A069 e A182 têm contradição direta em fonte primária ou checagem profissional, A167 e A184 são enunciados absolutos ("não fiscaliza", "nenhuma") contra registro de fiscalização, A024 e A103 dependem de uma leitura declarada da frase, e A110 e A183 são os achados 3 e 6.

## 5. Fontes externas consultadas nesta auditoria

Capturadas pelo processo do repositório (`python ferramentas/capturar-fontes.py 2026-10-16-sabatina-flavio-globo-2turno --pedido casos/2026-10-16-sabatina-flavio-globo-2turno/checagens/pedidos-captura/auditoria-final.json --saida capturas/2026-10-16-sabatina-flavio-globo-2turno-aud`, 17/10/2026):

- Congresso em Foco, decisão de Moraes sobre as armas (id 9117659250bc): https://www.congressoemfoco.com.br/noticia/121850/moraes-determina-que-comando-do-exercito-destrua-armas-de-bolsonaro
- Gazeta do Povo, idem (id 316f08de46d5): https://www.gazetadopovo.com.br/republica/moraes-manda-exercito-destruir-7-armas-de-bolsonaro/
- A Crítica de Campo Grande, idem (id 421eec8c7c48): https://acritica.net/justica/moraes-determina-destruicao-de-armas-apreendidas-com-jair-bolsonaro/
- Poder360, depoimento de Bolsonaro à PF, 4/nov/2021 (id a5dd69760514): https://www.poder360.com.br/governo/bolsonaro-diz-em-depoimento-que-nunca-buscou-informacoes-sigilosas-na-pf/
- Poder360, mesmo depoimento (id 74407be6f6ca): https://www.poder360.com.br/justica/bolsonaro-diz-que-sugeriu-mudanca-na-pf-do-rio-porque-estado-e-complicado/

Consultadas e não capturadas (não decisivas): resultados de busca sobre o plano de governo de 2022 e a margem equatorial (Itatiaia, eixos), sobre Vaccari e o Instituto Lula (nada encontrado), sobre a citação de Lottenberg (Correio Braziliense e Jovem Pan de 2021, sem a frase), sobre a entrevista de Eduardo (todas as versões do mesmo texto do Estadão Conteúdo; a página do SBT News lida era de 21/12/2025 e não tratava do assunto).

**Contagem exata de buscas: 9 chamadas** (7 WebSearch e 2 WebFetch), dentro do limite de 15.

## 6. O que fica para o autor

1. Decidir os achados 1 a 6 e registrar cada mudança em `CORRECOES.md` do caso (§7 da metodologia); regerar cartelas e render dos cortes 02 e 03 se A131, A085 ou A086 mudarem.
2. Achado 4: escolher a régua para valor de documento não público confirmado pela parte interessada e escrevê-la na metodologia, para não ser decidida caso a caso.
3. Achado 2: renderizar a página 18 do PDF da Quaest já capturado; se o número for lido, a A039 fica e a frase da explicação da A173 passa a ser verdadeira.
4. Achado 7: se a decisão de Moraes de 28/08/2026 estiver no portal do STF, capturá-la como N1 da A123.
5. Observações sem mudança de veredito (A024, A069, A077, A103, A139, A188): melhorias de fonte ou de texto, a critério do autor.
