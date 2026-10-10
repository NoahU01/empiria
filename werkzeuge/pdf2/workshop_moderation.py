"""PDF „Moderation deines Workshops“ im Stil des Musters „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Moderation deines Workshops – empiria"
T = "Moderation deines Workshops"

CSS = """
.seite--hell .liste > div { padding: 5.6mm 0; }
.seite--hell .liste p { font-size: 9pt; }
"""


def bauen():
    n = 4
    s1 = seite(titelseite(
        "Moderation deines Workshops", 'Dein Workshop.<br>Souverän moderiert.<br><span class="hl">Volle Wirkung.</span>',
        "Wir aktivieren die Beteiligten gezielt, wechseln bewusst die Perspektive und stellen die richtigen Fragen, "
        "um neue Blickwinkel auf die Themen zu bekommen.",
        kopfbild("Moderation deines Workshops"),
        [("Themen", "Strukturen, Prozesse &amp; Rollen"), ("Formate", "Kreativ- &amp; Vertriebsworkshops"), ("Ergebnis", "Handlungsklarheit")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:13mm;padding-bottom:13mm">' + kicker("Moderation")
        + '<h2>Erfahrung aus zahlreichen Workshops.</h2>'
        + '<p class="lead" style="max-width:150mm">Egal ob Strukturen, Prozesse und Rollen oder Kreativworkshops, Vertriebsansätze und mehr – wir bringen Deinen Workshop sicher ans Ziel.</p>'
        + punkte([("messages-square", "Gute Stimmung", "Wir sorgen für eine Atmosphäre, in der offen gesprochen wird – die Voraussetzung für jedes gute Ergebnis."),
                  ("route", "Workshops, die funktionieren", "Klare Steuerung durch den Tag, damit Energie und Zeit dort ankommen, wo sie etwas bringen."),
                  ("layout-grid", "Klare Erkenntnisse &amp; Strukturen", "Wir ordnen Diskussionen, statt sie laufen zu lassen – am Ende steht Struktur, keine losen Enden.")])
        + '</div><div class="rand" style="padding-top:12mm">'
        + punkte([("goal", "Ergebnisse, die tragen", "Ergebnisse, mit denen Dein Team direkt weiterarbeiten kann – nicht nur ein Protokoll zum Ablegen."),
                  ("layers", "Hohe Methodenvielfalt", "Von Kreativformaten bis zur klaren Entscheidungsrunde – wir wählen die Methode, die zum Thema passt."),
                  ("presentation", "Top Visualisierungen", "Ergebnisse werden sichtbar festgehalten statt nur besprochen – und sauber zusammengefasst.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:0;')
        + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:12mm"')
        + check(["Neustrukturierungen mit neuen oder geteilten Rollen", "Abteilungen mit vielen Themen, aber ohne klaren Weg nach vorn",
                 "Rollenklärung zwischen Führungskraft und neuer Stelle", "Führungswechsel, die mit einem Umbau zusammenfallen"])
        + '</div>', 2, n)

    faelle = [
        ("Restrukturierung mit geteilter Führung", "Bei der Neustrukturierung eines mittelständischen Unternehmens wurden komplett neue Rollen eingeführt – bis hin zu einer geteilten Führungsrolle. Der Workshop hat Rollen, Prozesse und Zuständigkeiten so konkret gemacht, dass sie sich direkt in den Arbeitsalltag übertragen ließen."),
        ("Klarheit nach zwei Strategieworkshops", "Eine Abteilung hatte nach zwei internen Strategieworkshops jede Menge Themen gesammelt, aber keinen klaren Weg nach vorn. Der Workshop brachte klare Schwerpunkte, klare Priorität und ein klares weiteres Vorgehen."),
        ("Einarbeitung einer neu geschaffenen Rolle", "Über mehrere Sequenzen wurden eine Führungskraft und ein neuer Mitarbeiter auf einer komplett neu geschaffenen Stelle begleitet. Die Rolle wurde ins Gesamtgefüge integriert und an den Schnittstellen geschärft – mit konkreten Methoden für den Alltag."),
        ("Neustart nach Führungswechsel", "Ein Führungswechsel ging mit einer Neustrukturierung der Abteilung einher. Erst wurde über mehrere Ebenen Vertrauen aufgebaut, dann ging es in die Inhalte – am Ende startete die Abteilung schlagkräftiger als zuvor."),
    ]
    s3 = seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
               + '<h2>Konkrete Usecases aus der Praxis.</h2>'
               + '<p class="lead">Ein Ausschnitt möglicher Workshopmoderationen – so vielfältig wie die Themen, die uns Teams mitbringen.</p>'
               + '<div class="liste">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
               + '<div class="kasten" style="margin-top:7mm"><div class="zwei"><div><p class="label">Im Fokus</p><h3>Prozess- und Strukturworkshop im Team</h3></div>'
               + '<p>Was kann künftig wegfallen? Am Anfang stand die Klärung, wofür die Abteilung steht und wo sie hinwill – erst danach entstanden Prozesse, die im Alltag tragen, statt dokumentiert abgelegt zu werden.</p></div></div>'
               + '</div>', 3, n, klasse="seite--hell")

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für den Workshop,<br>der <span class="hl">wirklich funktioniert?</span></h2>'
        + '<p class="lead">Schildere uns Dein Thema und wen Du im Raum hast – wir sagen Dir, wie wir den Workshop aufsetzen würden.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 4, n)
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=CSS)
