"""PDF „Paid Ads“ im Muster von KI zum Anfassen (10.10.2026).
Quelle: site/projekte/empiria-2/paid-ads.html (maßgeblich), ergänzend werkzeuge/pdf-seiten/pages.py P["paid-ads"].
"""
import os
import re

from lib import (ROOT, titelseite, kopfbild, seite, kopf, kicker, zeitstrahl, team, kontaktdaten, dokument, ico)

TITEL = "Paid Ads – empiria"
T = "Paid Ads"

CSS = """
.kanal svg, .kasten--kanal .punkte svg { width: 7mm; height: 7mm; margin-bottom: 3mm; }
.team3 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 8mm; align-items: center; margin-top: 9mm; }
.team3 .team { gap: 4mm; margin-top: 0; }
.team3 .person { width: 30mm; }
.team3 .person img { width: 24mm; height: 24mm; }
.team3 .kontaktdaten { margin-top: 0; }
.liste--frage { margin-top: 10mm; }
.liste--frage > div { grid-template-columns: 62mm 1fr; padding: 5.6mm 0; }
.liste--frage p { font-size: 9pt; }
"""


def _logo(name, farbe="#1a1817"):
    """Kanal-Logo (Google/Meta/LinkedIn) wie auf der 2.0-Seite – nur schwarz."""
    src = open(os.path.join(ROOT, "site", "projekte", "empiria-2", "paid-ads.html"), encoding="utf-8").read()
    pfad = re.search(rf'<symbol id="ic-{name}" viewBox="0 0 24 24">(.*?)</symbol>', src).group(1)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{pfad.replace("currentColor", farbe)}</svg>'


