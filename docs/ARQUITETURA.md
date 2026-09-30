# ARQUITETURA — as decisões técnicas, e por que cada uma

Este documento existe para a pergunta "por que assim e não do outro jeito". Se alguém for
mudar uma dessas decisões, que mude sabendo o que ela estava segurando.

---

## O desenho em uma linha

```
vídeo ──▶ [1] mídia ──▶ [2] transcrição ──▶ [3] falantes
                                                  │
                                                  ▼
                                        [4] alegações  (IA, sem internet)
                                                  │
                                                  ▼
                                        [5] checagens  (IA, com internet)
                                                  │
                              ┌───────────────────┴───────────────────┐
                              ▼                                       ▼
                     [6] cartelas PNG                         RELATORIO.md
                              │
                              ▼
                     [7] render ffmpeg ──▶ [8] validador ──▶ revisão por IA
```

**Determinístico:** 1, 2, 6, 7, 8. **Julgamento:** 3 (revisado), 4, 5 e a revisão final.

---

## 1. Separar extração de checagem em dois arquivos

**Decisão:** `alegacoes.json` não tem campo de veredito, e é escrito antes de qualquer busca.

**Por quê:** o viés de confirmação não entra na hora de julgar; ele entra na hora de **escolher o
que julgar**. Quem já sabe que uma frase é falsa extrai mais frases daquele falante e "não vê" as
que dariam certo. Separar em dois arquivos, com a internet fechada no primeiro, torna o viés
visível: se a extração foi enviesada, a contagem por papel no relatório mostra.

**O custo:** duas passadas na peça em vez de uma. Vale.

## 2. Transcrição local, não API

**Decisão:** `whisper.cpp` com `ggml-large-v3-turbo`, rodando na máquina.

**Por quê:**
- **Reprodutibilidade.** Mesmo arquivo + mesmo modelo + mesmos parâmetros = mesma saída. Uma API
  que muda de versão sem avisar não sustenta um veredito citável.
- **Procedência.** O `sha256` do modelo vai no cabeçalho da transcrição.
- **Custo e escala.** 45 minutos de sabatina saem em ~15 min de CPU, sem enviar a peça para
  lugar nenhum.

**Medido nesta máquina** (12 núcleos, 10 threads): ~2,8x tempo real.

**O custo:** 1,6 GB de modelo baixado uma vez. E ⛔ o whisper **não separa vozes** — daí o passo 3.

## 3. Falante por mapa de turnos escrito à mão

**Decisão:** ⛔ nada de diarização automática. Um `falantes.json` com intervalos, aplicado por script.

**Por quê:** atribuir uma frase à pessoa errada é o pior erro possível aqui — pior que errar o
veredito, porque coloca na boca de alguém algo que a pessoa não disse. Os diarizadores que rodam
offline erram exatamente na virada de turno, que é onde a frase muda de dono. Um arquivo de
turnos é auditável linha a linha; um vetor de embedding não é.

**Por que dá para fazer à mão:** numa sabatina o turno é evidente na leitura — pergunta longa,
resposta longa. Numa peça com muita interrupção cruzada, esta decisão precisa ser revista.

## 4. Cartela como quadro inteiro em PNG

**Decisão:** cada card é um PNG RGBA de 1920x1080 desenhado no Pillow, já com moldura e tarja no
lugar. O ffmpeg faz um `overlay=0:0` por cartela.

**As alternativas, e por que perderam:**

| Alternativa | Por que não |
|---|---|
| `drawtext` do ffmpeg | não quebra linha por largura real, sofre com acentuação e não faz canto arredondado |
| legenda ASS (libass) | boa para texto, ruim para caixa arredondada, barra colorida e composição |
| HTML + navegador headless | melhor resultado visual, e mais uma cadeia inteira de dependências para reproduzir |
| PNG só da tarja + `drawbox` para a moldura | 4 filtros a mais por card, e o alinhamento passa a depender de constante repetida em dois lugares |

O quadro inteiro faz o grafo de filtro virar **uma linha por card**, e o alinhamento existir em
um lugar só (o Pillow). O custo é ~150 KB por cartela em disco, que não entra no git.

## 5. Entrada com fade de 8 quadros (o selo entra seco)

🔧 **Revista em 30/set/2026.** Até 0.2.1 a decisão era corte seco. Ela foi trocada porque o padrão
de 29/set do editor de vídeos longos (V31: *todo elemento que entra tem animação*) passou a valer
aqui também (ver `CLAUDE.md`, nota de 29/set).

**Decisão:** cada cartela, e a legenda de abertura, entra com `fade=t=in:d=0,267:alpha=1`
(8 quadros a 30 fps). O `enable='between(t,entra,sai)'` continua mandando na saída, que segue
seca, e o selo permanente não anima: ele já está na tela no primeiro quadro.

