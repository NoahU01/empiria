#!/usr/bin/env python3
"""Methoden – Seiten für die Zusammenarbeit mit Menschen in Projekten (Entwicklung › Projekte › Methoden).

Übernommen aus muellerundstroebel/entwicklung (Kopien der Quellen hier im Ordner, quelle-*):
  · Storyboard Landing Page  (storyboard.html)    – mit dem Beispiel Müller & Ströbel (Schritt 4 Entwürfe, Schritt 5 Skizze)
  · Elevator Pitch          (elevator-pitch.html) – mit dem Beispiel Müller & Ströbel
Das Stylesheet von M&S (business-story-2.css + storyboard.css) wird auf `.sbm` begrenzt und über die
Variablen auf empiria umgestellt: Schwarz statt Navy, Weiß/Grau statt Sand, Gelb nur auf Schwarz, Lora 700/Poppins.

Aufruf: python3 werkzeuge/methoden/methoden.py
Ergebnis: site/projekte/methoden.html, methoden-storyboard.html, methoden-elevator-pitch.html
"""
import re
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent
sys.path.insert(0, str(HIER.parent / "ga"))
from ga_export import seite  # noqa: E402

BEISPIEL = '<p class="sbm-beispiel">Beispiel aus dem Projekt Müller &amp; Ströbel</p>'


# ---------- CSS von M&S auf .sbm begrenzen ----------
def _praefix(sel):
    sel = sel.strip()
    if not sel:
        return sel
    if sel in (":root", "html", "body"):
        return ".sbm"
    if sel == "*":
        return ".sbm, .sbm *"
    for anfang in ("html ", "body "):
        if sel.startswith(anfang):
            sel = sel[len(anfang):]
    return ".sbm " + sel


def begrenzen(css):
    css = re.sub(r"/\*.*?\*/", "", css, flags=re.S)
    out, i = [], 0
    while i < len(css):
        j = css.find("{", i)
        if j < 0:
            break
        kopf = css[i:j].strip()
        tiefe, k = 1, j + 1
        while tiefe:
            tiefe += {"{": 1, "}": -1}.get(css[k], 0)
            k += 1
        koerper = css[j + 1:k - 1]
        if kopf.startswith("@media"):
            out.append(f"{kopf} {{\n{begrenzen(koerper)}\n}}")
        elif kopf.startswith("@font-face") or kopf.startswith("@import"):
            pass
        elif kopf.startswith("@"):
            out.append(f"{kopf} {{{koerper}}}")
        else:
            out.append(", ".join(_praefix(s) for s in kopf.split(",")) + " {" + koerper + "}")
        i = k
    return "\n".join(out)


EMPIRIA = """
.sbm { --navy: #1a1817; --navy-2: #2a2725; --blau: #1a1817; --taupe: #b9b3ab; --taupe-d: #6b6762; --taupe-h: #fff400;
  --sand: #f3f1ee; --sand-2: #e6e2dc; --linie: #e4e0db; --ink: #1a1817; --ink-2: #3d3a37; --weiss: #fff;
  --head: 'Lora', Georgia, serif; --text: 'Poppins', Arial, sans-serif; --wrap: 74rem; --r: 18px;
  background: #fff; color: var(--ink); font: 400 17px/1.65 var(--text); }
.sbm h1, .sbm h2, .sbm h3 { font-weight: 700; letter-spacing: -.02em; line-height: 1.25; }
.sbm .held h1 { line-height: 1.3; }
.sbm .kicker { color: var(--navy); font-weight: 700; }
.sbm .kicker::before { background: currentColor; border-radius: 0; }
.sbm .sek--navy .kicker { color: #fff400; }
.sbm .sek--navy .kicker::before { background: #fff400; }
.sbm .hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }
.sbm-beispiel { display: table; margin: 0 0 1.2rem !important; padding: .3rem .8rem; border-radius: 999px; background: #f3f1ee;
  font: 600 .78rem/1.3 'Poppins', sans-serif; color: #3d3a37; }
/* Gelb nur auf Schwarz – auf hellen Flächen neutral */
.sbm .sb-t-punkte .sb-p--offen { outline-color: var(--taupe); }
.sbm .sb-p--offen i, .sbm .sb-legende .sb-p--offen i { box-shadow: inset 0 0 0 1.5px var(--taupe); }
.sbm .sb-karte::after { color: var(--taupe); }
.sbm .sb-nr { background: #fff400; color: #1a1817; }
.sbm .sb-weg > li.sb-weg--ziel .sb-weg__ico { background: #fff400; color: #1a1817; }
.sbm .sb-p--teil q, .sbm .sb-p--zuletzt q, .sbm .sb-verdichtung { border-color: var(--taupe); }
.sbm .sk-teil--kasten, .sbm .sk-teil--hinweis, .sbm .sk-teil--aufklappen { outline-color: var(--taupe); }
.sbm .sb-logik__listen > div:first-child .sb-liste span { color: var(--taupe-d); }
.sbm .sk-teil span, .sbm .sk-vorschau__quelle, .sbm .sb-schieben { color: var(--taupe-d); }
.sbm .sk--navy .sk-teil span, .sbm .sk--navy .sk-teil em { color: #fff400; }
.sbm .sk--sand { background: #ece9e4; }
.sbm .ep-mass { color: #fff400; }
@media (max-width: 991px) { .sbm .sb-t-punkte { border-left-color: var(--taupe); } }
"""
QUELL_CSS = begrenzen((HIER / "quelle-business-story-2.css").read_text(encoding="utf-8")
                      + (HIER / "quelle-storyboard-mus.css").read_text(encoding="utf-8"))


