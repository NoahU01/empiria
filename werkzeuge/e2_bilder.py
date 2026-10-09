"""Kopfbilder für empiria 2.0 – je Seite eine kleine Szene als grafisches Management Summary (Daniel, Runde 5, 10.10.2026).

Bildsprache (wie die Symbole der Wagenpaten-Seite): klare dunkle Linie (4 px), Flächen weiß oder hellgrau,
dahinter versetzt ein farbiger „Tupfer“ in der Farbe der Seite (Gelb = Strategiehandwerk, Magenta = Workshops).
Jede Szene erzählt den Kern der Seite in zwei bis drei Stationen, mit wenigen Stichworten – keine Details.
Themen-Icons nur bei ihrem Thema: Doppelpfeil = Strategie, Kreuz = Komplexe Themen, Kreis = Innovation.
"""
Y, K, M, G, W, G2 = "#fff400", "#1a1817", "#C51F5D", "#ebe8e3", "#ffffff", "#cfcac2"
S = 4  # Linienstärke


def _svg(inhalt, label):
    return (f'<svg class="e2-bild" viewBox="0 0 440 400" role="img" aria-label="{label}" '
            f'font-family="Poppins, Arial, sans-serif">{inhalt}</svg>')


def _use(sprite, x, y, s, farbe):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{farbe}" color="{farbe}">{sprite}</g>'


# ---------- Bausteine ----------
def tupfer(cx, cy, r, c):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{c}"/>'


def kasten(x, y, w, h, fill=W, r=10, sw=S, stroke=K, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}" {extra}/>'


def linie(x, y, w, c=K, h=7, op=1):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{h/2}" fill="{c}" opacity="{op}"/>'


def label(x, y, t, c=K, anchor="middle", size=12.5):
    return (f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="700" '
            f'letter-spacing="1.4" fill="{c}">{t}</text>')


def person(x, y, s=1, fill=W, hals=True):
    """Brustbild: Kopf + Schultern, Fußpunkt Mitte unten (x, y)."""
    return (f'<g transform="translate({x} {y}) scale({s})">'
            f'<path d="M-30 0v-10c0-17 13-28 30-28s30 11 30 28V0z" fill="{fill}" stroke="{K}" stroke-width="{S/s}" stroke-linejoin="round"/>'
            f'<circle cx="0" cy="-56" r="16" fill="{fill}" stroke="{K}" stroke-width="{S/s}"/></g>')


def haken(x, y, s=1, c=K):
    return f'<path d="M{x-9*s} {y}l{6*s} {6*s} {12*s}-{13*s}" fill="none" stroke="{c}" stroke-width="{S+.5}" stroke-linecap="round" stroke-linejoin="round"/>'


def doppelpfeil(x, y, s=1, c=K):
    return (f'<path transform="translate({x} {y}) scale({s})" d="M0 0l14 14L0 28M16 0l14 14-14 14" fill="none" stroke="{c}" '
            f'stroke-width="{S+1}" stroke-linecap="round" stroke-linejoin="round"/>')


def pfad(d, c=K, gestrichelt=True):
    dash = ' stroke-dasharray="2 11"' if gestrichelt else ""
    return f'<path d="{d}" fill="none" stroke="{c}" stroke-width="{S}" stroke-linecap="round"{dash}/>'


def zettel(x, y, c, rot=0, w=46, h=42):
    return (f'<g transform="rotate({rot} {x+w/2} {y+h/2})"><rect x="{x}" y="{y}" width="{w}" height="{h}" rx="5" fill="{c}" stroke="{K}" stroke-width="{S-1}"/>'
            f'{linie(x+9, y+12, w-18, K, 4, .55)}{linie(x+9, y+22, w-26, K, 4, .55)}</g>')


