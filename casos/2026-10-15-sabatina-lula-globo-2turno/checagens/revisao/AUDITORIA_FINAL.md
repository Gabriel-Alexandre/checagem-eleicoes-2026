# Auditoria final: caso 2026-10-15-sabatina-lula-globo-2turno

**Data:** 16/10/2026 · **Auditor:** Claude (auditor final, sem participação na extração, na checagem nem nas revisões deste caso) · **Base auditada:** `checagens/checagens-sabatina-completa.json` (193 checagens: 130 VERDADEIRO, 30 IMPRECISO, 30 INSUSTENTAVEL, 3 FALSO, 0 NAO_CHECAVEL) · **Régua:** `docs/METODOLOGIA.md` §2 a §5, `.cursor/rules/etica-e-risco.mdc`, `skills/revisar-checagem.md`.

Nada foi corrigido nos arquivos do caso. Este documento só registra o que foi conferido e o que foi achado. A decisão sobre cada achado é do autor do projeto.

---

## 1. A amostra

**Como foi sorteada.** Script em Python, `random.Random(15102026)`. Os ids de cada veredito foram ordenados e sorteados nesta ordem, com o mesmo gerador: todas as FALSO; 6 IMPRECISO; 8 INSUSTENTAVEL; 8 VERDADEIRO. Depois foram somados todos os ids dos 6 cortes em `recortes/SUGESTAO_DE_CORTES.json`. Refazer:

```python
import json, random
ch = json.load(open("checagens/checagens-sabatina-completa.json", encoding="utf-8"))["checagens"]
por = {}
for c in ch: por.setdefault(c["veredito"], []).append(c["id"])
for v in por: por[v].sort()
rng = random.Random(15102026)
falso = por["FALSO"]
imp = sorted(rng.sample(por["IMPRECISO"], 6))
ins = sorted(rng.sample(por["INSUSTENTAVEL"], 8))
ver = sorted(rng.sample(por["VERDADEIRO"], 8))
```

| Grupo | Ids |
|---|---|
| FALSO (todas) | A047, A124, A146 |
| IMPRECISO (6) | A082, A136, A150, A154, A180, A183 |
| INSUSTENTAVEL (8) | A018, A028, A029, A064, A126, A157, A158, A189 |
| VERDADEIRO (8) | A043, A095, A117, A137, A155, A169, A170, A185 |
| corte-01 | A016, A017, A018 |
| corte-02 | A036, A037, A038, A039, A040 |
| corte-03 | A073, A074, A075 |
| corte-04 | A145, A146, A147, A148, A149 |
| corte-05 | A182, A183, A184 |
| corte-06 | A191, A192, A193 |

**Total: 44 checagens distintas** (A018, A146 e A183 caíram no sorteio e também estão em corte).

## 2. O que foi conferido em cada uma

Para as 44, nesta ordem:

1. **Frase e falante:** a `frase` contra `transcricao/transcricao.json`, no intervalo da alegação, com o falante do segmento, e a leitura de 30 s antes e 30 s depois para ver se a `afirmacao` e o card mudam o sentido.
2. **Trechos:** cada `trecho` (partido nos `[...]`) procurado por script no texto capturado (`capturas/<caso>-*/texto/<id>.txt`, achado pela URL nos `capturas.json`). Os 2 casos que o script marcou como parciais (A018, Aos Fatos; A189, Jornal de Brasília) foram conferidos à mão: diferença só de espaço antes de vírgula. **Todos os trechos da amostra estão nas capturas.** Depois, leitura de cada trecho contra a coluna `prova`.
3. **Independência das fontes** (§3.1, regras 1 a 3).
4. **Árvore do §2.1 e régua de 10% do §2.2**, comparando com checagens irmãs do mesmo caso nos dois lados da mesa.
5. **Resumo lido sozinho**, e para os 22 itens de corte também a cartela renderizada (`overlay/cartelas-corte-0N/*.png`, conferidas A145 e A149).
6. **Arquivos de corte:** veredito, resumo, ressalva, número apurado e explicação dos 22 itens em `checagens-corte-0N.json` são idênticos aos da completa.
7. **Busca web (8 buscas, 2 leituras de página), só atrás do que contradiria um veredito:** taxa DES/dólar de novembro de 2003 (A149), empréstimo do Brasil ao FMI (A150), origem dos 2,8% (A124), número atual do Mais Médicos (A180), pedido de apoio de Lula a partidos (A029), comércio Brasil e Vietnã em 2026 (A039), divulgação do FGV Ibre (A126), comércio com a China (A036).

