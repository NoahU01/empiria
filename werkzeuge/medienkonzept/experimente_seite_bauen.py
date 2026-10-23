#!/usr/bin/env python3
"""Baut Medienkonzept › Persönliches Profil › Experimentierfeld (Daniel, 23.10.2026).
Hier wird Daniels Sprech weiterentwickelt: klarer, aufrüttelnder, Bilder außerhalb des Rasters.
Bewusst übertrieben – danach wird gestrichen. Nichts davon ist eingeplant; bestehende Entwürfe bleiben unberührt.

    python3 werkzeuge/medienkonzept/experimente_seite_bauen.py
"""
import os, html

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "69"
PF = "/assets/projekte/medienkonzept/postings/"

MASSSTAB = [
    ("Klare Meinung", "So, wie Daniel im Gespräch spricht: Er sagt, was Sache ist. Ohne Polster, ohne „vielleicht“."),
    ("Man merkt, wie es ist, mit ihm zu arbeiten", "Tempo, Klarheit, ein Augenzwinkern. Wer liest, soll denken: Mit dem will ich arbeiten."),
    ("Echt statt Schablone", "Kein Verlauf mit gelbem Balken als Standard, kein Lehrsatz am Ende. Fotos dürfen für sich stehen."),
]

EXPERIMENTE = [
    dict(nr="1", titel="Klartext", bild="ex1",
         bild_anders="Foto pur. Kein Satz, kein Verlauf, kein gelber Balken – das Gesicht trägt allein.",
         text_anders="Eine Meinung ohne Aufzählung und ohne Ratschlag-Liste. Der letzte Satz sitzt, danach ist Schluss.",
         streichen="„Weißt du, wen das am härtesten trifft?“ ist eine rhetorische Frage – vielleicht zu viel. Der Schlusssatz ist hart; prüfen, ob er für Vorstände trägt.",
         quelle="Rohantworten 12.10.: Führungskräfte über ihre Organisation, ohne Vorstand im Raum",
         text="""Jeder im Haus weiß es. Seit Jahren.

Die eine Führungskraft, bei der Themen versanden. Die Schnittstelle, die nie funktioniert. Der Bereichsleiter, der ein zentrales Problem einfach nicht gelöst kriegt.

Und keiner greift ein.

Weißt du, wen das am härtesten trifft? Die Guten. Die Motivierten. Die, die sich jeden Tag ins Zeug legen und zusehen, wie nebenan Fehlverhalten einfach durchgeht.

Wenn ich mit Führungskräften spreche und kein Vorstand im Raum ist, kommt genau das auf den Tisch. Mit spürbarem Ärger.

Führung heißt auch eingreifen. Auch wenn es unbequem ist. Auch bei jemandem auf deiner eigenen Ebene.

Wer wegschaut, hat sich trotzdem entschieden. Gegen die Guten."""),
    dict(nr="2", titel="Geständnis", bild="ex2",
         bild_anders="Eine gezeichnete Szene statt Foto oder Satzkarte: die typische Folie, durchgestrichen, ab ins Backup.",
         text_anders="Daniel verrät eine Eigenheit seiner Arbeitsweise – mit Augenzwinkern. Der Leser erfährt nebenbei, wie es ist, mit ihm zu arbeiten.",
         streichen="„Alle.“ als eigener Absatz ist Kunstpause – eventuell zurücknehmen. Prüfen, ob „Lieblingsfolie“ zu flapsig für Vorstände ist.",
         quelle="Rohantworten 14.10.: Welche Folie streichst du am häufigsten?",
         text="""Wenn ich in ein Projekt komme und es gibt schon Folien, mache ich als Erstes immer dasselbe.

Ich schiebe sie ins Backup. Alle.

Das hat nichts mit fehlendem Respekt vor der Arbeit zu tun, die darin steckt. Die meisten Folien erzählen das eigene Thema, mit allen Details, die dazugehören. Aus Sicht dessen, der präsentiert. Was der Entscheider davon hat, steht selten darin.

Ich selbst nutze für mich übrigens gar keine PowerPoint. Obwohl ich für Kunden sehr viele baue. Ich arbeite mit Gesamtbildern, meistens von Hand gezeichnet, oder mit einem One-Pager.

Wer mit mir arbeitet, muss also eines aushalten: Seine Lieblingsfolie ist erst einmal weg.

Dafür steht am Ende die Entscheidung."""),
    dict(nr="3", titel="Dialog", bild="ex3",
         bild_anders="Reine Typografie mit einer Durchstreichung: Die Pointe steht im Bild, der Text liefert die Szene.",
         text_anders="Nur Dialog und Ergebnis, ohne Einleitung „hat mir ein Vorstand gesagt“. Endet mit einer klaren Ansage zum Handwerk.",
         streichen="Der letzte Absatz erklärt, was die Geschichte schon zeigt – eventuell weglassen. Termin frühestens Mitte Dezember (Abstand zum sofort-sichtbar-Posting).",
         quelle="Rohantworten 13.10.: Landingpage in drei Wochen",
         text="""Kleine Runde, bei uns im Büro. Wir hatten das wichtigste Thema eines Vorstands gerade einmal sauber durchstrukturiert: Business Story, Zielgruppen, Aufbau des Pitches.

Ich: „Daraus müssen wir sofort eine Landingpage machen.“

Er: „Wenn ich damit zum Marketing gehe, kann ich froh sein, wenn ich die nächstes Jahr habe.“

Ich: „So weit, wie wir jetzt sind, brauche ich nicht einmal mehr Input von dir. Gib mir das Go, und sie ist in drei Wochen live.“

Er hat das Go gegeben.

Drei Wochen später war sie live.

Wenn ein Thema einmal sauber steht, ist der Rest Handwerk. Und Handwerk muss man nicht durch jede Abstimmungsrunde schicken."""),
]


