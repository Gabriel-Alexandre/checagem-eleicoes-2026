# PEÇA INTEIRA: a sabatina checada do começo ao fim, com cortes curtos

**Criado:** 15/out/2026, a pedido do autor, no dia da sabatina de Lula na TV Globo do 2º turno (21h15, logo depois do Jornal Nacional, 45 minutos, conduzida por Renata Lo Prete). Palavras dele:

> *"em vez de apenas analisar um trecho da sabatina, eu quero que ele analise a sabatina toda. E faça e guarde questões estatísticas relacionadas a quantas verdades foi, do lado do Lula, quantas é mentiras [...] do lado dos jornalistas"* · *"com o mesmo rigor que foi feito para o vídeo do Flávio"* · *"ao final, não vai ser gerado um vídeo gigantesco. O que vai ser gerado são apenas alguns cortes dos trechos mais, entre aspas, polêmicos. Ou mais importantes"* · *"focar nas partes que falam mais sobre fatos"* · *"tem que ser trechos bem curtos. Não pode ser trecho de, por exemplo, um minuto"* · *"pelo menos uns 5, 6 trechos diferentes. Não de continuidade"* · *"quando terminar a sabatina, eu passo a gravação para você e quero que simplesmente você execute e deixe tudo organizado"*

> ⚠️ Este arquivo é **operação**. A doutrina (vereditos, fontes, o que o projeto não conclui) continua em [`METODOLOGIA.md`](METODOLOGIA.md), e **ela ganha**. O braço de debate ([`DEBATES.md`](DEBATES.md)) é o irmão mais velho: lotes, junção, métricas e derivação de corte são as mesmas ferramentas, e o que está lá vale aqui salvo onde este arquivo diz outra coisa.

---

## 1. O que muda em relação às sabatinas de agosto e setembro

| | Casos 1 a 3 (um bloco) | Peça inteira (desde 15/out) |
|---|---|---|
| O que se checa | um bloco escolhido por tema | **a sabatina inteira**, recorte `sabatina-completa` (sem vídeo renderizado) |
| Volume | 20 a 25 alegações | 80 a 150 numa sabatina de 45 min (`extrair-alegacoes`, densidade) |
| Resultado | contagem do trecho | **métricas** gerais, por falante e por lado da mesa (entrevistado × jornalista), por assunto e por bloco, com o denominador à vista |
| O que vira vídeo | o bloco inteiro | **5 a 6 cortes curtos**, separados, que herdam a checagem da peça inteira |
| Relatório | do trecho | `RELATORIO_SABATINA_COMPLETA.md`: a peça toda, alegação por alegação, com a seção por falante e a lista de cortes |
| Camada extra | nenhuma | **considerações da IA**, separadas da checagem, com critérios registrados antes do evento (`consideracoes/CRITERIOS.md`) |

O que **não** muda: nenhum fato da memória do modelo, duas fontes independentes, a mesma régua para a jornalista e para o candidato, extração de internet fechada antes de qualquer busca, revisão adversarial em passada separada, e o validador como porta.

## 2. Os cortes curtos (direito autoral)

Decisão dele, 15/out: os cortes vão para o YouTube e **não podem** ser trechos longos. Os números moram em [`src/checagem/config.py`](../src/checagem/config.py) e o `derivar-recorte.py` recusa o que passa deles:

| Regra | Valor | Onde trava |
|---|---|---|
| trecho da emissora num corte | **até 30 s** (recusa acima), **15 s recomendado** (avisa acima) | `CORTE_MAX_S`, `CORTE_RECOMENDADO_S` |
| soma dos cortes da peça | **até 120 s** (menos de 5% de 45 min) | `CORTES_TOTAL_MAX_S` |
| distância entre dois cortes | **pelo menos 60 s**: um corte não é continuação do outro | `CORTES_INTERVALO_MIN_S` |
| quantos | **5 a 6** | `CORTES_QUANTIDADE` |

Passar de qualquer limite só com `--aceito-mais-longo "motivo"`; o motivo fica gravado no arquivo do corte e aparece no relatório.

