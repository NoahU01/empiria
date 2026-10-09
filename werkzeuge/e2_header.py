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


# ---------------------------------------------------------------- 1 · Flächig
def v1():
    """Reine Flächen, keine Linien – Seite aus Blöcken, die Zeit als großer Kreis."""
    return svg(f'''
<circle cx="300" cy="150" r="118" fill="{M}"/>
<path d="M300 150V32A118 118 0 0 1 402 91z" fill="{W}" opacity=".9"/>
{r(60, 96, 190, 270, G2, 18)}
{r(80, 118, 70, 12, K, 6)}{r(196, 118, 34, 12, K, 6)}
{r(80, 150, 150, 86, Y, 12)}
{r(80, 252, 44, 44, K, 10)}{r(133, 252, 44, 44, W, 10)}{r(186, 252, 44, 44, W, 10)}
{r(80, 316, 90, 28, M, 14)}
{t(334, 232, "48h", 40, W, 700, "middle", SERIF)}
''', "Flächig: Landingpage aus Blöcken, Zeit als Kreis")


# ---------------------------------------------------------------- 2 · Isometrisch
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
    raster = "".join(f'<path d="M{x} 0v400" stroke="#ebe7e1" stroke-width="1"/>' for x in range(0, 441, 20)) + \
             "".join(f'<path d="M0 {y}h440" stroke="#ebe7e1" stroke-width="1"/>' for y in range(0, 401, 20))
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
{r(14, 14, 412, 372, "#faf9f6", 16)}<g opacity=".9">{raster}</g>{r(14, 14, 412, 372, "none", 16, f'stroke="{G2}" stroke-width="2"')}
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
<circle cx="230" cy="200" r="168" fill="{M3}"/>
<circle cx="230" cy="200" r="168" fill="url(#hv4p)" opacity=".18"/>
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


# ---------------------------------------------------------------- 6 · Papier
OP45 = 'opacity=".45"'


def v6():
    """Papier & Schatten: Zettel aus dem Workshop werden zur fertigen Seite – haptisch, aber ruhig."""
    defs = '<filter id="hv6s" x="-20%" y="-20%" width="140%" height="150%"><feDropShadow dx="0" dy="8" stdDeviation="8" flood-color="#1a1817" flood-opacity=".16"/></filter>'
    z = lambda x, y, c, rot: f'<g transform="rotate({rot} {x+34} {y+32})" filter="url(#hv6s)">{r(x, y, 68, 64, c, 4)}{r(x+10, y+16, 44, 5, K, 2.5, OP45)}{r(x+10, y+28, 34, 5, K, 2.5, OP45)}</g>'
    return svg(f'''
{z(26, 60, Y, -8)}{z(70, 140, M3, 6)}{z(20, 226, W, -4)}{z(96, 300, Y, 9)}
<path d="M120 120c40-6 60 0 80 20" fill="none" stroke="{K}" stroke-width="2.5" stroke-dasharray="3 7" stroke-linecap="round"/>
<g transform="rotate(2 300 210)" filter="url(#hv6s)">{r(196, 40, 214, 320, W, 10)}
{r(214, 60, 60, 8, K, 4)}{r(214, 84, 176, 92, M, 8)}{r(228, 106, 110, 10, W, 5)}{r(228, 124, 76, 7, W, 3.5, 'opacity=".8"')}{r(228, 146, 52, 18, W, 9)}
{r(214, 194, 150, 8, K, 4)}{r(214, 210, 120, 6, G3, 3)}
{r(214, 232, 54, 46, G, 6)}{r(275, 232, 54, 46, G, 6)}{r(336, 232, 54, 46, G, 6)}
{r(214, 298, 176, 40, Y, 8)}{r(228, 312, 90, 8, K, 4)}</g>
<g transform="rotate(-24 312 46)">{r(282, 36, 60, 18, "#fff7a8", 2, 'opacity=".85"')}</g>
''', "Papier: Workshop-Zettel werden zur Landingpage", defs)


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


