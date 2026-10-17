# Correções da auditoria final (17/out/2026)

Aplicação, nos lotes, das decisões da IA que conduz o caso sobre os achados de `checagens/revisao/AUDITORIA_FINAL.md`. Nenhuma busca web nesta passada: as fontes novas já estavam capturadas em `capturas/2026-10-16-sabatina-flavio-globo-2turno-aud` (Poder360 `a5dd69760514` e `74407be6f6ca`; Congresso em Foco `9117659250bc`; Gazeta do Povo `316f08de46d5`), e a página 18 do PDF da Genial/Quaest (`capturas/2026-10-16-sabatina-flavio-globo-2turno-p04-r5`, bruto `6089a208e39f.pdf`) foi renderizada e guardada em `checagens/evidencias/quaest-maio-2026-escala-6x1-pagina-18.png`. Cada explicação mudada começa com "Auditoria final de 17/out/2026: ...".

Conferência: os lotes 04, 08, 09, 11, 13, 14 e 19 validam contra `esquemas/checagens.schema.json`, e a alegação A183 (na completa e no lote 05 de alegações, id local A011) valida contra `esquemas/alegacoes.schema.json`. Todo `trecho` dos ids mexidos, novo ou antigo, foi achado no texto capturado da própria URL com a função `conferir` de `ferramentas/conferir-trechos.py`. Todo número e ano de `resumo`, `ressalva` e `numero_apurado` está num trecho, numa derivação, na fala ou na data de referência. Sem travessão e sem termo de intenção. Só os lotes desses ids e os dois arquivos de alegação mudaram. O juntado, os arquivos de corte, as cartelas e o `revisao.json` ficam para a IA que conduz (`checagem-juntar`, `registrar-revisao`, render dos cortes 02 e 03).

| Id | Quem fala | Antes | Depois |
|---|---|---|---|
| A131 (corte-03) | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL |
| A039 | Flávio Bolsonaro | VERDADEIRO | VERDADEIRO (primária conferida no número) |
| A110 | Flávio Bolsonaro | FALSO | INSUSTENTAVEL |
| A071 | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL |
| A072 | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL |
| A085 (corte-02) | Renata Lo Prete | INSUSTENTAVEL | INSUSTENTAVEL (resumo e explicação) |
| A086 (corte-02) | Renata Lo Prete | VERDADEIRO | INSUSTENTAVEL |
| A074 | Renata Lo Prete | IMPRECISO | VERDADEIRO |
| A183 | Flávio Bolsonaro | FALSO | NAO_CHECAVEL |
| A123 | Flávio Bolsonaro | FALSO | FALSO (fonte nova e nuance) |

## A131 (lote 14)

- **Estava:** `VERDADEIRO`, confiança média; resumo "Em entrevista exibida em 10 de outubro, Eduardo disse que as nomeações de ministros vão passar por Jair Bolsonaro"; ressalva "Sobre a própria ida ao Itamaraty, Eduardo disse que depende da vontade de Flávio".
- **Passou a valer:** `INSUSTENTAVEL`, confiança média; resumo "Pelo Estadão Conteúdo, Eduardo disse que nomeações passam por Jair e que ir a um ministério depende de Flávio"; ressalva "A fala só aparece em textos de um mesmo serviço de agência; a entrevista original não foi achada"; explicação refeita. Fontes mantidas.
- **Por quê:** achado 1. As duas fontes que trazem a fala (Diário do Grande ABC e Times Brasil) são o mesmo texto do Estadão Conteúdo: pela regra 3 da METODOLOGIA §3.1, uma fonte só. A entrevista original ao SBT News (10/10/2026) não foi achada, nem pela auditoria nem por uma busca da IA que conduz em 17/out. Sem duas fontes independentes, a árvore do §2.1 dá `INSUSTENTAVEL`. O resumo diz o que a agência registrou, as duas partes: a fala geral sobre as nomeações e, sobre a própria ida a um ministério, a vontade de Flávio, que é o "isso" da pergunta. Com isso a cor deixa de contradizer a ressalva. O resumo diz "um ministério", e não "Itamaraty", porque é o que está no trecho capturado. Cartela e render do corte-03 precisam ser refeitos.

## A039 (lote 04)

- **Estava:** `VERDADEIRO`; a explicação dizia que o PDF da Quaest fora capturado, mas que o número vinha do Poder360 porque os percentuais estavam em gráfico sem texto.
- **Passou a valer:** `VERDADEIRO`, sem mudança de resumo, ressalva ou fontes. A explicação ganhou, no começo, a conferência da primária: a página 18 do PDF da Genial/Quaest de maio de 2026, renderizada em 17/out/2026, mostra 68% a favor do fim da escala 6x1 em maio de 2026 (69% em jul/2025, 72% em dez/2025). O número está em gráfico, sem texto extraível, e a imagem ficou em `checagens/evidencias/quaest-maio-2026-escala-6x1-pagina-18.png`. O trecho continua sendo o do Poder360, que reproduz a pesquisa. A `prova` da fonte N2 passou a citar a página lida.
- **Por quê:** achado 2. A regra 2 da §3.1 aceita imprensa quando a primária que ela cita foi conferida, e agora foi. É essa a diferença em relação à A173 e à A174 (Renata), que ficaram `INSUSTENTAVEL` porque a primária (Quaest com a Pax) não foi achada. A frase da explicação da A173 ("todas as outras checagens de pesquisa [...] têm o relatório do instituto") passa a ser verdadeira também no número.

