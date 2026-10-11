#!/usr/bin/env python3
"""Corporate Design · Merch – die Marke zum Anfassen (Daniel, 11.10.2026).

Nicht als Werbegeschenk gedacht, sondern für uns: Kleidung für Workshops und Messen, Sticker für MacBook und Auto,
Werkzeug für den Workshop. Bausteine: die drei Zeichen der Homepage (Doppelpfeil = Strategie, Kreuz = Komplexe Themen,
Kreis = Innovation), das Logo „empiria_“ mit seinem Unterstrich und der Claim „Strategie, die wirkt.“
Regel: ein Zeichen je Stück – winzig und präzise oder riesig angeschnitten, nie mittelgroß. Nur Schwarz, Weiß, Gelb.

Aufruf: python3 werkzeuge/ga/merch.py   →   site/projekte/merch.html
"""
import re
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ga_export import FORM, SITE, seite  # noqa: E402

S, G, W, GR = "#1a1817", "#fff400", "#ffffff", "#f3f1ee"
VB = {"forward": (2.83, 31.08, 226.78, 170.29)}
LOGO_SVG = (SITE / "assets" / "empiria-logo.svg").read_text(encoding="utf-8")
LOGO_PFADE = re.sub(r'class="cls-\d"', 'fill="currentColor"', "".join(re.findall(r"<(?:path|rect)[^>]*/>", LOGO_SVG)))
LOGO_VERH = 89.29 / 340.16


def z(name, x, y, b, farbe, extra=""):
    """Markenform in ein SVG setzen: x/y = links oben, b = Breite."""
    vx, vy, vw, vh = VB.get(name, (2.83, 2.83, 226.78, 226.78))
    h = b * vh / vw
    return (f'<svg x="{x}" y="{y}" width="{b}" height="{h:.2f}" viewBox="{vx} {vy} {vw} {vh}" '
            f'style="color:{farbe};overflow:visible" {extra}>{FORM[name]}</svg>')


def logo(x, y, b, farbe):
    return (f'<svg x="{x}" y="{y}" width="{b}" height="{b * LOGO_VERH:.2f}" viewBox="0 0 340.16 89.29" '
            f'style="color:{farbe}">{LOGO_PFADE}</svg>')


def sticker(inhalt):
    """Plott-/Sticker-Look: weißer Rand um die Form, leichter Schatten."""
    return f'<g filter="url(#schatten)" style="paint-order:stroke;stroke:#fff;stroke-width:22;stroke-linejoin:round">{inhalt}</g>'


DEFS = ('<defs><filter id="schatten" x="-20%" y="-20%" width="140%" height="140%">'
        '<feDropShadow dx="0" dy="6" stdDeviation="7" flood-color="#1a1817" flood-opacity=".18"/></filter>'
        '<filter id="weich" x="-20%" y="-20%" width="140%" height="140%">'
        '<feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#1a1817" flood-opacity=".22"/></filter></defs>')


def bild(inhalt):
    return f'<svg viewBox="0 0 400 400" aria-hidden="true">{DEFS}{inhalt}</svg>'


# ---------- Kleidung (Silhouetten) ----------
def shirt(x, y, s, farbe, druck="", kragen=False):
    """T-Shirt/Polo, Silhouette 290 × 300 bei s=1, links oben x/y."""
    naht = "#00000022" if farbe != S else "#ffffff22"
    polo = (f'<path d="M118 22 L145 58 L172 22" fill="none" stroke="{naht}" stroke-width="3"/>'
            f'<path d="M108 14 L145 50 L182 14 L172 2 Q145 18 118 2 Z" fill="{farbe}" stroke="{naht}" stroke-width="2"/>'
            f'<line x1="145" y1="50" x2="145" y2="92" stroke="{naht}" stroke-width="3"/>'
            f'<circle cx="145" cy="66" r="3" fill="{naht}"/><circle cx="145" cy="82" r="3" fill="{naht}"/>') if kragen else \
        f'<path d="M110 8 Q145 40 180 8" fill="none" stroke="{naht}" stroke-width="4"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#weich)">'
            f'<path d="M110 6 Q145 30 180 6 L238 26 L290 80 L252 120 L228 98 L228 296 Q145 306 62 296 L62 98 L38 120 L0 80 L52 26 Z" fill="{farbe}"/>'
            f'{polo}<g>{druck}</g></g>')


