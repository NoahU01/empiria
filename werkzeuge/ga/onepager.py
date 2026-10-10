#!/usr/bin/env python3
"""One-Pager A3 – Entwürfe (Daniel, 10.10.2026).

Beispielinhalt: „Strategie in den Alltag überführen“ (Texte von site/leistungen/strategie.html).
  A3 hoch · A Hell          – weiß, Lösung auf gelbem Band, Kontakt auf Grau
  A3 hoch · B Schwarz-Gelb  – schwarzer Kopf, Kontakt auf gelbem Band
  A3 quer · A Hell          – Kopf über die volle Breite, drei Spalten, Fragen-Leiste unten
  A3 quer · B Schwarz-Gelb  – schwarze Spalte links mit Titel und Kontakt, Inhalt rechts in zwei Spalten
PNG-Export (150 dpi) nach site/projekte/ga/onepager/.

Aufruf: python3 werkzeuge/ga/onepager.py [--ohne-png]
"""
import sys

from ga_basis import (GELB, SCHWARZ, FIRMA, PERSONEN, abschnitt, download, figur, ico, logo, masse, png_export, raster,
                      seite_schreiben, zeichen)

DATEI = "ga-onepager.html"
D = PERSONEN["daniel"]
PX = {"hoch": (1754, 2480), "quer": (2480, 1754)}

# ---------- Inhalte (von der Strategie-Seite) ----------
TITEL = 'Strategie in den Alltag <span class="op-hl">überführen.</span>'
LEAD = "Deine Strategie ist da – aber was bedeutet sie für deinen Verantwortungsbereich? Wir machen sie greifbar und wirksam im Alltag."
PROBLEM_H = "Strategisches Denken wird vorausgesetzt. Dir hat es aber keiner beigebracht."
PROBLEM_T = ("Du bist Abteilungs- oder Bereichsleiter, weil du fachlich überzeugt hast. Was danach oft folgt, sind harte Gespräche "
             "mit dem eigenen Team. Hart, weil das Fundament fehlt:")
PROBLEM_L = ["die klare Richtung", "die eigene Rolle", "das Handwerkszeug für den Alltag"]
LOESUNG_H = "Rolle, Richtung, Handwerkszeug für deinen Bereich."
LOESUNG = [("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"), ("compass", "Richtung", "Wie wollen wir wahrgenommen werden?"),
           ("wrench", "Handwerkszeug", "Wie kommen wir dort hin?")]
PERSP_H = "Wie sieht die Homepage Deiner Abteilung aus?"
PERSP_T = ("Stell Dir vor, wir gründen morgen Deine Abteilung als GmbH. Was stünde auf ihrer Homepage – "
           "und würde jeder im Team dasselbe hineinschreiben?")
FRAGEN = ["Welche Zielgruppe sprechen wir an?", "Welches konkrete Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
          "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"]
ERGEBNIS = "Jeder im Team versteht, wofür Dein Bereich da ist – und Du bestimmst seine Wahrnehmung."
ZUSAMMEN_H = "So arbeiten wir wirklich zusammen."
ZUSAMMEN = [("Direkter Draht, klare Worte", "Du arbeitest direkt mit mir – und bekommst ehrliches, direktes Feedback."),
            ("Dein Einsatz entscheidet", "Die Umsetzung bleibt Deine Aufgabe. Plane ein bis zwei Stunden pro Woche ein."),
            ("Dranbleiben, klar planen, umsetzen", "Regelmäßig abstimmen, flexibel umsteuern – und dann stringent umsetzen.")]


def k(t):
    return f'<p class="op-kicker">{t}</p>'


def problem(liste_cls=""):
    return (k("Problem") + f'<p class="op-h2">{PROBLEM_H}</p><p class="op-text">{PROBLEM_T}</p>'
            f'<ul class="op-liste {liste_cls}">' + "".join(f"<li>{x}</li>" for x in PROBLEM_L) + "</ul>")


def loesung_punkte():
    return '<div class="op-loes">' + "".join(f'<div>{ico(i)}<b>{t}</b><p>{q}</p></div>' for i, t, q in LOESUNG) + '</div>'


def loesung():
    return k("Lösung") + f'<p class="op-h2">{LOESUNG_H}</p>' + loesung_punkte()


