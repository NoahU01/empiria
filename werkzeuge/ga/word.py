#!/usr/bin/env python3
"""Word-Vorlagen – Entwürfe (Daniel, 10.10.2026).

Briefbogen A4 nach DIN 5008 (Form B) mit erster Seite und Folgeseite sowie Dokumentvorlage mit Titel- und Inhaltsseite
(Formatvorlagen H1–H3, Text, Liste, Tabelle, Zitat). Je zwei Varianten:
  Brief A · Ruhig    – Logo rechts, Fußzeile in vier Spalten mit feiner Linie
  Brief B · Akzent   – Logo links, Claim rechts, Fußzeile auf grauer Fläche
  Dokument A · Weiß  – helle Titelseite, Tabellenkopf schwarz
  Dokument B · Schwarz – schwarze Titelseite mit angeschnittenem Doppelpfeil, Tabellenkopf gelb
Die Seiten sind HTML-Attrappen in echten Maßen; daraus werden später die .dotx-Vorlagen gebaut.

Aufruf: python3 werkzeuge/ga/word.py
"""
from ga_basis import (GELB, SCHWARZ, FIRMA, PERSONEN, abschnitt, figur, logo, masse, ph, raster, seite_schreiben,
                      zeichen)

DATEI = "ga-word.html"
B = 210  # mm
D = PERSONEN["daniel"]


def blatt(inhalt, cls="", bg="#fff", fg=SCHWARZ):
    return masse(f'<div class="wd ga-blatt {cls}" style="--bg:{bg};--fg:{fg}"><div class="wd-in">{inhalt}</div></div>', B)


def fv(name):
    """Marke für die Formatvorlage am linken Rand (nur Ansicht, nicht Teil der Vorlage)."""
    return f'<span class="wd-fv">{name}</span>'


# ---------------- Briefbogen ----------------
def anschrift():
    zeilen = ["Musterfirma GmbH", "Frau Erika Mustermann", "Musterstraße 1", "12345 Musterstadt"]
    return ('<div class="wd-anschrift">'
            f'<p class="wd-ruecksende">{FIRMA["name"]} · {FIRMA["strasse"]} · {FIRMA["ort"]}</p>'
            '<div class="wd-adresse">' + "".join(f"<p>{ph(z)}</p>" for z in zeilen) + '</div></div>')


def infoblock():
    zeilen = [("Ansprechpartner", D["name"]), ("Telefon", D["tel"]), ("E-Mail", D["mail"]), ("Datum", "10. Oktober 2026")]
    return '<div class="wd-info">' + "".join(f'<p><span>{a}</span>{b}</p>' for a, b in zeilen) + '</div>'


def falzmarken():
    return '<span class="wd-falz" style="top:[105]"></span><span class="wd-loch"></span><span class="wd-falz" style="top:[210]"></span>'


def din_raster():
    return ('<div class="wd-din">'
            '<span class="wd-din-box" style="left:[20];top:[45];width:[85];height:[45]"><i>Anschriftfeld 85 × 45 mm</i></span>'
            '<span class="wd-din-box" style="left:[20];top:[45];width:[85];height:[17.7]"><i>Zusatz- und Vermerkzone</i></span>'
            '<span class="wd-din-box" style="left:[125];top:[50];width:[75];height:[40]"><i>Informationsblock</i></span>'
            '<span class="wd-din-box wd-din-text" style="left:[25];top:[98.5];width:[165];height:[168]"><i>Textbereich · Rand links 25 mm, rechts 20 mm</i></span>'
            '</div>')


