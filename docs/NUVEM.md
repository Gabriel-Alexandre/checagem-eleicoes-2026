# NUVEM · o caminho para quem não tem a máquina, ou a rede

Este documento existe porque o segundo caso do projeto foi feito num ambiente que **não alcançava o YouTube, o Hugging Face nem os portais de dados públicos**: só o GitHub. O pipeline local continua sendo o caminho principal ([`REPLICAR.md`](REPLICAR.md)); este é o desvio documentado, com o que ele muda e o que ele não muda.

---

## 1. A ideia, em uma frase

A parte **mecânica** (baixar, assinar, transcrever, capturar páginas) roda num runner do GitHub Actions, que tem internet aberta; a parte de **julgamento** (extrair, checar, escrever o card) continua onde sempre esteve, com a IA ou a pessoa seguindo as skills.

⛔ Nenhum workflow deste repositório extrai alegação, escolhe fonte ou escreve veredito.

## 2. Os dois workflows

| Workflow | Disparo | Faz | Devolve |
|---|---|---|---|
| [`nuvem-preparar-midia`](../.github/workflows/nuvem-preparar-midia.yml) | push de `casos/<slug>/fonte/PEDIDO_NUVEM.json` | baixa a peça, `midia registrar`, `midia audio`, quadros de referência a cada 5 s, `transcrever` com o mesmo motor e modelo do caminho local | vídeo, WAV, `transcricao.tar.gz`, `quadros.tar.gz`, `origem-download.json` |
| [`nuvem-capturar-fontes`](../.github/workflows/nuvem-capturar-fontes.yml) | push de `casos/<slug>/checagens/PEDIDO_CAPTURA.json` | baixa cada URL listada, guarda o bruto, extrai o texto, assina com sha256 | `capturas-rodada-<N>.tar.gz` |

Os dois publicam num **release em rascunho** chamado `nuvem-<slug>`.

🔴 **Rascunho, e não release publicado, de propósito.** Rascunho só é visível para quem tem escrita no repositório. O vídeo de origem pertence a quem o produziu e o projeto não o redistribui; página de jornal capturada também tem dono. O repositório continua guardando só o que sempre guardou: manifesto, transcrição, checagem e o recibo das capturas.

## 3. Os pedidos

`casos/<slug>/fonte/PEDIDO_NUVEM.json`:

```json
{
  "caso": "<slug>",
  "url": "https://www.youtube.com/watch?v=...",
  "arquivo": "<nome-do-arquivo>.mp4",
  "alternativas": ["outra publicação da MESMA peça, como a cópia do próprio veículo"],
  "comentarios_de": ["opcional: vídeo publicado pelo projeto, para ouvir o público"]
}
```

`casos/<slug>/checagens/PEDIDO_CAPTURA.json`:

```json
{
  "caso": "<slug>",
  "rodada": 3,
  "finalidade": "por que estas URLs, nesta rodada",
  "urls": ["https://...", { "url": "https://...", "navegador": true }]
}
```

`navegador: true` força a captura por navegador sem tela, para página que só monta o conteúdo com JavaScript. Sem isso, o navegador só entra quando a captura direta falha ou volta quase vazia.

## 4. O que muda na procedência

⚠️ **O YouTube recusa IP de datacenter** ("Sign in to confirm you're not a bot"). [`ferramentas/baixar-peca.py`](../ferramentas/baixar-peca.py) tenta, nesta ordem, o `yt-dlp`, espelhos públicos do mesmo vídeo (Invidious e Piped, que servem os mesmos fluxos pelo mesmo identificador) e as `alternativas` do pedido. O caminho que funcionou vai para `origem-download.json`, e o `CASO.json` o declara em `procedencia.como_foi_obtido`.

🔑 Isto é procedência, não detalhe técnico: uma cópia de outro canal pode ter começo e fim diferentes, e isso desloca todos os tempos do caso. O `sha256` amarra a checagem ao arquivo que foi de fato checado.

## 5. O que muda na transcrição

Nada no método: mesmo `whisper.cpp`, mesmo `ggml-large-v3-turbo`, mesmos parâmetros de feixe. O número de threads é o do runner (4), e vai registrado no cabeçalho da transcrição, como sempre. A versão exata do `whisper.cpp` compilada vai em `whisper-versao.txt`.

## 6. O que muda na checagem: as capturas

A regra 5 da [METODOLOGIA §3.1](METODOLOGIA.md) manda copiar o trecho, nunca parafrasear. Com a captura, o trecho é copiado **do texto baixado**, e o manifesto guarda o `sha256` do que foi lido. Quem duvidar de um trecho sabe exatamente qual versão da página o sustentava.

- O manifesto vai para `casos/<slug>/checagens/CAPTURAS.json` (no git).
- O bruto e o texto das páginas **não** entram no git.
- O validador anota quantas URLs citadas têm captura assinada, e avisa as que não têm.
- O relatório mostra o começo do `sha256` ao lado de cada fonte capturada.

⚠️ A busca que **descobre** a URL (um buscador, por exemplo) não é fonte. Resumo de buscador é texto escrito por um modelo; o trecho sai sempre da página capturada.

## 7. Como baixar o que o runner devolveu

O release em rascunho aparece em *Releases* para quem tem escrita no repositório. Pela API:

```bash
curl -H "Authorization: Bearer $GH_TOKEN" \
  https://api.github.com/repos/<dono>/checagem-eleicoes-2026/releases   # acha o rascunho e os assets
curl -L -H "Authorization: Bearer $GH_TOKEN" -H "Accept: application/octet-stream" \
  -o transcricao.tar.gz https://api.github.com/repos/<dono>/checagem-eleicoes-2026/releases/assets/<id>
```

## 8. O que este caminho NÃO resolve

- ⛔ **Não publica nada.** O release é rascunho, e a publicação do vídeo checado segue sendo decisão humana (METODOLOGIA §6).
- ⛔ Não conserta o YouTube: se nenhum espelho servir o vídeo, o caso usa a cópia alternativa e **declara** que usou.
- ⚠️ Cada pedido é um commit. É o preço de o disparo ser auditável: o histórico mostra o que foi pedido, quando, e com que finalidade.
