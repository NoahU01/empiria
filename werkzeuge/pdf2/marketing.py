"""PDF „Marketing 2.0“ – Übersicht über MES, sofort sichtbar, Paid Ads, Medien (Runde 2, Stand der 2.0-Seite 10.10.2026)."""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, dokument, ico
import _marketing_teile as mt

TITEL = "Marketing 2.0 – empiria"
T = "Marketing 2.0"

# Die vier Wege wie auf der Seite (Abschnitt „Unsere Lösungen“), Bausteine und Preise aus den jeweiligen 2.0-Seiten
WEGE = [
    ("layout-dashboard", "MarketingEcoSystem (MES)", "MES",
     "Homepage, Kanäle und Dashboard aus einer Hand – alles greift ineinander, Du musst uns nicht briefen.",
     ["Landingpage", "Social-Media-Kanäle", "Zentrales Dashboard"], "ab 399 €", "pro Monat"),
    ("users", "sofort sichtbar", "sofort sichtbar",
     "Digitale Sichtbarkeit für Agenturleiterinnen und Agenturleiter – ohne Briefing, mit fertigem Auftritt.",
     ["Social Media Postings", "E-Mail-Funnel", "Passende Landingpages"], "ab 349 €", "pro Monat"),
    ("megaphone", "Paid Ads", "Paid Ads",
     "Kampagnen auf Google, Meta und LinkedIn, die Anfragen bringen – klar ausgewertet statt Blackbox.",
     ["Google Ads", "Meta Ads", "LinkedIn Ads"], "Individuell", "Angebot nach Vorhaben"),
    ("presentation", "Medien, die Ergebnisse liefern", "Medien",
     "PowerPoint, Landingpage und Roll-up aus einer Hand – professionell umgesetzt, damit Deine Botschaft trägt.",
     ["PowerPoint", "Landingpage", "Roll-up"], "Individuell", "Angebot nach Vorhaben"),
]


def bauen():
    n = 4
    s1 = seite(titelseite(
        T, 'Marketing für Versicherer <span class="hl">anders gedacht.</span>',
        "Wir sind keine klassische Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das "
        "Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber.",
        kopfbild(T),
        [("Für wen", "Versicherer &amp; Makler"), ("Lösungen", "Vier Wege, ein Ergebnis"),
         ("Buchbar", "Komplett oder einzeln"), ("Grundlage", "Strategie vor Umsetzung")]))

    wege_icons = '<div class="wege4">' + "".join(
        f'<div>{ico(i, strich=1.3)}<b>{t}</b><p>{d}</p></div>' for i, t, _, d, *_ in WEGE) + '</div>'
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Unser Ansatz")
        + '<h2>Marketing, das Deine Strategie<br>zum Erfolg führt.</h2>'
        + '<p class="lead" style="max-width:150mm">Unsere langjährige Projekterfahrung und unsere tiefe Kenntnis von Geschäftsmodell, Strategie und '
          'Zielgruppen eines Versicherers fließen in jedes Projekt ein. Das macht uns von der ersten Minute an schnell und schlagkräftig.</p>'
        + punkte([("layout-grid", "Komplett oder einzeln", "Buche uns als klar definierte Marketingabteilung – oder hol Dir gezielt einzelne Medien dazu."),
                  ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe."),
                  ("circle-check", "Professionell umgesetzt", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – damit sie im entscheidenden Moment wirkt.")])
        + '</div><div class="rand" style="padding-top:12mm">' + kicker("Unsere Lösungen")
        + '<h2>Vier Wege. Ein Ergebnis:<br><span class="hl">Sichtbarkeit, die verkauft.</span></h2>'
        + '<p class="lead">Ob als Gesamtpaket oder einzeln buchbar – Du wählst, wir liefern professionell.</p>'
        + wege_icons + '</div>', 2, n)

    sp = [(f"Lösung 0{k + 1}", w[2], "", False) for k, w in enumerate(WEGE)]
    zeilen = [
        ("Investition", [f'{p}<span class="klein">{e}</span>' for *_, p, e in WEGE], "preis"),
        ("Bausteine", [mt.ul(b) for _, _, _, _, b, *_ in WEGE], ""),
        ("Im Detail", ["Drei Pakete: Eigenregie, Marketing as a Service, Unternehmertum",
                       "Drei Pakete: Fokus, Reichweite, Marktposition",
                       "Kanal-Check, vier Schritte von der Analyse bis zur Skalierung, kostenloser Potentialcheck",
                       "Use Cases von der Positionierung bis zum Pitch im Konsortium"], ""),
    ]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Die vier Wege im Vergleich")
        + '<h2>Du wählst, <span class="hl">wir liefern.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Jeder Weg ist einzeln buchbar – oder als Gesamtpaket, bei dem alles ineinandergreift.</p>'
        + mt.tabelle(sp, zeilen).replace('<col style="width:28mm">', '<col style="width:25mm">')
        + '<p class="notiz">Preise zzgl. Umsatzsteuer in gesetzlicher Höhe. Bei Paid Ads und Medien hängt der Umfang vom Vorhaben ab – '
          'Du bekommst zeitnah ein konkretes Angebot.</p>'
        + '<div class="kasten" style="margin-top:12mm"><div class="zwei"><div><p class="label">Alle Details</p>'
          '<h3>Zu jedem Weg gibt es ein eigenes PDF.</h3></div>'
          '<p style="margin-top:0">Pakete, Abläufe und Preise im Einzelnen findest Du auf den Seiten zu MarketingEcoSystem (MES), '
          'sofort sichtbar, Paid Ads und Medien – jeweils mit eigenem PDF zum Weitergeben.</p></div></div>'
        + '</div>', 3, n)

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Bereit, Dein Marketing auf das <span class="hl">nächste Level</span> zu bringen?',
                      "Kurze Wege statt langer Abstimmungsrunden: Schildere uns Deine Ausgangslage – wir melden uns zeitnah mit einem Vorschlag, welcher der vier Wege für Dich am meisten bringt.")
        + '</div>' + mt.draht(), 4, n)

    css = mt.CSS + """
.wege4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6mm; margin-top: 10mm; }
.wege4 > div { border-top: 1.6px solid #1a1817; padding-top: 5mm; }
.wege4 svg { width: 9mm; height: 9mm; display: block; }
.wege4 b { display: block; margin-top: 3.5mm; font-family: 'Lora', Georgia, serif; font-size: 11pt; line-height: 1.25; min-height: 2.5em; }
.wege4 p { margin-top: 2mm; font-size: 8.6pt; line-height: 1.5; color: #3d3a37; }
.tabelle thead th { vertical-align: top; }
.tabelle .preis .klein { font-family: 'Poppins', Arial, sans-serif; font-weight: 400; font-size: 7.2pt; }
"""
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=css)
