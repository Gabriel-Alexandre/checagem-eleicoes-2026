# ESTADO: onde o trabalho parou

**Atualizado em:** 17/out/2026 (versão 0.5.1; a sabatina de Flávio Bolsonaro do 2º turno em andamento, ver "Caso em andamento")

Uma sessão nova consegue continuar lendo **só este arquivo**. Ele diz o que está pronto, o que falta, e o comando exato para retomar. ⛔ Ele não guarda doutrina: isso é [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).

---

## Em uma frase

O pipeline roda de ponta a ponta, localmente ou pelos runners do GitHub ([`docs/NUVEM.md`](docs/NUVEM.md)). **Dois casos principais** estão fechados: o bloco de contas públicas da sabatina de Lula (auditado e corrigido em 26/set) e o **bloco de economia** da sabatina de Flávio Bolsonaro (refeito em 27/set a pedido do autor). O primeiro trecho do Flávio, sobre a tentativa de golpe, fica como registro. A revisão é por IA, em passada adversarial separada ([`skills/revisar-checagem.md`](skills/revisar-checagem.md)): registrada nas 21 checagens do bloco de economia, ainda não nos outros dois casos. O vídeo termina com a fala: sem cartela de encerramento e sem a cartela de divulgação do g1.

🆕 **30/set/2026: o bloco de economia passou a ser checado sobre a íntegra horizontal da sabatina** (44min18s, fornecida pelo autor), no lugar do clipe vertical do g1. As faixas pretas foram cortadas (`--cortar-faixas`), só o bloco (34:02 a 39:40) foi recortado, os cards ficaram opacos e passaram a entrar com fade. **Nenhum veredito mudou**; o que mudou foi o relógio dos tempos, oito correções de transcrição e a citação de `A018`. Tudo em [`CORRECOES.md`](casos/2026-08-28-sabatina-flavio-globo-economia/CORRECOES.md).

🆕 **1º/out/2026: nasceu o braço de DEBATE** ([`docs/DEBATES.md`](docs/DEBATES.md)), preparado **antes** do debate presidencial da TV Globo (21h30 de 1º/out, mediação de César Tralli, quatro candidatos presentes: Flávio Bolsonaro, Ronaldo Caiado, Augusto Cury e Romeu Zema; Lula avisou que não vai). O caso [`2026-10-01-debate-presidencial-globo`](casos/2026-10-01-debate-presidencial-globo/CASO.json) está aberto, **sem mídia**: falta o vídeo (o autor passa), a procedência, a transcrição, os turnos e a checagem. Ferramentas prontas e testadas: `metricas`, `lotes-de-debate`, `derivar-recorte`, `novo-caso-debate`, skills `checar-debate` e `consideracoes-do-debate`, e os **critérios das considerações da IA, registrados antes do evento** (`consideracoes/CRITERIOS.md`). ⚠️ O texto da resolução do TSE sobre IA e o prazo de publicação (§7 do `DEBATES.md`) são **decisão do autor**, não resolvida aqui.

🆕 **15/out/2026: a sabatina INTEIRA, com cortes curtos** ([`docs/PECA_INTEIRA.md`](docs/PECA_INTEIRA.md)), preparada **antes** da sabatina de Lula na TV Globo do 2º turno (21h15 de 15/out, logo após o Jornal Nacional, 45 min, Renata Lo Prete; Flávio Bolsonaro no dia seguinte). O caso [`2026-10-15-sabatina-lula-globo-2turno`](casos/2026-10-15-sabatina-lula-globo-2turno/CASO.json) está aberto **sem mídia**, com o critério dos cortes ([`recortes/SELECAO_DE_CORTES.md`](casos/2026-10-15-sabatina-lula-globo-2turno/recortes/SELECAO_DE_CORTES.md)) e o das considerações da IA ([`consideracoes/CRITERIOS.md`](casos/2026-10-15-sabatina-lula-globo-2turno/consideracoes/CRITERIOS.md)) registrados às 10h. Ferramentas novas, testadas e ensaiadas sobre a íntegra de 27/ago (o ensaio não entrou no git): `sugerir-cortes.py`, `rascunho-de-turnos.py`, limites de corte curto no `derivar-recorte.py` e relatório da peça inteira. **Para retomar:** o autor entrega a gravação e diz de onde veio; siga a skill [`checar-sabatina-completa`](skills/checar-sabatina-completa.md) do passo 0 ao 16.

🆕 **17/out/2026: a sabatina INTEIRA de Flávio Bolsonaro no 2º turno** (TV Globo, 16/out, Renata Lo Prete), caso [`2026-10-16-sabatina-flavio-globo-2turno`](casos/2026-10-16-sabatina-flavio-globo-2turno/CASO.json), com o mesmo passo a passo, a mesma régua e os mesmos critérios do caso de Lula de 15/out (que é o modelo). Ver a seção **"Caso em andamento"** logo abaixo: ela diz em que etapa está e o comando para retomar.

