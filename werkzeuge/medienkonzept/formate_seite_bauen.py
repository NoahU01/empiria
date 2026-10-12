#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Formate: Matrix aus Inhalten und Darstellungen,
Daniels persönliches Profil, Beispiele mit echten Bildern.

    python3 werkzeuge/medienkonzept/formate_seite_bauen.py
"""
import os

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
PF = "/assets/projekte/medienkonzept/postings/"
V = "8"

FELDER = ["Richtung", "Durchsetzung", "Zukunft", "Umsetzungspower"]

# Darstellungen: Name, Kanal, wirkt wie, Anteil, Beispiele je Themenfeld (Text, vorhanden?)
DARST = [
    ("Echtes Foto, vollflächig", "daniel", "Du, mittendrin", "ca. 40 %",
     {"Richtung": ("02 Strategie im Alltag", True), "Durchsetzung": ("01 Drei Fragen vor der Vorlage", True), "Zukunft": ("04 Die Neugründungs-Frage", True), "Umsetzungspower": ("Vorbereitung einer Klausur, Blick hinter die Kulissen", False)}),
    ("Flipchart oder Skizze, abfotografiert", "daniel", "Deine Arbeit", "ca. 20 %",
     {"Richtung": ("Die Prüffrage für jede Vision als Skizze", False), "Durchsetzung": ("„What’s in for me?“ am Flipchart", False), "Zukunft": ("Wertschöpfungskette neu gezeichnet", False), "Umsetzungspower": ("Wer? Bis wann? In welcher Form? – Foto vom Flipchart", False)}),
    ("Nur Text", "daniel", "Ein persönlicher Gedanke", "ca. 10 %",
     {"Umsetzungspower": ("03 Die iPad-Geschichte", True), "Durchsetzung": ("„Sie schicken mir wirklich kein Angebot?“", False)}),
    ("Dokument zum Durchblättern", "daniel", "Etwas zum Mitnehmen", "ca. 20 %",
     {"Durchsetzung": ("06 Ein Thema. Vier Gegenüber.", True), "Richtung": ("Die Prüffrage für jede Vision in fünf Schritten", False), "Zukunft": ("Die Neugründungs-Frage als Arbeitsblatt", False)}),
]
KANAL = {"daniel": "Daniel", "firma": "empiria", "beide": "Daniel · empiria teilt"}

# Beispiele mit Bild: Bild, Titel, Kanal, Satz
BEISPIELE = [
    ("v1.jpg", "Echtes Foto, vollflächig", "daniel", "Kein Text im Bild. Der Beitragstext trägt die Aussage, das Foto zeigt den Menschen."),
    ("b1.jpg", "Flipchart oder Skizze", "daniel", "Was du im Termin zeichnest, abfotografiert. Dein Erkennungszeichen."),
    (None, "Nur Text", "daniel", "Für eine starke Geschichte reicht der erste Satz. Kein Bild lenkt ab."),
    ("d1.jpg", "Dokument, 6 Seiten", "daniel", "Das Großzügige: eine Methode vollständig. Gestaltung wird hier erwartet."),
]

ERSTE = [
    ("01", "Echtes Foto statt gestalteter Karte"),
    ("02", "Echtes Foto statt gestalteter Karte"),
    ("03", "Nur Text oder Porträt vollflächig"),
    ("04", "Echtes Foto statt gestalteter Karte"),
    ("05", "Foto deines Flipcharts mit den drei Fragen"),
    ("06", "Dokument bleibt"),
]


def badge(k):
    return '<span class="mkf-kanal mkf-kanal--%s">%s</span>' % (k, KANAL[k])


def matrix():
    kopf = "<tr><th>Darstellung</th>%s<th>Anteil</th></tr>" % "".join("<th>%s</th>" % f for f in FELDER)
    zeilen = []
    for name, k, wirkt, anteil, bsp in DARST:
        zellen = []
        for f in FELDER:
            if f in bsp:
                t, da = bsp[f]
                zellen.append('<td class="%s">%s</td>' % ("mkf-da" if da else "mkf-idee", t))
            else:
                zellen.append('<td class="mkf-leer">–</td>')
        zeilen.append('<tr><th scope="row"><b>%s</b><small>%s</small></th>%s<td>%s</td></tr>' % (name, wirkt, "".join(zellen), anteil))
    return '<div class="mkf-tabelle"><table>%s%s</table></div>' % (kopf, "".join(zeilen))


def beispiele():
    karten = []
    for bild, titel, k, satz in BEISPIELE:
        if bild:
            b = '<img src="%s%s" alt="" loading="lazy">' % (PF, bild)
        else:
            b = ('<div class="mkf-nurtext"><div class="mkb-kopf"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><small>Geschäftsführer empiria</small></div></div>'
                 '<p>Ein befreundeter Vorstand hat einem Kollegen einmal beschrieben, wie ich arbeite:</p><p>„Er stellt Fragen, zeichnet, dreht das iPad um und sagt: Eigentlich ist es doch so.“</p><p class="mkf-mehr">… mehr</p></div>')
        karten.append('<figure class="mkf-bsp"><div class="mkf-bsp__bild">%s</div><figcaption><b>%s</b><span>%s</span></figcaption></figure>' % (b, titel, satz))
    return '<div class="mkf-raster">%s</div>' % "".join(karten)


def erste():
    z = "".join('<tr><td class="mkf-nr">%s</td><td>%s</td></tr>' % e for e in ERSTE)
    return '<div class="mkf-tabelle"><table style="min-width:0"><tr><th>Posting</th><th>Vorschlag</th></tr>%s</table></div>' % z


MAIN = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Formate</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; Formate</p>
      <h1>Themen und <span class="hl">Darstellungen.</span></h1>
      <p class="e2-lead">Daniels persönliches Profil: Themenfelder und Darstellungen. Diskussionsstand vom 12.10. – die Postingarten sind noch nicht festgelegt.</p>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Die Matrix</p><h2 class="e2-h2">Worüber wir sprechen, und wie es aussieht.</h2>
    <p class="e2-lead">Waagerecht die Themenfelder aus der Positionierung, senkrecht die Darstellungen. Schwarz gesetzt: gibt es schon als Entwurf. Grau: nächste Ideen.</p></div>
    ''' + matrix() + '''
    <p class="mkf-hinweis">Später dazu: kurzes Video, 30 bis 60 Sekunden, direkt in die Kamera – die persönlichste Form. Einordnungen von Branchennachrichten laufen quer über alle Themenfelder.</p>
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Die Darstellungen</p><h2 class="e2-h2">So sieht jede aus.</h2>
    <p class="e2-lead">Mit deinen Fotos, so wie sie im Feed erscheinen.</p></div>
    ''' + beispiele() + '''
  </div></section>

  <section class="e2-sek e2-sek--hell ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Für die ersten Postings</p><h2 class="e2-h2">Was das konkret heißt.</h2>
    <p class="e2-lead">Auf der Seite Entwürfe stehen bei 01, 02 und 04 beide Bildfassungen zum Vergleich.</p></div>
    ''' + erste() + '''
    <p class="mkf-knopf"><a class="e2-knopf" href="/projekte/medienkonzept-entwuerfe.html">Zu den Entwürfen &rarr;</a></p>
  </div></section>

  <section class="e2-sek ak-sec"><div class="e2-wrap">
    <div class="ak-kopf"><p class="e2-kicker">Messen</p><h2 class="e2-h2">Deine Zahlen entscheiden.</h2>
    <p class="e2-lead">Jedes Posting trägt drei Merkmale: Themenfeld, Darstellung und Kanal. Die monatliche Auswertung vergleicht, welche Darstellung zu Profilbesuchen, Kommentaren und Gesprächen führt. Was trägt, bauen wir aus, was nicht trägt, fliegt raus.</p></div>
  </div></section>

</main>'''


def main():
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Formate · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – Inhalte und Darstellungen für Daniels persönliches Profil."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    open(os.path.join(SITE, "projekte", "medienkonzept-formate.html"), "w", encoding="utf-8").write(kopf + MAIN + fuss)
    print("Formate-Seite gebaut")


if __name__ == "__main__":
    main()
