# ESTADO: onde o trabalho parou

**Atualizado em:** 1º/out/2026 (versão 0.4.0, três casos e o braço de debate preparado)

Uma sessão nova consegue continuar lendo **só este arquivo**. Ele diz o que está pronto, o que falta, e o comando exato para retomar. ⛔ Ele não guarda doutrina: isso é [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).

---

## Em uma frase

O pipeline roda de ponta a ponta, localmente ou pelos runners do GitHub ([`docs/NUVEM.md`](docs/NUVEM.md)). **Dois casos principais** estão fechados: o bloco de contas públicas da sabatina de Lula (auditado e corrigido em 26/set) e o **bloco de economia** da sabatina de Flávio Bolsonaro (refeito em 27/set a pedido do autor). O primeiro trecho do Flávio, sobre a tentativa de golpe, fica como registro. A revisão é por IA, em passada adversarial separada ([`skills/revisar-checagem.md`](skills/revisar-checagem.md)): registrada nas 21 checagens do bloco de economia, ainda não nos outros dois casos. O vídeo termina com a fala: sem cartela de encerramento e sem a cartela de divulgação do g1.

🆕 **30/set/2026: o bloco de economia passou a ser checado sobre a íntegra horizontal da sabatina** (44min18s, fornecida pelo autor), no lugar do clipe vertical do g1. As faixas pretas foram cortadas (`--cortar-faixas`), só o bloco (34:02 a 39:40) foi recortado, os cards ficaram opacos e passaram a entrar com fade. **Nenhum veredito mudou**; o que mudou foi o relógio dos tempos, oito correções de transcrição e a citação de `A018`. Tudo em [`CORRECOES.md`](casos/2026-08-28-sabatina-flavio-globo-economia/CORRECOES.md).

🆕 **1º/out/2026: nasceu o braço de DEBATE** ([`docs/DEBATES.md`](docs/DEBATES.md)), preparado **antes** do debate presidencial da TV Globo (21h30 de 1º/out, mediação de César Tralli, quatro candidatos presentes: Flávio Bolsonaro, Ronaldo Caiado, Augusto Cury e Romeu Zema; Lula avisou que não vai). O caso [`2026-10-01-debate-presidencial-globo`](casos/2026-10-01-debate-presidencial-globo/CASO.json) está aberto, **sem mídia**: falta o vídeo (o autor passa), a procedência, a transcrição, os turnos e a checagem. Ferramentas prontas e testadas: `metricas`, `lotes-de-debate`, `derivar-recorte`, `novo-caso-debate`, skills `checar-debate` e `consideracoes-do-debate`, e os **critérios das considerações da IA, registrados antes do evento** (`consideracoes/CRITERIOS.md`). ⚠️ O texto da resolução do TSE sobre IA e o prazo de publicação (§7 do `DEBATES.md`) são **decisão do autor**, não resolvida aqui.

---

## O que está pronto

| Camada | Estado |
|---|---|
| Pipeline (8 passos) | ✅ completo; recorte com `--enquadrar` para vídeo vertical e `--cortar-faixas` para horizontal com barras pretas; tempo de leitura e congelamento final no overlay; 🆕 card opaco e entrada com fade de 8 quadros; `--som-de-entrada` opcional; `ferramentas/migrar-tempos.py` para trocar a mídia de um caso |
| Validador | ✅ travas da 0.2.0: ano, ressalva, intenção, travessão, cobertura, `citacao_card`, arredondamento, capturas, plano; na 0.2.1, aviso para juízo extraído como alegação e para checagem sem revisão registrada |
| Evidência | ✅ captura de fonte com sha256 e conferência de trecho contra a página (`checagens/CAPTURAS.json`) |
| Nuvem | ✅ cinco workflows: preparar mídia, capturar fontes, segunda passada, renderizar, sondar vídeos |
| Testes | ✅ 92 passando, incluindo regressão sobre os três casos reais e os do corte de faixas e da entrada com fade |
| CI | ✅ `.github/workflows/validar.yml`: lint, testes, validador de todos os casos, plano de overlay sem diferença, links |