def hoodie(x, y, s, farbe, druck="", hinten=False):
    """Hoodie, Silhouette 320 × 330 bei s=1."""
    linie = "#ffffff1f" if farbe == S else "#00000018"
    kapuze = (f'<path d="M115 40 Q160 -18 205 40 Q200 70 160 74 Q120 70 115 40 Z" fill="{farbe}"/>' if hinten else
              f'<path d="M112 44 Q160 -14 208 44 L198 58 Q160 34 122 58 Z" fill="{farbe}"/>'
              f'<path d="M126 52 Q160 30 194 52 Q186 86 160 90 Q134 86 126 52 Z" fill="#0d0c0b" opacity=".55"/>'
              f'<line x1="148" y1="88" x2="146" y2="140" stroke="{linie}" stroke-width="4" stroke-linecap="round"/>'
              f'<line x1="172" y1="88" x2="174" y2="140" stroke="{linie}" stroke-width="4" stroke-linecap="round"/>')
    tasche = "" if hinten else f'<path d="M108 228 L212 228 L230 290 L90 290 Z" fill="none" stroke="{linie}" stroke-width="3"/>'
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#weich)">'
            f'<path d="M116 46 L56 74 L18 250 L56 260 L84 150 L84 318 Q160 330 236 318 L236 150 L264 260 L302 250 L264 74 L204 46 Z" fill="{farbe}"/>'
            f'<path d="M84 306 L236 306" stroke="{linie}" stroke-width="3"/>'
            f'{kapuze}{tasche}<g>{druck}</g></g>')


def cap(x, y, s, farbe, druck=""):
    return (f'<g transform="translate({x} {y}) scale({s})" filter="url(#weich)">'
            f'<ellipse cx="150" cy="158" rx="140" ry="24" fill="{farbe}"/>'
            f'<path d="M30 150 Q30 30 150 26 Q270 30 270 150 Z" fill="{farbe}"/>'
            f'<path d="M150 26 L150 150" stroke="#ffffff18" stroke-width="3"/>'
            f'<circle cx="150" cy="28" r="7" fill="{farbe}" stroke="#ffffff22" stroke-width="2"/>'
            f'<path d="M30 150 Q150 170 270 150" fill="none" stroke="#ffffff22" stroke-width="3"/>'
            f'<g>{druck}</g></g>')


# ---------- Die Stücke ----------
def m_hoodie():
    vorn = z("forward", 196, 120, 30, G)                                   # klein auf der Brust links (vom Träger aus)
    hinten = z("forward", 82, 150, 156, G) + logo(125, 112, 70, W)         # groß über den ganzen Rücken
    return bild(f'<rect width="400" height="400" fill="{G}"/>'
                + hoodie(-6, 70, .6, S, vorn)
                + hoodie(196, 70, .6, S, f'<g clip-path="url(#saum2)">{hinten}</g>'
                         '<clipPath id="saum2"><path d="M84 60 L236 60 L236 306 L84 306 Z"/></clipPath>', hinten=True))


def m_shirts():
    out = f'<rect width="400" height="400" fill="{GR}"/>'
    for i, (n, f) in enumerate((("forward", S), ("kreuz", S), ("kreis", S))):
        b = 52 if n == "forward" else 46
        druck = z(n, 145 - b / 2, 120 if n == "forward" else 112, b, f)
        out += shirt(8 + i * 128, 120, .42, W, druck)
    return bild(out + f'<text x="200" y="330" text-anchor="middle" font-family="Poppins" font-size="13" font-weight="600" letter-spacing="2" fill="{S}">STRATEGIE · KOMPLEXE THEMEN · INNOVATION</text>')


def m_polo():
    druck = z("forward", 180, 92, 26, G) + logo(110, 260, 70, "#ffffff55")
    return bild(f'<rect width="400" height="400" fill="{GR}"/>' + shirt(55, 60, 1, S, druck, kragen=True))


