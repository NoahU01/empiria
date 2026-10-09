"""Viele Darstellungsvarianten für drei Szenen (Daniel, 10.10.2026) – Hauptrichtungen Mono, Duo, Isometrisch 3D.

Bausteine sind die Profi-Icons (Phosphor, MIT, e2_phosphor.py). Variiert wird
  · der AUFBAU (ein Icon, Trio, Reihe mit Pfeilen, Raster, Rahmen, Kreis, Typo, beschriftet, gestapelt, Bodenlinie)
  · die DARSTELLUNG (Mono fein/normal/kräftig, Duo mit/ohne Fläche, Isometrisch 3D in vier Arten).
Prozess, Bauplan, Piktogramm, Typografisch sind hier Aufbau-Varianten innerhalb von Mono/Duo.
Farben sind Platzhalter (M = Akzent …) und werden je Bereich umgefärbt (e2_header.farbig).
"""
import math
from e2_phosphor import ICONS

K, W, G, G2, G3 = "#1a1817", "#ffffff", "#f1efeb", "#e3dfd8", "#b9b3ab"
M, M2, M3, M4, MT, ON = "#C51F5D", "#e27fa3", "#f5d3df", "#7a1339", "#C51F5E", "#FEFEFE"
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"

SZENEN = [
    dict(key="medien", titel="Medien, die Ergebnisse liefern", welt="cyan", wort="Wirkung",
         icons=["presentation", "browser", "play-circle", "stack"], labels=["POWERPOINT", "LANDINGPAGE", "VIDEO", "AUS EINER HAND"]),
    dict(key="ki", titel="KI zum Anfassen", welt="magenta", wort="KI",
         icons=["chat-text", "sparkle", "cards", "users-three"], labels=["PROMPT", "KI-TOOLS", "VERGLEICH", "TEAM"]),
    dict(key="sprint", titel="Sprint Landingpage", welt="magenta", wort="48h",
         icons=["browser", "timer", "device-mobile", "rocket-launch"], labels=["LANDINGPAGE", "48 STUNDEN", "MOBILE", "LIVE"]),
]


def svg(inhalt, defs=""):
    return f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" font-family="{SANS}"><defs>{defs}</defs>{inhalt}</svg>'


def ic(name, x, y, g, farbe=K, art="regular", ton=M, ton_op=".28"):
    inner = ICONS[name][art]
    if art == "duotone":
        inner = inner.replace('opacity="0.2"', f'fill="{ton}" opacity="{ton_op}"')
    return f'<g transform="translate({x:.1f} {y:.1f}) scale({g/256:.4f})" fill="{farbe}">{inner}</g>'


def txt(x, y, t, size=13, farbe=K, anchor="middle", serif=False, gewicht=700, extra=""):
    return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="{gewicht}" fill="{farbe}" text-anchor="{anchor}" font-family="{SERIF if serif else SANS}" {extra}>{t}</text>'


def pfeil(x1, y, x2, farbe=K, sw=3):
    return f'<path d="M{x1} {y}H{x2}M{x2-9} {y-8}l9 8-9 8" fill="none" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round" stroke-linejoin="round"/>'


# ================================================================ Darstellung (Mono/Duo) als Einstellung
MODI = {
    "mono_fein": dict(art="thin", flaeche=None),
    "mono": dict(art="regular", flaeche=None),
    "mono_kraeftig": dict(art="bold", flaeche=None),
    "duo": dict(art="duotone", flaeche=None),
    "duo_flaeche": dict(art="duotone", flaeche="kreis"),
    "duo_kachel": dict(art="duotone", flaeche="kachel"),
}


def hinten(modus, cx, cy, r):
    f = MODI[modus]["flaeche"]
    if f == "kreis":
        return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{M3}"/>'
    if f == "kachel":
        return f'<rect x="{cx-r}" y="{cy-r}" width="{2*r}" height="{2*r}" rx="{r*.22:.0f}" fill="{M3}"/>'
    return ""


# ================================================================ Aufbau-Varianten (je Szene, je Modus)
def a_einzel(sz, mo):
    a = MODI[mo]["art"]
    return svg(hinten(mo, 220, 200, 140) + ic(sz["icons"][0], 100, 80, 240, K, a))


def a_trio(sz, mo):
    a = MODI[mo]["art"]
    i = sz["icons"]
    return svg(hinten(mo, 160, 210, 120) + ic(i[0], 40, 96, 210, K, a) + ic(i[1], 286, 52, 104, MT, a) + ic(i[2], 300, 240, 92, K, a))


def a_reihe(sz, mo):
    a = MODI[mo]["art"]
    i, l = sz["icons"], sz["labels"]
    o = ""
    for k in range(3):
        cx = 70 + k * 150
        o += hinten(mo, cx, 180, 56) + ic(i[k], cx - 50, 130, 100, MT if k == 2 else K, a) + txt(cx, 268, l[k], 12)
    return svg(o + pfeil(126, 180, 164) + pfeil(276, 180, 314))