def absaetze(t):
    return "".join("<p>%s</p>" % html.escape(a).replace("\n", "<br>") for a in t.split("\n\n"))


def experiment(e):
    return '''<article class="mex-karte">
  <figure class="mex-bild"><img src="%s%s.jpg?v=%s" alt="" loading="lazy"></figure>
  <div class="mex-text"><p class="mex-nr"><b>%s</b><span>%s</span></p>
    <div class="mex-posting">%s</div>
    <dl class="mex-was"><div><dt>Bild – was anders ist</dt><dd>%s</dd></div><div><dt>Text – was anders ist</dt><dd>%s</dd></div><div class="mex-streichen"><dt>Was wir vermutlich wieder streichen</dt><dd>%s</dd></div></dl>
    <p class="mex-quelle">Grundlage: %s</p></div>
</article>''' % (PF, e["bild"], V, e["nr"], e["titel"], absaetze(e["text"]), e["bild_anders"], e["text_anders"], e["streichen"], e["quelle"])


def main():
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span>Persönliches Profil</span><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Experimentierfeld</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Persönliches Profil &middot; Experimentierfeld</p>
      <h1>Klar sagen, was <span class="hl">Sache ist.</span></h1>
      <p class="e2-lead">Hier entwickeln wir Daniels Sprech weiter – im Text und im Bild. Bewusst übertrieben: Was zu viel ist, streichen wir danach wieder raus. Nichts davon ist eingeplant, die Entwürfe im Redaktionsplan bleiben, wie sie sind.</p>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Der Maßstab</p><h2 class="e2-h2">Woran wir jedes Experiment messen.</h2></div>
    <ul class="mex-massstab">''' + "".join("<li><b>%s</b><span>%s</span></li>" % m for m in MASSSTAB) + '''</ul>
    <p class="mex-nie"><b>Nie:</b> Gossensprache oder Rumschimpfen. Klare Meinung ja, Krawall nein.</p>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Runde 1 &middot; 23.10.2026</p><h2 class="e2-h2">Drei Experimente.</h2>
    <p class="e2-lead">Jedes dreht an einem anderen Hebel: Klartext, Geständnis, Dialog. Alles aus Daniels eigenen Antworten – nichts erfunden.</p></div>
    <div class="mex-liste">''' + "".join(experiment(e) for e in EXPERIMENTE) + '''</div>
  </div></section>

</main>'''
    quelle = open(os.path.join(HIER, "seiten-vorlage.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Experimentierfeld · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Experimentierfeld für Daniels persönliches Profil: Sprech und Bilder weiterentwickeln."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-experimente.html"), "w", encoding="utf-8").write(kopf + main_html + fuss)
    print("Experimentierfeld gebaut ·", len(EXPERIMENTE), "Experimente")


if __name__ == "__main__":
    main()