---

## 🔄 Caso em andamento: `2026-10-16-sabatina-flavio-globo-2turno`

**Pedido do autor (17/out):** o mesmo que foi feito com a sabatina de Lula (`2026-10-15-sabatina-lula-globo-2turno`), do começo ao fim, uma etapa por vez, com commit e push nos dois repositórios ao fim de cada uma; ⛔ merge no `main` é dele. A gravação mora em `C:/Users/Gabriel/Videos/youtube/video-longo/video-11/gravacao-sabatina/sabatina-flavio-globo-2026-10-16.mp4` (movida de Downloads, sha256 `cffad1d8…`), ligada por hardlink em `fonte/`. Os cortes saem em `video-11/cortes-checados/`. Critérios copiados sem mudança do caso de 15/out (`ORIGEM_DOS_CRITERIOS.md` do caso).

| Etapa | O que é | Estado |
|---|---|---|
| E0 | preparo: gravação movida e ligada, branch atualizado, testes verdes, caso aberto, critérios copiados | ✅ 17/out |
| E1 | mídia e procedência: sinal da Globo em tela cheia (não é retransmissão, sem moldura nem terceiro), 42min48s contra 40 min anunciados no ar, `inicio_da_entrevista_s` = 0,0, tarja em 0:13, o intervalo comercial tirado na origem (o cronômetro da emissora prova que nada da entrevista saiu), o fim corta a despedida da apresentadora; caixa dos cortes por `--cortar-faixas` | ✅ 17/out |
| E2 | transcrição sem prompt (1.865 segmentos, 8.323 palavras), 22 correções por script com três leituras alternativas (todos os números iguais; o que não se resolveu, listado), 91 turnos à mão conferidos nos quadros; tempo de fala: Flávio Bolsonaro 25:00 (63,9%), Renata Lo Prete 14:09 (36,1%) | ✅ 17/out |
| E3 | 15 blocos; extração em 5 lotes de internet fechada, juntada sem buraco (0:00,9 a 42:47,5): **207 alegações** (Renata Lo Prete 83, Flávio Bolsonaro 124); duas falas de conversa privada movidas para exclusões pela régua do caso de 15/out; tempo de cada alegação palavra por palavra (`medir-tempo-das-alegacoes.py`, nova, com teste: 200 ajustadas, mediana 0,06 s, máx. 24,7 s); 6 cortes sugeridos (85,1 s) e bordas na pausa da voz (`bordas-na-pausa.py`, nova, com teste: todas 12,8 dB ou mais abaixo da fala); **commitado antes do 1º veredito** | ✅ 17/out |
| E4 | checagem em ondas (limite de 200 buscas por turno, somadas), capturas, trechos | ⬜ |
| E5 | revisão adversarial por lote, coerência entre lotes, coerência cruzada com os casos de Lula (15/out) e de Flávio (28/ago), "a frase que voltou", rodada 2 dos provisórios | ⬜ |
| E6 | métricas, relatório, cortes renderizados e validados, entrega com `LEIA-ME.md` | ⬜ |
| E7 | considerações da IA (duas passadas e o documento final) | ⬜ |
| E8 | auditoria final por amostra, por agente que não participou | ⬜ |
| E9 | validação final extensiva (os 10 itens do pedido), `CORRECOES.md` §5 | ⬜ |
| E10 | roteiro final e publicação, no repositório do canal | ⬜ |
| E11 | revalidação do roteiro e propagação nos dois repositórios | ⬜ |

**E4 em ondas (17/out):** 21 pedidos de 10 alegações (`lotes/checagem/`), três ondas de 7 agentes (01 a 07, 08 a 14, 15 a 21), cada agente com no máximo 7 buscas web; instruções comuns em `C:/Users/Gabriel/AppData/Local/Temp/claude/v11/prompt-checagem.txt` (fora do repositório; o essencial está na skill `checar-alegacao` e no `CORRECOES.md` do caso de 15/out). Capturas de cada pedido em `capturas/2026-10-16-sabatina-flavio-globo-2turno-pNN`. Junção: `python ferramentas/lotes-de-debate.py checagem-juntar 2026-10-16-sabatina-flavio-globo-2turno --recorte sabatina-completa`; conferência: `python ferramentas/conferir-trechos.py 2026-10-16-sabatina-flavio-globo-2turno --recorte sabatina-completa --capturas capturas/2026-10-16-sabatina-flavio-globo-2turno-*` mais as pastas de 15/out que foram reaproveitadas.

