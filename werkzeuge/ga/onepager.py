#!/usr/bin/env python3
"""One-Pager A3 – Entwurf 2 (Daniel, 10.10.2026): Aufbau wie die Volksfest-Seite.

Prinzip: wenige große Flächen übereinander (Weiß · Gelb · Weiß · Schwarz), viel Luft, große Lora-Überschriften,
pro Fläche genau eine Aussage. Nie Gelb auf Hellgrau.
  A3 hoch · A  Leistung mit Ansprechpartner  (Beispiel „Strategie in den Alltag überführen“)
  A3 hoch · B  Leistung ohne Person           (z. B. als Handout im Workshop)
  A3 hoch · C  Grundraster                    (leeres Raster zum Aufbereiten eigener Themen)
  A3 quer · A  Inhalt mit Ansprechpartner (Bild) – Kopf über volle Breite, drei Spalten, Fragenleiste, schwarzes Band
  A3 quer · B  Inhalt ohne Bild
  A3 quer · C  Kurzfassung mit schwarzer Titelspalte
  A3 quer · D  Grundraster mit schwarzer Titelspalte
PNG-Export (150 dpi) nach site/projekte/ga/onepager/.

Aufruf: python3 werkzeuge/ga/onepager.py [--ohne-png]
"""
import sys

from ga_basis import FIRMA, PERSONEN, abschnitt, download, figur, ico, logo, masse, png_export, raster, seite_schreiben, zeichen

DATEI = "ga-onepager.html"
PX = {"hoch": (1754, 2480), "quer": (2480, 1754)}
D = PERSONEN["daniel"]

LEISTUNG = dict(
    kicker="Strategiehandwerk",
    h1='Strategie in den Alltag <span class="hl">überführen.</span>',
    lead="Deine Strategie ist da – aber was bedeutet sie für Deinen Bereich? Wir machen sie greifbar und wirksam.",
    p_kicker="Das Problem",
    p_h2="Strategisches Denken wird vorausgesetzt. Beigebracht hat es Dir keiner.",
    p_label="Hart, weil das Fundament fehlt:",
    p_liste=["die klare Richtung", "die eigene Rolle", "das Handwerkszeug für den Alltag"],
    l_kicker="Die Lösung",
    l_h2="Rolle, Richtung, Handwerkszeug.",
    l_punkte=[("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"),
              ("compass", "Richtung", "Wie wollen wir wahrgenommen werden?"),
              ("wrench", "Handwerkszeug", "Wie kommen wir dorthin?")],
    e_kicker="Das Ergebnis",
    e_satz='Du führst Dein Team, statt es zu <span class="hl">vertrösten.</span>',
    nummern=False,
)
RASTER = dict(
    kicker="Thema",
    h1='Hier steht <span class="hl">das Thema.</span>',
    lead="Ein Satz, worum es geht und für wen es gedacht ist.",
    p_kicker="Ausgangslage",
    p_h2="Die Ausgangslage in einem klaren Satz.",
    p_label="Was heute fehlt:",
    p_liste=["Erster Punkt", "Zweiter Punkt", "Dritter Punkt"],
    l_kicker="Der Weg",
    l_h2="Drei Schritte zum Ergebnis.",
    l_punkte=[(None, "Schritt eins", "Kurz beschreiben, was passiert."),
              (None, "Schritt zwei", "Kurz beschreiben, was passiert."),
              (None, "Schritt drei", "Kurz beschreiben, was passiert.")],
    e_kicker="Das Ergebnis",
    e_satz='Das Ergebnis in einem <span class="hl">Satz.</span>',
    nummern=True,
)


def k(t):
    return f'<p class="op-k">{t}</p>'


def punkte(d):
    out = ""
    for i, (ic, t, p) in enumerate(d["l_punkte"]):
        kopf = f'<span class="op-nr">0{i + 1}</span>' if d["nummern"] else f'<span class="op-ico">{ico(ic, sw=1.5)}</span>'
        out += f'<div class="op-punkt">{kopf}<b>{t}</b><p>{p}</p></div>'
    return f'<div class="op-punkte">{out}</div>'


def problem_kasten(d):
    return (f'<div class="op-kasten"><p class="op-kasten__label">{d["p_label"]}</p>'
            f'<ul>{"".join(f"<li>{x}</li>" for x in d["p_liste"])}</ul></div>')


