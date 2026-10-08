"""Festumzug als Silhouette für die Wagenpaten-Seite (gelb, Details weiß ausgespart).
Sitzt auf der Oberkante der gelben Sektion. Der Zug läuft nach rechts."""

G = 176  # Grundlinie (Oberkante der gelben Sektion)

def r(x, y, w, h, c="s", rx=0): return f'<rect class="{c}" x="{x:.1f}" y="{y:.1f}" width="{w:.1f}" height="{h:.1f}"' + (f' rx="{rx}"' if rx else "") + "/>"
def p(d, c="s"): return f'<path class="{c}" d="{d}"/>'
def c(x, y, rad, k="s"): return f'<circle class="{k}" cx="{x:.1f}" cy="{y:.1f}" r="{rad}"/>'
def ln(d, w, k="l"): return f'<path class="{k}" stroke-width="{w}" d="{d}"/>'

def mensch(x, s=1.0, hut=True, schritt=1):
    """Gehende Person, Blick nach rechts. s = Größe (Kinder kleiner)."""
    h = lambda v: G - v * s
    a = 8 * s * schritt
    out = ln(f"M{x} {h(34)}L{x-a} {G}M{x} {h(34)}L{x+a} {G}", 6.5 * s)
    out += r(x - 8 * s, h(64), 16 * s, 34 * s, rx=4 * s)
    out += c(x + 1 * s, h(72), 7 * s)
    if hut:
        out += r(x - 9 * s, h(78), 20 * s, 3 * s) + r(x - 5 * s, h(85), 12 * s, 8 * s, rx=2) + ln(f"M{x+5*s} {h(84)}l5 -8", 1.6 * s)
    return out

def arm(x, s, zx, zy):
    return ln(f"M{x+4*s} {G-58*s}L{zx} {zy}", 5 * s)

def tuba(x):
    out = mensch(x) + f'<ellipse cx="{x}" cy="{G-50}" rx="15" ry="11" class="l" stroke-width="5"/>'
    out += ln(f"M{x+12} {G-56}Q{x+22} {G-80} {x+14} {G-92}", 7)
    out += c(x + 14, G - 104, 19) + c(x + 14, G - 104, 13, "f") + c(x + 14, G - 104, 5)
    return out

def trommel(x):
    return mensch(x) + c(x + 14, G - 44, 16) + c(x + 14, G - 44, 12, "f") + c(x + 14, G - 44, 8) + \
        ln(f"M{x+4} {G-58}L{x+30} {G-66}", 4) + c(x + 31, G - 67, 3.5)

def trompete(x):
    return mensch(x) + arm(x, 1, x + 18, G - 70) + ln(f"M{x+7} {G-72}H{x+30}", 3.5) + p(f"M{x+28} {G-72}L{x+38} {G-79}V{G-65}Z")

def posaune(x):
    return mensch(x) + arm(x, 1, x + 22, G - 68) + ln(f"M{x+7} {G-73}H{x+44}M{x+16} {G-67}H{x+44}", 2.6) + \
        ln(f"M{x+44} {G-73}V{G-67}", 2.6) + p(f"M{x+10} {G-73}L{x+2} {G-80}V{G-66}Z")

def klarinette(x):
    return mensch(x) + arm(x, 1, x + 14, G - 56) + ln(f"M{x+8} {G-71}L{x+20} {G-46}", 3.2) + p(f"M{x+17} {G-48}L{x+26} {G-42}L{x+19} {G-40}Z")

def fahne(x, streifen=True):
    out = mensch(x) + arm(x, 1, x + 10, G - 64) + ln(f"M{x+10} {G-30}L{x+12} {G-150}", 3.4)
    out += p(f"M{x+12} {G-148}C{x+30} {G-158} {x+44} {G-138} {x+64} {G-146}V{G-108}C{x+44} {G-100} {x+30} {G-120} {x+12} {G-110}Z")
    if streifen:
        out += p(f"M{x+12} {G-133}C{x+30} {G-143} {x+44} {G-123} {x+64} {G-131}V{G-123}C{x+44} {G-115} {x+30} {G-135} {x+12} {G-125}Z", "f")
    return out + c(x + 12, G - 153, 4)

def kind(x, ballon=True, h=1):
    s = .66
    out = mensch(x, s, hut=False, schritt=h)
    if ballon:
        out += arm(x, s, x + 12, G - 52) + ln(f"M{x+12} {G-52}Q{x+8} {G-80} {x+14} {G-100}", 1.4) + \
            f'<ellipse class="s" cx="{x+14}" cy="{G-110}" rx="9" ry="11"/>' + p(f"M{x+12} {G-99}h4l-2 4z")
    else:
        out += arm(x, s, x + 12, G - 64)
    return out

def pferd(x):
    o = lambda dx, dy: f"{x+dx} {G+dy}"
    out = f'<ellipse class="s" cx="{x}" cy="{G-52}" rx="35" ry="18"/>'
    out += p(f"M{o(14,-62)}Q{o(26,-92)} {o(42,-104)}L{o(52,-96)}Q{o(44,-78)} {o(36,-48)}Z")
    out += p(f"M{o(40,-106)}L{o(66,-88)}Q{o(70,-80)} {o(62,-78)}L{o(44,-86)}Z")
    out += p(f"M{o(41,-104)}L{o(43,-114)}L{o(48,-102)}Z") + c(x + 44, G - 118, 4.5)
    out += p(f"M{o(16,-62)}Q{o(24,-90)} {o(38,-104)}L{o(32,-102)}Q{o(18,-90)} {o(10,-64)}Z")
    out += "".join(r(x + lx, G - 42, 7, 36) + r(x + lx - 2, G - 7, 11, 7, rx=2) for lx in (-28, -18, 14, 24))
    out += p(f"M{o(-33,-60)}Q{o(-46,-46)} {o(-41,-20)}L{o(-35,-22)}Q{o(-38,-44)} {o(-29,-54)}Z")
    out += ln(f"M{x+20} {G-74}Q{x+30} {G-62} {x+37} {G-50}", 2.6, "lw")
    return out

