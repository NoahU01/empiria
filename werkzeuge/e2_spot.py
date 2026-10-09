"""Spot-Illustrationen je Seite in allen verbliebenen Darstellungsarten (Daniel, 10.10.2026).

Prinzip: Jede Seite hat EIN Motiv (welche Dinge, wo, mit welcher Beschriftung). Jede Darstellungsart zeichnet dieses
Motiv mit eigenen Mitteln – so ist der Vergleich fair und jedes Bild wird nur einmal „erfunden“.
Kein Farbkreis (Vignette) dahinter. Farben sind Platzhalter, die je Bereich umgefärbt werden (e2_header.farbig).
"""
import math

K, W, G, G2, G3 = "#1a1817", "#ffffff", "#f1efeb", "#e3dfd8", "#b9b3ab"
M, M2, M3, M4, MT, ON = "#C51F5D", "#e27fa3", "#f5d3df", "#7a1339", "#C51F5E", "#FEFEFE"
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"


# ================================================================ Darstellungsarten als Stift
class Stift:
    """Zeichnet Grundformen; eine Darstellungsart ist nur eine andere Einstellung dieser Grundformen.
    Rollen: w = weiße Fläche, a = Akzent, h = hell, k = dunkel, n = ohne Fläche."""
    def __init__(self, sw=3, linie=K, fuell=None, balken=(K, G3), schrift=K, extra="", schatten=False):
        self.sw, self.linie, self.schrift, self.extra, self.schatten = sw, linie, schrift, extra, schatten
        self.f = {"w": W, "a": M, "h": G, "k": K, "n": "none"}
        self.f.update(fuell or {})
        self.bal = balken

    def _st(self, rolle):
        s = self.linie if not isinstance(self.linie, dict) else self.linie.get(rolle, self.linie["*"])
        return f'stroke="{s}" stroke-width="{self.sw}" stroke-linejoin="round" stroke-linecap="round"' if s != "none" else 'stroke="none"'

    def box(self, x, y, w, h, rolle="w", rx=8):
        sch = ' filter="url(#hvsch)"' if self.schatten and rolle in ("w", "h") else ""
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}" rx="{rx}" fill="{self.f[rolle]}" {self._st(rolle)} {self.extra}{sch}/>'

    def kreis(self, cx, cy, r, rolle="w"):
        return f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="{self.f[rolle]}" {self._st(rolle)} {self.extra}/>'

    def pfad(self, d, rolle="n"):
        return f'<path d="{d}" fill="{self.f[rolle]}" {self._st(rolle)} {self.extra}/>'

    def balken(self, x, y, w, art=0, h=6):
        c = self.bal[art]
        return f'<rect x="{x:.1f}" y="{y:.1f}" width="{max(w,4):.1f}" height="{h}" rx="{h/2}" fill="{c}"/>' if c != "none" else ""

    def text(self, x, y, t, size=12, serif=False):
        return f'<text x="{x:.1f}" y="{y:.1f}" font-size="{size}" font-weight="700" fill="{self.schrift}" text-anchor="middle" font-family="{SERIF if serif else SANS}">{t}</text>'


STIFT = {
    "mono": Stift(4.5, {"a": MT, "*": K}, {"a": M3, "h": W}, (K, K)),
    "duo": Stift(3, M4, {"a": M, "h": M3, "k": M4, "w": W}, (M4, M2), M4),
    "iso": Stift(2.5, K, {"a": M, "h": G, "k": K}, (K, G3)),
    "glas": Stift(2, {"a": M, "*": "#ffffff"}, {"w": "rgba(255,255,255,.62)", "h": "rgba(255,255,255,.4)", "a": M, "k": K}, (K, "#8a847c"), K, schatten=True),
}


# ================================================================ Bauteile (zeichnen sich in einer Box)
def doku(s, x, y, w, h, akzent=False):
    o = s.box(x, y, w, h, "w", 5) + s.balken(x + w * .14, y + h * .13, w * .6, 0, 7)
    o += "".join(s.balken(x + w * .14, y + h * (.32 + i * .13), w * (.72 - (i % 2) * .22), 1, 5) for i in range(4))
    return o + (s.box(x + w * .14, y + h * .84, w * .4, h * .06, "a", 3) if akzent else "")


def folie(s, x, y, w, h, akzent=True):
    return (s.box(x, y, w, h, "w", 5) + s.balken(x + w * .1, y + h * .14, w * .5, 0, 7)
            + s.box(x + w * .1, y + h * .36, w * .36, h * .46, "a" if akzent else "h", 3)
            + s.balken(x + w * .54, y + h * .42, w * .34, 1, 5) + s.balken(x + w * .54, y + h * .56, w * .26, 1, 5))


