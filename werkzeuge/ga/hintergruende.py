#!/usr/bin/env python3
"""Geschäftsausstattung · Hintergrundbilder (Entwurf, Daniel 10.10.2026).

Vier Motive (Flächenwechsel · Anschnitt Gelb · Anschnitt Schwarz · Claim) in neun Formaten:
MacBook, iPad 13" quer/hoch, iPad mini quer/hoch, iPhone 13 mini, iPhone 15/16, iPhone Pro Max, Teams/Zoom.
Regeln: iPhone – oben Uhr/Widgets (bis ca. 30 %) und unten Dock/Knöpfe (ab ca. 85 %) frei;
Teams/Zoom – die Person sitzt mittig, Elemente nur am Rand.
Gestaltung in Originalpixeln, umgerechnet in cqw – Vorschau und PNG sind identisch.

Aufruf: python3 werkzeuge/ga/hintergruende.py           → Seite + 45 PNGs
        python3 werkzeuge/ga/hintergruende.py --ohne-png → nur Seite
Ergebnis: site/projekte/ga-hintergruende.html, site/projekte/ga/hintergruende/*.png
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ga_export import (GELB, GRAU, PFEIL_VERH, SCHWARZ, SEITE_CSS, SITE, WEISS, download, exportieren,  # noqa: E402
                       form, kopf, px_fn, seite)

ORDNER = SITE / "projekte" / "ga" / "hintergruende"
WEB = "/projekte/ga/hintergruende"

# Schlüssel, Name, Breite, Höhe, Art, Bildschirmbreite in cm (für die maßstäbliche Gerätereihe)
FORMATE = [
    ("macbook", "MacBook", 3024, 1964, "mac", 30.2),
    ("ipad13-quer", "iPad 13″ quer", 2752, 2064, "ipad", 28.1),
    ("ipad13-hoch", "iPad 13″ hoch", 2064, 2752, "ipad", 21.0),
    ("ipadmini-quer", "iPad mini quer", 2266, 1488, "ipad", 19.5),
    ("ipadmini-hoch", "iPad mini hoch", 1488, 2266, "ipad", 13.4),
    ("iphone13mini", "iPhone 13 mini", 1080, 2340, "iphone", 6.2),
    ("iphone15", "iPhone 15/16", 1179, 2556, "iphone", 6.7),
    ("iphonepromax", "iPhone Pro Max", 1290, 2796, "iphone", 7.3),
    ("teams", "Teams/Zoom", 1920, 1080, "video", 0),
]
FMT = {f[0]: f for f in FORMATE}

# Motiv: Name, Hintergrund (bestimmt die Farbe von Uhr/Datum), Vordergrund, Logo weiß?, Beschreibung
MOTIVE = {
    "wechsel": ("Flächenwechsel", GELB, SCHWARZ, False,
                "Die Idee der Website als Bild: oben Gelb, unten Schwarz – genau an der Kante sitzt der Doppelpfeil und wechselt mit der Fläche "
                "die Farbe (schwarz auf Gelb, gelb auf Schwarz). Uhr und Widgets stehen auf dem ruhigen Gelb."),
    "gelb": ("Anschnitt Gelb", GELB, SCHWARZ, False,
             "Ein einziges Zeichen, riesig und vom Rand angeschnitten: der Doppelpfeil läuft aus dem Bild – nach vorne. Viel freie Fläche für Symbole und Fenster."),
    "schwarz": ("Anschnitt Schwarz", SCHWARZ, GELB, True,
                "Dieselbe Geste auf Schwarz mit gelbem Pfeil. Für den Dunkelmodus und abends angenehm."),
    "claim": ("Claim", WEISS, SCHWARZ, False,
              "Weiß, nur der Claim „Strategie, die wirkt.“ – groß gesetzt wie die Überschriften der Website, „wirkt.“ im gelben Highlight."),
}

CSS = """
.hg { position: relative; width: 100%; container-type: inline-size; overflow: hidden; background: var(--bg); color: var(--fg); font-family: 'Poppins', sans-serif; }
.hg > * { position: absolute; }
.hg img { display: block; width: auto; }
.hg-flaeche { left: 0; width: 100%; overflow: hidden; }
.hg h2 { margin: 0; font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.025em; line-height: 1.32; color: var(--fg); white-space: nowrap; }
.hg .hl { background: #fff400; color: #1a1817; padding: 0 .1em .04em; border-radius: .12em; }
"""


def pfeil(p, breite, cx, cy, farbe):
    hoehe = breite * PFEIL_VERH
    return (f'<div style="position:absolute;left:{p(cx - breite / 2)};top:{p(cy - hoehe / 2)};width:{p(breite)}">'
            f'{form("forward", farbe)}</div>')


def logo(p, hell, x, y, hoehe, unten=False):
    datei = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    pos = f'bottom:{p(y)}' if unten else f'top:{p(y)}'
    return f'<img src="{datei}" alt="empiria" style="left:{p(x)};{pos};height:{p(hoehe)}">'


def hintergrund(motiv, fmt):
    _, bg, fg, hell, _ = MOTIVE[motiv]
    _, _, w, h, art, _ = FMT[fmt]
    p = px_fn(w)
    m = min(w, h)
    hoch = h > w
    rand, lh = .055 * m, .032 * m          # Randabstand, Logohöhe
    teile = []

    if motiv == "wechsel":
        if art == "video":
            g, b, cx = .72 * h, .32 * w, w - .3 * .32 * w
        elif art == "iphone":
            g, b, cx = .6 * h, .92 * w, .6 * w
        elif hoch:
            g, b, cx = .6 * h, .78 * w, .58 * w
        else:
            g, b, cx = .62 * h, .5 * w, .64 * w
        oben = f'<div class="hg-flaeche" style="top:0;height:{p(g)};background:{GELB}">{pfeil(p, b, cx, g, SCHWARZ)}</div>'
        unten = (f'<div class="hg-flaeche" style="top:{p(g)};height:{p(h - g)};background:{SCHWARZ}">'
                 f'<div style="position:absolute;left:0;top:{p(-g)};width:100%;height:{p(h)}">{pfeil(p, b, cx, g, GELB)}</div></div>')
        teile += [oben, unten]
        if art == "video":
            teile.append(logo(p, False, .045 * w, .07 * h, .045 * h))
        elif art != "iphone":
            teile.append(logo(p, True, rand, rand, lh, unten=True))

    elif motiv in ("gelb", "schwarz"):
        if art == "video":      # nur der erste Winkel ragt von rechts ins Bild – die Mitte bleibt der Person
            b = 1.3 * h / PFEIL_VERH
            teile.append(pfeil(p, b, .73 * w + b / 2, .5 * h, fg))
            teile.append(logo(p, hell, .045 * w, .07 * h, .045 * h))
        elif art == "iphone":   # Uhr oben frei, Pfeil in der unteren Hälfte, rechts angeschnitten
            b = 1.15 * w
            teile.append(pfeil(p, b, w - .3 * b, .69 * h, fg))
        elif hoch:
            b = 1.05 * w
            teile.append(pfeil(p, b, w - .3 * b, .55 * h, fg))
            teile.append(logo(p, hell, rand, rand, lh, unten=True))
        else:
            b = .85 * w
            teile.append(pfeil(p, b, w - .3 * b, .5 * h, fg))
            teile.append(logo(p, hell, rand, rand, lh, unten=True))

    elif motiv == "claim":
        if art == "video":
            gr = .045 * w
            teile.append(logo(p, hell, .045 * w, .07 * h, .045 * h))
            teile.append(f'<h2 style="left:{p(.045 * w)};bottom:{p(.08 * h)};font-size:{p(gr)}">Strategie,<br>die <span class="hl">wirkt.</span></h2>')
        elif hoch:
            gr = (.165 if art == "iphone" else .13) * w
            oben = (.5 if art == "iphone" else .46) * h
            teile.append(f'<h2 style="left:{p(.085 * w)};top:{p(oben)};font-size:{p(gr)}">Strategie,<br>die<br><span class="hl">wirkt.</span></h2>')
            if art != "iphone":
                teile.append(logo(p, hell, rand, rand, lh, unten=True))
        else:
            gr = .088 * w
            teile.append(f'<h2 style="left:{p(.07 * w)};bottom:{p(.2 * h)};font-size:{p(gr)}">Strategie,<br>die <span class="hl">wirkt.</span></h2>')
            teile.append(logo(p, hell, rand, rand, lh, unten=True))

    return f'<div class="hg" style="aspect-ratio:{w}/{h};--bg:{bg};--fg:{fg}">{"".join(teile)}</div>'


def png_name(motiv, fmt):
    w, h = FMT[fmt][2], FMT[fmt][3]
    return f"empiria-hintergrund-{motiv}-{fmt}-{w}x{h}.png"


def jobs():
    return [{"html": hintergrund(mo, f[0]), "w": f[2], "h": f[3], "pfad": ORDNER / png_name(mo, f[0])}
            for mo in MOTIVE for f in FORMATE]


# ----- Vorschau: Gerätereihe -----
SEITE_EXTRA = """
.gr { display: flex; align-items: flex-end; gap: 1.4rem; margin-top: 1.6rem; }
.gr + .gr { margin-top: 2.2rem; }
.gr figure { margin: 0; min-width: 0; container-type: inline-size; }
.gr .pm-label { font-size: .64rem; letter-spacing: .08em; }
.ger { position: relative; background: #1a1817; box-shadow: 0 14px 30px rgba(26,24,23,.12); }
.ger > .scr { position: relative; overflow: hidden; }
.ger--mac { padding: 2.2cqw 2.2cqw 3cqw; border-radius: 2.4cqw 2.4cqw .6cqw .6cqw; }
.ger--mac > .scr { border-radius: .6cqw; }
.ger--mac::after { content: ""; position: absolute; left: -6cqw; right: -6cqw; bottom: -2.4cqw; height: 2.4cqw; border-radius: 0 0 3cqw 3cqw; background: linear-gradient(#d6d3cf, #b9b5b0); }
.ger-basis { height: 1.4rem; }
.ger--ipad { padding: 3.6cqw; border-radius: 6cqw; }
.ger--ipad > .scr { border-radius: 3cqw; }
.ger--iphone { padding: 4.2cqw; border-radius: 15cqw; }
.ger--iphone > .scr { border-radius: 11cqw; }
.ger--video { padding: 0; border-radius: 1.2cqw; background: #2b2b2b; padding-top: 4cqw; }
.ger--video::before { content: "● ● ●"; position: absolute; left: 1.6cqw; top: 1.1cqw; font-size: 1.6cqw; letter-spacing: .3em; color: #6b6b6b; }
.ui { position: absolute; inset: 0; pointer-events: none; }
.ui-menue { position: absolute; left: 0; right: 0; top: 0; height: 2.1cqw; background: rgba(255,255,255,.45); backdrop-filter: blur(4px); }
.ui-dock { position: absolute; left: 30%; right: 30%; bottom: 1.6cqw; height: 5.4cqw; border-radius: 1.6cqw; background: rgba(255,255,255,.4); box-shadow: 0 0 0 1px rgba(0,0,0,.06); }
.ui-dock--ipad { left: 22%; right: 22%; height: 7cqw; bottom: 2.2cqw; border-radius: 2.4cqw; }
.ui-insel { position: absolute; left: 50%; top: 3.2cqw; width: 30cqw; height: 8.6cqw; transform: translateX(-50%); background: #000; border-radius: 99px; }
.ui-datum { position: absolute; left: 0; right: 0; top: 19cqw; text-align: center; font: 600 5.2cqw/1 -apple-system, 'Poppins', sans-serif; color: var(--ui); }
.ui-uhr { position: absolute; left: 0; right: 0; top: 25cqw; text-align: center; font: 600 23cqw/1 -apple-system, 'Poppins', sans-serif; letter-spacing: -.02em; color: var(--ui); }
.ui-knopf { position: absolute; bottom: 9cqw; width: 12cqw; height: 12cqw; border-radius: 50%; background: rgba(120,120,120,.35); backdrop-filter: blur(4px); }
.ui-strich { position: absolute; left: 50%; bottom: 2.2cqw; width: 36cqw; height: 1.3cqw; border-radius: 99px; transform: translateX(-50%); background: var(--ui); opacity: .8; }
.ui-person { position: absolute; left: 50%; bottom: 0; width: 34%; transform: translateX(-50%); }
.ui-person svg { display: block; width: 100%; height: auto; }
.pm-dl-titel { margin: 1.4rem 0 0; font: 600 .78rem/1.4 'Poppins', sans-serif; color: #1a1817; }
@media (max-width: 800px) {
  .gr { flex-wrap: wrap; align-items: flex-end; gap: 1.6rem 1rem; }
  .gr > figure { flex: 0 0 calc(50% - .5rem) !important; }
  .gr > figure.gr-breit { flex-basis: 100% !important; }
  .gr--phones > figure { flex: 0 0 calc(33.333% - .67rem) !important; }
}
"""

PERSON = ('<svg viewBox="0 0 200 170" aria-hidden="true"><circle cx="100" cy="58" r="38" fill="rgba(60,60,60,.55)"/>'
          '<path d="M14 170c0-48 38-74 86-74s86 26 86 74z" fill="rgba(60,60,60,.55)"/></svg>')


def geraet(motiv, fmt):
    _, name, w, h, art, _ = FMT[fmt]
    bg = MOTIVE[motiv][1]
    ui_farbe = "#fff" if bg == SCHWARZ else "#1a1817"
    ui = ""
    if art == "mac":
        ui = '<div class="ui"><span class="ui-menue"></span><span class="ui-dock"></span></div>'
    elif art == "ipad":
        ui = '<div class="ui"><span class="ui-dock ui-dock--ipad"></span></div>'
    elif art == "iphone":
        ui = (f'<div class="ui" style="--ui:{ui_farbe}"><span class="ui-insel"></span><span class="ui-datum">Samstag, 10. Oktober</span>'
              '<span class="ui-uhr">9:41</span><span class="ui-knopf" style="left:9cqw"></span><span class="ui-knopf" style="right:9cqw"></span>'
              '<span class="ui-strich"></span></div>')
    elif art == "video":
        ui = f'<div class="ui"><span class="ui-person">{PERSON}</span></div>'
    return f'<div class="ger ger--{art}"><div class="scr">{hintergrund(motiv, fmt)}{ui}</div></div>'


def reihe(motiv, formate, faktor, cls=""):
    figs = []
    for fmt in formate:
        _, name, w, h, art, cm = FMT[fmt]
        gewicht = (cm or 34) * faktor if art != "video" else 46
        breit = " gr-breit" if art in ("mac", "video") else ""
        basis = '<div class="ger-basis"></div>' if art == "mac" else ""
        figs.append(f'<figure class="{breit.strip()}" style="flex:{gewicht:.2f} 1 0">{geraet(motiv, fmt)}{basis}'
                    f'<p class="pm-label">{name} · {w} × {h}</p></figure>')
    return f'<div class="gr {cls}">{"".join(figs)}</div>'


def main_html():
    teile = []
    for i, (mo, (name, _, _, _, text)) in enumerate(MOTIVE.items(), 1):
        links = "".join(download(f"{WEB}/{png_name(mo, f[0])}", f[1]) for f in FORMATE)
        teile.append(f'<div class="pm-abschnitt"><h2>{i} · {name}</h2><p class="pm-text">{text}</p>'
                     + reihe(mo, ["macbook", "ipad13-quer", "ipad13-hoch", "ipadmini-quer", "ipadmini-hoch"], 1)
                     + reihe(mo, ["iphone13mini", "iphone15", "iphonepromax", "teams"], 1.7, "gr--phones")
                     + f'<p class="pm-dl-titel">PNG in Originalgröße laden</p><div class="pm-dl">{links}</div></div>')
    return (f'<main>\n<section class="pm"><div class="container">'
            + kopf('Hinter&shy;grund&shy;<span class="hl">bilder</span>',
                   'Vier Motive, eine Haltung: wenige, große Flächen und ein einziges Zeichen – wie auf der Website. Für MacBook, iPad, iPhone und Videokonferenzen. Die Geräte stehen im richtigen Größenverhältnis nebeneinander. '
                   'Auf dem iPhone bleiben Uhr und Widgets oben sowie die Knöpfe unten frei; bei Teams und Zoom sitzt die Person in der Mitte – alles Wichtige liegt am Rand.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{SEITE_EXTRA}</style>\n</main>')


if __name__ == "__main__":
    seite("ga-hintergruende.html", "Hintergrundbilder", main_html())
    if "--ohne-png" not in sys.argv:
        exportieren(CSS, jobs())
