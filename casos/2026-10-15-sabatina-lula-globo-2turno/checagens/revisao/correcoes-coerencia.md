# Correções da revisão de coerência entre lotes

Passada separada, em 16/10/2026, depois das revisões r1 a r8 (lote a lote), seguindo `skills/revisar-checagem.md` (pergunta 6: a mesma régua nos dois lados da mesa e entre checagens), `docs/METODOLOGIA.md` §2 e §2.2 e `.cursor/rules/etica-e-risco.mdc`. O revisor não checou nem revisou nenhuma alegação deste caso antes. Sem busca web: toda fonte que entrou abaixo já estava capturada nas pastas `capturas/2026-10-15-sabatina-lula-globo-2turno-*` e já era usada em outra checagem do caso; os trechos das dez checagens tocadas foram conferidos contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py` (todos achados). O validador, depois da junção, não acusa aviso novo de número ou ano; os dois erros novos são A092 e A093 com confiança baixa ainda sem revisão registrada.

**Nenhum veredito mudou.** Mudaram confiança, resumo, ressalva, explicação e fontes de dez checagens. As notas por checagem, inclusive dos pares examinados e mantidos, estão em `revisao-coerencia.json`.

## A110 (lote 09), resumo, ressalva, explicação e fontes · par A089, A098

- **Estava:** resumo "A PF investigava o Master desde 2024; o contrato da família de Lewandowski com o banco foi até setembro de 2025"; ressalva "As fontes não dão o mês em que a investigação começou e tratam da investigação do banco, que Vorcaro controlava"; três fontes (SBT News da liquidação, Migalhas, Metrópoles).
- **Passou a valer:** resumo "A PF de São Paulo investigava o Master desde 2023; o contrato da família de Lewandowski foi até setembro de 2025"; ressalva "Os inquéritos de 2023 constam de documento obtido pelo SBT News e tratam do Master e de fundos usados por Vorcaro"; entrou a reportagem do SBT News (coluna Nathalia Fruet, captura p08), com o mesmo trecho das checagens A089 e A098; explicação e data de referência refeitas.
- **Por quê:** a entrevistadora fala da investigação da PF três vezes em dois minutos (A089, A098, A110). Nos dois primeiros cards o vídeo diz "abertos desde 2023"; no terceiro dizia "desde 2024" e que as fontes não davam a data. Lidos em sequência, os cards se contradiziam sobre o mesmo fato, e a fonte que resolve já estava no caso.

## A116 (lote 09), confiança, ressalva, explicação e fontes · par A118

- **Estava:** confiança média; ressalva "As reportagens tratam do piso por família; não foi conferido se algum adicional mudou antes".
- **Passou a valer:** confiança alta; sem ressalva; entraram o Decreto 13.120 e a reportagem do Congresso em Foco, os mesmos da checagem A118.
- **Por quê:** é o mesmo fato (o reajuste de setembro de 2026 foi o primeiro do mandato) dito pela entrevistadora (A116) e pelo candidato (A118). A118 tinha confiança alta com o decreto, que corrige todos os componentes desde março de 2023; A116 tinha confiança média e uma ressalva sobre os adicionais que a fonte de A118 responde. O lado da mesa que acertou o mesmo fato recebia um card mais fraco.

## A092 e A093 (lote 08), confiança, resumo e explicação · par A085, A103

- **Estava:** A092 com confiança média e resumo "O único registro da bronca a Andrei Rodrigues é a fala do próprio Lula; não há nota oficial sobre ela"; A093 com confiança média e resumo "Não há registro público do alerta ao ministro da Justiça além da fala do próprio Lula na sabatina". Sem o prefixo de provisório. A explicação de A092 terminava com "A busca desta rodada foi limitada e não achou outro relato".
- **Passou a valer:** confiança baixa; explicação começando por "Busca interrompida pelo limite de buscas da rodada de 16/out; veredito provisório, a refazer:"; resumos "Não foi achado registro da bronca a Andrei Rodrigues além da fala do próprio Lula, nem nota oficial sobre ela" e "Não foi achado registro público do alerta ao ministro da Justiça além da fala do próprio Lula na sabatina". Veredito `INSUSTENTAVEL` mantido.
- **Por quê:** a regra de provisórios do caso (INSUSTENTAVEL por busca não exaustiva leva confiança baixa e o prefixo) já valia para A085 (as três conversas de Lula com Fachin, mesmo tipo de afirmação) e para A103, e a r4 citou A085 como "mesma régua" sem igualar o tratamento. A092 declarava a busca limitada; A093 é a mesma frase, o mesmo episódio e o mesmo lote. "Não há registro" afirma uma ausência que a busca interrompida não provou; "não foi achado" é o padrão dos cards provisórios (r4 em A103, r8 em A029).

## A103 (lote 08), explicação

- **Estava:** "... veredito provisório, a refazer. Revisão r4: entraram duas capturas ..."
- **Passou a valer:** "... veredito provisório, a refazer: na revisão r4 entraram duas capturas ..."
- **Por quê:** o prefixo de provisório é o mesmo em todas as checagens do caso, terminado em dois-pontos; esta era a única fora do formato.

## A065 (lote 05), ressalva, explicação e fontes · par A070, A081, A084, A115

- **Estava:** ressalva "As fontes não medem se Lula evitou o tema antes; a parte checada é o uso da palavra depois do 1º turno".
- **Passou a valer:** ressalva "Em 18 de setembro, antes do 1º turno, Lula já dizia que cinco ministros do STF estavam ligados ao caso Master"; entrou o Diario de Pernambuco de 18/09/2026 (captura p07, já usado em A081 e A084) com o trecho em que Lula diz que cinco ministros estão ligados direta ou indiretamente ao caso e cita Moraes e Toffoli; a explicação registra também as falas de 3 e 9 de setembro (A070). Veredito `VERDADEIRO` mantido, sobre o uso da palavra depois do 1º turno; a demora não é julgada, porque as fontes não datam o começo das suspeitas sobre ministros.
- **Por quê:** a ressalva dizia que as fontes não mediam o que outras checagens do mesmo vídeo mostram. Lido sozinho, o card verde dava a impressão de que Lula não tinha comentado com clareza antes do 1º turno; A070 e A115, mais adiante, mostram falas de setembro sobre o mesmo assunto.

## A030 (lote 03), ressalva, explicação, fontes e derivação · par A143

- **Estava:** sem ressalva; "os dois tinham 80 anos na data da fala".
- **Passou a valer:** ressalva "Alguns documentos registram o nascimento de Lula em 6 de outubro; por essa data ele teria 81 anos"; entrou a fonte TVT News e a derivação dos 81 anos, as mesmas de A143. Veredito `VERDADEIRO` mantido ("cerca de 80 anos").
- **Por quê:** a idade de Lula aparece duas vezes no vídeo (A030 e A143). A143 trazia a ressalva da data de registro; A030 não. O próprio arquivo do TSE usado em A001 registra 06/10/1945.

## A006 (lote 01), confiança · par A147

- **Estava:** confiança média.
- **Passou a valer:** confiança alta.
- **Por quê:** A006 e A147 conferem o mesmo ponto (7ª economia em 2010) com as mesmas duas séries do Banco Mundial e do FMI, e A147 tinha confiança alta.

## A046 (lote 04), explicação · par A035, A148, A154, A190

- **Estava:** "um desvio de cerca de 11,5% sobre o número dito".
- **Passou a valer:** "um desvio de cerca de 13% medido sobre o valor apurado (7,7 sobre 59)".
- **Por quê:** todas as outras contas de desvio do caso medem sobre o valor apurado (A008, A035, A036, A148, A150, A154, A188, A190), e A148 já tinha sido corrigida na r6 por usar bases diferentes. Pelas duas bases o desvio passa de 10%, então o veredito `IMPRECISO` não muda.

## A163 (lote 13), resumo · par A037, A038, A039, A178

- **Estava:** "Na PIA do IBGE, a compra de energia elétrica foi 1,05% dos custos da indústria em 2023; matérias-primas, 46%".
- **Passou a valer:** "Na PIA do IBGE, energia elétrica foi 1,05% dos custos da indústria em 2023 e matérias-primas, 46%; sem segunda fonte".
- **Por quê:** é provisório pelo mesmo motivo dos cards do candidato com uma base oficial só (A037 a A039, "sem segunda fonte"; A178, "falta uma segunda fonte independente"). Sem isso, o card laranja da entrevistadora, com um dado oficial que aponta contra a frase, não dizia por que não é vermelho.

## Para o autor, sem mudança feita

- **A032** segue com o erro do validador "nenhuma fonte N1 ou N2" (já estava antes desta passada). A comparação entre lotes não pede mudança: contagem de encontros públicos com data, confirmada por redações independentes, recebeu o mesmo tratamento que a contagem de tempo da entrevistadora em A140 (só imprensa, `VERDADEIRO`). É diferente de A017 (composição partidária do Senado, que tem registro oficial e ficou provisória). Fica para o autor decidir entre aceitar o aviso como exceção declarada ou buscar fonte oficial dos três encontros.
- **A026** tem, dentro da própria checagem, "agosto de 2025" no resumo e "julho de 2025" no número apurado para a mesma tarifa de 40% (ordem de 30/07, vigência em 06/08). Não é divergência entre lotes e não foi tocada.
