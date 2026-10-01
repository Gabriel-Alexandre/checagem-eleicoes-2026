---
name: consideracoes-do-debate
description: Camada editorial pedida pelo autor, separada da checagem. Depois que o debate foi checado e as métricas fechadas, a IA escreve considerações gerais sobre o debate com critérios registrados antes do evento (CRITERIOS.md), duas passadas (com nomes e anonimizada), pesquisas e análises externas atribuídas, teste de simetria e declaração do que não pode ser afirmado. Não recomenda voto e não soma nota.
---

# consideracoes-do-debate

Palavras do autor (1º/out/2026): *"colocar a IA para fazer considerações (gerais e não por candidato) buscando ser imparcial sobre quem se saiu melhor, ela pode considerar pesquisas e outras coisas que achar na internet"*.

## O que esta skill entrega

`casos/<slug>/consideracoes/CONSIDERACOES_IA.md`, com: (1) o que foi o debate, (2) critério a critério o que se observou, (3) a percepção pública medida por terceiros, (4) as duas passadas e onde divergiram, (5) o que o texto **não** pode afirmar, e (6) o **texto-base para a fala do vídeo** (curto, no tom dele).

## 🔴 As travas

1. ⛔ **Não é checagem e não entra nos arquivos da checagem.** `METODOLOGIA.md` §8 continua valendo para o checador. Esta camada é pedida pelo autor, é opinião de IA, e o vídeo diz que é.
2. ⛔ **Os critérios são os de [`CRITERIOS.md`](../casos/2026-10-01-debate-presidencial-globo/consideracoes/CRITERIOS.md), registrados antes do debate.** Critério novo só por adendo datado.
3. ⛔ **Sem soma e sem nota.** Nenhuma pontuação total, nenhum ranking numérico.
4. ⛔ **Sem recomendação de voto, sem previsão, sem leitura de intenção, sem adjetivo sobre pessoa.**
5. ⛔ **Nenhum fato sai da memória do modelo.** Pesquisa, comentário e dado externo entram com URL consultada e trecho copiado, no mesmo padrão da checagem.
6. 🔑 **Critério observável ou em branco.** Se a transcrição não sustenta, a IA diz que não conseguiu.

## O procedimento

### PASSO 0 · antes de começar
Leia `CRITERIOS.md`, `metricas/METRICAS_debate-completo.md` (as métricas **já fechadas**: validador aprovado e revisão registrada) e a transcrição com falantes. ⛔ Não comece com a revisão da checagem aberta: o C3 depende dela.

### PASSO 1 · passada A, com os nomes
Para cada um dos seis critérios e cada participante: o indicador, **dois exemplos** com citação literal e tempo (`[mm:ss]`), e o que não deu para observar. Tabelas de contagem para C1, C2, C4 e C6. O C3 usa só os números de `metricas/`.

### PASSO 2 · passada B, anonimizada
Gere `consideracoes/anonimizada.txt` com `Participante A a D` em **ordem sorteada** (registre a semente) e sem partido. A **segunda passada é feita sem olhar o resultado da A**, de preferência por um agente separado. Compare critério a critério: onde a leitura divergiu, o texto diz.

### PASSO 3 · percepção pública
Pesquisas e análises sobre o debate, **atribuídas** e com data: instituto, amostra, margem e como foi feita (telefone, painel online, enquete aberta); veículo e autor do comentário. Mínimo de duas fontes independentes; procure de orientações diferentes. Se, na hora, não existir nada confiável, escreva que **ainda não existe**. ⛔ Enquete aberta de rede social não é evidência.

### PASSO 4 · o teste de simetria
- troque os nomes de lugar e releia: cada frase continua justa?
- conte palavras por participante (±20%) e exemplos por critério (iguais)
- ⛔ rode `python referencias-conteudo/roteiros/scripts/detectar-cara-de-ia.py` **se** o texto for virar fala (no repositório do canal)

### PASSO 5 · como apresentar (decisão do autor)

| Forma | O que o texto diz | Risco |
|---|---|---|
| **A · critério a critério** | em cada critério, quem se destacou, **só quando a diferença é sustentável pelo indicador**; quando não é, diz que não houve diferença observável | menor: cada afirmação tem indicador e exemplo |
| **B · síntese que nomeia um** | uma frase dizendo quem se saiu melhor, apoiada nos critérios | **o maior**: é a frase que o projeto diz que não faz, e depende de pesar critérios (a IA não escolhe os pesos) |
| **C · só a percepção medida** | o que as pesquisas e análises externas registraram, atribuído | menor, mas depende de existir pesquisa no dia |

A IA entrega o **texto-base das três**, para o autor escolher. ⛔ Ela não escolhe a forma.

### PASSO 6 · o fecho do texto
Termine com *"o que não pode ser afirmado a partir disto"*: quem convenceu quem, quem vai ser eleito, quem governaria melhor, a intenção de qualquer participante.

## O que esta skill não é

Não é `checar-alegacao` (que confere frase contra dado), não é `revisar-checagem` e não substitui as agências de checagem nem os institutos de pesquisa: usa os dois como fonte.
