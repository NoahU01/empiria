#!/usr/bin/env python3
"""Weihnachtskarten – Entwürfe (Daniel, 17.10.2026).

Format: DIN lang quer (210 × 99 mm), Falz an der kurzen Seite → aufgeklappt 420 × 99 mm.
Je Variante: Vorderseite (zugeklappt), Rückseite, Innenseite (links Wünsche, rechts Platz für persönliche Worte).
Drei Varianten, jede aus der empiria-Formensprache:
  A · Ohne Agenda     – gelb, großer Stern im Anschnitt; Rückseite „Agenda für die Feiertage“
  B · Luft nach oben  – weiß, Doppelpfeile nach oben als Tannenbaum; Rückseite gelb „2027 kann kommen.“
  C · Abschalten      – schwarz, die Formen hängen als Kugeln; Rückseite: die gelbe Kugel ist heruntergefallen
Ansprache bewusst neutral (weder Du noch Sie).

Aufruf: python3 werkzeuge/ga/weihnachtskarten.py [--ohne-png]
"""
import sys

from ga_basis import (FORM, GELB, SCHWARZ, abschnitt, download, figur, logo, masse, png_export, raster,
                      seite_schreiben, zeichen)

DATEI = "ga-weihnachtskarten.html"
KARTE_PX, INNEN_PX = 840, 1680  # 4 px je mm


def pfeil_hoch(farbe):
    """Der Doppelpfeil, um 90° gedreht – zeigt nach oben."""
    return (f'<svg viewBox="31.08 -229.61 170.29 226.78" fill="{farbe}" color="{farbe}" aria-hidden="true">'
            f'<g transform="rotate(-90)">{FORM["forward"]}</g></svg>')


def karte(inhalt, bg, fg, cls, png):
    return (f'<div class="wk ga-blatt {cls}" style="--bg:{bg};--fg:{fg}" data-png="ga/weihnachtskarten/{png}.png" '
            f'data-pw="{KARTE_PX}">{inhalt}</div>')


def innen(links, akzent, png, cls=""):
    linien = "".join('<span class="wk-linie"></span>' for _ in range(4))
    return (f'<div class="wki ga-blatt {cls}" data-png="ga/weihnachtskarten/{png}.png" data-pw="{INNEN_PX}"><span class="wki-flaeche"></span>'
            f'<div class="wki-links"><p class="wki-kicker"><span class="wki-akzent">{akzent}</span>Frohe Weihnachten</p>{links}</div>'
            f'<div class="wki-rechts">{linien}</div>{logo(cls="wki-logo")}<span class="wki-falz"></span></div>')


def innentext(h, text):
    return f'<p class="wki-h">{h}</p><p class="wki-text">{text}</p>'


# ---------- A · Ohne Agenda ----------
def a_vorne():
    return karte(f'{logo(cls="wk-logo")}'
                 f'<span class="wka-stern">{zeichen("stern", SCHWARZ)}</span>'
                 f'<span class="wka-stern wka-stern--2">{zeichen("stern", SCHWARZ)}</span>'
                 f'<span class="wka-stern wka-stern--3">{zeichen("stern", SCHWARZ)}</span>'
                 '<p class="wk-spruch">Jetzt mal<br>ohne <span class="wk-hl wk-hl--schwarz">Agenda.</span></p>', GELB, SCHWARZ, "wka", "a-vorderseite")


def a_hinten():
    punkte = [("01", "Durchatmen."), ("02", "Zeit verschenken."), ("03", "Nichts optimieren.")]
    liste = "".join(f'<li><i>{n}</i>{t}</li>' for n, t in punkte)
    return karte('<p class="wk-kicker">Agenda für die Feiertage</p>'
                 f'<ol class="wka-agenda">{liste}</ol>'
                 f'<div class="wk-absender">{logo(True, "wk-logo-klein")}<span>www.empiria.de</span></div>',
                 SCHWARZ, "#fff", "wka-r", "a-rueckseite")


def a_innen():
    return innen(innentext("Danke für ein Jahr<br>voller <span class=\"wk-hl wk-hl--schwarz\">guter Fragen.</span>",
                           "Für das Vertrauen, die offenen Gespräche und jede Strategie, die im Alltag angekommen ist. "
                           "Wir wünschen Feiertage ohne Tagesordnung – und für 2027 Klarheit bei allem, was ansteht."),
                 zeichen("stern", SCHWARZ), "a-innen", "wki--gelb")


