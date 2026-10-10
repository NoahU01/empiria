"""PDF „Anforderungsprofil Digitaler Marketingmanager (m/w/d)“ – Stellenbeschreibung zum Weitergeben.

Inhalt 1:1 aus dem Modal #jobProfileModal auf site/projekte/empiria-2/dashboard-digitales-marketing.html.
Sachlich, eine Seite: drei Bereiche nebeneinander mit Linie, Hinweis als schwarzer Kasten, empiria-Kopf/Fuß wie alle 2.0-PDFs.
"""
from lib import seite, kopf, kicker, dokument, ico

TITEL = "Anforderungsprofil Digitaler Marketingmanager (m/w/d) – empiria"
DATEI = "anforderungsprofil-marketingmanager"

BEREICHE = [
    ("clipboard-list", "Aufgaben", [
        "Entwicklung der digitalen Marketingstrategie mit der Geschäftsführung",
        "Steuerung von Homepage, Social-Media-Kanälen und Content-Kalender als ein System",
        "Konzeption, Text und Gestaltung von Landingpages und Postings",
        "Technische Umsetzung und Pflege von Homepage, Kanälen und Dashboard",
        "Wöchentliches Reporting inkl. Antwortvorschlägen auf Kommentare",
        "Monatlicher Austausch mit fester Agenda zu Stand und nächsten Schritten",
        "Halbjährliches Review der Marketingstrategie",
    ]),
    ("target", "Anforderungen", [
        "Klares Verständnis von Geschäftsmodell und Marketingstrategie",
        "Strategisch-konzeptionelle Stärke wie ein Stratege",
        "Controlling-Kompetenz: liest Kennzahlen und zieht die richtigen Schlüsse",
        "Gestalterisches Können auf dem Niveau eines professionellen Grafikers",
        "Vertiefte Programmierkenntnisse für die technische Umsetzung",
        "Hohe Eigenständigkeit: trifft Entscheidungen und treibt Themen voran",
        "Kommunikationsstärke für die Abstimmung auf Geschäftsführungsebene",
    ]),
    ("graduation-cap", "Ausbildung &amp; Erfahrung", [
        "Studium mit Bezug zu Marketing, Kommunikation, Wirtschaft oder Mediengestaltung – gerne mit technischem Schwerpunkt",
        "Mehrjährige, einschlägige Berufserfahrung im digitalen Marketing – keine Einstiegsposition",
        "Praxiserfahrung über mehrere Disziplinen hinweg statt Spezialisierung auf nur einen Kanal",
    ]),
]

CSS = """
.profil { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; margin-top: 8mm; }
.bereich { border-top: 1.6px solid #1a1817; padding-top: 4.5mm; }
.bereich svg { width: 7mm; height: 7mm; margin-bottom: 3mm; }
.bereich h3 { font-size: 12.5pt; }
.bereich ul { list-style: none; margin-top: 2.5mm; }
.bereich li { position: relative; padding: 1.5mm 0 1.5mm 4mm; border-bottom: 1px solid #e4e0db; font-size: 8.8pt; line-height: 1.5; }
.bereich li:last-child { border-bottom: 0; }
.bereich li::before { content: ""; position: absolute; left: 0; top: 3.6mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1a1817; }
.hinweis p:last-child { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.4; color: #fff; margin-top: 2mm; }
"""


def bauen():
    bereiche = "".join(
        f'<div class="bereich">{ico(i)}<h3>{t}</h3>'
        f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for i, t, items in BEREICHE)
    s1 = seite(
        kopf("Anforderungsprofil") + '<div class="rand" style="padding-top:16mm">' + kicker("Anforderungsprofil")
        + '<h2>Digitaler <span class="hl">Marketingmanager</span> (m/w/d)</h2>'
        + '<p class="lead" style="max-width:174mm">Als Stratege, Controller, Grafiker und Entwickler in einem entwickelst Du die digitale '
          'Marketingstrategie, steuerst Homepage und Social-Media-Kanäle in einem übergreifenden Dashboard und setzt '
          'Kampagneninhalte und technische Anpassungen selbst um.</p>'
        + f'<div class="profil">{bereiche}</div>'
        + '<div class="kasten hinweis" style="margin-top:8mm"><p class="label">Hinweis</p>'
          '<p>Bei uns bekommst Du dieses Profil als eingespieltes Team, ohne die Suche, die Einarbeitung und das Risiko einer Einzelperson.</p></div>'
        + '</div>', 1, 1)
    return dokument(TITEL, [s1], extra_css=CSS)
