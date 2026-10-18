# Histórico

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).
Versionamento [semântico](https://semver.org/lang/pt-BR/).

---

## [0.5.3] · 18/out/2026

**Auditoria de coerência** do caso `2026-10-16-sabatina-flavio-globo-2turno`, em passada separada, com três regras tiradas da METODOLOGIA (§2.2 e §4.2) e dos precedentes do caso de 15/out, aplicadas à lista inteira dos dois lados da mesa (`CORRECOES.md` §6 do caso).

### Corrigido
- **Três frases de hipérbole e figura de linguagem saíram da lista** (A167, A183, A184, do bloco de armas), pela mesma régua que, no caso de 15/out, excluiu *"porque não tinha dinheiro para nada"*. Não há mais `NAO_CHECAVEL` na contagem.
- **Três `FALSO` passaram a `IMPRECISO`:** A069 (o dever do Senado de processar a denúncia tem base no art. 44 da Lei 1.079; a abertura do impeachment não é obrigatória), A182 (o porte é proibido como regra, art. 6º; a defesa com arma em casa é permitida) e A123 (na leitura de arma de fogo, que o contexto sustenta, nenhuma foi apreendida com os manifestantes; o absoluto segue errado). Precedente: a A050 do caso de 15/out.
- **Quatro `FALSO` mantidos**, com o melhor argumento contra cada um registrado: A024, A100, A103 e A165. As três `FALSO` do caso de 15/out foram relidas pelas mesmas regras e nenhuma muda.
- **A009 do caso `2026-08-28-sabatina-flavio-globo`** (a mesma frase da A123, revisão que estava pendente) passou de `FALSO` a `IMPRECISO`; plano de overlay refeito.
- Resultado do caso de 16/out: **204 afirmações, 131 verdadeiro, 29 impreciso, 40 sem comprovação, 4 falso** (Flávio Bolsonaro 66 · 26 · 25 · 4, em 121; Renata Lo Prete 65 · 3 · 15 · 0, em 83, sem mudança). Nenhum dos seis cortes muda. Métricas, relatório e considerações da IA refeitos.

## [0.5.2] · 17/out/2026

A sabatina de Flávio Bolsonaro na TV Globo do 2º turno (16/out, Renata Lo Prete), **checada inteira** com o mesmo passo a passo, a mesma régua e os mesmos critérios do caso de Lula de 15/out.

### O caso `2026-10-16-sabatina-flavio-globo-2turno`
- **Procedência:** o sinal da TV Globo em tela cheia, sem moldura nem terceiro; 42min48s contra 40 min anunciados no ar; o intervalo comercial foi tirado na origem (o cronômetro da emissora marca 31:37 antes e depois da emenda); `inicio_da_entrevista_s` = 0,0. A gravação foi movida para `Videos/youtube/video-longo/video-11/gravacao-sabatina/` e ligada por hardlink em `fonte/`.
- **Transcrição** sem prompt, com 22 correções conferidas em leituras alternativas; **91 turnos à mão**, conferidos nos quadros (Flávio Bolsonaro 25:00 de fala, Renata Lo Prete 14:09).
- **207 alegações** (Renata Lo Prete 83, Flávio Bolsonaro 124) em 5 lotes de internet fechada; a sugestão dos 6 cortes foi commitada às 12h43 de 17/out (`b5b1b59`), antes do primeiro veredito. Critérios copiados sem mudança (`37cdb3f`, `5812ef4`).
- **Checagem em ondas** dentro do limite de 200 buscas web por turno (três ondas de 7 agentes, até 7 buscas cada; rodadas 2 e 3 para os provisórios), revisão adversarial por lote, coerência com os casos de 15/out e 28/ago, **auditoria final por amostra** (51 checagens, 7 vereditos mudados) e **validação final** (nenhum veredito mudou). Resultado: **131 verdadeiro, 26 impreciso, 40 sem comprovação, 9 falso, 1 não checável**. Tudo o que mudou em `CORRECOES.md` §1 a §5.
- **6 cortes curtos** (87,6 s de emissora), bordas na pausa da voz, sincronia 0,0 ms, entregues em `Videos/youtube/video-longo/video-11/cortes-checados/`.
- **Considerações da IA**: duas passadas (com nomes e espelho), percepção pública atribuída e o documento final.

### Adicionado
- **`ferramentas/medir-tempo-das-alegacoes.py`**: o começo e o fim de cada alegação medidos palavra por palavra numa segunda transcrição em fila, aceitos só dentro da frase de origem, com a ordem dos ids acertada.
- **`ferramentas/bordas-na-pausa.py`**: leva a borda de cada corte para a pausa da voz (12 dB ou mais abaixo da fala, janelas de 40 ms) sem cortar alegação; `--conferir` transcreve a janela final; `--so-medir` mede o corte pronto.
- `tests/test_tempo_e_bordas.py` (18 testes).

### Corrigido
- `bordas-na-pausa.py --so-medir` media as bordas da sugestão, não as do corte entregue: agora lê `recortes/RECORTES.json` (`bordas_entregues`). Teste novo.

## [0.5.1] · 16/out/2026

A sabatina de Lula na TV Globo do 2º turno, **checada inteira** com a gravação que o autor entregou às 23h48 de 15/out.

### O caso `2026-10-15-sabatina-lula-globo-2turno`
- **Procedência:** captura de uma retransmissão (o sinal da GloboNews numa moldura vermelha, numa janela do projetor do OBS), com a fala de um terceiro no intervalo e depois do fim declarada como `Fora da sabatina` (papel `outro`) e fora de tudo. A entrevista é íntegra: de 0:50 a 45:55, com intervalo de 28:48 a 31:25 (00:42:32 de entrevista, 7359 palavras).
- **Transcrição** com 14 correções conferidas em passadas isoladas; **turnos escritos à mão** pela IA, conferidos nos quadros (Lula 00:23:49 de fala, Renata Lo Prete 00:14:12).
- **193 alegações** (Renata Lo Prete 74, Lula 119) extraídas em 6 lotes de internet fechada; a sugestão dos 6 cortes foi commitada às 00h44 (`d262c9b`), antes do primeiro veredito.
- **Checagem:** 128 verdadeiro, 31 impreciso, 31 sem comprovação, 3 falso. Revisão adversarial por IA nas 193 (8 revisores por lote, uma passada de coerência entre lotes e a revisão da rodada 2), com tudo o que mudou em `CORRECOES.md`. ⚠️ A primeira rodada esgotou o limite de buscas web: 34 vereditos saíram provisórios e foram refeitos numa rodada 2 com busca, revisada por outro agente. Depois, uma **auditoria final por amostra** (44 checagens sorteadas mais todas as dos cortes, por um agente que não tinha participado) achou 5 problemas: 4 vereditos mudaram (A039, A149, A155, A180), a A036 ganhou ressalva e A064 e A074 foram examinadas e mantidas pela regra de fato em apuração; corte-02 e corte-04 foram renderizados de novo (`CORRECOES.md` §4). Por fim, uma **validação final** (`CORRECOES.md` §5): o minuto dos cards passou a contar do início da entrevista (campo `inicio_da_entrevista_s`, com esquema e teste), as bordas dos seis cortes foram para a pausa da voz (três terminavam no começo da palavra seguinte), o tempo de cada alegação foi medido numa transcrição palavra por palavra, a A033 virou IMPRECISO pela mesma régua da A003 e da A154, e o card da A183 cita com `[...]` o verbo que o áudio não confirma. 704 trechos conferidos contra as páginas capturadas. Validador: 0 erros, 2 avisos esperados (A018 e A040, sem fonte oficial, e por isso sem comprovação).
- **6 cortes curtos** (81,4 s de emissora) renderizados e validados, entregues em `Videos/youtube/video-longo/video-9/cortes-checados/`.
- **Considerações da IA**: duas passadas (com nomes e espelho) e o documento final.

### Adicionado
- `midia recortar --caixa X,Y,W,H` e `sugerir-cortes.py --caixa`: corta uma caixa declarada (imagem dentro de moldura colorida) e leva a 1920x1080.
- Métricas: `DURACAO_PECA` e `PALAVRAS_PECA`, só com a mesa (sem os trechos `outro`).

### Corrigido
- `caixa_sem_faixas` devolvia uma dimensão ímpar (1102x617); agora 16k x 9k com k par. Teste novo.
- `capturar-fontes.py` quebrava em todo PDF no Windows com `PYTHONUTF8=1` (o `pdftotext` saía em Latin1): pede `-enc UTF-8` e lê bytes.
- `test_caso_real.py`: a peça inteira (sem vídeo próprio) e os cortes curtos derivados dela entram na regressão sem cobrar o que não se aplica a eles.
- `__init__.__version__` estava em 0.4.0 com o pacote em 0.5.0.

## [0.5.0] · 15/out/2026

Pedido do autor, no dia da sabatina de Lula na TV Globo do 2º turno (21h15, 45 min, Renata Lo Prete): checar a **sabatina inteira**, guardar as métricas dos dois lados da mesa e gerar só **5 a 6 cortes curtos**, separados, dos trechos mais importantes e com mais fato, por causa de direito autoral no YouTube. Deixar tudo pronto para ele só entregar a gravação.

### Adicionado

- **`docs/PECA_INTEIRA.md`** e a skill **`checar-sabatina-completa`** (com o ponteiro em `.claude/skills/`): a ordem de execução da gravação até os cortes, com prompts dos agentes, tempo esperado e a lista de conferência.
- **Limites de corte curto** em `config.py` (`CORTE_MAX_S` 30 s, `CORTE_RECOMENDADO_S` 15 s, `CORTES_TOTAL_MAX_S` 120 s, `CORTES_INTERVALO_MIN_S` 60 s; a régua do canal para telejornal é ~10 s por trecho, dentro da moldura), cobrados pelo `derivar-recorte.py`; passar deles só com `--aceito-mais-longo "motivo"`, gravado no corte (`fora_do_limite_de_tamanho` no esquema) e mostrado no relatório.
- **`ferramentas/sugerir-cortes.py`**: aplica o critério pré-registrado (fato, confronto jornalista x candidato, troca de turno, variedade de assunto, uma alegação checável do candidato por corte) **sem abrir o arquivo de vereditos**, e escreve `recortes/SUGESTAO_DE_CORTES.md` com os comandos prontos; `--fixar` para o trecho que ele quiser por repercussão, com o motivo dele.
- **`ferramentas/rascunho-de-turnos.py`**: agrupa os enquadramentos do vídeo, desenha a folha dos grupos para rotular, junta plano + texto + VT declarado num rascunho de turnos e desenha a folha dos turnos. Medido no ensaio sobre a sabatina de 27/ago: 96,5% da fala de Lula e 71% da fala dos jornalistas no falante certo. Não escreve o `falantes.json`.
- `config.recorte_da_peca_inteira()`: `sabatina-completa`, `debate-completo` ou `peca-completa`, conforme o formato do caso; `lotes-de-debate.py` e `derivar-recorte.py` inferem o recorte quando ele não é passado.
- `novo-caso-debate.py --formato sabatina --entrevistador ... --narracao`.
- Campos de roteiro nas métricas: `P_ENTREVISTADO_*`, `P_ENTREVISTADOR_*`, `J1_*` (jornalistas) e os percentuais `N_P?` e `C1_P?`.
- O caso **`casos/2026-10-15-sabatina-lula-globo-2turno/`** aberto antes do evento, com `recortes/SELECAO_DE_CORTES.md` e `consideracoes/CRITERIOS.md` registrados às 10h (a mesma régua vale para a sabatina de Flávio Bolsonaro de 16/out). Commits `37cdb3f` (10h07) e `5812ef4` (10h08, o ajuste para 15 s). 🔧 Às 10h56 (`5fad751`), ainda antes do evento, o `SELECAO_DE_CORTES.md` teve corrigido o horário do ajuste, que estava escrito como 10h40; o critério não mudou.
- 11 testes (123 no total).

### Mudado

- `python -m checagem relatorio --recorte <peça inteira>` funciona sem entrada em `RECORTES.json`: diz que a peça foi checada inteira, traz a tabela por falante (das métricas) e a lista de cortes com o motivo de cada um.
- `consideracoes-do-debate` vale também para sabatina, com a passada espelho no lugar da anonimizada.

### Descoberto no ensaio (e registrado onde mora)

- O tom de voz **não** separa Lula de uma entrevistadora (mediana de 192 Hz contra 188 Hz): `medir-tom.py` não serve de pista neste caso (`docs/PECA_INTEIRA.md` §4).
- Corte curto e denso congela o último quadro: 14 s de trecho com 3 cartelas viram 34 s de arquivo (`docs/PECA_INTEIRA.md` §2).

---

## [0.4.0] · 1º/out/2026

Pedido do autor, no dia do debate presidencial da TV Globo: um **novo braço** do projeto para peças longas com vários candidatos, sem substituir o que existe. Validação sobre a peça inteira, vídeo só de alguns cortes, métricas gerais e por candidato, e uma camada separada de considerações da IA.

### Adicionado

- **`python -m checagem metricas <slug> [--recorte ID]`**: métricas gerais, por falante (na ordem da primeira fala, nunca por resultado) e por assunto, com o denominador e o tempo de fala ao lado, avisos automáticos de assimetria e as ressalvas fixas de `etica-e-risco` §2 e §3. `src/checagem/metricas.py`.
- **`ferramentas/lotes-de-debate.py`**: divide a extração e a checagem em lotes para rodar em paralelo, junta com prova de cobertura (recusa lote faltando, alegação fora da janela, buraco entre janelas, veredito na extração, id inventado) e renumera `A001...`.
- **`ferramentas/derivar-recorte.py`**: o recorte que vira vídeo herda as checagens da peça inteira, com os mesmos ids, e recusa alegação cortada na borda.
- **`ferramentas/novo-caso-debate.py`** e o caso `casos/2026-10-01-debate-presidencial-globo/` (mídia por registrar).
- **`docs/DEBATES.md`**, as skills **`checar-debate`** e **`consideracoes-do-debate`**, e `casos/2026-10-01-debate-presidencial-globo/consideracoes/CRITERIOS.md`, registrado antes do debate.
- 18 testes (110 no total).

### Mudado

- `ferramentas/validar-todos.py` não desenha cartela de recorte sem vídeo (o `debate-completo` não tem render).
- `METODOLOGIA.md` §8 registra a camada de considerações como **separada** da checagem.

---

## [0.3.0] · 30/set/2026

Pedido do autor: usar a íntegra horizontal da sabatina como peça do caso de economia, cortar as faixas pretas, recortar só o bloco e seguir os padrões de 29/set do editor de vídeos longos.

### Adicionado

- **`midia <slug> recortar ... --cortar-faixas`** e **`midia <slug> faixas`**: medem a imagem útil com `cropdetect` em 24 cenas, recuam 4 px da borda mole, ajustam a 16:9 exato e par e levam a 1920x1080 sem deformar. O registro do recorte guarda a caixa, o que foi medido e o filtro (`docs/IDENTIDADE_VISUAL.md` §6.3.1).
- **`ferramentas/migrar-tempos.py`**: leva alegações, turnos e correções de uma mídia para outra. Mede o deslocamento pelo **fim** dos segmentos (o começo varia até 0,8 s entre passadas sobre o mesmo áudio), recusa quando as mídias não andam juntas e lista as correções que o texto novo não sustenta.
- **`renderizar --som-de-entrada`** (desligado por padrão): mixa um estalo de 90 ms em cada cartela que entra, no layout de canais da fala, sem mudar o nível dela.
- Testes do corte de faixas, da entrada com fade, da opacidade dos textos e do canto do card (92 no total).

### Mudado

- **Cartelas entram com fade de 8 quadros** (V31 do editor de longos), no lugar do corte seco; cada cartela vira uma entrada em laço só pela própria vida, então o grafo não cresce. O selo permanente segue seco. `docs/ARQUITETURA.md` §5 reescrita.
- **Card, selo e legenda opacos** (fundo 100%, era 94% no card): nada do vídeo fica por baixo do texto (V33).
- **Canto esquerdo do card arredondado**: o corpo escuro era um retângulo de quina reta sobre a faixa colorida.
- `nuvem-renderizar` passa `--cortar-faixas` quando o registro do recorte traz a caixa de corte.
- Versão do pacote alinhada em 0.3.0 (`pyproject.toml` dizia 0.2.0 e `__init__` 0.1.0).

### Caso Flávio economia: mídia trocada

O clipe vertical do g1 (`ae35ff24…`) deu lugar à íntegra horizontal (`a7006047…`, 44min18s, faixas pretas de 172 px cortadas), com o bloco recortado em 34:02 a 39:40. **Nenhum veredito, resumo ou fonte mudou.** Mudou o relógio (+2042,36 s, medido pelo fim de 58 segmentos idênticos, desvio de 0,08 s), oito correções de transcrição (incluindo `1922` por `2022` e a frase da pergunta seguinte que o motor puxou para o fim do bloco), o limite de turno de 35:32 e a citação de `A018`, que passou a usar `[...]` no verbo que o áudio não decide. Os dados sensíveis ao tempo foram reconferidos até 30/set: nada muda o veredito (`CORRECOES.md`).

---

## [Não publicado]

### Documentado

- **Medida de tempo de leitura dos cards** (§7.1): 17 dos 23 cards do caso publicado ficam na tela menos que o tempo de ler resumo e ressalva a 17 caracteres por segundo. Registrado como limitação conhecida (`ESTADO.md`), sem mudança no pipeline.

---

## [0.2.1] · 27/set/2026

Pedido do autor depois de ver o vídeo do bloco de economia: o vídeo termina com a fala, e a revisão é da própria IA.

### Mudado

- **Sem cartela de encerramento** (`ENCERRAMENTO_S = 0`): o vídeo termina junto com a fala, ou com o congelamento de leitura quando a fila de cards passa do fim do trecho. O endereço do repositório continua na legenda de abertura e no selo.
- **Sem a cartela de divulgação do g1**: os dois recortes do Flávio passaram a cortar na troca de cena antes dela (05:38,1 na economia, 02:38,9 no golpe), conferida quadro a quadro. Ela não é parte da entrevista.
- **Revisão adversarial por IA** no lugar da revisão humana obrigatória: campo `revisao_ia` no esquema, `ferramentas/registrar-revisao.py --ia`, skill nova [`revisar-checagem`](skills/revisar-checagem.md) e aviso no validador para checagem sem revisão registrada. Publicar continua sendo decisão do autor.
- O validador avisa quando a extração traz juízo, promessa ou hipótese como alegação (METODOLOGIA §4.2).

### Corrigido no caso Flávio economia, com registro em `CORRECOES.md`

A revisão adversarial aplicou a régua do §2.2 com mais rigor e mudou cinco checagens: `A005` (14% é a Selic nominal, não o juro real), `A007` (desvio de 14% no "um trilhão"), `A012` ("dívida primária" não existe) e `A020` ("fora do orçamento" troca o conceito) passaram de verdadeiro para impreciso; `A017` perdeu "voto contra" do resumo, que nenhuma fonte sustentava. Placar: 10 verdadeiro, 8 impreciso, 3 sem comprovação.

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