# ---------- B · Luft nach oben ----------
def b_vorne():
    """Viele kleine Doppelpfeile nach oben ergeben gemeinsam den Baum – der Stern ist die Spitze."""
    zeilen = [1, 2, 3, 4, 5]
    teile = []
    for r, n in enumerate(zeilen):
        for c in range(n):
            x = (c - (n - 1) / 2)
            if r == 0:
                teile.append(f'<span class="wkb-stern" style="--x:{x};--r:{r}">{zeichen("stern", GELB)}</span>')
            else:
                teile.append(f'<span class="wkb-p" style="--x:{x};--r:{r}">{pfeil_hoch(SCHWARZ)}</span>')
    return karte(f'{logo(cls="wk-logo")}<div class="wkb-baum">{"".join(teile)}<span class="wkb-stamm"></span></div>'
                 '<p class="wk-spruch">Nach oben ist<br>noch <span class="wk-hl">Luft.</span></p>', "#fff", SCHWARZ, "wkb", "b-vorderseite")


def b_hinten():
    return karte(f'<span class="wkb-r-pfeil">{pfeil_hoch(SCHWARZ)}</span>'
                 '<p class="wk-satz">2027 kann<br>kommen.</p>'
                 f'<div class="wk-absender">{logo(cls="wk-logo-klein")}<span>www.empiria.de</span></div>',
                 GELB, SCHWARZ, "wkb-r", "b-rueckseite")


def b_innen():
    return innen(innentext("Wachsen braucht<br>auch Pausen.",
                           "Danke für ein Jahr, in dem wir gemeinsam vorangekommen sind. Jetzt ist Zeit für Familie, "
                           "Freunde und alles, was im Kalender zu kurz kommt. Frohe Weihnachten und einen guten Start in 2027."),
                 pfeil_hoch(SCHWARZ), "b-innen", "wki--grau")


# ---------- C · Abschalten ----------
KUGELN = [("kreis", 118, 34, "#fff"), ("raute", 141, 52, "#fff"), ("stern", 162, 26, GELB), ("quadrat", 184, 44, "#fff")]


def c_vorne():
    kugeln = "".join(f'<span class="wkc-kugel" style="--x:{x};--l:{l}"><i></i><b></b>{zeichen(n, f)}</span>' for n, x, l, f in KUGELN)
    return karte(f'{logo(True, "wk-logo")}{kugeln}'
                 '<p class="wk-spruch">Abschalten ist auch<br>eine <span class="wk-hl">Strategie.</span></p>',
                 SCHWARZ, "#fff", "wkc", "c-vorderseite")


def c_hinten():
    return karte('<p class="wk-satz wk-satz--klein">Zwischen den Jahren<br>sind wir kurz offline.</p>'
                 '<span class="wkc-boden"></span><span class="wkc-gefallen"></span>'
                 f'<div class="wk-absender">{logo(cls="wk-logo-klein")}<span>www.empiria.de</span></div>',
                 "#fff", SCHWARZ, "wkc-r", "c-rueckseite")


def c_innen():
    return innen(innentext("Das Jahr darf jetzt<br>Pause machen.",
                           "Danke für die Zusammenarbeit, das Vertrauen und die vielen guten Gespräche. Wir wünschen "
                           "Feiertage ohne Termine – und einen Start ins Jahr 2027, der Lust auf Neues macht."),
                 '<span class="wki-punkt"></span>', "c-innen", "wki--schwarz")


VARIANTEN = [
    ("a", "A · Ohne Agenda", "Gelb, der empiria-Stern groß im Anschnitt. Der Spruch nimmt den Beratungsalltag auf die Schippe – "
     "und die Rückseite liefert die Agenda trotzdem: drei Punkte für die Feiertage.", a_vorne, a_hinten, a_innen),
    ("b", "B · Luft nach oben", "Viele kleine Doppelpfeile, alle nach oben, ergeben gemeinsam den Tannenbaum – mit gelbem "
     "Stern als Spitze. Die Rückseite in Gelb schaut nach vorn.", b_vorne, b_hinten, b_innen),
    ("c", "C · Abschalten", "Die empiria-Formen hängen als Christbaumkugeln von der Oberkante, eine leuchtet gelb. Auf der "
     "Rückseite ist genau diese Kugel heruntergefallen – und das Büro kurz offline.", c_vorne, c_hinten, c_innen),
]


