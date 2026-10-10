"""empiria 2.0 · PDF-Bausteine im Stil der Homepage (Maßstab: Volksfest-Seite).

Regeln (wie auf den 2.0-Seiten):
  · Schwarz – Weiß – Gelb, keine Sekundärfarben. Auf Gelb nur Schwarz, auf Weiß kein Gelb als Schrift/Linie.
  · Lora für Überschriften, Poppins für Text. Kicker mit kurzem Strich davor.
  · Ruhige Flächen: weiße Seiten, gelbe Bänder, schwarze Kästen. Gleiche Dinge stehen auf gleicher Höhe.
  · Mono-Kopfbilder und Lucide-Icons statt Skizzen.
Eine Seite ist 210 × 297 mm; jede Seite ist ein eigenes <section class="seite">.
"""
import html as _h
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "werkzeuge"))
from e2_lucide import ICONS  # noqa: E402

GELB, SCHWARZ, HELL = "#fff400", "#1a1817", "#f3f1ee"

CSS = r"""
@page { size: 210mm 297mm; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
html, body { background: #fff; }
body { font-family: 'Poppins', Arial, sans-serif; color: #1a1817; -webkit-print-color-adjust: exact; print-color-adjust: exact; font-size: 9.6pt; line-height: 1.55; }
.seite { position: relative; width: 210mm; height: 297mm; overflow: hidden; page-break-after: always; break-after: page; display: flex; flex-direction: column; }
.seite:last-child { page-break-after: auto; break-after: auto; }
.rand { padding: 0 18mm; }
.kopf { display: flex; justify-content: space-between; align-items: center; padding: 14mm 18mm 0; }
.kopf img { height: 5.2mm; }
.kopf span { font-size: 7.4pt; font-weight: 600; letter-spacing: .14em; text-transform: uppercase; }
.fuss { position: absolute; left: 0; right: 0; bottom: 0; display: flex; justify-content: space-between; align-items: center; padding: 0 18mm 11mm; font-size: 7.4pt; }
.fuss .strich { width: 9mm; height: 1.5px; background: #1a1817; }
.fuss--hell { color: #fff; } .fuss--hell .strich { background: #fff400; }

.kicker { display: flex; align-items: center; gap: 2.6mm; font-size: 7.6pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.kicker::before { content: ""; width: 6mm; height: 1.6px; background: currentColor; }
h1 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 38pt; line-height: 1.08; letter-spacing: -.02em; margin-top: 5mm; }
h2 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 24pt; line-height: 1.12; letter-spacing: -.015em; margin-top: 3.5mm; }
h3 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.2; }
.lead { font-size: 10.6pt; line-height: 1.6; margin-top: 4mm; max-width: 125mm; }
.hl { background: #fff400; padding: 0 .12em; border-radius: .12em; box-decoration-break: clone; -webkit-box-decoration-break: clone; white-space: nowrap; }
.dunkel .hl { color: #1a1817; }

/* Bänder über die ganze Breite */
.band { padding: 15mm 18mm 16mm; }
.band--gelb { background: #fff400; }
.band--hell { background: #f3f1ee; }
.band--schwarz { background: #1a1817; color: #fff; }
.band--schwarz .kicker { color: #fff400; }
.wachsen { flex: 1; padding-bottom: 24mm; display: flex; flex-direction: column; }
.mitte { justify-content: center; }
.seite--hell { background: #f3f1ee; }
.seite--gelb { background: #fff400; }
.posts--hoch .post__bild { min-height: 62mm; }
.posts--hoch { margin-top: 12mm; }
.post__unten b { font-size: 13.5pt; white-space: nowrap; }
.check { display: grid; grid-template-columns: 1fr 1fr; gap: 3mm 9mm; margin-top: 6mm; list-style: none; }
.check li { position: relative; padding: 2.4mm 0 2.4mm 7mm; border-bottom: 1px solid #dcd8d1; font-size: 9.4pt; }
.check li::before { content: ""; position: absolute; left: 0; top: 4.2mm; width: 3mm; height: 1.6mm; border-left: 1.6px solid #1a1817; border-bottom: 1.6px solid #1a1817; transform: rotate(-45deg); }
.kasten .punkte > div { border-color: rgba(255,255,255,.3); }
.kasten .punkte svg { color: #fff400; }
.kasten .punkte h3 { color: #fff; font-size: 11pt; }
.kasten .punkte p { color: rgba(255,255,255,.78); }

/* Titelseite */
.titel { padding: 14mm 18mm 0; display: flex; flex-direction: column; flex: 1; }
.titel .logo { height: 5.6mm; align-self: flex-start; }
.titel .kicker { margin-top: 30mm; }
.titel .sub { font-size: 11pt; line-height: 1.6; margin-top: 6mm; max-width: 130mm; color: #3d3a37; }
.titel .bild { flex: 1; display: flex; align-items: center; justify-content: center; padding: 8mm 0; }
.titel .bild svg { width: 120mm; height: auto; }
.fakten { display: grid; gap: 6mm; margin: 0 18mm; padding: 5mm 0 0; border-top: 1.6px solid #1a1817; }
.fakten span { display: block; font-size: 7pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.fakten b { display: block; margin-top: 1.4mm; font-family: 'Lora', Georgia, serif; font-size: 11.5pt; line-height: 1.25; }

/* Punkte mit Linie (Ansatz-Streifen) */
.punkte { display: grid; gap: 8mm; margin-top: 9mm; }
.punkte > div { border-top: 1.6px solid #1a1817; padding-top: 4.5mm; }
.punkte svg { width: 7mm; height: 7mm; margin-bottom: 3mm; }
.punkte p { margin-top: 1.8mm; font-size: 9pt; line-height: 1.55; }
.dunkel .punkte > div { border-color: rgba(255,255,255,.35); }

/* Werkzeuge / Logos */
.logos { display: grid; gap: 4mm; margin-top: 7mm; text-align: center; }
.logos img { height: 10mm; width: auto; filter: brightness(0); }
.logos b { display: block; margin-top: 2.5mm; font-size: 8pt; font-weight: 600; }

/* Post-Karten (Formate / Preise) – weiß · Farbfläche · weiß */
.posts { display: grid; grid-template-columns: repeat(3, 1fr); grid-template-rows: auto auto auto; column-gap: 5mm; margin-top: 9mm; }
.post { display: grid; grid-row: span 3; grid-template-rows: subgrid; border: 1px solid #dcd8d1; border-radius: 4.5mm; overflow: hidden; background: #fff; }
.post__kopf { display: flex; justify-content: space-between; align-items: center; gap: 2mm; padding: 3.4mm 3.4mm 3.4mm 4.2mm; min-height: 12mm; font-size: 7.8pt; font-weight: 600; }
.post__kopf em { font-style: normal; font-size: 6.2pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; background: #1a1817; color: #fff; padding: 1mm 2mm; border-radius: 9mm; white-space: nowrap; font-size: 5.6pt; flex: 0 0 auto; }
.post__bild { display: flex; flex-direction: column; justify-content: space-between; min-height: 40mm; padding: 4.5mm 5mm 5mm; background: #f3f1ee; }
.post--top .post__bild { background: #fff400; }
.post__bild small { font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.post__unten { display: flex; justify-content: space-between; align-items: flex-end; gap: 3mm; }
.post__unten b { display: block; font-family: 'Lora', Georgia, serif; line-height: 1.1; }
.post__unten .preis { display: block; margin-top: 2mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 14pt; }
.post__unten svg { width: 12mm; height: 12mm; flex: 0 0 auto; }
.post__text { padding: 4mm 4.2mm 5mm; font-size: 8.4pt; line-height: 1.5; color: #3d3a37; }
.post__text ul { list-style: none; margin-top: 3mm; padding-top: 3mm; border-top: 1px solid #ece9e5; }
.post__text li { position: relative; padding-left: 3.6mm; margin-top: 1.4mm; color: #1a1817; }
.post__text li::before { content: ""; position: absolute; left: 0; top: 1.9mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1a1817; }
.notiz { margin-top: 5mm; font-size: 7.6pt; color: #8a847c; }

/* Fall-Karten (Beispiele) */
.faelle { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4.5mm; margin-top: 9mm; }
.fall { background: #fff; border-radius: 4.5mm; padding: 5mm 5mm 5.5mm; }
.fall .sym { display: grid; place-items: center; width: 10mm; height: 10mm; border-radius: 2.6mm; background: #fff400; margin-bottom: 4mm; }
.fall .sym svg { width: 5.4mm; height: 5.4mm; }
.fall p { margin-top: 2mm; font-size: 8.6pt; line-height: 1.5; color: #3d3a37; }

/* schwarzer Kasten / Band mit Label */
.kasten { background: #1a1817; color: #fff; border-radius: 4.5mm; padding: 6mm 7mm; }
.kasten .punkte svg { width: 5.5mm; height: 5.5mm; margin-bottom: 2mm; }
.kasten .punkte p { font-size: 8.4pt; }
.kasten .label { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #fff400; }
.kasten h3 { color: #fff; font-size: 15pt; margin-top: 2mm; }
.kasten p { margin-top: 2.5mm; font-size: 9pt; line-height: 1.6; color: rgba(255,255,255,.82); }
.zwei { display: grid; grid-template-columns: 1fr 1fr; gap: 9mm; align-items: center; }

/* Zeitstrahl */
.zs { list-style: none; display: grid; position: relative; margin-top: 10mm; }
.zs::before { content: ""; position: absolute; left: 0; right: 0; top: 1.8mm; height: 1.6px; background: #1a1817; }
.zs li { position: relative; padding-right: 6mm; }
.zs .punkt { display: block; width: 3.8mm; height: 3.8mm; border-radius: 50%; background: #1a1817; box-shadow: 0 0 0 1.2mm #fff400; margin-bottom: 5mm; position: relative; }
.band--hell .zs .punkt { box-shadow: 0 0 0 1.2mm #f3f1ee; }
.seite > .zs-weiss .punkt, .weiss .zs .punkt { box-shadow: 0 0 0 1.2mm #fff; }
.zs .nr { font-size: 7pt; font-weight: 700; letter-spacing: .16em; }
.zs h3 { margin-top: 1.2mm; }
.zs p { margin-top: 1.6mm; font-size: 8.6pt; line-height: 1.5; }

.fuss__thema { display: flex; align-items: center; gap: 2.6mm; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.fuss__thema::before { content: ""; width: 6mm; height: 1.5px; background: currentColor; }

/* Variante B · Titel mit gelbem Fuß-Band */
.titel-b { display: flex; flex-direction: column; flex: 1; }
.titel-b .oben { padding: 14mm 18mm 0; }
.titel-b .oben .logo { height: 5.6mm; }
.titel-b .oben .kicker { margin-top: 26mm; }
.titel-b .oben .sub { font-size: 11pt; line-height: 1.6; margin-top: 6mm; max-width: 130mm; color: #3d3a37; }
.titel-b .unten { margin-top: auto; background: #fff400; padding: 12mm 18mm 14mm; display: flex; flex-direction: column; gap: 10mm; }
.titel-b .unten .bild { display: flex; justify-content: center; }
.titel-b .unten .bild svg { width: 105mm; height: auto; }
.titel-b .fakten { margin: 0; }

/* Variante B · Vergleichstabelle */
.tabelle { width: 100%; border-collapse: separate; border-spacing: 0; margin-top: 9mm; font-size: 8.6pt; }
.tabelle th, .tabelle td { padding: 3.4mm 4mm; text-align: left; vertical-align: top; border-bottom: 1px solid #e4e0db; }
.tabelle thead th { border-bottom: 0; padding-top: 5mm; padding-bottom: 5mm; vertical-align: bottom; }
.tabelle thead th b { display: block; font-family: 'Lora', Georgia, serif; font-size: 14pt; }
.tabelle thead th small { font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.tabelle thead th em { display: inline-block; margin-bottom: 2mm; font-style: normal; font-size: 5.6pt; font-weight: 700; letter-spacing: .12em; text-transform: uppercase; background: #1a1817; color: #fff; padding: 1mm 2mm; border-radius: 9mm; }
.tabelle .zeile { width: 26mm; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; }
.tabelle .mitte { background: #fff400; }
.tabelle thead .mitte { border-radius: 4mm 4mm 0 0; }
.tabelle tbody tr:last-child .mitte { border-radius: 0 0 4mm 4mm; border-bottom: 0; }
.tabelle .preis { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 13pt; }
.tabelle .ja { display: inline-block; width: 3mm; height: 1.6mm; border-left: 1.6px solid #1a1817; border-bottom: 1.6px solid #1a1817; transform: rotate(-45deg); margin: 0 0 .6mm 1mm; }
.tabelle .nein { color: #b9b3ab; }

/* Variante B · Beispiele als Liste */
.liste { margin-top: 8mm; border-top: 1.6px solid #1a1817; }
.liste > div { display: grid; grid-template-columns: 56mm 1fr; gap: 8mm; padding: 4.2mm 0; border-bottom: 1px solid #dcd8d1; }
.liste h3 { font-size: 11.5pt; }
.liste p { font-size: 8.8pt; line-height: 1.55; color: #3d3a37; }

/* Personen */
.seite--gelb .person span, .band--gelb .person span { color: #1a1817 !important; opacity: .75; }
.tabelle thead th b { white-space: nowrap; }
.team { display: flex; gap: 9mm; margin-top: 8mm; }
.person { text-align: center; width: 36mm; }
.person img { width: 26mm; height: 26mm; border-radius: 50%; object-fit: cover; background: #f3f1ee; filter: grayscale(1); }
.person b { display: block; margin-top: 2.5mm; font-family: 'Lora', Georgia, serif; font-size: 10.5pt; }
.person span { display: block; font-size: 7.6pt; color: #8a847c; line-height: 1.4; margin-top: .6mm; }
.kontaktdaten { display: grid; gap: 2.4mm; margin-top: 5mm; }
.kontaktdaten a, .kontaktdaten div { display: flex; align-items: center; gap: 3mm; padding: 3.4mm 5mm; border-radius: 9mm; background: #1a1817; color: #fff; text-decoration: none; font-weight: 600; font-size: 9pt; }
.kontaktdaten svg { width: 4.4mm; height: 4.4mm; }
"""