def fuss(art):
    """art: person | marke | raster"""
    if art == "person":
        return (f'<div class="op-person"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>{D["name"]}</b><span>{D["rolle2"]}</span></div></div>'
                f'<div class="op-kontakt"><span>{D["mail"]}</span><span>{D["tel"]}</span><span>www.empiria.de</span></div>')
    if art == "marke":
        return f'{logo(hell=True, cls="op-logo")}<div class="op-kontakt"><span>www.empiria.de</span></div>'
    return f'{logo(hell=True, cls="op-logo")}<div class="op-kontakt"><span>Workshop · Datum</span><span>www.empiria.de</span></div>'


def hoch(d, art, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["hoch"][0]}"' if png else ""
    pfeil = f'<span class="op-pfeil">{zeichen("forward", "#1a1817")}</span>'
    return (f'<div class="op op--hoch"{attr}>'
            f'<section class="op-kopf">{logo(cls="op-logo op-logo--kopf")}{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p>{pfeil}</section>'
            f'<section class="op-gelb"><div>{k(d["p_kicker"])}<h2>{d["p_h2"]}</h2></div>{problem_kasten(d)}</section>'
            f'<section class="op-weiss">{k(d["l_kicker"])}<h2>{d["l_h2"]}</h2>{punkte(d)}</section>'
            f'<section class="op-schwarz">{k(d["e_kicker"])}<p class="op-satz">{d["e_satz"]}</p><div class="op-fuss">{fuss(art)}</div></section>'
            f'</div>')


def fuss_spalte(art):
    """Fuß der schwarzen Titelspalte (quer)."""
    if art == "person":
        return (f'<div class="op-person"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>{D["name"]}</b><span>{D["rolle2"]}</span></div></div>'
                f'<div class="op-kontakt op-kontakt--liste"><span>{D["mail"]}</span><span>{D["tel"]}</span><span>www.empiria.de</span></div>')
    if art == "marke":
        return '<div class="op-kontakt op-kontakt--liste"><span>www.empiria.de</span></div>'
    return '<div class="op-kontakt op-kontakt--liste"><span>Workshop · Datum</span><span>www.empiria.de</span></div>'


def quer(d, art, png=None):
    """Schwarze Titelspalte links über die volle Höhe, rechts offene weiße Fläche ohne Kästen und Bänder."""
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["quer"][0]}"' if png else ""
    liste = (f'<div class="op-liste"><p class="op-liste__label">{d["p_label"]}</p>'
             f'<ul>{"".join(f"<li>{x}</li>" for x in d["p_liste"])}</ul></div>')
    return (f'<div class="op op--quer"{attr}>'
            f'<section class="op-spalte">{logo(hell=True, cls="op-logo")}'
            f'<div>{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p></div>'
            f'<div><span class="op-pfeil">{zeichen("forward", "#fff400")}</span>{fuss_spalte(art)}</div></section>'
            f'<div class="op-rechts">'
            f'<section class="op-zwei"><div>{k(d["p_kicker"])}<h2>{d["p_h2"]}</h2></div>{liste}</section>'
            f'<section>{k(d["l_kicker"])}<h2>{d["l_h2"]}</h2>{punkte(d)}</section>'
            f'<section>{k(d["e_kicker"])}<p class="op-satz">{d["e_satz"]}</p></section>'
            f'</div></div>')


# ---------- A3 quer · Inhalt: Kopf über die volle Breite, drei Spalten, Fragenleiste, schwarzes Band ----------
INHALT = dict(
    kicker="Strategiehandwerk",
    h1='Strategie in den Alltag <span class="hl">überführen.</span>',
    lead="Deine Strategie ist da – aber was bedeutet sie für Deinen Verantwortungsbereich? Wir machen sie greifbar und wirksam im Alltag.",
    spalten=[
        ("Problem", "Strategisches Denken wird vorausgesetzt. Beigebracht hat es Dir keiner.",
         "Du bist Bereichsleiter, weil Du fachlich überzeugt hast. Was folgt, sind harte Gespräche mit dem eigenen Team – hart, weil das Fundament fehlt:",
         [(None, "die klare Richtung", ""), (None, "die eigene Rolle", ""), (None, "das Handwerkszeug für den Alltag", "")]),
        ("Lösung", "Rolle, Richtung und Handwerkszeug für Deinen Bereich.", "",
         [("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"), ("compass", "Richtung", "Wie wollen wir wahrgenommen werden?"),
          ("wrench", "Handwerkszeug", "Wie kommen wir dorthin?")]),
        ("Zusammenarbeit", "So arbeiten wir wirklich zusammen.", "",
         [("01", "Direkter Draht, klare Worte", "Du arbeitest direkt mit mir und bekommst ehrliches Feedback."),
          ("02", "Dein Einsatz entscheidet", "Die Umsetzung bleibt Deine Aufgabe – plane ein bis zwei Stunden pro Woche ein."),
          ("03", "Dranbleiben", "Regelmäßig abstimmen, flexibel umsteuern, stringent umsetzen.")]),
    ],
    f_kicker="Perspektivwechsel",
    f_h="Wie sähe die Homepage Deines Bereichs aus?",
    fragen=["Welche Zielgruppe sprechen wir an?", "Welches Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
            "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"],
    ergebnis="Jeder im Team versteht, wofür Dein Bereich da ist – und Du bestimmst seine Wahrnehmung.",
)


