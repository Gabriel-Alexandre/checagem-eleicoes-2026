# Correções da revisão adversarial da rodada 3 (17/out/2026)

Passada separada sobre as duas checagens fechadas na rodada 2, parte rodada3 (`rodada2-rodada3.md`): A161 (lote 17, corte 04) e A113 (lote 12). O revisor não checou essas alegações antes. Sem busca web (zero chamadas) e sem fonte nova: só o que está nas pastas `capturas/2026-10-16-sabatina-flavio-globo-2turno-r2rodada3*` e nas capturas das rodadas anteriores. Depois das mudanças, os lotes 12 e 17 validam contra `esquemas/checagens.schema.json`. Todos os trechos das duas checagens (8 da A161, 11 da A113) foram achados no texto capturado da própria URL com a função `conferir` de `ferramentas/conferir-trechos.py`. Número e ano do resumo, da ressalva e do `numero_apurado` têm lastro, as parcelas das derivações estão nos trechos ou na fala, e não há travessão nem leitura de intenção. Os arquivos juntados (`checagens-sabatina-completa.json`, `checagens-corte-04.json`) não foram regerados aqui.

## A113 · Estava · Passou a valer · Por quê

- **Estava:** VERDADEIRO. Resumo: "As 27 superintendências da PF trocaram de chefe no governo atual, em etapas: 21 até março de 2023 e o RS em 2025". Confiança média.
- **Passou a valer:** IMPRECISO. Resumo: "O Diário Oficial registra 21 das 27 superintendências da PF trocadas até março de 2023, não as 27". Ressalva: "Até 2025 o Diário Oficial soma 22 trocas; outras cinco só aparecem numa fonte de imprensa, sem ato conferido". O número apurado, a explicação, a divergência e as derivações também mudaram: entram 22 = 21 mais 1, o desvio de 22% e o de 19%. Confiança média.
- **Por quê:** o Diário Oficial (N1) documenta 22 trocas: 18 no ato de 18/01/2023, mais Distrito Federal, Bahia e Roraima até 07/03/2023, mais o Rio Grande do Sul em 12/11/2025. Isso foi conferido de novo nas capturas `-r2rodada3-r6` e `-r8`, estado por estado. As outras cinco (Acre, Amapá, Ceará, Espírito Santo e Piauí) só entram pelo Portal Tela, que é fonte única e de imprensa, e o texto vem marcado na página como "Gerado por Telinha" e revisado pela redação. A matéria não cita ato oficial, e o próprio Diário Oficial desmente a "única exceção" do Rio Grande do Sul que ela aponta. Pelas regras 1 a 3 da §3.1, ela não fecha o número 27.
  - **O recorte de tempo:** a frase vem logo depois de "a primeira coisa que o meu adversário fez quando sentou na cadeira [...] foi botar o amigo dele, Andrei", e a extração, feita antes da checagem, leu "no início do governo Lula". Nessa leitura, o registro dá 21, não 27 (desvio de 22%). A rodada 2 adotou a leitura da gestão inteira depois de ver o resultado (§5). Mesmo nessa leitura, o documentado chega a 22 (desvio de 19%), e a troca do Rio Grande do Sul é de quase três anos depois da posse.
  - **A régua:** nas duas leituras, o desvio passa de 10% (§2.2), e o essencial confere: houve troca em massa no início da gestão Andrei, muito acima de "um". É a régua da A036 (o registro oficial confirma a ordem de grandeza e corrige o número).
  - **Por que não INSUSTENTAVEL:** a A114 e a A037 ficaram INSUSTENTAVEL porque só tinham imprensa. Aqui há N1 para o essencial e para o número apurado.
  - **Por que não FALSO:** nada inverte a frase, e as cinco superintendências sem ato conferido podem ter sido trocadas.
  - **O que falta:** com os atos dessas cinco no Diário Oficial, a leitura da gestão inteira daria 27.
- **Pendente fora do escopo desta passada:** a explicação da A114 ainda diz "a mesma régua da A113 (as 27 trocas atribuídas a Lula, só com imprensa)". Isso descreve a A113 da rodada 1 e precisa ser atualizado por quem puder editar a A114. O veredito da A114 não muda.

## A161 · Estava · Passou a valer · Por quê

- **Estava:** VERDADEIRO, com confiança média e o mesmo resumo e a mesma ressalva.
- **Passou a valer:** continua VERDADEIRO, sem mudança no resumo, na ressalva, nas fontes nem na confiança. Entram duas frases na explicação e uma na divergência:
  - **Na explicação:** os rótulos do gráfico são arredondados, não truncados, porque o próprio 2024 (2.436.190) aparece como 2,44 milhões. Logo, os 2,43 milhões de 2018 ficam abaixo de 2.435.000. A atribuição dos rótulos aos anos foi conferida de novo na página renderizada.
  - **Na divergência:** o boletim do 2º quadrimestre de 2025 dá percentuais (queda de 4,5% sobre o quadrimestre anterior, alta de 12,9% sobre 2024) que não fecham com 973.330 e 830.525. Isso mostra que a série é revista a cada edição, sem mudar a conclusão.
- **Por quê:**
  - **O ataque principal:** o valor de 2018 é um rótulo de gráfico. O rótulo "2,43Mi" está no texto capturado do PDF (o trecho existe, regra 5). A ligação entre o rótulo e o ano 2018 foi conferida aqui, renderizando as páginas dos dois boletins: no gráfico de 2014 a 2024, a linha de fechadas marca 2,43 em 2018 e 2,44 em 2024, e no de 2010 a 2020, 2,42 em 2018.
  - **O furo que havia:** a explicação dizia que 2.436.190 "fica acima de qualquer valor que arredonde para 2,43 milhões", mas não mostrava que o gráfico arredonda. Se os rótulos fossem truncados, 2018 poderia chegar a 2.439.999 e passar 2024. O rótulo do próprio 2024 (2,44 para 2.436.190) prova que o gráfico arredonda, e a ordem entre 2024 e 2018 sai do mesmo gráfico, na mesma revisão da série. A frase entrou na explicação.
  - **As fontes:** o Sebrae (N2, independente) cobre só de 2019 a 2024. Para o pico de 2018 a fonte é uma só, o Mapa de Empresas, em duas edições. A regra 1 fica atendida para a alegação (N1 mais N2 independentes, as duas com 2024 no topo do que cobrem), e a comparação com 2018 está no registro primário.
  - **A margem e a ressalva:** a margem é pequena e o resumo mostra os dois números (2.436.190 contra 2,43 milhões), então o card não esconde o quase empate. A ressalva cobre o número absoluto, o MEI, as baixas de ofício e o saldo positivo.
  - **O ano de 2025:** janeiro a agosto de 2025 está acima do mesmo período de 2024 mesmo com as revisões da série. Se o total de 2025 tiver passado o de 2024, o recorde continua no governo atual.

## A114 (lote 12), explicação · par A113

- **Estava:** "passou a INSUSTENTAVEL pela mesma régua da A113 (as 27 trocas atribuídas a Lula, só com imprensa), [...]"
- **Passou a valer:** a explicação diz que a A113 ganhou o Diário Oficial na rodada 3 e passou a IMPRECISO, e que a parte de 2020 desta comparação continua sem fonte N1 ou N2; o veredito da A114 não muda.
- **Por quê:** o revisor da rodada 3 apontou que a explicação descrevia a A113 de antes da rodada 3. Feito pela IA que conduz o caso.
