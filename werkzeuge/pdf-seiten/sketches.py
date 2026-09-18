"""Deckblatt-Skizzen im empiria-Stil (weiß/transparent gezeichnet, im PDF per invert grau/schwarz)."""
import os
W = "rgba(255,255,255,{a})"
def st(a=.42, w=1.6, fill=.05, dash=None):
    d = f' stroke-dasharray="{dash}"' if dash else ''
    if isinstance(fill, str): f = fill
    else: f = W.format(a=fill) if fill else 'none'
    return f'fill="{f}" stroke="{W.format(a=a)}" stroke-width="{w}" stroke-linecap="round" stroke-linejoin="round"{d}'
def bar(x, y, w, h=5, a=.4): return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{W.format(a=a)}"/>'
def head(cx, cy, r=9, a=.5):
    return (f'<circle cx="{cx}" cy="{cy}" r="{r}" {st(a, 1.6, .06)}/>'
            f'<path d="M{cx-r*1.7},{cy+r*3.1} c0,-{r*1.9} {r*0.8},-{r*1.8} {r*1.7},-{r*1.8} s{r*1.7},{-0.1*r} {r*1.7},{r*1.8}" {st(a, 1.6, .06)}/>')
def svg(vb, inner, label): return f'<svg viewBox="{vb}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="{label}">{inner}</svg>'
def ground(x1, x2, y, a=.25): return f'<path d="M{x1},{y} H{x2}" stroke="{W.format(a=a)}" stroke-width="1.4" stroke-linecap="round"/>'
def arrow(d, a=.6, w=2, dash=None):
    return f'<path d="{d}" {st(a, w, 0, dash)}/>'

def strategie():
    i = ground(20, 420, 232)
    # Weg von links unten nach rechts oben
    i += arrow("M40,222 C120,222 110,160 190,160 S260,104 330,96", .5, 2.2, "5 6")
    for (x, y, n) in [(40, 222, 1), (190, 160, 2), (330, 96, 3)]:
        i += f'<circle cx="{x}" cy="{y}" r="15" {st(.8, 2, "#1c1c1c")}/>'
        i += f'<text x="{x}" y="{y+4.5}" text-anchor="middle" font-family="Lora" font-weight="700" font-size="13" fill="{W.format(a=.9)}">{n}</text>'
    # Flagge
    i += f'<path d="M372,96 V20" {st(.7, 2, 0)}/><path d="M372,22 H410 L398,36 L410,50 H372" {st(.7, 1.8, .12)}/>'
    i += arrow("M345,96 H366", .5, 1.8)
    # Karten zu den Stationen
    for (x, y, w) in [(64, 176, 70), (206, 112, 78), (250, 180, 86)]:
        i += f'<rect x="{x}" y="{y}" width="{w}" height="30" rx="5" {st(.35, 1.3, .05)}/>' + bar(x+9, y+9, w*.62, 4, .45) + bar(x+9, y+18, w*.42, 4, .28)
    return svg("0 0 440 250", i, "Skizze: ein Weg in drei Stationen hin zu einer Flagge")

def komplexe():
    i = ground(20, 420, 238)
    # links: unsortierter Stapel Folien
    for k, (dx, dy, r) in enumerate([(0, 0, -7), (10, 8, 4), (20, 14, -2)]):
        i += f'<g transform="rotate({r} {80+dx} {120+dy})"><rect x="{24+dx}" y="{80+dy}" width="112" height="76" rx="5" {st(.38, 1.5, "#0f0f0f")}/>' + bar(36+dx, 94+dy, 70, 4, .35) + bar(36+dx, 104+dy, 88, 3.5, .22) + bar(36+dx, 112+dy, 60, 3.5, .22) + bar(36+dx, 120+dy, 80, 3.5, .22) + '</g>'
    i += arrow("M60,196 c10,8 22,-10 34,0 s22,8 34,-2", .4, 1.6)
    # Pfeil
    i += arrow("M172,128 H236", .7, 2.2) + arrow("M226,118 L238,128 L226,138", .7, 2.2)
    # rechts: klare Folie + Ziel
    i += f'<rect x="250" y="62" width="146" height="104" rx="6" {st(.55, 1.8, .08)}/>'
    i += bar(266, 80, 90, 7, .6) + bar(266, 96, 60, 4, .35)
    for k in range(3):
        i += f'<circle cx="{280 + k*43}" cy="{136}" r="12" {st(.5, 1.5, .08)}/>'
    i += f'<path d="M323,166 V214 M293,238 L323,214 L353,238" {st(.4, 1.6, 0)}/>'
    i += f'<circle cx="412" cy="42" r="20" {st(.75, 2, "#161616")}/><circle cx="412" cy="42" r="10" {st(.75, 1.8, 0)}/><circle cx="412" cy="42" r="3" fill="{W.format(a=.9)}"/>'
    return svg("0 0 440 250", i, "Skizze: ein Stapel unsortierter Folien wird zu einer klaren Folie mit Ziel")

