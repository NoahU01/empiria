"""PDF „Marketing 2.0“ – Übersicht über MES, sofort sichtbar, Paid Ads, Medien (Stil: Muster KI zum Anfassen)."""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, check, dokument, ico
import _marketing_teile as mt

TITEL = "Marketing 2.0 – empiria"
T = "Marketing 2.0"


def bauen():
    n = 4
    s1 = seite(titelseite(
        T, 'Marketing für Versicherer<br><span class="hl">anders gedacht.</span>',
        "Wir sind keine klassische Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das "
        "Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber.",
        kopfbild(T),
        [("Für wen", "Versicherer &amp; Makler"), ("Lösungen", "Vier Wege, ein Ergebnis"),
         ("Buchbar", "Komplett oder einzeln"), ("Grundlage", "Strategie vor Umsetzung")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Unser Ansatz")
        + '<h2>Marketing, das Deine Strategie<br>zum Erfolg führt.</h2>'
        + '<p class="lead" style="max-width:150mm">Unsere langjährige Projekterfahrung und unsere tiefe Kenntnis von Geschäftsmodell, Strategie und '
          'Zielgruppen eines Versicherers fließen in jedes Projekt ein. Das macht uns von der ersten Minute an schnell und schlagkräftig.</p>'
        + punkte([("layout-grid", "Komplett oder einzeln", "Buche uns als klar definierte Marketingabteilung – oder hol Dir gezielt einzelne Medien dazu."),
                  ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe."),
                  ("circle-check", "Professionell umgesetzt", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – damit sie im entscheidenden Moment wirkt.")])
        + '</div><div class="rand" style="padding-top:10mm">'
        + '<div class="kasten"><div class="zwei"><div><p class="label">Der Unterschied</p>'
          '<h3>Ein kurzes Briefing, ein paar gezielte Rückfragen – und es läuft.</h3></div>'
          '<p style="margin-top:0">Ob als komplette Marketingabteilung im Abo oder bei einzelnen Medien: Du musst uns nicht erklären, '
          'wie Versicherung funktioniert. Du kannst Dir sicher sein, dass es ab hier läuft.</p></div></div>'
        + kicker("Für wen wir arbeiten").replace('class="kicker"', 'class="kicker" style="margin-top:10mm"')
        + check(["Versicherer, die Marketing als feste Größe brauchen, ohne eigenes Team aufzubauen",
                 "Maklerunternehmen und Versicherungsbüros mit mehreren Mitarbeitenden",
                 "Agenturleitungen, die am Vertriebserfolg gemessen werden",
                 "Bereiche, die ein einzelnes Thema sichtbar machen müssen – schnell und sauber"])
        + '</div>', 2, n)

    wege = [
        ("MarketingEcoSystem (MES)", "Für Versicherer, Makler und Versicherungsbüros",
         "Homepage, Kanäle und Dashboard aus einer Hand – alles greift ineinander, Du musst uns nicht briefen.",
         ["Homepage", "Social-Media-Kanäle", "Zentrales Dashboard"], "ab 399 € mtl."),
        ("sofort sichtbar", "Für Agenturleitungen und Makler im Vertrieb",
         "Digitale Sichtbarkeit für Agenturleiterinnen und Agenturleiter – ohne Briefing, mit fertigem Auftritt.",
         ["Postings", "E-Mail-Funnel", "Landingpage"], "ab 349 € mtl."),
        ("Paid Ads", "Für alle, die jeden Euro nachvollziehen wollen",
         "Kampagnen auf Google und Meta, die Anfragen bringen – klar ausgewertet statt Blackbox.",
         ["Google Ads", "Meta Ads", "LinkedIn Ads"], "Umfang nach Vorhaben"),
        ("Medien, die Ergebnisse liefern", "Für Themen, die im entscheidenden Moment tragen müssen",
         "PowerPoint, Landingpage und Roll-up aus einer Hand – professionell umgesetzt, damit Deine Botschaft trägt.",
         ["PowerPoint", "Landingpage", "Roll-up"], "Umfang nach Vorhaben"),
    ]
    zeilen = "".join(
        f'<div><div><h3>{t}</h3><span class="unter">{fw}</span></div>'
        f'<div><p>{p}</p><div class="teile">{"".join(f"<span>{x}</span>" for x in teile)}</div>'
        f'<p class="preiszeile">Investition: <b>{preis}</b></p></div></div>'
        for t, fw, p, teile, preis in wege)
    s3 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Unsere Lösungen")
        + '<h2>Vier Wege. Ein Ergebnis:<br><span class="hl">Sichtbarkeit, die verkauft.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Ob als Gesamtpaket oder einzeln buchbar – Du wählst, wir liefern professionell.</p>'
        + f'<div class="liste wege">{zeilen}</div>'
        + '<p class="notiz">Preise zzgl. Umsatzsteuer in gesetzlicher Höhe. Bei Paid Ads und Medien hängt der Umfang vom Vorhaben ab – '
          'Du bekommst zeitnah ein konkretes Angebot.</p>'
        + '</div>', 3, n, klasse="seite--hell")

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Welcher Weg passt <span class="hl">zu Deinem Marketing?</span>',
                      "Schildere uns Deine Ausgangslage – wir melden uns zeitnah mit einem konkreten Vorschlag, welcher der vier Wege für Dich am meisten bringt.")
        + '</div>' + mt.draht(), 4, n)

    css = mt.CSS + """
.wege > div { grid-template-columns: 62mm 1fr; padding: 6.6mm 0; }
.wege h3 { font-size: 12.5pt; }
.wege .teile { display: flex; flex-wrap: wrap; gap: 1.6mm; margin-top: 2.6mm; }
.wege .teile span { font-size: 7.4pt; font-weight: 600; padding: .9mm 2.6mm; border: 1px solid #1a1817; border-radius: 9mm; }
"""
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=css)
