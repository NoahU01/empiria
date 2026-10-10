#!/usr/bin/env python3
"""Entwicklungsseite „Header“ (Daniel, 10.10.2026): zehn Stil-Varianten für das Kopfbild von „Sprint Landingpage“.
Wie Grafikstile in Illustrator – bewusst sehr unterschiedlich in Stil, Detailgrad und Anzahl der Elemente.
Nur Entwicklung (Branch Daniel), nie auf main.

    python3 werkzeuge/e2_header.py      # baut site/projekte/header.html (nach e2_bauen.py)
"""
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
QUELLE = SITE / "sprint-landingpage.html"   # seit 10.10. die 2.0-Fassung unter der echten Adresse
ZIEL = SITE / "projekte" / "header.html"

K, M, Y, V, C, W = "#1a1817", "#C51F5D", "#fff400", "#8613A1", "#0B9FBD", "#ffffff"
G, G2, G3 = "#f1efeb", "#e3dfd8", "#b9b3ab"
M2, M3, M4 = "#e27fa3", "#f5d3df", "#7a1339"
MT, ON = "#C51F5E", "#FEFEFE"   # Akzent als Linie/Schrift · Weiß auf Akzentfläche (werden je Farbwelt ersetzt)
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
        (210, M, M4, M4, r(18, 20, 120, 16, ON, 8) + r(18, 48, 80, 10, M3, 5) + r(18, 80, 60, 22, ON, 11)),
    ]
    teile = "".join(_platte(170, y - 150, 190, 118, 14, o, l, re_, inh) for y, o, l, re_, inh in pl)
    schwebend = _platte(170, 6, 190, 118, 14, W, G2, G3, r(18, 18, 30, 10, K, 5) + r(150, 18, 22, 10, K, 5) + r(66, 18, 70, 10, G3, 5))
    return svg(f'''
<ellipse cx="210" cy="372" rx="170" ry="22" fill="{G}"/>
{teile}
{schwebend}
<circle cx="390" cy="66" r="34" fill="{M3}"/><path d="M390 46v20l12 8" fill="none" stroke="{K}" stroke-width="4" stroke-linecap="round" stroke-linejoin="round"/>
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
<path d="M118 48v262" stroke="{MT}" stroke-width="1.6"/><path d="M112 48h12M112 310h12" stroke="{MT}" stroke-width="1.6"/>
<g transform="rotate(-90 106 180)">{t(106, 184, "48 STUNDEN", 10, MT, 700, "middle")}</g>
<g transform="rotate(-8 360 336)">{r(318, 316, 88, 40, "none", 6, f'stroke="{MT}" stroke-width="2.5"')}{t(362, 342, "FREIGABE", 11, MT, 700, "middle")}</g>
''', "Bauplan der Landingpage mit Abschnitten")


# ---------------------------------------------------------------- 4 · Duoton


# ---------------------------------------------------------------- 5 · Prozess
def v5():
    """Infografik: die drei Etappen des Sprints auf einer Zeitachse – inhaltlich am dichtesten."""
    def knoten(x, nr, farbe):
        return f'<circle cx="{x}" cy="250" r="16" fill="{farbe}" stroke="{K}" stroke-width="3"/>' + t(x, 255, nr, 13, {W: K, M: ON, K: W}[farbe], 700, "middle", SERIF)
    return svg(f'''
<path d="M40 250H404" stroke="{K}" stroke-width="3"/>
<path d="M40 250H404" stroke="{M}" stroke-width="9" stroke-linecap="round" stroke-dasharray="0 0" opacity=".0"/>
<rect x="150" y="244" width="200" height="12" rx="6" fill="{M}"/>
{knoten(70, "1", W)}{knoten(220, "2", M)}{knoten(374, "3", K)}
{r(26, 120, 92, 66, W, 8, f'stroke="{K}" stroke-width="3"')}<circle cx="72" cy="146" r="11" fill="{G2}" stroke="{K}" stroke-width="2.5"/><path d="M56 176c3-10 9-14 16-14s13 4 16 14" fill="{G2}" stroke="{K}" stroke-width="2.5"/>
<path d="M14 194h116" stroke="{K}" stroke-width="3" stroke-linecap="round"/>
{t(72, 292, "VORBEREITUNG", 10.5, K, 700, "middle")}{t(72, 310, "2–3 Std. · online", 10.5, "#6f6a64", 500, "middle")}
{r(156, 96, 128, 98, W, 10, f'stroke="{K}" stroke-width="3"')}{r(168, 110, 104, 26, M, 5)}{r(168, 146, 70, 7, K, 3.5)}
<rect x="168" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/><rect x="224" y="162" width="46" height="22" rx="4" fill="none" stroke="{K}" stroke-width="2" stroke-dasharray="4 4"/>
<circle cx="186" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/><circle cx="220" cy="214" r="9" fill="{M}" stroke="{K}" stroke-width="2.5"/><circle cx="254" cy="214" r="9" fill="{W}" stroke="{K}" stroke-width="2.5"/>
{t(220, 292, "SPRINT-WORKSHOP", 10.5, K, 700, "middle")}{t(220, 310, "2 Tage · Präsenz", 10.5, "#6f6a64", 500, "middle")}
{r(346, 100, 58, 100, W, 10, f'stroke="{K}" stroke-width="3"')}{r(354, 112, 42, 30, M, 4)}{r(354, 150, 34, 5, K, 2.5)}{r(354, 160, 26, 5, G3, 2.5)}{r(354, 174, 30, 12, K, 6)}
<circle cx="404" cy="96" r="14" fill="{K}" stroke="{K}" stroke-width="2.5"/><path d="M397 96l5 5 9-10" fill="none" stroke="{W}" stroke-width="3" stroke-linecap="round" stroke-linejoin="round"/>
{t(374, 292, "GO-LIVE", 10.5, K, 700, "middle")}{t(374, 310, "Feinschliff & live", 10.5, "#6f6a64", 500, "middle")}
<path d="M150 336v10h200v-10" fill="none" stroke="{K}" stroke-width="2.5" stroke-linejoin="round"/>
{t(250, 372, "48 Stunden", 22, K, 700, "middle", SERIF)}
''', "Ablauf: Vorbereitung, Sprint-Workshop, Go-live")