def browser(s, x, y, w, h):
    return (s.box(x, y, w, h, "w", 8) + s.pfad(f"M{x} {y+h*.16:.1f}H{x+w}") + s.kreis(x + 12, y + h * .08, 2.8, "k") + s.kreis(x + 22, y + h * .08, 2.8, "k")
            + s.box(x + w * .08, y + h * .26, w * .84, h * .28, "a", 4) + s.balken(x + w * .08, y + h * .63, w * .55, 0, 6)
            + s.balken(x + w * .08, y + h * .73, w * .4, 1, 5) + s.box(x + w * .08, y + h * .83, w * .28, h * .08, "k", h * .04))


def handy(s, x, y, w, h):
    return (s.box(x, y, w, h, "w", w * .18) + s.box(x + w * .14, y + h * .12, w * .72, h * .3, "a", 3)
            + s.balken(x + w * .14, y + h * .5, w * .6, 0, 4) + s.balken(x + w * .14, y + h * .59, w * .44, 1, 4) + s.box(x + w * .14, y + h * .74, w * .5, h * .08, "k", h * .04))


def uhr(s, cx, cy, r, text="48h"):
    return (s.pfad(f"M{cx} {cy-r:.1f}v{-r*.22:.1f}M{cx-r*.25:.1f} {cy-r*1.24:.1f}h{r*.5:.1f}") + s.kreis(cx, cy, r, "w")
            + s.pfad(f"M{cx} {cy}V{cy-r*.6:.1f}M{cx} {cy}l{r*.4:.1f} {r*.24:.1f}") + s.text(cx, cy + r * .68, text, r * .34, True))


def karten3(s, x, y, w, h, labels, akzent=1):
    o = ""
    zh = h / 3.3
    for i, lab in enumerate(labels):
        yy = y + i * zh * 1.15
        o += s.box(x, yy, w, zh, "a" if i == akzent else "w", zh / 2) + s.pfad(f"M{x+zh*.45:.1f} {yy+zh*.5:.1f}l{zh*.15:.1f} {zh*.15:.1f} {zh*.28:.1f}-{zh*.3:.1f}") + s.text(x + w * .6, yy + zh * .62, lab, zh * .3)
    return o


def ziel(s, cx, cy, r):
    return s.kreis(cx, cy, r, "w") + s.kreis(cx, cy, r * .62, "w") + s.kreis(cx, cy, r * .26, "a")


def flagge(s, x, y, h):
    return s.pfad(f"M{x} {y+h}V{y}") + s.pfad(f"M{x} {y+2}h{h*.5:.1f}l-{h*.1:.1f} {h*.16:.1f} {h*.1:.1f} {h*.16:.1f}H{x}", "a")


def birne(s, cx, cy, r):
    return (s.pfad(f"M{cx-r*.45:.1f} {cy+r*1.05:.1f}h{r*.9:.1f}M{cx-r*.3:.1f} {cy+r*1.3:.1f}h{r*.6:.1f}")
            + s.pfad(f"M{cx} {cy-r}a{r} {r} 0 0 0-{r*.6:.1f} {r*1.8:.1f}V{cy+r*.85:.1f}h{r*1.2:.1f}V{cy+r*.8:.1f}A{r} {r} 0 0 0 {cx} {cy-r}z", "h"))


def balken_fenster(s, x, y, w, h, trend=True):
    o = s.box(x, y, w, h, "w", 8) + s.pfad(f"M{x} {y+h*.14:.1f}H{x+w}")
    bw = w * .4 / 9
    for i, hh in enumerate((.3, .55, .42, .8)):
        o += s.box(x + w * .08 + bw * (1 + 2 * i), y + h * (.9 - hh * .65), bw, h * hh * .65, "a" if i == 3 else "k", 2)
    if trend:
        o += s.pfad(f"M{x+w*.56:.1f} {y+h*.8:.1f}l{w*.1:.1f}-{h*.22:.1f} {w*.1:.1f} {h*.1:.1f} {w*.16:.1f}-{h*.32:.1f}") + s.balken(x + w * .56, y + h * .26, w * .34, 0, 6)
    return o


def blase(s, x, y, w, h, rolle="w", links=True):
    sx = x + w * .22 if links else x + w * .78
    d = -1 if links else 1
    return (s.box(x, y, w, h, rolle, h * .3) + s.pfad(f"M{sx:.1f} {y+h-1:.1f}l{d*-2} 14 {d*16}-14", rolle)
            + s.balken(x + w * .15, y + h * .34, w * .6, 0 if rolle != "a" else 1, 5) + s.balken(x + w * .15, y + h * .58, w * .38, 1, 5))


