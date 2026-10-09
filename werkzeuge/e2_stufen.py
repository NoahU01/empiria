"""Detaillierungsstufen je Seite (Daniel, 10.10.2026) – für die Entwicklungsseite „Header“.

Fachbegriffe aus der Illustration:
  1. Icon           – ein Zeichen, ein Gegenstand. Sofort lesbar, keine Umgebung.
  2. Spot-Illustration (Vignette) – ein kleiner Ausschnitt: zwei bis vier Dinge in Beziehung, freigestellt, ohne Raum.
  3. Szene (Hero-Illustration)    – eine ganze Situation mit Menschen, Raum und Handlung.
Alle drei Stufen sind hier bewusst in EINER Darstellungsart gezeichnet (dunkle Linie, weiße Flächen, Bereichsfarbe als Akzent),
damit nur die Detaillierung verglichen wird. Farben sind Platzhalter und werden je Bereich umgefärbt (e2_header.farbig).
"""
K, W, G, G2, G3 = "#1a1817", "#ffffff", "#f1efeb", "#e3dfd8", "#b9b3ab"
M, M2, M3, M4, MT, ON = "#C51F5D", "#e27fa3", "#f5d3df", "#7a1339", "#C51F5E", "#FEFEFE"
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"
SW = 3  # Linienstärke in Vignetten und Szenen
BODEN = 360


def svg(inhalt, label):
    return (f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" aria-label="{label}" font-family="{SANS}">{inhalt}</svg>')


# ---------------------------------------------------------------- Grundformen
def P(d, fill="none", sw=SW, stroke=K, extra=""):
    return f'<path d="{d}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round" {extra}/>'


def R(x, y, w, h, fill=W, rx=6, sw=SW, stroke=K, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def B(x, y, w, c=K, h=6, op=1):  # Balken (Textzeile)
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{c}" opacity="{op}"/>'


def C(cx, cy, r, fill=W, sw=SW, stroke=K):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'


def T(x, y, txt, size=12, fill=K, weight=700, anchor="middle", fam=SANS):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="{fam}">{txt}</text>'


def tupfer(cx, cy, r, c=M3):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'


def boden(y=BODEN):
    return f'<path d="M20 {y}H420" stroke="{G2}" stroke-width="4" stroke-linecap="round"/>'


# ---------------------------------------------------------------- Menschen
def steh(x, fy=BODEN, s=1.0, f=W, arm=None):
    k = lambda v: v * s
    a = ""
    if arm == "zeig":
        a = P(f"M{x+k(20)} {fy-k(106)}L{x+k(58)} {fy-k(132)}")
    elif arm == "zeig_l":
        a = P(f"M{x-k(20)} {fy-k(106)}L{x-k(58)} {fy-k(132)}")
    elif arm == "hoch":
        a = P(f"M{x+k(20)} {fy-k(106)}L{x+k(36)} {fy-k(152)}")
    return (P(f"M{x-k(10)} {fy-k(62)}V{fy}M{x+k(10)} {fy-k(62)}V{fy}")
            + P(f"M{x-k(22)} {fy-k(60)}L{x-k(24)} {fy-k(102)}Q{x-k(24)} {fy-k(120)} {x-k(8)} {fy-k(120)}H{x+k(8)}Q{x+k(24)} {fy-k(120)} {x+k(24)} {fy-k(102)}L{x+k(22)} {fy-k(60)}Z", f)
            + a + C(x, fy - k(138), k(14)))


def sitz(x, ty, s=1.0, f=W):
    k = lambda v: v * s
    return (P(f"M{x-k(28)} {ty}V{ty-k(14)}Q{x-k(28)} {ty-k(40)} {x} {ty-k(40)}Q{x+k(28)} {ty-k(40)} {x+k(28)} {ty-k(14)}V{ty}Z", f)
            + C(x, ty - k(58), k(15)))


# ---------------------------------------------------------------- Gegenstände
def tisch(x1, x2, y, fy=BODEN):
    return P(f"M{x1} {y}H{x2}", sw=4) + P(f"M{x1+14} {y}L{x1+6} {fy}M{x2-14} {y}L{x2-6} {fy}")


def browser(x, y, w, h, akzent=True, dicht=True):
    s = R(x, y, w, h, W, 8) + P(f"M{x} {y+h*.16}H{x+w}") + f'<circle cx="{x+10}" cy="{y+h*.08}" r="2.6" fill="{K}"/><circle cx="{x+19}" cy="{y+h*.08}" r="2.6" fill="{K}"/>'
    if dicht:
        s += f'<rect x="{x+w*.08}" y="{y+h*.26}" width="{w*.84}" height="{h*.28}" rx="4" fill="{M if akzent else G2}"/>'
        s += B(x + w * .08, y + h * .62, w * .55, K, max(3, h * .045)) + B(x + w * .08, y + h * .72, w * .4, G3, max(3, h * .04))
        s += f'<rect x="{x+w*.08}" y="{y+h*.82}" width="{w*.3}" height="{h*.09}" rx="{h*.045}" fill="{K}"/>'
    return s


def handy(x, y, w, h):
    return (R(x, y, w, h, W, w * .18) + f'<rect x="{x+w*.14}" y="{y+h*.12}" width="{w*.72}" height="{h*.3}" rx="3" fill="{M}"/>'
            + B(x + w * .14, y + h * .5, w * .6, K, 3.5) + B(x + w * .14, y + h * .58, w * .44, G3, 3.5)
            + f'<rect x="{x+w*.14}" y="{y+h*.74}" width="{w*.5}" height="{h*.08}" rx="{h*.04}" fill="{K}"/>')


def uhr(cx, cy, r, text=None):
    s = P(f"M{cx} {cy-r}v{-r*.22}M{cx-r*.25} {cy-r*1.24}h{r*.5}") + C(cx, cy, r) + P(f"M{cx} {cy}V{cy-r*.62}M{cx} {cy}l{r*.42} {r*.24}")
    if text:
        s += T(cx, cy + r * .66, text, r * .34, K, 700, "middle", SERIF)
    return s


def blase(x, y, w, h, links=True, f=W, zeilen=2):
    sx = x + w * .22 if links else x + w * .78
    d = -1 if links else 1
    s = R(x, y, w, h, f, h * .3) + P(f"M{sx} {y+h-1}l{d*-2} 14 {d*16}-14", f)
    for i in range(zeilen):
        s += B(x + w * .15, y + h * (.32 + i * .26), w * (.6 - i * .2), K if f != M else W, 4, .7)
    return s


def zettel(x, y, c, rot=0, w=36, h=32):
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})">' + R(x, y, w, h, c, 3, 2) + B(x + 7, y + 10, w - 14, K, 3.5, .5) + B(x + 7, y + 18, w - 20, K, 3.5, .5) + "</g>")