---

## 3. ACHADOS

### Achado 1 · A149 (corte-04, vai para a tela) · VERDADEIRO sustentado por uma conversão de câmbio errada

**O problema.** "paguei os 30 bilhões do FMI" ficou VERDADEIRO porque a revisão r6 converteu o saldo do FMI de 30/11/2003 (23.358,59 milhões de DES) em "cerca de US$ 30,7 bilhões", usando a equivalência da carta de intenção de **agosto de 2002** (DES 22.821 milhões para uns US$ 30 bilhões, ou seja, US$ 1,3146 por DES). É câmbio de 15 meses antes. A mesma derivação é o argumento central da nota de revisão para não aplicar a régua de 10%.

**A evidência.** A tabela de taxas do FMI para novembro de 2003 dá 0,6902360 DES por dólar em 28/11/2003, isto é, **US$ 1,4488 por DES** (imf.org, `rms_mth.aspx?SelectDate=2003-11-30&reportType=SDRCV`). 23.358,59 × 1,4488 = **cerca de US$ 33,8 bilhões**, que é exatamente o pico de US$ 33,7 bilhões da reportagem de 2005 que a própria checagem cita. Os "30,7" não existem. Com o dado certo:
- dívida quitada no governo (pico do saldo): 30 contra 33,8, desvio de 11%;
- só o que foi sacado do acordo "de 30 bilhões" (17.199,64 milhões de DES × 1,4488): cerca de US$ 24,9 bilhões, desvio de 20%;
- só o pago em 2005: US$ 23,3 bilhões, desvio de 29%.

Nenhuma leitura fica dentro de 10%. E a régua não é igual: a A154 (Renata, "10 pontos" contra 11,19) foi rebaixada a IMPRECISO por um desvio de 10,6%, e a A149, com 11%, ficou verde. A cartela de A149 mostra a fala "30" e, em verde, "chegado a US$ 33,7 bi".

**O que deveria mudar.** Tirar a derivação de US$ 30,7 bilhões (ou refazê-la com o câmbio da data) e reavaliar A149 pela régua do §2.2; pela conta acima, IMPRECISO, com a essência (a quitação em dez/2005) na explicação. Conferir também a derivação "cerca de US$ 20 bilhões" da A145, que usa o mesmo câmbio de 2002 (com o de 31/12/2002, cerca de US$ 1,36 por DES, dá US$ 20,8 bilhões; o resumo "cerca de US$ 20 bi" continua de pé). Registrar em `CORRECOES.md` e regerar a cartela e o render do corte-04.

### Achado 2 · A039 (corte-02, vai para a tela) · a segunda fonte que "não existe" existe

**O problema.** "13% com o Vietnã" ficou INSUSTENTAVEL só por falta de segunda fonte independente do Comex Stat, e a explicação afirma que a imprensa vietnamita trazia "só dados de anos anteriores ou de produtos isolados". A busca não foi exaustiva.

**A evidência.** Vietnam News (agência VNA), 11/07/2026, "Việt Nam, Brazil seek ways to promote trade, investment cooperation": pela embaixadora do Vietnã no Brasil, o comércio bilateral foi de US$ 4,22 bilhões no 1º semestre de 2026, alta de 16,8%, e as exportações do Brasil ao Vietnã passaram de US$ 2 bilhões, **alta de 16,6%**. É fonte do lado do parceiro, independente do MDIC, e confirma o essencial (o comércio cresceu na casa dos dois dígitos). O Comex Stat dá 14,1% nas exportações de janeiro a setembro (desvio de cerca de 8% contra os 13% ditos).

Há ainda uma assimetria de régua na mesma resposta: a A036 (China, IMPRECISO contra o candidato) aceitou como segunda fonte o Poder360 reproduzindo a divulgação do MDIC, que pela regra 3 da §3.1 é a mesma fonte; a A039 (Vietnã, onde a base única fica perto do dito) foi barrada por não ter segunda fonte. A A126 (Renata) usa a A039 como a régua aplicada ao candidato, então a correção da A039 não altera a A126, mas a frase "mesma régua" passa a precisar de revisão.