# ---------------------------------------------------------------- 8 · Geräte
def v8():
    """Klare UI-Darstellung: echte Seite auf Laptop und Handy, dazu der erste Erfolg – am konkretesten."""
    defs = '<filter id="hv8s" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="10" flood-color="#1a1817" flood-opacity=".18"/></filter>'
    return svg(f'''
<g filter="url(#hv8s)">{r(28, 52, 330, 214, K, 14)}{r(38, 62, 310, 194, W, 6)}</g>
<path d="M8 276h370l-18 16H26z" fill="{G2}"/>
{r(52, 74, 46, 8, K, 4)}{r(250, 74, 26, 6, G3, 3)}{r(282, 74, 26, 6, G3, 3)}<rect x="314" y="70" width="26" height="14" rx="7" fill="{M}"/>
{r(52, 102, 150, 14, K, 3)}{r(52, 122, 98, 14, Y, 3)}{r(56, 125, 88, 8, K, 2, 'opacity=".9"')}
{r(52, 148, 140, 6, G3, 3)}{r(52, 160, 120, 6, G3, 3)}
<rect x="52" y="180" width="86" height="24" rx="12" fill="{M}"/>{t(95, 196, "Termin sichern", 8.5, W, 600, "middle")}
<defs><linearGradient id="hv8g" x1="0" y1="0" x2="1" y2="1"><stop offset="0" stop-color="{M}"/><stop offset="1" stop-color="{V}"/></linearGradient></defs>
{r(214, 100, 120, 104, "url(#hv8g)", 10)}<circle cx="274" cy="142" r="18" fill="{W}" opacity=".25"/><path d="M234 190l30-30 22 18 18-14 30 26z" fill="{W}" opacity=".35"/>
{r(52, 222, 88, 22, G, 6)}{r(148, 222, 88, 22, G, 6)}{r(244, 222, 88, 22, G, 6)}
<g filter="url(#hv8s)">{r(318, 150, 104, 200, K, 18)}{r(324, 156, 92, 188, W, 13)}</g>
{r(334, 172, 40, 6, K, 3)}{r(334, 188, 70, 10, K, 3)}{r(334, 202, 50, 10, Y, 3)}{r(334, 222, 72, 50, "url(#hv8g)", 6)}{r(334, 282, 60, 5, G3, 2.5)}{r(334, 292, 48, 5, G3, 2.5)}<rect x="334" y="306" width="56" height="18" rx="9" fill="{M}"/>
<g filter="url(#hv8s)">{r(120, 300, 186, 56, W, 14)}</g>
<circle cx="146" cy="328" r="13" fill="{Y}"/><path d="M140 328l4 4 8-9" fill="none" stroke="{K}" stroke-width="2.6" stroke-linecap="round" stroke-linejoin="round"/>
{t(168, 324, "Neue Anfrage", 12, K, 700)}{t(168, 340, "über Deine Landingpage", 10, "#6f6a64", 500)}
''', "Landingpage auf Laptop und Handy, erste Anfrage", defs)