def laptop(x, y, w, inhalt=None):
    h = w * .62
    s = R(x, y, w, h, W, 6) + P(f"M{x-w*.08} {y+h+10}H{x+w*1.08}L{x+w} {y+h}H{x}Z", G)
    s += inhalt if inhalt else (f'<rect x="{x+w*.1}" y="{y+h*.15}" width="{w*.8}" height="{h*.32}" rx="3" fill="{M}"/>' + B(x + w * .1, y + h * .6, w * .6, K, 4) + B(x + w * .1, y + h * .74, w * .4, G3, 4))
    return s


def tafel(x, y, w, h, beine=True):
    s = ""
    if beine:
        s += P(f"M{x+w*.2} {y+h}L{x+w*.12} {BODEN}M{x+w*.8} {y+h}L{x+w*.88} {BODEN}")
    return s + R(x, y, w, h, W, 6)


def folie(x, y, w, h, akzent=True):
    return (R(x, y, w, h, W, 4) + B(x + w * .1, y + h * .14, w * .5, K, max(4, h * .07))
            + f'<rect x="{x+w*.1}" y="{y+h*.36}" width="{w*.36}" height="{h*.46}" rx="3" fill="{M if akzent else G2}"/>'
            + B(x + w * .54, y + h * .4, w * .34, G3, 4) + B(x + w * .54, y + h * .54, w * .28, G3, 4))


def balken(x, y, w, h, n=4):
    s = R(x, y, w, h, W, 6)
    bw = w / (n * 2 + 1)
    for i, hh in enumerate([.35, .55, .45, .8, .65, .9][:n]):
        s += f'<rect x="{x+bw*(1+2*i)}" y="{y+h*(.88-hh*.7)}" width="{bw}" height="{h*hh*.7}" rx="2" fill="{M if i == n-1 else K}"/>'
    return s


def pflanze(x, fy=BODEN):
    return (P(f"M{x-14} {fy-30}h28l-4 30h-20z", G) + P(f"M{x} {fy-30}c-2-24-18-30-24-46M{x} {fy-30}c4-20 14-34 26-40M{x} {fy-30}c0-18-4-34 0-52", "none", 2.6))


def fenster(x, y, w, h):
    return R(x, y, w, h, G, 4) + P(f"M{x+w/2} {y}V{y+h}M{x} {y+h/2}H{x+w}", "none", 2)


def stern(cx, cy, r, f=M):
    import math
    pts = " ".join(f"{cx + (r if i % 2 == 0 else r*.45) * math.cos(math.radians(i*36-90)):.1f},{cy + (r if i % 2 == 0 else r*.45) * math.sin(math.radians(i*36-90)):.1f}" for i in range(10))
    return f'<polygon points="{pts}" fill="{f}" stroke="{K}" stroke-width="{SW}" stroke-linejoin="round"/>'


def ziel(cx, cy, r):
    return C(cx, cy, r) + C(cx, cy, r * .62) + C(cx, cy, r * .26, M)


def flagge(x, y, h, f=M):
    return P(f"M{x} {y+h}V{y}") + P(f"M{x} {y+2}h{h*.5}l-{h*.1} {h*.16} {h*.1} {h*.16}H{x}", f)


def birne(cx, cy, r, f=M3):
    return (P(f"M{cx-r*.45} {cy+r*1.05}h{r*.9}M{cx-r*.3} {cy+r*1.3}h{r*.6}")
            + P(f"M{cx} {cy-r}a{r} {r} 0 0 0-{r*.6} {r*1.8}V{cy+r*.85}h{r*1.2}V{cy+r*.8}A{r} {r} 0 0 0 {cx} {cy-r}z", f))


def megafon(x, y, s=1.0, f=M):
    k = lambda v: v * s
    return (P(f"M{x} {y+k(18)}v{k(24)}h{k(18)}l{k(46)} {k(26)}V{y-k(8)}l-{k(46)} {k(26)}z", f)
            + P(f"M{x+k(18)} {y+k(42)}l{k(6)} {k(26)}h{k(14)}l-{k(4)}-{k(26)}")
            + P(f"M{x+k(78)} {y+k(16)}a{k(16)} {k(16)} 0 0 1 0 {k(28)}M{x+k(88)} {y+k(4)}a{k(30)} {k(30)} 0 0 1 0 {k(52)}"))


