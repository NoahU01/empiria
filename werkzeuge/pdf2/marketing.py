"""PDF „Marketing 2.0“ – Übersichts-PDF mit Kapiteln (Runde 3, Stand der 2.0-Seiten 10.10.2026).

Aufbau: Titel · Ansatz + vier Wege · Überblick (Vergleichstabelle) · Kapitel 01 MES · 02 sofort sichtbar ·
03 Paid Ads · 04 Medien (je zwei Seiten, verdichtet aus den Unterseiten) · Schluss.
Quellen: site/projekte/empiria-2/marketing.html und die vier Unterseiten; Texte aus den Modulen der Unter-PDFs.
"""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, dokument, ico
import _marketing_teile as mt
from paid_ads import _logo, _chips, EMPFEHLUNG

TITEL = "Marketing 2.0 – empiria"
T = "Marketing 2.0"
N = 12

# Die vier Wege wie auf der Seite (Abschnitt „Unsere Lösungen“), Bausteine und Preise aus den jeweiligen 2.0-Seiten
WEGE = [
    ("layout-dashboard", "MarketingEcoSystem (MES)", "MES",
     "Homepage, Kanäle und Dashboard aus einer Hand – alles greift ineinander, Du musst uns nicht briefen."),
    ("users", "sofort sichtbar", "sofort sichtbar",
     "Digitale Sichtbarkeit für Agenturleiterinnen und Agenturleiter – ohne Briefing, mit fertigem Auftritt."),
    ("megaphone", "Paid Ads", "Paid Ads",
     "Kampagnen auf Google, Meta und LinkedIn, die Anfragen bringen – klar ausgewertet statt Blackbox."),
    ("presentation", "Medien, die Ergebnisse liefern", "Medien",
     "PowerPoint, Landingpage und Roll-up aus einer Hand – professionell umgesetzt, damit Deine Botschaft trägt."),
]


def kapitel(nr, name, h2, lead):
    """Kapitel-Einstieg: große Kapitelnummer, Kicker = Name der Unterseite, H2 = Kopfzeile, Lead = Kopftext."""
    return (f'<div class="kap"><span class="kap__nr">{nr}</span><span class="kap__linie"></span></div>'
            + kicker(name) + f'<h2>{h2}</h2><p class="lead" style="max-width:160mm">{lead}</p>')


def details(name):
    return f'<p class="notiz details">Alle Details: eigenes PDF „{name}“ auf empiria.de</p>'


def band_gelb(kick, items, extra=""):
    return (f'<div class="band band--gelb kap-band">{kicker(kick)}' + (extra or punkte(items)) + '</div>')


# ---------------------------------------------------------------- Überblick
def ueberblick(nr):
    sp = [(f"Kapitel 0{k + 1}", w[2], "", False) for k, w in enumerate(WEGE)]
    zeilen = [
        ("Investition", ['ab 399 €<span class="klein">monatlich (Eigenregie)</span>',
                         'ab 349 €<span class="klein">monatlich bei jährlicher Zahlung</span>',
                         'Nach Vorhaben<span class="klein">Mindestlaufzeit drei Monate</span>',
                         'Nach Vorhaben<span class="klein">je nach Medium und Umfang</span>'], "preis"),
        ("Bausteine", [mt.ul(["Landingpage", "Social-Media-Kanäle", "Zentrales Dashboard"]),
                       mt.ul(["Social Media Postings", "E-Mail-Funnel", "Passende Landingpages"]),
                       mt.ul(["Google Ads", "Meta Ads", "LinkedIn Ads"]),
                       mt.ul(["PowerPoint", "Landingpage", "Roll-up"])], ""),
        ("Wahl", ["Drei Pakete: Eigenregie, Marketing as a Service, Unternehmertum",
                  "Drei Pakete: Fokus, Reichweite, Marktposition",
                  "Kanal-Check und kostenloser Potentialcheck",
                  "Medien nach Deinem Ziel, nicht nach Format"], ""),
        ("Im PDF", ["ab Seite 4", "ab Seite 6", "ab Seite 8", "ab Seite 10"], "seite-ref"),
    ]
    return seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Überblick")
        + '<h2>Du wählst, <span class="hl">wir liefern.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Ob als Gesamtpaket oder einzeln buchbar – die vier Wege mit Bausteinen und Investition auf einen Blick.</p>'
        + mt.tabelle(sp, zeilen).replace('<col style="width:28mm">', '<col style="width:25mm">')
        + '<p class="notiz">Preise zzgl. Umsatzsteuer in gesetzlicher Höhe. Bei Paid Ads und Medien richtet sich die Investition nach Deinem Vorhaben – '
          'Umfang, Laufzeit und Investition klären wir gemeinsam.</p>'
        + '<div class="kasten" style="margin-top:10mm"><div class="zwei"><div><p class="label">Komplett oder einzeln</p>'
          '<h3>Deine Marketingabteilung – oder gezielt einzelne Medien.</h3></div>'
          '<p style="margin-top:0">Buche uns als klar definierte Marketingabteilung – oder hol Dir gezielt einzelne Medien dazu. '
          'Auf den folgenden Seiten findest Du jeden Weg als eigenes Kapitel.</p></div></div>'
        + '</div>', nr, N)


