#!/usr/bin/env python3
"""Zusaetzliche Bausteine fuer die ueberarbeiteten empiria-PDFs.

Ergaenzt pdf_vorlage.CSS um Komponenten, die dem Homepage-Design naeher kommen:
mehr Weissraum, Sektionsrhythmus (weiss/grau/schwarz), klare Preisdarstellung
und eine Uebersichtstabelle, die Entscheidern sofort Orientierung gibt.
"""

CSS_EXTRA = """
/* ---------- Sektionsrhythmus wie auf der Homepage ---------- */
.page--grey { background: #f4f2f0; }
.band { background: var(--ink); color: #fff; border-radius: 5mm; padding: 9mm 9mm; margin: 9mm 0; }
.band .kicker { color: #fff; opacity: .72; }
.band h2 { color: #fff; font-size: 17pt; margin-bottom: 3mm; }
.band p { font-size: 10pt; line-height: 1.7; color: #e4e2df; max-width: 140mm; }

/* ---------- Format-Kopf einer Produktseite ---------- */
.fmt-head { display: flex; align-items: baseline; gap: 5mm; margin-bottom: 2mm; }
.fmt-no { font-family: var(--serif); font-weight: 700; font-size: 11pt; color: var(--acc); }
.fmt-meta { margin-left: auto; font-size: 8.5pt; color: var(--g50); font-weight: 500; }
.fmt h2 { font-size: 23pt; line-height: 1.12; margin-bottom: 4mm; max-width: 150mm; }
.fmt .lead { font-size: 10.5pt; line-height: 1.75; color: var(--ink2); max-width: 152mm; }

/* ---------- "Fuer wen" ---------- */
.who { margin-top: 6mm; }
.who-title { font-family: var(--serif); font-weight: 700; font-size: 11.5pt; margin-bottom: 3mm; }
.who ul { list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 7mm; }
.who li { position: relative; padding-left: 5.5mm; font-size: 9.3pt; line-height: 1.55; color: var(--g70); }
.who li::before { content: ""; position: absolute; left: 0; top: 1.7mm; width: 2.2mm; height: 2.2mm;
                  border-radius: 50%; background: var(--acc); }

/* ---------- Ablauf (Schrittkette) ---------- */
.steps { display: grid; gap: 3.5mm; margin-top: 6mm; }
.step { display: grid; grid-template-columns: 9mm 1fr; column-gap: 4mm; align-items: start; }
.step .sn { font-family: var(--serif); font-weight: 700; font-size: 10.5pt; color: var(--acc);
            border: 0.8pt solid var(--acc); border-radius: 50%; width: 7.5mm; height: 7.5mm;
            display: flex; align-items: center; justify-content: center; }
.step b { display: block; font-family: var(--serif); font-size: 11pt; }
.step .sm { font-size: 8pt; color: var(--g50); font-weight: 500; margin: .6mm 0 1.2mm; }
.step p { font-size: 9.3pt; line-height: 1.6; color: var(--g70); }

/* ---------- Preise: ruhige Zeilen statt gequetschter Kaesten ---------- */
.prices { margin-top: 6mm; border-top: 0.8pt solid var(--line); }
.prc { display: grid; grid-template-columns: 1fr auto; gap: 8mm; align-items: start;
       padding: 4.5mm 0; border-bottom: 0.8pt solid var(--line); }
.prc-name { display: flex; align-items: baseline; gap: 3.5mm; margin-bottom: 1.8mm; }
.prc-name b { font-family: var(--serif); font-weight: 700; font-size: 12.5pt; }
.prc-dur { font-size: 8pt; letter-spacing: .1em; text-transform: uppercase; color: var(--acc); font-weight: 600; }
.prc p { font-size: 9.3pt; line-height: 1.6; color: var(--g70); max-width: 112mm; }
.prc ul { list-style: none; margin-top: 2mm; }
.prc li { position: relative; padding-left: 4.5mm; font-size: 8.8pt; line-height: 1.55; color: var(--g70); }
.prc li::before { content: "–"; position: absolute; left: 0; color: var(--g50); }
.prc-amount { font-family: var(--serif); font-weight: 700; font-size: 17pt; white-space: nowrap; text-align: right; }
.prc-amount small { display: block; font-family: var(--sans); font-weight: 500; font-size: 7.5pt;
                    color: var(--g50); letter-spacing: .04em; margin-top: 1mm; }

/* ---------- Uebersichtstabelle (Orientierung auf einen Blick) ---------- */
.ov { margin-top: 6mm; width: 100%; border-collapse: collapse; }
.ov th { text-align: left; font-size: 6.8pt; letter-spacing: .12em; text-transform: uppercase;
         color: var(--g50); font-weight: 600; padding: 0 5mm 2.5mm 0; border-bottom: 0.8pt solid var(--line); }
.ov td { padding: 4mm 5mm 4mm 0; border-bottom: 0.8pt solid var(--line); vertical-align: top; }
.ov td:last-child, .ov th:last-child { padding-right: 0; text-align: right; }
.ov .t-name { font-family: var(--serif); font-weight: 700; font-size: 11pt; }
.ov .t-sub { display: block; font-size: 8.5pt; color: var(--g70); line-height: 1.5; margin-top: .8mm; }
.ov .t-dur { font-size: 9pt; color: var(--g70); white-space: nowrap; }
.ov .t-price { font-family: var(--serif); font-weight: 700; font-size: 11.5pt; white-space: nowrap; }

/* ---------- Schlusszeile einer Seite ----------
   Bewusst im Fluss (nicht absolut am Seitenrand): sonst schiebt sich die Zeile
   bei laengeren Seiten unter den Inhalt. */
.pagenote { margin-top: 4mm; font-size: 7pt; color: var(--g50); line-height: 1.5; }
"""


