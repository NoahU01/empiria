"""PDF „Training & Sparring“ im Muster von KI zum Anfassen (10.10.2026).
Quelle: site/projekte/empiria-2/training-sparring.html (maßgeblich), dazu die beiden Format-Seiten
praesentationsseminar.html und sparring.html sowie ergänzend werkzeuge/pdf-seiten/pages.py P["training-sparring"].
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, check, zeitstrahl, team, kontaktdaten, dokument, ico)

TITEL = "Training & Sparring – empiria"
T = "Training &amp; Sparring"

CSS = """
.tabelle--zwei .zeile { width: 34mm; }
.tabelle--zwei { margin-top: 6mm; }
.tabelle--zwei thead th { padding-top: 1mm; padding-bottom: 3mm; }
.tabelle--zwei td { padding-top: 2.8mm; padding-bottom: 2.8mm; }
.tabelle--zwei th:nth-child(2), .tabelle--zwei td:nth-child(2) { width: 72mm; }
.tabelle--zwei td { font-size: 9pt; }
.wann { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 6mm; }
.wann div { display: flex; align-items: center; gap: 3mm; padding: 3.4mm 4mm; border: 1px solid #dcd8d1; border-radius: 9mm; font-size: 8.6pt; font-weight: 600; background: #fff; }
.wann svg { width: 5mm; height: 5mm; flex: 0 0 auto; }
.kicker--abstand { margin-top: 9mm; }
.notiz { text-wrap: balance; }
.turbo > div { display: flex; align-items: center; gap: 3mm; padding-top: 4mm; }
.kasten .turbo svg { margin: 0; flex: 0 0 auto; }
.kasten .turbo h3 { font-size: 10pt; }
.check--eng { margin-top: 4mm; row-gap: 1mm; }
.check--eng li { padding-top: 2mm; padding-bottom: 2mm; font-size: 9pt; }
"""


def bauen():
    n = 5
    s1 = seite(titelseite(
        "Training &amp; Sparring", 'Begleitung,<br><span class="hl">die wirkt.</span><br>Bis in den Alltag.',
        "Für Dein Team als Trainingsbegleitung, für Dich als Führungskraft im vertraulichen Sparring – "
        "zugeschnitten auf die Versicherungsbranche und Deinen Alltag.",
        kopfbild("Training & Sparring"),
        [("Format 01", "Teams befähigen"), ("Format 02", "1:1 Sparring"), ("Branche", "Versicherungen")]))

    def zeile(label, a, b):
        return f'<tr><td class="zeile">{label}</td><td>{a}</td><td>{b}</td></tr>'
    tabelle = ('<table class="tabelle tabelle--zwei"><thead><tr><th></th>'
               '<th><small>Format 01</small><b>Teams befähigen</b></th><th><small>Format 02</small><b>1:1 Sparring</b></th></tr></thead><tbody>'
               + zeile("Für wen", "Führungskräfte und ihre Teams, die Themen und Präsentationen vorbereiten", "Vorstandsmitglieder und Führungskräfte")
               + zeile("Worum es geht", "Business Storytelling, Visualisierung und Begleitung an echten Terminen", "Strategie, Geschäftsmodell und Führung")
               + zeile("So läuft es", "Onboarding, 2 Tage Training in Präsenz, 3–6 Monate Anwendungsphase", "So flexibel, wie es für Dich passt – vom Treffen bis zur Kurznachricht")
               + zeile("Ergebnis", "Dein Team überzeugt ohne Dich.", "Eine Richtung, mit der sich weiterarbeiten lässt.")
               + '</tbody></table>')
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:11mm;padding-bottom:11mm">' + kicker("Unser Ansatz")
        + '<h2>Drei Dinge, die den Unterschied machen.</h2>'
        + '<p class="lead">Inhalte aus Deiner Praxis, ehrliche Rückmeldung und eine Begleitung, die nicht nach dem Termin endet.</p>'
        + punkte([("target", "Auf Deinen Alltag zugeschnitten", "Inhalte und Fälle aus Deiner Praxis in der Versicherungsbranche."),
                  ("lock", "Vertraulich &amp; auf Augenhöhe", "Offen, ehrlich und mit klarer Rückmeldung – auch wenn sie unbequem ist."),
                  ("route", "Begleitung statt Einmal-Termin", "Wir bleiben dran, bis die Wirkung im Alltag messbar ankommt.")])
        + '</div><div class="rand" style="padding-top:9mm">' + kicker("Training &amp; Sparring")
        + '<h2>Zwei Formate. Ein Ziel: Wirkung im Alltag.</h2>'
        + '<p class="lead">Wähle das Format – wir passen es auf Dich an.</p>'
        + tabelle
        + '<p class="notiz">Beide Formate lassen sich kombinieren: Dein Team wird befähigt – und Du bekommst zusätzlich ein Gegenüber für Deine eigenen Themen.</p>'
        + '</div>', 2, n)

    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Format 01")
        + '<h2>Teams befähigen, <span class="hl">professionell zu kommunizieren.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft ins Leere? '
          'Wir bringen ihm bei, wie es geht, und begleiten es dabei, wenn es zählt: beim nächsten Kundenpitch, beim Rückversicherer, in der nächsten Abstimmungsrunde.</p>'
        + punkte([("message-square-text", "Business Storytelling &amp; Gesprächstaktik", "Bei jedem Termin zuerst klären: Wer sitzt im Raum, und welches Ergebnis wird gebraucht?"),
                  ("presentation", "Visualisierung &amp; Standards", "Folien, die verdichten statt überladen – für den Auftritt und für die Projektarbeit."),
                  ("route", "Umsetzungsbegleitung", "3–6 Monate an den echten Terminen Deines Teams, bis die Wirkung im Alltag ankommt.")])
        + '</div><div class="band band--hell wachsen" style="margin-top:12mm;padding-top:12mm">' + kicker("Ablauf")
        + '<h2>Vom Onboarding bis in den Alltag.</h2>'
        + '<div style="margin-top:-2mm">' + zeitstrahl([("01", "Onboarding", "2–3 Stunden, online."),
                      ("02", "Vorbereitung", "2–3 Wochen."),
                      ("03", "Training", "2 Tage in Präsenz."),
                      ("04", "Anwendung", "3–6 Monate, individuell.")]) + '</div>'
        + '<div class="kasten" style="margin-top:9mm"><div class="zwei"><div><p class="label">Lernlogik nach der 70-20-10-Regel</p>'
        + '<h3>Wirkung entsteht in der Anwendung.</h3></div>'
        + '<p style="margin-top:0">10 % Impulse im Seminar, 20 % kollegialer Austausch und gezielte Begleitung, '
          '70 % Lernen durch Anwendung an echten, relevanten Themen.</p></div></div>'
        + '</div>', 3, n)

    wann = [("coffee", "Persönliches Treffen"), ("mountain", "Offsite"), ("car", "Telefonat aus dem Auto"), ("message-circle", "Kurznachricht")]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Format 02")
        + '<h2>1:1 Sparring für Vorstände <span class="hl">und Führungskräfte.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Seit vielen Jahren begleiten wir Vorstandsmitglieder und Führungskräfte vertrauensvoll bei strategischen Themen, '
          'Ideen zum Geschäftsmodell oder Führungsfragen – offen, ohne interne Rücksichten.</p>'
        + '<p class="kicker kicker--abstand">Worüber wir sprechen</p>'
        + '<ul class="check check--eng">' + "".join(f"<li>{x}</li>" for x in [
            "Strategische Themen und Geschäftsmodellfragen", "Führungsfragen",
            "Komplexe Situationen aus mehreren Perspektiven", "Lösungswege und Vorgehensweisen abwägen",
            "Positionierung gegenüber Vorstand und Bereichen", "Umgang mit dem Aufsichtsrat",
            "Steuerung von Konzernunternehmen", "Konzeption von Kommunikation nach außen"]) + '</ul>'
        + '<p class="kicker kicker--abstand">Wann wir sprechen</p>'
        + '<div class="wann">' + "".join(f'<div>{ico(i)}{t}</div>' for i, t in wann) + '</div>'
        + '<div class="kasten" style="margin-top:10mm"><p class="label">Mehr als nur Sparring</p><h3>Umsetzungsturbo!</h3>'
        + '<p>Aus dem Sparring entstehen oft Ideen, die Du sofort vorantreiben willst. Intern fehlt dann meist einer von drei Erfolgsbausteinen – '
          'wir liefern das Ergebnis, ganz ohne weiteres Briefing.</p>'
        + '<div class="punkte turbo" style="grid-template-columns:repeat(3,1fr);margin-top:5mm">' + "".join(
            f'<div>{ico(i)}<h3>{t}</h3></div>' for i, t in
            [("user-round", "Jemand, der das Thema versteht"), ("timer", "Die Kapazität für die Umsetzung"), ("wrench", "Die Skills für die Umsetzung")]) + '</div>'
        + '</div></div>', 4, n)

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Begleitung, <span class="hl">die wirklich weiterbringt?</span></h2>'
        + '<p class="lead">Sag uns, ob es um Dein Team oder um Dich geht – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es wirken? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 5, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
