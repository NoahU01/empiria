"""PDF „MarketingEcoSystem (MES)“ (Seite dashboard-digitales-marketing) – Runde 2, Stand der 2.0-Seite 10.10.2026.

Inhalt inkl. aller Pop-ups: Erklär-Knöpfe (Landingpage, Social-Media-Kanäle, Dashboard, MES-Kreislauf), MES-Struktur,
„Mehr erfahren“ je Paket (Eigenregie, Marketing as a Service, Unternehmertum) und Anforderungsprofil-Hinweis.
"""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, dokument, ico
import _marketing_teile as mt

TITEL = "MarketingEcoSystem (MES) – empiria"
T = "MarketingEcoSystem (MES)"


def bauen():
    n = 7
    s1 = seite(titelseite(
        T, 'Du konzentrierst Dich auf <span class="hl">Dein Business.</span>',
        "Unser MarketingEcoSystem (MES) führt Homepage, digitale Kanäle und zentrales Dashboard an einem Ort zusammen – "
        "damit alles ineinandergreift, statt nebeneinanderher zu laufen.",
        kopfbild(T),
        [("Für wen", "Versicherer &amp; Makler"), ("Überblick", "Alle Kanäle auf einen Blick"),
         ("Analyse", "Schwachstellen inkl. Lösungsvorschlag"), ("Investition", "ab 399 € mtl.")]))

    # 2 · Ansatz (gelb) + „Der Unterschied zur Agentur“ (schwarzes Band, auf der Seite hervorgehoben)
    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Echter Nutzen statt Pseudo-Reporting")
        + '<h2>Kein Kennzahlenfriedhof.<br>Ein Ökosystem, das lebt.</h2>'
        + '<p class="lead">Alle Kanäle laufen an einem Ort zusammen – bewertet statt nur gemacht, mit Lösung statt nur Problem.</p>'
        + punkte([("puzzle", "Kanäle greifen ineinander", "Homepage, Social Media und Content sind kein Nebeneinander einzelner Aktionen mehr, die im Sand verlaufen, sondern Dein MES – Google Ads, Meta, Website und mehr an einem Ort."),
                  ("eye", "Kein Blindflug mehr", "Dein Marketing wird laufend geprüft – Schwachstellen fallen auf, bevor sie zum Problem werden, inklusive konkretem Lösungsvorschlag."),
                  ("zap", "Zurück in die Umsetzung", "Wir sehen, ob etwas funktioniert, wissen, warum wir etwas anpassen – und setzen die nächste Optimierung direkt um, ohne Extra-Auftrag.")])
        + '</div><div class="band band--schwarz wachsen mitte">' + kicker("Der Unterschied zur Agentur")
        + '<h2>Du musst uns <span class="hl">nicht briefen.</span></h2>'
        + '<div class="zwei agentur"><p>Bei einer Agentur liegt die Überlegung zu Markterfolg und Marketingstrategie bei Dir – '
          'Du musst briefen und sagen, was zu tun ist.</p>'
          '<p>Bei uns nicht: Wir sind Profis für das, was wir tun, holen die wichtigsten Informationen mit wenigen gezielten Fragen ab '
          'und sorgen für die permanente Umsetzung.</p></div>'
        + '</div>', 2, n, hell_fuss=True)

    # 3 · Alles greift ineinander – die drei Erklär-Pop-ups + MES-Struktur
    bausteine = [
        ("app-window", "Landingpage",
         "<p>Das Herzstück Deines MES: eine klar auf Deine Zielgruppe zugeschnittene Seite, die genau ein zentrales Problem löst und "
         "Interessierte zum nächsten Schritt führt. Sie wird laufend von uns betreut und optimiert – auf Basis dessen, was das Dashboard zeigt.</p>"),
        ("megaphone", "Social-Media-Kanäle",
         "<p>LinkedIn, Facebook und Instagram sorgen für einen dauerhaften Außenauftritt bei der richtigen Zielgruppe und bringen Menschen auf Deine Landingpage.</p>"
         + mt.ul(["<b>Profile</b> – Unternehmens- und ggf. persönliche Profile, gepflegt und aktuell",
                  "<b>Postings</b> – geplant, produziert und veröffentlicht nach Content-Kalender",
                  "<b>Kommentare</b> – Reaktionen aus der Zielgruppe, inklusive Antwortvorschlägen"])),
        ("layout-dashboard", "Dashboard",
         "<p>Führt die Informationen aus Homepage und Kanälen an einem Ort zusammen und trackt, wie sich die Entwicklungen darstellen. "
         "Aus den Ergebnissen leiten wir Optimierungsempfehlungen ab, die direkt wieder in die Kanäle einfließen – Dein MES verbessert sich fortlaufend.</p>"),
    ]
    kreislauf = ('<div class="kasten kreis"><p class="label">Der Kreislauf Deines MES</p>'
                 + zeitstrahl([("01", "Konzeption &amp; Umsetzung", "Wir überlegen uns, wie das Ganze aufgebaut werden soll, und setzen es in Homepage, Kanälen und Content um."),
                               ("02", "Tracking &amp; Analyse", "Das Dashboard misst, ob eingetreten ist, was wir wollten, und wir werten die Entwicklung aus."),
                               ("03", "Ableitung Next Step", "Aus der Analyse leiten wir den nächsten Schritt ab – und starten wieder bei der Konzeption.")])
                 + '</div>')
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("MarketingEcoSystem (MES)")
        + '<h2>Alles greift <span class="hl">ineinander.</span></h2>'
        + '<p class="lead" style="max-width:165mm">Kanäle bringen Besucher auf die Landingpage, das Dashboard führt alle Informationen zusammen, '
          'trackt die Entwicklung und gibt Optimierungsempfehlungen zurück in die Kanäle. So bleibt Dein MES in einem fortlaufenden Kreislauf immer aktuell.</p>'
        + '<div class="liste bausteine">' + "".join(
            f'<div><h3>{ico(i)}{t}</h3><div>{txt}</div></div>' for i, t, txt in bausteine) + '</div>'
        + kreislauf + '</div>', 3, n)

    # 4 · Pakete (Post-Karten der Seite als Vergleichstabelle)
    s4 = seite(kopf(T) + _pakete(), 4, n)

    # 5 · So läuft es ab: Eigenregie + Marketing as a Service (Pop-ups „Mehr erfahren“)
    takte = [("Laufende Betreuung", "durchgehend"), ("Review zur Marketingstrategie", "alle 6 Monate"),
             ("Persönlicher Austausch", "monatlich"), ("Digitales Reporting", "wöchentlich")]
    maas = ('<div class="kasten maas"><p class="label">Marketing as a Service – so läuft es ab</p><div class="maas__raster">'
            '<div class="maas__kick"><h3>Kick-off</h3><ul><li>Klärung Marketingstrategie</li><li>Erstmaliges Aufsetzen von Homepage, Kanälen und Dashboard</li></ul></div>'
            '<div class="maas__takte">' + "".join(f'<div><b>{t}</b><span>{z}</span></div>' for t, z in takte) + '</div></div>'
            '<p>Nach dem Kick-off mit Klärung der Marketingstrategie und dem erstmaligen Aufsetzen von Homepage, Kanälen und Dashboard läuft die Betreuung '
            'dauerhaft weiter – mit einem halbjährlichen Review zur Marketingstrategie, monatlichem Austausch mit fester Agenda und wöchentlichem Reporting.</p></div>')
    s5 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("So läuft es ab")
        + '<h2>Eigenregie <span class="hl">Schritt für Schritt.</span></h2>'
        + zeitstrahl([("01", "Bestandsaufnahme", "Wir sichten Deine bestehende Homepage und Kanäle – Voraussetzung ist, dass beides bereits da ist."),
                      ("02", "Anbindung", "Wir verknüpfen Homepage und Kanäle mit Deinem Dashboard und binden sie ins Reporting ein, ohne selbst etwas daran zu verändern."),
                      ("03", "Laufendes Reporting", "Du bekommst wöchentlich ein Reporting zum Status und monatlich eine Bewertung inklusive Optimierungsvorschlägen."),
                      ("04", "Umsetzung in Eigenregie", "Die Optimierung entscheidest und setzt Du selbst um – wir liefern die Grundlage dafür.")])
        + maas + '</div>', 5, n)

    # 6 · Unternehmertum + Alternative: Inhouse
    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("So läuft es ab")
        + '<h2>Unternehmertum <span class="hl">als Partner.</span></h2>'
        + zeitstrahl([("01", "Gemeinsames Gespräch", "Wir schauen gemeinsam, ob die Voraussetzungen für eine Partnerschaft stimmen – und ob wir zueinander passen."),
                      ("02", "Individuelles Modell", "Auf dieser Grundlage entwickeln wir gemeinsam, wie eine Beteiligung konkret aussehen könnte."),
                      ("03", "Umsetzung als Partner", "Wir werden Teil des Teams und begleiten den Erfolg direkt mit – statt nur laufend Rechnungen zu stellen.")])
        + '</div><div class="band band--hell wachsen" style="margin-top:14mm">' + kicker("Alternative: Inhouse")
        + '<h2>Dein virtueller Marketingmitarbeiter.</h2>'
        + '<div class="zwei inhouse"><p>Willst Du Marketing as a Service lieber selbst umsetzen, statt es zu buchen? Dann brauchst Du dafür jemanden im Team.</p>'
          '<p>Nur: Wie müsste diese Person eigentlich aufgestellt sein, um alles das abzudecken, was wir hier übernehmen? Wir haben das Anforderungsprofil '
          'aufgeschrieben – als fertiges Konkurrenzprodukt zu uns, das Du Dir direkt herunterladen kannst.</p></div>'
        + '<div class="kasten" style="margin-top:8mm"><div class="zwei"><div><p class="label">Anforderungsprofil</p>'
          '<h3>Digitaler Marketingmanager (m/w/d)</h3>'
          '<p>Aufgaben, Fähigkeiten und Rahmen für Deinen Marketingmitarbeiter – als fertige Vorlage zum Download auf unserer Seite.</p></div>'
          '<p style="margin-top:0">Als Stratege, Controller, Grafiker und Entwickler in einem: Bei uns bekommst Du dieses Profil als eingespieltes Team, '
          'ohne die Suche, die Einarbeitung und das Risiko einer Einzelperson.</p></div></div>'
        + '</div>', 6, n, klasse="")

    s7 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Bereit, Dein Marketing auf das <span class="hl">nächste Level</span> zu bringen?',
                      "Kurze Wege statt langer Abstimmungsrunden: Schildere uns Deine Ausgangslage – wir sagen Dir, welches Paket zu Deinem Haus passt.")
        + '</div>' + mt.draht(), 7, n)

    css = mt.CSS + """
.agentur { align-items: start; margin-top: 8mm; }
.agentur p { font-size: 10pt; line-height: 1.6; color: rgba(255,255,255,.85); }
.bausteine > div { grid-template-columns: 50mm 1fr; padding: 4.2mm 0; }
.bausteine > div { align-items: start; }
.bausteine h3 { display: flex; align-items: center; gap: 3mm; }
.bausteine h3 svg { width: 6mm; height: 6mm; flex: 0 0 auto; }
.bausteine p { font-size: 9pt; }
.bausteine ul { list-style: none; margin-top: 2mm; }
.bausteine li { position: relative; padding-left: 3.6mm; margin-top: 1.2mm; font-size: 8.8pt; color: #3d3a37; }
.bausteine li::before { content: ""; position: absolute; left: 0; top: 2mm; width: 1.3mm; height: 1.3mm; border-radius: 50%; background: #1a1817; }
.kreis { margin-top: 9mm; padding: 6mm 7mm 4mm; }
.kreis .zs { margin-top: 6mm; }
.kreis .zs::before { background: rgba(255,255,255,.4); }
.kreis .zs .punkt { background: #fff400; box-shadow: 0 0 0 1.2mm #1a1817; }
.kreis .zs .nr { color: #fff400; }
.kreis .zs h3 { color: #fff; font-size: 11.5pt; }
.kreis .zs p { color: rgba(255,255,255,.8); margin-top: 1.6mm; font-size: 8.4pt; }
.maas { margin-top: 16mm; padding: 8mm 7mm; }
.band--schwarz .hl { color: #1a1817; }
.maas__raster { display: grid; grid-template-columns: 52mm 1fr; gap: 7mm; margin-top: 6mm; }
.maas__kick { border-top: 1.6px solid rgba(255,255,255,.35); padding-top: 3.5mm; }
.maas__kick h3 { margin-top: 0; font-size: 12pt; }
.maas__kick ul { list-style: none; margin-top: 2mm; }
.maas__kick li { position: relative; padding-left: 3.6mm; margin-top: 1.4mm; font-size: 8.6pt; color: rgba(255,255,255,.82); }
.maas__kick li::before { content: ""; position: absolute; left: 0; top: 2mm; width: 1.3mm; height: 1.3mm; border-radius: 50%; background: #fff400; }
.maas__takte > div { display: flex; justify-content: space-between; align-items: baseline; padding: 4mm 0; border-top: 1px solid rgba(255,255,255,.25); }
.maas__takte > div:first-child { border-top: 1.6px solid rgba(255,255,255,.35); }
.maas__takte b { font-family: 'Lora', Georgia, serif; font-size: 10.5pt; }
.maas__takte span { font-size: 7pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }
.maas > p { margin-top: 7mm; font-size: 8.6pt; }
.inhouse { align-items: start; margin-top: 6mm; }
.inhouse p { font-size: 9.4pt; line-height: 1.6; }
.tabelle--paket td { padding-top: 3.2mm; padding-bottom: 3.2mm; }
.tabelle .preis .klein { font-family: 'Poppins', Arial, sans-serif; font-weight: 400; font-size: 7.2pt; }
"""
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6, s7], extra_css=css)


