#!/usr/bin/env python3
"""One-Pager A3 – Entwurf 2 (Daniel, 10.10.2026): Aufbau wie die Volksfest-Seite.

Prinzip: wenige große Flächen übereinander (Weiß · Gelb · Weiß · Schwarz), viel Luft, große Lora-Überschriften,
pro Fläche genau eine Aussage. Nie Gelb auf Hellgrau.
  A3 hoch · A  Leistung mit Ansprechpartner  (Beispiel „Strategie in den Alltag überführen“)
  A3 hoch · B  Leistung ohne Person           (z. B. als Handout im Workshop)
  A3 hoch · C  Grundraster                    (leeres Raster zum Aufbereiten eigener Themen)
  A3 quer · A  Leistung, gelbe Titelspalte links
  A3 quer · B  Grundraster quer
PNG-Export (150 dpi) nach site/projekte/ga/onepager/.

Aufruf: python3 werkzeuge/ga/onepager.py [--ohne-png]
"""
import sys

from ga_basis import PERSONEN, abschnitt, download, figur, ico, logo, masse, png_export, raster, seite_schreiben, zeichen

DATEI = "ga-onepager.html"
PX = {"hoch": (1754, 2480), "quer": (2480, 1754)}
D = PERSONEN["daniel"]

LEISTUNG = dict(
    kicker="Strategiehandwerk",
    h1='Strategie in den Alltag <span class="hl">überführen.</span>',
    lead="Deine Strategie ist da – aber was bedeutet sie für Deinen Bereich? Wir machen sie greifbar und wirksam.",
    p_kicker="Das Problem",
    p_h2="Strategisches Denken wird vorausgesetzt. Beigebracht hat es Dir keiner.",
    p_label="Hart, weil das Fundament fehlt:",
    p_liste=["die klare Richtung", "die eigene Rolle", "das Handwerkszeug für den Alltag"],
    l_kicker="Die Lösung",
    l_h2="Rolle, Richtung, Handwerkszeug.",
    l_punkte=[("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"),
              ("compass", "Richtung", "Wie wollen wir wahrgenommen werden?"),
              ("wrench", "Handwerkszeug", "Wie kommen wir dorthin?")],
    e_kicker="Das Ergebnis",
    e_satz='Du führst Dein Team, statt es zu <span class="hl">vertrösten.</span>',
    nummern=False,
)
RASTER = dict(
    kicker="Thema",
    h1='Hier steht <span class="hl">das Thema.</span>',
    lead="Ein Satz, worum es geht und für wen es gedacht ist.",
    p_kicker="Ausgangslage",
    p_h2="Die Ausgangslage in einem klaren Satz.",
    p_label="Was heute fehlt:",
    p_liste=["Erster Punkt", "Zweiter Punkt", "Dritter Punkt"],
    l_kicker="Der Weg",
    l_h2="Drei Schritte zum Ergebnis.",
    l_punkte=[(None, "Schritt eins", "Kurz beschreiben, was passiert."),
              (None, "Schritt zwei", "Kurz beschreiben, was passiert."),
              (None, "Schritt drei", "Kurz beschreiben, was passiert.")],
    e_kicker="Das Ergebnis",
    e_satz='Das Ergebnis in einem <span class="hl">Satz.</span>',
    nummern=True,
)


def k(t):
    return f'<p class="op-k">{t}</p>'


def punkte(d):
    out = ""
    for i, (ic, t, p) in enumerate(d["l_punkte"]):
        kopf = f'<span class="op-nr">0{i + 1}</span>' if d["nummern"] else f'<span class="op-ico">{ico(ic, sw=1.5)}</span>'
        out += f'<div class="op-punkt">{kopf}<b>{t}</b><p>{p}</p></div>'
    return f'<div class="op-punkte">{out}</div>'


def problem_kasten(d):
    return (f'<div class="op-kasten"><p class="op-kasten__label">{d["p_label"]}</p>'
            f'<ul>{"".join(f"<li>{x}</li>" for x in d["p_liste"])}</ul></div>')


