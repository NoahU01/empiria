"""PDF „KI zum Anfassen“ – Muster für alle 2.0-PDFs (Daniel, 10.10.2026)."""
from lib import (check, titelseite, kopfbild, seite, kopf, kicker, punkte, posts, faelle, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "KI zum Anfassen – empiria"


def bauen():
    n = 5
    s1 = seite(titelseite(
        "KI zum Anfassen", 'Deine KI.<br><span class="hl">Zum Anfassen.</span><br>Volle Wirkung.',
        "Über KI wird geredet – oft von Menschen, die sie selbst noch nie genutzt haben. Wir gehen direkt in die Anwendung: "
        "verschiedene KI-Tools, echte Fälle aus Eurem Alltag, Erkenntnisse, die sofort etwas bringen.",
        kopfbild("KI zum Anfassen"),
        [("Format", "½ bis 2 Tage"), ("Tools", "ChatGPT, Claude, Gemini &amp; mehr"), ("Fokus", "Echte Usecases"), ("Investition", "ab 2.500 €")]))

    s2 = seite(
        kopf("KI zum Anfassen")
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Das bekommst Du")
        + '<h2>Anwendung statt Vortrag.</h2><p class="lead">Wir reden nicht über KI – wir nutzen sie, gemeinsam mit Dir und Deinem Team.</p>'
        + punkte([("sliders-horizontal" if False else "zap", "Direkt in die Anwendung", "Kein weiterer Arbeitskreis, keine Theorie – wir starten sofort, mit direktem Mehrwert für Dein Unternehmen."),
                  ("layers", "Tools im Vergleich", "Mehrere KI-Tools gleichzeitig – live erleben, wie unterschiedlich sie denken und welche Ergebnisse sie liefern."),
                  ("target", "Echte Usecases", "Anwendungsfälle, die für Versicherer wirklich relevant sind – mit direkt verwertbaren Erkenntnissen.")])
        + '</div><div class="rand" style="padding-top:10mm">' + kicker("Die Werkzeuge")
        + '<h2>Mehrere Tools im direkten Vergleich.</h2><p class="lead">Wir zeigen an Euren Fällen, wie unterschiedlich die Tools denken und liefern.</p>'
        + '<div class="logos" style="grid-template-columns:repeat(6,1fr)">' + "".join(
            f'<div><img src="assets/tools/{d}-magenta.png" alt=""><b>{t}</b></div>' for d, t in
            [("chatgpt", "ChatGPT"), ("claude", "Claude"), ("perplexity", "Perplexity"), ("gemini", "Gemini"), ("notebooklm", "NotebookLM"), ("nanobanana", "Nano Banana")])
        + '</div>' + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:10mm"')
        + check(["Vorstände, die im Haus mehr Tempo bei neuen Ideen wollen", "Grundsatz- und Strategieabteilungen mit Analysebedarf",
                 "Marketing und Kommunikation für schnellere Inhalte", "Führungskräfte, die selbst schlagkräftiger werden wollen"])
        + '</div>', 2, n)

    # Daniel 10.10.: Formate als Vergleichstabelle (B) mit schwarzem Kasten (A), Beispiele als Liste (B)
    import ki_varianten
    kasten = ('<div class="kasten" style="margin-top:7mm"><p class="label">In jedem Format enthalten</p>'
              + punkte([("clipboard-list", "Vorbereitung", "Wir stimmen Fragestellung und Teilnehmende vorab mit Dir ab."),
                        ("layers", "Mehrere Tools", "Ihr arbeitet live mit verschiedenen KI-Tools an Euren Fällen."),
                        ("file-text", "Dokumentation", "Die Ergebnisse bekommst Du sauber dokumentiert für das weitere Vorgehen.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
              + '</div>')
    s3 = ki_varianten.formate_tabelle(3, kasten)
    s4 = ki_varianten.beispiele_liste(4)

    s5 = seite(
        kopf("KI zum Anfassen") + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit, KI <span class="hl">wirklich anzufassen?</span></h2>'
        + '<p class="lead">Sag uns, welche Fragestellung bei Euch ansteht und wer dabei sein soll – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "noah_ki"]) + kontaktdaten() + '</div></div>', 5, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5])
