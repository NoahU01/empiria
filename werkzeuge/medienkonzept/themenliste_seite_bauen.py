#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Themenliste: konkrete Aussagen je Thema, mit Mehrwert, Herkunft und Vorschlag für Typ/Variante.
Herkunft: I = Interview 12./13.10. · P = Positionierung & Pitch / Homepage · F = Fundus (frühere Postings) · R = Recherche/Radar · Idee = Vorschlag von Claude, Daniel bestätigt.

    python3 werkzeuge/medienkonzept/themenliste_seite_bauen.py
"""
import html
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "42"

# (Gruppe, Unterzeile, [(Aussage, Mehrwert für den Leser, Herkunft, Typ · Variante, Foto?)])
LISTE = [
    ("01 · Strategie, die im Alltag ankommt", "Baustein 1 · Strategie in den Alltag überführen", [
        ("Zielbild heißt: Jeder hat das Geschäftsmodell seines Bereichs verstanden.", "Drei Prüffragen fürs eigene Zielbild: Wie funktionieren wir? Wie sind wir erfolgreich? Was ist mein Beitrag?", "I", "Werkzeug · B Checkliste", False),
        ("Gibt der Vorstand kein Zielbild vor, ist das deine Chance.", "Freiraum statt Warten: Der Bereichsleiter darf es so bauen, wie sein Bereich es braucht.", "I", "Szene · F Foto mit Verlauf und Wort", True),
        ("Die Strategie gibt der Chef vor – erst danach kommt das Team dazu.", "Die Reihenfolge und ihr Grund: Ein Zukunftsbild, das zu früh im Team diskutiert wird, erzeugt Angst um Jobs.", "I", "Szene · B Foto mit Satz", True),
        ("Der Einstieg in die Strategie dauert drei Stunden, keine zwei Tage.", "So läuft er: drei Gespräche ohne Vorbereitung, spiegeln, dann das Vorgehen entlang der Stakeholder.", "I", "Werkzeug · D Zeitleiste", False),
        ("Strategie ist die Verbindung zwischen heute und dem Zielbild.", "Wer beide Enden kennt, findet den Weg fast von allein – ohne Vision keine Strategie.", "I", "Modell · C Heute – Vision", False),
        ("Wie viel deiner Woche zahlt auf die Strategie ein?", "Ein ehrlicher Selbsttest: operative Brände und strategische Arbeit sauber trennen.", "I", "Frage · E Skala", False),
        ("Wie sähe die Homepage deiner Abteilung aus?", "Die Prüffrage für jede Vision: Zielgruppe, Problem, Nutzen, Unterschied, Zusammenarbeit.", "P", "Zum Mitnehmen · Dokument", False),
    ]),
    ("02 · Führung, die trägt", "Baustein 1 · klare Aussagen zu Rolle, Umsetzung und Wichtigkeit", [
        ("Erst befördern, dann 12 bis 24 Monate entwickeln – das ist der größte Fehler.", "Was vor dem ersten Tag geklärt sein muss: die Rolle und ihre drei Säulen.", "I", "Modell · D Drei Kreise", False),
        ("Neu in der Rolle – und überladen mit Regelterminen ohne Mehrwert.", "Die ersten 30 Tage: jeden Regeltermin auf seinen Beitrag zum Ziel prüfen.", "I", "Frage · D Ja oder nein", False),
        ("Geduldetes Fehlverhalten von Führungskräften demotiviert die Guten am meisten.", "Was Wegschauen kostet – und warum Führung auch Eingreifen heißt.", "I", "Szene · B Foto mit Satz", True),
        ("„Von dieser Person hätten wir mehr erwartet.“", "Wenn eine neue Führungskraft untergeht, fehlt meist das System – selten das Können.", "I", "Satz · D Zettel", False),
        ("Logik allein verändert wenig.", "Persönlichkeiten, Macht- und Interessenströmungen sind stärker als jedes Konzept – was das für die Umsetzung heißt.", "I", "Szene · A Foto pur", True),
        ("„Führung macht einsam. Je höher du kommst, desto weniger sagt dir jemand die Wahrheit.“", "Wer sagt dir die Wahrheit? Und was tust du, damit es jemand tut?", "F · I", "Szene · B Foto mit Satz (Porträt)", True),
    ]),
    ("03 · KI aus eigener Praxis", "Baustein 1 · was KI heute im Alltag eines Bereichs bringt", [
        ("Viele reden über KI, die sie nie selbst genutzt haben.", "Eine Mindestregel: Wer mitentscheidet, hat KI vorher selbst im Alltag ausprobiert.", "I · F", "Frage · B Schwarz", False),
        ("Taskforce, Verbote – und privat wird genutzt, was geschäftlich nicht erlaubt ist.", "Das Risiko dahinter und wie kontrollierte Freiräume aussehen können.", "I", "Eingeordnet · F Posting im Posting", False),
        ("Alle wollen KI-Schnellboote – die offiziell gar nicht fahren dürfen.", "Wie ein Bereich KI erproben kann, ohne an der Governance vorbeizulaufen.", "I", "Satz · A Satzkarte", False),
        ("Ich nutze KI, um schneller und besser zu entscheiden.", "Drei konkrete Anwendungen aus deinem Alltag – ohne dein System zu zeigen.", "I", "Szene · C Foto mit Uhrzeit", True),
    ]),
    ("04 · Entscheidungen herbeiführen", "Baustein 2 · Komplexe Themen strukturieren und kommunizieren", [
        ("Why – How – What next.", "Die Struktur für jede Vorstandsvorlage, Why als Ausgangssituation, Problem, Lösung.", "I · P", "Modell · A", False),
        ("Vorstandsvorlagen scheitern am Aufbau, nicht an der Länge.", "Die eine Prüffrage: Wie denkt ein Vorstand, um entscheiden zu können?", "I", "Werkzeug · E Was nicht hineingehört", False),
        ("„Bei uns kommen viel zu oft Themen auf der falschen Flugebene an.“", "Woran man die richtige Flughöhe erkennt – und was es kostet, wenn sie fehlt.", "I", "Satz · C Anführungszeichen", False),
        ("Diskussionen kippen, sobald die Bedeutung für das Unternehmen fehlt.", "Vor jedem Termin in einem Satz klären, was das Thema für das Haus bedeutet.", "I", "Szene · B Foto mit Satz", True),
        ("Aus vier Folien wurde eine. 22:25 Uhr: „Passt. Lass es so.“", "Wirkung entsteht, wenn der Entscheider sofort versteht – nicht durch mehr Fakten.", "F · I", "Satz · B Nachricht", False),
        ("Erst drei Fragen, dann die Folie.", "Wen brauche ich? Wen habe ich übersehen? An wem richte ich es aus?", "P", "Werkzeug · B Checkliste", False),
        ("„Kann mir einer kurz einordnen, mit welchem Ergebnis wir rausgehen?“", "Die ersten drei Minuten eines Termins entscheiden, ob er etwas bringt.", "I", "Werkzeug · D Zeitleiste", False),
        ("Wenn ihr es nicht einfach erklären könnt, habt ihr es nicht im Griff.", "Warum Entscheider bei Faktensammlungen misstrauisch werden – Erfahrung aus einem gewonnenen Pitch.", "I", "Szene · A Foto pur", True),
    ]),
    ("05 · Vertrieb, der die Strategie umsetzt", "Baustein 2 · Material noch dünn – nächste Interviewrunde", [
        ("Nach der Vertriebstagung: tolle Stimmung. Nach vier Wochen spricht keiner mehr davon.", "Was vorbereitet sein muss, damit die Impulse im Alltag ankommen.", "I", "Szene · D Foto mit Zeichen", True),
        ("What's in it for me – für jeden Vertriebspartner.", "Mehrwert in einem Satz erklären, bevor über das Produkt gesprochen wird.", "I", "Szene · A Foto pur (Flipchart „What's in for me“)", True),
        ("Ohne klare Unternehmensstrategie setzt jeder Regionalleiter eigene Schwerpunkte.", "Woran man eine echte Vertriebsstrategie erkennt.", "I", "Frage · A Fragekarte", False),
        ("Eine Idee fürs Neugeschäft dieses Jahr ist noch keine Vertriebsstrategie.", "Der Unterschied zwischen Maßnahme und Plan, erfolgreich zu sein.", "I", "Satz · A Satzkarte", False),
    ]),
    ("06 · Geschäftsmodell der Zukunft", "Baustein 3 · immer hinterfragen, ob es so organisiert sein muss wie heute", [
        ("Wie würdest du deinen Bereich heute neu gründen?", "Drei Unterfragen: Aufgabenzuschnitt, Platz in der Wertschöpfung, Zielgruppen.", "P · I", "Frage · C Fragezeichen", False),
        ("Die meisten sehen nur die Grenzen, die heute gesteckt sind.", "Was sich ändert, wenn man die Grenzen bewusst wegdenkt.", "I", "Szene · E Foto mit gelbem Balken", True),
        ("Wie würden wir eine Weiterbildungsakademie heute neu gründen?", "Ein Beispiel aus der Praxis, wie Neudenken konkret aussieht (anonymisiert).", "I", "Szene · A Foto pur", True),
        ("Erst den Kern im Griff, dann neu denken.", "Warum Innovation ohne stabile Basis eine Wunschliste bleibt.", "P", "Modell · C Heute – Vision", False),
    ]),
    ("07 · Branche und Regulierung eingeordnet", "Quer · Konsequenzen statt Detailauslegung · Zahlen vor Verwendung neu prüfen", [
        ("AI Act: ab 02.12.2027 Hochrisiko-Pflichten, auch für KI in der Tarifierung.", "Was das für einen Bereich heißt – und wer heute dafür zuständig sein sollte.", "R", "Eingeordnet · E Datum", False),
        ("77 % sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.", "Was ein Bereich tun kann, damit Strategie Termine im Kalender bekommt.", "R", "Eingeordnet · B Zahl auf Foto", True),
        ("Versicherer planen kein Personalwachstum – die Effizienz soll mit KI kommen.", "Welche Fragen sich ein Bereichsleiter jetzt stellen sollte.", "R", "Eingeordnet · F Posting im Posting", False),
        ("DORA im Alltag: was es für Prozesse und Verantwortung bedeutet.", "Konsequenzen und wie man es positiv nutzt – Inhalt kommt aus dem Branchen-Radar.", "R", "Eingeordnet · C Riesige Zahl", False),
    ]),
    ("08 · Du als Person", "Quer · Analogien aus deinem Leben – bitte bestätigen, ob sie zu dir passen", [
        ("Meine Tochter hat Spaß an Buchhaltung.", "Was Begeisterung mit Verstehen zu tun hat – auch im Team.", "I · Idee", "Szene · Du als Person", True),
        ("Beim Lego kommt zuerst das Bild auf der Packung.", "Ohne Zielbild baut jeder etwas anderes.", "I · Idee", "Szene · Du als Person", True),
        ("Auf dem Mountainbike wählst du die Linie, bevor es steil wird.", "Entscheidungen vorbereiten, bevor der Druck kommt.", "I · Idee", "Szene · Du als Person", True),
    ]),
]


def zeile(nr, aussage, mehrwert, herkunft, format_, foto):
    return '<tr><td class="tl-nr">%02d</td><td><b>%s</b><span>%s</span></td><td><em>%s</em></td><td>%s%s</td></tr>' % (
        nr, html.escape(aussage), html.escape(mehrwert), herkunft, format_, ' <i class="tl-foto">Foto</i>' if foto else "")


def main():
    n = 0
    gruppen = []
    for titel, unter, eintraege in LISTE:
        zeilen = []
        for e in eintraege:
            n += 1
            zeilen.append(zeile(n, *e))
        gruppen.append('<div class="tl-gruppe"><h3>%s</h3><p class="tl-unter">%s</p><div class="mkf-tabelle tl-tab"><table><tr><th>Nr</th><th>Aussage · Mehrwert für den Leser</th><th>Herkunft</th><th>Vorschlag</th></tr>%s</table></div></div>' % (titel, unter, "".join(zeilen)))
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich mzb-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Themenliste</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Themenliste &middot; zur Freigabe</p>
      <h1>Worüber du <span class="hl">sprichst.</span></h1>
      <p class="e2-lead">%d Aussagen aus deinem Interview, deiner Positionierung und der Recherche – je mit Mehrwert für den Leser und einem Vorschlag für Typ und Variante. 16 davon mit Foto von dir – passend zu zwei Foto-Postings pro Woche. Bitte je Nummer: <b>stimmt</b>, <b>schärfen</b> oder <b>raus</b>.</p>
      <p class="tl-legende">Herkunft: <b>I</b> Interview 12./13.10. · <b>P</b> Positionierung &amp; Homepage · <b>F</b> Fundus früherer Postings · <b>R</b> Recherche / Branchen-Radar · <b>Idee</b> Vorschlag von mir, bitte bestätigen</p>
  </div></section>

  <section class="e2-sek ak-sec tl"><div class="e2-wrap">
    %s
  </div></section>

</main>''' % (n, "".join(gruppen))
    quelle = open(os.path.join(HIER, "seiten-vorlage.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Themenliste · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Themenliste für Daniels persönliches Profil zur Freigabe."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-themenliste.html"), "w", encoding="utf-8").write(kopf + main_html + fuss)
    print("Themenliste gebaut:", n, "Aussagen")


if __name__ == "__main__":
    main()