def fuss(art):
    """art: person | marke | raster"""
    if art == "person":
        return (f'<div class="op-person"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>{D["name"]}</b><span>{D["rolle2"]}</span></div></div>'
                f'<div class="op-kontakt"><span>{D["mail"]}</span><span>{D["tel"]}</span><span>www.empiria.de</span></div>')
    if art == "marke":
        return f'{logo(hell=True, cls="op-logo")}<div class="op-kontakt"><span>www.empiria.de</span></div>'
    return f'{logo(hell=True, cls="op-logo")}<div class="op-kontakt"><span>Workshop · Datum</span><span>www.empiria.de</span></div>'


def hoch(d, art, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["hoch"][0]}"' if png else ""
    pfeil = f'<span class="op-pfeil">{zeichen("forward", "#1a1817")}</span>'
    return (f'<div class="op op--hoch"{attr}>'
            f'<section class="op-kopf">{logo(cls="op-logo op-logo--kopf")}{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p>{pfeil}</section>'
            f'<section class="op-gelb"><div>{k(d["p_kicker"])}<h2>{d["p_h2"]}</h2></div>{problem_kasten(d)}</section>'
            f'<section class="op-weiss">{k(d["l_kicker"])}<h2>{d["l_h2"]}</h2>{punkte(d)}</section>'
            f'<section class="op-schwarz">{k(d["e_kicker"])}<p class="op-satz">{d["e_satz"]}</p><div class="op-fuss">{fuss(art)}</div></section>'
            f'</div>')


def quer(d, art, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["quer"][0]}"' if png else ""
    pfeil = f'<span class="op-pfeil">{zeichen("forward", "#1a1817")}</span>'
    return (f'<div class="op op--quer"{attr}>'
            f'<section class="op-spalte">{logo(cls="op-logo op-logo--kopf")}<div>{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p></div>{pfeil}</section>'
            f'<div class="op-rechts">'
            f'<section class="op-zwei"><div>{k(d["p_kicker"])}<h2>{d["p_h2"]}</h2></div>{problem_kasten(d)}</section>'
            f'<section class="op-weiss">{k(d["l_kicker"])}<h2>{d["l_h2"]}</h2>{punkte(d)}</section>'
            f'<section class="op-schwarz">{k(d["e_kicker"])}<p class="op-satz">{d["e_satz"]}</p><div class="op-fuss">{fuss(art)}</div></section>'
            f'</div></div>')