def oi_zeile(kopf, titel, text):
    if kopf is None:
        k_html = '<span class="oi-strich"></span>'
    elif kopf.isdigit():
        k_html = f'<span class="oi-nr">{kopf}</span>'
    else:
        k_html = f'<span class="oi-ico">{ico(kopf, sw=1.5)}</span>'
    return f'<li>{k_html}<div><b>{titel}</b>{f"<p>{text}</p>" if text else ""}</div></li>'


def oi_spalte(kk, h, t, liste):
    return (f'<div class="oi-spalte">{k(kk)}<h2>{h}</h2>{f"<p class=oi-text>{t}</p>" if t else "<span></span>"}'
            f'<ul class="oi-liste">{"".join(oi_zeile(*z) for z in liste)}</ul></div>')


def oi_fuss(d, mit_bild):
    if mit_bild:
        links = (f'<div class="op-person"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>{D["name"]}</b><span>{D["rolle2"]}</span></div></div>'
                 f'<div class="oi-daten"><span>{D["mail"]}</span><span>{D["tel"]}</span><span>{FIRMA["web"]}</span></div>')
    else:
        links = (f'{logo(hell=True, cls="oi-logo-fuss")}'
                 f'<div class="oi-daten"><span>{FIRMA["name"]} · {FIRMA["strasse"]} · {FIRMA["ort"]}</span><span>{FIRMA["web"]}</span></div>')
    return (f'<footer class="oi-fuss"><div class="oi-links">{links}</div>'
            f'<div class="oi-ergebnis"><p class="op-k">Das Ergebnis</p><p>{d["ergebnis"]}</p></div></footer>')


def oi_kopf(d):
    return (f'<header class="oi-kopf">{logo(cls="oi-logo")}'
            f'<div class="oi-titel"><div>{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p></div>'
            f'<span class="oi-pfeil">{zeichen("forward", "#1a1817")}</span></div></header>')


def oi_fragen(d):
    fragen = "".join(f'<li><span class="oi-nr">0{i + 1}</span><b>{f}</b></li>' for i, f in enumerate(d["fragen"]))
    return f'<section class="oi-fragen">{k(d["f_kicker"])}<div class="oi-fragen__in"><h3>{d["f_h"]}</h3><ol>{fragen}</ol></div></section>'


def hoch_inhalt(d, mit_bild, png=None):
    """A3 hoch · Inhalt: Kopf, Problem | Lösung, Zusammenarbeit über die volle Breite, Fragen, schwarzes Band."""
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["hoch"][0]}"' if png else ""
    zk, zh, _, zl = d["spalten"][2]
    zus = (f'<section class="oi-zus"><div>{k(zk)}<h2>{zh}</h2></div>'
           f'<ul class="oi-liste oi-liste--quer">{"".join(oi_zeile(*z) for z in zl)}</ul></section>')
    return (f'<div class="op op--inhalt op--inhalt-hoch"{attr}>{oi_kopf(d)}'
            f'<section class="oi-spalten">{"".join(oi_spalte(*sp) for sp in d["spalten"][:2])}</section>'
            f'{zus}{oi_fragen(d)}{oi_fuss(d, mit_bild)}</div>')


def quer_inhalt(d, mit_bild, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX["quer"][0]}"' if png else ""
    return (f'<div class="op op--inhalt"{attr}>{oi_kopf(d)}'
            f'<section class="oi-spalten">{"".join(oi_spalte(*sp) for sp in d["spalten"])}</section>'
            f'{oi_fragen(d)}{oi_fuss(d, mit_bild)}</div>')