def band(kicker, h2, text):
    """Dunkler Block als Rhythmuswechsel - Pendant zur schwarzen Sektion der Homepage."""
    return (f'<div class="band"><p class="kicker">{kicker}</p><h2>{h2}</h2>'
            f'<p>{text}</p></div>')


def who(title, items):
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="who"><p class="who-title">{title}</p><ul>{lis}</ul></div>'


def steps(items):
    """items: (titel, meta, text)"""
    out = ""
    for n, (t, meta, txt) in enumerate(items, 1):
        m = f'<span class="sm">{meta}</span>' if meta else ""
        out += (f'<div class="step"><span class="sn">{n}</span><div><b>{t}</b>{m}'
                f'<p>{txt}</p></div></div>')
    return f'<div class="steps">{out}</div>'


def price_row(name, dur, text, bullets=None, amount=None, amount_note=None):
    b = ""
    if bullets:
        b = "<ul>" + "".join(f"<li>{x}</li>" for x in bullets) + "</ul>"
    d = f'<span class="prc-dur">{dur}</span>' if dur else ""
    if amount:
        note = f"<small>{amount_note}</small>" if amount_note else ""
        right = f'<div class="prc-amount">{amount}{note}</div>'
    else:
        right = '<div class="prc-amount" style="font-size:11pt;color:var(--g70)">auf Anfrage</div>'
    return (f'<div class="prc"><div><div class="prc-name"><b>{name}</b>{d}</div>'
            f'<p>{text}</p>{b}</div>{right}</div>')


def overview(rows):
    """rows: (name, sub, dauer, preis)"""
    body = ""
    for name, sub, dur, price in rows:
        body += (f'<tr><td><span class="t-name">{name}</span>'
                 f'<span class="t-sub">{sub}</span></td>'
                 f'<td class="t-dur">{dur}</td>'
                 f'<td class="t-price">{price}</td></tr>')
    return ('<table class="ov"><thead><tr><th>Format</th><th>Dauer</th>'
            '<th>Investition</th></tr></thead><tbody>' + body + '</tbody></table>')
