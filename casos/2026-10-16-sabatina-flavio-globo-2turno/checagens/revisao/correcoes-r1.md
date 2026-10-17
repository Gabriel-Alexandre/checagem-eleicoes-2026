# Correções da revisão r1 (lotes 01, 02 e 03)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, `docs/METODOLOGIA.md` §2, §3 e §5 e `.cursor/rules/etica-e-risco.mdc`. Duas buscas web, as duas atrás do que contradiria um veredito: os juros nominais só do governo central (A003) e uma fonte para os R$ 36 bilhões de prejuízo das estatais (A019). Nenhuma achou o dado. A captura feita nessa procura (`capturas/2026-10-16-sabatina-flavio-globo-2turno-rv1`, pedido em `checagens/pedidos-captura/revisao-r1.json`: a nota do BC de 30/09 na cópia do Poder360 e o Raio X da Dívida de agosto da Câmara) não entrou como fonte, porque nenhuma das duas separa o governo central. Toda fonte nova abaixo já estava capturada. Os 95 trechos dos três lotes, depois das mudanças, foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py`, por palavra inteira (95 de 95 achados); os três lotes validam contra `esquemas/checagens.schema.json`; números, anos e termos de intenção de `resumo`, `ressalva` e `numero_apurado` foram conferidos com `numeros_de()`, `anos_de()` e `_tem_intencao()` do validador (nenhum aviso). Nenhum veredito mudou. Uma checagem (A015) foi marcada como provisória. As notas por checagem estão em `revisao-r1.json`.

## A002 (lote 01), explicação

- **Estava:** "o coordenador da campanha, Rogério Marinho, disse que uma vitória de Flávio levaria a Selic a 12% ou 13% (EQI)"
- **Passou a valer:** "o coordenador da campanha, Rogério Marinho, disse que uma eventual vitória de Flávio poderia levar a Selic à faixa de 12% a 13% ao ano (EQI)"
- **Por quê:** o trecho do EQI diz "poderia levar a taxa básica de juros para a faixa de 12% a 13% ao ano"; a explicação transformava a hipótese em afirmação (pergunta 3).

## A015 (lote 02), explicação e confiança

- **Estava:** explicação sem o marcador de provisório, terminando em "A busca nesta rodada foi limitada a duas consultas sobre o tema."; confiança `media`.
- **Passou a valer:** a explicação começa por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e termina com o que falta ("procurar declarações nominais de economistas ligados à campanha ou que declararam apoio ao candidato sobre o ajuste de R$ 200 bilhões sem mexer nas despesas obrigatórias, e algum levantamento de opinião de economistas que permita falar ou não em consenso"); confiança `baixa`.
- **Por quê:** a árvore do §2.1 só dá INSUSTENTAVEL depois de busca exaustiva, e a própria checagem declarava duas consultas. É o defeito da A155 do caso de 15/out, provisória sem marcador que escapou da rodada 2. Veredito, resumo e fontes sem mudança; a rodada 2 refaz.

## A016 (lote 02), resumo

- **Estava:** "A coordenadora econômica de Flávio falou em ajuste de 1,5% do PIB, cerca de R$ 190 bi; a campanha fala em R$ 200 bi"
- **Passou a valer:** "A coordenadora econômica falou em ajuste de 1,5% do PIB, cerca de R$ 190 bi; o discurso da campanha é de R$ 200 bi"
- **Por quê:** "a campanha fala em R$ 200 bi" contradizia a ressalva ("a campanha evita cravar o valor"). O SBT, no trecho, diz que integrantes da campanha "evitam cravar o tamanho do ajuste", mas "o discurso é de um corte em torno de R$ 200 bilhões" (perguntas 7 e 8).

## A016 (lote 02), ressalva

- **Estava:** "A campanha evita cravar o valor; a coordenadora falou em 1,5% do PIB, cerca de R$ 190 bilhões"
- **Passou a valer:** "Integrantes da campanha evitam cravar o valor, e ainda não há plano completo com os gastos a cortar"
- **Por quê:** a ressalva repetia o dado do resumo e deixava de fora o que limita o VERDADEIRO: o valor não foi cravado (SBT) e não há plano completo com a discriminação dos gastos (Poder360), ambos com trecho (pergunta 8).

## A018 (lote 02), trecho e prova da fonte Money Times

- **Estava:** trecho "As estatais federais registraram superávits sucessivos, como o saldo positivo de R$ 2,5 bilhões em 2021 e de R$ 4,8 bilhões em 2022."
- **Passou a valer:** o trecho começa com "Vale lembrar que a série do Banco Central não considera a Petrobras, a Eletrobras, nem as empresas do setor financeiro (os bancos públicos).", seguido de `[...]` e do trecho antigo (captura p02-r2 `547a05b233f7`); a prova cita a exclusão.
- **Por quê:** a explicação afirma que "a imprensa registra que os bancos públicos também ficam fora" da série, e nenhum trecho da A018 dizia isso (pergunta 3).