def m_cap():
    return bild(f'<rect width="400" height="400" fill="{G}"/>' + cap(50, 110, 1, S, z("forward", 122, 70, 56, G)))


def m_macbook():
    deckel = (f'<g filter="url(#weich)"><rect x="40" y="70" width="320" height="220" rx="16" fill="#d7d8db"/>'
              f'<rect x="40" y="70" width="320" height="220" rx="16" fill="url(#alu)"/></g>'
              f'<linearGradient id="alu" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="#fff" stop-opacity=".45"/>'
              f'<stop offset=".6" stop-color="#fff" stop-opacity="0"/></linearGradient>'
              f'<rect x="60" y="290" width="280" height="10" rx="4" fill="#bfc1c5"/>')
    return bild(f'<rect width="400" height="400" fill="{S}"/>' + deckel
                + sticker(z("forward", 300, 92, 38, G)))


def m_sticker():
    s = (sticker(z("forward", 40, 60, 150, G)) + sticker(z("kreuz", 230, 50, 120, S))
         + sticker(z("kreis", 245, 215, 105, S)) + sticker(z("forward", 70, 260, 80, S))
         + f'<g filter="url(#schatten)"><rect x="40" y="200" width="160" height="44" rx="10" fill="#fff"/>{logo(56, 211, 128, S)}</g>'
         + f'<g filter="url(#schatten)"><rect x="168" y="300" width="118" height="54" rx="10" fill="#fff"/>'
           f'<rect x="178" y="310" width="98" height="34" rx="6" fill="{G}"/>'
           f'<text x="227" y="335" text-anchor="middle" font-family="Lora" font-weight="700" font-size="22" fill="{S}">wirkt.</text></g>')
    return bild(f'<rect width="400" height="400" fill="{GR}"/>' + s)


def m_auto():
    auto = (f'<g filter="url(#weich)"><path d="M40 250 Q40 205 90 196 L310 196 Q360 205 360 250 L360 318 Q360 330 346 330 L54 330 Q40 330 40 318 Z" fill="#e9e7e3"/>'
            f'<path d="M92 104 Q96 92 110 92 L290 92 Q304 92 308 104 L332 196 L68 196 Z" fill="{S}"/>'
            f'<rect x="52" y="214" width="62" height="22" rx="6" fill="#c5281f"/><rect x="286" y="214" width="62" height="22" rx="6" fill="#c5281f"/>'
            f'<rect x="150" y="262" width="100" height="26" rx="4" fill="#fff" stroke="#cfcac3"/>'
            f'<rect x="40" y="300" width="320" height="30" rx="8" fill="#d4d1cc"/></g>')
    plott = logo(108, 166, 82, W) + z("forward", 278, 156, 34, G)
    return bild(f'<rect width="400" height="400" fill="{G}"/>' + auto + plott)


def m_magnete():
    tafel = (f'<g filter="url(#weich)"><rect x="30" y="60" width="340" height="250" rx="10" fill="#fff"/>'
             f'<rect x="30" y="60" width="340" height="250" rx="10" fill="none" stroke="#cfcac3" stroke-width="6"/></g>'
             f'<rect x="70" y="100" width="92" height="64" rx="3" fill="#fff8a8"/><rect x="190" y="118" width="92" height="64" rx="3" fill="#fff8a8"/>'
             f'<rect x="110" y="210" width="92" height="64" rx="3" fill="#fff8a8"/>'
             f'<path d="M84 122h60M84 136h44M204 140h60M204 154h40M124 232h60M124 246h50" stroke="#1a181766" stroke-width="4" stroke-linecap="round"/>')
    mag = ""
    for cx, cy, n, bg, fg in ((158, 96, "forward", G, S), (278, 114, "kreuz", S, G), (198, 206, "kreis", S, W)):
        mag += (f'<g filter="url(#schatten)"><circle cx="{cx}" cy="{cy}" r="22" fill="{bg}"/></g>'
                + z(n, cx - (13 if n == "forward" else 11), cy - (10 if n == "forward" else 11), 26 if n == "forward" else 22, fg))
    return bild(f'<rect width="400" height="400" fill="{GR}"/>' + tafel + mag)


