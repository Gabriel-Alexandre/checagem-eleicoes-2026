# De onde vêm os critérios deste caso

Os dois critérios deste caso **não foram escritos para ele**. Foram registrados no caso da sabatina de Lula (`2026-10-15-sabatina-lula-globo-2turno`) na manhã de 15/out/2026, antes das duas sabatinas do 2º turno (Lula às 21h15 de 15/out, Flávio Bolsonaro às 21h15 de 16/out), e copiados para cá em 17/out/2026 **sem mudar um caractere**, por pedido do autor: a mesma régua nas duas entrevistas.

| Arquivo deste caso | Copiado de | Commits que o registraram antes das sabatinas | sha256 (igual nos dois casos) |
|---|---|---|---|
| `recortes/SELECAO_DE_CORTES.md` | o arquivo de mesmo nome do caso de 15/out | `37cdb3f` (15/out, 10h07, o critério), `5812ef4` (10h08, 15 s recomendados), `5fad751` e `552b9a4` (10h56, só o horário escrito do ajuste, de "10h40" para "10h08", conferido no `git log`; o critério não mudou) | `a75bb9fa8eaa0ac4…` |
| `consideracoes/CRITERIOS.md` | o arquivo de mesmo nome do caso de 15/out | `37cdb3f` (15/out, 10h07) | `da9cc1fa10f7282a…` |

Como conferir: `git log --format='%h %ad %s' -- casos/2026-10-15-sabatina-lula-globo-2turno/recortes/SELECAO_DE_CORTES.md` e `sha256sum` dos dois pares de arquivos. O próprio `CRITERIOS.md` já dizia, antes das sabatinas, que ele vale *"sem mudar uma vírgula"* para a de Flávio Bolsonaro.

⚠️ O texto dos dois arquivos fala em "onze horas antes de a sabatina começar". Isso é de quando foram escritos, para a sabatina de 15/out; para esta, eles foram registrados cerca de 35 horas antes. O texto fica como está, porque mudar uma palavra quebraria a prova de que é o mesmo critério.

A sugestão de cortes deste caso (`recortes/SUGESTAO_DE_CORTES.md`) é commitada **antes do primeiro veredito**; o horário desse commit é a outra metade da prova.
