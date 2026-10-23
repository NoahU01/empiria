#!/usr/bin/env python3
"""Baut Medienkonzept › Persönliches Profil › Experimentierfeld (Daniel, 23.10.2026).
Hier wird Daniels Sprech weiterentwickelt: klarer, aufrüttelnder, Bilder außerhalb des Rasters.
Bewusst übertrieben – danach wird gestrichen. Nichts davon ist eingeplant; bestehende Entwürfe bleiben unberührt.

    python3 werkzeuge/medienkonzept/experimente_seite_bauen.py
"""
import os, html

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
V = "71"
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
    dict(nr="1", titel="Der nächste Schritt", grad="sofort einsetzbar",
         grenze="Trägt. Kann so in den Redaktionsplan.",
         beispiele=[
            dict(titel="Folien ins Backup", bilder=["st1"], hebel="Echtes Foto mit Handschrift-Notiz",
                 text="""Mein erster Handgriff in fast jedem Projekt hat nichts mit Strategie zu tun. Ich räume Folien weg.

Die Arbeit darin ist oft gut. Nur erzählen die meisten Folien das eigene Thema, mit allen Details, aus Sicht dessen, der präsentiert. Was der Entscheider davon hat, steht selten darin.

Also fangen wir anders an: erst das Gesamtbild, auf einem Blatt. Dann entscheiden wir, welche Details es wirklich braucht.

Meistens sind es deutlich weniger, als alle dachten."""),
            dict(titel="Der Kalender", bilder=["s1b"], hebel="Nachgebauter Wochenkalender, ein gelber Block",
                 text="""Wenn ich mit frisch beförderten Führungskräften spreche, sehe ich fast immer denselben Kalender.

Regeltermine von morgens bis abends. Viele davon geerbt. Welchen Mehrwert sie bringen, können die meisten selbst nicht sagen.

Und irgendwo dazwischen, wenn es gut läuft, eine halbe Stunde für das, wofür sie eigentlich befördert wurden.

Mein Rat für die ersten Wochen: Gehe jeden Regeltermin einmal durch und frage dich, was passieren würde, wenn du nicht hingehst.

Bei manchen ist die ehrliche Antwort: nichts."""),
            dict(titel="„Dass es läuft“", bilder=["s1c"], hebel="Selfie mit Kundensatz in Handschrift",
                 text="""Von allem, was Kunden über die Zusammenarbeit mit uns sagen, mag ich einen Satz am liebsten. Er steht auf dem Bild.

Darin geht es nicht um Folien, Workshops oder Methoden. Es geht um ein Gefühl: Ich muss mich nicht mehr um alles selbst kümmern.

Dahinter steckt wenig Magie. Ich halte den Aufwand für mein Gegenüber so klein wie möglich. Ich entwickle das Besprochene sofort weiter, rufe die drei Leute an, die wir brauchen, und sorge für den nächsten Termin.

Wer länger mit mir arbeitet, weiß: Zwischen den Terminen passiert am meisten."""),
         ]),
    dict(nr="2", titel="Mutig", grad="klare Kante",
         grenze="Trägt, solange der Text nach der harten These hilfsbereit bleibt. Die These darf wehtun, der Ton darf nicht von oben herab sein.",
         beispiele=[
            dict(titel="27 Folien, 1 Bild", bilder=["st2"], hebel="Plakat mit harter Zahl",
                 text="""Ich sage es so direkt, wie ich es im Projekt auch sage: Wenn deine Vorstandsvorlage 27 Folien hat, weißt du noch nicht genau, was du entscheiden lassen willst.

Ich habe das oft genug gesehen. Wer sein Thema richtig durchdrungen hat, kriegt es auf ein Bild. Wer nicht, versteckt sich hinter Folie 14.

Bei mir wandern bestehende Folien deshalb als Erstes ins Backup. Alle. Dann zeichnen wir das Gesamtbild. Und ganz schnell merkt man, ob das Thema trägt.

Das tut kurz weh. Und spart dir die nächste Schleife."""),
            dict(titel="Kein Konfliktseminar", bilder=["s2b"], hebel="Gelbes Plakat, Absage als Headline",
                 text="""Ein Führungsteam wollte von mir ein Angebot für ein Konfliktmanagement-Seminar.

Ich habe keines geschrieben.

Nach ein paar Fragen war klar: Keiner wusste so richtig, wo der Bereich hin soll. Kein Zielbild, keine Richtung. Jeder hat den Alltag anders interpretiert. Natürlich gibt es da Konflikte.

Dagegen hilft kein Seminar. Dagegen hilft Klarheit.

Genau da haben wir angesetzt. Und eine der drei Führungskräfte, die mir am Anfang noch erklärt hatte „Ich bin Projektleiter, keine Führungskraft“, sagte im dritten oder vierten Termin ganz selbstverständlich: „Ich in meiner Rolle als Führungskraft …“

Das war Weltklasse."""),
            dict(titel="Nein sagen", bilder=["s2c"], hebel="Porträt mit Karte „Nein“, ein Satz",
                 text="""Ich sage öfter Nein, als man denkt.

Wenn mich jemand für ein Thema holen will, in dem ich nicht gut bin, sage ich das. Je mehr es ins rein Psychologische geht, desto klarer bin ich raus. Und für Themen, bei denen Menschen in eine Richtung gedrückt werden sollen, obwohl jeder sieht, dass es nicht funktioniert, bin ich gar nicht zu haben.

Ich arbeite über Klarheit, Nutzen und Sinn. Mit Druck arbeite ich nicht.

Die meisten nehmen das dankend an, weil sie ein Ergebnis wollen. Dann einigen wir uns auf einen Weg, der funktioniert. Oder ich nenne ihnen jemanden, der besser passt.

Ein Nein zur richtigen Zeit erspart beiden Seiten viel Frust."""),
         ]),
    dict(nr="3", titel="Grenzwertig", grad="Humor mit Spitze",
         grenze="Satire auf Sitzungen und Workshops. Trägt nur, wenn du die Zuspitzung unterschreibst – manche Vorstände lesen darin Spott über ihre eigenen Runden.",
         beispiele=[
            dict(titel="Die Hitliste", bilder=["st3a", "st3b", "st3c", "st3d", "st3e"], hebel="Dokument-Karussell, fünf Seiten",
                 text="""Kleines Geständnis: Ich führe eine Hitliste. Folien, die in meinen Projekten als Erstes fliegen.

Die Plätze 3 bis 1 stehen im Dokument. Wer schon einmal in einer Vorstandssitzung saß, kennt jede davon.

Klingt gemein? Ein bisschen. Aber jede dieser Folien kostet Minuten, in denen keiner über die Entscheidung redet.

Mein Tausch: alles ins Backup, ein Gesamtbild auf den Tisch. Dann reden wir über das, was zählt.

Und jetzt du: Welche Folie würdest du sofort löschen?"""),
            dict(titel="Workshop-Bingo", bilder=["s3b"], hebel="Bingo-Karte zum Mitspielen",
                 text="""Für deinen nächsten Strategie-Workshop habe ich dir etwas mitgebracht.

Kreuze an, was fällt. Bei einer vollen Reihe darfst du laut „Bingo“ rufen. Oder leise lächeln.

Im Ernst: Jeder dieser Sätze ist ein Zeichen dafür, dass gerade keiner entscheiden will. „Lass uns das offline klären“ heißt meistens: gar nicht. „Parkplatz“ heißt: für immer.

Wenn du in deinem nächsten Workshop drei davon hörst, stelle eine einzige Frage: Was entscheiden wir heute?

Dann wird es kurz still. Und dann wird es gut."""),
            dict(titel="Die Stellenanzeige", bilder=["s3c"], hebel="Nachgebaute Anzeige als Satire",
                 text="""Wenn Häuser ehrlich ausschreiben würden, was ihrem Vorstand fehlt, sähe die Anzeige ungefähr so aus.

Gesucht wird jemand, der widerspricht, wenn alle nicken. Der eine andere Perspektive einnimmt und sie gut begründet. Der Fragen stellt, die unbequem sind, und Zusammenhänge zeigt, die keiner sehen wollte.

Anforderungen: keine Angst vor Hierarchie. Keine Lust auf Kompromisse aus Höflichkeit.

Wir bieten: einen Vorstand, der endlich wieder etwas Neues hört.

Ich weiß, diese Anzeige wird so nie erscheinen. Aber falls du gerade an deine eigene Runde denkst: Wer würde sich darauf bewerben?"""),
         ]),
    dict(nr="4", titel="Zu wild", grad="bewusst drüber",
         grenze="Hier soll es kippen. Makaber, laut, mit erfundenen Zahlen als Stilmittel. Einzelne Elemente – der Stempel, der Fahndungsaufruf als Form – können wir trotzdem eine Stufe tiefer übernehmen.",
         beispiele=[
            dict(titel="GELÖSCHT.", bilder=["st4"], hebel="Stempel, Versalien, „Deal?“",
                 text="""ICH LÖSCHE DEINE FOLIEN.

Alle 27.

Ja, auch die mit der Animation, an der du bis 23 Uhr gesessen hast.

Ja, auch die, die dein Chef so mag.

Ins Backup damit. Keine Diskussion.

Dafür bekommst du ein Bild. Ein einziges. Und eine Entscheidung.

Wer das nicht aushält, ist bei mir falsch. Wer es aushält, ist in drei Wochen durch.

Deal?"""),
            dict(titel="Todesanzeige", bilder=["s4b"], hebel="Traueranzeige für eine Strategie",
                 text="""Wir nehmen Abschied.

Von einer Strategie, die mit großem Aufwand entstanden ist. Zwei Tage Klausur, 84 Folien, ein Leitbild mit sieben Werten.

Sie hat den Alltag nie erreicht. Montags wusste keiner, was sie für die eigene Arbeit bedeutet.

Sie hinterlässt ein Plakat im Flur und eine Mappe im Schrank.

Von Beileidsbekundungen bitten wir abzusehen. Stattdessen: Macht es beim nächsten Mal anders. Erst das Zielbild, das jeder versteht. Dann die Strategie als Weg dorthin. Und dann jemand, der sie jeden Montag in den Alltag trägt."""),
            dict(titel="Steckbrief", bilder=["s4c"], hebel="Fahndungsplakat „Tot oder lebendig“",
                 text="""Fahndungsaufruf.

Seit dem Frühjahr spurlos verschwunden: die Entscheidung.

Beschreibung: klar, eigentlich längst überfällig. Zuletzt gesehen in einer Vorstandssitzung. Seitdem dreimal vertagt. Hört auf den Namen „Lass uns das noch einmal vertiefen“.

Sachdienliche Hinweise: Sie versteckt sich meistens dort, wo keiner sagen kann, was das Thema für das Unternehmen bedeutet.

Belohnung: ein Bereich, der wieder vorankommt.

Festnehmen kann sie übrigens jeder, der in den Lead geht."""),
         ]),
]