def innovation():
    i = ground(20, 420, 232)
    # Mauer aus Blöcken, ein Block herausgelöst
    bw, bh = 62, 34
    for r in range(4):
        off = 0 if r % 2 == 0 else bw / 2
        for c in range(4):
            x = 40 + off + c * bw
            y = 232 - (r + 1) * bh
            if (r, c) == (2, 2):
                i += f'<rect x="{x+2}" y="{y+2}" width="{bw-4}" height="{bh-4}" rx="3" {st(.5, 1.4, 0, "4 4")}/>'
                continue
            if x + bw > 300: continue
            i += f'<rect x="{x+2}" y="{y+2}" width="{bw-4}" height="{bh-4}" rx="3" {st(.35, 1.4, .06)}/>'
    # herausgelöster Block, gedreht, oben rechts
    i += f'<g transform="rotate(-14 352 70)"><rect x="323" y="53" width="58" height="30" rx="3" {st(.8, 2, .14)}/></g>'
    i += arrow("M236,120 C260,70 290,64 314,70", .6, 1.8, "5 5") + arrow("M304,62 L316,70 L305,80", .6, 1.8)
    i += f'<path d="M352,20 v12 M352,108 v12 M402,70 h12 M290,70 h-0 M390,34 l8,-8 M390,106 l8,8" {st(.5, 1.6, 0)}/>'
    return svg("0 0 440 250", i, "Skizze: eine Mauer aus Bausteinen, ein Baustein wird herausgelöst und neu gedacht")

def sprint():
    i = ground(20, 420, 236)
    i += f'<rect x="40" y="30" width="270" height="186" rx="10" {st(.42, 1.6, .05)}/>'
    i += f'<path d="M40,52 H310" {st(.3, 1.2, 0)}/>'
    for k in range(3): i += f'<circle cx="{56+k*11}" cy="41" r="3" fill="{W.format(a=.5)}"/>'
    i += f'<rect x="56" y="64" width="238" height="58" rx="5" {st(.4, 1.3, .08)}/>' + bar(70, 80, 120, 8, .6) + bar(70, 96, 84, 4, .35) + f'<rect x="70" y="106" width="46" height="10" rx="5" fill="{W.format(a=.55)}"/>'
    for k in range(3):
        x = 56 + k * 82
        i += f'<rect x="{x}" y="134" width="74" height="66" rx="5" {st(.35, 1.3, .05)}/>' + f'<circle cx="{x+14}" cy="150" r="6" {st(.45, 1.3, .08)}/>' + bar(x+10, 166, 52, 4, .4) + bar(x+10, 176, 40, 3.5, .25) + bar(x+10, 185, 46, 3.5, .25)
    # Stoppuhr
    i += f'<circle cx="350" cy="150" r="58" {st(.8, 2.2, .12)}/><path d="M340,84 h20 M350,84 v8 M392,104 l8,-8" {st(.8, 2.2, 0)}/>'
    i += f'<path d="M350,150 V112" {st(.9, 2.4, 0)}/><path d="M350,150 L378,166" {st(.9, 2.4, 0)}/>'
    i += f'<text x="350" y="190" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="17" fill="{W.format(a=.9)}">48h</text>'
    return svg("0 0 440 250", i, "Skizze: eine Landingpage im Browser mit einer Stoppuhr für 48 Stunden")

