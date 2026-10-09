"""Kopfbilder für empiria 2.0 – je Seite eine kleine Illustration zum Thema (Daniel, 10.10.2026).
Stil: kräftige, ruhige Flächen und Linien wie die Icons der Startseite; Gelb/Schwarz für Strategiehandwerk,
Magenta/Schwarz für Workshops. Die Themen-Icons (Doppelpfeil = Strategie, Kreuz = Komplexe Themen,
Kreis = Innovation) erscheinen nur bei ihrem Thema."""
Y, K, M, G, W = "#fff400", "#1a1817", "#C51F5D", "#ebe8e3", "#ffffff"


def _svg(inhalt, label):
    return f'<svg class="e2-bild" viewBox="0 0 400 400" role="img" aria-label="{label}">{inhalt}</svg>'


def _use(sprite, x, y, s, farbe):
    return f'<g transform="translate({x} {y}) scale({s})" fill="{farbe}" color="{farbe}">{sprite}</g>'


def strategie(F):
    # Ziel (Fahne) → Doppelpfeil → Alltag (abgehakte Aufgaben)
    return _svg(f'''
<circle cx="112" cy="104" r="78" fill="{Y}"/>
<path d="M104 140V54" stroke="{K}" stroke-width="10" stroke-linecap="round"/><path d="M104 56l56 18-56 20z" fill="{K}"/>
{_use(F["forward"], 214, 74, .46, K)}
{"".join(f'<rect x="136" y="{y}" width="236" height="42" rx="21" fill="{G}"/><circle cx="160" cy="{y+21}" r="14" fill="{Y}" stroke="{K}" stroke-width="5"/><path d="M153 {y+21}l5 5 9-10" fill="none" stroke="{K}" stroke-width="4.5" stroke-linecap="round" stroke-linejoin="round"/><rect x="188" y="{y+16}" width="{w}" height="10" rx="5" fill="{K}" opacity=".75"/>' for y, w in ((236, 120), (290, 90), (344, 150)))}
''', "Vom Ziel in den Alltag")


def komplexe_themen(F):
    # Wirrwarr links → Kreuz → klare Linien rechts
    return _svg(f'''
<path d="M36 120c40-30 70 40 30 60s-40-70 20-60 40 70 0 80-60-10-20 40 80 10 40 50-70-20-50 20" fill="none" stroke="{K}" stroke-width="7" stroke-linecap="round" stroke-linejoin="round"/>
<circle cx="200" cy="200" r="74" fill="{Y}"/>
{_use(F["kreuz"], 147, 147, .456, K)}
{"".join(f'<rect x="300" y="{y}" width="84" height="14" rx="7" fill="{K}"/>' for y in (138, 178, 218, 258))}
<circle cx="292" cy="145" r="0" />
''', "Aus Komplexität wird Struktur")


def innovation(F):
    # Heute (Kreis) und Morgen (gelber Kreis), Bausteine wandern hinüber
    return _svg(f'''
<circle cx="270" cy="150" r="104" fill="{Y}"/>
{_use(F["kreis"], 46, 126, .98, K)}
<rect x="104" y="206" width="40" height="40" rx="6" fill="{K}"/><rect x="150" y="252" width="40" height="40" rx="6" fill="{K}"/>
<rect x="262" y="112" width="40" height="40" rx="6" fill="{K}"/><rect x="312" y="150" width="40" height="40" rx="6" fill="none" stroke="{K}" stroke-width="6" stroke-dasharray="6 7"/>
<path d="M200 214L246 170" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round" stroke-dasharray="2 12"/><path d="M226 166h22v22" fill="none" stroke="{K}" stroke-width="6" stroke-linecap="round" stroke-linejoin="round"/>
''', "Geschäftsmodell neu denken")


def workshops(F):
    return _svg(f'''
<path d="M120 300l-34 84M280 300l34 84M200 300v84" stroke="{K}" stroke-width="10" stroke-linecap="round"/>
<rect x="56" y="60" width="288" height="240" rx="18" fill="{W}" stroke="{K}" stroke-width="10"/>
<rect x="88" y="96" width="70" height="70" rx="6" fill="{M}" transform="rotate(-4 123 131)"/>
<rect x="170" y="100" width="70" height="70" rx="6" fill="{Y}" transform="rotate(3 205 135)"/>
<rect x="252" y="96" width="62" height="70" rx="6" fill="{K}"/>
<rect x="92" y="196" width="140" height="12" rx="6" fill="{K}"/><rect x="92" y="222" width="190" height="12" rx="6" fill="{G}"/><rect x="92" y="248" width="110" height="12" rx="6" fill="{G}"/>
''', "Workshop am Board")


