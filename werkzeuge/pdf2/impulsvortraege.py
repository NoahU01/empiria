"""PDF „Impulsvorträge“ im Stil des Musters KI zum Anfassen (10.10.2026).
Quelle: site/projekte/empiria-2/impulsvortraege.html (drei Vorträge), ergänzend P["impulsvortraege"] und
P["vortrag-1..3"] im alten PDF (Kurzbeschreibungen, Anlässe, Merkmale je Vortrag)."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, check, dokument)

TITEL = "Impulsvorträge – empiria"
T = "Impulsvorträge"
N = 4

CSS = """
.vortraege { margin-top: 9mm; border-top: 1.6px solid #1a1817; }
.vortrag { display: grid; grid-template-columns: 62mm 1fr; gap: 9mm; padding: 5.5mm 0 6mm; border-bottom: 1px solid #dcd8d1; }
.vortrag small { display: block; font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.vortrag h3 { font-size: 14pt; line-height: 1.22; margin-top: 2.4mm; }
.vortrag p { font-size: 9.2pt; line-height: 1.6; color: #3d3a37; }
.vortrag ul { list-style: none; display: grid; grid-template-columns: repeat(3, 1fr); gap: 4mm; margin-top: 4mm; }
.vortrag li { border-top: 1.2px solid #1a1817; padding-top: 2.2mm; font-size: 8.2pt; line-height: 1.45; color: #3d3a37; }
.anlaesse .check li { font-size: 10.4pt; padding-top: 3.6mm; padding-bottom: 3.6mm; }
.anlaesse .check li::before { top: 5.6mm; }
.kasten.klein h3 { font-size: 12.5pt; }
.vortrag li b { display: block; font-family: 'Lora', Georgia, serif; font-size: 10pt; color: #1a1817; margin-bottom: .6mm; }
"""

VORTRAEGE = [
    ("Relevanz", "Warum sich niemand für Dein Produkt interessiert.",
     "Ein wachrüttelnder Impuls darüber, warum Qualität allein nicht überzeugt – und was ein Produkt wirklich braucht, damit es gehört, verstanden und gewollt wird.",
     [("Ehrlich", "Eine klare Analyse, warum Botschaften verpuffen."), ("Nah dran", "Beispiele aus echten Projekten."),
      ("Umsetzbar", "Ansatzpunkte, die am nächsten Tag funktionieren.")]),
    ("Strategie im Alltag", "Strategie, die endlich ankommt.",
     "Die beste Strategie nützt nichts, wenn sie in der Schublade landet. Der Vortrag zeigt, wie Strategie so kommuniziert wird, dass sie im Alltag Deines Teams ankommt – und wirkt.",
     [("Verständlich", "In einer Sprache, die jede Ebene versteht."), ("Verankert", "Wie aus Folien echte Entscheidungen werden."),
      ("Mitreißend", "Greifbar statt abstrakt – mit echter Zustimmung.")]),
    ("Perspektivwechsel", "Gründe Deinen stärksten Konkurrenten!",
     "Was, wenn Du selbst der schärfste Angreifer auf Dein eigenes Geschäftsmodell wärst? Der Vortrag deckt blinde Flecken auf, bevor es jemand anders tut.",
     [("Provokant", "Stellt bequeme Wahrheiten infrage."), ("Konkret", "Ein Denkwerkzeug, das Teams selbst anwenden."),
      ("Wachrüttelnd", "Zeigt Angriffsfläche, bevor es teuer wird.")]),
]


def bauen():
    s1 = seite(titelseite(
        T, 'Impulse,<br><span class="hl">die nachwirken.</span><br>Nicht nur unterhalten.',
        "Drei Vorträge aus echter Beratungserfahrung – für den Moment, in dem ein Impuls mehr bewirken soll als ein weiterer Foliensatz.",
        kopfbild("Impulsvorträge"),
        [("Thema", "Relevanz"), ("Thema", "Strategie im Alltag"), ("Thema", "Perspektivwechsel"), ("Anlass", "Kickoff, Tagung, Event")]))

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
        f'<div class="vortrag"><div><small>{k}</small><h3>{t}</h3></div><div><p>{p}</p>'
        f'<ul>{"".join(f"<li><b>{a}</b>{b}</li>" for a, b in m)}</ul></div></div>' for k, t, p, m in VORTRAEGE)
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:13mm">' + kicker("Unsere Impulsvorträge")
        + '<h2>Drei Themen. <span class="hl">Eine Wirkung.</span></h2>'
        + '<p class="lead">Wähle das Thema – wir passen den Vortrag auf Deinen Anlass an.</p>'
        + f'<div class="vortraege">{zeilen}</div>'
        + '<div class="kasten klein" style="margin-top:8mm"><div class="zwei"><div><p class="label">Für Deinen Anlass</p>'
          '<h3>Umfang, Dauer und Investition stimmen wir auf Deinen Anlass ab.</h3></div>'
          '<p>Ob Kickoff, Vertriebstag oder Führungskräfte-Tagung: Jeder Vortrag wird auf Deinen Anlass und Dein Publikum zugeschnitten.</p></div></div>'
        + '</div>', 3, N)

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für einen Impuls, <span class="hl">der nachwirkt?</span></h2>'
        + '<p class="lead">Sag uns, worum es bei Deinem Anlass geht und wen Du im Raum hast – wir schlagen Dir den Vortrag vor, der dort am meisten bewegt.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist im Raum, wann ist der Anlass? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termin und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel"]) + kontaktdaten() + '</div></div>', 4, N)
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=CSS)
