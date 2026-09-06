---
name: checar-alegacao
description: PASSO 5 do pipeline. Pega alegacoes/alegacoes.json e produz checagens/checagens.json — um veredito por alegação (VERDADEIRO, IMPRECISO, INSUSTENTAVEL, FALSO ou NAO_CHECAVEL), com no mínimo duas fontes independentes, trecho copiado, URL e data de consulta. Use depois que as alegações estiverem extraídas e validadas. Busca na internet é obrigatória; memória do modelo não vale como fonte, nem para "eu sei que esse número é esse". Difere de extrair-alegacoes, que é o passo anterior e não julga nada.
---

# checar-alegacao — PASSO 5

## O que esta skill entrega

`casos/<slug>/checagens/checagens.json`, válido contra `esquemas/checagens.schema.json`, com
**uma checagem por alegação** — inclusive para as não checáveis.

## 🔴 A regra que vale sobre todas as outras

> **Nenhum número, data ou fato sai da memória do modelo.**
>
> Você pode "lembrar" que o PIB cresceu 7,5% em 2010. Não importa. Ou existe um `trecho` copiado
> de uma fonte com URL e data de consulta, ou o número **não entra no arquivo**. O validador
> avisa quando um número do veredito não aparece em trecho nenhum, e esse aviso é um defeito
> real, não ruído.

Isto não é desconfiança do modelo. É que a promessa do projeto é **rastreabilidade**, e uma
lembrança não é rastreável nem quando está certa.

---

## Antes de checar a primeira alegação

| Leia | Para saber |
|---|---|
| `docs/METODOLOGIA.md` §2 e §3 | os cinco vereditos, a árvore de decisão, a régua do `IMPRECISO`, a hierarquia de fontes |
| `casos/<slug>/alegacoes/alegacoes.json` | inclusive o `o_que_conferir`, que **você escreveu antes de saber a resposta** |
| `docs/FONTES_BRASIL.md` | onde mora cada dado público brasileiro, com o link direto |

---

## O procedimento, alegação por alegação

### 0. Não checável passa direto

