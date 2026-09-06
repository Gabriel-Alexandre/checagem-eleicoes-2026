# FONTES — onde mora cada dado público brasileiro

Atalho de trabalho para o PASSO 5. ⚠️ **Não é lista de autoridade:** estar aqui não dispensa
abrir, conferir e copiar o trecho. Endereço de portal público muda com frequência; se um link
não abrir, procure a base pelo nome da instituição em vez de citar de memória.

Classificação por nível: ver [`METODOLOGIA.md` §3](METODOLOGIA.md).

---

## Economia e contas públicas

| Dado | Onde | Nível |
|---|---|---|
| PIB, inflação, desemprego, população, rendimento | **IBGE** — SIDRA (`sidra.ibge.gov.br`) e Agência IBGE Notícias | N1 |
| Séries monetárias, câmbio, juros, crédito, dívida externa | **Banco Central** — Sistema Gerenciador de Séries Temporais (SGS) | N1 |
| Dívida pública, resultado primário, arrecadação, despesa | **Tesouro Nacional** — Tesouro Transparente e Relatório Mensal da Dívida | N1 |
| Arrecadação federal | **Receita Federal** — relatórios mensais de arrecadação | N1 |
| Execução orçamentária linha a linha | **Portal da Transparência** e SIOP | N1 |
| Projeções de mercado (Focus) | **Banco Central** — Relatório Focus | N1 |
| Séries tratadas, deflacionadas e comparáveis no tempo | **IPEADATA** (Ipea) | N2 |
| Indicadores de conjuntura e IGP | **FGV/IBRE** | N2 |
| Comparação internacional | **Banco Mundial**, **FMI**, **OCDE** | N2 |

⚠️ **A armadilha número um da economia é nominal contra real.** Valor em reais de anos diferentes
só se compara deflacionado, e a `explicacao` tem que dizer por qual índice.

## Trabalho e previdência

| Dado | Onde | Nível |
|---|---|---|
| Emprego formal (saldo, admissões, desligamentos) | **CAGED / Novo CAGED**, Ministério do Trabalho | N1 |
| Desemprego, informalidade, rendimento | **IBGE** — PNAD Contínua | N1 |
| Benefícios, fila, concessões do INSS | **INSS** e **Dataprev** — boletins e painéis estatísticos | N1 |
| Séries longas do RGPS | **Anuário Estatístico da Previdência Social** | N1 |

⚠️ **"Fila do INSS" não tem definição única.** Requerimento em análise, requerimento fora do prazo
legal e requerimento com exigência pendente são números diferentes. A `explicacao` declara qual
definição a fonte usa. Comparar duas definições diferentes é o erro clássico aqui.

## Saúde

| Dado | Onde | Nível |
|---|---|---|
| Mortalidade, natalidade, internações, procedimentos | **DataSUS** — TabNet (SIM, SINASC, SIH, SIA) | N1 |
| Cobertura vacinal | **Ministério da Saúde** — PNI / LocalizaSUS | N1 |
| Leitos, estabelecimentos, profissionais | **CNES** | N1 |
| Análise e comparação | **Fiocruz**, **Conass**, **Conasems** | N2 |

## Educação

| Dado | Onde | Nível |
|---|---|---|
| Censo Escolar, matrículas, docentes, infraestrutura | **INEP** | N1 |
| IDEB, SAEB, aprendizado | **INEP** | N1 |
| ENEM, ensino superior, censo da educação superior | **INEP** | N1 |
| Institutos federais, universidades, obras | **MEC** e **Painel de Obras** | N1 |
| Comparação internacional | **PISA/OCDE** | N2 |

## Segurança pública e justiça

| Dado | Onde | Nível |
|---|---|---|
| Homicídios, roubos, vitimização, efetivo | **Anuário Brasileiro de Segurança Pública** (FBSP) | N2 |
| Registros administrativos por estado | **SINESP** e as secretarias estaduais | N1 |
| Mortes violentas com série longa | **DataSUS/SIM**, causa externa | N1 |
| População prisional | **SISDEPEN / Senappen** | N1 |
| Decisão judicial | **STF**, **STJ**, **TSE** — inteiro teor, nunca o resumo da notícia | N1 |
| Estatísticas do Judiciário | **CNJ** — Justiça em Números | N1 |

🔴 **Segurança pública tem defasagem de cerca de um ano** e metodologia que varia entre estados.
Comparar ano fechado com ano parcial é o erro mais comum. E ⛔ nunca escreva veredito que sugira
culpa em processo sem decisão definitiva (ver `.cursor/rules/etica-e-risco.mdc` §5).

## Meio ambiente

| Dado | Onde | Nível |
|---|---|---|
| Desmatamento (taxa anual e alertas) | **INPE** — PRODES e DETER | N1 |
| Queimadas | **INPE** — Programa Queimadas | N1 |
| Emissões | **SEEG / Observatório do Clima** | N2 |
| Autuações e embargos | **IBAMA** | N1 |

⚠️ **PRODES e DETER medem coisas diferentes.** O primeiro é a taxa anual consolidada (ano
referência de agosto a julho); o segundo é alerta em tempo quase real. Trocar um pelo outro
produz números que parecem contradizer e não contradizem.

## Eleições

| Dado | Onde | Nível |
|---|---|---|
| Candidaturas, prestação de contas, resultados | **TSE** — Portal de Dados Abertos | N1 |
| Pesquisas registradas | **TSE** — registro de pesquisas eleitorais | N1 |
| Institutos | Quaest, Datafolha, Ipec, AtlasIntel — a divulgação do próprio instituto | N2 |

⚠️ **Pesquisa se cita com margem de erro, data de campo e número de registro no TSE.** Sem isso,
comparação entre duas pesquisas é ruído.

## Checagem profissional (N3)

**Agência Lupa** · **Aos Fatos** · **Projeto Comprova** · **Estadão Verifica** ·
**AFP Checamos** · **Fato ou Fake** (Globo) · **Boatos.org** (⚠️ N4, sem selo IFCN).

Ótimas para achar a primária rápido em frase famosa. ⛔ **Não pare nelas:** a primária é que entra
como fonte principal.

## Transcrições e íntegras

Poder360, Agência Brasil, o site do próprio veículo e o canal oficial. Servem para **conferir a
sua transcrição**, e são N4 para fato.

---

## Três armadilhas que valem para tudo

1. **Recorte temporal.** "Caiu 30%" contra qual base, em que período? Quem escolhe o ponto de
   partida escolhe o resultado. A `explicacao` declara a janela.
2. **Mudança de metodologia.** Série que trocou de método não se compara antes e depois sem nota.
   IBGE e INEP avisam nas notas técnicas; leia-as.
3. **Estoque contra fluxo.** "Criamos 2 milhões de empregos" (fluxo, saldo do período) e "há 2
   milhões de empregados a mais" (estoque) não são a mesma frase.