# ---------- Szenen ----------
def startseite(F):
    # Erkennen (Lupe über dem Knoten) » Einordnen (Baustein ins Geschäftsmodell) » Verändern (Fahne auf Stufen)
    knoten = '<path d="M58 250c18-26 52-6 34 14s-46-6-20-26 46 6 26 34-38 2-26-18" fill="none" stroke="#1a1817" stroke-width="4" stroke-linecap="round"/>'
    return _svg(f'''
{tupfer(84, 250, 56, Y)}
{knoten}
<circle cx="96" cy="240" r="44" fill="none" stroke="{K}" stroke-width="{S+1}"/><path d="M128 272l26 26" stroke="{K}" stroke-width="{S+6}" stroke-linecap="round"/>
{label(98, 340, "ERKENNEN")}
{pfad("M146 206C160 180 168 168 178 160")}
{kasten(172, 112, 124, 92, W, 12)}
{"".join(kasten(184 + c * 36, 124 + r * 36, 28, 28, G, 5, S - 1) for r in (0, 1) for c in (0, 1, 2) if (r, c) != (1, 2))}
<rect x="264" y="146" width="28" height="28" rx="5" fill="{Y}" stroke="{K}" stroke-width="{S-1}" transform="rotate(-12 278 160)"/>
{label(234, 232, "EINORDNEN")}
{pfad("M304 150C318 140 322 134 324 126")}
{tupfer(372, 84, 46, Y)}
<path d="M318 120h30v-26h30v-26h30" fill="none" stroke="{K}" stroke-width="{S}" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M392 68V18" stroke="{K}" stroke-width="{S+1}" stroke-linecap="round"/><path d="M392 20l30 10-30 11z" fill="{K}"/>
{label(372, 152, "VERÄNDERN")}
''', "Schmerz erkennen, einordnen, verändern")


def strategie(F):
    # Strategiepapier » drei Karten (Rolle, Richtung, Handwerkszeug) » das Team zieht mit
    return _svg(f'''
{tupfer(96, 112, 70, Y)}
{kasten(40, 40, 116, 150, W, 10)}
{linie(58, 62, 64, K, 9)}{linie(58, 80, 44, K, 6, .45)}
<path d="M60 160l22-22 18 14 32-36" fill="none" stroke="{K}" stroke-width="{S}" stroke-linecap="round" stroke-linejoin="round"/>
<path d="M118 116h16v16" fill="none" stroke="{K}" stroke-width="{S}" stroke-linecap="round" stroke-linejoin="round"/>
{label(98, 220, "STRATEGIE")}
{doppelpfeil(176, 96, 1.3)}
{"".join(f'{kasten(226, y, 198, 46, f, 23)}{haken(252, y+23, 1)}{label(276, y+28, t, K, "start", 12)}' for y, t, f in ((40, "ROLLE", W), (96, "RICHTUNG", Y), (152, "HANDWERKSZEUG", W)))}
{pfad("M320 214v30")}
<rect x="196" y="252" width="232" height="128" rx="18" fill="{G}"/>
{person(256, 372, 1)}{person(312, 372, 1.12, Y)}{person(368, 372, 1)}
{label(312, 274, "ALLTAG", K)}
''', "Strategie in den Alltag: Rolle, Richtung, Handwerkszeug")


def komplexe_themen(F):
    # Folienberg » Kreuz (strukturieren) » eine Kernbotschaft, die beim Entscheider ankommt
    folien = "".join(f'<g transform="rotate({r} {x+52} {y+36})">{kasten(x, y, 104, 72, W, 8, S-1)}{linie(x+12, y+14, 52, K, 6, .5)}{linie(x+12, y+28, 76, G2, 5)}{linie(x+12, y+40, 64, G2, 5)}</g>'
                     for x, y, r in ((24, 214, -8), (44, 190, 6), (20, 160, -3), (52, 132, 9), (28, 104, -6)))
    return _svg(f'''
{folien}
{label(84, 318, "NOCH EINE FOLIE …", "#6f6a64", "middle", 11)}
{pfad("M146 208C170 206 176 204 186 200")}
<circle cx="220" cy="196" r="40" fill="{Y}"/>
{_use(F["kreuz"], 194, 170, .224, K)}
{pfad("M262 192C276 190 282 188 292 186")}
{tupfer(372, 128, 56, Y)}
{kasten(300, 92, 120, 86, W, 12)}
{linie(316, 112, 70, K, 10)}{linie(316, 132, 50, K, 6, .45)}
<circle cx="392" cy="150" r="13" fill="none" stroke="{K}" stroke-width="{S-1}"/><circle cx="392" cy="150" r="4" fill="{K}"/>
{label(360, 76, "KERNBOTSCHAFT")}
{person(360, 330, 1.05)}{haken(400, 236, 1.1)}
<path d="M360 196v-8" stroke="{K}" stroke-width="{S}" stroke-linecap="round" stroke-dasharray="2 9"/>
{label(360, 360, "ENTSCHEIDER")}
''', "Vom Folienberg zur Kernbotschaft")


