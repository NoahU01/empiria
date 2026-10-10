#!/usr/bin/env python3
"""Geschäftsausstattung · Hintergrundbilder (Entwurf, Daniel 10.10.2026).

Vier Motive (Drei Leistungen · Muster Schwarz · Muster Gelb · Startseite) in neun Formaten:
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
    # iPad: iPadOS nutzt EIN Bild für quer und hoch und schneidet die Mitte aus → quadratisch, Wichtiges im mittleren 75-%-Feld
    ("ipad13", "iPad 13″", 2752, 2752, "ipadq", 28.1),
    ("ipadmini", "iPad mini", 2266, 2266, "ipadq", 19.5),
    ("iphone13mini", "iPhone 13 mini", 1080, 2340, "iphone", 6.2),
    ("iphone15", "iPhone 15/16", 1179, 2556, "iphone", 6.7),
    ("iphonepromax", "iPhone Pro Max", 1290, 2796, "iphone", 7.3),
    ("teams", "Teams/Zoom", 1920, 1080, "video", 0),
]
FMT = {f[0]: f for f in FORMATE}

# Motiv: Name, Hintergrund (bestimmt die Farbe von Uhr/Datum), Vordergrund, Logo weiß?, Beschreibung
MOTIVE = {
    "leistungen": ("Drei Leistungen", GELB, SCHWARZ, False,
                   "Die drei Leistungskarten der Startseite als Vollflächen: Gelb mit Doppelpfeil, Schwarz mit gelbem Kreuz, "
                   "Grau mit Kreis. Nebeneinander auf breiten Bildschirmen, übereinander auf iPad und iPhone."),
    "muster-schwarz": ("Muster Schwarz", SCHWARZ, GELB, True,
                       "Ein ruhiges Raster aus Doppelpfeilen, kaum sichtbar auf Schwarz – nur einer leuchtet gelb. "
                       "Für den Dunkelmodus; Symbole und Fenster bleiben gut lesbar."),
    "muster-gelb": ("Muster Gelb", GELB, SCHWARZ, False,
                    "Dasselbe Raster auf Gelb, Ton in Ton – der eine Doppelpfeil ist schwarz."),
    "startseite": ("Startseite", WEISS, SCHWARZ, False,
                   "Der Kopf der Homepage als Bild: „Strategie, die wirkt.“ groß mit gelbem Highlight, daneben der Doppelpfeil."),
    "claim-schwarz": ("Claim Schwarz", SCHWARZ, GELB, True,
                      "Dieselbe Komposition dunkel: weißer Claim, „wirkt.“ im gelben Highlight, gelber Doppelpfeil."),
    "claim-anschnitt-weiss": ("Claim · Anschnitt Weiß", WEISS, SCHWARZ, False,
                              "Claim oben links, ein riesiger schwarzer Doppelpfeil läuft unten rechts aus dem Bild."),
    "claim-anschnitt-schwarz": ("Claim · Anschnitt Schwarz", SCHWARZ, GELB, True,
                                "Claim weiß auf Schwarz, der riesige Doppelpfeil gelb im Anschnitt – die kräftigste Variante."),
    "claim-gelb": ("Claim Gelb", GELB, SCHWARZ, False,
                   "Vollfläche Gelb: Claim schwarz, „wirkt.“ als schwarzer Kasten mit gelber Schrift, schwarzer Doppelpfeil im Anschnitt."),
}
# Claim-Motive: Schrift, Highlight-Fläche, Highlight-Schrift, Pfeil, Anschnitt?
CLAIM = {
    "startseite": ("#1a1817", GELB, "#1a1817", SCHWARZ, False),
    "claim-schwarz": ("#ffffff", GELB, "#1a1817", GELB, False),
    "claim-anschnitt-weiss": ("#1a1817", GELB, "#1a1817", SCHWARZ, True),
    "claim-anschnitt-schwarz": ("#ffffff", GELB, "#1a1817", GELB, True),
    "claim-gelb": ("#1a1817", SCHWARZ, GELB, SCHWARZ, True),
}


def claim_h2(p, x, y, gr, motiv, extra=""):
    fgt, hlbg, hlfg, _, _ = CLAIM[motiv]
    return (f'<h2 style="left:{p(x)};top:{p(y)};font-size:{p(gr)};color:{fgt};{extra}">Strategie,<br>die '
            f'<span class="hl" style="background:{hlbg};color:{hlfg}">wirkt.</span></h2>')
GRAU_FL = "#f3f1ee"

CSS = """
.hg { position: relative; width: 100%; container-type: inline-size; overflow: hidden; background: var(--bg); color: var(--fg); font-family: 'Poppins', sans-serif; }
.hg > * { position: absolute; }
.hg img { display: block; width: auto; }
.hg h2 { margin: 0; font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.025em; line-height: 1.32; color: #1a1817; white-space: nowrap; }
.hg .hl { background: #fff400; color: #1a1817; padding: 0 .1em .04em; border-radius: .12em; }
"""


def zeichen_html(p, name, breite, cx, cy, farbe):
    hoehe = breite * (PFEIL_VERH if name == "forward" else 1)
    return (f'<div style="position:absolute;left:{p(cx - breite / 2)};top:{p(cy - hoehe / 2)};width:{p(breite)}">'
            f'{form(name, farbe)}</div>')


def logo(p, hell, x, y, hoehe, unten=False):
    datei = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    pos = f'bottom:{p(y)}' if unten else f'top:{p(y)}'
    return f'<img src="{datei}" alt="empiria" style="left:{p(x)};{pos};height:{p(hoehe)}">'


def flaeche(p, x, y, w, h, farbe, inhalt=""):
    return f'<div style="left:{p(x)};top:{p(y)};width:{p(w)};height:{p(h)};background:{farbe};overflow:hidden">{inhalt}</div>'


def hintergrund(motiv, fmt):
    _, bg, fg, hell, _ = MOTIVE[motiv]
    _, _, w, h, art, _ = FMT[fmt]
    p = px_fn(w)
    m = min(w, h)
    hoch = h > w
    rand, lh = .055 * m, .032 * m
    teile = []

    if art == "ipadq":  # quadratisch; sichtbar bleibt quer das mittlere 75 % der Höhe, hoch das mittlere 75 % der Breite
        s0, s1 = .125 * w, .875 * w
        if motiv == "leistungen":
            felder = [(GELB, "forward", SCHWARZ, .26), (SCHWARZ, "kreuz", GELB, .5), (GRAU_FL, "kreis", SCHWARZ, .74)]
            for i, (farbe, z, zf, cy) in enumerate(felder):
                gr = .15 * w
                teile.append(flaeche(p, 0, i * h / 3, w, h / 3 + 1, farbe, zeichen_html(p, z, gr, s0 + .05 * w + gr / 2, cy * h - i * h / 3, zf)))
        elif motiv.startswith("muster"):
            ton = "#2b2926" if motiv == "muster-schwarz" else "#ebe100"
            n = 8
            zelle = w / n
            for r in range(n):
                for c in range(n):
                    an = (c, r) == (5, 3)
                    teile.append(zeichen_html(p, "forward", zelle * .52, (c + .5) * zelle, (r + .5) * zelle, fg if an else ton))
        else:  # Claim-Motive
            pf, an = CLAIM[motiv][3], CLAIM[motiv][4]
            gr = .1 * w
            if an:
                teile.append(claim_h2(p, s0 + .05 * w, .2 * h, gr, motiv))
                b = .5 * w  # Anschnitt an der sichtbaren Kante (unten 87,5 %, rechts 87,5 %) – quer und hoch gleich
                teile.append(zeichen_html(p, "forward", b, .875 * w - .3 * b, .875 * h - .35 * b * PFEIL_VERH, pf))
            else:
                teile.append(claim_h2(p, s0 + .05 * w, .3 * h, gr, motiv))
                teile.append(zeichen_html(p, "forward", .26 * w, s0 + .05 * w + .13 * w, .3 * h + 2 * gr * 1.32 + .1 * h, pf))
        return f'<div class="hg" style="aspect-ratio:1/1;--bg:{bg};--fg:{fg}">{"".join(teile)}</div>'

    if motiv == "leistungen":
        felder = [(GELB, "forward", SCHWARZ), (SCHWARZ, "kreuz", GELB), (GRAU_FL, "kreis", SCHWARZ)]
        if not hoch:  # drei Spalten
            sw = w / 3
            for i, (farbe, z, zf) in enumerate(felder):
                gr = (.5 if art != "video" else .4) * sw
                teile.append(flaeche(p, i * sw, 0, sw + 1, h, farbe, zeichen_html(p, z, gr, sw / 2, h * (.5 if art != "video" else .3), zf)))
            if art == "video":
                teile.append(logo(p, False, .03 * w, .06 * h, .04 * h))
            else:
                teile.append(logo(p, False, rand, rand, lh, unten=True))
        else:  # drei Bänder; auf dem iPhone bleibt oben Platz für die Uhr
            grenzen = [0, .42, .71, 1] if art == "iphone" else [0, 1 / 3, 2 / 3, 1]
            for i, (farbe, z, zf) in enumerate(felder):
                y0, y1 = grenzen[i] * h, grenzen[i + 1] * h
                gr = (.26 if art == "iphone" else .24) * w
                if art == "iphone":
                    cy = (y1 - .045 * h - gr * .5) if i == 0 else (y0 + y1) / 2 - (.03 * h if i == 2 else 0)
                else:
                    cy = (y0 + y1) / 2
                x = .1 * w + gr / 2
                teile.append(flaeche(p, 0, y0, w, y1 - y0 + 1, farbe, zeichen_html(p, z, gr, x, cy - y0, zf)))
            if art != "iphone":
                teile.append(logo(p, False, w - rand - lh * 4.4, rand, lh, unten=True))

    elif motiv.startswith("muster"):
        ton = "#2b2926" if motiv == "muster-schwarz" else "#ebe100"
        spalten = {"mac": 8, "ipad": 7 if not hoch else 5, "iphone": 4, "video": 9}[art]
        zelle = w / spalten
        zeilen = int(h / zelle)  # nur ganze Reihen, keine angeschnittenen Pfeile an den Kanten
        oy = (h - zeilen * zelle) / 2
        # der eine Pfeil: rechts der Mitte; iPhone in der unteren Hälfte, Teams am Rand (Person mittig)
        if art == "iphone":
            hx, hy = spalten - 2, int((.66 * h - oy) / zelle)
        elif art == "video":
            hx, hy = spalten - 2, int((.5 * h - oy) / zelle)
        else:
            hx, hy = int(spalten * .62), int((.42 * h - oy) / zelle)
        for r in range(zeilen):
            for c in range(spalten):
                farbe = fg if (c, r) == (hx, hy) else ton
                if art in ("mac", "ipad") and c == 0 and r == zeilen - 1:
                    continue  # hier steht das Logo
                teile.append(zeichen_html(p, "forward", zelle * .52, (c + .5) * zelle, oy + (r + .5) * zelle, farbe))
        if art == "video":
            teile.append(logo(p, hell, .03 * w, .06 * h, .04 * h))
        elif art != "iphone":
            teile.append(logo(p, hell, rand, rand, lh, unten=True))

    else:  # Claim-Motive
        pf, an = CLAIM[motiv][3], CLAIM[motiv][4]
        if an:
            if art == "video":
                gr = .05 * w
                teile.append(claim_h2(p, .045 * w, .08 * h, gr, motiv))
                b = .26 * w
                teile.append(zeichen_html(p, "forward", b, w - .3 * b, h - .35 * b * PFEIL_VERH, pf))
            elif art == "iphone":
                gr = .15 * w
                teile.append(claim_h2(p, .085 * w, .33 * h, gr, motiv))
                b = 1.1 * w
                teile.append(zeichen_html(p, "forward", b, w - .3 * b, h - .38 * b * PFEIL_VERH, pf))
            else:
                gr = .085 * w
                teile.append(claim_h2(p, .08 * w, .12 * h, gr, motiv))
                b = .55 * w
                teile.append(zeichen_html(p, "forward", b, w - .3 * b, h - .35 * b * PFEIL_VERH, pf))
                teile.append(logo(p, hell, rand, rand, lh, unten=True))
        elif art == "video":
            gr = .05 * w
            teile.append(claim_h2(p, .045 * w, .08 * h, gr, motiv))
            teile.append(zeichen_html(p, "forward", .17 * w, w - .045 * w - .085 * w, .2 * h, pf))
        elif art == "iphone":
            gr = .15 * w
            teile.append(claim_h2(p, .085 * w, .5 * h, gr, motiv))
            teile.append(zeichen_html(p, "forward", .34 * w, .085 * w + .17 * w, .5 * h + 2 * gr * 1.32 + .1 * h, pf))
        else:
            gr = .085 * w
            teile.append(claim_h2(p, .08 * w, 0, gr, motiv, "top:50%;transform:translateY(-55%)"))
            teile.append(zeichen_html(p, "forward", .24 * w, w - .1 * w - .12 * w, .48 * h, pf))
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


def geraet(motiv, fmt, lage=None):
    _, name, w, h, art, _ = FMT[fmt]
    bg = MOTIVE[motiv][1]
    ui_farbe = "#fff" if bg == SCHWARZ else "#1a1817"
    ui = ""
    if art == "mac":
        ui = '<div class="ui"><span class="ui-menue"></span><span class="ui-dock"></span></div>'
    elif art == "ipadq":
        ui = '<div class="ui"><span class="ui-dock ui-dock--ipad"></span></div>'
    elif art == "iphone":
        ui = (f'<div class="ui" style="--ui:{ui_farbe}"><span class="ui-insel"></span><span class="ui-datum">Samstag, 10. Oktober</span>'
              '<span class="ui-uhr">9:41</span><span class="ui-knopf" style="left:9cqw"></span><span class="ui-knopf" style="right:9cqw"></span>'
              '<span class="ui-strich"></span></div>')
    elif art == "video":
        ui = f'<div class="ui"><span class="ui-person">{PERSON}</span></div>'
    if art == "ipadq":  # dieselbe quadratische Datei, so beschnitten, wie iPadOS sie zeigt
        if lage == "quer":
            bild = f'<div style="width:100%;margin-top:-12.5%">{hintergrund(motiv, fmt)}</div>'
            return f'<div class="ger ger--ipad"><div class="scr" style="aspect-ratio:4/3">{bild}{ui}</div></div>'
        bild = f'<div style="width:133.333%;margin-left:-16.667%">{hintergrund(motiv, fmt)}</div>'
        return f'<div class="ger ger--ipad"><div class="scr" style="aspect-ratio:3/4">{bild}{ui}</div></div>'
    return f'<div class="ger ger--{art}"><div class="scr">{hintergrund(motiv, fmt)}{ui}</div></div>'


def reihe(motiv, formate, faktor, cls=""):
    figs = []
    for eintrag in formate:
        fmt, _, lage = eintrag.partition(":")
        _, name, w, h, art, cm = FMT[fmt]
        if art == "ipadq":
            gewicht = cm * (1 if lage == "quer" else .75) * faktor
            label = f"{name} {lage} · dieselbe Datei {w} × {h}"
        else:
            gewicht = (cm or 34) * faktor if art != "video" else 46
            label = f"{name} · {w} × {h}"
        breit = " gr-breit" if art in ("mac", "video") else ""
        basis = '<div class="ger-basis"></div>' if art == "mac" else ""
        figs.append(f'<figure class="{breit.strip()}" style="flex:{gewicht:.2f} 1 0">{geraet(motiv, fmt, lage)}{basis}'
                    f'<p class="pm-label">{label}</p></figure>')
    return f'<div class="gr {cls}">{"".join(figs)}</div>'


def main_html():
    teile = []
    for i, (mo, (name, _, _, _, text)) in enumerate(MOTIVE.items(), 1):
        links = "".join(download(f"{WEB}/{png_name(mo, f[0])}", f[1]) for f in FORMATE)
        teile.append(f'<div class="pm-abschnitt"><h2>{i} · {name}</h2><p class="pm-text">{text}</p>'
                     + reihe(mo, ["macbook", "ipad13:quer", "ipad13:hoch", "ipadmini:quer", "ipadmini:hoch"], 1)
                     + reihe(mo, ["iphone13mini", "iphone15", "iphonepromax", "teams"], 1.7, "gr--phones")
                     + f'<p class="pm-dl-titel">PNG in Originalgröße laden</p><div class="pm-dl">{links}</div></div>')
    return (f'<main>\n<section class="pm"><div class="container">'
            + kopf('Hinter&shy;grund&shy;<span class="hl">bilder</span>',
                   'Motive aus der Bildsprache der Homepage – Für MacBook, iPad, iPhone und Videokonferenzen. Beim iPad gibt es je ein quadratisches Bild für quer und hoch – iPadOS schneidet daraus selbst die Mitte aus; gezeigt ist, was in beiden Lagen zu sehen ist. Die Geräte stehen im richtigen Größenverhältnis nebeneinander. '
                   'Auf dem iPhone bleiben Uhr und Widgets oben sowie die Knöpfe unten frei; bei Teams und Zoom sitzt die Person in der Mitte – alles Wichtige liegt am Rand.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{SEITE_EXTRA}</style>\n</main>')


if __name__ == "__main__":
    seite("ga-hintergruende.html", "Hintergrundbilder", main_html())
    if "--ohne-png" not in sys.argv:
        exportieren(CSS, jobs())
