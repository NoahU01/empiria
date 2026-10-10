#!/usr/bin/env python3
"""Roll-up 100 × 200 cm – Entwürfe (Daniel, 10.10.2026).

Sechs Varianten:
  A · Claim            – weiß, „Strategie, die wirkt.“ + großer Doppelpfeil
  B · Leistungen       – schwarz, die drei Leistungen mit ihren Zeichen
  C · Drei Leistungen  – die Leistungskarten der Homepage als Bänder (gelb/schwarz/grau)
  D · Muster           – schwarz, Raster aus Doppelpfeilen, einer gelb
  E · Anschnitt        – schwarz, riesiger gelber Doppelpfeil läuft rechts hinaus
  F · Frage            – weiß, die Leitfrage der Startseite
Dazu eine Aufbau-Ansicht mit Sichtzonen. PNG-Vorschau (1000 × 2353 px) nach site/projekte/ga/rollup/.

Aufruf: python3 werkzeuge/ga/rollup.py [--ohne-png]
"""
import sys

from ga_basis import (GELB, SCHWARZ, FIRMA, abschnitt, download, figur, ico, logo, masse, png_export, raster,
                      seite_schreiben, zeichen)

DATEI = "ga-rollup.html"
B = 1000  # mm
PX = (1000, 2000)


def rollup(inhalt, bg, fg, cls="", png=None):
    attr = f' data-png="ga/rollup/{png}.png" data-pw="{PX[0]}"' if png else ""
    return f'<div class="ru ga-blatt {cls}" style="--bg:{bg};--fg:{fg}"{attr}><div class="ru-in">{inhalt}</div></div>'


def kicker(t):
    return f'<p class="ru-kicker">{t}</p>'


def fuss(bg, fg, pfeil=True, text=None):
    p = f'<span class="ru-fpfeil">{zeichen("forward", fg)}</span>' if pfeil else ""
    return f'<div class="ru-fuss" style="background:{bg};color:{fg}"><span>{text or FIRMA["web"]}</span>{p}</div>'


def var_a(png=None):
    return rollup(logo(cls="ru-logo") + '<div class="ru-block">' + kicker("Strategiehandwerk") +
                  '<p class="ru-h ru-h--gross">Strategie,<br>die <span class="ru-hl">wirkt.</span></p></div>'
                  f'<span class="ru-pfeil-a">{zeichen("forward", SCHWARZ)}</span>' + fuss(GELB, SCHWARZ, False),
                  "#fff", SCHWARZ, "ru--a", png)


def var_b(png=None):
    leist = [("forward", "Strategie in den Alltag überführen"), ("kreuz", "Komplexe Themen strukturieren &amp; kommunizieren"),
             ("kreis", "Innovation &amp; Geschäftsmodell neu denken")]
    liste = "".join(f'<li><i class="ru-zeichen ru-zeichen--{n}">{zeichen(n, GELB)}</i><b>{t}</b></li>' for n, t in leist)
    return rollup(logo(True, "ru-logo") + '<div class="ru-block">' + kicker("Strategiehandwerk") +
                  '<p class="ru-h">Wir übersetzen Deine Strategie in <span class="ru-hl">Wirkung.</span></p>'
                  f'<ol class="ru-liste">{liste}</ol></div>' +
                  f'<p class="ru-web">{FIRMA["web"]}</p>', SCHWARZ, "#fff", "ru--b", png)


def var_c(png=None):
    """Drei Leistungen – die Leistungskarten der Homepage als Bänder."""
    baender = [("ru-band--gelb", "forward", SCHWARZ, "Strategie in den Alltag überführen"),
               ("ru-band--schwarz", "kreuz", GELB, "Komplexe Themen strukturieren &amp; kommunizieren"),
               ("ru-band--grau", "kreis", SCHWARZ, "Innovation &amp; Geschäftsmodell neu denken")]
    b_html = "".join(f'<div class="ru-band {c}"><span class="ru-band__z">{zeichen(z, f)}</span><p>{t}</p></div>' for c, z, f, t in baender)
    return rollup(logo(cls="ru-logo") + '<div class="ru-block ru-block--c">'
                  '<p class="ru-h">Strategie,<br>die <span class="ru-hl">wirkt.</span></p></div>' +
                  f'<div class="ru-baender">{b_html}</div>', "#fff", SCHWARZ, "ru--c", png)


