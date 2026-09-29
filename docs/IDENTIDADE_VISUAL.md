# IDENTIDADE VISUAL — a tela do vídeo checado

Dono das medidas: [`src/checagem/config.py`](../src/checagem/config.py). Este documento explica
**por que** cada medida é o que é. ⛔ Se os dois divergirem, o código ganha e este arquivo se
conserta.

---

## 1. O princípio: a cor antes do texto

O espectador lê a tela em duas camadas, e nessa ordem:

1. **A moldura**, em meio segundo, na visão periférica — "isto aqui é verde ou vermelho?"
2. **A tarja**, em três a cinco segundos — "por quê, e com que fonte?"

Por isso a moldura é a cor do veredito, e por isso ela envolve o quadro inteiro em vez de ser um
selo de canto. É a leitura que sobrevive ao vídeo assistido sem som, em tela pequena, no meio de
um feed.

## 2. As cinco cores

| Veredito | Rótulo na tela | Hex |
|---|---|---|
| `VERDADEIRO` | VERDADEIRO | `#12A150` |
| `IMPRECISO` | IMPRECISO | `#E5A50A` |
| `INSUSTENTAVEL` | SEM COMPROVAÇÃO | `#E8590C` |
| `FALSO` | FALSO | `#D62828` |
| `NAO_CHECAVEL` | NÃO CHECÁVEL | `#6B7280` |

Três decisões dentro disso:

- **`INSUSTENTAVEL` aparece como "SEM COMPROVAÇÃO"** na tela. "Insustentável" é palavra de
  metodologia; "sem comprovação" é o que o espectador entende sem glossário. A chave do dado
  continua sendo `INSUSTENTAVEL` — rótulo é apresentação, chave é contrato.
- **Verde e vermelho são distinguíveis por posição e por texto**, nunca só por cor: o badge sempre
  traz a palavra. Cerca de 8% dos homens têm alguma deficiência de visão de cor; um vídeo de
  checagem que só funciona para quem distingue verde de vermelho falha com eles.
- **O amarelo do `IMPRECISO` é o mesmo da `ressalva`**, inclusive dentro de um card verde. Isso
  faz o "certo, mas" ter cor própria, e é o que impede o verde de virar aplauso.

## 3. A tarja

```
┌──────────────────────────────────────────────────────────────┐
│▌ [ BADGE ]  Falante · 20:07 · A012                           │  ← 46px + 18
│▌ "a citação literal, no máximo duas linhas, entre aspas"     │  ← itálico, #D5DBE5
│▌ O resumo da checagem, com o dado, em no máximo duas linhas  │  ← SemiBold 40px
│▌ Ressalva: quando existe, em amarelo                         │
│▌ FONTES: IBGE · Tesouro Nacional                             │  ← 24px, #A8B0BD
└──────────────────────────────────────────────────────────────┘
   ▲ barra de 14px na cor do veredito
```

| Medida | Valor | Por quê |
|---|---|---|
| margem lateral | 64px | fora da zona de corte de 5% de qualquer plataforma |
| margem inferior | 56px | ⚠️ ainda pode cobrir crédito de emissora, e o PASSO 8 manda conferir |
| altura | calculada | o card cresce com o texto; ⛔ altura fixa corta frase ou deixa buraco |
| raio | 22px | arredondado o bastante para não parecer legenda automática |
| fundo | `#0D1016` a 94% | opaco o suficiente para o texto sobreviver a cenário claro |
| citação | 33px itálico | menor e mais leve que o resumo: é prova, não é a conclusão |
| resumo | 40px SemiBold | a linha que tem que ser lida se só uma for lida |

**A citação vem antes do resumo**, e não depois. O espectador precisa saber **o que foi dito**
antes de ler o julgamento. Inverter isso transforma o card num veredito sobre uma frase que o
espectador ainda não sabe qual é.

## 4. A moldura

10px na cor do veredito, com um degrau interno preto de 2px. O degrau existe porque cenário de
estúdio de TV costuma ser claro e saturado: sem ele, a moldura verde some contra um fundo verde
e a amarela some contra estúdio bege.

## 5. O selo permanente

Canto superior direito, sempre: **CHECAGEM ABERTA** e "metodologia e fontes no repositório".

Ele existe porque cortes deste vídeo vão circular sem a descrição. Um card afirmando que uma frase
é falsa, sem nenhuma indicação de quem checou e onde estão as fontes, é acusação sem lastro — que
é exatamente o comportamento que o projeto quer combater.

## 6. A cartela de abertura

7 segundos, no começo: o que cada cor quer dizer, e a frase "toda checagem tem no mínimo duas
fontes independentes". Sem ela, a moldura verde é decoração. ⛔ Não pule a legenda por achar que
"todo mundo entende": a diferença entre `IMPRECISO` e `SEM COMPROVAÇÃO` é justamente o que
distingue este projeto de um selo de "fake news".

## 7. Tempo de tela

| Constante | Valor | Por quê |
|---|---|---|
| permanência depois da fala | 4,0s | ~40 palavras de card a uma leitura de 200 palavras/min |
| teto | 14,0s | card parado demais vira ruído e some da atenção |
| piso | 3,0s | abaixo disso não dá para ler duas linhas e ver a cor |
| folga entre cards | 0,2s | ⛔ dois cards na tela é defeito, não estilo |

⚠️ Quando o piso não é alcançável porque as falas estão coladas, o PASSO 6 **avisa**. O conserto é
na extração (duas alegações que eram uma), ⛔ nunca encolhendo a permanência global.

### 7.1 Medida de 29/set/2026: o tempo de leitura (registro, sem mudança no pipeline)

O card entra quando a frase começa e fica até 4,0 s depois de ela acabar, então o tempo total na tela é a fala mais a permanência (limitado pelo piso e pelo teto da tabela). É esse tempo total que foi medido abaixo.

Medido no caso publicado (`plano-bloco-contas-publicas.json` contra o `resumo` e a `ressalva` de cada checagem, o texto que o card mostra além da frase e das fontes), pela régua de legenda de 17 caracteres por segundo (a confortável para público geral, com mínimo de 0,83 s por evento): **17 dos 23 cards ficam na tela menos que o tempo de ler resumo e ressalva** (mediana de 185 caracteres, que pedem ~11 s; os cards ficam de 3,0 a 14,0 s). O espectador pode pausar, e a frase citada ajuda a leitura, então isso não é defeito declarado: é uma medida para a próxima decisão sobre o tamanho do resumo ou as constantes de tempo, que é decisão do mantenedor.

A mesma régua veio do editor de vídeos que conta este projeto em vídeo, onde texto que fica menos que o tempo de leitura e cena que troca antes de assentar pesaram na qualidade percebida.

## 8. O que nunca entra na tela

⛔ contagem cumulativa ("3ª informação falsa") · ⛔ adjetivo sobre a pessoa · ⛔ emoji ·
⛔ URL longa · ⛔ travessão · ⛔ animação de entrada que chame mais atenção que o dado ·
⛔ música ou efeito sonoro sobre a fala original.