CSS_INHALT = masse("""
.op--inhalt { aspect-ratio: 420 / 297; display: flex; flex-direction: column; }
.op--inhalt > header, .op--inhalt > section, .op--inhalt > footer { padding: 0 [22]; }
.op--inhalt > .oi-kopf { padding-top: [16]; }
.oi-titel { display: flex; justify-content: space-between; align-items: flex-end; gap: [16]; margin-top: [14]; }
.op--inhalt h1 { font-size: [38pt]; line-height: 1.2; white-space: nowrap; }
.op--inhalt .op-lead { margin-top: [5]; font-size: [12pt]; max-width: [230]; }
.oi-logo { display: block; height: [8]; width: auto; margin-left: [-1.7]; }
.oi-pfeil { flex: 0 0 [40]; margin-bottom: [2]; }
.oi-pfeil svg { display: block; width: 100%; height: auto; }
.op--inhalt .op-k { font-size: [8pt]; margin-bottom: [4]; }
.oi-spalten { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto auto auto 1fr; column-gap: [14]; margin-top: [16]; }
.oi-spalte { display: grid; grid-template-rows: subgrid; grid-row: span 4; align-content: start; }
.op--inhalt h2 { font-size: [16pt]; line-height: 1.25; }
.oi-text { margin: [4] 0 0; font: 300 [9.5pt]/1.55 'Poppins', sans-serif; color: #3d3a37; }
.oi-liste { list-style: none; margin: [5] 0 0; padding: 0; }
.oi-liste li { display: grid; grid-template-columns: [8] 1fr; align-items: baseline; padding: [2.6] 0; border-top: [0.3] solid #d9d5cf; }
.oi-liste li:last-child { border-bottom: [0.3] solid #d9d5cf; }
.oi-liste b { display: block; font: 700 [11pt]/1.3 'Lora', serif; }
.oi-liste p { margin: [1] 0 0; font: 300 [9pt]/1.45 'Poppins', sans-serif; color: #3d3a37; }
.oi-strich { display: block; width: [3.5]; height: [0.6]; background: #1a1817; transform: translateY([-1.2]); }
.oi-ico { display: block; width: [5]; height: [5]; transform: translateY([0.8]); }
.oi-ico svg { display: block; width: 100%; height: 100%; }
.oi-nr { font: 700 [7.5pt]/1 'Poppins', sans-serif; letter-spacing: .12em; }
.op--inhalt > .oi-fragen { margin-top: auto; padding-top: [12]; padding-bottom: [14]; }
.oi-fragen__in { display: grid; grid-template-columns: repeat(3, 1fr); column-gap: [14]; align-items: start; }
.oi-fragen__in ol { grid-column: 2 / span 2; }
.oi-fragen h3 { margin: 0; font: 700 [14pt]/1.25 'Lora', serif; letter-spacing: -.01em; }
.oi-fragen ol { list-style: none; margin: 0; padding: 0; display: grid; grid-template-columns: repeat(5, 1fr); column-gap: [6]; }
.oi-fragen li { border-top: [0.6] solid #1a1817; padding-top: [3]; }
.oi-fragen li .oi-nr { display: block; margin-bottom: [2]; }
.oi-fragen li b { font: 700 [10.5pt]/1.3 'Lora', serif; }
.oi-fuss { background: #1a1817; color: #fff; display: grid; grid-template-columns: repeat(3, 1fr); column-gap: [14]; align-items: center; }
.op--inhalt > .oi-fuss { padding-top: [9]; padding-bottom: [9]; }
.oi-links { display: flex; align-items: center; gap: [10]; }
.oi-links .op-person img { width: [15]; height: [15]; }
.oi-links .op-person b { font-size: [11pt]; }
.oi-links .op-person span { font-size: [8pt]; }
.oi-logo-fuss { display: block; height: [7]; width: auto; margin-left: [-1.7]; }
.oi-daten { display: flex; flex-direction: column; gap: [1.2]; font: 400 [8.5pt]/1.3 'Poppins', sans-serif; color: rgba(255,255,255,.8); white-space: nowrap; }
.oi-ergebnis .op-k { color: #fff400; }
.op--inhalt:not(.op--inhalt-hoch) .op-k, .op--blatt-quer .op-k, .op--quer .op-k { gap: [3]; }
.op--inhalt:not(.op--inhalt-hoch) .op-k::before, .op--blatt-quer .op-k::before, .op--quer .op-k::before { width: [8]; height: [0.6]; }
.op--inhalt:not(.op--inhalt-hoch) .oi-ergebnis { grid-column: 2 / span 2; }
.oi-links { white-space: nowrap; }
.oi-ergebnis p:last-child { margin: 0; font: 700 [13pt]/1.35 'Lora', serif; }
""", 420)


