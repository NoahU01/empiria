#!/usr/bin/env python3
"""Geschäftsausstattung · Hintergrundbilder (Entwurf, Daniel 10.10.2026).

Fünf Motive (Doppelpfeil auf Weiß, Gelb, Schwarz · Formen-Kacheln · Claim) in neun Formaten:
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

# Motiv: Name, Hintergrund, Vordergrund, Logo weiß?, Beschreibung
MOTIVE = {
    "weiss": ("Doppelpfeil auf Weiß", WEISS, SCHWARZ, False,
              "Die ruhigste Variante: weiße Fläche, großer schwarzer Doppelpfeil in der Mitte, kleines Logo in der Ecke."),
    "gelb": ("Doppelpfeil auf Gelb", GELB, SCHWARZ, False,
             "Dieselbe Komposition auf Gelb – alles darauf schwarz. Am auffälligsten, gut für Messe- und Präsentationsrechner."),
    "schwarz": ("Doppelpfeil auf Schwarz", SCHWARZ, GELB, True,
                "Dieselbe Komposition auf Schwarz mit gelbem Doppelpfeil. Augenschonend im Dunkelmodus, wirkt edel."),
    "formen": ("Formen-Kacheln", GRAU, SCHWARZ, False,
               "Graue Fläche mit weißen Kacheln aus den Markenformen, eine Kachel gelb – wie die Icon-Raster der Website."),
    "claim": ("Claim", WEISS, SCHWARZ, False,
              "Weiß mit Logo und Claim „Strategie, die wirkt.“ im gelben Highlight, links ausgerichtet wie die Website-Überschriften."),
}

CSS = """
.hg { position: relative; width: 100%; container-type: inline-size; overflow: hidden; background: var(--bg); color: var(--fg); font-family: 'Poppins', sans-serif; }
.hg > * { position: absolute; }
.hg img { display: block; width: auto; }
.hg-raster { display: grid; }
.hg-raster > span { display: flex; align-items: center; justify-content: center; background: #fff; }
.hg-raster > span.gelb { background: #fff400; }
.hg h2 { margin: 0; font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.2; color: var(--fg); white-space: nowrap; }
.hg .hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; }
"""


def pfeil(p, w, h, breite, cx, cy, farbe):
    hoehe = breite * PFEIL_VERH
    return f'<div style="left:{p(cx - breite / 2)};top:{p(cy - hoehe / 2)};width:{p(breite)}">{form("forward", farbe)}</div>'


def logo(p, hell, x, y, hoehe, rechts=False):
    datei = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    pos = f'right:{p(x)}' if rechts else f'left:{p(x)}'
    return f'<img src="{datei}" alt="empiria" style="{pos};top:{p(y)};height:{p(hoehe)}">'


def kacheln(p, namen, spalten, zelle, gap, x, y):
    zeilen = (len(namen) + spalten - 1) // spalten
    breite = spalten * zelle + (spalten - 1) * gap
    inhalt = "".join(
        f'<span class="{"gelb" if n == "forward" else ""}" style="border-radius:{p(zelle * .17)}">'
        f'<i style="display:block;width:{p(zelle * (.52 if n == "forward" else .46))}">{form(n, SCHWARZ)}</i></span>' for n in namen)
    return (f'<div class="hg-raster" style="left:{p(x)};top:{p(y)};width:{p(breite)};grid-template-columns:repeat({spalten},1fr);'
            f'gap:{p(gap)};grid-auto-rows:{p(zelle)}">{inhalt}</div>'), breite, zeilen * zelle + (zeilen - 1) * gap


def claim(p, groesse, x, y, zweizeilig, hell, logo_h):
    """Logo + Claim als Block; y = Oberkante des Blocks."""
    datei = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    umbruch = "<br>" if zweizeilig else " "
    return (f'<div style="left:{p(x)};top:{p(y)}"><img src="{datei}" alt="empiria" style="height:{p(logo_h)};margin-bottom:{p(groesse * .38)}">'
            f'<h2 style="font-size:{p(groesse)}">Strategie,{umbruch}die <span class="hl">wirkt.</span></h2></div>')


def hintergrund(motiv, fmt):
    _, bg, fg, hell, _ = MOTIVE[motiv]
    _, _, w, h, art, _ = FMT[fmt]
    p = px_fn(w)
    m = min(w, h)
    teile = []
    hoch = h > w

    if motiv in ("weiss", "gelb", "schwarz"):
        if art == "video":  # Person mittig → Pfeil an den rechten Rand, Logo oben links
            b = .16 * w
            teile.append(pfeil(p, w, h, b, w - .07 * w - b / 2, h * .5, fg))
            teile.append(logo(p, hell, .05 * w, .075 * h, .045 * h))
        elif art == "iphone":  # Uhr oben, Dock unten frei → Pfeil in der Mitte, kein Logo
            teile.append(pfeil(p, w, h, .56 * w, w / 2, h * .57, fg))
        else:
            b = (.46 if hoch else .31) * w
            teile.append(pfeil(p, w, h, b, w / 2, h * (.52 if hoch else .5), fg))
            teile.append(logo(p, hell, .05 * m, h - .05 * m - .035 * m, .035 * m))

    elif motiv == "formen":
        if art == "video":  # Kacheln am rechten Rand, Logo oben links
            z, g = .085 * w, .014 * w
            html, bw, bh = kacheln(p, ["forward", "kreis", "stern"], 1, z, g, 0, 0)
            html = html.replace(f"left:{p(0)};top:{p(0)}", f"left:{p(w - .06 * w - bw)};top:{p((h - bh) / 2)}")
            teile.append(html)
            teile.append(logo(p, hell, .05 * w, .075 * h, .045 * h))
        elif hoch:
            z, g = (.2 if art == "iphone" else .15) * w, (.035 if art == "iphone" else .025) * w
            namen = ["forward", "kreis", "kreuz", "stern", "raute", "blase"]
            html, bw, bh = kacheln(p, namen, 3, z, g, 0, 0)
            cy = h * (.57 if art == "iphone" else .52)
            teile.append(html.replace(f"left:{p(0)};top:{p(0)}", f"left:{p((w - bw) / 2)};top:{p(cy - bh / 2)}"))
            if art != "iphone":
                teile.append(logo(p, hell, .05 * m, h - .05 * m - .035 * m, .035 * m))
        else:
            z, g = .115 * w, .018 * w
            namen = ["forward", "kreis", "kreuz", "quadrat", "stern", "raute", "blase", "blitz"]
            html, bw, bh = kacheln(p, namen, 4, z, g, 0, 0)
            teile.append(html.replace(f"left:{p(0)};top:{p(0)}", f"left:{p((w - bw) / 2)};top:{p((h - bh) / 2)}"))
            teile.append(logo(p, hell, .05 * m, h - .05 * m - .035 * m, .035 * m))

    elif motiv == "claim":
        if art == "video":  # Logo oben links, Claim unten links – Mitte bleibt frei
            gr = .042 * w
            teile.append(logo(p, hell, .05 * w, .075 * h, .045 * h))
            teile.append(f'<div style="left:{p(.05 * w)};bottom:{p(.08 * h)}"><h2 style="font-size:{p(gr)}">Strategie,<br>die <span class="hl">wirkt.</span></h2></div>')
            b = .075 * w
            teile.append(pfeil(p, w, h, b, w - .05 * w - b / 2, h - .08 * h - b * PFEIL_VERH / 2, fg))
        elif hoch:
            gr = (.13 if art == "iphone" else .1) * w
            lh = (.05 if art == "iphone" else .04) * w
            blockh = lh + gr * .38 + 2 * gr * 1.2
            cy = h * (.58 if art == "iphone" else .5)
            teile.append(claim(p, gr, .1 * w, cy - blockh / 2, True, hell, lh))
            if art != "iphone":
                b = .14 * w
                teile.append(pfeil(p, w, h, b, w - .1 * w - b / 2, h - .05 * m - b * PFEIL_VERH / 2 - .02 * m, fg))
        else:
            gr = .065 * w
            lh = .028 * w
            blockh = lh + gr * .38 + gr * 1.2
            teile.append(claim(p, gr, .09 * w, (h - blockh) / 2, False, hell, lh))
            b = .1 * w
            teile.append(pfeil(p, w, h, b, w - .09 * w - b / 2, h - .06 * m - b * PFEIL_VERH / 2, fg))

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
                   'Fünf Motive für MacBook, iPad, iPhone und Videokonferenzen. Die Geräte stehen im richtigen Größenverhältnis nebeneinander. '
                   'Auf dem iPhone bleiben Uhr und Widgets oben sowie die Knöpfe unten frei; bei Teams und Zoom sitzt die Person in der Mitte – alles Wichtige liegt am Rand.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{SEITE_EXTRA}</style>\n</main>')


if __name__ == "__main__":
    seite("ga-hintergruende.html", "Hintergrundbilder", main_html())
    if "--ohne-png" not in sys.argv:
        exportieren(CSS, jobs())