def rollup(x, y, w, h):
    return (R(x, y, w, h, W, 3) + f'<rect x="{x+w*.12}" y="{y+h*.1}" width="{w*.76}" height="{h*.06}" rx="2" fill="{K}"/>'
            + f'<rect x="{x+w*.12}" y="{y+h*.24}" width="{w*.76}" height="{h*.34}" rx="3" fill="{M}"/>'
            + B(x + w * .12, y + h * .66, w * .6, G3, 4) + B(x + w * .12, y + h * .74, w * .45, G3, 4)
            + P(f"M{x-6} {y+h}h{w+12}v8h-{w+12}z", G))


def mikro(x, fy=BODEN, h=150):
    return P(f"M{x} {fy}V{fy-h}M{x-22} {fy}h44") + P(f"M{x} {fy-h}l14-18") + R(x + 6, fy - h - 40, 18, 28, K, 9, 2)


def play(cx, cy, r, f=M):
    return C(cx, cy, r, f) + f'<path d="M{cx-r*.28} {cy-r*.42}L{cx+r*.46} {cy}L{cx-r*.28} {cy+r*.42}z" fill="{W}"/>'


def stuhl(x, fy=BODEN, links=True):
    d = 1 if links else -1
    return P(f"M{x} {fy}V{fy-50}h{d*44}V{fy}M{x} {fy-50}V{fy-110}", "none")


def tasse(x, y):
    return P(f"M{x} {y}h22v16a8 8 0 0 1-8 8h-6a8 8 0 0 1-8-8z", W) + P(f"M{x+22} {y+4}a6 6 0 0 1 0 12")


def doku(x, y, w, h, akzent=False):
    return R(x, y, w, h, W, 4) + B(x + w * .14, y + h * .14, w * .6, K, 5) + "".join(B(x + w * .14, y + h * (.32 + i * .12), w * (.72 - (i % 2) * .2), G3, 4) for i in range(4)) + (f'<rect x="{x+w*.14}" y="{y+h*.82}" width="{w*.4}" height="{h*.08}" rx="2" fill="{M}"/>' if akzent else "")


def pfeil(x1, y1, x2, y2, gestrichelt=True):
    import math
    a = math.atan2(y2 - y1, x2 - x1)
    l, b = 12, .5
    p1 = (x2 - l * math.cos(a - b), y2 - l * math.sin(a - b)); p2 = (x2 - l * math.cos(a + b), y2 - l * math.sin(a + b))
    dash = ' stroke-dasharray="2 9"' if gestrichelt else ""
    return (f'<path d="M{x1} {y1}L{x2} {y2}" stroke="{K}" stroke-width="{SW}" stroke-linecap="round"{dash}/>'
            + P(f"M{p1[0]:.1f} {p1[1]:.1f}L{x2} {y2}L{p2[0]:.1f} {p2[1]:.1f}"))


def doppelpfeil(x, y, s=1.0, c=K):
    return P(f"M{x} {y}l{14*s} {14*s}-{14*s} {14*s}M{x+16*s} {y}l{14*s} {14*s}-{14*s} {14*s}", "none", SW + 1.5, c)


def icon(inhalt, label):
    """Stufe 1: ein Zeichen, groß, mit Bereichsfarbe als ruhigem Kreis dahinter."""
    return svg(tupfer(220, 200, 128) + inhalt, label)


# ================================================================ je Seite: (Icon, Vignette, Szene)
def startseite():
    i = icon(ziel(212, 210, 92) + P("M250 172l70-70", "none", 7) + P("M300 96h26v26", "none", 7) + doppelpfeil(150, 92, 1.4), "Wirkung")
    v = svg(tupfer(230, 210, 150)
            + doku(40, 110, 110, 150) + pfeil(166, 186, 214, 186)
            + R(226, 120, 150, 130, W, 10) + "".join(R(240 + c * 44, 136 + r * 52, 34, 40, G2 if (r, c) != (0, 1) else M, 4, 2.5) for r in (0, 1) for c in (0, 1, 2))
            + T(300, 286, "EINORDNEN", 12) + T(95, 286, "STRATEGIE", 12) + flagge(390, 70, 70), "Strategie wird eingeordnet und wirkt")
    s = svg(boden() + fenster(300, 40, 100, 80)
            + tafel(56, 70, 210, 150) + "".join(R(72 + c * 64, 88 + r * 62, 52, 50, M if (r, c) == (0, 2) else G, 4, 2.5) for r in (0, 1) for c in (0, 1, 2))
            + steh(296, BODEN, 1, M, "zeig_l") + steh(380, BODEN, .92, W) + pflanze(30) + doppelpfeil(330, 150, .9), "Führungskraft und Berater ordnen das Geschäftsmodell")
    return i, v, s


def strategie():
    i = icon(P("M120 330C170 260 250 290 300 200", "none", 7, K, 'stroke-dasharray="3 16"') + flagge(296, 90, 120), "Ziel im Alltag")
    karten = "".join(R(250, 70 + j * 62, 160, 48, f, 24) + P(f"M270 {94+j*62}l7 7 13-14", "none", 4) + T(300, 99 + j * 62, t, 12, K, 700, "start")
                     for j, (t, f) in enumerate((("ROLLE", W), ("RICHTUNG", M), ("WERKZEUG", W))))
    v = svg(tupfer(110, 170, 90) + doku(50, 80, 120, 160) + doppelpfeil(186, 146, 1.2) + karten + T(110, 270, "STRATEGIE", 12), "Strategie wird zu Rolle, Richtung, Werkzeug")
    s = svg(boden() + tafel(40, 50, 200, 150) + browser(56, 64, 168, 122, True)
            + T(140, 222, "UNSERE ABTEILUNG", 10) + steh(270, BODEN, 1, M, "zeig_l") + tisch(300, 430, 280, BODEN)
            + sitz(330, 280, .8) + sitz(392, 280, .8, M3), "Führungskraft erklärt dem Team das Zielbild")
    return i, v, s


