"""PDF „Sprint Landingpage“ im Stil des Musters „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument, ico)

TITEL = "Sprint Landingpage – empiria"
T = "Sprint Landingpage"

CSS = """
.vergleich { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm; margin-top: 8mm; }
.vergleich > div { border-top: 1.6px solid #1a1817; padding-top: 4.5mm; }
.vergleich .label { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.vergleich h3 { margin-top: 2mm; }
.vergleich p { margin-top: 2mm; font-size: 9pt; line-height: 1.55; color: #3d3a37; }
.paket { display: grid; grid-template-columns: 62mm 1fr; margin-top: 9mm; border-radius: 4.5mm; overflow: hidden; }
.paket__preis { background: #fff400; padding: 7mm 7mm 8mm; display: flex; flex-direction: column; justify-content: space-between; }
.paket__preis small { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.paket__preis h3 { margin-top: 2.5mm; font-size: 13pt; }
.paket__preis b { white-space: nowrap; font-family: 'Lora', Georgia, serif; font-size: 24pt; line-height: 1; letter-spacing: -.01em; }
.paket__preis svg { width: 12mm; height: 12mm; flex: 0 0 auto; }
.paket__unten { display: flex; justify-content: space-between; align-items: flex-end; gap: 3mm; }
.seite--hell .liste > div { padding: 6.6mm 0; }
.seite--hell .liste p { font-size: 9.2pt; }
.paket__liste { background: #1a1817; color: #fff; padding: 7mm 8mm; list-style: none; }
.paket__liste li { position: relative; padding: 2.6mm 0 2.6mm 8mm; border-bottom: 1px solid rgba(255,255,255,.18); font-size: 9.2pt; }
.paket__liste li:last-child { border-bottom: 0; }
.paket__liste li::before { content: ""; position: absolute; left: .5mm; top: 4.2mm; width: 3mm; height: 1.6mm; border-left: 1.6px solid #fff400; border-bottom: 1.6px solid #fff400; transform: rotate(-45deg); }
.zs .meta { display: block; margin-top: 1.2mm; font-size: 7.6pt; font-weight: 600; }
"""


def bauen():
    n = 6
    s1 = seite(titelseite(
        "Sprint Landingpage", '<span class="hl">Schnell live.</span><br>Klar im Fokus.<br>Volle Wirkung.',
        "Wenn es schnell gehen muss: Im Sprint entwickeln wir Deine fokussierte Landingpage – ohne Abstriche bei Qualität, Layout und Wirkung.",
        kopfbild("Sprint Landingpage"),
        [("Ablauf", "Onboarding, Sprint, Review"), ("Umfang", "Fix &amp; fokussiert"), ("Technik", "Mobil optimiert"), ("Investition", "15.850 €")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:14mm;padding-bottom:14mm">' + kicker("Erfolgsfaktor")
        + '<h2>So funktioniert Deine<br>Landingpage optimal.</h2>'
        + '<p class="lead">Eine Landingpage richtet sich an eine klar definierte Zielgruppe und löst genau ein zentrales Problem dieser Zielgruppe – mit vertrieblichem Ziel.</p>'
        + punkte([("target", "Ein Fokus", "Eine Zielgruppe, ein Problem, eine Lösung – keine Ablenkung durch andere Themen."),
                  ("users", "Zugeschnitten", "Visualisierung, Ansprache und Argumente exakt auf diese Zielgruppe zugeschnitten."),
                  ("flag", "Ein klares Ziel", "Nie alles erklären, immer der nächste Schritt: Kontaktdaten, Webinar-Anmeldung oder Download mit echtem Mehrwert.")])
        + '</div><div class="rand" style="padding-top:16mm">' + kicker("Der Unterschied")
        + '<h2>Hier bin ich richtig.</h2>'
        + '<p class="lead">Schon im Header muss die Zielgruppe das Gefühl bekommen: Hier finde ich eine Lösung für mein Thema.</p>'
        + '<div class="vergleich">'
        + '<div><p class="label">Homepage</p><h3>Ein Sammelsurium an Themen</h3><p>Zum Unternehmen, zum Team, zu Produkten. Besucher müssen sich zurechtfinden und selbst suchen, was sie wollen.</p></div>'
        + '<div><p class="label">Landingpage</p><h3>Ein Thema, ein Ziel</h3><p>Eine klar definierte Zielgruppe, ein zentrales Problem und der Fokus auf den nächsten Schritt.</p></div>'
        + '</div></div>', 2, n)

    s3 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>Drei Schritte zur<br><span class="hl">fertigen Landingpage.</span></h2>'
        + '<p class="lead">So läuft der Sprint konkret ab –<br>von der Vorbereitung bis zum Go&#8209;live.</p>'
        + zeitstrahl([("01 · 2–3 Std. · online", "Onboarding", "Wir klären Zielgruppe, Problem und Ziel – damit der Sprint vom ersten Moment an sitzt."),
                      ("02 · 2 Tage · Präsenz", "Sprint-Workshop", "<b>Tag 1:</b> Sparring &amp; parallele Entwicklung der Rohversion.<br><b>Tag 2:</b> Vorstellung, Feedback, Feinschliff &amp; Go-live."),
                      ("03 · im Nachgang", "Review", "Kurzes Fazit: Hat alles gepasst, wie war das Feedback – und wo gibt es noch gezielten Anpassungsbedarf?")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:16mm">' + kicker("Das Versprechen")
        + '<h2>Tempo ohne Kompromisse.</h2>'
        + punkte([("timer", "Schneller Start", "Kein monatelanger Prozess – wir starten in den Sprint, sobald der Rahmen steht."),
                  ("layout-grid", "Fokussierter Umfang", "Ein klar begrenztes Set an Inhalten und Elementen, damit der Sprint hält, was er verspricht."),
                  ("circle-check", "Ohne Kompromisse", "Trotz Tempo: sauber gebaut, mobil optimiert und technisch startklar.")])
        + '</div>', 3, n)

    liste = ["Konzeption, Text &amp; Design Deiner vollständigen Landingpage", "Umsetzung im zweitägigen Sprint-Workshop bei Dir vor Ort",
             "Feedbackrunde &amp; Feinschliff direkt im Workshop", "Live-Schaltung Deiner Landingpage im Anschluss an den Sprint",
             "Review im Nachgang, damit alles wie gewünscht läuft", "Durchgeführt von 2 Beraterinnen und Beratern von empiria"]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Investition")
        + '<h2>Ein Paket, ein Preis.</h2>'
        + '<p class="lead">Klar kalkuliert statt versteckter Zusatzkosten: Konzeption, Umsetzung und Live-Schaltung in einem Leistungspaket.</p>'
        + '<div class="paket"><div class="paket__preis"><div><small>Dein Leistungspaket</small><h3>Sprint-Landingpage</h3></div>'
        + f'<div class="paket__unten"><b>15.850 €</b>{ico("rocket", strich=1.3)}</div></div>'
        + '<ul class="paket__liste">' + "".join(f"<li>{x}</li>" for x in liste) + '</ul></div>'
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe sowie zzgl. Spesen (Anfahrt und zwei Übernachtungen für je zwei Personen).</p>'
        + '</div><div class="band band--hell wachsen" style="margin-top:14mm;padding-top:14mm">' + kicker("Für wen das gemacht ist")
        + '<h2>Wenn es schnell gehen muss.</h2>'
        + check(["Bereiche mit kurzfristigem Vertriebspush, etwa im Endjahresgeschäft", "Teams vor Messe, Event oder Vertriebstagung",
                 "Marketing, dem jemand ausgefallen ist und der Termin trotzdem steht", "Alle, die zeigen wollen, dass es auch schnell und sauber geht"])
        + '</div>', 4, n)

    faelle = [
        ("Dynamik in den Kreativworkshop bringen", "Das Thema wird gezielt in einem Kreativworkshop eingesetzt, damit es danach direkt weitergeht. So werden Ergebnisse nicht unnötig verzögert und gehen im Nachgang nicht unter."),
        ("Schnell auf eine Vertriebssituation reagieren", "Eine Marktchance oder eine Marktveränderung ist aufgekommen. Oder es soll kurzfristig ein Push für den Vertrieb gesetzt werden – etwa im Endjahresgeschäft."),
        ("Eine Situation retten", "Etwas wurde schlicht vergessen oder jemand im Marketing ist ausgefallen. Aber ein wichtiger Termin steht an: eine Messe, ein Event, ein Vertriebsmeeting, ein Produktlaunch."),
        ("Zum Wachrütteln", "Diskussionen im Unternehmen ziehen sich lange hin, mit vielen Erklärungen, warum etwas nicht möglich ist. Der Sprint beweist, dass es auch schnell und professionell geht."),
        ("Als Methodiktraining im Marketing", "Der Sprint gibt Einblick in eine schlagkräftige Methodik. Sie wird als Schulung fürs eigene Marketingteam nutzbar."),
        ("Kunden &amp; Partner begeistern", "Sehr schnell entsteht eine einsetzbare Lösung, die Kunden, Kooperations- und Vertriebspartner begeistert – etwa große Makler, Bankpartner oder Partner in einem neuen Ländermarkt."),
    ]
    s5 = seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Anwendungsfälle")
               + '<h2>Typische Anwendungsfälle.</h2><p class="lead">So setzen Unternehmen den Sprint konkret ein.</p>'
               + '<div class="liste">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
               + '</div>', 5, n, klasse="seite--hell")

    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Deine Seite<br><span class="hl">in 48 Stunden?</span></h2>'
        + '<p class="lead">Sag uns, um welches Thema es geht und wann der Sprint starten soll – wir melden uns mit einem unverbindlichen Angebot.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Thema, Zielgruppe und Wunschtermin für den Sprint – eine Mail oder ein Anruf reicht."),
                      ("02", "Angebot erhalten", "Wir melden uns zeitnah, um alles Weitere persönlich zu besprechen."),
                      ("03", "Sprint starten", "Onboarding, zwei Tage Sprint bei Dir vor Ort – und Deine Landingpage ist live.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "noah_pm"]) + kontaktdaten() + '</div></div>', 6, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=CSS)