CSS_HOCH = masse("""
.op { position: relative; container-type: inline-size; background: #fff; color: #1a1817; overflow: hidden;
  box-shadow: 0 0 0 1px #e4e0db, 0 18px 40px rgba(26,24,23,.08); font-family: 'Poppins', sans-serif; }
.op--hoch { aspect-ratio: 297 / 420; display: grid; grid-template-rows: 36% 22% 22% 20%; }
.op section { position: relative; padding: [20] [24]; }
.op-logo { display: block; height: [7]; width: auto; }
.op-logo--kopf { position: absolute; top: [16]; left: [24]; }
.op-k { display: flex; align-items: center; gap: [3]; margin: 0 0 [5]; font: 700 [9pt]/1 'Poppins', sans-serif; letter-spacing: .16em; text-transform: uppercase; }
.op-k::before { content: ""; width: [8]; height: [0.6]; background: currentColor; }
.op h1 { margin: 0; font: 700 [56pt]/1.16 'Lora', Georgia, serif; letter-spacing: -.02em; }
.op h2 { margin: 0; font: 700 [26pt]/1.25 'Lora', Georgia, serif; letter-spacing: -.015em; }
.op .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }
.op-lead { margin: [7] 0 0; max-width: [160]; font: 300 [14pt]/1.55 'Poppins', sans-serif; color: #3d3a37; }
.op-kopf { display: flex; flex-direction: column; justify-content: flex-end; padding-bottom: [22] !important; }
.op-kopf > :not(.op-logo):not(.op-pfeil) { max-width: [190]; }
.op-pfeil { position: absolute; right: [24]; bottom: [22]; width: [52]; }
.op-pfeil svg { display: block; width: 100%; height: auto; }
.op-gelb { background: #fff400; display: grid; grid-template-columns: 1.1fr .9fr; gap: [14]; align-items: center; }
.op-kasten { background: #1a1817; color: #fff; border-radius: [5]; padding: [10] [11]; }
.op-kasten__label { margin: 0 0 [4]; font: 600 [11pt]/1.4 'Poppins', sans-serif; color: rgba(255,255,255,.7); }
.op-kasten ul { list-style: none; margin: 0; padding: 0; }
.op-kasten li { position: relative; padding: [2.2] 0 [2.2] [6]; font: 700 [14pt]/1.35 'Lora', serif; }
.op-kasten li::before { content: ""; position: absolute; left: 0; top: [5]; width: [2.4]; height: [2.4]; border-radius: 50%; background: #fff400; }
.op-weiss { display: flex; flex-direction: column; justify-content: center; }
.op-punkte { display: grid; grid-template-columns: repeat(3, 1fr); gap: [12]; margin-top: [10]; }
.op-punkt { border-top: [0.6] solid #1a1817; padding-top: [6]; }
.op-ico { display: block; width: [9]; height: [9]; margin-bottom: [4]; }
.op-ico svg { width: 100%; height: 100%; display: block; }
.op-nr { display: block; margin-bottom: [3]; font: 700 [22pt]/1 'Lora', serif; }
.op-punkt b { display: block; font: 700 [15pt]/1.25 'Lora', serif; }
.op-punkt p { margin: [2.5] 0 0; font: 300 [11pt]/1.5 'Poppins', sans-serif; color: #3d3a37; }
.op-schwarz { background: #1a1817; color: #fff; display: flex; flex-direction: column; justify-content: center; }
.op-satz { margin: 0; max-width: [230]; font: 700 [30pt]/1.25 'Lora', serif; letter-spacing: -.015em; }
.op-schwarz .hl { color: #1a1817; }
.op-fuss { display: flex; align-items: center; justify-content: space-between; gap: [10]; margin-top: [12]; padding-top: [7]; border-top: [0.3] solid rgba(255,255,255,.25); }
.op-person { display: flex; align-items: center; gap: [5]; }
.op-person img { width: [16]; height: [16]; border-radius: 50%; object-fit: cover; filter: grayscale(1); background: #3a3733; }
.op-person b { display: block; font: 700 [12pt]/1.2 'Lora', serif; }
.op-person span { display: block; margin-top: [1]; font: 400 [9pt]/1.3 'Poppins', sans-serif; color: rgba(255,255,255,.65); }
.op-kontakt { display: flex; gap: [7]; font: 400 [10pt]/1.3 'Poppins', sans-serif; color: rgba(255,255,255,.85); }
.op-schwarz .op-k { color: #fff400; }
""", 297)

CSS_QUER = masse("""
.op--quer { aspect-ratio: 420 / 297; display: grid; grid-template-columns: 38% 62%; }
.op--quer section { padding: [18] [20]; }
.op-spalte { background: #fff400; display: flex; flex-direction: column; justify-content: center; }
.op--quer .op-logo--kopf { top: [16]; left: [20]; }
.op--quer h1 { font-size: [44pt]; }
.op--quer .op-lead { font-size: [12.5pt]; max-width: none; }
.op--quer .op-pfeil { left: [20]; right: auto; bottom: [16]; width: [40]; }
.op-rechts { display: grid; grid-template-rows: 1fr 1fr auto; height: 100%; min-height: 0; }
.op--quer .op-rechts > section { min-height: 0; }
.op--quer section { padding: [14] [18]; }
.op--quer .op-kasten { padding: [8] [9]; }
.op--quer .op-kasten li { font-size: [12pt]; padding-top: [1.6]; padding-bottom: [1.6]; }
.op--quer .op-kasten__label { font-size: [10pt]; }
.op--quer .op-punkt p { font-size: [10pt]; }
.op--quer .op-punkt b { font-size: [13pt]; }
.op--quer .op-ico { width: [7]; height: [7]; margin-bottom: [3]; }
.op--quer .op-fuss { margin-top: [6]; padding-top: [5]; }
.op--quer .op-person img { width: [12]; height: [12]; }
.op-spalte .hl { background: #1a1817; color: #fff; }
.op--quer .op-kasten li::before { top: [3.4]; width: [2]; height: [2]; }
.op--quer .op-k { font-size: [8pt]; margin-bottom: [4]; }
.op--quer .op-kontakt { font-size: [8pt]; gap: [6]; white-space: nowrap; }
.op--quer .op-person b { font-size: [10pt]; }
.op--quer .op-person span { font-size: [7.5pt]; }
.op-zwei { display: grid; grid-template-columns: 1fr 1fr; gap: [12]; align-items: center; }
.op--quer h2 { font-size: [19pt]; }
.op--quer .op-punkte { margin-top: [7]; }
.op--quer .op-satz { font-size: [21pt]; }
.op--quer .op-fuss { margin-top: [8]; }
""", 420)

