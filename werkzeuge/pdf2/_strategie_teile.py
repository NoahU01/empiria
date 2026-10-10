"""Gemeinsame Bausteine für die Strategiehandwerk-PDFs (Strategie, Komplexe Themen, Innovation, Teams befähigen).

Nur Zusammensetzungen aus lib.py – lib.py selbst bleibt unverändert. Kein eigenes Typo-CSS:
Drei Personen nebeneinander nutzen dieselbe Anordnung wie die Marketing-PDFs (_marketing_teile.CSS, Klasse team3).
"""
from lib import kicker, zeitstrahl, team, kontaktdaten
from _marketing_teile import CSS as TEAM3_CSS  # noqa: F401  (team3, .liste .unter)

# Aufzählungen innerhalb einer Liste (Module, Phasen) – gleiche Punkte wie in den Post-Karten
LISTE_CSS = """
.liste ul, .zs ul { list-style: none; margin-top: 2mm; }
.zs ul li { font-size: 8.4pt !important; }
.liste ul li, .zs ul li { position: relative; padding-left: 3.6mm; margin-top: 1.2mm; font-size: 8.8pt; line-height: 1.5; color: #1a1817; }
.liste ul li::before, .zs ul li::before { content: ""; position: absolute; left: 0; top: 1.55mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1a1817; }
.liste p + p, .liste ul + p { margin-top: 2mm; }
.liste h3 .unter { font-family: 'Poppins', Arial, sans-serif; margin: 0 0 1.4mm; }
"""


def zeichen(name, breite):
    """Großes Themen-Zeichen der Homepage (e2_bauen.FORM), schwarz – Breite inline, damit kein extra_css nötig ist."""
    import e2_bauen
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return (f'<svg viewBox="{vb}" style="width:{breite}mm" aria-hidden="true" fill="#1a1817" color="#1a1817">'
            f'{e2_bauen.FORM[name]}</svg>')


def schluss(h2, lead, personen):
    """Einheitlicher Schluss: Jetzt loslegen + drei Schritte + gelbes Band mit Team und Kontaktdaten."""
    oben = ('<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen") + f'<h2>{h2}</h2><p class="lead">{lead}</p>'
            + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                          ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                          ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
            + '</div>')
    if len(personen) >= 3:
        unten = ('<div class="band band--gelb wachsen mitte team3" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
                 + '<h2>Aus Gespräch wird Klarheit.</h2>' + team(personen) + kontaktdaten() + '</div>')
    else:
        unten = ('<div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
                 + '<h2>Aus Gespräch wird Klarheit.</h2>'
                 + '<div class="zwei" style="margin-top:9mm">' + team(personen) + kontaktdaten() + '</div></div>')
    return oben + unten


def liste(zeilen):
    """zeilen = [(unter, titel, html_rechts)] – Liste wie ki_varianten.beispiele_liste, optional mit kleinem Label über dem Titel."""
    return '<div class="liste">' + "".join(
        f'<div><h3>{f"<span class=unter>{u}</span>" if u else ""}{t}</h3><div>{r}</div></div>' for u, t, r in zeilen) + '</div>'