**O que deveria mudar.** Capturar a matéria da VNA, refazer a A039 com duas fontes e escolher o veredito pela árvore. Pelo recorte usado nos outros países (exportação, janeiro a setembro), o resultado tende a VERDADEIRO com ressalva (o período do dado vietnamita é o semestre, 16,6%). Regerar a cartela do corte-02. Registrar a questão de independência da A036 (a conta continua certa; o que falta é declarar que o Poder360 não é fonte independente, ou trocar por uma que seja).

### Achado 3 · A155 · veredito provisório publicado como final, com o essencial sem lastro

**O problema.** "boa parte dos economistas considerar [...] a trajetória da dívida [...] insustentável" (Renata) está VERDADEIRO, mas a explicação diz que "a busca deste pedido foi interrompida pelo limite de consultas da sessão", a nota de revisão começa com "Veredito provisório (busca interrompida)" e termina com "Antes de ir à tela, pede o Prisma Fiscal ou outra pesquisa com economistas". A rodada 2 não passou por ela. As fontes (IFI e FMI) são instituições e projeções; nenhuma mede o que "boa parte dos economistas" considera, e a ressalva admite que "não há levantamento de quantos economistas a chamam de insustentável".

**A evidência.** `revisao_ia.nota` da A155; explicação da A155. Comparação com o outro lado da mesa: a A157 (Lula, "a maior política de crédito") e a A158 (Lula, "cansei de brigar com Mantega e Meirelles") ficaram INSUSTENTAVEL justamente porque a medida do todo não existe nas fontes. Mesma situação, veredito diferente.

**O que deveria mudar.** Fechar a busca pedida pela própria revisão (pesquisa com economistas, Prisma Fiscal, relatórios de bancos e consultorias) ou, sem ela, aplicar a régua da A157: INSUSTENTAVEL, com o resumo dizendo o que IFI e FMI projetam. Fora da amostra, o mesmo filtro achou mais três checagens cuja nota ainda começa por "provisório" sem passagem pela rodada 2 (A104, A105, A156); vale conferir se foram fechadas.

### Achado 4 · A180 · IMPRECISO apoiado em dado de quase dois anos antes da fala

**O problema.** "Nós já contratamos 16 mil [...] para ir para 28" foi rebaixado a IMPRECISO com dois cálculos: (a) como saldo, 13,9 mil entre dez/2022 e **nov/2024**; (b) como entradas, mais de 23 mil em 2023 e 2024. A própria explicação diz que "o total de contratações até a data da fala não foi publicado". A leitura (a) julga uma frase de outubro de 2026 com um dado de novembro de 2024, que é o anacronismo do §5. A leitura (b) não contradiz a frase: "já contratamos 16 mil" fica abaixo do registrado, e o informe de março de 2024 diz que mais de 16.340 entraram só em 2023.

**A evidência.** A revisão anterior da própria A180 tinha mantido INSUSTENTAVEL exatamente por isso ("o dado é de mais de dois anos antes da fala e a regra é usar o dado da data da fala (§5, anacronismo), que não foi achado"); a rodada 2 inverteu sem dado novo da data. A busca desta auditoria também não achou balanço de 2026 (a meta de 28 mil e o número de 2024 e 2025 aparecem, o de 2026 não). O resumo atual ("as contratações passam de 16 mil") num card amarelo dá a impressão de erro do candidato por ter dito um número menor que o real.

**O que deveria mudar.** Pela árvore, sem dado da data da fala para a leitura de saldo e sem contradição na leitura de entradas: INSUSTENTAVEL, com o resumo dizendo o último dado datado (26,7 mil em atividade em nov/2024, a partir de 12,8 mil) e o que faltou.

### Achado 5 · A064 (e, por paridade, A074) · INSUSTENTAVEL para a existência de suspeitas que as fontes confirmam

**O problema.** A frase da Renata afirma que o STF vive uma crise ligada ao caso Master e que "suspeitas [...] pairam sobre vários ministros". As três fontes confirmam isso, e o resumo também ("Ministros do STF são citados em relatórios e reportagens do caso Master"). O laranja vem da regra de ética §5, que trata de fato **em apuração** (culpa, envolvimento); a existência da suspeita e da citação é fato consumado, documentado. O card fica com cor e texto apontando para lados opostos, e a explicação ainda usa um rótulo que não é veredito ("SEM COMPROVAÇÃO").

