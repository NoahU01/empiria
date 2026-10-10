"""PDF „Innovation & Geschäftsmodell neu denken“ – im Muster „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Innovation & Geschäftsmodell neu denken – empiria"
T = "Innovation &amp; Geschäftsmodell"
N = 5


def zeichen(name):
    """Großes, gefülltes Themen-Zeichen der Homepage (e2_bauen.FORM / THEMEN_ZEICHEN), schwarz."""
    import e2_bauen
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg class="zeichen" viewBox="{vb}" aria-hidden="true" fill="#1a1817" color="#1a1817">{e2_bauen.FORM[name]}</svg>'


CSS = """
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p, .sub, .text { text-wrap: pretty; }
.titel .bild svg.zeichen { width: 80mm; }
.reihe { display: grid; gap: 7mm; margin-top: 5mm; }
.reihe > div { border-top: 1.6px solid #1a1817; padding-top: 4mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.25; }
.label-s { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-top: 9mm; }
.text { font-size: 9.6pt; line-height: 1.6; margin-top: 6mm; max-width: 150mm; }
.satz { font-size: 9.6pt; line-height: 1.6; margin-top: 9mm; max-width: 140mm; }
.gegeben { display: grid; grid-template-columns: repeat(3, 1fr); gap: 7mm; margin-top: 5mm; }
.gegeben > div { border-top: 1px solid rgba(255,255,255,.3); padding-top: 4mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 14pt; line-height: 1.3; color: #fff; }
.pills { display: flex; flex-wrap: wrap; gap: 3.5mm; margin-top: 9mm; }
.pills span { border: 1.6px solid #1a1817; border-radius: 9mm; padding: 3mm 6mm; background: #fff; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12pt; }
.kasten .frage { margin-top: 6mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 17pt; color: #fff; }
.schluss .zwei { grid-template-columns: 99mm 1fr; gap: 8mm; }
.schluss .team { gap: 3mm; }
.schluss .person { width: 31mm; }
.schluss .person img { width: 24mm; height: 24mm; }
"""


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Innovation &amp; Geschäftsmodell <span class="hl">neu denken.</span>',
        "Neue Ideen, neues Geschäftsmodell: Was davon hat in zehn Jahren noch Bestand? Wir hinterfragen und strukturieren es mit Dir.",
        zeichen("kreis"),
        [("Zukunft", "Des Geschäftsmodells"), ("Partner", "Kooperationen &amp; Fusionen"),
         ("Invest", "Beteiligungen"), ("Angebot", "Neue Zusatzservices")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:14mm">' + kicker("Das Problem")
        + '<h2>Du entwickelst weiter. Bevor die Grundfrage <span class="hl">geklärt ist.</span></h2>'
        + '<p class="lead">Eine Idee für ein neues Geschäftsmodell oder Produkt entsteht, und sofort wird an Features, Prozessen und der Umsetzung gefeilt.</p>'
        + '<p class="label-s">Dabei bleibt offen</p>'
        + '<div class="reihe" style="grid-template-columns:repeat(3,1fr)"><div>Welches Problem hat der Kunde eigentlich?</div><div>Wie löst Du es?</div><div>Ist er überhaupt bereit, es zu lösen?</div></div>'
        + '<p class="text">… diese Fragen bleiben unbeantwortet, während längst weitergebaut wird.</p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Nichts davon ist in Stein gemeißelt.</h2>'
        + '<p class="lead" style="max-width:150mm">Wer sein Geschäftsmodell wirklich hinterfragt, stößt schnell an eine Grenze: Vieles gilt als gegeben, nur weil es schon immer so war.</p>'
        + punkte([("search", "Grundfragen geklärt", "Kundenproblem, Lösung und Zahlungsbereitschaft – bevor weitergebaut wird."),
                  ("puzzle", "Altlasten hinterfragt", "Was wirklich gesetzt ist und was nur so aussieht."),
                  ("compass", "Klare Entscheidungen", "Mit Substanz für Innovation, Kooperation oder Investition.")])
        + '<p class="satz">Genau hier gehen wir mit Dir grundlegend ran – sei es für das gesamte Unternehmen oder für einzelne Bereiche.</p>'
        + '</div>', 2, N)

    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + '<div class="kasten" style="padding:10mm 10mm 11mm"><p class="label">Gilt als gegeben</p>'
        + '<div class="gegeben"><div>„Das war schon immer so.“</div><div>„Das ist bei uns gesetzt.“</div><div>„Das macht man in unserer Branche nicht.“</div></div>'
        + '<p class="frage">Und was, wenn nicht?</p></div>'
        + '</div><div class="band band--hell wachsen mitte" style="margin-top:16mm">' + kicker("Einsatzmöglichkeiten")
        + '<h2>Für das gesamte Unternehmen<br>oder für einzelne Bereiche.</h2>'
        + '<p class="lead" style="max-width:150mm">Dies gilt für die Zukunft Eures Geschäftsmodells genauso wie für konkrete Fragen zu Kooperationen, Fusionen, Beteiligungen oder neuen Zusatzservices.</p>'
        + '<div class="pills">' + "".join(f'<span>{x}</span>' for x in ["Zukunft des Geschäftsmodells", "Kooperationen", "Fusionen", "Beteiligungen", "Neue Zusatzservices"]) + '</div>'
        + '</div>', 3, N)

    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Unsere Methoden")
        + '<h2>Methoden schaffen Erkenntnis. <span class="hl">Nicht umgekehrt.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Wir bringen eigene Methoden und Frameworks mit und helfen Dir, Dich von genau diesen alten Denkmustern zu lösen. '
          'Wir nutzen Methoden, um Erkenntnisse zu schaffen – wir wenden sie nicht unreflektiert an.</p>'
        + '<div class="kasten" style="margin-top:10mm;padding:8mm 9mm 9mm"><div class="zwei"><div><p class="label">Ein bewährter Ansatz</p>'
        + '<h3>Als würdet Ihr Euer Thema morgen neu gründen.</h3></div>'
        + '<p style="margin-top:0">Wir denken mit Dir so, als würdet Ihr Euer Thema morgen als eigenes Unternehmen neu gründen – ganz ohne Altlasten.</p></div></div>'
        + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:13mm"')
        + check(["Vorstände, die das Geschäftsmodell grundlegend hinterfragen wollen", "Bereiche vor Entscheidungen zu Kooperationen oder Fusionen",
                 "Strategie und Business Development bei Beteiligungsfragen", "Teams, die neue Zusatzservices ernsthaft prüfen wollen"])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Das Ergebnis")
        + '<h2>Du weißt, ob die Idee trägt.</h2>'
        + '<p class="lead" style="max-width:150mm">Du verstehst, worauf es in Eurem Geschäftsmodell wirklich ankommt – heute und in Zukunft. '
          'Ihr trefft Entscheidungen zu Innovation, Kooperationen oder Investitionen mit echter Substanz dahinter.</p>'
        + '<p class="satz" style="font-family:\'Lora\',Georgia,serif;font-weight:700;font-size:15pt;line-height:1.3">Und Ihr traut Euch, auch mal ganz neu zu denken.</p>'
        + '</div>', 4, N)

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Welche Idee soll auf den <span class="hl">Prüfstand?</span></h2>'
        + '<p class="lead">Lass uns darüber sprechen, welche Themen Dich aktuell bewegen. Gemeinsam klären wir, ob und wie wir Dir weiterhelfen können.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte schluss" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr", "noah_pm"]) + kontaktdaten() + '</div></div>', 5, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