def var_d(png=None):
    """Muster – ein ruhiges Raster aus Doppelpfeilen auf Schwarz, einer leuchtet gelb."""
    sp, zelle, y0, zeilen = 5, 170, 860, 4
    pfeile = "".join(f'<span class="ru-m" style="left:{c * zelle + 0}px;top:{r * zelle}px"></span>' for r in range(zeilen) for c in range(sp))
    muster = "".join(
        f'<span class="ru-m{" ru-m--an" if (c, r) == (3, 1) else ""}" style="--x:{c};--y:{r}">{zeichen("forward", GELB if (c, r) == (3, 1) else "#2e2b28")}</span>'
        for r in range(zeilen) for c in range(sp))
    return rollup(logo(True, "ru-logo") + '<div class="ru-block">' + kicker("Strategiehandwerk") +
                  '<p class="ru-h ru-h--gross">Strategie,<br>die <span class="ru-hl">wirkt.</span></p></div>' +
                  f'<div class="ru-muster">{muster}</div><p class="ru-web">{FIRMA["web"]}</p>', SCHWARZ, "#fff", "ru--d", png)


def var_e(png=None):
    """Anschnitt – ein riesiger gelber Doppelpfeil läuft rechts aus dem Roll-up."""
    return rollup(logo(True, "ru-logo") + '<div class="ru-block">' + kicker("Strategiehandwerk") +
                  '<p class="ru-h ru-h--gross">Strategie,<br>die <span class="ru-hl">wirkt.</span></p></div>' +
                  f'<span class="ru-pfeil-e">{zeichen("forward", GELB)}</span><p class="ru-web">{FIRMA["web"]}</p>', SCHWARZ, "#fff", "ru--e", png)


def var_i(png=None):
    """Zitat – der Leitsatz groß, Gelb nur auf „Handwerk.“."""
    return rollup(logo(True, "ru-logo") + '<div class="ru-block ru-block--i">'
                  '<p class="ru-zitat">„Strategie ist<br>keine Zauberei,<br>sondern<br><span class="ru-hl">Handwerk.</span>“</p>'
                  f'<p class="ru-quelle">{"Daniel Ströbel · Strategiehandwerker"}</p></div>'
                  f'<span class="ru-pfeil-i">{zeichen("forward", GELB)}</span><p class="ru-web">{FIRMA["web"]}</p>',
                  SCHWARZ, "#fff", "ru--i", png)


def var_m(png=None):
    """Referenzen – Claim und alle 14 Kundenlogos in Originalfarbe auf Weiß."""
    from linkedin import KUNDEN, LOGO_SKALA
    logos = "".join(f'<span><img src="/assets/logos/{d}" alt="{n}" style="height:{50 * LOGO_SKALA[d] / 8.5:.3f}cqw"></span>' for d, n in KUNDEN)
    return rollup(logo(cls="ru-logo") + '<div class="ru-block">' + kicker("Strategiehandwerk") +
                  '<p class="ru-h">Strategie,<br>die <span class="ru-hl">wirkt.</span></p></div>'
                  f'<p class="ru-kicker ru-ref-k">Wir arbeiten unter anderem für</p><div class="ru-ref">{logos}</div>'
                  f'<p class="ru-web">{FIRMA["web"]}</p>', "#fff", SCHWARZ, "ru--m", png)


def var_n(png=None):
    """Problem – der Problem-Abschnitt der Homepage: Aussage und schwarzer Kasten mit den drei Fragen."""
    fragen = ["Warum bewegt sich da nichts?", "Warum zieht mein Team nicht mit?", "Warum kommt meine Strategie im Alltag nicht an?"]
    return rollup(logo(cls="ru-logo") + '<div class="ru-block">' + kicker("Problem") +
                  '<p class="ru-h">Die Strategie steht.<br>Trotzdem passiert<br>zu <span class="ru-hl">wenig.</span></p></div>'
                  '<div class="ru-kasten">' + "".join(f'<p class="ru-kfrage">{f}</p>' for f in fragen) +
                  '<p class="ru-kantwort">Die Antwort liegt selten an der Strategie selbst. Es liegt daran, dass sie niemand in den Alltag übersetzt hat.</p></div>'
                  f'<p class="ru-web">{FIRMA["web"]}</p>', "#fff", SCHWARZ, "ru--n", png)