### Caso 1 · `casos/2026-08-27-sabatina-lula-globo`

| | |
|---|---|
| Peça | Sabatina da TV Globo, 27/ago/2026, 44min33s, 1920x1080 |
| Trecho checado | `bloco-contas-publicas`, 22:32 a 27:24 (4min52s) |
| Alegações | 23 (18 do entrevistado, 5 da entrevistadora) e 1 exclusão declarada |
| Vereditos | 14 verdadeiro · 4 impreciso · 3 falso · 2 não checável (`A017` mudou de verdadeiro para impreciso em 26/set, registrado) |
| Fontes | 56 citações, 38 URLs, 24 instituições; 32 URLs com captura assinada (as demais recusaram o robô, e isso está registrado) |
| Correções | [`CORRECOES.md`](casos/2026-08-27-sabatina-lula-globo/CORRECOES.md), com a auditoria de 26/set e as contestações do vídeo publicado |
| Validador | ✅ 0 erros, 1 aviso (`A016` entra 13,1s depois da fala, por causa do tempo de leitura dos cards anteriores) |
| Vídeo | ⚠️ **precisa ser renderizado de novo** por quem tem o arquivo de origem: o plano mudou (textos corrigidos, tempo de leitura, congelamento final; sem cartela de encerramento desde 27/set). O arquivo de origem não está no repositório nem no rascunho |

### Caso 3 (principal do Flávio) · `casos/2026-08-28-sabatina-flavio-globo-economia`

| | |
|---|---|
| Por que existe | O autor avaliou que o trecho do golpe tinha muito juízo de valor e pouco fato conferível. Uma sondagem de 15 vídeos (`sondagem-rodada-1.json`) achou o segundo trecho oficial do g1: o bloco inteiro de economia, escolhido por tema, como o do Lula |
| Peça | 🔧 **30/set/2026: íntegra horizontal** da sabatina, 44min18s, 1920x886 com faixas pretas laterais, sha256 `a7006047…`, fornecida pelo autor (canal de origem não informado; conferida pelo conteúdo e pela fala, ver `CASO.json`). Antes era o clipe vertical do g1 (`ae35ff24…`, 540x960). O recorte `bloco-economia` vai de 34:02,3 a 39:40,45 e usa `--cortar-faixas` (imagem útil 1568x882, recuada 4 px da borda mole, levada a 1920x1080).
| Transcrição | 98 segmentos (o bloco transcrito de novo na mídia nova, `transcricao-bloco-economia.json`); 8 correções com segunda passada, entre elas `1922` por `2022` e duas do fim do bloco, onde o motor puxou frase da pergunta seguinte; leituras não resolvidas declaradas |
| Falantes | César Tralli, Renata Vasconcellos e Flávio Bolsonaro; 🔧 trocas refeitas em 30/set na íntegra (plano aberto quando um entrevistador fala, close quando Flávio responde) e contra o Poder360; o limite de 35:32 mudou |
| Alegações | 21, só fato (5 dos entrevistadores, 16 do entrevistado); nenhum juízo, promessa ou hipótese |
| Vereditos | 10 verdadeiro · 8 impreciso · 3 sem comprovação (5 mudanças da revisão adversarial por IA de 27/set, registradas em `CORRECOES.md`) |
| Revisão | ✅ `revisao_ia` nas 21 checagens: 16 mantidas, 5 alteradas |
| Fontes | 55 trechos, 53 URLs, todos conferidos contra a página capturada (7 rodadas de captura) |
| Validador | ✅ 0 erros, 2 avisos (A011 e A014 sem fonte N1/N2, e por isso sem comprovação) |
| Vídeo | ✅ 1920x1080, 30 fps, 5min38s, termina com a última fala (sem cartela do g1 nem de encerramento), sem faixa preta, cards opacos com fade; renderizado localmente em 30/set e conferido: 169 quadros sem linha preta na borda, 21 cards sem vídeo por baixo (variação de 0,38 dentro do card contra 10,5 ou mais no vídeo puro), último quadro limpo. Versão leve de 25 MB (crf 32) ao lado. ⚠️ O MP4 de referência no rascunho `nuvem-…` continua o do clipe: o runner não tem a íntegra, e `render/PEDIDO_RENDER.json` (rodada 2) é da mídia antiga |