## A110 (lote 11)

- **Estava:** `FALSO`; resumo "Em nota, a PF disse que a troca no Rio não tinha relação com o desempenho do superintendente"; sem ressalva; data de referência "agosto de 2019 e maio de 2020".
- **Passou a valer:** `INSUSTENTAVEL`, confiança média; resumo "A PF negou em 2019 relação com desempenho; em depoimento de 2021, Bolsonaro atribuiu a troca à gestão local"; ressalva "Nenhuma fonte mede o desempenho da superintendência do Rio na época da troca"; data de referência com o depoimento de 3/nov/2021; `divergencia_entre_fontes` com as duas versões oficiais do motivo. Entraram duas fontes, as duas páginas do Poder360 de 4/nov/2021 sobre o depoimento de Bolsonaro à PF, com o trecho "Que sugeriu a mudança porque o Estado do Rio de Janeiro é muito complicado e entendia que necessitava de um dirigente da Polícia Federal local com maior liberdade de trabalho" e o "melhorar a gestão local" sobre Ricardo Saadi. Pela regra 3, as duas valem como uma fonte só (mesmo veículo, mesmo depoimento), e isso está declarado na `prova` e na explicação.
- **Por quê:** achado 3. Há duas versões oficiais do motivo da troca de 2019: a da PF, que negou relação com desempenho, e a do próprio presidente, em depoimento no inquérito que apurou a interferência, que a atribuiu à gestão local. As fontes divergem sobre o motivo de um terceiro e não contradizem um dado (nenhuma mede o desempenho), e o §2.1 só manda `FALSO` quando as fontes contradizem o essencial. É a régua do caso para falas sobre motivo (A081, A089, A196).

## A071 (lote 08)

- **Estava:** `VERDADEIRO`; resumo "Os 7 repasses documentados somam US$ 12,3 milhões; no dólar de cada data, R$ 69,8 milhões"; ressalva "Reportagens citaram R$ 65 milhões; convertendo cada parcela pelo dólar do dia do repasse, o total é R$ 69,8 milhões".
- **Passou a valer:** `INSUSTENTAVEL`, confiança média; resumo "Reportagens com planilha e relatório do Coaf somam US$ 12,3 milhões em 7 repasses, R$ 69,8 milhões; a PF apura"; ressalva "Os valores vêm de documentos não públicos lidos pela imprensa; o câmbio do Banco Central só prova a conversão". Explicação com a frase da auditoria no começo e com as três passagens que davam `VERDADEIRO` reescritas. Fontes, derivações de câmbio e divergência entre fontes mantidas.
- **Por quê:** achado 4, régua 1 da §3.1. O valor só tem fonte de imprensa sobre material de investigação não público (planilha e comprovante do Intercept, relatório do Coaf da piauí, relatório da PF no O Povo). A série do Banco Central prova a conversão, não o valor. É a régua da A090 (Flávio) e da A126 do caso de 15/out. A A153 daquele caso só saiu de `INSUSTENTAVEL` quando a primária foi capturada, e por isso é citada com essa nuance. A investigação está em curso (etica-e-risco §5), e o card não diz que o valor é falso.

## A072 (lote 08)

- **Estava:** `VERDADEIRO`; resumo "Mensagens registram acordo de US$ 24 milhões com Vorcaro, cerca de R$ 134 milhões no câmbio da época"; ressalva "Acerto em dólares: a conversão vai de R$ 122 milhões, no câmbio do dia da fala, a R$ 145,1 milhões, no de janeiro de 2025".
- **Passou a valer:** `INSUSTENTAVEL`, confiança média; resumo "Reportagens com mensagens e relatório da PF dão acordo de US$ 24 milhões, cerca de R$ 134 milhões; a PF apura"; ressalva "O valor vem de material de investigação não público lido pela imprensa; o câmbio do Banco Central só prova a conversão". Explicação com a frase da auditoria no começo e com as passagens que davam `VERDADEIRO` reescritas. A faixa de conversão (R$ 122,0 a R$ 145,1 milhões) continua em `numero_apurado` e nas derivações. Fontes e derivações mantidas.
- **Por quê:** achado 4, a mesma régua da A071. A confirmação de Flávio sobre a conversa (Correio da Manhã) também chega pela imprensa e não substitui a primária. A072 e A086 são a mesma afirmação e saem idênticas no veredito, no resumo e na ressalva.

## A085 (lote 09)

