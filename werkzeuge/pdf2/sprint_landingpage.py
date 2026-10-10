"""PDF „Sprint Landingpage“ – Runde 2 (10.10.2026): Inhalt = aktuelle 2.0-Seite inkl. Pop-ups
(Vorschau „Aufbau der Landingpage“, alle „Mehr lesen“-Texte). „48“ steht nur im Titelbild."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument, ico)

TITEL = "Sprint Landingpage – empiria"
T = "Sprint Landingpage"

# Sonderbausteine: Homepage/Landingpage-Vergleich und das Leistungspaket (eine Spalte – keine Vergleichstabelle möglich)
CSS = """
.vergleich { display: grid; grid-template-columns: 1fr 1fr; gap: 8mm; margin-top: 9mm; }
.vergleich > div { border-top: 1.6px solid #1a1817; padding-top: 4.5mm; }
.vergleich .label { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.vergleich h3 { margin-top: 2mm; }
.vergleich p { margin-top: 2mm; font-size: 9pt; line-height: 1.55; color: #3d3a37; }
.paket { display: grid; grid-template-columns: 62mm 1fr; margin-top: 14mm; border-radius: 4.5mm; overflow: hidden; }
.paket__preis { background: #fff400; padding: 9mm 7mm 9mm; display: flex; flex-direction: column; justify-content: space-between; }
.paket__preis small { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; }
.paket__preis h3 { margin-top: 2.5mm; }
.paket__preis b { white-space: nowrap; font-family: 'Lora', Georgia, serif; font-size: 24pt; line-height: 1; letter-spacing: -.01em; }
.paket__preis svg { width: 12mm; height: 12mm; flex: 0 0 auto; }
.paket__unten { display: flex; justify-content: space-between; align-items: flex-end; gap: 3mm; }
.paket__liste { background: #1a1817; color: #fff; padding: 8mm 9mm; list-style: none; }
.paket__liste li { position: relative; padding: 4.6mm 0 4.6mm 8mm; border-bottom: 1px solid rgba(255,255,255,.18); font-size: 9.2pt; }
.paket__liste li:last-child { border-bottom: 0; }
.paket__liste li::before { content: ""; position: absolute; left: .5mm; top: 6.2mm; width: 3mm; height: 1.6mm; border-left: 1.6px solid #fff400; border-bottom: 1.6px solid #fff400; transform: rotate(-45deg); }
.aufbau > div { grid-template-columns: 11mm 62mm 1fr; gap: 4mm; align-items: center; padding: 4.6mm 0; }
.aufbau svg { width: 5.5mm; height: 5.5mm; }
.zs .tag { display: block; margin-top: 1.6mm; font-size: 8.6pt; line-height: 1.5; }
"""


def bauen():
    n = 7
    s1 = seite(titelseite(
        "Sprint Landingpage", '<span class="hl">Schnell live.</span><br>Klar im Fokus.<br>Volle Wirkung.',
        "Wenn es schnell gehen muss: Im Sprint entwickeln wir Deine fokussierte Landingpage – ohne Abstriche bei Qualität, Layout und Wirkung.",
        kopfbild("Sprint Landingpage"),
        [("Ablauf", "Onboarding, Sprint, Review"), ("Sprint", "2 Tage bei Dir vor&nbsp;Ort"), ("Technik", "Mobil optimiert"), ("Investition", "15.850 €")]))

    # Erfolgsfaktor (Seite hat kein Problem → gelbes Band mit den vier Punkten der Seite)
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:13mm;padding-bottom:13mm">' + kicker("Erfolgsfaktor")
        + '<h2>So funktioniert Deine<br>Landingpage optimal.</h2>'
        + '<p class="lead">Eine Landingpage richtet sich an eine klar definierte Zielgruppe und löst genau ein zentrales Problem dieser Zielgruppe – mit vertrieblichem Ziel.</p>'
        + punkte([("target", "Ein Fokus", "Eine Zielgruppe, ein Problem, eine Lösung – keine Ablenkung durch andere Themen."),
                  ("users", "Zugeschnitten", "Visualisierung, Ansprache und Argumente exakt auf diese Zielgruppe zugeschnitten."),
                  ("signpost", "Der nächste Schritt", "Nie der Anspruch, alles zu erklären – immer der Fokus auf den nächsten Schritt."),
                  ("flag", "Ein klares Ziel", "Kontaktdaten, Webinar-Anmeldung oder Download mit echtem Mehrwert.")], spalten=4)
        + '</div><div class="rand" style="padding-top:14mm">' + kicker("Der Unterschied")
        + '<h2>Hier bin ich richtig.</h2>'
        + '<p class="lead">Schon im Header muss die Zielgruppe das Gefühl bekommen: Hier bin ich richtig, hier finde ich eine Lösung für mein Thema.</p>'
        + '<div class="vergleich">'
        + '<div><p class="label">Homepage</p><h3>Ein Sammelsurium an Themen</h3><p>Zum Unternehmen, zum Team, zu Produkten. Besucher müssen sich zurechtfinden und selbst suchen, was sie wollen.</p></div>'
        + '<div><p class="label">Landingpage</p><h3>Ein Thema, ein Ziel</h3><p>Eine klar definierte Zielgruppe, ein zentrales Problem und der Fokus auf den nächsten Schritt.</p></div>'
        + '</div></div>', 2, n)

    # Pop-up „Vorschau ansehen“: Aufbau der Landingpage
    teile = [("app-window", "Header", "Erster Eindruck, Navigation &amp; ggf. Testimonials"),
             ("search", "Problem", "Die Ausgangslage, die Dein Gegenüber wiedererkennt"),
             ("star", "Lösung &amp; USP", "Dein Angebot und was Dich unterscheidet"),
             ("route", "Ablauf / Zusammenarbeit", "Wie die Zusammenarbeit konkret abläuft"),
             ("users", "About us", "Wer dahintersteht – Vertrauen durch Gesicht"),
             ("file-text", "Leadmagnet", "Ein Mehrwert im Tausch gegen Kontaktdaten"),
             ("mail", "Kontakt", "Der letzte Schritt zur Anfrage"),
             ("layers", "Footer", "Rechtliches &amp; ergänzende Links")]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Aufbau der Landingpage")
        + '<h2>Grundlegende Struktur<br>der Landingpage.</h2>'
        + '<p class="lead" style="max-width:150mm">Jede Landingpage folgt einem klar durchdachten Aufbau: ein eindeutiges Ziel, eine genau definierte Zielgruppe '
          'und ein thematischer Einstieg, der diese Zielgruppe so abholt, dass sie bereit ist, den nächsten Schritt zu gehen.</p>'
        + '<div class="liste aufbau">' + "".join(f'<div>{ico(i)}<h3>{t}</h3><p>{p}</p></div>' for i, t, p in teile) + '</div>'
        + '<div class="kasten" style="margin-top:10mm"><div class="zwei"><div><p class="label">Für Dein Thema</p><h3>Gezielt angepasst</h3></div>'
        + '<p style="margin-top:0">Für Dein Thema passen wir diesen Aufbau gezielt an. Denn nicht jede Sektion ist bei jedem Thema zwingend notwendig oder sinnvoll.</p></div></div>'
        + '</div>', 3, n)

    # Ablauf: Zeitstrahl im gelben Band, die drei Zusagen der Seite darunter
    s4 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:15mm;padding-bottom:17mm">' + kicker("Ablauf")
        + '<h2>Drei Schritte zur<br>fertigen Landingpage.</h2>'
        + '<p class="lead">So läuft der Sprint konkret ab – von der Vorbereitung bis zum Go&#8209;live.</p>'
        + zeitstrahl([("01 · 2–3 STD. · ONLINE", "Onboarding", "Wir klären Zielgruppe, Problem und Ziel – damit der Sprint vom ersten Moment an sitzt."),
                      ("02 · 2 TAGE · PRÄSENZ", "Sprint-Workshop", "<b>Tag 1</b><br>Sparring &amp; parallele Entwicklung der Rohversion<span class=\"tag\"><b>Tag 2</b><br>Vorstellung, Feedback, Feinschliff &amp; Go-live</span>"),
                      ("03 · IM NACHGANG", "Review", "Kurzes Fazit: Hat alles gepasst, wie war das Feedback – und wo gibt es noch gezielten Anpassungsbedarf?")])
        + '</div><div class="rand wachsen mitte" style="padding-top:6mm">' + kicker("Tempo ohne Kompromisse")
        + punkte([("timer", "Schneller Start", "Kein monatelanger Prozess – wir starten in den Sprint, sobald der Rahmen steht."),
                  ("layout-grid", "Fokussierter Umfang", "Ein klar begrenztes Set an Inhalten und Elementen, damit der Sprint hält, was er verspricht."),
                  ("circle-check", "Ohne Kompromisse", "Trotz Tempo: sauber gebaut, mobil optimiert und technisch startklar.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:7mm;')
        + '</div>', 4, n)

    liste = ["Konzeption, Text &amp; Design Deiner vollständigen Landingpage", "Umsetzung im zweitägigen Sprint-Workshop bei Dir vor&nbsp;Ort",
             "Feedbackrunde &amp; Feinschliff direkt im Workshop", "Live-Schaltung Deiner Landingpage im Anschluss an den Sprint",
             "Review im Nachgang, damit alles wie gewünscht&nbsp;läuft", "Durchgeführt von 2 Beraterinnen und Beratern von empiria"]
    s5 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:15mm;padding-bottom:16mm">' + kicker("Investition")
        + '<h2>Ein Paket, ein Preis.</h2>'
        + '<p class="lead">Klar kalkuliert statt versteckter Zusatzkosten: Konzeption, Umsetzung und Live-Schaltung in einem Leistungspaket.</p>'
        + '</div><div class="rand" style="padding-top:4mm">'
        + '<div class="paket"><div class="paket__preis"><div><small>Dein Leistungspaket</small><h3>Sprint-Landingpage</h3></div>'
        + f'<div class="paket__unten"><b>15.850 €</b>{ico("rocket", strich=1.3)}</div></div>'
        + '<ul class="paket__liste">' + "".join(f"<li>{x}</li>" for x in liste) + '</ul></div>'
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe sowie zzgl. Spesen (Anfahrt und zwei Übernachtungen für je zwei Personen).</p>'
        + '</div>', 5, n)

    # Anwendungsfälle: volle Texte aus den „Mehr lesen“-Fenstern
    faelle = [
        ("Dynamik in den Kreativworkshop bringen", "Das Thema wird gezielt in einem Kreativworkshop eingesetzt, damit es danach direkt weitergeht – statt dass die Ergebnisse unnötig verzögert werden oder im Nachgang untergehen."),
        ("Schnell auf eine Vertriebssituation reagieren", "Eine Marktchance oder eine Marktveränderung ist aufgekommen, oder es soll kurzfristig ein Push für den Vertrieb gesetzt werden – etwa im Endjahresgeschäft."),
        ("Eine Situation retten", "Etwas wurde schlicht vergessen oder jemand im Marketing ist ausgefallen – aber ein wichtiger Termin steht an: eine große Messe, ein Event, ein Vertriebsmeeting, ein Produktlaunch."),
        ("Zum Wachrütteln", "Diskussionen im Unternehmen ziehen sich immer wieder lange hin, mit vielen Erklärungen, warum etwas nicht möglich ist. Der Sprint beweist, dass es auch schnell und professionell geht."),
        ("Als Methodiktraining im Marketing", "Der Sprint wird eingesetzt, um Einblicke in eine schlagkräftige Methodik zu gewinnen und sie als Schulung fürs eigene Marketingteam nutzbar zu machen."),
        ("Kunden &amp; Partner begeistern", "Kunden, Kooperationspartner oder Vertriebspartner werden begeistert, weil sehr schnell eine einsetzbare Lösung entsteht – etwa gegenüber großen Maklern, Bankpartnern oder Kooperationspartnern in einem neuen Ländermarkt."),
    ]
    s6 = seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Anwendungsfälle")
               + '<h2>Typische Anwendungsfälle.</h2><p class="lead">So setzen Unternehmen den Sprint konkret ein.</p>'
               + '<div class="liste">' + "".join(f'<div style="padding:6mm 0"><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
               + '</div>', 6, n, klasse="seite--hell")

    s7 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Deine<br><span class="hl">neue Landingpage?</span></h2>'
        + '<p class="lead">Sag uns kurz, um welches Thema es geht und wann der Sprint starten soll – wir melden uns zeitnah, um alles Weitere persönlich zu besprechen.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Thema, Zielgruppe und Wunschtermin für den Sprint – eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem unverbindlichen Angebot."),
                      ("03", "Festzurren", "Termine für Onboarding und Sprint klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "noah_pm"]) + kontaktdaten() + '</div></div>', 7, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=CSS)