BRIEF_TEXT = [
    "vielen Dank für das offene Gespräch in der vergangenen Woche. Wie besprochen, fasse ich Ihnen hier unseren Vorschlag zusammen, "
    "wie wir Ihre Strategie gemeinsam in den Alltag Ihres Bereichs überführen.",
    "Im Mittelpunkt stehen drei Dinge, die Ihnen als Führungskraft Handlungsklarheit verschaffen: Ihre Rolle, die Richtung Ihres Bereichs "
    "und das praktische Handwerkszeug für den Alltag. Dafür arbeiten wir in kurzen, regelmäßigen Terminen – direkt mit Ihnen und, wo es "
    "sinnvoll ist, mit einzelnen Personen aus Ihrem Team.",
]
BRIEF_TEXT2 = [
    "Damit das gelingt, planen Sie bitte ein bis zwei Stunden pro Woche ein. Eine Strategie im Alltag zu verankern, geht nicht von heute "
    "auf morgen – sie funktioniert nur, wenn wir dranbleiben.",
    "Gerne stimmen wir die nächsten Schritte in einem kurzen Telefonat ab. Ich melde mich dazu Anfang nächster Woche bei Ihnen.",
]


def gruss():
    return f'<p>Mit freundlichen Grüßen</p><p class="wd-unterschrift">{D["name"]}<br><span>{D["rolle"]}</span></p>'


def fusszeile_a():
    spalten = [
        [FIRMA["name"], FIRMA["strasse"], FIRMA["ort"]],
        [f'Telefon {D["tel"]}', D["mail"], FIRMA["web"]],
        [f'Geschäftsführer {FIRMA["gf"]}', f'{FIRMA["gericht"]} · {FIRMA["hrb"]}', f'USt-IdNr. {FIRMA["ust"]}'],
        [ph("Bank"), ph("IBAN DE.. .... .... .... .... .."), ph("BIC ........")],
    ]
    return '<div class="wd-fuss wd-fuss--a">' + "".join("<div>" + "".join(f"<p>{z}</p>" for z in s) + "</div>" for s in spalten) + '</div>'


def fusszeile_b():
    zeilen = [f'<b>{FIRMA["name"]}</b> · {FIRMA["strasse"]} · {FIRMA["ort"]} · {FIRMA["web"]}',
              f'Geschäftsführer {FIRMA["gf"]} · {FIRMA["gericht"]} {FIRMA["hrb"]} · USt-IdNr. {FIRMA["ust"]} · '
              f'{ph("Bank · IBAN DE.. · BIC ....")}']
    return '<div class="wd-fuss wd-fuss--b">' + "".join(f"<p>{z}</p>" for z in zeilen) + '</div>'


def brief_kopf(var):
    if var == "a":
        return logo(cls="wd-logo wd-logo--rechts")
    return logo(cls="wd-logo wd-logo--links") + '<p class="wd-claim">Strategie, die <span class="wd-hl">wirkt.</span></p>'


def brief_erste(var):
    text = "".join(f"<p>{t}</p>" for t in BRIEF_TEXT)
    return blatt(din_raster() + falzmarken() + brief_kopf(var) + anschrift() + infoblock() +
                 '<div class="wd-brieftext">'
                 '<p class="wd-betreff">Strategie in den Alltag überführen – unser Vorschlag</p>'
                 f'<p>Sehr geehrte Frau {ph("Mustermann")},</p>{text}</div>' +
                 (fusszeile_a() if var == "a" else fusszeile_b()), f"wd--brief wd--{var}")


def brief_folge(var):
    kopf = (logo(cls="wd-logo wd-logo--rechts wd-logo--klein") if var == "a" else
            logo(cls="wd-logo wd-logo--links wd-logo--klein") + f'<span class="wd-kopfpfeil">{zeichen("forward", SCHWARZ)}</span>')
    text = "".join(f"<p>{t}</p>" for t in BRIEF_TEXT2)
    return blatt(falzmarken() + kopf + f'<div class="wd-brieftext wd-brieftext--folge">{text}{gruss()}</div>'
                 '<p class="wd-seite">Seite 2 von 2</p>', f"wd--brief wd--folge wd--{var}")