**Como sem inflar o grafo:** o motivo original do corte seco era o custo de `-loop 1 -t D` por
cartela. O custo só é grande se o laço dura o vídeo inteiro. Aqui cada cartela vira uma entrada em
laço **só pela sua própria vida** (`-t` = tempo na tela + 0,25 s), deslocada para o segundo certo
por `setpts=PTS+entra/TB`, e o `overlay` usa `eof_action=pass`. São segundos de quadros por
cartela, não minutos.

**Som:** o padrão V32 do mesmo editor pede um som no quadro de cada entrada. Aqui ele é **opt-in**
(`--som-de-entrada`, um estalo de 90 ms a -20 dBFS, mixado sem tocar na fala). O motivo é que o
PASSO 7 copia o áudio sem reencodar para o vídeo ser conferível contra a peça original, e mixar
muda o arquivo de áudio. Qual das duas regras vale no vídeo publicado é decisão do mantenedor
(`ESTADO.md`).

## 6. Uma cartela por vez na tela

**Decisão:** a janela de um card é cortada 0,2s antes do próximo começar.

**Por quê:** com dois cards, o espectador não sabe a qual frase a moldura se refere — e a moldura
é a leitura mais rápida da tela. Quando as falas estão coladas demais, o script **avisa** em vez
de encolher a permanência global. Card curto é um problema de extração (duas alegações que eram
uma), não de tempo de tela.

## 7. O validador como porta, não como relatório

**Decisão:** `passo8_validar.py` sai com código 1.

**Por quê:** metodologia que ninguém executa vira enfeite em três semanas. As travas que só existem
em prosa não sobrevivem à quinta sessão de trabalho. As que estão em código sobrevivem.

**A trava mais importante que ele implementa:** a citação do card tem que existir na transcrição,
comparada com texto normalizado. Um modelo parafraseia sem perceber, e aspa parafraseada num vídeo
de checagem é exatamente o defeito que o projeto diz combater.

## 7.1 Derivado não é exigido, é conferido

**Decisão (0.2.0):** as cartelas PNG são derivadas e ficam fora do git; o validador **não** as
exige num clone limpo, mas confere que o plano versionado concorda com as checagens (mesmo
conjunto de ids, mesmo veredito). A CI redesenha as cartelas e reprova se o plano regerado
diferir do versionado.

**Por quê:** até a 0.1.1 o validador exigia as PNGs, e a CI reprovou em todos os pushes desde o
primeiro commit. Uma porta que reprova sempre é tão inútil quanto uma que aprova sempre:
ninguém olha mais para ela. O risco real não era a PNG faltar; era o plano ficar velho e a
moldura sair com a cor de um veredito que já mudou.

## 8. Mídia fora do git, manifesto dentro

**Decisão:** `.gitignore` cobre vídeo, áudio e render; `MIDIA.json` com `sha256` é versionado.

**Por quê:** o repositório guarda **o que foi dito e a checagem**, não o arquivo. Quem clona baixa
a peça pela `url_oficial` e confere o hash. Um repositório de 700 MB por caso morre no terceiro
caso.

## 9. Recorte guarda o tempo absoluto

**Decisão:** `RECORTES.json` grava `origem_inicio_s`, e a transcrição de um recorte já nasce com o
deslocamento aplicado.

**Por quê:** sem isso, um card checado num recorte de 5 min não sabe voltar ao minuto certo da peça
inteira, e a transcrição do recorte vira uma segunda verdade que ninguém consegue casar com a
primeira. Com isso, a checagem feita num recorte serve, sem recálculo, para renderizar a peça toda.

---

## Dependências, e o que cada uma segura

| Ferramenta | Para quê | Se sumir |
|---|---|---|
| **ffmpeg / ffprobe** | medir, extrair áudio, recortar, renderizar | não há pipeline |
| **whisper.cpp** (`whisper-cli`) | transcrever | dá para trocar por outro ASR, desde que grave modelo e parâmetros |
| **Pillow** | desenhar as cartelas | trocar exige refazer o `passo6` inteiro |
| **jsonschema** | validar os contratos | o validador degrada para os testes próprios e avisa |
| **Inter** (OFL) | tipografia | qualquer fonte variável com acentuação latina serve |

⛔ Sem dependência de nuvem no caminho crítico. A única etapa que precisa de internet é a **busca
de fontes** do PASSO 5, que é justamente a etapa que precisa da internet por definição.

🌐 **O desvio documentado:** quando o ambiente de trabalho não alcança o YouTube nem os portais,
os passos mecânicos (baixar, transcrever, capturar páginas) rodam num runner do GitHub com o
mesmo motor e o mesmo modelo, e devolvem o resultado num release em rascunho. Ver
[`NUVEM.md`](NUVEM.md). O runner é substituível por qualquer máquina com rede; o método não muda.