**A evidência.** Explicação e resumo da A064; a nota da revisão chama este de "o argumento mais forte desta revisão" e o mantém só por paridade com a A074 (Lula, "o Toffoli também está implicado"), em que o resumo também confirma a citação de Toffoli nas mensagens e a suspeição declarada por ele em 15/09. A paridade é legítima, mas pode ser mantida nos dois sentidos.

**O que deveria mudar.** Separar, para os dois lados, o que é documentado (existe suspeita, o ministro é citado no material da PF) do que está em apuração (o envolvimento). A064 e A074 podem ir a VERDADEIRO com ressalva "a apuração não concluiu", mantendo a simetria; A073 (ranking "o mais implicado") e A075 (Mendonça, ligado ao caso só pela relatoria) continuam INSUSTENTAVEL pelos motivos que já têm. Achado de menor gravidade que os anteriores: é escolha de método, mas hoje o card laranja da A064 deixa a impressão de que a jornalista afirmou algo sem base.

---

## 4. O que ficou de pé

| Id | Veredito | Por que fica |
|---|---|---|
| A016 | VERDADEIRO | 70 contra 68 do PT (Agência Câmara, duas matérias): desvio de 3%, ressalva com a federação |
| A017 | VERDADEIRO | 9 senadores no fim do 2º turno e no comunicado da posse (Senado); a divergência de 8 está escrita |
| A018 | INSUSTENTAVEL | "99% de tudo" sem universo definido; 21%, 23% e 37% contradizem a leitura literal, e o card diz que nenhuma fonte dá 99% |
| A028 | INSUSTENTAVEL | nada sustenta nem contradiz; o resumo diz o que se achou |
| A029 | INSUSTENTAVEL | só relato de bastidor negado e conversas do presidente do PT; a busca desta auditoria não achou pedido de Lula com registro |
| A036 | IMPRECISO | 12,0% (jan a set) e 16,6% (12 meses) contra 20%; a busca confirmou 12% no acumulado e queda em setembro (ver nota de independência no Achado 2) |
| A037 | IMPRECISO | 2,2% no Comex Stat e 8,6% na base indonésia contra 15%; o recorte de jan a mai (15,5%) foi recusado com motivo |
| A038 | VERDADEIRO | 15,8% (Comex) e 16,7% (Eurostat) contra 16%; ressalva da corrente de comércio |
| A040 | INSUSTENTAVEL | média de 10,5% sem lista nem período; 41 países do Poder360 não prova o contrário |
| A043 | VERDADEIRO | Quaest em 1º e Datafolha "no mesmo patamar"; "no topo" não exige 1º isolado |
| A047 | FALSO | o §1189 não exige terrorismo político e os EUA designaram cartéis (2025) e o próprio PCC e CV (2026) pela mesma seção. Ponto que a explicação poderia citar: a definição de "terrorism" do 22 U.S.C. 2656f é de violência politicamente motivada, o que dá base parcial à leitura de Lula; não muda o veredito, porque a prática contradiz o essencial |
| A073 | INSUSTENTAVEL | ranking de envolvimento sem critério; o resumo traz o dado que favorece a frase (181 de 218 páginas) |
| A075 | INSUSTENTAVEL | Mendonça liga-se ao caso pela relatoria e por pedido de investigação não julgado |
| A082 | IMPRECISO | EC 45 promulgada no governo, mas proposta de 1992 e promulgada pelo Congresso; houve emenda de 1977 sobre o Judiciário |
| A095 | VERDADEIRO | três apurações (uma com confirmação do próprio Lula) dão Mantega como quem levou Vorcaro |
| A117 | VERDADEIRO | 17/09 a 04/10/2026 são 17 dias; conta refeita |
| A124 | FALSO | 2022 fechou com superávit (BC 1,25%, TCU 0,6%); a busca não achou base para 2,8%; mesmo veredito do caso de 27/ago |
| A126 | INSUSTENTAVEL | o 24,9% só aparece numa cadeia de reproduções do Estadão; a busca não achou a divulgação do FGV Ibre |
| A136 | IMPRECISO | perdão aprovado pela Câmara em 14/10, pendente no Senado na data da fala |
| A137 | VERDADEIRO | R$ 12,86 bi (exposição de motivos) contra 12,7: 1,2% |
| A145 | IMPRECISO | na posse o saldo era cerca de US$ 20,8 bi; os 30 eram o tamanho do acordo (ver nota de câmbio no Achado 1) |
| A146 | FALSO | PIB de +3,05% em 2002 e +1,14% em 2003 em três fontes; "não estava crescendo" tem sentido oposto |
| A147 | VERDADEIRO | 7º em 2010 no FMI e no Banco Mundial |
| A148 | VERDADEIRO | 270 entre 250,8 (acréscimo) e 288,6 (estoque), menos de 10% nas duas leituras |
| A150 | IMPRECISO | acordo de até US$ 10 bi; a busca confirmou 10 e que o NAB só vigorou em 2011 |
| A154 | IMPRECISO | 10 contra 11,19 pontos, 10,6% sobre o apurado; régua aplicada à jornalista mesmo com o erro a favor do entrevistado |
| A157 | INSUSTENTAVEL | só a comparação do BNDES existe, e ela pesa contra; falta medida do conjunto |
| A158 | INSUSTENTAVEL | um relato para Meirelles, nenhum para Mantega |
| A169 | VERDADEIRO | 60% da geração e 71% da distribuição privadas já em 2017, e depois a Eletrobras saiu do controle estatal |
| A170 | VERDADEIRO | privatização concluída em 09/06/2022 |
| A182 | INSUSTENTAVEL | só o governo relata a paralisação; equipes subiram nas contas de imprensa; sem série oficial |
| A183 | IMPRECISO | o programa funcionava; enfraquecimento e risco confirmados por fontes independentes do governo (Aos Fatos, Rádio Senado) |
| A184 | VERDADEIRO | o TCU diz que o financiamento ajudou a aumentar as cirurgias |
| A185 | VERDADEIRO | a ementa do Acórdão 1622/2026 traz "baixa efetividade na redução do tempo de espera" |
| A189 | INSUSTENTAVEL | não há medida nacional da espera; o TCU mostra 2 anos só em procedimentos raros |
| A191 | VERDADEIRO | 80 e 120 kWh na Lei 15.235/2025, com a ressalva do público. Observação: as duas fontes são da mesma norma (lei e exposição de motivos); a explicação declara isso, e para norma vigente a norma é o registro do fato, mas a contagem de "duas fontes" fica no limite da regra 3 da §3.1 |
| A192 | IMPRECISO | 17 milhões de pessoas contra cerca de 50 milhões; troca de unidade |
| A193 | VERDADEIRO | gratuidade custeada pela União na Lei 15.348/2026; mesma observação da A191 sobre fontes da mesma norma |