VARIANTEN = [
    ("a", "A · Claim", "weiß", var_a), ("b", "B · Leistungen", "schwarz", var_b),
    ("c", "C · Drei Leistungen", "weiß · gelb · schwarz · grau", var_c), ("d", "D · Muster", "schwarz", var_d),
    ("e", "E · Anschnitt", "schwarz", var_e), ("i", "F · Zitat", "schwarz", var_i),
    ("m", "G · Referenzen", "weiß · Logos in Originalfarbe", var_m), ("n", "H · Problem", "weiß · schwarzer Kasten", var_n),
]


def inhalt():
    figuren = [figur(fn(f"rollup-{k}"), f"<b>{t}</b> · {farbe} · 100 × 200 cm",
                     download(f"ga/rollup/rollup-{k}.png", f"PNG-Vorschau · {PX[0]} × {PX[1]} px")) for k, t, farbe, fn in VARIANTEN]
    teile = [abschnitt("Acht Varianten", "<b>A</b> Claim und Doppelpfeil. <b>B</b> die drei Leistungen mit ihren Zeichen. "
                       "<b>C</b> die Leistungskarten als Bänder. <b>D</b> ein Raster aus Doppelpfeilen, einer leuchtet. "
                       "<b>E</b> der Doppelpfeil im Anschnitt. <b>F</b> der Leitsatz als Zitat. "
                       "<b>G</b> Referenzen: Claim und alle 14 Kundenlogos in Originalfarbe – für Messen in der Versicherungsbranche. "
                       "<b>H</b> der Problem-Abschnitt der Homepage: Aussage und schwarzer Kasten mit den drei Fragen, die jede Führungskraft kennt.",
                       raster(figuren, 4, 2, "gap:2.4rem 1.4rem"))]
    zonen = ('<div class="ru-zonen">'
             '<div class="ru-z" style="top:0;height:15%"><span>Kopfzone · 170–200 cm</span><small>Logo – sichtbar über Köpfe hinweg</small></div>'
             '<div class="ru-z ru-z--auge" style="top:15%;height:40%"><span>Augenhöhe · 90–170 cm</span><small>Botschaft – hier wird gelesen</small></div>'
             '<div class="ru-z" style="top:55%;height:32.5%"><span>Mitte · 25–90 cm</span><small>Bild, Details, Liste</small></div>'
             '<div class="ru-z ru-z--fuss" style="top:87.5%;height:12.5%"><span>Fußzone · 0–25 cm</span><small>oft verdeckt – nur Web-Adresse</small></div></div>')
    aufbau = '<div class="ga-raster ru-aufbau">' + "".join([figur(var_a().replace('<div class="ru-in">', zonen + '<div class="ru-in">', 1), "<b>Sichtzonen</b> · am Beispiel A"),
                     '<div class="ru-mass">' + "".join(f'<p><b>{a}</b><span>{b}</span></p>' for a, b in [
                         ("Format", "100 × 200 cm, hoch (Standard-Kassette)"),
                         ("Rand", "8 cm seitlich, Logo 8 cm vom oberen Rand"),
                         ("Überschrift", "Lora Bold, ca. 300–400 pt – lesbar aus 5–8 m"),
                         ("Text", "Poppins Light, ca. 90–110 pt"),
                         ("Fuß", "untere 25 cm: farbige Fläche, nur Web-Adresse"),
                         ("Druckdaten", "als PDF 1:1 oder 1:10 mit Anschnitt laut Druckerei (noch anzulegen)"),
                     ]) + '</div>']) + '</div>'
    teile.append(abschnitt("Aufbau &amp; Sichtzonen", "Ein Roll-up wird im Stehen und aus Entfernung gelesen. Darum steht die Botschaft auf "
                           "Augenhöhe, das Logo ganz oben und unten nichts Wichtiges – der Standfuß und Tische verdecken diesen Bereich oft.", aufbau))
    return "".join(teile)