def m_tasse():
    t = (f'<g filter="url(#weich)"><path d="M285 160 Q340 160 340 205 Q340 250 285 250" fill="none" stroke="{S}" stroke-width="22"/>'
         f'<path d="M90 110 L290 110 L280 318 Q278 330 266 330 L114 330 Q102 330 100 318 Z" fill="{S}"/>'
         f'<ellipse cx="190" cy="110" rx="100" ry="14" fill="#2a2725"/></g>'
         f'<text x="128" y="206" font-family="Lora" font-weight="700" font-size="28" fill="#fff">Strategie,</text>'
         f'<text x="128" y="250" font-family="Lora" font-weight="700" font-size="28" fill="#fff">die</text>'
         f'<rect x="176" y="224" width="94" height="36" rx="5" fill="{G}"/>'
         f'<text x="223" y="250" text-anchor="middle" font-family="Lora" font-weight="700" font-size="28" fill="{S}">wirkt.</text>')
    return bild(f'<rect width="400" height="400" fill="{G}"/>' + t)


def m_notizbuch():
    n = (f'<g filter="url(#weich)"><rect x="95" y="50" width="210" height="300" rx="10" fill="{S}"/></g>'
         f'<rect x="95" y="50" width="12" height="300" rx="4" fill="#0f0e0d"/>'
         + z("forward", 170, 170, 70, "#2b2826")
         + f'<rect x="268" y="50" width="14" height="300" fill="{G}"/>')
    return bild(f'<rect width="400" height="400" fill="{GR}"/>' + n)


def m_pin():
    p = (f'<g filter="url(#weich)" style="paint-order:stroke;stroke:#3a3632;stroke-width:14;stroke-linejoin:round">{z("forward", 110, 132, 180, G)}</g>')
    return bild(f'<rect width="400" height="400" fill="{S}"/>' + p)


def m_glas():
    reihe = "".join(z("forward", 22 + i * 64, 168, 44, "#ffffff") for i in range(6))
    g = (f'<rect width="400" height="400" fill="#c9d3d6"/>'
         f'<rect x="0" y="0" width="400" height="400" fill="url(#raum)"/>'
         f'<linearGradient id="raum" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#e8eef0"/><stop offset="1" stop-color="#aebbc0"/></linearGradient>'
         f'<rect x="0" y="140" width="400" height="100" fill="#ffffff" opacity=".55"/>'
         f'<g opacity=".95">{reihe}</g>'
         f'<rect x="196" y="0" width="8" height="400" fill="#8c999e"/>'
         + logo(250, 330, 110, S))
    return bild(g)


STUECKE = [
    ("Kleidung", "Hoodie", "Workshops · Messe · Team",
     "Vorne winzig der gelbe Doppelpfeil auf der Brust. Hinten groß über den ganzen Rücken – darüber klein das Logo.", m_hoodie),
    ("Kleidung", "Drei T-Shirts", "Ein Zeichen je Leistung",
     "Weiße Shirts mit Pfeil, Kreuz oder Kreis. Im Workshop trägt jeder das Zeichen seines Themas.", m_shirts),
    ("Kleidung", "Polo", "Kundentermine",
     "Schwarz, der Doppelpfeil klein in Gelb gestickt. Ruhig genug für den Vorstandstermin.", m_polo),
    ("Kleidung", "Cap", "Volksfest · Sommer",
     "Schwarz mit gelbem Doppelpfeil vorne, gestickt. Sonst nichts.", m_cap),
    ("Alltag", "MacBook-Deckel", "Geplotteter Aufkleber",
     "Ja, das ergibt Sinn: ein kleiner gelber Doppelpfeil, oben rechts in der Ecke, aus Folie geplottet. Präzise statt bunt beklebt.", m_macbook),
    ("Alltag", "Sticker-Set", "Laptop · Flasche · Notizbuch",
     "Die drei Zeichen, das Logo und „wirkt.“ als Konturschnitt mit weißem Rand – zum Weitergeben im Workshop.", m_sticker),
    ("Alltag", "Auto", "Heckscheibe",
     "Weiß geplottet unten links das Logo, rechts der gelbe Doppelpfeil. Klein, nicht vollflächig – wirkt wie ein Markenauto.", m_auto),
    ("Workshop", "Magnete", "Whiteboard · Moderationswand",
     "Pfeil, Kreuz und Kreis als runde Magnete: Damit markieren wir live, was Strategie, was komplex und was neu ist.", m_magnete),
    ("Workshop", "Tasse", "Besprechung · Büro",
     "Schwarz, der Claim in Weiß, „wirkt.“ im gelben Kasten – wie auf der Homepage.", m_tasse),
    ("Workshop", "Notizbuch", "Für jeden Teilnehmer",
     "Schwarzer Einband, der Doppelpfeil schwarz auf schwarz geprägt, ein gelbes Gummiband.", m_notizbuch),
    ("Details", "Anstecknadel", "Revers · Rucksack",
     "Emaille, gelb mit schwarzer Kante: der Doppelpfeil als kleines Erkennungszeichen.", m_pin),
    ("Details", "Glastür", "Büro · Besprechungsraum",
     "Ein Band aus Doppelpfeilen als Milchglasfolie auf Augenhöhe – Sichtschutz und Marke zugleich.", m_glas),
]