# ---------------- Dokumentvorlage ----------------
def doku_titel(var):
    if var == "a":
        return blatt(logo(cls="wd-logo wd-logo--links") +
                     '<div class="wd-titel">'
                     '<p class="wd-kicker">Konzept</p>'
                     '<p class="wd-h-titel">Strategie in den Alltag <span class="wd-hl">überführen.</span></p>'
                     '<p class="wd-untertitel">Rolle, Richtung und Handwerkszeug für Deinen Bereich</p></div>'
                     f'<span class="wd-titelpfeil">{zeichen("forward", SCHWARZ)}</span>'
                     '<div class="wd-meta">' + "".join(f'<p><span>{a}</span>{b}</p>' for a, b in [
                         ("Für", ph("Musterfirma GmbH")), ("Von", f'{D["name"]}, {FIRMA["name"]}'), ("Stand", "Oktober 2026 · Version 1.0")]) +
                     '</div>', "wd--doku wd--titel-a")
    return blatt(logo(True, "wd-logo wd-logo--links") +
                 f'<span class="wd-titelpfeil wd-titelpfeil--b">{zeichen("forward", GELB)}</span>'
                 '<div class="wd-titel wd-titel--b">'
                 '<p class="wd-kicker">Konzept</p>'
                 '<p class="wd-h-titel">Strategie in den Alltag <span class="wd-hl">überführen.</span></p>'
                 '<p class="wd-untertitel">Rolle, Richtung und Handwerkszeug für Deinen Bereich</p>'
                 '<div class="wd-meta wd-meta--b">' + "".join(f'<p><span>{a}</span>{b}</p>' for a, b in [
                     ("Für", ph("Musterfirma GmbH")), ("Von", f'{D["name"]}, {FIRMA["name"]}'), ("Stand", "Oktober 2026 · Version 1.0")]) +
                 '</div></div>', "wd--doku wd--titel-b", SCHWARZ, "#fff")


def doku_inhalt(var):
    zeilen = [("Rolle", "Wofür stehe ich und mein Bereich?", "Klares Selbstverständnis"),
              ("Richtung", "Wie wollen wir wahrgenommen werden?", "Gemeinsames Zielbild"),
              ("Handwerkszeug", "Wie kommen wir dort hin?", "Werkzeuge für den Alltag")]
    tabelle = ('<table class="wd-tab"><thead><tr><th>Baustein</th><th>Leitfrage</th><th>Ergebnis</th></tr></thead><tbody>' +
               "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td></tr>" for a, b, c in zeilen) + '</tbody></table>')
    kopf = (logo(cls="wd-logo wd-logo--links wd-logo--klein") + '<p class="wd-kopftitel">Strategie in den Alltag überführen</p>')
    inhalt = (
        f'<div class="wd-doc">'
        f'<div class="wd-zeile">{fv("Überschrift 1")}<h2 class="wd-h1"><span class="wd-nr">1</span>Ausgangslage</h2></div>'
        f'<div class="wd-zeile">{fv("Standard")}<p>Strategisches Denken wird vorausgesetzt – beigebracht hat es aber kaum jemandem. '
        'Wer Abteilungs- oder Bereichsleiter wird, hat fachlich überzeugt. Was danach oft folgt, sind harte Gespräche mit dem eigenen Team.</p></div>'
        f'<div class="wd-zeile">{fv("Überschrift 2")}<h3 class="wd-h2">1.1 Was fehlt</h3></div>'
        f'<div class="wd-zeile">{fv("Aufzählung")}<ul class="wd-liste"><li>die klare Richtung</li><li>die eigene Rolle</li><li>das Handwerkszeug für den Alltag</li></ul></div>'
        f'<div class="wd-zeile">{fv("Überschrift 3")}<h4 class="wd-h3">Drei Bausteine</h4></div>'
        f'<div class="wd-zeile">{fv("Tabelle")}{tabelle}</div>'
        f'<div class="wd-zeile">{fv("Beschriftung")}<p class="wd-beschr">Tabelle 1 · Bausteine des Strategiemodells</p></div>'
        f'<div class="wd-zeile">{fv("Zitat")}<blockquote class="wd-zitat"><p>„Strategie ist keine Zauberei, sondern Handwerk.“</p>'
        f'<cite>{D["name"]}</cite></blockquote></div>'
        f'<div class="wd-zeile">{fv("Standard")}<p>Jeder im Team versteht, wofür der Bereich da ist – und die Führungskraft bestimmt seine Wahrnehmung.</p></div>'
        '</div>')
    fuss = f'<div class="wd-dfuss"><span>{FIRMA["name"]} · Strategie in den Alltag überführen</span><span>Seite 2</span></div>'
    return blatt(kopf + inhalt + fuss, f"wd--doku wd--inhalt wd--i{var}")


