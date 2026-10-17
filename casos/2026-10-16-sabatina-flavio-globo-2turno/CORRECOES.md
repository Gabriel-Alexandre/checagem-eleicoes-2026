# CORREÇÕES · sabatina de Flávio Bolsonaro na TV Globo, 2º turno (16/out/2026)

Registro de tudo o que mudou na checagem DEPOIS do primeiro veredito, antes de qualquer publicação. ⛔ Veredito não se edita em silêncio (METODOLOGIA §7). Cada passada foi feita por um agente de IA que não escreveu a checagem que revisou. O modelo deste arquivo é o `CORRECOES.md` do caso de Lula de 15/out (`casos/2026-10-15-sabatina-lula-globo-2turno/`), com a mesma régua.

## 3. Transcrição

As 22 correções da transcrição estão em `transcricao/CORRECOES_DE_TRANSCRICAO.md`, e as três leituras alternativas que as sustentam, em `transcricao/leituras-alternativas/`. Todos os números conferidos saíram iguais na segunda leitura. As leituras que não se resolveram (entre elas *"um dinheiro totalmente ilícito"*, em 18:32, que as quatro leituras escrevem assim e o contexto pede *"lícito"*) estão listadas em `transcricao/correcoes.json`, campo `como_foram_conferidas`, e não vão para a tela sem `[...]`.

⚠️ O campo `revisao_humana: true` de `transcricao/transcricao.json` é marcado sozinho pelo `ferramentas/corrigir-transcricao.py` quando aplica correções; nesta transcrição as correções foram conferidas pela IA, por passadas do motor em janelas isoladas, e **nenhuma pessoa ouviu o áudio**.

🔧 Uma coisa do método que vale registrar: a 2ª leitura usou `-mc 0` (nenhum texto anterior como contexto) e, com isso, o whisper.cpp também descartou o prompt; as duas versões dela (sem e com prompt) saíram iguais. Ela foi tratada como uma leitura sem prompt, e a 3ª leitura, sem o `-mc 0`, é a que tem prompt.