# ---------------------------------------------------------------- Kapitel 01 · MES
def mes(nr):
    a = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("01", "MarketingEcoSystem (MES)", 'Du konzentrierst Dich auf <span class="hl">Dein Business.</span>',
                  "Unser MarketingEcoSystem (MES) führt Homepage, digitale Kanäle und zentrales Dashboard an einem Ort zusammen – "
                  "damit alles ineinandergreift, statt nebeneinanderher zu laufen.")
        + '</div>'
        + band_gelb("Echter Nutzen statt Pseudo-Reporting", [
            ("puzzle", "Kanäle greifen ineinander", "Homepage, Social Media und Content laufen nicht mehr nebeneinanderher, sondern in Deinem MES – Google Ads, Meta, Website und mehr an einem Ort."),
            ("eye", "Kein Blindflug mehr", "Dein Marketing wird laufend geprüft – Schwachstellen fallen auf, bevor sie zum Problem werden, inklusive konkretem Lösungsvorschlag."),
            ("zap", "Zurück in die Umsetzung", "Wir sehen, ob etwas funktioniert, wissen, warum wir etwas anpassen – und setzen die nächste Optimierung direkt um.")])
        + '<div class="band band--schwarz wachsen mitte">' + kicker("Der Unterschied zur Agentur")
        + '<h2>Du musst uns <span class="hl">nicht briefen.</span></h2>'
        + '<div class="zwei agentur"><p>Bei einer Agentur liegt die Überlegung zu Markterfolg und Marketingstrategie bei Dir – '
          'Du musst briefen und sagen, was zu tun ist.</p>'
          '<p>Bei uns nicht: Wir sind Profis für das, was wir tun, holen die wichtigsten Informationen mit wenigen gezielten Fragen ab '
          'und sorgen für die permanente Umsetzung.</p></div></div>', nr, N, hell_fuss=True)

    sp = [("Du setzt selbst um", "Eigenregie", "", False),
          ("Wir übernehmen alles", "Marketing as a Service", "Meistgewählt", True),
          ("Wir wachsen gemeinsam", "Unternehmertum", "", False)]
    zeilen = [
        ("Investition", ['ab 399 €<span class="klein">monatlich</span>', 'ab 3.500 €<span class="klein">monatlich</span>',
                         'Auf Anfrage<span class="klein">Partnerschaft</span>'], "preis"),
        ("Leistung", ["Anbindung an Dashboard &amp; Reporting – die Optimierung übernimmst Du selbst.",
                      "Laufende Betreuung und Optimierung von Homepage, Kanälen und Reporting.",
                      "Unternehmerische Partnerschaft, wenn es für beide Seiten passt."], ""),
        ("Rahmen", ["Mindestlaufzeit drei Monate zzgl. einmaliger Setup-Kosten", "Mindestlaufzeit zwölf Monate, keine einmaligen Setup-Kosten",
                    "Gemeinsames Gespräch zur Prüfung, ob eine Beteiligung passt"], ""),
    ]
    b = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Der Kreislauf Deines MES")
        + '<h2>Alles greift <span class="hl">ineinander.</span></h2>'
        + '<p class="lead" style="max-width:165mm">Kanäle bringen Besucher auf die Landingpage, das Dashboard führt alle Informationen zusammen '
          'und gibt Optimierungsempfehlungen zurück in die Kanäle.</p>'
        + zeitstrahl([("01", "Konzeption &amp; Umsetzung", "Wir planen den Aufbau und setzen ihn in Homepage, Kanälen und Content um."),
                      ("02", "Tracking &amp; Analyse", "Das Dashboard misst, ob eingetreten ist, was wir wollten."),
                      ("03", "Ableitung Next Step", "Wir leiten den nächsten Schritt ab – und starten neu.")])
        + '<div class="abschnitt">' + kicker("Pakete") + '<h2>Drei Wege, <span class="hl">uns zu buchen.</span></h2></div>'
        + mt.tabelle(sp, zeilen).replace('tabelle--fest', 'tabelle--fest tabelle--kompakt')
        + '<p class="notiz">Der Preis richtet sich nach dem vereinbarten Umfang. Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>'
        + details("MarketingEcoSystem (MES)") + '</div>', nr + 1, N)
    return [a, b]


