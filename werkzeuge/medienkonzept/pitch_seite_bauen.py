#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Pitch: Daniels Business Story als 30- und 10-Sekunden-Pitch (Daniel, 16.10.2026).
Aufbau wie der Elevator Pitch von Müller & Ströbel: Logik → Pitch → Regeln → Fragen danach. Arbeitsstand zum Weiterentwickeln.
Grundlage: Positionierung & Pitch (11.10.2026) und Daniels Erklärung des Dreiklangs (16.10.2026).

    python3 werkzeuge/medienkonzept/pitch_seite_bauen.py
"""
import os, re

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "63"

# Der Dreiklang – jeder Schritt baut auf dem vorigen auf
SCHRITTE = [
    ("1", "Strategie in den Alltag überführen", "Klarheit",
     [("Vision", "Wie würdest du deinen Bereich heute neu gründen? Daraus entsteht das Bild vom Geschäftsmodell der Zukunft."),
      ("Strategie", "Der Weg von heute dorthin. Ist das Bild klar, ergibt er sich fast von allein.")],
     "„Ich weiß, wo wir hinwollen, kann es einfach erklären – und jeder kennt seinen Beitrag.“"),
    ("2", "Komplexe Themen strukturieren und kommunizieren", "Wirkung",
     [("Stakeholder", "Niemand ist allein: Vorstand, Aufsichtsrat, Vertrieb, Nachbarbereiche haben eigene Ziele."),
      ("Erfolgsmap", "An wem richte ich mich aus? Wen brauche ich? Wen habe ich übersehen? Daraus folgt die Taktik.")],
     "„Ich bringe mein Vorhaben nach vorn – mit den richtigen Leuten, in der richtigen Reihenfolge.“"),
    ("3", "Geschäftsmodell und Innovation neu denken", "Raum für Neues",
     [("Fundament", "Der Bereich läuft, die Stellhebel sind klar. Erst jetzt ist der Kopf frei."),
      ("Über den Tellerrand", "Innovativ über das Geschäftsmodell nachdenken – für das Unternehmen oder den eigenen Bereich.")],
     "„Ich habe den Status quo im Griff – und gestalte, was kommt.“"),
]

PITCH_30 = [
    "Jeder Versicherer hat eine Strategie. Die Frage ist, wie viel davon im Alltag ankommt.",
    "Da setze ich als Strategiehandwerker an: Sie geben mir ein Thema, ich mache daraus ein Ergebnis.",
    "Erst Klarheit: Wie würden Sie Ihren Bereich heute neu gründen? Daraus folgt die Strategie – und jeder kennt seinen Beitrag.",
    "Dann Wirkung: Wen brauchen Sie, und wen haben Sie bisher übersehen? So kommt Ihr Thema voran.",
    "Und wenn das läuft, ist der Kopf frei für das Geschäftsmodell von morgen.",
    "Was liegt bei Ihnen gerade auf dem Tisch, das nicht so vorankommt?",
]
PITCH_10 = "Ich bin Strategiehandwerker für Führungskräfte bei Versicherern. Ich sorge dafür, dass ihre Strategie im Alltag ankommt: erst Klarheit, dann Wirkung, dann Raum für Neues."
KURZ = "Aus der Strategie auf der Folie wird ein Bereich, der funktioniert."

REGELN = [
    ("Bei ihm anfangen", "Mit dem Problem, das er selbst sieht: Die Strategie steht, aber sie kommt nicht an."),
    ("Ein Gedanke je Satz", "Jeder Schritt ein Satz – der Dreiklang trägt die Reihenfolge."),
    ("Seine Worte", "Bereich, Vorstand, Vertrieb – kein Beraterdeutsch, keine Methodennamen."),
    ("Mit einer Frage enden", "Danach redet er. Wer zuhört, erfährt, welcher Schritt gerade dran ist."),
]

FRAGEN = [
    ("„Was liegt bei Ihnen gerade auf dem Tisch, das nicht so vorankommt?“", "Zeigt das konkrete Thema."),
    ("„Wie würden Sie Ihren Bereich heute neu gründen?“", "Zeigt, ob ein Zielbild da ist – Schritt 1."),
    ("„Wen bräuchten Sie, damit es schneller vorangeht?“", "Zeigt die Stakeholder – Schritt 2."),
    ("„Was würden Sie anders machen, wenn das Tagesgeschäft Sie nicht bremsen würde?“", "Zeigt den Raum für Neues – Schritt 3."),
]


def woerter(t):
    return len(re.findall(r"\w+", t))


def schritte():
    h = []
    for nr, titel, wort, punkte, danach in SCHRITTE:
        h.append('<article class="mpp-schritt"><p class="mpp-schritt__nr"><b>%s</b><span>%s</span></p><h3>%s</h3><dl>%s</dl><p class="mpp-danach"><small>Danach</small>%s</p></article>'
                 % (nr, wort, titel, "".join("<dt>%s</dt><dd>%s</dd>" % p for p in punkte), danach))
    return '<div class="mpp-schritte">%s</div>' % '<span class="mpp-pfeil" aria-hidden="true">→</span>'.join(h)


def main():
    w30 = sum(woerter(s) for s in PITCH_30)
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><a href="/projekte/medienkonzept-zuordnung.html">Logik</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Pitch</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Business Story &middot; Arbeitsstand</p>
      <h1>Strategiehandwerk in <span class="hl">30 Sekunden.</span></h1>
      <p class="e2-lead">Die Story hinter allem, was wir posten und auf der Homepage zeigen – verdichtet auf das, was Daniel einem Vorstand in der Kaffeepause sagt. Erst die Logik, dann der Pitch.</p>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Die Logik</p><h2 class="e2-h2">Drei Schritte, die aufeinander aufbauen.</h2>
    <p class="e2-lead">Jeder Schritt räumt etwas auf. Erst wenn er sitzt, trägt der nächste.</p></div>
    <p class="mpp-ueber"><small>Über allem</small><b>Du gibst mir ein Thema. Ich sorge dafür, dass daraus ein Ergebnis wird.</b></p>
    ''' + schritte() + '''
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Der Pitch</p><h2 class="e2-h2">Gesprochen, nicht gelesen.</h2>
    <p class="e2-lead">Per Sie für das erste Gespräch – unter Bekannten einfach per Du.</p></div>
    <div class="mpp-pitch">
      <article class="mpp-karte mpp-karte--lang"><p class="mpp-karte__kopf"><b>30 Sekunden</b><span>''' + str(w30) + ''' Wörter · gesprochen etwa ''' + str(round(w30 / 2.4 / 5) * 5) + ''' Sekunden</span></p>
        ''' + "".join("<p>%s</p>" % s for s in PITCH_30) + '''</article>
      <article class="mpp-karte mpp-karte--kurz"><p class="mpp-karte__kopf"><b>10 Sekunden</b><span>Für die Vorstellungsrunde oder „Und was machen Sie?“</span></p>
        <p class="mpp-zehn">''' + PITCH_10 + '''</p>
        <p class="mpp-kurz"><small>Kurz gesagt</small>''' + KURZ + '''</p></article>
    </div>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">So bleibt es einfach</p><h2 class="e2-h2">Vier Regeln für jede Fassung.</h2></div>
    <ul class="mpp-regeln">''' + "".join("<li><b>%s</b><span>%s</span></li>" % r for r in REGELN) + '''</ul>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Nach dem Pitch</p><h2 class="e2-h2">Eine Frage genügt.</h2>
    <p class="e2-lead">Die Antwort zeigt, welcher der drei Schritte gerade dran ist.</p></div>
    <ul class="mpp-fragen">''' + "".join("<li><b>%s</b><span>%s</span></li>" % f for f in FRAGEN) + '''</ul>
    <p class="mpp-quelle">Grundlage: Positionierung &amp; Pitch (11.10.2026) und Daniels Erklärung des Dreiklangs (16.10.2026). Aufbau wie der Elevator Pitch von Müller &amp; Ströbel.</p>
  </div></section>

</main>'''
    quelle = open(os.path.join(HIER, "seiten-vorlage.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Pitch · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Daniels Business Story als 30- und 10-Sekunden-Pitch."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-pitch.html"), "w", encoding="utf-8").write(kopf + main_html + fuss)
    print("Pitch-Seite gebaut ·", w30, "Wörter (30 s) ·", len(PITCH_10.split()), "Wörter (10 s)")


if __name__ == "__main__":
    main()
