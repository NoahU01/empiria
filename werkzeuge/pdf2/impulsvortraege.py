"""PDF „Impulsvorträge“ im Muster KI zum Anfassen – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/impulsvortraege.html (Aufbau, Überschriften, Kopftexte), dazu die Seiten hinter
„Mehr erfahren“ (site/vortrag-1..3.html: Kopftext und drei Merkmale je Vortrag) und als Sonderthema
„Strategie für Aufsichtsräte“ (site/strategie-aufsichtsrat.html bzw. P["strategie-fuer-aufsichtsraete"], verdichtet).
"""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, check, dokument)

TITEL = "Impulsvorträge – empiria"
T = "Impulsvorträge"
N = 5

CSS = """
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p, .sub { text-wrap: pretty; }
/* Vorträge: Liste wie beispiele_liste, rechts Kopftext + die drei Merkmale der Vortragsseite */
.liste small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-bottom: 1.6mm; }
.liste > div { padding: 6.6mm 0 7mm; }
.merkmale { list-style: none; display: grid; grid-template-columns: repeat(3, 1fr); gap: 4.5mm; margin-top: 3.6mm; }
.merkmale li { border-top: 1.2px solid #1a1817; padding-top: 2mm; font-size: 8pt; line-height: 1.45; color: #3d3a37; }
.merkmale b { display: block; font-family: 'Lora', Georgia, serif; font-size: 9.6pt; color: #1a1817; margin-bottom: .6mm; }
/* Anlässe */
.anlaesse .check li { font-size: 10.4pt; padding-top: 3.6mm; padding-bottom: 3.6mm; }
.anlaesse .check li::before { top: 5.6mm; }
/* Sonderthema-Band (schwarz): Zeitstrahl, Fakten und Haken auf Schwarz */
.band--schwarz .hl { color: #1a1817; }
.band--schwarz .lead { color: rgba(255,255,255,.85); }
.band--schwarz .zs::before { background: rgba(255,255,255,.4); }
.band--schwarz .zs .punkt { background: #fff400; box-shadow: 0 0 0 1.2mm #1a1817; }
.band--schwarz .zs .nr { color: #fff400; }
.band--schwarz .zs p { color: rgba(255,255,255,.8); }
.band--schwarz .check li { border-color: rgba(255,255,255,.22); color: rgba(255,255,255,.9); }
.band--schwarz .check li::before { border-color: #fff400; }
.ar-fakten { display: grid; grid-template-columns: repeat(4, 1fr); gap: 0; margin-top: 8mm; padding-top: 4mm; border-top: 1.6px solid rgba(255,255,255,.4); }
.ar-fakten > div { padding-right: 6mm; }
.ar-fakten span { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }
.ar-fakten b { display: block; margin-top: 1.2mm; font-family: 'Lora', Georgia, serif; font-size: 11pt; line-height: 1.25; }
.band--schwarz .zs { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
.ar-ziel { margin-top: 9mm; }
.ar-ziel p + p { margin-top: 2mm; }
.ar-ziel .label { font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #fff400; }
.ar-ziel p { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 13pt; line-height: 1.35; color: #fff; }
.ar-unten { display: grid; grid-template-columns: 1fr 1fr; gap: 9mm; margin-top: 10mm; padding-top: 7mm; border-top: 1px solid rgba(255,255,255,.22); }
.ar-unten .label { font-size: 6.8pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; color: #fff400; }
.ar-unten h3 { color: #fff; font-size: 13pt; margin-top: 2mm; }
.ar-unten p { margin-top: 2.5mm; font-size: 8.8pt; line-height: 1.6; color: rgba(255,255,255,.82); }
.ar-unten .check { grid-template-columns: 1fr; gap: 0; margin-top: 2mm; }
.ar-unten .check li { font-size: 8.8pt; padding-top: 1.9mm; padding-bottom: 1.9mm; }
.ar-unten .check li::before { top: 3.6mm; }
"""