def mes():
    i = ''
    cx, cy, R = 220, 130, 92
    i += f'<circle cx="{cx}" cy="{cy}" r="{R}" {st(.35, 1.6, 0, "6 6")}/>'
    # Pfeilspitzen auf dem Kreis
    for (x, y, rot) in [(300, 84, 60), (220, 222, 180), (140, 84, 300)]:
        i += f'<g transform="rotate({rot} {x} {y})"><path d="M{x-7},{y-6} L{x+3},{y} L{x-7},{y+6}" {st(.6, 2, 0)}/></g>'
    # Knoten: Landingpage (oben), Kanäle (rechts unten), Dashboard (links unten)
    i += f'<rect x="{cx-44}" y="{cy-R-30}" width="88" height="60" rx="6" {st(.6, 1.8, "#161616")}/>' + bar(cx-34, cy-R-18, 50, 5, .6) + bar(cx-34, cy-R-8, 64, 3.5, .3) + bar(cx-34, cy-R+1, 40, 3.5, .3) + f'<rect x="{cx-34}" y="{cy-R+12}" width="26" height="8" rx="4" fill="{W.format(a=.5)}"/>'
    x, y = cx + 80, cy + 46
    i += f'<rect x="{x-22}" y="{y-38}" width="44" height="76" rx="7" {st(.6, 1.8, "#161616")}/>' + f'<rect x="{x-14}" y="{y-26}" width="28" height="26" rx="3" {st(.4, 1.2, .1)}/>' + bar(x-14, y+6, 28, 3.5, .35) + bar(x-14, y+14, 18, 3.5, .35)
    x, y = cx - 80, cy + 46
    i += f'<rect x="{x-44}" y="{y-32}" width="88" height="64" rx="6" {st(.6, 1.8, "#161616")}/>'
    for k, hgt in enumerate([14, 24, 18, 34, 28]):
        i += f'<rect x="{x-32+k*14}" y="{y+20-hgt}" width="8" height="{hgt}" rx="2" fill="{W.format(a=.5)}"/>'
    i += f'<path d="M{x-34},{y-14} l18,-6 16,4 18,-10 14,-2" {st(.7, 1.6, 0)}/>'
    i += f'<circle cx="{cx}" cy="{cy}" r="22" {st(.8, 2, "#1c1c1c")}/><path d="M{cx-9},{cy} a9,9 0 1 1 3,7" {st(.85, 2, 0)}/><path d="M{cx-12},{cy+2} l3,-5 4,4" {st(.85, 2, 0)}/>'
    return svg("0 0 440 262", i, "Skizze: Kreislauf aus Landingpage, Social-Media-Kanälen und Dashboard")

def sofort():
    i = ground(20, 420, 238)
    # Landingpage-Fenster hinten
    i += f'<rect x="150" y="26" width="240" height="160" rx="9" {st(.38, 1.6, .05)}/><path d="M150,46 H390" {st(.28, 1.2, 0)}/>'
    i += bar(170, 62, 110, 8, .55) + bar(170, 78, 150, 4, .3) + bar(170, 88, 120, 4, .3) + f'<rect x="170" y="102" width="52" height="12" rx="6" fill="{W.format(a=.5)}"/>'
    i += f'<rect x="300" y="60" width="72" height="56" rx="5" {st(.35, 1.2, .08)}/><path d="M318,98 l12,-14 10,10 8,-6 14,10" {st(.4, 1.3, 0)}/>'
    i += f'<rect x="170" y="128" width="100" height="40" rx="5" {st(.3, 1.2, .05)}/><rect x="280" y="128" width="92" height="40" rx="5" {st(.3, 1.2, .05)}/>'
    # Smartphone mit Posting vorne links
    i += f'<rect x="64" y="70" width="98" height="168" rx="14" {st(.7, 2, "#161616")}/>'
    i += f'<circle cx="84" cy="96" r="7" {st(.5, 1.3, .1)}/>' + bar(96, 92, 44, 4, .5)
    i += f'<rect x="76" y="110" width="74" height="62" rx="4" {st(.45, 1.3, .1)}/><path d="M86,160 l14,-18 12,12 10,-8 18,14" {st(.5, 1.4, 0)}/>'
    i += bar(76, 182, 64, 4, .45) + bar(76, 192, 48, 4, .3)
    i += f'<path d="M80,212 c4,-6 12,-6 12,0 c0,-6 8,-6 12,0 c0,6 -12,12 -12,12 s-12,-6 -12,-12z" {st(.6, 1.3, .15)}/>'
    # Briefumschlag rechts
    i += f'<g transform="rotate(8 360 196)"><rect x="318" y="170" width="86" height="56" rx="5" {st(.7, 1.9, "#161616")}/><path d="M320,174 L361,204 L402,174" {st(.7, 1.8, 0)}/></g>'
    i += arrow("M300,214 C280,230 230,232 186,210", .5, 1.6, "4 5")
    return svg("0 0 440 250", i, "Skizze: Smartphone mit Posting, Landingpage und E-Mail")