def bauen():
    n = 5
    s1 = seite(titelseite(
        "Performance Marketing", 'Google, Meta &amp;<br>LinkedIn Ads<br><span class="hl">für Deine Zielgruppe.</span><br>Zur richtigen Zeit.',
        "Auf dem passenden Kanal erreichen wir genau die Menschen, die zu Deiner Branche und Deinem Angebot passen. "
        "Du weißt bei jedem Euro, wohin er fließt und was er auslöst.",
        kopfbild("Paid Ads"),
        [("Kanäle", "Google, Meta &amp; LinkedIn"), ("Leistung", "Strategie, Setup, Optimierung"),
         ("Reporting", "Jeden Monat"), ("Einstieg", "Kostenloser Potentialcheck")]))

    kanaele = [("google", "Google Ads", "Deine Anzeige erscheint genau dann, wenn jemand aktiv nach Deiner Lösung sucht. Aus Suchanfragen werden Anfragen, aus Klicks werden Termine."),
               ("meta", "Meta Ads", "Facebook und Instagram erreichen Deine Zielgruppe im Alltag, bevor sie aktiv sucht. Wir testen Motive, finden die Gewinner und skalieren sie."),
               ("linkedin", "LinkedIn Ads", "Entscheider nach Branche, Position und Unternehmensgröße ansprechen: Auf LinkedIn erreichst Du die Menschen, die im B2B unterschreiben.")]
    fragen = [("Wen willst Du erreichen?", "Privatkunden · Geschäftskunden · Beides"),
              ("Wie kommen Deine Kunden heute auf Dich?", "Sie suchen aktiv nach einer Lösung · Empfehlungen und Netzwerk · Social Media und Inhalte · Vertrieb und Kaltakquise"),
              ("Was soll die Kampagne bringen?", "Anfragen und Termine · Verkäufe im Shop · Bekanntheit in der Zielgruppe · Bewerbungen"),
              ("Was bringt Dir eine Anfrage?", "Unter 500 € · 500 bis 5.000 € · Über 5.000 € Umsatz im Schnitt")]
    ablauf = zeitstrahl([("01", "Analyse &amp; Strategie", "Wir prüfen Dein bestehendes Konto oder starten bei null. Ziel, Zielgruppe und Budget stehen fest, bevor der erste Euro läuft."),
                         ("02", "Setup &amp; Start", "Kampagnen, Tracking und Anzeigen werden sauber aufgebaut und gehen live. Ab dem ersten Tag misst jedes Ergebnis."),
                         ("03", "Optimierung", "Wir werten Deine Anzeigen laufend aus und optimieren sie: Was funktioniert, bekommt mehr Budget."),
                         ("04", "Reporting &amp; Skalierung", "Du siehst jeden Monat, wohin jeder Euro geflossen ist und was er gebracht hat.")])
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Leistungen")
        + '<h2>Der richtige Kanal für Deine Zielgruppe.</h2><p class="lead">Wir übernehmen Strategie, Setup und laufende Optimierung. Du konzentrierst Dich auf Dein Unternehmen.</p>'
        + '<div class="punkte kanal" style="grid-template-columns:repeat(3,1fr)">'
        + "".join(f'<div>{_logo(k)}<h3>{t}</h3><p>{p}</p></div>' for k, t, p in kanaele) + '</div>'
        + '</div><div class="rand weiss" style="padding-top:11mm">' + kicker("Ablauf")
        + '<h2>Vier Schritte zu planbarem Ergebnis.</h2><p class="lead">So wird aus Deinem Budget ein nachvollziehbares Ergebnis.</p>'
        + ablauf + '</div>', 2, n)

    empfehlung = [("google", "Google Ads", "Dein Angebot wird gesucht. Google Ads holt genau die Menschen ab, die gerade nach Deiner Lösung suchen."),
                  ("meta", "Meta Ads", "Deine Zielgruppe muss erst auf Dich aufmerksam werden. Auf Facebook und Instagram erreichst Du sie im Alltag."),
                  ("linkedin", "LinkedIn Ads", "Du willst Entscheider erreichen. LinkedIn zielt nach Branche, Position und Unternehmensgröße.")]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Kanal-Check")
        + '<h2>Welcher Kanal passt zu Deinem Business?</h2>'
        + '<p class="lead">Du willst wissen, welcher Kanal der richtige für Dein Unternehmen ist? Nach unserem Kanal-Check weißt Du es.</p>'
        + '<div class="liste liste--frage">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in fragen) + '</div>'
        + '<div class="kasten kasten--kanal" style="margin-top:12mm;padding:8mm 7mm"><p class="label">Unsere Empfehlung für Dich</p>'
        + '<div class="punkte" style="grid-template-columns:repeat(3,1fr);margin-top:5mm">'
        + "".join(f'<div>{_logo(k, "#fff400")}<h3>{t}</h3><p>{p}</p></div>' for k, t, p in empfehlung) + '</div></div>'
        + '</div>', 3, n)

    faq = [("Was brauche ich, um zu starten?", "Zugriff auf Deine bestehenden Konten, falls vorhanden, sowie Klarheit über Dein Budget und Dein Ziel. Den Rest klären wir gemeinsam im Auftakt."),
           ("Wann sehe ich erste Ergebnisse?", "Erste Daten liegen meist nach wenigen Wochen vor. Belastbare Aussagen brauchen etwas mehr Zeit, damit die Kampagnen wirklich lernen können."),
           ("Welche Plattformen betreut ihr?", "Google, Meta und LinkedIn. Welcher Kanal für Dich der richtige Start ist, hängt von Zielgruppe und Angebot ab, nicht davon, was gerade angesagt ist."),
           ("Gibt es Mindestlaufzeiten?", "Ja, mindestens drei Monate. Kampagnen brauchen diese Zeit, um belastbare Daten zu liefern und sauber optimiert zu werden. Danach läuft die Zusammenarbeit monatlich weiter."),
           ("Woher weiß ich, wie gut meine Anzeigen laufen?", "Du hast vollen Zugriff auf Dein Konto und bekommst jeden Monat eine klare Auswertung: Was hat jeder Euro gebracht, und woran arbeiten wir als Nächstes.")]
    s4 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("FAQ")
        + '<h2>Häufige Fragen.</h2><p class="lead">Wenn Du weitere Fragen hast, vereinbare einfach ein Gespräch mit uns. Wir klären alles, was offen ist.</p>'
        + '<div class="liste">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faq) + '</div>'
        + '<div class="kasten" style="margin-top:8mm"><div class="zwei"><div><p class="label">Kostenloser Potentialcheck</p>'
        + '<h3>Wie viel Potential steckt in Deinem Produkt?</h3></div>'
        + '<p style="margin-top:0">Schick uns Deine Website. Noch diese Woche bekommst Du unsere Potentialanalyse für Dein Unternehmen und Deine Performance Ads – keine Verpflichtung.</p></div></div>'
        + '</div>', 4, n, klasse="seite--hell")

    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Werbung, <span class="hl">die Anfragen bringt?</span></h2>'
        + '<p class="lead">Sag uns, welche Zielgruppe Du erreichen willst und mit welchem Budget Du rechnest – wir schlagen Dir den passenden Kanal vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Zielgruppe, Angebot und Budgetrahmen – eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag zum passenden Kanal."),
                      ("03", "Festzurren", "Umfang, Laufzeit und Investition klären wir gemeinsam, bevor der erste Euro läuft.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="team3">' + team(["daniel", "kerstin_content", "noah_pm"]) + kontaktdaten() + '</div></div>', 5, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5], extra_css=CSS)
