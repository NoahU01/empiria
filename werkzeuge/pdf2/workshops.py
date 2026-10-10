"""PDF „Workshops“ – Runde 2 (10.10.2026): Übersicht wie die 2.0-Seite; Preise/Umfang aus den drei Detailseiten.
Keine gelbe Spalte, weil die Übersichtsseite keinen Favoriten markiert."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Workshops – empiria"
T = "Workshops"

CSS = """
.tabelle--formate { table-layout: fixed; margin-top: 10mm; }
.tabelle--formate .zeile, .tabelle--formate thead th:first-child { width: 30mm; }
.tabelle--formate thead th { vertical-align: top; padding-top: 2mm; }
.tabelle--formate thead th b { white-space: normal; line-height: 1.15; margin-top: 1mm; }
.tabelle--formate td { padding-top: 4.6mm; padding-bottom: 4.6mm; }
.tabelle--formate .staffel { display: grid; grid-template-columns: auto 1fr; column-gap: 2.5mm; row-gap: .8mm; }
.tabelle--formate .staffel b { font-family: 'Lora', Georgia, serif; white-space: nowrap; }
.formate > div { grid-template-columns: 56mm 1fr; }
.formate small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.2mm; }
.formate p + p { margin-top: 1.6mm; }
.kontakt3 .team { margin-top: 9mm; gap: 12mm; }
.kontakt3 .kontaktdaten { grid-template-columns: 1.35fr 1fr 1fr; margin-top: 9mm; }
.kontakt3 .kontaktdaten div { justify-content: center; }
"""

FORMATE = [
    ("Format 01", "KI zum Anfassen",
     "Echte KI-Tools, echte Usecases aus der Versicherungsbranche – Schluss mit Arbeitskreisen ohne Praxis.",
     "Wir arbeiten mit mehreren KI-Tools gleichzeitig – vom ersten Ausprobieren bis zur konkreten Fallbearbeitung."),
    ("Format 02", "Sprint Landingpage",
     "Deine Landingpage in 48 Stunden live – für den Moment, in dem es schnell gehen muss.",
     "Onboarding, zwei Tage Sprint bei Dir vor Ort, Review – ohne Abstriche bei Qualität, Layout und Wirkung."),
    ("Format 03", "Moderation deines Workshops",
     "Gezielte Aktivierung, Perspektivwechsel und Handlungsklarheit – für Ergebnisse, mit denen sich weiterarbeiten lässt.",
     "Ob Strukturen, Prozesse und Rollen oder Kreativworkshops und Vertriebsansätze – wir bringen Deinen Workshop sicher ans Ziel."),
]


def formate_tabelle(nr, n):
    cols = [("Format 01", "KI zum<br>Anfassen"), ("Format 02", "Sprint<br>Landingpage"), ("Format 03", "Moderation deines<br>Workshops")]
    head = '<th></th>' + "".join(f'<th><small>{d}</small><b>{t}</b></th>' for d, t in cols)

    def zeile(label, werte, cls=""):
        return f'<tr><td class="zeile">{label}</td>' + "".join(f'<td class="{cls}">{w}</td>' for w in werte) + '</tr>'
    staffel = ('<div class="staffel"><span>½ Tag</span><b>2.500 €</b><span>1 Tag</span><b>3.900 €</b>'
               '<span>2 Tage</span><b>7.350 €</b></div>')
    body = (zeile("Investition", ["ab 2.500 €", "15.850 €", "auf Anfrage"], "preis")
            + zeile("Preise", [staffel, "Ein Leistungspaket: Konzeption, Umsetzung und Live-Schaltung",
                               "Umfang, Termine und Investition klären wir gemeinsam mit Dir"])
            + zeile("Umfang", ["½ bis 2 Tage, je nach Format", "2–3 Std. Onboarding online, 2 Tage Sprint vor Ort, Review",
                               "Abgestimmt auf Dein Thema und Deine Runde"])
            + zeile("Formate", ["KI&#8209;Einstieg, KI&#8209;Sprint, KI&#8209;Deep&#8209;Dive", "Sprint-Workshop mit 2 Beraterinnen und Beratern von empiria",
                                "Strukturen, Prozesse &amp; Rollen, Kreativ- und Vertriebsworkshops"])
            + zeile("Ergebnis", ["Direkt verwertbare Erkenntnisse aus echten Usecases", "Deine fertige Landingpage – live geschaltet",
                                 "Handlungsklarheit und Strukturen, die im Alltag tragen"])
            + zeile("Ansprech&shy;partner", ["Daniel Ströbel<br>Noah Hermanns", "Daniel Ströbel<br>Noah Hermanns", "Daniel Ströbel<br>Kerstin Christ"]))
    return seite(kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Investition")
                 + '<h2>Die Formate im Überblick.</h2><p class="lead">Umfang, Ergebnis und Investition der drei Workshops – so, wie sie auf den Detailseiten beschrieben sind.</p>'
                 + f'<table class="tabelle tabelle--formate"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
                 + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen. KI zum Anfassen inklusive Vorbereitung und Dokumentation der Ergebnisse; '
                   'Sprint Landingpage zzgl. Anfahrt und zwei Übernachtungen für je zwei Personen.</p>'
                 + '</div>', nr, n)


def bauen():
    n = 4
    s1 = seite(titelseite(
        "Workshops", 'Workshops, <span class="hl">die wirken.</span><br>Nicht nur Theorie.',
        "Ob Künstliche Intelligenz, eine neue Landingpage oder die Moderation Deines nächsten Workshops. "
        "Aus unseren Projekten sind Formate entstanden, die Du direkt buchen kannst.",
        kopfbild("Workshops"),
        [("Format 01", "KI zum Anfassen"), ("Format 02", "Sprint Landingpage"), ("Format 03", "Moderation deines Workshops")]))

    zeilen = "".join(f'<div><div><small>{k}</small><h3>{t}</h3></div><p>{a}</p></div>' for k, t, a, b in FORMATE)
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:13mm;padding-bottom:14mm">' + kicker("Unser Ansatz")
        + '<h2>Workshops, die nicht<br>bei der Theorie bleiben.</h2>'
        + '<p class="lead">Wir gehen direkt in die Anwendung – mit klaren Ergebnissen und einer Moderation, die trägt.</p>'
        + punkte([("zap", "Direkt anwendbar", "Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag."),
                  ("target", "Auf Dein Team zugeschnitten", "Jeder Workshop ist auf Deinen Anwendungsfall und Dein Team zugeschnitten – nicht von der Stange."),
                  ("users", "Professionell moderiert", "Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.")])
        + '</div><div class="rand" style="padding-top:13mm">' + kicker("Unsere Workshops")
        + '<h2>Drei Formate. Ein Ziel: Ergebnisse.</h2><p class="lead">Wähle das Format – wir bringen Dein Team ans Ziel.</p>'
        + f'<div class="liste formate">{zeilen}</div>'
        + '</div>', 2, n)

    s3 = formate_tabelle(3, n)

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für einen Workshop,<br>der Dich <span class="hl">wirklich weiterbringt?</span></h2>'
        + '<p class="lead">Sag uns, worum es geht und wer dabei sein soll – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag zum passenden Format."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte kontakt3" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + team(["daniel", "kerstin_hr", "noah_pm"]) + kontaktdaten() + '</div>', 4, n)
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=CSS)