# Kopftexte und Merkmale wörtlich von den Vortragsseiten (vortrag-1..3.html)
VORTRAEGE = [
    ("Relevanz", "Warum sich niemand für Dein Produkt interessiert.",
     "Ein wachrüttelnder Impuls darüber, warum Qualität allein nicht überzeugt – und was ein Produkt wirklich braucht, "
     "damit es gehört, verstanden und gewollt wird.",
     [("Ehrlich", "Kein Motivations-Bla-Bla – eine klare Analyse, warum Botschaften verpuffen."),
      ("Nah dran", "Beispiele aus echten Projekten statt austauschbarer Theorie."),
      ("Umsetzbar", "Mit konkreten Ansatzpunkten, die am nächsten Tag im Job funktionieren.")]),
    ("Strategie im Alltag", "Strategie, die endlich ankommt.",
     "Die beste Strategie nützt nichts, wenn sie in der Schublade landet. Dieser Vortrag zeigt, wie Strategie so kommuniziert wird, "
     "dass sie im Alltag Deines Teams tatsächlich ankommt – und wirkt.",
     [("Verständlich", "Strategie in einer Sprache, die jede Ebene im Unternehmen versteht."),
      ("Verankert", "Zeigt, wie aus Folien echte Entscheidungen im Alltag werden."),
      ("Mitreißend", "Macht Strategie greifbar statt abstrakt – und schafft echte Zustimmung.")]),
    ("Perspektivwechsel", "Gründe Deinen stärksten Konkurrenten!",
     "Ein provokanter Perspektivwechsel: Was, wenn Du selbst der schärfste Angreifer auf Dein eigenes Geschäftsmodell wärst? "
     "Dieser Vortrag deckt blinde Flecken auf, bevor es jemand anders tut.",
     [("Provokant", "Stellt bequeme Wahrheiten über das eigene Geschäftsmodell infrage."),
      ("Konkret", "Ein Denkwerkzeug, das Teams direkt selbst anwenden können."),
      ("Wachrüttelnd", "Macht sichtbar, wo Angriffsfläche entsteht – bevor es teuer wird.")]),
]


