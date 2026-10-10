"""PDF „Anforderungsprofil Digitaler Marketingmanager (m/w/d)“ – Stellenbeschreibung zum Weitergeben.

Inhalt 1:1 aus dem Modal #jobProfileModal auf site/projekte/empiria-2/dashboard-digitales-marketing.html.
Sachlich, eine Seite: drei Bereiche nebeneinander mit Linie, Hinweis als schwarzer Kasten, empiria-Kopf/Fuß wie alle 2.0-PDFs.
"""
import _marketing_teile as mt
from lib import seite, kopf, kicker, dokument, ico, titelseite, team, kontaktdaten

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
.posting { display: grid; grid-template-columns: 50mm 1fr; gap: 8mm; align-items: center; padding: 5mm 0; border-top: 1px solid #dcd8d1; }
.posting:first-of-type { border-top: 1.6px solid #1a1817; }
.motiv { width: 50mm; height: 50mm; overflow: hidden; border-radius: 3.5mm; padding: 4.5mm; display: flex; flex-direction: column; justify-content: space-between; }
.motiv small { font-size: 5.6pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.motiv b { font-family: 'Lora', Georgia, serif; font-size: 11.5pt; line-height: 1.15; display: block; }
.motiv span { font-size: 6.2pt; line-height: 1.4; }
.motiv img { height: 3mm; align-self: flex-start; }
.motiv--gelb { background: #fff400; color: #1a1817; }
.motiv--schwarz { background: #1a1817; color: #fff; } .motiv--schwarz img { filter: invert(1); }
.motiv--hell { background: #f3f1ee; color: #1a1817; }
.posting .label { font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.posting h3 { margin-top: 2mm; }
.posting p { margin-top: 2mm; font-size: 8.8pt; line-height: 1.6; color: #3d3a37; }
.adresse { margin-top: 6mm; font-size: 9pt; line-height: 1.6; }
.hinweis p:last-child { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.4; color: #fff; margin-top: 2mm; }
"""


def bauen():
    bereiche = "".join(
        f'<div class="bereich">{ico(i)}<h3>{t}</h3>'
        f'<ul>{"".join(f"<li>{x}</li>" for x in items)}</ul></div>' for i, t, items in BEREICHE)
    titel = seite(titelseite(
        "Anforderungsprofil &amp; Leadmagnet", 'Dein digitaler Marketingmanager.<br><span class="hl">Fertig zum Ausschreiben.</span>',
        "Dieses Dokument enthält alles, was Du brauchst, um genau diese Rolle selbst zu besetzen: das vollständige Anforderungsprofil "
        "für einen digitalen Marketingmanager – plus fertige Postingtexte und Postingbilder, mit denen Du direkt auf die Suche gehen kannst.",
        '<svg viewBox="0 0 24 24" style="width:62mm;height:62mm" fill="none" stroke="#1a1817" stroke-width="0.9" stroke-linecap="round" stroke-linejoin="round">' + __import__("lib").ICONS["clipboard-list"] + '</svg>',
        [("Teil 1", "Profil"), ("Teil 2", "Postingtexte"), ("Teil 3", "Postingbilder"), ("Alternative", "Unser Team")]))
    s1 = seite(
        kopf("Anforderungsprofil") + '<div class="rand" style="padding-top:16mm">' + kicker("Anforderungsprofil")
        + '<h2>Digitaler <span class="hl">Marketingmanager</span> (m/w/d)</h2>'
        + '<p class="lead" style="max-width:174mm">Als Stratege, Controller, Grafiker und Entwickler in einem entwickelst Du die digitale '
          'Marketingstrategie, steuerst Homepage und Social-Media-Kanäle in einem übergreifenden Dashboard und setzt '
          'Kampagneninhalte und technische Anpassungen selbst um.</p>'
        + f'<div class="profil">{bereiche}</div>'
        + '<div class="kasten hinweis" style="margin-top:8mm"><p class="label">Hinweis</p>'
          '<p>Bei uns bekommst Du dieses Profil als eingespieltes Team, ohne die Suche, die Einarbeitung und das Risiko einer Einzelperson.</p></div>'
        + '</div>', 2, 4)
    logo = '<img src="assets/empiria-logo.svg" alt="">'
    postings = [
        ("gelb", "Stellenanzeige", "Digitaler Marketing&shy;manager gesucht.", "Strategie, Umsetzung und Technik in einer Rolle – für alle, die digitales Marketing wirklich end-to-end verantworten wollen.",
         "Posting 1 · Ausschreibung · LinkedIn &amp; Karriereseite", "Wir suchen: Digitaler Marketingmanager (m/w/d) in Vollzeit.",
         ["Du entwickelst unsere digitale Marketingstrategie mit, steuerst Homepage, Social-Media-Kanäle und Dashboard als ein System – und setzt selbst um, statt nur zu briefen: von der Kampagnenidee bis zur technischen Umsetzung.",
          "Klingt nach Dir? Wir freuen uns auf Deine Bewerbung."]),
        ("schwarz", "Anforderungsprofil", "Stratege. Controller. Grafiker. Entwickler.", "Vier Rollen, eine Stelle. Gesucht wird eine Person mit echter Bandbreite – keine Spezialisierung auf nur einen Kanal.",
         "Posting 2 · Profilschärfe · LinkedIn", "Diese Stelle ist kein 08/15-Marketing-Job.",
         ["Wer bei uns digitales Marketing verantwortet, denkt strategisch, liest Kennzahlen wie ein Controller, gestaltet auf professionellem Niveau und bringt Umsetzungen technisch selbst in die IT ein.",
          "Mehrjährige Erfahrung im digitalen Marketing gesucht – keine Einstiegsposition."]),
        ("hell", "Jetzt bewerben", "Marketing, das wirklich wirkt.", "Volle Verantwortung statt Zuarbeit: Du gestaltest, wie unser digitales Marketing funktioniert – nicht nur, wie es aussieht.",
         "Posting 3 · Candidate Appeal · Instagram &amp; LinkedIn", "Lust auf Marketing mit echter Wirkung statt Kennzahlenfriedhof?",
         ["Bei uns übernimmst Du digitales Marketing end-to-end: Strategie, Kanäle, Dashboard, Umsetzung. Direkte Abstimmung mit der Geschäftsführung, hohe Eigenständigkeit, echte Entscheidungsspielräume.",
          "Interesse? Wir freuen uns auf Dich."]),
    ]
    zeilen = "".join(
        f'<div class="posting"><div class="motiv motiv--{f}"><small>{k}</small><div><b>{t}</b><span style="display:block;margin-top:2mm">{sub}</span></div>{logo}</div>'
        f'<div><p class="label">{lab}</p><h3>{h}</h3>{"".join(f"<p>{x}</p>" for x in ps)}</div></div>'
        for f, k, t, sub, lab, h, ps in postings)
    s2 = seite(
        kopf("Anforderungsprofil") + '<div class="rand" style="padding-top:16mm">' + kicker("Bonus")
        + '<h2>Drei fertige Stellenanzeigen <span class="hl">zum Veröffentlichen.</span></h2>'
        + '<p class="lead" style="max-width:170mm">Willst Du diese Stelle selbst besetzen? Hier sind drei fertige Postings inklusive Bild, mit denen Du direkt '
          'nach genau diesem Profil ausschreiben kannst – auf LinkedIn, der Karriereseite oder in Social Media. Unternehmensname und Kontakt einfach anpassen.</p>'
        + f'<div style="margin-top:5mm">{zeilen}</div></div>', 3, 4)
    s3 = seite(
        kopf("Anforderungsprofil") + '<div class="rand" style="padding-top:16mm">' + kicker("Viel Erfolg")
        + '<h2>Viel Erfolg bei der Suche nach Deinem <span class="hl">digitalen Marketingmanager.</span></h2>'
        + '<p class="lead">Wenn Du Dir das lieber sparen und die Rolle direkt von uns als eingespieltes Team übernehmen lassen willst, melde Dich einfach – wir freuen uns auf Dich.</p>'
        + '<p class="adresse"><b>empiria GmbH</b> · Kapellengasse 6 · 74564 Crailsheim</p>'
        + '</div>' + mt.draht() + '', 4, 4)
    return dokument(TITEL, [titel, s1, s2, s3], extra_css=CSS + mt.CSS)