def schalter(name, text, an=True):
    return (f'<input type="checkbox" class="wd-schalter wd-schalter--{name}" id="wd-{name}"{" checked" if an else ""}>'
            f'<label class="wd-schalter-label" for="wd-{name}"><span></span>{text}</label>')


def inhalt():
    teile = []
    for var, titel, text in [
        ("a", "Briefbogen · Variante A · Ruhig", "Logo rechts oben, darunter nichts als Anschrift und Informationsblock. Die Fußzeile trägt alle "
         "Pflichtangaben in vier Spalten über einer feinen Linie. Druckt auf jedem Bürodrucker sauber."),
        ("b", "Briefbogen · Variante B · Akzent", "Logo links, rechts der Claim mit gelbem Highlight. Die Fußzeile steht auf einer grauen Fläche "
         "bis zum Rand – wirkt hochwertiger, braucht aber vorgedrucktes Papier oder randlosen Druck. Folgeseite mit kleinem Doppelpfeil."),
    ]:
        teile.append(abschnitt(titel, text, schalter(f"din{var}", "DIN-5008-Raster einblenden", False) + raster([
            figur(brief_erste(var), "<b>Erste Seite</b> · A4 · DIN 5008 Form B"),
            figur(brief_folge(var), "<b>Folgeseite</b> · A4")])))
    for var, titel, text in [
        ("a", "Dokumentvorlage · Variante A · Weiß", "Helle Titelseite mit großem Doppelpfeil und Metadaten unten. Auf der Inhaltsseite "
         "Tabellenkopf in Schwarz, Aufzählungszeichen und Zitatlinie in Gelb."),
        ("b", "Dokumentvorlage · Variante B · Schwarz", "Schwarze Titelseite, der gelbe Doppelpfeil läuft aus dem rechten Rand. Inhaltsseite "
         "mit gelbem Tabellenkopf und schwarzen Aufzählungsstrichen – sonst identisch."),
    ]:
        teile.append(abschnitt(titel, text, schalter(f"fv{var}", "Namen der Formatvorlagen einblenden") + raster([
            figur(doku_titel(var), "<b>Titelseite</b> · A4"),
            figur(doku_inhalt(var), "<b>Inhaltsseite</b> · A4 · Formatvorlagen")])))
    fvs = [("Titel", "Lora Bold", "40 pt", "Zeilenabstand 1,15"), ("Überschrift 1", "Lora Bold", "20 pt", "vor 18 pt, nach 8 pt · mit Nummer"),
           ("Überschrift 2", "Lora Bold", "14 pt", "vor 14 pt, nach 6 pt"), ("Überschrift 3", "Poppins SemiBold", "10 pt", "Großbuchstaben, gesperrt, nach 6 pt"),
           ("Standard", "Poppins Regular", "9,5 pt", "Zeilenabstand 1,5 · nach 6 pt"), ("Aufzählung", "Poppins Regular", "9,5 pt", "Zeichen: Quadrat Gelb (A) / Strich Schwarz (B)"),
           ("Tabelle", "Poppins", "8,5 pt", "Kopf Schwarz/Weiß (A) oder Gelb/Schwarz (B), Linien 0,5 pt"),
           ("Zitat", "Lora Bold", "13 pt", "gelbe Linie links, 3 pt"), ("Beschriftung", "Poppins Regular", "7,5 pt", "Grau #6F6A64")]
    tab = ('<div class="wd-fvtab"><table><thead><tr><th>Formatvorlage</th><th>Schrift</th><th>Größe</th><th>Abstand &amp; Details</th></tr></thead><tbody>' +
           "".join(f"<tr><td><b>{a}</b></td><td>{b}</td><td>{c}</td><td>{d}</td></tr>" for a, b, c, d in fvs) + '</tbody></table></div>')
    teile.append(abschnitt("Formatvorlagen im Überblick", "Diese Formatvorlagen werden in der Word-Vorlage hinterlegt – damit jedes Dokument "
                           "automatisch richtig aussieht. Seitenränder: oben 25 mm, links 25 mm, rechts 20 mm, unten 25 mm.", tab))
    hinweis = (f'<p class="ga-hinweis">{ph("gestrichelt")}<span>= Platzhalter. Empfängeranschrift und Bankverbindung sind Beispiele; '
               f'die Bankdaten fehlen noch. Brieftext und Dokumentinhalt sind Beispieltext auf Basis der Seite „Strategie in den Alltag überführen“.</span></p>')
    return hinweis + "".join(teile)