**Conferências que passaram em toda a amostra:** todas as frases estão na transcrição com o falante certo; nenhum card muda o sentido do que foi dito no contexto; todos os trechos estão nas capturas; os arquivos de corte batem com a completa; nenhum resumo da amostra tem leitura de intenção ou adjetivo sobre a pessoa.

## 5. Fontes externas consultadas nesta auditoria

- FMI, taxas do DES em novembro de 2003: https://www.imf.org/external/np/fin/data/rms_mth.aspx?SelectDate=2003-11-30&reportType=SDRCV
- Vietnam News (VNA), 11/07/2026: https://vietnamnews.vn/economy/1785257/viet-nam-brazil-seek-ways-to-promote-trade-investment-cooperation.html
- Correio do Estado, sobre o empréstimo ao FMI (US$ 10 bi): https://correiodoestado.com.br/mix/brasil-emprestou-fortuna-ao-fmi-apos-ser-um-dos-maiores-devedores/
- Agência Gov, Mais Médicos e a meta de 28 mil (jul/2024): https://agenciagov.ebc.com.br/noticias/202407/em-18-meses-mais-medicos-praticamente-dobra-numero-de-profissionais
- Comprerural, comércio com a China de janeiro a setembro de 2026: https://comprerural.com/exportacoes-brasileiras-para-os-eua-sobem-319-em-setembro-ante-setembro-de-2025/

⚠️ As duas primeiras ainda não estão em `capturas/`. Se o autor decidir corrigir A149 e A039, elas precisam ser capturadas pelo processo do repositório antes de entrarem como fonte.
