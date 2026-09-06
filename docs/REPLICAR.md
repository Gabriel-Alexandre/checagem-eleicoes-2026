# REPLICAR — do arquivo de vídeo ao vídeo checado

Este documento existe para uma pessoa que nunca viu o projeto conseguir refazer um caso inteiro, ou abrir um caso novo, sem perguntar nada a ninguém. Ele é o passo a passo; o **porquê** de cada decisão está em [`ARQUITETURA.md`](ARQUITETURA.md) e a régua de julgamento está em [`METODOLOGIA.md`](METODOLOGIA.md).

⏱️ **Quanto custa:** para um caso de 45 minutos, cerca de 20 minutos de máquina (transcrição e render) e de 3 a 6 horas de trabalho de julgamento e conferência de fontes, dependendo da densidade da peça.

---

## 0. Preparar a máquina (uma vez)

| | Como instalar |
|---|---|
| Python 3.10+ | python.org |
| **ffmpeg / ffprobe** | `scoop install ffmpeg` · `apt install ffmpeg` · `brew install ffmpeg` |
| **whisper.cpp** (`whisper-cli`) | `scoop install whisper-cpp` · `brew install whisper-cpp` · ou compile de `ggerganov/whisper.cpp` |
| um agente de IA com busca na web | Claude Code, Cursor, ou você mesmo, à mão |

```bash
git clone https://github.com/Gabriel-Alexandre/checagem-eleicoes-2026
cd checagem-eleicoes-2026
pip install -r requirements.txt
python -m checagem ativos baixar-fontes      # Inter, licença OFL
```

⚠️ **No Windows com scoop, os shims podem não estar no PATH do shell:**

```bash
export PATH="$HOME/scoop/shims:$PATH"
```

🔴 **Sem `ffprobe` nada funciona**, porque é ele que mede o arquivo. O pipeline reclama com o comando de instalação na mensagem, em vez de quebrar com stack trace.

---

## 1. Refazer o caso que já está aqui

