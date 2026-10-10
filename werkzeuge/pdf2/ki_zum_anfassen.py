"""PDF „KI zum Anfassen“ – Muster für alle 2.0-PDFs (Daniel, 10.10.2026)."""
from lib import (check, titelseite, kopfbild, seite, kopf, kicker, punkte, posts, faelle, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "KI zum Anfassen – empiria"
T = "KI zum Anfassen"

CSS = """
.liste p + p { margin-top: 1.6mm; }
.liste--voll > div { padding: 5.4mm 0; }
.kasten--fokus .zeile { display: grid; grid-template-columns: 42mm 1fr; gap: 8mm; padding: 9.5mm 0; border-bottom: 1px solid rgba(255,255,255,.18); }
.kasten--fokus .zeile:last-child { border-bottom: 0; }
.kasten--fokus .zeile p { margin-top: 0; }
.kasten--fokus .zeile p:not(.label) { font-size: 9.6pt; line-height: 1.6; }
.kasten--fokus .zeile .label { padding-top: 1mm; }
"""

# Beispiele mit den vollen Texten aus den „Mehr lesen“-Fenstern der Seite (Runde 2)
FAELLE = [
    ("Sparring zu verschiedenen Zielgruppen inkl. Ansprache&shy;möglichkeiten", [
        "Ein Produktentwicklungsteam wollte gemeinsam mit Kolleginnen und Kollegen aus dem Marketing herausfinden, wie sich verschiedene KI-Tools als Sparringspartner nutzen lassen – für die Erarbeitung von Zielgruppenprofilen im Versicherungsvertrieb inklusive passender Ansprachemöglichkeiten.",
        "Bewusst wurden dabei auch ungewöhnliche, kreative und auf den ersten Blick unpassende Zielgruppen durchgespielt, um die Grenzen der Tools auszuloten – und danach gezielt mit den vielversprechendsten Ansätzen weiterzuarbeiten."]),
    ("Generierung von Produktideen", [
        "Der Auftrag kam direkt vom Vorstand: Im Unternehmen ging es trotz eigens dafür eingerichteter Bereiche einfach nicht schnell genug voran – es fehlte an neuen Ideen. Im Sparring ging es dabei gar nicht darum, ob die entstandenen Produktideen am Ende umsetzbar sind.",
        "Es ging darum, eingefahrene Denkmuster aufzubrechen, einen echten Impuls zu setzen und gemeinsam mit dem Team den Diskussionsprozess neu in Gang zu bringen – und dabei herauszufinden, an welchen Stellen sich KI auch künftig sinnvoll einsetzen lässt."]),
    ("Erstellung von Ideen für Marketingkampagnen", [
        "Ein Marketingbereich wollte sich digitaler aufstellen und KI-Tools künftig stärker in den Arbeitsalltag integrieren. Da die Nutzung von KI im Konzern aktuell noch vergleichsweise restriktiv geregelt ist, wurde bewusst auf eigenen Geräten und ganz ohne Unternehmens- oder personenbezogene Daten gearbeitet.",
        "So konnte der Marketingleiter mit seinem Team auf der grünen Wiese verschiedene KI-Tools zur Entwicklung von Marketingkampagnen ausprobieren – nicht um fertige Kampagnen mitzunehmen, sondern um einen echten Markteinblick zu bekommen: Was kann KI heute wirklich, jenseits dessen, was in Meetings darüber gemunkelt wird? Aus den Erkenntnissen entstanden konkrete Impulse für die weitere Arbeit im eigenen Haus."]),
    ("Erstellung von textlichem und grafischem Content für Social Media", [
        "Die Leiterin eines Social-Media-Teams kam mit einem klaren Anliegen auf uns zu: verschiedene KI-Tools live ausprobieren, um ein Gefühl dafür zu bekommen, was bei der Erstellung von textlichem und grafischem Content grundsätzlich schon möglich ist – vor allem die textlichen Ergebnisse sollten direkt nutzbar sein.",
        "Unser Vorsprung im Umgang mit den Tools half dabei, einen echten zeitlichen Sprung zu machen, statt bei null anzufangen. Am Ende stand mehr als nur ein erster Eindruck: eine konkrete Entscheidungsvorlage, mit der das Social-Media-Team auswählen konnte, welche Tools es sich für die tägliche Arbeit wirklich wünscht."]),
    ("Entwicklung von HTML-Seiten für Homepages und Intranetseiten", [
        "Angefragt wurde dieses Thema aus ganz unterschiedlichen Bereichen – aus Grundsatzabteilungen, aus der IT, aber auch aus Marketing und Kommunikation. Das Grundverständnis war dabei bereits vorhanden: HTML-Seiten, ob Homepage oder Intranetseite, sind statischen PDFs deutlich überlegen – sie lassen sich einfacher weiterentwickeln, teilweise auswerten (Nutzung, Absprungverhalten) und mit interaktiven Elementen anreichern.",
        "Im Sparring ging es darum, herauszufinden, in welchen Konstellationen sich die Entwicklung solcher Seiten am geschicktesten umsetzen lässt, wie sich dabei Automatisierungen und Agents einbauen lassen, wie unser eigenes Setup dazu aussieht – und welche Tools an welchen Stellen ihre jeweiligen Stärken und Schwächen ausspielen."]),
    ("Hinterfragen des eigenen Geschäftsmodells", [
        "Dieses Thema kam gleich aus zwei Richtungen auf uns zu – einmal direkt vom Vorstand, einmal von der Einheit, die sich um Unternehmensstrategie und Business Development kümmert. Im Kern ging es darum, wie sich das eigene Geschäftsmodell geschickt mit KI hinterfragen lässt: Wie baut man Prompts auf, die wirklich weiterhelfen?",
        "Wie lässt sich KI nutzen, um gezielt Daten im Internet zu recherchieren, Dokumente zu analysieren und daraus eigene Studien und Analysen mit konkreten Ableitungen zu entwickeln? Am Ende stand ein echtes Gefühl dafür, wie sich die Tools praktisch einsetzen lassen – und wie ein Prompt aufgebaut sein muss, damit das Ergebnis wirklich trägt."]),
]
SONDER = (("Ausgangslage", "In vielen Unternehmen ist der Umgang mit KI noch nicht sauber geregelt – dabei ist Führungskräften, die wirklich vorankommen wollen, längst klar, dass sich KI auch privat und unternehmensunabhängig nutzen lässt: um schnell Klarheit zu einzelnen Themen zu bekommen, die eigenen Gedanken zu strukturieren oder sogar während der Autofahrt ein Sparring zu führen – selbstverständlich ohne jegliche Unternehmensdetails preiszugeben."),
          ("Im Sparring", "Genau diese eigene Erfahrung wird im Sparring weitergegeben: wie sich als Führungskraft schlagkräftig und schnell mit KI-Tools agieren lässt, welche Tools sich wofür eignen und welche Alltagstipps und -tricks dabei wirklich weiterhelfen."))


def beispiele(nr, n):
    """Seite 1: Überschrift + drei Fälle; Seite 2: drei Fälle + Sonderthema als schwarzes Band."""
    erste = nr == 4
    faelle = FAELLE[:3] if erste else FAELLE[3:]
    zeilen = "".join(f'<div><h3>{t}</h3><div>' + "".join(f"<p>{x}</p>" for x in ps) + '</div></div>' for t, ps in faelle)
    kopfteil = (kicker("Beispiele") + '<h2>Konkrete Use Cases aus der Praxis.</h2>'
                '<p class="lead" style="max-width:150mm">Eine Auswahl der Themen, die wir mit unseren Kunden bereits in der Praxis umsetzen durften – vom ersten Ausprobieren '
                'bis zum vertieften Kennenlernen der verschiedenen Tools für den eigenen Einsatz oder im gesamten Team.</p>') if erste else kicker("Beispiele")
    return seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kopfteil
                 + f'<div class="liste liste--voll">{zeilen}</div></div>', nr, n, klasse="seite--hell")