def bauen():
    s1 = seite(titelseite(
        T, 'Impulse,<br><span class="hl">die nachwirken.</span><br>Nicht nur unterhalten.',
        "Drei Vorträge aus echter Beratungserfahrung – für den Moment, in dem ein Impuls mehr bewirken soll als ein weiterer Foliensatz.",
        kopfbild("Impulsvorträge"),
        [("Thema 01", "Relevanz"), ("Thema 02", "Strategie im Alltag"), ("Thema 03", "Perspektivwechsel"), ("Sonderthema", "Aufsichtsräte")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:13mm;padding-bottom:14mm">' + kicker("Unser Ansatz")
        + '<h2>Impulse, die eine These haben.</h2>'
        + '<p class="lead">Kein Standard-Vortrag von der Stange, sondern eine klare These, die zum Nachdenken und Diskutieren einlädt.</p>'
        + punkte([("star", "Aus echter Erfahrung", "Jeder Vortrag speist sich aus echten Projekten und Beratungserfahrung – keine austauschbare Theorie."),
                  ("target", "Auf Deinen Anlass zugeschnitten", "Ob Kickoff, Vertriebstag oder Führungskräfte-Tagung – der Vortrag wird auf Deinen Anlass zugeschnitten."),
                  ("messages-square", "Diskussionsstark", "Pointiert und mit klarer These, damit im Anschluss wirklich diskutiert wird – nicht nur genickt.")])
        + '</div><div class="band band--hell wachsen mitte anlaesse" style="padding-top:12mm">' + kicker("Für welche Anlässe")
        + '<h2>Wenn ein Impuls mehr bewirken soll als ein weiterer Foliensatz.</h2>'
        + check(["Kickoffs, bei denen der Ton für das Jahr gesetzt wird", "Vertriebstagungen mit vielen Teilnehmenden",
                 "Führungskräfte-Events, die nachwirken sollen", "Strategietage, an denen Denkmuster aufbrechen sollen"]).replace('class="check"', 'class="check" style="margin-top:10mm"')
        + '</div>', 2, N)

    zeilen = "".join(
        f'<div><div><small>{k}</small><h3>{t}</h3></div><div><p>{p}</p>'
        f'<ul class="merkmale">{"".join(f"<li><b>{a}</b>{b}</li>" for a, b in m)}</ul></div></div>' for k, t, p, m in VORTRAEGE)
    s3 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Unsere Impulsvorträge")
        + '<h2>Drei Themen. <span class="hl">Eine Wirkung.</span></h2>'
        + '<p class="lead">Wähle das Thema – wir passen den Vortrag auf Deinen Anlass an.</p>'
        + f'<div class="liste">{zeilen}</div>'
        + '<p class="notiz">Umfang, Dauer und Investition stimmen wir auf Deinen Anlass ab – ob Kickoff, Vertriebstag oder Führungskräfte-Tagung.</p>'
        + '</div>', 3, N, klasse="seite--hell")

    # Sonderthema als schwarzes Band (Daniel, Runde 2) – verdichtet aus „Strategie für Aufsichtsräte“
    s4 = seite(
        kopf(T)
        + '<div class="band band--schwarz wachsen" style="margin-top:10mm;padding-top:13mm">' + kicker("Sonderthema · Impulsvortrag &amp; Schulung")
        + '<h2>Strategie für <span class="hl">Aufsichtsräte.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Beraten, hinterfragen, überwachen: Woran erkennt ein Aufsichtsrat, ob eine Strategie trägt – '
          'und welche Fragen muss er dem Vorstand stellen?</p>'
        + '<div class="ar-fakten">' + "".join(f'<div><span>{l}</span><b>{v}</b></div>' for l, v in
            [("Dauer", "Halber Tag"), ("Format", "Vortrag &amp; Schulung"), ("Nachweis", "Mit Zertifikat"), ("Für", "Versicherungs&shy;unternehmen")]) + '</div>'
        + zeitstrahl([("IMPULS", "Wie entsteht Strategie?", "Wie eine Strategie im Versicherungs&shy;unternehmen entsteht – und was sie tragfähig macht."),
                      ("ROLLE", "Beraten oder überwachen?", "Was der Aufsichtsrat bei der Strategie leisten soll – und wo seine Rolle endet."),
                      ("FRAGEN", "Was fragen wir den Vorstand?", "Die Fragen, an denen sich zeigt, ob eine Strategie wirklich durchdacht ist."),
                      ("KENNZAHLEN", "Gelingt die Umsetzung?", "Die Kennzahlen, an denen der Aufsichtsrat erkennt, ob die Strategie ankommt.")])
        + '<div class="ar-ziel"><p class="label">Das Ziel</p><p>Euer Gremium ordnet eine Strategie fundiert ein, stellt die richtigen Fragen '
          'und erkennt an Kennzahlen, ob die Umsetzung gelingt.</p></div>'
        + '<div class="ar-unten"><div><p class="label">Aus einem Guss</p><h3>Unser Vortrag. Eure Strategie.</h3>'
          '<p>Besonders wirksam wird der Tag, wenn der Vorstand ein eigenes Praxisthema einbringt – die Unternehmens- oder die Vertriebsstrategie. '
          'Das stimmen wir im Vorfeld mit dem Vorstand ab. So diskutiert der Aufsichtsrat nicht abstrakt, sondern direkt am eigenen Unternehmen.</p></div>'
        + '<div><p class="label">Aus der Praxis, nicht aus dem Lehrbuch</p>'
        + check(["Vorstandsklausuren konzipiert", "Strategien auf Konzernebene entwickelt", "Führungskräfte bis auf Aufsichtsratsebene begleitet",
                 "Aufsichtsräte bereits mehrfach geschult", "Zertifikat als Nachweis für jedes Mitglied", "Als Fortbildung anrechenbar"])
        + '</div></div></div>', 4, N, hell_fuss=True)

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für einen Impuls, <span class="hl">der nachwirkt?</span></h2>'
        + '<p class="lead">Sag uns, worum es bei Deinem Anlass geht und wen Du im Raum hast – wir schlagen Dir den Vortrag vor, der dort am meisten bewegt.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist im Raum, wann ist der Anlass? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termin und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel"]) + kontaktdaten() + '</div></div>', 5, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
