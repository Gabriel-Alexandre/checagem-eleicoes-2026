# ESTADO — onde o trabalho parou

**Atualizado em:** 06/set/2026 · 🔧 11/set/2026 (duas correções de documentação, nenhuma de veredito: ver `CHANGELOG.md` 0.1.1)

Uma sessão nova consegue continuar lendo **só este arquivo**. Ele diz o que está pronto, o que falta, e o comando exato para retomar. ⛔ Ele não guarda doutrina: isso é [`docs/METODOLOGIA.md`](docs/METODOLOGIA.md).

---

## Em uma frase

O pipeline está completo e roda de ponta a ponta. **Um caso foi fechado** — o bloco de contas públicas da sabatina do dia 27 de agosto — com 23 alegações checadas, validador em zero erro e vídeo de 4min52s em Full HD renderizado.

---

## O que está pronto

| Camada | Estado |
|---|---|
| Pipeline (8 passos) | ✅ completo, rodado de ponta a ponta |
| Metodologia, arquitetura, fontes, identidade visual, replicação | ✅ escritas |
| Skills (4) e rules (4) | ✅ escritas, com espelho em `.claude/skills/` |
| Esquemas JSON (3) | ✅ `caso`, `alegacoes`, `checagens` |
| Testes | ✅ 35 passando, incluindo regressão sobre o caso real |
| CI | ✅ `.github/workflows/validar.yml` — lint, testes, validador e links |

### O caso fechado

`casos/2026-08-27-sabatina-lula-globo`

| | |
|---|---|
| Peça | Sabatina da TV Globo, 27/ago/2026, 44min33s, 1920x1080 |
| Transcrição | 709 segmentos, 7.299 palavras, `whisper.cpp` com `large-v3-turbo` |
| Correções de transcrição | 5, todas registradas com antes, depois e como foram conferidas |
| Falantes | 110 turnos, cobertura total, justificados em `NOTA_DE_ATRIBUICAO.md` |
| Trecho checado | `bloco-contas-publicas` — 22:32 a 27:24 (4min52s) |
| Alegações | 23 (18 do entrevistado, 5 da entrevistadora) + 1 exclusão declarada |
| Vereditos | 15 verdadeiro · 3 impreciso · 3 falso · 2 não checável |
| Fontes | 52 citações (33 URLs distintas, 20 instituições), com URL, data de consulta e trecho copiado · 🔧 era "56" até 11/set, número escrito sem contar |
| Validador | ✅ 0 erros, 0 avisos |
| Vídeo | ✅ 1920x1080, 30 fps, 4min52s, áudio a −28 dB, duração idêntica à entrada |

---

## ⬜ O que falta, em ordem de valor

1. **Checar os outros 40 minutos da peça.** O trecho fechado é uma prova de conceito. A peça inteira tem blocos densos sobre INSS, Banco Master, educação e segurança pública, todos ainda não extraídos.
   ```bash
   # a transcrição e os falantes da peça inteira JÁ existem: comece no PASSO 4
   # skills/extrair-alegacoes.md, cobertura de 0 a 2655s
   ```

2. **Revisão humana declarada.** Nenhuma checagem tem `revisao_humana` preenchida. O esquema só a exige quando a confiança é baixa, e nenhuma é — mas a doutrina diz que **nada vai ao ar sem uma pessoa ter lido**, e esse registro não existe ainda.

3. **Abrir um segundo caso.** A série de sabatinas teve seis candidatos. Um segundo caso é o que prova que o pipeline não foi moldado para um vídeo só. ⚠️ Serve também para testar a atribuição de falante numa peça com outra dinâmica de interrupção.

4. **Publicar o repositório.** Ele nasce privado; a abertura é decisão do autor.

---

## ⚠️ Limitações conhecidas, e onde estão escritas

| Limitação | Onde |
|---|---|
| O detector de tom **não separa vozes** em áudio de TV comprimido | `casos/.../transcricao/NOTA_DE_ATRIBUICAO.md` §4 |
| A voz da retrospectiva (00:57 a 01:51) **não foi identificada** | mesma nota, §3 |
| Uma frase teve a transcrição **não resolvida** e ficou fora, declarada | `alegacoes/...json`, campo `exclusoes` |
| O validador **não pega ano errado** dentro de um resumo | `docs/METODOLOGIA.md` §3.1 · `numeros_de()` |
| A checagem do G20 usa o conceito de governo geral do FMI, que **não é** o do setor público consolidado brasileiro | `checagens/...json`, A007, campo `divergencia_entre_fontes` |
| A exclusividade "na história do Brasil" (A006) **não é verificável** antes de 2001, quando as séries comparáveis começam | idem, A006 |
| Não há fade entre cartelas: corte seco, decisão deliberada | `docs/ARQUITETURA.md` §5 |

---

## 🧾 O que quebrou nesta primeira rodada, e não pode voltar

Cada linha aqui é um defeito que aconteceu de verdade. Estão listados porque a próxima sessão não deve gastar tempo redescobrindo.

| Sintoma | Causa | Conserto, já aplicado |
|---|---|---|
| Cartela com duração **negativa** | duas alegações saem da **mesma frase**, e a janela era cortada no começo da seguinte | as cartelas entram em **fila**: `_janelas()` em `passo6_overlay.py` |
| `ValueError: b'Regular' is not in list` | o arquivo itálico da Inter chama a instância de `Italic`, não `Regular` | tradução do nome do peso em `tipografia.fonte()` |
| `Unrecognized option 'filter_complex_script'` | a opção **foi removida no ffmpeg 8**; a máquina tem a 9 | `_opcao_de_script()` escolhe `-/filter_complex` conforme a versão |
| "SEM COMPROVAÇÃO" escrevendo **por cima** da descrição, na legenda | coluna de rótulo fixa em 300px | a coluna é medida na própria fonte |
| Ressalva **cortada no meio da frase** | cabia em uma linha só | duas linhas |
| Card dizendo "FONTES: IBGE" com **dois** documentos do IBGE | instituições repetidas colapsavam em um nome | o card mostra a contagem de documentos |
| O selo "CHECAGEM ABERTA" **sumia nos intervalos** | ele era desenhado dentro da cartela | virou camada própria, sobreposta o vídeo inteiro |
| Linha de fontes **estourando a caixa** em 92px | os nomes eram concatenados sem medir; "US Department of the Treasury / Federal Reserve Bank of St. Louis" mais um segundo nome dava 1802px numa caixa de 1710px | a linha é construída **medindo em pixels**, e o que não cabe vira "(+N)" |
| Medição de áudio voltando **vazia sem erro** | `volumedetect` escreve em nível informativo, e o comando rodava com `-v error` | `_nivel_de_audio()` roda com `-v info` |
| Resumo afirmando "a maior taxa desde **1986**" sem fonte | escrito de memória; o validador trata ano como data e não pegou | corrigido e registrado em `casos/.../CORRECOES.md` |
| Duas fontes com a **mesma URL** contadas como duas | dois pedaços da mesma base | juntadas num trecho só; o validador reprova a duplicata |

---

## Como retomar, em três comandos

```bash
cd checagem-eleicoes-2026
python -m pytest -q                       # 35 testes
python ferramentas/conferir-links.py      # nenhum link quebrado
python -m checagem validar 2026-08-27-sabatina-lula-globo --recorte bloco-contas-publicas
```

Se os três passarem, o repositório está no estado descrito aqui. Se algum falhar, **conserte antes de escrever qualquer coisa nova**: seguir em frente com a porta reprovando é como o projeto perde a única coisa que ele tem, que é ser conferível.