# ---------------------------------------------------------------- Kapitel 02 · sofort sichtbar
def sofort(nr):
    a = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("02", "sofort sichtbar", 'Digital sichtbar. <span class="hl">Ohne Briefing.</span><br>Sofort einsatzbereit.',
                  "Ein fertiges System aus Postings, Landingpage und E-Mail-Funnel für Agenturleiter und Makler, die am Vertriebserfolg "
                  "gemessen werden und für Marketing weder Zeit noch Nerven übrig haben.")
        + '</div>'
        + band_gelb("Was sofort sichtbar mitbringt", [
            ("message-square-text", "Social Media Postings", "Fertige Postings, genau auf Deine Zielgruppe abgestimmt – sofort einsetzbar, ohne eigene Content-Produktion."),
            ("mail", "E-Mail-Funnel", "Aktiviert Deine Bestandskunden und leitet sie auf die passende, zielgruppenspezifische Landingpage weiter."),
            ("app-window", "Passende Landingpages", "Mit Download-Dokument, Podcast-Folge und optimierten Kontaktdaten – in Deinem Corporate Design.")])
        + '<div class="rand weiss" style="padding-top:11mm">' + kicker("Ablauf")
        + '<h2>Monate werden <span class="hl">zu Tagen.</span></h2>'
        + zeitstrahl([("01", "Auftragsklärung", "Wir klären kurz Deinen Vertriebsfokus – ohne Konzeptphase."),
                      ("02", "Zielgruppen auswählen", "Du wählst die vorbereiteten Profile, die zu Dir passen."),
                      ("03", "Stil &amp; Auftritt", "Du bringst Dein Design ein – Logo, Bilder, Kontaktdaten, Farbwelt."),
                      ("04", "Live gehen", "Postings, Landingpage und E-Mail-Funnel gehen live.")])
        + '</div>', nr, N)

    sp = [("Eine Zielgruppe", "Fokus", "", False), ("Mehrere Zielgruppen", "Reichweite", "Beliebt", True),
          ("Planbare Neukontakte", "Marktposition", "", False)]
    zeilen = [
        ("Investition", ['349 €<span class="klein">pro Monat bei jährlicher Zahlung<br>435 € bei monatlicher Zahlung</span>',
                         '499 €<span class="klein">pro Monat bei jährlicher Zahlung<br>625 € bei monatlicher Zahlung</span>',
                         '999 €<span class="klein">pro Monat bei jährlicher Zahlung<br>1.250 € bei monatlicher Zahlung</span>'], "preis"),
        ("Ziel", ["Erreiche eine klar definierte Zielgruppe ganzjährig – mit fertigen Postings, Mailings und Landingpage.",
                  "Gewinne Kontakte aus mehreren Zielgruppen, ohne eigenen Aufwand für Content oder Kampagnen.",
                  "Positioniere Deine Berater gezielt, mach Stärken sichtbar und sorge für planbare Neukontakte."], ""),
        ("Enthalten", [mt.ul(["1 digitale Vertriebsstrecke", "Individualisierungspaket", "Contentplan für Social Media"]),
                       mt.ul(["3 digitale Vertriebsstrecken", "Erweiterte Individualisierung", "Performance-Reporting"]),
                       mt.ul(["10 digitale Vertriebsstrecken", "Automatisierung der Postings", "Regelmäßige 1:1&#8209;Beratung"])], ""),
    ]
    kasten = ('<div class="kasten kasten--kompakt" style="margin-top:5mm"><p class="label">Für jedes Paket gilt</p>'
              + punkte([("timer", "Drei Monate Mindestlaufzeit", "Je Vertriebsstrecke – danach verlängern, Zielgruppe wechseln oder unkompliziert kündigen."),
                        ("app-window", "In Deinem Design", "Logo, Bilder, Kontaktdaten und Farbwelt werden auf Deine Agentur angepasst."),
                        ("shield-check", "Anfragen direkt bei Dir", "Per Anruf, E-Mail oder Formular – ohne Umweg über uns. Landingpages auf EU-Servern.")])
              .replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;') + '</div>')
    b = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Preise")
        + '<h2>Die passenden Pakete für<br><span class="hl">Deinen Vertriebsfokus.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Monatlich buchbar, mit Rabatt bei jährlicher Zahlung – jede Vertriebsstrecke mit einer Mindestlaufzeit von drei Monaten.</p>'
        + mt.tabelle(sp, zeilen).replace('tabelle--fest', 'tabelle--fest tabelle--kompakt')
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>' + kasten
        + details("sofort sichtbar") + '</div>', nr + 1, N)
    return [a, b]