CSS = masse("""
.ru { position: relative; aspect-ratio: 100 / 200; container-type: inline-size; background: var(--bg); color: var(--fg); overflow: hidden;
  border-radius: 4px; font-family: 'Poppins', sans-serif; }
.ru p, .ru ol { margin: 0; }
.ru-in { position: absolute; inset: 0; }
.ru-logo { position: absolute; left: [70]; top: [80]; height: [86]; width: auto; display: block; }
.ru-block { position: absolute; left: [80]; right: [80]; top: [400]; }
.ru-kicker { display: flex; align-items: center; gap: [20]; margin-bottom: [40] !important; font: 700 [24]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.ru-kicker::before { content: ""; width: [50]; height: [5]; background: currentColor; }
.ru-h { font: 700 [92]/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; }
.ru-h--gross { font-size: [128]; line-height: 1.3; }
.ru-hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; }
.ru-text { margin-top: [50] !important; font: 300 [34]/1.5 'Poppins', sans-serif; max-width: [640]; }
.ru-fuss { position: absolute; left: 0; right: 0; bottom: 0; height: [250]; display: flex; align-items: center; justify-content: space-between;
  padding: 0 [80]; font: 600 [40]/1 'Poppins', sans-serif; letter-spacing: .02em; }
.ru-fuss em { display: block; margin-top: [14]; font-style: normal; font-weight: 400; opacity: .85; }
.ru-fpfeil { width: [90]; }
.ru-fpfeil svg, .ru-pfeil-a svg, .ru-pfeil-d svg { width: 100%; height: auto; display: block; }
/* A */
.ru-pfeil-a { position: absolute; left: [80]; bottom: [420]; width: [520]; }
/* B */
.ru--b .ru-block { top: [340]; }
.ru--b .ru-h { font-size: [80]; }
.ru--b .ru-kicker { color: #fff400; }
.ru-liste { list-style: none; padding: 0; margin-top: [70] !important; border-top: [3] solid rgba(255,255,255,.35); }
.ru-liste li { display: grid; grid-template-columns: [70] 1fr; align-items: center; padding: [32] 0; border-bottom: [3] solid rgba(255,255,255,.35); }
.ru-zeichen { display: block; width: [46]; }
.ru-zeichen svg { display: block; width: 100%; height: auto; }
.ru-liste small { display: block; font: 700 [24]/1 'Poppins', sans-serif; letter-spacing: .14em; color: #fff400; }
.ru-liste b { display: block; font: 700 [40]/1.22 'Lora', serif; }
.ru-formate { margin-top: [56] !important; font: 300 [30]/1.5 'Poppins', sans-serif; }
.ru-formate span { display: block; margin-bottom: [10]; font: 700 [22]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; opacity: .7; }
/* C · Drei Leistungen */
.ru-block--c { top: [330]; }
.ru--c .ru-h { font-size: [110]; }
.ru-baender { position: absolute; left: 0; right: 0; top: [780]; bottom: 0; display: grid; grid-template-rows: 1fr 1fr 1.25fr; }
.ru-band { position: relative; padding: [60] [80]; }
.ru-band--gelb { background: #fff400; color: #1a1817; }
.ru-band--schwarz { background: #1a1817; color: #fff; }
.ru-band--grau { background: #f3f1ee; color: #1a1817; }
.ru-band__z { position: absolute; right: [80]; top: [60]; width: [130]; }
.ru-band__z svg { display: block; width: 100%; height: auto; }
.ru-band p { position: absolute; left: [80]; top: [60]; max-width: [460]; font: 700 [42]/1.3 'Lora', Georgia, serif; letter-spacing: -.01em; }
.ru-web { position: absolute; left: [80]; bottom: [90]; font: 600 [36]/1 'Poppins', sans-serif; letter-spacing: .02em; }
/* D · Muster */
.ru-muster { position: absolute; left: [40]; right: [40]; top: [880]; display: grid; grid-template-columns: repeat(5, 1fr); row-gap: [60]; }
.ru-m { display: block; width: 52%; margin: 0 auto; }
.ru-m svg { display: block; width: 100%; height: auto; }
.ru--d .ru-kicker, .ru--e .ru-kicker { color: #fff400; }
/* E · Anschnitt */
.ru-pfeil-e { position: absolute; right: [-180]; top: [960]; width: [640]; }
.ru-pfeil-e svg { display: block; width: 100%; height: auto; }
.ru--e .ru-web, .ru--d .ru-web { color: #fff; }
/* G · Referenzen */
.ru--m .ru-h { font-size: [100]; }
.ru-ref-k { position: absolute; left: [80]; top: [800]; }
.ru-ref { position: absolute; left: [80]; right: [80]; top: [880]; display: grid; grid-template-columns: 1fr 1fr; grid-auto-rows: [92]; column-gap: [50]; }
.ru-ref span { display: flex; align-items: center; }
.ru-ref img { display: block; width: auto; max-width: 92%; object-fit: contain; }
/* H · Problem */
.ru--n .ru-h { font-size: [64]; }
.ru-kasten { position: absolute; left: [80]; right: [80]; top: [780]; background: #1a1817; color: #fff; border-radius: [22]; padding: [58] [54]; }
.ru-kfrage { font: 700 [40]/1.3 'Lora', Georgia, serif; letter-spacing: -.01em; }
.ru-kfrage + .ru-kfrage { margin-top: [30] !important; }
.ru-kantwort { margin-top: [46] !important; padding-top: [40]; border-top: [4] solid #fff400; font: 300 [28]/1.55 'Poppins', sans-serif; color: rgba(255,255,255,.8); }
.ru-stufe svg, .ru-pfeil-i svg, .ru-pfeil-k svg, .ru-zz__z svg { display: block; width: 100%; height: auto; }
/* H · Zitat */
.ru-block--i { top: [380]; }
.ru-zitat { font: 700 [86]/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; }
.ru-quelle { margin-top: [56] !important; font: 600 [24]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }
.ru-pfeil-i { position: absolute; left: [80]; bottom: [250]; width: [200]; }
.ru--i .ru-web, .ru--b .ru-web { color: #fff; }
/* Sichtzonen */
.ru-zonen { position: absolute; inset: 0; z-index: 2; pointer-events: none; }
.ru-z { position: absolute; left: 0; right: 0; border-top: 1px dashed #C51F5D; display: flex; flex-direction: column; align-items: flex-end; padding: [14] [20]; }
.ru-z:first-child { border-top: 0; }
.ru-z span { background: #C51F5D; color: #fff; font: 600 [21]/1 'Poppins', sans-serif; padding: [8] [12]; border-radius: [6]; }
.ru-z small { margin-top: [8]; background: rgba(255,255,255,.92); color: #1a1817; font: 400 [19]/1.3 'Poppins', sans-serif; padding: [4] [10]; border-radius: [6]; }
.ru-z--auge { background: rgba(197,31,93,.06); }
.ru-z--fuss { background: rgba(26,24,23,.18); }
.ru-aufbau { grid-template-columns: minmax(0, 1fr) minmax(0, 2.2fr); gap: 2.4rem; }
.ru-aufbau .ga-wrap { max-width: 340px; }
.ru-mass { align-self: center; }
.ru-mass p { display: grid; grid-template-columns: 8rem 1fr; gap: 1rem; margin: 0; padding: .75rem 0; border-bottom: 1px solid #e4e0db; font-size: .95rem; line-height: 1.45; }
.ru-mass b { font-weight: 600; }
@media (max-width: 800px) { .ru-aufbau { grid-template-columns: 1fr; } .ru-aufbau .ga-wrap { max-width: 260px; } .ru-mass p { grid-template-columns: 6.5rem 1fr; font-size: .88rem; } }
""", 850)  # Maße aus dem 85er-Raster, skaliert auf 100 cm Breite


def bauen(mit_png=True):
    seite_schreiben(DATEI, "Roll-up",
                    'Roll-<span class="hl">up</span>',
                    "Acht Entwürfe für das Roll-up im Format 100 × 200 cm – für Messen, Vorträge und Workshops. Wenig Text, große Schrift, "
                    "die Botschaft auf Augenhöhe. Alle Entwürfe sind maßstäblich; die PNGs sind Vorschauen, keine Druckdaten.",
                    ["Entwurf 2", "100 × 200 cm", "8 Varianten", "Sichtzonen"], inhalt(), CSS)
    if mit_png:
        png_export(DATEI, "rollup")


if __name__ == "__main__":
    bauen("--ohne-png" not in sys.argv)