def komplexe():
    i = icon(P("M96 230c30-60 70 20 40 40s-30-70 20-60 40 60 10 60", "none", 7) + pfeil(196, 214, 330, 214, False).replace(f'stroke-width="{SW}"', 'stroke-width="7"'), "Aus Wirrwarr wird eine Linie")
    stapel = "".join(f'<g transform="rotate({r} {x+60} {y+40})">{folie(x, y, 120, 80, False)}</g>' for x, y, r in ((40, 190, -8), (54, 160, 6), (36, 128, -3)))
    v = svg(stapel + pfeil(180, 190, 226, 190) + tupfer(320, 180, 96) + folie(244, 120, 160, 110) + ziel(380, 270, 26) + T(324, 330, "EINE BOTSCHAFT", 12), "Vom Folienstapel zur einen Botschaft")
    s = svg(boden() + R(40, 40, 190, 120, W, 4) + folie(52, 52, 166, 96)
            + steh(260, BODEN, 1, M, "zeig_l") + tisch(290, 430, 270) + sitz(326, 270, .8) + sitz(388, 270, .8, M3)
            + C(400, 160, 16, W, 2.5) + P("M392 160l6 6 10-11", "none", 3), "Präsentation vor Entscheidern, die zustimmen")
    return i, v, s


def innovation():
    i = icon(birne(220, 186, 80, W) + P("M200 300h40", "none", 6) + C(220, 186, 30, M, 0), "Neu denken")
    v = svg(P("M40 330V160c0-40 30-64 70-64s70 24 70 64v170z", G) + P("M118 100l-12 40 16 24-12 30 14 26-8 26", "none") + T(110, 360, "GILT ALS GEGEBEN", 11)
            + tupfer(330, 230, 90) + "".join(R(x, y, 46, 46, f, 6) for x, y, f in ((270, 260, W), (318, 260, M), (366, 260, W), (294, 212, W), (342, 212, M3)))
            + R(330, 140, 46, 46, W, 6, SW, K, 'transform="rotate(14 353 163)"') + pfeil(354, 190, 356, 206, False), "Bausteine werden neu zusammengesetzt")
    s = svg(boden() + tafel(60, 50, 320, 170) + "".join(zettel(80 + (n % 6) * 48, 70 + (n // 6) * 46, [M3, W, M, W, G2, M3][n % 6], (n * 7) % 9 - 4) for n in range(12))
            + T(220, 205, "NEU GEGRÜNDET – OHNE ALTLASTEN", 10) + steh(110, BODEN, .9, W, "hoch") + steh(330, BODEN, .9, M, "zeig_l"), "Team denkt das Geschäftsmodell neu")
    return i, v, s


def teams():
    i = icon(R(150, 110, 150, 100, W, 8, 6) + P("M170 140h80M170 170h50", "none", 6) + steh(320, 330, 1.05, M, "zeig_l").replace(f'stroke-width="{SW}"', 'stroke-width="5"'), "Souverän präsentieren")
    v = svg(tupfer(220, 200, 140) + folie(130, 80, 200, 130) + steh(110, 360, .9, M, "zeig") + blase(300, 220, 110, 60, True, W) + P("M326 248l8 8 14-16", "none", 4) + T(220, 250, "STORY TRÄGT", 11), "Teammitglied präsentiert, Coach gibt Rückmeldung")
    s = svg(boden() + R(40, 40, 180, 110, W, 4) + folie(52, 52, 156, 86) + steh(250, BODEN, 1, M, "zeig_l") + tisch(280, 430, 270) + sitz(316, 270, .8) + sitz(386, 270, .8)
            + steh(60, BODEN, .8, M3) + blase(20, 150, 70, 40, False, W, 1) + T(55, 176, "✓", 18), "Team überzeugt im Vorstand, Coach im Hintergrund")
    return i, v, s


def workshops():
    i = icon(tafel(130, 90, 180, 130, False).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + P("M170 220l-18 70M270 220l18 70", "none", 6) + "".join(R(150 + n * 50, 112, 38, 34, c, 4, 0) for n, c in enumerate((M, K, M))) + P("M152 176h120M152 196h80", "none", 6), "Workshop-Board")
    v = svg(tupfer(220, 210, 150) + tafel(60, 70, 200, 150, False) + "".join(zettel(78 + (n % 3) * 58, 88 + (n // 3) * 56, [M, M3, W][n % 3], (n * 9) % 11 - 5, 44, 40) for n in range(6))
            + pfeil(274, 150, 304, 150) + R(314, 90, 96, 130, M, 8) + "".join(P(f"M330 {120+j*30}l6 6 11-12", "none", 4, W) + B(352, 117 + j * 30, 40, W, 6) for j in range(3)) + T(362, 250, "ERGEBNIS", 12), "Aus den Zetteln wird ein Ergebnis")
    s = svg(boden() + tafel(110, 40, 220, 140) + "".join(zettel(126 + (n % 4) * 50, 56 + (n // 4) * 52, [M, W, M3, W][n % 4], (n * 7) % 9 - 4, 40, 38) for n in range(8))
            + steh(70, BODEN, .95, M, "zeig") + tisch(150, 420, 290) + sitz(190, 290, .78) + sitz(260, 290, .78, M3) + sitz(330, 290, .78) + laptop(360, 250, 50), "Team arbeitet am Board, moderiert")
    return i, v, s


def ki():
    i = icon(blase(120, 120, 200, 130, True, W, 2).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + stern(320, 120, 40), "KI im Gespräch")
    v = svg(tupfer(200, 200, 150) + laptop(60, 110, 230, R(80, 128, 190, 28, G, 14, 2) + B(94, 139, 110, K, 5, .6) + R(120, 168, 150, 44, M, 12, 0) + B(134, 182, 100, W, 5) + B(134, 194, 70, W, 5, .8))
            + "".join(R(320, 90 + j * 66, 90, 52, f, 10) + T(365, 121 + j * 66, n, 11, c) for j, (n, f, c) in enumerate((("TOOL A", W, K), ("TOOL B", M, W), ("TOOL C", W, K)))) + stern(290, 104, 18), "Prompt, Antwort, drei Tools im Vergleich")
    s = svg(boden() + R(120, 36, 200, 120, W, 6) + "".join(R(134 + j * 62, 52, 54, 88, [W, M3, W][j], 4, 2.5) + T(161 + j * 62, 70, "ABC"[j], 11) for j in range(3))
            + tisch(40, 400, 280) + laptop(66, 238, 64) + laptop(190, 238, 64) + laptop(312, 238, 64) + sitz(98, 236, .7, M) + sitz(222, 236, .7) + sitz(344, 236, .7, M3) + stern(350, 50, 18), "Team probiert KI-Tools an echten Fällen")
    return i, v, s


def sprint():
    i = icon(browser(110, 100, 200, 160, True, False).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + P("M226 140l-34 50h28l-12 44 40-58h-28z", M, 5), "Landingpage im Sprint")
    v = svg(tupfer(200, 200, 150) + browser(40, 80, 240, 200) + handy(250, 160, 76, 140) + uhr(350, 110, 46, "48h"), "Seite, Handy und 48 Stunden")
    s = svg(boden() + tafel(40, 40, 200, 150, False) + browser(56, 54, 168, 122) + uhr(300, 90, 40, "48h")
            + tisch(120, 420, 290) + laptop(150, 250, 62) + sitz(181, 248, .78, M) + laptop(310, 250, 62) + sitz(341, 248, .78)
            + R(250, 150, 60, 26, K, 13, 0) + T(280, 168, "LIVE", 11, W) + steh(70, BODEN, .82, M3), "Zwei Tage vor Ort, die Seite geht live")
    return i, v, s


def moderation():
    i = icon(blase(110, 110, 170, 110, True, W, 2).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + blase(220, 180, 120, 80, False, M, 1).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Moderation")
    v = svg(tupfer(220, 200, 150) + tafel(60, 70, 230, 170, False) + "".join(zettel(76 + (n % 4) * 52, 88 + (n // 4) * 74, [M, M3, W, M3][n % 4], (n * 7) % 9 - 4, 42, 38) for n in range(8))
            + P("M70 170h210", "none", 2, K, 'stroke-dasharray="3 7"') + P("M300 260l50-80", "none", 6) + P("M346 186l10-18 6 4-10 18z", M, 2), "Moderator ordnet die Beiträge")
    s = svg(boden() + tafel(150, 40, 200, 140) + "".join(zettel(166 + (n % 4) * 46, 56 + (n // 4) * 56, [M, W, M3, W][n % 4], (n * 7) % 9 - 4, 36, 34) for n in range(8))
            + steh(110, BODEN, 1, M, "zeig") + sitz(200, 330, .74) + sitz(270, 330, .74, M3) + sitz(340, 330, .74) + blase(290, 200, 70, 40, False, W, 1), "Moderator führt durch den Workshop")
    return i, v, s


def marketing():
    i = icon(megafon(130, 170, 1.9, M), "Sichtbar werden")
    v = svg(tupfer(220, 200, 150) + handy(40, 110, 70, 126) + browser(130, 96, 120, 100) + R(130, 214, 120, 56, W, 8) + B(144, 232, 80, K, 5) + B(144, 246, 60, G3, 5)
            + pfeil(260, 180, 300, 180) + R(312, 132, 96, 96, M, 14) + P("M330 160h60v40h-60zM330 160l30 22 30-22", "none", 4, W) + T(360, 252, "ANFRAGEN", 11), "Kanäle bringen Anfragen")
    s = svg(boden() + fenster(320, 40, 90, 70) + tisch(30, 300, 270) + laptop(60, 230, 70) + balken(160, 170, 110, 90)
            + sitz(95, 228, .78, M) + megafon(320, 170, .9, M3) + handy(350, 250, 40, 70) + blase(250, 110, 60, 40, False, W, 1), "Marketing im Abo: Kanäle laufen, Anfragen kommen")
    return i, v, s


def mes():
    i = icon(balken(120, 110, 200, 160, 4).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Dashboard")
    v = svg(tupfer(220, 200, 150) + R(40, 70, 300, 200, W, 10) + P("M40 100h300") + balken(60, 116, 120, 130, 4) + P("M200 230l30-40 30 20 50-60", "none", 4, MT) + B(200, 120, 110, K, 6)
            + blase(300, 240, 120, 60, False, M, 2) + T(360, 330, "VIRTUELLER MITARBEITER", 9), "Alle Kennzahlen an einem Ort")
    s = svg(boden() + R(200, 40, 210, 140, W, 8) + balken(214, 54, 90, 112, 4) + P("M316 140l20-30 20 14 40-50", "none", 4, MT)
            + P("M120 180C160 160 170 120 196 110M120 220C170 220 180 160 200 150", "none", 2.5, K, 'stroke-dasharray="3 7"') + handy(70, 150, 40, 70) + browser(40, 240, 90, 70)
            + tisch(160, 420, 290) + sitz(300, 290, .82, M) + tasse(360, 266), "Ökosystem läuft, Du konzentrierst Dich aufs Business")
    return i, v, s


def sofort():
    i = icon(P("M90 200c40-60 90-80 130-80s90 20 130 80c-40 60-90 80-130 80s-90-20-130-80z", W, 6) + C(220, 200, 40, M, 6), "Sichtbar")
    v = svg(tupfer(220, 200, 150) + R(40, 80, 120, 150, W, 10) + R(52, 92, 96, 70, M, 6, 0) + B(52, 174, 80, K, 5) + B(52, 186, 60, G3, 5)
            + browser(180, 90, 140, 130) + R(330, 110, 80, 60, W, 6) + P("M330 110l40 30 40-30", "none") + T(220, 270, "POSTING · LANDINGPAGE · E-MAIL", 11), "Fertiges Paket aus Postings, Seite, E-Mail")
    s = svg(boden() + tisch(30, 260, 270) + laptop(70, 230, 80) + sitz(110, 228, .8, M)
            + "".join(steh(290 + j * 48, BODEN, .62, [W, M3, W][j]) for j in range(3)) + handy(300, 120, 40, 70) + P("M200 180C240 140 260 140 300 150", "none", 2.5, K, 'stroke-dasharray="3 7"')
            + R(150, 120, 60, 40, M, 6) + T(180, 145, "LIVE", 11, W), "Makler wird sofort sichtbar bei seinen Kunden")
    return i, v, s


def paidads():
    i = icon(ziel(220, 200, 96) + P("M220 200l90-90", "none", 6) + P("M300 96l16 6 6 16-22-22z", M, 4), "Zielgenau")
    v = svg(tupfer(220, 200, 150) + handy(50, 90, 90, 170) + R(64, 120, 62, 26, W, 4, 2) + T(95, 138, "ANZEIGE", 9)
            + pfeil(156, 180, 196, 180) + browser(208, 110, 120, 110) + pfeil(338, 170, 362, 170) + R(368, 140, 50, 60, M, 8) + P("M380 166l6 6 12-13", "none", 4, W), "Anzeige, Seite, Anfrage")
    s = svg(boden() + "".join(steh(40 + j * 30, BODEN, .5, G if j != 2 else M3) for j in range(5))
            + P("M200 80h200l-70 110v90l-60 30v-120z", M3) + T(300, 120, "GOOGLE · META", 11) + steh(320, BODEN, .62, M) + pfeil(170, 280, 230, 220), "Die richtigen Menschen zur richtigen Zeit")
    return i, v, s


def medien():
    i = icon(folie(110, 120, 150, 100, True).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + rollup(270, 90, 70, 190).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Medien")
    v = svg(tupfer(220, 200, 150) + folie(40, 110, 160, 100) + browser(150, 170, 120, 110) + rollup(300, 60, 80, 220), "PowerPoint, Landingpage, Roll-up")
    s = svg(boden() + R(40, 40, 200, 120, W, 4) + folie(52, 52, 176, 96) + rollup(290, 90, 80, 250)
            + "".join(sitz(80 + j * 64, 340, .7, [W, M3, W][j]) for j in range(3)) + steh(250, BODEN, .9, M, "zeig_l"), "Auftritt mit Präsentation und Roll-up")
    return i, v, s


def powerpoint():
    i = icon(folie(100, 120, 240, 160).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Folie")
    v = svg(tupfer(220, 200, 150) + "".join(f'<g transform="translate({j*28} {j*-22})">{folie(70, 160, 220, 140, j == 2)}</g>' for j in range(3)) + T(220, 340, "EINE BOTSCHAFT JE FOLIE", 11), "Folien, die aufeinander aufbauen")
    s = svg(boden() + R(50, 40, 240, 150, W, 4) + folie(64, 54, 212, 122) + steh(330, BODEN, 1, M, "zeig_l") + "".join(sitz(80 + j * 70, 340, .66, [W, M3, W][j]) for j in range(3)), "Vortrag mit klarer Folie")
    return i, v, s


def landingpage():
    i = icon(browser(110, 100, 220, 170).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Eine Seite")
    v = svg(tupfer(220, 200, 150) + browser(40, 80, 240, 200) + handy(270, 150, 80, 150) + T(370, 110, "90+", 22, K, 700, "middle", SERIF) + T(370, 128, "PAGESPEED", 9), "Desktop, Handy, schnell")
    s = svg(boden() + tisch(30, 280, 270) + laptop(80, 220, 90) + sitz(125, 218, .8) + steh(340, BODEN, .9, M) + handy(370, 170, 40, 70) + P("M180 200C240 150 290 150 360 180", "none", 2.5, K, 'stroke-dasharray="3 7"'), "Kunde findet die Seite und fragt an")
    return i, v, s


def rollup_s():
    i = icon(rollup(170, 80, 100, 250).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Roll-up")
    v = svg(tupfer(220, 200, 150) + rollup(120, 50, 110, 290) + steh(320, 340, .9, W) + P("M250 170h40", "none", 2.5, K, 'stroke-dasharray="3 7"'), "Ein Blick im Vorbeigehen")
    s = svg(boden() + rollup(60, 70, 100, 270) + R(180, 230, 120, 60, G, 4) + tisch(180, 300, 230) + steh(330, BODEN, .9, M, "zeig_l") + steh(390, BODEN, .86) + blase(340, 120, 70, 40, False, W, 1), "Messestand: das Roll-up eröffnet das Gespräch")
    return i, v, s


def video():
    i = icon(R(110, 110, 220, 150, W, 14, 6) + play(220, 185, 42), "Video")
    v = svg(tupfer(220, 200, 150) + R(50, 80, 260, 170, W, 10) + play(180, 165, 36) + P("M60 270h240", "none", 4) + P("M60 270h140", "none", 4, MT) + C(200, 270, 8, M) + handy(320, 150, 80, 150), "Video auf Bildschirm und Handy")
    s = svg(boden() + R(200, 50, 200, 130, W, 6) + play(300, 115, 28) + P("M60 360l40-100h60l40 100", "none") + R(80, 210, 70, 50, K, 6, 0) + C(115, 235, 14, W, 2) + steh(320, BODEN, .9, M), "Dreh mit Kamera, Botschaft in Bewegung")
    return i, v, s


def training():
    i = icon(steh(170, 320, 1.1, W) + steh(270, 320, 1.1, M) + P("M290 150l24-24 16 12 30-34", "none", 6, MT) + P("M344 104h18v18", "none", 6, MT), "Begleitung")
    v = svg(tupfer(220, 200, 150) + steh(130, 340, .95, M) + steh(220, 340, .95, W) + P("M280 280l40-40 30 20 50-70", "none", 5, MT) + P("M380 186h22v22", "none", 5, MT) + T(110, 380, "IM ALLTAG, NICHT IM SEMINAR", 11, K, 700, "start"), "Begleitung bis die Wirkung kommt")
    s = svg(boden() + fenster(310, 40, 90, 70) + tisch(40, 300, 280) + laptop(70, 240, 64) + sitz(102, 238, .8, M) + sitz(240, 278, .8) + doku(150, 248, 50, 30)
            + steh(360, BODEN, .9, M3, "zeig_l"), "Training im Arbeitsalltag des Teams")
    return i, v, s


def sparring():
    i = icon(blase(110, 120, 140, 100, True, W, 2).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + blase(200, 190, 140, 90, False, M, 1).replace(f'stroke-width="{SW}"', 'stroke-width="6"'), "Offenes Gespräch")
    v = svg(tupfer(220, 200, 150) + sitz(120, 300, 1.1, W) + sitz(320, 300, 1.1, M) + tasse(196, 276) + P("M70 300h300", "none", 4) + blase(150, 90, 100, 56, True, W, 2) + birne(300, 120, 26), "Zwei Menschen, ein offenes Gespräch")
    s = svg(boden() + fenster(160, 40, 120, 90) + pflanze(400) + stuhl(60) + sitz(100, 300, .9, M) + P("M60 310h80", "none", 4)
            + stuhl(380, BODEN, False) + sitz(340, 300, .9) + P("M300 310h80", "none", 4) + R(180, 290, 80, 10, G, 3) + tisch(170, 270, 290) + tasse(190, 266) + tasse(226, 266), "Vertrauliches 1:1 auf Augenhöhe")
    return i, v, s


def impuls():
    i = icon(P("M200 120a20 20 0 0 1 40 0v70a20 20 0 0 1-40 0z", W, 6) + P("M180 180a40 40 0 0 0 80 0M220 220v50M190 280h60", "none", 6) + C(220, 140, 6, M, 0), "Impuls")
    v = svg(tupfer(220, 200, 150) + steh(160, 340, 1, M, "hoch") + P("M200 340l20-90h70l20 90z", W) + R(280, 80, 130, 80, W, 6) + T(345, 128, "THESE", 16, K, 700, "middle", SERIF), "Vortrag mit klarer These")
    s = svg(R(20, 290, 400, 20, G, 3) + P("M20 290h400") + R(120, 40, 200, 110, W, 4) + T(220, 104, "THESE", 22, K, 700, "middle", SERIF) + steh(220, 290, .8, M, "hoch")
            + "".join(sitz(60 + j * 64, 392, .6, [W, M3, W, W, M3, W][j]) for j in range(6)), "Bühne, Publikum, Diskussion")
    return i, v, s


def tools():
    i = icon(R(130, 130, 80, 80, W, 12, 6) + R(230, 130, 80, 80, M, 12, 6) + R(180, 220, 80, 80, W, 12, 6) + P("M210 170h20M220 210v10", "none", 6), "Tools greifen ineinander")
    v = svg(tupfer(220, 200, 150) + balken(40, 90, 120, 100) + handy(200, 70, 70, 130) + browser(290, 100, 120, 100) + P("M100 190v40h270v-30M235 200v30", "none", 2.5, K, 'stroke-dasharray="3 7"') + R(170, 250, 110, 50, M, 10) + T(225, 280, "EIN ORT", 12, W), "Drei Systeme an einem Ort")
    s = svg(boden() + R(150, 40, 260, 160, W, 8) + balken(166, 56, 100, 120) + browser(280, 56, 116, 100) + tisch(30, 420, 280) + laptop(60, 240, 60) + sitz(90, 238, .8, M) + tasse(300, 256), "Arbeitsplatz mit einem Dashboard statt fünf Tools")
    return i, v, s


def bester():
    i = icon(tafel(140, 110, 160, 120, False).replace(f'stroke-width="{SW}"', 'stroke-width="6"') + stern(300, 120, 44), "Der beste Workshop")
    v = svg(tupfer(220, 200, 150) + tafel(50, 80, 210, 160, False) + T(155, 130, "1 ZIEL", 18, K, 700, "middle", SERIF) + "".join(zettel(70 + j * 60, 160, [M, W, M3][j], (j * 7) % 9 - 4, 46, 40) for j in range(3)) + stern(330, 130, 50), "Ein Ziel, alle beteiligt, ein Ergebnis")
    s = svg(boden() + tafel(130, 40, 180, 130) + T(220, 90, "1 ZIEL", 16, K, 700, "middle", SERIF) + "".join(zettel(146 + j * 52, 110, [M, W, M3][j], 0, 40, 36) for j in range(3))
            + "".join(steh(60 + j * 80, BODEN, .74, [M, W, M3, W, M][j], "hoch" if j in (0, 3) else None) for j in range(5)), "Alle im Raum arbeiten mit")
    return i, v, s


# Isometrisch als Beispiel, wie eine Darstellungsart über alle drei Stufen trägt
def _iso(x, y):
    return 220 + (x - y) * 22, 150 + (x + y) * 12.7


def _quader(x, y, w, d, h, oben=W):
    a = [_iso(x, y), _iso(x + w, y), _iso(x + w, y + d), _iso(x, y + d)]
    f = lambda pts: " ".join(f"{p[0]:.1f},{p[1]:.1f}" for p in pts)
    s = f'<polygon points="{f([a[3], a[2], (a[2][0], a[2][1]-h), (a[3][0], a[3][1]-h)])}" fill="{G2}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>'
    s += f'<polygon points="{f([a[2], a[1], (a[1][0], a[1][1]-h), (a[2][0], a[2][1]-h)])}" fill="{G}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>'
    return s + f'<polygon points="{f([(p[0], p[1]-h) for p in a])}" fill="{oben}" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>'


def iso_stufen():
    i = svg(tupfer(220, 200, 128) + '<g transform="translate(220 210) scale(1.7) translate(-220 -150)">' + _quader(-2, -2, 4, 4, 24, W) + _quader(-1.4, -1.4, 2.8, 1.2, 0, M) + _quader(-1.4, .4, 1.8, .5, 0, K) + "</g>", "Isometrisches Icon")
    v = svg(tupfer(220, 200, 150) + _quader(-4, -3, 6, 5, 18) + _quader(-3.4, -2.4, 4.8, 1.6, 0, M) + _quader(-3.4, .2, 2, 1.6, 0, G2) + _quader(-.8, .2, 2, 1.6, 0, G2)
            + _quader(3, -1, 1.4, 2.4, 70, W) + _quader(3.2, -.8, 1, 1, 0, M) + _quader(-3, 4, 1.6, 1.6, 30, M3), "Isometrische Vignette")
    s = svg('<g transform="translate(66 52) scale(.7)">' + f'<polygon points="{" ".join(f"{a:.0f},{b:.0f}" for a, b in (_iso(-6, -6), _iso(7, -6), _iso(7, 7), _iso(-6, 7)))}" fill="{G}" stroke="{K}" stroke-width="2.5"/>'
            + _quader(-5, -5, 6, 1, 70) + _quader(-4.6, -4.6, 5, .2, 0, M) + _quader(-1, 0, 6, 2, 24) + _quader(-.5, -1.2, 1, 1, 46, M) + _quader(2.5, -1.2, 1, 1, 46, W)
            + _quader(-.5, 2.4, 1, 1, 46, W) + _quader(2.5, 2.4, 1, 1, 46, M3) + _quader(.4, .4, 1.6, 1, 28, W) + _quader(4.6, -5, 1.6, 1.6, 40, W) + "</g>", "Isometrische Szene")
    return i, v, s


# (Zeile, Bereich, Farbwelt, Funktion)
SEITEN = [
    ("Startseite", "Strategie, die wirkt.", "gelb", startseite),
    ("Strategie in den Alltag überführen", "Strategiehandwerk", "gelb", strategie),
    ("Komplexe Themen strukturieren & kommunizieren", "Strategiehandwerk", "gelb", komplexe),
    ("Innovation & Geschäftsmodell neu denken", "Strategiehandwerk", "gelb", innovation),
    ("Teams befähigen, professionell zu kommunizieren", "Strategiehandwerk / Training", "gelb", teams),
    ("Workshops", "Formate", "magenta", workshops),
    ("KI zum Anfassen", "Workshops", "magenta", ki),
    ("Sprint Landingpage", "Workshops", "magenta", sprint),
    ("Moderation deines Workshops", "Workshops", "magenta", moderation),
    ("Der beste Workshop", "Workshops", "magenta", bester),
    ("Marketing 2.0", "Formate", "cyan", marketing),
    ("MarketingEcoSystem (MES)", "Marketing 2.0", "cyan", mes),
    ("sofort sichtbar", "Marketing 2.0", "cyan", sofort),
    ("Paid Ads", "Marketing 2.0", "cyan", paidads),
    ("Medien, die Ergebnisse liefern", "Marketing 2.0", "cyan", medien),
    ("PowerPoint", "Medien", "cyan", powerpoint),
    ("Landingpage", "Medien", "cyan", landingpage),
    ("Roll-up", "Medien", "cyan", rollup_s),
    ("Video", "Medien", "cyan", video),
    ("Digitale Tools", "Marketing 2.0", "cyan", tools),
    ("Training & Sparring", "Formate", "violett", training),
    ("1:1 Sparring", "Training & Sparring", "violett", sparring),
    ("Impulsvorträge", "Einzelseite", "violett", impuls),
]