🔑 **A régua do canal para telejornal** (skill `trechos-de-terceiros-no-video` do repositório do canal, `LOW_TICKET_1`): *até ~10 s por trecho*, **dentro da moldura** (o retângulo 3D do editor de longos, nunca em tela cheia), cada trecho seguido do comentário dele, crédito da emissora na tela e na descrição. Os 15 s daqui cabem uma pergunta curta e a resposta; o que passar de ~10 s pede o comentário dele logo em seguida.

⚠️ **O quadro congelado.** Num corte curto e denso, as cartelas fazem fila e o último quadro congela até a última ser lida. Medido no ensaio de 15/out: **14 s de trecho com 3 cartelas viram 34 s de arquivo** (20 s de quadro parado, sem som). O áudio da emissora continua sendo só o trecho. Se o congelamento passar de ~10 s, há duas saídas, e as duas são dele: um corte com menos alegações, ou o editor de longos mostrar as cartelas (que são arte do projeto, não da emissora) sobre a narração dele em vez do quadro congelado da emissora.

⚠️ **Não é parecer jurídico.** A Lei 9.610/98, art. 46, III permite a citação "na medida justificada para o fim a atingir", com indicação de autor e origem; trecho curto, crédito da emissora na tela e na descrição e a análise por cima são o que pesa a favor. O Content ID do YouTube é automático e não lê a lei: um corte pode ser reivindicado mesmo assim, e a contestação é dele.

## 3. Como os cortes são escolhidos (critério ANTES dos vereditos)

[`etica-e-risco`](../.cursor/rules/etica-e-risco.mdc) §1: a escolha do recorte não pode ser feita pelo resultado. Ele pediu os trechos *"mais polêmicos ou mais importantes"* e *"que falam mais sobre fatos"*. As duas coisas viram critério **observável antes da checagem**, registrado em `casos/<slug>/recortes/SELECAO_DE_CORTES.md` **antes do evento**, e calculado por `ferramentas/sugerir-cortes.py`, que **não abre** o arquivo de vereditos:

- **fato:** alegações checáveis dentro da janela (dado duro pesa mais);
- **confronto:** a jornalista afirma fato e o candidato responde com fato na mesma janela;
- **troca de turno:** viradas entre jornalista e candidato, o sinal observável de "momento quente" (sem ler tom, intenção ou resultado);
- **variedade:** um assunto por corte antes de repetir assunto;
- todo corte tem **pelo menos uma alegação checável do candidato**.

"Polêmico" no sentido de repercussão (o trecho que a imprensa destacou) é a porta `--fixar INICIO-FIM "motivo"`: entra, com o motivo dele escrito, e o relatório mostra que veio de fora do critério.

## 4. Quem falou o quê

Uma jornalista e um candidato, mais o VT de abertura. O PASSO 3 continua manual; [`ferramentas/rascunho-de-turnos.py`](../ferramentas/rascunho-de-turnos.py) adianta o trabalho com o **enquadramento** (a emissora mostra quem fala) e o **texto** (pergunta, vocativo, nome de quem pergunta), e entrega folhas de quadros para conferir no olho.

📏 Medido no ensaio de 15/out sobre a sabatina de 27/ago: 89% do tempo no lado certo da mesa, **96,5% da fala de Lula** certa, mas **71% da fala dos jornalistas** (pergunta em plano aberto herda o falante anterior). ⛔ **O tom de voz não separa Lula de uma entrevistadora** (192 Hz de mediana contra 188 Hz): não use `medir-tom.py` como pista neste caso.

## 5. O pipeline, comando a comando

