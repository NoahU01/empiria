#!/usr/bin/env python3
"""Baut zwei PDFs der Workshop-Agenda - zum Moderieren und zum Mitnehmen.

    moderation  4 Seiten, 11 pt, Notizspalte rechts. Zum Ausdrucken und
                Danebenlegen. Kein Block bricht ueber eine Seitengrenze.
    kompakt     2 Seiten, eng gesetzt, ohne Notizspalte. Fuer die Tasche.

Die Seiten sind feste Kaesten von 210x297 mm, keine Fliesspaginierung.
Nur so laesst sich "Seite X von Y" verlaesslich setzen - Chrome kennt die
CSS-Zaehler fuer Druckseiten nicht.

Aufruf:  python3 werkzeuge/pdf-agenda/agenda_pdf.py [zielordner]
"""
import os, pathlib, subprocess, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from agenda_lesen import bloecke, kopf, BEGINN

HERE = pathlib.Path(__file__).resolve().parent
ROOT = HERE.parent.parent
BUILD = HERE / "_build"
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

TITEL = "Workshop Vision &amp; Strategie"
DATUM = "06. Oktober 2026"

# Welche Bloecke auf welche Seite. Geprueft wird das ueber die Messung in
# messen.py - bleibt unten Platz, passt mehr drauf.
VERTEILUNG = {"moderation": [[1, 2], [3], [4], [5]],
              "kompakt": [[1, 2], [3, 4, 5]]}