### Caso 2 (registro) · `casos/2026-08-28-sabatina-flavio-globo`

| | |
|---|---|
| Peça | ⚠️ **trecho oficial publicado pelo g1** (Facebook), 2min44s, vertical 720x1280, sha256 `f09911b7…`. O vídeo pedido (YouTube `o0W3MnZTqyA`) não pôde ser baixado; a íntegra do Globoplay não toca fora do Brasil. Ver `CASO.json`, procedência |
| Transcrição | `whisper.cpp` `large-v3-turbo` no runner; 43 segmentos; correções registradas; segunda passada feita |
| Falantes | César Tralli (pergunta) e Flávio Bolsonaro (resposta); diverge do Poder360, que atribui a pergunta a Renata Vasconcellos ([`NOTA_DE_ATRIBUICAO.md`](casos/2026-08-28-sabatina-flavio-globo/transcricao/NOTA_DE_ATRIBUICAO.md)) |
| Alegações | 19 (15 do entrevistado, 4 do entrevistador), cobertura do trecho inteiro, extraídas antes de qualquer busca |
| Vereditos | 12 verdadeiro · 1 impreciso · 1 sem comprovação · 2 falso · 3 não checável |
| Fontes | 48 citações, 33 URLs, 16 instituições; 33 de 33 com captura assinada; 48 de 48 trechos encontrados na página capturada |
| Validador | ✅ 0 erros; avisos para os três juízos extraídos (`A004` a `A006`, registrados em `CORRECOES.md`) e para a revisão ainda não registrada |
| Vídeo | recorte refeito até 02:38,9, antes da cartela do g1, e plano sem encerramento. Pedido de render no runner em `render/PEDIDO_RENDER.json` (rodada 2); até ele rodar, o MP4 do rascunho `nuvem-2026-08-28-sabatina-flavio-globo` (62,8 MB) é o anterior, com as duas cartelas |

---

## ⬜ O que falta, em ordem de valor

1. 🔴 **Revisão adversarial por IA do caso Lula e do trecho do golpe** ([`skills/revisar-checagem.md`](skills/revisar-checagem.md)), registrada com `python ferramentas/registrar-revisao.py <slug> --recorte <id> --ia --notas revisao.json`. Mudança de veredito vai para `CORRECOES.md`. Prioridade: Lula `A007` e `A017`; golpe `A009`, `A013`, `A017`, `A018`.
2. **Renderizar de novo o vídeo do caso Lula** (quem tem `fonte/sabatina-lula-globo-2026-08-27.mp4`):
   ```bash
   python -m checagem midia 2026-08-27-sabatina-lula-globo recortar bloco-contas-publicas --inicio 1352.32 --duracao 292 --motivo "o mesmo de RECORTES.json"   # se o recorte não existir
   python -m checagem overlay    2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   python -m checagem renderizar 2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   python -m checagem validar    2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   ```
   Confira os parâmetros exatos do recorte em `recortes/RECORTES.json` antes de rodar.
