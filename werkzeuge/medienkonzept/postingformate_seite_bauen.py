#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Postingformate: Themen und Postingtypen für Daniels persönliches Profil.

    python3 werkzeuge/medienkonzept/postingformate_seite_bauen.py
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
PF = "/assets/projekte/medienkonzept/postings/"
V = "25"

THEMEN = [
    ("Baustein 1 · Strategie in den Alltag überführen", "Strategie, die im Alltag ankommt", "Zielbild, Vision und Strategie so klar, dass jeder weiß, wie der Bereich erfolgreich ist und was sein Beitrag ist.",
     "Zielbild heißt: Jeder hat das Geschäftsmodell verstanden · Die Strategie gibt der Chef vor · operativ und strategisch trennen"),
    ("Baustein 1 · Strategie in den Alltag überführen", "Führung, die trägt", "Führungskräfte, die ihre Rolle von Anfang an ausfüllen und Strategie in ihren Bereich bringen.",
     "Erst befördern, dann entwickeln ist falsch · Rolle und drei Säulen · geduldetes Fehlverhalten demotiviert die Guten"),
    ("Baustein 2 · Komplexe Themen strukturieren und kommunizieren", "Entscheidungen herbeiführen", "Vorstand, Aufsichtsrat und Stakeholder so ansprechen, dass entschieden wird.",
     "Why – How – What next · Themen auf der falschen Flugebene · Diskussionen kippen, wenn die Bedeutung fehlt"),
    ("Baustein 2 · Komplexe Themen strukturieren und kommunizieren", "Vertrieb, der die Strategie umsetzt", "Vertriebsstrategie, Markteinführungen und Tagungen, die im Alltag etwas bewegen.",
     "Nach der Vertriebstagung spricht nach vier Wochen keiner mehr davon · What's in it for me"),
    ("Baustein 3 · Innovation und Geschäftsmodell neu denken", "Geschäftsmodell der Zukunft", "Neu denken auf einem Kern, den man im Griff hat – nicht als Wunschliste.",
     "Die Neugründungs-Frage · Aufgabenzuschnitt, Platz in der Wertschöpfung, Zielgruppen"),
    ("Baustein 3 · Innovation und Geschäftsmodell neu denken", "KI aus eigener Praxis", "Erfahrungswissen statt Meinung: wie KI hilft, schneller und besser zu entscheiden.",
     "Viele reden mit, ohne KI selbst zu nutzen · Taskforce und Verbote im Haus"),
    ("Quer über alle drei", "Branche und Regulierung eingeordnet", "Was die Branche bewegt und was AI Act, DORA oder BaFin im Alltag bewirken. Quelle: Branchen-Radar, montags.",
     "Konsequenzen statt Detailauslegung · Studien und Zahlen mit Quelle"),
]

# Typ, Bild, was der Leser bekommt, Bild-Beschreibung, Foto nötig, Messgröße, Beleg/Einschätzung
TYPEN = [
    ("Die Szene", "v1.jpg", "Ein echter Moment aus deiner Arbeit – und was er über Führung oder Strategie zeigt.",
     "Echtes Foto, ohne Text. Ab und zu mit einem Satz im Bild (wie die Entwürfe 01, 02, 04).", True,
     "Kommentare, Profilbesuche", "Belegt: persönliche Fotos bis +50 % Engagement (van der Blom 2025); deine Szenen-Postings hatten 70 % mehr Reaktionen als Thesen."),
    ("Der Satz", "t1.jpg", "Ein wörtlicher Satz eines Vorstands oder Kunden – und deine Einordnung.",
     "Satzkarte in Gelb oder Porträt aus dem Bestand mit dem Satz (wie Entwurf 03).", False,
     "Reichweite", "Belegt an deinen Zahlen: Satz plus Führungsthema hatte die höchste Reichweite (Median 1.848)."),
    ("Die Frage", "k1.jpg", "Eine Prüffrage, die der Leser für sich beantwortet.",
     "Fragekarte, ein Wort im gelben Block, Markenzeichen dazu.", False,
     "Kommentare", "Einschätzung: Fragen zum Selbsttest regen Kommentare an; keine Köderfrage am Schluss."),
    ("Das Modell", "m1.jpg", "Ein Zusammenhang auf einen Blick, den man speichert.",
     "Diagramm im empiria-Design – aus deinen Werkzeugen (Why – How – What next, drei Säulen, Erfolgsmap).", False,
     "Speichern", "Einschätzung: Bildbeiträge mit 5,3 % Engagement (Socialinsider); Speichern gilt als starkes Signal (Branchenbeobachtung, nicht von LinkedIn bestätigt)."),
    ("Das Werkzeug", "p5.jpg", "Drei Schritte, die man morgen anwenden kann.",
     "Werkzeugkarte in Schwarz.", False,
     "Speichern", "Einschätzung, wie beim Modell."),
    ("Eingeordnet", "z1.jpg", "Eine Branchen- oder Regulierungsnachricht – und was sie für einen Bereich heißt.",
     "Zahl oder Schlagzeile groß, mit Quelle. Inhalte aus dem Branchen-Radar.", False,
     "Reichweite außerhalb deines Netzwerks", "Einschätzung: aktuelle Themen erreichen neue Leser; LinkedIn bewertet Relevanz für ein Fachpublikum (LinkedIn-Team)."),
    ("Zum Mitnehmen", "d1.jpg", "Eine Methode vollständig, auf 6 bis 8 Seiten.",
     "Dokument im empiria-Design zum Durchblättern (wie Entwurf 06).", False,
     "Speichern", "Belegt: Dokumente haben die höchste Engagement-Rate, 7,0 % (Socialinsider, 1,3 Mio. Beiträge)."),
]