CSS = r"""
@page { size: A4; margin: 0; }
* { box-sizing: border-box; margin: 0; padding: 0; }
:root { --ink:#1a1817; --g70:#58564f; --g50:#8a8783; --g25:#d8d4cf;
        --bg:#f4f3f1; --hl:#fff400; --warn:#b3262c;
        --serif:"Lora",Georgia,serif; --sans:"Poppins",sans-serif; }
body { font-family: var(--sans); font-weight: 300; color: var(--ink);
       -webkit-print-color-adjust: exact; print-color-adjust: exact; }
b, strong { font-weight: 600; }

.page { width: 210mm; height: 297mm; position: relative; overflow: hidden;
        page-break-after: always; padding: 16mm 15mm 16mm 18mm; }
.page:last-child { page-break-after: auto; }

/* Kopf- und Fusszeile tragen die Orientierung: Wer die Blaetter nach dem
   Termin wieder einsammelt, findet die Reihenfolge ohne Lesen. */
.kopf { display: flex; justify-content: space-between; align-items: baseline;
        padding-bottom: 3mm; border-bottom: .4pt solid var(--ink);
        margin-bottom: 7mm; }
.kopf .wo { font-size: 8pt; font-weight: 500; letter-spacing: .06em;
            text-transform: uppercase; }
.kopf .wann { font-size: 8pt; color: var(--g50); }
.fuss { position: absolute; left: 18mm; right: 15mm; bottom: 10mm;
        display: flex; justify-content: space-between; align-items: baseline;
        padding-top: 2.5mm; border-top: .4pt solid var(--g25);
        font-size: 7.6pt; color: var(--g50); }

h1 { font-family: var(--serif); font-weight: 600; font-size: 27pt;
     line-height: 1.14; letter-spacing: -.01em; }
h1 .hl { background: var(--hl); padding: 0 1.5mm; }
.unterzeile { margin-top: 4mm; font-size: 10pt; color: var(--g70); }
.unterzeile b { font-weight: 600; color: var(--ink); }

.tag { font-size: 7.4pt; font-weight: 600; letter-spacing: .13em;
       text-transform: uppercase; color: var(--g50); margin-bottom: 2.5mm; }
h2 { font-family: var(--serif); font-weight: 600; font-size: 14pt;
     line-height: 1.25; margin-bottom: 4mm; }

/* ---- Seite 1: Ziel des Termins ---------------------------------------- */
.ziele { display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm;
         margin-bottom: 6mm; }
.ziel { border-top: 1.2pt solid var(--ink); padding-top: 2.5mm; }
.ziel .nr { font-family: var(--serif); font-weight: 700; font-size: 9pt;
            color: var(--g50); }
.ziel b { display: block; font-size: 9.6pt; line-height: 1.3; margin: 1mm 0 1.5mm; }
.ziel p { font-size: 8.4pt; line-height: 1.55; color: var(--g70); }

.zitat { background: var(--bg); padding: 5mm 6mm; margin-bottom: 5mm; }
.zitat p { font-family: var(--serif); font-weight: 500; font-size: 11pt;
           line-height: 1.5; }
.zitat span { display: block; margin-top: 2.5mm; font-size: 7.4pt;
              font-weight: 600; letter-spacing: .12em; text-transform: uppercase;
              color: var(--g50); }
.nichtziel { border-left: 1.5pt solid var(--g25); padding-left: 4mm;
             margin-bottom: 7mm; }
.nichtziel span { display: block; font-size: 7.4pt; font-weight: 600;
                  letter-spacing: .12em; text-transform: uppercase;
                  color: var(--g50); margin-bottom: 1.5mm; }
.nichtziel p { font-size: 8.8pt; line-height: 1.6; color: var(--g70); }

/* ---- Ablauf auf einen Blick ------------------------------------------- */
.uebersicht { border-top: .4pt solid var(--g25); }
.uz { display: grid; grid-template-columns: 20mm 7mm 1fr 16mm;
      gap: 3mm; align-items: baseline;
      padding: 2.6mm 0; border-bottom: .4pt solid var(--g25); }
.uz .zeit { font-size: 9pt; font-weight: 500; }
.uz .nr { font-family: var(--serif); font-weight: 700; font-size: 9pt;
          color: var(--g50); }
.uz .was { font-size: 9.6pt; }
.uz .dau { font-size: 8.4pt; color: var(--g50); text-align: right; }
/* Zwei der fuenf Bloecke sind der Kern des Termins. Zwei vollflaechig
   gelbe Zeilen verschmelzen zu einem Klotz - ein Balken links markiert
   dasselbe, ohne die Uebersicht zu ueberstrahlen. */
.uz--kern { position: relative; }
.uz--kern::before { content: ""; position: absolute; left: -3.5mm; top: 1.4mm;
                    bottom: 1.4mm; width: 1.6mm; background: var(--hl); }
.uz--kern .was { font-weight: 500; }
.summe { display: flex; justify-content: space-between; margin-top: 3mm;
         font-size: 8.6pt; color: var(--g50); }

/* ---- Die Bloecke ------------------------------------------------------ */
.block { display: grid; grid-template-columns: 19mm 1fr; gap: 4.5mm;
         padding-bottom: 4.5mm; margin-bottom: 4.5mm;
         border-bottom: .4pt solid var(--g25); }
.block:last-of-type { border-bottom: 0; }
/* Die Minuten stehen gross, die Uhrzeit klein darunter: Beim Moderieren
   zaehlt zuerst, wie lang der Block ist - dann, ob man in der Zeit liegt. */
.zeitspur .min { font-family: var(--serif); font-weight: 700; font-size: 20pt;
                 line-height: 1; }
.zeitspur .min small { font-family: var(--sans); font-weight: 500;
                       font-size: 8pt; display: block; margin-top: .6mm;
                       letter-spacing: .04em; }
.zeitspur .uhr { margin-top: 2mm; padding-top: 1.6mm;
                 border-top: .4pt solid var(--g25);
                 font-size: 8pt; color: var(--g50); line-height: 1.35; }
.bkopf { display: flex; align-items: baseline; gap: 3mm; margin-bottom: 3mm; }
.bkopf .nr { font-family: var(--serif); font-weight: 700; font-size: 10pt;
             color: var(--g50); }
.bkopf h3 { font-family: var(--serif); font-weight: 600; font-size: 13pt;
            line-height: 1.22; }
.block--kern .bkopf h3 { background: var(--hl); padding: 0 1.5mm; }

.feld { margin-bottom: 2.8mm; }
.feld:last-child { margin-bottom: 0; }
.feld > dt { font-size: 7.4pt; font-weight: 600; letter-spacing: .12em;
             text-transform: uppercase; color: var(--g50); margin-bottom: 1.2mm; }
.feld p, .feld li { font-size: 9.4pt; line-height: 1.58; color: var(--g70); }
.feld ul { list-style: none; }
.feld li { position: relative; padding-left: 4mm; margin-bottom: .9mm; }
.feld li::before { content: ""; position: absolute; left: 0; top: 1.9mm;
                   width: 1.4mm; height: 1.4mm; background: var(--g50); }
.feld--fragen li::before { background: var(--ink); }
.feld--fragen li { font-style: italic; }
.warnung { border-left: 1.5pt solid var(--warn); padding-left: 3mm; }
.warnung p { color: var(--warn); }
.kette { list-style: none; counter-reset: k; }
.kette li { position: relative; padding-left: 7mm; margin-bottom: 1.8mm;
            counter-increment: k; }
.kette li::before { content: counter(k); position: absolute; left: 0; top: 0;
                    width: 4.6mm; height: 4.6mm; border-radius: 50%;
                    background: var(--ink); color: #fff; font-size: 7pt;
                    font-weight: 600; display: flex; align-items: center;
                    justify-content: center; }
.kette li.reserve::before { background: #fff; color: var(--g50);
                            border: .6pt solid var(--g25); }
.kette b { display: block; font-size: 9.4pt; color: var(--ink); }
.rollen { display: grid; grid-template-columns: 1fr 1fr; gap: 2.4mm 5mm; }
.rolle b { display: block; font-size: 9.2pt; }
.rolle span { display: block; font-size: 8.4pt; line-height: 1.5; color: var(--g70); }

/* ---- Notizspalte: nur in der Moderationsfassung ------------------------ */
.mit-notiz .block { grid-template-columns: 20mm 1fr 42mm; }
.notiz { border-left: .4pt dashed var(--g25); }

/* ---- Die kompakte Fassung zieht alles enger --------------------------- */
.eng { padding: 12mm 12mm 14mm; }
.eng .fuss { left: 12mm; right: 12mm; bottom: 7mm; }
.eng .block { grid-template-columns: 17mm 1fr; gap: 4mm;
              padding-bottom: 3.6mm; margin-bottom: 3.6mm; }
.eng .zeitspur .min { font-size: 15pt; }
.eng .zeitspur .min small { font-size: 6.6pt; }
.eng .zeitspur .uhr { font-size: 6.8pt; margin-top: 1.2mm; padding-top: 1mm; }
.eng .bkopf { margin-bottom: 1.8mm; }
.eng .bkopf h3 { font-size: 10.5pt; }
.eng .feld { margin-bottom: 1.8mm; }
.eng .feld > dt { font-size: 6.4pt; margin-bottom: .6mm; }
.eng .feld p, .eng .feld li { font-size: 7.6pt; line-height: 1.42; }
.eng .feld li { margin-bottom: .3mm; padding-left: 3.2mm; }
.eng .feld li::before { top: 1.4mm; width: 1.1mm; height: 1.1mm; }
.eng .kette li { padding-left: 5.4mm; margin-bottom: .9mm; }
.eng .kette li::before { width: 3.6mm; height: 3.6mm; font-size: 5.8pt; }
.eng .kette b { font-size: 7.6pt; }
.eng .rolle b { font-size: 7.6pt; }
.eng .rolle span { font-size: 7pt; line-height: 1.38; }
.eng h1 { font-size: 17pt; }
.eng .uz { padding: 1.5mm 0; }
.eng .uz .was { font-size: 8.2pt; }
.eng .uz .zeit { font-size: 7.8pt; }
"""