def innovation(F):
    # Gilt als gegeben (Steintafel mit Riss) » Kreis (hinterfragen) » Bausteine neu zusammengesetzt
    bausteine = "".join(kasten(x, y, 44, 44, f, 7, S - 1, extra=f'transform="rotate({r} {x+22} {y+22})"')
                        for x, y, f, r in ((286, 216, W, 0), (332, 216, K, 0), (378, 216, W, 0), (309, 170, Y, 0), (355, 170, W, 0), (334, 104, W, 14), (386, 124, Y, -10)))
    return _svg(f'''
<path d="M30 300V140c0-40 30-68 74-68s74 28 74 68v160z" fill="{G}" stroke="{K}" stroke-width="{S}" stroke-linejoin="round"/>
{linie(62, 156, 84, K, 6, .45)}{linie(62, 176, 70, K, 6, .45)}{linie(62, 196, 80, K, 6, .45)}
<path d="M118 72l-12 40 18 24-14 30 16 26-10 22" fill="none" stroke="{K}" stroke-width="{S}" stroke-linejoin="round" stroke-linecap="round"/>
<path d="M20 300h170" stroke="{K}" stroke-width="{S}" stroke-linecap="round"/>
{label(104, 334, "GILT ALS GEGEBEN")}
<circle cx="234" cy="170" r="32" fill="none" stroke="{K}" stroke-width="{S+4}"/>
{label(188, 116, "UND WENN NICHT?", K, "start", 11)}
{tupfer(344, 206, 68, Y)}
{bausteine}
{pfad("M376 160C380 154 380 150 378 146")}
<path d="M274 262h160" stroke="{K}" stroke-width="{S}" stroke-linecap="round"/>
{label(354, 300, "NEU GEDACHT")}
''', "Geschäftsmodell neu denken")


def workshops(F):
    # Team am Board: echte Fälle, Zettel, am Ende ein klares Ergebnis
    return _svg(f'''
{tupfer(330, 92, 64, M)}
{kasten(70, 40, 300, 196, W, 14)}
<path d="M140 236l-22 60M300 236l22 60" stroke="{K}" stroke-width="{S}" stroke-linecap="round"/>
{zettel(96, 66, Y, -4)}{zettel(152, 62, M, 3)}{zettel(96, 124, G, 2)}{zettel(152, 122, Y, -3)}
{pfad("M214 110C232 108 238 108 248 110")}
{kasten(258, 72, 92, 108, Y, 10, S)}
{haken(282, 102, .9)}{linie(298, 99, 36, K, 6)}{haken(282, 130, .9)}{linie(298, 127, 28, K, 6)}{haken(282, 158, .9)}{linie(298, 155, 32, K, 6)}
{label(304, 206, "ERGEBNIS")}
{label(150, 206, "ECHTE FÄLLE", "#6f6a64")}
{person(130, 392, 1.1)}{person(220, 392, 1.2, M)}{person(310, 392, 1.1)}
''', "Workshop: echte Fälle, klares Ergebnis")


def ki_zum_anfassen(F):
    # Laptop mit Prompt und Antwort, daneben drei Tools im Vergleich, vorne das Team
    funke = lambda x, y, s, c: f'<path transform="translate({x} {y}) scale({s})" d="M0-22c3 13 9 19 22 22-13 3-19 9-22 22-3-13-9-19-22-22 13-3 19-9 22-22z" fill="{c}" stroke="{K}" stroke-width="{3/s}" stroke-linejoin="round"/>'
    return _svg(f'''
{tupfer(296, 70, 54, M)}
{kasten(52, 60, 250, 168, W, 14)}
<path d="M30 248h294l-16-20H46z" fill="{G}" stroke="{K}" stroke-width="{S}" stroke-linejoin="round"/>
{kasten(74, 84, 150, 34, G, 17, S - 1)}{linie(90, 98, 96, K, 6, .55)}
{kasten(130, 132, 150, 50, W, 14, S - 1)}{linie(146, 146, 110, K, 6)}{linie(146, 162, 76, K, 6, .45)}
{funke(268, 128, .9, Y)}
{"".join(f'{kasten(340, y, 76, 52, f, 12, S - 1)}{label(378, y+31, t, c, "middle", 11)}' for y, t, f, c in ((64, "TOOL A", W, K), (126, "TOOL B", M, W), (188, "TOOL C", W, K)))}
<path d="M322 90h10M322 152h10M322 214h10" stroke="{K}" stroke-width="{S-1}" stroke-linecap="round"/>
{label(378, 268, "IM VERGLEICH", "#6f6a64", "middle", 11)}
{person(130, 392, 1)}{person(210, 392, 1.1, Y)}{person(290, 392, 1)}
''', "KI zum Anfassen: Tools ausprobieren und vergleichen")


