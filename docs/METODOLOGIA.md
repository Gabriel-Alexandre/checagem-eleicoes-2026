# METODOLOGIA — como uma frase vira um veredito

**Dono do fato:** este arquivo. Qualquer outro documento, skill ou script que contradiga o que está aqui está errado, e o conserto é no outro arquivo.

Este é o documento mais importante do repositório. Ele existe porque a promessa do projeto não é "a IA disse que é falso": é **qualquer pessoa conseguir refazer o caminho e chegar ao mesmo veredito**. Se um veredito não puder ser refeito por um terceiro a partir do que está escrito aqui e dos arquivos de evidência, ele não é um veredito, é uma opinião com cara de dado.

---

## 1. O princípio, em quatro frases

1. **A afirmação é a unidade de trabalho**, não a pessoa e não o trecho. Cada asserção verificável vira uma linha própria, com o tempo exato em que foi dita.
2. **Nenhum veredito nasce da memória do modelo.** Todo número, data, valor e citação tem que ter uma URL consultada, com data de consulta e trecho copiado.
3. **Duas fontes independentes, no mínimo**, para qualquer veredito que não seja `NAO_CHECAVEL`. Independentes quer dizer que uma não é reprodução da outra.
4. **A régua é a mesma para todo mundo.** Entrevistado e entrevistadores passam pelo mesmo funil. Um projeto que só checa um lado da mesa não é checagem, é campanha.

---

## 2. Os cinco vereditos

O espectador precisa entender a cor em meio segundo. Por isso são cinco, e não quinze.

| Veredito | Cor | Hex | O que significa | Exige fonte? |
|---|---|---|---|---|
| `VERDADEIRO` | verde | `#12A150` | O que foi dito confere com as fontes primárias, dentro da margem declarada | ✅ 2+ |
| `IMPRECISO` | amarelo | `#E5A50A` | A essência está certa, mas o número, a data ou o recorte estão materialmente errados | ✅ 2+ |
| `INSUSTENTAVEL` | laranja | `#E8590C` | A afirmação foi feita como fato, e as fontes disponíveis **não a sustentam** — sem que se prove o contrário | ✅ 2+ |
| `FALSO` | vermelho | `#D62828` | As fontes contradizem diretamente o que foi dito | ✅ 2+ |
| `NAO_CHECAVEL` | cinza | `#6B7280` | Opinião, promessa, previsão, juízo de valor, intenção, pergunta retórica | ❌ |

> 🔴 **`INSUSTENTAVEL` não é meio-termo covarde.** Ele existe porque "não achei prova de que é verdade" e "achei prova de que é mentira" são coisas diferentes, e tratar as duas como `FALSO` é o erro mais comum de checagem amadora. Quando as fontes contradizem, é `FALSO`. Quando elas simplesmente não sustentam, é `INSUSTENTAVEL`, e o texto do card diz **o que faltou**.

> ⚠️ **`NAO_CHECAVEL` não é "não deu tempo".** É uma classificação positiva: a frase, por natureza, não tem valor de verdade hoje. "Vou dobrar o investimento no ano que vem" é `NAO_CHECAVEL`. "Dobrei o investimento no ano passado" **nunca** é `NAO_CHECAVEL`.

### 2.1 A árvore de decisão

```
A frase afirma algo sobre o mundo que pode ser conferido contra um registro?
├── NÃO  → NAO_CHECAVEL   (opinião · promessa · previsão · valor · intenção · pergunta)
└── SIM
    ├── Achei 2+ fontes independentes qualificadas?
    │   ├── NÃO, e a busca foi exaustiva → INSUSTENTAVEL
    │   └── SIM
    │       ├── As fontes confirmam o essencial E o número/recorte → VERDADEIRO
    │       ├── Confirmam o essencial, mas o número/recorte está errado → IMPRECISO
    │       └── Contradizem o essencial → FALSO
```

### 2.2 A régua do `IMPRECISO` (para não virar gosto pessoal)

Um número só é rebaixado de `VERDADEIRO` para `IMPRECISO` quando o desvio **muda a leitura**:

| Situação | Veredito |
|---|---|
| Arredondamento que não muda a ordem de grandeza (R$ 3,5 bi contra R$ 3,47 bi) | `VERDADEIRO`, com a ressalva escrita no card |
| Desvio ≥ 10% no valor, ou ≥ 20% quando o valor é uma estimativa oficial com intervalo | `IMPRECISO` |
| Número certo, período errado (atribui a um governo o que aconteceu em outro) | `IMPRECISO` |
| Número certo, unidade errada (milhão por bilhão, nominal por real) | `IMPRECISO` |
| Recorte escolhido que inverte a tendência do dado completo | `IMPRECISO` |
| Número que não existe em fonte nenhuma | `INSUSTENTAVEL` |
| Número que existe e é outro, com sentido oposto | `FALSO` |