# ---------------------------------------------------------------- 7 · Typografisch
def v7():
    """Typografisch: die Zahl ist das Bild. Sehr wenige Elemente."""
    return svg(f'''
{t(16, 300, "48", 250, K, 700, "start", SERIF, 'letter-spacing="-12"')}
{t(290, 300, "h", 110, MT, 700, "start", SERIF)}
<g transform="rotate(6 368 104)">{r(322, 24, 92, 160, W, 14, f'stroke="{K}" stroke-width="5"')}{r(334, 42, 68, 46, M, 7)}{r(334, 98, 56, 7, K, 3.5)}{r(334, 112, 40, 7, G3, 3.5)}{r(334, 134, 44, 18, K, 9)}</g>
<path d="M20 340h400" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
{t(20, 372, "VON NULL AUF LIVE", 13, K, 700, "start", SANS, 'letter-spacing="3"')}
''', "48 Stunden – typografisch")


# ================================================================ Runde 2 (Daniel, 10.10.2026): neue Stile


# ---------------------------------------------------------------- Riso-Druck


# ---------------------------------------------------------------- Radial


# ---------------------------------------------------------------- Piktogramm-Raster




# ---------------------------------------------------------------- Szene



# ================================================================ Runde 3 (Daniel, 10.10.2026): viele weitere Darstellungsarten
# Alle zeigen dasselbe Motiv (Landingpage, 48 Stunden, Handy), damit nur die Darstellungsart verglichen wird.
import math


def _browser(x, y, w, h, stroke=K, sw=4, fill=W, rx=12, leiste=True):
    s = f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'
    if leiste:
        s += f'<path d="M{x} {y+30}h{w}" stroke="{stroke}" stroke-width="{sw}"/><circle cx="{x+18}" cy="{y+15}" r="5" fill="{stroke}"/><circle cx="{x+34}" cy="{y+15}" r="5" fill="{stroke}"/>'
    return s






def s_glas():
    """Glas: matte, durchscheinende Karten über weichen Farbflächen – modern, technisch."""
    defs = ('<filter id="hvgb" x="-50%" y="-50%" width="200%" height="200%"><feGaussianBlur stdDeviation="26"/></filter>'
            '<filter id="hvgs" x="-20%" y="-20%" width="140%" height="160%"><feDropShadow dx="0" dy="10" stdDeviation="12" flood-color="#1a1817" flood-opacity=".12"/></filter>')
    return svg(f'''
<g filter="url(#hvgb)"><circle cx="150" cy="150" r="96" fill="{M}" opacity=".75"/><circle cx="310" cy="260" r="90" fill="{M2}" opacity=".8"/><circle cx="300" cy="110" r="60" fill="#cfcac2"/></g>
<g filter="url(#hvgs)"><rect x="60" y="80" width="270" height="230" rx="22" fill="#ffffff" fill-opacity=".55" stroke="#ffffff" stroke-width="2"/></g>
<rect x="84" y="104" width="60" height="10" rx="5" fill="{K}" opacity=".7"/>
<rect x="84" y="134" width="190" height="16" rx="8" fill="{K}"/><rect x="84" y="160" width="140" height="10" rx="5" fill="{K}" opacity=".4"/>
<rect x="84" y="196" width="100" height="30" rx="15" fill="{M}"/>
<g filter="url(#hvgs)"><rect x="270" y="170" width="120" height="180" rx="24" fill="#ffffff" fill-opacity=".7" stroke="#ffffff" stroke-width="2"/></g>
{t(330, 250, "48h", 30, K, 700, "middle", SERIF)}{t(330, 274, "BIS LIVE", 10, K, 700, "middle", SANS, 'letter-spacing="2" opacity=".6"')}
''', "Glas: durchscheinende Karten über Farbflächen", defs)








def s_popart():
    """Pop-Art: Halbtonpunkte, dicke Kontur, Sternplatzer – laut, comicnah."""
    defs = f'<pattern id="hvpp" width="12" height="12" patternUnits="userSpaceOnUse"><circle cx="6" cy="6" r="3.4" fill="{M2}"/></pattern>'
    stern = " ".join(f"{330 + (64 if i % 2 == 0 else 40) * math.cos(math.radians(i * 18 - 90)):.1f},{110 + (64 if i % 2 == 0 else 40) * math.sin(math.radians(i * 18 - 90)):.1f}" for i in range(20))
    return svg(f'''
<rect x="20" y="20" width="400" height="360" rx="0" fill="url(#hvpp)"/>
{_browser(56, 96, 250, 250, K, 7, W, 6)}
<rect x="80" y="152" width="200" height="70" fill="{M}" stroke="{K}" stroke-width="6"/>
<path d="M80 250h170M80 274h120" stroke="{K}" stroke-width="8" stroke-linecap="round"/>
<polygon points="{stern}" fill="{M}" stroke="{K}" stroke-width="6" stroke-linejoin="round"/>
{t(330, 120, "48H!", 26, ON, 700, "middle", SANS)}
''', "Pop-Art: Landingpage mit Sternplatzer", defs)