def fragen():
    return '<ol class="op-fragen">' + "".join(f'<li><small>0{i + 1}</small><span>{f}</span></li>' for i, f in enumerate(FRAGEN)) + '</ol>'


def zusammen(nur_titel=False):
    return (k("Zusammenarbeit") + f'<p class="op-h2">{ZUSAMMEN_H}</p><div class="op-zus">' +
            "".join(f'<div><small>0{i + 1}</small><b>{t}</b><p>{p}</p></div>' for i, (t, p) in enumerate(ZUSAMMEN)) + '</div>')


def kontakt(hell=False):
    return ('<div class="op-kontakt"><img src="/assets/ansprechpartner-daniel.webp" alt="">'
            f'<div><p class="op-kname">{D["name"]}</p><p class="op-krolle">{D["rolle2"]}</p></div>'
            '<div class="op-kdaten">' + "".join(f'<p>{ico(i)}{t}</p>' for i, t in
                                                [("mail", D["mail"]), ("phone", D["tel"]), ("globe", FIRMA["web"])]) + '</div></div>')


def blatt(fmt, inhalt, cls, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX[fmt][0]}"' if png else ""
    return f'<div class="op op--{fmt} ga-blatt {cls}"{attr}><div class="op-in">{inhalt}</div></div>'


# ---------- A3 hoch ----------
def hoch_a(png=None):
    return blatt("hoch",
                 '<header class="op-kopf">' + logo(cls="op-logo") + '<span class="op-thema">Strategiehandwerk</span></header>'
                 f'<section class="op-hero"><div><p class="op-h1">{TITEL}</p><p class="op-lead">{LEAD}</p></div>'
                 f'<span class="op-pfeil">{zeichen("forward", SCHWARZ)}</span></section>'
                 f'<section class="op-zwei"><div>{k("Problem")}<p class="op-h2">{PROBLEM_H}</p></div><div><p class="op-text">{PROBLEM_T}</p>'
                 '<ul class="op-liste">' + "".join(f"<li>{x}</li>" for x in PROBLEM_L) + '</ul></div></section>'
                 f'<section class="op-band op-band--gelb">{loesung()}</section>'
                 f'<section class="op-persp"><div>{k("Perspektivwechsel")}<p class="op-h2">{PERSP_H}</p><p class="op-text">{PERSP_T}</p>'
                 f'<div class="op-ergebnis"><small>Ergebnis</small><p>{ERGEBNIS}</p></div></div>{fragen()}</section>'
                 f'<section class="op-sek--zus">{zusammen()}</section>'
                 f'<footer class="op-fuss op-fuss--grau">{kontakt()}</footer>', "op--ha", png)


def hoch_b(png=None):
    return blatt("hoch",
                 '<section class="op-hero op-hero--schwarz">' + logo(True, "op-logo") +
                 f'<div>{k("Strategiehandwerk")}<p class="op-h1">{TITEL}</p><p class="op-lead">{LEAD}</p></div>'
                 f'<span class="op-pfeil">{zeichen("forward", GELB)}</span></section>'
                 f'<section class="op-spalten"><div>{problem("op-liste--strich")}</div><div>{loesung()}</div></section>'
                 f'<section class="op-band op-band--grau op-persp"><div>{k("Perspektivwechsel")}<p class="op-h2">{PERSP_H}</p>'
                 f'<p class="op-text">{PERSP_T}</p><div class="op-ergebnis op-ergebnis--gelb"><small>Ergebnis</small><p>{ERGEBNIS}</p></div></div>{fragen()}</section>'
                 f'<section class="op-sek--zus">{zusammen()}</section>'
                 f'<footer class="op-fuss op-fuss--gelb">{kontakt()}' + logo(cls="op-logo op-logo--fuss") + '</footer>', "op--hb", png)


# ---------- A3 quer ----------
def quer_a(png=None):
    return blatt("quer",
                 '<header class="op-kopf">' + logo(cls="op-logo") + '<span class="op-thema">Strategiehandwerk</span></header>'
                 f'<section class="op-hero"><p class="op-h1">{TITEL}</p><p class="op-lead">{LEAD}</p>'
                 f'<span class="op-pfeil">{zeichen("forward", SCHWARZ)}</span></section>'
                 f'<section class="op-drei"><div>{problem()}</div><div class="op-karte op-karte--gelb">{loesung()}</div><div>{zusammen()}</div></section>'
                 f'<section class="op-leiste"><div>{k("Perspektivwechsel")}<p class="op-h3">{PERSP_H}</p></div>{fragen()}</section>'
                 f'<footer class="op-fuss op-fuss--quer">{kontakt()}<p class="op-ergebnis-zeile"><small>Ergebnis</small>{ERGEBNIS}</p></footer>',
                 "op--qa", png)


