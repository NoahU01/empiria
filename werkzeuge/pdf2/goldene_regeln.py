"""PDF „Die 3 goldenen Regeln für erfolgreiche Gespräche mit Entscheidern“ – 1 Seite, plakativ (10.10.2026).
Inhalt 1:1 aus site/assets/downloads/rollup-golden-rules-thumb.jpg, Gestaltung im Stil der 2.0-PDFs (ohne Berg, ohne Gold)."""
from lib import (seite, kicker, dokument, ico)

TITEL = "Die 3 goldenen Regeln für erfolgreiche Gespräche mit Entscheidern – empiria"
DATEI = "EMP_01_rollup_golden_rules"

REGELN = [
    ("trophy", "Mache Deine Zielgruppe erfolgreich",
     ["Du „verkaufst“ nicht Dein Thema, sondern den Erfolg, der hieraus entstehen wird.",
      "Wenn Du kein Problem löst bzw. einen Mehrwert schaffst, ist Dein Thema aktuell nicht relevant."]),
    ("coffee", "Spare Deiner Zielgruppe Arbeit",
     ["Deine Aufgabe ist es, Struktur zu schaffen und gezielte Informationen bereitzustellen.",
      "Deine Zielgruppe hat keine Zeit, Deine Präsentation zu überarbeiten."]),
    ("signpost", "Zeige den nächsten Schritt auf",
     ["Du schaffst Vertrauen, wenn Du klar aufzeigst, „Was“ jetzt zu tun ist – nicht „Wie“.",
      "Auf dieser Basis können Entscheidungen getroffen werden."]),
]

CSS = """
.poster-kopf { padding: 14mm 18mm 0; }
.poster-kopf img { height: 5.6mm; }
.poster { padding: 0 18mm; }
.poster .kicker { margin-top: 22mm; }
.poster h1 { font-size: 36pt; line-height: 1.08; margin-top: 6mm; }
.regeln { display: grid; grid-template-columns: repeat(3, 1fr); gap: 9mm; margin-top: 18mm; }
.regel > svg { width: 11mm; height: 11mm; display: block; }
.regel h3 { font-size: 15pt; line-height: 1.2; margin-top: 5mm; padding-top: 4.5mm; border-top: 1.6px solid #1a1817; min-height: 23mm; }
.regel p { font-size: 10pt; line-height: 1.6; color: #3d3a37; margin-top: 4mm; }
.regel p + p { margin-top: 3mm; }
.frage { margin-top: auto; background: #fff400; padding: 14mm 18mm 12mm; display: flex; flex-direction: column; }
.frage h2 { font-size: 27pt; line-height: 1.14; margin-top: 4mm; max-width: 165mm; }
.frage .unten { display: flex; justify-content: space-between; align-items: center; margin-top: 11mm; padding-top: 4.5mm; border-top: 1.6px solid #1a1817; }
.frage .unten img { height: 5.6mm; }
.frage .unten span { font-size: 10pt; font-weight: 600; letter-spacing: .02em; }
"""


def bauen():
    regeln = "".join(
        f'<div class="regel">{ico(i, strich=1.4)}<h3>{t}</h3>' + "".join(f"<p>{x}</p>" for x in ps) + '</div>'
        for i, t, ps in REGELN)
    s1 = seite(
        '<div class="poster-kopf"><img src="assets/empiria-logo.svg" alt="empiria"></div>'
        + '<div class="poster">' + kicker("Gespräche mit Entscheidern")
        + '<h1>Die 3 goldenen Regeln<br>für erfolgreiche Gespräche<br><span class="hl">mit Entscheidern.</span></h1>'
        + f'<div class="regeln">{regeln}</div></div>'
        + '<div class="frage">' + kicker("Die Frage dahinter")
        + '<h2>Welche Bedeutung hat Dein Thema in der Welt Deiner Zielgruppe?</h2>'
        + '<div class="unten"><span>empiria GmbH</span><span>www.empiria.de</span></div></div>')
    return dokument(TITEL, [s1], extra_css=CSS)