def feld_html(f):
    art, inhalt, lab = f["art"], f["inhalt"], f["label"]
    kl = " feld--fragen" if lab.lower().startswith("leitfrage") else ""
    if art == "text":
        k = '<div class="warnung">' if False else ""
        return f'<div class="feld{kl}"><dt>{lab}</dt><p>{inhalt}</p></div>'
    if art == "warnung":
        return (f'<div class="feld"><dt>{lab}</dt>'
                f'<div class="warnung"><p>{inhalt}</p></div></div>')
    if art == "liste":
        li = "".join(f"<li>{x}</li>" for x in inhalt)
        return f'<div class="feld{kl}"><dt>{lab}</dt><ul>{li}</ul></div>'
    if art == "kette":
        li = "".join(
            f'<li class="reserve"><b>{t}</b>{r}</li>' if res
            else f"<li><b>{t}</b>{r}</li>" for t, r, res in inhalt)
        return f'<div class="feld"><dt>{lab}</dt><ol class="kette">{li}</ol></div>'
    if art == "rollen":
        r = "".join(f'<div class="rolle"><b>{b}</b><span>{s}</span></div>'
                    for b, s in inhalt)
        return f'<div class="feld"><dt>{lab}</dt><div class="rollen">{r}</div></div>'
    return ""


def block_html(b, notiz):
    felder = "".join(feld_html(f) for f in b["felder"])
    n = '<div class="notiz"></div>' if notiz else ""
    kern = " block--kern" if b["kern"] else ""
    return f'''<div class="block{kern}">
      <div class="zeitspur">
        <span class="min">{b["min"]}<small>Min</small></span>
        <span class="uhr">{b["von"]}<br>bis {b["bis"]}</span>
      </div>
      <div class="inhalt"><div class="bkopf"><span class="nr">{b["nr"]}</span>
        <h3>{b["titel"]}</h3></div>{felder}</div>{n}</div>'''


def uebersicht_html(bl):
    z = ['<div class="uebersicht">']
    for b in bl:
        k = " uz--kern" if b["kern"] else ""
        z.append(f'<div class="uz{k}"><span class="zeit">{b["von"]}–{b["bis"]}</span>'
                 f'<span class="nr">{b["nr"]}</span>'
                 f'<span class="was">{b["titel"]}</span>'
                 f'<span class="dau">{b["min"]} Min</span></div>')
    z.append('</div><div class="summe"><span>Fünf Blöcke</span>'
             f'<span>{sum(b["min"] for b in bl)} Minuten · '
             f'{bl[0]["von"]} bis {bl[-1]["bis"]} Uhr</span></div>')
    return "".join(z)


