#!/usr/bin/env python3
"""Baut aus allen 21 PDFs EIN durchgehendes PDF - in Menuereihenfolge.

Zum Durchsehen am Stueck. Die Reihenfolge ist dieselbe wie bei
pdfs_exportieren.py, damit die Nummerierung der Einzeldateien und die
Abfolge im Sammel-PDF zusammenpassen.

Nicht zusammengefuegt werden die fertigen PDFs - dafuer gibt es auf diesem
Rechner kein Werkzeug (weder poppler noch ghostscript noch pypdf). Stattdessen
werden die HTML-Quellen aus _build/ hintereinandergehaengt und in einem Zug
ueber Chrome gedruckt: derselbe Weg wie bei den Einzel-PDFs, also identisches
Ergebnis. Jede Seite bekommt dabei die Farbvariablen ihres eigenen PDFs als
style-Attribut mit - sonst wuerde das ganze Dokument im Theme des ersten
PDFs erscheinen.

Aufruf:  python3 werkzeuge/pdfs_zusammenfassen.py [zieldatei]
         ohne Angabe: ~/Downloads/empiria-pdfs/empiria-alle-pdfs.pdf
"""
import os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
BUILD = os.path.join(HERE, "pdf-seiten", "_build")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

sys.path.insert(0, HERE)
from pdfs_exportieren import menue_reihenfolge, UNTERSEITEN, titel  # noqa: E402


def reihenfolge():
    folge = [s for s in menue_reihenfolge()
             if os.path.exists(os.path.join(BUILD, f"_pdfsrc_{s}.html"))]
    folge += [s for s in UNTERSEITEN if s not in folge]
    return [s for s in folge if os.path.exists(os.path.join(BUILD, f"_pdfsrc_{s}.html"))]


def teile(slug):
    """(CSS, Theme-Variablen, Seiten-HTML) einer PDF-Quelle."""
    t = open(os.path.join(BUILD, f"_pdfsrc_{slug}.html"), encoding="utf-8").read()
    css = t.split("<style>", 1)[1].split("</style>", 1)[0]
    m = re.search(r":root\{([^}]*)\}", css)
    vars_ = m.group(1) if m else ""
    css = css[:m.start()] + css[m.end():] if m else css      # :root hier raus
    body = t.split("<body>", 1)[1].rsplit("</body>", 1)[0]
    return css, vars_, body


def mit_theme(body, vars_):
    """Die Farbvariablen an jede Seite haengen.

    Eine Seite kann bereits ein eigenes style-Attribut tragen (page(farbe=...)).
    Das muss gewinnen, steht also HINTER den Theme-Variablen.
    """
    def ersetzen(m):
        rest = m.group(1)
        s = re.search(r'style="([^"]*)"', rest)
        if s:
            rest = rest[:s.start()] + rest[s.end():]
            return f'<section{rest} style="{vars_}{s.group(1)}">'
        return f'<section{rest} style="{vars_}">'
    return re.sub(r'<section((?:(?!>).)*?class="page(?:(?!>).)*?)>', ersetzen, body)


def main(ziel):
    folge = reihenfolge()
    namen = titel()

    # assets/ muss neben der Quelle liegen - die HTML-Pfade sind relativ.
    link = os.path.join(BUILD, "assets")
    if not os.path.exists(link):
        os.symlink(os.path.join(ROOT, "site", "assets"), link)

    css = None
    stuecke = []
    for i, slug in enumerate(folge, 1):
        c, vars_, body = teile(slug)
        if css is None:
            css = c                       # in allen Quellen identisch
        stuecke.append(f"<!-- {i:02d} {slug} -->" + mit_theme(body, vars_))
        print(f"  {i:02d}  {namen.get(slug, slug)}")

    doc = ('<!doctype html><html lang="de"><head><meta charset="utf-8">'
           '<title>empiria – alle PDFs</title>'
           '<link rel="stylesheet" href="assets/fonts/fonts.local.css">'
           f'<style>{css}</style></head><body>{"".join(stuecke)}</body></html>')

    quelle = os.path.join(BUILD, "_pdfsrc_alle.html")
    open(quelle, "w", encoding="utf-8").write(doc)

    os.makedirs(os.path.dirname(ziel), exist_ok=True)
    subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                    f"--print-to-pdf={ziel}", "--virtual-time-budget=60000",
                    "file://" + quelle], capture_output=True, timeout=600)
    if not os.path.exists(ziel):
        raise SystemExit("PDF-Rendering fehlgeschlagen")

    seiten = len(re.findall(r'<section[^>]*class="page', doc))
    print(f"\n{len(folge)} PDFs, {seiten} Seiten -> {ziel} "
          f"({os.path.getsize(ziel)/1024/1024:.1f} MB)")


if __name__ == "__main__":
    ziel = (sys.argv[1] if len(sys.argv) > 1
            else os.path.expanduser("~/Downloads/empiria-pdfs/empiria-alle-pdfs.pdf"))
    main(os.path.abspath(ziel))