3. **Checar o resto da íntegra da sabatina de Flávio.** 🔧 O arquivo existe desde 30/set (dentro do caso `2026-08-28-sabatina-flavio-globo-economia/fonte/`, fora do git; o `MIDIA.json` traz o sha256). Falta transcrever a peça toda (`python -m checagem transcrever <slug>`, uns 30 min de CPU), extrair e checar o que está fora do bloco de economia, com slug ou recorte novo. Uma checagem publicada da entrevista inteira (Aos Fatos) já existe e contamina a extração: declare-a.
   **Antes de publicar o vídeo de economia, decisões e conferências que são do autor** (⬜ não são pendência de andamento, são o que a IA não pode fechar):
   - ouvir `35:12` a `35:17` e confirmar **`outubro de 2022`** (o motor escreve 1922 em sete de oito decodificações e 2022 só na passada longa com prompt; a correção se apoia em referência e contexto, não no áudio);
   - decidir o **som de entrada** dos cards: o padrão V32 do editor de longos pede som, mas o PASSO 7 copia o áudio sem reencodar. O `--som-de-entrada` existe e está desligado (`docs/ARQUITETURA.md` §5);
   - `A021`: a nota do BC de 31/08 traz a tabela de elasticidades como imagem e ninguém leu o número novo.
4. **Checar os outros 40 minutos da peça de Lula.** Transcrição e falantes da peça inteira já existem: comece no PASSO 4.
5. **Os outros quatro candidatos da série.**
6. 🆕 **O debate da Globo, quando o vídeo chegar:** siga [`skills/checar-debate.md`](skills/checar-debate.md) (comandos em `docs/DEBATES.md` §2). Antes de rodar o PASSO 0, o autor entrega o arquivo e diz de onde veio.

---

## ⚠️ Limitações conhecidas, e onde estão escritas

| Limitação | Onde |
|---|---|
| O caso Flávio do golpe (registro) é um **trecho escolhido pelo veículo**, não a íntegra; o de economia usa a íntegra fornecida pelo autor, com **origem de download não informada** | `CASO.json` de cada caso, procedência |
| A íntegra tem 44min18s e o Globoplay lista cerca de 1 h; a diferença não foi esclarecida | `CASO.json` do caso de economia |
| A transcrição do bloco de economia tem três pontos sem decisão: o verbo de `A018` (a citação usa `[...]`), a fala "Meio trilhão de reais..." (0,6 s) e uma interjeição de Renata em 37:29 que o motor principal não escreveu | `CORRECOES.md` e `NOTA_DE_ATRIBUICAO.md` §3 do caso |
| O ambiente de trabalho **não alcança o YouTube**, e o runner é recusado por ele | `fonte/origem-download.json` do caso Flávio; `docs/NUVEM.md` |
| O proxy da sessão **não deixa enviar binário** à API do GitHub | `docs/NUVEM.md` §7.1 |
| O detector de tom **não separa vozes** em áudio de TV comprimido | nota de atribuição do caso Lula, §4 |
| O validador cobra ano e número por **aviso**, não por erro: aviso tem que ser lido | `docs/METODOLOGIA.md` §3.1 |
| Portais que recusam robô (IBGE, portal do STF) ficam sem captura assinada, e isso é registrado | `checagens/CAPTURAS.json` de cada caso |
| A checagem do G20 usa o conceito de governo geral do FMI | caso Lula, `A007` |
| 🆕 **17 dos 23 cards** ficam na tela menos que o tempo de ler resumo e ressalva (17 caracteres por segundo); registrado como medida, sem mudança no pipeline | `docs/IDENTIDADE_VISUAL.md` §7.1 |

---

## 🧾 O que quebrou nesta primeira rodada, e não pode voltar

Cada linha aqui é um defeito que aconteceu de verdade. Estão listados porque a próxima sessão não deve gastar tempo redescobrindo.

