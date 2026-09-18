#!/usr/bin/env python3
"""Holt die Skizzen/Grafiken einer Website-Seite fuer die PDF-Nutzung.

Die Produktseiten enthalten aufwendige Inline-SVGs (Mockups, Modelle, Ablaeufe).
In den PDFs fehlten sie - dieses Skript findet sie, ordnet sie der naechsten
Ueberschrift zu und legt sie unter werkzeuge/pdf-seiten/sk/ ab.

Aufruf:
    python3 skizzen_holen.py <seite.html>              # nur auflisten
    python3 skizzen_holen.py <seite.html> --speichern <praefix>
"""
import html as _h
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SITE = os.path.join(ROOT, "site")
SK = os.path.join(ROOT, "werkzeuge", "pdf-seiten", "sk")
MIN_KANTE = 250          # kleiner ist ein Icon, keine Skizze


def _svg_bei(t, start):
    """Vollstaendiges <svg>...</svg> ab Position start (verschachtelt sicher)."""
    # Das ">" muss mitgematcht werden - sonst endet der Ausschnitt bei "</svg"
    # und das SVG bleibt offen, wodurch es im PDF alles Nachfolgende verschluckt.
    tag = re.compile(r"<(/?)svg\b[^>]*>")
    depth, k = 0, start
    while True:
        m = tag.search(t, k)
        if not m:
            return None
        if m.group(1):
            depth -= 1
            if depth == 0:
                return t[start:m.end()]
        else:
            depth += 1
        k = m.end()


def _text(s):
    return re.sub(r"\s+", " ", _h.unescape(re.sub(r"<[^>]+>", " ", s))).strip()


def finden(pfad):
    t = open(pfad, encoding="utf-8").read()
    t = re.sub(r"(?s)<defs>.*?</defs>", " ", t)      # Icon-Sprites ausblenden
    treffer = []
    for m in re.finditer(r'<svg[^>]*viewBox="([^"]+)"', t):
        vb = m.group(1).split()
        if len(vb) != 4:
            continue
        if float(vb[2]) < MIN_KANTE and float(vb[3]) < MIN_KANTE:
            continue
        svg = _svg_bei(t, m.start())
        if not svg:
            continue
        # C2PA-Signaturen sind je ~14 kB Base64 und im PDF wertlos
        svg = re.sub(r"(?s)<metadata>.*?</metadata>", "", svg)
        if len(svg) < 900:                            # zu klein = Deko
            continue
        davor = t[max(0, m.start() - 3000):m.start()]
        heads = re.findall(r"<h[23][^>]*>(.*?)</h[23]>", davor, re.S)
        treffer.append(dict(viewbox=m.group(1), laenge=len(svg), svg=svg,
                            ueberschrift=_text(heads[-1])[:60] if heads else "-"))
    return treffer


if __name__ == "__main__":
    pfad = sys.argv[1]
    if not os.path.isabs(pfad):
        pfad = os.path.join(SITE, pfad)
    treffer = finden(pfad)
    speichern = "--speichern" in sys.argv
    praefix = sys.argv[sys.argv.index("--speichern") + 1] if speichern else None

    print(f"{len(treffer)} Skizze(n) in {os.path.basename(pfad)}")
    for i, s in enumerate(treffer, 1):
        print(f"  {i}. viewBox {s['viewbox']:14s} {s['laenge']:6d} Zeichen   nach: {s['ueberschrift']}")
        if speichern:
            ziel = os.path.join(SK, f"{praefix}-{i}.svg")
            open(ziel, "w", encoding="utf-8").write(s["svg"])
            print(f"     -> sk/{praefix}-{i}.svg")