**Contagem de buscas web do turno de 17/out (limite 200, somadas entre todos os agentes):** 2 na E0/E1 (data e duração) · onda 1 (pedidos 01 a 07): 47 → 49 no total; 6 provisórios com o marcador (A008, A009, A010, A020, A023, A062) · onda 2 (pedidos 08 a 14): 46 → 95 no total; 4 provisórios com o marcador (A071, A072, A086, A113) · onda 3 (pedidos 15 a 21): 49 → 144 · revisores r1 a r5: 9 → 153 · r6 e r7: 2 → 155 · rodada 2 (quatro partes, 27 provisórios refeitos): 37 → 192 · revisão da rodada 2: até 1 · passada de coerência: até 2. 🔴 **Ficaram provisórias, com o marcador, por falta de busca no turno: A113 ("26 das 27" superintendências trocadas) e A161 ("recordista em empresas fechadas", no corte-04).** A auditoria final (E8) também precisa de busca. As duas e a auditoria ficam para o turno seguinte.

**Para retomar:** leia a linha da primeira etapa ⬜ acima e a skill [`checar-sabatina-completa`](skills/checar-sabatina-completa.md); o modelo de cada artefato está no caso de 15/out (`CORRECOES.md` §1 a §5 traz as lições). Ambiente: `export PATH="$HOME/scoop/shims:$PATH" PYTHONIOENCODING=utf-8 PYTHONUTF8=1`.

---

## O que está pronto

| Camada | Estado |
|---|---|
| Pipeline (8 passos) | ✅ completo; recorte com `--enquadrar` para vídeo vertical e `--cortar-faixas` para horizontal com barras pretas; tempo de leitura e congelamento final no overlay; 🆕 card opaco e entrada com fade de 8 quadros; `--som-de-entrada` opcional; `ferramentas/migrar-tempos.py` para trocar a mídia de um caso |
| Validador | ✅ travas da 0.2.0: ano, ressalva, intenção, travessão, cobertura, `citacao_card`, arredondamento, capturas, plano; na 0.2.1, aviso para juízo extraído como alegação e para checagem sem revisão registrada |
| Evidência | ✅ captura de fonte com sha256 e conferência de trecho contra a página (`checagens/CAPTURAS.json`) |
| Nuvem | ✅ cinco workflows: preparar mídia, capturar fontes, segunda passada, renderizar, sondar vídeos |
| Testes | ✅ 123 passando, incluindo regressão sobre os três casos reais, o braço de debate e o da sabatina inteira (cortes curtos, sugestão sem veredito, relatório da peça) |
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

0. ✅ **A sabatina de Lula do 2º turno (15/out): checada inteira em 16/out** (CHANGELOG 0.5.1). 193 alegações, 128 V · 31 I · 31 S · 3 F, revisão por IA em todas, uma auditoria final por amostra (44 checagens, 4 vereditos corrigidos) e uma validação final (A033 corrigida, o minuto dos cards contado do início da entrevista, bordas dos cortes na pausa da voz, tempo de cada alegação medido por palavra; `CORRECOES.md` §5), validador 0 erros, métricas, `RELATORIO_SABATINA_COMPLETA.md`, 6 cortes renderizados em `Videos/youtube/video-longo/video-9/cortes-checados/` (com `LEIA-ME.md`) e as considerações em `consideracoes/`. ⬜ **Decisões que são dele, não da IA:** quais cortes entram e em que ordem; o que fazer com o quadro congelado no fim de cada corte (10 a 39 s); se as considerações entram no vídeo e de que forma; o merge do branch no `main` (os links da descrição dependem dele).
   ⚠️ `registrar-revisao.py` escreve no arquivo JUNTADO: se rodar `checagem-juntar` de novo, registre a revisão de novo com `checagens/revisao/revisao.json`.
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
| 🆕 O **tom de voz não separa Lula** de uma entrevistadora (192 Hz contra 188 Hz de mediana, medido em 15/out); o rascunho de turnos usa o enquadramento, e erra mais na fala de jornalista em plano aberto (71% certa) | `docs/PECA_INTEIRA.md` §4 |
| 🆕 Corte curto com várias cartelas congela o último quadro (14 s de trecho viraram 34 s de arquivo no ensaio) | `docs/PECA_INTEIRA.md` §2 |
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
python -m pytest -q                       # 200 testes
python ferramentas/conferir-links.py      # nenhum link quebrado
python ferramentas/validar-todos.py       # os três casos, 0 erros
```

Se os três passarem, o repositório está no estado descrito aqui. Se algum falhar, **conserte antes de escrever qualquer coisa nova**: seguir em frente com a porta reprovando é como o projeto perde a única coisa que ele tem, que é ser conferível.
