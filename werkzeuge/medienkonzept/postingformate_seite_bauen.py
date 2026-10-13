#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Postingformate: Themen und Postingtypen für Daniels persönliches Profil.

    python3 werkzeuge/medienkonzept/postingformate_seite_bauen.py
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
PF = "/assets/projekte/medienkonzept/postings/"
V = "33"

THEMEN = [
    ("Baustein 1 · Strategie in den Alltag überführen", "Strategie, die im Alltag ankommt", "Zielbild, Vision und Strategie so klar, dass jeder weiß, wie der Bereich erfolgreich ist und was sein Beitrag ist.",
     "Zielbild heißt: Jeder hat das Geschäftsmodell verstanden · Die Strategie gibt der Chef vor · operativ und strategisch trennen"),
    ("Baustein 1 · Strategie in den Alltag überführen", "Führung, die trägt", "Klare Aussagen zu Rolle, Umsetzung und Wichtigkeit von Führung – als Teil der Strategie.",
     "Erst befördern, dann entwickeln ist falsch · Rolle und drei Säulen · geduldetes Fehlverhalten demotiviert die Guten"),
    ("Baustein 1 · Strategie in den Alltag überführen", "KI aus eigener Praxis", "Erfahrungswissen statt Meinung: wie KI hilft, schneller und besser zu entscheiden.",
     "Viele reden mit, ohne KI selbst zu nutzen · Taskforce und Verbote im Haus"),
    ("Baustein 2 · Komplexe Themen strukturieren und kommunizieren", "Entscheidungen herbeiführen", "Vorstand, Aufsichtsrat und Stakeholder so ansprechen, dass entschieden wird.",
     "Why – How – What next · Themen auf der falschen Flugebene · Diskussionen kippen, wenn die Bedeutung fehlt"),
    ("Baustein 2 · Komplexe Themen strukturieren und kommunizieren", "Vertrieb, der die Strategie umsetzt", "Vertriebsstrategie, Markteinführungen und Tagungen, die im Alltag etwas bewegen.",
     "Nach der Vertriebstagung spricht nach vier Wochen keiner mehr davon · What's in it for me"),
    ("Baustein 3 · Innovation und Geschäftsmodell neu denken", "Geschäftsmodell der Zukunft", "Hinterfragen, ob es so organisiert sein muss wie heute – Zukunftsbilder erlaubt.",
     "Die Neugründungs-Frage · Aufgabenzuschnitt, Platz in der Wertschöpfung, Zielgruppen"),
    ("Quer über alle drei", "Branche und Regulierung eingeordnet", "Was die Branche bewegt und was AI Act, DORA oder BaFin im Alltag bewirken. Quelle: Branchen-Radar, montags.",
     "Konsequenzen statt Detailauslegung · Studien und Zahlen mit Quelle"),
]

