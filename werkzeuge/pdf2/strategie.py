"""PDF „Strategie in den Alltag überführen“ – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/strategie.html inkl. Strategiemodell-Modal und der drei Zusammenarbeit-Dialoge."""
from lib import (titelseite, seite, kopf, kicker, punkte, zeitstrahl, dokument)
from _strategie_teile import TEAM3_CSS, LISTE_CSS, zeichen, schluss, liste

TITEL = "Strategie in den Alltag überführen – empiria"
T = "Strategie in den Alltag"
N = 6

# Sonderbaustein: die „Homepage Deiner Abteilung“ aus dem Perspektivwechsel (Browserfenster wie auf der Seite)
CSS = TEAM3_CSS + LISTE_CSS + """
.browser { border: 1px solid #dcd8d1; border-radius: 4.5mm; overflow: hidden; background: #fff; }
.browser__leiste { display: flex; align-items: center; gap: 1.6mm; padding: 3.2mm 4.5mm; background: #1a1817; color: #fff; font-size: 7.6pt; font-weight: 600; }
.browser__leiste i { width: 2.2mm; height: 2.2mm; border-radius: 50%; background: rgba(255,255,255,.35); }
.browser__leiste i:first-child { background: #fff400; }
.browser__leiste span { margin-left: 3mm; }
.browser__zeile { display: grid; grid-template-columns: 8mm 1fr 5mm; align-items: center; padding: 3.8mm 4mm; border-top: 1px solid #ece9e5; font-size: 8.8pt; }
.browser__zeile:first-of-type { border-top: 0; }
.browser__zeile b { font-size: 7pt; letter-spacing: .14em; }
.browser__zeile em { font-style: normal; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12pt; text-align: right; }
"""


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Strategie in den<br>Alltag <span class="hl">überführen.</span>',
        "Deine Strategie ist da – aber was bedeutet sie für Deinen Verantwortungsbereich? Wir machen sie greifbar und wirksam im Alltag.",
        zeichen("forward", 92),
        [("Für wen", "Abteilungs- &amp; Bereichsleiter"), ("Fokus", "Rolle, Richtung, Handwerkszeug"),
         ("Begleitung", "Direkt mit Daniel"), ("Dein Einsatz", "1–2 Stunden pro Woche")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Das Problem")
        + '<h2>Strategisches Denken wird vorausgesetzt. Dir hat es aber <span class="hl">keiner beigebracht.</span></h2>'
        + '<p class="lead">Du bist Abteilungs- oder Bereichsleiter, weil Du fachlich überzeugt hast. Was danach oft folgt, sind harte Gespräche mit dem eigenen Team. '
          'Strategisches Denken stand nie auf dem Lehrplan – trotzdem wird es ab dem ersten Tag vorausgesetzt.</p>'
        + kicker("Hart, weil das Fundament fehlt").replace('class="kicker"', 'class="kicker" style="margin-top:9mm"')
        + punkte([("compass", "Die klare Richtung", ""), ("user-round", "Die eigene Rolle", ""),
                  ("wrench", "Das Handwerkszeug für den Alltag", "")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Rolle, Richtung, Handwerkszeug<br>für Deinen Bereich.</h2>'
        + '<p class="lead">Wir arbeiten an drei Dingen, die Dir als Führungskraft Handlungsklarheit verschaffen.</p>'
        + punkte([("user-round", "Rolle", "Wofür stehe ich und mein Bereich?"),
                  ("eye", "Richtung", "Wie wollen wir wahrgenommen werden?"),
                  ("route", "Handwerkszeug", "Wie kommen wir dort hin?")])
        + '<p class="lead" style="margin-top:9mm">Dies umfasst das praktische Handwerkszeug, mit dem Du als Führungskraft im Alltag vorankommst.</p>'
        + '</div>', 2, N)

    alltag = [
        ("", "Führungs- und Arbeitsalltag", "<p>Wie sichern wir die Zielerreichung?</p>"),
        ("", "Strategie&shy;kommunikation", "<p>Wie erklären wir die Strategie intern?</p>"),
        ("", "Positionierung &amp; Pitch", "<p>Welches Problem lösen wir – und was macht uns einzigartig?</p>"),
    ]
    s3 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Unser Strategiemodell")
        + '<h2>Vom Selbstverständnis bis in den <span class="hl">Alltag Deines Bereichs.</span></h2>'
        + zeitstrahl([("01", "Selbstverständnis", "Wofür stehen wir? Unternehmensstrategie, Führungsverständnis und die Zielgruppe („What’s in for me?“) fließen ein – die Basis für alles Weitere."),
                      ("02", "Vision", "Der Blick nach vorn: Wie wollen wir wahrgenommen werden? Das zukünftige Geschäfts- und Organisationsmodell."),
                      ("03", "Strategie", "Der ehrliche Abgleich mit der Ausgangssituation, dem heutigen Modell, zeigt den Weg: Mission, Stoßrichtungen und Handlungsfelder."),
                      ("04", "Alltag", "Die Detaillierung der Strategie – im Führungsalltag, nach innen und in der Positionierung nach außen.")])
        + kicker("Detaillierung der Strategie").replace('class="kicker"', 'class="kicker" style="margin-top:11mm"')
        + liste(alltag)
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:12mm">' + kicker("Das Ergebnis")
        + '<h2>Du führst Dein Team, <span class="hl">statt es zu vertrösten.</span></h2>'
        + '<p class="lead">Du kannst jederzeit erklären, wofür Dein Bereich steht und wie das Zielbild aussieht. '
          'Dein Team zieht mit, weil die Richtung geklärt ist – nicht, weil Du sie ständig neu erklären musst.</p>'
        + '</div>', 3, N, hell_fuss=True)

    fragen = ["Welche Zielgruppe sprechen wir an?", "Welches konkrete Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
              "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"]
    browser = ('<div class="browser"><div class="browser__leiste"><i></i><i></i><i></i><span>www.deine-abteilung-gmbh.de</span></div>'
               + "".join(f'<div class="browser__zeile"><b>{i + 1:02d}</b><span>{q}</span><em>?</em></div>' for i, q in enumerate(fragen))
               + '</div>')
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Perspektivwechsel")
        + '<h2>Wie sieht die Homepage<br><span class="hl">Deiner Abteilung</span> aus?</h2>'
        + '<p class="lead">Ziemlich wahrscheinlich hast Du keine – die meisten haben keine. Also warum die Frage? Weil hier sofort klar wird, ob Du den Mehrwert Deines Bereichs sauber erklären kannst. '
          'Und wenn Du das nicht kannst, kann auch keiner in Deinem Team aktiv zu Deiner Strategie beitragen.</p>'
        + '<div class="zwei" style="margin-top:10mm;align-items:start"><div>' + kicker("Gedankenexperiment")
        + '<h3 style="margin-top:4mm">Stell Dir vor, wir gründen morgen Deine Abteilung als GmbH.</h3>'
        + '<p style="margin-top:3mm">Und verkaufen Eure Dienstleistungen an Deinen aktuellen Arbeitgeber. Was stünde auf der Homepage – und würde jeder im Team dasselbe hineinschreiben?</p></div>'
        + browser + '</div>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Ergebnis")
        + '<h2>Jeder im Team versteht, wofür Dein Bereich da ist.</h2>'
        + '<p class="lead">Und Du bestimmst seine Wahrnehmung.</p>'
        + '</div>', 4, N)

    zusammen = [
        ("01", "Direkter Draht, klare Worte",
         "<p>Du arbeitest direkt mit mir – Daniel – zusammen. Bei Bedarf binde ich gezielt einzelne Teammitglieder ein, die Verantwortung für Dein Projekt bleibt aber durchgehend bei mir.</p>"
         "<p>Dabei sage ich, was ich denke: ehrliches, direktes Feedback, auch zu Themen, die gerade nicht passen. Nicht um zu ärgern, sondern um den Fokus zu schärfen und Wege sichtbar zu machen, die auf den ersten Blick nicht offensichtlich sind.</p>"),
        ("02", "Dein Einsatz entscheidet",
         "<p>Eine Strategie lässt sich nicht von außen in Dein Unternehmen hineintragen. Wir unterstützen Dich maximal – die Umsetzung bleibt aber Deine Aufgabe.</p>"
         "<p>Plane dafür ein bis zwei Stunden pro Woche ein.</p>"),
        ("03", "Dranbleiben, klar planen, umsetzen",
         "<p>Wir stimmen uns regelmäßig ab, statt nur punktuell – ohne festen Rhythmus verliert jedes Projekt seine Dynamik.</p>"
         "<p>Wir vereinbaren ein klares Vorgehen und bleiben flexibel genug, um auf Engpässe im Unternehmen zu reagieren und, wenn nötig, umzusteuern.</p>"
         "<p>Und ab einem gewissen Punkt zählt eine schnelle, stringente Umsetzung mehr als eine weitere Abstimmungsschleife.</p>"),
    ]
    s5 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Zusammenarbeit")
        + '<h2>So arbeiten wir wirklich zusammen.</h2>'
        + liste(zusammen)
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:12mm">' + kicker("Dranbleiben")
        + '<h2>Eine Strategie im Alltag zu verankern, geht nicht von heute auf morgen.</h2>'
        + '<p class="lead">Sie funktioniert nur, wenn wir dranbleiben.</p>'
        + '</div>', 5, N, hell_fuss=True)

    s6 = seite(kopf(T) + schluss('Wir sind <span class="hl">für Dich da!</span>',
                                 "Lass uns darüber sprechen, welche Themen Dich aktuell bewegen. Gemeinsam klären wir, ob und wie wir Dir weiterhelfen können.",
                                 ["daniel", "kerstin_hr", "noah_pm"]), 6, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=CSS)
