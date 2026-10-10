"""PDF „Training & Sparring“ – Runde 3 (10.10.2026): Übersichts-PDF mit einem Kapitel je Unterseite.
Quellen: site/projekte/empiria-2/training-sparring.html (Übersicht, maßgeblich) sowie die beiden dort verlinkten Unterseiten
praesentationsseminar.html (Kapitel 01, inkl. „Module & Ergebnis“-Dialoge und Zeitplan) und sparring.html (Kapitel 02).
Impulsvorträge sind auf der Seite nur im Menü verlinkt, nicht als Format – deshalb kein eigenes Kapitel.
Keine Preise: Weder die Übersicht noch die Unterseiten nennen welche.
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument, ico)
from _strategie_teile import LISTE_CSS

TITEL = "Training & Sparring – empiria"
T = "Training &amp; Sparring"
N = 7

CSS = LISTE_CSS + """
.tabelle--zwei .zeile { width: 34mm; }
.tabelle--zwei { margin-top: 4mm; }
.tabelle--zwei thead th { padding-top: 1mm; padding-bottom: 2mm; }
.tabelle--zwei td { padding-top: 2.4mm; padding-bottom: 2.4mm; }
.tabelle--zwei th:nth-child(2), .tabelle--zwei td:nth-child(2) { width: 72mm; }
.tabelle--zwei td { font-size: 9pt; }
.kap { display: flex; align-items: flex-end; gap: 5mm; margin-bottom: 5mm; }
.kap__nr { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 44pt; line-height: .8; letter-spacing: -.02em; }
.kap__linie { flex: 1; height: 1.6px; background: #1a1817; margin-bottom: 1.2mm; }
.kapkopf-alt { display: flex; align-items: flex-end; gap: 5mm; padding-bottom: 4mm; border-bottom: 1.6px solid #1a1817; margin-bottom: 7mm; }
.kapnr { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 50pt; line-height: .8; letter-spacing: -.02em; }
.kapkopf .kicker { margin-bottom: .6mm; }
.ohne-icon svg { display: none; }
.ohne-icon > div { padding-top: 3.6mm; }
.ohne-icon p { margin-top: 0; }
.liste small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 1.6mm; }
.modliste > div { padding: 3.4mm 0; }
.band--hell .notiz { margin-top: 3.5mm; }
.liste .erg { margin-top: 1.8mm; color: #1a1817; }
.wann { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 5mm; }
.wann > div { border-top: 1.6px solid #1a1817; padding-top: 3.6mm; display: flex; align-items: center; gap: 2.6mm; }
.wann svg { width: 5.6mm; height: 5.6mm; flex: 0 0 auto; }
.wann b { font-family: 'Lora', Georgia, serif; font-size: 10pt; line-height: 1.2; display: block; }
.ueber { margin-top: 5mm; columns: 2; column-gap: 9mm; list-style: none; border-top: 1.6px solid #1a1817; }
.ueber li { break-inside: avoid; position: relative; padding: 1.5mm 0 1.5mm 7mm; border-bottom: 1px solid #dcd8d1; font-size: 9.2pt; line-height: 1.45; }
.ueber li::before { content: ""; position: absolute; left: 0; top: 3.9mm; width: 3mm; height: 1.6mm; border-left: 1.6px solid #1a1817; border-bottom: 1.6px solid #1a1817; transform: rotate(-45deg); }
.turbo .punkte > div { display: flex; align-items: center; gap: 3.5mm; padding-top: 4mm; }
.turbo .punkte svg { margin: 0; flex: 0 0 auto; width: 6mm; height: 6mm; color: #fff400; }
.turbo .punkte h3 { font-size: 11pt; line-height: 1.3; color: #fff; }
.turbo h2 { color: #fff; }
.turbo .lead { color: rgba(255,255,255,.85); max-width: 165mm; }
.turbo .schluss { margin-top: 6mm; display: grid; grid-template-columns: 1fr 1fr; gap: 9mm; }
.turbo .schluss p { font-size: 9.2pt; line-height: 1.6; color: rgba(255,255,255,.82); }
.turbo .schluss p b { color: #fff; font-weight: 600; }
.turbo .notiz { color: rgba(255,255,255,.55); margin-top: 4mm; }
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p { text-wrap: pretty; }
"""


def kapitel(nr, name, h2, lead):
    """Kapitel-Einstieg: große Nummer, Kicker = Name der Unterseite, H2 = Kopfzeile, Lead = Kopftext."""
    return (f'<div class="kap"><span class="kap__nr">{nr}</span><span class="kap__linie"></span></div>' + kicker(name) + f'<h2>{h2}</h2>'
            + f'<p class="lead" style="max-width:150mm">{lead}</p>')


def notiz(name):
    return f'<p class="notiz">Alle Details: eigenes PDF „{name}“ auf empiria.de</p>'


def bauen():
    s1 = seite(titelseite(
        "Training &amp; Sparring", 'Begleitung,<br><span class="hl">die wirkt.</span><br>Bis in den Alltag.',
        "Für Dein Team als Trainingsbegleitung, für Dich als Führungskraft im vertraulichen Sparring.",
        kopfbild("Training & Sparring"),
        [("Kapitel 01", "Teams befähigen"), ("Kapitel 02", "1:1 Sparring"), ("Branche", "Versicherungen")]))

    # ---------- Ansatz + Überblick ----------
    def zeile(label, a, b):
        return f'<tr><td class="zeile">{label}</td><td>{a}</td><td>{b}</td></tr>'
    tabelle = ('<table class="tabelle tabelle--zwei"><thead><tr><th></th>'
               '<th><small>Kapitel 01</small><b>Teams befähigen</b></th><th><small>Kapitel 02</small><b>1:1 Sparring</b></th></tr></thead><tbody>'
               + zeile("Kurz gesagt", "Dein Team bereitet Themen vor, die nicht überzeugen? Wir bringen ihm bei, wie es geht – und begleiten es dabei, wenn es zählt.",
                       "Strategisches Sparring auf Augenhöhe für Führungskräfte in der Versicherungsbranche – vertraulich, erfahren und mit klarer Rückmeldung.")
               + zeile("Für wen", "Führungskräfte und ihre Teams, die Themen und Präsentationen vorbereiten", "Vorstandsmitglieder und Führungskräfte – von der Abteilung bis zum Vorstand")
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
        + '</div><div class="rand" style="padding-top:8mm">' + kicker("Überblick")
        + '<h2>Zwei Formate. Ein Ziel: Wirkung im Alltag.</h2>'
        + '<p class="lead">Wähle das Format – wir passen es auf Dich an.</p>'
        + tabelle
        + '</div>', 2, N)

    # ---------- Kapitel 01 · Teams befähigen ----------
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("01", "Teams befähigen", 'Teams befähigen, professionell zu <span class="hl">kommunizieren.</span>',
                  "Du bist Führungskraft in der Versicherungsbranche und Dein Team bereitet Themen und Präsentationen vor, die nicht überzeugen?")
        + kicker("Das Problem").replace('class="kicker"', 'class="kicker" style="margin-top:9mm"')
        + punkte([("presentation", "", "Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft ins Leere."),
                  ("users", "", "Dein Team präsentiert im Lenkungsausschuss oder beim Kunden – und hinterher denkst Du: Das hätte besser laufen müssen."),
                  ("message-square-text", "", "Die Story trägt nicht, die Unterlagen überzeugen nicht und im Raum fehlt die Souveränität, auf Fragen zu reagieren.")]).replace("<h3></h3>", "").replace('class="punkte"', 'class="punkte ohne-icon"', 1)
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:11mm;padding-top:12mm">' + kicker("Die Lösung")
        + '<h2>Befähigung und Begleitung<br>bei der Umsetzung.</h2>'
        + '<p class="lead">Wir bringen Deinem Team bei, wie das geht – und lassen es danach nicht allein.</p>'
        + punkte([("briefcase", "An echten Themen", "Wir arbeiten an echten Themen aus Eurem Alltag: dem nächsten Kundenpitch, dem nächsten Gespräch mit dem Rückversicherer, der nächsten wichtigen Abstimmungsrunde im eigenen Haus."),
                  ("calendar", "Genau dann, wenn es zählt", "Vor dem Termin, beim letzten Schliff, danach beim Analysieren, was gut lief und was nicht – genau dann sind wir da. So baut sich etwas auf, das ein einzelnes Seminar nie schafft.")], 2)
        + '</div>', 3, N)

    bausteine = [
        ("Baustein 01 · Story", "Business Storytelling &amp; Gesprächstaktik",
         "Mindset, Methodik, Umsetzung: wie Entscheider denken, wie eine Business Story zielgruppengerecht aufgebaut wird und wie ein Termin startet und geführt wird.",
         "Dein Team baut zügig und sicher eine überzeugende Business Story auf und leitet professionell durch den Termin."),
        ("Baustein 02 · Folien", "Visualisierung &amp; Nutzung Standards",
         "Aus der Business Story entstehen professionelle Folien – Vortragsfolien für den Auftritt und Beraterfolien für die Projektarbeit.",
         "Dein Team erstellt auf Basis einer klaren Story schnell professionelle, überzeugende Folien."),
        ("Baustein 03 · Alltag", "Umsetzungsbegleitung",
         "3–6 Monate an echten Themen, nach der 70-20-10-Regel: Auftrag klären, Storyboard, Präsentation, Gesprächstaktik für den Termin, anschließendes Review.",
         "Dein Team setzt die Inhalte sicher bei echten Themen um und geht strukturiert in entscheidende Termine."),
    ]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Module &amp; Ergebnis")
        + '<h2>Drei Bausteine: <span class="hl">Story, Folien, Alltag.</span></h2>'
        + '<div class="liste modliste">' + "".join(f'<div><div><small>{k}</small><h3>{t}</h3></div><div><p>{p}</p><p class="erg"><b>Ergebnis:</b> {e}</p></div></div>'
                                          for k, t, p, e in bausteine) + '</div>'
        + '</div><div class="band band--hell wachsen" style="margin-top:8mm;padding-top:9mm;padding-bottom:20mm">' + kicker("Ablauf")
        + '<h2>Vom Onboarding bis <span class="hl">in den Alltag.</span></h2>'
        + '<div style="margin-top:-3mm">' + zeitstrahl([("01", "Onboarding", "2–3 Std., online"), ("02", "Vorbereitung", "2–3 Wochen"),
                      ("03", "Training", "2 Tage, Präsenz"), ("04", "Anwendung", "3–6 Monate, individuell")]) + '</div>'
        + '<div class="kasten" style="margin-top:7mm"><div class="zwei" style="grid-template-columns:1fr 1.25fr"><div><p class="label">Das Ergebnis</p><h3>Dein Team überzeugt ohne Dich.</h3></div>'
        + '<p style="margin-top:0">Dein Team bereitet Themen so auf, dass sie überzeugen, und tritt sicher auf, wenn es zählt. Du bekommst Ergebnisse, mit denen Du wirklich arbeiten kannst.</p></div></div>'
        + notiz("Teams befähigen, professionell zu kommunizieren")
        + '</div>', 4, N)

    # ---------- Kapitel 02 · 1:1 Sparring ----------
    s5 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("02", "1:1 Sparring", 'Offen sprechen. <span class="hl">Klar entscheiden.</span><br>Volle Wirkung.',
                  "Seit vielen Jahren begleite ich Vorstandsmitglieder und Führungskräfte vertrauensvoll bei strategischen Themen, "
                  "Ideen zum Geschäftsmodell oder Führungsfragen.")
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Das bekommst Du")
        + '<h2>Ein Gegenüber, das mitdenkt<br>und mitgestaltet.</h2>'
        + punkte([("lock", "Offen &amp; vertraulich", "Ein Raum, in dem Themen wirklich offen besprochen werden können – ohne interne Rücksichten."),
                  ("star", "Erfahrung, die trägt", "Viele Jahre Sparring mit Vorstandsmitgliedern, Hauptabteilungs- und Abteilungsleitern in der Versicherungsbranche."),
                  ("eye", "Mehrere Perspektiven", "Komplexe Situationen werden aus unterschiedlichen Blickwinkeln betrachtet – für Lösungswege, die wirklich passen.")])
        + punkte([("compass", "Klarheit &amp; Handlungs&shy;sicherheit", "Am Ende steht nicht nur eine Einschätzung, sondern eine Richtung, mit der sich weiterarbeiten lässt."),
                  ("rocket", "Vom Gespräch zur Umsetzung", "Wenn es ans Vorantreiben geht, entsteht daraus schnell ein einsatzbereites Konzept – kommunikativ oder inhaltlich."),
                  ("megaphone", "Schlagkräftig nach außen", "Ob gegenüber dem Vorstand oder anderen Bereichen: Sparring macht Positionierung und Auftreten sichtbar stärker.")])
        + '</div>', 5, N)

    wann = [("users", "Persönliches Treffen"), ("map-pin", "Offsite"), ("car", "Telefonat aus dem Auto"), ("message-circle", "Kurznachricht")]
    ueber = ["Strategische Themen und Geschäftsmodellfragen", "Führungsfragen", "Betrachtung komplexer Situationen aus unterschiedlichen Perspektiven",
             "Abwägen von Lösungswegen und Vorgehensweisen", "Positionierung gegenüber Vorstand und anderen Bereichen", "Umgang mit dem Aufsichtsrat",
             "Steuerung von Konzernunternehmen", "Konzeption von Kommunikation nach außen", "… und vieles mehr"]
    s6 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Themen")
        + '<h2>So flexibel, wie es <span class="hl">für Dich passt.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Der Alltag hält sich oftmals nicht an planbare Termine. Ich richte mich immer danach, wie es für Dich als Führungskraft passt. '
          'Oftmals ist ein kurzer Austausch genauso hilfreich wie ein strukturierter Termin – bei Bedarf auch zu Randzeiten.</p>'
        + '<p class="kicker" style="margin-top:7mm">Wann wir sprechen</p>'
        + '<div class="wann">' + "".join(f'<div>{ico(i)}<b>{t}</b></div>' for i, t in wann) + '</div>'
        + '<p class="kicker" style="margin-top:7mm">Worüber wir sprechen</p>'
        + '<ul class="ueber">' + "".join(f"<li>{x}</li>" for x in ueber) + '</ul>'
        + '</div><div class="band band--schwarz wachsen turbo" style="margin-top:8mm;padding-top:9mm">' + kicker("Mehr als nur Sparring")
        + '<h2>Umsetzungsturbo!</h2>'
        + '<p class="lead">In unseren Gesprächen entstehen oft Ideen, die Du am liebsten sofort vorantreiben würdest. '
          'Dabei fehlt intern meist immer einer der drei Erfolgsbausteine:</p>'
        + '<div class="punkte" style="margin-top:6mm;grid-template-columns:repeat(3,1fr)">' + "".join(
            f'<div style="border-color:rgba(255,255,255,.35)">{ico(i)}<h3>{t}</h3></div>' for i, t in
            [("user-round", "Jemand, der das Thema versteht"), ("timer", "Die Kapazität für die Umsetzung"), ("wrench", "Die Skills für die Umsetzung")]) + '</div>'
        + '<div class="schluss"><p>Genau hier finde ich oftmals direkt eine Lösung, wie es schnell gehen kann. Ganz ohne weiteres Briefing, '
          'denn wir kennen die Hintergründe bereits aus dem Sparring.</p>'
          '<p><b>Wir liefern das Ergebnis:</b> Egal, ob wir es komplett konzipieren und erstellen oder Dein Team direkt mit einbinden.</p></div>'
        + notiz("Sparring für Führungskräfte")
        + '</div>', 6, N, hell_fuss=True)

    # ---------- Schluss ----------
    s7 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Begleitung, <span class="hl">die wirklich weiterbringt?</span></h2>'
        + '<p class="lead">Sag uns, ob es um Dein Team oder um Dich geht – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es wirken? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 7, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
