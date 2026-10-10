"""PDF „Training & Sparring“ im Muster KI zum Anfassen – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/training-sparring.html (maßgeblich), dazu die beiden Format-Seiten
praesentationsseminar.html und sparring.html sowie ergänzend werkzeuge/pdf-seiten/pages.py P["training-sparring"].
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, check, zeitstrahl, team, kontaktdaten, dokument, ico)

TITEL = "Training & Sparring – empiria"
T = "Training &amp; Sparring"

CSS = """
.tabelle--zwei .zeile { width: 34mm; }
.tabelle--zwei { margin-top: 3mm; }
.tabelle--zwei thead th { padding-top: 1mm; padding-bottom: 2mm; }
.tabelle--zwei td { padding-top: 2.4mm; padding-bottom: 2.4mm; }
.tabelle--zwei th:nth-child(2), .tabelle--zwei td:nth-child(2) { width: 72mm; }
.tabelle--zwei td { font-size: 9pt; }
.wann { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 5mm; }
.wann > div { border-top: 1.6px solid #1a1817; padding-top: 3.6mm; display: flex; align-items: center; gap: 2.6mm; }
.wann svg { width: 5.6mm; height: 5.6mm; flex: 0 0 auto; }
.wann b { font-family: 'Lora', Georgia, serif; font-size: 10pt; line-height: 1.2; display: block; }
.band--hell .zs h3 { font-size: 11pt; }
.band--hell .zs li { padding-right: 4mm; }
.band--hell .zs { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
.liste small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 1.6mm; }
.liste .erg { margin-top: 1.8mm; color: #1a1817; }
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p { text-wrap: pretty; }
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
        "Für Dein Team als Trainingsbegleitung, für Dich als Führungskraft im vertraulichen Sparring.",
        kopfbild("Training & Sparring"),
        [("Format 01", "Teams befähigen"), ("Format 02", "1:1 Sparring"), ("Branche", "Versicherungen")]))

    def zeile(label, a, b):
        return f'<tr><td class="zeile">{label}</td><td>{a}</td><td>{b}</td></tr>'
    tabelle = ('<table class="tabelle tabelle--zwei"><thead><tr><th></th>'
               '<th><small>Format 01</small><b>Teams befähigen</b></th><th><small>Format 02</small><b>1:1 Sparring</b></th></tr></thead><tbody>'
               + zeile("Kurz gesagt", "Dein Team bereitet Themen vor, die nicht überzeugen? Wir bringen ihm bei, wie es geht – und begleiten es dabei, wenn es zählt.",
                       "Strategisches Sparring auf Augenhöhe für Führungskräfte in der Versicherungsbranche – vertraulich, erfahren und mit klarer Rückmeldung.")
               + zeile("Für wen", "Führungskräfte und ihre Teams, die Themen und Präsentationen vorbereiten", "Vorstandsmitglieder und Führungskräfte")
               + zeile("Worum es geht", "Business Storytelling, Visualisierung und Begleitung an echten Terminen", "Strategie, Geschäftsmodell und Führung")
               + zeile("So läuft es", "Onboarding, 2 Tage Training in Präsenz, 3–6 Monate Anwendungsphase", "So flexibel, wie es für Dich passt – vom Treffen bis zur Kurznachricht")
               + zeile("Ergebnis", "Dein Team überzeugt ohne Dich.", "Eine Richtung, mit der sich weiterarbeiten lässt.")
               + '</tbody></table>')
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:9mm;padding-bottom:9mm">' + kicker("Unser Ansatz")
        + '<h2>Drei Dinge, die den Unterschied machen.</h2>'
        + '<p class="lead">Inhalte aus Deiner Praxis, ehrliche Rückmeldung und eine Begleitung, die nicht nach dem Termin endet.</p>'
        + punkte([("target", "Auf Deinen Alltag zugeschnitten", "Inhalte und Fälle aus Deiner Praxis in der Versicherungsbranche."),
                  ("lock", "Vertraulich &amp; auf Augenhöhe", "Offen, ehrlich und mit klarer Rückmeldung – auch wenn sie unbequem ist."),
                  ("route", "Begleitung statt Einmal-Termin", "Wir bleiben dran, bis die Wirkung im Alltag messbar ankommt.")])
        + '</div><div class="rand" style="padding-top:8mm">' + kicker("Training &amp; Sparring")
        + '<h2>Zwei Formate. Ein Ziel: Wirkung im Alltag.</h2>'
        + '<p class="lead">Wähle das Format – wir passen es auf Dich an.</p>'
        + tabelle
        + '</div>', 2, n)

    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Format 01")
        + '<h2>Teams befähigen, <span class="hl">professionell zu kommunizieren.</span></h2>'
        + '<p class="lead" style="max-width:155mm">Dein Team bereitet Themen vor, die nicht überzeugen? Wir bringen ihm bei, wie es geht – und begleiten es dabei, wenn es zählt: '
          'beim nächsten Kundenpitch, beim Rückversicherer, in der nächsten Abstimmungsrunde.</p>'
        + '<div class="liste">' + "".join(f'<div><div><small>{k}</small><h3>{t}</h3></div><div><p>{p}</p><p class="erg"><b>Ergebnis:</b> {e}</p></div></div>' for k, t, p, e in [
            ("Baustein 01", "Business Storytelling &amp; Gesprächstaktik",
             "Mindset, Methodik, Umsetzung: wie Entscheider denken, wie eine Business Story zielgruppengerecht aufgebaut wird und wie ein Termin startet und geführt wird.",
             "Dein Team baut zügig und sicher eine überzeugende Business Story auf und leitet professionell durch den Termin."),
            ("Baustein 02", "Visualisierung &amp; Nutzung Standards",
             "Aus der Business Story entstehen professionelle Folien – als Vortragsfolien für den Auftritt und als Beraterfolien für die Projektarbeit.",
             "Dein Team erstellt auf Basis einer klaren Story schnell professionelle, überzeugende Folien."),
            ("Baustein 03", "Umsetzungsbegleitung",
             "3–6 Monate an echten Themen, nach der 70-20-10-Regel: Auftrag klären, Storyboard, Präsentation, Gesprächstaktik für den Termin, anschließendes Review.",
             "Dein Team setzt die Inhalte sicher bei echten Themen um und geht strukturiert in entscheidende Termine.")]) + '</div>'
        + '</div><div class="band band--hell wachsen" style="margin-top:12mm;padding-top:12mm">' + kicker("Ablauf")
        + '<h2>Vom Onboarding bis in den Alltag.</h2>'
        + '<div style="margin-top:-2mm">' + zeitstrahl([("01", "Onboarding", "2–3 Std., online"),
                      ("02", "Vorbereitungsphase", "2–3 Wochen"),
                      ("03", "Training", "2 Tage, Präsenz"),
                      ("04", "Anwendungsphase", "3–6 Monate, individuell")]) + '</div>'
        + '</div>', 3, n)

    wann = [("users", "Persönliches Treffen"), ("map-pin", "Offsite"), ("car", "Telefonat aus dem Auto"), ("message-circle", "Kurznachricht")]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Format 02")
        + '<h2>1:1 Sparring für Vorstände <span class="hl">und Führungskräfte.</span></h2>'
        + '<p class="lead" style="max-width:155mm">Strategisches Sparring auf Augenhöhe für Führungskräfte in der Versicherungsbranche – vertraulich, erfahren und mit klarer Rückmeldung. '
          'Bei strategischen Themen, Ideen zum Geschäftsmodell oder Führungsfragen.</p>'
        + '<p class="kicker" style="margin-top:9mm">Worüber wir sprechen</p>'
        + '<ul class="check check--eng">' + "".join(f"<li>{x}</li>" for x in [
            "Strategische Themen und Geschäftsmodellfragen", "Positionierung gegenüber Vorstand und anderen Bereichen", "Führungsfragen",
            "Umgang mit dem Aufsichtsrat", "Betrachtung komplexer Situationen aus unterschiedlichen Perspektiven",
            "Steuerung von Konzernunternehmen", "Abwägen von Lösungswegen und Vorgehensweisen", "Konzeption von Kommunikation nach außen"]) + '</ul>'
        + '<p class="kicker" style="margin-top:9mm">Wann wir sprechen</p>'
        + '<div class="wann">' + "".join(f'<div>{ico(i)}<b>{t}</b></div>' for i, t in wann) + '</div>'
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