CSS = masse("""
.wd { position: relative; aspect-ratio: 210 / 297; container-type: inline-size; background: var(--bg); color: var(--fg); overflow: hidden;
  border-radius: 3px; font-family: 'Poppins', sans-serif; }
.wd p, .wd h1, .wd h2, .wd h3, .wd h4, .wd ul, .wd blockquote { margin: 0; }
.wd-in { position: absolute; inset: 0; font: 400 [9.5pt]/1.5 'Poppins', sans-serif; }
.wd-hl { background: #fff400; color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; }
.wd-logo { position: absolute; top: [17]; height: [10]; width: auto; display: block; }
.wd-logo--rechts { right: [18.5]; }
.wd-logo--links { left: [23.5]; }
.wd-logo--klein { top: [12]; height: [7]; }
.wd-claim { position: absolute; right: [20]; top: [19.6]; font: 700 [11pt]/1 'Lora', Georgia, serif; letter-spacing: -.01em; }
.wd-kopfpfeil { position: absolute; right: [20]; top: [13]; width: [7]; }
.wd-kopfpfeil svg, .wd-titelpfeil svg { width: 100%; height: auto; display: block; }
/* DIN 5008 */
.wd-falz, .wd-loch { position: absolute; left: [4]; width: [5]; height: 0; border-top: [0.25] solid #b9b3ab; }
.wd-loch { top: [148.5]; width: [7]; }
.wd-anschrift { position: absolute; left: [25]; top: [45]; width: [80]; height: [45]; }
.wd-ruecksende { position: absolute; top: [10.5]; left: 0; font: 400 [6.5pt]/1 'Poppins', sans-serif; color: #6f6a64; white-space: nowrap; }
.wd-ruecksende::after { content: ""; display: block; margin-top: [1.4]; width: [12]; height: [0.4]; background: #fff400; }
.wd-adresse { position: absolute; top: [17.7]; left: 0; }
.wd-adresse p { line-height: 1.45; }
.wd-info { position: absolute; left: [125]; top: [50]; width: [65]; font-size: [8pt]; line-height: 1.55; }
.wd-info p { display: grid; grid-template-columns: [26] 1fr; }
.wd-info span { color: #6f6a64; }
.wd-brieftext { position: absolute; left: [25]; right: [20]; top: [103.5]; }
.wd-brieftext p { margin-bottom: [4.2]; }
.wd-brieftext--folge { top: [32]; }
.wd-betreff { font: 600 [10pt]/1.4 'Poppins', sans-serif; margin-bottom: [8.5] !important; }
.wd-unterschrift { margin-top: [14] !important; font-weight: 600; }
.wd-unterschrift span { font-weight: 400; color: #6f6a64; }
.wd-seite { position: absolute; right: [20]; bottom: [12]; font-size: [7.5pt]; color: #6f6a64; }
.wd-fuss { position: absolute; left: [25]; right: [20]; bottom: [10]; font: 400 [6.5pt]/1.55 'Poppins', sans-serif; color: #3d3a37; }
.wd-fuss--a { display: grid; grid-template-columns: 1fr 1.15fr 1.35fr 1.1fr; gap: [4]; padding-top: [3.2]; border-top: [0.25] solid #1a1817; }
.wd-fuss--a div:first-child p:first-child { font-weight: 600; color: #1a1817; }
.wd-fuss--b { left: 0; right: 0; bottom: 0; padding: [5.5] [20] [7] [25]; background: #f3f1ee; }
.wd-fuss--b b { font-weight: 600; color: #1a1817; }
.wd--b .wd-anschrift .wd-ruecksende::after { background: #1a1817; }
/* DIN-Raster (Ansicht) */
.wd-din { display: none; position: absolute; inset: 0; pointer-events: none; z-index: 3; }
.wd-din-box { position: absolute; border: 1px dashed #0B9FBD; background: rgba(11,159,189,.05); }
.wd-din-box i { position: absolute; right: [1]; bottom: [0.8]; font: 500 [5.5pt]/1 'Poppins', sans-serif; font-style: normal; color: #0B9FBD; }
.wd-din-text i { bottom: auto; top: [1]; }
/* Dokument: Titelseite */
.wd-titel { position: absolute; left: [25]; right: [25]; top: [92]; }
.wd-kicker { display: flex; align-items: center; gap: [3]; margin-bottom: [7] !important; font: 700 [8pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.wd-kicker::before { content: ""; width: [8]; height: [0.6]; background: currentColor; }
.wd-h-titel { font: 700 [40pt]/1.15 'Lora', Georgia, serif; letter-spacing: -.02em; color: inherit; }
.wd-untertitel { margin-top: [7] !important; font: 300 [13pt]/1.45 'Poppins', sans-serif; max-width: [120]; }
.wd-titelpfeil { position: absolute; right: [25]; bottom: [46]; width: [40]; }
.wd-meta { position: absolute; left: [25]; right: [25]; bottom: [24]; border-top: [0.3] solid currentColor; padding-top: [4]; font-size: [8.5pt]; line-height: 1.7; }
.wd-meta p { display: grid; grid-template-columns: [20] 1fr; }
.wd-meta span { font: 700 [7pt]/2 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; opacity: .6; }
.wd--titel-b .wd-kicker { color: #fff400; }
.wd-titel--b { top: auto; bottom: [24]; }
.wd-meta--b { position: static; margin-top: [22]; }
.wd-titelpfeil--b { right: [-48]; top: [34]; bottom: auto; width: [150]; }
/* Dokument: Inhaltsseite */
.wd-kopftitel { position: absolute; right: [20]; top: [13.6]; font: 700 [6.5pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #6f6a64; }
.wd-doc { position: absolute; left: [25]; right: [20]; top: [34]; }
.wd-zeile { position: relative; }
.wd-doc p { margin-bottom: [3.2]; }
.wd-h1 { display: flex; align-items: baseline; gap: [4]; margin: 0 0 [4] !important; font: 700 [20pt]/1.2 'Lora', Georgia, serif; letter-spacing: -.02em; }
.wd-nr { display: inline-block; min-width: [5]; font: 700 [20pt]/1 'Lora', serif; }
.wd--ia .wd-nr { background: #fff400; padding: [0.6] [1.6] [1]; border-radius: [0.8]; }
.wd--ib .wd-nr { color: #1a1817; }
.wd-h2 { margin: [5] 0 [2.5] !important; font: 700 [14pt]/1.25 'Lora', Georgia, serif; }
.wd-h3 { margin: [4.5] 0 [2.5] !important; font: 600 [9pt]/1.2 'Poppins', sans-serif; letter-spacing: .12em; text-transform: uppercase; }
.wd-liste { list-style: none; padding: 0; margin: 0 0 [3] !important; }
.wd-liste li { position: relative; padding-left: [6]; }
.wd-liste li::before { content: ""; position: absolute; left: [0.6]; top: .62em; width: [1.8]; height: [1.8]; background: #fff400; box-shadow: 0 0 0 [0.2] #1a1817 inset; }
.wd--ib .wd-liste li::before { width: [3]; height: [0.5]; top: .75em; background: #1a1817; box-shadow: none; left: 0; }
.wd-tab { width: 100%; border-collapse: collapse; font-size: [8.5pt]; line-height: 1.4; margin-top: [1]; }
.wd-tab th { text-align: left; padding: [2] [2.5]; font: 600 [7.5pt]/1.3 'Poppins', sans-serif; letter-spacing: .06em; text-transform: uppercase; background: #1a1817; color: #fff; }
.wd--ib .wd-tab th { background: #fff400; color: #1a1817; }
.wd-tab td { padding: [2.2] [2.5]; border-bottom: [0.2] solid #d9d5ce; vertical-align: top; }
.wd-tab td b { font-weight: 600; }
.wd-beschr { margin-top: [1.6] !important; font-size: [7.5pt]; color: #6f6a64; }
.wd-zitat { margin: [5] 0 [5] !important; padding: [1] 0 [1] [6]; border-left: [1.05] solid #fff400; }
.wd--ib .wd-zitat { border-left-color: #1a1817; }
.wd-zitat p { margin: 0 !important; font: 700 [13pt]/1.35 'Lora', Georgia, serif; }
.wd-zitat cite { display: block; margin-top: [2]; font: 400 [7.5pt]/1 'Poppins', sans-serif; font-style: normal; color: #6f6a64; }
.wd-dfuss { position: absolute; left: [25]; right: [20]; bottom: [12]; display: flex; justify-content: space-between; padding-top: [2.5];
  border-top: [0.25] solid #d9d5ce; font-size: [7pt]; color: #6f6a64; }
.wd .ga-ph { outline-offset: 0; }
.wd-fv { display: none; position: absolute; right: calc(100% + [3]); top: [0.6]; white-space: nowrap; font: 500 [5.5pt]/1 'Poppins', sans-serif;
  color: #fff; background: #0B9FBD; padding: [0.8] [1.2]; border-radius: [0.6]; }
/* Schalter */
.wd-schalter { position: absolute; opacity: 0; pointer-events: none; }
.wd-schalter-label { display: inline-flex; align-items: center; gap: .6rem; margin-top: 1.2rem; font: 500 .85rem/1 'Poppins', sans-serif; color: #3d3a37; cursor: pointer; user-select: none; }
.wd-schalter-label span { position: relative; width: 2.3rem; height: 1.3rem; border-radius: 999px; background: #d9d5ce; transition: background .2s; }
.wd-schalter-label span::after { content: ""; position: absolute; left: .15rem; top: .15rem; width: 1rem; height: 1rem; border-radius: 50%; background: #fff; transition: transform .2s; }
.wd-schalter:checked + .wd-schalter-label span { background: #1a1817; }
.wd-schalter:checked + .wd-schalter-label span::after { transform: translateX(1rem); }
.wd-schalter:focus-visible + .wd-schalter-label span { outline: 2px solid #0B9FBD; outline-offset: 2px; }
.wd-schalter:checked ~ .ga-raster .wd-din { display: block; }
.wd-schalter:checked ~ .ga-raster .wd-fv { display: block; }
/* Formatvorlagen-Tabelle */
.wd-fvtab { margin-top: 1.6rem; overflow-x: auto; }
.wd-fvtab table { width: 100%; min-width: 40rem; border-collapse: collapse; font-size: .92rem; line-height: 1.45; }
.wd-fvtab th { text-align: left; padding: .7rem .8rem; font: 700 .72rem/1.2 'Poppins', sans-serif; letter-spacing: .12em; text-transform: uppercase; border-bottom: 2px solid #1a1817; }
.wd-fvtab td { padding: .7rem .8rem; border-bottom: 1px solid #e4e0db; vertical-align: top; }
.wd-fvtab td b { font-weight: 600; }
""", B)


def bauen():
    seite_schreiben(DATEI, "Word-Vorlagen",
                    'Word-<span class="hl">Vorlagen</span>',
                    "Briefbogen nach DIN 5008 und eine Dokumentvorlage für Konzepte, Angebote und Berichte – jeweils in zwei Varianten. "
                    "Die Seiten sind maßstäbliche Attrappen; daraus entstehen im nächsten Schritt die echten Word-Vorlagen (.dotx) mit Formatvorlagen.",
                    ["Entwurf 1", "A4", "Briefbogen DIN 5008", "Dokumentvorlage", "je 2 Varianten"], inhalt(), CSS)


if __name__ == "__main__":
    bauen()
