"""Captura as fontes de um caso: baixa cada URL, guarda o bruto, extrai o texto e assina.

    python ferramentas/capturar-fontes.py <slug> [--pedido caminho] [--saida pasta]

Lê `casos/<slug>/checagens/PEDIDO_CAPTURA.json`:

    { "caso": "<slug>", "rodada": 3,
      "urls": ["https://...", {"url": "https://...", "navegador": true}] }

e escreve, na pasta de saída (padrão `capturas/<slug>/`):

    bruto/<id>.<ext>      o que o servidor devolveu, byte a byte
    texto/<id>.txt        o texto legível extraído do bruto (HTML, PDF ou JSON)
    capturas.json         o manifesto: URL, hora da captura em UTC, status, tipo, sha256

🔑 Por que isto existe. O `trecho` de uma fonte é COPIADO, nunca parafraseado (METODOLOGIA
§3.1 regra 5). Copiar exige ter a página inteira na mão, e uma página de governo muda sem
aviso. O manifesto grava o `sha256` do que foi lido no momento da consulta: quem duvidar de um
trecho sabe exatamente qual versão da página o sustentava.

⚠️ O bruto e o texto NÃO entram no git: são páginas de terceiros, algumas com direito
autoral. Entra só o manifesto (`checagens/CAPTURAS.json`), que é o recibo, não a mercadoria.

Quando o servidor devolve erro ou uma página vazia (sites que só montam o conteúdo com
JavaScript), a captura tenta de novo com um navegador sem tela, se o Playwright estiver
instalado. O manifesto registra qual dos dois caminhos produziu o texto.
"""

from __future__ import annotations

import argparse
import hashlib
import html
import json
import re
import subprocess
import sys
import urllib.error
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

RAIZ = Path(__file__).resolve().parents[1]
AGENTE = ("Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) "
          "Chrome/128.0 Safari/537.36 checagem-eleicoes-2026/0.2 (+github.com/Gabriel-Alexandre)")

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")


def _id(url: str) -> str:
    return hashlib.sha1(url.encode("utf-8")).hexdigest()[:12]


def _baixar(url: str, tempo: int = 60) -> tuple[int, str, bytes]:
    req = urllib.request.Request(url, headers={
        "User-Agent": AGENTE,
        "Accept": "text/html,application/xhtml+xml,application/json,application/pdf,*/*;q=0.8",
        "Accept-Language": "pt-BR,pt;q=0.9,en;q=0.6",
    })
    try:
        with urllib.request.urlopen(req, timeout=tempo) as r:  # noqa: S310
            return r.status, r.headers.get("Content-Type", ""), r.read()
    except urllib.error.HTTPError as e:
        return e.code, e.headers.get("Content-Type", "") if e.headers else "", e.read() or b""


def _navegador(url: str) -> tuple[int, str, bytes] | None:
    try:
        from playwright.sync_api import sync_playwright
    except ImportError:
        return None
    # Página que nunca "assenta" (anúncio, vídeo, telemetria) estoura o networkidle; o que
    # importa é o texto, que já está lá depois do DOM carregado e de uns segundos de script.
    try:
        with sync_playwright() as p:
            nav = p.chromium.launch()
            pag = nav.new_page(user_agent=AGENTE, locale="pt-BR")
            resp = pag.goto(url, wait_until="domcontentloaded", timeout=60_000)
            pag.wait_for_timeout(6000)
            conteudo = pag.content().encode("utf-8")
            status = resp.status if resp else 0
            nav.close()
    except Exception as e:  # tempo esgotado, TLS, navegador: registra e segue
        print(f"   navegador falhou em {url}: {e}".splitlines()[0], flush=True)
        return None
    return status, "text/html; renderizado", conteudo


def _charset(tipo: str, bruto: bytes) -> str:
    """A codificação da página: o cabeçalho HTTP, depois o <meta>, e UTF-8 por último.

    ⚠️ Página de governo antiga (o Planalto, por exemplo) ainda vem em Windows-1252. Lida como
    UTF-8, "bilhões" vira "bilh�es", e um trecho com acento quebrado não é cópia literal.
    """
    m = re.search(r"charset=([\w-]+)", tipo or "", re.I) or \
        re.search(rb'<meta[^>]+charset=["\']?([\w-]+)', bruto[:4000], re.I)
    if m:
        nome = m.group(1).decode() if isinstance(m.group(1), bytes) else m.group(1)
        try:
            "".encode(nome)
            return nome
        except LookupError:
            pass
    try:
        bruto.decode("utf-8")
        return "utf-8"
    except UnicodeDecodeError:
        return "cp1252"