PERSONEN = {
    "daniel": ("assets/ansprechpartner-daniel.webp", "Daniel Ströbel", "Strategiehandwerker"),
    "noah_ki": ("assets/ansprechpartner-noah.webp", "Noah Hermanns", "KI Native"),
    "noah_pm": ("assets/ansprechpartner-noah.webp", "Noah Hermanns", "Experte Performance Marketing"),
    "kerstin_hr": ("assets/ansprechpartner-kerstin.webp", "Kerstin Christ", "Expertin HR &amp; Weiterbildung"),
    "kerstin_content": ("assets/ansprechpartner-kerstin.webp", "Kerstin Christ", "Expertin Content &amp; Sichtbarkeit"),
}


def ico(name, farbe="currentColor", strich=1.5):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="{strich}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[name]}</svg>')


# Variante „Kopf/Fuß B“ (Punkt 7): oben nur das Logo, unten Thema + Seitenzahl
KOPF_FUSS_B = True   # Daniel 10.10.: oben nur Logo, unten Thema + Seitenzahl
_THEMA = ""


def kopf(rechts=""):
    global _THEMA
    _THEMA = rechts or _THEMA
    if KOPF_FUSS_B:
        rechts = ""
    return f'<div class="kopf"><img src="assets/empiria-logo.svg" alt="empiria"><span>{rechts}</span></div>'