CSS = """
.mc { padding: 5rem 0 6rem; }
.mc-kicker { display: inline-flex; align-items: center; gap: .6rem; margin: 0 0 1.2rem; font: 700 .78rem/1 'Poppins', sans-serif; letter-spacing: .15em; text-transform: uppercase; color: #1a1817; }
.mc-kicker::before { content: ""; width: 1.5rem; height: 2px; background: currentColor; }
.mc h1 { margin: 0; font: 700 clamp(2.6rem, 5.4vw, 4.4rem)/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; color: #1a1817; }
.mc h2 { margin: 0; font: 700 clamp(1.9rem, 3.4vw, 2.7rem)/1.25 'Lora', Georgia, serif; letter-spacing: -.02em; color: #1a1817; }
.mc .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }
.mc-lead { margin: 1.4rem 0 0; max-width: 42rem; font: 300 1.15rem/1.65 'Poppins', sans-serif; color: #3d3a37; }
.mc-abschnitt { margin-top: 5.5rem; }
.mc-bausteine { display: grid; grid-template-columns: repeat(5, minmax(0, 1fr)); gap: 1rem; margin-top: 2.2rem; }
.mc-baustein { display: flex; flex-direction: column; gap: 1rem; padding: 1.6rem 1.4rem; border-radius: 18px; background: #f3f1ee; }
.mc-baustein__z { height: 4.2rem; display: flex; align-items: center; }
.mc-baustein__z svg { height: 100%; width: auto; }
.mc-baustein b { font: 700 1.15rem/1.25 'Lora', Georgia, serif; color: #1a1817; }
.mc-baustein small { font: 400 .9rem/1.5 'Poppins', sans-serif; color: #3d3a37; }
.mc-regeln { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; margin-top: 1.2rem; }
.mc-regel { padding: 1.4rem 1.4rem; border-radius: 18px; background: #1a1817; color: #fff; }
.mc-regel b { display: block; font: 700 1.2rem/1.3 'Lora', Georgia, serif; color: #fff400; }
.mc-regel p { margin: .5rem 0 0; font: 400 .95rem/1.55 'Poppins', sans-serif; color: #d8d3cc; }
.mc-gruppe { margin: 3.4rem 0 0; font: 700 .78rem/1 'Poppins', sans-serif; letter-spacing: .15em; text-transform: uppercase; color: #6b6762; }
.mc-raster { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.4rem; margin-top: 2.4rem; }
.mc-karte { border-radius: 18px; background: #fff; border: 1px solid #e4e0db; overflow: hidden; }
.mc-karte__bild svg { display: block; width: 100%; height: auto; aspect-ratio: 1; }
.mc-karte__text { padding: 1.2rem 1.3rem 1.4rem; }
.mc-karte__text small { display: block; font: 700 .74rem/1 'Poppins', sans-serif; letter-spacing: .12em; text-transform: uppercase; color: #6b6762; }
.mc-karte__text b { display: block; margin-top: .55rem; font: 700 1.45rem/1.25 'Lora', Georgia, serif; color: #1a1817; }
.mc-karte__text p { margin: .5rem 0 0; font: 400 .95rem/1.55 'Poppins', sans-serif; color: #3d3a37; }
@media (max-width: 1000px) { .mc-bausteine { grid-template-columns: repeat(3, minmax(0, 1fr)); } .mc-raster { grid-template-columns: repeat(2, minmax(0, 1fr)); } }
@media (max-width: 640px) { .mc-bausteine, .mc-raster, .mc-regeln { grid-template-columns: minmax(0, 1fr); } }
"""