def quer_b(png=None):
    return blatt("quer",
                 '<aside class="op-seite">' + logo(True, "op-logo") +
                 f'<div class="op-seite-titel">{k("Strategiehandwerk")}<p class="op-h1">{TITEL}</p><p class="op-lead">{LEAD}</p></div>'
                 f'<span class="op-pfeil">{zeichen("forward", GELB)}</span>{kontakt()}</aside>'
                 '<div class="op-rechts">'
                 f'<section>{problem("op-liste--strich")}</section><section>{loesung()}</section>'
                 f'<section>{k("Perspektivwechsel")}<p class="op-h2">{PERSP_H}</p>{fragen()}</section>'
                 f'<section>{zusammen()}</section>'
                 f'<p class="op-ergebnis-band"><small>Ergebnis</small>{ERGEBNIS}</p></div>', "op--qb", png)


def inhalt():
    f = []
    for fmt, titel, text, fns in [
        ("hoch", "A3 hoch", "<b>A · Hell</b> folgt der Website: weißer Kopf, die Lösung auf dem gelben Band, Kontakt unten auf Grau. "
         "<b>B · Schwarz-Gelb</b> startet mit einem schwarzen Kopf und endet mit einem gelben Kontaktband – kräftiger, gut als Auslage.",
         [("a", "A · Hell", hoch_a), ("b", "B · Schwarz-Gelb", hoch_b)]),
        ("quer", "A3 quer", "<b>A · Hell</b>: Titel über die volle Breite, darunter drei Spalten – Problem, Lösung (gelbe Karte), Zusammenarbeit – "
         "und die fünf Fragen als Leiste. <b>B · Schwarz-Gelb</b>: eine schwarze Spalte links trägt Titel, Doppelpfeil und Kontakt; "
         "rechts stehen die vier Themen in zwei Spalten.", [("a", "A · Hell", quer_a), ("b", "B · Schwarz-Gelb", quer_b)]),
    ]:
        mm = "297 × 420 mm" if fmt == "hoch" else "420 × 297 mm"
        figs = [figur(fn(f"{fmt}-{v}"), f"<b>{fmt.capitalize()} · {t}</b> · A3 · {mm}",
                      download(f"ga/onepager/{fmt}-{v}.png", f"PNG · {PX[fmt][0]} × {PX[fmt][1]} px (150 dpi)")) for v, t, fn in fns]
        f.append(abschnitt(titel, text, raster(figs, 2 if fmt == "hoch" else 1, 1)))
    return "".join(f)


