"""Skyline Crailsheim für die Wagenpaten-Seite (gelbe Silhouette, Details weiß ausgespart)."""
import math

G = 270  # Grundlinie (Oberkante der gelben Sektion)
B = 1440

def r(x, y, w, h, c="s"): return f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"/>'
def p(d, c="s"): return f'<path class="{c}" d="{d}"/>'
def fenster(x0, y0, sp, zl, w, h, dx, dy):
    return "".join(r(x0 + i * dx, y0 + j * dy, w, h, "f") for j in range(zl) for i in range(sp))

def haus(x, w, h, rh, fen=True):
    s = p(f"M{x} {G}V{G-h}L{x+w/2} {G-h-rh}L{x+w} {G-h}V{G}Z")
    if fen and w >= 26:
        n = max(1, int((w - 8) // 14))
        s += fenster(x + (w - (n * 14 - 6)) / 2, G - h + 10, n, max(1, int((h - 18) // 18)), 8, 9, 14, 18)
    return s

def baum(x, h, rk):
    return r(x - 2, G - h, 4, h) + f'<circle class="s" cx="{x}" cy="{G-h}" r="{rk}"/>'

def diebsturm(cx):
    s = r(cx - 22, G - 125, 44, 125)
    s += r(cx - 27, G - 137, 54, 12)
    s += p(f"M{cx-29} {G-137}L{cx} {G-192}L{cx+29} {G-137}Z")
    s += r(cx - 1, G - 202, 2, 12)
    s += r(cx - 3, G - 100, 6, 14, "f") + r(cx - 3, G - 60, 6, 14, "f")
    s += "".join(r(cx - 22 + 7 + i * 9, G - 135, 4, 6, "f") for i in range(4))
    return s

def riesenrad(cx, cy, R):
    s = f'<g class="l">'
    s += f'<circle cx="{cx}" cy="{cy}" r="{R}" stroke-width="7"/><circle cx="{cx}" cy="{cy}" r="{R*.72:.1f}" stroke-width="3"/>'
    for k in range(12):
        a = math.pi * 2 * k / 12
        s += f'<path d="M{cx} {cy}L{cx+R*math.cos(a):.1f} {cy+R*math.sin(a):.1f}" stroke-width="3"/>'
    s += f'<path d="M{cx} {cy}L{cx-R*.62:.1f} {G}M{cx} {cy}L{cx+R*.62:.1f} {G}" stroke-width="9"/></g>'
    s += f'<circle class="s" cx="{cx}" cy="{cy}" r="11"/>'
    for k in range(12):
        a = math.pi * 2 * k / 12 + math.pi / 12
        x, y = cx + R * math.cos(a), cy + R * math.sin(a)
        s += f'<rect class="s" x="{x-8:.1f}" y="{y+1:.1f}" width="16" height="13" rx="3"/>'
    return s

def festzelt(x, w):
    h, peak = 52, 46
    s = r(x, G - h, w, h)
    q = w / 4
    s += p(f"M{x-10} {G-h}L{x+q} {G-h-peak}L{x+2*q} {G-h-peak*.55}L{x+3*q} {G-h-peak}L{x+w+10} {G-h}Z")
    # Wimpel auf den Spitzen
    for fx in (x + q, x + 3 * q):
        s += r(fx - 1.5, G - h - peak - 26, 3, 26) + p(f"M{fx+1.5} {G-h-peak-26}L{fx+20} {G-h-peak-20}L{fx+1.5} {G-h-peak-14}Z")
    # Zierkante (Bögen) und Streifen
    n = int(w // 20)
    s += "".join(f'<path class="f" d="M{x+i*20+2} {G-h+2}a8 8 0 0 0 16 0z"/>' for i in range(n))
    s += "".join(r(x + 14 + i * 28, G - h + 16, 5, h - 16, "f") for i in range(int((w - 20) // 28)) if abs(x + 14 + i * 28 - (x + w / 2)) > 22)
    s += p(f"M{x+w/2-16} {G}V{G-22}a16 16 0 0 1 32 0V{G}Z", "f")
    return s

def rathaus(x):
    w, h = 170, 72
    s = r(x, G - h, w, h)
    s += p(f"M{x-6} {G-h}L{x+22} {G-h-30}L{x+w-22} {G-h-30}L{x+w+6} {G-h}Z")
    s += "".join(p(f"M{x+20+i*30} {G-h-28}V{G-h-42}h14V{G-h-28}Z") for i in (0, 4))
    s += fenster(x + 14, G - h + 14, 6, 2, 10, 14, 26, 26)
    cx = x + w / 2
    s += r(cx - 20, G - 182, 40, 82)            # Turmschaft
    s += r(cx - 24, G - 186, 48, 6)             # Gesims
    s += r(cx - 16, G - 214, 32, 28)            # Glockengeschoss
    s += p(f"M{cx-19} {G-214}C{cx-19} {G-232} {cx-6} {G-232} {cx-4} {G-244}H{cx+4}C{cx+6} {G-232} {cx+19} {G-232} {cx+19} {G-214}Z")  # Welsche Haube
    s += r(cx - 6, G - 258, 12, 14)             # Laterne
    s += p(f"M{cx-8} {G-258}C{cx-8} {G-266} {cx} {G-266} {cx} {G-280}C{cx} {G-266} {cx+8} {G-266} {cx+8} {G-258}Z")
    s += r(cx - 1, G - 292, 2, 14)
    s += f'<circle class="f" cx="{cx}" cy="{G-160}" r="10"/><path class="l2" d="M{cx} {G-160}V{G-167}M{cx} {G-160}h5"/>'
    s += p(f"M{cx-6} {G-196}V{G-204}a6 6 0 0 1 12 0V{G-196}Z", "f")
    s += p(f"M{cx-12} {G}V{G-26}a12 12 0 0 1 24 0V{G}Z", "f")
    return s

def kirche(x):
    s = r(x + 30, G - 60, 120, 60)
    s += p(f"M{x+26} {G-60}L{x+52} {G-104}L{x+150} {G-104}L{x+156} {G-60}Z")
    s += r(x, G - 150, 34, 150)
    s += p(f"M{x-3} {G-150}L{x+17} {G-232}L{x+37} {G-150}Z")
    s += r(x + 16, G - 246, 2, 16)
    s += "".join(p(f"M{x+46+i*26} {G-14}V{G-40}a6 8 0 0 1 12 0V{G-14}Z", "f") for i in range(4))
    s += p(f"M{x+12} {G-130}V{G-120}h10V{G-130}a5 6 0 0 0 -10 0Z", "f")
    s += f'<circle class="f" cx="{x+17}" cy="{G-100}" r="6"/>'
    return s

def villa(x):
    s = r(x, G - 78, 96, 78)
    s += "".join(r(x + i * 16, G - 88, 10, 10) for i in range(7))
    s += r(x + 84, G - 120, 30, 120)
    s += p(f"M{x+80} {G-120}L{x+99} {G-160}L{x+118} {G-120}Z")
    s += r(x - 12, G - 104, 22, 104)
    s += "".join(r(x - 12 + i * 8, G - 112, 6, 8) for i in range(3))
    s += "".join(p(f"M{x+14+i*24} {G-30}V{G-50}a6 6 0 0 1 12 0V{G-30}Z", "f") for i in range(3))
    s += p(f"M{x+93} {G-90}V{G-104}a6 6 0 0 1 12 0V{G-90}Z", "f") + r(x - 5, G - 80, 8, 12, "f")
    return s

def hochhaus(x):
    w, h = 64, 176
    s = r(x, G - h, w, h) + r(x + 8, G - h - 10, w - 16, 10) + r(x + w - 18, G - h - 30, 2, 20)
    s += fenster(x + 8, G - h + 8, 4, 13, 8, 6, 13, 12.5)
    return s

def wagen(x):
    s = r(x + 18, G - 40, 120, 14)
    s += r(x, G - 34, 20, 3)
    s += "".join(f'<circle class="s" cx="{cx}" cy="{G-13}" r="13"/><circle class="f" cx="{cx}" cy="{G-13}" r="4"/>' for cx in (x + 40, x + 116))
    s += f'<path class="l" stroke-width="5" d="M{x+24} {G-40}V{G-74}Q{x+78} {G-104} {x+132} {G-74}V{G-40}"/>'
    s += "".join(p(f"M{x+34+i*16} {G-82+abs(i-3)*3}l6 12l6 -12z") for i in range(7))
    for bx, by in ((x + 50, G - 120), (x + 78, G - 132), (x + 108, G - 118)):
        s += f'<circle class="s" cx="{bx}" cy="{by}" r="9"/><path class="l" stroke-width="1.6" d="M{bx} {by+9}Q{bx-4} {by+24} {bx} {G-92}"/>'
    s += "".join(r(x + 30 + i * 22, G - 56, 12, 12, "s") for i in range(5))
    return s

def bruecke(x, w):
    s = r(x, G - 32, w, 32) + r(x - 4, G - 38, w + 8, 6)
    s += "".join(r(x + 4 + i * 12, G - 48, 3, 10) for i in range(int(w // 12)))
    s += r(x - 4, G - 50, w + 8, 3)
    n = 3; bw = (w - 16) / n
    s += "".join(p(f"M{x+8+i*bw+3:.1f} {G}V{G-8}a{bw/2-3:.1f} {16} 0 0 1 {bw-6:.1f} 0V{G}Z", "f") for i in range(n))
    return s

def wasserturm(cx):
    s = p(f"M{cx-13} {G}L{cx-9} {G-148}H{cx+9}L{cx+13} {G}Z")
    s += f'<ellipse class="s" cx="{cx}" cy="{G-162}" rx="27" ry="20"/>'
    s += r(cx - 24, G - 184, 48, 6)
    s += p(f"M{cx-21} {G-184}C{cx-24} {G-206} {cx-5} {G-206} {cx-2} {G-222}H{cx+2}C{cx+5} {G-206} {cx+24} {G-206} {cx+21} {G-184}Z")
    s += r(cx - 1, G - 234, 2, 13)
    s += "".join(r(cx - 18 + i * 10, G - 166, 5, 9, "f") for i in range(4))
    s += r(cx - 2, G - 120, 4, 12, "f") + r(cx - 2, G - 80, 4, 12, "f") + p(f"M{cx-6} {G}V{G-14}a6 6 0 0 1 12 0V{G}Z", "f")
    return s

def eiloder(ex):
    s = r(ex - 7, G - 28, 4, 26) + r(ex + 3, G - 28, 4, 26)
    s += p(f"M{ex-13} {G}h10v-4h-6z") + p(f"M{ex+13} {G}h-10v-4h6z")
    s += f'<ellipse class="s" cx="{ex-7}" cy="{G-36}" rx="11" ry="10"/><ellipse class="s" cx="{ex+7}" cy="{G-36}" rx="11" ry="10"/>'
    s += r(ex - 11, G - 31, 8, 2.5, "f") + r(ex + 3, G - 31, 8, 2.5, "f")
    s += p(f"M{ex-10} {G-76}H{ex+10}L{ex+13} {G-46}H{ex-13}Z")
    s += "".join(f'<circle class="f" cx="{ex}" cy="{G-70+i*8}" r="1.6"/>' for i in range(3))
    s += f'<circle class="s" cx="{ex}" cy="{G-84}" r="7"/>'
    s += p(f"M{ex-21} {G-99}L{ex-11} {G-90}H{ex+11}L{ex+21} {G-99}L{ex+7} {G-95}L{ex} {G-108}L{ex-7} {G-95}Z")
    s += f'<path class="l" stroke-width="5" stroke-linecap="round" d="M{ex+9} {G-72}L{ex+22} {G-84}M{ex-9} {G-72}L{ex-15} {G-52}"/>'
    s += f'<path class="l" stroke-width="2.4" d="M{ex+22} {G-80}V{G-130}"/>'
    s += p(f"M{ex-6} {G-124}a28 22 0 0 1 56 0" + "a7 4.5 0 0 0 -14 0" * 4 + "Z")
    s += r(ex + 21, G - 154, 2, 9)
    return s

TEILE = [
    bruecke(4, 140),
    haus(150, 22, 30, 14, False), haus(172, 50, 56, 28), baum(240, 34, 15),
    diebsturm(286),
    haus(322, 40, 44, 24),
    riesenrad(456, 140, 92),
    baum(566, 30, 14),
    festzelt(590, 176),
    haus(778, 30, 58, 22, False),
    rathaus(816),
    haus(992, 40, 50, 24),
    kirche(1042),
    haus(1206, 26, 40, 16, False),
    wasserturm(1268),
    villa(1328),
    haus(1450, 24, 40, 18, False),
    hochhaus(1478),
    eiloder(1578),
    wagen(1612), haus(1754, 26, 30, 16, False),
]

def svg():
    inhalt = "".join(TEILE)
    return ('<div class="skyline" aria-hidden="true"><svg viewBox="-6 -26 1792 296">'
            '<style>.s{fill:#fff400}.f{fill:#fff}.l{fill:none;stroke:#fff400}.l2{fill:none;stroke:#fff400;stroke-width:2;stroke-linecap:round}</style>'
            + inhalt + "</svg></div>")

if __name__ == "__main__":
    print(len(svg()))
