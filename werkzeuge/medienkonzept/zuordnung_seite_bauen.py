#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Zuordnung: Kern → Strategiehandwerk (Dreiklang) → Themen der Postings → Lösungen auf der Homepage.
Aufbau nach dem Vorbild der Storyboard-Zuordnung (methoden-storyboard.html).

    python3 werkzeuge/medienkonzept/zuordnung_seite_bauen.py
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "25"

# Baustein: (Nr, Titel, Satz aus Daniels Worten, [(Thema, Worum es geht, aus deinem Material)], [(Lösung, URL)])
BAUSTEINE = [
    ("01", "Strategie in den Alltag überführen",
     "Klarheit über das Geschäftsmodell des Bereichs: wie er heute und in Zukunft funktioniert, wie er erfolgreich ist und was jeder dazu beiträgt.",
     [("Strategie, die im Alltag ankommt", "Zielbild, Vision und Strategie so klar, dass jeder seinen Beitrag kennt.",
       "Zielbild heißt: Jeder hat das Geschäftsmodell verstanden · Die Strategie gibt der Chef vor · operativ und strategisch trennen"),
      ("Führung, die trägt", "Führungskräfte, die ihre Rolle von Anfang an ausfüllen und Strategie in ihren Bereich bringen.",
       "Erst befördern, dann entwickeln ist falsch · Rolle und drei Säulen · geduldetes Fehlverhalten demotiviert die Guten")],
     [("Strategie in den Alltag überführen", "/leistungen/strategie"), ("1:1 Sparring", "/sparring"), ("Training & Sparring", "/training-sparring")]),
    ("02", "Komplexe Themen strukturieren und kommunizieren",
     "Niemand ist allein auf der Welt: die Stakeholder-Map, wie man mit wem umgeht und wie man das eigene Thema in echten Mehrwert übersetzt.",
     [("Entscheidungen herbeiführen", "Vorstand, Aufsichtsrat und Stakeholder so ansprechen, dass entschieden wird.",
       "Why – How – What next · Themen auf der falschen Flugebene · Diskussionen kippen, wenn die Bedeutung fehlt"),
      ("Vertrieb, der die Strategie umsetzt", "Vertriebsstrategie, Markteinführungen und Tagungen, die im Alltag etwas bewegen.",
       "Nach der Vertriebstagung spricht nach vier Wochen keiner mehr davon · What's in it for me")],
     [("Komplexe Themen strukturieren & kommunizieren", "/leistungen/komplexe-themen"), ("Teams befähigen, professionell zu kommunizieren", "/praesentationsseminar"),
      ("Moderation deines Workshops", "/workshop-moderation"), ("Medien, die Ergebnisse liefern", "/medien"), ("Marketing 2.0", "/marketing")]),
    ("03", "Innovation und Geschäftsmodell neu denken",
     "Wenn Klarheit und Durchsetzung stehen: Wie würden wir den Bereich heute neu gründen, und was würden wir gar nicht mehr machen?",
     [("Geschäftsmodell der Zukunft", "Neu denken auf einem Kern, den man im Griff hat – nicht als Wunschliste.",
       "Die Neugründungs-Frage · Aufgabenzuschnitt, Platz in der Wertschöpfung, Zielgruppen · erst den Kern im Griff"),
      ("KI aus eigener Praxis", "Erfahrungswissen statt Meinung: wie KI hilft, schneller und besser zu entscheiden.",
       "Viele reden mit, ohne KI selbst zu nutzen · Taskforce und Verbote im Haus")],
     [("Innovation & Geschäftsmodell neu denken", "/leistungen/innovation"), ("KI zum Anfassen", "/ki-zum-anfassen"),
      ("Sprint Landingpage", "/sprint-landingpage"), ("MarketingEcoSystem (MES)", "/dashboard-digitales-marketing")]),
]


def thema(t, w, m):
    return '<div class="mzo-thema"><b>%s</b><p>%s</p><small>%s</small></div>' % (t, w, m)


def zeile(nr, titel, satz, themen, loesungen):
    ls = "".join('<li><a href="%s">%s</a></li>' % (u, n) for n, u in loesungen)
    return '''<div class="mzo-zeile">
  <div class="mzo-baustein"><span class="mzo-nr">%s</span><b>%s</b><p>%s</p></div>
  <span class="mzo-pfeil" aria-hidden="true">&rarr;</span>
  <div class="mzo-themen">%s</div>
  <span class="mzo-pfeil" aria-hidden="true">&rarr;</span>
  <div class="mzo-loesung"><small>Auf der Homepage</small><ul>%s</ul></div>
</div>''' % (nr, titel, satz, "".join(thema(*t) for t in themen), ls)


MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Zuordnung</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Zuordnung &middot; Vorschlag zur Entscheidung</p>
      <h1>Vom Kern zur <span class="hl">Lösung.</span></h1>
      <p class="e2-lead">Über allem steht Strategie bei Versicherern in Wirkung bringen. Darunter der Dreiklang des Strategiehandwerks, daraus die Themen der Postings – und jedes Thema führt zu einer Lösung auf der Homepage.</p>
  </div></section>

  <section class="e2-sek ak-sec mzo"><div class="e2-wrap">
    <div class="mzo-kern"><small>Über allem</small><b>Strategie bei Versicherern in Wirkung bringen.</b><span>Du gibst mir ein Thema – ich mache ein Ergebnis daraus.</span></div>
    <div class="mzo-kopf" aria-hidden="true"><span><i>1</i>Strategiehandwerk</span><span><i>2</i>Themen der Postings</span><span><i>3</i>Lösungen auf der Homepage</span></div>
    ''' + "\n".join(zeile(*b) for b in BAUSTEINE) + '''
    <div class="mzo-quer">
      <div><small>Quer über alle drei</small><b>Branche und Regulierung eingeordnet</b><p>Was die Branche bewegt und was AI Act, DORA oder BaFin-Vorgaben im Alltag bewirken – eingeordnet in den Baustein, den es betrifft. Quelle: Branchen-Radar, montags.</p></div>
      <div><small>Quer über alle drei</small><b>Du als Person</b><p>Analogien und Erlebnisse aus deinem Leben, die zu einem der Themen führen.</p></div>
    </div>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Was sich ändert</p><h2 class="e2-h2">Sieben Themen statt sechs.</h2>
    <p class="e2-lead">Die bisherigen sechs Themenfelder waren aus dem Interview gebündelt, nicht aus dem Dreiklang abgeleitet – Baustein 3 fehlte. Neu ist „Geschäftsmodell der Zukunft“; „Branche und Regulierung“ läuft jetzt quer über alle drei Bausteine. Ob die Themen tragen, zeigen Branchen-Radar und monatliche Auswertung.</p></div>
  </div></section>

</main>'''


def main():
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Zuordnung · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – vom Kern über das Strategiehandwerk zu den Themen der Postings und den Lösungen."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-zuordnung.html"), "w", encoding="utf-8").write(kopf + MAIN + fuss)
    print("Zuordnung gebaut")


if __name__ == "__main__":
    main()