def basis(sel, W):
    return masse(f"""
{sel} .op-in {{ position: absolute; inset: 0; font: 400 [9.5pt]/1.5 'Poppins', sans-serif; }}
{sel} .op-kicker {{ display: flex; align-items: center; gap: [2.5]; margin-bottom: [4] !important; font: 700 [7pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }}
{sel} .op-kicker::before {{ content: ""; width: [6]; height: [0.5]; background: currentColor; }}
{sel} .op-h1 {{ font: 700 [40pt]/1.14 'Lora', Georgia, serif; letter-spacing: -.02em; }}
{sel} .op-h2 {{ font: 700 [17pt]/1.22 'Lora', Georgia, serif; letter-spacing: -.015em; }}
{sel} .op-h3 {{ font: 700 [14pt]/1.25 'Lora', Georgia, serif; letter-spacing: -.01em; }}
{sel} .op-lead {{ margin-top: [5] !important; font: 300 [12pt]/1.5 'Poppins', sans-serif; max-width: [150]; }}
{sel} .op-text {{ margin-top: [3.5] !important; }}
{sel} .op-logo {{ height: [9]; width: auto; display: block; }}
{sel} .op-kopf {{ position: absolute; left: [18.5]; right: [20]; top: [14]; display: flex; justify-content: space-between; align-items: center; }}
{sel} .op-thema {{ display: flex; align-items: center; gap: [2.5]; font: 700 [7pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }}
{sel} .op-thema::before {{ content: ""; width: [6]; height: [0.5]; background: currentColor; }}
{sel} .op-liste {{ list-style: none; padding: 0; margin-top: [3] !important; }}
{sel} .op-liste li {{ position: relative; padding: [1.6] 0 [1.6] [6]; border-bottom: [0.25] solid #d9d5ce; font-weight: 500; }}
{sel} .op-liste li::before {{ content: ""; position: absolute; left: 0; top: 50%; width: [2.2]; height: [2.2]; margin-top: [-1.1]; border-radius: 50%; background: #fff400; box-shadow: 0 0 0 [0.3] #1a1817 inset; }}
{sel} .op-liste--strich li::before {{ width: [3]; height: [0.5]; margin-top: [-0.25]; border-radius: 0; background: #1a1817; box-shadow: none; }}
{sel} .op-loes {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: [6]; margin-top: [6]; }}
{sel} .op-loes > div {{ border-top: [0.5] solid currentColor; padding-top: [3.5]; }}
{sel} .op-loes svg {{ width: [6.5]; height: [6.5]; display: block; margin-bottom: [2.5]; }}
{sel} .op-loes b {{ display: block; font: 700 [12pt]/1.2 'Lora', serif; }}
{sel} .op-loes p {{ margin-top: [1.5] !important; }}
{sel} .op-fragen {{ list-style: none; padding: 0; counter-reset: f; }}
{sel} .op-fragen li {{ display: grid; grid-template-columns: [10] 1fr; align-items: baseline; padding: [2.6] 0; border-bottom: [0.25] solid #d9d5ce; }}
{sel} .op-fragen li:first-child {{ border-top: [0.25] solid #d9d5ce; }}
{sel} .op-fragen small {{ font: 700 [7pt]/1 'Poppins', sans-serif; letter-spacing: .12em; }}
{sel} .op-fragen span {{ font: 700 [11pt]/1.3 'Lora', serif; }}
{sel} .op-ergebnis {{ margin-top: [6]; background: #1a1817; color: #fff; border-radius: [3]; padding: [5] [6]; }}
{sel} .op-ergebnis small, {sel} .op-ergebnis-zeile small, {sel} .op-ergebnis-band small {{ display: block; margin-bottom: [2]; font: 700 [7pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }}
{sel} .op-ergebnis p {{ font: 700 [12pt]/1.35 'Lora', serif; }}
{sel} .op-ergebnis--gelb {{ background: #fff400; color: #1a1817; }}
{sel} .op-ergebnis--gelb small {{ color: #1a1817 !important; }}
{sel} .op-zus {{ display: grid; grid-template-columns: repeat(3, 1fr); gap: [6]; margin-top: [5]; }}
{sel} .op-zus small {{ font: 700 [7pt]/1 'Poppins', sans-serif; letter-spacing: .14em; }}
{sel} .op-zus b {{ display: block; margin-top: [2]; font: 700 [11.5pt]/1.25 'Lora', serif; }}
{sel} .op-zus p {{ margin-top: [1.6] !important; }}
{sel} .op-kontakt {{ display: flex; align-items: center; gap: [5]; }}
{sel} .op-kontakt img {{ width: [20]; height: [20]; border-radius: 50%; object-fit: cover; background: #e4e0db; }}
{sel} .op-kname {{ font: 700 [13pt]/1.2 'Lora', serif; }}
{sel} .op-krolle {{ margin-top: [1] !important; font: 600 [6.5pt]/1.3 'Poppins', sans-serif; letter-spacing: .12em; text-transform: uppercase; }}
{sel} .op-kdaten {{ margin-left: [6]; font-size: [8.5pt]; line-height: 1.7; }}
{sel} .op-kdaten p {{ display: flex; align-items: center; gap: [2]; }}
{sel} .op-kdaten svg {{ width: [3.2]; height: [3.2]; flex: 0 0 auto; }}
{sel} .op-pfeil svg {{ width: 100%; height: auto; display: block; }}
""", W)


