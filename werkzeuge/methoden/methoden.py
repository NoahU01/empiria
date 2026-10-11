#!/usr/bin/env python3
"""Methoden – Seiten für die Zusammenarbeit mit Menschen in Projekten (Entwicklung › Projekte › Methoden).

Storyboard Landing Page: übernommen aus muellerundstroebel/entwicklung/storyboard.html (Kopie der Quelle hier im
Ordner: quelle-storyboard-mus.html/.css), auf das empiria-Design umgestellt (Weiß/Grau/Schwarz, Gelb als Akzent,
Lora/Poppins), Ansprache per Du, projektbezogene Inhalte von Müller & Ströbel neutralisiert.

Aufruf: python3 werkzeuge/methoden/methoden.py
Ergebnis: site/projekte/methoden.html, site/projekte/methoden-storyboard.html
"""
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "ga"))
from ga_export import seite  # noqa: E402

QUELLE = HIER / "quelle-storyboard-mus.html"
QUELLE_CSS = HIER / "quelle-storyboard-mus.css"

# Ansprache per Du, Inhalte ohne Projektbezug (Reihenfolge wichtig: längere Stellen zuerst)
ERSETZEN = [
    ('<h1>So entsteht die Landingpage.</h1>', '<h1>So entsteht die <span class="hl">Landingpage.</span></h1>'),
    ("Sie beantworten enge Punkte.", "Du beantwortest enge Punkte."),
    ("Ich kürze und ordne Ihre Antworten. Wo etwas fehlt, frage ich nach.",
     "Wir kürzen und ordnen Deine Antworten. Wo etwas fehlt, fragen wir nach."),
    ("Sie sehen die acht Sätze untereinander", "Du siehst die acht Sätze untereinander"),
    ("<h3>Ihr Wortlaut</h3>", "<h3>Dein Wortlaut</h3>"),
    ("Ihre Antworten", "Deine Antworten"),
    ("<b>Ihre Lage</b>", "<b>Die Lage</b>"),
    ("F2 · Ihre Lage", "F2 · Die Lage"),
    ("Tobias und Daniel mit Telefon", "Ansprechpartner mit Telefon"),
]
ZITAT = re.compile(r"<q>.*?</q>")
STATUS = re.compile(r'sb-p sb-p--(da|teil)"><i aria-label="(vorhanden|teilweise)">')


def storyboard_main():
    s = QUELLE.read_text(encoding="utf-8")
    main = s[s.index("<main>") + 6:s.index("</main>")]
    for a, b in ERSETZEN:
        assert a in main, a
        main = main.replace(a, b)
    main = ZITAT.sub("", main)                              # keine Kundenzitate aus dem M&S-Projekt
    main = STATUS.sub('sb-p sb-p--offen"><i aria-label="offen">', main)  # Vorlage: alle Punkte offen
    main = main.replace('<p class="kicker">Storyboard</p>', '<p class="kicker">Methode · Storyboard</p>')
    return main


VARIABLEN = """
.sbm { --navy: #1a1817; --navy-2: #2a2725; --taupe: #b9b3ab; --taupe-d: #6b6762; --taupe-h: #fff400;
  --sand: #f3f1ee; --sand-2: #e6e2dc; --linie: #e4e0db; --ink: #1a1817; --ink-2: #3d3a37; --weiss: #fff;
  --head: 'Lora', Georgia, serif; --text: 'Poppins', Arial, sans-serif; --r: 18px;
  font: 400 17px/1.65 var(--text); color: var(--ink); }
:where(.sbm) ul, :where(.sbm) ol { list-style: none; margin: 0; padding: 0; }
:where(.sbm) :where(p, h1, h2, h3) { margin: 0; }
.sbm h1, .sbm h2, .sbm h3 { font-family: var(--head); font-weight: 700; letter-spacing: -.02em; line-height: 1.2; color: var(--navy); }
.sbm .wrap { width: 100%; max-width: 74rem; margin: 0 auto; padding: 0 2rem; }
.sbm .ico { width: 1.6rem; height: 1.6rem; fill: none; stroke: currentColor; stroke-width: 1.5; stroke-linecap: round; stroke-linejoin: round; }
.sbm .sek { padding: 7rem 0; }
.sbm .sek--sand { background: var(--sand); }
.sbm .sek--navy { background: var(--navy); color: var(--weiss); }
.sbm .sek--navy h2, .sbm .sek--navy h3 { color: var(--weiss); }
.sbm .kicker { display: inline-flex; align-items: center; gap: .6rem; margin-bottom: 1.2rem; font-size: .78rem; font-weight: 700; letter-spacing: .15em; text-transform: uppercase; color: var(--navy); }
.sbm .kicker::before { content: ""; width: 1.5rem; height: 2px; background: currentColor; }
.sbm .sek--navy .kicker { color: #fff400; }
.sbm .h2 { font-size: clamp(2.2rem, 4.4vw, 3.4rem); max-width: 20ch; line-height: 1.25; }
.sbm .lead { margin-top: 1.4rem; max-width: 40rem; font-size: 1.18rem; line-height: 1.65; color: var(--ink-2); font-weight: 300; }
.sbm .held { padding: 5.5rem 0 6rem; }
.sbm .held h1 { font-size: clamp(2.8rem, 5.6vw, 4.6rem); line-height: 1.3; }
.sbm .hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }
@media (max-width: 991px) { .sbm .sek { padding: 5rem 0; } .sbm .held { padding: 3.5rem 0 4.5rem; } }
"""
# Korrekturen nach dem Übernehmen: Gelb (--taupe-h) nur auf Schwarz, auf hellen Flächen neutral
KORREKTUR = """
.sbm .sb-weg b, .sbm .sb-t-frage b, .sbm .sb-t-abschnitt b, .sbm .sb-bau__liste b, .sbm .sb-karte h3 { font-weight: 700; }
.sbm .sb-weg b { line-height: 1.1; }
.sbm .sb-t-punkte .sb-p--offen { outline-color: var(--taupe); }
.sbm .sb-p--offen i, .sbm .sb-legende .sb-p--offen i { box-shadow: inset 0 0 0 1.5px var(--taupe); }
.sbm .sb-karte::after { color: var(--taupe); }
.sbm .sb-treppe i { background: #fff400; }
.sbm .sb-t-punkte { }
.sbm .sb-weg > li.sb-weg--ziel .sb-weg__ico { background: #fff400; color: var(--navy); }
.sbm .sb-nr { background: #fff400; }
.sbm .sb-mock__a--3 .sb-treppe i { background: #fff400; }
"""


