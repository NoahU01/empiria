"""PDF „Workshops“ – Übersicht über die drei Formate, im Stil des Musters „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Workshops – empiria"
T = "Workshops"

CSS = """
.tabelle--formate { table-layout: fixed; margin-top: 11mm; }
.tabelle--formate .zeile, .tabelle--formate thead th:first-child { width: 30mm; }
.tabelle--formate thead th { vertical-align: top; padding-top: 2mm; }
.tabelle--formate thead th b { white-space: normal; line-height: 1.15; margin-top: 1mm; }
.tabelle--formate td { padding-top: 3mm; padding-bottom: 3mm; }
.kontakt3 .team { margin-top: 9mm; gap: 12mm; }
.kontakt3 .kontaktdaten { grid-template-columns: 1.35fr 1fr 1fr; margin-top: 9mm; }
.kontakt3 .kontaktdaten div { justify-content: center; }
"""


def formate(nr, n):
    cols = [("Format 01", "KI zum<br>Anfassen"), ("Format 02", "Sprint<br>Landingpage"), ("Format 03", "Workshop-<br>Moderation")]
    head = '<th></th>' + "".join(f'<th><small>{d}</small><b>{t}</b></th>' for d, t in cols)

    def zeile(label, werte, cls=""):
        return f'<tr><td class="zeile">{label}</td>' + "".join(f'<td class="{cls}">{w}</td>' for w in werte) + '</tr>'
    body = (zeile("Investition", ["ab 2.500 €", "15.850 €", "nach Anlass"], "preis")
            + zeile("Inhalt", ["Echte KI-Tools, echte Usecases aus der Versicherungsbranche – Schluss mit Arbeitskreisen ohne Praxis.",
                                      "Deine Landingpage in 48 Stunden live – für den Moment, in dem es schnell gehen muss.",
                                      "Gezielte Aktivierung, Perspektivwechsel und Handlungsklarheit – für Ergebnisse, mit denen sich weiterarbeiten lässt."])
            + zeile("Umfang", ["½ bis 2 Tage", "Onboarding, 2 Tage Sprint vor Ort, Review", "nach Anlass"])
            + zeile("Ergebnis", ["Direkt verwertbare Erkenntnisse aus Euren Fällen", "Eine fertige Landingpage, live geschaltet", "Handlungsklarheit und Strukturen, die tragen"]))
    kasten = ('<div class="kasten" style="margin-top:7mm"><p class="label">In jedem Workshop enthalten</p>'
              + punkte([("target", "Echte Fälle", "Ergebnisse aus echten Fällen Deines Hauses, nicht aus Fallstudien."),
                        ("file-text", "Dokumentation", "Eine Dokumentation, die auch Wochen später noch verständlich ist."),
                        ("route", "Nächste Schritte", "Klare nächste Schritte statt einer Liste offener Punkte.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
              + '</div>')
    return seite(kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Unsere Workshops")
                 + '<h2>Drei Formate. Ein Ziel: Ergebnisse.</h2><p class="lead">Wähle das Format – wir bringen Dein Team ans Ziel.</p>'
                 + f'<table class="tabelle tabelle--formate"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
                 + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen.</p>' + kasten
                 + '</div>', nr, n)


def bauen():
    n = 4
    s1 = seite(titelseite(
        "Workshops", 'Workshops,<br><span class="hl">die wirken.</span><br>Nicht nur Theorie.',
        "Ob Künstliche Intelligenz, eine neue Landingpage oder die Moderation Deines nächsten Workshops. "
        "Aus unseren Projekten sind Formate entstanden, die Du direkt buchen kannst.",
        kopfbild("Workshops"),
        [("Format 01", "KI zum Anfassen"), ("Format 02", "Sprint Landingpage"), ("Format 03", "Moderation deines Workshops")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:14mm;padding-bottom:14mm">' + kicker("Unser Ansatz")
        + '<h2>Workshops, die nicht<br>bei der Theorie bleiben.</h2>'
        + '<p class="lead">Wir gehen direkt in die Anwendung – mit klaren Ergebnissen und einer Moderation, die trägt.</p>'
        + punkte([("zap", "Direkt anwendbar", "Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag."),
                  ("target", "Auf Dein Team zugeschnitten", "Jeder Workshop ist auf Deinen Anwendungsfall und Dein Team zugeschnitten – nicht von der Stange."),
                  ("users", "Professionell moderiert", "Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.")])
        + '</div><div class="rand" style="padding-top:16mm">' + kicker("Für wen das gemacht ist")
        + '<h2>Teams, die weiterkommen wollen –<br>nicht nur tagen.</h2>'
        + '<p class="lead">Unsere Workshops entstehen aus Projekten in der Versicherungsbranche. Deshalb sitzen die Beispiele, und deshalb kommt Dein Team schneller ins Arbeiten.</p>'
        + check(["Teams, die KI endlich praktisch nutzen wollen statt darüber zu reden",
                 "Bereiche mit kurzfristigem Vertriebsdruck und einem Thema, das online muss",
                 "Neustrukturierungen, Rollenklärungen und Führungswechsel",
                 "Strategietage, die zu Ergebnissen führen sollen statt zu Themensammlungen"]).replace('class="check"', 'class="check" style="margin-top:8mm"')
        + '</div>', 2, n)

    s3 = formate(3, n)

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