def sprint_landingpage(F):
    # Halb gebaute Landingpage + Handy, Stoppuhr 48h: in zwei Tagen live
    return _svg(f'''
{tupfer(330, 300, 70, M)}
{kasten(30, 44, 270, 300, W, 16)}
<path d="M30 82h270" stroke="{K}" stroke-width="{S}"/><circle cx="54" cy="63" r="6" fill="{K}"/><circle cx="74" cy="63" r="6" fill="{K}"/>
<rect x="52" y="102" width="226" height="74" rx="10" fill="{M}"/>{linie(70, 124, 120, W, 9)}{linie(70, 144, 80, W, 7, .8)}
{linie(52, 196, 170, K, 8)}{linie(52, 216, 130, G2, 7)}
<rect x="52" y="240" width="104" height="70" rx="10" fill="none" stroke="{K}" stroke-width="{S-1}" stroke-dasharray="7 7"/>
<rect x="174" y="240" width="104" height="70" rx="10" fill="none" stroke="{K}" stroke-width="{S-1}" stroke-dasharray="7 7"/>
{kasten(250, 150, 78, 138, W, 14)}<rect x="262" y="172" width="54" height="30" rx="5" fill="{M}"/>{linie(262, 212, 46, K, 6)}{linie(262, 226, 34, G2, 6)}{kasten(262, 244, 40, 14, K, 7, 0)}
<circle cx="350" cy="300" r="56" fill="{Y}" stroke="{K}" stroke-width="{S+1}"/><path d="M350 236v-14M334 220h32M392 256l9-9" stroke="{K}" stroke-width="{S+1}" stroke-linecap="round"/>
<text x="350" y="314" text-anchor="middle" font-family="Lora, Georgia, serif" font-weight="700" font-size="36" fill="{K}">48h</text>
{kasten(330, 44, 86, 34, K, 17, 0)}{label(373, 66, "LIVE", W)}<circle cx="347" cy="61" r="5" fill="{M}"/>
''', "Landingpage in 48 Stunden live")


def workshop_moderation(F):
    # Moderator am Board, Beiträge der Teilnehmenden, am Ende Handlungsklarheit
    return _svg(f'''
{tupfer(122, 120, 74, M)}
{kasten(40, 40, 240, 180, W, 14)}
{zettel(60, 62, Y, -4, 40, 36)}{zettel(106, 66, M, 3, 40, 36)}{zettel(60, 110, G, 2, 40, 36)}
<path d="M164 70v124" stroke="{K}" stroke-width="{S-1}" stroke-dasharray="2 10" stroke-linecap="round"/>
{zettel(180, 62, G, -2, 40, 36)}{zettel(226, 66, Y, 4, 40, 36)}{zettel(196, 112, M, -3, 40, 36)}
<path d="M88 172c40 18 100 18 150 0" fill="none" stroke="{K}" stroke-width="{S}" stroke-linecap="round"/><path d="M226 162l14 10-16 8" fill="none" stroke="{K}" stroke-width="{S}" stroke-linecap="round" stroke-linejoin="round"/>
{label(160, 248, "PERSPEKTIVWECHSEL", "#6f6a64", "middle", 11)}
{person(76, 392, 1.15, M)}<path d="M92 330l-14-104" stroke="{K}" stroke-width="{S}" stroke-linecap="round"/>
{kasten(150, 270, 76, 40, W, 14, S-1)}<path d="M168 310l-6 12 18-12" fill="{W}" stroke="{K}" stroke-width="{S-1}" stroke-linejoin="round"/>{linie(164, 284, 46, K, 5, .55)}{linie(164, 294, 30, K, 5, .55)}
{person(196, 392, .9)}{person(256, 392, .9)}
{pfad("M300 150C318 150 326 150 334 150")}
{kasten(330, 96, 96, 120, Y, 12)}
{haken(350, 124, .8)}{linie(364, 121, 46, K, 6)}{haken(350, 152, .8)}{linie(364, 149, 36, K, 6)}{haken(350, 180, .8)}{linie(364, 177, 42, K, 6)}
{label(378, 242, "KLARHEIT")}
''', "Moderierter Workshop mit klaren Ergebnissen")


BILDER = {"strategie": strategie, "komplexe-themen": komplexe_themen, "innovation": innovation, "workshops": workshops,
          "ki-zum-anfassen": ki_zum_anfassen, "sprint-landingpage": sprint_landingpage, "workshop-moderation": workshop_moderation, "index": startseite}