def sonderthema(nr, n):
    """Sonderthema mit vollem Text als schwarzes Band (gleicher Aufbau wie „Im Fokus“ bei der Moderation)."""
    return seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Sonderthema")
                 + '<h2>Persönliche KI-Nutzung<br>für Führungskräfte im Alltag.</h2>'
                 + '<p class="lead">Wie Du als Führungskraft KI im Alltag schnell und klug nutzt – ganz ohne Unternehmensdaten preiszugeben.</p>'
                 + '<div class="kasten kasten--fokus" style="margin-top:10mm;padding:5mm 8mm">'
                 + "".join(f'<div class="zeile"><p class="label">{l}</p><p>{x}</p></div>' for l, x in SONDER)
                 + '</div></div>', nr, n, klasse="seite--hell")


def bauen():
    n = 7
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
        + punkte([("zap", "Direkt in die praktische Anwendung", "Kein weiterer Arbeitskreis, keine Theorie von Menschen, die KI selbst noch nie genutzt haben – wir starten sofort, mit echtem, direktem Mehrwert für Dein Unternehmen."),
                  ("layers", "Verschiedene Tools im Vergleich", "Wir arbeiten mit mehreren KI-Tools gleichzeitig und erleben live, wie unterschiedlich sie denken und welche Ergebnisse sie liefern."),
                  ("target", "Echte Usecases, echte Erkenntnisse", "Wir spielen Anwendungsfälle durch, die für ein Versicherungsunternehmen wirklich relevant sind – und bringen direkt verwertbare Erkenntnisse mit.")])
        + '</div><div class="rand" style="padding-top:14mm">' + kicker("Die Werkzeuge")
        + '<h2>Mehrere Tools im direkten Vergleich.</h2><p class="lead">Wir zeigen an Euren Fällen, wie unterschiedlich die Tools denken und liefern.</p>'
        + '<div class="logos" style="grid-template-columns:repeat(3,1fr);row-gap:11mm;margin-top:13mm">' + "".join(
            f'<div><img src="assets/tools/{d}-magenta.png" alt="" style="height:13mm"><b style="font-size:9pt">{t}</b></div>' for d, t in
            [("chatgpt", "ChatGPT"), ("claude", "Claude"), ("perplexity", "Perplexity"), ("gemini", "Gemini"), ("notebooklm", "NotebookLM"), ("nanobanana", "Nano Banana")])
        + '</div>'
        + '</div>', 2, n)

    # Daniel 10.10.: Formate als Vergleichstabelle (B) mit schwarzem Kasten (A), Beispiele als Liste (B)
    import ki_varianten
    kasten = ('<div class="kasten" style="margin-top:7mm"><p class="label">In jedem Format enthalten</p>'
              + punkte([("clipboard-list", "Vorbereitung", "Wir stimmen Fragestellung und Teilnehmende vorab mit Dir ab."),
                        ("layers", "Mehrere Tools", "Ihr arbeitet live mit verschiedenen KI-Tools an Euren Fällen."),
                        ("file-text", "Dokumentation", "Die Ergebnisse bekommst Du sauber dokumentiert für das weitere Vorgehen.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;')
              + '</div>')
    # ki_varianten rechnet mit 5 Seiten – Seitenzahl im Fuß auf 6 setzen (ki_varianten bleibt unverändert)
    s3 = ki_varianten.formate_tabelle(3, kasten).replace("<span>03 / 05</span>", f"<span>03 / {n:02d}</span>")
    s4, s5, s6 = beispiele(4, n), beispiele(5, n), sonderthema(6, n)

    s7 = seite(
        kopf("KI zum Anfassen") + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit, KI <span class="hl">wirklich anzufassen?</span></h2>'
        + '<p class="lead">Sag uns, welche Fragestellung bei Euch ansteht und wer dabei sein soll – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "noah_ki"]) + kontaktdaten() + '</div></div>', 7, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