SEITE_CSS = """
.op-reihe { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.6rem; margin-top: 1.8rem; align-items: start; }
.op-reihe--quer { grid-template-columns: repeat(2, minmax(0, 1fr)); }
@media (max-width: 900px) { .op-reihe, .op-reihe--quer { grid-template-columns: 1fr; } }
"""


def inhalt(mit_png):
    def dl(n, t):
        return download(f"ga/onepager/{n}.png", t)
    h = [figur(hoch(LEISTUNG, "person", "a3-hoch-leistung-person" if mit_png else None), "A · Leistung mit Ansprechpartner", dl("a3-hoch-leistung-person", "PNG · 1754 × 2480 px")),
         figur(hoch(LEISTUNG, "marke", "a3-hoch-leistung" if mit_png else None), "B · Leistung ohne Person", dl("a3-hoch-leistung", "PNG · 1754 × 2480 px")),
         figur(hoch(RASTER, "raster", "a3-hoch-raster" if mit_png else None), "C · Grundraster für eigene Themen", dl("a3-hoch-raster", "PNG · 1754 × 2480 px"))]
    q = [figur(quer(LEISTUNG, "person", "a3-quer-leistung" if mit_png else None), "A · Leistung, gelbe Titelspalte", dl("a3-quer-leistung", "PNG · 2480 × 1754 px")),
         figur(quer(RASTER, "raster", "a3-quer-raster" if mit_png else None), "B · Grundraster quer", dl("a3-quer-raster", "PNG · 2480 × 1754 px"))]
    return (abschnitt("A3 hoch", "Vier Flächen übereinander wie auf der Volksfest-Seite: Thema auf Weiß, Problem auf Gelb mit schwarzem Kasten, "
                      "Lösung auf Weiß, Ergebnis auf Schwarz. Je Fläche genau eine Aussage. A mit Ansprechpartner, B ohne Person "
                      "(z. B. als Handout im Workshop), C als leeres Grundraster zum Aufbereiten eigener Themen.",
                      f'<div class="op-reihe">{"".join(h)}</div>')
            + abschnitt("A3 quer", "Gelbe Titelspalte links, rechts dieselben drei Flächen: Problem, Lösung, Ergebnis.",
                        f'<div class="op-reihe op-reihe--quer">{"".join(q)}</div>'))


def main():
    mit_png = "--ohne-png" not in sys.argv
    seite_schreiben(DATEI, "One-Pager", 'One-<span class="hl">Pager</span>',
                    "Ein Blatt, eine Leistung oder ein Thema – aufgebaut wie die Volksfest-Seite: große Flächen, viel Luft, je Fläche eine Aussage. "
                    "Mit Ansprechpartner, ohne Person oder als leeres Grundraster.",
                    ["Entwurf 2", "A3 hoch & quer", "mit / ohne Person", "Grundraster"],
                    inhalt(mit_png), CSS_HOCH + CSS_QUER + SEITE_CSS)
    if mit_png:
        png_export(DATEI, "onepager")


if __name__ == "__main__":
    main()
