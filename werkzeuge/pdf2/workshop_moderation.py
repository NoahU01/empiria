"""PDF „Moderation deines Workshops“ – Runde 2 (10.10.2026): Inhalt = aktuelle 2.0-Seite inkl. aller „Mehr lesen“-Texte."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Moderation deines Workshops – empiria"
T = "Moderation deines Workshops"

CSS = """
.kasten--fokus .zeile { display: grid; grid-template-columns: 42mm 1fr; gap: 8mm; padding: 9.5mm 0; border-bottom: 1px solid rgba(255,255,255,.18); }
.kasten--fokus .zeile:last-child { border-bottom: 0; }
.kasten--fokus .zeile p { margin-top: 0; }
.kasten--fokus .zeile p:not(.label) { font-size: 9.6pt; line-height: 1.6; }
.kasten--fokus .zeile .label { padding-top: 1mm; }
.liste p + p { margin-top: 1.6mm; }
"""


def bauen():
    n = 5
    s1 = seite(titelseite(
        "Moderation deines Workshops", 'Dein Workshop.<br>Souverän moderiert.<br><span class="hl">Volle Wirkung.</span>',
        "Wir aktivieren die Beteiligten gezielt, wechseln bewusst die Perspektive und stellen die richtigen Fragen, "
        "um neue Blickwinkel auf die Themen zu bekommen.",
        kopfbild("Moderation deines Workshops"),
        [("Themen", "Strukturen, Prozesse &amp; Rollen"), ("Formate", "Kreativ- &amp; Vertriebsworkshops"), ("Ergebnis", "Handlungsklarheit")]))

    # Seite ohne Problem → gelbes Band mit den Punkten der Seite (sechs, wie auf der Seite)
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:14mm;padding-bottom:15mm">' + kicker("Moderation")
        + '<h2>Erfahrung aus<br>zahlreichen Workshops.</h2>'
        + '<p class="lead" style="max-width:150mm">Egal ob Strukturen, Prozesse und Rollen oder Kreativworkshops, Vertriebsansätze und mehr – wir bringen Deinen Workshop sicher ans Ziel.</p>'
        + punkte([("messages-square", "Gute Stimmung", "Wir sorgen für eine Atmosphäre, in der offen gesprochen wird – die Voraussetzung für jedes gute Ergebnis."),
                  ("route", "Workshops, die funktionieren", "Klare Steuerung durch den Tag, damit Energie und Zeit dort ankommen, wo sie etwas bringen."),
                  ("layout-grid", "Klare Erkenntnisse &amp; Strukturen", "Wir ordnen Diskussionen, statt sie laufen zu lassen – am Ende steht Struktur, keine losen Enden.")])
        + '</div><div class="rand wachsen mitte" style="padding-top:4mm">'
        + punkte([("goal", "Ergebnisse, die tragen", "Ergebnisse, mit denen Dein Team direkt weiterarbeiten kann – nicht nur ein Protokoll zum Ablegen."),
                  ("layers", "Hohe Methodenvielfalt", "Von Kreativformaten bis zur klaren Entscheidungsrunde – wir wählen die Methode, die zum Thema passt."),
                  ("presentation", "Top Visualisierungen &amp; Zusammenfassungen", "Ergebnisse werden sichtbar festgehalten statt nur besprochen – und sauber zusammengefasst.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:0;')
        + '<div class="kasten" style="margin-top:12mm"><div class="zwei"><div><p class="label">Unser Vorgehen</p>'
        + '<h3>Wir aktivieren. Wir wechseln die Perspektive. Wir stellen die richtigen Fragen.</h3></div>'
        + '<p style="margin-top:0">So entstehen neue Blickwinkel auf die Themen – und Handlungsklarheit statt einer weiteren Runde, in der alle reden und nichts passiert.</p></div></div>'
        + '</div>', 2, n)

    # Beispiele: volle Texte aus den „Mehr lesen“-Fenstern
    faelle = [
        ("Restrukturierung mit geteilter Führung",
         ["Im Zuge der Neustrukturierung eines mittelständischen Unternehmens wurden komplett neue Rollen eingeführt – bis hin zu einer geteilten Führungsrolle.",
          "Der Workshop hat Rollen, Prozesse, Verantwortlichkeiten und Zuständigkeiten so konkret gemacht, dass sie sich direkt in den Arbeitsalltag übertragen ließen."]),
        ("Klarheit nach zwei Strategieworkshops",
         ["Eine Abteilung hatte bereits zwei interne Strategieworkshops hinter sich – und jede Menge Themen gesammelt, aber keinen klaren Weg mehr nach vorn.",
          "Der Workshop hat Struktur in die Themen gebracht: klare Schwerpunkte, klare Priorität, klares weiteres Vorgehen."]),
        ("Einarbeitung einer neu geschaffenen Rolle",
         ["Über mehrere Sequenzen hinweg wurde eine Führungskraft und ein neuer Mitarbeiter begleitet, dessen Stelle komplett neu geschaffen worden war.",
          "Die Rolle musste ins Gesamtgefüge integriert und nach außen an den Schnittstellen im Unternehmen geschärft werden – inklusive konkreter Methoden, mit denen der Mitarbeiter seine neue Spezialrolle ausfüllen konnte."]),
        ("Neustart nach Führungswechsel",
         ["Ein Wechsel der Führungskraft ging mit einer Neustrukturierung der Abteilung einher – eine komplexe Situation, die gemeinsam aufgelöst werden musste.",
          "Über mehrere Ebenen wurde zunächst Vertrauen aufgebaut, damit alle den Weg mitgehen, bevor es in die Inhalte ging. Ergebnis: eine Abteilung, die schlagkräftiger in die Zukunft startete als zuvor."]),
    ]
    # Im Fokus: voller Text als schwarzes Band
    fokus = [("Ausgangslage", "In gewachsenen Strukturen verschieben sich Zuständigkeiten über die Jahre, und es kommen laufend neue Themen dazu – was fehlt, ist die systemische Müllabfuhr: die Frage, was künftig wegfallen oder deutlich anders laufen kann."),
             ("Die Hürde", "Genau das lässt sich intern kaum beantworten, weil sich jede Veränderung wie das Aufgeben von etwas Etabliertem anfühlt, dessen Konsequenzen niemand absehen will."),
             ("Der Ansatz", "Deshalb stand am Anfang nicht die Optimierung einzelner Schritte, sondern die Klärung, wofür die Abteilung steht und wo sie hinwill."),
             ("Das Ergebnis", "Erst danach entstanden Prozesse und Strukturen, die im Alltag tragen – weil der Mehrwert verstanden ist und für alle Klarheit herrscht, statt sauber dokumentiert abgelegt zu werden, wo niemand mehr hineinschaut.")]
    s3 = seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
               + '<h2>Konkrete Usecases aus der Praxis.</h2>'
               + '<p class="lead">Ein Ausschnitt möglicher Workshopmoderationen – so vielfältig wie die Themen, die uns Teams mitbringen.</p>'
               + '<div class="liste">' + "".join(f'<div style="padding:6.5mm 0"><h3>{t}</h3><div>' + "".join(f"<p>{x}</p>" for x in ps) + '</div></div>' for t, ps in faelle) + '</div>'
               + '</div>', 3, n, klasse="seite--hell")

    s4 = seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Im Fokus")
               + '<h2>Prozess- und Strukturworkshop<br>im Team.</h2>'
               + '<p class="lead">Was kann wegfallen? Erst klären, wofür die Abteilung steht – dann Prozesse, die im Alltag tragen.</p>'
               + '<div class="kasten kasten--fokus" style="margin-top:10mm;padding:5mm 8mm">'
               + "".join(f'<div class="zeile"><p class="label">{l}</p><p>{x}</p></div>' for l, x in fokus)
               + '</div></div>', 4, n, klasse="seite--hell")

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für den Workshop,<br>der <span class="hl">wirklich funktioniert?</span></h2>'
        + '<p class="lead">Schildere uns Dein Thema und wen Du im Raum hast – wir sagen Dir, wie wir den Workshop aufsetzen würden.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 5, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
