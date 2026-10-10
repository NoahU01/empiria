"""PDF „Medien, die Ergebnisse liefern“ – Runde 2 (10.10.2026), Aufbau wie alle 2.0-PDFs.
Reihenfolge wie die Seite: Ansatz → Medien wirksam einsetzen (Info-Fenster) → Beispiele („Mehr lesen“ in voller Länge) → Kontakt.
Quelle: site/projekte/empiria-2/medien.html (maßgeblich, inkl. Erklär-Popups), ergänzend werkzeuge/pdf-seiten/pages.py P["medien"].
Medien sind PowerPoint, Landingpage und Roll-up (kein Video).
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Medien, die Ergebnisse liefern – empiria"
T = "Medien"

CSS = """
.liste--lang { margin-top: 7mm; }
.liste--lang > div { padding: 3mm 0; }
.liste--lang p { line-height: 1.5; }
.liste--lang p { font-size: 8.4pt; }
.team3 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 8mm; align-items: center; margin-top: 9mm; }
.team3 .team { gap: 4mm; margin-top: 0; }
.team3 .person { width: 30mm; }
.team3 .person img { width: 24mm; height: 24mm; }
.team3 .kontaktdaten { margin-top: 0; }
"""


def bauen():
    n = 4
    s1 = seite(titelseite(
        "Medien, die Ergebnisse liefern", 'Deine Botschaft.<br><span class="hl">Auf den Punkt.</span><br>Volle Wirkung.',
        "Wir sind keine typische Medienagentur. Wir sind Profis in den Themen Geschäftsmodell Versicherung, Strategie und Kommunikation.",
        kopfbild("Medien, die Ergebnisse liefern"),
        [("Medium 01", "PowerPoint"), ("Medium 02", "Landingpage"), ("Medium 03", "Roll-up")]))

    # Seite 2: Ansatz (gelbes Band) + Medien wirksam einsetzen (Info-Fenster der drei Medien, voller Text)
    medien = [("Medium 01", "PowerPoint", "Eine Präsentation, die Deine Business Story trägt – klar strukturiert, professionell gestaltet und startklar für den nächsten großen Moment im Raum."),
              ("Medium 02", "Landingpage", "Eine klar auf Deine Zielgruppe zugeschnittene Seite, die genau ein zentrales Problem löst und Interessierte gezielt zum nächsten Schritt führt."),
              ("Medium 03", "Roll-up", "Der Gesamtzusammenhang aus Sicht Deiner Zielgruppe – in einem Bild visualisiert und dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist.")]
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:10mm;padding-bottom:10mm">' + kicker("Unser Ansatz")
        + '<h2>Wir sind keine Medienagentur, sondern Profis für Wirkung.</h2>'
        + '<p class="lead" style="max-width:none">Bevor ein einziges Medium entsteht, verstehen wir Dein Geschäftsmodell, Deine Strategie und Deine Zielgruppe.</p>'
        + punkte([("briefcase", "Geschäftsmodell &amp; Strategie", "Wir verstehen, wie Dein Geschäftsmodell funktioniert und wohin Deine Strategie steuert – bevor wir über Medien sprechen."),
                  ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe – der entscheidende Erfolgsfaktor, damit Kommunikation ankommt."),
                  ("award", "Professionelle Medien", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – professionell gebaut, damit sie im entscheidenden Moment wirkt.")])
        + '</div><div class="rand" style="padding-top:9mm">' + kicker("Medien wirksam einsetzen")
        + '<h2>Es geht nicht um Medien, sondern um Deine Ziele.</h2>'
        + '<p class="lead" style="max-width:none">Wir starten nie mit der Frage PowerPoint, Landingpage oder Roll-up, sondern damit, was Du und Dein Team benötigen, '
          'um erfolgreich zu sein. Wenn diese Taktik steht, entwickeln wir zielgerichtete Medien, die genau dieses Ergebnis liefern.</p>'
        + punkte([(i, t, p) for (l, t, p), i in zip(medien, ["presentation", "app-window", "rollup"])]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:7mm;')
        + '</div>', 2, n)

    # Seite 3: Beispiele – volle Texte aus den „Mehr lesen“-Fenstern
    faelle = [("Positionierung eines Unternehmens neu ausrichten",
               "Ein kleineres Konzernunternehmen mit klarem Spezialsegment – etwa Pensionskasse, Schadenmanagement oder Ventilmakler – soll professioneller am Markt auftreten. "
               "Dies gelingt nicht mit einer Homepage hier und einer intern zusammengestellten PowerPoint dort. Es braucht eine Gesamtlogik, die Kooperationspartnern, "
               "Vertriebspartnern und Kunden gleichermaßen verständlich macht, wofür das Unternehmen steht – aus einer Hand entwickelt und strategisch wie vertrieblich durchdacht."),
              ("Produktlaunch oder Produktrelaunch",
               "Klassisch wird hier in gedruckten Broschüren und PowerPoints mit 150 Detailfolien gedacht – Medien, mit denen kein Vertriebspartner etwas anfangen kann. "
               "Ein Vertriebsimpuls funktioniert nur, wenn er die Zielgruppe tatsächlich erfolgreich macht. Deshalb entscheiden wir gezielt, welche Medien wirklich wirken, "
               "und setzen dafür oft auf eine durchdachte Kombination digitaler Formate statt auf das eine überladene Dokument."),
              ("Aufsichtsrats- und Gremientermine",
               "Hier zählt nicht das letzte Detail, sondern der Gesamtnutzen fürs Unternehmen – professionell vorgetragen und vertrauensbildend. "
               "Ob Markteintritt, strategisches Umsteuern im Risikoportfolio oder ein neues Bestandsführungssystem: Große Themen müssen kompakt und verständlich erzählt werden. "
               "Zumal im Gremium oft fachfremde Personen ohne Versicherungshintergrund sitzen – die Übersetzung in ihre Welt entscheidet, ob die Botschaft ankommt."),
              ("Gespräche mit dem Rückversicherer",
               "Der Rückversicherer muss verstehen, wohin sich das Geschäftsmodell des Versicherers bewegt – stringent erzählt, nicht nur in harten Zahlen. "
               "Das gilt für die jährlichen Erneuerungsgespräche genauso wie für die Vorbereitung auf Monte Carlo oder Baden-Baden: "
               "Es geht darum, die strategische Richtung so darzulegen, dass sie im Gespräch trägt.")]
    s3 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
        + '<h2>Konkrete Use Cases aus der Praxis.</h2>'
        + '<p class="lead" style="max-width:none">Eine Auswahl realer Anwendungsfälle, die zeigen, wie unsere Medien in der Praxis wirken.</p>'
        + '<div class="liste liste--lang">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + '<div class="kasten" style="margin-top:6mm"><p class="label">Im Fokus</p><h3>Der entscheidende Pitch im Konsortium</h3>'
        + '<p>Eine Ausschreibung bei einem Großkunden, angetreten gemeinsam mit Kooperationspartnern gegen namhafte Wettbewerber. '
          'Statt Standardfolien mit Interpretationsspielraum liefern wir Medien, die zu 100&nbsp;% zeigen: Wir haben den Kunden verstanden – und die Lösung ist maßgeschneidert. '
          'Die Story wird so erzählt, dass sie im Raum sitzt und den Ausschlag gibt.</p></div>'
        + '</div>', 3, n, klasse="seite--hell")

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Medien, <span class="hl">die wirklich wirken?</span></h2>'
        + '<p class="lead">Schildere uns Dein Thema und die Zielgruppe – wir sagen Dir, welches Medium dafür trägt und was es braucht.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="team3">' + team(["daniel", "kerstin_content", "noah_pm"]) + kontaktdaten() + '</div></div>', 4, n)
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=CSS)