## A019 (lote 02), trecho e prova da fonte Money Times

- **Estava:** trecho só com o déficit de R$ 5,93 bilhões de janeiro a abril de 2026.
- **Passou a valer:** o trecho ganhou, depois de `[...]`, a frase "Vale lembrar que a série do Banco Central não considera a Petrobras, a Eletrobras, nem as empresas do setor financeiro (os bancos públicos)." (mesma captura `547a05b233f7`); a prova cita a exclusão.
- **Por quê:** a ressalva, que vai para a tela, diz "sem Petrobras e bancos públicos", e nenhum trecho da A019 trazia os bancos públicos (perguntas 3 e 7).

## A021 (lote 03), fontes

- **Estava:** 3 fontes (Lista de Alto Risco do TCU, acórdão do levantamento na SPU, InfoMoney). A `divergencia_entre_fontes` cita "cerca de 742 mil no levantamento do Acórdão 160/2024", número sem trecho nesta checagem.
- **Passou a valer:** 4 fontes. Entrou TCU, "Gestão do patrimônio imobiliário federal gerido pela SPU é ineficiente, diz TCU" (já capturada e usada na A022, `058953b1e507`), com o trecho "A SPU é responsável pela gestão de cerca de 742 mil imóveis, avaliados em, aproximadamente, R$ 1,35 trilhão."
- **Por quê:** METODOLOGIA §3.1, regra 6; a divergência registrada precisava de trecho na própria checagem (pergunta 3). Veredito, resumo e ressalva sem mudança.

## A026 (lote 03), resumo

- **Estava:** "No orçamento de 2027, a Previdência leva R$ 1.215,1 bi de R$ 2.830,1 bi; saúde e educação têm pisos próprios"
- **Passou a valer:** "No projeto de orçamento de 2027, a Previdência leva R$ 1.215,1 bi de R$ 2.830,1 bi; saúde e educação têm pisos próprios"
- **Por quê:** os valores são do PLOA 2027, projeto enviado em agosto e não aprovado na data da fala; "orçamento de 2027" lia como lei aprovada (perguntas 5 e 8).

## A027 (lote 03), resumo

- **Estava:** "A Petrobras fala em produzir em cerca de sete anos; a perfuração exploratória já começou em 2025"
- **Passou a valer:** "A Petrobras fala em produzir em cerca de sete anos; a perfuração exploratória foi licenciada em 2025"
- **Por quê:** nenhum trecho dá a data do início da perfuração. O InfoAmazonia dá a licença do Ibama em 20/10/2025, a Exame diz que a licença permite perfuração imediata e o InfoMoney registra o poço em perfuração em agosto de 2026; "começou em 2025" é provável, mas não está escrito em fonte (pergunta 7). Veredito sem mudança.

## Registrado sem mudança nos lotes

- **A003:** o melhor argumento contra o IMPRECISO é de recorte: a frase fala de "o governo", e a conta divide os juros do setor público consolidado (R$ 1.182,2 bi) pelas dotações federais de saúde e educação (R$ 505 bi). O veredito só continua IMPRECISO se os juros do governo central passarem de cerca de R$ 1.122 bi (2,22 vezes 505). A busca da revisão não achou esse número. Fica IMPRECISO pela mesma medida de juros usada na A007 do caso de 28/08 contra o candidato, e a explicação já declara a lacuna. Pergunta para a passada de coerência.
- **A011:** 7 contra 7,75 dá 9,7% sobre o apurado e 10,7% sobre o dito. Fica VERDADEIRO pela base usada no projeto (o apurado) e pelo mesmo veredito na A006 de 28/08; a A033 do caso de 15/out mediu sobre o dito. Pergunta para a passada de coerência.
- **A025 e A027:** os dois lados usam "exploração" no sentido comum de extração; a checagem seguiu o critério escrito antes da busca (exploração técnica contra produção) e deu IMPRECISO aos dois. Se o autor preferir a leitura comum, as duas mudam juntas.
- **A020:** provisória. O total que falta já está capturado na A021 (cerca de 761 mil imóveis, TCU). Hoje o resumo da A020 cita 655 mil de 2018 e o da A021 cita 761 mil; a rodada 2 deve alinhar os dois cards.
- **A008, A009, A010, A020, A023:** provisórias com o marcador exato e confiança baixa; o que falta está anotado em `revisao-r1.json`.