def main_aus(datei):
    s = (HIER / datei).read_text(encoding="utf-8")
    return s[s.index("<main>") + 6:s.index("</main>")]


def storyboard_main():
    m = main_aus("quelle-storyboard-mus.html")
    m = m.replace('<p class="kicker">Storyboard</p>', BEISPIEL + '<p class="kicker">Methode · Storyboard</p>', 1)
    m = m.replace("<h1>So entsteht die Landingpage.</h1>", '<h1>So entsteht die <span class="hl">Landingpage.</span></h1>', 1)
    return m


STORYBOARD_CSS = """
.sbm .sk--skizze { border-color: #1a1817; }
.sbm .sk--skizze.sk--navy { border-color: #fff400; }
.sbm .sk--leer { border-color: var(--taupe); }
"""


def storyboard():
    html = (f'<main>\n<div class="sbm">{storyboard_main()}</div>\n'
            f'<style>{QUELL_CSS}{EMPIRIA}{STORYBOARD_CSS}</style>\n</main>')
    seite("methoden-storyboard.html", "Storyboard Landing Page", html)


# ---------- Elevator Pitch ----------
def pitch():
    m = main_aus("quelle-elevator-pitch-mus.html")
    assert '<p class="kicker">Elevator Pitch</p>' in m
    m = m.replace('<p class="kicker">Elevator Pitch</p>', BEISPIEL + '<p class="kicker">Methode · Elevator Pitch</p>', 1)
    m = m.replace("<h1>Unsere Story<br>in 30/10 Sekunden.</h1>", '<h1>Unsere Story<br>in <span class="hl">30/10 Sekunden.</span></h1>', 1)
    m = re.sub(r'<a class="ep-dl".*?</a>', "", m, flags=re.S)        # Download (PDF im M&S-Design) entfällt
    i = m.find('<div class="lp-dl"')
    if i >= 0:
        m = m[:m.rfind("<section", 0, i)] + m[m.find("</section>", i) + 10:]
    m = m.replace('href="/entwicklung/storyboard.html', 'href="/projekte/methoden-storyboard.html')
    html = f'<main>\n<div class="sbm">{m}</div>\n<style>{QUELL_CSS}{EMPIRIA}</style>\n</main>'
    seite("methoden-elevator-pitch.html", "Elevator Pitch", html)


# ---------- Übersicht ----------
def uebersicht():
    karten = [("/projekte/methoden-storyboard.html", "SB", "Storyboard Landing Page",
               "Von den Antworten zur Landingpage: 12 Punkte, 8 Fragen des Lesers, 4 Abschnitte, Entwürfe A und B, daraus die Skizze."),
              ("/projekte/methoden-elevator-pitch.html", "EP", "Elevator Pitch",
               "Von der Landingpage zur halben Minute: sechs Bausteine, sechs Sätze – und eine Kurzfassung für die Vorstellungsrunde.")]
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
    pitch()
    uebersicht()