def rad(x, y, rad_):
    out = c(x, y, rad_) + c(x, y, rad_ - 4, "f")
    out += "".join(ln(f"M{x} {y}l{rad_*dx:.1f} {rad_*dy:.1f}", 2.2) for dx, dy in ((1,0),(-1,0),(0,1),(0,-1),(.7,.7),(-.7,.7),(.7,-.7),(-.7,-.7)))
    return out + c(x, y, 4)

def bierwagen(x):
    out = r(x, G - 44, 150, 10) + rad(x + 26, G - 20, 20) + rad(x + 124, G - 16, 16)
    for i, (bx, by) in enumerate(((10, 0), (42, 0), (74, 0), (26, 1), (58, 1))):
        X, Y = x + bx, G - 76 - by * 30
        out += r(X, Y, 30, 32, rx=8) + r(X, Y + 9, 30, 2.5, "f") + r(X, Y + 21, 30, 2.5, "f")
    out += r(x + 112, G - 70, 28, 26)
    out += ln(f"M{x+150} {G-38}L{x+214} {G-58}", 3.2)
    return out

def kutscher(x):
    # sitzende Figur auf dem Bock
    y = G - 70
    out = r(x - 8, y - 32, 16, 30, rx=4) + c(x + 1, y - 40, 7) + r(x - 9, y - 46, 20, 3) + r(x - 5, y - 53, 12, 8, rx=2)
    out += ln(f"M{x+4} {y-26}L{x+22} {y-20}", 5) + ln(f"M{x+22} {y-20}Q{x+40} {y-70} {x+70} {y-56}", 1.6)
    return out

def traktor(x):
    out = r(x, G - 44, 60, 20, rx=3) + r(x + 6, G - 78, 30, 36, rx=3) + r(x + 11, G - 72, 20, 14, "f", 2)
    out += ln(f"M{x+50} {G-44}V{G-66}", 4) + rad(x + 18, G - 20, 20) + rad(x + 56, G - 13, 13)
    out += ln(f"M{x} {G-30}H{x-18}", 3)
    return out

def festwagen(x):
    out = r(x + 18, G - 40, 120, 14)
    out += "".join(c(cx, G - 13, 13) + c(cx, G - 13, 4, "f") for cx in (x + 40, x + 116))
    out += ln(f"M{x+24} {G-40}V{G-74}Q{x+78} {G-104} {x+132} {G-74}V{G-40}", 5)
    out += "".join(p(f"M{x+34+i*16} {G-82+abs(i-3)*3}l6 12l6 -12z") for i in range(7))
    for bx, by in ((x + 50, G - 120), (x + 78, G - 132), (x + 108, G - 118)):
        out += c(bx, by, 9) + ln(f"M{bx} {by+9}Q{bx-4} {by+24} {bx} {G-92}", 1.6)
    out += "".join(r(x + 30 + i * 22, G - 56, 12, 12) for i in range(5))
    return out

def eiloder(ex):
    s = r(ex - 7, G - 28, 4, 26) + r(ex + 3, G - 28, 4, 26)
    s += p(f"M{ex-13} {G}h10v-4h-6z") + p(f"M{ex+13} {G}h-10v-4h6z")
    s += f'<ellipse class="s" cx="{ex-7}" cy="{G-36}" rx="11" ry="10"/><ellipse class="s" cx="{ex+7}" cy="{G-36}" rx="11" ry="10"/>'
    s += r(ex - 11, G - 31, 8, 2.5, "f") + r(ex + 3, G - 31, 8, 2.5, "f")
    s += p(f"M{ex-10} {G-76}H{ex+10}L{ex+13} {G-46}H{ex-13}Z")
    s += "".join(c(ex, G - 70 + i * 8, 1.6, "f") for i in range(3))
    s += c(ex, G - 84, 7)
    s += p(f"M{ex-21} {G-99}L{ex-11} {G-90}H{ex+11}L{ex+21} {G-99}L{ex+7} {G-95}L{ex} {G-108}L{ex-7} {G-95}Z")
    s += ln(f"M{ex+9} {G-72}L{ex+22} {G-84}M{ex-9} {G-72}L{ex-15} {G-52}", 5)
    s += ln(f"M{ex+22} {G-80}V{G-130}", 2.4)
    s += p(f"M{ex-6} {G-124}a28 22 0 0 1 56 0" + "a7 4.5 0 0 0 -14 0" * 4 + "Z")
    return s + r(ex + 21, G - 154, 2, 9)

TEILE = [
    festwagen(14), traktor(170),
    kind(300), kind(336, False, -1), kind(372),
    bierwagen(440), kutscher(566), pferd(694), pferd(790),
    trommel(880), tuba(956), posaune(1030), trompete(1112), trompete(1182), klarinette(1250),
    fahne(1330), fahne(1416, False),
    kind(1510, False), kind(1546), kind(1582, False, -1),
    eiloder(1676),
]

def svg():
    return ('<div class="umzug" aria-hidden="true"><svg viewBox="0 -2 1740 178">'
            '<style>.s{fill:#fff400}.f{fill:#fff}.l{fill:none;stroke:#fff400;stroke-linecap:round;stroke-linejoin:round}'
            '.lw{fill:none;stroke:#fff;stroke-linecap:round}</style>' + "".join(TEILE) + "</svg></div>")
