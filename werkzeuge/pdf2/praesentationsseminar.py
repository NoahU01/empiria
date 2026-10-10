"""PDF „Teams befähigen, professionell zu kommunizieren“ – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/praesentationsseminar.html inkl. der drei „Module & Ergebnis“-Dialoge (tm0–tm2)
und des Zeitplan-Modals (onboardingModalOverlay)."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, dokument)
from _strategie_teile import TEAM3_CSS, LISTE_CSS, schluss, liste

TITEL = "Teams befähigen, professionell zu kommunizieren – empiria"
T = "Teams befähigen"
N = 7

CSS = TEAM3_CSS + LISTE_CSS


def ul(items):
    return "<ul>" + "".join(f"<li>{x}</li>" for x in items) + "</ul>"


def ergebnis(text, mt="8mm"):
    """Schwarzer Kasten „Ergebnis“ (Zwischenergebnis eines Bausteins)."""
    return (f'<div class="kasten" style="margin-top:{mt}"><p class="label">Ergebnis</p>'
            f'<p style="font-size:9.6pt;color:#fff;max-width:150mm">{text}</p></div>')


def bauen():
    s1 = seite(titelseite(
        "Befähigung und Begleitung, kein Seminar", 'Teams befähigen, professionell zu <span class="hl">kommunizieren.</span>',
        "Du bist Führungskraft in der Versicherungsbranche und Dein Team bereitet Themen und Präsentationen vor, die nicht überzeugen?",
        kopfbild("Teams befähigen, professionell zu kommunizieren"),
        [("Onboarding", "2–3 Std., online"), ("Training", "2 Tage, Präsenz"), ("Begleitung", "3–6 Monate"), ("Bausteine", "Story, Folien, Alltag")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Das Problem")
        + '<h2>Dein Team bereitet vor. Und erreicht das Ziel <span class="hl">trotzdem nicht.</span></h2>'
        + punkte([("presentation", "", "Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft ins Leere."),
                  ("users", "", "Dein Team präsentiert im Lenkungsausschuss oder beim Kunden – und hinterher denkst Du: Das hätte besser laufen müssen."),
                  ("message-square-text", "", "Die Story trägt nicht, die Unterlagen überzeugen nicht und im Raum fehlt die Souveränität, auf Fragen zu reagieren.")]).replace("<h3></h3>", "")
        + '<p class="lead" style="margin-top:7mm"><b>Es wird Zeit, bisherige Denkmuster mit einfachen Logiken zu durchbrechen.</b></p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Befähigung und Begleitung<br>bei der Umsetzung.</h2>'
        + '<p class="lead">Wir bringen Deinem Team bei, wie das geht – und lassen es danach nicht allein.</p>'
        + punkte([("message-square-text", "Story", "Business Storytelling &amp; Gesprächstaktik: Wer sitzt im Raum, und welches Ergebnis wird gebraucht?"),
                  ("presentation", "Folien", "Visualisierung &amp; Nutzung Standards: klare Visualisierung statt Informationsüberladung."),
                  ("refresh-cw", "Alltag", "Begleitung Umsetzung: Anwendung bei echten Themen, abgestimmt auf die Termine Deines Teams.")])
        + '</div>', 2, N)

    module = [
        ("Modul 1", "Mindset",
         "<p>Zu Beginn wird das Verständnis dafür geschärft, wie Entscheider denken, wie sie Themen bewerten und warum in der Praxis viele Kommunikationsthemen nicht das gewünschte Ergebnis erzielen.</p>"
         + ul(["Die drei goldenen Regeln erfolgreicher Gespräche mit Entscheidern", "Nutzenorientierung statt Themenfokus",
               "Erfolgsmuster: „Ich mache meine Zielgruppe erfolgreich“ statt „Ich will überzeugen“"])
         + "<p><b>Ergebnis:</b> Die Teilnehmer haben ein klares strategisches Verständnis davon, wie sie ihr Thema zum Erfolg führen, indem sie den Mehrwert für ihre Zielgruppe in den Mittelpunkt stellen.</p>"),
        ("Modul 2", "Methodik",
         "<p>Eine klare, leicht anwendbare Systematik, um eine Business Story zielgruppengerecht aufzubauen – auch komplexe Inhalte verständlich, fokussiert und logisch. Die Teilnehmer arbeiten aktiv mit ihrem eigenen Thema.</p>"
         + ul(["Die Kernlogik erfolgreicher Business-Storytelling-Bausteine", "Systematischer Aufbau einer storybasierten Argumentation",
               "Übertragung der Struktur auf Präsentation, Videokonferenz, Projektkommunikation"])
         + "<p><b>Ergebnis:</b> Die Teilnehmer können jederzeit zügig und sicher eine überzeugende Business Story aufbauen – unabhängig vom Kommunikationsformat.</p>"),
        ("Modul 3", "Umsetzung",
         "<p>Start und Führung eines Termins: Ein klarer Einstieg und ein präziser nächster Schritt sind entscheidend für Zustimmung und Handlungsbereitschaft.</p>"
         + ul(["Einstiegstechniken mit sofortiger Klarheit", "Die Rolle des nächsten Schritts (psychologische Wirkung von Zielklarheit)", "Story souverän im Termin einsetzen"])
         + "<p><b>Ergebnis:</b> Die Teilnehmer wissen genau, wie sie ihre Präsentation oder ihr Gespräch beginnen und wie sie strukturiert auf ein Ziel hinarbeiten.</p>"),
    ]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Baustein 01 · Story")
        + '<h2>Business Storytelling &amp; <span class="hl">Gesprächstaktik.</span></h2>'
        + '<p class="lead">Dein Team lernt, bei jedem Termin zuerst zu klären: Wer sitzt im Raum, und welches Ergebnis wird gebraucht.</p>'
        + liste(module)
        + '</div>', 3, N)

    arten = [
        ("", "Vortragsfolien",
         "<p>Der Foliensatz für den Auftritt: verdichtet auf Story und Kernbotschaft, sofort erfassbar.</p>"
         + ul(["Fokus auf Story und Kernbotschaften", "Starke Verdichtung, hohe Lesbarkeit, schnelle Erfassbarkeit",
               "Klare Blickführung – funktionierend in Präsenz- und Online-Situationen"])),
        ("", "Beraterfolien",
         "<p>Der Foliensatz für die Projektarbeit: umfangreicher als eine Vortragsfolie, aber trotzdem klar und professionell.</p>"
         + ul(["Projektdokumentationen, Statusberichte, Analysen, Angebotsfolien", "Detaillierter und umfangreicher – aber klar strukturiert und professionell gestaltet",
               "Logische Nachvollziehbarkeit und saubere visuelle Ordnung"])),
    ]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Baustein 02 · Folien")
        + '<h2>Visualisierung &amp; <span class="hl">Nutzung Standards.</span></h2>'
        + '<p class="lead">Aufbauend auf der Business Story aus Baustein 01 überführen wir die Inhalte in professionelle Folien: klare Visualisierung statt Informationsüberladung, '
          'gemessen an Struktur, Aussagekraft und grafischer Qualität.</p>'
        + kicker("Zwei grundlegende Arten von Präsentationen").replace('class="kicker"', 'class="kicker" style="margin-top:10mm"')
        + liste(arten)
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:12mm">' + kicker("Ergebnis")
        + '<p class="lead" style="margin-top:5mm;max-width:150mm">Die Teilnehmer haben das Handwerkszeug und die Sicherheit, um auf Basis einer klaren Business Story schnell professionelle, überzeugende Folien zu erstellen.</p>'
        + '</div>', 4, N, hell_fuss=True)

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Baustein 03 · Alltag · 3–6 Monate")
        + '<h2><span class="hl">Begleitung Umsetzung.</span></h2>'
        + '<p class="lead">Die Seminarinhalte werden konsequent in den Arbeitsalltag überführt. Erfolg entsteht nicht im Training, sondern in der Anwendung bei echten Themen – '
          'individuell abgestimmt auf die konkreten Projekte und Termine Deines Teams.</p>'
        + kicker("Vorgehen – schlank und fokussiert").replace('class="kicker"', 'class="kicker" style="margin-top:10mm"')
        + zeitstrahl([("01", "Auftrag", "Auftrag und Zielbild klären"), ("02", "Storyboard", "Storyboard für das konkrete Thema entwickeln"),
                      ("03", "Präsentation", "Professionelle Präsentation auf Basis der Story erstellen"),
                      ("04", "Termin", "Gesprächstaktik für den Termin festlegen und anwenden"), ("05", "Review", "Anschließendes Review zur Reflexion und Optimierung")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Lernlogik &amp; Erfolgsfaktor")
        + '<h2>Orientierung an der 70-20-10-Regel.</h2>'
        + punkte([("presentation", "10 %", "Impulse im Seminar"), ("users", "20 %", "Kollegialer Austausch und gezielte Begleitung"),
                  ("refresh-cw", "70 %", "Lernen durch Anwendung an echten, relevanten Themen")])
        + ergebnis(("Die Teilnehmer setzen die Inhalte sicher bei echten Themen um, entwickeln klare Stories und professionelle Präsentationen und gehen strukturiert in entscheidende Termine."), "9mm")
        + '</div>', 5, N)

    phasen = [
        ("01", "Onboarding", "2–3 Std., online · Onboarding der Teilnehmer als Onlineveranstaltung.",
         ["Einführung in die theoretischen Grundlagen", "Vermittlung zentraler Kernbotschaften", "Gemeinsame Erarbeitung der zentralen Methodik zur Strukturierung einer Präsentation"]),
        ("02", "Vorbereitung", "2–3 Wochen · Vorbereitungsphase vor den beiden Seminartagen.",
         ["Vorbereitung einer Präsentation durch die Teilnehmer für das Seminar", "Sammlung von Fragestellungen", "Zusendung der Präsentation an empiria",
          "Analyse der zugesandten Präsentationen durch empiria"]),
        ("03", "Training", "2 Tage, Präsenz · Praxistraining, aufbauend auf dem Input des Onboardings sowie der vorbereiteten Praxisthemen.",
         ["Wiederholung und Vertiefung der theoretischen Grundlagen", "Anwendung der Methoden auf die vorbereiteten Praxisthemen", "Diskussion und Optimierungen"]),
        ("04", "Anwendung", "3–6 Monate, individuell · Weiterentwicklung und Anwendung der Präsentationen in der Praxis.",
         ["Gezielte Vorbereitung von Praxisthemen und Anwendung der Präsentationen", "Klärung von Rückfragen mit empiria",
          "Optimierung und Anpassung von Präsentationen", "Regelmäßige Reviews (online)"]),
    ]
    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>Vom Onboarding bis <span class="hl">in den Alltag.</span></h2>'
        + '<p class="lead">Kurz vorbereiten, intensiv trainieren – und dann über Monate dort begleiten, wo es zählt: bei Deinen echten Terminen.</p>'
        + zeitstrahl([(n, t, f"{d}</p>{ul(l)}<p hidden>") for n, t, d, l in phasen])
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:12mm">' + kicker("Das Ergebnis")
        + '<h2>Dein Team überzeugt <span class="hl">ohne Dich.</span></h2>'
        + '<p class="lead">Dein Team bereitet Themen so auf, dass sie überzeugen, und tritt sicher auf, wenn es zählt. Du bekommst Ergebnisse, mit denen Du wirklich arbeiten kannst.</p>'
        + '</div>', 6, N, hell_fuss=True)

    s7 = seite(kopf(T) + schluss('Bereit, Dein Team <span class="hl">überzeugend auftreten</span> zu lassen?',
                                 "Wir arbeiten an echten Themen aus Eurem Alltag: dem nächsten Kundenpitch, dem nächsten Gespräch mit dem Rückversicherer, der nächsten wichtigen Abstimmungsrunde im eigenen Haus.",
                                 ["daniel", "kerstin_hr"]), 7, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