CSS_INHALT_HOCH = masse("""
.op--inhalt-hoch { aspect-ratio: 297 / 420; }
.op--inhalt-hoch > header, .op--inhalt-hoch > section, .op--inhalt-hoch > footer { padding-left: [20]; padding-right: [20]; }
.op--inhalt-hoch > .oi-kopf { padding-top: [16]; }
.op--inhalt-hoch .oi-logo { height: [7]; margin-left: [-1.5]; }
.op--inhalt-hoch .oi-titel { margin-top: [18]; gap: [12]; }
.op--inhalt-hoch h1 { font-size: [40pt]; line-height: 1.3; white-space: normal; }
.op--inhalt-hoch .op-lead { margin-top: [7]; font-size: [12pt]; max-width: [170]; }
.op--inhalt-hoch .oi-pfeil { flex-basis: [42]; }
.op--inhalt-hoch .op-k { font-size: [8pt]; margin-bottom: [4]; }
.op--inhalt-hoch .oi-spalten { grid-template-columns: repeat(2, 1fr); column-gap: [14]; margin-top: [18]; }
.op--inhalt-hoch h2 { font-size: [16pt]; }
.op--inhalt-hoch .oi-text { font-size: [9.5pt]; margin-top: [4]; }
.op--inhalt-hoch .oi-liste { margin-top: [5]; }
.op--inhalt-hoch .oi-liste li { grid-template-columns: [8] 1fr; padding: [2.6] 0; border-width: [0.3]; }
.op--inhalt-hoch .oi-liste b { font-size: [11pt]; }
.op--inhalt-hoch .oi-liste p { font-size: [9pt]; margin-top: [1]; }
.op--inhalt-hoch .oi-strich { width: [3.5]; height: [0.6]; transform: translateY([-1.2]); }
.op--inhalt-hoch .oi-ico { width: [5]; height: [5]; transform: translateY([0.8]); }
.op--inhalt-hoch .oi-nr { font-size: [7.5pt]; }
.op--inhalt-hoch > .oi-zus { margin-top: auto; padding-top: [14]; }
.oi-liste--quer { display: grid; grid-template-columns: repeat(3, 1fr); column-gap: [10]; }
.oi-liste--quer li, .oi-liste--quer li:last-child { grid-template-columns: [8] 1fr; border-bottom: 0; border-top: [0.6] solid #1a1817; }
.op--inhalt-hoch > .oi-fragen { margin-top: auto; padding-top: [14]; padding-bottom: [14]; }
.op--inhalt-hoch .oi-liste--quer li, .op--inhalt-hoch .oi-liste--quer li:last-child { border-top: [0.6] solid #1a1817; border-bottom: 0; }
.op--inhalt-hoch .oi-fragen__in { display: block; }
.op--inhalt-hoch .oi-fragen h3 { font-size: [14pt]; margin-bottom: [6]; }
.op--inhalt-hoch .oi-fragen ol { column-gap: [5]; }
.op--inhalt-hoch .oi-fragen li { border-top-width: [0.6]; padding-top: [3]; }
.op--inhalt-hoch .oi-fragen li .oi-nr { margin-bottom: [2]; }
.op--inhalt-hoch .oi-fragen li b { font-size: [10pt]; }
.op--inhalt-hoch > .oi-fuss { grid-template-columns: 1fr; row-gap: [7]; padding-top: [10]; padding-bottom: [11]; column-gap: 0; }
.op--inhalt-hoch .oi-ergebnis { order: -1; }
.op--inhalt-hoch .oi-ergebnis p:last-child { font-size: [15pt]; }
.op--inhalt-hoch .oi-links { justify-content: space-between; gap: [8]; padding-top: [6]; border-top: [0.3] solid rgba(255,255,255,.25); }
.op--inhalt-hoch .oi-links .op-person img { width: [14]; height: [14]; }
.op--inhalt-hoch .oi-links .op-person b { font-size: [11pt]; }
.op--inhalt-hoch .oi-links .op-person span { font-size: [8pt]; }
.op--inhalt-hoch .oi-daten { flex-direction: row; gap: [6]; font-size: [8.5pt]; }
.op--inhalt-hoch .oi-logo-fuss { height: [6.5]; margin-left: [-1.4]; }
""", 297)


# ---------- Arbeitsblatt: druckerfreundlich, nur Weiß – Kopf und eine angedeutete Inhaltsfläche ----------
BLATT = dict(
    kicker="Workshop",
    h1='Hier steht die <span class="hl">Überschrift.</span>',
    lead="Ein Satz, worum es auf diesem Blatt geht.",
)


def arbeitsblatt(d, fmt, png=None):
    attr = f' data-png="ga/onepager/{png}.png" data-pw="{PX[fmt][0]}"' if png else ""
    return (f'<div class="op op--blatt op--blatt-{fmt}"{attr}><div class="ab-in">'
            f'<header class="ab-kopf">{logo(cls="oi-logo")}</header>'
            f'<div class="ab-titel">{k(d["kicker"])}<h1>{d["h1"]}</h1><p class="op-lead">{d["lead"]}</p></div>'
            f'<div class="ab-flaeche"><span>Inhaltsfläche</span></div>'
            f'<footer class="ab-fuss"><span>{FIRMA["web"]}</span></footer></div></div>')