O repositório traz um caso completo: [`casos/2026-08-27-sabatina-lula-globo`](../casos/2026-08-27-sabatina-lula-globo/). O que **não** está aqui é o vídeo, que não é redistribuído (ver [§6](#6-por-que-o-vídeo-não-está-no-repositório)).

```bash
SLUG=2026-08-27-sabatina-lula-globo

# 1. ponha o vídeo em casos/$SLUG/fonte/ com o nome que está no CASO.json
# 2. confira que é o MESMO arquivo:
python -m checagem midia $SLUG registrar
```

O `sha256` impresso tem que bater com o de `CASO.json`. **Se não bater, é outro arquivo**, e os tempos das alegações não vão cair no lugar certo. Isso não é frescura de engenheiro: um corte de dois segundos no começo desloca todos os 23 cards.

Depois:

```bash
python -m checagem midia $SLUG audio
python -m checagem transcrever $SLUG                 # ~15 min para 45 min de áudio
python ferramentas/corrigir-transcricao.py $SLUG     # aplica as correções registradas
python -m checagem falantes $SLUG
python -m checagem validar $SLUG --recorte bloco-contas-publicas
```

O validador tem que sair com **0 erros**. Se sair com erro na trava de citação, sua transcrição saiu diferente da que gerou as alegações — o que é esperado se você usou outro modelo. Nesse caso, ou use o mesmo modelo declarado em `transcricao.json`, ou refaça as citações.

Para chegar ao vídeo:

```bash
python -m checagem midia $SLUG recortar bloco-contas-publicas --inicio 1352.32 --duracao 292 \
    --motivo "ver RECORTES.json"
python -m checagem overlay    $SLUG --recorte bloco-contas-publicas
python -m checagem renderizar $SLUG --recorte bloco-contas-publicas
python -m checagem relatorio  $SLUG --recorte bloco-contas-publicas
```

---

## 2. Abrir um caso novo

### 2.1 PASSO 0 · procedência

> 🔴 **Um caso começa checando o próprio arquivo.** Se você não sabe de onde veio o vídeo, se ele está inteiro e de que dia é, toda a checagem em cima dele é castelo sobre areia.

Descubra, com busca na internet e **duas fontes**: data e horário, veículo e programa, **nome completo de quem estava na mesa**, se o arquivo é a íntegra ou um recorte, e se existe transcrição publicada por terceiro (é a melhor conferência da sua).

Confira contra o próprio vídeo, extraindo quadros:

```bash
ffmpeg -v error -ss 120 -i video.mp4 -frames:v 1 -y quadro.png
```

⚠️ Uma fonte dizendo "os entrevistadores foram A e B" **não prova** que este arquivo é aquele programa.

Crie a pasta e escreva o `CASO.json` seguindo [`esquemas/caso.schema.json`](../esquemas/caso.schema.json):

```bash
SLUG=2026-08-28-sabatina-fulano-veiculo     # AAAA-MM-DD-formato-pessoa-veiculo
mkdir -p casos/$SLUG/{fonte,recortes,transcricao,alegacoes,checagens,overlay,render}
```

### 2.2 PASSOS 1 a 3 · mídia, transcrição, falantes

```bash
python -m checagem midia $SLUG registrar
python -m checagem midia $SLUG audio
python -m checagem transcrever $SLUG
```

**Confira a transcrição.** Nome próprio e número falado são onde o motor mais erra, e são exatamente os campos que a checagem usa. Erro achado vai para `transcricao/correcoes.json` e entra por script, com antes, depois e como foi conferido:

```bash
python ferramentas/corrigir-transcricao.py $SLUG --conferir   # só verifica
python ferramentas/corrigir-transcricao.py $SLUG              # aplica e escreve o registro
```

🔑 **Como conferir sem ouvir mil vezes:** transcreva de novo **só a janela suspeita**, isolada, com outros parâmetros. Se duas passadas independentes concordarem, é correção; se discordarem, o trecho fica registrado como não resolvido e a frase não vira alegação.

```bash
ffmpeg -v error -i audio.wav -ss 143 -t 16 -y /tmp/janela.wav
whisper-cli -m ~/.cache/whisper-models/ggml-large-v3-turbo.bin -f /tmp/janela.wav \
    -l pt -bs 8 -bo 8 -np -nt
```

Depois escreva `transcricao/falantes.json` com os turnos e aplique:

```bash
python -m checagem falantes $SLUG
python -m checagem transcrever $SLUG --so-texto     # regera o .txt legível, com falante
```

**Como decidir quem falou o quê**, em ordem de força da evidência:

1. **A pessoa é chamada pelo nome na resposta** ("Renata, nem os contratos foram suspensos") — é a evidência mais forte e a mais barata.
2. **Um quadro do vídeo no meio do bloco de pergunta.** Sampleie de 5 a 8 segundos **depois** do início do turno: o diretor de TV costuma segurar o entrevistado na tela durante a primeira frase da pergunta.
3. ⛔ **Não confie em quadro tirado no primeiro segundo do turno** e não confie em plano aberto: nele todo mundo aparece e ninguém está identificado.

⚠️ O script imprime quanto tempo cada pessoa falou. **Olhe esse número.** Numa sabatina o entrevistado costuma ficar entre 55% e 75%; muito fora disso quase sempre é turno mal escrito.

> 🧪 **O que NÃO funcionou, para você não repetir.** Este projeto escreveu uma ferramenta que mede a frequência fundamental da voz ([`ferramentas/medir-tom.py`](../ferramentas/medir-tom.py)), na expectativa de separar um entrevistador homem de uma entrevistadora mulher pelo tom. **No áudio desta sabatina ela não separou nada**: o som de TV é comprimido e filtrado, o fundamental fica atenuado e o estimador erra a oitava. A ferramenta ficou no repositório porque o método é válido em áudio limpo e porque ela avisa quando não serve — mas ⛔ não conte com ela.

### 2.3 PASSOS 4 e 5 · a parte que é julgamento

Não há comando. Um agente de IA (ou você) segue, nesta ordem:

1. [`skills/extrair-alegacoes.md`](../skills/extrair-alegacoes.md) — varre a transcrição inteira, em ordem, **com a internet fechada**, e escreve `alegacoes/`.
2. [`skills/checar-alegacao.md`](../skills/checar-alegacao.md) — busca fontes e escreve `checagens/`.

🔴 **A ordem e a separação em dois arquivos são o coração do método.** Quem já sabe a resposta escolhe as perguntas. Ver [`METODOLOGIA §5`](METODOLOGIA.md).

### 2.4 Escolher o recorte da primeira rodada

⚠️ **Não comece por 45 minutos.** Faça a primeira rodada inteira num trecho de 5 minutos: o ciclo completo leva minutos em vez de horas, e todo defeito de formato aparece igual.

```bash
python -m checagem midia $SLUG recortar bloco-x --inicio 1352.32 --duracao 292 \
    --motivo "maior densidade de afirmação numérica por minuto da peça"
```

Como escolher, e isto é decisão editorial, não técnica:

- densidade de fato por minuto;
- **os dois lados falando** — trecho só de resposta esconde a alegação do entrevistador;
- um trecho **contínuo**, nunca uma colagem;
- ⛔ **não escolha o trecho pelo resultado esperado.** O `--motivo` sai no relatório, onde qualquer pessoa pode discordar dele.

### 2.5 PASSOS 6 a 8 · desenhar, renderizar, validar

```bash
python -m checagem overlay    $SLUG --recorte bloco-x
python -m checagem renderizar $SLUG --recorte bloco-x
python -m checagem validar    $SLUG --recorte bloco-x
python -m checagem relatorio  $SLUG --recorte bloco-x
```

---

## 3. 🔴 A conferência com o olho, que os números não substituem

O validador confere **texto de JSON**. Ele não vê a imagem. Uma cartela que cobre a assinatura da emissora, um texto que estoura a caixa, uma moldura verde numa fala que a tarja diz ser falsa: nada disso reprova em validador nenhum.

**Antes de renderizar**, componha uma cartela sobre um quadro e olhe:

```bash
python - <<'PY'
import subprocess
from PIL import Image
subprocess.run(["ffmpeg","-v","error","-ss","108","-i","recortes/bloco-x.mp4",
                "-frames:v","1","-y","/tmp/bg.png"], check=True)
bg = Image.open("/tmp/bg.png").convert("RGBA")
bg.alpha_composite(Image.open("overlay/cartelas-bloco-x/A012.png").convert("RGBA"))
bg.convert("RGB").save("/tmp/preview.jpg", quality=90)
PY
```

**Depois de renderizar**, extraia um quadro no meio de cada card e um **no intervalo entre dois**:

| Confira | Reprova quando |
|---|---|
| a moldura tem a cor do veredito da tarja | verde na moldura e FALSO na tarja |
| a citação cabe em 2 linhas e termina com sentido | corta no meio de um número |
| a ressalva não fica pela metade | termina em reticências no meio da frase |
| a linha de fontes não some com duas fontes da mesma casa | diz "FONTES: IBGE" onde há dois documentos |
| a cartela não cobre o rodapé de crédito da emissora | tapa a assinatura da fonte original |
| o texto não estoura a caixa | qualquer letra encostando na borda |
| a legenda de abertura aparece e sai | fica presa, ou nunca aparece |
| no intervalo entre cards não sobra moldura | resto de tarja ou moldura sem card |
| o áudio está lá e sincronizado | vídeo mudo, ou fala fora do card |

> 🧾 **Dois defeitos reais desta primeira rodada, que só o olho pegou:** na cartela de legenda, o rótulo "SEM COMPROVAÇÃO" escrevia por cima da descrição, porque a coluna era fixa em 300px; e a ressalva do card saía cortada no meio de uma frase, porque cabia em uma linha só. Os dois passaram por todos os validadores.

---

## 4. O que dá errado, e o conserto

| Sintoma | Causa | Conserto |
|---|---|---|
| `'whisper-cli' não está no PATH` | shims do scoop fora do PATH do shell | `export PATH="$HOME/scoop/shims:$PATH"` |
| `peso 'Regular' não existe em Inter-Italic` | o arquivo itálico chama a instância de `Italic`, não `Regular` | já tratado em `tipografia.fonte()`; se aparecer, é fonte de outra família |
| `a citação NÃO existe na transcrição` | citação parafraseada, ou transcrição diferente da que gerou as alegações | copie a frase **literal** do `transcricao.txt`, ou refaça a transcrição com o modelo declarado |
| `a mesma URL aparece duas vezes` | dois pedaços da mesma base citados como duas fontes | junte no mesmo `trecho`; duas entradas do mesmo endereço são uma fonte |
| `o número X aparece em resumo mas não em nenhum trecho` | número calculado (subtração, unidade, arredondamento) | declare em `derivacoes`, com as parcelas e a conta |
| `nenhuma fonte N1 ou N2` | alegação numérica sustentada só em imprensa | vá à base primária; a matéria serve de ponteiro, não de fonte |
| `confiança baixa sem revisão humana` | veredito frágil sem alguém assinando | preencha `revisao_humana`, ou reveja o veredito |
| cartela entra muito depois da fala | alegações demais empilhadas no mesmo trecho | confira se houve fatiamento a mais; ⛔ não apague alegação para o vídeo ficar bonito |
| `o vídeo é 1280x720 e as cartelas foram desenhadas para 1920x1080` | recorte de outra resolução | as cartelas são quadros inteiros; recorte na resolução da peça |
| render sem áudio | a entrada não tinha faixa de áudio | o `renderizar` avisa; confira o recorte |
| script morre com `UnicodeEncodeError` | console do Windows em cp1252 | já tratado em `config.py`; se voltar, é script novo sem o `reconfigure` |

---

## 5. Ordem de leitura, se você quiser entender antes de rodar

1. [`METODOLOGIA.md`](METODOLOGIA.md) — os cinco vereditos, a hierarquia de fontes, as armadilhas de enquadramento. **É o documento que manda.**
2. [`ARQUITETURA.md`](ARQUITETURA.md) — por que cada decisão técnica é o que é.
3. [`FONTES_BRASIL.md`](FONTES_BRASIL.md) — onde mora cada dado público brasileiro.
4. [`IDENTIDADE_VISUAL.md`](IDENTIDADE_VISUAL.md) — a tela.
5. [`../ESTADO.md`](../ESTADO.md) — onde o trabalho parou.

---

## 6. Por que o vídeo não está no repositório

O repositório guarda **o que foi dito e a checagem**, não o arquivo. Três razões, e as três importam:

- **Tamanho.** Uma sabatina são 700 MB. Um repositório de texto morre no terceiro caso.
- **Direito.** A peça pertence a quem a produziu. O uso de trechos para checagem se apoia em citação para fins de crítica e informação; redistribuir a íntegra é outra coisa.
- **Método.** O que precisa ser auditável é a transcrição, o veredito e a fonte. O `sha256` em `fonte/MIDIA.json` amarra tudo isso a um arquivo específico, e quem tiver o arquivo confere em um comando.
