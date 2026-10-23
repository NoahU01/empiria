#!/usr/bin/env python3
"""Baut Medienkonzept › Persönliches Profil › Experimentierfeld (Daniel, 23.10.2026).
Hier wird Daniels Sprech weiterentwickelt: klarer, aufrüttelnder, Bilder außerhalb des Rasters.
Bewusst übertrieben – danach wird gestrichen. Nichts davon ist eingeplant; bestehende Entwürfe bleiben unberührt.

    python3 werkzeuge/medienkonzept/experimente_seite_bauen.py
"""
import os, html

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "70"
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

STUFEN = [
    dict(nr="1", titel="Der nächste Schritt", grad="sofort einsetzbar", bilder=["st1"],
         sprache="Ich-Perspektive, ein lockerer Einstieg, sonst ruhig erklärt.",
         bild="Echtes Foto mit handschriftlicher Notiz und Pfeil – wirkt wie ein Schnappschuss aus dem Workshop.",
         darstellung="Einzelbild, wie bisher.",
         grenze="Trägt. Kann so in den Redaktionsplan.",
         text="""Mein erster Handgriff in fast jedem Projekt hat nichts mit Strategie zu tun. Ich räume Folien weg.

Die Arbeit darin ist oft gut. Nur erzählen die meisten Folien das eigene Thema, mit allen Details, aus Sicht dessen, der präsentiert. Was der Entscheider davon hat, steht selten darin.

Also fangen wir anders an: erst das Gesamtbild, auf einem Blatt. Dann entscheiden wir, welche Details es wirklich braucht.

Meistens sind es deutlich weniger, als alle dachten."""),
    dict(nr="2", titel="Mutig", grad="klare Kante", bilder=["st2"],
         sprache="Direkte Ansprache, eine harte These, die der Leser auf sich beziehen muss.",
         bild="Plakat mit Zahl: 27 Folien durchgestrichen, 1 Bild groß dagegen.",
         darstellung="Einzelbild als Plakat – eine Aussage, sonst nichts.",
         grenze="Trägt, wenn der Ton danach wieder hilfsbereit wird. Die These darf weh tun, der Text darf nicht von oben herab sein.",
         text="""Ich sage es so direkt, wie ich es im Projekt auch sage: Wenn deine Vorstandsvorlage 27 Folien hat, weißt du noch nicht genau, was du entscheiden lassen willst.

Ich habe das oft genug gesehen. Wer sein Thema richtig durchdrungen hat, kriegt es auf ein Bild. Wer nicht, versteckt sich hinter Folie 14.

Bei mir wandern bestehende Folien deshalb als Erstes ins Backup. Alle. Dann zeichnen wir das Gesamtbild. Und ganz schnell merkt man, ob das Thema trägt.

Das tut kurz weh. Und spart dir die nächste Schleife."""),
    dict(nr="3", titel="Grenzwertig", grad="Humor mit Spitze", bilder=["st3a", "st3b", "st3c", "st3d", "st3e"],
         sprache="Augenzwinkern, Hitliste, eine echte Frage zum Mitmachen am Ende.",
         bild="Nachgebaute Folien mit Stempel „→ Backup“ – Wiedererkennung aus jedem Sitzungssaal.",
         darstellung="Dokument-Karussell mit fünf Seiten statt Einzelbild. Neu für den Feed.",
         grenze="Die Hitliste ist meine Zuspitzung, nicht dein Erlebnis – nur nehmen, wenn du die Plätze so unterschreibst. Kann für manche Vorstände nach Spott über ihre eigenen Sitzungen klingen.",
         text="""Kleines Geständnis: Ich führe eine Hitliste. Folien, die in meinen Projekten als Erstes fliegen.

Die Plätze 3 bis 1 stehen im Dokument. Wer schon einmal in einer Vorstandssitzung saß, kennt jede davon.

Klingt gemein? Ein bisschen. Aber jede dieser Folien kostet Minuten, in denen keiner über die Entscheidung redet.

Mein Tausch: alles ins Backup, ein Gesamtbild auf den Tisch. Dann reden wir über das, was zählt.

Und jetzt du: Welche Folie würdest du sofort löschen?"""),
    dict(nr="4", titel="Zu wild", grad="bewusst drüber", bilder=["st4"],
         sprache="Großbuchstaben, Stakkato, Ansage an den Leser, „Deal?“.",
         bild="Foto abgedunkelt, riesiger Stempel „GELÖSCHT.“, Text in Versalien.",
         darstellung="Einzelbild im Werbeplakat-Stil.",
         grenze="Hier kippt es: Großbuchstaben schreien, „in drei Wochen durch“ ist ein Zahlenversprechen ohne Beleg, „Wer das nicht aushält, ist bei mir falsch“ stößt genau die Vorstände vor den Kopf, die wir erreichen wollen. Einzelne Elemente (der Stempel, „Auch deine Lieblingsfolie“) können wir trotzdem in Stufe 2 oder 3 übernehmen.",
         text="""ICH LÖSCHE DEINE FOLIEN.

Alle 27.

Ja, auch die mit der Animation, an der du bis 23 Uhr gesessen hast.

Ja, auch die, die dein Chef so mag.

Ins Backup damit. Keine Diskussion.

Dafür bekommst du ein Bild. Ein einziges. Und eine Entscheidung.

Wer das nicht aushält, ist bei mir falsch. Wer es aushält, ist in drei Wochen durch.

Deal?"""),
]


def stufe(e):
    bilder = "".join('<img src="%s%s.jpg?v=%s" alt="" loading="lazy">' % (PF, b, V) for b in e["bilder"])
    karussell = " mex-bild--karussell" if len(e["bilder"]) > 1 else ""
    return '''<article class="mex-karte mex-stufe mex-stufe--%s">
  <figure class="mex-bild%s">%s</figure>
  <div class="mex-text"><p class="mex-nr"><b>%s</b><span>%s</span><em>%s</em></p>
    <div class="mex-posting">%s</div>
    <dl class="mex-was"><div><dt>Sprache</dt><dd>%s</dd></div><div><dt>Bild</dt><dd>%s</dd></div><div><dt>Darstellung</dt><dd>%s</dd></div><div class="mex-streichen"><dt>Wo die Grenze liegt</dt><dd>%s</dd></div></dl></div>
</article>''' % (e["nr"], karussell, bilder, e["nr"], e["titel"], e["grad"], absaetze(e["text"]), e["sprache"], e["bild"], e["darstellung"], e["grenze"])


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
    <div class="ak-kopf"><p class="e2-kicker">Runde 2 &middot; 23.10.2026</p><h2 class="e2-h2">Ein Thema, vier Stufen.</h2>
    <p class="e2-lead">Dieselbe Aussage – „Folien wandern bei mir als Erstes ins Backup“ – von Stufe zu Stufe lauter: in der Sprache, im Bild und in der Darstellung. Ziel: die Stelle finden, an der du sagst, jetzt wird es zu wild.</p></div>
    <ol class="mex-leiter"><li>Der nächste Schritt</li><li>Mutig</li><li>Grenzwertig</li><li>Zu wild</li></ol>
    <div class="mex-liste">''' + "".join(stufe(e) for e in STUFEN) + '''</div>
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