⛔ **Nunca** classifique como `FALSO` uma frase que está certa no fato e errada no ornamento. O card diz "certo, com ressalva". Confundir os dois destrói a credibilidade da série inteira.

---

## 3. Hierarquia de fontes

| Nível | O que é | Exemplos | Vale sozinha? |
|---|---|---|---|
| **N1 — Primária oficial** | o registro do próprio fato | IBGE (SIDRA), Banco Central (SGS), Tesouro Transparente, TCU, STF/STJ (inteiro teor), INEP, DataSUS, Dataprev/INSS, Portal da Transparência, Diário Oficial da União, Painel de Obras do PAC | ✅ conta como 1 fonte forte |
| **N2 — Institucional de referência** | quem trata o dado primário com método público | IPEA, FGV/IBRE, Banco Mundial, FMI, OCDE, Fiocruz, Fórum Brasileiro de Segurança Pública, Observatório do Clima | ✅ |
| **N3 — Checagem profissional** | agências signatárias do IFCN | Lupa, Aos Fatos, Comprova, Estadão Verifica, AFP Checamos, Fato ou Fake | ✅ se citarem a primária |
| **N4 — Imprensa com apuração própria** | matéria que apurou, não que reproduziu | Folha, Estadão, O Globo, Valor, Reuters, AP, Poder360, Agência Brasil | ⚠️ só como ponteiro para a N1/N2 |
| **N5 — ⛔ não entra** | rede social, blog, site partidário, canal de opinião, agregador sem fonte, **memória do modelo de IA** | — | ❌ |

### 3.1 As regras duras

1. **Todo veredito não-`NAO_CHECAVEL` precisa de ≥ 2 fontes**, sendo **pelo menos 1 de N1 ou N2** quando a afirmação envolve número, série histórica, valor monetário ou ranking.
2. **Duas fontes N3/N4 só bastam** quando ambas citam explicitamente a mesma primária e essa primária foi conferida (aí ela vira a fonte N1, e as outras duas viram apoio).
3. **Independência:** duas matérias que reproduzem o mesmo release contam como **uma**. Se as duas URLs têm o mesmo parágrafo, é uma fonte.
4. **Data de consulta obrigatória.** Série histórica é revista; o que era verdade na consulta pode deixar de ser. O card cita o dado, e o arquivo de checagem cita a data.
5. **Trecho copiado obrigatório.** Cada fonte guarda o `trecho` que prova o ponto. "A fonte diz que sim" não é evidência; é confiança.
6. ⛔ **Nunca** escreva um número que não esteja dentro de um `trecho` de alguma fonte do arquivo.

   **A exceção declarada, e só ela: o número derivado.** "A dívida subiu 10,25 pontos" não está escrito em fonte nenhuma — ele sai de `81,93 − 71,68`, e os dois pontos da conta estão. O mesmo vale para conversão de unidade (R$ milhões para R$ trilhões) e arredondamento. Nesse caso o número entra no campo `derivacoes`, com **o valor, as parcelas e a conta**:

   ```json
   "derivacoes": [
     { "valor": "10,25 pontos percentuais",
       "de": "81.93 menos 71.68",
       "como": "subtração dos dois pontos da série de dívida em % do PIB" }
   ]
   ```

   O validador confere que **todas as parcelas de `de` aparecem em algum `trecho`** e só então aceita o valor. 🔑 A diferença entre isto e uma exceção genérica é que aqui a conta fica escrita e qualquer pessoa refaz. ⛔ Não use `derivacoes` para dar passagem a número que você não achou: isso é `INSUSTENTAVEL`.

   ⚠️ **O que a regra 6 não pega:** ano. `1986` em "a maior taxa desde 1986" passa pelo validador porque ano é tratado como data, não como quantidade. Isso é decisão consciente para o aviso não virar ruído, e o preço é que **ano errado só cai numa leitura que não seja o validador**. Aconteceu na primeira rodada deste repositório, e está registrado em `casos/2026-08-27-sabatina-lula-globo/CORRECOES.md`. 🔧 **Quem pegou foi uma segunda leitura da própria IA, não uma pessoa** (até 11/set este parágrafo dizia "revisão humana", e estava errado). É exatamente por isso que a revisão humana segue obrigatória antes de publicar: uma releitura da mesma IA pegou este caso, e nada garante que pegue o próximo.

---

## 4. O que vira alegação, e o que não vira

### 4.1 Entra