def paid_ads():
    i = ground(20, 420, 238)
    # Suchfeld mit Anzeige
    i += f'<rect x="30" y="30" width="230" height="130" rx="9" {st(.42, 1.6, .05)}/>'
    i += f'<rect x="46" y="46" width="198" height="24" rx="12" {st(.5, 1.4, .08)}/><circle cx="62" cy="58" r="5" {st(.6, 1.4, 0)}/><path d="M66,62 l4,4" {st(.6, 1.4, 0)}/>' + bar(78, 56, 90, 4, .4)
    i += f'<rect x="46" y="82" width="198" height="36" rx="5" {st(.6, 1.6, .12)}/><rect x="54" y="90" width="26" height="9" rx="2" fill="{W.format(a=.55)}"/>' + bar(86, 91, 110, 5, .6) + bar(54, 106, 150, 3.5, .3)
    i += bar(46, 130, 160, 4, .25) + bar(46, 140, 120, 3.5, .18)
    # Social Post
    i += f'<rect x="200" y="104" width="118" height="126" rx="9" {st(.6, 1.8, "#141414")}/>' + f'<circle cx="216" cy="120" r="7" {st(.5, 1.3, .1)}/>' + bar(228, 116, 50, 4, .45)
    i += f'<rect x="210" y="134" width="98" height="60" rx="4" {st(.4, 1.3, .1)}/><path d="M220,184 l16,-20 12,12 10,-8 20,16" {st(.45, 1.4, 0)}/>'
    i += f'<rect x="210" y="202" width="54" height="14" rx="7" fill="{W.format(a=.55)}"/>'
    # Balken + Trend
    for k, hgt in enumerate([30, 48, 66, 92]):
        i += f'<rect x="{338+k*20}" y="{232-hgt}" width="13" height="{hgt}" rx="2.5" {st(.55, 1.4, .1)}/>'
    i += arrow("M334,150 L366,128 L386,138 L420,96", .8, 2.2) + arrow("M404,94 L421,95 L418,112", .8, 2.2)
    return svg("0 0 440 250", i, "Skizze: Suchanzeige, Social-Media-Anzeige und steigende Ergebnisse")

def medien():
    i = ground(20, 420, 238)
    # Leinwand mit Folie
    i += f'<rect x="28" y="40" width="190" height="124" rx="6" {st(.5, 1.7, .07)}/>' + bar(44, 58, 104, 8, .6) + bar(44, 74, 70, 4, .32)
    for k in range(3): i += f'<rect x="{44+k*56}" y="94" width="46" height="52" rx="4" {st(.4, 1.3, .06)}/>' + f'<circle cx="{67+k*56}" cy="112" r="8" {st(.45, 1.3, .1)}/>' + bar(52+k*56, 128, 30, 3.5, .35)
    i += f'<path d="M123,164 V210 M96,238 L123,210 L150,238" {st(.38, 1.6, 0)}/>'
    # Smartphone Landingpage
    i += f'<rect x="236" y="92" width="72" height="140" rx="12" {st(.65, 1.9, .1)}/>' + bar(248, 112, 44, 6, .55) + bar(248, 124, 34, 3.5, .3) + f'<rect x="248" y="136" width="48" height="36" rx="3" {st(.35, 1.2, .08)}/>' + f'<rect x="248" y="182" width="30" height="9" rx="4.5" fill="{W.format(a=.5)}"/>' + bar(248, 200, 44, 3.5, .25)
    # Roll-up
    i += f'<rect x="336" y="28" width="72" height="196" rx="3" {st(.55, 1.8, .08)}/>' + f'<rect x="326" y="224" width="92" height="10" rx="3" {st(.55, 1.6, .12)}/>'
    i += bar(348, 46, 48, 7, .6) + bar(348, 60, 34, 4, .3) + f'<circle cx="372" cy="110" r="22" {st(.45, 1.4, .08)}/><path d="M362,110 l7,7 13,-14" {st(.6, 1.6, 0)}/>' + bar(348, 150, 48, 4, .35) + bar(348, 160, 40, 4, .35) + bar(348, 170, 44, 4, .35)
    return svg("0 0 440 250", i, "Skizze: Präsentationsfolie, Landingpage auf dem Smartphone und Roll-up")