def s_greybox():
    """Lo-Fi-Wireframe: nur graue Kästen, ein Akzent – nüchtern, Konzeptphase."""
    return svg(f'''
{r(60, 50, 320, 300, "#f4f3f0", 10)}
{r(84, 74, 70, 14, "#cfcac2", 4)}{r(300, 74, 56, 14, "#cfcac2", 4)}
{r(84, 110, 272, 110, "#e3dfd8", 6)}<path d="M84 110l272 110M356 110L84 220" stroke="#cfcac2" stroke-width="2"/>
{r(84, 240, 84, 60, "#e3dfd8", 6)}{r(178, 240, 84, 60, "#e3dfd8", 6)}{r(272, 240, 84, 60, "#e3dfd8", 6)}
{r(84, 316, 110, 20, M, 10)}
''', "Lo-Fi-Wireframe in Grau")


















# ---------------------------------------------------------------- Farbwelten
FARBWELT = {
    "magenta": {"#C51F6A": "#f5d3df", "#C51F5D": "#C51F5D", "#C51F5E": "#C51F5D", "#FEFEFE": "#ffffff", "#e27fa3": "#e27fa3", "#f5d3df": "#f5d3df", "#7a1339": "#7a1339"},
    "cyan":    {"#C51F6A": "#cdebf2", "#C51F5D": "#0B9FBD", "#C51F5E": "#0a8aa4", "#FEFEFE": "#ffffff", "#e27fa3": "#72c6d8", "#f5d3df": "#d4eef4", "#7a1339": "#06576a"},
    "violett": {"#C51F6A": "#ead3f1", "#C51F5D": "#8613A1", "#C51F5E": "#8613A1", "#FEFEFE": "#ffffff", "#e27fa3": "#bb7bcc", "#f5d3df": "#ecd9f1", "#7a1339": "#4e0b5e"},
    "gelb":    {"#C51F6A": "#fff400", "#C51F5D": "#fff400", "#C51F5E": "#1a1817", "#FEFEFE": "#1a1817", "#e27fa3": "#fff86b", "#f5d3df": "#fffbc7", "#7a1339": "#1a1817"},
}


def farbig(bild, welt, zusatz):
    """Ein Bild in eine andere Farbwelt umfärben; IDs eindeutig machen, damit mehrere Kopien auf einer Seite gehen."""
    zuordnung = FARBWELT[welt]
    bild = re.sub("|".join(re.escape(k) for k in zuordnung), lambda m: zuordnung[m.group(0)], bild)
    return re.sub(r'(id="|url\(#)(hv[a-z0-9]+)', lambda m: f"{m.group(1)}{m.group(2)}-{zusatz}", bild)


JS = """<script>
document.addEventListener("click", function (e) {
  var z = e.target.closest(".hv-zelle"); if (!z) return;
  var ziel = document.querySelector(".hv-vorschau .e2-kopfbild svg"), bild = z.querySelector("svg");
  if (ziel && bild) { ziel.replaceWith(bild.cloneNode(true)); }
  document.querySelectorAll(".hv-zelle.ist-aktiv").forEach(function (x) { x.classList.remove("ist-aktiv"); });
  z.classList.add("ist-aktiv");
  var v = document.querySelector(".hv-vorschau"); if (v.getBoundingClientRect().bottom < 0 || v.getBoundingClientRect().top > innerHeight) v.scrollIntoView({ behavior: "smooth" });
  document.querySelector(".hv-vorschau-label").textContent = "Vorschau im Kopf: " + z.getAttribute("data-name");
});
</script>"""

# ================================================================ Runde 4 (Daniel, 10.10.2026)
# Trennung: DARSTELLUNGSART (Stil, gilt für alle Seiten) ≠ MOTIV (was gezeigt wird, je Seite anders).
# Damit ein Stil über alle Themen trägt, wird er hier als Funktion (Thema → Bild) gebaut und an vier
# sehr unterschiedlichen Themen in ihren Farbwelten erprobt. Uhr, Netz, Fallblatt usw. sind Motive, keine Stile.