def fuss(nr, gesamt, hell=False):
    links = f'<span class="fuss__thema">{_THEMA}</span>' if KOPF_FUSS_B else '<span class="strich"></span>'
    return f'<div class="fuss{" fuss--hell" if hell else ""}">{links}<span>{nr:02d} / {gesamt:02d}</span></div>'


def kicker(t):
    return f'<p class="kicker">{t}</p>'


def kopfbild(titel):
    """Das Mono-Kopfbild der Homepage (e2_kopfbilder), in Schwarz-Gelb."""
    import e2_kopfbilder as kb
    from e2_header import farbig
    seite = next(x for x in kb.SEITEN if x[0] == titel)
    svg = farbig(kb.bild(seite)[0], "gelb", "pdf")
    return svg.replace('viewBox="0 0 440 400"', f'viewBox="{kb.eng(seite)}"', 1)


def titelseite(kick, h1, sub, bild, fakten):
    f = "".join(f'<div><span>{l}</span><b>{v}</b></div>' for l, v in fakten)
    return (f'<div class="titel"><img class="logo" src="assets/empiria-logo.svg" alt="empiria">{kicker(kick)}<h1>{h1}</h1>'
            f'<p class="sub">{sub}</p><div class="bild">{bild}</div></div>'
            f'<div class="fakten" style="grid-template-columns:repeat({len(fakten)},1fr)">{f}</div><div style="height:16mm"></div>')


