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
MT, ON = "#C51F5E", "#FEFEFE"   # Akzent als Linie/Schrift · Weiß auf Akzentfläche (werden je Farbwelt ersetzt)
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"


def svg(inhalt, label, defs=""):
    return (f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" aria-label="{label}" font-family="{SANS}">'
            f'<defs>{defs}</defs>{inhalt}</svg>')


def r(x, y, w, h, fill, rx=0, extra=""):
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" {extra}/>'


def t(x, y, txt, size=12, fill=K, weight=700, anchor="start", fam=SANS, extra=""):
    return f'<text x="{x}" y="{y}" font-size="{size}" font-weight="{weight}" fill="{fill}" text-anchor="{anchor}" font-family="{fam}" {extra}>{txt}</text>'






# ---------------------------------------------------------------- 3 · Bauplan


# ---------------------------------------------------------------- 4 · Duoton


# ---------------------------------------------------------------- 5 · Prozess


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
    "magenta": {"#C51F5D": "#C51F5D", "#C51F5E": "#C51F5D", "#FEFEFE": "#ffffff", "#e27fa3": "#e27fa3", "#f5d3df": "#f5d3df", "#7a1339": "#7a1339"},
    "cyan":    {"#C51F5D": "#0B9FBD", "#C51F5E": "#0a8aa4", "#FEFEFE": "#ffffff", "#e27fa3": "#72c6d8", "#f5d3df": "#d4eef4", "#7a1339": "#06576a"},
    "violett": {"#C51F5D": "#8613A1", "#C51F5E": "#8613A1", "#FEFEFE": "#ffffff", "#e27fa3": "#bb7bcc", "#f5d3df": "#ecd9f1", "#7a1339": "#4e0b5e"},
    "gelb":    {"#C51F5D": "#fff400", "#C51F5E": "#1a1817", "#FEFEFE": "#1a1817", "#e27fa3": "#fff86b", "#f5d3df": "#fffbc7", "#7a1339": "#1a1817"},
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






# nur für Sprint gezeichnet, nicht als Stil über alle Themen tragfähig (bleiben zur Entscheidung im Raster)
# Piktogramm-System, Typografisch, Lo-Fi-Wireframe: gute Ideen für einzelne Stellen, nicht für den Kopf → Seite „Darstellungsideen“ (e2_ideen.py)


CSS4 = """<style>
.hv-st-scroll { overflow-x: auto; margin: 0 2rem; -webkit-overflow-scrolling: touch; }
.hv-st-raster { display: grid; grid-template-columns: 10rem repeat(4, minmax(240px, 1fr)); min-width: 1120px; border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
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
Jede Spalte zeichnet dasselbe Motiv in einer der verbliebenen Darstellungsarten – so siehst Du, welche Art über alle Themen trägt. Farbe je Bereich.</p></div>
<div class="hv-st-scroll"><div class="hv-st-raster">{kopf}{zeilen}</div></div></section>'''


def main():
    h = QUELLE.read_text(encoding="utf-8")
    kopf = re.search(r'<section class="e2-kopf" id="intro">.*?</section>', h, re.S).group(0)
    bild_alt = re.search(r'<svg class="e2-bild".*?</svg>', kopf, re.S).group(0)
    a, b = h.index("<main>"), h.index("</main>") + 7
    import e2_spot as sp
    eintraege = [(f(sp.MOTIVE["sprint"]), n) for n, f in sp.STILE]
    zellen = "".join(f'<figure class="hv-zelle" data-name="{i} · {n}">{farbig(bild, "magenta", f"r{i}")}<figcaption><b>{i}</b>{n}</figcaption></figure>'
                     for i, (bild, n) in enumerate(eintraege, 1))
    vorschau = kopf.replace(bild_alt, farbig(eintraege[0][0], "magenta", "vs")).replace('id="intro"', 'id="vorschau"')
    inhalt = f'''<section class="hv-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Header</p>
<h1>Kopfbilder: Spot-Illustration und Darstellungsart</h1>
<p>Eine <b>Darstellungsart</b> ist die Bildsprache und gilt für alle Seiten; das <b>Motiv</b> wechselt je Seite und sorgt zusammen mit der Bereichsfarbe dafür, dass es kein Einheitsbrei wird.
Im Rennen sind noch Monolinie, Duoton, Isometrisch 3D und Glas. Gute Ideen für einzelne Stellen stehen auf der Seite „Darstellungsideen“.</p></div></section>
{stufen_raster()}
<div class="hv-vorschau"><div class="e2-wrap"><h2 class="hv-h2" style="margin-top:3rem!important">Im echten Kopf ansehen</h2><p class="hv-vorschau-label">Vorschau im Kopf – Klick auf ein Feld im Raster zeigt es hier: 1 · Monolinie</p></div>{vorschau}</div>
<section><div class="e2-wrap"><div class="hv-raster" style="margin-top:1.6rem">{zellen}</div><div style="height:5rem"></div></div></section>'''
    js = JS.replace('".hv-vorschau-label").textContent = "Vorschau im Kopf: "', '".hv-vorschau-label").textContent = "Vorschau im Kopf – Klick auf ein Feld im Raster zeigt es hier: "')
    seite = h[:a] + "<main>\n" + CSS4 + '<div class="e2-alt e2-alt--magenta e2-seite--sprint-landingpage">' + inhalt + "</div>" + js + "\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Header-Varianten · Darstellungsarten · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent), "·", len(eintraege), "Darstellungsarten")


if __name__ == "__main__":
    main()