def fuss(nr, von):
    return (f'<div class="fuss"><span>empiria GmbH · SV Akademie</span>'
            f'<span>Seite {nr} von {von}</span></div>')


def kopfzeile(wo):
    return (f'<div class="kopf"><span class="wo">{wo}</span>'
            f'<span class="wann">{TITEL.replace("&amp;", "&")} · {DATUM}</span></div>')


def seite1(k, bl, eng):
    titelblock = f'''<h1>Workshop<br><span class="hl">Vision &amp; Strategie.</span></h1>
    <p class="unterzeile"><b>{DATUM}</b> · {bl[0]["von"]} bis {bl[-1]["bis"]} Uhr ·
      {sum(b["min"] for b in bl)} Minuten</p>'''
    ziele = "".join(f'<div class="ziel"><span class="nr">{n}</span>'
                    f"<b>{h}</b><p>{p}</p></div>" for n, h, p in k["ziele"])
    if eng:
        return (f'<div class="page eng">{titelblock}'
                f'<div style="height:6mm"></div>'
                f'<p class="tag">Ziel des Termins</p><div class="ziele">{ziele}</div>'
                f'<p class="tag">Der Ablauf</p>{uebersicht_html(bl)}')
    return (f'<div class="page"><div style="height:2mm"></div>{titelblock}'
            f'<div style="height:9mm"></div>'
            f'<p class="tag">Ziel des Termins</p>'
            f'<h2>Gemeinsam vertreten wir die Vision und verwirklichen sie.</h2>'
            f'<div class="ziele">{ziele}</div>'
            f'<div class="zitat"><p>„{k["zitat"]}“</p><span>Wunschergebnis</span></div>'
            f'<div class="nichtziel"><span>Nicht Ziel des Termins</span>'
            f'<p>{k["nicht_ziel"]}</p></div>'
            f'<p class="tag">Der Ablauf</p>{uebersicht_html(bl)}')


def bauen(fassung):
    bl, k = bloecke(), kopf()
    eng = fassung == "kompakt"
    verteilung = VERTEILUNG[fassung]
    gesamt = len(verteilung) + (0 if eng else 1)
    seiten = []

    if eng:
        # Seite 1 traegt Kopf und die ersten Bloecke zusammen
        erste = seite1(k, bl, True) + '<div style="height:5mm"></div>'
        erste += "".join(block_html(b, False) for b in bl
                         if int(b["nr"]) in verteilung[0])
        seiten.append(erste + fuss(1, gesamt) + "</div>")
        rest = verteilung[1:]
    else:
        seiten.append(seite1(k, bl, False) + fuss(1, gesamt) + "</div>")
        rest = verteilung

    for i, gruppe in enumerate(rest, start=2):
        kl = "page eng" if eng else "page mit-notiz"
        wo = f"Block {' und '.join(f'{n:02d}' for n in gruppe)}"
        inhalt = "".join(block_html(b, not eng) for b in bl
                         if int(b["nr"]) in gruppe)
        seiten.append(f'<div class="{kl}">{kopfzeile(wo)}{inhalt}'
                      f"{fuss(i, gesamt)}</div>")

    titel = f"Agenda {DATUM} – Workshop Vision und Strategie"
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8">'
            f"<title>{titel}</title>"
            f'<link rel="stylesheet" href="assets/fonts/fonts.local.css">'
            f"<style>{CSS}</style></head><body>{''.join(seiten)}</body></html>")


def main():
    os.chdir(ROOT)
    BUILD.mkdir(exist_ok=True)
    link = BUILD / "assets"
    if not link.exists():
        link.symlink_to(ROOT / "site" / "assets")
    ziel = pathlib.Path(sys.argv[1]).expanduser() if len(sys.argv) > 1 \
        else pathlib.Path.home() / "Downloads"
    ziel.mkdir(parents=True, exist_ok=True)

    for fassung, name in (("moderation", "Agenda-Vision-Strategie-Moderation"),
                          ("kompakt", "Agenda-Vision-Strategie-Kompakt")):
        src = BUILD / f"_src_{fassung}.html"
        src.write_text(bauen(fassung), encoding="utf-8")
        pdf = ziel / f"{name}.pdf"
        subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                        "--no-pdf-header-footer", f"--print-to-pdf={pdf}",
                        "--virtual-time-budget=8000", "file://" + str(src)],
                       capture_output=True, timeout=180)
        if not pdf.exists():
            raise SystemExit(f"Rendern fehlgeschlagen: {fassung}")
        print(f"{name}.pdf  ({pdf.stat().st_size // 1024} KB)  ->  {ziel}")


if __name__ == "__main__":
    main()
