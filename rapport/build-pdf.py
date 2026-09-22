#!/usr/bin/env python3
"""Génère outils-open-source.pdf comme calque EXACT du HTML (rendu web),
en une seule page continue — PAS de format A4, pas de marges de page.

Méthode : on retire le bloc `@media print` du HTML (sinon Chromium pagine en A4),
on fixe une `@page` unique à la largeur du rendu web (1000 px) et à la hauteur
réelle du contenu, puis on imprime avec Chromium headless.

Dépendances : chromium (fourni ici par Playwright) + le paquet python `playwright`
(uniquement pour mesurer la hauteur du contenu).  Le fichier HTML n'est pas modifié.

    pip install playwright
    python3 build-pdf.py
"""
import os, glob, subprocess
from playwright.sync_api import sync_playwright

HERE = os.path.dirname(os.path.abspath(__file__))
HTML = os.path.join(HERE, "outils-open-source.html")
OUT  = os.path.join(HERE, "outils-open-source.pdf")
TMP  = "/tmp/continuous-report.html"
WIDTH = 1000          # largeur du rendu web (comme dans le navigateur)
BUFFER = 90           # petite marge basse pour éviter toute coupure

def find_chrome():
    for pat in ("/opt/pw-browsers/chromium-*/chrome-linux/chrome",
                "/opt/pw-browsers/chromium/chrome-linux/chrome"):
        hits = sorted(glob.glob(pat))
        if hits:
            return hits[-1]
    return "chromium"   # repli : chromium présent dans le PATH

def strip_print_css(src: str) -> str:
    """Retire `@page{size:A4...}` et tout le bloc `@media print{...}`."""
    i = src.index("@page{ size:A4; margin:12mm; }")
    j = src.index("@media print{", i)
    depth, end = 0, None
    for p in range(src.index("{", j), len(src)):
        if src[p] == "{": depth += 1
        elif src[p] == "}":
            depth -= 1
            if depth == 0:
                end = p + 1; break
    return src[:i].rstrip() + "\n" + src[end:].lstrip("\n ")

def build(cleaned: str, height: int) -> str:
    inject = ("  *{-webkit-print-color-adjust:exact !important;"
              "print-color-adjust:exact !important;}\n"
              f"  @page{{ size:{WIDTH}px {height}px; margin:0; }}\n")
    return cleaned.replace("</style>", inject + "</style>", 1)

def main():
    chrome = find_chrome()
    cleaned = strip_print_css(open(HTML, encoding="utf-8").read())

    # 1) placeholder, puis mesure de la hauteur réelle du contenu à WIDTH px
    open(TMP, "w", encoding="utf-8").write(build(cleaned, 20000))
    with sync_playwright() as pw:
        b = pw.chromium.launch(executable_path=chrome, args=["--no-sandbox"])
        pg = b.new_page(viewport={"width": WIDTH, "height": 1200})
        pg.goto("file://" + TMP, wait_until="networkidle")
        h = pg.evaluate("Math.ceil(document.body.getBoundingClientRect().height)")
        b.close()
    paper = h + BUFFER
    print(f"Hauteur du contenu : {h}px  ->  page continue {WIDTH}x{paper}px")

    # 2) page unique définitive
    open(TMP, "w", encoding="utf-8").write(build(cleaned, paper))
    subprocess.run([chrome, "--headless=new", "--no-sandbox", "--disable-gpu",
                    "--hide-scrollbars", "--no-pdf-header-footer",
                    "--virtual-time-budget=10000",
                    f"--print-to-pdf={OUT}", "file://" + TMP], check=True,
                   capture_output=True, text=True)
    print(f"PDF généré : {OUT}  ({os.path.getsize(OUT)} octets)")

if __name__ == "__main__":
    main()
