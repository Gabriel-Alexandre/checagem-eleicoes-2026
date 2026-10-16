# Correções da revisão r2 (lotes 04 e 05)

Revisão adversarial por IA, passada separada, em 16/10/2026, seguindo `skills/revisar-checagem.md`. Sem busca web nesta rodada: a fonte nova abaixo já estava capturada em `capturas/2026-10-15-sabatina-lula-globo-2turno-p05`, e o trecho foi conferido contra o texto capturado com a mesma normalização de `ferramentas/conferir-trechos.py`. Nenhum veredito mudou. As notas por checagem (A040 a A065) estão em `revisao-r2.json`.

## A042 (lote 04), explicação

- **Estava:** "o governo já acionou o rito da lei (consultas e análise na Camex), em 2025 e em 2026; o que não houve foi a retaliação."
- **Passou a valer:** "o governo já acionou o rito da lei, com a abertura formal do processo em 13 de agosto de 2026; o que não houve foi a retaliação."
- **Por quê:** METODOLOGIA §1 (nenhum veredito nasce da memória do modelo) e pergunta 7 do roteiro. Nenhum trecho das cinco fontes registra acionamento da lei em 2025, nem consultas na Camex; a abertura de 13/08/2026 tem lastro no trecho da Band. Veredito, resumo e ressalva sem mudança.

## A057 (lote 05), fontes

- **Estava:** 3 fontes (Diário do Nordeste, Gazeta do Povo, Poder360). O campo `divergencia_entre_fontes` citava o Congresso em Foco ("diz que foi em abril"), que não estava na lista.
- **Passou a valer:** 4 fontes. Entrou Congresso em Foco (N4), "Ex-ministro de Lula, Camilo Santana assume liderança do PT no Senado" (captura p05 `0264a4417ba2`), com o trecho "Camilo Santana já ocupava a vice-liderança desde abril, quando retomou seu mandato no Senado. O parlamentar estava afastado para comando do Ministério da Educação desde 2023."
- **Por quê:** pergunta 3 do roteiro. A divergência registrada não tinha trecho de fonte; agora as duas datas (junho no Poder360, abril no Congresso em Foco) estão nas fontes, e o novo trecho confirma também que ele foi ministro da Educação. Veredito, resumo e ressalva sem mudança.

## Registrado sem mudança no lote

- **A042, arquivo de alegações:** a `afirmacao` ("O governo Lula não acionou a lei da reciprocidade contra os Estados Unidos") é mais larga que a frase, que trata de aplicar a retaliação. A checagem avaliou a frase no contexto, e o card está certo; o ajuste da `afirmacao` é da extração, fora dos lotes.
- **A063:** checagem provisória. Ao refazer, a régua de "bastante" deve ser a mesma da A053 (ocasiões distintas bastaram lá), além da contagem comparada que o critério previa.
- **A064:** fica INSUSTENTAVEL por simetria com A074 e A076 (falas de Lula sobre ministros e pessoas citadas no caso Master, também INSUSTENTAVEL pela ética §5). Se o autor decidir que a existência de suspeitas é fato concluído, as três mudam juntas.
