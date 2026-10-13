#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Logik (Datei medienkonzept-zuordnung.html) als Flussdiagramm:
Drei Töpfe (empiria · Daniel · Analysen) → Positionierung nach außen → Themen für Daniel je Baustein (mit Lösungen) → Postings.
Jeder Punkt trägt seine Herkunft (T1/T2/T3). Erklärungen per Hover/Antippen. Arbeitsansicht: kompakt, Fakten.

    python3 werkzeuge/medienkonzept/zuordnung_seite_bauen.py
"""
import html
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
PF = "/assets/projekte/medienkonzept/postings/"
V = "30"

TOEPFE = [
    ("T1", "empiria", "Was wir lösen – Homepage und Pitch", "Die Strategie steht. Trotzdem passiert zu wenig – wir bringen sie in Wirkung.", [
        ("Zielgruppe", "Führungskräfte bei kleinen und mittleren Versicherern: Vorstand, Hauptabteilungs-, Abteilungsleiter."),
        ("Problem", "Die Strategie steht. Trotzdem passiert zu wenig. Strategisches Denken wird vorausgesetzt, beigebracht hat es keiner."),
        ("Lösung", "Über allem die Umsetzungspower: Du gibst ein Thema ab, wir machen ein Ergebnis daraus. Darunter der Dreiklang des Strategiehandwerks."),
        ("Mehrwert", "Handlungsklarheit · Handlungssicherheit · fundiertes Neudenken. Aus dem Problemverwalter wird jemand, der steuert."),
    ], "Grundlagen: Positionierung & Pitch (11.10.), Homepage"),
    ("T2", "Daniel Ströbel", "Wer dahintersteht – Briefing, LinkedIn, Interview", "28 Jahre Versicherung. Man muss ihn nicht briefen – er macht aus einem Thema ein Ergebnis.", [
        ("Glaubwürdig", "28 Jahre Versicherung seit der Ausbildung, zwei Abteilungen geführt, Vorstandsklausuren, über 300 Projekte."),
        ("Arbeitsweise", "Man muss ihn nicht briefen. Fragen, Skizze auf dem iPad, das What next – und der Umsetzungsturbo zwischen den Terminen."),
        ("Positionen", "Elf klare Positionen, z. B.: Die Strategie gibt der Chef vor. Vorlagen scheitern am Aufbau. Erst befördern, dann entwickeln ist falsch."),
        ("Mensch", "Offen, klar, Humor, kein Fachbegriffe-Bingo, kein Prediger. Lego, Mountainbike, die Fragen der Kinder."),
    ], "Grundlagen: Personal-Brand-Profil, Interview 12./13.10."),
    ("T3", "Analysen", "Was ankommt – Zielgruppe und LinkedIn", "Gelesen wird, worin man sich wiedererkennt und was etwas mitgibt – mit Bild, im eigenen Fachgebiet.", [
        ("Zielgruppe", "Liest, wenn sie sich wiedererkennt und ein Problem sieht, das sie noch nicht gesehen hat (91 %, Edelman). Alltag: Regeltermine, Vorlagen, verpuffte Tagungen, KI-Verbote."),
        ("Themen", "Fachgebiet beständig halten – LinkedIn belohnt Expertise in einem Gebiet. Branchenthemen nur übersetzt: Was heißt das heute für deinen Bereich?"),
        ("Form", "Dokument 7,0 %, Bild 5,3 %, nur Text 2,0 %. Persönliche Fotos bis +50 %. 700–900 Zeichen. KI-Texte −45 %."),
        ("Deine Zahlen", "Szene und wörtlicher Satz schlagen These: +70 % Reaktionen, Satz plus Führungsthema mit der höchsten Reichweite."),
    ], "Grundlagen: Was auf LinkedIn nachweislich wirkt, Was Daniels Postings bisher zeigen"),
]

POSITIONIERUNG = ("Strategiehandwerker für Führungskräfte bei Versicherern.",
                  "Die Strategie steht – trotzdem passiert zu wenig. Daniel bringt sie in Wirkung: Du gibst ein Thema ab, er macht ein Ergebnis daraus.")
POS_REGELN = [
    ("Wofür", "Den Dreiklang des Strategiehandwerks – Klarheit, Durchsetzung, Neudenken.", "T1"),
    ("Für wen", "Vorstand, Hauptabteilungs- und Abteilungsleiter bei kleinen und mittleren Versicherern. Blick von heute aus.", "T1 · T3"),
    ("Woran man ihn erkennt", "Szenen und Sätze aus 28 Jahren Versicherung, Skizze statt Folie, das What next.", "T2 · T3"),
    ("Bewusst nicht", "Große Neuausrichtung, Zukunftsthemen ohne Umsetzung, Belehrung von oben.", "T1 · T2"),
]

# (Nr, Baustein, Problem, Ergebnis, Gewicht, [(Thema, [(Postingidee, Herkunft)])], [(Lösung, URL)])
BAUSTEINE = [
    ("01", "Strategie in den Alltag überführen", "Was bedeutet die Strategie für meinen Bereich?", "Handlungsklarheit", "ca. 40 %",
     [("Strategie, die im Alltag ankommt", [("Zielbild heißt: Jeder hat das Geschäftsmodell verstanden", "T2"), ("Die Strategie gibt der Chef vor – nicht das ganze Team", "T2"), ("Wie sähe die Homepage deiner Abteilung aus?", "T1")]),
      ("Führung, die trägt", [("Erst befördern, dann entwickeln ist falsch", "T2"), ("Neu in der Rolle – und überladen mit Regelterminen", "T3"), ("Führung macht einsam", "T2 · T3")])],
     [("Strategie", "/leistungen/strategie"), ("1:1 Sparring", "/sparring"), ("Training & Sparring", "/training-sparring")]),
    ("02", "Komplexe Themen strukturieren und kommunizieren", "Wie bringe ich mein Thema bei den Menschen durch, die ich brauche?", "Handlungssicherheit", "ca. 40 %",
     [("Entscheidungen herbeiführen", [("Why – How – What next", "T1 · T2"), ("Themen auf der falschen Flugebene", "T2"), ("Aus vier Folien wird eine", "T2 · T3")]),
      ("Vertrieb, der die Strategie umsetzt", [("Nach der Vertriebstagung spricht keiner mehr davon", "T2"), ("What's in it for me – für den Vertrieb", "T1 · T2")])],
     [("Komplexe Themen", "/leistungen/komplexe-themen"), ("Präsentationsseminar", "/praesentationsseminar"), ("Workshop-Moderation", "/workshop-moderation"), ("Medien", "/medien"), ("Marketing 2.0", "/marketing")]),
    ("03", "Innovation und Geschäftsmodell neu denken", "Trägt die Idee – bevor wir weiterbauen?", "Fundiertes Neudenken", "ca. 20 %",
     [("Geschäftsmodell der Zukunft", [("Wie würdest du deinen Bereich heute neu gründen?", "T1 · T2"), ("Erst den Kern im Griff, dann neu denken", "T1")]),
      ("KI aus eigener Praxis", [("Taskforce, Verbote – und privat wird genutzt", "T2 · T3"), ("Was KI heute im eigenen Bereich bringt", "T2")])],
     [("Innovation", "/leistungen/innovation"), ("KI zum Anfassen", "/ki-zum-anfassen"), ("Sprint Landingpage", "/sprint-landingpage"), ("MES", "/dashboard-digitales-marketing")]),
]

TYPEN = [("Die Szene", "v1.jpg", "Foto"), ("Der Satz", "t1.jpg", "Karte"), ("Die Frage", "k1.jpg", "Karte"), ("Das Modell", "m1.jpg", "Grafik"),
         ("Das Werkzeug", "p5.jpg", "Karte"), ("Eingeordnet", "z1.jpg", "Karte"), ("Zum Mitnehmen", "d1.jpg", "Dokument")]


def e(t):
    return html.escape(t, quote=True)


def topf(tag, titel, unter, kernsatz, punkte, quelle):
    li = "".join('<li tabindex="0" data-tip="%s"><b>%s</b></li>' % (e(t), k) for k, t in punkte)
    return '<div class="lg-topf"><span class="lg-tag">%s</span><b class="lg-topf__t">%s</b><small>%s</small><p class="lg-kern">%s</p><ul>%s</ul><em>%s</em></div>' % (tag, titel, unter, kernsatz, li, quelle)


def baustein(nr, titel, problem, ergebnis, gewicht, themen, loesungen):
    th = ""
    for name, ideen in themen:
        idl = "".join('<li>%s <i>%s</i></li>' % (i, h) for i, h in ideen)
        th += '<div class="lg-thema"><b>%s</b><ul>%s</ul></div>' % (name, idl)
    ls = " · ".join('<a href="%s">%s</a>' % (u, n) for n, u in loesungen)
    return '''<div class="lg-spalte">
  <div class="lg-baustein"><span class="lg-nr">%s</span><b>%s</b><span class="lg-gew">%s</span></div>
  <p class="lg-pe"><span>Problem:</span> %s <span>Ergebnis:</span> %s</p>
  %s
  <p class="lg-loes"><span>Lösung:</span> %s</p>
</div>''' % (nr, titel, gewicht, problem, ergebnis, th, ls)


PFEIL = '<div class="lg-pfeil" aria-hidden="true"><span></span></div>'

MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich mzb-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Logik</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Logik &middot; Arbeitsansicht</p>
      <h1>Von den Grundlagen zum <span class="hl">Posting.</span></h1>
  </div></section>

  <section class="e2-sek ak-sec lg"><div class="e2-wrap">
    <p class="lg-stufe"><i>A</i>Drei Töpfe – worauf alles aufbaut <span>Punkte per Hover oder Antippen</span></p>
    <div class="lg-toepfe">''' + "".join(topf(*t) for t in TOEPFE) + '''</div>
    ''' + PFEIL + '''
    <p class="lg-stufe"><i>B</i>Positionierung nach außen – Daniel Ströbel</p>
    <div class="lg-pos">
      <div class="lg-pos__kern"><b>''' + POSITIONIERUNG[0] + '''</b><span>''' + POSITIONIERUNG[1] + '''</span></div>
      <div class="lg-pos__regeln">''' + "".join('<div><small>%s</small><span>%s</span><i>%s</i></div>' % r for r in POS_REGELN) + '''</div>
    </div>
    ''' + PFEIL + '''
    <p class="lg-stufe"><i>C</i>Themen für Daniel – je Baustein, mit Postingideen und Lösung</p>
    <div class="lg-baum">''' + "".join(baustein(*b) for b in BAUSTEINE) + '''</div>
    <p class="lg-quer"><b>Quer:</b> Branche und Regulierung eingeordnet <i>T3</i> – immer übersetzt in einen der drei Bausteine · Du als Person <i>T2</i> – Analogien, die zu einem Thema führen.</p>
    ''' + PFEIL + '''
    <p class="lg-stufe"><i>D</i>Postings – wie sie aussehen</p>
    <div class="lg-postings">
      <div class="lg-typen">''' + "".join('<figure><img src="%s%s" alt="" loading="lazy"><figcaption>%s<span>%s</span></figcaption></figure>' % (PF, b, n, a) for n, b, a in TYPEN) + '''</div>
      <ul class="lg-regeln">
        <li>Erst die Szene oder der Satz, dann die Aussage, dann der Mehrwert <i>T2 · T3</i></li>
        <li>Daniels Stimme aus dem Diktat, 700–900 Zeichen, kein Link <i>T2 · T3</i></li>
        <li>Nie Text ohne Bild – Foto, Karte, Grafik oder Dokument im Wechsel <i>T3</i></li>
        <li>Fünf pro Woche, ein Foto von Daniel <i>T2 · T3</i></li>
      </ul>
      <p class="lg-weiter"><a href="/projekte/medienkonzept-postingformate.html">Postingformate im Detail &rarr;</a> · <a href="/projekte/medienkonzept-entwuerfe.html">Entwürfe &rarr;</a></p>
    </div>
  </div></section>

</main>'''


def main():
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Logik · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – von den drei Grundlagen-Töpfen über die Positionierung zu Themen und Postings."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-zuordnung.html"), "w", encoding="utf-8").write(kopf + MAIN + fuss)
    print("Logik gebaut")


if __name__ == "__main__":
    main()
