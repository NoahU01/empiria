#!/usr/bin/env python3
"""Vergleichsseite A/B für das Muster-PDF – site/projekte/pdf-varianten.html (nur Entwicklung)."""
import os, shutil, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, HERE)
import ki_zum_anfassen, ki_varianten
BUILD = os.path.join(HERE, "_build"); ZIEL = os.path.join(ROOT, "site", "projekte", "pdf-varianten")
os.makedirs(ZIEL, exist_ok=True)


def bilder(name, html):
    src = os.path.join(BUILD, f"{name}.html"); open(src, "w", encoding="utf-8").write(html)
    out = os.path.join(BUILD, f"{name}-seiten")
    subprocess.run(["node", os.path.join(HERE, "seiten.mjs"), src, out, ""], check=True)
    return out


a = bilder("var-a", ki_zum_anfassen.bauen())
b = bilder("var-b", ki_varianten.bauen_b())
c = bilder("var-c", ki_varianten.bauen_kopffuss())
for d, pre in ((a, "a"), (b, "b"), (c, "c")):
    for f in os.listdir(d):
        shutil.copy(os.path.join(d, f), os.path.join(ZIEL, f"{pre}-{f}"))

PUNKTE = [
    ("1 · Titelseite", "A: Bild auf Weiß, Fakten unten.", "B: unteres Drittel gelb – Bild und Fakten im Band, Highlight schwarz.", "a-seite-1.png", "b-seite-1.png"),
    ("2 · Seite „Das bekommst Du“", "A: Band + Werkzeuge + „Für wen“ (drei Themen).", "B: nur Band + Werkzeuge, Logos größer, „Für wen“ raus.", "a-seite-2.png", "b-seite-2.png"),
    ("3 · Formate: Karten oder Tabelle", "A: Post-Karten wie auf der Homepage.", "B: Vergleichstabelle, Mitte gelb.", "a-seite-3.png", "b-seite-3.png"),
    ("4 · Schwarzer Kasten „In jedem Format enthalten“", "A: mit Kasten.", "B: ohne Kasten, Karten luftiger.", "a-seite-3.png", "b-seite-4.png"),
    ("5 · Beispiele", "A: sechs Kacheln mit Kurzsatz.", "B: Liste mit Titel links und zwei Sätzen rechts.", "a-seite-4.png", "b-seite-5.png"),
    ("6 · Letzte Seite", "A: drei Schritte + gelbes Kontakt-Band.", "B: ganze Seite gelb, ein Satz, Team und Kontakt.", "a-seite-5.png", "b-seite-6.png"),
    ("7 · Kopf und Fuß (alle Seiten)", "A: oben Logo + Thema, unten Strich + Seitenzahl.", "B: oben nur Logo, unten Thema + Seitenzahl.", "a-seite-2.png", "c-seite-2.png"),
]
zeilen = "".join(f'''<section><h2>{t}</h2><div class="paar">
<figure><figcaption><b>A</b> {ta}</figcaption><a href="pdf-varianten/{ia}" target="_blank"><img src="pdf-varianten/{ia}" alt=""></a></figure>
<figure><figcaption><b>B</b> {tb}</figcaption><a href="pdf-varianten/{ib}" target="_blank"><img src="pdf-varianten/{ib}" alt=""></a></figure></div></section>''' for t, ta, tb, ia, ib in PUNKTE)
html = f'''<!doctype html><html lang="de"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1">
<meta name="robots" content="noindex"><title>PDF-Varianten · KI zum Anfassen</title>
<link rel="stylesheet" href="/assets/fonts/fonts.local.css"><style>
body {{ margin: 0; font-family: Poppins, sans-serif; color: #1a1817; background: #f3f1ee; }}
header {{ padding: 40px 6vw 10px; }} h1 {{ font-family: Lora, serif; font-size: 2.4rem; margin: .3rem 0; }}
.k {{ font-size: .75rem; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }}
section {{ padding: 30px 6vw; border-top: 1px solid #dcd8d1; }} h2 {{ font-family: Lora, serif; font-size: 1.5rem; margin: 0 0 16px; }}
.paar {{ display: grid; grid-template-columns: 1fr 1fr; gap: 28px; }}
figure {{ margin: 0; }} figcaption {{ font-size: .9rem; margin-bottom: 10px; min-height: 2.6em; }}
figcaption b {{ display: inline-grid; place-items: center; width: 1.6em; height: 1.6em; border-radius: 50%; background: #fff400; margin-right: .4em; }}
img {{ width: 100%; display: block; box-shadow: 0 6px 30px rgba(0,0,0,.08); background: #fff; }}
@media (max-width: 800px) {{ .paar {{ grid-template-columns: 1fr; }} }}
</style></head><body><header><p class="k">PDF-Muster · KI zum Anfassen</p><h1>Varianten im Vergleich</h1>
<p>Links die jetzige Fassung (A), rechts die Alternative (B). Bild anklicken = groß ansehen.</p></header>{zeilen}</body></html>'''
open(os.path.join(ROOT, "site", "projekte", "pdf-varianten.html"), "w", encoding="utf-8").write(html)
print("fertig")