`checavel: false` → veredito `NAO_CHECAVEL`, `fontes: []`, e a `explicacao` diz **por que** a
frase não tem valor de verdade ("é uma promessa de mandato futuro", "é um juízo de valor sobre
qualidade, sem critério declarado"). ⛔ "Não deu para checar" não é justificativa: isso é
`INSUSTENTAVEL`.

### 1. Releia o `o_que_conferir`

É o seu critério, escrito antes de você saber o resultado. Se durante a busca você sentir vontade
de mudá-lo, pare: ou apareceu uma razão metodológica de verdade (e ela vai escrita na
`explicacao`), ou você está movendo a trave.

### 2. Vá à fonte primária primeiro

Ordem de busca, sempre:

1. **A base oficial do dado** (IBGE/SIDRA, BCB/SGS, Tesouro Transparente, INEP, DataSUS,
   Dataprev, TCU, Portal da Transparência, inteiro teor da decisão judicial, Diário Oficial).
2. **A instituição de referência** que trata esse dado com método público (IPEA, FGV/IBRE, FBSP,
   Banco Mundial, FMI, OCDE).
3. **A agência de checagem** que já olhou esta frase (Lupa, Aos Fatos, Comprova, Estadão Verifica,
   AFP Checamos, Fato ou Fake) — ótima como confirmação e como atalho para a primária.
4. **A imprensa com apuração própria**, e só como ponteiro para 1 ou 2.

⚠️ **Comece pela agência de checagem quando a frase é famosa** — e depois vá à primária que ela
cita. O que ⛔ não pode é parar na agência: a fonte que entra no arquivo é a primária, e a agência
entra como segunda fonte.

### 3. Teste a independência

Duas matérias que reproduzem o mesmo release são **uma** fonte. Se os dois trechos que você
copiaria são o mesmo parágrafo, procure outra.

### 4. Escolha o veredito pela árvore, não pelo estômago

Rode a árvore de decisão da METODOLOGIA §2.1, nesta ordem, sem pular.

Os quatro erros que mais aparecem:

| Erro | Como se corrige |
|---|---|
| Marcar `FALSO` o que é `IMPRECISO` | as fontes **contradizem** ou só **não batem no número**? |
| Marcar `FALSO` o que é `INSUSTENTAVEL` | você achou prova do contrário, ou não achou prova nenhuma? |
| Marcar `VERDADEIRO` por arredondamento generoso | rode a régua da §2.2 e escreva a `ressalva` |
| Marcar `NAO_CHECAVEL` por preguiça de buscar | o validador reprova: alegação `checavel: true` não recebe `NAO_CHECAVEL` |

### 5. Escreva o `resumo` — é o que vai para a tela

Até 120 caracteres. Ele precisa funcionar sozinho, para quem pegou o vídeo no meio.

| ⛔ Não | ✅ Sim |
|---|---|
| "Ele mentiu sobre a fila do INSS" | "A fila estava em 251 mil no mês da fala, segundo o INSS" |
| "Correto" | "IBGE confirma: 7,5% em 2010, a maior taxa desde 1986" |
| "Tentou esconder que o valor caiu" | "O valor citado é o previsto; o efetivamente pago foi R$ 1,9 bi" |

Três travas do `resumo`:
- fala do **enunciado**, nunca da intenção (⛔ "tentou", "omitiu de propósito", "sabia que");
- **traz o dado**, não o adjetivo;
- ⛔ não usa travessão, e não abrevia fonte a ponto de virar sigla desconhecida.

### 6. Preencha o resto

| Campo | Regra |
|---|---|
| `explicacao` | o raciocínio inteiro: que dado resolve, o que a fonte diz, por que este veredito e **não o vizinho**. Para `FALSO` e `INSUSTENTAVEL`, no mínimo ~120 caracteres, e o validador cobra |
| `numero_dito` / `numero_apurado` | quando há número. Escreva com unidade |
| `data_de_referencia` | obrigatório em `numero`, `serie_historica` e `valor_monetario`. Sem ela, um número certo vira anacronismo |
| `ressalva` | o "certo, mas": arredondamento, recorte, intervalo de confiança, revisão pendente |
| `divergencia_entre_fontes` | ⛔ silenciar divergência é o pior defeito possível aqui. Se IBGE e FGV não batem, isso vai escrito |
| `confianca` | `alta` (N1 direta e inequívoca) · `media` (exige interpretação, ou só N2/N3) · `baixa` (fontes divergem, ou o dado tem revisão pendente) |

🔴 **`confianca: "baixa"` exige `revisao_humana` preenchida.** O validador reprova sem ela. Um
veredito frágil pode ir ao ar, mas só com uma pessoa assinando a decisão.

### 7. Cada fonte carrega a sua própria prova

```json
{
  "nivel": "N1",
  "instituicao": "Instituto Nacional do Seguro Social (INSS)",
  "titulo": "Painel de requerimentos em análise — agosto/2026",
  "url": "https://...",
  "consultada_em": "2026-09-05",
  "trecho": "O estoque de requerimentos em análise encerrou agosto em 251.402 pedidos",
  "prova": "É o número da fila no mês da fala, na definição de 'em análise' usada pelo próprio INSS"
}
```

- `trecho` é **copiado**, não parafraseado. É ele que sustenta o número.
- `prova` diz o que **este** trecho resolve **nesta** alegação. "Confirma o que foi dito" não serve.
- ⛔ `nivel` N5 não existe: rede social, blog, site partidário e memória de modelo não entram.
- ⛔ **Duas entradas com a mesma URL são uma fonte só.** Se você precisa citar dois pedaços da
  mesma base, junte no mesmo `trecho`. O validador reprova a duplicata, e com razão.

### 7.1 Número que saiu de uma conta

Se o número do card não está escrito em fonte nenhuma porque você o **calculou** — subtraiu dois
pontos de uma série, converteu milhões em trilhões, arredondou —, ele vai em `derivacoes`:

```json
"derivacoes": [
  { "valor": "10,25 pontos percentuais",
    "de": "81.93 menos 71.68",
    "como": "subtração dos dois pontos da série de dívida em % do PIB" }
]
```

O validador confere que **cada parcela de `de` aparece em algum `trecho`**. 🔑 A conta fica escrita
e qualquer pessoa refaz. ⛔ Isto não é uma saída para número que você não achou: número sem fonte é
`INSUSTENTAVEL`, não derivação.

---

## O anacronismo, que derruba checagem boa

O veredito é sobre **o que valia na data da fala**. Se a série foi revista depois, ou se o número
mudou no mês seguinte, isso não torna a frase falsa: vai na `ressalva`, com as duas datas.

> ✅ "251 mil era o número de agosto, mês da fala. Em outubro, o INSS informou 268 mil."
> ⛔ "Falso: hoje a fila está em 268 mil."

---

## Antes de entregar

- [ ] Toda alegação tem exatamente uma checagem, com o mesmo `id`
- [ ] Todo veredito não `NAO_CHECAVEL` tem ≥ 2 fontes, com URLs diferentes
- [ ] Alegação numérica tem ≥ 1 fonte N1 ou N2
- [ ] Nenhum número no `resumo` ou em `numero_apurado` que não esteja num `trecho`
- [ ] Todo `trecho` é copiado, e toda `prova` diz o que ele resolve **aqui**
- [ ] `data_de_referencia` preenchida onde o esquema exige
- [ ] Divergência entre fontes está escrita, não escondida
- [ ] Nenhum `resumo` fala de intenção
- [ ] `python -m checagem validar <slug>` sai com 0

**Próximo passo:** `skills/fechar-caso.md`.