# ---------------------------------------------------------------- Kapitel 03 · Paid Ads
def paid(nr):
    kanaele = [("google", "Google Ads", "Deine Anzeige erscheint genau dann, wenn jemand aktiv nach Deiner Lösung sucht. Aus Suchanfragen werden Anfragen."),
               ("meta", "Meta Ads", "Facebook und Instagram erreichen Deine Zielgruppe im Alltag, bevor sie aktiv sucht. Wir testen Motive und skalieren die Gewinner."),
               ("linkedin", "LinkedIn Ads", "Entscheider nach Branche, Position und Unternehmensgröße ansprechen – die Menschen, die im B2B unterschreiben.")]
    kanal_punkte = ('<div class="punkte kanal" style="grid-template-columns:repeat(3,1fr)">'
                    + "".join(f'<div>{_logo(k)}<h3>{t}</h3><p>{p}</p></div>' for k, t, p in kanaele) + '</div>')
    a = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("03", "Paid Ads", '<span class="hl">Google, Meta &amp; LinkedIn</span><br>Ads für Deine Zielgruppe.',
                  "Auf dem passenden Kanal erreichen wir genau die Menschen, die zu Deiner Branche und Deinem Angebot passen. "
                  "Du weißt bei jedem Euro, wohin er fließt und was er auslöst.")
        + '</div>'
        + band_gelb("Der richtige Kanal für Deine Zielgruppe", None, kanal_punkte)
        + '<div class="rand weiss" style="padding-top:11mm">' + kicker("Ablauf")
        + '<h2>Vier Schritte zu planbarem Ergebnis.</h2>'
        + zeitstrahl([("01", "Analyse &amp; Strategie", "Ziel, Zielgruppe und Budget stehen fest, bevor Geld fließt."),
                      ("02", "Setup &amp; Start", "Kampagnen, Tracking und Anzeigen werden sauber aufgebaut und gehen live."),
                      ("03", "Optimierung", "Was funktioniert, bekommt mehr Budget."),
                      ("04", "Reporting &amp; Skalierung", "Du siehst jeden Monat, wohin jeder Euro geflossen ist.")])
        + '</div>', nr, N)

    b = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Kanal-Check")
        + '<h2>Welcher Kanal passt zu <span class="hl">Deinem Business?</span></h2>'
        + '<p class="lead" style="max-width:165mm">Vier kurze Fragen zu Zielgruppe, Kundenweg, Ziel und Wert einer Anfrage – daraus ergibt sich Deine Empfehlung.</p>'
        + '<div class="liste empf">' + "".join(
            f'<div><h3>{_logo(k)}{t}</h3><div><p>{p}</p><small>Spricht dafür im Kanal-Check</small>{_chips(c)}</div></div>'
            for k, t, p, c in EMPFEHLUNG) + '</div>'
        + '<div class="kasten pc" style="margin-top:8mm"><p class="label">Kostenloser Potentialcheck</p>'
          '<h3>Wie viel Potential steckt in Deinem Produkt?</h3>'
          '<p>Schick uns Deine Website. Noch diese Woche bekommst Du unsere Potentialanalyse – mit Gesamteinschätzung und den drei Hebeln mit dem größten Effekt. '
          'Kein Spam, keine Verpflichtung.</p>'
          '<div class="pruef"><div>Tracking &amp; Messung</div><div>Zielgruppen</div><div>Kanalwahl</div><div>Anzeigen &amp; Motive</div></div></div>'
        + details("Paid Ads") + '</div>', nr + 1, N)
    return [a, b]


