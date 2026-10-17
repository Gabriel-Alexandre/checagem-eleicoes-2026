# Correções da revisão r4 (lotes 10, 11 e 12)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`. Duas buscas web, as duas atrás do que contradiria um veredito: uma sobre prisão ou processo de Vaccari por fraude em fundos de pensão (A101), outra sobre manifestação da PF, entre 9 e 16/out, que confirmasse o relato atribuído a Vorcaro (A103 e A104). A segunda não achou nada que mudasse os vereditos. A primeira achou a denúncia da Operação Greenfield, capturada em `capturas/2026-10-16-sabatina-flavio-globo-2turno-rv4` (pedido em `checagens/pedidos-captura/revisao-r4.json`). Os outros trechos novos já estavam capturados (p10 e p11/p12). Todo trecho dos três lotes, novo e antigo, foi conferido por palavra inteira contra o texto capturado da sua URL, com a normalização de `ferramentas/conferir-trechos.py` (113 de 113), e os três lotes validam contra `esquemas/checagens.schema.json`. Nenhum veredito mudou de cor; um passou a provisório (A095). As notas por checagem estão em `revisao-r4.json`.

## A094 (lote 10), explicação

- **Estava:** "O Povo e o Correio da Manhã registram o relato de cerca de R$ 30 milhões em espécie ao Instituto Lula (o valor aparece no relato e nos documentos citados pela revista, não no trecho transcrito do áudio)."
- **Passou a valer:** "(O Povo atribui o valor à própria gravação; o trecho do áudio transcrito pelo SBT News não traz o número)"
- **Por quê:** pergunta 3. O trecho do O Povo, que é fonte da própria checagem, começa por "Na gravação, Vorcaro alega ter negociado [...] um repasse de aproximadamente R$ 30 milhões"; a explicação dizia o contrário do trecho. O veredito não muda: a autenticidade do áudio e o pagamento seguem em apuração (etica-e-risco §5).

## A095 (lote 10), explicação e confiança

- **Estava:** VERDADEIRO, confiança "media", explicação sem marcador, dizendo que as regras comerciais de transparência para patrocínio "não foram localizadas em documento público dentro do limite de buscas".
- **Passou a valer:** a explicação começa por "Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:" e termina dizendo o que falta; confiança "baixa". O veredito (VERDADEIRO) fica até a rodada 2.
- **Por quê:** é um provisório de fato sem o marcador, como a A155 do caso de 15/out. A frase tem duas normas (transparência na compra de patrocínio e separação da linha editorial); só a segunda tem fonte, e a busca da primeira parou no limite. E a `citacao_card` mostra justamente a primeira ("obedecem a regras de transparência"), então o card verde ficava apoiado na metade não buscada (pergunta 8). As duas fontes são documentos do próprio Grupo Globo, o que a explicação já declarava.

## A098 (lote 10), resumo

- **Estava:** "A PF já tinha inquéritos sobre o Master e o BC o advertiu em novembro de 2024, antes do acordo; o caso segue em apuração"
- **Passou a valer:** "A PF já tinha inquéritos sobre o Master e o BC o convocou em novembro de 2024, antes do acordo; o caso segue em apuração"
- **Por quê:** pergunta 7. Os trechos falam em "termo de compromisso" e em convocação "para um termo de comparecimento"; "advertência" é nome de sanção administrativa do BC, que nenhuma fonte diz ter sido aplicada. A `prova` da fonte Finsiders ("advertência formal") foi corrigida do mesmo jeito.

## A101 (lote 11), fontes

- **Estava:** 4 fontes, todas sobre a Lava Jato e a CPI de 2016.
- **Passou a valer:** 5 fontes. Entrou Estado de Minas (com Agência Brasil), "Vaccari e mais 13 ex-diretores da Funcef se tornam réus na Operação Greenfield" (29/05/2017, captura rv4 `b9986c6a1804`): a Justiça Federal do DF aceitou a denúncia da Greenfield que tornou Vaccari réu por crimes contra o sistema financeiro e gestão fraudulenta ligados à Funcef.
- **Por quê:** a busca da revisão, feita para tentar derrubar o IMPRECISO, achou que a ligação de Vaccari com fraude em fundo de pensão é mais forte do que o card dizia: não só citação em CPI, mas ação penal. Não muda o veredito, porque a prisão continua sendo da Lava Jato e nenhuma fonte registra prisão pela Greenfield.

## A101 (lote 11), ressalva

- **Estava:** "A prisão existiu, mas pela Lava Jato; fundos de pensão aparecem só em citações na CPI de 2016"
- **Passou a valer:** "A prisão foi pela Lava Jato; por fraude na Funcef, fundo de pensão da Caixa, ele virou réu em 2017 na Operação Greenfield"
- **Por quê:** perguntas 7 e 8. A ressalva vai para a tela e diminuía, contra o candidato, o que existe no registro. O ano 2017 está no trecho novo.

## A101 (lote 11), explicação e data de referência

