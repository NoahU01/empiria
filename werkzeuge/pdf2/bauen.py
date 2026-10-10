#!/usr/bin/env python3
"""empiria 2.0 · PDFs bauen.

Aufruf:  python3 werkzeuge/pdf2/bauen.py [slug …]     (ohne Angabe: alle fertigen)
Ergebnis: site/assets/downloads/2.0/empiria-<slug>.pdf  + -1.png / -2.png (Vorschauen für den Download-Kasten)
          und eine Seitenübersicht zum Prüfen: werkzeuge/pdf2/_build/<slug>-seiten/seite-N.png
Die alten PDFs in site/assets/downloads/ bleiben unangetastet (sie gehören zu den Live-Seiten).
"""
import importlib
import os
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
BUILD = os.path.join(HERE, "_build")
ZIEL = os.path.join(ROOT, "site", "assets", "downloads", "2.0")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
FERTIG = {"ki-zum-anfassen": "ki_zum_anfassen"}


def main(slugs):
    os.makedirs(BUILD, exist_ok=True); os.makedirs(ZIEL, exist_ok=True)
    link = os.path.join(BUILD, "assets")
    if not os.path.exists(link):
        os.symlink(os.path.join(ROOT, "site", "assets"), link)
    for slug in slugs:
        mod = importlib.import_module(FERTIG[slug])
        src = os.path.join(BUILD, f"{slug}.html")
        open(src, "w", encoding="utf-8").write(mod.bauen())
        pdf = os.path.join(ZIEL, f"empiria-{slug}.pdf")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                        "--virtual-time-budget=8000", "file://" + src], capture_output=True, timeout=180)
        # Seitenbilder (zum Prüfen) und die ersten zwei als Vorschau für den Download-Kasten
        subprocess.run(["node", os.path.join(HERE, "seiten.mjs"), src, os.path.join(BUILD, f"{slug}-seiten"),
                        os.path.join(ZIEL, f"empiria-{slug}")], check=True)
        print(f"{slug}: {pdf}  ({os.path.getsize(pdf) // 1024} KB)")


if __name__ == "__main__":
    main(sys.argv[1:] or list(FERTIG))