def a_raster(sz, mo):
    a = MODI[mo]["art"]
    i, l = sz["icons"], sz["labels"]
    o = ""
    for k in range(4):
        x, y = 70 + (k % 2) * 160, 40 + (k // 2) * 170
        o += f'<rect x="{x}" y="{y}" width="140" height="150" rx="18" fill="{M3 if (mo.startswith("duo") and k == 1) else G}"/>' + ic(i[k], x + 30, y + 18, 80, MT if k == 1 else K, a) + txt(x + 70, y + 128, l[k], 11)
    return svg(o)


def a_rahmen(sz, mo):
    a = MODI[mo]["art"]
    i = sz["icons"]
    sw = {"mono_fein": 2, "mono": 3.5, "mono_kraeftig": 6}.get(mo, 3.5)
    return svg(f'<rect x="70" y="50" width="300" height="300" rx="36" fill="{M3 if mo.startswith("duo") else "none"}" stroke="{K}" stroke-width="{sw}"/>'
               + ic(i[0], 130, 90, 180, K, a) + txt(220, 316, sz["labels"][0], 14) + f'<circle cx="370" cy="50" r="34" fill="{M}"/>' + ic(i[1], 346, 26, 48, ON, "fill"))


def a_kreis(sz, mo):
    a = MODI[mo]["art"]
    i = sz["icons"]
    o = f'<circle cx="220" cy="200" r="140" fill="none" stroke="{G3}" stroke-width="2" stroke-dasharray="3 9"/>' + hinten(mo, 220, 200, 78)
    o += ic(i[0], 160, 140, 120, K, a)
    for k, ang in enumerate((-60, 60, 180)):
        x = 220 + 140 * math.cos(math.radians(ang)) - 32; y = 200 + 140 * math.sin(math.radians(ang)) - 32
        o += f'<circle cx="{x+32:.1f}" cy="{y+32:.1f}" r="40" fill="{W}" stroke="{G2}" stroke-width="2"/>' + ic(i[k + 1], x, y, 64, MT if k == 0 else K, a)
    return svg(o)


def a_typo(sz, mo):
    a = MODI[mo]["art"]
    w = sz["wort"]
    gr = 210 if len(w) <= 3 else (150 if len(w) <= 5 else 96)
    return svg(hinten(mo, 340, 110, 70) + txt(24, 290, w, gr, K, "start", True, 700, 'letter-spacing="-6"') + ic(sz["icons"][0], 290, 50, 110, MT, a)
               + f'<path d="M24 330h392" stroke="{K}" stroke-width="4" stroke-linecap="round"/>' + txt(24, 364, sz["titel"].upper(), 12, K, "start", False, 700, 'letter-spacing="2"'))


def a_beschriftet(sz, mo):
    a = MODI[mo]["art"]
    i, l = sz["icons"], sz["labels"]
    o = hinten(mo, 200, 200, 110) + ic(i[0], 100, 100, 200, K, a)
    for k, (x, y, tx, ty, anc) in enumerate(((290, 140, 404, 110, "end"), (120, 270, 36, 330, "start"), (290, 270, 404, 330, "end"))):
        o += f'<path d="M{x} {y}L{tx if anc == "end" else tx} {ty}" stroke="{K}" stroke-width="1.4"/><circle cx="{x}" cy="{y}" r="4" fill="{MT}"/>' + txt(tx, ty - 8, l[k], 12, K, anc)
    return svg(o)


def a_gestapelt(sz, mo):
    a = MODI[mo]["art"]
    i = sz["icons"]
    o = ""
    for k, (x, y, f) in enumerate(((60, 70, G), (130, 130, G2 if not mo.startswith("duo") else M3), (200, 190, W))):
        o += f'<rect x="{x}" y="{y}" width="190" height="150" rx="18" fill="{f}" stroke="{K}" stroke-width="{2 if mo == "mono_fein" else 3}"/>' + ic(i[k], x + 55, y + 35, 80, MT if k == 2 else K, a)
    return svg(o)


def a_boden(sz, mo):
    a = MODI[mo]["art"]
    i = sz["icons"]
    o = f'<path d="M30 330H410" stroke="{K}" stroke-width="3" stroke-linecap="round"/>'
    for k, (x, g) in enumerate(((40, 170), (230, 110), (340, 76))):
        o += f'<ellipse cx="{x+g/2}" cy="334" rx="{g*.42:.0f}" ry="8" fill="{G2}"/>' + ic(i[k], x, 326 - g, g, MT if k == 1 else K, a)
    return svg(hinten(mo, 300, 120, 60) + o)


AUFBAU = [(a_einzel, "Ein Icon"), (a_trio, "Trio"), (a_reihe, "Reihe mit Pfeilen (Prozess)"), (a_raster, "Raster (Piktogramm)"), (a_rahmen, "Rahmen"),
          (a_kreis, "Kreis"), (a_typo, "Typo + Icon"), (a_beschriftet, "Beschriftet (Bauplan)"), (a_gestapelt, "Gestapelt"), (a_boden, "Auf einer Linie")]


# ================================================================ Isometrisch 3D – mit Profi-Icons
S3 = .866


def _p(x, y, z, s=32, c=(220, 200)):
    return c[0] + (x - y) * S3 * s, c[1] + (x + y) * .5 * s - z * s


def _poly(pts, fill, sw=2):
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{fill}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>'


def _wuerfel(x, y, w, h, oben=W, links=G, rechts=G2, s=32, c=(220, 200)):
    P = lambda a, b, z: _p(a, b, z, s, c)
    return (_poly([P(x, y + w, 0), P(x + w, y + w, 0), P(x + w, y + w, h), P(x, y + w, h)], links)
            + _poly([P(x + w, y, 0), P(x + w, y + w, 0), P(x + w, y + w, h), P(x + w, y, h)], rechts)
            + _poly([P(x, y, h), P(x + w, y, h), P(x + w, y + w, h), P(x, y + w, h)], oben))


def _icon_oben(name, x, y, w, h, farbe=K, art="bold", s=32, c=(220, 200)):
    """Icon liegt auf der Deckfläche eines Würfels (isometrisch verzerrt)."""
    ox, oy = _p(x, y, h, s, c)
    k = w * s / 256 * .74
    off = w * .13
    ox2, oy2 = _p(x + off, y + off, h, s, c)
    return f'<g transform="matrix({S3*k:.4f} {.5*k:.4f} {-S3*k:.4f} {.5*k:.4f} {ox2:.1f} {oy2:.1f})" fill="{farbe}">{ICONS[name][art]}</g>'


def _icon_stehend(name, x, y, z, b, farbe=K, art="bold", s=32, c=(220, 200)):
    """Icon auf einer aufrechten Tafel (Ebene y = konst.)."""
    ox, oy = _p(x, y, z + b, s, c)
    k = b * s / 256
    return f'<g transform="matrix({S3*k:.4f} {.5*k:.4f} 0 {k:.4f} {ox:.1f} {oy:.1f})" fill="{farbe}">{ICONS[name][art]}</g>'


def i_wuerfel(sz):
    i = sz["icons"]
    o = _wuerfel(-1, -1, 4, 1.2, W) + _icon_oben(i[0], -1, -1, 4, 1.2)
    o += _wuerfel(3.6, -.6, 2.4, 2.2, M, M2, M4) + _icon_oben(i[1], 3.6, -.6, 2.4, 2.2, ON)
    o += _wuerfel(.4, 3.8, 2.4, .7, W) + _icon_oben(i[2], .4, 3.8, 2.4, .7)
    return svg(o)


def i_aufsteller(sz):
    i = sz["icons"]
    o = _wuerfel(-3, -3, 9, .35, G, G2, G3)
    for k, (x, y, b, f) in enumerate(((-2.4, -1.6, 2.8, W), (2.0, .2, 2.2, M), (-1.0, 3.0, 1.8, W))):
        P = lambda a, bb, z: _p(a, bb, z)
        z0 = .35
        o += _poly([P(x, y, z0), P(x + b, y, z0), P(x + b, y, z0 + b), P(x, y, z0 + b)], f, 2.2)
        o += _poly([P(x, y, z0 + b), P(x + b, y, z0 + b), P(x + b + .0, y - .25, z0 + b), P(x, y - .25, z0 + b)], G2, 2)
        o += _icon_stehend(i[k], x + b * .13, y, z0 + b * .13, b * .74, ON if f == M else K)
    return svg(o)


def i_stapel(sz):
    i = sz["icons"]
    o = ""
    for k, (z, f, l, rr) in enumerate(((0, W, G, G2), (1.3, W, G, G2), (2.6, M, M2, M4))):
        o += _wuerfel(-1.5, -1.5, 5, .6, f, l, rr, 32, (220, 290 - z * 32)) + _icon_oben(i[2 - k], -.3, -.3, 2.6, .6, ON if f == M else K, "bold", 32, (220, 290 - z * 32))
    return svg(o)


def i_kacheln(sz):
    i = sz["icons"]
    o = ""
    for k, (x, y, h, f) in enumerate(((-3, -1, .9, W), (0, -2.5, 1.8, M), (1.5, 1.5, .9, W), (-1.5, 2.5, .5, W))):
        o += _wuerfel(x, y, 2.6, h, f, M2 if f == M else G, M4 if f == M else G2) + _icon_oben(i[k], x, y, 2.6, h, ON if f == M else K)
    return svg(o)


ISO = [(i_wuerfel, "Isometrisch · Icon-Würfel"), (i_aufsteller, "Isometrisch · Aufsteller auf Platte"), (i_stapel, "Isometrisch · Ebenen gestapelt"), (i_kacheln, "Isometrisch · Kacheln verschieden hoch")]

GRUPPEN = [
    ("Mono", [("mono", "normal"), ("mono_fein", "fein"), ("mono_kraeftig", "kräftig")]),
    ("Duo", [("duo", "zweitönig"), ("duo_flaeche", "mit Kreis"), ("duo_kachel", "mit Kachel")]),
]