def baustein_svg(name):
    vx, vy, vw, vh = VB.get(name, (2.83, 2.83, 226.78, 226.78))
    return f'<svg viewBox="{vx} {vy} {vw} {vh}" style="color:#1a1817" aria-hidden="true">{FORM[name]}</svg>'


def main_html():
    bausteine = [
        (baustein_svg("forward"), "Doppelpfeil", "Strategie. Das Hauptzeichen – vorwärts."),
        (baustein_svg("kreuz"), "Kreuz", "Komplexe Themen."),
        (baustein_svg("kreis"), "Kreis", "Innovation."),
        ('<svg viewBox="0 0 340.16 89.29" style="color:#1a1817;height:2.2rem" aria-hidden="true">' + LOGO_PFADE + '</svg>', "Logo", "„empiria_“ – mit dem Unterstrich, der wie ein Cursor wartet."),
        ('<span class="hl" style="font:700 1.9rem/1 Lora,Georgia,serif">wirkt.</span>', "Claim", "Das letzte Wort im gelben Kasten."),
    ]
    b_html = "".join(f'<div class="mc-baustein"><span class="mc-baustein__z">{s}</span><b>{t}</b><small>{x}</small></div>' for s, t, x in bausteine)
    regeln = [("Ein Zeichen je Stück", "Pfeil oder Kreuz oder Kreis – nie alles auf einmal. Das Logo begleitet höchstens klein."),
              ("Winzig oder riesig", "Klein und präzise auf der Brust oder groß und angeschnitten auf dem Rücken. Mittelgroß wirkt wie Werbung."),
              ("Schwarz, Weiß, Gelb", "Keine weiteren Farben. Gelb steht auf Schwarz oder als Fläche, nie als dünner Rand auf Weiß.")]
    r_html = "".join(f'<div class="mc-regel"><b>{t}</b><p>{x}</p></div>' for t, x in regeln)
    karten = "".join(f'<article class="mc-karte"><div class="mc-karte__bild">{fn()}</div><div class="mc-karte__text">'
                     f'<small>{g} · {wo}</small><b>{titel}</b><p>{text}</p></div></article>'
                     for g, titel, wo, text, fn in STUECKE)
    gruppen = f'<div class="mc-raster">{karten}</div>'
    return f'''<main>
<section class="mc"><div class="container">
  <p class="mc-kicker">Corporate Design · Merch</p>
  <h1>Die Marke zum <span class="hl">Anfassen.</span></h1>
  <p class="mc-lead">Nicht als Werbegeschenk, sondern für uns: Kleidung für Workshops und Messen, Aufkleber für MacBook und Auto, Werkzeug für die Moderationswand. Gebaut aus den Zeichen, die wir schon haben.</p>
  <div class="mc-abschnitt"><p class="mc-kicker">Bausteine</p><h2>Fünf Zeichen. Mehr braucht es nicht.</h2><div class="mc-bausteine">{b_html}</div></div>
  <div class="mc-abschnitt"><p class="mc-kicker">Regeln</p><h2>Damit es nach Marke aussieht.</h2><div class="mc-regeln">{r_html}</div></div>
  <div class="mc-abschnitt"><p class="mc-kicker">Die Stücke</p><h2>Zwölf Ideen für <span class="hl">uns.</span></h2>{gruppen}</div>
</div></section>
<style>{CSS}</style>
</main>'''


if __name__ == "__main__":
    seite("merch.html", "Merch", main_html())