CSS = """
.op { position: relative; container-type: inline-size; background: #fff; color: #1a1817; overflow: hidden; border-radius: 3px; font-family: 'Poppins', sans-serif; }
.op p, .op ul, .op ol { margin: 0; }
.op--hoch { aspect-ratio: 297 / 420; }
.op--quer { aspect-ratio: 420 / 297; }
.op-hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; }
""" + basis(".op--hoch", 297) + basis(".op--quer", 420)

LAYOUT_HOCH = """
/* ---- hoch: Fluss-Layout, Bänder laufen randabfallend ---- */
.op--hoch .op-in { display: flex; flex-direction: column; padding: 0 [20]; }
.op--hoch .op-kopf { position: static; margin-top: [14]; }
.op--hoch .op-logo { margin-left: [-1.5]; }
.op--ha .op-hero { margin-top: [18]; display: flex; justify-content: space-between; align-items: flex-end; gap: [12]; }
.op--ha .op-hero .op-pfeil { flex: 0 0 [50]; margin-bottom: [3]; }
.op-zwei { margin-top: [14]; display: grid; grid-template-columns: 1fr 1fr; column-gap: [14]; align-items: start; }
.op-zwei .op-text { margin-top: [7] !important; }
.op-band { margin: [12] [-20] 0; padding: [9] [20] [10]; }
.op-band--gelb { background: #fff400; }
.op-band--grau { background: #f3f1ee; }
.op-persp { display: grid; grid-template-columns: 1fr 1fr; column-gap: [14]; align-items: start; }
.op-persp .op-fragen { margin-top: [10]; }
.op--ha .op-persp { margin-top: [11]; }
.op--hoch .op-sek--zus { margin-top: [12]; margin-bottom: [10]; }
.op--hoch .op-fuss { margin: auto [-20] 0; padding: [7] [20]; display: flex; align-items: center; justify-content: space-between; }
.op-fuss--grau { background: #f3f1ee; }
.op-fuss--gelb { background: #fff400; }
.op-logo--fuss { height: [8] !important; }
.op-hero--schwarz { position: relative; margin: 0 [-20]; padding: [14] [20] [14]; background: #1a1817; color: #fff; }
.op-hero--schwarz > div { margin-top: [16]; max-width: [175]; }
.op-hero--schwarz .op-kicker { color: #fff400; }
.op-hero--schwarz .op-pfeil { position: absolute; right: [20]; bottom: [19]; width: [44]; }
.op--hb .op-spalten { margin-top: [13]; display: grid; grid-template-columns: 1fr 1.2fr; gap: [14]; }
.op--hb .op-loes { grid-template-columns: 1fr; gap: [3.5]; margin-top: [5]; }
.op--hb .op-loes > div { display: grid; grid-template-columns: [9] [36] 1fr; align-items: center; border-top: [0.3] solid #d9d5ce; padding-top: [3.5]; }
.op--hb .op-loes svg { margin: 0; }
.op--hb .op-loes p { margin: 0 !important; }
"""

