# Critério de escolha dos cortes, registrado ANTES da sabatina

**Escrito em 15/out/2026, às 10h, cerca de onze horas antes de a sabatina começar (21h15).** O horário do commit que contém este arquivo é a prova de que o critério não foi escolhido olhando o que foi dito, e muito menos os vereditos. ⛔ **Nada neste arquivo muda depois da sabatina.** Critério novo entra em `SELECAO_DE_CORTES_ADENDO.md`, com data e motivo, e o relatório mostra quais cortes vieram do critério original e quais do adendo.

Operação: [`docs/PECA_INTEIRA.md`](../../../docs/PECA_INTEIRA.md) §2 e §3. Quem aplica: [`ferramentas/sugerir-cortes.py`](../../../ferramentas/sugerir-cortes.py), que **não abre** o arquivo de checagens.

---

## O pedido, nas palavras dele

*"apenas alguns cortes dos trechos mais, entre aspas, polêmicos. Ou mais importantes"* · *"focar nas partes que falam mais sobre fatos"* · *"trechos bem curtos. Não pode ser trecho de, por exemplo, um minuto"* · *"pelo menos uns 5, 6 trechos diferentes. Não de continuidade"*

## O critério

Roda **depois da extração (PASSO 4) e antes da checagem (PASSO 5)**. Usa só o que existe nesse momento: a transcrição com falantes e a lista de alegações, sem veredito.

1. **Candidatas.** Toda janela que começa e termina em borda de segmento da transcrição, dura de **8 a 15 s** (até 30 s se não couberem cinco cortes; ajustado às 10h08, um minuto depois do commit original e ainda antes do evento (o horário estava escrito como 10h40, corrigido às 11h pelo `git log`), para a régua de telejornal do canal: ~10 s por trecho), **contém cada alegação inteira** (nenhuma frase cortada na borda) e tem **pelo menos uma alegação checável do candidato**.
2. **Pontos de cada janela** (sem veredito, sem tom, sem intenção):
   - **fato:** cada alegação checável vale 1,0 se for dado duro (número, série, valor, comparação, ranking) e 0,8 se for evento, norma, data ou atribuição; opinião, promessa e previsão valem 0;
   - **confronto:** +1,0 quando a jornalista afirma fato e o candidato responde com fato na mesma janela; +0,5 a mais se for o mesmo assunto;
   - **troca de turno:** +0,4 por virada entre jornalista e candidato, até 3 (o "momento quente" observável);
   - desempate: alegações checáveis por segundo, depois a que vem primeiro.
3. **Escolha:** a de mais pontos primeiro, até **6 cortes**, com **60 s** entre um e outro, **120 s** somados, e **um assunto por corte** antes de repetir assunto.
4. **Polêmico por repercussão** (o trecho que a imprensa destacou na noite, o que ele achou mais importante): entra só por `--fixar INICIO-FIM "motivo"`, com o motivo dele escrito, e o relatório mostra que veio de fora do critério.

## O que NÃO entra no critério

- ⛔ o veredito de qualquer alegação ("porque ali tem um FALSO", "porque ali ele acertou");
- ⛔ se o trecho é bom ou ruim para o candidato;
- ⛔ tom de voz, expressão, interrupção avaliada como grosseria, qualquer leitura de intenção;
- ⛔ a contagem de cortes "a favor" e "contra": a simetria aqui é de método, não de resultado.

## Depois da escolha

A ordem em que os cortes aparecem no vídeo e quais deles ele usa são **decisão editorial dele**; o repositório registra. Um corte que ele tirar continua checado, nas métricas e no relatório.
