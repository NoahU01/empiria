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
        (210, M, M4, "#9b1848", r(18, 20, 120, 16, W, 8) + r(18, 48, 80, 10, M3, 5) + r(18, 80, 60, 22, W, 11)),
    ]
    teile = "".join(_platte(170, y - 150, 190, 118, 14, o, l, re_, inh) for y, o, l, re_, inh in pl)
    schwebend = _platte(170, 6, 190, 118, 14, W, G2, G3, r(18, 18, 30, 10, K, 5) + r(150, 18, 22, 10, K, 5) + r(66, 18, 70, 10, G3, 5))
    return svg(f'''
<ellipse cx="210" cy="372" rx="170" ry="22" fill="{G}"/>
{teile}
{schwebend}
<circle cx="390" cy="66" r="34" fill="{Y}"/><path d="M390 46v20l12 8" fill="none" stroke="{K}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
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
<path d="M118 48v262" stroke="{M}" stroke-width="1.6"/><path d="M112 48h12M112 310h12" stroke="{M}" stroke-width="1.6"/>
<g transform="rotate(-90 106 180)">{t(106, 184, "48 STUNDEN", 10, M, 700, "middle")}</g>
<g transform="rotate(-8 360 336)">{r(318, 316, 88, 40, "none", 6, f'stroke="{M}" stroke-width="2.5"')}{t(362, 342, "FREIGABE", 11, M, 700, "middle")}</g>
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
{r(36, 300, 120, 40, M4, 20)}<circle cx="60" cy="320" r="6" fill="{Y}"/>{t(74, 325, "LIVE · 48h", 13, W)}
''', "Duoton: Landingpage auf Desktop und Handy", defs)


# ---------------------------------------------------------------- 5 · Prozess
def v5():
    """Infografik: die drei Etappen des Sprints auf einer Zeitachse – inhaltlich am dichtesten."""
    def knoten(x, nr, farbe):
        return f'<circle cx="{x}" cy="250" r="16" fill="{farbe}" stroke="{K}" stroke-width="3"/>' + t(x, 255, nr, 13, K if farbe != K else W, 700, "middle", SERIF)
    return svg(f'''
<path d="M40 250H404" stroke="{K}" stroke-width="3"/>
<path d="M40 250H404" stroke="{M}" stroke-width="9" stroke-linecap="round" stroke-dasharray="0 0" opacity=".0"/>
<rect x="150" y="244" width="200" height="12" rx="6" fill="{M}"/>
{knoten(70, "1", W)}{knoten(220, "2", M)}{knoten(374, "3", Y)}
{r(26, 120, 92, 66, W, 8, f'stroke="{K}" stroke-width="3"')}<circle cx="72" cy="146" r="11" fill="{G2}" stroke="{K}" stroke-width="2.5"/><path d="M56 176c3-10 9-14 16-14s13 4 16 14" fill="{G2}" stroke="{K}" stroke-width="2.5"/>
<path d="M14 194h116" stroke="{K}" stroke-width="3" stroke-linecap="round"/>
{t(72, 292, "VORBEREITUNG", 10.5, K, 700, "middle")}{t(72, 310, "2–3 Std. · online", 10.5, "#6f6a64", 500, "middle")}
{r(156, 96, 128, 98, W, 10, f'stroke="{K}" stroke-width="3"')}{r(168, 110, 104, 26, M, 5)}{r(168, 146, 70, 7, K, 3.5)}
<rect x="168" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/><rect x="224" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="186" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/><circle cx="220" cy="214" r="9" fill="{Y}" stroke="{K}" stroke-width="2.5"/><circle cx="254" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/>
{t(220, 292, "SPRINT-WORKSHOP", 10.5, K, 700, "middle")}{t(220, 310, "2 Tage · Präsenz", 10.5, "#6f6a64", 500, "middle")}
{r(346, 100, 58, 100, W, 10, f'stroke="{K}" stroke-width="3"')}{r(354, 112, 42, 30, M, 4)}{r(354, 150, 34, 5, K, 2.5)}{r(354, 160, 26, 5, G3, 2.5)}{r(354, 174, 30, 12, K, 6)}
<circle cx="404" cy="96" r="14" fill="{Y}" stroke="{K}" stroke-width="2.5"/><path d="M397 96l5 5 9-10" fill="none" stroke="{K}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{t(374, 292, "GO-LIVE", 10.5, K, 700, "middle")}{t(374, 310, "Feinschliff & live", 10.5, "#6f6a64", 500, "middle")}
<path d="M150 336v10h200v-10" fill="none" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>
{t(250, 372, "48 Stunden", 22, K, 700, "middle", SERIF)}
''', "Ablauf: Vorbereitung, Sprint-Workshop, Go-live")