def _texto_de_html(bruto: bytes, tipo: str = "") -> str:
    t = bruto.decode(_charset(tipo, bruto), errors="replace")
    t = re.sub(r"(?is)<(script|style|noscript|svg)[^>]*>.*?</\1>", " ", t)
    t = re.sub(r"(?i)<br\s*/?>|</(p|div|li|h[1-6]|tr|table|section|article)>", "\n", t)
    t = re.sub(r"(?s)<[^>]+>", " ", t)
    t = html.unescape(t)
    t = re.sub(r"[ \t\r\f\v]+", " ", t)
    t = re.sub(r"\n\s*\n+", "\n\n", t)
    return t.strip()


def _texto_de_pdf(caminho: Path) -> str:
    r = subprocess.run(["pdftotext", "-layout", str(caminho), "-"], capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else ""


def capturar(slug: str, pedido: Path, saida: Path) -> Path:
    dados = json.loads(pedido.read_text(encoding="utf-8"))
    (saida / "bruto").mkdir(parents=True, exist_ok=True)
    (saida / "texto").mkdir(parents=True, exist_ok=True)
    manifesto_path = saida / "capturas.json"
    manifesto = (json.loads(manifesto_path.read_text(encoding="utf-8"))
                 if manifesto_path.exists() else {"caso": slug, "capturas": []})

    for item in dados["urls"]:
        url = item if isinstance(item, str) else item["url"]
        forcar_navegador = isinstance(item, dict) and item.get("navegador", False)
        ident = _id(url)
        caminho = "direto"
        try:
            status, tipo, bruto = (0, "", b"") if forcar_navegador else _baixar(url)
        except Exception as e:  # rede, TLS, tempo esgotado: registra e segue
            status, tipo, bruto = 0, f"erro: {e}", b""

        ext = "pdf" if ("pdf" in tipo or bruto[:4] == b"%PDF") else (
            "json" if "json" in tipo else "html")
        texto = ""
        if bruto:
            arq = saida / "bruto" / f"{ident}.{ext}"
            arq.write_bytes(bruto)
            if ext == "pdf":
                texto = _texto_de_pdf(arq)
            elif ext == "json":
                texto = bruto.decode("utf-8", errors="replace")
            else:
                texto = _texto_de_html(bruto, tipo)

        if (status != 200 or len(texto) < 400) and ext != "pdf":
            renderizado = _navegador(url)
            if renderizado and renderizado[2]:
                status, tipo, bruto = renderizado
                ext = "html"
                (saida / "bruto" / f"{ident}.html").write_bytes(bruto)
                texto = _texto_de_html(bruto)
                caminho = "navegador"

        (saida / "texto" / f"{ident}.txt").write_text(f"URL: {url}\n\n{texto}", encoding="utf-8")
        # Os links da página, à parte: servem para achar a publicação certa (a íntegra de um
        # vídeo, o documento anexo), e não entram no trecho de ninguém.
        if bruto and ext == "html":
            hrefs = sorted(set(re.findall(r'href="([^"#]+)"', bruto.decode("utf-8", errors="replace"))))
            (saida / "links").mkdir(exist_ok=True)
            (saida / "links" / f"{ident}.txt").write_text("\n".join(hrefs), encoding="utf-8")
        registro = {
            "id": ident,
            "url": url,
            "capturada_em": datetime.now(timezone.utc).isoformat(timespec="seconds"),
            "status": status,
            "tipo": tipo,
            "caminho": caminho,
            "bytes": len(bruto),
            "sha256": hashlib.sha256(bruto).hexdigest() if bruto else None,
            "caracteres_de_texto": len(texto),
        }
        manifesto["capturas"] = [c for c in manifesto["capturas"] if c["url"] != url] + [registro]
        marca = "ok " if status == 200 and texto else "!! "
        print(f"{marca}{status} {len(texto):>7} {caminho:<9} {url}", flush=True)
        # O manifesto é gravado a cada URL: uma falha no meio não apaga o que já foi capturado.
        manifesto_path.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n",
                                  encoding="utf-8")

    manifesto_path.write_text(json.dumps(manifesto, ensure_ascii=False, indent=2) + "\n",
                              encoding="utf-8")
    return manifesto_path


def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description="captura as fontes de um caso, com sha256")
    p.add_argument("slug")
    p.add_argument("--pedido", default=None)
    p.add_argument("--saida", default=None)
    a = p.parse_args(argv)
    pedido = Path(a.pedido) if a.pedido else RAIZ / "casos" / a.slug / "checagens" / "PEDIDO_CAPTURA.json"
    saida = Path(a.saida) if a.saida else RAIZ / "capturas" / a.slug
    capturar(a.slug, pedido, saida)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