def inhalt():
    teile = []
    for k, titel, text, vorne, hinten, inn in VARIANTEN:
        dl = lambda n, t: download(f"ga/weihnachtskarten/{k}-{n}.png", t)
        aussen = raster([figur(vorne(), "<b>Vorderseite</b> · zugeklappt · 210 × 99 mm", dl("vorderseite", "PNG Vorderseite")),
                         figur(hinten(), "<b>Rückseite</b> · 210 × 99 mm", dl("rueckseite", "PNG Rückseite"))], 2, 1)
        inn_fig = ('<div class="wk-innen-wrap">' +
                   figur(inn(), "<b>Innenseite</b> · aufgeklappt · 420 × 99 mm · links die Wünsche, rechts Platz für persönliche Worte",
                         dl("innen", "PNG Innenseite")) + '</div>')
        teile.append(abschnitt(titel, text, aussen + inn_fig))
    return "".join(teile)


KARTE_CSS = masse("""
.wk { position: relative; aspect-ratio: 210 / 99; container-type: inline-size; background: var(--bg); color: var(--fg); overflow: hidden;
  border-radius: 3px; font-family: 'Poppins', sans-serif; }
.wk p, .wk ol { margin: 0; }
.wk-logo { position: absolute; left: [12]; top: [11]; height: [4.6]; width: auto; display: block; }
.wk-spruch { position: absolute; left: [12]; bottom: [12]; font: 700 [11.5]/1.08 'Lora', Georgia, serif; letter-spacing: -.02em; }
.wk-hl { background: #fff400; color: #1a1817; padding: 0 .1em .04em; border-radius: .12em; }
.wk-hl--schwarz { background: #1a1817; color: #fff400; }
.wk svg { display: block; width: 100%; height: auto; }
.wk-kicker { position: absolute; left: [12]; top: [12]; display: flex; align-items: center; gap: [2.4];
  font: 700 [3.2]/1 'Poppins', sans-serif; letter-spacing: .16em; text-transform: uppercase; color: #fff400; }
.wk-kicker::before { content: ""; width: [6]; height: [0.7]; background: currentColor; }
.wk-satz { position: absolute; left: [12]; top: [12]; font: 700 [10]/1.1 'Lora', Georgia, serif; letter-spacing: -.02em; }
.wk-satz--klein { font-size: [8.4]; }
.wk-absender { position: absolute; left: [12]; right: [12]; bottom: [10]; display: flex; justify-content: space-between; align-items: flex-end;
  font: 500 [2.8]/1 'Poppins', sans-serif; letter-spacing: .04em; }
.wk-logo-klein { height: [3.8]; width: auto; display: block; }
/* A · Ohne Agenda */
.wka-stern { position: absolute; right: [-22]; top: [-26]; width: [112]; }
.wka-stern--2 { right: [96]; top: [16]; width: [11]; }
.wka-stern--3 { right: [84]; top: [36]; width: [6]; }
.wka-agenda { position: absolute; left: [12]; top: [26]; list-style: none; padding: 0; display: grid; gap: [3.6]; }
.wka-agenda li { display: flex; align-items: baseline; gap: [5]; font: 700 [8.6]/1.05 'Lora', Georgia, serif; letter-spacing: -.01em; }
.wka-agenda i { font: 700 [3.4]/1 'Poppins', sans-serif; font-style: normal; color: #fff400; letter-spacing: .06em; width: [6]; }
/* B · Luft nach oben */
.wkb-baum { position: absolute; right: [50]; top: [9]; width: 0; height: [80]; }
.wkb-p, .wkb-stern { position: absolute; left: calc(var(--x) * [12.2]); transform: translateX(-50%); }
.wkb-p { width: [9.4]; top: calc(var(--r) * [13.2] + [1.5]); }
.wkb-stern { width: [11]; top: [-1]; }
.wkb-stamm { position: absolute; left: 0; top: [67.8]; width: [4.4]; height: [5.6]; transform: translateX(-50%); background: #1a1817; border-radius: 0 0 [0.6] [0.6]; }
.wkb-r-pfeil { position: absolute; right: [46]; bottom: [-34]; width: [64]; }
/* C · Abschalten */
.wkc-kugel { position: absolute; top: 0; left: calc(var(--x) * 100cqw / 210); display: flex; flex-direction: column; align-items: center;
  transform: translateX(-50%); }
.wkc-kugel i { display: block; width: [0.35]; height: calc(var(--l) * 100cqw / 210); background: rgba(255,255,255,.6); }
.wkc-kugel b { display: block; width: [3.2]; height: [1.8]; border-radius: [0.4] [0.4] 0 0; background: rgba(255,255,255,.85); }
.wkc-kugel svg { width: [13]; margin-top: [-0.3]; }
.wkc-boden { position: absolute; left: [12]; right: [12]; bottom: [24]; height: [0.5]; background: #1a1817; }
.wkc-gefallen { position: absolute; right: [44]; bottom: [24.5]; width: [12]; height: [12]; border-radius: 50%; background: #fff400; }
.wkc-r .wk-absender { bottom: [10]; }
""", 210)