# ---------------------------------------------------------------- 9 · Dunkle Bühne
def v9():
    """Dunkle Bühne: helle Linien auf Schwarz, Magenta und Gelb leuchten – wirkt hochwertig, eher technisch."""
    defs = '<filter id="hv9g" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="6" result="b"/><feMerge><feMergeNode in="b"/><feMergeNode in="SourceGraphic"/></feMerge></filter>'
    L = 'fill="none" stroke="#f4f3f0" stroke-width="2.4" stroke-linecap="round" stroke-linejoin="round"'
    return svg(f'''
{r(10, 10, 420, 380, K, 26)}
<g opacity=".08">{"".join(f'<circle cx="{x}" cy="{y}" r="1.4" fill="#fff"/>' for x in range(30, 430, 24) for y in range(30, 390, 24))}</g>
<rect x="56" y="66" width="200" height="270" rx="12" {L}/><path d="M56 96h200" {L}/>
<rect x="74" y="114" width="164" height="60" rx="8" fill="none" stroke="{M}" stroke-width="3" filter="url(#hv9g)"/>
<path d="M88 136h96M88 152h60" {L}/><path d="M74 196h140M74 212h100" {L} opacity=".6"/>
<rect x="74" y="236" width="74" height="44" rx="6" {L} opacity=".6"/><rect x="164" y="236" width="74" height="44" rx="6" {L} opacity=".6"/>
<rect x="74" y="298" width="80" height="22" rx="11" fill="{M}" filter="url(#hv9g)"/>
<circle cx="320" cy="170" r="74" fill="none" stroke="#3a3735" stroke-width="10"/>
<circle cx="320" cy="170" r="74" fill="none" stroke="{Y}" stroke-width="10" stroke-linecap="round" stroke-dasharray="420 465" transform="rotate(-90 320 170)" filter="url(#hv9g)"/>
{t(320, 168, "48:00", 30, W, 600, "middle")}{t(320, 192, "STUNDEN BIS LIVE", 9, "#bdb7af", 700, "middle", SANS, 'letter-spacing="2"')}
<circle cx="296" cy="300" r="6" fill="{M}" filter="url(#hv9g)"/>{t(310, 305, "LIVE", 14, W, 700)}
''', "Dunkle Bühne: Countdown bis zum Go-live", defs)


# ---------------------------------------------------------------- 10 · Fokus
def v10():
    """Konzeptbild: aus dem Sammelsurium einer Homepage wird eine fokussierte Seite – erklärt das Prinzip."""
    streu = [(40, 70, "r"), (92, 52, "c"), (60, 120, "l"), (118, 100, "r"), (30, 170, "c"), (86, 166, "l"), (130, 150, "r"), (50, 226, "l"), (104, 214, "c"), (36, 280, "r"), (90, 272, "l"), (138, 252, "r"), (70, 330, "c"), (124, 312, "l")]
    def e(x, y, k):
        if k == "r": return r(x, y, 30, 22, G2, 4, f'stroke="{G3}" stroke-width="2"')
        if k == "c": return f'<circle cx="{x+12}" cy="{y+12}" r="12" fill="{G2}" stroke="{G3}" stroke-width="2"/>'
        return r(x, y + 8, 40, 7, G3, 3.5)
    return svg(f'''
{"".join(e(*s) for s in streu)}
<path d="M176 60C214 130 226 170 232 200C226 230 214 270 176 340" fill="none" stroke="{K}" stroke-width="3" stroke-linecap="round"/>
<path d="M176 60L232 200L176 340" fill="{G}" opacity=".6"/>
<path d="M234 200h22" stroke="{K}" stroke-width="3" stroke-linecap="round"/><path d="M250 192l10 8-10 8" fill="none" stroke="{K}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{r(276, 66, 140, 268, W, 18, f'stroke="{K}" stroke-width="4"')}
{r(292, 92, 108, 74, M, 10)}{r(304, 110, 70, 9, W, 4.5)}{r(304, 126, 48, 7, W, 3.5, 'opacity=".8"')}
{r(292, 182, 96, 8, K, 4)}{r(292, 198, 76, 7, G3, 3.5)}{r(292, 212, 86, 7, G3, 3.5)}
<rect x="292" y="250" width="108" height="34" rx="17" fill="{K}"/>{t(346, 271, "1 Ziel", 12, W, 700, "middle")}
{t(110, 376, "Homepage: alles", 11, "#8a847c", 600, "middle")}{t(346, 360, "Landingpage: eins", 11, K, 700, "middle")}
''', "Fokus: von vielen Themen zu einem klaren Ziel")