| Sintoma | Causa | Conserto, já aplicado |
|---|---|---|
| Cartela com duração **negativa** | duas alegações saem da **mesma frase**, e a janela era cortada no começo da seguinte | as cartelas entram em **fila**: `_janelas()` em `passo6_overlay.py` |
| `ValueError: b'Regular' is not in list` | o arquivo itálico da Inter chama a instância de `Italic`, não `Regular` | tradução do nome do peso em `tipografia.fonte()` |
| `Unrecognized option 'filter_complex_script'` | a opção **foi removida no ffmpeg 8**; a máquina tem a 9 | `_opcao_de_script()` escolhe `-/filter_complex` conforme a versão |
| "SEM COMPROVAÇÃO" escrevendo **por cima** da descrição, na legenda | coluna de rótulo fixa em 300px | a coluna é medida na própria fonte |
| Ressalva **cortada no meio da frase** | cabia em uma linha só | duas linhas |
| Card dizendo "FONTES: IBGE" com **dois** documentos do IBGE | instituições repetidas colapsavam em um nome | o card mostra a contagem de documentos |
| O selo "CHECAGEM ABERTA" **sumia nos intervalos** | ele era desenhado dentro da cartela | virou camada própria, sobreposta o vídeo inteiro |
| Linha de fontes **estourando a caixa** em 92px | os nomes eram concatenados sem medir; "US Department of the Treasury / Federal Reserve Bank of St. Louis" mais um segundo nome dava 1802px numa caixa de 1710px | a linha é construída **medindo em pixels**, e o que não cabe vira "(+N)" |
| Medição de áudio voltando **vazia sem erro** | `volumedetect` escreve em nível informativo, e o comando rodava com `-v error` | `_nivel_de_audio()` roda com `-v info` |
| Resumo afirmando "a maior taxa desde **1986**" sem fonte | escrito de memória; o validador trata ano como data e não pegou | corrigido e registrado em `casos/.../CORRECOES.md` |
| Duas fontes com a **mesma URL** contadas como duas | dois pedaços da mesma base | juntadas num trecho só; o validador reprova a duplicata |
| CI vermelha desde o primeiro commit | num clone limpo as cartelas (derivadas, fora do git) não existem, e o validador reprovava | cartela ausente numa cópia sem a pasta vira nota; pasta incompleta segue reprovando |
| Trecho "de fonte" que não estava na página | trechos reescritos ou truncados, e uma URL que não existia (caso Lula) | captura com sha256 e `ferramentas/conferir-trechos.py`, que confere cada trecho contra a página |
| "o PIB" casando dentro de "brutO PIB" | a comparação de citação e de trecho era de substring | palavra inteira, no validador e na conferência de trechos |
| Card de `FALSO` com 3s na tela | piso fixo de 3s e cinco alegações em 20s no fim do trecho do caso Flávio | tempo de leitura por card e congelamento final declarado no plano |
| Borda preta de 3 a 4 colunas no quadro final, mesmo com o corte certo | a borda entre a faixa e a imagem é mole: a compressão espalha cinza (coluna 172 tem luma 33) | `--cortar-faixas` recua 4 px para dentro da borda medida |
| Deslocamento entre duas mídias medido com dispersão de 0,78 s | o **começo** de cada segmento do motor varia entre passadas sobre o mesmo áudio; o **fim** não (±0,04 s) | `ferramentas/migrar-tempos.py` mede pelo fim |
| "outubro de **1922**" na transcrição nova | erro recorrente do motor no áudio de outra codificação (sete de oito decodificações) onde o clipe acertava | correção por script, com a conferência no áudio marcada como pendente |
| Fala de entrevistador dentro do último turno de Flávio | o motor escreveu "Então, quero ouvir o senhor, candidato", frase da **pergunta seguinte**, que fica depois do corte | nove decodificações concordam contra ela; corrigido por script |
| Quina reta no canto esquerdo do card | o corpo escuro era um retângulo sobre a faixa colorida | corpo arredondado só à direita (`corners` do Pillow) |
| Upload do vídeo final recusado | o proxy da sessão só aceita corpo JSON na API do GitHub | o runner renderiza a partir do que está versionado (`nuvem-renderizar`) |

---

## Como retomar, em três comandos

```bash
cd checagem-eleicoes-2026
python -m pytest -q                       # 92 testes
python ferramentas/conferir-links.py      # nenhum link quebrado
python ferramentas/validar-todos.py       # os três casos, 0 erros
```

Se os três passarem, o repositório está no estado descrito aqui. Se algum falhar, **conserte antes de escrever qualquer coisa nova**: seguir em frente com a porta reprovando é como o projeto perde a única coisa que ele tem, que é ser conferível.