def storyboard():
    css = VARIABLEN + QUELLE_CSS.read_text(encoding="utf-8") + KORREKTUR
    html = f'<main>\n<div class="sbm">{storyboard_main()}</div>\n<style>{css}</style>\n</main>'
    seite("methoden-storyboard.html", "Storyboard Landing Page", html)


def uebersicht():
    karten = [("/projekte/methoden-storyboard.html", "SB", "Storyboard Landing Page",
               "Von den Antworten zur Landingpage: 12 Punkte, 8 Fragen des Lesers, 4 Abschnitte. Zum gemeinsamen Erarbeiten einer Seite.")]
    k = "".join(f'<a class="mt-karte" href="{h}"><span class="mt-tag">{t}</span><b>{n}</b><small>{x}</small></a>' for h, t, n, x in karten)
    html = f'''<main>
<section class="mt"><div class="container">
  <p class="mt-kicker">Projekte</p>
  <h1>Methoden für die <span class="hl">Zusammenarbeit.</span></h1>
  <p class="mt-lead">Seiten, die wir nutzen, wenn wir in Projekten mit Menschen zusammenarbeiten – zum Erklären, gemeinsamen Erarbeiten und Festhalten.</p>
  <div class="mt-raster">{k}</div>
</div></section>
<style>
.mt {{ padding: 5rem 0 6rem; }}
.mt-kicker {{ display: inline-flex; align-items: center; gap: .6rem; margin: 0 0 1.2rem; font: 700 .78rem/1 'Poppins', sans-serif; letter-spacing: .15em; text-transform: uppercase; color: #1a1817; }}
.mt-kicker::before {{ content: ""; width: 1.5rem; height: 2px; background: currentColor; }}
.mt h1 {{ margin: 0; font: 700 clamp(2.4rem, 5vw, 3.8rem)/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; color: #1a1817; }}
.mt .hl {{ background: #fff400; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }}
.mt-lead {{ margin: 1.4rem 0 0; max-width: 40rem; font: 300 1.15rem/1.65 'Poppins', sans-serif; color: #3d3a37; }}
.mt-raster {{ display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.2rem; margin-top: 3.2rem; }}
.mt-karte {{ display: flex; flex-direction: column; gap: .6rem; padding: 1.8rem 1.6rem; border-radius: 18px; background: #f3f1ee; color: #1a1817; text-decoration: none; transition: transform .15s ease; }}
.mt-karte:hover {{ transform: translateY(-2px); }}
.mt-tag {{ display: grid; place-items: center; width: 3rem; height: 3rem; border-radius: 12px; background: #1a1817; color: #fff400; font: 700 .85rem/1 'Poppins', sans-serif; letter-spacing: .06em; }}
.mt-karte b {{ margin-top: .6rem; font: 700 1.4rem/1.25 'Lora', Georgia, serif; }}
.mt-karte small {{ font: 400 .95rem/1.55 'Poppins', sans-serif; color: #3d3a37; }}
@media (max-width: 900px) {{ .mt-raster {{ grid-template-columns: 1fr; }} }}
</style>
</main>'''
    seite("methoden.html", "Methoden", html)


if __name__ == "__main__":
    storyboard()
    uebersicht()