def beispiel(e):
    bilder = e["bilder"]
    gross = "|".join("%s%s.jpg?v=%s" % (PF, b, V) for b in bilder)
    zahl = '<span class="mex-seiten">%d Seiten</span>' % len(bilder) if len(bilder) > 1 else ""
    return '''<article class="mex-bsp"><button type="button" class="mex-thumb" data-gross="%s" aria-label="Bild groß ansehen"><img src="%s%s.jpg?v=%s" alt="" loading="lazy">%s</button>
  <b>%s</b><span>%s</span><details><summary>Text lesen</summary><div class="mex-posting">%s</div></details></article>''' % (gross, PF, bilder[0], V, zahl, e["titel"], e["hebel"], absaetze(e["text"]))


def stufe(st):
    return '''<div class="mex-stufenblock mex-stufenblock--%s"><div class="mex-stufenkopf"><p class="mex-nr"><b>%s</b><span>%s</span><em>%s</em></p><p class="mex-grenze">%s</p></div>
  <div class="mex-raster">%s</div></div>''' % (st["nr"], st["nr"], st["titel"], st["grad"], st["grenze"], "".join(beispiel(e) for e in st["beispiele"]))


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
    <div class="ak-kopf"><p class="e2-kicker">Runde 2 &middot; 23.10.2026</p><h2 class="e2-h2">Vier Stufen, je drei Beispiele.</h2>
    <p class="e2-lead">Von Stufe zu Stufe lauter – in Sprache, Bild und Darstellung. Jedes Beispiel nimmt ein anderes Thema aus deinen Antworten. Bild antippen zum Vergrößern, Text aufklappen. Ziel: die Stelle finden, an der du sagst, jetzt wird es zu wild.</p></div>
    <ol class="mex-leiter"><li>Der nächste Schritt</li><li>Mutig</li><li>Grenzwertig</li><li>Zu wild</li></ol>
    <div class="mex-stufen">''' + "".join(stufe(e) for e in STUFEN) + '''</div>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Runde 1 &middot; 23.10.2026</p><h2 class="e2-h2">Drei Experimente.</h2>
    <p class="e2-lead">Jedes dreht an einem anderen Hebel: Klartext, Geständnis, Dialog. Alles aus Daniels eigenen Antworten – nichts erfunden.</p></div>
    <div class="mex-liste">''' + "".join(experiment(e) for e in EXPERIMENTE) + '''</div>
  </div></section>

</main>
<dialog class="mex-gross" id="mex-gross"><button type="button" class="mex-zu" aria-label="Schließen">×</button><div class="mex-gross__bilder"></div></dialog>
<script>
(function(){var d=document.getElementById('mex-gross'),b=d.querySelector('.mex-gross__bilder');
document.addEventListener('click',function(e){var t=e.target.closest('.mex-thumb');if(t){b.innerHTML=t.dataset.gross.split('|').map(function(u){return '<img src="'+u+'" alt="">';}).join('');d.showModal();return;}
if(e.target.closest('.mex-zu')||e.target===d)d.close();});})();
</script>'''
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
