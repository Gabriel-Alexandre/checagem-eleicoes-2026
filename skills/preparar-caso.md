---
name: preparar-caso
description: PASSOS 0 a 3 do pipeline. Abre um caso novo a partir de um arquivo de vídeo de sabatina, debate ou entrevista: confere a procedência da peça em fontes públicas, escreve CASO.json, assina a mídia, extrai o áudio, transcreve com whisper.cpp local, escreve o mapa de turnos e atribui falante a cada segmento. Use sempre que chegar um vídeo novo para checar, ou quando alguém pedir para "começar um caso". Termina onde extrair-alegacoes começa.
---

# preparar-caso — PASSOS 0 a 3

## O que esta skill entrega

Um caso pronto para extração: pasta criada, `CASO.json` conferido, mídia assinada, transcrição
com falante em cada segmento, e um recorte escolhido para a primeira rodada.

---

## PASSO 0 · procedência, antes de tudo

> 🔴 **Um caso começa checando o próprio arquivo.** Se você não sabe de onde veio o vídeo, se ele
> está inteiro e de que dia é, toda a checagem em cima dele é castelo sobre areia.

Descubra, com busca na internet e ≥ 2 fontes:

| O que | Por que importa |
|---|---|
| data e horário do evento | o veredito usa a fonte vigente **na data da fala** |
| veículo e programa | identifica a peça e permite achar a íntegra oficial |
| **quem estava na mesa, nome completo** | atribuir frase à pessoa errada é o pior erro do projeto |
| se o arquivo é a **íntegra** ou um recorte | corte muda contexto, e isso vai declarado |
| se existe transcrição publicada por terceiro | é a melhor conferência da sua transcrição |

⚠️ **Confira o vídeo contra o que você achou.** Extraia alguns quadros
(`ffmpeg -ss <t> -i <video> -frames:v 1 quadro.png`) e confirme cenário, pessoas e o que estiver
escrito na tela. Uma fonte dizendo "os entrevistadores foram A e B" não prova que **este arquivo**
é aquele programa.

Escreva `casos/<slug>/CASO.json` seguindo `esquemas/caso.schema.json`. O `slug` é
`AAAA-MM-DD-<formato>-<pessoa>-<veiculo>`, tudo minúsculo com hífen.

## PASSO 1 · assinar e preparar a mídia

```bash
python -m checagem midia <slug> registrar     # sha256, duração, resolução, fps
python -m checagem midia <slug> audio         # WAV 16 kHz mono
```

O `sha256` é o que amarra a checagem a **este** arquivo. Ele vai no `CASO.json`, no relatório e
no vídeo publicado.

### Escolher o recorte da primeira rodada

⚠️ **Não comece por 45 minutos.** Faça a primeira rodada inteira num recorte de 5 minutos: o
ciclo completo (extrair, checar, desenhar, renderizar, validar) leva minutos em vez de horas, e
todo defeito de formato aparece igual.

Como escolher, e isto é decisão editorial, não técnica:

- densidade de fato por minuto — um bloco com números, datas e comparações rende mais;
- **os dois lados falando** — trecho só de resposta esconde a alegação do entrevistador;
- um trecho **contínuo**, nunca uma colagem: contexto cortado é o defeito que este projeto combate;
- ⛔ **não escolha o trecho pelo resultado esperado.** O motivo vai escrito em `--motivo` e sai no
  relatório, onde qualquer pessoa pode discordar dele.

```bash
python -m checagem midia <slug> recortar bloco-economia \
    --inicio 1200 --duracao 300 --motivo "maior densidade de números por minuto na peça"
python -m checagem midia <slug> audio --recorte bloco-economia
```

## PASSO 2 · transcrever

```bash
python -m checagem transcrever <slug>
```

Roda `whisper.cpp` local com `large-v3-turbo`. ~3x tempo real: 45 min de áudio levam ~15 min.
O cabeçalho da transcrição guarda o `sha256` do modelo e os parâmetros — é o que torna a
transcrição refazível.

**Confira a transcrição contra a peça.** Numa sabatina de TV existe quase sempre uma transcrição
publicada (Poder360, o próprio veículo). Divergência achada não se conserta em silêncio: vai em
`transcricao/CORRECOES_DE_TRANSCRICAO.md`, com antes, depois e quem conferiu no áudio.

⚠️ **Nome próprio é onde o reconhecimento mais erra**, e nome próprio errado numa citação é
exatamente o tipo de defeito que desqualifica o projeto. Confira um a um.

## PASSO 3 · quem falou o quê

Escreva `casos/<slug>/transcricao/falantes.json` com os turnos. Numa sabatina a virada é evidente
na leitura: pergunta longa, resposta longa.

```json
{ "caso": "<slug>",
  "turnos": [
    { "inicio_s": 0.0,   "fim_s": 118.4, "falante": "César Tralli" },
    { "inicio_s": 118.4, "fim_s": 190.2, "falante": "Lula" } ] }
```

```bash
python -m checagem falantes <slug>
python -m checagem transcrever <slug> --so-texto   # regera o .txt legível, agora com falante
```

O script imprime quanto tempo cada pessoa falou. **Olhe esse número:** numa sabatina de 40 min o
entrevistado costuma ficar entre 55% e 75%. Muito fora disso quase sempre é turno mal escrito.

---

## Antes de passar para o PASSO 4

- [ ] `CASO.json` com procedência conferida em ≥ 2 fontes, e `integralidade` declarada
- [ ] `fonte/MIDIA.json` com o sha256
- [ ] transcrição gerada, conferida nos nomes próprios e nos números falados
- [ ] `falantes.json` escrito e aplicado, sem segmento órfão
- [ ] recorte da primeira rodada criado, com `--motivo` escrito
- [ ] `python -m checagem validar <slug>` não acusa nada da parte de mídia e transcrição

**Próximo passo:** `skills/extrair-alegacoes.md`.
