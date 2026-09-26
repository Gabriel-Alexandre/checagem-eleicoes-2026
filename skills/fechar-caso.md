---
name: fechar-caso
description: PASSOS 6 a 8 do pipeline, mais a revisão final. Desenha as cartelas do overlay, renderiza o vídeo anotado em Full HD, roda o validador, gera o RELATORIO.md do caso e faz a conferência visual quadro a quadro antes de qualquer publicação. Use quando as checagens estiverem escritas e o próximo passo for ver o vídeo pronto. Não escreve veredito nem busca fonte: para isso são extrair-alegacoes e checar-alegacao.
---

# fechar-caso — PASSOS 6 a 8

## O que esta skill entrega

`casos/<slug>/render/<slug>-checado[-recorte].mp4` em 1920x1080, com moldura colorida e tarja de
checagem, mais o `RELATORIO.md` do caso e o validador passando com 0 erros.

---

## PASSO 6 · desenhar as cartelas

```bash
python -m checagem overlay <slug> --recorte <id>
```

Cada cartela é um **quadro inteiro** de 1920x1080 transparente, já com moldura e tarja no lugar.
Saem em `overlay/cartelas-<recorte>/` e o `plano-<recorte>.json` diz quando cada uma entra e sai.

**Olhe os avisos.** `A007: citacao não cabe em duas linhas` quer dizer que a citação sairia
cortada com reticências: escreva `citacao_card` (PASSO 4), nunca aumente o limite de linhas.

`A012 fica só 1,8s na tela` quer dizer que duas falas checadas estão coladas.
Não é para ignorar: card que ninguém consegue ler é ruído colorido. Conserto possível:

- juntar duas alegações que são a mesma coisa checável (volta ao PASSO 4);
- aceitar, quando a fala seguinte é do mesmo assunto e o espectador já tem o contexto.

⛔ **Não conserte encurtando a permanência dos outros cards.** As constantes de tempo estão em
`src/checagem/config.py` e valem para o projeto inteiro; mexer nelas por causa de um caso é criar
duas réguas.

## PASSO 7 · renderizar

```bash
python -m checagem renderizar <slug> --recorte <id>
```

`libx264 crf 16 preset slow`, `yuv420p`, áudio **copiado** sem reencodar, `+faststart`.
O script confere sozinho que a duração de saída casa com a de entrada, **mais os segundos da
cartela de encerramento**, e que a faixa de áudio sobreviveu.

🔧 **A cartela de encerramento** fica sobre o último quadro congelado, depois do fim do trecho:
diz onde conferir as fontes, como contestar e **quantas checagens tiveram revisão humana**. Ela é
acrescentada ao fim, e não sobreposta, para nunca disputar a tela com um card. O áudio continua
copiado; ele simplesmente acaba antes do vídeo.

⏱️ ~1 a 3 min para 5 minutos de vídeo. Uma peça de 45 min leva de 20 a 40 min.

## PASSO 8 · validar

```bash
python -m checagem validar <slug> --recorte <id>
python -m checagem relatorio <slug> --recorte <id>
```

O validador é a porta e sai com código 1 se achar erro. ⛔ Nada é publicado com ele reprovando.

---

## 🔴 A conferência com o olho, que os números não substituem

> Esta seção existe porque validador confere **texto de JSON**; ele não vê a imagem. Um card que
> cobre a legenda da emissora, um texto que estoura a caixa, uma moldura verde numa fala que a
> tarja diz ser falsa: nada disso reprova em validador nenhum.

Extraia quadros no meio de cada card e **olhe**:

```bash
ffmpeg -v error -ss <t> -i render/<arquivo>.mp4 -frames:v 1 -y /tmp/q.png
```

| Confira | Reprova quando |
|---|---|
| a moldura tem a cor do veredito da tarja | verde na moldura e FALSO na tarja |
| a citação cabe em 2 linhas e termina com sentido | corta no meio de um número |
| o card não cobre o rodapé de crédito da emissora | tapa a assinatura da fonte original |
| o texto não estoura a caixa | qualquer letra encostando na borda |
| a legenda de abertura aparece e sai | fica presa, ou nunca aparece |
| o áudio está lá e sincronizado | vídeo mudo, ou fala fora do card |
| o primeiro e o último quadro estão íntegros | quadro preto na ponta |

⚠️ **Confira também um quadro de intervalo**, entre dois cards: ali não pode sobrar moldura nem
resto de tarja.

---

## O relatório e a publicação

O `RELATORIO.md` é o que sustenta a frase "as fontes estão no repositório". Ele traz a contagem,
cada alegação com veredito, a análise inteira e o trecho copiado de cada fonte.

> 🔴 **A contagem é dado do caso, não veredito sobre a pessoa.** ⛔ O relatório não escreve "o
> candidato mentiu N vezes" como conclusão, e a peça de divulgação também não. Ver
> `docs/METODOLOGIA.md` §8.

Antes de publicar, três coisas que não são técnicas:

1. **Uma pessoa leu os cards e as fontes**, e registrou isso:
   `python ferramentas/registrar-revisao.py <slug> --recorte <id> --revisor "Nome"`. A skill
   `checar-alegacao` produz; a publicação é decisão humana. ⛔ A IA não preenche este campo em
   nome de ninguém. Depois de registrar, rode o PASSO 6 de novo: a cartela de encerramento
   mostra a contagem.
2. **Direito de resposta declarado.** O `README` do caso diz como contestar e o que acontece
   quando a contestação procede.
3. **O vídeo aponta para o repositório.** Card sem fonte visível vira acusação sem lastro; a marca
   permanente no canto e a descrição levam a quem quiser conferir.

---

## Antes de dar por fechado

- [ ] `validar` sai com 0 erros, e cada aviso foi lido e resolvido ou justificado
- [ ] `python ferramentas/validar-todos.py` passa (é o que a CI roda)
- [ ] avisos de card curto foram lidos e decididos, um a um
- [ ] conferi com o olho ao menos um quadro por card, e um de intervalo
- [ ] o MP4 tem áudio, tem 1920x1080 e a mesma duração da entrada
- [ ] `RELATORIO.md` gerado, com todas as fontes clicáveis
- [ ] `ESTADO.md` atualizado com o que ficou pronto e o que falta
