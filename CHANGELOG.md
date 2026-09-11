# Histórico

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).
Versionamento [semântico](https://semver.org/lang/pt-BR/).

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