- **Estava:** `INSUSTENTAVEL`; resumo "Reportagens dão US$ 13,3 milhões, pouco mais de R$ 75 milhões, no laudo da produtora; o laudo não é público".
- **Passou a valer:** `INSUSTENTAVEL`, confiança média; resumo "Reportagens dão US$ 13,3 milhões, pouco mais de R$ 75 milhões, em laudo da produtora anexado a inquérito em curso"; explicação com a frase da auditoria no começo. Ressalva e fontes mantidas.
- **Por quê:** achado 4. O veredito já era o da régua escolhida, e o resumo passou a dizer que a apuração está em curso (etica-e-risco §5). O lastro é o trecho da Tribuna de Jundiaí ("anexada ao inquérito que tramita na Polícia Civil de São Paulo"). A A085 e a A086, da mesma pergunta e no mesmo corte, agora saem com a mesma cor. As cartelas e o render do corte-02 precisam ser refeitos.

## A086 (lote 09)

- **Estava:** `VERDADEIRO`; resumo e ressalva iguais aos da A072 antiga.
- **Passou a valer:** idêntica à A072 no veredito (`INSUSTENTAVEL`), no resumo, na ressalva e na confiança (média), com a mesma reescrita da explicação. Ficaram a frase própria sobre a razão de 1,79 com a A085 e a fonte própria da TVT News ("custo declarado superior a R$ 75 milhões"), com as derivações.
- **Por quê:** achado 4, como na A072.

## A074 (lote 08)

- **Estava:** `IMPRECISO`; resumo "O fundo nasceu para um projeto imobiliário que não saiu do papel e nunca teve terreno; depois recebeu verba do filme"; sem ressalva.
- **Passou a valer:** `VERDADEIRO`, confiança média; resumo "Registros do Texas e relatório da PF: o fundo foi criado em 2020 para um empreendimento imobiliário"; ressalva "O fundo nunca teve imóvel e, desde 2025, sua única atividade conhecida é receber o dinheiro do filme"; explicação refeita. Fontes mantidas.
- **Por quê:** achado 5. "Fundo imobiliário" é o objeto registrado do fundo: o Intercept traz os registros, e a TVT News traz o relatório da PF. O `IMPRECISO` punia uma implicação que a frase não faz, e a cor contradizia o próprio resumo. O que as fontes acrescentam (nenhum imóvel; desde a remessa de 13/02/2025, só o dinheiro do filme, pelo O Povo) vai na ressalva. A A075 (Flávio) continua `INSUSTENTAVEL` pelo motivo que já tem: o que o fundo faz com o dinheiro está em apuração.

## A183 (lote 19; alegação na completa e no lote 05 de alegações, id local A011)

- **Estava:** `FALSO`, confiança alta; resumo "O Estatuto exige antecedentes limpos para comprar arma e pune com até 6 anos a arma de uso restrito sem autorização"; fontes: Lei 10.826/2003 e Decreto 11.615/2023. Na alegação: `checavel: true`, tipo `norma_vigente`.
- **Passou a valer:** `NAO_CHECAVEL`, confiança alta, `fontes: []`, sem número apurado, ressalva nem data de referência; resumo "Figura de linguagem: a própria frase diz que a causa é a falta de fiscalização, checada em separado". A explicação tem o porquê. Na alegação: `checavel: false`, tipo `juizo_de_valor`.
- **Por quê:** achado 6. "Autoriza" é figura, e a própria oração dá a causa ("porque não tem fiscalização nenhuma"). A parte checável da oração é a da A184, já `FALSO`. A lei não autoriza criminoso a comprar arma, e ninguém na fala diz que ela autoriza legalmente. Contar as duas como `FALSO` seria contar a mesma afirmação duas vezes. A METODOLOGIA §2 e §5 exige que o `NAO_CHECAVEL` diga o porquê, e a explicação diz. O validador vai avisar que há uma alegação `juizo_de_valor` na extração (§4.2); a explicação responde ao aviso. As duas normas continuam como fontes da A184.

## A123 (lote 13)

- **Estava:** `FALSO`, com seis fontes, nenhuma delas sobre arma de fogo ligada à condenação.
- **Passou a valer:** `FALSO`, sem mudança de resumo, ressalva ou confiança. Entraram duas fontes sobre a decisão de Moraes assinada em 28/08/2026 e publicada em 01/09/2026, que manda destruir sete armas apreendidas de Bolsonaro: Congresso em Foco (`9117659250bc`) e Gazeta do Povo (`316f08de46d5`). As duas citam o mesmo trecho da decisão: "Nessa perspectiva, os armamentos apreendidos, empregados ou destinados à atuação da associação criminosa armada qualificam-se como instrumentos do crime e sujeitam-se ao confisco como efeito da condenação". A explicação ganhou o achado, a declaração da regra 2 (a decisão não foi capturada no portal do STF, e as duas reportagens reproduzem a mesma primária) e a nuance: as armas foram apreendidas depois de um episódio com um agente de segurança de Bolsonaro, não no curso da investigação do golpe, e o que as liga à organização armada é a qualificação da decisão. A data de referência ganhou a decisão.
- **Por quê:** achado 7. A revisão r5 chamou de forte a leitura "arma de fogo", e o arquivo não tinha a prova que a responde. A decisão é registro judicial, anterior à fala e sobre a condenação definitiva, e contradiz o "em lugar nenhum" também nessa leitura.