# ---------- Symbolbibliothek (24er-Raster, Linie) ----------
GLYPH = {
    "browser": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8.5h18"/><path d="M6.5 13h7M6.5 16h4.5"/>',
    "uhr": '<circle cx="12" cy="13.5" r="7"/><path d="M12 13.5V10M12 13.5l3 2M10 3h4M12 3v3.5"/>',
    "handy": '<rect x="7" y="2.5" width="10" height="19" rx="2.2"/><path d="M11 18.5h2"/>',
    "fahne": '<path d="M5.5 21V3.5"/><path d="M5.5 4h12l-2.5 4 2.5 4h-12"/>',
    "team": '<circle cx="8" cy="8.5" r="3"/><circle cx="16.5" cy="9.5" r="2.5"/><path d="M2.5 19.5c.6-3.4 2.8-5.5 5.5-5.5s4.9 2.1 5.5 5.5M14 14.6c.8-.4 1.6-.6 2.5-.6 2.4 0 4.2 1.9 4.8 5"/>',
    "liste": '<rect x="4" y="3" width="16" height="18" rx="2"/><path d="M8 9l2 2 4-4M8 15.5h8"/>',
    "kompass": '<circle cx="12" cy="12" r="9"/><path d="M14.8 9.2l-1.6 4-4 1.6 1.6-4z"/>',
    "dashboard": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M7.5 16v-3.5M11.5 16V9M15.5 16v-5"/>',
    "trend": '<path d="M3.5 17l5.5-5.5 4 3.5 7-7.5"/><path d="M15 7.5h5v5"/>',
    "megafon": '<path d="M3.5 10v4h3l7 4.5v-13l-7 4.5z"/><path d="M17 9.5a3.5 3.5 0 0 1 0 5M19.5 7a7 7 0 0 1 0 10"/>',
    "blasen": '<path d="M3 4.5h11v8H8.5L5 15.5v-3H3z"/><path d="M14 8.5h7v8h-1.5v3l-3.5-3H11v-2"/>',
    "birne": '<path d="M9 17.5h6M10 21h4"/><path d="M12 3a6 6 0 0 0-3.5 10.9V17.5h7v-3.6A6 6 0 0 0 12 3z"/>',
    "person": '<circle cx="12" cy="8" r="4"/><path d="M4 21c.9-4 4-6.5 8-6.5s7.1 2.5 8 6.5"/>',
    "ziel": '<circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.2"/>',
    "stift": '<path d="M4 20l1-4.5L16 4.5l3.5 3.5-11 11z"/><path d="M14 7l3.5 3.5"/>',
    "haken": '<circle cx="12" cy="12" r="9"/><path d="M7.5 12.5l3 3 6-6.5"/>',
    "schloss": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
}


def glyph(name, x, y, groesse, farbe=K, staerke=2.0, fuell="none"):
    s = groesse / 24
    return (f'<g transform="translate({x} {y}) scale({s:.3f})" fill="{fuell}" stroke="{farbe}" stroke-width="{staerke:.2f}" '
            f'stroke-linecap="round" stroke-linejoin="round">{GLYPH[name]}</g>')


# ---------- Vier Probethemen aus den vier Bereichen der Live-Seite ----------
THEMEN = [
    dict(key="strategie", titel="Strategie in den Alltag überführen", bereich="Strategiehandwerk", welt="gelb",
         haupt="fahne", neben=["kompass", "team", "liste"], wort="Alltag",
         kacheln=[("person", "ROLLE"), ("kompass", "RICHTUNG"), ("stift", "WERKZEUG"), ("team", "TEAM"), ("ziel", "ZIELBILD"), ("liste", "ALLTAG"), ("birne", "KLARHEIT"), ("haken", "UMSETZUNG")]),
    dict(key="sprint", titel="Sprint Landingpage", bereich="Workshops", welt="magenta",
         haupt="browser", neben=["uhr", "handy", "ziel"], wort="48h",
         kacheln=[("ziel", "ZIELGRUPPE"), ("stift", "TEXT"), ("browser", "DESIGN"), ("handy", "MOBILE"), ("blasen", "FEEDBACK"), ("uhr", "2 TAGE"), ("trend", "ANFRAGEN"), ("haken", "GO-LIVE")]),
    dict(key="mes", titel="MarketingEcoSystem", bereich="Marketing 2.0", welt="cyan",
         haupt="dashboard", neben=["trend", "megafon", "team"], wort="MES",
         kacheln=[("dashboard", "KENNZAHLEN"), ("megafon", "KAMPAGNEN"), ("trend", "REICHWEITE"), ("blasen", "ANFRAGEN"), ("ziel", "ZIELGRUPPE"), ("liste", "BERICHT"), ("uhr", "LAUFEND"), ("team", "BETREUUNG")]),
    dict(key="sparring", titel="1:1 Sparring", bereich="Training & Sparring", welt="violett",
         haupt="blasen", neben=["birne", "person", "schloss"], wort="1:1",
         kacheln=[("blasen", "OFFEN"), ("birne", "KLAR"), ("team", "AUGENHÖHE"), ("schloss", "VERTRAULICH"), ("haken", "ENTSCHEIDEN"), ("uhr", "FLEXIBEL"), ("kompass", "RICHTUNG"), ("trend", "UMSETZUNG")]),
]
SPRINT = THEMEN[1]


# ---------- Stile als Funktion (Thema → Bild) ----------
def u_monolinie(th):
    """Monolinie: ein großes Symbol, drumherum kleine, alles in einer Linienstärke; ein Teil in Akzentfarbe."""
    return svg(f'''
<circle cx="190" cy="196" r="128" fill="none" stroke="{G2}" stroke-width="2" stroke-dasharray="3 9"/>
{glyph(th["haupt"], 86, 92, 208, K, 1.1)}
{glyph(th["neben"][0], 330, 60, 72, MT, 2.2)}{glyph(th["neben"][1], 352, 196, 60, K, 2.2)}{glyph(th["neben"][2], 316, 300, 64, K, 2.2)}
<circle cx="296" cy="96" r="5" fill="{MT}"/>
''', "Monolinie")




def u_riso(th):
    """Riso-Druck: dieselbe Zeichnung in zwei Druckfarben (Akzent + Schwarz), leicht verrutscht übereinander."""
    defs = f'<pattern id="hvrp" width="7" height="7" patternUnits="userSpaceOnUse" patternTransform="rotate(30)"><circle cx="3.5" cy="3.5" r="1.7" fill="{M}"/></pattern>'
    farbe = (f'<g style="mix-blend-mode:multiply"><circle cx="196" cy="206" r="120" fill="url(#hvrp)"/><circle cx="360" cy="110" r="40" fill="{M}"/>'
             + glyph(th["haupt"], 98, 104, 200, M, 2.6) + "</g>")
    schwarz = (f'<g style="mix-blend-mode:multiply" transform="translate(-7 6)">' + glyph(th["haupt"], 98, 104, 200, K, 1.4)
               + glyph(th["neben"][0], 330, 80, 60, K, 2.4) + glyph(th["neben"][1], 330, 260, 64, K, 2.4) + "</g>")
    return svg(farbe + schwarz, "Riso-Druck in Akzent und Schwarz", defs)