def zettelwand(s, x, y, w, h, n=6, trenner=False, titel=None):
    o = s.box(x, y, w, h, "w", 6)
    sp = 3 if n <= 6 else 4
    zw, zh = w * .8 / sp, (h * .7) / ((n + sp - 1) // sp)
    oy = y + (h * .22 if titel else h * .12)
    for i in range(n):
        xx, yy = x + w * .1 + (i % sp) * zw, oy + (i // sp) * zh
        rot = (i * 7) % 9 - 4
        o += f'<g transform="rotate({rot} {xx+zw*.4:.1f} {yy+zh*.4:.1f})">' + s.box(xx, yy, zw * .82, zh * .78, ["a", "h", "w"][i % 3], 3) + s.balken(xx + zw * .12, yy + zh * .26, zw * .5, 0, 3) + "</g>"
    if trenner:
        o += s.pfad(f"M{x+w*.06:.1f} {y+h*.5:.1f}H{x+w*.94:.1f}")
    if titel:
        o += s.text(x + w / 2, y + h * .14, titel, h * .1, True)
    return o


def laptop(s, x, y, w):
    h = w * .62
    return (s.box(x, y, w, h, "w", 6) + s.pfad(f"M{x-w*.08:.1f} {y+h+10:.1f}H{x+w*1.08:.1f}L{x+w} {y+h:.1f}H{x}Z", "h")
            + s.box(x + w * .08, y + h * .14, w * .84, h * .2, "h", h * .1) + s.balken(x + w * .14, y + h * .21, w * .5, 0, 5)
            + s.box(x + w * .3, y + h * .44, w * .62, h * .34, "a", 8) + s.balken(x + w * .36, y + h * .54, w * .44, 1 if True else 0, 5))


def tools3(s, x, y, w, h):
    o = ""
    for i, lab in enumerate(("A", "B", "C")):
        yy = y + i * h / 3
        o += s.box(x, yy, w, h / 3 - 10, "a" if i == 1 else "w", 10) + s.text(x + w / 2, yy + h / 6, "TOOL " + lab, 11)
    return o


def rollup(s, x, y, w, h):
    return (s.box(x, y, w, h, "w", 3) + s.box(x + w * .12, y + h * .08, w * .76, h * .06, "k", 2) + s.box(x + w * .12, y + h * .22, w * .76, h * .36, "a", 3)
            + s.balken(x + w * .12, y + h * .66, w * .6, 1, 5) + s.balken(x + w * .12, y + h * .74, w * .45, 1, 5) + s.box(x - 6, y + h, w + 12, 9, "h", 2))


def video(s, x, y, w, h):
    cx, cy, r = x + w / 2, y + h * .45, h * .2
    return (s.box(x, y, w, h, "w", 10) + s.kreis(cx, cy, r, "a") + s.pfad(f"M{cx-r*.3:.1f} {cy-r*.42:.1f}L{cx+r*.46:.1f} {cy}L{cx-r*.3:.1f} {cy+r*.42:.1f}z", "w")
            + s.pfad(f"M{x+w*.08:.1f} {y+h*.86:.1f}H{x+w*.92:.1f}") + s.kreis(x + w * .5, y + h * .86, 6, "a"))


def stein(s, x, y, w, h):
    return (s.pfad(f"M{x} {y+h}V{y+w*.5:.1f}a{w/2} {w/2} 0 0 1 {w} 0V{y+h}z", "h") + s.pfad(f"M{x+w*.6:.1f} {y+4}l-{w*.1:.1f} {h*.2:.1f} {w*.1:.1f} {h*.14:.1f}-{w*.08:.1f} {h*.16:.1f} {w*.1:.1f} {h*.14:.1f}")
            + "".join(s.balken(x + w * .18, y + h * (.5 + i * .1), w * (.5 - i * .08), 0, 5) for i in range(3)))


def bausteine(s, x, y, g):
    o = ""
    for (cx, cy, r_) in ((0, 1, "w"), (1, 1, "a"), (2, 1, "w"), (.5, 0, "w"), (1.5, 0, "h")):
        o += s.box(x + cx * g * 1.06, y + cy * g * 1.06, g, g, r_, 5)
    return o + f'<g transform="rotate(14 {x+g*1.5:.1f} {y-g*.9:.1f})">' + s.box(x + g, y - g * 1.4, g, g, "w", 5) + "</g>"


def person(s, x, fy, k=1.0, rolle="w", arm=None):
    f = lambda v: v * k
    o = s.pfad(f"M{x-f(10):.1f} {fy-f(62):.1f}V{fy}M{x+f(10):.1f} {fy-f(62):.1f}V{fy}")
    o += s.pfad(f"M{x-f(22):.1f} {fy-f(60):.1f}L{x-f(24):.1f} {fy-f(102):.1f}Q{x-f(24):.1f} {fy-f(120):.1f} {x-f(8):.1f} {fy-f(120):.1f}H{x+f(8):.1f}Q{x+f(24):.1f} {fy-f(120):.1f} {x+f(24):.1f} {fy-f(102):.1f}L{x+f(22):.1f} {fy-f(60):.1f}Z", rolle)
    if arm == "zeig":
        o += s.pfad(f"M{x+f(20):.1f} {fy-f(106):.1f}L{x+f(56):.1f} {fy-f(132):.1f}")
    return o + s.kreis(x, fy - f(138), f(14), "w")


def stern(s, cx, cy, r):
    pts = " ".join(f"{cx + (r if i % 2 == 0 else r*.45) * math.cos(math.radians(i*36-90)):.1f},{cy + (r if i % 2 == 0 else r*.45) * math.sin(math.radians(i*36-90)):.1f}" for i in range(10))
    return s.pfad("M" + pts.replace(" ", "L") + "Z", "a")


def brief(s, x, y, w, h, rolle="a"):
    return s.box(x, y, w, h, rolle, 8) + s.pfad(f"M{x+w*.14:.1f} {y+h*.28:.1f}l{w*.36:.1f} {h*.28:.1f} {w*.36:.1f}-{h*.28:.1f}")


def raster6(s, x, y, w, h):
    o = s.box(x, y, w, h, "w", 10)
    for r_ in (0, 1):
        for c in (0, 1, 2):
            o += s.box(x + w * .08 + c * w * .3, y + h * .12 + r_ * h * .42, w * .24, h * .32, "a" if (r_, c) == (0, 1) else "h", 4)
    return o


def haken_kachel(s, x, y, w, h):
    return s.box(x, y, w, h, "a", 12) + s.pfad(f"M{x+w*.28:.1f} {y+h*.52:.1f}l{w*.14:.1f} {w*.14:.1f} {w*.3:.1f}-{w*.32:.1f}")


def liste_kachel(s, x, y, w, h):
    o = s.box(x, y, w, h, "a", 10)
    for j in range(3):
        yy = y + h * (.24 + j * .25)
        o += s.pfad(f"M{x+w*.16:.1f} {yy:.1f}l{w*.07:.1f} {w*.07:.1f} {w*.13:.1f}-{w*.14:.1f}") + s.balken(x + w * .46, yy - 2, w * .4, 1, 6)
    return o


def trend(s, x, y, w, h):
    return s.pfad(f"M{x} {y+h}l{w*.35:.1f}-{h*.45:.1f} {w*.25:.1f} {h*.2:.1f} {w*.4:.1f}-{h*.75:.1f}") + s.pfad(f"M{x+w*.78:.1f} {y}h{w*.22:.1f}v{h*.22:.1f}")


def pult(s, x, y, w, h):
    return s.pfad(f"M{x} {y+h}l{w*.15:.1f}-{h} h{w*.7:.1f} l{w*.15:.1f} {h}z", "w")


def tasse(s, x, y):
    return s.pfad(f"M{x} {y}h24v18a8 8 0 0 1-8 8h-8a8 8 0 0 1-8-8z", "w") + s.pfad(f"M{x+24} {y+4}a7 7 0 0 1 0 14")


def wort(s, x, y, t, size):
    return s.text(x, y, t, size, True)


TEILE = dict(doku=doku, folie=folie, browser=browser, handy=handy, uhr=uhr, karten3=karten3, ziel=ziel, flagge=flagge, birne=birne,
             balken_fenster=balken_fenster, blase=blase, zettelwand=zettelwand, laptop=laptop, tools3=tools3, rollup=rollup, video=video,
             stein=stein, bausteine=bausteine, person=person, stern=stern, brief=brief, raster6=raster6, haken_kachel=haken_kachel,
             liste_kachel=liste_kachel, trend=trend, pult=pult, tasse=tasse, wort=wort)


# ================================================================ Motive je Seite
# Jedes Teil: (Bauteil, Argumente, Beschriftung für Bauplan/Prozess oder None). „pfeile“: Verbindungen in der Grundanordnung.
def E(teil, *args, label=None, **kw):
    return dict(teil=teil, args=args, kw=kw, label=label)


MOTIVE = {
    "startseite": dict(wort="Wirkung", teile=[E("doku", 30, 110, 110, 150, label="STRATEGIE"), E("raster6", 170, 120, 150, 130, label="EINORDNEN"), E("flagge", 370, 110, 120, label="WIRKUNG")],
                       pfeile=[(150, 186, 162, 186), (330, 186, 356, 186)]),
    "strategie": dict(wort="Alltag", teile=[E("doku", 40, 100, 120, 170, label="STRATEGIE"), E("karten3", 210, 100, 200, 190, ["ROLLE", "RICHTUNG", "WERKZEUG"], label="HANDLUNGSKLARHEIT")],
                      pfeile=[(172, 186, 198, 186)]),
    "komplexe": dict(wort="1 Botschaft", teile=[E("folie", 30, 170, 120, 80, False, label=None), E("folie", 44, 140, 120, 80, False, label=None), E("folie", 26, 110, 120, 80, False, label="FOLIENBERG"),
                                                E("folie", 220, 120, 180, 120, label="EINE BOTSCHAFT"), E("ziel", 380, 270, 30, label="ZIEL")],
                     pfeile=[(170, 180, 206, 180)]),
    "innovation": dict(wort="Neu", teile=[E("stein", 40, 110, 140, 220, label="GILT ALS GEGEBEN"), E("bausteine", 250, 230, 50, label="NEU GEDACHT"), E("birne", 360, 110, 34, label="IDEE")],
                       pfeile=[(196, 230, 236, 230)]),
    "teams": dict(wort="Souverän", teile=[E("folie", 140, 70, 200, 130, label="STORY"), E("person", 100, 350, 1.0, "a", "zeig", label="TEAM"), E("blase", 290, 230, 120, 64, "w", True, label="FEEDBACK")],
                  pfeile=[]),
    "workshops": dict(wort="Ergebnis", teile=[E("zettelwand", 30, 90, 220, 170, 6, label="ECHTE FÄLLE"), E("liste_kachel", 300, 100, 110, 150, label="ERGEBNIS")],
                      pfeile=[(262, 176, 288, 176)]),
    "ki": dict(wort="KI", teile=[E("laptop", 30, 110, 240, label="PROMPT"), E("tools3", 310, 90, 100, 200, label="TOOLS IM VERGLEICH"), E("stern", 286, 92, 20, label=None)], pfeile=[]),
    "sprint": dict(wort="48h", teile=[E("browser", 30, 90, 240, 190, label="LANDINGPAGE"), E("handy", 240, 170, 76, 140, label="MOBILE"), E("uhr", 360, 120, 46, "48h", label="48 STUNDEN")], pfeile=[]),
    "moderation": dict(wort="Klarheit", teile=[E("zettelwand", 30, 80, 250, 190, 8, True, label="BEITRÄGE"), E("blase", 290, 110, 120, 70, "a", False, label="MODERATION"), E("liste_kachel", 310, 210, 100, 110, label="KLARHEIT")], pfeile=[]),
    "bester": dict(wort="1 Ziel", teile=[E("zettelwand", 40, 80, 230, 190, 3, False, "1 ZIEL", label="EIN ZIEL"), E("stern", 350, 160, 56, label="ERGEBNIS")], pfeile=[(282, 170, 300, 170)]),
    "marketing": dict(wort="Anfragen", teile=[E("handy", 30, 100, 76, 140, label="SOCIAL"), E("browser", 126, 90, 150, 130, label="SEITE"), E("brief", 320, 120, 96, 76, label="ANFRAGEN")],
                      pfeile=[(286, 158, 310, 158)]),
    "mes": dict(wort="MES", teile=[E("balken_fenster", 30, 70, 300, 200, label="KENNZAHLEN"), E("blase", 270, 240, 140, 70, "a", False, label="VIRTUELLER MITARBEITER")], pfeile=[]),
    "sofort": dict(wort="Sofort", teile=[E("handy", 30, 90, 90, 160, label="POSTINGS"), E("browser", 140, 90, 160, 140, label="LANDINGPAGE"), E("brief", 320, 120, 90, 70, "w", label="E-MAIL")], pfeile=[]),
    "paidads": dict(wort="Treffer", teile=[E("handy", 30, 90, 90, 170, label="ANZEIGE"), E("browser", 160, 110, 140, 120, label="SEITE"), E("haken_kachel", 340, 130, 70, 70, label="ANFRAGE")],
                    pfeile=[(130, 175, 150, 175), (310, 168, 330, 168)]),
    "medien": dict(wort="Medien", teile=[E("folie", 20, 110, 170, 110, label="POWERPOINT"), E("browser", 150, 180, 130, 120, label="LANDINGPAGE"), E("rollup", 310, 60, 90, 250, label="ROLL-UP")], pfeile=[]),
    "powerpoint": dict(wort="Folie", teile=[E("folie", 40, 180, 220, 140, False, label=None), E("folie", 80, 140, 220, 140, False, label=None), E("folie", 120, 100, 240, 150, label="EINE BOTSCHAFT JE FOLIE")], pfeile=[]),
    "landingpage": dict(wort="90+", teile=[E("browser", 30, 90, 240, 200, label="DESKTOP"), E("handy", 250, 160, 80, 150, label="MOBILE"), E("wort", 375, 140, "90+", 34, label="PAGESPEED")], pfeile=[]),
    "rollup": dict(wort="Auftritt", teile=[E("rollup", 110, 50, 120, 290, label="ROLL-UP"), E("person", 330, 350, .95, "w", label="BESUCHER")], pfeile=[(250, 170, 300, 190)]),
    "video": dict(wort="Video", teile=[E("video", 30, 90, 270, 180, label="VIDEO"), E("handy", 320, 150, 84, 150, label="MOBILE")], pfeile=[]),
    "tools": dict(wort="1 Ort", teile=[E("balken_fenster", 30, 80, 130, 110, False, label="DASHBOARD"), E("handy", 180, 70, 70, 130, label="APP"), E("browser", 280, 90, 130, 110, label="SEITE"),
                                       E("brief", 160, 260, 120, 60, "a", label="EIN ORT")], pfeile=[(95, 200, 200, 255), (215, 210, 220, 250), (345, 210, 260, 255)]),
    "training": dict(wort="Wirkung", teile=[E("person", 120, 340, 1.0, "a", label="TEAM"), E("person", 210, 340, 1.0, "w", label="COACH"), E("trend", 270, 140, 140, 120, label="WIRKUNG")], pfeile=[]),
    "sparring": dict(wort="1:1", teile=[E("blase", 40, 110, 170, 100, "w", True, label="OFFEN"), E("blase", 190, 200, 170, 90, "a", False, label="AUF AUGENHÖHE"), E("birne", 370, 110, 34, label="KLARHEIT"), E("tasse", 80, 300, label=None)], pfeile=[]),
    "impuls": dict(wort="These", teile=[E("person", 130, 340, 1.0, "a", "zeig", label="IMPULS"), E("pult", 170, 250, 110, 90, label=None), E("folie", 250, 70, 170, 110, label="THESE")], pfeile=[]),
}


# ================================================================ Rendern je Darstellungsart
def _teile(stift, motiv, mit_pfeilen=True):
    o = "".join(TEILE[t["teil"]](stift, *t["args"], **t["kw"]) for t in motiv["teile"])
    if mit_pfeilen:
        for (x1, y1, x2, y2) in motiv["pfeile"]:
            a = math.atan2(y2 - y1, x2 - x1)
            p1 = (x2 - 11 * math.cos(a - .5), y2 - 11 * math.sin(a - .5)); p2 = (x2 - 11 * math.cos(a + .5), y2 - 11 * math.sin(a + .5))
            o += stift.pfad(f"M{x1} {y1}L{x2} {y2}") + stift.pfad(f"M{p1[0]:.1f} {p1[1]:.1f}L{x2} {y2}L{p2[0]:.1f} {p2[1]:.1f}")
    return o


def _box(t):
    """Ungefähre Box eines Teils (für Beschriftung und Prozess-Anordnung)."""
    a = t["args"]
    if t["teil"] in ("uhr", "ziel", "birne"):
        return a[0] - a[2], a[1] - a[2], 2 * a[2], 2 * a[2]
    if t["teil"] == "stern":
        return a[0] - a[2], a[1] - a[2], 2 * a[2], 2 * a[2]
    if t["teil"] == "flagge":
        return a[0], a[1], a[2] * .5, a[2]
    if t["teil"] == "person":
        return a[0] - 26 * a[2], a[1] - 152 * a[2], 52 * a[2], 152 * a[2]
    if t["teil"] == "laptop":
        return a[0], a[1], a[2], a[2] * .62
    if t["teil"] == "bausteine":
        return a[0], a[1] - a[2] * 1.4, a[2] * 3.2, a[2] * 2.5
    if t["teil"] == "wort":
        return a[0] - 40, a[1] - 34, 80, 40
    if t["teil"] == "tasse":
        return a[0], a[1], 32, 26
    return a[0], a[1], a[2], a[3]


def bild(inhalt, label, defs=""):
    return f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" aria-label="{label}" font-family="{SANS}"><defs>{defs}</defs>{inhalt}</svg>'


def r_mono(m):
    return bild(_teile(STIFT["mono"], m), "Monolinie")


def r_duo(m):
    return bild(_teile(STIFT["duo"], m), "Duoton")










def r_glas(m):
    defs = ('<filter id="hvgl" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="28"/></filter>'
            '<filter id="hvsch" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="8" stdDeviation="9" flood-color="#1a1817" flood-opacity=".12"/></filter>')
    return bild(f'<g filter="url(#hvgl)"><circle cx="130" cy="150" r="90" fill="{M}" opacity=".7"/><circle cx="320" cy="260" r="90" fill="{M2}" opacity=".8"/><circle cx="320" cy="110" r="60" fill="#cfcac2"/></g>'
                + _teile(STIFT["glas"], m), "Glas", defs)




# ---------------------------------------------------------------- Isometrisch 3D: Grundplatte, darauf stehen die Dinge
ISO_C, ISO_S, ISO_N = (220, 250), 27.0, 8   # Bildmitte der Platte, Länge einer Rastereinheit, Rastergröße der Platte


def _p(x, y, z=0.0):
    """Weltkoordinate (Raster 0–10 auf der Platte, z nach oben) → Bildpunkt."""
    return ISO_C[0] + (x - y) * .866 * ISO_S, ISO_C[1] + (x + y - ISO_N) * .5 * ISO_S - z * ISO_S


def _poly(pts, fill, sw=2.2):
    return f'<polygon points="{" ".join(f"{a:.1f},{b:.1f}" for a, b in pts)}" fill="{fill}" stroke="{K}" stroke-width="{sw}" stroke-linejoin="round"/>'


def _platte():
    t, n = .45, ISO_N
    o = _poly([_p(0, n), _p(n, n), _p(n, n, -t), _p(0, n, -t)], G2) + _poly([_p(n, 0), _p(n, n), _p(n, n, -t), _p(n, 0, -t)], G3)
    o += _poly([_p(0, 0), _p(n, 0), _p(n, n), _p(0, n)], G)
    o += "".join(f'<path d="M{_p(i, 0)[0]:.1f} {_p(i, 0)[1]:.1f}L{_p(i, n)[0]:.1f} {_p(i, n)[1]:.1f}M{_p(0, i)[0]:.1f} {_p(0, i)[1]:.1f}L{_p(n, i)[0]:.1f} {_p(n, i)[1]:.1f}" stroke="{G2}" stroke-width="1.2"/>' for i in range(2, n, 2))
    return o


def _pflanze(x, y):
    a, b = _p(x, y)
    return (_poly([_p(x - .35, y - .35), _p(x + .35, y - .35), _p(x + .35, y + .35), _p(x - .35, y + .35)], G2)
            + _poly([_p(x - .35, y + .35), _p(x + .35, y + .35), _p(x + .35, y + .35, .7), _p(x - .35, y + .35, .7)], W)
            + _poly([_p(x + .35, y - .35), _p(x + .35, y + .35), _p(x + .35, y + .35, .7), _p(x + .35, y - .35, .7)], G2)
            + f'<circle cx="{a:.1f}" cy="{b - 1.6*ISO_S:.1f}" r="{.9*ISO_S:.1f}" fill="{M3}" stroke="{K}" stroke-width="2.2"/>')


def _schild(stift, t, px, py, breite, sockel=.35, fuss=True):
    """Ein Bauteil als aufrechte Tafel auf einem Fuß: steht in der Ebene y = py, Vorderseite zum Betrachter."""
    x0, y0, w, h = _box(t)
    hoehe = breite * h / w
    if hoehe > 4.4:                      # hohe Dinge (Roll-up) nicht aus dem Bild ragen lassen
        breite, hoehe = 4.4 * w / h, 4.4
    k = breite / w
    a, b, d = .866 * ISO_S * k, .5 * ISO_S * k, ISO_S * k
    ox, oy = _p(px, py, hoehe + sockel)
    e, f = ox - (a * x0), oy - (b * x0 + d * y0)
    rueck = [_p(px, py, sockel), _p(px + breite, py, sockel), _p(px + breite, py, sockel + hoehe), _p(px, py, sockel + hoehe)]
    dick = .18
    hinten = [(q[0] + .866 * dick * ISO_S, q[1] - .5 * dick * ISO_S) for q in rueck]
    o = _poly([rueck[3], rueck[2], hinten[2], hinten[3]], G2) + _poly([rueck[1], rueck[2], hinten[2], hinten[1]], G3)
    fx, fy = _p(px + breite / 2, py)
    gx, gy = _p(px + breite / 2, py, sockel)
    if fuss:
        o += f'<ellipse cx="{fx:.1f}" cy="{fy:.1f}" rx="{.5*ISO_S:.1f}" ry="{.25*ISO_S:.1f}" fill="{G3}" opacity=".6"/><path d="M{fx:.1f} {fy:.1f}V{gy:.1f}" stroke="{K}" stroke-width="2.4"/>'
    o += _poly(rueck, W)
    o += f'<g transform="matrix({a:.4f} {b:.4f} 0 {d:.4f} {e:.2f} {f:.2f})">' + TEILE[t["teil"]](STIFT["iso"], *t["args"], **t["kw"]) + "</g>"
    return o


def _figur(px, py, rolle):
    x, y = _p(px, py)
    f = {"a": M, "w": W}.get(rolle, W)
    s = ISO_S
    return (f'<ellipse cx="{x:.1f}" cy="{y:.1f}" rx="{.6*s:.1f}" ry="{.3*s:.1f}" fill="{G3}" opacity=".6"/>'
            + f'<path d="M{x-.2*s:.1f} {y:.1f}v{-1*s:.1f}M{x+.2*s:.1f} {y+.1*s:.1f}v{-1*s:.1f}" stroke="{K}" stroke-width="2.4" stroke-linecap="round"/>'
            + f'<rect x="{x-.45*s:.1f}" y="{y-2.6*s:.1f}" width="{.9*s:.1f}" height="{1.7*s:.1f}" rx="{.4*s:.1f}" fill="{f}" stroke="{K}" stroke-width="2.4"/>'
            + f'<circle cx="{x:.1f}" cy="{y-3.05*s:.1f}" r="{.42*s:.1f}" fill="{W}" stroke="{K}" stroke-width="2.4"/>')


def _quader(x, y, w, d, h, oben=W):
    return (_poly([_p(x, y + d), _p(x + w, y + d), _p(x + w, y + d, h), _p(x, y + d, h)], W)
            + _poly([_p(x + w, y), _p(x + w, y + d), _p(x + w, y + d, h), _p(x + w, y, h)], G2)
            + _poly([_p(x, y, h), _p(x + w, y, h), _p(x + w, y + d, h), _p(x, y + d, h)], oben))


def _tisch(x, y, w, d, h):
    beine = "".join(f'<path d="M{_p(a, b)[0]:.1f} {_p(a, b)[1]:.1f}L{_p(a, b, h)[0]:.1f} {_p(a, b, h)[1]:.1f}" stroke="{K}" stroke-width="2.4"/>' for a, b in ((x + .15, y + d - .15), (x + w - .15, y + d - .15), (x + w - .15, y + .15)))
    return beine + _quader(x, y, w, d, .22, W).replace(f'{_p(x, y)[1]:.1f}', f'{_p(x, y)[1]:.1f}') if False else beine + "".join(
        [_poly([_p(x, y + d, h - .22), _p(x + w, y + d, h - .22), _p(x + w, y + d, h), _p(x, y + d, h)], W),
         _poly([_p(x + w, y, h - .22), _p(x + w, y + d, h - .22), _p(x + w, y + d, h), _p(x + w, y, h)], G2),
         _poly([_p(x, y, h), _p(x + w, y, h), _p(x + w, y + d, h), _p(x, y + d, h)], W)])


def r_iso3d(m):
    """Kleine Bürosituation auf der Platte: großes Board hinten, Tisch mit dem zweiten Ding, weitere als Aufsteller, Menschen davor."""
    teile = [t for t in m["teile"] if t["teil"] not in ("tasse", "pult")]
    figuren = [t for t in teile if t["teil"] == "person"]
    schilder = sorted([t for t in teile if t["teil"] != "person"], key=lambda t: -(_box(t)[2] * _box(t)[3]))
    stuecke = [(15.0, _pflanze(7.2, .9))]
    if schilder:
        stuecke.append((2.6, _schild(STIFT["iso"], schilder[0], .5, 1.3, 4.6)))
    if len(schilder) > 1:
        t = schilder[1]; w, h = _box(t)[2], _box(t)[3]
        breite = max(1.4, min(2.8, 2.8 * min(1, (w / h) * 1.1)))
        stuecke.append((10.5, _tisch(4.0, 3.8, 3.2, 1.4, 1.1) + _schild(STIFT["iso"], t, 4.3, 4.4, breite, 1.15, False)))
    for j, (t, (px, py, b)) in enumerate(zip(schilder[2:], ((.6, 5.2, 2.2), (2.6, 6.4, 1.8)))):
        stuecke.append((px + py, _schild(STIFT["iso"], t, px, py, b)))
    for j, t in enumerate(figuren[:2]):
        px, py = ((4.8, 6.2), (6.4, 6.5))[j]
        stuecke.append((px + py + 1, _figur(px, py, t["args"][3] if len(t["args"]) > 3 else "w")))
    if not figuren:
        stuecke.append((14.6, _figur(5.4, 6.4, "a")))
    return bild(_platte() + "".join(o for _, o in sorted(stuecke, key=lambda v: v[0])), "Isometrisch 3D")


STILE = [("Monolinie", r_mono), ("Duoton", r_duo), ("Isometrisch 3D", r_iso3d), ("Glas", r_glas)]

# Seiten (Zeilen) – Titel, Bereich, Farbwelt, Motiv
SEITEN = [
    ("Startseite", "Strategie, die wirkt.", "gelb", "startseite"), ("Strategie in den Alltag überführen", "Strategiehandwerk", "gelb", "strategie"),
    ("Komplexe Themen", "Strategiehandwerk", "gelb", "komplexe"), ("Innovation & Geschäftsmodell", "Strategiehandwerk", "gelb", "innovation"),
    ("Teams befähigen", "Strategiehandwerk / Training", "gelb", "teams"), ("Workshops", "Formate", "magenta", "workshops"),
    ("KI zum Anfassen", "Workshops", "magenta", "ki"), ("Sprint Landingpage", "Workshops", "magenta", "sprint"),
    ("Moderation deines Workshops", "Workshops", "magenta", "moderation"), ("Der beste Workshop", "Workshops", "magenta", "bester"),
    ("Marketing 2.0", "Formate", "cyan", "marketing"), ("MarketingEcoSystem", "Marketing 2.0", "cyan", "mes"),
    ("sofort sichtbar", "Marketing 2.0", "cyan", "sofort"), ("Paid Ads", "Marketing 2.0", "cyan", "paidads"),
    ("Medien", "Marketing 2.0", "cyan", "medien"), ("PowerPoint", "Medien", "cyan", "powerpoint"), ("Landingpage", "Medien", "cyan", "landingpage"),
    ("Roll-up", "Medien", "cyan", "rollup"), ("Video", "Medien", "cyan", "video"), ("Digitale Tools", "Marketing 2.0", "cyan", "tools"),
    ("Training & Sparring", "Formate", "violett", "training"), ("1:1 Sparring", "Training & Sparring", "violett", "sparring"),
    ("Impulsvorträge", "Einzelseite", "violett", "impuls"),
]
