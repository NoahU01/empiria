"""PDF „Strategie in den Alltag überführen“ – im Muster „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Strategie in den Alltag überführen – empiria"
T = "Strategie in den Alltag"
N = 6


def zeichen(name):
    """Großes, gefülltes Themen-Zeichen der Homepage (e2_bauen.FORM / THEMEN_ZEICHEN), schwarz."""
    import e2_bauen
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg class="zeichen" viewBox="{vb}" aria-hidden="true" fill="#1a1817" color="#1a1817">{e2_bauen.FORM[name]}</svg>'


CSS = """
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p, .sub { text-wrap: pretty; }
.liste--gross > div { padding: 6.5mm 0; }
.liste--gross p { font-size: 9.4pt; }
.liste--gross p + p { margin-top: 2mm; }
.titel .bild svg.zeichen { width: 92mm; }
.fehlt { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; margin-top: 5mm; }
.fehlt > div { border-top: 1.6px solid #1a1817; padding-top: 4mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.25; }
.satz { font-size: 9.6pt; line-height: 1.6; margin-top: 9mm; max-width: 140mm; }
.label-s { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-top: 9mm; }
.browser { border: 1px solid #dcd8d1; border-radius: 4.5mm; overflow: hidden; background: #fff; }
.browser__leiste { display: flex; align-items: center; gap: 1.6mm; padding: 3.2mm 4.5mm; background: #1a1817; color: #fff; font-size: 7.6pt; font-weight: 600; }
.browser__leiste i { width: 2.2mm; height: 2.2mm; border-radius: 50%; background: rgba(255,255,255,.35); }
.browser__leiste i:nth-child(1) { background: #fff400; }
.browser__leiste span { margin-left: 3mm; }
.browser__zeile { display: grid; grid-template-columns: 8mm 1fr 5mm; align-items: center; padding: 4.2mm 4mm; border-top: 1px solid #ece9e5; font-size: 8.8pt; white-space: nowrap; }
.browser__zeile:first-of-type { border-top: 0; }
.browser__zeile b { font-size: 7pt; letter-spacing: .14em; }
.browser__zeile em { font-style: normal; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12pt; text-align: right; }
.schluss .zwei { grid-template-columns: 99mm 1fr; gap: 8mm; }
.schluss .team { gap: 3mm; }
.schluss .person { width: 31mm; }
.schluss .person img { width: 24mm; height: 24mm; }
"""


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Strategie in den<br>Alltag <span class="hl">überführen.</span>',
        "Deine Strategie ist da – aber was bedeutet sie für Deinen Verantwortungsbereich? Wir machen sie greifbar und wirksam im Alltag.",
        zeichen("forward"),
        [("Für wen", "Abteilungs- &amp; Bereichsleiter"), ("Fokus", "Rolle, Richtung, Handwerkszeug"),
         ("Begleitung", "Direkt mit Daniel"), ("Ergebnis", "Handlungsklarheit")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:14mm">' + kicker("Das Problem")
        + '<h2>Strategisches Denken wird vorausgesetzt. Dir hat es aber <span class="hl">keiner beigebracht.</span></h2>'
        + '<p class="lead">Du bist Abteilungs- oder Bereichsleiter, weil Du fachlich überzeugt hast. Strategisches Denken stand nie auf dem Lehrplan – trotzdem wird es ab dem ersten Tag vorausgesetzt.</p>'
        + '<p class="label-s">Was folgt, sind harte Gespräche mit dem Team – weil das Fundament fehlt</p>'
        + '<div class="fehlt"><div>die klare Richtung</div><div>die eigene Rolle</div><div>das Handwerkszeug für den Alltag</div></div>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:13mm">' + kicker("Die Lösung")
        + '<h2>Rolle, Richtung, Handwerkszeug<br>für Deinen Bereich.</h2>'
        + '<p class="lead">Wir arbeiten an drei Dingen, die Dir als Führungskraft Handlungsklarheit verschaffen.</p>'
        + punkte([("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"),
                  ("eye", "Richtung", "Wie wollen wir wahrgenommen werden?"),
                  ("route", "Handwerkszeug", "Wie kommen wir dort hin?")])
        + '<p class="satz">Dies umfasst das praktische Handwerkszeug, mit dem Du als Führungskraft im Alltag vorankommst.</p>'
        + '</div>', 2, N)

    s3 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Unser Strategiemodell")
        + '<h2>Vom Selbstverständnis bis in den <span class="hl">Alltag Deines Bereichs.</span></h2>'
        + '<p class="lead">Dieselbe Struktur, mit der wir im Sparring arbeiten – Schritt für Schritt vom Fundament bis in den Alltag.</p>'
        + zeitstrahl([("01", "Selbstverständnis", "Wofür steht Dein Bereich? Die Antwort ist die Basis für alles Weitere."),
                      ("02", "Vision", "Der Blick nach vorn: Wie wollt Ihr wahrgenommen werden?"),
                      ("03", "Strategie", "Der ehrliche Abgleich mit der Ausgangssituation zeigt, welcher Weg dorthin führt."),
                      ("04", "Alltag", "Konkret im Führungs- und Arbeitsalltag, nach innen und in der Positionierung nach außen.")])
        + '<div class="kasten" style="margin-top:14mm;padding:8mm 9mm 9mm"><p class="label">Das Ergebnis</p>'
        + '<h3 style="font-size:19pt;margin-top:3mm">Du führst Dein Team, statt es zu vertrösten.</h3>'
        + '<p style="font-size:9.6pt;max-width:140mm">Du kannst jederzeit erklären, wofür Dein Bereich steht und wie das Zielbild aussieht. '
          'Dein Team zieht mit, weil die Richtung geklärt ist – nicht, weil Du sie ständig neu erklären musst.</p></div>'
        + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:14mm"')
        + check(["Abteilungs- und Bereichsleitungen, die fachlich überzeugt haben", "Führungskräfte, die ihrem Bereich Richtung geben müssen"])
        + '</div>', 3, N)

    fragen = ["Welche Zielgruppe sprechen wir an?", "Welches konkrete Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
              "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"]
    browser = ('<div class="browser"><div class="browser__leiste"><i></i><i></i><i></i><span>www.deine-abteilung-gmbh.de</span></div>'
               + "".join(f'<div class="browser__zeile"><b>{i + 1:02d}</b><span>{q}</span><em>?</em></div>' for i, q in enumerate(fragen))
               + '</div>')
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Perspektivwechsel")
        + '<h2>Wie sieht die Homepage<br><span class="hl">Deiner Abteilung</span> aus?</h2>'
        + '<p class="lead" style="max-width:150mm">Ziemlich wahrscheinlich hast Du keine – die meisten haben keine. Aber hier wird sofort klar, ob Du den Mehrwert Deines Bereichs sauber erklären kannst. '
          'Wenn nicht, kann auch keiner in Deinem Team aktiv zu Deiner Strategie beitragen.</p>'
        + '<div class="zwei" style="margin-top:11mm;align-items:start"><div>' + kicker("Gedankenexperiment")
        + '<h3 style="font-size:15pt;margin-top:4mm">Stell Dir vor, wir gründen morgen Deine Abteilung als GmbH.</h3>'
        + '<p style="margin-top:3mm;font-size:9.4pt">Und verkaufen Eure Dienstleistungen an Deinen aktuellen Arbeitgeber. Was stünde auf der Homepage – und würde jeder im Team dasselbe hineinschreiben?</p></div>'
        + browser + '</div>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Ergebnis")
        + '<h2>Jeder im Team versteht,<br>wofür Dein Bereich da ist.</h2>'
        + '<p class="lead">Und Du bestimmst seine Wahrnehmung.</p>'
        + '</div>', 4, N)

    zusammen = [
        ("Direkter Draht, klare Worte",
         ["Du arbeitest direkt mit mir – Daniel – zusammen. Bei Bedarf binde ich gezielt einzelne Teammitglieder ein, die Verantwortung für Dein Projekt bleibt aber durchgehend bei mir.",
          "Dabei sage ich, was ich denke: ehrliches, direktes Feedback, auch zu Themen, die gerade nicht passen – um den Fokus zu schärfen und Wege sichtbar zu machen, die nicht offensichtlich sind."]),
        ("Dein Einsatz entscheidet",
         ["Eine Strategie lässt sich nicht von außen in Dein Unternehmen hineintragen. Wir unterstützen Dich maximal – die Umsetzung bleibt aber Deine Aufgabe.",
          "Plane dafür ein bis zwei Stunden pro Woche ein."]),
        ("Dranbleiben, klar planen, umsetzen",
         ["Wir stimmen uns regelmäßig ab statt nur punktuell – ohne festen Rhythmus verliert jedes Projekt seine Dynamik. Wir vereinbaren ein klares Vorgehen und bleiben flexibel genug, um bei Engpässen umzusteuern.",
          "Ab einem gewissen Punkt zählt eine schnelle, stringente Umsetzung mehr als eine weitere Abstimmungsschleife."]),
    ]
    s5 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Zusammenarbeit")
        + '<h2>So arbeiten wir wirklich zusammen.</h2>'
        + '<div class="liste liste--gross">' + "".join(f'<div><h3>{t}</h3><div>' + "".join(f"<p>{x}</p>" for x in ps) + '</div></div>' for t, ps in zusammen) + '</div>'
        + '<div class="kasten" style="margin-top:9mm;padding:8mm 9mm 9mm"><div class="zwei"><div><p class="label">Dranbleiben</p>'
        + '<h3>Eine Strategie im Alltag zu verankern, geht nicht von heute auf morgen.</h3></div>'
        + '<p>Sie funktioniert nur, wenn wir dranbleiben – mit regelmäßiger Abstimmung, einem klaren Vorgehen und Deinem Einsatz von ein bis zwei Stunden pro Woche.</p></div></div>'
        + '</div>', 5, N, klasse="seite--hell")

    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Lass uns über <span class="hl">Deinen Bereich sprechen.</span></h2>'
        + '<p class="lead">Kein Pitch, kein Angebot von der Stange: ein offenes Gespräch über Deinen Verantwortungsbereich – und was ihn gerade ausbremst.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte schluss" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr", "noah_pm"]) + kontaktdaten() + '</div></div>', 6, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=CSS)