def training_sparring():
    i = ground(20, 420, 236)
    # links: Team vor einer Tafel
    i += f'<rect x="40" y="26" width="160" height="96" rx="6" {st(.45, 1.6, .06)}/>' + bar(56, 44, 90, 7, .55) + arrow("M58,96 l24,-18 20,10 28,-22 26,8", .5, 1.6)
    for k, x in enumerate([54, 100, 146, 192]):
        i += head(x, 168, 10, .5)
    # rechts: 1:1
    i += head(292, 160, 12, .6) + head(386, 160, 12, .6)
    i += f'<path d="M268,82 h64 a8,8 0 0 1 8,8 v22 a8,8 0 0 1 -8,8 h-40 l-12,12 v-12 h-12 a8,8 0 0 1 -8,-8 v-22 a8,8 0 0 1 8,-8z" {st(.6, 1.6, .1)}/>' + bar(278, 96, 40, 4, .45) + bar(278, 106, 28, 4, .3)
    i += f'<path d="M350,56 h56 a8,8 0 0 1 8,8 v22 a8,8 0 0 1 -8,8 h-12 v12 l-12,-12 h-32 a8,8 0 0 1 -8,-8 v-22 a8,8 0 0 1 8,-8z" {st(.6, 1.6, .1)}/><path d="M366,76 l8,8 16,-16" {st(.7, 1.8, 0)}/>'
    i += f'<path d="M232,40 V226" {st(.2, 1.2, 0, "4 6")}/>'
    return svg("0 0 440 250", i, "Skizze: ein Team vor einer Tafel und ein Gespräch unter vier Augen")

def praesentation():
    i = ground(20, 420, 236)
    i += f'<rect x="150" y="22" width="220" height="136" rx="6" {st(.5, 1.7, .07)}/>' + bar(168, 40, 120, 8, .6) + bar(168, 56, 80, 4, .32)
    i += f'<path d="M172,136 l30,-22 26,14 30,-34 26,10 36,-30" {st(.6, 1.8, 0)}/>'
    for (x, y) in [(202, 114), (228, 128), (258, 94), (284, 104)]: i += f'<circle cx="{x}" cy="{y}" r="3.5" fill="{W.format(a=.7)}"/>'
    # Sprecher
    i += head(104, 150, 12, .75)
    i += f'<path d="M126,166 L160,126" {st(.75, 2, 0)}/>'
    # Publikum
    for x in [230, 290, 350]: i += head(x, 204, 9, .4)
    return svg("0 0 440 250", i, "Skizze: eine Person präsentiert eine Folie vor ihrem Team")

def sparring():
    i = ground(20, 420, 236)
    def chair(x, flip=False):
        s = -1 if flip else 1
        return (f'<path d="M{x},{236} V{190} H{x+s*70} V{236}" {st(.45, 1.6, 0)}/>'
                f'<path d="M{x-s*4},{190} V{120} a10,10 0 0 1 {s*10},-10 h{s*8} a10,10 0 0 1 {s*10},10 V{190}" {st(.45, 1.6, .06)}/>'
                f'<rect x="{min(x, x+s*74)}" y="176" width="74" height="16" rx="6" {st(.45, 1.6, .08)}/>')
    i += chair(70) + chair(370, True)
    i += head(116, 124, 13, .7) + head(324, 124, 13, .7)
    i += f'<path d="M160,40 h84 a10,10 0 0 1 10,10 v28 a10,10 0 0 1 -10,10 h-60 l-14,14 v-14 h-10 a10,10 0 0 1 -10,-10 v-28 a10,10 0 0 1 10,-10z" {st(.6, 1.7, .1)}/>' + bar(172, 56, 58, 4.5, .5) + bar(172, 68, 40, 4.5, .3)
    i += f'<path d="M206,100 h70 a10,10 0 0 1 10,10 v26 a10,10 0 0 1 -10,10 h-8 v14 l-14,-14 h-48 a10,10 0 0 1 -10,-10 v-26 a10,10 0 0 1 10,-10z" {st(.75, 1.9, .12)}/><path d="M226,123 l9,9 20,-20" {st(.8, 2, 0)}/>'
    i += f'<rect x="196" y="206" width="48" height="30" rx="3" {st(.3, 1.4, .05)}/>'
    return svg("0 0 440 250", i, "Skizze: zwei Sessel im Gespräch mit Sprechblasen, eine mit Haken")

