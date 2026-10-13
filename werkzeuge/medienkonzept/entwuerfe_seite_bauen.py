#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Entwürfe (Aufbau wie AVRG › Social Media: Raster, Großansicht,
Text kopieren, Bild herunterladen) und die Datendatei entwuerfe.js.

    python3 werkzeuge/medienkonzept/entwuerfe_seite_bauen.py beitraege.json
beitraege.json = Export der Supabase-Tabelle beitraege (id, feld, art, kernaussage, text, geplant_am).
"""
import json, os, sys, zipfile

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
MK = os.path.join(SITE, "assets", "projekte", "medienkonzept")
V = "49"  # Versionsnummer für CSS/JS

# Ergänzungen je Beitrag (Supabase-ID → Darstellung)
EXTRA = {
    36: dict(bild="rp01", termin="Di 20.10.", format="Szene · B Foto mit Satz", offen="Passt das Bühnenfoto, oder hast du ein Foto aus einem Strategiegespräch?"),
    37: dict(bild="rp02", termin="Mi 21.10.", format="Modell · A Why · How · Next", offen="Gibt es eine echte Vorlage, die an der Bedeutung gescheitert ist? Ein Satz dazu macht den Einstieg stärker."),
    38: dict(bild="rp03", termin="Do 22.10.", format="Szene · B Foto mit Satz (Porträt)", offen="Den Satz hast du schon einmal gepostet – als Wiederaufnahme in Ordnung?"),
    39: dict(bild="rp04", termin="Mo 19.10.", format="Frage · E Skala", offen=""),
    40: dict(bild="rp05", termin="Fr 16.10.", format="Szene · A Foto pur (Flipchart)", offen="Aus welchem Termin stammt das Flipchart-Foto? Ein Halbsatz zum Anlass macht es zur echten Szene."),
    41: dict(bild="mo5", termin="Mi 14.10.", format="Modell · E Erfolgsmap", offen=""),
    42: dict(bild="rp07", termin="Do 15.10.", format="Szene · F Foto mit Verlauf und Wort", offen=""),
    43: dict(bild="rp08", termin="Fr 23.10.", format="Eingeordnet · B Zahl auf Foto", offen="Zahlen vor dem Posten an der Quelle prüfen (Wieselhuber)."),
}
FELDER = {"01 Strategie im Alltag": "01 Strategie im Alltag", "02 Komplexe Themen": "02 Komplexe Themen", "Branche eingeordnet": "Branche eingeordnet"}

PLAN = [
    ("KW 44", "Mo 26.10.", "30 · Wie würdest du deinen Bereich heute neu gründen?", "Frage · C Fragezeichen"),
    ("KW 44", "Di 27.10.", "12 · Logik allein verändert wenig.", "Szene · A Foto pur"),
    ("KW 44", "Mi 28.10.", "08 · Erst befördern, dann entwickeln ist der größte Fehler.", "Modell · D Drei Kreise"),
    ("KW 44", "Do 29.10.", "10 · Geduldetes Fehlverhalten demotiviert die Guten.", "Szene · B Foto mit Satz"),
    ("KW 44", "Fr 30.10.", "07 · Wie sähe die Homepage deiner Abteilung aus?", "Zum Mitnehmen · Dokument"),
    ("KW 45", "Mo 02.11.", "09 · Neu in der Rolle – überladen mit Regelterminen.", "Skizze · C Isometrisch"),
    ("KW 45", "Di 03.11.", "21 · Diskussionen kippen, sobald die Bedeutung fehlt.", "Szene · D Kritzelei auf Foto"),
    ("KW 45", "Mi 04.11.", "04 · Der Einstieg dauert drei Stunden, keine zwei Tage.", "Werkzeug · D Zeitleiste"),
    ("KW 45", "Do 05.11.", "20 · Themen auf der falschen Flugebene.", "Szene · B Foto mit Satz"),
    ("KW 45", "Fr 06.11.", "34 · AI Act grob eingeordnet.", "Eingeordnet · F Posting im Posting"),
]


def main(pfad):
    daten = sorted(json.load(open(pfad, encoding="utf-8")), key=lambda e: e["geplant_am"])
    posts = []
    for e in daten:
        if "Firmenprofil" in e["kanal"]:
            continue
        x = EXTRA[e["id"]]
        posts.append(dict(id=e["id"], kanal="firma" if "Firmenprofil" in e["kanal"] else "daniel",
                          feld=e["feld"], art=e["art"], kern=e["kernaussage"], text=e["text"], **x))
    open(os.path.join(MK, "entwuerfe.js"), "w", encoding="utf-8").write(
        "/* Medienkonzept empiria – Entwürfe für Daniels LinkedIn-Profil (aus Supabase beitraege, Stand 12.10.2026). */\n"
        "window.MK_ENTWUERFE = " + json.dumps(posts, ensure_ascii=False, indent=1) + ";\n"
        "window.MK_FELDER = " + json.dumps(FELDER, ensure_ascii=False) + ";\n")
    # Paket: alle Bilder, Dokument-PDF und Texte
    md = ["# Postings Daniel Ströbel – LinkedIn (Entwürfe, Stand 12.10.2026)", ""]
    for i, p in enumerate(posts):
        md += ["## %02d · %s · %s · %s" % (i + 1, p["termin"], p["feld"], p["art"]), "", "Bild: %s.jpg · %s" % (p["bild"], p["format"]), "", p["text"], ""]
    with zipfile.ZipFile(os.path.join(MK, "postings", "Postings-Daniel.zip"), "w", zipfile.ZIP_DEFLATED) as z:
        z.writestr("Texte.md", "\n".join(md))
        for p in posts:
            for s in p.get("seiten", [p["bild"]] + ([p["alt"]] if p.get("alt") else [])):
                z.write(os.path.join(MK, "postings", s + ".jpg"), s + ".jpg")
            if p.get("pdf"):
                z.write(os.path.join(MK, "postings", p["pdf"]), p["pdf"])
    # Seite aus der Beitragsarten-Seite ableiten (Kopf, Menü, Fuß bleiben identisch)
    quelle = open(os.path.join(HIER, "seiten-vorlage.html"), encoding="utf-8").read()
    kopf, rest = quelle.split('<main class="ak">', 1)
    fuss = rest.split("</main>", 1)[1]
    kopf = (kopf.replace("<title>Beitragsarten · Medienkonzept – empiria</title>", "<title>Entwürfe · Medienkonzept – empiria</title>")
                .replace('content="Medienkonzept empiria – drei Beispiele für Beiträge von Daniel."',
                         'content="Medienkonzept empiria – die ersten Postings für Daniels LinkedIn-Profil zur Freigabe."')
                .replace("medienkonzept.css?v=1", "medienkonzept.css?v=" + V))
    fuss = fuss.replace('<script src="/script.js"></script>',
                        '<script src="/assets/projekte/medienkonzept/entwuerfe.js?v=%s"></script>\n'
                        '<script src="/assets/projekte/medienkonzept/entwuerfe-seite.js?v=%s"></script>\n'
                        '<script src="/script.js"></script>' % (V, V))
    plan_zeilen = "".join('<tr><td style="white-space:nowrap">%s<br><b>%s</b></td><td>%s<br><span style="color:#6b6661">%s</span></td></tr>' % z for z in PLAN)
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Entwürfe</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; LinkedIn Daniel Ströbel</p>
      <h1>Die ersten Postings. Fertig zur <span class="hl">Freigabe.</span></h1>
      <p class="e2-lead">Redaktionsplan ab Mi 14.10. Die ersten acht Postings sind fertig mit Bild und Text – antippen zum Lesen. Freigabe im Chat: je Posting „passt“ oder ein Satz, was nicht stimmt. Erst nach deiner Freigabe kommt ein Posting in Buffer.</p>
  </div></section>

  <section class="e2-sek"><div class="e2-wrap">
    <div class="ig">
      <div class="ig-kopf"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><p>Persönliches LinkedIn-Profil · Strategie in Wirkung bringen<br>Start Mi 14.10., jeweils 8:30 Uhr über Buffer</p></div></div>
      <div class="ig-filter" id="mke-filter" role="group" aria-label="Nach Themenfeld filtern"></div>
      <div class="ig-raster" id="mke-raster"></div>
      <div class="ig-plan"><span><b>KW 42:</b> Mi 14. · Do 15. · Fr 16.10.</span><span><b>KW 43:</b> Mo 19. bis Fr 23.10.</span><span><b>8:30 Uhr</b> über Buffer · ohne Link</span></div>
      <div class="ig-paket"><p><b>Alles auf einmal:</b> Bilder in 1080 × 1350, das Dokument als PDF und alle Texte.</p><a class="e2-knopf" href="/assets/projekte/medienkonzept/postings/Postings-Daniel.zip" download>Paket herunterladen</a></div>
    </div>

    <div class="mke-plan"><h2 class="e2-h2" style="font-size:clamp(1.6rem,2.6vw,2.2rem);margin-top:3rem">KW 44 und 45 · geplant</h2>
      <div class="mkf-tabelle"><table style="min-width:0"><tr><th>Termin</th><th>Aussage (Themenliste) · Typ und Variante</th></tr>{{PLAN}}</table></div></div>

  </div></section>

</main>

<dialog class="ig-modal" id="mke-modal" aria-label="Posting in Großansicht"><div class="ig-modal__innen">
  <div class="ig-modal__bild mke-bild" id="mke-bild"></div>
  <div class="ig-modal__text">
    <div class="ig-modal__kopf"><img id="mke-avatar" src="/assets/ansprechpartner-daniel.webp" alt=""><span><b id="mke-name">Daniel Ströbel</b><small id="mke-format"></small></span><button type="button" class="ig-zu" id="mke-zu" aria-label="Schließen">×</button></div>
    <div class="ig-kanal mke-variante" id="mke-variante" role="group" aria-label="Bildfassung" hidden><button type="button" data-v="bild" aria-pressed="true">Vorschlag</button><button type="button" data-v="alt" aria-pressed="false">Alternative</button></div>
    <p class="ig-caption" id="mke-text"></p>
    <div class="ig-aktionen"><button type="button" id="mke-kopieren">Text kopieren</button><a id="mke-laden" href="#" download>Bild herunterladen</a><a id="mke-pdf" href="#" download hidden>Dokument (PDF)</a></div>
    <dl class="ig-meta" id="mke-meta"></dl>
    <div class="ig-blaettern"><button type="button" id="mke-zurueck">← Vorheriges</button><button type="button" id="mke-vor">Nächstes →</button></div>
  </div>
</div></dialog>'''.replace("{{PLAN}}", plan_zeilen)
    open(os.path.join(SITE, "projekte", "medienkonzept-entwuerfe.html"), "w", encoding="utf-8").write(kopf + main_html + fuss)
    print("Seite, Daten und Paket gebaut:", len(posts), "Postings")


if __name__ == "__main__":
    main(sys.argv[1])
