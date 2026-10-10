"""PDF „Paid Ads“ – Runde 2 (10.10.2026), Aufbau wie alle 2.0-PDFs.
Quelle: site/projekte/empiria-2/paid-ads.html (maßgeblich) inkl. Kanal-Check (Fragen, Antworten, Empfehlungstexte),
Potentialcheck (Ablauf und Prüfbereiche) und FAQ. Reihenfolge wie auf der Seite:
Leistungen → Kanal-Check → Ablauf → Potentialcheck → FAQ → Kontakt.
"""
import os
import re

from lib import (ROOT, titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Paid Ads – empiria"
T = "Paid Ads"

# nur Sonderbausteine: Kanal-Logos, Empfehlungs-Zeilen, Team mit drei Personen
CSS = """
.kanal svg { width: 7mm; height: 7mm; margin-bottom: 3mm; }
.liste--frage { margin-top: 6mm; }
.liste--frage > div { padding: 2.8mm 0; align-items: center; }
.liste--frage h3 { font-size: 11pt; }
.antworten { display: flex; flex-wrap: wrap; gap: 1.4mm; }
.antworten span { font-size: 7.6pt; line-height: 1.3; padding: 1mm 2.6mm; border: 1px solid #1a1817; border-radius: 9mm; white-space: nowrap; }
.empf > div { grid-template-columns: 50mm 1fr; padding: 6mm 0; }
.empf h3 { display: flex; align-items: center; gap: 3mm; font-size: 13pt; }
.empf h3 svg { width: 6.5mm; height: 6.5mm; flex: 0 0 auto; }
.empf small { display: block; margin-top: 4mm; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.empf .antworten { margin-top: 2mm; }
.pruef { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 4mm; }
.pruef div { border-top: 1px solid rgba(255,255,255,.35); padding-top: 2.6mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 10.5pt; line-height: 1.25; color: #fff; }
.pc .punkte { margin-top: 6mm; }
.pc .punkte svg { display: none; }
.pc .lead { max-width: 160mm; }
.liste--faq > div { padding: 6.5mm 0; }
.team3 { display: grid; grid-template-columns: 1.3fr 1fr; gap: 8mm; align-items: center; margin-top: 9mm; }
.team3 .team { gap: 4mm; margin-top: 0; }
.team3 .person { width: 30mm; }
.team3 .person img { width: 24mm; height: 24mm; }
.team3 .kontaktdaten { margin-top: 0; }
"""

SRC = open(os.path.join(ROOT, "site", "projekte", "empiria-2", "paid-ads.html"), encoding="utf-8").read()


def _logo(name, farbe="#1a1817"):
    """Kanal-Logo (Google/Meta/LinkedIn) aus der 2.0-Seite – einfarbig."""
    pfad = re.search(rf'<symbol id="ic-{name}" viewBox="0 0 24 24">(.*?)</symbol>', SRC).group(1)
    return f'<svg viewBox="0 0 24 24" aria-hidden="true">{pfad.replace("currentColor", farbe)}</svg>'


def _chips(items):
    return '<div class="antworten">' + "".join(f"<span>{x}</span>" for x in items) + '</div>'


# Kanal-Check: Fragen und Antworten exakt wie im Mini-Funnel der Seite
FRAGEN = [("Wen willst Du erreichen?", ["Privatkunden", "Geschäftskunden", "Beides"]),
          ("Wie kommen Deine Kunden heute auf Dich?", ["Sie suchen aktiv nach einer Lösung und finden mich", "Über Empfehlungen und mein Netzwerk",
                                                      "Über Social Media und Inhalte", "Über Vertrieb und Kaltakquise"]),
          ("Was soll die Kampagne in erster Linie bringen?", ["Anfragen und Termine", "Verkäufe im Shop", "Bekanntheit in meiner Zielgruppe", "Bewerbungen"]),
          ("Wie viel Umsatz bringt Dir eine Anfrage im Schnitt?", ["Unter 500 €", "500 bis 5.000 €", "Über 5.000 €"])]

# Ergebnis-Texte des Kanal-Checks; „Spricht dafür“ = die Antworten, die im Check am stärksten auf diesen Kanal zählen
EMPFEHLUNG = [("google", "Google Ads", "Dein Angebot wird gesucht. Google Ads holt genau die Menschen ab, die gerade nach Deiner Lösung suchen, und macht aus der Suche eine Anfrage.",
               ["Sie suchen aktiv nach einer Lösung", "Anfragen und Termine", "500 bis 5.000 € je Anfrage"]),
              ("meta", "Meta Ads", "Deine Zielgruppe muss erst auf Dich aufmerksam werden. Auf Facebook und Instagram erreichst Du sie im Alltag, mit Motiven, die wir testen und skalieren.",
               ["Privatkunden", "Social Media und Inhalte", "Verkäufe im Shop", "Bekanntheit in der Zielgruppe", "Unter 500 € je Anfrage"]),
              ("linkedin", "LinkedIn Ads", "Du willst Entscheider erreichen. LinkedIn lässt uns nach Branche, Position und Unternehmensgröße zielen, genau dort, wo im B2B entschieden wird.",
               ["Geschäftskunden", "Empfehlungen und Netzwerk", "Vertrieb und Kaltakquise", "Bewerbungen", "Über 5.000 € je Anfrage"])]


def bauen():
    n = 6
    s1 = seite(titelseite(
        "Performance Marketing", '<span class="hl">Google, Meta &amp; LinkedIn</span><br>Ads für Deine Zielgruppe.<br>Zur richtigen Zeit.',
        "Auf dem passenden Kanal erreichen wir genau die Menschen, die zu Deiner Branche und Deinem Angebot passen. "
        "Du weißt bei jedem Euro, wohin er fließt und was er auslöst.",
        kopfbild("Paid Ads"),
        [("Kanäle", "Google, Meta &amp; LinkedIn"), ("Leistung", "Strategie, Setup, Optimierung"),
         ("Laufzeit", "Mindestens drei Monate"), ("Einstieg", "Kostenloser Potentialcheck")]))

    kanaele = [("google", "Google Ads", "Deine Anzeige erscheint genau dann, wenn jemand aktiv nach Deiner Lösung sucht. Aus Suchanfragen werden Anfragen, aus Klicks werden Termine."),
               ("meta", "Meta Ads", "Facebook und Instagram erreichen Deine Zielgruppe im Alltag, bevor sie aktiv sucht. Wir testen Motive, finden die Gewinner und skalieren sie."),
               ("linkedin", "LinkedIn Ads", "Entscheider nach Branche, Position und Unternehmensgröße ansprechen: Auf LinkedIn erreichst Du die Menschen, die im B2B unterschreiben.")]
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:11mm;padding-bottom:11mm">' + kicker("Leistungen")
        + '<h2>Der richtige Kanal für Deine Zielgruppe.</h2><p class="lead">Wir übernehmen Strategie, Setup und laufende Optimierung. Du konzentrierst Dich auf Dein Unternehmen.</p>'
        + '<div class="punkte kanal" style="grid-template-columns:repeat(3,1fr)">'
        + "".join(f'<div>{_logo(k)}<h3>{t}</h3><p>{p}</p></div>' for k, t, p in kanaele) + '</div>'
        + '</div><div class="rand" style="padding-top:10mm">' + kicker("Kanal-Check")
        + '<h2>Welcher Kanal passt zu Deinem Business?</h2>'
        + '<p class="lead">Du willst wissen, welcher Kanal der richtige für Dein Unternehmen ist? Nach unserem Kanal-Check weißt Du es.</p>'
        + '<div class="liste liste--frage">' + "".join(f'<div><h3>{q}</h3>{_chips(a)}</div>' for q, a in FRAGEN) + '</div>'
        + '</div>', 2, n)

    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Kanal-Check · Ergebnis")
        + '<h2>Unsere Empfehlung für Dich.</h2>'
        + '<p class="lead">Aus Deinen Antworten ergibt sich, welcher Kanal für Dich der richtige Start ist – entscheidend sind Zielgruppe und Angebot, nicht das, was gerade angesagt ist.</p>'
        + '<div class="liste empf">' + "".join(
            f'<div><h3>{_logo(k)}{t}</h3><div><p>{p}</p><small>Spricht dafür im Kanal-Check</small>{_chips(a)}</div></div>'
            for k, t, p, a in EMPFEHLUNG) + '</div>'
        + '<div class="kasten" style="margin-top:9mm"><div class="zwei"><div><p class="label">Zweiter Kanal</p><h3>Oft passt mehr als ein Kanal.</h3></div>'
        + '<p style="margin-top:0">Der Kanal-Check nennt Dir auch, welcher Kanal als zweiter passt. Ob und wann sich der lohnt, klären wir im Gespräch.</p></div></div>'
        + '</div>', 3, n)

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>Vier Schritte zu planbarem Ergebnis.</h2><p class="lead">So wird aus Deinem Budget ein nachvollziehbares Ergebnis.</p>'
        + zeitstrahl([("01", "Analyse &amp; Strategie", "Wir prüfen Dein bestehendes Konto oder starten bei null. Ziel, Zielgruppe und Budget stehen fest, bevor der erste Euro läuft."),
                      ("02", "Setup &amp; Start", "Kampagnen, Tracking und Anzeigen werden sauber aufgebaut und gehen live. Ab dem ersten Tag misst jedes Ergebnis."),
                      ("03", "Optimierung", "Wir werten Deine Anzeigen laufend aus und optimieren sie: Was funktioniert, bekommt mehr Budget."),
                      ("04", "Reporting &amp; Skalierung", "Du siehst jeden Monat, wohin jeder Euro geflossen ist und was er gebracht hat. Alle Zahlen liegen offen, ausgebaut wird dort, wo sie es rechtfertigen.")])
        + '</div><div class="band band--gelb wachsen pc" style="margin-top:9mm;padding-top:10mm">' + kicker("Kostenloser Potentialcheck")
        + '<h2>Wie viel Potential steckt in Deinem Produkt?</h2>'
        + '<p class="lead">Schick uns Deine Website. Noch diese Woche bekommst Du unsere Potentialanalyse für Dein Unternehmen und Deine Performance Ads.</p>'
        + punkte([("app-window", "Website nennen", "Du gibst uns die Adresse Deiner Website – mehr brauchen wir für den Start nicht."),
                  ("mail", "Kurz ergänzen", "Deine E-Mail-Adresse und ob Du bereits Ads schaltest: Google, Meta, LinkedIn oder noch nicht."),
                  ("file-text", "Analyse erhalten", "Antwort noch diese Woche. Kein Spam, keine Verpflichtung.")])
        + '<div class="kasten" style="margin-top:7mm"><p class="label">Das schauen wir uns an</p>'
        + '<div class="pruef"><div>Tracking &amp; Messung</div><div>Zielgruppen</div><div>Kanalwahl</div><div>Anzeigen &amp; Motive</div></div>'
        + '<p>Du bekommst eine Gesamteinschätzung und die drei Hebel mit dem größten Effekt markiert.</p></div>'
        + '</div>', 4, n)

    faq = [("Was brauche ich, um zu starten?", "Zugriff auf Deine bestehenden Konten, falls vorhanden, sowie Klarheit über Dein Budget und Dein Ziel. Den Rest klären wir gemeinsam im Auftakt."),
           ("Wann sehe ich erste Ergebnisse?", "Erste Daten liegen meist nach wenigen Wochen vor. Belastbare Aussagen brauchen etwas mehr Zeit, damit die Kampagnen wirklich lernen können."),
           ("Welche Plattformen betreut ihr?", "Google, Meta und LinkedIn. Welcher Kanal für Dich der richtige Start ist, hängt von Zielgruppe und Angebot ab, nicht davon, was gerade angesagt ist. Der Kanal-Check gibt Dir eine erste Antwort."),
           ("Gibt es Mindestlaufzeiten?", "Ja, mindestens drei Monate. Kampagnen brauchen diese Zeit, um belastbare Daten zu liefern und sauber optimiert zu werden. Danach läuft die Zusammenarbeit monatlich weiter."),
           ("Woher weiß ich, wie gut meine Anzeigen laufen?", "Du hast vollen Zugriff auf Dein Konto und bekommst jeden Monat eine klare Auswertung: Was hat jeder Euro gebracht, und woran arbeiten wir als Nächstes.")]
    s5 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("FAQ")
        + '<h2>Häufige Fragen.</h2><p class="lead">Wenn Du weitere Fragen hast, vereinbare einfach ein Gespräch mit uns. Wir klären alles, was offen ist.</p>'
        + '<div class="liste liste--faq">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faq) + '</div>'
        + '<div class="kasten" style="margin-top:10mm"><div class="zwei"><div><p class="label">Noch Fragen offen?</p><h3>Kurze Wege statt langer Abstimmungsrunden.</h3></div>'
        + '<p style="margin-top:0">Schreib uns an daniel.stroebel@empiria.de oder ruf an unter +49 176 3134 7217 – wir klären alles, was offen ist.</p></div></div>'
        + '</div>', 5, n, klasse="seite--hell")

    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für Werbung, <span class="hl">die Anfragen bringt?</span></h2>'
        + '<p class="lead">Sag uns, welche Zielgruppe Du erreichen willst und mit welchem Budget Du rechnest – wir schlagen Dir den passenden Kanal vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Zielgruppe, Angebot und Budgetrahmen – eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag zum passenden Kanal."),
                      ("03", "Festzurren", "Umfang, Laufzeit und Investition klären wir gemeinsam, bevor der erste Euro läuft.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="team3">' + team(["daniel", "kerstin_content", "noah_pm"]) + kontaktdaten() + '</div></div>', 6, n)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=CSS)