# ---------------------------------------------------------------- Kapitel 04 · Medien
def medien(nr):
    medien_l = [("Medium 01", "PowerPoint", "Eine Präsentation, die Deine Business Story trägt – klar strukturiert und professionell gestaltet."),
                ("Medium 02", "Landingpage", "Eine Seite für Deine Zielgruppe, die ein zentrales Problem löst und zum nächsten Schritt führt."),
                ("Medium 03", "Roll-up", "Der Gesamtzusammenhang in einem Bild – im Raum präsent, auch wenn der Beamer aus ist.")]
    a = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">'
        + kapitel("04", "Medien, die Ergebnisse liefern", 'Deine Botschaft. <span class="hl">Auf den Punkt.</span><br>Volle Wirkung.',
                  "Wir sind keine typische Medienagentur. Wir sind Profis in den Themen Geschäftsmodell Versicherung, Strategie und Kommunikation.")
        + '</div>'
        + band_gelb("Unser Ansatz", [
            ("briefcase", "Geschäftsmodell &amp; Strategie", "Wir verstehen Dein Geschäftsmodell und Deine Strategie – bevor wir über Medien sprechen."),
            ("target", "Auf den Punkt gebracht", "Wir übersetzen komplexe Themen in die Welt Deiner Zielgruppe – damit Kommunikation ankommt."),
            ("award", "Professionelle Medien", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – damit sie im entscheidenden Moment wirkt.")])
        + '<div class="rand" style="padding-top:11mm">' + kicker("Medien wirksam einsetzen")
        + '<h2>Es geht nicht um Medien, sondern um Deine Ziele.</h2>'
        + punkte([(i, t, p) for (l, t, p), i in zip(medien_l, ["presentation", "app-window", "rollup"])]).replace('<div class="punkte" style="', '<div class="punkte medien-p" style="')
        + '</div>', nr, N)

    faelle = [("Positionierung eines Unternehmens neu ausrichten",
               "Ein kleineres Konzernunternehmen mit klarem Spezialsegment soll professioneller am Markt auftreten – mit einer Homepage hier und einer internen PowerPoint dort gelingt das nicht. "
               "Es braucht eine Gesamtlogik, die Kooperationspartnern, Vertriebspartnern und Kunden verständlich macht, wofür das Unternehmen steht."),
              ("Produktlaunch oder Produktrelaunch",
               "Broschüren und PowerPoints mit 150 Detailfolien helfen keinem Vertriebspartner – ein Vertriebsimpuls funktioniert nur, wenn er die Zielgruppe erfolgreich macht. "
               "Deshalb setzen wir gezielt auf die Medien, die wirken, oft auf eine durchdachte Kombination digitaler Formate."),
              ("Aufsichtsrats- und Gremientermine",
               "Hier zählt nicht das letzte Detail, sondern der Gesamtnutzen fürs Unternehmen – kompakt, verständlich und vertrauensbildend erzählt. "
               "Gerade für fachfremde Gremienmitglieder entscheidet die Übersetzung in ihre Welt, ob die Botschaft ankommt.")]
    b = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
        + '<h2>Konkrete Use Cases aus der Praxis.</h2>'
        + '<p class="lead" style="max-width:160mm">Eine Auswahl realer Anwendungsfälle, die zeigen, wie unsere Medien in der Praxis wirken.</p>'
        + '<div class="liste faelle-l">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + '<div class="kasten" style="margin-top:8mm"><p class="label">Im Fokus</p><h3>Der entscheidende Pitch im Konsortium</h3>'
          '<p>Eine Ausschreibung bei einem Großkunden, gemeinsam mit Kooperationspartnern gegen namhafte Wettbewerber. '
          'Statt Standardfolien liefern wir Medien, die zu 100&nbsp;% zeigen: Wir haben den Kunden verstanden – und die Lösung ist maßgeschneidert.</p></div>'
        + details("Medien, die Ergebnisse liefern") + '</div>', nr + 1, N, klasse="seite--hell")
    return [a, b]


def bauen():
    s1 = seite(titelseite(
        T, 'Marketing für Versicherer <span class="hl">anders gedacht.</span>',
        "Wir sind keine klassische Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das "
        "Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber.",
        kopfbild(T),
        [("Für wen", "Versicherer &amp; Makler"), ("Lösungen", "Vier Wege, ein Ergebnis"),
         ("Buchbar", "Komplett oder einzeln"), ("Grundlage", "Strategie vor Umsetzung")]))

    wege_icons = '<div class="wege4">' + "".join(
        f'<div>{ico(i, strich=1.3)}<b>{t}</b><p>{d}</p></div>' for i, t, _, d in WEGE) + '</div>'
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Unser Ansatz")
        + '<h2>Marketing, das Deine Strategie<br>zum Erfolg führt.</h2>'
        + '<p class="lead" style="max-width:150mm">Unsere langjährige Projekterfahrung und unsere tiefe Kenntnis von Geschäftsmodell, Strategie und '
          'Zielgruppen eines Versicherers fließen in jedes Projekt ein. Das macht uns von der ersten Minute an schnell und schlagkräftig.</p>'
        + punkte([("layout-grid", "Komplett oder einzeln", "Buche uns als klar definierte Marketingabteilung – oder hol Dir gezielt einzelne Medien dazu."),
                  ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe."),
                  ("circle-check", "Professionell umgesetzt", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – damit sie im entscheidenden Moment wirkt.")])
        + '</div><div class="rand" style="padding-top:12mm">' + kicker("Unsere Lösungen")
        + '<h2>Vier Wege. Ein Ergebnis:<br><span class="hl">Sichtbarkeit, die verkauft.</span></h2>'
        + '<p class="lead">Ob als Gesamtpaket oder einzeln buchbar – Du wählst, wir liefern professionell.</p>'
        + wege_icons + '</div>', 2, N)

    s3 = ueberblick(3)
    kap = mes(4) + sofort(6) + paid(8) + medien(10)

    s12 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Bereit, Dein Marketing auf das <span class="hl">nächste Level</span> zu bringen?',
                      "Kurze Wege statt langer Abstimmungsrunden: Schildere uns Deine Ausgangslage – wir melden uns zeitnah mit einem Vorschlag, welcher der vier Wege für Dich am meisten bringt.")
        + '</div>' + mt.draht(), 12, N)

    css = mt.CSS + """
.wege4 { display: grid; grid-template-columns: repeat(4, 1fr); gap: 6mm; margin-top: 10mm; }
.wege4 > div { border-top: 1.6px solid #1a1817; padding-top: 5mm; }
.wege4 svg { width: 9mm; height: 9mm; display: block; }
.wege4 b { display: block; margin-top: 3.5mm; font-family: 'Lora', Georgia, serif; font-size: 11pt; line-height: 1.25; min-height: 2.5em; }
.wege4 p { margin-top: 2mm; font-size: 8.6pt; line-height: 1.5; color: #3d3a37; }
.tabelle thead th { vertical-align: top; }
.tabelle .preis .klein { font-family: 'Poppins', Arial, sans-serif; font-weight: 400; font-size: 7.2pt; line-height: 1.4; margin-top: 1.4mm; }
.tabelle .seite-ref { font-weight: 600; }
.band--schwarz .hl { color: #1a1817; }
/* Kapitel-Einstieg */
.kap { display: flex; align-items: flex-end; gap: 5mm; margin-bottom: 5mm; }
.kap__nr { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 44pt; line-height: .8; letter-spacing: -.02em; }
.kap__linie { flex: 1; height: 1.6px; background: #1a1817; margin-bottom: 1.2mm; }
.kap-band { margin-top: 9mm; padding-top: 9mm; padding-bottom: 10mm; }
.kap-band .punkte { margin-top: 6mm; }
.details { margin-top: 3mm; color: #5c5853; }
.abschnitt { margin-top: 11mm; }
.tabelle--kompakt { margin-top: 6mm; }
.tabelle--kompakt thead th { padding-top: 3mm; padding-bottom: 3.5mm; }
.tabelle--kompakt td { padding-top: 3mm; padding-bottom: 3mm; }
/* MES */
.agentur { align-items: start; margin-top: 7mm; }
.agentur p { font-size: 10pt; line-height: 1.6; color: rgba(255,255,255,.85); }
/* sofort sichtbar */
.kasten--kompakt { padding: 5.5mm 7mm 6mm; }
.kasten--kompakt .punkte svg { display: none; }
.kasten--kompakt .punkte > div { padding-top: 3.4mm; }
/* Paid Ads */
.kanal svg { width: 7mm; height: 7mm; margin-bottom: 3mm; }
.antworten { display: flex; flex-wrap: wrap; gap: 1.4mm; }
.antworten span { font-size: 7.4pt; line-height: 1.3; padding: 1mm 2.6mm; border: 1px solid #1a1817; border-radius: 9mm; white-space: nowrap; }
.empf > div { grid-template-columns: 50mm 1fr; padding: 4mm 0; }
.medien-p { margin-top: 7mm; }
.medien-p svg { display: none; }
.empf h3 { display: flex; align-items: center; gap: 3mm; font-size: 13pt; }
.empf h3 svg { width: 6.5mm; height: 6.5mm; flex: 0 0 auto; }
.empf small { display: block; margin-top: 3mm; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; }
.empf .antworten { margin-top: 2mm; }
.pruef { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 5mm; }
.pruef div { border-top: 1px solid rgba(255,255,255,.35); padding-top: 2.6mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 10.5pt; line-height: 1.25; color: #fff; }
/* Medien */
.medien > div { grid-template-columns: 56mm 1fr; }
.liste small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.2mm; }
.faelle-l > div { padding: 6mm 0; }
"""
    return dokument(TITEL, [s1, s2, s3] + kap + [s12], extra_css=css)