def css_blatt(w, rand, h1):
    f = 'hoch' if w == 297 else 'quer'
    return masse(f"""
.op--blatt-{f} {{ aspect-ratio: {w} / {297 if w == 420 else 420}; }}
.op--blatt-{f} .ab-in {{ position: absolute; inset: 0; display: flex; flex-direction: column; padding: [16] [{rand}] [12]; }}
.op--blatt-{f} .ab-kopf {{ position: absolute; right: [{rand}]; top: [16]; }}
.op--blatt-{f} .oi-logo {{ height: [7]; margin: 0; }}
.op--blatt-{f} .ab-titel {{ margin-top: 0; padding-right: [40]; }}
.op--blatt-{f} .op-k {{ font-size: [8pt]; margin-bottom: [4]; }}
.op--blatt-{f} h1 {{ font-size: [{h1}pt]; line-height: 1.3; }}
.op--blatt-{f} .op-lead {{ margin-top: [4]; font-size: [11pt]; max-width: [200]; }}
.op--blatt-{f} .ab-flaeche {{ flex: 1; min-height: 0; margin-top: [12]; border: [0.3] dashed #cfc9c1; border-radius: [2];
  display: flex; align-items: center; justify-content: center; }}
.op--blatt-{f} .ab-flaeche span {{ font: 600 [8pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #b3ada5; }}
.op--blatt-{f} .ab-fuss {{ display: flex; justify-content: flex-end; margin-top: [6]; font: 400 [7.5pt]/1 'Poppins', sans-serif; color: #6b6762; letter-spacing: .04em; }}
""", w)


CSS_BLATT = css_blatt(297, 20, 30) + css_blatt(420, 22, 32)


CSS_HOCH = masse("""
.ga .op h1, .ga .op h2, .ga .op h3 { color: inherit; }
.op li, .op p { line-height: 1.4; }
.op li b { display: block; }
.op { line-height: 1.4; }
.op { position: relative; container-type: inline-size; background: #fff; color: #1a1817; overflow: hidden;
  box-shadow: 0 0 0 1px #e4e0db, 0 18px 40px rgba(26,24,23,.08); font-family: 'Poppins', sans-serif; }
.op--hoch { aspect-ratio: 297 / 420; display: grid; grid-template-rows: 36% 22% 22% 20%; }
.op section { position: relative; padding: [20] [24]; }
.op-logo { display: block; height: [7]; width: auto; }
.op-logo--kopf { position: absolute; top: [16]; left: [24]; }
.op-k { display: flex; align-items: center; gap: [3]; margin: 0 0 [5]; font: 700 [9pt]/1 'Poppins', sans-serif; letter-spacing: .16em; text-transform: uppercase; }
.op-k::before { content: ""; width: [8]; height: [0.6]; background: currentColor; }
.op h1 { margin: 0; font: 700 [56pt]/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; }
.op h2 { margin: 0; font: 700 [26pt]/1.25 'Lora', Georgia, serif; letter-spacing: -.015em; }
.op .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; white-space: nowrap; }
.op-lead { margin: [7] 0 0; max-width: [160]; font: 300 [14pt]/1.55 'Poppins', sans-serif; color: #3d3a37; }
.op-kopf { display: flex; flex-direction: column; justify-content: flex-end; padding-bottom: [22] !important; }
.op-kopf > :not(.op-logo):not(.op-pfeil) { max-width: [190]; }
.op-pfeil { position: absolute; right: [24]; bottom: [22]; width: [52]; }
.op-pfeil svg { display: block; width: 100%; height: auto; }
.op-gelb { background: #fff400; display: grid; grid-template-columns: 1.1fr .9fr; gap: [14]; align-items: center; }
.op-kasten { background: #1a1817; color: #fff; border-radius: [5]; padding: [10] [11]; }
.op-kasten__label { margin: 0 0 [4]; font: 600 [11pt]/1.4 'Poppins', sans-serif; color: rgba(255,255,255,.7); }
.op-kasten ul { list-style: none; margin: 0; padding: 0; }
.op-kasten li { position: relative; padding: [2.2] 0 [2.2] [6]; font: 700 [14pt]/1.35 'Lora', serif; }
.op-kasten li::before { content: ""; position: absolute; left: 0; top: [5]; width: [2.4]; height: [2.4]; border-radius: 50%; background: #fff400; }
.op-weiss { display: flex; flex-direction: column; justify-content: center; }
.op-punkte { display: grid; grid-template-columns: repeat(3, 1fr); gap: [12]; margin-top: [10]; }
.op-punkt { border-top: [0.6] solid #1a1817; padding-top: [6]; }
.op-ico { display: block; width: [9]; height: [9]; margin-bottom: [4]; }
.op-ico svg { width: 100%; height: 100%; display: block; }
.op-nr { display: block; margin-bottom: [3]; font: 700 [22pt]/1 'Lora', serif; }
.op-punkt b { display: block; font: 700 [15pt]/1.25 'Lora', serif; }
.op-punkt p { margin: [2.5] 0 0; font: 300 [11pt]/1.5 'Poppins', sans-serif; color: #3d3a37; }
.op-schwarz { background: #1a1817; color: #fff; display: flex; flex-direction: column; justify-content: center; }
.op-satz { margin: 0; max-width: [230]; font: 700 [30pt]/1.25 'Lora', serif; letter-spacing: -.015em; }
.op-schwarz .hl { color: #1a1817; }
.op-fuss { display: flex; align-items: center; justify-content: space-between; gap: [10]; margin-top: [12]; padding-top: [7]; border-top: [0.3] solid rgba(255,255,255,.25); }
.op-person { display: flex; align-items: center; gap: [5]; }
.op-person img { width: [16]; height: [16]; border-radius: 50%; object-fit: cover; filter: grayscale(1); background: #3a3733; }
.op-person b { display: block; font: 700 [12pt]/1.2 'Lora', serif; }
.op-person span { display: block; margin-top: [1]; font: 400 [9pt]/1.3 'Poppins', sans-serif; color: rgba(255,255,255,.65); }
.op-kontakt { display: flex; gap: [7]; font: 400 [10pt]/1.3 'Poppins', sans-serif; color: rgba(255,255,255,.85); }
.op-schwarz .op-k { color: #fff400; }
""", 297)