LAYOUT_QUER = """/* ---- quer A ---- */
.op--qa .op-kopf { left: [18.5]; right: [20]; top: [14]; }
.op--qa .op-hero { position: absolute; left: [20]; right: [20]; top: [38]; }
.op--qa .op-hero .op-h1 { max-width: [300]; }
.op--qa .op-hero .op-lead { max-width: [230]; }
.op--qa .op-hero .op-pfeil { position: absolute; right: 0; bottom: [1]; width: [46]; }
.op-drei { position: absolute; left: [20]; right: [20]; top: [93]; display: grid; grid-template-columns: 1fr 1.1fr 1fr; gap: [10]; align-items: start; }
.op-karte { border-radius: [3]; padding: [7] [7] [8]; margin-top: [-7]; }
.op-karte--gelb { background: #fff400; }
.op--qa .op-loes, .op--qa .op-zus { grid-template-columns: 1fr; gap: [3.5]; margin-top: [4.5]; }
.op--qa .op-loes > div { display: grid; grid-template-columns: [9] 1fr; column-gap: [1]; padding-top: [3]; }
.op--qa .op-loes svg { grid-row: 1 / span 2; margin: 0; width: [6]; height: [6]; }
.op--qa .op-zus > div { border-top: [0.25] solid #d9d5ce; padding-top: [3]; }
.op--qa .op-zus b { margin-top: [1.4]; }
.op-leiste { position: absolute; left: [20]; right: [20]; top: [216]; display: grid; grid-template-columns: [80] 1fr; gap: [10]; align-items: start; }
.op-leiste .op-fragen { display: grid; grid-template-columns: repeat(5, 1fr); gap: [5]; }
.op-leiste .op-fragen li, .op-leiste .op-fragen li:first-child { display: block; border: 0; border-top: [0.5] solid #1a1817; padding: [3] 0 0; }
.op-leiste .op-fragen small { display: block; margin-bottom: [1.6]; }
.op-fuss--quer { position: absolute; left: 0; right: 0; bottom: 0; display: flex; align-items: center; justify-content: space-between; background: #1a1817; color: #fff; padding: [6.5] [20]; }
.op-ergebnis-zeile { max-width: [150]; font: 700 [11pt]/1.35 'Lora', serif; }
/* ---- quer B ---- */
.op-seite { position: absolute; left: 0; top: 0; bottom: 0; width: [140]; background: #1a1817; color: #fff; padding: [16] [16]; }
.op-seite .op-kicker { color: #fff400; }
.op-seite-titel { position: absolute; left: [16]; right: [14]; top: [56]; }
.op-seite .op-h1 { font-size: [34pt]; }
.op-seite .op-lead { font-size: [11pt]; }
.op-seite .op-pfeil { position: absolute; left: [16]; bottom: [60]; width: [30]; }
.op-seite .op-kontakt { position: absolute; left: [16]; right: [12]; bottom: [16]; flex-wrap: wrap; gap: [4]; }
.op-seite .op-kontakt img { width: [16]; height: [16]; }
.op-seite .op-kdaten { margin-left: 0; flex-basis: 100%; }
.op-rechts { position: absolute; left: [156]; right: [18]; top: [16]; bottom: [16]; display: grid; grid-template-columns: 1fr 1fr; grid-template-rows: auto auto auto; align-content: space-between; column-gap: [14]; row-gap: [11]; }
.op-rechts .op-h2 { font-size: [15pt]; }
.op--qb .op-loes { grid-template-columns: 1fr; gap: [2.6]; margin-top: [4]; }
.op--qb .op-loes > div { display: grid; grid-template-columns: [8] [35] 1fr; align-items: center; border-top: [0.25] solid #d9d5ce; padding-top: [2.6]; }
.op--qb .op-loes svg { margin: 0; width: [5.5]; height: [5.5]; }
.op--qb .op-loes b { font-size: [11pt]; }
.op--qb .op-loes p { margin: 0 !important; }
.op--qb .op-fragen { margin-top: [4]; }
.op--qb .op-fragen li { padding: [1.9] 0; }
.op--qb .op-fragen span { font-size: [10pt]; }
.op--qb .op-zus { grid-template-columns: 1fr; gap: [3]; margin-top: [4]; }
.op--qb .op-zus > div { display: grid; grid-template-columns: [8] 1fr; border-top: [0.25] solid #d9d5ce; padding-top: [2.6]; }
.op--qb .op-zus small { grid-row: 1 / span 2; padding-top: [1]; }
.op--qb .op-zus b { margin: 0; font-size: [10.5pt]; }
.op-ergebnis-band { grid-column: 1 / -1; background: #fff400; border-radius: [3]; padding: [5] [7]; font: 700 [12pt]/1.35 'Lora', serif; }
.op-ergebnis-band small { color: #1a1817 !important; }
"""

CSS += masse(LAYOUT_HOCH, 297) + masse(LAYOUT_QUER, 420)


def bauen(mit_png=True):
    seite_schreiben(DATEI, "One-Pager A3",
                    'One-<span class="hl">Pager</span>',
                    "Ein Blatt, das eine Leistung auf einen Blick erklärt – zum Auslegen, Mitgeben oder als PDF. Beispielinhalt ist "
                    "„Strategie in den Alltag überführen“, die Texte stammen von der Leistungsseite. A3 hoch und A3 quer, je zwei Varianten.",
                    ["Entwurf 1", "A3 hoch &amp; quer", "je 2 Varianten", "Beispiel: Strategie"], inhalt(), CSS)
    if mit_png:
        png_export(DATEI, "onepager")


if __name__ == "__main__":
    bauen("--ohne-png" not in sys.argv)
