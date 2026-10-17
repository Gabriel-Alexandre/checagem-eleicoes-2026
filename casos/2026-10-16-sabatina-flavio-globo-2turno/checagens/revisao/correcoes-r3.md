# Correções da revisão r3 (lotes 07, 08 e 09, A061 a A090)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. O revisor não checou nenhuma destas alegações. **Nenhum veredito mudou.** As mudanças são de confiança, resumo, explicação, data de referência, número apurado e fontes. Toda fonte nova abaixo já estava capturada nas pastas `capturas/2026-10-16-sabatina-flavio-globo-2turno-p07-r2` e `-p08-r2`. Os 113 trechos dos três lotes, antigos e novos, foram conferidos contra o texto capturado, por palavra inteira, com a normalização de `ferramentas/conferir-trechos.py`, e todos foram encontrados. Os três lotes passam no `esquemas/checagens.schema.json`. Houve uma busca web, atrás do que contradiria a A090 (fonte com os 160 milhões ou com o contrato de Huck), e ela não achou nenhuma. As notas por checagem estão em `revisao-r3.json`.

Provisórios conferidos, com o marcador exato e a confiança baixa: A062, A071, A072 e A086. Não foram refeitos.

## A063 (lote 07), confiança

- **Estava:** `alta`.
- **Passou a valer:** `media`.
- **Por quê:** as quatro fontes são N4, e a parte "não só a investigação" exige interpretação (o pedido formal à PGR e ao STF aparece como iniciativa da liderança da oposição). Pela skill `checar-alegacao`, `alta` é para N1 direta e inequívoca. O veredito `VERDADEIRO` fica: o essencial é a defesa do impeachment.

## A067 (lote 07), resumo

- **Estava:** "Mensagens ligam o filho de Nunes Marques a R$ 500 mil por mês via consultoria; ele admite R$ 281,6 mil e nega o resto"
- **Passou a valer:** "Mensagens ligam filho de Nunes Marques a R$ 500 mil mensais; ele diz que recebeu R$ 281,6 mil da consultoria por serviço"
- **Por quê:** "admite R$ 281,6 mil e nega o resto" podia ser lido como confissão de parte de um pagamento de Vorcaro. O trecho do Times Brasil diz que a assessoria do advogado afirma que ele recebeu R$ 281,6 mil da Consult por serviços prestados à própria empresa (pergunta 8).

## A070 (lote 07), fontes

- **Estava:** 6 fontes; a `divergencia_entre_fontes` citava o Jornal de Brasília ("o encontro resultou de apelos de líderes do PT e do ministro de Relações Institucionais") sem fonte nem trecho.
- **Passou a valer:** 7 fontes. Entrou Jornal de Brasília, "Lula tem encontro Alcolumbre, em gesto de aproximação três meses após rejeição de Messias" (captura p07-r2 `a00f3d530923`), com o trecho dos apelos de Camilo Santana, Teresa Leitão e José Guimarães e o de que o encontro foi na casa de Moraes, com Zanin.
- **Por quê:** pergunta 3; a divergência é parte da checagem e precisava de lastro. O veredito `VERDADEIRO` com ressalva fica.

## A087 (lote 09), resumo

- **Estava:** "Negociação previa US$ 24 milhões; repasse foi de US$ 10,6 milhões, com parcelas atrasadas cobradas por Flávio"
- **Passou a valer:** "Negociação previa US$ 24 milhões; os repasses documentados somam US$ 12,3 milhões, e Flávio cobrou parcelas atrasadas"
- **Por quê:** pergunta 5 (anacronismo). US$ 10,6 milhões é o total repassado até maio de 2025. Na data da fala, o Coaf, segundo o Poder360 com a piauí (01/09/2026), somava 7 parcelas e US$ 12,3 milhões, contando a de US$ 1,6 milhão de 16/09/2025. O lote 08 (A071) já usava esse total.

## A087 (lote 09), número apurado, data de referência, explicação e fontes

- **Estava:** `numero_apurado` "US$ 10,6 milhões repassados de US$ 24 milhões negociados"; `data_de_referencia` "repasses de fevereiro a maio de 2025"; explicação "o repassado foi US$ 10,6 milhões, cerca de R$ 61 milhões, de fevereiro a maio de 2025"; 3 fontes.
- **Passou a valer:** `numero_apurado` "US$ 12,3 milhões repassados em 7 parcelas (US$ 10,6 milhões até maio de 2025), de US$ 24 milhões negociados"; `data_de_referencia` "repasses de fevereiro a setembro de 2025, somados pelo Coaf e noticiados em 01/09/2026"; a explicação dá os dois totais e diz que o pago é cerca de metade do combinado; entrou Poder360, "Filme Dark Horse recebeu R$ 65 milhões de Daniel Vorcaro" (captura p08-r2 `063167ccf3af`), com o trecho da parcela de setembro e do total de US$ 12,3 milhões.
- **Por quê:** o mesmo da entrada anterior. O veredito `VERDADEIRO` fica: com US$ 12,3 milhões de US$ 24 milhões, o contrato continua não cumprido.

## A088 (lote 09), explicação e fontes

- **Estava:** "o fundo usado na captação enviou US$ 13,3 milhões, acima dos US$ 10,6 milhões atribuídos a Vorcaro"; 4 fontes.
- **Passou a valer:** "enviou US$ 13,3 milhões, acima dos US$ 12,3 milhões que o Coaf atribui a Vorcaro em 7 parcelas (Poder360, com a piauí)"; entrou a mesma fonte do Poder360 (captura p08-r2 `063167ccf3af`).
- **Por quê:** pergunta 5; a comparação usava o total de maio de 2025. Com o total vigente na data da fala a diferença diminui, mas o fundo ainda mandou ao filme mais do que Vorcaro pôs nele, e o veredito `VERDADEIRO` fica.

## Registrado sem mudança no lote

- **A080:** a explicação cita Folha Vitória e Diario de Pernambuco, que não estão entre as fontes da checagem; o que eles sustentariam já está nos trechos da TVT News e do InfoMoney.
- **A086:** provisório; o `numero_apurado` usa os US$ 10,6 milhões de maio de 2025, e a rodada 2 deve usar o total de US$ 12,3 milhões e sair com o mesmo veredito da A072, que é a mesma afirmação.
- **A089:** a transcrição em 1112,6 s registra "um dinheiro totalmente ilícito", provável erro do motor por "lícito"; a frase não foi extraída, mas merece ser ouvida.
