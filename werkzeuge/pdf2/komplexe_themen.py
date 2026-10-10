"""PDF „Komplexe Themen strukturieren & kommunizieren“ – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/komplexe-themen.html inkl. der vier Schritt-Dialoge (ls0–ls3)
und der dort verlinkten „3 goldenen Regeln“ (Inhalt wie goldene_regeln.REGELN)."""
from lib import (titelseite, seite, kopf, kicker, punkte, zeitstrahl, check, dokument)
from _strategie_teile import TEAM3_CSS, LISTE_CSS, zeichen, schluss, liste
from goldene_regeln import REGELN

TITEL = "Komplexe Themen strukturieren & kommunizieren – empiria"
T = "Komplexe Themen"
N = 7

CSS = TEAM3_CSS + LISTE_CSS


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Komplexe Themen strukturieren &amp; <span class="hl">kommunizieren.</span>',
        "Überall dort, wo Du als Führungskraft in der Versicherungsbranche Menschen von Deinem Thema überzeugen willst, sorgen wir dafür, dass Deine Botschaft wirkt.",
        zeichen("kreuz", 76),
        [("Gremien", "Vorstand &amp; Aufsichtsrat"), ("Intern", "Lenkungsausschuss &amp; Betriebsrat"),
         ("Vertrieb", "Tagung &amp; Kundenpitch"), ("Partner", "Rückversicherer &amp; Kooperationen")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Das Problem")
        + '<h2>Deine Präsentation ist vollständig. <span class="hl">Und wirkungslos.</span></h2>'
        + '<p class="lead">Vor jedem wichtigen Termin derselbe Reflex: „Wir brauchen eine Präsentation.“ „Noch eine Folie.“ „Noch ein Punkt, ja nichts vergessen.“ '
          'Am Ende funktioniert es trotzdem nicht – weil die ganze Energie in die Präsentation floss und nicht in die Taktik, mit der Du zum Erfolg kommst.</p>'
        + '<p class="lead">Wer sitzt im Raum, wie gewinnst Du diese Entscheider, in welchen Schritten erreichst Du Dein Ziel? Mit diesen Fragen hat sich vorher kaum jemand beschäftigt.</p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:10mm">' + kicker("Die Lösung")
        + '<h2>Die Präsentation ist nie das Ziel.<br>Das Ergebnis ist es.</h2>'
        + '<p class="lead">Wir sind keine Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber. Ein kurzes Briefing, ein paar gezielte Rückfragen, und Du kannst Dir sicher sein, dass es ab&nbsp;hier&nbsp;läuft.</p>'
        + zeitstrahl([("01", "Ergebnis &amp; Zielgruppe", "Welches Ergebnis willst Du – und welche Bedeutung hat Dein Thema für die Zielgruppe?"),
                      ("02", "Business Story", "Warum? Wie? Was jetzt? – verdichtet zu einer klaren Kernbotschaft."),
                      ("03", "Medien", "Aus der Business Story entstehen Medien – gezielt für den jeweiligen Einsatz."),
                      ("04", "Taktisches Briefing", "Dein Vorgehen vor, während und nach dem Termin – bis zum Ergebnis.")])
        + '</div>', 2, N)

    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Schritt 01")
        + '<h2>Ergebnis &amp; <span class="hl">Zielgruppe.</span></h2>'
        + '<p class="lead">Wir arbeiten heraus, welches Ergebnis Du erreichen willst, und strukturieren Dein Thema so, dass es in der Welt Deines Gesprächspartners ankommt.</p>'
        + '<div class="kasten" style="margin-top:9mm"><div class="zwei"><div><p class="label">Die zentrale Frage</p>'
        + '<h3>Welche Bedeutung hat Dein Thema für die Zielgruppe?</h3></div>'
        + '<p style="margin-top:0">Hier liegen die meisten Stolpersteine, und hier entscheidet sich der Erfolg.</p></div></div>'
        + '</div><div class="band band--hell wachsen mitte" style="margin-top:12mm">' + kicker("Die 3 goldenen Regeln")
        + '<h2>Für erfolgreiche Gespräche mit Entscheidern.</h2>'
        + punkte([(i, t, " ".join(ps)) for i, t, ps in REGELN])
        + '<p class="lead" style="margin-top:8mm">Die Frage dahinter: Welche Bedeutung hat Dein Thema in der Welt Deiner Zielgruppe?</p>'
        + '</div>', 3, N)

    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Schritt 02")
        + '<h2>Business <span class="hl">Story.</span></h2>'
        + '<p class="lead">Unabhängig vom Medium erstellen wir Deine Business Story: Warum? Wie? Was jetzt? – und das Ganze abschließend verdichtet zu einer klaren Kernbotschaft.</p>'
        + punkte([("compass", "Why", "Warum ist dieses Thema für die Zielgruppe wichtig?"),
                  ("route", "How", "Wie gehen wir dabei grundsätzlich vor?"),
                  ("signpost", "What next?", "Was muss als Nächstes gemacht werden?")])
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:14mm">' + kicker("Zwischenergebnis · nach Schritt 2")
        + '<h2>Jetzt weißt Du schon, <span class="hl">wie Du gewinnst.</span></h2>'
        + '<p class="lead">Der Weg zum Ziel und Deine Business Story sind geklärt, bevor überhaupt eine Folie entsteht. An dieser Stelle hast Du absolute Handlungsklarheit.</p>'
        + '<p class="lead"><b>Spoiler Alert:</b> Oftmals kommt etwas anderes heraus, als Du am Anfang gedacht hast.</p>'
        + '</div>', 4, N, hell_fuss=True)

    medien = [
        ("", "PowerPoint", "<p>Eine Präsentation, die Deine Business Story trägt – klar strukturiert, professionell gestaltet und startklar für den nächsten großen Moment im Raum.</p>"),
        ("", "Landingpage", "<p>Eine klar auf Deine Zielgruppe zugeschnittene Seite, die genau ein zentrales Problem löst und Interessierte gezielt zum nächsten Schritt führt.</p>"),
        ("", "Roll-up", "<p>Der Gesamtzusammenhang aus Sicht Deiner Zielgruppe – in einem Bild visualisiert und dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist.</p>"),
    ]
    briefing = [
        ("", "Framework", "<p>Briefing auf Basis unseres Frameworks für den optimalen Ablauf eines Termins.</p>"),
        ("", "Storyboard", "<p>Ausführliches Storyboard mit Ablauf, Zeitplan, Sprechtext und Folienvorschau.</p>"),
    ]
    s5 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Schritt 03 · Medien")
        + '<h2>Weit über die klassische PowerPoint hinaus.</h2>'
        + '<p class="lead">Aus der Business Story entstehen professionelle Medien – gezielt für den jeweiligen Einsatz.</p>'
        + liste(medien)
        + '<div class="kasten" style="margin-top:6mm"><div class="zwei"><div><p class="label">Gut zu wissen</p>'
        + '<h3>Bessere KI-Folien allein sind kein Qualitätsmaßstab.</h3></div>'
        + '<p style="margin-top:0">Da reicht es nicht aus, dass die Folien Deiner KI besser aussehen als das, was Du selbst erstellen kannst.</p></div></div>'
        + kicker("Schritt 04 · Taktisches Briefing").replace('class="kicker"', 'class="kicker" style="margin-top:11mm"')
        + '<p class="lead">Dein taktisches Vorgehen unmittelbar vor, während und nach dem Termin: Einstieg, Moderation, und wie Du im Raum dafür sorgst, dass Du Dein Ergebnis bekommst.</p>'
        + liste(briefing)
        + '</div>', 5, N, klasse="seite--hell")

    s6 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Überall dort, wo es zählt")
        + '<h2>Wenn Du Menschen von Deinem Thema <span class="hl">überzeugen willst.</span></h2>'
        + '<p class="lead">Überall dort, wo Du als Führungskraft in der Versicherungsbranche Menschen von Deinem Thema überzeugen willst, sorgen wir dafür, dass Deine Botschaft wirkt.</p>'
        + check(["Vorstand", "Aufsichtsrat", "Projektlenkungsausschuss", "Vertriebstagung",
                 "Betriebsrat", "Kooperationspartner", "Rückversicherer", "Kundenpitch"]).replace('class="check"', 'class="check" style="margin-top:8mm"')
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:14mm">' + kicker("Das Ergebnis")
        + '<h2>Eine Botschaft, die bleibt und Dein <span class="hl">Ziel erreicht.</span></h2>'
        + '<p class="lead">Du gehst bestens vorbereitet in entscheidende Termine. Deine Themen kommen dort an, wo sie ankommen müssen.</p>'
        + '<p class="lead">Und die richtigen Entscheidungen werden getroffen – deshalb werden wir für wichtige Themen immer wieder gebucht.</p>'
        + '</div>', 6, N, hell_fuss=True)

    s7 = seite(kopf(T) + schluss('Wir sind <span class="hl">für Dich da!</span>',
                                 "Lass uns darüber sprechen, welche Themen Dich aktuell bewegen. Gemeinsam klären wir, ob und wie wir Dir weiterhelfen können.",
                                 ["daniel", "kerstin_hr", "noah_pm"]), 7, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