```bash
SLUG=2026-10-15-sabatina-lula-globo-2turno     # o caso já foi aberto antes do evento
export PATH="$HOME/scoop/shims:$PATH"

# PASSO 0 e 1 · a peça (o autor entrega o arquivo e diz de onde veio)
#   copiar o vídeo para casos/$SLUG/fonte/ e preencher `procedencia` no CASO.json ANTES de transcrever
python -m checagem midia $SLUG registrar
python -m checagem midia $SLUG audio
python -m checagem midia $SLUG faixas            # só mede: tem faixa preta? (então os cortes usam --cortar-faixas)

# PASSO 2 · transcrição (~15 min de CPU para 45 min de vídeo) e, em paralelo, os planos
python -m checagem transcrever $SLUG
python ferramentas/rascunho-de-turnos.py planos $SLUG          # ~1,5 min; folha-de-planos.jpg
#   segunda passada nos nomes, números e anos; correções por script (corrigir-transcricao.py)

# PASSO 3 · turnos
#   rotular transcricao/planos-rotulos.json olhando a folha
python ferramentas/rascunho-de-turnos.py turnos $SLUG --pergunta "Renata Lo Prete" --responde "Lula" --vt INI-FIM --folha
#   conferir TODO turno da jornalista e o começo de cada resposta; escrever transcricao/falantes.json
python -m checagem falantes $SLUG
#   escrever metricas/blocos.json (os temas da entrevista, lidos no vídeo)

# PASSO 4 · extração em lotes, internet FECHADA (um agente por lote, skills/extrair-alegacoes.md)
python ferramentas/lotes-de-debate.py extracao-dividir $SLUG --minutos 8
python ferramentas/lotes-de-debate.py extracao-juntar  $SLUG

# a escolha dos cortes, ANTES de qualquer veredito
python ferramentas/sugerir-cortes.py $SLUG                     # recortes/SUGESTAO_DE_CORTES.md
#   commit da sugestão (o horário do commit prova que veio antes da checagem)

# PASSO 5 · checagem em lotes (um agente por pedido, skills/checar-alegacao.md)
python ferramentas/lotes-de-debate.py checagem-dividir $SLUG --tamanho 10
python ferramentas/lotes-de-debate.py checagem-juntar  $SLUG
python ferramentas/capturar-fontes.py $SLUG
python ferramentas/conferir-trechos.py $SLUG --recorte sabatina-completa --capturas capturas/$SLUG

# revisão adversarial, por quem não checou (skills/revisar-checagem.md), sobre o conjunto
python ferramentas/registrar-revisao.py $SLUG --recorte sabatina-completa --ia --notas revisao.json

# a porta, as métricas e o relatório da peça inteira
python -m checagem validar   $SLUG --recorte sabatina-completa
python -m checagem metricas  $SLUG --recorte sabatina-completa --blocos casos/$SLUG/metricas/blocos.json
python -m checagem relatorio $SLUG --recorte sabatina-completa

# os cortes (os comandos exatos saem prontos no SUGESTAO_DE_CORTES.md)
python -m checagem midia $SLUG recortar corte-01 --inicio S --duracao S --motivo "..." [--cortar-faixas]
python ferramentas/derivar-recorte.py $SLUG --para corte-01 --inicio S --fim S
python -m checagem overlay $SLUG --recorte corte-01
python -m checagem renderizar $SLUG --recorte corte-01
python -m checagem validar $SLUG --recorte corte-01
```

O roteiro do agente, com os prompts de cada lote e a lista do que conferir antes de fechar, é a skill [`checar-sabatina-completa`](../skills/checar-sabatina-completa.md).

## 6. As saídas, e quem lê cada uma

| Arquivo | Para quê |
|---|---|
| `metricas/METRICAS_sabatina-completa.md` e `.json` | os números da peça, por falante, por lado da mesa, por assunto e por bloco; o bloco `para_roteiro` do JSON tem cada ⟦campo⟧ do roteiro do vídeo já preenchido (`N_*`, `C1_*`, `J1_*`, `P_ENTREVISTADO_*`, `P_ENTREVISTADOR_*`, `B1_*`...) |
| `RELATORIO_SABATINA_COMPLETA.md` | o documento público: alegação por alegação, com fontes, a seção por falante e a lista de cortes |
| `recortes/SELECAO_DE_CORTES.md` · `SUGESTAO_DE_CORTES.md` | o critério (antes do evento) e a aplicação dele (antes dos vereditos) |
| `render/<slug>-checado-corte-NN.mp4` | os cortes com cartela, para o editor de longos e o de cortes |
| `consideracoes/CONSIDERACOES_IA.md` | a camada separada pedida pelo autor (skill `consideracoes-do-debate`, que vale também para sabatina) |

🔴 **O que as métricas nunca viram** (inalterado): nota, placar, "mentiu N vezes", ranking por falsidade, soma de `FALSO` com `IMPRECISO`. "Mentira" não é veredito deste projeto: `FALSO` diz que o enunciado não bate com o dado, não que a pessoa sabia ([`METODOLOGIA.md`](METODOLOGIA.md) §8). O vídeo dele já explica isso desde o VIDEO_002.
