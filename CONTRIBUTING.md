# Como contribuir

Há duas formas de contribuir com este projeto, e a primeira vale mais que a segunda.

---

## 1. Contestar um veredito

**É a contribuição mais valiosa.** Todo veredito aqui é uma afirmação sobre o mundo, com fontes abertas, e existe para poder ser contestado.

Abra uma **issue** com:

- o **id** da alegação (`A012`) e o caso (`2026-08-27-sabatina-lula-globo`);
- **a fonte** que sustenta a contestação, com URL e o trecho relevante;
- o que, especificamente, você acha que está errado: o veredito, o número, o recorte temporal, a leitura da frase, a escolha da fonte.

⛔ **O que não move a agulha:** "isso está errado", "vocês são tendenciosos", "faltou contexto" sem dizer qual. A resposta é dada com fonte, não com opinião, e para isso a contestação precisa ter fonte também.

✅ **O que acontece se você tiver razão:** entra uma linha em `casos/<slug>/CORRECOES.md`, com data, o que estava escrito e o que passou a valer; o relatório é corrigido; e o vídeo, quando possível, é refeito. **Nada é apagado em silêncio.**

> 🔑 Um veredito que muda porque a evidência mudou é o processo funcionando. Um veredito que muda sem registro é o processo quebrado.

---

## 2. Mexer no código ou na documentação

### Antes de abrir o editor

Leia, nesta ordem:

1. [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md) — é o documento que manda. Qualquer código que a contrarie está errado.
2. [`ESTADO.md`](ESTADO.md) — onde o trabalho parou e o que já quebrou uma vez.
3. [`docs/ARQUITETURA.md`](docs/ARQUITETURA.md) — por que cada decisão técnica é o que é. Se você for mudar uma delas, mude sabendo o que ela estava segurando.

### Antes de abrir o PR

```bash
pip install -r requirements.txt -r requirements-dev.txt
ruff check src tests ferramentas
pytest -q
python ferramentas/conferir-links.py
python -m checagem validar 2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
```

Os quatro têm que passar. O último é a porta: ⛔ **nada é dado por pronto com ele reprovando.**

### O que faz um PR ser recusado

| | |
|---|---|
| ⛔ Afrouxar uma trava para um caso passar | o problema é o caso, não a trava |
| ⛔ Remover um teste em vez de consertar o código | os testes de `test_caso_real.py` são a doutrina em código |
| ⛔ Adicionar dependência de nuvem no caminho crítico | só a busca de fontes precisa de internet, e por definição |
| ⛔ Escrever número sem fonte, mesmo em documentação | vale para o repositório inteiro, não só para as checagens |
| ⛔ Mudar constante de tela por causa de um caso | as constantes de `config.py` valem para o projeto; caso específico se resolve na extração |
| ⛔ Editar doutrina no ponteiro de `.claude/skills/` | a fonte é `skills/`; o ponteiro é só ponteiro |

### O que sempre é bem-vindo

- **Um caso novo**, com procedência conferida e o validador passando.
- **Uma trava nova no validador**, com o teste que a prova e a linha correspondente na metodologia.
- **Uma armadilha de fonte** documentada em [`docs/FONTES_BRASIL.md`](docs/FONTES_BRASIL.md): estoque contra fluxo, mudança de metodologia, recorte temporal.
- **Um defeito que você encontrou olhando o vídeo.** Os validadores conferem texto de JSON; eles não veem a imagem, e três defeitos reais desta primeira rodada só apareceram no olho.

---

## 3. Estilo

- **Português**, em código, comentário, commit e documentação. O projeto é sobre debate público brasileiro; a barreira de idioma não ajuda ninguém aqui.
- **Comentário explica por quê, não o quê.** Se o código precisa de comentário para dizer o que faz, reescreva o código.
- **Mensagem de commit no imperativo**, dizendo o efeito: `conserta a fila de cartelas quando duas alegações saem da mesma frase`.
- ⛔ **Travessão em nome de arquivo, nunca.** Hífen simples.
- Nomes de arquivo: documento em `SCREAMING_SNAKE_CASE.md`, skill e regra em `kebab-case`, módulo em `passoN_nome.py`.

---

## 4. Uma nota sobre ano eleitoral

Este repositório checa fala de candidato durante uma campanha. O erro aqui não é neutro: **ele beneficia alguém.**

Por isso, três coisas não são negociáveis em nenhuma contribuição:

1. ⛔ **A régua é a mesma para os dois lados da mesa.** Pergunta de jornalista que afirma fato é alegação, e o relatório publica a contagem por papel justamente para que um desequilíbrio fique visível.
2. ⛔ **Nada de julgar intenção.** O card fala do enunciado.
3. ⛔ **Nenhuma saída deste repositório conclui "mentiu N vezes"** sobre ninguém, nem no relatório, nem em peça de divulgação.

Leia [`.cursor/rules/etica-e-risco.mdc`](.cursor/rules/etica-e-risco.mdc) antes de qualquer contribuição com decisão editorial.
