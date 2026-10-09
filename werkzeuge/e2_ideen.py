#!/usr/bin/env python3
"""Entwicklungsseite „Darstellungsideen“ (Daniel, 10.10.2026): Darstellungen, die gut sind – aber nicht als Standard
für die Kopfbilder, sondern für einzelne Stellen auf den Seiten. Nur Entwicklung (Branch Daniel), nie auf main.

    python3 werkzeuge/e2_ideen.py      # baut site/projekte/darstellungsideen.html (nach e2_bauen.py)
"""
import re
from e2_header import (QUELLE, SITE, THEMEN, K, MT, SERIF, SANS, W, G3, svg, t, r, glyph, farbig, u_pikto, v7, s_greybox)

ZIEL = SITE / "projekte" / "darstellungsideen.html"
PUNKT = {"gelb": "#fff400", "magenta": "#C51F5D", "cyan": "#0B9FBD", "violett": "#8613A1"}


def u_typo(wort, symbol, zeile):
    """Typografisch: die Zahl / das Kennwort ist das Bild, ein Symbol als Akzent."""
    gross = 230 if len(wort) <= 2 else (190 if len(wort) <= 3 else 150)
    return svg(f'''
{t(16, 290, wort, gross, K, 700, "start", SERIF, 'letter-spacing="-8"')}
<circle cx="370" cy="88" r="52" fill="{MT}"/>{glyph(symbol, 342, 60, 56, W, 2.2)}
<path d="M20 330h400" stroke="{K}" stroke-width="5" stroke-linecap="round"/>
{t(20, 364, zeile, 13, K, 700, "start", SANS, 'letter-spacing="3"')}
''', "Typografisch: " + wort)


IDEEN = [
    dict(name="Piktogramm-System",
         wann="Wo mehrere Features oder Bausteine auf einen Blick gezeigt werden sollen – Leistungsumfang, Paketinhalte, „Das bekommst Du“.",
         nicht="Nicht als Kopfbild: sieht auf jeder Seite gleich aus und erzählt keine Geschichte.",
         bilder=[(u_pikto(th), th["welt"], th["titel"]) for th in THEMEN]),
    dict(name="Typografisch",
         wann="Wo eine starke Zahl oder ein Kennwort die Aussage trägt – Kennzahlen-Abschnitt, Preis, Versprechen („48 h“, „1:1“, „300+ Projekte“).",
         nicht="Nicht als Kopfbild-Standard: viele Seiten haben keine solche Zahl.",
         bilder=[(v7(), "magenta", "Sprint Landingpage · 48 h"), (u_typo("300+", "liste", "PROJEKTE SEIT 2012"), "gelb", "Startseite · Kennzahlen"),
                 (u_typo("1:1", "blasen", "AUF AUGENHÖHE"), "violett", "1:1 Sparring"), (u_typo("90+", "trend", "PAGESPEED ALS STANDARD"), "cyan", "Landingpage · Qualität")]),
    dict(name="Lo-Fi-Wireframe",
         wann="Als Detail, wenn der Aufbau einer Seite oder eines Mediums gezeigt wird – „So ist Deine Landingpage aufgebaut“, Folienvorschau, Roll-up-Entwurf.",
         nicht="Nicht als Kopfbild: zeigt eine Konzeptphase, nicht die Wirkung.",
         bilder=[(s_greybox(), "magenta", "Sprint Landingpage · Aufbau"), (s_greybox(), "cyan", "Landingpage · Aufbau")]),
]

CSS = """<style>
.di-intro { padding: 4.5rem 0 1rem; }
.di-intro h1 { font-family: var(--font-serif); font-size: clamp(2.2rem, 4.6vw, 3.4rem); line-height: 1.15; }
.di-intro p { max-width: 46rem; margin-top: 1.1rem !important; font-size: 1.06rem; line-height: 1.6; color: #3d3a37; }
.di-idee { padding: 2.6rem 0 1rem; border-top: 1px solid #e3dfd8; margin-top: 2rem; }
.di-idee h2 { font-family: var(--font-serif); font-size: 1.9rem; }
.di-regeln { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1rem; margin: 1.2rem 0 1.6rem; }
.di-regeln p { padding: 1rem 1.2rem; border-radius: 14px; background: #f4f3f0; font-size: .95rem; line-height: 1.55; color: #3d3a37; }
.di-regeln b { display: block; margin-bottom: .3rem; color: #1a1817; }
.di-regeln .ja b::before { content: "✓ "; color: #1f8a4c; } .di-regeln .nein b::before { content: "✕ "; color: #C51F5D; }
.di-raster { display: grid; grid-template-columns: repeat(4, minmax(0, 1fr)); border-top: 1px solid #e3dfd8; border-left: 1px solid #e3dfd8; }
.di-raster figure { margin: 0; padding: 1rem; border-right: 1px solid #e3dfd8; border-bottom: 1px solid #e3dfd8; }
.di-raster figcaption { display: flex; align-items: center; gap: .45rem; margin-top: .5rem; font-size: .82rem; font-weight: 600; }
.di-raster figcaption i { width: .7rem; height: .7rem; border-radius: 50%; }
.hv-bild { display: block; width: 100%; height: auto; }
@media (max-width: 900px) { .di-raster { grid-template-columns: repeat(2, minmax(0, 1fr)); } .di-regeln { grid-template-columns: minmax(0, 1fr); } }
</style>"""


def main():
    h = QUELLE.read_text(encoding="utf-8")
    a, b = h.index("<main>"), h.index("</main>") + 7
    teile = ""
    for n, idee in enumerate(IDEEN):
        bilder = "".join(f'<figure>{farbig(bild, welt, "di" + str(n) + str(k))}<figcaption><i style="background:{PUNKT[welt]}"></i>{cap}</figcaption></figure>'
                         for k, (bild, welt, cap) in enumerate(idee["bilder"]))
        teile += (f'<section class="di-idee"><div class="e2-wrap"><h2>{idee["name"]}</h2><div class="di-regeln"><p class="ja"><b>Einsetzen</b>{idee["wann"]}</p>'
                  f'<p class="nein"><b>Nicht so</b>{idee["nicht"]}</p></div><div class="di-raster">{bilder}</div></div></section>')
    inhalt = ('<section class="di-intro"><div class="e2-wrap"><p class="e2-kicker">Entwicklung · Darstellungsideen</p><h1>Gute Darstellungen für einzelne Stellen</h1>'
              '<p>Hier sammeln wir Darstellungen, die überzeugen – aber nicht als Standard für die Kopfbilder taugen. Sie kommen dort zum Einsatz, wo ihr Inhalt passt: '
              'mehrere Bausteine, eine starke Zahl, der Aufbau eines Mediums. Jede Idee mit Regel, wann sie passt und wann nicht.</p></div></section>' + teile + '<div style="height:5rem"></div>')
    seite = h[:a] + "<main>\n" + CSS + '<div class="e2-alt e2-alt--magenta">' + inhalt + "</div>\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Darstellungsideen · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent))


if __name__ == "__main__":
    main()