def u_duoton(th):
    """Duoton: nur Töne der Akzentfarbe – helle Fläche, dunkle Linie, ein voller Akzent."""
    return svg(f'''
<rect x="44" y="60" width="300" height="280" rx="28" fill="{M3}"/>
<circle cx="344" cy="96" r="54" fill="{M}"/>{glyph(th["neben"][0], 320, 72, 48, ON, 2.6)}
{glyph(th["haupt"], 92, 104, 196, M4, 1.4)}
<rect x="250" y="270" width="150" height="70" rx="18" fill="{W}" stroke="{M4}" stroke-width="2"/>{glyph(th["neben"][1], 266, 286, 38, MT, 2.4)}
<rect x="314" y="294" width="70" height="8" rx="4" fill="{M2}"/><rect x="314" y="310" width="46" height="8" rx="4" fill="{M3}"/>
''', "Duoton in der Akzentfarbe")




def u_pikto(th):
    """Piktogramm-System: neun Felder, in der Mitte das Kennwort."""
    k = ""
    for i in range(9):
        x, y = 34 + (i % 3) * 128, 18 + (i // 3) * 128
        if i == 4:
            k += r(x, y, 116, 116, M, 18) + t(x + 58, y + 70, th["wort"], 30 if len(th["wort"]) < 5 else 22, ON, 700, "middle", SERIF)
        else:
            n, lab = th["kacheln"][i if i < 4 else i - 1]
            k += r(x, y, 116, 116, G, 18) + glyph(n, x + 38, y + 26, 40, K, 2.2) + t(x + 58, y + 98, lab, 8.5, K, 700, "middle", SANS, 'letter-spacing="1.2"')
    return svg(k, "Piktogramm-System")






UNIVERSAL = [
    (u_monolinie, "Monolinie", "ein großes Symbol, alles in einer Linie, ein Teil in Akzent"),
    (u_riso, "Riso: Akzent + Schwarz", "zwei Druckfarben leicht verrutscht, Rasterpunkte"),
    (u_duoton, "Duoton", "nur Töne der Akzentfarbe"),
]
# nur für Sprint gezeichnet, nicht als Stil über alle Themen tragfähig (bleiben zur Entscheidung im Raster)
NUR_SPRINT = [
    (v2, "Isometrisch · Platten", "trägt Produkte und Aufbau, bei Beratung (Sparring) ohne Gegenstand schwach"),
    (v3, "Bauplan", "braucht beschriftbare Teile – die haben wir nicht überall"),
    (v5, "Prozess-Infografik", "Motiv „Ablauf“, kein Stil – alle Köpfe sähen gleich aus"),
    (s_glas, "Glas", "braucht Geräte/Oberflächen"),
    (s_popart, "Pop-Art / Halbton", "sehr laut, prägt die Marke stark"),
]
# Piktogramm-System, Typografisch, Lo-Fi-Wireframe: gute Ideen für einzelne Stellen, nicht für den Kopf → Seite „Darstellungsideen“ (e2_ideen.py)

OK = '<span class="hv-ok" title="für alle Unterseiten geeignet">✓</span>'

CSS4 = """<style>
.hv-kb-raster { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.2rem; }
.hv-kb { display: grid; grid-template-columns: minmax(0, 1.15fr) minmax(0, .85fr); gap: 1.2rem; align-items: center; padding: 1.4rem 1.4rem 1.4rem 1.6rem; border: 1px solid #e3dfd8; border-radius: 18px; background: #fff; }
.hv-kb__kicker { display: flex; align-items: center; gap: .5rem; margin: 0 0 .6rem !important; font-size: .74rem; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; color: #6f6a64; }
.hv-kb__kicker i { width: .7rem; height: .7rem; border-radius: 50%; flex: 0 0 auto; }
.hv-kb h3 { font-family: var(--font-serif); font-size: 1.45rem; line-height: 1.2; }
.hv-kb__warum { margin-top: .8rem !important; font-size: .84rem; line-height: 1.5; color: #6f6a64; }
.hv-kb__warum b { color: #1a1817; }
@media (max-width: 1000px) { .hv-kb-raster { grid-template-columns: minmax(0, 1fr); } }
@media (max-width: 520px) { .hv-kb { grid-template-columns: minmax(0, 1fr); } }
.hv-va { grid-template-columns: repeat(5, minmax(0, 1fr)) !important; }
.hv-va-gruppe { grid-column: 1 / -1; margin: 0 !important; padding: .55rem .9rem; background: #1a1817; color: #fff; font-size: .8rem; font-weight: 700; letter-spacing: .1em; text-transform: uppercase; border-right: 1px solid #e3dfd8; }
.hv-va-titel { display: flex; align-items: center; gap: .6rem; margin: 2.6rem 0 1rem !important; font-family: var(--font-serif); font-size: 1.5rem; }
.hv-va-titel i { width: .9rem; height: .9rem; border-radius: 50%; }
@media (max-width: 900px) { .hv-va { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; } }
.hv-fs { grid-template-columns: 10rem repeat(4, minmax(240px, 1fr)) !important; min-width: 1120px !important; }
.hv-st-scroll { overflow-x: auto; margin: 0 2rem; -webkit-overflow-scrolling: touch; }
.hv-st-raster { display: grid; grid-template-columns: 10rem repeat(2, minmax(260px, 1fr)); min-width: 680px; border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.hv-st-raster > div { padding: .6rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; background: #fff; }
.hv-st-kopf { position: sticky; top: 0; z-index: 2; background: #f4f3f0 !important; }
.hv-st-kopf b { display: block; font-family: var(--font-serif); font-size: 1rem; }
.hv-st-name { position: sticky; left: 0; z-index: 1; }
.hv-st-ecke { left: 0; z-index: 3; }
.hv-st-name small { display: block; margin-top: .2rem; font-size: .74rem; line-height: 1.35; color: #8a847c; }
.hv-st-name b { font-size: .86rem; line-height: 1.3; }
.hv-st-name i { display: block; width: .75rem; height: .75rem; margin-bottom: .45rem; border-radius: 50%; }
@media (max-width: 760px) { .hv-st-scroll { margin: 0 1rem; } }
.hv-intro { padding: 4.5rem 0 1.4rem; }
.hv-intro h1 { font-family: var(--font-serif); font-size: clamp(2.2rem, 4.6vw, 3.4rem); line-height: 1.15; }
.hv-intro p { max-width: 48rem; margin-top: 1.1rem !important; font-size: 1.06rem; line-height: 1.6; color: #3d3a37; }
.hv-h2 { margin: 3.4rem 0 .6rem !important; font-family: var(--font-serif); font-size: 1.9rem; }
.hv-h2 + p { max-width: 48rem; margin-bottom: 1.4rem !important; color: #3d3a37; }
.hv-raster { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.hv-zelle { margin: 0; padding: 1.1rem 1.1rem .9rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; background: #fff; cursor: pointer; }
.hv-zelle:hover { background: #faf9f7; }
.hv-zelle.ist-aktiv { box-shadow: inset 0 0 0 3px #1a1817; }
.hv-zelle figcaption { margin-top: .5rem; font-size: .84rem; font-weight: 600; color: #1a1817; }
.hv-zelle figcaption b { font-family: var(--font-serif); margin-right: .35rem; }
.hv-zelle figcaption small { display: block; margin-top: .2rem; font-weight: 500; font-size: .76rem; line-height: 1.4; color: #8a847c; }
.hv-ok { display: inline-grid; place-items: center; width: 1.15rem; height: 1.15rem; margin-left: .35rem; border-radius: 50%; background: #1f8a4c; color: #fff; font-size: .7rem; vertical-align: 1px; }
.hv-bild { display: block; width: 100%; height: auto; }
.hv-vorschau { background: #fff; border-bottom: 1px solid #e3dfd8; scroll-margin-top: 80px; }
.hv-vorschau .e2-kopf { padding: 1.4rem 0 1.2rem !important; }
.hv-vorschau .e2-kopf h1 { font-size: clamp(1.8rem, 3vw, 2.6rem) !important; }
.hv-vorschau .e2-kopf__inhalt, .hv-vorschau .hero-anlaesse { display: none !important; }
.hv-vorschau .e2-kopfbild { width: min(100%, 16rem) !important; }
.hv-vorschau-label { padding-top: .6rem; font-size: .8rem; font-weight: 600; color: #8a847c; }
.hv-probe { display: grid; grid-template-columns: 11rem repeat(4, minmax(0, 1fr)); border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.hv-probe > div { padding: .8rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; font-size: .82rem; font-weight: 600; }
.hv-probe .kopf { background: #f4f3f0; }
.hv-probe .kopf small { display: block; font-weight: 500; color: #8a847c; }
.hv-probe .kopf i { display: inline-block; width: .7rem; height: .7rem; margin-right: .35rem; border-radius: 50%; vertical-align: 0; }
@media (max-width: 1100px) { .hv-raster { grid-template-columns: repeat(3, minmax(0, 1fr)); } }
@media (max-width: 760px) { .hv-raster { grid-template-columns: repeat(2, minmax(0, 1fr)); } .hv-probe { grid-template-columns: repeat(2, minmax(0, 1fr)); } .hv-probe .leer { display: none; } }
</style>"""


def kopfbilder():
    """Runde 9: Mono für alle 23 Seiten, Aufbau je Seite gezielt gewählt (e2_kopfbilder.py) – im Kopf-Layout dargestellt."""
    import e2_kopfbilder as kb
    punkt = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}
    karten = ""
    for n, seite in enumerate(kb.SEITEN):
        titel, bereich, welt, h1, aufbau, daten, warum = seite
        b, name = kb.bild(seite)
        karten += (f'<article class="hv-kb"><div class="hv-kb__text"><p class="hv-kb__kicker"><i style="background:{punkt[welt]}"></i>{titel}</p>'
                   f'<h3>{h1}</h3><p class="hv-kb__warum"><b>{name}</b> – {warum}</p></div><div class="hv-kb__bild">{farbig(b, welt, "kb" + str(n))}</div></article>')
    return f'''<section class="hv-st"><div class="e2-wrap"><h2 class="hv-h2">Kopfbilder – Mono, je Seite</h2>
<p>Alle 23 Seiten der Live-Homepage in der Darstellungsart <b>Mono</b>. Ein strenges System: eine Icon-Familie mit überall gleicher Strichstärke, nur drei Aufbauten (Trio, Reihe, Zahl) mit festem Raster, nur Linien – Farbe nur über ein Icon in Akzentfarbe, keine Farbflächen. Sag mir einfach, welche Seite noch nicht passt.</p>
<div class="hv-kb-raster">{karten}</div></div></section>'''


