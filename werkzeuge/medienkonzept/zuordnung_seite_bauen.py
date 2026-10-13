#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Zuordnung – Arbeitsansicht.
Oben die Positionierung nach außen (Wortlaut der Homepage), darunter die Gesamtzuordnung als schlanker Entscheidungsbaum:
Kern → Strategiehandwerk (Dreiklang) → Themen → Lösungen. Erklärtexte per Hover/Antippen.

    python3 werkzeuge/medienkonzept/zuordnung_seite_bauen.py
"""
import html
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "28"

# Positionierung nach außen – Fragen im Wortlaut bzw. Geist der Homepage
SPITZEN = [
    ("1", "Warum kommt meine Strategie im Alltag nicht an?", "Rolle, Richtung, Handwerkszeug für den eigenen Bereich – und Führungskräfte, die die Strategie tragen."),
    ("2", "Wie bringe ich mein Thema durch?", "Vorstand, Aufsichtsrat, Lenkungsausschuss, Vertriebstagung: Das Ergebnis zählt, nicht die Präsentation."),
    ("3", "Wie hören wir auf, auf der Stelle zu treten?", "Entschiedenes ins Funktionieren bringen: nächster Schritt, Tempo, entscheidungsreif – auch bei KI und Regulierung im eigenen Bereich."),
]

# Baustein: (Nr, Titel, Erklärung, [(Thema, Spitze, Erklärung)], [(Lösung, URL)])
BAUSTEINE = [
    ("01", "Strategie in den Alltag überführen", "Was bedeutet die Strategie für deinen Bereich? Rolle, Richtung, Handwerkszeug.",
     [("Strategie, die im Alltag ankommt", "1", "Zielbild heißt: Jeder hat das Geschäftsmodell seines Bereichs verstanden. Die Strategie gibt der Chef vor. Operativ und strategisch trennen."),
      ("Führung, die trägt", "1", "Erst befördern, dann entwickeln ist falsch. Rolle und drei Säulen. Geduldetes Fehlverhalten demotiviert die Guten.")],
     [("Strategie in den Alltag überführen", "/leistungen/strategie"), ("1:1 Sparring", "/sparring"), ("Training & Sparring", "/training-sparring")]),
    ("02", "Komplexe Themen strukturieren und kommunizieren", "Überall, wo du Menschen von deinem Thema überzeugen musst.",
     [("Entscheidungen herbeiführen", "2", "Why – How – What next. Themen auf der falschen Flugebene. Diskussionen kippen, wenn die Bedeutung fehlt."),
      ("Vertrieb, der die Strategie umsetzt", "2", "Vertriebstagung: tolle Stimmung, nach vier Wochen spricht keiner mehr davon. What's in it for me.")],
     [("Komplexe Themen strukturieren & kommunizieren", "/leistungen/komplexe-themen"), ("Präsentationsseminar", "/praesentationsseminar"),
      ("Workshop-Moderation", "/workshop-moderation"), ("Medien", "/medien"), ("Marketing 2.0", "/marketing")]),
    ("03", "Innovation und Geschäftsmodell neu denken", "Bevor weitergebaut wird: Trägt die Idee? Für Unternehmen oder einzelne Bereiche.",
     [("Geschäftsmodell der Zukunft", "", "Die Neugründungs-Frage. Kooperationen, Fusionen, Zusatzservices. Erst den Kern im Griff."),
      ("KI aus eigener Praxis", "3", "Viele reden mit, ohne KI selbst zu nutzen. Was KI heute im eigenen Bereich bringt – statt Taskforce und Verbote.")],
     [("Innovation & Geschäftsmodell neu denken", "/leistungen/innovation"), ("KI zum Anfassen", "/ki-zum-anfassen"),
      ("Sprint Landingpage", "/sprint-landingpage"), ("MES", "/dashboard-digitales-marketing")]),
]
QUER = [("Branche und Regulierung eingeordnet", "3", "Was eine Branchennachricht oder AI Act, DORA, BaFin heute für deinen Bereich heißt. Quelle: Branchen-Radar."),
        ("Du als Person", "", "Analogien und Erlebnisse, die zu einem der Themen führen.")]


def tip(t):
    return html.escape(t, quote=True)


def chip(name, spitze, erkl):
    marke = '<i class="mzb-sp">%s</i>' % spitze if spitze else '<i class="mzb-sp mzb-sp--leer">B</i>'
    return '<span class="mzb-chip" tabindex="0" data-tip="%s">%s<span>%s</span></span>' % (tip(erkl), marke, name)


def spalte(nr, titel, erkl, themen, loesungen):
    ls = "".join('<a href="%s">%s</a>' % (u, n) for n, u in loesungen)
    return '''<div class="mzb-spalte">
  <span class="mzb-baustein" tabindex="0" data-tip="%s"><b>%s</b>%s</span>
  <div class="mzb-themen">%s</div>
  <div class="mzb-loes"><small>Lösungen</small>%s</div>
</div>''' % (tip(erkl), nr, titel, "".join(chip(*t) for t in themen), ls)


MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich mzb-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Zuordnung</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Zuordnung &middot; Arbeitsansicht</p>
      <h1>Positionierung und <span class="hl">Zuordnung.</span></h1>
  </div></section>

  <section class="e2-sek ak-sec mzb"><div class="e2-wrap">
    <h2 class="mzb-h">1 · Wie wir uns positionieren</h2>
    <div class="mzb-pos">
      <div><small>Kern</small><b>Die Strategie steht. Trotzdem passiert zu wenig.</b><span>Wir bringen sie in Wirkung – du gibst ein Thema ab, wir machen ein Ergebnis daraus.</span></div>
      <div><small>Für wen</small><b>Vorstand, Hauptabteilungs- und Abteilungsleiter</b><span>bei kleinen und mittleren Versicherern. Blick von heute aus: Was heißt das jetzt für deinen Bereich?</span></div>
      <div><small>Bewusst nicht</small><b>Die große Neuausrichtung</b><span>wie bei McKinsey, Roland Berger, BCG – und keine Zukunftsthemen ohne Umsetzung.</span></div>
    </div>
    <div class="mzb-spitzen">''' + "".join('<div class="mzb-spitze"><i class="mzb-sp">%s</i><div><b>%s</b><span>%s</span></div></div>' % s for s in SPITZEN) + '''</div>
    <p class="mzb-notiz">Rund 80 % der Postings zahlen auf diese drei Fragen ein. Baustein 3 und Vertrieb kommen vor, wenn es einen Anlass gibt.</p>

    <h2 class="mzb-h" style="margin-top:3.2rem">2 · Gesamtzuordnung</h2>
    <p class="mzb-notiz" style="margin-top:0">Innere Landkarte: Jedes Thema hat einen Platz im Strategiehandwerk und einen Weg zur Lösung. Ziffer = Frage, auf die es einzahlt · B = Begleiter. Erklärung per Hover oder Antippen.</p>
    <div class="mzb-kern">Strategie bei Versicherern in Wirkung bringen</div>
    <div class="mzb-baum">''' + "".join(spalte(*b) for b in BAUSTEINE) + '''</div>
    <div class="mzb-quer"><small>Quer über alle drei</small>''' + "".join(chip(*q) for q in QUER) + '''</div>
  </div></section>

</main>'''


def main():
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Zuordnung · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Positionierung und Zuordnung der Themen zum Strategiehandwerk und zu den Lösungen."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-zuordnung.html"), "w", encoding="utf-8").write(kopf + MAIN + fuss)
    print("Zuordnung gebaut")


if __name__ == "__main__":
    main()
