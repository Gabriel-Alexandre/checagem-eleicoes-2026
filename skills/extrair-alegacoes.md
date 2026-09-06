---
name: extrair-alegacoes
description: PASSO 4 do pipeline. Varre a transcrição de um caso, do começo ao fim, e escreve alegacoes/alegacoes.json — a lista de tudo que foi afirmado como fato, por qualquer pessoa da mesa, com tempo, falante e citação literal. Use sempre que houver uma transcrição pronta e revisada de uma sabatina, debate ou entrevista e o próximo passo for descobrir o que ali é checável. NUNCA emite veredito e NUNCA busca na internet, de propósito: quem já sabe a resposta escolhe as perguntas. Difere de checar-alegacao, que é o passo seguinte e é quem julga.
---

# extrair-alegacoes — PASSO 4

## O que esta skill entrega

Um arquivo `casos/<slug>/alegacoes/alegacoes.json` (ou `alegacoes-<recorte>.json`) válido contra
`esquemas/alegacoes.schema.json`, com **todas** as afirmações de fato do trecho varrido.

## 🔴 As três travas que definem este passo

1. **⛔ Nenhum veredito.** O arquivo de alegações não tem campo de veredito e não pode ganhar um.
2. **⛔ Nenhuma busca na internet.** Enquanto esta skill roda, a internet está fechada. Saber a
   resposta antes de escolher a pergunta é como a checagem vira militância: você começa a "não
   ver" as frases que dariam certo.
3. **Varredura, não pesca.** Você lê a transcrição **inteira, em ordem**, do primeiro ao último
   segmento do intervalo declarado em `cobertura`. ⛔ Não pule para o trecho polêmico.

> Se você já sabe que uma frase é falsa quando a está extraindo, isso não muda nada aqui: ela entra
> com os mesmos campos que todas as outras, e o julgamento é do passo 5.

---

## Antes de escrever a primeira linha

| Leia | Para saber |
|---|---|
| `docs/METODOLOGIA.md` §4 | o que vira alegação e o que não vira |
| `casos/<slug>/CASO.json` | os nomes exatos e o papel de cada falante |
| `casos/<slug>/transcricao/transcricao.txt` | a peça, com tempo na margem |
| `esquemas/alegacoes.schema.json` | os campos e os valores aceitos |

⚠️ **O nome do falante é copiado do `CASO.json`, caractere a caractere.** O validador recusa
qualquer outro, e com razão: nome escrito de duas formas vira duas pessoas na contagem.

---

## O procedimento, segmento a segmento

Para **cada** segmento da transcrição, na ordem:

### 1. A frase afirma algo sobre o mundo?

Passe pelo filtro da METODOLOGIA §4.1 e §4.2. Na dúvida, três perguntas:

- Existe, em algum lugar, um registro que confirmaria ou desmentiria isto? → entra
- Se duas pessoas honestas discordarem, elas discordam sobre **um fato** ou sobre **um valor**? →
  fato entra, valor não
- A frase está no passado ou no presente? Futuro é promessa, e promessa não entra como checável

### 2. A pergunta do jornalista também conta

> 🔴 Esta é a regra que mais gente esquece, e é a que sustenta a legitimidade do projeto.

"Por que o senhor cortou 30% do orçamento?" **afirma** um corte de 30%. Isso é uma alegação do
entrevistador, com `papel: "entrevistador"`, e passa pelo mesmo funil. Um projeto que só extrai
alegação de um lado da mesa não é checagem.

Ao final, se a peça tem 10 ou mais alegações e nenhuma é de entrevistador, **volte e releia**: ou
a mesa não afirmou nada (raro numa sabatina) ou a varredura foi enviesada. O validador avisa.

### 3. Fatie

Uma alegação = uma coisa checável (METODOLOGIA §4.3).

> *"Devolvemos R$ 3,5 bilhões aos aposentados e a fila do INSS caiu para 251 mil pessoas."*

São **duas** alegações: o valor devolvido e o tamanho da fila. Fontes diferentes, vereditos
possivelmente diferentes. Elas podem compartilhar o mesmo `inicio_s`/`fim_s`.

### 4. Copie a citação, não a reescreva

`frase` é **literal**. Da transcrição, sem consertar concordância, sem tirar hesitação que muda o
sentido, sem juntar duas falas separadas. Corte interno se marca com `[...]`.

> 🔴 O validador confere isto: ele normaliza a transcrição e procura a citação dentro dela. Uma
> citação parafraseada **reprova o caso**. Não é rigor decorativo — é a diferença entre um vídeo
> de checagem e um vídeo que inventa aspas.

Se a frase literal for longa demais para caber num card, **não corte na extração**: o campo
`afirmacao` é onde você escreve a proposição enxuta. A `frase` continua sendo a prova.

### 5. Escreva a `afirmacao`

A proposição isolada, em uma linha, no formato "X é/foi Y". É isto que o passo 5 vai checar.