def varianten3():
    """Runde 8: drei Szenen, sehr viele Varianten – Mono, Duo, Isometrisch 3D (e2_varianten.py)."""
    import e2_varianten as va
    punkt = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}
    out = ""
    for n, sz in enumerate(va.SZENEN):
        zellen, nr = "", 0
        def zelle(bild, name):
            nonlocal zellen, nr
            nr += 1
            zellen += f'<figure class="hv-zelle" data-name="{sz["titel"]} · {name}">{farbig(bild, sz["welt"], "v" + str(n) + "x" + str(nr))}<figcaption><b>{nr}</b>{name}</figcaption></figure>'
        zellen += '<p class="hv-va-gruppe">Mono</p>'
        for f, name in va.AUFBAU:
            zelle(f(sz, "mono"), "Mono · " + name)
        zellen += '<p class="hv-va-gruppe">Duo</p>'
        for k, (f, name) in enumerate(va.AUFBAU):
            mo = ("duo", "duo_flaeche", "duo_kachel")[k % 3]
            zelle(f(sz, mo), "Duo · " + name + {"duo": "", "duo_flaeche": " · Kreis", "duo_kachel": " · Kachel"}[mo])
        zellen += '<p class="hv-va-gruppe">Strichstärke &amp; Fläche</p>'
        for mo, name in (("mono_fein", "Mono fein"), ("mono_kraeftig", "Mono kräftig"), ("duo_flaeche", "Duo mit Kreis"), ("duo_kachel", "Duo mit Kachel")):
            zelle(va.a_trio(sz, mo), name + " · Trio")
        out += (f'<h3 class="hv-va-titel"><i style="background:{punkt[sz["welt"]]}"></i>{sz["titel"]}</h3><div class="hv-raster hv-va">{zellen}</div>')
    return f'''<section class="hv-st"><div class="e2-wrap"><h2 class="hv-h2">Drei Szenen – viele Varianten</h2>
<p>Medien, KI zum Anfassen und Sprint Landingpage in den beiden Hauptrichtungen <b>Mono</b> und <b>Duo</b>. Bei Mono und Duo wechselt der Aufbau (ein Icon, Trio, Prozess, Raster, Rahmen, Kreis, Typo, beschriftet, gestapelt, auf einer Linie). Nenne mir einfach die Nummern, die Dir gefallen.</p>
{out}</div></section>'''


