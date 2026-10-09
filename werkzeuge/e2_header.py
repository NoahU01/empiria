#!/usr/bin/env python3
"""Entwicklungsseite „Header“ (Daniel, 10.10.2026): zehn Stil-Varianten für das Kopfbild von „Sprint Landingpage“.
Wie Grafikstile in Illustrator – bewusst sehr unterschiedlich in Stil, Detailgrad und Anzahl der Elemente.
Nur Entwicklung (Branch Daniel), nie auf main.

    python3 werkzeuge/e2_header.py      # baut site/projekte/header.html (nach e2_bauen.py)
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
QUELLE = SITE / "projekte" / "empiria-2" / "sprint-landingpage.html"
ZIEL = SITE / "projekte" / "header.html"

K, M, Y, V, C, W = "#1a1817", "#C51F5D", "#fff400", "#8613A1", "#0B9FBD", "#ffffff"
G, G2, G3 = "#f1efeb", "#e3dfd8", "#b9b3ab"
M2, M3, M4 = "#e27fa3", "#f5d3df", "#7a1339"
MT, ON = "#C51F5E", "#FEFEFE"   # Akzent als Linie/Schrift · Weiß auf Akzentfläche (werden je Farbwelt ersetzt)
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"


def svg(inhalt, label, defs=""):
    return (f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" aria-label="{label}" font-family="{SANS}">'
            f'<defs>{defs}</defs>{inhalt}</svg>')


def r(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def t(x, y, txt, size=12, fill=K, weight=700, anchor="start", fam=SANS, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="{fam}" {extra}>{txt}</text>'


def _platte(tx, ty, w, h, d, oben, links, rechts, inhalt=""):
    A = (tx, ty); B = (tx + .866 * w, ty + .5 * w); C = (tx + .866 * (w - h), ty + .5 * (w + h)); D = (tx - .866 * h, ty + .5 * h)
    p = lambda *pts: " ".join(f"{x:.1f},{y:.1f}" for x, y in pts)
    s = lambda q: (q[0], q[1] + d)
    return (f'<polygon points="{p(D, C, s(C), s(D))}" fill="{links}"/><polygon points="{p(C, B, s(B), s(C))}" fill="{rechts}"/>'
            f'<polygon points="{p(A, B, C, D)}" fill="{oben}"/>'
            f'<g transform="matrix(.866 .5 -.866 .5 {tx} {ty})">{inhalt}</g>')


def v2():
    """Isometrisch: die Abschnitte der Seite als Platten, die zusammengesetzt werden."""
    pl = [
        (330, W, G2, G3, r(18, 18, 70, 70, M3, 8) + r(100, 18, 70, 70, M3, 8)),
        (270, W, G2, G3, r(18, 18, 152, 14, K, 7) + r(18, 44, 110, 10, G3, 5) + r(18, 64, 130, 10, G3, 5)),
        (210, M, M4, M4, r(18, 20, 120, 16, ON, 8) + r(18, 48, 80, 10, M3, 5) + r(18, 80, 60, 22, ON, 11)),
    ]
    teile = "".join(_platte(170, y - 150, 190, 118, 14, o, l, re_, inh) for y, o, l, re_, inh in pl)
    schwebend = _platte(170, 6, 190, 118, 14, W, G2, G3, r(18, 18, 30, 10, K, 5) + r(150, 18, 22, 10, K, 5) + r(66, 18, 70, 10, G3, 5))
    return svg(f'''
<ellipse cx="210" cy="372" rx="170" ry="22" fill="{G}"/>
{teile}
{schwebend}
<circle cx="390" cy="66" r="34" fill="{M3}"/><path d="M390 46v20l12 8" fill="none" stroke="{K}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
{t(390, 120, "48h", 18, K, 700, "middle", SERIF)}
''', "Isometrisch: Abschnitte der Landingpage werden zusammengesetzt")


# ---------------------------------------------------------------- 3 · Bauplan
def v3():
    """Bauplan: Wireframe mit Beschriftung und Maßlinie – viel Information, feine Linie, Magenta als Akzent."""
    ab = [(52, 48, "HEADER"), (104, 58, "PROBLEM"), (166, 46, "LÖSUNG"), (216, 40, "ABLAUF"), (260, 50, "KONTAKT")]
    wf = "".join(f'<rect x="150" y="{y}" width="140" height="{h}" fill="{W}" stroke="{K}" stroke-width="1.6"/>' for y, h, _ in ab)
    wf += (r(162, 60, 60, 7, K, 3) + r(162, 74, 90, 4, G3, 2) + f'<rect x="162" y="84" width="34" height="9" rx="4.5" fill="{M}"/>'
           + f'<circle cx="170" cy="122" r="7" fill="none" stroke="{K}" stroke-width="1.6"/>' + r(184, 116, 90, 4, K, 2) + r(184, 126, 70, 4, G3, 2) + r(162, 140, 112, 4, G3, 2)
           + "".join(r(162 + i * 40, 174, 32, 30, G, 4, f'stroke="{K}" stroke-width="1.2"') for i in range(3))
           + "".join(f'<circle cx="{170 + i * 32}" cy="236" r="6" fill="{W}" stroke="{K}" stroke-width="1.4"/>' for i in range(4)) + '<path d="M176 236h20M208 236h20M240 236h20" stroke="#1a1817" stroke-width="1.2"/>'
           + r(162, 272, 112, 8, G, 2, f'stroke="{K}" stroke-width="1"') + r(162, 286, 112, 8, G, 2, f'stroke="{K}" stroke-width="1"') + f'<rect x="162" y="298" width="44" height="9" rx="4.5" fill="{M}"/>')
    an = ""
    for i, (y, h, name) in enumerate(ab):
        links = i % 2 == 1
        ym = y + h / 2
        if links:
            an += f'<path d="M150 {ym}H96" stroke="{K}" stroke-width="1"/><circle cx="150" cy="{ym}" r="2.5" fill="{K}"/>' + t(92, ym + 4, name, 10, K, 700, "end")
        else:
            an += f'<path d="M290 {ym}H340" stroke="{K}" stroke-width="1"/><circle cx="290" cy="{ym}" r="2.5" fill="{K}"/>' + t(344, ym + 4, name, 10, K, 700)
    return svg(f'''
{wf}{an}
<path d="M118 48v262" stroke="{MT}" stroke-width="1.6"/><path d="M112 48h12M112 310h12" stroke="{MT}" stroke-width="1.6"/>
<g transform="rotate(-90 106 180)">{t(106, 184, "48 STUNDEN", 10, MT, 700, "middle")}</g>
<g transform="rotate(-8 360 336)">{r(318, 316, 88, 40, "none", 6, f'stroke="{MT}" stroke-width="2.5"')}{t(362, 342, "FREIGABE", 11, MT, 700, "middle")}</g>
''', "Bauplan der Landingpage mit Abschnitten")


# ---------------------------------------------------------------- 4 · Duoton
def v4():
    """Duoton Magenta mit Rasterpunkten: Desktop und Handy, nur Magenta-Töne."""
    defs = f'<pattern id="hv4p" width="8" height="8" patternUnits="userSpaceOnUse"><circle cx="4" cy="4" r="2" fill="{M}"/></pattern>'
    return svg(f'''
{r(52, 92, 270, 196, W, 14, f'stroke="{M4}" stroke-width="3"')}
<path d="M52 122h270" stroke="{M4}" stroke-width="3"/><circle cx="72" cy="107" r="5" fill="{M2}"/><circle cx="88" cy="107" r="5" fill="{M2}"/>
{r(72, 140, 120, 14, M4, 7)}{r(72, 164, 90, 9, M2, 4.5)}{r(72, 192, 72, 26, M, 13)}
{r(206, 138, 100, 130, M3, 10)}{r(206, 138, 100, 130, "url(#hv4p)", 10, 'opacity=".55"')}
{r(72, 236, 120, 9, M3, 4.5)}{r(72, 252, 96, 9, M3, 4.5)}
{r(286, 170, 100, 186, W, 18, f'stroke="{M4}" stroke-width="3"')}
{r(298, 192, 76, 60, M, 8)}{r(298, 262, 60, 8, M4, 4)}{r(298, 276, 44, 8, M2, 4)}{r(298, 300, 48, 20, M, 10)}
{r(316, 342, 40, 5, M2, 2.5)}
{r(36, 300, 120, 40, M4, 20)}<circle cx="60" cy="320" r="6" fill="{M2}"/>{t(74, 325, "LIVE · 48h", 13, W)}
''', "Duoton: Landingpage auf Desktop und Handy", defs)


# ---------------------------------------------------------------- 5 · Prozess
def v5():
    """Infografik: die drei Etappen des Sprints auf einer Zeitachse – inhaltlich am dichtesten."""
    def knoten(x, nr, farbe):
        return f'<circle cx="{x}" cy="250" r="16" fill="{farbe}" stroke="{K}" stroke-width="3"/>' + t(x, 255, nr, 13, {W: K, M: ON, K: W}[farbe], 700, "middle", SERIF)
    return svg(f'''
<path d="M40 250H404" stroke="{K}" stroke-width="3"/>
<path d="M40 250H404" stroke="{M}" stroke-width="9" stroke-linecap="round" stroke-dasharray="0 0" opacity=".0"/>
<rect x="150" y="244" width="200" height="12" rx="6" fill="{M}"/>
{knoten(70, "1", W)}{knoten(220, "2", M)}{knoten(374, "3", K)}
{r(26, 120, 92, 66, W, 8, f'stroke="{K}" stroke-width="3"')}<circle cx="72" cy="146" r="11" fill="{G2}" stroke="{K}" stroke-width="2.5"/><path d="M56 176c3-10 9-14 16-14s13 4 16 14" fill="{G2}" stroke="{K}" stroke-width="2.5"/>
<path d="M14 194h116" stroke="{K}" stroke-width="3" stroke-linecap="round"/>
{t(72, 292, "VORBEREITUNG", 10.5, K, 700, "middle")}{t(72, 310, "2–3 Std. · online", 10.5, "#6f6a64", 500, "middle")}
{r(156, 96, 128, 98, W, 10, f'stroke="{K}" stroke-width="3"')}{r(168, 110, 104, 26, M, 5)}{r(168, 146, 70, 7, K, 3.5)}
<rect x="168" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/><rect x="224" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="186" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/><circle cx="220" cy="214" r="9" fill="{M}" stroke="{K}" stroke-width="2.5"/><circle cx="254" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/>
{t(220, 292, "SPRINT-WORKSHOP", 10.5, K, 700, "middle")}{t(220, 310, "2 Tage · Präsenz", 10.5, "#6f6a64", 500, "middle")}
{r(346, 100, 58, 100, W, 10, f'stroke="{K}" stroke-width="3"')}{r(354, 112, 42, 30, M, 4)}{r(354, 150, 34, 5, K, 2.5)}{r(354, 160, 26, 5, G3, 2.5)}{r(354, 174, 30, 12, K, 6)}
<circle cx="404" cy="96" r="14" fill="{K}" stroke="{K}" stroke-width="2.5"/><path d="M397 96l5 5 9-10" fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{t(374, 292, "GO-LIVE", 10.5, K, 700, "middle")}{t(374, 310, "Feinschliff & live", 10.5, "#6f6a64", 500, "middle")}
<path d="M150 336v10h200v-10" fill="none" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>
{t(250, 372, "48 Stunden", 22, K, 700, "middle", SERIF)}
''', "Ablauf: Vorbereitung, Sprint-Workshop, Go-live")


# ---------------------------------------------------------------- 7 · Typografisch
def v7():
    """Typografisch: die Zahl ist das Bild. Sehr wenige Elemente."""
    return svg(f'''
{t(16, 300, "48", 250, K, 700, "start", SERIF, 'letter-spacing="-12"')}
{t(290, 300, "h", 110, MT, 700, "start", SERIF)}
<g transform="rotate(6 368 104)">{r(322, 24, 92, 160, W, 14, f'stroke="{K}" stroke-width="5"')}{r(334, 42, 68, 46, M, 7)}{r(334, 98, 56, 7, K, 3.5)}{r(334, 112, 40, 7, G3, 3.5)}{r(334, 134, 44, 18, K, 9)}</g>
<path d="M20 340h400" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
{t(20, 372, "VON NULL AUF LIVE", 13, K, 700, "start", SANS, 'letter-spacing="3"')}
''', "48 Stunden – typografisch")


# ================================================================ Runde 2 (Daniel, 10.10.2026): neue Stile
MUL = 'style="mix-blend-mode:multiply"'


# ---------------------------------------------------------------- Riso-Druck
def v11():
    """Riso-Druck: zwei Druckfarben (Grau, Akzent), leicht versetzt übereinander gedruckt – grafisch, mit Charakter."""
    defs = f'<pattern id="hv11p" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><circle cx="3.5" cy="3.5" r="1.6" fill="{M}"/></pattern>'
    gelb = (r(56, 70, 250, 290, "#d9d4cc", 14) + f'<circle cx="330" cy="292" r="74" fill="#d9d4cc"/>')
    mag = (f'<g transform="translate(9 -7)" {MUL}>'
           + r(56, 70, 250, 290, "none", 14, f'stroke="{M}" stroke-width="5"') + f'<path d="M56 112h250" stroke="{M}" stroke-width="5"/>'
           + f'<circle cx="80" cy="91" r="6" fill="{M}"/><circle cx="100" cy="91" r="6" fill="{M}"/>'
           + r(80, 134, 202, 70, M, 8) + r(80, 222, 150, 10, M, 5) + r(80, 242, 110, 10, M, 5)
           + r(80, 272, 92, 62, "url(#hv11p)", 8) + r(190, 272, 92, 62, "url(#hv11p)", 8)
           + f'<circle cx="330" cy="292" r="74" fill="none" stroke="{M}" stroke-width="5"/><path d="M330 292V238M330 292l30 18" stroke="{M}" stroke-width="7" stroke-linecap="round"/>'
           + f'<path d="M330 210v-16M314 192h32" stroke="{M}" stroke-width="6" stroke-linecap="round"/></g>')
    return svg(f'''<g {MUL}>{gelb}</g>{mag}
{t(118, 176, "LIVE", 30, ON, 700, "start", SANS, 'letter-spacing="4"')}
''', "Riso-Druck: Landingpage und Stoppuhr in zwei Druckfarben", defs)


# ---------------------------------------------------------------- Radial
def v12():
    """Uhr-Infografik: die 48 Stunden als Ring, Tag 1 und Tag 2 mit ihren Inhalten, in der Mitte die Seite."""
    import math
    cx, cy, R = 220, 196, 112
    def bogen(a0, a1, rad):
        p0 = (cx + rad * math.sin(math.radians(a0)), cy - rad * math.cos(math.radians(a0)))
        p1 = (cx + rad * math.sin(math.radians(a1)), cy - rad * math.cos(math.radians(a1)))
        gross = 1 if a1 - a0 > 180 else 0
        return f'M{p0[0]:.1f} {p0[1]:.1f}A{rad} {rad} 0 {gross} 1 {p1[0]:.1f} {p1[1]:.1f}'
    striche = ""
    for h in range(0, 48, 3):
        a = h / 48 * 360; lang = 16 if h % 12 == 0 else 8
        x0, y0 = cx + (R + 18) * math.sin(math.radians(a)), cy - (R + 18) * math.cos(math.radians(a))
        x1, y1 = cx + (R + 18 + lang) * math.sin(math.radians(a)), cy - (R + 18 + lang) * math.cos(math.radians(a))
        striche += f'<path d="M{x0:.1f} {y0:.1f}L{x1:.1f} {y1:.1f}" stroke="{K}" stroke-width="{3 if lang == 16 else 2}" stroke-linecap="round"/>'
    return svg(f'''
<path d="{bogen(2, 178, R)}" fill="none" stroke="{M}" stroke-width="26" stroke-linecap="round"/>
<path d="{bogen(182, 356, R)}" fill="none" stroke="#d9d4cc" stroke-width="26" stroke-linecap="round"/>
{striche}
{t(cx, 38, "0 h", 11, K, 700, "middle")}{t(cx, 368, "24 h", 11, K, 700, "middle")}
{t(372, 150, "TAG 1", 11, MT, 700)}{t(372, 166, "Sparring &amp;", 10, K, 500)}{t(372, 180, "Rohversion", 10, K, 500)}
{t(68, 214, "TAG 2", 11, K, 700, "end")}{t(68, 230, "Feinschliff", 10, K, 500, "end")}{t(68, 244, "&amp; Go-live", 10, K, 500, "end")}
{r(184, 124, 72, 140, W, 14, f'stroke="{K}" stroke-width="4"')}{r(194, 140, 52, 32, M, 6)}{r(194, 182, 42, 6, K, 3)}{r(194, 194, 30, 6, G3, 3)}{r(194, 234, 36, 14, K, 7)}
<circle cx="{cx - 8}" cy="{cy - R}" r="13" fill="{K}"/><path d="M{cx-13} {cy-R}l4 4 7-8" fill="none" stroke="{W}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
''', "48 Stunden als Ring: Tag 1 und Tag 2")


# ---------------------------------------------------------------- Piktogramm-Raster
PIKTO = {
    "ZIELGRUPPE": '<circle cx="0" cy="0" r="20" fill="none" stroke="{c}" stroke-width="4"/><circle cx="0" cy="0" r="10" fill="none" stroke="{c}" stroke-width="4"/><circle r="3" fill="{c}"/>',
    "PROBLEM": '<path d="M0-21L22 18H-22z" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round"/><path d="M0-6v10" stroke="{c}" stroke-width="4" stroke-linecap="round"/><circle cy="11" r="2.6" fill="{c}"/>',
    "LÖSUNG": '<path d="M-14 0l9 9 19-20" fill="none" stroke="{c}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/><circle r="22" fill="none" stroke="{c}" stroke-width="4"/>',
    "TEXT": '<path d="M-20-12h40M-20 0h40M-20 12h26" stroke="{c}" stroke-width="4" stroke-linecap="round"/>',
    "DESIGN": '<rect x="-21" y="-18" width="42" height="36" rx="4" fill="none" stroke="{c}" stroke-width="4"/><path d="M-21-6h42M-6-6v24" stroke="{c}" stroke-width="4"/>',
    "MOBILE": '<rect x="-13" y="-22" width="26" height="44" rx="6" fill="none" stroke="{c}" stroke-width="4"/><path d="M-5 15h10" stroke="{c}" stroke-width="4" stroke-linecap="round"/>',
    "FEEDBACK": '<path d="M-20-16h40v24H-2l-12 10V8h-6z" fill="none" stroke="{c}" stroke-width="4" stroke-linejoin="round"/>',
    "GO-LIVE": '<path d="M-6 20V-20" stroke="{c}" stroke-width="4" stroke-linecap="round"/><path d="M-6-20l24 8-24 9" fill="{c}"/>',
}


def v13():
    """Piktogramm-System: neun Kacheln, jede ein Baustein des Sprints – modular, sachlich, gut übertragbar."""
    namen = ["ZIELGRUPPE", "PROBLEM", "LÖSUNG", "TEXT", None, "DESIGN", "MOBILE", "FEEDBACK", "GO-LIVE"]
    k = ""
    for i, n in enumerate(namen):
        x, y = 34 + (i % 3) * 128, 18 + (i // 3) * 128
        if n is None:
            k += r(x, y, 116, 116, M, 18) + t(x + 58, y + 68, "48h", 34, ON, 700, "middle", SERIF) + t(x + 58, y + 92, "SPRINT", 9, ON, 700, "middle", SANS, 'letter-spacing="2"')
        else:
            k += r(x, y, 116, 116, G, 18) + f'<g transform="translate({x+58} {y+50})">{PIKTO[n].format(c=K)}</g>' + t(x + 58, y + 100, n, 9, K, 700, "middle", SANS, 'letter-spacing="1.4"')
    return svg(k, "Neun Bausteine des Sprints als Piktogramme")


# ---------------------------------------------------------------- Szene
def v15():
    """Szene in Linien: Zwei Tage vor Ort – Beraterin, Kunde, Laptop, an der Wand entsteht die Seite."""
    def person(x, y, fill, s=1):
        return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-34 0v-16c0-20 15-32 34-32s34 12 34 32V0z" fill="{fill}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>'
                f'<circle cy="-66" r="18" fill="{W}" stroke="{K}" stroke-width="4"/></g>')
    return svg(f'''
<circle cx="250" cy="110" r="96" fill="{M3}"/>
{r(150, 30, 220, 150, W, 12, f'stroke="{K}" stroke-width="4"')}<path d="M150 56h220" stroke="{K}" stroke-width="4"/>
{r(170, 72, 180, 46, M, 6)}{r(184, 86, 90, 8, ON, 4)}{r(184, 100, 60, 6, ON, 3)}
{r(170, 130, 82, 34, "none", 6, f'stroke="{K}" stroke-width="2.5" stroke-dasharray="5 5"')}{r(266, 130, 84, 34, G, 6, f'stroke="{K}" stroke-width="2.5"')}
<path d="M260 180v18" stroke="{K}" stroke-width="4"/>
{person(110, 300, M3)}{person(330, 300, W)}
<path d="M30 300h380" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
<path d="M60 300l-12 80M380 300l12 80" stroke="{K}" stroke-width="4" stroke-linecap="round"/>
<path d="M176 298l12-52h86l-10 52z" fill="{W}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/><circle cx="226" cy="272" r="5" fill="{K}"/>
{r(126, 210, 54, 34, W, 17, f'stroke="{K}" stroke-width="3"')}<path d="M140 244l-6 10 14-10" fill="{W}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>{r(138, 222, 30, 5, K, 2.5)}{r(138, 232, 20, 5, G3, 2.5)}
{r(330, 330, 84, 30, K, 15)}{t(372, 350, "TAG 2", 11, W, 700, "middle")}
''', "Zwei Tage vor Ort: gemeinsam entsteht die Landingpage")



# ================================================================ Runde 3 (Daniel, 10.10.2026): viele weitere Darstellungsarten
# Alle zeigen dasselbe Motiv (Landingpage, 48 Stunden, Handy), damit nur die Darstellungsart verglichen wird.
import math


def _browser(x, y, w, h, stroke=K, sw=4, fill=W, rx=12, leiste=True):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if leiste:
        s += f'<path d="M{x} {y+30}h{w}" stroke="{stroke}" stroke-width="{sw}"/><circle cx="{x+18}" cy="{y+15}" r="5" fill="{stroke}"/><circle cx="{x+34}" cy="{y+15}" r="5" fill="{stroke}"/>'
    return s


def s_skizze():
    """Handskizze: wackelige Marker-Linie, Schraffur statt Fläche."""
    defs = ('<filter id="hvsk"><feTurbulence type="fractalNoise" baseFrequency=".035" numOctaves="2" seed="4"/><feDisplacementMap in="SourceGraphic" scale="5"/></filter>'
            f'<pattern id="hvskp" width="9" height="9" patternUnits="userSpaceOnUse" patternTransform="rotate(-35)"><path d="M0 4.5h9" stroke="{MT}" stroke-width="2.6"/></pattern>')
    return svg(f'''<g filter="url(#hvsk)" fill="none" stroke="{K}" stroke-width="3.6" stroke-linecap="round" stroke-linejoin="round">
<path d="M48 72c80-4 170-3 252 2l-3 236c-80 4-168 3-250-1z"/><path d="M50 108c80 2 170 1 249-2"/>
<path d="M74 132h196v64H74z" fill="url(#hvskp)" stroke="{MT}"/>
<path d="M74 222c40-6 90 4 140-2M74 244c30-4 70 2 100-1"/>
<path d="M74 274h76v22H74z" fill="{M}" stroke="{K}"/>
<circle cx="336" cy="280" r="64" fill="{W}"/><path d="M336 280v-38M336 280l26 14M336 208v-10M322 196h28"/>
<path d="M300 154c30 -24 54 -20 70 4m-12 -12 12 12 -16 6"/>
</g>{t(336, 372, "48 h", 26, K, 700, "middle", SERIF, 'font-style="italic"')}''', "Handskizze einer Landingpage mit Stoppuhr", defs)


def s_softd():
    """Weiches 3D: Fläche mit Tiefe, Verläufe und weicher Schatten – wie Knete/Clay."""
    defs = ('<linearGradient id="hv3a" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#ffffff"/><stop offset="1" stop-color="#ece9e4"/></linearGradient>'
            f'<linearGradient id="hv3b" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{M2}"/><stop offset="1" stop-color="{M}"/></linearGradient>'
            f'<radialGradient id="hv3c" cx=".35" cy=".3" r=".8"><stop offset="0" stop-color="#ffffff"/><stop offset=".6" stop-color="{M3}"/><stop offset="1" stop-color="{M2}"/></radialGradient>'
            '<filter id="hv3s" x="-30%" y="-30%" width="160%" height="170%"><feDropShadow dx="0" dy="16" stdDeviation="14" flood-color="#1a1817" flood-opacity=".18"/></filter>')
    return svg(f'''
<ellipse cx="220" cy="356" rx="170" ry="18" fill="#1a1817" opacity=".06"/>
<g filter="url(#hv3s)"><rect x="56" y="74" width="260" height="250" rx="28" fill="#d8d4cd"/><rect x="56" y="62" width="260" height="250" rx="28" fill="url(#hv3a)"/></g>
<rect x="80" y="90" width="44" height="12" rx="6" fill="#d8d4cd"/>
<rect x="80" y="120" width="212" height="84" rx="18" fill="url(#hv3b)"/>
<rect x="80" y="222" width="150" height="14" rx="7" fill="#d8d4cd"/><rect x="80" y="246" width="110" height="14" rx="7" fill="#e6e2dc"/>
<rect x="80" y="274" width="96" height="22" rx="11" fill="{K}"/>
<g filter="url(#hv3s)"><circle cx="340" cy="250" r="64" fill="url(#hv3c)"/></g>
{t(340, 262, "48h", 32, M4, 700, "middle", SERIF)}
''', "Weiches 3D: Landingpage und Uhr als Objekte", defs)


def s_glas():
    """Glas: matte, durchscheinende Karten über weichen Farbflächen – modern, technisch."""
    defs = ('<filter id="hvgb" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter>'
            '<filter id="hvgs" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#1a1817" flood-opacity=".12"/></filter>')
    return svg(f'''
<g filter="url(#hvgb)"><circle cx="150" cy="150" r="96" fill="{M}" opacity=".75"/><circle cx="310" cy="260" r="90" fill="{M2}" opacity=".8"/><circle cx="300" cy="110" r="60" fill="#cfcac2"/></g>
<g filter="url(#hvgs)"><rect x="60" y="80" width="270" height="230" rx="22" fill="#ffffff" fill-opacity=".55" stroke="#ffffff" stroke-width="2"/></g>
<rect x="84" y="104" width="60" height="10" rx="5" fill="{K}" opacity=".7"/>
<rect x="84" y="134" width="190" height="16" rx="8" fill="{K}"/><rect x="84" y="160" width="140" height="10" rx="5" fill="{K}" opacity=".4"/>
<rect x="84" y="196" width="100" height="30" rx="15" fill="{M}"/>
<g filter="url(#hvgs)"><rect x="270" y="170" width="120" height="180" rx="24" fill="#ffffff" fill-opacity=".7" stroke="#ffffff" stroke-width="2"/></g>
{t(330, 250, "48h", 30, K, 700, "middle", SERIF)}{t(330, 274, "BIS LIVE", 10, K, 700, "middle", SANS, 'letter-spacing="2" opacity=".6"')}
''', "Glas: durchscheinende Karten über Farbflächen", defs)


def s_einlinie():
    """Eine Linie: Browser, Handy und Uhr in einem durchgehenden Strich, ein Farbpunkt."""
    return svg(f'''
<circle cx="152" cy="150" r="26" fill="{M}"/>
<path d="M24 330H60V70h240v40H60M100 150h30M100 190h170M100 214h120M100 254h70v22h-70v-22M300 110v120c0-40 30-70 66-70s66 30 66 70-30 70-66 70-66-30-66-70M366 230v-40M366 230l26 16M300 230v100H24" fill="none" stroke="{K}" stroke-width="4" stroke-linejoin="round" stroke-linecap="round"/>
''', "Eine durchgehende Linie")


def s_bauhaus():
    """Bauhaus-Komposition: Grundformen ergeben Seite und Zeit – abstrakt."""
    return svg(f'''
<rect x="60" y="60" width="200" height="280" fill="{K}"/>
<path d="M260 60a140 140 0 0 1 0 280z" fill="{M}"/>
<circle cx="160" cy="150" r="58" fill="{W}"/>
<rect x="90" y="250" width="140" height="22" fill="{W}"/><rect x="90" y="286" width="90" height="22" fill="{M}"/>
<path d="M330 200h60" stroke="{K}" stroke-width="8"/><circle cx="330" cy="200" r="10" fill="{K}"/>
<path d="M160 150V108M160 150l30 18" stroke="{K}" stroke-width="8" stroke-linecap="square"/>
''', "Bauhaus: Grundformen als Seite und Uhr")


def s_pixel():
    """Pixel: alles aus Quadraten – digital, verspielt-nerdig."""
    P = 12
    karte = [
        "....................",
        ".KKKKKKKKKKKKKKKK...",
        ".K.K.K..........K...",
        ".KKKKKKKKKKKKKKKK...",
        ".K..............K...",
        ".K.MMMMMMMMMMM..K...",
        ".K.MMMMMMMMMMM..K...",
        ".K.MMMMMMMMMMM..K...",
        ".K..............K...",
        ".K.KKKKKKKK.....K...",
        ".K.GGGGGG.......K...",
        ".K..............K.KKK",
        ".K.MMMM.........KK.MK",
        ".K..............KK.MK",
        ".KKKKKKKKKKKKKKKKK.MK",
        ".................KKKK",
    ]
    farbe = {"K": K, "M": M, "G": G3}
    px = "".join(r(30 + x * P * 1.25, 60 + y * P * 1.25, P * 1.25 - 2, P * 1.25 - 2, farbe[c]) for y, z in enumerate(karte) for x, c in enumerate(z) if c in farbe)
    return svg(px + t(300, 380, "48H", 22, K, 700, "middle", "monospace"), "Pixel: Landingpage und Handy aus Quadraten")


def s_popart():
    """Pop-Art: Halbtonpunkte, dicke Kontur, Sternplatzer – laut, comicnah."""
    defs = f'<pattern id="hvpp" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="3.4" fill="{M2}"/></pattern>'
    stern = " ".join(f"{330 + (64 if i % 2 == 0 else 40) * math.cos(math.radians(i * 18 - 90)):.1f},{110 + (64 if i % 2 == 0 else 40) * math.sin(math.radians(i * 18 - 90)):.1f}" for i in range(20))
    return svg(f'''
<rect x="20" y="20" width="400" height="360" rx="0" fill="url(#hvpp)"/>
{_browser(56, 96, 250, 250, K, 7, W, 6)}
<rect x="80" y="152" width="200" height="70" fill="{M}" stroke="{K}" stroke-width="6"/>
<path d="M80 250h170M80 274h120" stroke="{K}" stroke-width="8" stroke-linecap="round"/>
<polygon points="{stern}" fill="{M}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
{t(330, 120, "48H!", 26, ON, 700, "middle", SANS)}
''', "Pop-Art: Landingpage mit Sternplatzer", defs)


def s_linol():
    """Linolschnitt: dunkle Fläche, die Motive als weiße Schnitte, raue Kanten."""
    defs = '<filter id="hvln"><feTurbulence type="fractalNoise" baseFrequency=".08" numOctaves="2" seed="2"/><feDisplacementMap in="SourceGraphic" scale="4"/></filter>'
    return svg(f'''<g filter="url(#hvln)">
<rect x="30" y="30" width="380" height="340" rx="10" fill="{K}"/>
<g fill="none" stroke="{W}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round">
<rect x="70" y="80" width="200" height="220" rx="6"/><path d="M70 112h200M96 240h120M96 266h80"/>
<circle cx="320" cy="250" r="56"/><path d="M320 250v-34M320 250l22 12M320 180v-10"/>
</g>
<rect x="92" y="134" width="156" height="78" fill="{M}"/>
{"".join(f'<path d="M{96 + i * 14} 140l40 66" stroke="{K}" stroke-width="3"/>' for i in range(9))}
</g>''', "Linolschnitt: Landingpage und Uhr", defs)


def s_blueprint():
    """Blaupause in Akzentfarbe: helle Linien auf dunkler Fläche, mit Maßen – technisch, edel."""
    gitter = "".join(f'<path d="M{x} 30v340" stroke="{W}" stroke-opacity=".08"/>' for x in range(30, 411, 20)) + "".join(f'<path d="M30 {y}h380" stroke="{W}" stroke-opacity=".08"/>' for y in range(30, 371, 20))
    L = f'fill="none" stroke="{W}" stroke-width="2"'
    return svg(f'''
<rect x="30" y="30" width="380" height="340" rx="16" fill="{M4}"/>{gitter}
<rect x="150" y="70" width="140" height="260" rx="6" {L}/><path d="M150 100h140M150 170h140M150 230h140M150 290h140" {L} stroke-opacity=".7"/>
<rect x="164" y="114" width="80" height="8" fill="{W}"/><rect x="164" y="132" width="60" height="6" fill="{W}" opacity=".6"/><rect x="164" y="148" width="40" height="12" rx="6" fill="{W}"/>
<path d="M120 70v260M114 70h12M114 330h12" {L}/><g transform="rotate(-90 106 200)">{t(106, 204, "48 STUNDEN", 10, W, 700, "middle")}</g>
<path d="M290 135h50M290 200h50M290 260h50" {L} stroke-dasharray="3 4"/>
{t(346, 139, "HERO", 10, W, 700)}{t(346, 204, "LÖSUNG", 10, W, 700)}{t(346, 264, "KONTAKT", 10, W, 700)}
''', "Blaupause: Aufbau der Landingpage")


def s_icon():
    """Ein großes Symbol: nur ein Zeichen, dicke Linie – maximal reduziert."""
    return svg(f'''
<rect x="70" y="70" width="300" height="240" rx="28" fill="none" stroke="{K}" stroke-width="14"/>
<path d="M70 126h300" stroke="{K}" stroke-width="14"/>
<path d="M232 152l-62 88h56l-20 70 76-100h-58z" fill="{M}" stroke="{K}" stroke-width="10" stroke-linejoin="round"/>
''', "Ein Symbol: Seite mit Blitz")


def s_silhouette():
    """Scherenschnitt: nur Silhouetten in einer Farbe – zwei Menschen arbeiten an der Seite."""
    return svg(f'''
<rect x="140" y="50" width="160" height="110" rx="8" fill="{M}"/><rect x="156" y="72" width="80" height="10" fill="{W}"/><rect x="156" y="92" width="110" height="26" fill="{W}" opacity=".5"/>
<path d="M216 160v24" stroke="{M}" stroke-width="6"/>
<circle cx="110" cy="210" r="28" fill="{K}"/><path d="M58 330c0-50 22-84 52-84s52 34 52 84z" fill="{K}"/>
<circle cx="330" cy="210" r="28" fill="{K}"/><path d="M278 330c0-50 22-84 52-84s52 34 52 84z" fill="{K}"/>
<path d="M180 300h80l14-52h-80z" fill="{K}"/>
<rect x="30" y="330" width="380" height="12" rx="6" fill="{K}"/>
''', "Scherenschnitt: zwei Menschen, eine Seite")


def s_verlauf():
    """Verlauf modern: weiche Farbverläufe, schwebende Karten – wie Software-Websites."""
    defs = (f'<linearGradient id="hvva" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{M2}"/><stop offset="1" stop-color="{M4}"/></linearGradient>'
            '<filter id="hvvs" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="14" stdDeviation="14" flood-color="#1a1817" flood-opacity=".18"/></filter>')
    return svg(f'''
<path d="M70 300c-40-120 40-240 170-240s190 110 150 210-280 150-320 30z" fill="url(#hvva)"/>
<g filter="url(#hvvs)"><rect x="90" y="110" width="210" height="150" rx="16" fill="{W}"/></g>
<rect x="108" y="130" width="100" height="10" rx="5" fill="{K}"/><rect x="108" y="150" width="160" height="8" rx="4" fill="#dcd8d1"/><rect x="108" y="166" width="130" height="8" rx="4" fill="#dcd8d1"/>
<rect x="108" y="200" width="84" height="26" rx="13" fill="{M}"/>
<g filter="url(#hvvs)"><rect x="250" y="220" width="130" height="64" rx="14" fill="{W}"/></g>
<circle cx="276" cy="252" r="14" fill="{M3}"/>{t(298, 248, "Live", 12, K, 700)}{t(298, 264, "nach 48 h", 10, "#8a847c", 600)}
''', "Verlauf: schwebende Karten über weicher Farbfläche", defs)


def s_netz():
    """Netz: Bausteine als Knoten, verbunden zur fertigen Seite – zeigt Zusammenhänge."""
    knoten = [(80, 90, "ZIELGRUPPE"), (80, 200, "PROBLEM"), (80, 310, "LÖSUNG")]
    k = "".join(f'<path d="M{x+30} {y}C{200} {y} {200} 200 {286} 200" fill="none" stroke="{K}" stroke-width="3"/>' for x, y, _ in knoten)
    k += "".join(f'<circle cx="{x}" cy="{y}" r="30" fill="{W}" stroke="{K}" stroke-width="4"/>' + t(x, y + 50, n, 10, K, 700, "middle", SANS, 'letter-spacing="1.2"') for x, y, n in knoten)
    k += f'<circle cx="80" cy="90" r="9" fill="{M}"/><path d="M80 186v16" stroke="{K}" stroke-width="5" stroke-linecap="round"/><circle cx="80" cy="212" r="3" fill="{K}"/><path d="M68 310l8 8 16-17" fill="none" stroke="{K}" stroke-width="5" stroke-linecap="round" stroke-linejoin="round"/>'
    return svg(k + f'''
<rect x="290" y="110" width="110" height="180" rx="18" fill="{W}" stroke="{K}" stroke-width="4"/><rect x="304" y="132" width="82" height="50" rx="8" fill="{M}"/>
<rect x="304" y="194" width="60" height="7" rx="3.5" fill="{K}"/><rect x="304" y="208" width="44" height="7" rx="3.5" fill="{G3}"/><rect x="304" y="250" width="56" height="20" rx="10" fill="{K}"/>
<circle cx="286" cy="200" r="7" fill="{K}"/>
''', "Netz: Zielgruppe, Problem und Lösung führen zur Seite")


def s_greybox():
    """Lo-Fi-Wireframe: nur graue Kästen, ein Akzent – nüchtern, Konzeptphase."""
    return svg(f'''
{r(60, 50, 320, 300, "#f4f3f0", 10)}
{r(84, 74, 70, 14, "#cfcac2", 4)}{r(300, 74, 56, 14, "#cfcac2", 4)}
{r(84, 110, 272, 110, "#e3dfd8", 6)}<path d="M84 110l272 110M356 110L84 220" stroke="#cfcac2" stroke-width="2"/>
{r(84, 240, 84, 60, "#e3dfd8", 6)}{r(178, 240, 84, 60, "#e3dfd8", 6)}{r(272, 240, 84, 60, "#e3dfd8", 6)}
{r(84, 316, 110, 20, M, 10)}
''', "Lo-Fi-Wireframe in Grau")


def s_fallblatt():
    """Fallblatt-Anzeige: 48:00 wie auf dem Bahnsteig – Typografie mit Mechanik."""
    def blatt(x, z):
        return (f'<rect x="{x}" y="120" width="76" height="120" rx="10" fill="{K}"/><path d="M{x} 180h76" stroke="#3d3a37" stroke-width="3"/>'
                f'<circle cx="{x+4}" cy="180" r="3" fill="#3d3a37"/><circle cx="{x+72}" cy="180" r="3" fill="#3d3a37"/>' + t(x + 38, 210, z, 84, W, 600, "middle", SANS))
    return svg(f'''
{blatt(28, "4")}{blatt(110, "8")}{t(206, 206, ":", 70, K, 700, "middle")}{blatt(232, "0")}{blatt(314, "0")}
{r(28, 268, 140, 34, M, 17)}{t(98, 290, "BIS LIVE", 12, ON, 700, "middle", SANS, 'letter-spacing="2"')}
{t(186, 290, "Sprint Landingpage · Gleis 1", 12, "#6f6a64", 600)}
''', "Fallblatt-Anzeige 48:00")


def s_comic():
    """Comic-Panels: drei Bilder, eine kleine Geschichte – erzählend."""
    def panel(x, inhalt, txt):
        return f'<rect x="{x}" y="70" width="124" height="230" rx="4" fill="{W}" stroke="{K}" stroke-width="5"/>{inhalt}' + t(x + 62, 330, txt, 11, K, 700, "middle", SANS, 'letter-spacing="1.4"')
    p1 = (f'<circle cx="64" cy="210" r="16" fill="{W}" stroke="{K}" stroke-width="4"/><path d="M38 270c0-26 12-40 26-40s26 14 26 40" fill="{W}" stroke="{K}" stroke-width="4"/>'
          f'<path d="M30 92h94v52H72l-14 14v-14H30z" fill="{W}" stroke="{K}" stroke-width="3.5" stroke-linejoin="round"/>' + t(77, 114, "Wir brauchen", 10, K, 600, "middle") + t(77, 130, "eine Seite!", 10, K, 700, "middle"))
    p2 = (f'<rect x="164" y="150" width="96" height="66" rx="6" fill="{W}" stroke="{K}" stroke-width="4"/><rect x="174" y="162" width="76" height="18" fill="{M}"/><path d="M156 226h112" stroke="{K}" stroke-width="5" stroke-linecap="round"/>'
          + t(212, 112, "Tag 1–2", 16, K, 700, "middle", SERIF))
    stern = " ".join(f"{354 + (46 if i % 2 == 0 else 28) * math.cos(math.radians(i * 22.5 - 90)):.1f},{150 + (46 if i % 2 == 0 else 28) * math.sin(math.radians(i * 22.5 - 90)):.1f}" for i in range(16))
    p3 = (f'<polygon points="{stern}" fill="{M}" stroke="{K}" stroke-width="3.5" stroke-linejoin="round"/>' + t(354, 156, "LIVE!", 13, ON, 700, "middle")
          + f'<rect x="330" y="206" width="48" height="80" rx="9" fill="{W}" stroke="{K}" stroke-width="4"/><rect x="338" y="218" width="32" height="20" fill="{M}"/>')
    return svg(panel(16, p1, "BRIEFING") + panel(158, p2, "SPRINT") + panel(300, p3, "GO-LIVE"), "Comic: Briefing, Sprint, Go-live")


def s_brutal():
    """Neo-Brutalismus: dicke Konturen, harter Versatzschatten, große Labels – direkt, kantig."""
    return svg(f'''
<rect x="62" y="72" width="250" height="230" fill="{K}"/><rect x="50" y="60" width="250" height="230" fill="{W}" stroke="{K}" stroke-width="6"/>
<path d="M50 100h250" stroke="{K}" stroke-width="6"/><rect x="66" y="74" width="12" height="12" fill="{K}"/><rect x="86" y="74" width="12" height="12" fill="{K}"/>
<rect x="72" y="122" width="206" height="70" fill="{M}" stroke="{K}" stroke-width="5"/>
<rect x="72" y="212" width="140" height="14" fill="{K}"/><rect x="72" y="238" width="100" height="14" fill="{K}"/>
<rect x="232" y="252" width="176" height="64" fill="{K}"/><rect x="222" y="242" width="176" height="64" fill="{M3}" stroke="{K}" stroke-width="6"/>
{t(310, 284, "LIVE IN", 14, K, 700, "middle")}{t(310, 300, "48 STUNDEN", 14, K, 700, "middle")}
''', "Neo-Brutalismus: dicke Kontur, harter Schatten")


def s_punkte():
    """Punktraster: die Seite aus einem Feld von Punkten – reduziert, digital."""
    pkt = ""
    for gy in range(22):
        for gx in range(26):
            x, y = 30 + gx * 15, 40 + gy * 15
            c = "#e3dfd8"; rr = 3.2
            if 3 <= gx <= 16 and 2 <= gy <= 19 and (gx in (3, 16) or gy in (2, 19, 4)): c = K
            if 5 <= gx <= 14 and 6 <= gy <= 9: c = M; rr = 4.4
            if 5 <= gx <= 11 and gy in (12, 14): c = K
            if (gx - 21) ** 2 + (gy - 14) ** 2 <= 16 and (gx - 21) ** 2 + (gy - 14) ** 2 >= 9: c = M if gx >= 21 or gy <= 14 else K; rr = 4
            pkt += f'<circle cx="{x}" cy="{y}" r="{rr}" fill="{c}"/>'
    return svg(pkt, "Punktraster: Seite und Uhr")


def s_origami():
    """Origami/Low-Poly: die Seite aus gefalteten Facetten."""
    return svg(f'''
<polygon points="60,80 300,60 280,320 70,330" fill="#f4f3f0"/>
<polygon points="60,80 300,60 180,190" fill="#ffffff"/><polygon points="300,60 280,320 180,190" fill="#e3dfd8"/>
<polygon points="70,330 280,320 180,190" fill="#ece9e4"/><polygon points="60,80 70,330 180,190" fill="#f7f6f3"/>
<polygon points="96,120 250,110 236,170 104,176" fill="{M}"/><polygon points="96,120 250,110 170,150" fill="{M2}"/>
<polygon points="300,240 380,200 400,290 330,330" fill="{M4}"/><polygon points="300,240 380,200 350,270" fill="{M}"/>
<polygon points="380,200 400,290 350,270" fill="{M2}"/>
''', "Origami: gefaltete Facetten")


def s_aquarell():
    """Aquarell: weiche Farbwolken, darüber eine feine Tuschelinie."""
    defs = ('<filter id="hvaq" x="-30%" y="-30%" width="160%" height="160%"><feTurbulence type="fractalNoise" baseFrequency=".02" numOctaves="3" seed="7"/>'
            '<feDisplacementMap in="SourceGraphic" scale="30"/><feGaussianBlur stdDeviation="5"/></filter>')
    return svg(f'''
<g filter="url(#hvaq)" opacity=".85"><rect x="70" y="120" width="210" height="90" fill="{M2}"/><circle cx="330" cy="260" r="70" fill="{M3}"/><rect x="80" y="250" width="120" height="50" fill="#d9d4cc"/></g>
<g fill="none" stroke="{K}" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round">
<rect x="56" y="80" width="250" height="250" rx="8"/><path d="M56 108h250M80 236h150M80 256h110"/><rect x="80" y="126" width="196" height="80" rx="4"/>
<circle cx="330" cy="260" r="58"/><path d="M330 260v-32M330 260l22 12"/></g>
''', "Aquarell mit Tuschelinie", defs)


def s_karte():
    """Wegkarte: der Weg vom Start zum Live-Gang mit Stationen – wie eine Landkarte."""
    hoehen = "".join(f'<path d="M{20+i*6} {360-i*14}c60-30 120 10 180-20s140-10 220-40" fill="none" stroke="#e3dfd8" stroke-width="2"/>' for i in range(0, 20, 3))
    pin = lambda x, y, c: f'<path d="M{x} {y}c-14-18-20-26-20-36a20 20 0 0 1 40 0c0 10-6 18-20 36z" fill="{c}" stroke="{K}" stroke-width="3"/><circle cx="{x}" cy="{y-36}" r="7" fill="{W}"/>'
    return svg(f'''{hoehen}
<path d="M60 330C120 320 100 250 170 240S240 170 210 130 290 70 380 80" fill="none" stroke="{K}" stroke-width="4" stroke-dasharray="2 12" stroke-linecap="round"/>
{pin(60, 330, W)}{t(60, 360, "START", 10, K, 700, "middle")}
<circle cx="170" cy="240" r="12" fill="{W}" stroke="{K}" stroke-width="3"/>{t(190, 244, "Briefing", 11, K, 600)}
<circle cx="214" cy="140" r="12" fill="{M}" stroke="{K}" stroke-width="3"/>{t(234, 144, "Sprint · 2 Tage", 11, K, 600)}
<path d="M380 80V20" stroke="{K}" stroke-width="4" stroke-linecap="round"/><path d="M380 22l34 12-34 13z" fill="{M}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>
{t(380, 108, "LIVE", 12, K, 700, "middle")}
''', "Wegkarte vom Start zum Go-live")


def s_isolinie():
    """Isometrische Linienzeichnung: räumlich, aber nur Kontur – leichter als die Platten."""
    def iso(x, y):  # Rasterkoordinaten → Bild
        return 220 + (x - y) * 26, 120 + (x + y) * 15
    def poly(pts, fill="none"):
        return f'<polygon points="{" ".join(f"{a:.0f},{b:.0f}" for a, b in (iso(*p) for p in pts))}" fill="{fill}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
    def quader(x, y, w, d, h, oben=W):
        a = [iso(x, y), iso(x + w, y), iso(x + w, y + d), iso(x, y + d)]
        top = " ".join(f"{p[0]:.0f},{p[1]-h:.0f}" for p in a)
        s = f'<polygon points="{" ".join(f"{p[0]:.0f},{p[1]:.0f}" for p in (a[3], a[2], (a[2][0], a[2][1]-h), (a[3][0], a[3][1]-h)))}" fill="{W}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
        s += f'<polygon points="{" ".join(f"{p[0]:.0f},{p[1]:.0f}" for p in (a[2], a[1], (a[1][0], a[1][1]-h), (a[2][0], a[2][1]-h)))}" fill="{W}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
        return s + f'<polygon points="{top}" fill="{oben}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>'
    return svg(poly([(-3, -3), (7, -3), (7, 7), (-3, 7)]) + quader(-2, -2, 6, 1.4, 14) + quader(-2, 0, 4, 2.4, 14, M) + quader(-2, 3, 2.6, 2.6, 14) + quader(1, 3, 2.6, 2.6, 14)
               + quader(5, 4, 1.4, 2.2, 70), "Isometrische Linienzeichnung")


# ---------------------------------------------------------------- Farbwelten
FARBWELT = {
    "magenta": {"#C51F5D": "#C51F5D", "#C51F5E": "#C51F5D", "#FEFEFE": "#ffffff", "#e27fa3": "#e27fa3", "#f5d3df": "#f5d3df", "#7a1339": "#7a1339"},
    "cyan":    {"#C51F5D": "#0B9FBD", "#C51F5E": "#0a8aa4", "#FEFEFE": "#ffffff", "#e27fa3": "#72c6d8", "#f5d3df": "#d4eef4", "#7a1339": "#06576a"},
    "violett": {"#C51F5D": "#8613A1", "#C51F5E": "#8613A1", "#FEFEFE": "#ffffff", "#e27fa3": "#bb7bcc", "#f5d3df": "#ecd9f1", "#7a1339": "#4e0b5e"},
    "gelb":    {"#C51F5D": "#fff400", "#C51F5E": "#1a1817", "#FEFEFE": "#1a1817", "#e27fa3": "#fff86b", "#f5d3df": "#fffbc7", "#7a1339": "#1a1817"},
}


def farbig(bild, welt, zusatz):
    """Ein Bild in eine andere Farbwelt umfärben; IDs eindeutig machen, damit mehrere Kopien auf einer Seite gehen."""
    zuordnung = FARBWELT[welt]
    bild = re.sub("|".join(re.escape(k) for k in zuordnung), lambda m: zuordnung[m.group(0)], bild)
    return re.sub(r'(id="|url\(#)(hv[a-z0-9]+)', lambda m: f"{m.group(1)}{m.group(2)}-{zusatz}", bild)


# ---------------------------------------------------------------- Liste
# (Funktion, Name, aus Runde)
STILE = [
    (v2, "Isometrisch · Platten", 1), (v3, "Bauplan", 1), (v4, "Duoton", 1), (v5, "Prozess-Infografik", 1), (v7, "Typografisch", 1),
    (v11, "Riso-Druck (Grau + Akzent)", 2), (v12, "Uhr-Infografik", 2), (v13, "Piktogramm-System", 2), (v15, "Szene in Linien", 2),
    (s_skizze, "Handskizze", 3), (s_softd, "Weiches 3D", 3), (s_glas, "Glas", 3), (s_einlinie, "Eine Linie", 3), (s_bauhaus, "Bauhaus-Formen", 3),
    (s_pixel, "Pixel", 3), (s_popart, "Pop-Art / Halbton", 3), (s_linol, "Linolschnitt", 3), (s_blueprint, "Blaupause dunkel", 3), (s_icon, "Ein großes Symbol", 3),
    (s_silhouette, "Scherenschnitt", 3), (s_verlauf, "Verlauf modern", 3), (s_netz, "Netz / Zusammenhang", 3), (s_greybox, "Lo-Fi-Wireframe", 3), (s_fallblatt, "Fallblatt-Anzeige", 3),
    (s_comic, "Comic-Panels", 3), (s_brutal, "Neo-Brutalismus", 3), (s_punkte, "Punktraster", 3), (s_origami, "Origami / Low-Poly", 3), (s_aquarell, "Aquarell + Tusche", 3),
    (s_karte, "Wegkarte", 3), (s_isolinie, "Isometrisch · Linie", 3),
]

# Qualitätssicherung: Seitenbaum der Live-Seite und Eignung der Stile
BAUM = [
    ("Startseite", "", ["Strategie, die wirkt."]),
    ("Strategiehandwerk", "gelb", ["Strategie in den Alltag überführen", "Komplexe Themen strukturieren & kommunizieren", "Innovation & Geschäftsmodell neu denken", "Teams befähigen, professionell zu kommunizieren"]),
    ("Workshops", "magenta", ["KI zum Anfassen", "Sprint Landingpage", "Moderation deines Workshops"]),
    ("Marketing 2.0", "cyan", ["MarketingEcoSystem (MES)", "sofort sichtbar", "Paid Ads", "Medien › PowerPoint, Landingpage, Roll-up, Video"]),
    ("Training & Sparring", "violett", ["Teams befähigen (Präsentationsseminar)", "1:1 Sparring"]),
    ("Weitere Einzelseiten", "", ["Impulsvorträge", "Digitale Tools", "Der beste Workshop"]),
]
EIGNUNG = [  # Stil, abstrakte Beratung (Strategie, Sparring), greifbare Produkte (Medien, Landingpage, Ads), Formate mit Ablauf (Workshops), Urteil
    ("Piktogramm-System", "ja", "ja", "ja", "trägt alles: jede Seite hat 8–9 Bausteine; einheitlich, in jeder Farbe gleich gut"),
    ("Szene in Linien", "ja", "ja", "ja", "Menschen und Situation gibt es bei jedem Thema; beratungsnah"),
    ("Isometrisch · Linie / Platten", "teils", "ja", "teils", "stark bei Aufbau und Schichten (Strategie-Ebenen, MES), schwach bei Sparring"),
    ("Bauplan / Blaupause", "teils", "ja", "teils", "perfekt für Medien; für Strategie nur als „Bauplan des Bereichs“"),
    ("Netz / Wegkarte", "ja", "teils", "ja", "zeigen Zusammenhang bzw. Weg – passt zu Strategie, Innovation, Abläufen"),
    ("Prozess-Infografik", "teils", "teils", "ja", "jede Seite hat einen Ablauf, aber alle Köpfe sähen gleich aus"),
    ("Duoton / Verlauf / Glas", "nein", "ja", "teils", "brauchen ein Gerät oder Produkt – für Beratungsthemen leer"),
    ("Typografisch / Fallblatt", "teils", "teils", "teils", "nur wo es eine starke Zahl gibt (48 h, 1:1); bei Strategie fehlt sie"),
    ("Uhr-Infografik", "nein", "teils", "teils", "nur für zeitgebundene Formate"),
    ("Bauhaus, Pixel, Pop-Art, Comic, Aquarell …", "–", "–", "–", "Stilmittel – gehen mit jedem Motiv, aber prägen den Markenauftritt stark"),
]

CSS = """<style>
.hv-intro { padding: 4.5rem 0 1.4rem; }
.hv-intro h1 { font-family: var(--font-serif); font-size: clamp(2.2rem, 4.6vw, 3.4rem); line-height: 1.15; }
.hv-intro p { max-width: 46rem; margin-top: 1.1rem !important; font-size: 1.08rem; line-height: 1.6; color: #3d3a37; }
.hv-h2 { margin: 3.4rem 0 1.2rem !important; font-family: var(--font-serif); font-size: 1.9rem; }
.hv-raster { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.hv-zelle { margin: 0; position: relative; padding: 1.1rem 1.1rem .9rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; background: #fff; cursor: pointer; transition: background .15s; }
.hv-zelle:hover { background: #faf9f7; }
.hv-zelle.ist-aktiv { box-shadow: inset 0 0 0 3px #1a1817; }
.hv-zelle figcaption { display: flex; gap: .5rem; align-items: baseline; margin-top: .5rem; font-size: .82rem; font-weight: 600; color: #3d3a37; }
.hv-zelle figcaption b { font-family: var(--font-serif); color: #1a1817; }
.hv-zelle figcaption i { margin-left: auto; white-space: nowrap; font-style: normal; font-weight: 500; color: #8a847c; }
.hv-bild { display: block; width: 100%; height: auto; }
.hv-vorschau { position: sticky; top: 72px; z-index: 5; background: #fff; border-bottom: 1px solid #e3dfd8; }
.hv-vorschau .e2-kopf { padding: 1.6rem 0 1.4rem !important; }
.hv-vorschau .e2-kopf h1 { font-size: clamp(1.8rem, 3vw, 2.6rem) !important; }
.hv-vorschau .e2-kopf__inhalt, .hv-vorschau .hero-anlaesse { display: none !important; }
.hv-vorschau .e2-kopfbild { width: min(100%, 17rem) !important; }
.hv-vorschau-label { font-size: .8rem; font-weight: 600; color: #8a847c; }
.hv-farben { display: grid; grid-template-columns: 9rem repeat(4, minmax(0, 1fr)); border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.hv-farben > div { padding: .8rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; font-size: .82rem; font-weight: 600; }
.hv-farben .kopf { background: #f4f3f0; }
.hv-tab { width: 100%; border-collapse: collapse; font-size: .92rem; }
.hv-tab th, .hv-tab td { padding: .7rem .8rem; border-bottom: 1px solid #e3dfd8; text-align: left; vertical-align: top; }
.hv-tab th { font-size: .78rem; letter-spacing: .08em; text-transform: uppercase; color: #6f6a64; }
.hv-tab .ja { color: #1a7a3c; font-weight: 700; } .hv-tab .teils { color: #9a6a00; font-weight: 700; } .hv-tab .nein { color: #C51F5D; font-weight: 700; }
.hv-baum { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1rem; }
.hv-baum > div { padding: 1rem 1.1rem; border: 1px solid #e3dfd8; border-radius: 14px; }
.hv-baum b { display: flex; align-items: center; gap: .5rem; font-size: .98rem; }
.hv-baum b i { width: .8rem; height: .8rem; border-radius: 50%; }
.hv-baum ul { margin: .5rem 0 0; padding-left: 1.1rem; font-size: .9rem; color: #3d3a37; line-height: 1.55; }
@media (max-width: 1100px) { .hv-raster { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 760px) { .hv-raster { grid-template-columns: repeat(2, minmax(0, 1fr)); } .hv-baum { grid-template-columns: minmax(0, 1fr); } .hv-farben { grid-template-columns: repeat(2, minmax(0, 1fr)); } .hv-farben .kopf:first-child { display: none; } }
</style>"""

JS = """<script>
document.addEventListener("click", function (e) {
  var z = e.target.closest(".hv-zelle"); if (!z) return;
  var ziel = document.querySelector(".hv-vorschau .e2-kopfbild svg"), bild = z.querySelector("svg");
  if (ziel && bild) { ziel.replaceWith(bild.cloneNode(true)); }
  document.querySelectorAll(".hv-zelle.ist-aktiv").forEach(function (x) { x.classList.remove("ist-aktiv"); });
  z.classList.add("ist-aktiv");
  document.querySelector(".hv-vorschau-label").textContent = "Vorschau im Kopf: " + z.getAttribute("data-name");
});
</script>"""

PUNKT = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1", "": "#cfcac2"}


def main():
    h = QUELLE.read_text(encoding="utf-8")
    kopf = re.search(r'<section class="e2-kopf" id="intro">.*?</section>', h, re.S).group(0)
    bild_alt = re.search(r'<svg class="e2-bild".*?</svg>', kopf, re.S).group(0)
    a, b = h.index("<main>"), h.index("</main>") + 7
    bilder = [f() for f, _, _ in STILE]
    zellen = "".join(f'<figure class="hv-zelle" data-name="{i} · {n}">{farbig(bild, "magenta", f"r{i}")}<figcaption><b>{i}</b>{n}<i>{"Runde " + str(rd) if rd < 3 else "neu"}</i></figcaption></figure>'
                     for i, ((_, n, rd), bild) in enumerate(zip(STILE, bilder), 1))
    vorschau = kopf.replace(bild_alt, farbig(bilder[7], "magenta", "vs")).replace('id="intro"', 'id="vorschau"')
    proben = [7, 8, 1, 30]  # Piktogramm, Szene, Bauplan, Isometrisch-Linie (Index in STILE, 0-basiert)
    farben = '<div class="kopf"></div>' + "".join(f'<div class="kopf">{w.capitalize()}</div>' for w in ("gelb", "magenta", "cyan", "violett"))
    for j in proben:
        farben += f'<div>{j+1} · {STILE[j][1]}</div>' + "".join(f'<div>{farbig(bilder[j], w, f"f{j}{w}")}</div>' for w in ("gelb", "magenta", "cyan", "violett"))
    baum = "".join(f'<div><b><i style="background:{PUNKT[f]}"></i>{k}</b><ul>{"".join(f"<li>{x}</li>" for x in s)}</ul></div>' for k, f, s in BAUM)
    tab = "".join(f'<tr><td><b>{n}</b></td><td class="{x}">{x}</td><td class="{y}">{y}</td><td class="{z}">{z}</td><td>{u}</td></tr>' for n, x, y, z, u in EIGNUNG)
    inhalt = f'''<section class="hv-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Header · Runde 3</p>
<h1>Darstellungsarten im Überblick</h1>
<p>Dasselbe Motiv (Sprint Landingpage) in {len(STILE)} Darstellungsarten – nur die Bilder, damit Du viel auf einmal siehst und gezielt aussortieren kannst.
Ein Klick auf ein Feld zeigt das Bild oben im echten Kopf. Kein Gelb mehr in den Workshop-Bildern; alle Bilder sind auf die Farbwelten Gelb, Magenta, Cyan und Violett umstellbar.</p></div></section>
<div class="hv-vorschau"><div class="e2-wrap"><p class="hv-vorschau-label">Vorschau im Kopf: 8 · Piktogramm-System</p></div>{vorschau}</div>
<section><div class="e2-wrap"><h2 class="hv-h2">Alle Darstellungsarten</h2><div class="hv-raster">{zellen}</div>
<h2 class="hv-h2">Farbprobe: dieselben Bilder in allen Farbwelten</h2><div class="hv-farben">{farben}</div>
<h2 class="hv-h2">Qualitätssicherung: passt der Stil für alle Themen?</h2>
<p style="max-width:46rem;color:#3d3a37;margin-bottom:1.2rem">Die Live-Seite hat drei Ebenen: Startseite, Kategorien und Einzelseiten. Die Themen reichen von reiner Beratung ohne Produkt (Strategie, Sparring) über Formate mit Ablauf (Workshops) bis zu greifbaren Produkten (Landingpage, Roll-up, Ads, Dashboard). Ein Bildstil muss alle drei Arten tragen.</p>
<div class="hv-baum">{baum}</div>
<table class="hv-tab" style="margin-top:1.6rem"><thead><tr><th>Stil</th><th>Beratung</th><th>Produkte</th><th>Formate mit Ablauf</th><th>Urteil</th></tr></thead><tbody>{tab}</tbody></table>
<div style="height:5rem"></div></div></section>'''
    seite = h[:a] + "<main>\n" + CSS + '<div class="e2-alt e2-alt--magenta e2-seite--sprint-landingpage">' + inhalt + "</div>" + JS + "\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Header-Varianten · Darstellungsarten · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent), "·", len(STILE), "Stile")


if __name__ == "__main__":
    main()