# Typ, Bild, was der Leser bekommt, Bild-Beschreibung, Foto nötig, Messgröße, Beleg/Einschätzung
TYPEN = [
    ("Die Szene", True, "Ein echter Moment aus deiner Arbeit – und was er über Führung oder Strategie zeigt.", "Kommentare, Profilbesuche",
     "Belegt: persönliche Fotos bis +50 % Engagement (van der Blom 2025); deine Szenen-Postings +70 % Reaktionen gegenüber Thesen.",
     [("A", "Foto pur", "v1.jpg"), ("B", "Foto mit einem Satz", "s1.jpg"), ("C", "Foto als Karte", "p1.jpg")]),
    ("Der Satz", False, "Ein wörtlicher Satz eines Vorstands oder Kunden – und deine Einordnung.", "Reichweite",
     "Belegt an deinen Zahlen: Satz plus Führungsthema hatte die höchste Reichweite (Median 1.848).",
     [("A", "Satzkarte Gelb", "t1.jpg"), ("B", "Porträt mit Satz", "p3.jpg"), ("C", "Die Nachricht", "c1.jpg")]),
    ("Die Frage", False, "Eine Prüffrage, die der Leser für sich beantwortet.", "Kommentare",
     "Einschätzung: Fragen zum Selbsttest regen Kommentare an; nie als Köderfrage am Schluss.",
     [("A", "Fragekarte Weiß", "k1.jpg"), ("B", "Schwarz mit Icon", "k2.jpg")]),
    ("Das Modell", False, "Ein Zusammenhang auf einen Blick, den man speichert.", "Speichern",
     "Einschätzung: Bildbeiträge 5,3 % Engagement (Socialinsider); Speichern gilt als starkes Signal (Branchenbeobachtung).",
     [("A", "Drei Stufen", "m1.jpg"), ("B", "Drei Icons", "m2.jpg"), ("C", "Ohne / Mit", "m3.jpg")]),
    ("Das Werkzeug", False, "Drei Schritte oder Fragen, die man morgen anwenden kann.", "Speichern",
     "Einschätzung, wie beim Modell.",
     [("A", "Liste Schwarz", "p5.jpg"), ("B", "Checkliste Gelb", "w2.jpg")]),
    ("Eingeordnet", False, "Eine Branchen- oder Regulierungsnachricht – und was sie heute für einen Bereich heißt.", "Reichweite außerhalb deines Netzwerks",
     "Einschätzung: LinkedIn bewertet Relevanz für ein Fachpublikum (LinkedIn-Team). Inhalte aus dem Branchen-Radar.",
     [("A", "Zahl", "z1.jpg"), ("B", "Zahl auf Foto", "n1.jpg"), ("C", "Schlagzeile", "z2.jpg")]),
    ("Zum Mitnehmen", False, "Eine Methode vollständig, auf 6 bis 8 Seiten zum Durchblättern.", "Speichern",
     "Belegt: Dokumente haben die höchste Engagement-Rate, 7,0 % (Socialinsider, 1,3 Mio. Beiträge).",
     [("A", "Titelseite", "d1.jpg"), ("", "Innenseite", "d2.jpg"), ("", "Schlussseite", "d6.jpg")]),
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
    for t, foto, leser, mess, beleg, varianten in TYPEN:
        vs = "".join('<figure><img src="%s%s" alt="" loading="lazy"><figcaption>%s%s</figcaption></figure>' % (
            PF, bild, ('<b>%s</b> ' % v) if v else "", name) for v, name, bild in varianten)
        k.append('''<article class="mpv-typ"><div class="mpv-text">
<span class="mpf-foto mpf-foto--%s">%s</span><h3>%s</h3><p>%s</p><dl><div><dt>Messen an</dt><dd>%s</dd></div><div><dt>Grundlage</dt><dd>%s</dd></div></dl></div>
<div class="mpv-varianten">%s</div></article>''' % ("ja" if foto else "nein", "Foto von dir nötig" if foto else "ohne Foto von dir", t, leser, mess, beleg, vs))
    k.append('''<article class="mpv-typ mpv-typ--quer"><div class="mpv-text"><span class="mpf-foto mpf-foto--ja">Handyfoto, kein Porträt</span><h3>Quer: Du als Person</h3>
<p>Eine Analogie aus deinem Leben, die zu einem Thema führt – Lego, Mountainbike, die Fragen deiner Kinder. Meist als Szene, mit einem Foto vom Gegenstand oder Ort, nie von den Kindern. Bewusst wenig Gestaltung, damit es nach Alltag aussieht.</p></div>
<div class="mpv-varianten"><figure><div class="mpv-leer">Dein Foto folgt</div><figcaption><b>A</b> Foto pur</figcaption></figure><figure><div class="mpv-leer">Dein Foto folgt</div><figcaption><b>B</b> Foto mit einem Satz</figcaption></figure></div></article>''')
    return '<div class="mpv">%s</div>' % "".join(k)


def woche():
    z = "".join('<tr><td class="mkf-nr">%s</td><td>%s</td><td>%s</td></tr>' % w for w in WOCHE)
    return '<div class="mkf-tabelle"><table style="min-width:0"><tr><th>Tag</th><th>Postingtyp</th><th>Foto von dir nötig</th></tr>%s</table></div>' % z


MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Postingformate</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Postingformate &middot; Vorschlag zur Entscheidung</p>
      <h1>Worüber du sprichst. Und wie es <span class="hl">aussieht.</span></h1>
      <p class="e2-lead">Zwei Achsen für dein persönliches Profil: sieben Themen aus dem Strategiehandwerk und sieben Postingtypen. Nur zwei Typen brauchen ein Foto – so tragen fünf Postings pro Woche, und es wird nicht eintönig. Jedes Thema kann in jedem Typ erscheinen.</p>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Achse 1</p><h2 class="e2-h2">Die Themen.</h2>
    <p class="e2-lead">Abgeleitet aus dem Dreiklang des Strategiehandwerks – je Baustein zwei Themen, eines quer dazu. Die Herleitung zeigt die Seite <a href="/projekte/medienkonzept-zuordnung.html">Zuordnung</a>.</p></div>
    ''' + themen() + '''
    <p class="mpf-quer"><b>Quer dazu: du als Person.</b> Analogien und Erlebnisse aus deinem Leben würzen jedes Thema – meist als Szene mit Foto. Die Gewichtung der Themen folgt der laufenden Auswertung.</p>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Achse 2</p><h2 class="e2-h2">Die Postingtypen.</h2>
    <p class="e2-lead">Sieben Typen mit je zwei bis drei Varianten. Nur die Szene braucht ein Foto von dir – alles andere entsteht aus Schrift, Gelb, Schwarz und den Icons der Homepage. So wechselt das Bild jeden Tag, und man erkennt dich trotzdem.</p></div>
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