WOCHE = [
    ("Mo", "Die Frage", "nein"),
    ("Di", "Die Szene – alle zwei Wochen „Du als Person“", "ja, ein Foto"),
    ("Mi", "Das Modell oder Das Werkzeug", "nein"),
    ("Do", "Der Satz", "nein (Porträt aus dem Bestand)"),
    ("Fr", "Eingeordnet – alle zwei Wochen Zum Mitnehmen", "nein"),
]


def themen():
    k = []
    for bs, t, w, m in THEMEN:
        quer = " mpf-thema--quer" if bs.startswith("Quer") else ""
        k.append('<div class="mpf-thema%s"><span class="mpf-nr">%s</span><b>%s</b><p>%s</p><small>Aus deinem Material: %s</small></div>' % (quer, bs, t, w, m))
    return '<div class="mpf-themen">%s</div>' % "".join(k)


def typen():
    k = []
    for t, bild, leser, b, foto, mess, beleg in TYPEN:
        k.append('''<article class="mpf-typ"><div class="mpf-typ__bild"><img src="%s%s" alt="" loading="lazy"></div><div class="mpf-typ__text">
<span class="mpf-foto mpf-foto--%s">%s</span><b>%s</b><p>%s</p><dl><div><dt>Bild</dt><dd>%s</dd></div><div><dt>Messen an</dt><dd>%s</dd></div><div><dt>Grundlage</dt><dd>%s</dd></div></dl></div></article>''' % (
            PF, bild, "ja" if foto else "nein", "Foto von dir nötig" if foto else "ohne Foto von dir", t, leser, b, mess, beleg))
    k.append('''<article class="mpf-typ mpf-typ--leer"><div class="mpf-typ__bild mpf-platzhalter"><span>Dein Foto:<br>Lego, Mountainbike, Lustiges Taschenbuch</span></div><div class="mpf-typ__text">
<span class="mpf-foto mpf-foto--ja">Handyfoto, kein Porträt</span><b>Du als Person</b><p>Eine Analogie aus deinem Leben, die zu einem Thema führt – die Frage deiner Kinder, die Tochter mit Spaß an Buchhaltung, das Mountainbike.</p><dl><div><dt>Bild</dt><dd>Ein Foto vom Gegenstand oder Ort, nicht von dir und nie von den Kindern.</dd></div><div><dt>Messen an</dt><dd>Kommentare, Profilbesuche</dd></div><div><dt>Grundlage</dt><dd>Einschätzung: macht dich als Person greifbar; aus deinem Interview, 13.10.</dd></div></dl></div></article>''')
    return '<div class="mpf-typen">%s</div>' % "".join(k)


def woche():
    z = "".join('<tr><td class="mkf-nr">%s</td><td>%s</td><td>%s</td></tr>' % w for w in WOCHE)
    return '<div class="mkf-tabelle"><table style="min-width:0"><tr><th>Tag</th><th>Postingtyp</th><th>Foto von dir nötig</th></tr>%s</table></div>' % z


MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Postingformate</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Postingformate &middot; Vorschlag zur Entscheidung</p>
      <h1>Worüber du sprichst. Und wie es <span class="hl">aussieht.</span></h1>
      <p class="e2-lead">Zwei Achsen für dein persönliches Profil: sieben Themen aus dem Strategiehandwerk und acht Postingtypen. Nur zwei Typen brauchen ein Foto – so tragen fünf Postings pro Woche, und es wird nicht eintönig. Jedes Thema kann in jedem Typ erscheinen.</p>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Achse 1</p><h2 class="e2-h2">Die Themen.</h2>
    <p class="e2-lead">Abgeleitet aus dem Dreiklang des Strategiehandwerks – je Baustein zwei Themen, eines quer dazu. Die Herleitung zeigt die Seite <a href="/projekte/medienkonzept-zuordnung.html">Zuordnung</a>.</p></div>
    ''' + themen() + '''
    <p class="mpf-quer"><b>Quer dazu: du als Person.</b> Analogien und Erlebnisse aus deinem Leben würzen jedes Thema – und sind ab und zu ein eigenes Posting.</p>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Achse 2</p><h2 class="e2-h2">Die Postingtypen.</h2>
    <p class="e2-lead">Jeder Typ hat eine Aufgabe und ein festes Bild. So wechselt das Aussehen von Tag zu Tag, und trotzdem erkennt man dich an Schrift, Gelb und Ton.</p></div>
    ''' + typen() + '''
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Die Woche</p><h2 class="e2-h2">Fünf Postings, ein Foto.</h2>
    <p class="e2-lead">Die Themen wandern durch die Woche, damit keins zweimal hintereinander kommt. Start: drei Postings pro Woche, dann fünf.</p></div>
    ''' + woche() + '''
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Ehrlich gesagt</p><h2 class="e2-h2">Was belegt ist und was nicht.</h2></div>
    <ul class="mpf-ehrlich">
      <li><b>Belegt:</b> Dokumente erzielen das meiste Engagement, Text ohne Bild das wenigste; persönliche Fotos wirken; ein klares Fachgebiet wird belohnt; deine Szenen und Sätze liefen besser als deine Thesen.</li>
      <li><b>Einschätzung:</b> dass Frage, Modell, Werkzeug und Eingeordnet als gestaltete Karten auf deinem Profil tragen. Dafür gibt es keine direkte Studie. Darum werten wir jeden Typ nach vier Wochen aus und bauen um, was nicht trägt.</li>
    </ul>
  </div></section>

</main>'''


def main():
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Postingformate · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Themen und Postingtypen für Daniels persönliches Profil."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-postingformate.html"), "w", encoding="utf-8").write(kopf + MAIN + fuss)
    print("Postingformate-Seite gebaut")


if __name__ == "__main__":
    main()
