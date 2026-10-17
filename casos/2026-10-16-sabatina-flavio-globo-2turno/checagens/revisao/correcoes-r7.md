# Correções da revisão r7 (lotes 18, 19, 20 e 21)

Revisão adversarial por IA, passada separada, em 17/10/2026, seguindo `skills/revisar-checagem.md`, sobre as alegações A171 a A207. O revisor não checou nenhuma delas. Foi feita **uma** busca web, atrás do que contradiria um veredito (A180, emissões de CRs de CACs); ela não contradisse e nada dela entrou. As duas fontes novas abaixo já estavam capturadas: `capturas/2026-10-16-sabatina-flavio-globo-2turno-p20` (Gazeta do Povo, `46c2805812fb`) e `capturas/2026-10-15-sabatina-lula-globo-2turno-p06` (Poder360, já usado na A189), e cada trecho, novo ou antigo, foi conferido por palavra inteira contra o texto capturado com a normalização de `ferramentas/conferir-trechos.py`: todos achados. Os quatro lotes validam contra `esquemas/checagens.schema.json`. **Nenhum veredito mudou.** As notas por checagem estão em `revisao-r7.json`.

## A185 (lote 19), explicação e derivação

- **Estava:** "desvio de cerca de 7% sobre quatro anos, abaixo dos 10% da régua"; derivação "44,5 meses contra 48, desvio de cerca de 7%".
- **Passou a valer:** "desvio de cerca de 8% medido sobre o período apurado (3,5 meses sobre 44,5), abaixo dos 10% da régua"; derivação "44,5 meses contra 48 ditos, desvio de cerca de 8% medido sobre o apurado (3,5 dividido por 44,5)".
- **Por quê:** pergunta 6. As contas de desvio deste caso (A011, A012, A022, A097, A120, A179) e do caso de 15/out (correção da A046 na coerência) medem sobre o valor apurado; esta media sobre o número dito. Pelas duas bases o desvio fica abaixo de 10%, e o veredito `VERDADEIRO` não muda.

## A187 (lote 19), explicação e derivação

- **Estava:** "607,88 dividido por 189 dá cerca de 3,2 vezes: 'triplicou' confere em termos nominais", sem a conta da régua.
- **Passou a valer:** "607,88 dividido por 189 dá cerca de 3,2 vezes; 'o triplo' contra 3,2 vezes é desvio de cerca de 7% sobre o apurado, e 600 contra 607,88, de cerca de 1%, os dois abaixo da régua de 10% do §2.2"; nova derivação "cerca de 7%" (de "607,88 dividido por 189, contra o triplo dito").
- **Por quê:** pergunta 6. O VERDADEIRO dependia da régua de 10% e ela não estava escrita. O veredito não muda.

## A192 (lote 20), fontes e explicação

- **Estava:** duas fontes (SBT News e Times Brasil), que reproduzem o mesmo documento da PF, não capturado.
- **Passou a valer:** entrou o Poder360, "Saiba quem é Márcio Canella, preso em operação contra lavagem de dinheiro" (15/10/2026), com o trecho "A ação mira uma organização criminosa suspeita de usar postos de combustíveis na Região Metropolitana do Rio para lavar dinheiro."; a explicação registra que é apuração própria do dia da prisão, a mesma fonte da A189.
- **Por quê:** pergunta 4 e regra 2 da §3.1: as duas fontes antigas remontam à mesma peça não capturada. A nova confirma o objeto da operação sem depender dela. O veredito `VERDADEIRO` (conteúdo da suspeita, não culpa) segue a régua da A110 do caso de 15/out e da A112 deste caso.

## A193 (lote 20), fontes e explicação

- **Estava:** o "originalmente o seu candidato" se apoiava no acordo de Jair Bolsonaro com Bacellar (Jovem Pan, 2025) e na busca de outros nomes por Flávio (Diário do Rio).
- **Passou a valer:** entrou a Gazeta do Povo, "PL define chapa pura no Rio de Janeiro após desembarque de aliados" (04/08/2026), com o trecho "Douglas Ruas assume candidatura após troca no grupo de Flávio Douglas Ruas passou a ser o nome do PL para disputar o governo do Rio depois que Rodrigo Bacellar deixou a corrida eleitoral após ser preso em operações da Polícia Federal."; a explicação cita a "troca no grupo de Flávio".
- **Por quê:** pergunta 3. O melhor argumento contra o card é que o acordo documentado era do pai, não de Flávio; a página, já capturada e não usada, liga Bacellar ao grupo de Flávio. O veredito `VERDADEIRO` e a ressalva não mudam.

## Provisórios conferidos, sem mudança

A173, A174, A191, A194, A199, A200 e A201: a explicação começa pelo marcador exato ("Busca interrompida pelo limite de buscas da rodada de 17/out/2026; veredito provisório, a refazer:") e a confiança é baixa. O que falta em cada um está na nota de `revisao-r7.json`. Nenhum veredito provisório sem marcador foi achado nos quatro lotes.
