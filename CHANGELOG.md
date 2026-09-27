# Histórico

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).
Versionamento [semântico](https://semver.org/lang/pt-BR/).

---

## [0.2.0] · 26/set/2026

Segunda rodada: o repositório olhado de fora, as travas que faltavam, o que o público apontou no vídeo publicado, e o segundo caso.

### Corrigido

- **A CI reprovava em todos os pushes desde o primeiro commit.** O validador exigia as cartelas PNG, que são derivadas e ficam fora do git: num clone limpo a porta fechava para todo mundo, e o `ESTADO.md` dizia que os três comandos passavam. Agora pasta ausente é nota, pasta incompleta é erro, e a CI desenha as cartelas antes de validar e reprova plano de overlay velho.
- **A trava da citação casava em pedaço de palavra.** A comparação era de substring sobre o texto normalizado: uma citação que começasse no meio de uma palavra passava. Agora é palavra inteira, no validador e na conferência de trecho, com teste.
- A captura de fonte lia página em Windows-1252 como UTF-8 (acento quebrado não é cópia literal) e não descomprimia gzip mandado sem pedido.
- A documentação dizia `--fade` no PASSO 6, opção que nunca existiu; `FADE_S` era constante morta.
- O relatório não avisava em cima quando a peça não é íntegra, regra de `etica-e-risco` §4 que só existia em prosa.

### Adicionado: travas no validador

Cada uma com teste que prova o defeito que pega (`tests/test_travas_novas.py`):

- **ano na tela também precisa de lastro** (`anos_de()`), o conserto do "desde 1986";
- número e ano da **ressalva** passam pela mesma regra do resumo;
- **VERDADEIRO com número dito diferente do apurado** exige ressalva que mostre o valor apurado (defeito apontado por um espectador, ver abaixo);
- travessão e leitura de intenção em texto de tela reprovam;
- `data_de_referencia` obrigatória onde o esquema já dizia que era;
- alegação fora da `cobertura` declarada reprova;
- o plano de overlay tem que concordar com as checagens (veredito velho deixaria a moldura com a cor errada);
- fonte consultada antes da extração vira aviso;
- nota com a contagem de revisão humana e de capturas assinadas, e aviso para trecho que não está na página capturada.

### Adicionado: a tela

- `citacao_card`: trecho literal menor da fala, conferido contra a transcrição, para quando a citação não cabe em duas linhas. A cartela mede e avisa texto cortado.
- Legenda de abertura sem o veículo repetido, com data legível, o endereço do repositório e "arredondamento vira ressalva".
- **Cartela de encerramento** sobre o último quadro congelado: onde conferir, como contestar e quantas checagens tiveram revisão humana. O áudio continua copiado.
- `midia recortar --enquadrar`: vídeo vertical entra inteiro em 1920x1080, sem corte nem deformação.
- **Tempo de leitura por card** e **congelamento final**: cada card fica no mínimo o tempo de ler o resumo e a ressalva, e a fila que passa do fim do trecho congela o último quadro antes do encerramento, declarado no plano ([`docs/IDENTIDADE_VISUAL.md` §7](docs/IDENTIDADE_VISUAL.md)). O plano do caso Lula foi regerado: três cards que ficavam 3s na tela passaram a ficar entre 6,6s e 9s, e o vídeo ganha 2s de congelamento no fim. ⚠️ O vídeo publicado do caso Lula precisa ser renderizado de novo pela pessoa que tem o arquivo de origem.

### Adicionado: evidência e nuvem

- `ferramentas/capturar-fontes.py` e `conferir-trechos.py`: cada fonte é capturada com sha256, e cada trecho é conferido contra a página. O recibo vai para `checagens/CAPTURAS.json`.
- `ferramentas/comparar-transcricao.py`: lista onde a transcrição diverge de uma publicada, com prioridade para número e nome próprio.
- `ferramentas/registrar-revisao.py`, para a pessoa que revisou registrar isso; `ferramentas/validar-todos.py`, o que a CI roda.
- Workflows `nuvem-preparar-midia`, `nuvem-capturar-fontes`, `nuvem-segunda-passada` e `nuvem-renderizar`, para quem não tem a máquina ou a rede ([`docs/NUVEM.md`](docs/NUVEM.md)). Tudo volta num release em **rascunho**, que só quem tem escrita no repositório vê.

### Corrigido no caso Lula, com registro em `CORRECOES.md`

- **`A017` passou de VERDADEIRO para IMPRECISO.** O registro oficial do Senado lista Francisco Lopes como presidente do Banco Central aprovado em 1999; a checagem o tratava como interino, e o trecho da lista citada omitia a linha dele. Foram cinco presidentes e quatro trocas no governo FHC, não três.
- `A021`: um espectador apontou "94 bi marcado como verdadeiro, com 92,4 bi na tela". O veredito estava certo pela régua (1,7%), mas o card não dizia o arredondamento. Corrigido, e a fonte da IFI apontava para uma URL que não existia.
- `A007`: contestação pública (Argentina e Arábia Saudita). Arábia Saudita, improcedente; Argentina, procedente como divergência de conceito, agora no card. Veredito mantido pelo critério escrito antes da checagem.
- `A009`: a média "0,9%" de 2011 a 2020 era projeção de 2019; o realizado é 0,3%.
- Lastro de texto de tela em `A002`, `A006`, `A010`, `A011` e `A013`; trechos reescritos ou truncados refeitos como cópia literal em `A005`, `A006`, `A018`, `A020` e `A023`; revisão da série do BCB registrada em `A002` e `A003`.

### O caso Flávio refeito (27/set)

- O autor achou o primeiro trecho do Flávio focado em juízo de valor. Estava certo: três juízos foram extraídos como alegações, contra a METODOLOGIA §4.2. O validador passou a avisar, e o erro está registrado no caso (e o mesmo, menor, no caso Lula).
- Caso novo, `2026-08-28-sabatina-flavio-globo-economia`: o bloco de economia oficial do g1, escolhido por tema. 21 alegações de fato, 55 trechos conferidos, 14 verdadeiras, 4 imprecisas, 3 sem comprovação.
- `nuvem-sondar-videos`: consulta metadados de vídeos candidatos sem baixar.
- Travessão no nome de instituição (linha de fontes do card) passa a reprovar; SEM COMPROVAÇÃO sem fonte N1/N2 vira aviso, como manda a árvore do §2.1.

### O segundo caso

`2026-08-28-sabatina-flavio-globo`. O vídeo pedido (cópia do canal "EDUARDO BOLSONARO" no YouTube) não pôde ser baixado: o YouTube recusa servidor, e a íntegra oficial do Globoplay não toca fora do Brasil. O caso foi feito sobre o **trecho oficial publicado pelo g1** (2min44s), declarado como `trecho` no topo do relatório e na cartela. Ver `ESTADO.md`.

---

## [0.1.1] — 11/set/2026

### Corrigido

- **A contagem de fontes estava errada em dois documentos.** `ESTADO.md` e este `CHANGELOG` diziam **56 citações de fonte**; a contagem feita sobre `checagens-bloco-contas-publicas.json` dá **52** (33 URLs distintas, 20 instituições). O 56 foi escrito sem ser contado, e nenhum validador confere número de documentação. Descoberto ao reunir material para um vídeo sobre o projeto, pela regra de recalcular número derivado antes de reusá-lo. ⚠️ Nenhum veredito, fonte ou alegação mudou: só o número que descrevia o total.
- **A documentação dizia que o erro do "desde 1986" tinha sido pego pela revisão humana. Não foi.** O registro da sessão de 06/set mostra que quem pegou foi uma segunda leitura da própria IA, depois de o validador reprovar outros itens; nenhuma pessoa tinha lido a checagem naquele momento. Corrigido em `casos/.../CORRECOES.md` (com a linha antiga riscada, não apagada), em `docs/METODOLOGIA.md` §3.1 e na limitação abaixo. ⚠️ É o mesmo defeito do erro que a frase descrevia: soava certo e foi escrito sem conferir. **Revisão humana registrada segue em zero** (`ESTADO.md`, item 2).

---

## [0.1.0] — 06/set/2026

Primeira versão. Prova de conceito completa: um caso real, do arquivo de vídeo ao vídeo checado, com o processo inteiro aberto.

### Adicionado

**O pipeline**, em oito passos, com cinco determinísticos e três de julgamento:

- `passo1_midia` — assina a mídia com sha256, mede, extrai áudio 16 kHz mono e recorta trechos guardando o tempo absoluto na peça;
- `passo2_transcrever` — `whisper.cpp` local, com o sha256 do modelo gravado no cabeçalho da transcrição;
- `passo3_falantes` — aplica um mapa de turnos escrito à mão, e imprime a distribuição de tempo de fala;
- `passo6_overlay` — desenha cada cartela como um quadro inteiro de 1920x1080 no Pillow, e enfileira as janelas de exibição;
- `passo7_renderizar` — um `overlay` por cartela, áudio copiado sem reencodar, com conferência de duração e de nível de áudio;
- `passo8_validar` — a porta, que sai com código 1;
- `relatorio` — o documento público do caso, com cada fonte, trecho e derivação.

**A metodologia**, com cinco vereditos (`VERDADEIRO`, `IMPRECISO`, `INSUSTENTAVEL`, `FALSO`, `NAO_CHECAVEL`), árvore de decisão, hierarquia de fontes em quatro níveis e as armadilhas de enquadramento.

**As travas que o validador executa:**

- a citação do card tem que existir na transcrição, comparada em texto normalizado;
- todo número do veredito precisa de lastro num trecho de fonte, ou de uma derivação declarada com as parcelas e a conta;
- duas fontes independentes, com URLs distintas, e pelo menos uma primária ou institucional quando a alegação é numérica;
- nenhuma alegação sem checagem, e nenhuma checagem órfã;
- confiança baixa exige revisão humana registrada;
- nenhuma cartela sobreposta, nenhuma fora do vídeo.

**Quatro skills** (`preparar-caso`, `extrair-alegacoes`, `checar-alegacao`, `fechar-caso`), **quatro regras** sempre ativas e **três esquemas JSON**.

**Duas ferramentas de apoio:** `corrigir-transcricao.py`, que aplica correções de reconhecimento deixando rastro, e `conferir-links.py`, que impede documentação apontando para arquivo inexistente.

**35 testes**, incluindo regressão sobre o caso publicado, e CI que roda lint, testes, validador e links.

**O caso `2026-08-27-sabatina-lula-globo`:** sabatina da TV Globo com Luiz Inácio Lula da Silva, 44min33s. Transcrição completa (709 segmentos), 110 turnos de falante justificados um a um, e o bloco de contas públicas (4min52s) checado com **23 alegações** e 52 citações de fonte (33 URLs distintas).

### Decisões de arquitetura registradas

- **Extração e checagem em arquivos separados**, com a internet fechada na primeira: quem já sabe a resposta escolhe as perguntas.
- **Transcrição local**, não API: mesma entrada, mesmo modelo, mesma saída.
- **Falante por mapa de turnos escrito à mão**, não diarização automática: atribuir frase à pessoa errada é o pior erro possível aqui, e um arquivo de turnos é auditável linha a linha.
- **Cartela como quadro inteiro em PNG**, não `drawtext`: quebra de linha medida em pixels, acentuação e canto arredondado.
- **Corte seco, sem fade**, e **uma cartela por vez na tela**.
- **Mídia fora do git, manifesto dentro:** o repositório guarda o que foi dito e a checagem, não o arquivo.

### Corrigido durante a primeira rodada

Todos são defeitos que aconteceram de verdade e estão registrados em [`ESTADO.md`](ESTADO.md):

- cartela com duração negativa quando duas alegações saíam da mesma frase — as janelas viraram fila;
- `ValueError` ao pedir o peso `Regular` no arquivo itálico da Inter, que chama a instância de `Italic`;
- `Unrecognized option 'filter_complex_script'`, removida no ffmpeg 8 — a opção agora é escolhida pela versão;
- o rótulo "SEM COMPROVAÇÃO" escrevendo por cima da descrição na cartela de legenda, por coluna de largura fixa;
- ressalva cortada no meio da frase, por caber em uma linha só;
- card dizendo "FONTES: IBGE" com dois documentos do IBGE — passou a mostrar a contagem;
- o selo "CHECAGEM ABERTA" sumindo nos intervalos entre cards — virou camada própria;
- medição de nível de áudio voltando vazia sem erro, porque `volumedetect` escreve em nível informativo;
- a linha de fontes do card estourando a caixa em 92px, porque os nomes das instituições eram concatenados sem medir.

### Corrigido no conteúdo do caso

Registrado em [`casos/2026-08-27-sabatina-lula-globo/CORRECOES.md`](casos/2026-08-27-sabatina-lula-globo/CORRECOES.md):

- um resumo afirmava "a maior taxa desde 1986" **sem fonte nenhuma**, escrito de memória;
- duas fontes com a mesma URL contadas como duas fontes distintas;
- trechos citados que não continham os números afirmados na checagem.

⚠️ Nenhuma dessas correções mudou um veredito. Todas apertaram a evidência de vereditos que já eram os mesmos.

### Limitações conhecidas

- O validador **não pega ano errado** dentro de um resumo: ano é tratado como data, não como quantidade. Foi assim que o "desde 1986" passou; quem pegou foi uma segunda leitura da própria IA, não uma pessoa (🔧 corrigido em 0.1.1).
- O detector de frequência fundamental (`ferramentas/medir-tom.py`) **não separa vozes** em áudio de televisão comprimido. Ficou no repositório porque avisa quando não serve.
- A voz da retrospectiva de abertura do caso **não foi identificada**, e está declarada como narração em off, sem atribuição a ninguém.
- **Sem revisão humana registrada** em nenhuma checagem. O esquema só a exige quando a confiança é baixa, e nenhuma é — mas a doutrina diz que nada vai ao ar sem uma pessoa ter lido.