CSS_QUER = masse("""
.op--quer { aspect-ratio: 420 / 297; display: grid; grid-template-columns: 34% 66%; }
.op--quer .op-spalte { background: #1a1817; color: #fff; padding: [20] [18] [18]; display: flex; flex-direction: column; justify-content: space-between; }
.op-spalte .op-k { color: #fff400; }
.op-spalte > .op-logo { align-self: flex-start; }
.op--quer h1 { line-height: 1.3; }
.op--quer h1 { font-size: [40pt]; }
.op-spalte .hl { color: #1a1817; }
.op--quer .op-lead { font-size: [12pt]; max-width: none; color: rgba(255,255,255,.75); }
.op--quer .op-pfeil { position: static; display: block; width: [30]; margin-bottom: [12]; }
.op--quer .op-person img { width: [13]; height: [13]; }
.op--quer .op-person b { font-size: [11pt]; }
.op--quer .op-person span { font-size: [8pt]; }
.op-kontakt--liste { flex-direction: column; gap: [1.6]; margin-top: [6]; font-size: [9pt]; color: rgba(255,255,255,.8); }
.op-rechts { display: flex; flex-direction: column; justify-content: space-between; padding: [20] [22] [20] [22]; }
.op--quer .op-rechts section { padding: 0; }
.op--quer .op-k { font-size: [8pt]; margin-bottom: [4]; }
.op--quer h2 { font-size: [20pt]; }
.op-zwei { display: grid; grid-template-columns: 1fr 1fr; gap: [16]; align-items: start; }
.op-liste__label { margin: [1] 0 [3]; font: 600 [10pt]/1.4 'Poppins', sans-serif; color: #6b6762; }
.op-liste ul { list-style: none; margin: 0; padding: 0; }
.op-liste li { position: relative; padding: [2.4] 0 [2.4] [7]; border-bottom: [0.3] solid #d9d5cf; font: 700 [12.5pt]/1.35 'Lora', serif; }
.op-liste li::before { content: ""; position: absolute; left: 0; top: [5.3]; width: [3.5]; height: [0.6]; background: #1a1817; }
.op--quer .op-punkte { margin-top: [7]; gap: [12]; }
.op--quer .op-punkt b { font-size: [13pt]; }
.op--quer .op-punkt p { font-size: [10pt]; }
.op--quer .op-ico { width: [7]; height: [7]; margin-bottom: [3]; }
.op--quer .op-nr { font-size: [18pt]; }
.op--quer .op-satz { font-size: [24pt]; max-width: none; }
""", 420)

SEITE_CSS = """
.op-reihe { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.6rem; margin-top: 1.8rem; align-items: start; }
.op-reihe--quer { grid-template-columns: repeat(2, minmax(0, 1fr)); }
.op-reihe--blatt { grid-template-columns: minmax(0, 297fr) minmax(0, 594fr); align-items: end; }
@media (max-width: 900px) { .op-reihe, .op-reihe--quer, .op-reihe--blatt { grid-template-columns: 1fr; } }
"""