def _pakete():
    sp = [("Du setzt selbst um", "Eigenregie", "", False),
          ("Wir übernehmen alles", "Marketing as a Service", "Meistgewählt", True),
          ("Wir wachsen gemeinsam", "Unternehmertum", "", False)]
    zeilen = [
        ("Investition", ['ab 399 €<span class="klein">monatlich</span>', 'ab 3.500 €<span class="klein">monatlich</span>',
                         'Auf Anfrage<span class="klein">Partnerschaft</span>'], "preis"),
        ("Leistung", ["Wir verknüpfen Deine Homepage und digitalen Kanäle mit unserem Dashboard inkl. Reporting – die Optimierung übernimmst Du selbst.",
                      "Wir übernehmen die laufende Betreuung und Optimierung von Homepage, Social-Media-Kanälen und Reporting.",
                      "Wir suchen unternehmerische Partnerschaften – wenn die Voraussetzungen für beide Seiten stimmen."], ""),
        ("Enthalten", [mt.ul(["Anbindung an unser Dashboard &amp; Reporting – ohne Eingriff in Homepage oder Kanäle",
                              "Regelmäßiges Reporting zum Status und zu Optimierungs&shy;möglichkeiten"]),
                       mt.ul(["Homepage – von uns betreut &amp; laufend optimiert", "Firmenaccounts &amp; Profile: LinkedIn, Facebook, Instagram",
                              "Content-Kalender, Postings &amp; Umsetzung aus einer Hand", "Monatlicher Austausch plus wöchentliches Reporting"]),
                       mt.ul(["Teil des Teams statt nur Dienstleister", "Kein laufendes Honorar, sondern Beteiligung am Erfolg",
                              "Für Unternehmen mit Potenzial, das wir mit aufbauen wollen", "Langfristig, partnerschaftlich, auf Augenhöhe"])], ""),
        ("Rahmen", ["Mindestlaufzeit drei Monate zzgl. einmaliger Setup-Kosten", "Mindestlaufzeit zwölf Monate, keine einmaligen Setup-Kosten",
                    "Gemeinsames Gespräch zur Prüfung, ob eine Beteiligung zueinander passt"], ""),
    ]
    return ('<div class="rand" style="padding-top:16mm">' + kicker("Pakete")
            + '<h2>Drei Wege, <span class="hl">uns zu buchen.</span></h2>'
            + '<p class="lead" style="max-width:150mm">Vom Dashboard in Eigenregie bis zur vollständigen Betreuung – wähle den Umfang, der wirklich zu Deinem Business passt.</p>'
            + mt.tabelle(sp, zeilen).replace('tabelle--fest', 'tabelle--fest tabelle--paket')
            + '<p class="notiz">Der Preis richtet sich nach dem vereinbarten Umfang. Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p></div>')