def vortrag1():
    i = ground(20, 420, 236)
    # Produkt auf Sockel im Spotlight
    i += f'<path d="M220,10 L150,200 H290 Z" fill="{W.format(a=.06)}" stroke="none"/>'
    i += f'<rect x="170" y="200" width="100" height="36" rx="3" {st(.45, 1.6, .06)}/>'
    i += f'<path d="M190,140 L220,124 L250,140 V184 L220,200 L190,184 Z" {st(.8, 2, .12)}/><path d="M190,140 L220,156 L250,140 M220,156 V200" {st(.7, 1.6, 0)}/>'
    # Publikum schaut weg (Köpfe mit Blickrichtung, Handy)
    for (x, flip) in [(62, False), (112, True), (330, False), (382, True)]:
        i += head(x, 176, 10, .4)
        i += f'<rect x="{x-7}" y="196" width="14" height="22" rx="2.5" {st(.55, 1.3, "#1c1c1c")}/>'
    i += f'<text x="220" y="100" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="26" fill="{W.format(a=.75)}">?</text>'
    return svg("0 0 440 250", i, "Skizze: ein Produkt im Spotlight, das Publikum schaut aufs Handy")

def vortrag2():
    i = ground(20, 420, 236)
    # Schublade mit Strategiepapier -> Pfeile zu Team
    i += f'<rect x="40" y="120" width="130" height="116" rx="4" {st(.42, 1.6, .05)}/><path d="M40,178 H170" {st(.35, 1.4, 0)}/><rect x="92" y="146" width="26" height="6" rx="3" fill="{W.format(a=.45)}"/><rect x="92" y="204" width="26" height="6" rx="3" fill="{W.format(a=.45)}"/>'
    i += f'<g transform="rotate(-10 104 80)"><rect x="66" y="40" width="80" height="96" rx="4" {st(.75, 1.9, "#161616")}/>' + bar(78, 56, 48, 6, .6) + bar(78, 70, 56, 3.5, .35) + bar(78, 80, 44, 3.5, .35) + f'<circle cx="106" cy="108" r="12" {st(.6, 1.5, 0)}/><circle cx="106" cy="108" r="4" fill="{W.format(a=.7)}"/></g>'
    i += arrow("M160,70 C220,40 250,80 280,100", .6, 1.9, "5 5") + arrow("M268,96 L282,101 L274,114", .6, 1.9)
    for (x, y) in [(310, 160), (356, 150), (402, 160)]: i += head(x, y, 11, .6)
    for (x, y) in [(310, 118), (356, 108), (402, 118)]: i += f'<circle cx="{x}" cy="{y}" r="9" {st(.7, 1.6, .12)}/><path d="M{x-4},{y} l3,3 6,-6" {st(.8, 1.6, 0)}/>'
    return svg("0 0 440 250", i, "Skizze: eine Strategie verlässt die Schublade und kommt beim Team an")

def vortrag3():
    i = ground(20, 420, 236)
    def building(x, a, dash=None, fill=.06):
        return (f'<path d="M{x},236 V120 L{x+50},90 L{x+100},120 V236" {st(a, 1.8, fill, dash)}/>'
                + "".join(f'<rect x="{x+18+c*38}" y="{140+r*32}" width="26" height="20" rx="2" {st(a*.8, 1.3, 0, dash)}/>' for r in range(2) for c in range(2))
                + f'<rect x="{x+38}" y="208" width="24" height="28" rx="2" {st(a*.8, 1.3, 0, dash)}/>')
    i += building(50, .55) + building(290, .6, "5 5", 0)
    i += arrow("M270,160 H176", .8, 2.2) + arrow("M188,148 L174,160 L188,172", .8, 2.2)
    i += f'<path d="M220,40 V226" {st(.25, 1.2, 0, "3 6")}/>'
    return svg("0 0 440 250", i, "Skizze: das eigene Unternehmen und sein gestrichelt gezeichnetes Spiegelbild als Angreifer")

def load(name):
    # Skizzen liegen neben diesem Skript in sk/ (frueher: fester Cloud-Pfad).
    d = os.path.join(os.path.dirname(os.path.abspath(__file__)), "sk")
    s = open(os.path.join(d, f"{name}.svg"), encoding="utf-8").read()
    return s