| `frase` (literal) | `afirmacao` (proposição) |
|---|---|
| "nós já devolvemos, olha, mais de três bilhões e meio pros aposentado" | O governo federal já devolveu mais de R$ 3,5 bilhões a aposentados lesados |
| "a fila caiu, hoje ela está em duzentos e cinquenta e um mil" | A fila de análise do INSS está em 251 mil pedidos |

### 6. Classifique `tipo` e `checavel`

`checavel: false` só com `tipo` em `opiniao`, `promessa`, `previsao`, `juizo_de_valor`,
`hipotese`. O validador cruza os dois campos e reprova a incoerência.

⚠️ **Não abuse do não checável.** "Esse foi o melhor programa social da história" tem um juízo
(`melhor`) e pode ter um fato embutido (a existência e o alcance do programa). Extraia o fato como
alegação separada e deixe o juízo de fora — não classifique a frase inteira como opinião para não
ter trabalho.

### 7. Escreva `o_que_conferir` ANTES de qualquer busca

Duas ou três linhas: **que dado, de que fonte, de que período** resolveria esta alegação.

```json
"o_que_conferir": [
  "série do estoque de requerimentos do INSS em análise, Dataprev/INSS, no mês da fala",
  "qual definição de 'fila' a fonte usa: só o que passou do prazo legal, ou tudo em análise"
]
```

🔑 **Por que antes:** escrever o critério antes de ver o resultado é o que impede o passo 5 de
aceitar a primeira fonte que confirma o que se quer. Quando o critério já está escrito, uma fonte
que responde outra pergunta fica visivelmente fora do lugar.

---

## Densidade: quantas alegações são esperadas

Régua medida em sabatina de TV, para conferir se a varredura foi rasa:

| Peça | Faixa esperada |
|---|---|
| 5 min de sabatina | 8 a 18 alegações |
| 5 min de **bloco escolhido por densidade** | pode passar de 20 |
| 45 min de sabatina | 60 a 140 alegações |

⚠️ Muito **abaixo** da faixa quer dizer varredura rasa.

⚠️ Muito **acima** é um sinal, não um veredito: pode ser que você esteja fatiando a mesma coisa
duas vezes, ou extraindo cortesia como fato — mas também pode ser que o trecho seja mesmo denso.
O bloco de contas públicas do caso `2026-08-27-sabatina-lula-globo` deu **23 alegações em 4min52s**,
e a conferência mostrou que o corte estava certo: cada uma se resolve numa fonte diferente.

🔑 **O teste que separa os dois casos:** pegue duas alegações vizinhas e pergunte se elas se
resolvem no **mesmo** dado. Se sim, era uma. Se não, eram duas.

> 🔴 **Densidade alta cobra preço no vídeo, não na extração.** Muitas alegações coladas fazem as
> cartelas entrarem em fila, e uma delas pode aparecer bem depois da frase que cita. O PASSO 6
> avisa quando isso passa do teto. ⛔ O conserto é rever se houve fatiamento a mais, **nunca**
> apagar alegação para o vídeo ficar mais bonito.

---

## Formato de saída

```json
{
  "caso": "2026-08-27-sabatina-lula-globo",
  "gerado_em": "2026-09-05",
  "fonte_transcricao": "transcricao/transcricao.json",
  "recorte": "bloco-economia",
  "cobertura": { "inicio_s": 1200.0, "fim_s": 1500.0 },
  "alegacoes": [
    {
      "id": "A001",
      "inicio_s": 1207.4,
      "fim_s": 1213.9,
      "falante": "Lula",
      "papel": "entrevistado",
      "frase": "nós devolvemos três bilhões e meio de reais pros aposentados",
      "afirmacao": "O governo federal devolveu R$ 3,5 bilhões a aposentados lesados por descontos indevidos",
      "tipo": "valor_monetario",
      "checavel": true,
      "assunto": "inss",
      "contexto": "Resposta sobre a fraude nos descontos associativos do INSS",
      "o_que_conferir": [
        "valor total ressarcido, no portal do INSS ou da CGU, na data da fala",
        "se o valor citado é o pago ou o previsto"
      ]
    }
  ]
}
```

- `id` é `A001`, `A002`… em **ordem cronológica de fala**. O validador reprova fora de ordem.
- `inicio_s` e `fim_s` são o tempo **na peça inteira**, mesmo quando você está lendo um recorte.
  A transcrição já vem com o deslocamento aplicado — copie o que está lá.

---

## Antes de entregar

- [ ] Varri o intervalo inteiro declarado em `cobertura`, em ordem, sem pular
- [ ] Nenhuma alegação tem veredito, e eu não busquei nada na internet
- [ ] Toda `frase` é literal e existe na transcrição
- [ ] Todo `falante` está escrito como no `CASO.json`
- [ ] Extraí alegações **de todos os papéis** que afirmaram fato, não só do entrevistado
- [ ] `checavel` e `tipo` são coerentes
- [ ] Todo item tem `o_que_conferir` escrito
- [ ] `python -m checagem validar <slug>` passa a parte de alegações

**Próximo passo:** `skills/checar-alegacao.md`.