- Número, percentual, valor, ranking, posição, data, prazo.
- Afirmação sobre o passado ("fizemos", "foi aprovado", "caiu", "cresceu").
- Atribuição a terceiro ("o TCU disse", "a pesquisa mostra").
- Comparação entre períodos, governos ou países.
- Descrição de norma vigente ("a lei determina", "a Constituição proíbe").
- **Pergunta que carrega um fato embutido.** A pergunta do jornalista "por que o senhor cortou o orçamento em 30%?" afirma um corte de 30%, e essa afirmação é checável.

### 4.2 Não entra

- Opinião declarada como opinião ("eu acho", "na minha avaliação").
- Promessa e plano ("vou fazer", "no meu governo será").
- Juízo de valor ("foi o melhor programa da história") — a **parte factual** dentro dele pode virar alegação separada, o juízo não.
- Hipótese e cenário ("se o Congresso aprovar").
- Cortesia, transição, ironia sem conteúdo factual.

### 4.3 A regra de fatiar

> 🔴 **Uma alegação = uma coisa checável.** Se uma frase tem dois números que se checam em fontes diferentes, são **duas** alegações, com o mesmo intervalo de tempo. Se a frase tem um fato e um juízo colado, o fato vira alegação e o juízo é descartado.

E **a frase citada é literal**. O campo `frase` copia o que a transcrição registrou, sem consertar gramática, sem cortar hesitação relevante, sem juntar frases separadas. Corte interno se marca com `[...]`.

---

## 5. Enquadramento honesto

Estes são os erros que transformam checagem em militância. Cada um já derrubou um projeto sério.

| Armadilha | O antídoto no processo |
|---|---|
| **Checar só um lado** | o funil de extração roda igual para entrevistado e entrevistadores, e o relatório publica a contagem por falante |
| **Escolher só o que dá errado** | a extração é feita por varredura da transcrição inteira, em ordem, antes de qualquer checagem. ⛔ Não se escolhe o que checar depois de saber o resultado |
| **Julgar a intenção** | o card fala do enunciado, nunca do motivo. ⛔ Nada de "tentou esconder que" |
| **Anacronismo** | o veredito usa a fonte vigente **na data da fala**, e o card diz a data de referência |
| **Falsa precisão** | se a fonte primária tem intervalo de confiança ou revisão, o card mostra o intervalo |
| **Fonte única com cara de duas** | teste de independência da regra 3 da §3.1 |
| **Corrigir o entrevistado com dado mais novo** | se o dado mudou depois da fala, o veredito é sobre o que valia na data, e a atualização vai numa nota |
| **Encher de cinza pra não se comprometer** | `NAO_CHECAVEL` exige justificativa escrita de **por que** a frase não tem valor de verdade |

---

## 6. Quem faz o quê

| Etapa | Quem executa | Determinístico? |
|---|---|---|
| 1. Preparar mídia (hash, áudio, recorte) | script | ✅ |
| 2. Transcrever | script (`whisper.cpp`) | ✅ mesma entrada, mesma saída |
| 3. Atribuir falante | humano + IA, contra o vídeo | ⚠️ revisado |
| 4. Extrair alegações | **IA**, seguindo a skill `extrair-alegacoes` | ❌ julgamento |
| 5. Checar cada alegação | **IA**, seguindo a skill `checar-alegacao`, com busca na web | ❌ julgamento |
| 6. Validar schema, fontes e contagem | script | ✅ |
| 7. Montar overlay e renderizar | script | ✅ |
| 8. Revisão final | **humano** | ❌ |

> 🔴 **A IA analisa. O humano publica.** Nenhum vídeo vai ao ar sem um humano ter lido os cards e as fontes. O repositório é aberto justamente para que esse humano não precise ser o autor.

---

## 7. Correção e direito de resposta

- Erro encontrado depois da publicação vira uma entrada em `CORRECOES.md` do caso, com data, o que estava escrito, o que passou a valer e a fonte que motivou a mudança. ⛔ Não se edita um veredito em silêncio.
- Contestação de qualquer pessoa citada entra como issue e é respondida com fonte, não com opinião.
- O veredito muda se a evidência mudar. Isso é o processo funcionando, não uma falha dele.

---

## 8. O que este projeto NÃO é

- ⛔ Não é apuração jornalística: não entrevista, não ouve fonte humana, não obtém documento inédito. Ele confere o que foi dito contra o que já está publicado.
- ⛔ Não mede intenção, caráter, coerência ideológica ou desempenho de governo.
- ⛔ Não recomenda voto, não classifica candidato e não soma placar de "quem mentiu mais" como conclusão editorial. A contagem existe como dado do caso, não como veredito sobre a pessoa.
- ⛔ Não substitui as agências de checagem profissionais: ele as usa como fonte e aponta para elas.
