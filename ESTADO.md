# ESTADO: onde o trabalho parou

**Atualizado em:** 27/set/2026 (versão 0.2.0, dois casos)

Uma sessão nova consegue continuar lendo **só este arquivo**. Ele diz o que está pronto, o que falta, e o comando exato para retomar. ⛔ Ele não guarda doutrina: isso é [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).

---

## Em uma frase

O pipeline roda de ponta a ponta, localmente ou pelos runners do GitHub ([`docs/NUVEM.md`](docs/NUVEM.md)). **Dois casos** estão fechados para revisão humana: o bloco de contas públicas da sabatina de Lula (auditado e corrigido em 26/set) e o trecho oficial do g1 da sabatina de Flávio Bolsonaro. Nenhum dos dois tem revisão humana registrada.

---

## O que está pronto

| Camada | Estado |
|---|---|
| Pipeline (8 passos) | ✅ completo; recorte com `--enquadrar` para vídeo vertical; tempo de leitura e congelamento final no overlay |
| Validador | ✅ travas da 0.2.0: ano, ressalva, intenção, travessão, cobertura, `citacao_card`, arredondamento, capturas, plano |
| Evidência | ✅ captura de fonte com sha256 e conferência de trecho contra a página (`checagens/CAPTURAS.json`) |
| Nuvem | ✅ quatro workflows: preparar mídia, capturar fontes, segunda passada, renderizar |
| Testes | ✅ 72 passando, incluindo regressão sobre os dois casos reais |
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
| Vídeo | ⚠️ **precisa ser renderizado de novo** por quem tem o arquivo de origem: o plano mudou (textos corrigidos, encerramento, tempo de leitura, 2s de congelamento final). O arquivo de origem não está no repositório nem no rascunho |

### Caso 2 · `casos/2026-08-28-sabatina-flavio-globo`

| | |
|---|---|
| Peça | ⚠️ **trecho oficial publicado pelo g1** (Facebook), 2min44s, vertical 720x1280, sha256 `f09911b7…`. O vídeo pedido (YouTube `o0W3MnZTqyA`) não pôde ser baixado; a íntegra do Globoplay não toca fora do Brasil. Ver `CASO.json`, procedência |
| Transcrição | `whisper.cpp` `large-v3-turbo` no runner; 43 segmentos; correções registradas; segunda passada feita |
| Falantes | César Tralli (pergunta) e Flávio Bolsonaro (resposta); diverge do Poder360, que atribui a pergunta a Renata Vasconcellos ([`NOTA_DE_ATRIBUICAO.md`](casos/2026-08-28-sabatina-flavio-globo/transcricao/NOTA_DE_ATRIBUICAO.md)) |
| Alegações | 19 (15 do entrevistado, 4 do entrevistador), cobertura do trecho inteiro, extraídas antes de qualquer busca |
| Vereditos | 12 verdadeiro · 1 impreciso · 1 sem comprovação · 2 falso · 3 não checável |
| Fontes | 48 citações, 33 URLs, 16 instituições; 33 de 33 com captura assinada; 48 de 48 trechos encontrados na página capturada |
| Validador | ✅ 0 erros, 0 avisos |
| Vídeo | ✅ 1920x1080, 3min12s (2min44s do trecho, 19,7s de congelamento de leitura, 8s de encerramento), renderizado e conferido quadro a quadro na sessão de 27/set. O MP4 de referência foi renderizado de novo pelo workflow `nuvem-renderizar` em 27/set (plano idêntico ao versionado, porta em 0 erros e 0 avisos) e está no release em rascunho `nuvem-2026-08-28-sabatina-flavio-globo`: 62,8 MB, sha256 `32ec046350bfcb35dbf0904219751e907bb4fa278c3dda0088db1bc044aed3c4` |

---

## ⬜ O que falta, em ordem de valor

1. 🔴 **Revisão humana dos dois casos.** Nenhuma checagem tem `revisao_humana`. Prioridade: Flávio `A009`, `A013`, `A017`, `A018` e a atribuição da pergunta; Lula `A007` e `A017`. Registrar com `python ferramentas/registrar-revisao.py`.
2. **Renderizar de novo o vídeo do caso Lula** (quem tem `fonte/sabatina-lula-globo-2026-08-27.mp4`):
   ```bash
   python -m checagem midia 2026-08-27-sabatina-lula-globo recortar bloco-contas-publicas --inicio 1352.32 --duracao 292 --motivo "o mesmo de RECORTES.json"   # se o recorte não existir
   python -m checagem overlay    2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   python -m checagem renderizar 2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   python -m checagem validar    2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
   ```
   Confira os parâmetros exatos do recorte em `recortes/RECORTES.json` antes de rodar.
3. **Checar a íntegra da sabatina de Flávio.** Precisa do arquivo: coloque-o em `casos/2026-08-28-sabatina-flavio-globo/fonte/` a partir de uma rede no Brasil (Globoplay) ou libere o YouTube na política de rede do ambiente, e comece no PASSO 1 com um slug novo ou um recorte novo. Uma checagem publicada da entrevista inteira (Aos Fatos) já existe e contamina a extração: declare-a, como foi feito aqui.
4. **Checar os outros 40 minutos da peça de Lula.** Transcrição e falantes da peça inteira já existem: comece no PASSO 4.
5. **Os outros quatro candidatos da série.**

---

## ⚠️ Limitações conhecidas, e onde estão escritas

| Limitação | Onde |
|---|---|
| O caso Flávio é um **trecho escolhido pelo veículo**, não a íntegra | `CASO.json`, procedência; topo do relatório |
| O ambiente de trabalho **não alcança o YouTube**, e o runner é recusado por ele | `fonte/origem-download.json` do caso Flávio; `docs/NUVEM.md` |
| O proxy da sessão **não deixa enviar binário** à API do GitHub | `docs/NUVEM.md` §7.1 |
| O detector de tom **não separa vozes** em áudio de TV comprimido | nota de atribuição do caso Lula, §4 |
| O validador cobra ano e número por **aviso**, não por erro: aviso tem que ser lido | `docs/METODOLOGIA.md` §3.1 |
| Portais que recusam robô (IBGE, portal do STF) ficam sem captura assinada, e isso é registrado | `checagens/CAPTURAS.json` de cada caso |
| A checagem do G20 usa o conceito de governo geral do FMI | caso Lula, `A007` |

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
| Upload do vídeo final recusado | o proxy da sessão só aceita corpo JSON na API do GitHub | o runner renderiza a partir do que está versionado (`nuvem-renderizar`) |

---

## Como retomar, em três comandos

```bash
cd checagem-eleicoes-2026
python -m pytest -q                       # 72 testes
python ferramentas/conferir-links.py      # nenhum link quebrado
python ferramentas/validar-todos.py       # os dois casos, 0 erros
```

Se os três passarem, o repositório está no estado descrito aqui. Se algum falhar, **conserte antes de escrever qualquer coisa nova**: seguir em frente com a porta reprovando é como o projeto perde a única coisa que ele tem, que é ser conferível.