def ki_zum_anfassen(F):
    return _svg(f'''
<rect x="40" y="96" width="290" height="244" rx="22" fill="{W}" stroke="{K}" stroke-width="10"/>
<rect x="70" y="134" width="170" height="44" rx="22" fill="{G}"/>
<rect x="132" y="196" width="170" height="44" rx="22" fill="{M}"/>
<rect x="70" y="258" width="130" height="44" rx="22" fill="{G}"/>
<path d="M316 30c6 44 30 68 74 74-44 6-68 30-74 74-6-44-30-68-74-74 44-6 68-30 74-74z" fill="{M}"/>
<path d="M356 214c3 20 13 30 33 33-20 3-30 13-33 33-3-20-13-30-33-33 20-3 30-13 33-33z" fill="{Y}" stroke="{K}" stroke-width="5"/>
''', "KI im Gespräch")


def sprint_landingpage(F):
    return _svg(f'''
<rect x="30" y="70" width="290" height="290" rx="20" fill="{W}" stroke="{K}" stroke-width="10"/>
<path d="M30 116h290" stroke="{K}" stroke-width="10"/><circle cx="60" cy="93" r="7" fill="{K}"/><circle cx="84" cy="93" r="7" fill="{K}"/>
<rect x="58" y="142" width="234" height="74" rx="10" fill="{M}"/>
<rect x="58" y="236" width="180" height="12" rx="6" fill="{K}"/><rect x="58" y="262" width="140" height="12" rx="6" fill="{G}"/>
<rect x="58" y="296" width="96" height="34" rx="17" fill="{K}"/>
<circle cx="316" cy="290" r="66" fill="{Y}" stroke="{K}" stroke-width="10"/><path d="M316 222v-14M300 206h32" stroke="{K}" stroke-width="10" stroke-linecap="round"/>
<text x="316" y="304" text-anchor="middle" font-family="Lora, Georgia, serif" font-weight="700" font-size="40" fill="{K}">48h</text>
''', "Landingpage in 48 Stunden")


def workshop_moderation(F):
    return _svg(f'''
<rect x="40" y="50" width="320" height="230" rx="18" fill="{W}" stroke="{K}" stroke-width="10"/>
{"".join(f'<rect x="{x}" y="{y}" width="56" height="50" rx="6" fill="{c}" transform="rotate({r} {x+28} {y+25})"/>' for x, y, c, r in ((74, 84, M, -5), (138, 90, Y, 4), (82, 152, G, 3), (226, 84, Y, -3), (290, 92, M, 5), (238, 154, G, -4)))}
<path d="M200 90v160" stroke="{K}" stroke-width="5" stroke-dasharray="2 12" stroke-linecap="round"/>
<path d="M80 300h150a24 24 0 0 1 24 24v26a24 24 0 0 1-24 24h-92l-40 26v-26h-18a24 24 0 0 1-24-24v-26a24 24 0 0 1 24-24z" fill="{M}"/>
<rect x="88" y="324" width="110" height="10" rx="5" fill="{W}"/><rect x="88" y="344" width="70" height="10" rx="5" fill="{W}"/>
''', "Moderierter Workshop")


def startseite(F):
    # Die drei Leistungen mit ihren Zeichen
    return _svg(f'''
<rect x="26" y="26" width="200" height="200" rx="26" fill="{Y}"/>{_use(F["forward"], 56, 56, .6, K)}
<rect x="244" y="96" width="130" height="130" rx="22" fill="{K}"/>{_use(F["kreuz"], 266, 118, .37, Y)}
<rect x="106" y="244" width="150" height="130" rx="22" fill="{G}"/>{_use(F["kreis"], 136, 264, .39, K)}
''', "Strategie, Komplexe Themen, Innovation")


BILDER = {"strategie": strategie, "komplexe-themen": komplexe_themen, "innovation": innovation, "workshops": workshops,
          "ki-zum-anfassen": ki_zum_anfassen, "sprint-landingpage": sprint_landingpage, "workshop-moderation": workshop_moderation, "index": startseite}
