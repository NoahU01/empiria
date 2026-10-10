"""PDF „Innovation & Geschäftsmodell neu denken“ – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/innovation.html (die Seite hat keine Pop-ups)."""
from lib import (titelseite, seite, kopf, kicker, punkte, dokument)
from _strategie_teile import TEAM3_CSS, LISTE_CSS, zeichen, schluss

TITEL = "Innovation & Geschäftsmodell neu denken – empiria"
T = "Innovation &amp; Geschäftsmodell"
N = 5

CSS = TEAM3_CSS + LISTE_CSS


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Innovation &amp; Geschäftsmodell <span class="hl">neu denken.</span>',
        "Neue Ideen, neues Geschäftsmodell: Was davon hat in zehn Jahren noch Bestand? Wir hinterfragen und strukturieren es mit Dir.",
        zeichen("kreis", 80),
        [("Für", "Unternehmen &amp; Bereiche"), ("Themen", "Kooperationen, Fusionen, Beteiligungen"),
         ("Ansatz", "Neu gründen, ohne Altlasten"), ("Ergebnis", "Entscheidungen mit Substanz")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Das Problem")
        + '<h2>Du entwickelst weiter. Bevor die Grundfrage <span class="hl">geklärt ist.</span></h2>'
        + '<p class="lead">Eine Idee für ein neues Geschäftsmodell oder Produkt entsteht, und sofort wird an Features, Prozessen und der Umsetzung gefeilt.</p>'
        + kicker("Dabei bleibt offen").replace('class="kicker"', 'class="kicker" style="margin-top:9mm"')
        + punkte([("search", "Welches Problem hat der Kunde eigentlich?", ""), ("puzzle", "Wie löst Du es?", ""),
                  ("handshake", "Ist er überhaupt bereit, es zu lösen?", "")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
        + '<p class="lead" style="margin-top:7mm">… diese Fragen bleiben unbeantwortet, während längst weitergebaut wird.</p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Nichts davon ist in Stein gemeißelt.</h2>'
        + '<p class="lead">Wer sein Geschäftsmodell wirklich hinterfragt, stößt schnell an eine Grenze: Vieles gilt als gegeben, nur weil es schon immer so war – dabei ist es oft längst nicht mehr in Stein gemeißelt.</p>'
        + '<p class="lead">Genau hier gehen wir mit Dir grundlegend ran, sei es für das gesamte Unternehmen oder für einzelne Bereiche.</p>'
        + '</div>', 2, N)

    einsatz = [("trending-up", "Zukunft des Geschäfts&shy;modells", ""), ("handshake", "Kooperationen", ""), ("blocks", "Fusionen", ""),
               ("briefcase", "Beteiligungen", ""), ("sparkles", "Neue Zusatz&shy;services", "")]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + '<div class="kasten" style="padding:8mm 8mm 9mm"><p class="label">Gilt als gegeben</p>'
        + punkte([("refresh-cw", "„Das war schon immer&nbsp;so.“", ""), ("lock", "„Das ist bei uns gesetzt.“", ""),
                  ("shield-check", "„Das macht man in unserer Branche nicht.“", "")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
        + '<h2 style="color:#fff;margin-top:8mm">Und was, wenn nicht?</h2></div>'
        + '</div><div class="band band--hell wachsen mitte" style="margin-top:14mm">' + kicker("Einsatzmöglichkeiten")
        + '<h2>Für das gesamte Unternehmen oder für <span class="hl">einzelne Bereiche.</span></h2>'
        + '<p class="lead">Dies gilt für die Zukunft Eures Geschäftsmodells genauso wie für konkrete Fragen zu Kooperationen, Fusionen, Beteiligungen oder neuen Zusatzservices.</p>'
        + punkte(einsatz, spalten=5).replace('<div class="punkte" style="', '<div class="punkte" style="gap:6mm;')
        + '</div>', 3, N)

    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Unsere Methoden")
        + '<h2>Wir nutzen Methoden, um <span class="hl">Erkenntnisse zu schaffen.</span></h2>'
        + '<p class="lead">Wir bringen dafür eigene Methoden und Frameworks mit und helfen Dir, Dich von genau diesen alten Denkmustern zu lösen. Wir wenden sie nicht unreflektiert an.</p>'
        + '<div class="kasten" style="margin-top:9mm"><div class="zwei"><div><p class="label">Ein bewährter Ansatz</p>'
        + '<h3>Als würdet Ihr Euer Thema morgen neu gründen.</h3></div>'
        + '<p style="margin-top:0">Wir denken mit Dir so, als würdet Ihr Euer Thema morgen als eigenes Unternehmen neu gründen – ganz ohne Altlasten.</p></div></div>'
        + '</div><div class="band band--schwarz dunkel wachsen mitte" style="margin-top:14mm">' + kicker("Das Ergebnis")
        + '<h2>Du weißt, ob die <span class="hl">Idee trägt.</span></h2>'
        + '<p class="lead">Du verstehst, worauf es in Eurem Geschäftsmodell wirklich ankommt – heute und in Zukunft. '
          'Ihr trefft Entscheidungen zu Innovation, Kooperationen oder Investitionen mit echter Substanz dahinter.</p>'
        + '<p class="lead">Und Ihr traut Euch, auch mal ganz neu zu denken.</p>'
        + '</div>', 4, N, hell_fuss=True)

    s5 = seite(kopf(T) + schluss('Wir sind <span class="hl">für Dich da!</span>',
                                 "Lass uns darüber sprechen, welche Themen Dich aktuell bewegen. Gemeinsam klären wir, ob und wie wir Dir weiterhelfen können.",
                                 ["daniel", "kerstin_hr", "noah_pm"]), 5, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
