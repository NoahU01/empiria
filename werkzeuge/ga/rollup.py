#!/usr/bin/env python3
"""Roll-up 100 × 200 cm – Entwürfe (Daniel, 10.10.2026).

Vier Varianten:
  A · Claim       – weiß, „Strategie, die wirkt.“ + großer Doppelpfeil
  B · Leistungen  – schwarz, die drei Leistungen
  C · Team        – weiß, Teamfoto, Namen und Rollen
  D · Frage       – gelb, die Leitfrage der Startseite
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
                  fuss(GELB, SCHWARZ), SCHWARZ, "#fff", "ru--b", png)


def var_c(png=None):
    namen = [("Kerstin Christ", "Expertin HR &amp; Weiterbildung"), ("Daniel Ströbel", "Strategiehandwerker"),
             ("Noah Hermanns", "Experte Performance Marketing")]
    return rollup(logo(cls="ru-logo") + '<div class="ru-block">' + kicker("Kontakt") +
                  '<p class="ru-h">Wir sind<br>für <span class="ru-hl">Dich da!</span></p>'
                  '<p class="ru-text">Direkter Draht – keine Warteschleifen, kein Ticketsystem.</p></div>'
                  '<img class="ru-team" src="/assets/team-portrait.webp" alt="">'
                  '<div class="ru-namen">' + "".join(f'<p><b>{n}</b><span>{r}</span></p>' for n, r in namen) + '</div>' +
                  fuss(SCHWARZ, GELB, text=f'Strategie, die wirkt. <em>{FIRMA["web"]}</em>'), "#fff", SCHWARZ, "ru--c", png)


def var_d(png=None):
    fragen = ["Warum bewegt sich da nichts?", "Warum zieht mein Team nicht mit?"]
    return rollup(logo(cls="ru-logo") + '<div class="ru-block">' + kicker("Die Strategie steht") +
                  '<p class="ru-h">Warum kommt meine Strategie im Alltag nicht an?</p>' +
                  "".join(f'<p class="ru-frage">{f}</p>' for f in fragen) + '</div>' +
                  fuss(SCHWARZ, GELB, text=f'Strategie, die wirkt. <em>{FIRMA["web"]}</em>'), GELB, SCHWARZ, "ru--d", png)


VARIANTEN = [
    ("a", "A · Claim", "weiß", var_a), ("b", "B · Leistungen", "schwarz", var_b),
    ("c", "C · Team", "weiß + Foto", var_c), ("d", "D · Frage", "gelb", var_d),
]


def inhalt():
    figuren = [figur(fn(f"rollup-{k}"), f"<b>{t}</b> · {farbe} · 100 × 200 cm",
                     download(f"ga/rollup/rollup-{k}.png", f"PNG-Vorschau · {PX[0]} × {PX[1]} px")) for k, t, farbe, fn in VARIANTEN]
    teile = [abschnitt("Vier Varianten", "<b>A</b> setzt allein auf den Claim und den Doppelpfeil – wirkt aus 10 m Entfernung. "
                       "<b>B</b> erklärt in drei Zeilen, was empiria tut. <b>C</b> zeigt die Menschen – gut für Messen und Netzwerk-Abende. "
                       "<b>D</b> holt die Leitfrage der Startseite auf Gelb und spricht Führungskräfte direkt an.",
                       raster(figuren, 4, 2, "gap:2.2rem 1.2rem"))]
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
/* C */
.ru--c .ru-block { top: [360]; }
.ru-team { position: absolute; left: [-40]; right: [-40]; width: calc(100% + [80]); bottom: [490]; height: auto; display: block; }
.ru-namen { position: absolute; left: [80]; right: [80]; bottom: [320]; display: grid; grid-template-columns: repeat(3, 1fr); gap: [24]; }
.ru-namen p { border-top: [5] solid #1a1817; padding-top: [24]; }
.ru-namen b { display: block; font: 700 [25]/1.2 'Lora', serif; white-space: nowrap; }
.ru-namen span { display: block; margin-top: [10]; font: 400 [17]/1.4 'Poppins', sans-serif; }
/* D */
.ru--d .ru-block { top: [380]; }
.ru--d .ru-h { font-size: [96]; }
.ru-frage { margin-top: [40] !important; padding-top: [40]; border-top: [4] solid #1a1817; font: 700 [44]/1.25 'Lora', serif; }
.ru-frage:first-of-type { margin-top: [80] !important; }
.ru-text--d { margin-top: [70] !important; }
.ru-pfeil-d { position: absolute; right: [80]; bottom: [340]; width: [260]; }
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
                    "Vier Entwürfe für das Roll-up im Format 100 × 200 cm – für Messen, Vorträge und Workshops. Wenig Text, große Schrift, "
                    "die Botschaft auf Augenhöhe. Alle Entwürfe sind maßstäblich; die PNGs sind Vorschauen, keine Druckdaten.",
                    ["Entwurf 1", "100 × 200 cm", "4 Varianten", "Sichtzonen"], inhalt(), CSS)
    if mit_png:
        png_export(DATEI, "rollup")


if __name__ == "__main__":
    bauen("--ohne-png" not in sys.argv)
