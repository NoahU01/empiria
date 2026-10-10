"""PDF „sofort sichtbar“ – Stil: Muster KI zum Anfassen.

Daniel 10.10.: keine Zahl der Zielgruppenpakete hervorheben, „Zielgruppenpaket“ nicht als Bildbeschriftung;
das Produkt-Logo (ink) darf als Kicker auf der Titelseite stehen.
"""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, check, dokument, ico
import _marketing_teile as mt

TITEL = "sofort sichtbar – empiria"
T = "sofort sichtbar"
LOGO = '<img class="ss-logo" src="assets/sofort-sichtbar-logo-ink.svg" alt="sofort sichtbar">'


def bauen():
    n = 6
    s1 = seite(titelseite(
        "LOGO", 'Digital sichtbar.<br><span class="hl">Ohne Briefing.</span><br>Sofort einsatzbereit.',
        "Ein fertiges System aus Postings, Landingpage und E-Mail-Funnel für Agenturleiter und Makler, die am Vertriebserfolg "
        "gemessen werden und für Marketing weder Zeit noch Nerven übrig haben.",
        kopfbild(T),
        [("Start", "Ohne Briefing"), ("Paket", "Alles in einem"), ("Auftritt", "Eigener Auftritt"), ("Investition", "ab 349 € mtl.")]
    ).replace('<p class="kicker">LOGO</p>', f'<p class="kicker ss-kicker">{LOGO}</p>'))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Was sofort sichtbar mitbringt")
        + '<h2>Fertig gedacht,<br>nicht nur fertig gebaut.</h2>'
        + '<p class="lead">Alles in einem Paket – abgestimmt auf Deine Vertriebsschwerpunkte.</p>'
        + punkte([("message-square-text", "Social Media Postings", "Fertige Postings, die genau auf Deine Zielgruppe abgestimmt sind – sofort einsetzbar, ohne eigene Content-Produktion."),
                  ("mail", "E-Mail-Funnel", "Aktiviert Deine Bestandskunden und leitet sie auf die passende, zielgruppenspezifische Landingpage weiter."),
                  ("app-window", "Passende Landingpages", "Mit Download-Dokument, integrierter Podcast-Folge und optimierten Kontaktdaten – fertig für jede Zielgruppe und jeden Anlass.")])
        + '</div><div class="band band--schwarz wachsen mitte">' + kicker("Individualisierung")
        + '<h2>Alles in Deinem <span class="hl">Corporate Design.</span></h2>'
        + '<p class="lead" style="color:rgba(255,255,255,.85);max-width:150mm">Logo, Bilder, Kontaktdaten und Farbwelt werden eingebunden, damit alles aussieht, als wäre es für Deine Agentur gebaut.</p>'
        + '<div class="ind">' + "".join(f'<span>{x}</span>' for x in ["Logo", "Bilder", "Kontaktdaten", "Farbwelt"]) + '</div>'
        + '</div>', 2, n, hell_fuss=True)

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
    kasten = ('<div class="kasten kasten--kompakt" style="margin-top:6mm"><p class="label">Für jedes Paket gilt</p>'
              + punkte([("timer", "Drei Monate Mindestlaufzeit", "Je Vertriebsstrecke – danach verlängern, Zielgruppe wechseln oder unkompliziert kündigen."),
                        ("app-window", "In Deinem Design", "Logo, Bilder, Kontaktdaten und Farbwelt werden auf Deine Agentur angepasst."),
                        ("shield-check", "Anfragen direkt bei Dir", "Per Anruf, E-Mail oder Formular – ohne Umweg über uns. Landingpages auf EU-Servern.")])
              .replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:5mm;') + '</div>')
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Preise")
        + '<h2>Die passenden Pakete für<br><span class="hl">Deinen Vertriebsfokus.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Monatlich buchbar, mit Rabatt bei jährlicher Zahlung – jede Vertriebsstrecke mit einer Mindestlaufzeit von drei Monaten.</p>'
        + mt.tabelle(sp, zeilen)
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>' + kasten
        + '</div>', 3, n)

    vergleich = (
        '<div class="kasten vergleich">'
        '<div class="v-zeile"><span class="v-label">Klassische Agentur</span><div class="v-bahn">'
        + "".join(f'<span class="v-pill v-pill--voll">{x}</span>' for x in ["Auftragsklärung", "Konzeption", "Umsetzung", "Optimierung"])
        + f'<span class="v-ico">{ico("rocket")}</span></div></div>'
        '<div class="v-zeile"><span class="v-label">sofort sichtbar</span><div class="v-bahn v-bahn--ss">'
        '<span class="v-pill">Auftragsklärung</span>'
        f'<span class="v-ico v-ico--gelb">{ico("rocket")}</span>'
        f'<span class="v-bonus">{ico("timer")}Mehr Zeit für Kundengespräche</span></div></div></div>')
    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>Monate werden <span class="hl">zu Tagen.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Mit sofort sichtbar bist Du online, bevor eine klassische Agentur die Auftragsklärung abgeschlossen hat.</p>'
        + vergleich + '</div>'
        + '<div class="band band--hell wachsen mitte" style="margin-top:14mm">' + kicker("In vier Schritten live")
        + '<h2>Vom Gespräch zum fertigen Auftritt.</h2>'
        + zeitstrahl([("01", "Auftragsklärung", "Wir klären kurz Deinen Vertriebsfokus – ohne die wochenlange Konzeptphase einer klassischen Agentur."),
                      ("02", "Zielgruppen auswählen", "Du wählst aus den vorbereiteten Profilen die aus, die zu Deinen Kundinnen und Kunden passen."),
                      ("03", "Stil &amp; Auftritt festlegen", "Du wählst Deinen Stil und bringst Dein Design ein – Logo, Bilder, Kontaktdaten, Farbwelt."),
                      ("04", "Live gehen", "Postings, Landingpage und E-Mail-Funnel gehen live – und Du hast mehr Zeit für Kundengespräche.")])
        + '</div>', 4, n)

    fragen = [
        ("Kann ich mehrere Zielgruppenpakete gleichzeitig buchen?", "Ja. Du kannst mehrere Vertriebsstrecken parallel buchen oder eine einzelne Lizenz im Jahresverlauf für wechselnde Zielgruppen nutzen – je nachdem, was gerade in Deinem Vertriebsfokus steht."),
        ("Wofür kann ich sofort sichtbar einsetzen?", "Für Neukundengewinnung, Bestandskundenaktivierung und im Beratungsalltag – etwa mit einer kurzen Erinnerungs-Mail samt passender Landingpage vor und nach einem Termin."),
        ("Wie kommen Anfragen DSGVO-konform bei mir an?", "Direkt bei Dir – per Anruf, E-Mail oder Formular, das automatisch an Deine Adresse weitergeleitet wird. Es gibt keinen Umweg über uns, und die Landingpages laufen auf Servern innerhalb der EU."),
        ("Wie individuell sind die Landingpages?", "Logo, Bilder, Kontaktdaten und Farbwelt werden auf Deine Agentur angepasst. Struktur und Inhalte bleiben bewusst standardisiert, damit Du schnell online bist – für eine komplett individuelle Lösung sprechen wir gerne separat."),
        ("Gibt es eine Mindestlaufzeit?", "Ja, drei Monate je Vertriebsstrecke, damit Landingpage und Sichtbarkeit Zeit haben zu wirken. Danach kannst Du verlängern, die Zielgruppe wechseln oder unkompliziert kündigen."),
        ("Wie hoch ist mein monatlicher Zeitaufwand?", "Sehr gering. Nach der Einrichtung übernehmen wir den technischen Teil – Du investierst Deine Zeit nur ins Posten der Inhalte und in Deine eigentlichen Kundengespräche."),
    ]
    s5 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("FAQ")
        + '<h2>Häufige Fragen.</h2>'
        + '<p class="lead" style="max-width:150mm">Was Agenturleiterinnen und Agenturleiter uns am häufigsten fragen.</p>'
        + '<div class="liste faq">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in fragen) + '</div>'
        + '</div>', 5, n, klasse="seite--hell")

    extra = f'<div>{ico("app-window")}sofortsichtbar.de</div>'
    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Bereit, <span class="hl">sofort sichtbar</span> zu werden?',
                      "Kurze Wege statt langer Abstimmungsrunden: Sag uns, welche Zielgruppen in Deinem Vertriebsfokus stehen – wir melden uns zeitnah mit einem konkreten Vorschlag.")
        + '</div>' + mt.draht(extra), 6, n)

    css = mt.CSS + """
.ss-kicker img.ss-logo { height: 4.6mm; width: auto; display: block; }
.vergleich { margin-top: 9mm; padding: 6mm 6mm; display: grid; gap: 3.5mm; }
.v-zeile { display: grid; grid-template-columns: 30mm 1fr; align-items: center; gap: 4mm; }
.v-label { font-size: 7pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #fff; }
.v-zeile:last-child .v-label { color: #fff400; }
.v-bahn { display: flex; align-items: center; gap: 2mm; padding: 2.6mm; border-radius: 3.5mm; background: rgba(255,255,255,.06); border: 1px solid transparent; }
.v-bahn--ss { border-color: rgba(255,244,0,.6); }
.v-pill { display: flex; align-items: center; justify-content: center; height: 11mm; padding: 0 3mm; border-radius: 2.6mm; background: rgba(255,255,255,.1); font-size: 7.4pt; font-weight: 600; color: #fff; white-space: nowrap; }
.v-pill--voll { flex: 1 1 0; }
.v-bahn--ss .v-pill { font-size: 6.6pt; padding: 0 2.4mm; }
.v-ico { flex: 0 0 auto; display: grid; place-items: center; width: 11mm; height: 11mm; border-radius: 2.6mm; border: 1px solid rgba(255,255,255,.35); color: #fff; }
.v-ico svg { width: 5.4mm; height: 5.4mm; }
.v-ico--gelb { color: #fff400; border-color: #fff400; }
.v-bonus { display: flex; align-items: center; gap: 2mm; margin-left: 2mm; font-size: 8pt; font-weight: 600; color: #fff; }
.v-bonus svg { width: 4.6mm; height: 4.6mm; color: #fff400; }
.zs h3 { font-size: 11.5pt; }
.tabelle .preis .klein { font-family: 'Poppins', Arial, sans-serif; font-weight: 400; font-size: 7.2pt; line-height: 1.4; margin-top: 1.4mm; }
.kasten--kompakt { padding: 5.5mm 7mm 6mm; }
.kasten--kompakt .punkte svg { display: none; }
.kasten--kompakt .punkte > div { padding-top: 3.4mm; }
.team3 .kontaktdaten { display: grid; grid-template-columns: 1fr 1fr; }
.faq > div { padding: 6.4mm 0; }
.band--schwarz .hl { color: #1a1817; }
.ind { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 10mm; }
.ind span { display: block; padding-top: 4mm; border-top: 1.6px solid #fff400; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; color: #fff; }
.faq p { font-size: 9.2pt; }

"""
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=css)
