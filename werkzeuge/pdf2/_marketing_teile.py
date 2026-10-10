"""Gemeinsame Bausteine für die Marketing-PDFs (Marketing 2.0, MES, sofort sichtbar, Anforderungsprofil).

Nur Zusammensetzungen aus lib.py – lib.py selbst bleibt unverändert.
"""
from lib import kicker, zeitstrahl, team, kontaktdaten, ico

# Drei Personen nebeneinander + Kontaktdaten darunter (die Marketing-Seiten nennen drei Ansprechpartner)
CSS = """
.team3 .team { gap: 10mm; margin-top: 9mm; }
.team3 .person { width: 40mm; }
.team3 .kontaktdaten { display: flex; gap: 3mm; margin-top: 10mm; }
.team3 .kontaktdaten div { flex: 1 1 auto; justify-content: center; padding: 3.4mm 4.6mm; }
.liste .unter { display: block; margin-top: 1.6mm; font-size: 7pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; }
.liste .preiszeile { margin-top: 2.4mm; font-size: 8.6pt; color: #1a1817; }
.liste .preiszeile b { font-family: 'Lora', Georgia, serif; font-size: 10.5pt; }
.tabelle--fest { table-layout: fixed; }
.tabelle--fest .zeile { padding-left: 3mm; padding-right: 2mm; }
.tabelle--fest thead th b { white-space: normal; font-size: 13pt; line-height: 1.15; margin-top: 1mm; }
.tabelle--fest th, .tabelle--fest td { padding-left: 3.6mm; padding-right: 3.6mm; }
.tabelle ul { list-style: none; }
.tabelle ul li { position: relative; padding-left: 3.4mm; margin-top: 1.2mm; }
.tabelle ul li:first-child { margin-top: 0; }
.tabelle ul li::before { content: ""; position: absolute; left: 0; top: 1.9mm; width: 1.3mm; height: 1.3mm; border-radius: 50%; background: #1a1817; }
.tabelle .klein { display: block; margin-top: 1mm; font-size: 7.4pt; color: #5c5853; }
.tabelle .mitte .klein { color: #1a1817; }
"""


def schritte(lead_h2, lead):
    """Drei Schritte (wie im Muster KI zum Anfassen) – Texte aus den alten PDFs der Marketing-Seiten."""
    return (kicker("Jetzt loslegen") + f'<h2>{lead_h2}</h2><p class="lead">{lead}</p>'
            + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                          ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                          ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")]))


def draht(extra=""):
    """Gelbes Band: drei Personen wie auf den Marketing-Seiten + Kontaktdaten."""
    k = kontaktdaten()
    if extra:   # zusätzliche Kontakt-Pille (z. B. sofortsichtbar.de) an das Ende der Liste hängen
        k = k[:-len("</div>")] + extra + "</div>"
    return ('<div class="band band--gelb wachsen mitte team3" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
            + '<h2>Aus Gespräch wird Klarheit.</h2>'
            + team(["daniel", "kerstin_content", "noah_pm"]) + k + '</div>')


def tabelle(spalten, zeilen):
    """Vergleichstabelle wie ki_varianten.formate_tabelle: spalten = [(klein, name, badge, mitte)], zeilen = [(label, [werte], cls)]."""
    head = '<th></th>' + "".join(
        f'<th class="{"mitte" if m else ""}">{"<em>" + b + "</em><br>" if b else ""}<small>{k}</small><b>{n}</b></th>' for k, n, b, m in spalten)
    body = ""
    for label, werte, cls in zeilen:
        body += f'<tr><td class="zeile">{label}</td>' + "".join(
            f'<td class="{"mitte " if spalten[i][3] else ""}{cls}">{w}</td>' for i, w in enumerate(werte)) + '</tr>'
    cols = '<colgroup><col style="width:28mm">' + '<col>' * len(spalten) + '</colgroup>'
    return f'<table class="tabelle tabelle--fest">{cols}<thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"
