"""PDF „Workshops“ – Runde 3 (10.10.2026): Übersichts-PDF mit Kapiteln.
Aufbau: Titel · Ansatz · Überblick (Liste + Vergleichstabelle ohne gelbe Spalte, die Seite markiert keinen Favoriten)
· Kapitel 01 KI zum Anfassen · 02 Sprint Landingpage · 03 Moderation deines Workshops · Schluss.
Inhalte der Kapitel verdichtet aus den 2.0-Unterseiten bzw. ihren Modulen (die Module bleiben unverändert).
„48“ steht nur dort, wo die Seiten es selbst nennen: im Überblick (Text der Workshops-Seite) und einmal im Sprint-Kapitel."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument, ico)
import sprint_landingpage

TITEL = "Workshops – empiria"
T = "Workshops"

CSS = sprint_landingpage.CSS + """
.tabelle--formate { table-layout: fixed; margin-top: 10mm; }
.tabelle--formate .zeile, .tabelle--formate thead th:first-child { width: 30mm; }
.tabelle--formate thead th { vertical-align: top; padding-top: 2mm; }
.tabelle--formate thead th b { white-space: normal; line-height: 1.15; margin-top: 1mm; }
.tabelle--formate td { padding-top: 4.6mm; padding-bottom: 4.6mm; }
.tabelle--formate .staffel { display: grid; grid-template-columns: auto 1fr; column-gap: 2.5mm; row-gap: .8mm; }
.tabelle--formate .staffel b { font-family: 'Lora', Georgia, serif; white-space: nowrap; }
.formate > div { grid-template-columns: 56mm 1fr; }
.formate small { display: block; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.2mm; }
.kontakt3 .team { margin-top: 9mm; gap: 12mm; }
.kontakt3 .kontaktdaten { grid-template-columns: 1.35fr 1fr 1fr; margin-top: 9mm; }
.kontakt3 .kontaktdaten div { justify-content: center; }
/* Kapitel-Einstieg: große Kapitelnummer */
.kap { display: flex; align-items: flex-end; gap: 5mm; margin-bottom: 5mm; }
.kap__nr { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 44pt; line-height: .8; letter-spacing: -.02em; }
.kap__linie { flex: 1; height: 1.6px; background: #1a1817; margin-bottom: 1.2mm; }
.kapnr-alt { display: block; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 50pt; line-height: .9; letter-spacing: -.03em; margin-bottom: 5mm; }
.kap-kurz .tabelle td { padding-top: 2.8mm; padding-bottom: 2.8mm; }
.kap-kurz .tabelle thead th { padding-top: 4mm; padding-bottom: 3.5mm; }
.liste--kap > div { padding: 4.6mm 0; }
.liste--kap h3 { font-size: 11pt; }
.kasten--fokus .kopfzeile { padding: 2mm 0 4mm; border-bottom: 1px solid rgba(255,255,255,.18); }
.kasten--fokus .kopfzeile h3 { margin-top: 1.5mm; }
.kasten--fokus .zeile { display: grid; grid-template-columns: 34mm 1fr; gap: 8mm; padding: 3.4mm 0; border-bottom: 1px solid rgba(255,255,255,.18); }
.kasten--fokus .zeile:last-child { border-bottom: 0; }
.kasten--fokus .zeile p { margin-top: 0; }
.kasten--fokus .zeile .label { padding-top: .8mm; }
.paket--kap { margin-top: 8mm; grid-template-columns: 58mm 1fr; }
.paket--kap .paket__preis { padding: 7mm 7mm; }
.paket--kap .paket__preis b { font-size: 21pt; }
.paket--kap .paket__liste { padding: 4mm 8mm; }
.paket--kap .paket__liste li { padding: 2.6mm 0 2.6mm 8mm; font-size: 8.8pt; }
.paket--kap .paket__liste li::before { top: 4mm; }
"""

FORMATE = [
    ("Format 01", "KI zum Anfassen",
     "Echte KI-Tools, echte Usecases aus der Versicherungsbranche – Schluss mit Arbeitskreisen ohne Praxis."),
    ("Format 02", "Sprint Landingpage",
     "Deine Landingpage in 48 Stunden live – für den Moment, in dem es schnell gehen muss."),
    ("Format 03", "Moderation deines Workshops",
     "Gezielte Aktivierung, Perspektivwechsel und Handlungsklarheit – für Ergebnisse, mit denen sich weiterarbeiten lässt."),
]

N = 10


def kapitel_kopf(nr, name, h2, lead):
    """Kapitel-Einstieg am Seitenanfang: große Nummer, Kicker = Unterseite, H2 = Kopfzeile, Lead = Kopftext."""
    return (f'<div class="rand" style="padding-top:16mm"><div class="kap"><span class="kap__nr">{nr}</span><span class="kap__linie"></span></div>' + kicker(name)
            + f'<h2>{h2}</h2><p class="lead">{lead}</p></div>')


def details(name):
    return f'<p class="notiz">Alle Details: eigenes PDF „{name}“ auf empiria.de</p>'


def ueberblick_liste(nr):
    zeilen = "".join(f'<div><div><small>{k}</small><h3>{t}</h3></div><p>{a}</p></div>' for k, t, a in FORMATE)
    return seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:13mm;padding-bottom:14mm">' + kicker("Unser Ansatz")
        + '<h2>Workshops, die nicht<br>bei der Theorie bleiben.</h2>'
        + '<p class="lead">Wir gehen direkt in die Anwendung – mit klaren Ergebnissen und einer Moderation, die trägt.</p>'
        + punkte([("zap", "Direkt anwendbar", "Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag."),
                  ("target", "Auf Dein Team zugeschnitten", "Jeder Workshop ist auf Deinen Anwendungsfall und Dein Team zugeschnitten – nicht von der Stange."),
                  ("users", "Professionell moderiert", "Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.")])
        + '</div><div class="rand" style="padding-top:13mm">' + kicker("Unsere Workshops")
        + '<h2>Drei Formate. Ein Ziel: Ergebnisse.</h2><p class="lead">Wähle das Format – wir bringen Dein Team ans Ziel.</p>'
        + f'<div class="liste formate">{zeilen}</div>'
        + '</div>', nr, N)


def ueberblick_tabelle(nr):
    cols = [("Format 01", "KI zum<br>Anfassen"), ("Format 02", "Sprint<br>Landingpage"), ("Format 03", "Moderation deines<br>Workshops")]
    head = '<th></th>' + "".join(f'<th><small>{d}</small><b>{t}</b></th>' for d, t in cols)

    def zeile(label, werte, cls=""):
        return f'<tr><td class="zeile">{label}</td>' + "".join(f'<td class="{cls}">{w}</td>' for w in werte) + '</tr>'
    staffel = ('<div class="staffel"><span>½ Tag</span><b>2.500 €</b><span>1 Tag</span><b>3.900 €</b>'
               '<span>2 Tage</span><b>7.350 €</b></div>')
    body = (zeile("Investition", ["ab 2.500 €", "15.850 €", "auf Anfrage"], "preis")
            + zeile("Preise", [staffel, "Ein Leistungspaket: Konzeption, Umsetzung und Live-Schaltung",
                               "Umfang, Termine und Investition klären wir gemeinsam mit Dir"])
            + zeile("Umfang", ["½ bis 2 Tage, je nach Format", "2–3 Std. Onboarding online, 2 Tage Sprint vor Ort, Review",
                               "Abgestimmt auf Dein Thema und Deine Runde"])
            + zeile("Formate", ["KI&#8209;Einstieg, KI&#8209;Sprint, KI&#8209;Deep&#8209;Dive", "Sprint-Workshop mit 2 Beraterinnen und Beratern von empiria",
                                "Strukturen, Prozesse &amp; Rollen, Kreativ- und Vertriebsworkshops"])
            + zeile("Ergebnis", ["Direkt verwertbare Erkenntnisse aus echten Usecases", "Deine fertige Landingpage – live geschaltet",
                                 "Handlungsklarheit und Strukturen, die im Alltag tragen"])
            + zeile("Ansprech&shy;partner", ["Daniel Ströbel<br>Noah Hermanns", "Daniel Ströbel<br>Noah Hermanns", "Daniel Ströbel<br>Kerstin Christ"]))
    return seite(kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Überblick")
                 + '<h2>Die Formate im Überblick.</h2><p class="lead">Umfang, Ergebnis und Investition der drei Workshops – die Einzelheiten stehen in den Kapiteln ab Seite 4.</p>'
                 + f'<table class="tabelle tabelle--formate"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
                 + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen. KI zum Anfassen inklusive Vorbereitung und Dokumentation der Ergebnisse; '
                   'Sprint Landingpage zzgl. Anfahrt und zwei Übernachtungen für je zwei Personen.</p>'
                 + '</div>', nr, N)


# ---------- Kapitel 01 · KI zum Anfassen ----------
def ki_a(nr):
    tools = [("chatgpt", "ChatGPT"), ("claude", "Claude"), ("perplexity", "Perplexity"), ("gemini", "Gemini"), ("notebooklm", "NotebookLM"), ("nanobanana", "Nano Banana")]
    return seite(
        kopf(T)
        + kapitel_kopf("01", "KI zum Anfassen", 'Deine KI. <span class="hl">Zum Anfassen.</span><br>Volle Wirkung.',
                       "Über KI wird geredet – oft von Menschen, die sie selbst noch nie genutzt haben. Wir gehen direkt in die Anwendung: "
                       "verschiedene KI-Tools, echte Fälle aus Eurem Alltag, Erkenntnisse, die sofort etwas bringen.")
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:11mm;padding-bottom:12mm">' + kicker("Das bekommst Du")
        + '<h2>Anwendung statt Vortrag.</h2>'
        + punkte([("zap", "Direkt in die Anwendung", "Kein weiterer Arbeitskreis, keine Theorie – wir starten sofort, mit direktem Mehrwert für Dein Unternehmen."),
                  ("layers", "Tools im Vergleich", "Mehrere KI-Tools gleichzeitig – live erleben, wie unterschiedlich sie denken und welche Ergebnisse sie liefern."),
                  ("target", "Echte Usecases", "Anwendungsfälle, die für ein Versicherungsunternehmen wirklich relevant sind – mit direkt verwertbaren Erkenntnissen.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:7mm;')
        + '</div><div class="rand wachsen mitte" style="padding-top:8mm">' + kicker("Die Werkzeuge")
        + '<div class="logos" style="grid-template-columns:repeat(6,1fr);margin-top:8mm">' + "".join(
            f'<div><img src="assets/tools/{d}-magenta.png" alt="" style="height:10mm"><b>{t}</b></div>' for d, t in tools)
        + '</div></div>', nr, N)


def ki_b(nr):
    cols = [("½ Tag", "KI-Einstieg", "2.500 €", False), ("1 Tag", "KI-Sprint", "3.900 €", True), ("2 Tage", "KI-Deep-Dive", "7.350 €", False)]
    head = '<th></th>' + "".join(f'<th class="{"mitte" if m else ""}">{"<em>Meistgewählt</em><br>" if m else ""}<small>{d}</small><b>{n}</b></th>' for d, n, _, m in cols)

    def zeile(label, werte, cls=""):
        return f'<tr><td class="zeile">{label}</td>' + "".join(f'<td class="{"mitte " if cols[i][3] else ""}{cls}">{w}</td>' for i, w in enumerate(werte)) + '</tr>'
    ja, nein = '<span class="ja"></span>', '<span class="nein">–</span>'
    body = (zeile("Investition", [c[2] for c in cols], "preis")
            + zeile("Ziel", ["KI-Tools ausprobieren, erste Erfahrungen sammeln", "Tools kennenlernen, kompakte Fragestellung bearbeiten", "Direkter Einstieg in einen konkreten Usecase"])
            + zeile("Eigene Fragestellung", [nein, "kompakt", "konkreter Usecase"])
            + zeile("Abschluss&shy;besprechung", [nein, ja, ja]))
    faelle = [
        ("Sparring zu Zielgruppen", "Produktentwicklung und Marketing nutzen KI-Tools als Sparringspartner für Zielgruppenprofile im Versicherungsvertrieb – inklusive passender Ansprache. Bewusst auch mit ungewöhnlichen Zielgruppen, um die Grenzen der Tools auszuloten."),
        ("Generierung von Produktideen", "Der Auftrag kam vom Vorstand: Es fehlte an neuen Ideen. Ziel war nicht die Umsetzbarkeit, sondern eingefahrene Denkmuster aufzubrechen und die Diskussion im Team neu in Gang zu bringen."),
        ("Geschäftsmodell hinterfragen", "Vorstand und Strategieeinheit wollten wissen, wie sich das eigene Geschäftsmodell mit KI hinterfragen lässt: Prompts, die tragen, Recherche, Dokumentenanalyse und eigene Studien."),
    ]
    return seite(
        kopf(T) + '<div class="rand kap-kurz" style="padding-top:16mm">' + kicker("Formate")
        + '<h2>Drei Formate für jeden Anspruch.</h2>'
        + f'<table class="tabelle" style="margin-top:6mm"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen – inklusive Vorbereitung und Dokumentation der Ergebnisse.</p>'
        + '</div><div class="band band--hell wachsen" style="margin-top:9mm;padding-top:10mm">' + kicker("Beispiele")
        + '<div class="liste liste--kap" style="margin-top:6mm">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + details("KI zum Anfassen") + '</div>', nr, N)


# ---------- Kapitel 02 · Sprint Landingpage ----------
def sprint_a(nr):
    return seite(
        kopf(T)
        + kapitel_kopf("02", "Sprint Landingpage", '<span class="hl">Schnell live.</span> Klar im Fokus.<br>Volle Wirkung.',
                       "Wenn es schnell gehen muss: Im Sprint entwickeln wir Deine fokussierte Landingpage – ohne Abstriche bei Qualität, Layout und Wirkung.")
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:11mm;padding-bottom:12mm">' + kicker("Erfolgsfaktor")
        + punkte([("target", "Ein Fokus", "Eine Zielgruppe, ein Problem, eine Lösung – keine Ablenkung durch andere Themen."),
                  ("users", "Zugeschnitten", "Visualisierung, Ansprache und Argumente exakt auf diese Zielgruppe zugeschnitten."),
                  ("signpost", "Der nächste Schritt", "Nie der Anspruch, alles zu erklären – immer der Fokus auf den nächsten Schritt."),
                  ("flag", "Ein klares Ziel", "Kontaktdaten, Webinar-Anmeldung oder Download mit echtem Mehrwert.")], spalten=4).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:7mm;')
        + '</div><div class="rand weiss wachsen mitte" style="padding-top:4mm">' + kicker("Ablauf")
        + zeitstrahl([("01 · 2–3 STD. · ONLINE", "Onboarding", "Wir klären Zielgruppe, Problem und Ziel – damit der Sprint vom ersten Moment an sitzt."),
                      ("02 · 2 TAGE · PRÄSENZ", "Sprint-Workshop", "<b>Tag 1:</b> Sparring &amp; parallele Entwicklung der Rohversion. <b>Tag 2:</b> Vorstellung, Feedback, Feinschliff &amp; Go-live."),
                      ("03 · IM NACHGANG", "Review", "Kurzes Fazit: Hat alles gepasst, wie war das Feedback – und wo gibt es noch gezielten Anpassungsbedarf?")]).replace('<ol class="zs" style="', '<ol class="zs" style="margin-top:8mm;')
        + '</div>', nr, N)


def sprint_b(nr):
    liste = ["Konzeption, Text &amp; Design Deiner vollständigen Landingpage", "Umsetzung im zweitägigen Sprint-Workshop bei Dir vor&nbsp;Ort",
             "Feedbackrunde &amp; Feinschliff direkt im Workshop", "Live-Schaltung im Anschluss an den Sprint",
             "Review im Nachgang, damit alles wie gewünscht&nbsp;läuft", "Durchgeführt von 2 Beraterinnen und Beratern von empiria"]
    faelle = [
        ("Schnell auf eine Vertriebssituation reagieren", "Eine Marktchance oder eine Marktveränderung ist aufgekommen, oder es soll kurzfristig ein Push für den Vertrieb gesetzt werden – etwa im Endjahresgeschäft."),
        ("Eine Situation retten", "Etwas wurde vergessen oder jemand im Marketing ist ausgefallen – aber ein wichtiger Termin steht an: eine große Messe, ein Event, ein Vertriebsmeeting, ein Produktlaunch."),
        ("Kunden &amp; Partner begeistern", "Sehr schnell entsteht eine einsetzbare Lösung – etwa gegenüber großen Maklern, Bankpartnern oder Kooperationspartnern in einem neuen Ländermarkt."),
    ]
    return seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Investition")
        + '<h2>Ein Paket, ein Preis.</h2>'
        + '<p class="lead">Deine Landingpage in 48 Stunden live – Konzeption, Umsetzung und Live-Schaltung in einem Leistungspaket.</p>'
        + '<div class="paket paket--kap"><div class="paket__preis"><div><small>Dein Leistungspaket</small><h3>Sprint-Landingpage</h3></div>'
        + f'<div class="paket__unten"><b>15.850 €</b>{ico("rocket", strich=1.3)}</div></div>'
        + '<ul class="paket__liste">' + "".join(f"<li>{x}</li>" for x in liste) + '</ul></div>'
        + '<p class="notiz">Zzgl. Umsatzsteuer in gesetzlicher Höhe sowie zzgl. Spesen (Anfahrt und zwei Übernachtungen für je zwei Personen).</p>'
        + '</div><div class="band band--hell wachsen" style="margin-top:8mm;padding-top:9mm">' + kicker("Anwendungsfälle")
        + '<div class="liste liste--kap" style="margin-top:5mm">' + "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + details("Sprint Landingpage") + '</div>', nr, N)


# ---------- Kapitel 03 · Moderation deines Workshops ----------
def moderation_a(nr):
    return seite(
        kopf(T)
        + kapitel_kopf("03", "Moderation deines Workshops", 'Dein Workshop. Souverän moderiert.<br><span class="hl">Volle Wirkung.</span>',
                       "Wir aktivieren die Beteiligten gezielt, wechseln bewusst die Perspektive und stellen die richtigen Fragen, "
                       "um neue Blickwinkel auf die Themen zu bekommen.")
        + '<div class="band band--gelb wachsen" style="margin-top:10mm;padding-top:11mm">' + kicker("Moderation")
        + '<h2>Erfahrung aus<br>zahlreichen Workshops.</h2>'
        + punkte([("messages-square", "Gute Stimmung", "Eine Atmosphäre, in der offen gesprochen wird – die Voraussetzung für jedes gute Ergebnis."),
                  ("route", "Workshops, die funktionieren", "Klare Steuerung durch den Tag, damit Energie und Zeit dort ankommen, wo sie etwas bringen."),
                  ("layout-grid", "Klare Erkenntnisse &amp; Strukturen", "Wir ordnen Diskussionen, statt sie laufen zu lassen – am Ende steht Struktur."),
                  ("goal", "Ergebnisse, die tragen", "Ergebnisse, mit denen Dein Team direkt weiterarbeiten kann – nicht nur ein Protokoll."),
                  ("layers", "Hohe Methodenvielfalt", "Von Kreativformaten bis zur Entscheidungsrunde – die Methode, die zum Thema passt."),
                  ("presentation", "Top Visualisierungen", "Ergebnisse werden sichtbar festgehalten statt nur besprochen – und sauber zusammengefasst.")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:7mm;row-gap:7mm;')
        + '</div>', nr, N)

FOKUS = [("Ausgangslage", "In gewachsenen Strukturen verschieben sich Zuständigkeiten, laufend kommen neue Themen dazu – was fehlt, ist die systemische Müllabfuhr: Was kann wegfallen oder deutlich anders laufen?"),
         ("Der Ansatz", "Am Anfang stand nicht die Optimierung einzelner Schritte, sondern die Klärung, wofür die Abteilung steht und wo sie hinwill."),
         ("Das Ergebnis", "Prozesse und Strukturen, die im Alltag tragen – weil der Mehrwert verstanden ist und für alle Klarheit herrscht.")]


def moderation_b(nr):
    faelle = [
        ("Restrukturierung mit geteilter Führung", "Bei der Neustrukturierung eines mittelständischen Unternehmens wurden komplett neue Rollen eingeführt – bis hin zu einer geteilten Führungsrolle. Der Workshop hat Rollen, Prozesse und Zuständigkeiten so konkret gemacht, dass sie sich direkt in den Alltag übertragen ließen."),
        ("Klarheit nach zwei Strategieworkshops", "Eine Abteilung hatte zwei interne Strategieworkshops hinter sich – viele Themen, aber keinen klaren Weg nach vorn. Der Workshop hat Struktur gebracht: klare Schwerpunkte, klare Priorität, klares weiteres Vorgehen."),
        ("Neustart nach Führungswechsel", "Ein Führungswechsel ging mit einer Neustrukturierung der Abteilung einher. Erst wurde über mehrere Ebenen Vertrauen aufgebaut, dann ging es in die Inhalte – mit einer Abteilung, die schlagkräftiger startete als zuvor."),
    ]
    return seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
        + '<h2>Konkrete Usecases aus der Praxis.</h2>'
        + '<p class="lead">Ein Ausschnitt möglicher Workshopmoderationen – so vielfältig wie die Themen, die uns Teams mitbringen.</p>'
        + '<div class="liste liste--kap">' + "".join(f'<div style="padding:4.6mm 0"><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle) + '</div>'
        + '<div class="kasten kasten--fokus" style="margin-top:8mm;padding:5mm 8mm 2mm">'
        + '<div class="kopfzeile"><p class="label">Im Fokus</p><h3>Prozess- und Strukturworkshop im Team</h3></div>'
        + "".join(f'<div class="zeile"><p class="label">{l}</p><p>{x}</p></div>' for l, x in FOKUS)
        + '</div>'
        + details("Moderation deines Workshops") + '</div>', nr, N, klasse="seite--hell")


def bauen():
    s1 = seite(titelseite(
        "Workshops", 'Workshops, <span class="hl">die wirken.</span><br>Nicht nur Theorie.',
        "Ob Künstliche Intelligenz, eine neue Landingpage oder die Moderation Deines nächsten Workshops. "
        "Aus unseren Projekten sind Formate entstanden, die Du direkt buchen kannst.",
        kopfbild("Workshops"),
        [("Format 01", "KI zum Anfassen"), ("Format 02", "Sprint Landingpage"), ("Format 03", "Moderation deines Workshops")]))

    s10 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für einen Workshop,<br>der Dich <span class="hl">wirklich weiterbringt?</span></h2>'
        + '<p class="lead">Sag uns, worum es geht und wer dabei sein soll – wir schlagen Dir das passende Format vor.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag zum passenden Format."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte kontakt3" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + team(["daniel", "kerstin_hr", "noah_pm"]) + kontaktdaten() + '</div>', N, N)

    seiten = [s1, ueberblick_liste(2), ueberblick_tabelle(3),
              ki_a(4), ki_b(5), sprint_a(6), sprint_b(7), moderation_a(8), moderation_b(9), s10]
    return dokument(TITEL, seiten, extra_css=CSS)
