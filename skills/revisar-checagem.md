---
name: revisar-checagem
description: Revisão adversarial, feita pela própria IA, de cada checagem já escrita. Roda depois de checar-alegacao e antes de fechar-caso, em passada separada, e tenta DERRUBAR cada veredito relendo a fala, os trechos capturados e a régua da metodologia. Registra o resultado em `revisao_ia` com ferramentas/registrar-revisao.py --ia. Não busca fonte nova para confirmar o que já foi decidido; busca, sim, o que contradiria.
---

# revisar-checagem: a revisão por IA

🔧 **Desde 27/set/2026 a revisão do projeto é feita pela própria IA**, por decisão do autor. Ela substitui a exigência de uma pessoa ler cada card antes de publicar. Para funcionar como revisão, e não como carimbo, ela tem três travas.

## 🔴 As três travas

1. **Passada separada.** A revisão não acontece no mesmo passo em que o veredito foi escrito. Releia do zero: a `frase` na transcrição, cada `trecho` na página capturada, a régua.
2. **Postura adversarial.** O objetivo é derrubar o veredito. Para cada checagem, escreva o melhor argumento contra ele e diga por que ele cai ou fica de pé.
3. **Registro com nota.** Toda revisão vai para `revisao_ia`, com uma nota que diga o que foi conferido e o que se decidiu. "Ok" não é nota. Veredito mudado vai também para `CORRECOES.md`.

## O roteiro, checagem por checagem

| # | Pergunta | Se falhar |
|---|---|---|
| 1 | A `frase` é o que a pessoa disse, no contexto em que disse? A `afirmacao` não estica nem encolhe a frase? | refazer a extração daquela alegação |
| 2 | É fato, e não juízo, promessa ou hipótese (METODOLOGIA §4.2)? | remover, com registro |
| 3 | Cada `trecho` está na página capturada (`CAPTURAS.json` diz "encontrado") e prova o que a coluna `prova` diz? | trocar a fonte ou rebaixar o veredito |
| 4 | Há ao menos duas fontes independentes, e N1/N2 quando é número? Alguma fonte primária contradiz as secundárias? | a primária ganha; registrar a divergência |
| 5 | A data do dado é a que valia na data da fala? | refazer com o dado da data certa |
| 6 | O veredito segue a árvore do §2.1 e a régua de 10% do §2.2? A mesma régua foi usada nos dois lados da mesa e nos outros casos? | ajustar o veredito |
| 7 | Resumo e ressalva: todo número e todo ano têm lastro? Há leitura de intenção, travessão, adjetivo? | reescrever |
| 8 | O card, lido sozinho em cinco segundos, deixa o espectador com a impressão certa? | reescrever o resumo |

## Registro

```bash
python ferramentas/registrar-revisao.py <slug> --recorte <id> --ia --notas revisao.json
python -m checagem validar <slug> --recorte <id>      # avisa se faltou revisão
```

`revisao.json`: `{"revisor": "Claude (revisão adversarial por IA, passada separada)", "A001": {"decisao": "mantido", "nota": "...", "verificacoes": ["1", "3", "5"]}}`

## O que esta revisão não é

⛔ Não é releitura de cortesia do próprio texto. ⛔ Não é busca de fonte para confirmar o veredito. ⛔ Não publica: publicar continua sendo decisão do autor do projeto.
