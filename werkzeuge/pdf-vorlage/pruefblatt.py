#!/usr/bin/env python3
"""Rendert jede Seite jeder PDF-Quelle als PNG - Grundlage fuer die Sichtpruefung.

Abstaende und Ueberlauf lassen sich messen (messen.py, abstaende.py), die
gestalterische Qualitaet nicht: leere Seitenhaelften, unleserlich kleine
Skizzen, schlechte Headline-Umbrueche sieht man nur, wenn man die Seite ansieht.

Aufruf:
    python3 pruefblatt.py                 # alle Quellen in _build/
    python3 pruefblatt.py strategie ...   # einzelne
Ergebnis: <scratch>/pruefblatt/<slug>-<seite>.png
"""
import glob, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
BUILD = os.path.join(ROOT, "werkzeuge", "pdf-seiten", "_build")
OUT = os.environ.get("PRUEFBLATT_OUT", os.path.join(BUILD, "_pruefblatt"))

sys.path.insert(0, HERE)
from vorschaubilder import screenshot_pages  # noqa: E402


def seiten_zahl(src):
    # nur die Seiten-Sections zaehlen - 'class="page-no"' steht in jedem Kopf
    return open(src, encoding="utf-8").read().count('<section class="page')


def main(slugs):
    os.makedirs(OUT, exist_ok=True)
    for slug in slugs:
        src = os.path.join(BUILD, f"_pdfsrc_{slug}.html")
        if not os.path.exists(src):
            print(f"{slug:30s} keine Quelle in _build/")
            continue
        n = seiten_zahl(src)
        shots = screenshot_pages(src, list(range(1, n + 1)), OUT)
        for p, f in shots.items():
            ziel = os.path.join(OUT, f"{slug}-{p}.png")
            os.replace(f, ziel)
        print(f"{slug:30s} {n} Seite(n)")
    print(f"\n-> {OUT}")


if __name__ == "__main__":
    args = sys.argv[1:] or sorted(
        os.path.basename(f)[len("_pdfsrc_"):-5]
        for f in glob.glob(os.path.join(BUILD, "_pdfsrc_*.html")))
    main(args)