def punkte(items, spalten=3):
    return f'<div class="punkte" style="grid-template-columns:repeat({spalten},1fr)">' + "".join(
        f'<div>{ico(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p in items) + '</div>'


def posts(items):
    out = ""
    for it in items:
        top = it.get("top")
        out += (f'<article class="post{" post--top" if top else ""}"><div class="post__kopf"><span>{it["kopf"]}</span>'
                f'{"<em>" + it["badge"] + "</em>" if it.get("badge") else ""}</div>'
                f'<div class="post__bild"><small>{it["label"]}</small><div class="post__unten"><div><b>{it["name"]}</b>'
                f'<span class="preis">{it["preis"]}</span></div>{ico(it["ico"], strich=1.3)}</div></div>'
                f'<div class="post__text">{it["text"]}<ul>{"".join(f"<li>{x}</li>" for x in it["liste"])}</ul></div></article>')
    return f'<div class="posts">{out}</div>'


def faelle(items):
    return '<div class="faelle">' + "".join(
        f'<div class="fall"><span class="sym">{ico(i, strich=1.7)}</span><h3>{t}</h3><p>{p}</p></div>' for i, t, p in items) + '</div>'


def zeitstrahl(items):
    return f'<ol class="zs" style="grid-template-columns:repeat({len(items)},1fr)">' + "".join(
        f'<li><span class="punkt"></span><span class="nr">{n}</span><h3>{t}</h3><p>{p}</p></li>' for n, t, p in items) + '</ol>'


def team(keys):
    return '<div class="team">' + "".join(
        f'<div class="person"><img src="{PERSONEN[k][0]}" alt=""><b>{PERSONEN[k][1]}</b><span>{PERSONEN[k][2]}</span></div>' for k in keys) + '</div>'


def kontaktdaten():
    return ('<div class="kontaktdaten">'
            f'<div>{ico("mail")}daniel.stroebel@empiria.de</div>'
            f'<div>{ico("phone")}+49 176 3134 7217</div>'
            f'<div>{ico("app-window")}www.empiria.de</div></div>')


def check(items):
    return '<ul class="check">' + "".join(f"<li>{x}</li>" for x in items) + '</ul>'


def seite(inhalt, nr=None, gesamt=None, hell_fuss=False, klasse=""):
    f = fuss(nr, gesamt, hell_fuss) if nr else ""
    return f'<section class="seite {klasse}">{inhalt}{f}</section>'


# Daniel 10.10.: Der gelbe Highlight-Kasten darf die Buchstaben der Zeile darüber nie verdecken.
# Deshalb haben Überschriften mit Highlight mehr Zeilenabstand – gilt für alle PDFs und schlägt eigenes extra_css.
HL_SCHUTZ = """
:is(h1, h2, h3, p, b):has(> .hl), :is(h1, h2, h3, p, b):has(.hl) { line-height: 1.32 !important; }
.hl { padding-top: 0 !important; padding-bottom: 0 !important; line-height: inherit; }
"""


def dokument(titel, seiten, extra_css=""):
    """extra_css: zusätzliche Regeln nur für dieses PDF (lib.py bleibt für alle gleich)."""
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{_h.escape(titel)}</title>'
            f'<link rel="stylesheet" href="assets/fonts/fonts.local.css"><style>{CSS}{extra_css}{HL_SCHUTZ}</style></head><body>{"".join(seiten)}</body></html>')
