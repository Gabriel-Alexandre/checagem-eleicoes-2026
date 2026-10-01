# DEBATES: o braço do projeto para peças longas com vários candidatos

**Criado:** 1º/out/2026, a pedido do autor, no dia do debate presidencial da TV Globo. Palavras dele: *"esse projeto não vai substituir o que já existe, mas sim vai ser um novo braço do projeto"*, *"dessa vez a validação deve ser para todo o debate (mas não precisa editar o vídeo para tudo, rode apenas a validação para obter as métricas e classificações)"*.

> ⚠️ Este arquivo é **operação**: diz como rodar o braço de debate. A doutrina (vereditos, fontes, o que o projeto não conclui) continua em [`METODOLOGIA.md`](METODOLOGIA.md), e **ela ganha** de qualquer coisa aqui.

---

## 1. O que muda em relação à sabatina

| | Sabatina (casos 1 a 3) | Debate |
|---|---|---|
| Peça | uma pessoa respondendo a dois entrevistadores | quatro candidatos, um mediador, tréplicas, perguntas de candidato para candidato, cadeira vazia |
| O que se checa | **um bloco**, escolhido por tema, antes de qualquer checagem | **a peça inteira** (recorte `debate-completo`, sem vídeo renderizado) |
| O que vira vídeo | o bloco inteiro, com a cartela de cada alegação | **alguns cortes** (recortes de vídeo que **herdam** as checagens da peça inteira) |
| Volume | 20 a 25 alegações | 150 a 300 (ver `skills/extrair-alegacoes.md`, densidade) |
| Resultado | contagem do trecho | métricas gerais, **por candidato** e por assunto, com o denominador sempre à vista |
| Camada extra | nenhuma | **considerações da IA** sobre o debate, num arquivo separado ([§6](#6-as-considerações-da-ia-uma-camada-separada)) |

O que **não** muda: nenhum fato sai da memória do modelo, duas fontes independentes, a mesma régua para todos, a extração acontece de internet fechada e antes de qualquer busca, a revisão adversarial roda em passada separada, e o validador é a porta.

## 2. O pipeline do debate, comando a comando

```bash
SLUG=2026-10-01-debate-presidencial-globo      # o caso já foi aberto (ferramentas/novo-caso-debate.py)
export PATH="$HOME/scoop/shims:$PATH"

# PASSO 0 a 3: a peça
#   preencher procedencia no CASO.json (como o arquivo foi obtido, se é íntegra) ANTES de transcrever
python -m checagem midia $SLUG registrar
python -m checagem midia $SLUG audio
python -m checagem transcrever $SLUG                       # ~1 h de CPU para 2 h de vídeo (whisper.cpp local)
python ferramentas/comparar-transcricao.py $SLUG ref.txt --so-relevantes   # se houver transcrição publicada
python ferramentas/corrigir-transcricao.py $SLUG           # correção por script, nunca em silêncio
#   escrever transcricao/falantes.json (turnos) -> ver §3
python -m checagem falantes $SLUG

# PASSO 4: extração em lotes (internet FECHADA)
python ferramentas/lotes-de-debate.py extracao-dividir $SLUG --minutos 8
#   um agente por lote, seguindo skills/extrair-alegacoes.md, lendo casos/$SLUG/lotes/extracao/lote-NN.txt
python ferramentas/lotes-de-debate.py extracao-juntar  $SLUG --recorte debate-completo

# PASSO 5: checagem em lotes
python ferramentas/lotes-de-debate.py checagem-dividir $SLUG --recorte debate-completo --tamanho 10
#   um agente por pedido, seguindo skills/checar-alegacao.md
python ferramentas/lotes-de-debate.py checagem-juntar  $SLUG --recorte debate-completo
python ferramentas/capturar-fontes.py $SLUG                # baixa e assina as fontes
python ferramentas/conferir-trechos.py $SLUG --recorte debate-completo --capturas capturas/$SLUG

# revisão adversarial, em passada separada, sobre o conjunto (skills/revisar-checagem.md)
python ferramentas/registrar-revisao.py $SLUG --recorte debate-completo --ia --notas revisao.json

# a porta e as métricas
python -m checagem validar  $SLUG --recorte debate-completo
python -m checagem metricas $SLUG --recorte debate-completo

# só para os cortes que viram vídeo (§5)
python -m checagem midia $SLUG recortar corte-01 --inicio S --duracao S --motivo "..." --cortar-faixas
python ferramentas/derivar-recorte.py $SLUG --de debate-completo --para corte-01 --inicio S --fim S
python -m checagem overlay $SLUG --recorte corte-01 && python -m checagem renderizar $SLUG --recorte corte-01
python -m checagem validar $SLUG --recorte corte-01
```

`python ferramentas/lotes-de-debate.py status $SLUG` mostra o que já voltou e o que falta.

### 2.1 Por que lotes, e o que impede os lotes de estragar a trava

Uma extração de 2 h numa passada só estoura o contexto de qualquer agente e fica rasa no fim. Os lotes (~8 min, cortados **em virada de turno**, nunca no meio de uma resposta) rodam em paralelo. A junção é onde a trava mora:

- cada lote **declara a janela que varreu** (`cobertura`) e o script **recusa** lote com cobertura diferente da pedida, alegação fora da janela e buraco entre janelas;
- ⛔ **veredito na extração derruba a junção** (o PASSO 4 não tem veredito);
- a duplicata exata da borda é descartada, os ids são **renumerados** `A001...` na ordem da fala, e o mapa `lote → id final` fica em `alegacoes/lotes/mapa-de-ids.json`;
- a junção da checagem acusa **alegação sem checagem** e **id inventado**.

⚠️ **O que os lotes não resolvem, e a revisão resolve:** dois agentes podem usar réguas ligeiramente diferentes para "isto é fato". Por isso a revisão adversarial é **uma só, sobre o conjunto, na ordem cronológica**, por quem não escreveu nenhuma checagem, e a pergunta fixa dela é: *"alegação parecida, de candidatos diferentes, recebeu o mesmo veredito?"* (§4).

## 3. Quem falou o quê, num debate

O PASSO 3 é manual de propósito ([`passo3_falantes.py`](../src/checagem/passo3_falantes.py)): atribuir frase à pessoa errada é o pior erro do projeto. No debate o risco é maior:

- **Mais de dois rostos.** O whisper não separa vozes. A atribuição é por **turno lido na transcrição, conferido no vídeo** (a emissora mostra o nome do candidato falando e muda de plano).
- **Mediador × candidato.** A fala do mediador (regras, tempo, apresentação de tema) normalmente não afirma fato; a que afirma (ex.: contexto da pergunta) entra com `papel: entrevistador`.
- **Pergunta de candidato para candidato** afirma fato com frequência, e **entra**, com o nome de quem perguntou. É a trava de simetria da pergunta do jornalista, aplicada ao debatedor.
- **Pergunta ao ausente (cadeira vazia).** O candidato que pergunta é o falante. ⛔ O ausente **não é falante** e nada que alguém diga sobre ele vira fala dele. Alegação sobre o ausente se checa como qualquer outra.
- **Sobreposição de fala.** Quando dois falam juntos e a transcrição mistura, a frase **não** vira alegação (vai para `exclusoes` com o motivo). É a regra da "frase que ficou de fora".
- **Réplica e tréplica.** Cada fala continua sendo do candidato que a disse, mesmo respondendo a outro; o `contexto` da alegação registra a quem ele respondia.
- **Direito de resposta e intervalos.** Vinheta e comercial não têm falante: ficam fora dos turnos (o PASSO 3 avisa de segmento sem dono, e isso é esperado nelas).

## 4. As métricas, e como não virar placar

`python -m checagem metricas <slug> --recorte debate-completo` escreve `casos/<slug>/metricas/metricas-debate-completo.json` e `METRICAS_debate-completo.md`.

| Sai | Como se lê |
|---|---|
| **Geral** | alegações, checáveis, não checáveis, cada veredito em número e em % dos checáveis, por papel |
| **Por falante** | tempo de fala, alegações, checáveis, cada veredito, % dos checáveis, **alegações por minuto de fala**, assuntos e tipos. ⛔ **Na ordem da primeira fala, nunca por resultado** |
| **Por assunto** | quem falou do quê, com a distribuição de vereditos |
| **Avisos automáticos** | candidatos com número de checáveis muito diferente, tempo de fala diferente, candidato sem alegação checável, checagem sem revisão |
| **Ressalvas fixas** | as quatro de [`etica-e-risco.mdc`](../.cursor/rules/etica-e-risco.mdc) §2 e §3, em todo relatório |

🔴 **O que as métricas nunca viram** (regra do projeto, inalterada): nota, índice, placar, "quem mentiu mais", ranking por falsidade, soma de `FALSO` com `IMPRECISO`.

🔑 **Duas leituras de assimetria que a fala do vídeo precisa carregar**, porque `etica-e-risco` §3 manda: (1) tempo de fala e quantidade de afirmação checável **não são iguais** entre candidatos; (2) assunto com fonte pública boa (economia) rende mais `VERDADEIRO`/`IMPRECISO` do que promessa, que é `NAO_CHECAVEL` e fica fora do percentual.

### 4.1 A pergunta fixa da revisão adversarial no debate

Além do roteiro de `skills/revisar-checagem.md`, a passada olha o conjunto em **pares**: para cada par de alegações **do mesmo tipo e do mesmo assunto, de candidatos diferentes**, o mesmo critério foi aplicado? (mesma tolerância de arredondamento, mesmo tratamento de "nominal × real", mesma exigência de data de referência.) Divergência vai para o `CORRECOES.md`, com o antes e o depois, **antes** de as métricas serem fechadas.

## 5. Quais trechos viram vídeo (critério declarado ANTES dos vereditos)

[`etica-e-risco`](../.cursor/rules/etica-e-risco.mdc) §1: *a escolha do recorte não pode ser feita pelo resultado.* No debate, onde o vídeo mostra **cortes**, isso vira regra operacional:

1. **Declare o critério antes de ver o veredito de qualquer alegação** e grave em `casos/<slug>/recortes/SELECAO_DE_CORTES.md` (com data e hora do commit).
2. O critério usa só o que existe **depois da extração e antes da checagem**: estrutura do debate (um corte por bloco, abertura, o confronto direto entre candidatos, a pergunta ao ausente, as considerações finais) e **densidade de alegações checáveis** (número de alegações por minuto, que sai do PASSO 4).
3. **Simetria:** o mesmo número de cortes por candidato (±1) e duração parecida (±20%). Os números saem de `metricas` de **tempo de fala**, nunca de veredito.
4. Cada corte é **contínuo** (o script de derivação recusa alegação cortada na borda) e carrega o card **com o crédito da emissora**.
5. Depois de escolhidos os cortes, a ordem em que aparecem **no vídeo** é decisão editorial dele; o repositório só registra.

⛔ Cortes escolhidos "porque tem um FALSO" ou "porque o candidato X foi mal ali" não passam. Se o autor quiser incluir um trecho por ser polêmico, o motivo dele vai escrito no `--motivo` do recorte, e o relatório mostra que a regra foi quebrada.

## 6. As considerações da IA: uma camada separada

O autor quer que, no fim do vídeo, a IA faça **considerações gerais sobre o debate**, buscando imparcialidade, podendo usar pesquisas e o que achar na internet. Isso **não é checagem** e **não mora** nos arquivos da checagem: [`METODOLOGIA.md`](METODOLOGIA.md) §8 continua valendo (o checador não classifica candidato). É uma **camada editorial pedida pelo autor**, com protocolo próprio ([`skills/consideracoes-do-debate.md`](../skills/consideracoes-do-debate.md)) e critérios pré-registrados em [`casos/2026-10-01-debate-presidencial-globo/consideracoes/CRITERIOS.md`](../casos/2026-10-01-debate-presidencial-globo/consideracoes/CRITERIOS.md), **commitados antes de o debate acontecer**.

Em uma frase: **os critérios nascem antes do debate, a análise roda duas vezes (uma com os nomes, outra anonimizada), as pesquisas e comentários externos entram atribuídos e com a data, e o texto declara o que a IA não pode afirmar.**

## 7. Riscos que são decisão do autor (não da IA)

| Risco | Fato | O que o repositório faz |
|---|---|---|
| 🔴 **Prazo da resolução do TSE sobre IA** | A resolução de março/2026 veda publicar, republicar ou impulsionar **novos conteúdos sintéticos produzidos ou alterados por IA** num intervalo que, nas duas leituras que a imprensa traz, começa em 1º/out e termina em 5/out (72 h antes do pleito de 4/out até 24 h depois). O texto exato, o alcance (só conteúdo com voz e imagem de candidato? só propaganda eleitoral?) e se checagem jornalística entra **não foram confirmados em fonte primária** e as fontes divergem até no número da resolução (23.748 ou 23.755) | **Registra e calcula; não decide.** Ler o texto no site do TSE e, se o autor quiser segurança, consultar quem entende de direito eleitoral antes de publicar |
| 🔴 **"IA diz quem se saiu melhor"** | A mesma resolução proíbe que **provedores de sistemas de IA** ranqueiem ou recomendem candidatos; a imprensa descreve o alvo como o provedor, não o usuário que publica uma análise. É a frase de maior risco do vídeo, e a mais próxima do que o projeto diz que não faz | A camada de considerações tem critérios observáveis, não escolhe voto, e a forma final (apontar quem se destacou em cada critério, ou nomear um) é **decisão dele** (`skills/consideracoes-do-debate.md` §5) |
| **Rotulagem** | A resolução exige aviso claro em conteúdo de propaganda criado ou alterado por IA. Checagem não é propaganda, mas o vídeo **diz** que a IA fez, no primeiro segundo | O trailer já diz; a descrição e um selo na tela repetem |
| **Direito de resposta e contestação** | Qualquer pessoa citada pode contestar com fonte (`etica-e-risco` §6) | Issue no repositório; correção vai para `CORRECOES.md`; com o pleito perto, o prazo de correção é curto: ver `etica-e-risco` §5 |
| **Trecho da emissora** | Cortes de debate citam a emissora (Lei 9.610/98, art. 46, III: citar indicando autor e origem). O **tamanho** do trecho pesa mais do que a citação em si | Crédito na tela e na descrição, card por cima, cortes curtos; o tamanho total é decisão dele |

## 8. Falhas que este braço já prevê (leia antes de rodar)

| Se acontecer | Faça |
|---|---|
| Transcrição troca nome próprio, número ou ano (o `1922` do caso Flávio) | `ferramentas/corrigir-transcricao.py` com segunda passada; nunca em silêncio |
| Dois lotes dão veredito diferente para alegação parecida | revisão em pares (§4.1) |
| Candidato com muito menos alegações checáveis | **mostre**, não esconda: o aviso automático das métricas e a fala do vídeo carregam isso |
| Fato em apuração (processo sem trânsito, inquérito) | `INSUSTENTAVEL` ou `NAO_CHECAVEL`, nunca `FALSO` (`etica-e-risco` §5) |
| Dado que só existe depois do debate (pesquisa nova, número divulgado na própria noite) | a data da fonte é a **data da fala**; anacronismo derruba checagem boa (`skills/checar-alegacao.md`) |
| Mais de 999 alegações | divida a peça em dois recortes (`A###` vai até `A999`) |
