"""PDF „Teams befähigen, professionell zu kommunizieren“ – im Muster „KI zum Anfassen“ (10.10.2026)."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Teams befähigen, professionell zu kommunizieren – empiria"
T = "Teams befähigen"
N = 7


CSS = """
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p, .sub, .text, .reihe > div { text-wrap: pretty; }
.reihe { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; margin-top: 9mm; }
.reihe > div { border-top: 1.6px solid #1a1817; padding-top: 4mm; font-size: 9.6pt; line-height: 1.55; }
.text { font-size: 9.6pt; line-height: 1.6; margin-top: 7mm; max-width: 150mm; }
.satz { font-size: 9.6pt; line-height: 1.6; margin-top: 9mm; max-width: 150mm; }
.punkte h3 { min-height: 3.6em; }
.punkte small { display: block; font-family: 'Poppins', Arial, sans-serif; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.5mm; }
.liste .unter { display: block; font-family: 'Poppins', Arial, sans-serif; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.6mm; }
.liste ul { list-style: none; margin-top: 2.4mm; }
.liste li { position: relative; padding-left: 4mm; margin-top: 1mm; font-size: 8.6pt; line-height: 1.5; color: #1a1817; }
.liste li::before { content: ""; position: absolute; left: 0; top: 1.9mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1a1817; }
.arten { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; margin-top: 10mm; }
.art { background: #fff; border: 1px solid #dcd8d1; border-radius: 4.5mm; padding: 8mm 7.5mm 9mm; }
.art svg { width: 9mm; height: 9mm; margin-bottom: 4mm; }
.art h3 { font-size: 15pt; }
.art > p { margin-top: 2.5mm; font-size: 9.6pt; line-height: 1.6; color: #3d3a37; min-height: 4.8em; }
.art ul { list-style: none; margin-top: 5mm; padding-top: 4mm; border-top: 1px solid #ece9e5; }
.art li { position: relative; padding-left: 4.5mm; margin-top: 2.6mm; font-size: 9.2pt; line-height: 1.5; }
.art li::before { content: ""; position: absolute; left: 0; top: 2.1mm; width: 1.4mm; height: 1.4mm; border-radius: 50%; background: #1a1817; }
.anteile { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; margin-top: 7mm; }
.anteile > div { border-top: 1.6px solid #1a1817; padding-top: 4mm; }
.anteile b { display: block; font-family: 'Lora', Georgia, serif; font-size: 34pt; line-height: 1; }
.anteile span { display: block; margin-top: 2.5mm; font-size: 9pt; line-height: 1.5; }
.band--schwarz .hl { color: #1a1817; }
.zs--klein h3 { font-size: 10.5pt; line-height: 1.25; }
.zs--klein li { padding-right: 4mm; }
.zs--phasen h3 { min-height: 1.2em; }
.zs--phasen .dauer { display: block; margin-top: 1mm; font-size: 7.6pt; font-weight: 600; }
.zs--phasen ul { list-style: none; margin-top: 3mm; }
.zs--phasen li li { position: relative; padding: 0 0 0 3.6mm; margin-top: 1.6mm; font-size: 8.4pt; line-height: 1.45; }
.zs--phasen li li::before { content: ""; position: absolute; left: 0; top: 1.8mm; width: 1.3mm; height: 1.3mm; border-radius: 50%; background: #1a1817; }
"""


def ergebnis(text, mt="9mm"):
    return (f'<div class="kasten" style="margin-top:{mt};padding:6.5mm 8mm 7mm"><p class="label">Ergebnis</p>'
            f'<p style="font-size:9.6pt;color:#fff">{text}</p></div>')


def bauen():
    s1 = seite(titelseite(
        "Befähigung und Begleitung, kein Seminar", 'Teams befähigen, professionell zu <span class="hl">kommunizieren.</span>',
        "Du bist Führungskraft in der Versicherungsbranche und Dein Team bereitet Themen und Präsentationen vor, die nicht überzeugen? "
        "Dann braucht es kein Seminar, sondern Begleitung bei der Umsetzung.",
        kopfbild("Teams befähigen, professionell zu kommunizieren"),
        [("Onboarding", "2–3 Std., online"), ("Training", "2 Tage, Präsenz"), ("Begleitung", "3–6 Monate"), ("Bausteine", "Story, Folien, Alltag")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:14mm">' + kicker("Das Problem")
        + '<h2>Dein Team bereitet vor. Und erreicht das Ziel <span class="hl">trotzdem nicht.</span></h2>'
        + '<div class="reihe"><div>Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft ins Leere.</div>'
          '<div>Dein Team präsentiert im Lenkungsausschuss oder beim Kunden – und hinterher denkst Du: Das hätte besser laufen müssen.</div>'
          '<div>Die Story trägt nicht, die Unterlagen überzeugen nicht und im Raum fehlt die Souveränität, auf Fragen zu reagieren.</div></div>'
        + '<p class="text"><b>Es wird Zeit, bisherige Denkmuster mit einfachen Logiken zu durchbrechen.</b></p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Befähigung und Begleitung<br>bei der Umsetzung.</h2>'
        + '<p class="lead">Wir bringen Deinem Team bei, wie das geht – und lassen es danach nicht allein.</p>'
        + punkte([("message-square-text", "<small>Baustein 01 · Story</small>Storytelling &amp; Gesprächstaktik", "Bei jedem Termin zuerst klären: Wer sitzt im Raum, und welches Ergebnis wird gebraucht?"),
                  ("presentation", "<small>Baustein 02 · Folien</small>Visualisierung &amp; Standards", "Klare Visualisierung statt Informationsüberladung – aufbauend auf der Business Story."),
                  ("refresh-cw", "<small>Baustein 03 · Alltag</small>Umsetzungs&shy;begleitung", "Anwendung bei echten Themen – abgestimmt auf die Projekte und Termine Deines Teams.")])
        + '<p class="satz">Wir arbeiten an echten Themen aus Eurem Alltag: dem nächsten Kundenpitch, dem nächsten Gespräch mit dem Rückversicherer, der nächsten wichtigen Abstimmungsrunde im eigenen Haus.</p>'
        + '</div>', 2, N)

    module = [
        ("Modul 1", "Mindset", "Wie Entscheider denken, wie sie Themen bewerten – und warum viele Kommunikationsthemen in der Praxis nicht das gewünschte Ergebnis erzielen.",
         ["Die drei goldenen Regeln erfolgreicher Gespräche mit Entscheidern", "Nutzenorientierung statt Themenfokus", "„Ich mache meine Zielgruppe erfolgreich“ statt „Ich will überzeugen“"]),
        ("Modul 2", "Methodik", "Eine klare, leicht anwendbare Systematik, um eine Business Story zielgruppengerecht aufzubauen. Die Teilnehmer arbeiten dabei direkt an ihrem eigenen Thema.",
         ["Die Kernlogik erfolgreicher Business-Storytelling-Bausteine", "Systematischer Aufbau einer storybasierten Argumentation", "Übertragung auf Präsentation, Videokonferenz, Projektkommunikation"]),
        ("Modul 3", "Umsetzung", "Start und Führung eines Termins: Ein klarer Einstieg und ein präziser nächster Schritt sind entscheidend für Zustimmung und Handlungsbereitschaft.",
         ["Einstiegstechniken mit sofortiger Klarheit", "Die Rolle des nächsten Schritts", "Story souverän im Termin einsetzen"]),
    ]
    s3 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Baustein 01 · Story")
        + '<h2>Business Storytelling &amp; <span class="hl">Gesprächstaktik.</span></h2>'
        + '<p class="lead">Dein Team lernt, bei jedem Termin zuerst zu klären: Wer sitzt im Raum, und welches Ergebnis wird gebraucht.</p>'
        + '<div class="liste">' + "".join(f'<div><h3><span class="unter">{u}</span>{t}</h3><div><p>{p}</p><ul>{"".join(f"<li>{x}</li>" for x in l)}</ul></div></div>' for u, t, p, l in module) + '</div>'
        + ergebnis("Die Teilnehmer haben ein klares strategisches Verständnis davon, wie sie ihr Thema zum Erfolg führen, zügig und sicher eine überzeugende Business Story aufbauen und professionell durch den Termin leiten.")
        + '</div>', 3, N)

    s4 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Baustein 02 · Folien")
        + '<h2>Visualisierung &amp; <span class="hl">Nutzung Standards.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Aufbauend auf der Business Story aus Baustein 01 überführen wir die Inhalte in professionelle Folien: klare Visualisierung statt Informationsüberladung, '
          'gemessen an Struktur, Aussagekraft und grafischer Qualität.</p>'
        + '<p class="text" style="margin-top:9mm">Dabei unterscheiden wir zwei grundlegende Arten von Präsentationen.</p>'
        + '<div class="arten" style="margin-top:5mm">'
        + '<div class="art">' + __import__("lib").ico("presentation") + '<h3>Vortragsfolien</h3><p>Der Foliensatz für den Auftritt: verdichtet auf Story und Kernbotschaft, sofort erfassbar.</p>'
          '<ul><li>Fokus auf Story und Kernbotschaften</li><li>Starke Verdichtung, hohe Lesbarkeit, schnelle Erfassbarkeit</li><li>Klare Blickführung – in Präsenz- und Online-Situationen</li></ul></div>'
        + '<div class="art">' + __import__("lib").ico("file-text") + '<h3>Beraterfolien</h3><p>Der Foliensatz für die Projektarbeit: umfangreicher als eine Vortragsfolie, aber trotzdem klar und professionell.</p>'
          '<ul><li>Projektdokumentationen, Statusberichte, Analysen, Angebotsfolien</li><li>Detaillierter – aber klar strukturiert und professionell gestaltet</li><li>Logische Nachvollziehbarkeit und saubere visuelle Ordnung</li></ul></div>'
        + '</div>'
        + ergebnis("Die Teilnehmer haben das Handwerkszeug und die Sicherheit, um auf Basis einer klaren Business Story schnell professionelle, überzeugende Folien zu erstellen.", "10mm")
        + '</div>', 4, N, klasse="seite--hell")

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Baustein 03 · Alltag · 3–6 Monate")
        + '<h2>Umsetzungs&shy;begleitung.</h2>'
        + '<p class="lead" style="max-width:150mm">Erfolg entsteht nicht im Training, sondern in der Anwendung bei echten Themen – individuell abgestimmt auf die konkreten Projekte und Termine Deines Teams.</p>'
        + '<p class="text" style="margin-top:10mm"><b>Vorgehen in der Umsetzungsbegleitung – schlank und fokussiert</b></p>'
        + zeitstrahl([("01", "Auftrag und Zielbild klären", ""), ("02", "Storyboard für das Thema entwickeln", ""),
                      ("03", "Präsentation auf Basis der Story erstellen", ""), ("04", "Gesprächstaktik festlegen und anwenden", ""),
                      ("05", "Review zur Reflexion und Optimierung", "")]).replace('class="zs"', 'class="zs zs--klein"').replace("<p></p>", "")
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:13mm">' + kicker("Lernlogik &amp; Erfolgsfaktor")
        + '<h2>Orientierung an der 70-20-10-Regel.</h2>'
        + '<div class="anteile"><div><b>10 %</b><span>Impulse im Seminar</span></div><div><b>20 %</b><span>Kollegialer Austausch und gezielte Begleitung</span></div>'
          '<div><b>70 %</b><span>Lernen durch Anwendung an echten, relevanten Themen</span></div></div>'
        + ergebnis("Die Teilnehmer setzen die Inhalte sicher bei echten Themen um, entwickeln klare Stories und professionelle Präsentationen und gehen strukturiert in entscheidende Termine.", "10mm")
        + '</div>', 5, N)

    phasen = [("01", "Onboarding", "2–3 Std., online", ["Einführung in die theoretischen Grundlagen", "Vermittlung zentraler Kernbotschaften", "Gemeinsame Erarbeitung der Methodik zur Strukturierung einer Präsentation"]),
              ("02", "Vorbereitung", "2–3 Wochen", ["Teilnehmer bereiten eine Präsentation für das Seminar vor", "Sammlung von Fragestellungen", "Analyse der zugesandten Präsentationen durch empiria"]),
              ("03", "Training", "2 Tage, Präsenz", ["Wiederholung und Vertiefung der Grundlagen", "Anwendung der Methoden auf die vorbereiteten Praxisthemen", "Diskussion und Optimierungen"]),
              ("04", "Anwendung", "3–6 Monate, individuell", ["Gezielte Vorbereitung von Praxisthemen", "Klärung von Rückfragen mit empiria", "Optimierung und Anpassung von Präsentationen", "Regelmäßige Reviews (online)"])]
    zs = ('<ol class="zs zs--phasen" style="grid-template-columns:repeat(4,1fr)">' + "".join(
        f'<li><span class="punkt"></span><span class="nr">{n}</span><h3>{t}</h3><span class="dauer">{d}</span><ul>{"".join(f"<li>{x}</li>" for x in p)}</ul></li>' for n, t, d, p in phasen) + '</ol>')
    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>Vom Onboarding bis <span class="hl">in den Alltag.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Kurz vorbereiten, intensiv trainieren – und dann über Monate dort begleiten, wo es zählt: bei Deinen echten Terminen.</p>'
        + zs
        + '</div><div class="band band--schwarz wachsen mitte" style="margin-top:16mm">' + kicker("Das Ergebnis")
        + '<h2 style="color:#fff;font-size:34pt;margin-top:5mm">Dein Team überzeugt<br><span class="hl">ohne Dich.</span></h2>'
        + '<p class="lead" style="color:rgba(255,255,255,.85);max-width:150mm">Dein Team bereitet Themen so auf, dass sie überzeugen, und tritt sicher auf, wenn es zählt. Du bekommst Ergebnisse, mit denen Du wirklich arbeiten kannst.</p>'
        + '</div>', 6, N, hell_fuss=True)

    s7 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit, Dein Team<br><span class="hl">überzeugend auftreten</span> zu lassen?</h2>'
        + '<p class="lead">Schildere uns, wo Dein Team heute steht und vor welchen Terminen es steht – wir schlagen ein passendes Begleitungskonzept vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 7, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