INNEN_CSS = masse("""
.wki { position: relative; aspect-ratio: 420 / 99; container-type: inline-size; background: #fff; color: #1a1817; overflow: hidden;
  border-radius: 3px; font-family: 'Poppins', sans-serif; }
.wki p { margin: 0; }
.wki-flaeche { position: absolute; left: 0; top: 0; bottom: 0; width: 50%; }
.wki--gelb .wki-flaeche { background: #fff400; }
.wki--grau .wki-flaeche { background: #f3f1ee; }
.wki--schwarz .wki-flaeche { background: #1a1817; }
.wki--schwarz .wki-links { color: #fff; }
.wki--schwarz .wki-text { color: #d8d3cc; }
.wki--schwarz .wki-kicker { color: #fff400; }
.wki--gelb .wki-text { color: #1a1817; }
.wki-links { position: absolute; left: [14]; top: [14]; width: [172]; }
.wki-kicker { display: flex; align-items: center; gap: [2.6]; font: 700 [3]/1 'Poppins', sans-serif; letter-spacing: .16em; text-transform: uppercase; }
.wki-akzent { display: block; width: [5]; }
.wki-akzent svg { display: block; width: 100%; height: auto; }
.wki-punkt { display: block; width: [4]; height: [4]; border-radius: 50%; background: #fff400; box-shadow: 0 0 0 [0.4] #1a1817; }
.wki-h { margin-top: [7] !important; font: 700 [8.6]/1.12 'Lora', Georgia, serif; letter-spacing: -.02em; }
.wki-text { margin-top: [5] !important; max-width: [160]; font: 300 [3.7]/1.55 'Poppins', sans-serif; color: #3d3a37; }
.wki-rechts { position: absolute; left: [230]; right: [16]; top: [30]; display: grid; gap: [13]; }
.wk-linie { display: block; height: [0.3]; background: #d9d5ce; }
.wki-logo { position: absolute; right: [16]; bottom: [10]; height: [4.2]; width: auto; display: block; }
.wki-falz { position: absolute; left: 50%; top: 0; bottom: 0; border-left: 1px dashed #c9c4bd; }
.ga-export .wki-falz { display: none; }
""", 420)

CSS = KARTE_CSS + INNEN_CSS + """
.wk-innen-wrap { margin-top: 1.6rem; }
"""

if __name__ == "__main__":
    seite_schreiben(DATEI, "Weihnachtskarten", 'Weihnachts<span class="hl">karten</span>',
                    "DIN lang im Querformat, gefalzt an der kurzen Seite. Zugeklappt Spruch und Bild, aufgeklappt eine lange "
                    "Doppelseite: links ein kurzer Wunsch, rechts Platz für persönliche Worte. Drei Varianten aus der "
                    "empiria-Formensprache – je mit Vorderseite, Rückseite und Innenseite.",
                    ["Drei Varianten", "DIN lang quer · 210 × 99 mm", "Falz an der kurzen Seite", "aufgeklappt 420 × 99 mm"],
                    inhalt(), CSS)
    if "--ohne-png" not in sys.argv:
        png_export(DATEI, "weihnachtskarten")
