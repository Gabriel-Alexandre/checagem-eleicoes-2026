---
name: checar-alegacao
description: PASSO 5 do pipeline. Pega alegacoes/alegacoes.json e produz checagens/checagens.json — um veredito por alegação (VERDADEIRO, IMPRECISO, INSUSTENTAVEL, FALSO ou NAO_CHECAVEL), com no mínimo duas fontes independentes, trecho copiado, URL e data de consulta. Use depois que as alegações estiverem extraídas e validadas. Busca na internet é obrigatória; memória do modelo não vale como fonte, nem para "eu sei que esse número é esse". Difere de extrair-alegacoes, que é o passo anterior e não julga nada.
---

# checar-alegacao — ponteiro

🔴 **A doutrina desta skill NÃO mora aqui.** Ela mora em [`skills/checar-alegacao.md`](../../../skills/checar-alegacao.md),
que é a convenção do repositório e a fonte única. Este arquivo existe só para tornar a skill
invocável dentro do Claude Code.

**Abra `skills/checar-alegacao.md` e siga o que está escrito lá, do começo ao fim.**

⛔ Não edite este ponteiro com regra nova: edição de doutrina vai no arquivo de `skills/`.