def feinschliff():
    """Runde 7: Monolinie/Duoton mit einer professionellen Icon-Familie (Phosphor, MIT) – sechs Strichstärken an vier Themen."""
    from e2_phosphor import ICONS
    themen = [("Strategie in den Alltag", "gelb", "flag-banner", "compass", "list-checks"), ("Sprint Landingpage", "magenta", "browser", "timer", "device-mobile"),
              ("MarketingEcoSystem", "cyan", "presentation-chart", "trend-up", "megaphone"), ("1:1 Sparring", "violett", "chats-circle", "lightbulb", "handshake")]
    staerken = [("thin", "Fein"), ("light", "Leicht"), ("regular", "Normal"), ("bold", "Kräftig"), ("fill", "Gefüllt"), ("duotone", "Zweitönig")]
    punkt = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}

    def ic(name, w, x, y, g, farbe):
        inner = ICONS[name][w]
        if w == "duotone":
            inner = inner.replace('opacity="0.2"', f'fill="{M}" opacity=".28"')
        return f'<g transform="translate({x} {y}) scale({g/256:.4f})" fill="{farbe}">{inner}</g>'

    def spot(haupt, akzent, neben, w):
        return svg(ic(haupt, w, 40, 96, 210, K) + ic(akzent, w, 286, 52, 104, MT) + ic(neben, w, 300, 240, 92, K), "Spot")

    kopf = '<div class="hv-st-kopf hv-st-ecke"></div>' + "".join(f'<div class="hv-st-kopf"><b>{t}</b><small><i style="display:inline-block;width:.6rem;height:.6rem;border-radius:50%;background:{punkt[f]}"></i></small></div>' for t, f, *_ in themen)
    zeilen = ""
    for z, (w, name) in enumerate(staerken):
        zeilen += f'<div class="hv-st-name"><b>{name}</b><small>Phosphor · {w}</small></div>'
        zeilen += "".join(f'<div class="hv-st-bild">{farbig(spot(h, a, n, w), welt, "fs" + str(z) + str(k))}</div>' for k, (_, welt, h, a, n) in enumerate(themen))
    return f'''<section class="hv-st"><div class="e2-wrap"><h2 class="hv-h2">Monolinie &amp; Duoton – mit Profi-Icons</h2>
<p>Statt selbst gezeichneter Formen eine professionelle Icon-Familie (Phosphor, frei nutzbar). Je Zeile eine Strichstärke – <b>tippe die Zeile an, die Dir gefällt</b>. Danach baue ich damit alle 23 Seiten.</p></div>
<div class="hv-st-scroll"><div class="hv-st-raster hv-fs">{kopf}{zeilen}</div></div></section>'''


