"""PDF „MarketingEcoSystem (MES)“ (Seite dashboard-digitales-marketing) – Stil: Muster KI zum Anfassen."""
from lib import titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, check, dokument
import _marketing_teile as mt

TITEL = "MarketingEcoSystem (MES) – empiria"
T = "MarketingEcoSystem (MES)"


def bauen():
    n = 6
    s1 = seite(titelseite(
        T, 'Du konzentrierst Dich<br>auf <span class="hl">Dein Business.</span>',
        "Unser MarketingEcoSystem (MES) führt Homepage, digitale Kanäle und zentrales Dashboard an einem Ort zusammen – "
        "damit alles ineinandergreift, statt nebeneinanderher zu laufen.",
        kopfbild(T),
        [("Für wen", "Versicherer &amp; Makler"), ("Überblick", "Alle Kanäle auf einen Blick"),
         ("Analyse", "Schwachstellen inkl. Lösung"), ("Investition", "ab 399 € mtl.")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:12mm">' + kicker("Echter Nutzen statt Pseudo-Reporting")
        + '<h2>Kein Kennzahlenfriedhof.<br>Ein Ökosystem, das lebt.</h2>'
        + '<p class="lead">Alle Kanäle laufen an einem Ort zusammen – bewertet statt nur gemacht, mit Lösung statt nur Problem.</p>'
        + punkte([("puzzle", "Kanäle greifen ineinander", "Homepage, Social Media und Content sind kein Nebeneinander einzelner Aktionen mehr, sondern Dein MES – Google Ads, Meta, Website und mehr an einem Ort."),
                  ("eye", "Kein Blindflug mehr", "Dein Marketing wird laufend geprüft – Schwachstellen fallen auf, bevor sie zum Problem werden, inklusive konkretem Lösungsvorschlag."),
                  ("zap", "Zurück in die Umsetzung", "Wir sehen, ob etwas funktioniert, wissen, warum wir etwas anpassen – und setzen die nächste Optimierung direkt um, ohne Extra-Auftrag.")])
        + '</div><div class="rand" style="padding-top:10mm">'
        + '<div class="kasten"><div class="zwei"><div><p class="label">Der Unterschied zur Agentur</p><h3>Du musst uns nicht briefen.</h3></div>'
          '<p style="margin-top:0">Bei einer Agentur liegt die Überlegung zu Markterfolg und Marketingstrategie bei Dir. Bei uns nicht: '
          'Wir holen die wichtigsten Informationen mit wenigen gezielten Fragen ab und sorgen für die permanente Umsetzung.</p></div></div>'
        + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:10mm"')
        + check(["Versicherer ohne eigenes Marketingteam", "Maklerunternehmen mit mehreren Mitarbeitenden",
                 "Versicherungsbüros, die digital sichtbar werden wollen", "Alle, die Wirkung sehen wollen statt Pseudo-Reporting"])
        + '</div>', 2, n)

    s3 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("So funktioniert Dein MES")
        + '<h2>Alles greift <span class="hl">ineinander.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Kanäle bringen Besucher auf die Landingpage, das Dashboard führt alle Informationen zusammen, '
          'trackt die Entwicklung und gibt Optimierungsempfehlungen zurück in die Kanäle.</p>'
        + punkte([("app-window", "Landingpage", "Das Herzstück: eine klar auf Deine Zielgruppe zugeschnittene Seite, die ein zentrales Problem löst und zum nächsten Schritt führt – laufend von uns betreut und optimiert."),
                  ("megaphone", "Social-Media-Kanäle", "LinkedIn, Facebook und Instagram: Profile gepflegt, Postings nach Content-Kalender, Kommentare aus der Zielgruppe inklusive Antwortvorschlägen."),
                  ("layout-dashboard", "Dashboard", "Führt die Informationen aus Homepage und Kanälen an einem Ort zusammen und trackt die Entwicklung. Daraus leiten wir Optimierungsempfehlungen ab.")])
        + '</div><div class="band band--hell wachsen" style="margin-top:14mm">' + kicker("Der Kreislauf")
        + '<h2>Fortlaufend aktuell.</h2>'
        + '<p class="lead">So bleibt Dein MES in einem fortlaufenden Kreislauf immer aktuell.</p>'
        + zeitstrahl([("01", "Konzeption &amp; Umsetzung", "Wir überlegen, wie das Ganze aufgebaut werden soll, und setzen es in Homepage, Kanälen und Content um."),
                      ("02", "Tracking &amp; Analyse", "Das Dashboard misst, ob eingetreten ist, was wir wollten, und wir werten die Entwicklung aus."),
                      ("03", "Ableitung Next Step", "Aus der Analyse leiten wir den nächsten Schritt ab – und starten wieder bei der Konzeption.")])
        + '</div>', 3, n)

    sp = [("Du setzt selbst um", "Eigenregie", "", False),
          ("Wir übernehmen alles", "Marketing as a Service", "Meistgewählt", True),
          ("Wir wachsen gemeinsam", "Unternehmertum", "", False)]
    zeilen = [
        ("Investition", ["ab 399 € mtl.", "ab 3.500 € mtl.", "Auf Anfrage"], "preis"),
        ("Leistung", ["Wir verknüpfen Deine Homepage und Kanäle mit unserem Dashboard inkl. Reporting – die Optimierung übernimmst Du selbst.",
                      "Wir übernehmen die laufende Betreuung und Optimierung von Homepage, Social-Media-Kanälen und Reporting.",
                      "Wir suchen unternehmerische Partnerschaften – wenn die Voraussetzungen für beide Seiten stimmen."], ""),
        ("Enthalten", [mt.ul(["Anbindung an Dashboard &amp; Reporting – ohne Eingriff in Homepage oder Kanäle",
                              "Regelmäßiges Reporting zu Status und Optimierungs&shy;möglichkeiten"]),
                       mt.ul(["Homepage – betreut &amp; laufend optimiert", "Firmenaccounts &amp; Profile: LinkedIn, Facebook, Instagram",
                              "Content-Kalender, Postings &amp; Umsetzung", "Monatlicher Austausch plus wöchentliches Reporting"]),
                       mt.ul(["Teil des Teams statt nur Dienstleister", "Kein laufendes Honorar, sondern Beteiligung am Erfolg",
                              "Langfristig, partnerschaftlich, auf Augenhöhe"])], ""),
        ("Rahmen", ["Mindestlaufzeit drei Monate, zzgl. einmaliger Setup-Kosten", "Mindestlaufzeit zwölf Monate, keine einmaligen Setup-Kosten",
                    "Gemeinsames Gespräch zur Prüfung, ob eine Beteiligung passt"], ""),
    ]
    s4 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Pakete")
        + '<h2>Drei Wege, <span class="hl">uns zu buchen.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Vom Dashboard in Eigenregie bis zur vollständigen Betreuung – wähle den Umfang, der wirklich zu Deinem Business passt.</p>'
        + mt.tabelle(sp, zeilen).replace('tabelle--fest', 'tabelle--fest tabelle--paket')
        + '<p class="notiz">Der Preis richtet sich nach dem vereinbarten Umfang. Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>'
        + '</div>', 4, n)

    ablauf = [
        ("Eigenregie", "Wir sichten Deine bestehende Homepage und Kanäle und verknüpfen sie mit Deinem Dashboard, ohne selbst etwas daran zu verändern. "
                       "Du bekommst wöchentlich ein Reporting zum Status und monatlich eine Bewertung mit Optimierungsvorschlägen – die Umsetzung entscheidest Du selbst."),
        ("Marketing as a Service", "Nach dem Kick-off mit Klärung der Marketingstrategie setzen wir Homepage, Kanäle und Dashboard erstmalig auf. "
                                   "Danach läuft die Betreuung dauerhaft weiter – mit halbjährlichem Strategie-Review, monatlichem Austausch mit fester Agenda und wöchentlichem Reporting."),
        ("Unternehmertum", "Im gemeinsamen Gespräch prüfen wir, ob die Voraussetzungen für eine Partnerschaft stimmen, und entwickeln ein individuelles Modell der Beteiligung. "
                           "Dann werden wir Teil des Teams und begleiten den Erfolg direkt mit."),
    ]
    s5 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Ablauf")
        + '<h2>So läuft es ab.</h2>'
        + '<div class="liste ablauf">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in ablauf) + '</div>'
        + '<div class="kasten" style="margin-top:12mm;padding:8mm 7mm"><div class="zwei"><div><p class="label">Alternative: Inhouse</p>'
          '<h3>Dein virtueller Marketingmitarbeiter.</h3></div>'
          '<p style="margin-top:0">Willst Du Marketing as a Service lieber selbst umsetzen, brauchst Du dafür jemanden im Team. '
          'Wie diese Person aufgestellt sein müsste, steht im Anforderungsprofil „Digitaler Marketingmanager (m/w/d)“ – als fertige Vorlage zum Download auf unserer Seite.</p></div></div>'
        + '</div>', 5, n, klasse="seite--hell")

    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">'
        + mt.schritte('Dein Marketing als <span class="hl">lebendes Ökosystem?</span>',
                      "Schildere uns Deine Ausgangslage – wir sagen Dir, welches Paket zu Deinem Haus passt.")
        + '</div>' + mt.draht(), 6, n)

    css = mt.CSS + """
.ablauf > div { padding: 7mm 0; }
.ablauf p { font-size: 9.4pt; }
.tabelle--paket td { padding-top: 4mm; padding-bottom: 4mm; }
"""
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=css)
