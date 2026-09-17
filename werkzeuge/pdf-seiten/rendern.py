#!/usr/bin/env python3
"""Rendert die PDF-Quellen aus _build/ zu fertigen PDFs + WebP-Vorschauen.

Ersetzt die alte render.js (Playwright, Cloud-Pfade) durch Chrome direkt.

Aufruf:
    python3 rendern.py                 # alle
    python3 rendern.py marketing ...   # einzelne
Ergebnis: site/assets/downloads/empiria-<slug>.pdf  +  -1.webp / -2.webp
          (und dieselben Dateien in cowork-vorschau/assets/downloads/)
"""
import glob, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BUILD = os.path.join(HERE, "_build")
TARGETS = [os.path.join(ROOT, "site", "assets", "downloads"),
           os.path.join(ROOT, "cowork-vorschau", "assets", "downloads")]
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

sys.path.insert(0, os.path.join(ROOT, "werkzeuge", "pdf-vorlage"))
from vorschaubilder import screenshot_pages, png_to_webp  # noqa: E402


def render_pdf(src_html, out_pdf):
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={out_pdf}", "--virtual-time-budget=8000",
                    "file://" + os.path.abspath(src_html)],
                   capture_output=True, timeout=180)
    if not os.path.exists(out_pdf):
        raise RuntimeError(f"PDF-Rendering fehlgeschlagen: {src_html}")


def main(slugs):
    # assets/ muss neben der Quelle liegen (relative Pfade im HTML)
    link = os.path.join(BUILD, "assets")
    if not os.path.exists(link):
        os.symlink(os.path.join(ROOT, "site", "assets"), link)

    for slug in slugs:
        src = os.path.join(BUILD, f"_pdfsrc_{slug}.html")
        if not os.path.exists(src):
            print(f"{slug:32s} uebersprungen (keine Quelle in _build/)")
            continue
        primary = TARGETS[0]
        os.makedirs(primary, exist_ok=True)
        pdf = os.path.join(primary, f"empiria-{slug}.pdf")
        render_pdf(src, pdf)

        with tempfile.TemporaryDirectory() as td:
            shots = screenshot_pages(src, [1, 2], td)
            for i, p in enumerate([1, 2], 1):
                png_to_webp(shots[p], os.path.join(primary, f"empiria-{slug}-{i}.webp"))

        for extra in TARGETS[1:]:
            if not os.path.isdir(extra):
                continue
            for name in (f"empiria-{slug}.pdf", f"empiria-{slug}-1.webp", f"empiria-{slug}-2.webp"):
                shutil.copy(os.path.join(primary, name), os.path.join(extra, name))

        print(f"{slug:32s} PDF {os.path.getsize(pdf)//1024:5d} KB  + 2 Vorschauen")


if __name__ == "__main__":
    args = sys.argv[1:]
    if not args:
        args = sorted(os.path.basename(f)[len("_pdfsrc_"):-5]
                      for f in glob.glob(os.path.join(BUILD, "_pdfsrc_*.html")))
    main(args)