def inhalt(mit_png):
    def dl(n, t):
        return download(f"ga/onepager/{n}.png", t)

    def f(html_fn, name, label, groesse):
        return figur(html_fn(name if mit_png else None), label, dl(name, f"PNG · {groesse} px"))
    H, Q = "1754 × 2480", "2480 × 1754"
    hi = [f(lambda n: hoch_inhalt(INHALT, True, n), "a3-hoch-inhalt-person", "A · mit Ansprechpartner", H),
          f(lambda n: hoch_inhalt(INHALT, False, n), "a3-hoch-inhalt", "B · ohne Bild", H)]
    hk = [f(lambda n: hoch(LEISTUNG, "person", n), "a3-hoch-leistung-person", "C · mit Ansprechpartner", H),
          f(lambda n: hoch(LEISTUNG, "marke", n), "a3-hoch-leistung", "D · ohne Bild", H),
          f(lambda n: hoch(RASTER, "raster", n), "a3-hoch-raster", "E · Grundraster", H)]
    qi = [f(lambda n: quer_inhalt(INHALT, True, n), "a3-quer-inhalt-person", "A · mit Ansprechpartner", Q),
          f(lambda n: quer_inhalt(INHALT, False, n), "a3-quer-inhalt", "B · ohne Bild", Q)]
    qk = [f(lambda n: quer(LEISTUNG, "person", n), "a3-quer-leistung", "C · mit Ansprechpartner", Q),
          f(lambda n: quer(RASTER, "raster", n), "a3-quer-raster", "D · Grundraster", Q)]
    ab = [f(lambda n: arbeitsblatt(BLATT, "hoch", n), "a3-hoch-arbeitsblatt", "Arbeitsblatt hoch", H),
          f(lambda n: arbeitsblatt(BLATT, "quer", n), "a3-quer-arbeitsblatt", "Arbeitsblatt quer", Q)]
    return (abschnitt("A3 hoch · Inhalt",
                      "Das Arbeitsformat für echte Inhalte: Überschrift über die volle Breite, darunter Problem und Lösung nebeneinander, "
                      "die Zusammenarbeit in drei Schritten, fünf Fragen und unten ein schwarzes Band mit dem Ergebnis.",
                      f'<div class="op-reihe op-reihe--quer">{"".join(hi)}</div>')
            + abschnitt("A3 hoch · Kurzfassung",
                        "Wenig Text, große Flächen wie auf der Volksfest-Seite: Thema, Problem, Lösung, Ergebnis – je Fläche eine Aussage.",
                        f'<div class="op-reihe">{"".join(hk)}</div>')
            + abschnitt("A3 quer · Inhalt",
                        "Überschrift über die volle Breite, darunter drei gleich breite Spalten (Problem, Lösung, Zusammenarbeit), "
                        "fünf Fragen und unten ein schwarzes Band mit dem Ergebnis.",
                        f'<div class="op-reihe op-reihe--quer">{"".join(qi)}</div>')
            + abschnitt("A3 quer · Kurzfassung",
                        "Wenig Text: schwarze Titelspalte links, rechts eine offene weiße Fläche mit Problem, Lösung und Ergebnis.",
                        f'<div class="op-reihe op-reihe--quer">{"".join(qk)}</div>')
            + abschnitt("Arbeitsblatt · hoch und quer",
                        "Für Workshops und zum Ausdrucken: fast nur Weiß, keine schwarzen oder gelben Flächen. Oben Logo, Überschrift und ein Satz, "
                        "darunter die freie Fläche für den Inhalt (gestrichelt angedeutet, wird nicht gedruckt).",
                        f'<div class="op-reihe op-reihe--blatt">{"".join(ab)}</div>'))


def main():
    mit_png = "--ohne-png" not in sys.argv
    seite_schreiben(DATEI, "One-Pager", 'One-<span class="hl">Pager</span>',
                    "Ein Blatt für eine Leistung oder ein Thema, in A3 hoch und quer. Die Inhaltsfassung trägt echte Inhalte über die volle Breite, "
                    "die Kurzfassung arbeitet mit wenig Text und großen Flächen. Jeweils mit Ansprechpartner oder ohne Bild.",
                    ["Entwurf 3", "A3 hoch & quer", "Inhalt & Kurzfassung", "mit / ohne Bild"],
                    inhalt(mit_png), CSS_HOCH + CSS_QUER + CSS_INHALT + CSS_INHALT_HOCH + CSS_BLATT + SEITE_CSS)
    if mit_png:
        png_export(DATEI, "onepager")


if __name__ == "__main__":
    main()