VARIANTEN = [
    (v1, "Flächig", "Nur Farbflächen, keine Linien. Ruhig, grafisch, sehr reduziert.", "niedrig", "wenige"),
    (v2, "Isometrisch", "Die Seite als Platten, die zusammengesetzt werden. Räumlich, aber nicht realistisch.", "mittel", "mittel"),
    (v3, "Bauplan", "Wireframe mit Beschriftung und Maßlinie. Fein, sachlich, viel Information.", "hoch", "viele"),
    (v4, "Duoton Magenta", "Nur Magenta-Töne mit Rasterpunkten. Desktop und Handy.", "mittel", "mittel"),
    (v5, "Prozess-Infografik", "Die drei Etappen des Sprints auf einer Zeitachse – erklärt den Ablauf.", "hoch", "viele"),
    (v6, "Papier & Schatten", "Workshop-Zettel werden zur fertigen Seite. Haptisch, leicht gedreht.", "mittel", "mittel"),
    (v7, "Typografisch", "Die Zahl ist das Bild. Lora in groß, ein Handy als Akzent.", "niedrig", "sehr wenige"),
    (v8, "Geräte-UI", "Echte Seite auf Laptop und Handy, dazu die erste Anfrage. Am konkretesten.", "hoch", "viele"),
    (v9, "Dunkle Bühne", "Helle Linien auf Schwarz, Countdown leuchtet. Hochwertig, technisch.", "mittel", "mittel"),
    (v10, "Fokus-Prinzip", "Vom Sammelsurium der Homepage zur fokussierten Seite. Erklärt das Warum.", "mittel", "viele"),
]

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
.hv-text { flex-basis: 100%; margin: .2rem 0 0 3.6rem; color: #6f6a64; font-size: .98rem; }
.hv-var .e2-kopf { padding-top: 2.6rem; }
.hv-bild { display: block; width: 100%; height: auto; }
@media (max-width: 600px) { .hv-text { margin-left: 0; } }
</style>"""


def main():
    h = QUELLE.read_text(encoding="utf-8")
    kopf = re.search(r'<section class="e2-kopf" id="intro">.*?</section>', h, re.S).group(0)
    bild_alt = re.search(r'<svg class="e2-bild".*?</svg>', kopf, re.S).group(0)
    a, b = h.index("<main>"), h.index("</main>") + 7
    teile = []
    for i, (f, name, text, detail, menge) in enumerate(VARIANTEN, 1):
        k = kopf.replace(bild_alt, f()).replace('id="intro"', f'id="kopf-{i}"')
        teile.append(f'<div class="hv-var" id="v{i}"><div class="e2-wrap"><div class="hv-band"><span class="hv-nr">{i}</span>'
                     f'<span class="hv-name">{name}</span><span class="hv-chip">Detailgrad: {detail}</span><span class="hv-chip">Elemente: {menge}</span>'
                     f'<p class="hv-text">{text}</p></div></div>{k}</div>')
    links = "".join(f'<a href="#v{i}">{i} · {v[1]}</a>' for i, v in enumerate(VARIANTEN, 1))
    intro = (f'<section class="hv-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Header</p>'
             f'<h1>Zehn Stile für den Kopf von „Sprint Landingpage“</h1>'
             f'<p>Gleicher Text, gleiche Aufteilung – nur die Illustration rechts wechselt. Die Stile unterscheiden sich bewusst stark in Bildsprache, '
             f'Detailgrad und Anzahl der Elemente. Wähle aus, was zu empiria passt; danach übertragen wir den Stil auf alle Seiten.</p>'
             f'<div class="hv-index">{links}</div></div></section>')
    seite = h[:a] + "<main>\n" + CSS + '<div class="e2-alt e2-alt--magenta e2-seite--sprint-landingpage">' + intro + "".join(teile) + "</div>\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Header-Varianten · Sprint Landingpage · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent))


if __name__ == "__main__":
    main()