- **Estava:** "[...] sem prisão por isso. Nas buscas feitas não apareceu prisão de Vaccari por fraude em fundos de pensão." · data: "prisão de abril de 2015 (Lava Jato); CPI dos Fundos de Pensão de 2016"
- **Passou a valer:** a explicação acrescenta a denúncia aceita da Greenfield (maio de 2017) e diz que a acusação de fraude em fundo de pensão existe como ação penal, não como motivo de prisão · data: acrescenta "denúncia da Greenfield aceita em maio de 2017".
- **Por quê:** a mesma da fonte nova.

## A102 (lote 11), resumo

- **Estava:** "Os 10% são relato de Vorcaro em delação rejeitada, sem prova; R$ 1 bi seria a comissão, não o valor a investir"
- **Passou a valer:** "Os 10% são relato de Vorcaro em delação rejeitada, sem comprovação; R$ 1 bi seria a comissão, não o valor a investir"
- **Por quê:** pergunta 7. A própria checagem registra a divergência (a Veja diz que mensagens ajudam a corroborar o relato; a PGR não viu prova dos pagamentos). "Sem prova" afirma ausência; "sem comprovação" diz o que está documentado, e é a forma usada na A099.

## A103 e A104 (lote 11), trecho e prova da fonte TNH1

- **Estava:** o trecho do TNH1 só trazia o parágrafo dos 10% e do R$ 1 bilhão.
- **Passou a valer:** o trecho acrescenta, com `[...]`, "Mensagens encontradas pela Polícia Federal no celular de Vorcaro ajudaram a corroborar o relato de Vorcaro." e "Mensagens no celular mostram que o banqueiro foi pessoalmente ao Postalis, em Brasília, se reunir com a cúpula do fundo e também conseguiu reuniões com Petros e Previ" (mesma página, captura p10 `c2d9587bedcb`); a `prova` diz que é a leitura da revista, não manifestação da PF.
- **Por quê:** pergunta 3. A ressalva da A104 (texto de tela) e a explicação da A103 citam essas mensagens, e nenhum trecho as trazia.

## A103 (lote 11), explicação

- **Estava:** "A própria Veja (reproduzida no TNH1) só diz que mensagens obtidas pela PF registram contatos para reuniões com dirigentes de fundos, o que é diferente de a PF confirmar a oferta e a propina atribuídas a Vaccari."
- **Passou a valer:** a explicação passa a expor o melhor argumento a favor da frase (segundo a Veja, mensagens achadas pela PF "ajudaram a corroborar o relato") e diz por que ele não muda o FALSO: é a leitura da revista sobre material apreendido, as mensagens descritas tratam de contatos com dirigentes de fundos e não da oferta e da propina atribuídas a Vaccari, e a única manifestação da PF é a nota que nega ter o relato.
- **Por quê:** a explicação dizia que a Veja "só" falava de contatos, o que encolhia o texto da revista. Um FALSO contra o candidato precisa mostrar o argumento contrário mais forte.

## A106 (lote 11), ressalva e explicação

- **Estava:** ressalva nula; "A apresentadora suprimiu o palavrão e encurtou a frase, sem mudar o sentido".
- **Passou a valer:** ressalva "Na transcrição, a frase é sobre trocar alguém da segurança na ponta da linha; a citação omitiu da segurança"; a explicação registra a troca de "esperar" por "deixar" e a omissão de "da segurança", e mantém o VERDADEIRO porque a sequência citada (troca o chefe, troca o ministro) está literal na transcrição.
- **Por quê:** perguntas 1 e 6, com a mesma régua da citação aplicada aos dois lados da mesa. A palavra omitida é a que sustenta a leitura de que a fala tratava da segurança pessoal e não da PF; o espectador precisa saber que ela existe. Está no trecho do Poder360.

## A107 (lote 11), explicação

- **Estava:** "A data exata da saída não entra no card porque o Diário do Nordeste traz 23 de abril e não foi capturada uma segunda fonte com a data."
- **Passou a valer:** "A data exata da saída não entra no card: o Diário do Nordeste traz 23 de abril, e as fontes da A116 situam o pedido de demissão na manhã de 23 (A Gazeta, com Folhapress) e o anúncio em 24 de abril de 2020 (InfoMoney, Poder360)."
- **Por quê:** a frase antiga deixou de ser verdadeira dentro do próprio caso: a A116 (lote 12) tem as datas com trecho capturado (p12).

## A110 (lote 11), fontes, explicação e data de referência

- **Estava:** 4 fontes; "Se a referência for à troca de 2020, não foi achada justificativa de maus resultados, e Moro disse que nenhuma razão aceitável lhe foi apresentada." · data "agosto de 2019".
- **Passou a valer:** entrou Metrópoles, "Tácio Muzzi é nomeado superintendente da Polícia Federal no Rio de Janeiro" (26/05/2020, captura p11/p12 `3863fe826c55`), com o trecho de que o superintendente que saiu, Carlos Henrique Oliveira, foi confirmado diretor-executivo, "segundo cargo mais importante da corporação"; a explicação usa esse dado para a troca de 2020 · data "agosto de 2019 e maio de 2020".
- **Por quê:** a frase do candidato fala "na época", no contexto da reunião de 2020, e para 2020 o FALSO se apoiava só na palavra de Moro, parte na disputa. A promoção do superintendente que saiu contradiz "maus resultados" por um registro de fato, e a fonte já estava capturada (é da A109).