# ---------------------------------------------------------------- 7 · Typografisch
def v7():
    """Typografisch: die Zahl ist das Bild. Sehr wenige Elemente."""
    return svg(f'''
{t(16, 300, "48", 250, K, 700, "start", SERIF, 'letter-spacing="-12"')}
{t(290, 300, "h", 110, M, 700, "start", SERIF)}
<g transform="rotate(6 368 104)">{r(322, 24, 92, 160, W, 14, f'stroke="{K}" stroke-width="5"')}{r(334, 42, 68, 46, M, 7)}{r(334, 98, 56, 7, K, 3.5)}{r(334, 112, 40, 7, G3, 3.5)}{r(334, 134, 44, 18, K, 9)}</g>
<path d="M20 340h400" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
{t(20, 372, "VON NULL AUF LIVE", 13, K, 700, "start", SANS, 'letter-spacing="3"')}
''', "48 Stunden – typografisch")


# ================================================================ Runde 2 (Daniel, 10.10.2026): neue Stile
MUL = 'style="mix-blend-mode:multiply"'


# ---------------------------------------------------------------- Riso-Druck
def v11():
    """Riso-Druck: zwei Druckfarben (Gelb, Magenta), leicht versetzt übereinander gedruckt – grafisch, mit Charakter."""
    defs = f'<pattern id="hv11p" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><circle cx="3.5" cy="3.5" r="1.6" fill="{M}"/></pattern>'
    gelb = (r(56, 70, 250, 290, Y, 14) + f'<circle cx="330" cy="292" r="74" fill="{Y}"/>')
    mag = (f'<g transform="translate(9 -7)" {MUL}>'
           + r(56, 70, 250, 290, "none", 14, f'stroke="{M}" stroke-width="5"') + f'<path d="M56 112h250" stroke="{M}" stroke-width="5"/>'
           + f'<circle cx="80" cy="91" r="6" fill="{M}"/><circle cx="100" cy="91" r="6" fill="{M}"/>'
           + r(80, 134, 202, 70, M, 8) + r(80, 222, 150, 10, M, 5) + r(80, 242, 110, 10, M, 5)
           + r(80, 272, 92, 62, "url(#hv11p)", 8) + r(190, 272, 92, 62, "url(#hv11p)", 8)
           + f'<circle cx="330" cy="292" r="74" fill="none" stroke="{M}" stroke-width="5"/><path d="M330 292V238M330 292l30 18" stroke="{M}" stroke-width="7" stroke-linecap="round"/>'
           + f'<path d="M330 210v-16M314 192h32" stroke="{M}" stroke-width="6" stroke-linecap="round"/></g>')
    return svg(f'''<g {MUL}>{gelb}</g>{mag}
{t(118, 176, "LIVE", 30, Y, 700, "start", SANS, 'letter-spacing="4"')}
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
<path d="{bogen(182, 356, R)}" fill="none" stroke="{Y}" stroke-width="26" stroke-linecap="round"/>
{striche}
{t(cx, 38, "0 h", 11, K, 700, "middle")}{t(cx, 368, "24 h", 11, K, 700, "middle")}
{t(372, 150, "TAG 1", 11, M, 700)}{t(372, 166, "Sparring &amp;", 10, K, 500)}{t(372, 180, "Rohversion", 10, K, 500)}
{t(68, 214, "TAG 2", 11, K, 700, "end")}{t(68, 230, "Feinschliff", 10, K, 500, "end")}{t(68, 244, "&amp; Go-live", 10, K, 500, "end")}
{r(184, 124, 72, 140, W, 14, f'stroke="{K}" stroke-width="4"')}{r(194, 140, 52, 32, M, 6)}{r(194, 182, 42, 6, K, 3)}{r(194, 194, 30, 6, G3, 3)}{r(194, 234, 36, 14, K, 7)}
<circle cx="{cx - 8}" cy="{cy - R}" r="13" fill="{K}"/><path d="M{cx-13} {cy-R}l4 4 7-8" fill="none" stroke="{Y}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
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
            k += r(x, y, 116, 116, M, 18) + t(x + 58, y + 68, "48h", 34, W, 700, "middle", SERIF) + t(x + 58, y + 92, "SPRINT", 9, W, 700, "middle", SANS, 'letter-spacing="2"')
        else:
            k += r(x, y, 116, 116, G, 18) + f'<g transform="translate({x+58} {y+50})">{PIKTO[n].format(c=K)}</g>' + t(x + 58, y + 100, n, 9, K, 700, "middle", SANS, 'letter-spacing="1.4"')
    return svg(k, "Neun Bausteine des Sprints als Piktogramme")


# ---------------------------------------------------------------- Fortschrittskurve
def v14():
    """Datengrafik: Fortschritt über 48 Stunden als Kurve mit Meilensteinen – wirkt analytisch, wie ein Chart."""
    X0, Y0, X1, Y1 = 58, 320, 410, 70   # Achsen
    px = lambda h: X0 + (X1 - X0) * h / 48
    py = lambda v: Y0 - (Y0 - Y1) * v / 100
    kurve = f"M{px(0)} {py(0)}C{px(10)} {py(4)} {px(14)} {py(38)} {px(24)} {py(58)}S{px(38)} {py(86)} {px(48)} {py(100)}"
    ms = [(0, 0, "Briefing"), (18, 46, "Rohversion"), (32, 76, "Feedback"), (48, 100, "Live")]
    gitter = "".join(f'<path d="M{X0} {py(v)}H{X1}" stroke="{G2}" stroke-width="1.5"/>' + t(X0 - 10, py(v) + 4, f"{v}%", 10, "#8a847c", 600, "end") for v in (0, 50, 100))
    xs = "".join(t(px(h), Y0 + 22, f"{h}h", 10, "#8a847c", 600, "middle") for h in (0, 12, 24, 36, 48))
    punkte = "".join(f'<circle cx="{px(h)}" cy="{py(v)}" r="7" fill="{W}" stroke="{K}" stroke-width="3"/>' + t(px(h) + (12 if h == 0 else -12), py(v) - 12, n, 11, K, 700, "start" if h == 0 else "end") for h, v, n in ms)
    return svg(f'''
{gitter}{xs}
<path d="{kurve}L{px(48)} {Y0}L{px(0)} {Y0}z" fill="{M3}"/>
<path d="{kurve}" fill="none" stroke="{M}" stroke-width="5" stroke-linecap="round"/>
<path d="M{X0} {Y0}H{X1}" stroke="{K}" stroke-width="2.5"/>
<path d="M{px(24)} {Y1 - 6}V{Y0}" stroke="{K}" stroke-width="1.5" stroke-dasharray="4 5"/>{t(px(24) - 6, Y1 + 4, "Tag 2", 10, "#8a847c", 600, "end")}
{punkte}
{r(X0, 352, 150, 30, K, 15)}{t(X0 + 75, 372, "fertig in 48 Stunden", 11, W, 600, "middle")}
''', "Fortschritt über 48 Stunden als Kurve")


# ---------------------------------------------------------------- Szene
def v15():
    """Szene in Linien: Zwei Tage vor Ort – Beraterin, Kunde, Laptop, an der Wand entsteht die Seite."""
    def person(x, y, fill, s=1):
        return (f'<g transform="translate({x} {y}) scale({s})"><path d="M-34 0v-16c0-20 15-32 34-32s34 12 34 32V0z" fill="{fill}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/>'
                f'<circle cy="-66" r="18" fill="{W}" stroke="{K}" stroke-width="4"/></g>')
    return svg(f'''
<circle cx="250" cy="110" r="96" fill="{M3}"/>
{r(150, 30, 220, 150, W, 12, f'stroke="{K}" stroke-width="4"')}<path d="M150 56h220" stroke="{K}" stroke-width="4"/>
{r(170, 72, 180, 46, M, 6)}{r(184, 86, 90, 8, W, 4)}{r(184, 100, 60, 6, W, 3)}
{r(170, 130, 82, 34, "none", 6, f'stroke="{K}" stroke-width="2.5" stroke-dasharray="5 5"')}{r(266, 130, 84, 34, G, 6, f'stroke="{K}" stroke-width="2.5"')}
<path d="M260 180v18" stroke="{K}" stroke-width="4"/>
{person(110, 300, Y)}{person(330, 300, W)}
<path d="M30 300h380" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
<path d="M60 300l-12 80M380 300l12 80" stroke="{K}" stroke-width="4" stroke-linecap="round"/>
<path d="M176 298l12-52h86l-10 52z" fill="{W}" stroke="{K}" stroke-width="4" stroke-linejoin="round"/><circle cx="226" cy="272" r="5" fill="{K}"/>
{r(126, 210, 54, 34, W, 17, f'stroke="{K}" stroke-width="3"')}<path d="M140 244l-6 10 14-10" fill="{W}" stroke="{K}" stroke-width="3" stroke-linejoin="round"/>{r(138, 222, 30, 5, K, 2.5)}{r(138, 232, 20, 5, G3, 2.5)}
{r(330, 330, 84, 30, K, 15)}{t(372, 350, "TAG 2", 11, W, 700, "middle")}
''', "Zwei Tage vor Ort: gemeinsam entsteht die Landingpage")


VARIANTEN = [
    (v2, "Isometrisch", "Die Seite als Platten, die zusammengesetzt werden. Räumlich, aber nicht realistisch.", "mittel", "mittel", False),
    (v3, "Bauplan", "Wireframe mit Beschriftung und Maßlinie – jetzt frei auf Weiß, ohne Karopapier.", "hoch", "viele", False),
    (v4, "Duoton Magenta", "Nur Magenta-Töne, Desktop und Handy – jetzt ohne gepunkteten Kreis.", "mittel", "mittel", False),
    (v5, "Prozess-Infografik", "Die drei Etappen des Sprints auf einer Zeitachse – erklärt den Ablauf.", "hoch", "viele", False),
    (v7, "Typografisch", "Die Zahl ist das Bild. Lora in groß, ein Handy als Akzent.", "niedrig", "sehr wenige", False),
    (v11, "Riso-Druck", "Zwei Druckfarben leicht versetzt übereinander – grafisch, mit Charakter, ohne Schwarz.", "mittel", "mittel", True),
    (v12, "Uhr-Infografik", "Die 48 Stunden als Ring: Tag 1 Sparring & Rohversion, Tag 2 Feinschliff & Go-live.", "hoch", "mittel", True),
    (v13, "Piktogramm-System", "Neun Kacheln, jede ein Baustein des Sprints. Modular, sachlich, gut auf andere Seiten übertragbar.", "mittel", "viele", True),
    (v14, "Fortschrittskurve", "Fortschritt über 48 Stunden als Chart mit Meilensteinen. Analytisch.", "mittel", "mittel", True),
    (v15, "Szene in Linien", "Zwei Tage vor Ort: Menschen am Tisch, an der Wand entsteht die Seite.", "mittel", "mittel", True),
]

NEU = '<span class="hv-chip hv-chip--neu">neu</span>'

CSS = """<style>
.hv-intro { padding: 4.5rem 0 1rem; }
.hv-intro h1 { font-family: var(--font-serif); font-size: clamp(2.4rem, 5vw, 3.6rem); line-height: 1.15; }
.hv-intro p { max-width: 44rem; margin-top: 1.2rem !important; font-size: 1.1rem; line-height: 1.6; color: #3d3a37; }
.hv-index { display: flex; flex-wrap: wrap; gap: .5rem; margin-top: 1.6rem; }
.hv-index a { padding: .4rem .85rem; border: 1px solid #e7e4df; border-radius: 999px; font-size: .85rem; font-weight: 600; color: #1a1817; text-decoration: none; }
.hv-index a:hover { background: #f4f3f0; }
.hv-var { border-top: 1px solid #e7e4df; scroll-margin-top: 90px; }
.hv-band { display: flex; flex-wrap: wrap; align-items: center; gap: .6rem 1rem; padding-top: 2.4rem; }
.hv-nr { display: grid; place-items: center; width: 2.6rem; height: 2.6rem; border-radius: 10px; background: #1a1817; color: #fff; font-family: var(--font-serif); font-weight: 700; }
.hv-name { font-family: var(--font-serif); font-weight: 700; font-size: 1.5rem; }
.hv-chip { padding: .25rem .7rem; border-radius: 999px; background: #f4f3f0; font-size: .8rem; font-weight: 600; color: #3d3a37; }
.hv-chip--neu { background: #C51F5D; color: #fff; }
.hv-text { flex-basis: 100%; margin: .2rem 0 0 3.6rem; color: #6f6a64; font-size: .98rem; }
.hv-var .e2-kopf { padding-top: 2.6rem; }
.hv-bild { display: block; width: 100%; height: auto; }
@media (max-width: 600px) { .hv-chip--neu { background: #C51F5D; color: #fff; }
.hv-text { margin-left: 0; } }
</style>"""


def main():
    h = QUELLE.read_text(encoding="utf-8")
    kopf = re.search(r'<section class="e2-kopf" id="intro">.*?</section>', h, re.S).group(0)
    bild_alt = re.search(r'<svg class="e2-bild".*?</svg>', kopf, re.S).group(0)
    a, b = h.index("<main>"), h.index("</main>") + 7
    teile = []
    for i, (f, name, text, detail, menge, neu) in enumerate(VARIANTEN, 1):
        k = kopf.replace(bild_alt, f()).replace('id="intro"', f'id="kopf-{i}"')
        teile.append(f'<div class="hv-var" id="v{i}"><div class="e2-wrap"><div class="hv-band"><span class="hv-nr">{i}</span>'
                     f'<span class="hv-name">{name}</span><span class="hv-chip">Detailgrad: {detail}</span><span class="hv-chip">Elemente: {menge}</span>{NEU if neu else ""}'
                     f'<p class="hv-text">{text}</p></div></div>{k}</div>')
    links = "".join(f'<a href="#v{i}">{i} · {v[1]}</a>' for i, v in enumerate(VARIANTEN, 1))
    intro = (f'<section class="hv-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Header</p>'
             f'<h1>Header-Stile für „Sprint Landingpage“ · Runde 2</h1>'
             f'<p>Gleicher Text, gleiche Aufteilung – nur die Illustration rechts wechselt. Fünf Stile aus Runde 1 sind geblieben (Bauplan und Duoton bereinigt), fünf sind neu. Die Stile unterscheiden sich bewusst stark in Bildsprache, '
             f'Detailgrad und Anzahl der Elemente. Wähle aus, was zu empiria passt; danach übertragen wir den Stil auf alle Seiten.</p>'
             f'<div class="hv-index">{links}</div></div></section>')
    seite = h[:a] + "<main>\n" + CSS + '<div class="e2-alt e2-alt--magenta e2-seite--sprint-landingpage">' + intro + "".join(teile) + "</div>\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Header-Varianten · Sprint Landingpage · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent))


if __name__ == "__main__":
    main()
