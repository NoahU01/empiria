"""PDF „Medien, die Ergebnisse liefern“ im Muster von KI zum Anfassen (10.10.2026).
Quelle: site/projekte/empiria-2/medien.html (maßgeblich, inkl. Erklär-Popups), ergänzend werkzeuge/pdf-seiten/pages.py P["medien"].
Medien sind PowerPoint, Landingpage und Roll-up (kein Video).
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, check, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Medien, die Ergebnisse liefern – empiria"
T = "Medien"

CSS = """
.medien { display: grid; gap: 5mm; margin-top: 10mm; }
.medium { display: grid; grid-template-columns: 74mm 1fr; border: 1px solid #dcd8d1; border-radius: 4.5mm; overflow: hidden; background: #fff; }
.medium__bild { display: flex; align-items: center; justify-content: center; height: 47mm; padding: 5mm 8mm; background: #f3f1ee; }
.medium__bild svg { width: 100%; height: 100%; }
.medium__text { display: flex; flex-direction: column; justify-content: center; padding: 5mm 9mm; }
.medium__text small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.medium__text h3 { margin-top: 1.6mm; font-size: 15pt; }
.medium__text p { text-wrap: pretty; }
.medium__text p { margin-top: 2.4mm; font-size: 9.2pt; line-height: 1.55; color: #3d3a37; }
.medien-check .check { margin-top: 9mm; row-gap: 4mm; }
.medien-check .check li { padding-top: 3.4mm; padding-bottom: 3.4mm; }
.team3 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 8mm; align-items: center; margin-top: 9mm; }
.team3 .team { gap: 4mm; margin-top: 0; }
.team3 .person { width: 30mm; }
.team3 .person img { width: 24mm; height: 24mm; }
.team3 .kontaktdaten { margin-top: 0; }
"""


def bauen():
    n = 5
    s1 = seite(titelseite(
        "Medien, die Ergebnisse liefern", 'Deine Botschaft.<br><span class="hl">Auf den Punkt.</span><br>Volle Wirkung.',
        "Wir sind keine typische Medienagentur. Wir sind Profis in den Themen Geschäftsmodell Versicherung, Strategie und Kommunikation "
        "– und übersetzen Deine Themen in die Welt Deiner Zielgruppe.",
        kopfbild("Medien, die Ergebnisse liefern"),
        [("Medium 01", "PowerPoint"), ("Medium 02", "Landingpage"), ("Medium 03", "Roll-up")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:15mm;padding-bottom:15mm">' + kicker("Unser Ansatz")
        + '<h2>Wir sind keine Medienagentur, sondern Profis für Wirkung.</h2>'
        + '<p class="lead">Bevor ein einziges Medium entsteht, verstehen wir Dein Geschäftsmodell, Deine Strategie und Deine Zielgruppe.</p>'
        + punkte([("briefcase", "Geschäftsmodell &amp; Strategie", "Wir verstehen, wie Dein Geschäftsmodell funktioniert und wohin Deine Strategie steuert – bevor wir über Medien sprechen."),
                  ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe – damit Kommunikation ankommt."),
                  ("presentation", "Professionelle Medien", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – professionell gebaut, damit sie im entscheidenden Moment wirkt.")])
        + '</div><div class="rand" style="padding-top:16mm">' + kicker("Für wen das gemacht ist")
        + '<h2>Themen, die im entscheidenden Moment tragen müssen.</h2>'
        + '<div class="medien-check">' + check(["Themen, die im Vorstand oder Gremium tragen müssen", "Vertrieb und Messeauftritte mit klarer Botschaft",
                 "Bereiche ohne eigene Medienproduktion", "Auftritte, bei denen die Unterlage den Unterschied macht"]) + '</div>'
        + '</div>', 2, n)

    medien = [("Medium 01", "PowerPoint", "Eine Präsentation, die Deine Business Story trägt – klar strukturiert, professionell gestaltet und startklar für den nächsten großen Moment im Raum."),
              ("Medium 02", "Landingpage", "Eine klar auf Deine Zielgruppe zugeschnittene Seite, die genau ein zentrales Problem löst und Interessierte gezielt zum nächsten Schritt führt."),
              ("Medium 03", "Roll-up", "Der Gesamtzusammenhang aus Sicht Deiner Zielgruppe – in einem Bild visualisiert und dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist.")]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Medien wirksam einsetzen")
        + '<h2>Es geht nicht um Medien, sondern um <span class="hl">Deine Ziele.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Wir starten nie mit der Frage PowerPoint, Landingpage oder Roll-up, sondern damit, was Du und Dein Team benötigen, '
          'um erfolgreich zu sein. Wenn diese Taktik steht, entwickeln wir zielgerichtete Medien, die genau dieses Ergebnis liefern.</p>'
        + '<div class="medien">' + "".join(
            f'<div class="medium"><div class="medium__bild">{kopfbild(t)}</div><div class="medium__text"><small>{l}</small><h3>{t}</h3><p>{p}</p></div></div>'
            for l, t, p in medien) + '</div>'
        + '</div>', 3, n)

    faelle = [("Positionierung eines Unternehmens neu ausrichten", "Ein kleineres Konzernunternehmen mit klarem Spezialsegment soll professioneller am Markt auftreten. Es braucht eine Gesamtlogik, die Kooperationspartnern, Vertriebspartnern und Kunden verständlich macht, wofür das Unternehmen steht – aus einer Hand."),
              ("Produktlaunch oder Produktrelaunch", "Statt gedruckter Broschüren und PowerPoints mit 150 Detailfolien entscheiden wir gezielt, welche Medien wirklich wirken. Oft ist das eine durchdachte Kombination digitaler Formate, die Vertriebspartner tatsächlich erfolgreich macht."),
              ("Aufsichtsrats- und Gremientermine", "Ob Markteintritt, Umsteuern im Risikoportfolio oder ein neues Bestandsführungssystem: Große Themen müssen kompakt und vertrauensbildend erzählt werden. Die Übersetzung in die Welt fachfremder Gremienmitglieder entscheidet, ob die Botschaft ankommt."),
              ("Gespräche mit dem Rückversicherer", "Der Rückversicherer muss verstehen, wohin sich das Geschäftsmodell bewegt – stringent erzählt, nicht nur in harten Zahlen. Das gilt für die jährlichen Erneuerungsgespräche ebenso wie für Monte Carlo oder Baden-Baden.")]
    s4 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
        + '<h2>Konkrete Use Cases aus der Praxis.</h2>'
        + '<p class="lead">Eine Auswahl realer Anwendungsfälle, die zeigen, wie unsere Medien in der Praxis wirken.</p>'
        + '<div class="liste">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + '<div class="kasten" style="margin-top:8mm"><div class="zwei"><div><p class="label">Im Fokus</p><h3>Der entscheidende Pitch im Konsortium</h3></div>'
        + '<p style="margin-top:0">Ausschreibung bei einem Großkunden, gemeinsam mit Kooperationspartnern gegen namhafte Wettbewerber: Statt Standardfolien liefern wir Medien, '
          'die zu 100 % zeigen, dass wir den Kunden verstanden haben – erzählt so, dass die Story im Raum sitzt.</p></div></div>'
        + '</div>', 4, n, klasse="seite--hell")

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Medien, <span class="hl">die wirklich wirken?</span></h2>'
        + '<p class="lead">Schildere uns Dein Thema und die Zielgruppe – wir sagen Dir, welches Medium dafür trägt und was es braucht.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="team3">' + team(["daniel", "kerstin_content", "noah_pm"]) + kontaktdaten() + '</div></div>', 5, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