def stufen_raster():
    """Runde 6: je Seite der Live-Homepage eine Spot-Illustration – in jeder verbliebenen Darstellungsart (e2_spot.py)."""
    import e2_spot as sp
    punkt = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}
    kopf = '<div class="hv-st-kopf hv-st-ecke"></div>' + "".join(f'<div class="hv-st-kopf"><b>{n}</b></div>' for n, _ in sp.STILE)
    zeilen = ""
    for z, (titel, bereich, welt, key) in enumerate(sp.SEITEN):
        m = sp.MOTIVE[key]
        zeilen += (f'<div class="hv-st-name"><i style="background:{punkt[welt]}"></i><b>{titel}</b><small>{bereich}</small></div>'
                   + "".join(f'<div class="hv-st-bild">{farbig(f(m), welt, "sp" + str(z) + "x" + str(k))}</div>' for k, (_, f) in enumerate(sp.STILE)))
    return f'''<section class="hv-st"><div class="e2-wrap hv-st-wrap"><h2 class="hv-h2">Spot-Illustration je Seite – in allen Darstellungsarten</h2>
<p>Jede Zeile ist eine Seite der Live-Homepage mit ihrem Motiv als <b>Spot-Illustration</b> (ein Ausschnitt mit zwei bis vier Dingen, ohne Farbkreis dahinter).
Jede Spalte zeichnet dasselbe Motiv in einer der verbliebenen Darstellungsarten (Monolinie, Duoton) – so siehst Du, welche Art über alle Themen trägt. Farbe je Bereich.</p></div>
<div class="hv-st-scroll"><div class="hv-st-raster">{kopf}{zeilen}</div></div></section>'''


def main():
    """Hinweis 10.10.: Archivseite – baut nicht mehr neu (Quelle hat sich geändert); header.html bleibt als Archiv stehen."""
    h = QUELLE.read_text(encoding="utf-8")
    kopf = re.search(r'<section class="e2-kopf" id="intro">.*?</section>', h, re.S).group(0)
    bild_alt = re.search(r'<svg class="e2-bild".*?</svg>', kopf, re.S).group(0)
    a, b = h.index("<main>"), h.index("</main>") + 7
    eintraege = [(f(SPRINT), n, txt, True) for f, n, txt in UNIVERSAL] + [(f(), n, txt, False) for f, n, txt in NUR_SPRINT]
    zellen = "".join(f'<figure class="hv-zelle" data-name="{i} · {n}">{farbig(bild, "magenta", f"r{i}")}<figcaption><b>{i}</b>{n}{OK if ok else ""}<small>{txt}</small></figcaption></figure>'
                     for i, (bild, n, txt, ok) in enumerate(eintraege, 1))
    vorschau = kopf.replace(bild_alt, farbig(eintraege[0][0], "magenta", "vs")).replace('id="intro"', 'id="vorschau"')
    punkt = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}
    probe = '<div class="kopf leer"></div>' + "".join(f'<div class="kopf"><i style="background:{punkt[th["welt"]]}"></i>{th["titel"]}<small>{th["bereich"]}</small></div>' for th in THEMEN)
    for j, (f, n, _) in enumerate(UNIVERSAL, 1):
        probe += f'<div class="leer">{j} · {n}</div>' + "".join(f'<div>{farbig(f(th), th["welt"], "p" + str(j) + th["key"])}</div>' for th in THEMEN)
    inhalt = f'''<section class="hv-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Header · Runde 4</p>
<h1>Kopfbilder: Detaillierung und Darstellungsart</h1>
<p>Wichtig ist die Trennung: Eine <b>Darstellungsart</b> ist die Bildsprache (Linie, Farbfläche, Druck, Karten, Foto …) und gilt für alle Seiten.
Das <b>Motiv</b> wechselt je Seite (Browser, Fahne, Dashboard, Sprechblasen …) – zusammen mit der Bereichsfarbe sorgt es dafür, dass es kein Einheitsbrei wird.
Uhr, Netz und Wegkarte waren Motive, keine Darstellungsarten – sie sind deshalb raus. Ein grüner Haken heißt: als Stil für alle Unterseiten nutzbar und unten an vier Themen erprobt.</p></div></section>
{kopfbilder()}
{varianten3()}
{feinschliff()}
{stufen_raster()}
<div class="hv-vorschau"><div class="e2-wrap"><h2 class="hv-h2" style="margin-top:1rem!important">Darstellungsarten</h2><p class="hv-vorschau-label">Vorschau im Kopf – Klick auf ein Feld im Raster zeigt es hier: 1 · Monolinie</p></div>{vorschau}</div>
<section><div class="e2-wrap"><h2 class="hv-h2">Alle Darstellungsarten</h2><p>Alle zeigen hier das Motiv „Sprint Landingpage“. 1–3 sind als Stil gebaut und tragen jedes Thema; 4–8 sind nur für Sprint gezeichnet und stehen noch zur Entscheidung. Piktogramm-System, Typografisch und Lo-Fi-Wireframe sind auf die Seite „Darstellungsideen“ umgezogen.</p>
<div class="hv-raster">{zellen}</div>
<h2 class="hv-h2">Probe: ein Stil, vier Themen</h2><p>Je ein Thema aus jedem Bereich der Live-Seite, jeweils in seiner Farbwelt: Strategiehandwerk (Gelb), Workshops (Magenta), Marketing 2.0 (Cyan), Training &amp; Sparring (Violett).</p>
<div class="hv-probe">{probe}</div><div style="height:5rem"></div></div></section>'''
    js = JS.replace('".hv-vorschau-label").textContent = "Vorschau im Kopf: "', '".hv-vorschau-label").textContent = "Vorschau im Kopf – Klick auf ein Feld im Raster zeigt es hier: "')
    seite = h[:a] + "<main>\n" + CSS4 + '<div class="e2-alt e2-alt--magenta e2-seite--sprint-landingpage">' + inhalt + "</div>" + js + "\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Header-Varianten · Darstellungsarten · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent), "·", len(eintraege), "Darstellungsarten")


if __name__ == "__main__":
    main()
