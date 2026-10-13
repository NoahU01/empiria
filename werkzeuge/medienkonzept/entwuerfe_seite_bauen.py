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
V = "35"  # Versionsnummer für CSS/JS

# Ergänzungen je Beitrag (Supabase-ID → Darstellung)
EXTRA = {
    25: dict(bild="w2", alt="v1", termin="Di 20.10.", format="Das Werkzeug · B Checkliste Gelb (Alternative: Szene A)",
             offen="Gibt es eine Vorlage, bei der die drei Fragen bei dir oder einem Kunden etwas gedreht haben? Ein Satz dazu macht ihn stärker."),
    26: dict(bild="k2", alt="m3", termin="Mi 21.10.", format="Die Frage · B Schwarz mit Zeichen (Alternative: Modell C)",
             offen="Noch ohne eigene Szene, deshalb eher erklärend. Wo hast du zuletzt erlebt, dass eine Strategie auf der Folie steht und im Alltag nichts ändert?"),
    27: dict(bild="s1", termin="Do 22.10.", format="Die Szene · B Foto mit einem Satz",
             offen="Stimmt die Szene so, und darf das Zitat ohne Namen verwendet werden?"),
    28: dict(bild="v4", termin="Mo 26.10.", format="Die Szene · A Foto pur",
             offen="Noch ohne eigene Szene. In welchem Termin hat die Neugründungs-Frage zuletzt etwas ausgelöst?"),
    29: dict(bild="p5", termin="Di 27.10.", format="Das Werkzeug · A Liste Schwarz",
             offen="Einziger Beitrag mit Türspalt zum Angebot (letzter Absatz). So lassen oder ohne?"),
    30: dict(bild="d1", termin="Mi 28.10.", format="Zum Mitnehmen · Dokument, 6 Seiten (PDF)", pdf="Ein-Thema-vier-Gegenueber.pdf",
             seiten=["d1", "d2", "d3", "d4", "d5", "d6"],
             offen="Passen die vier Gegenüber und die Satzanfänge so? Das Dokument ist fertig gesetzt."),
}
FELDER = {"01 Strategie im Alltag": "01 Strategie im Alltag", "02 Komplexe Themen": "02 Komplexe Themen", "03 Geschäftsmodell": "03 Geschäftsmodell"}


def main(pfad):
    daten = sorted(json.load(open(pfad, encoding="utf-8")), key=lambda e: e["id"])
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
    quelle = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()
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
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Entwürfe</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; LinkedIn Daniel Ströbel</p>
      <h1>Die ersten Postings. Fertig zur <span class="hl">Freigabe.</span></h1>
      <p class="e2-lead">Jedes Posting mit Bild und Text, so wie es auf LinkedIn erscheint. Antippen: Text lesen, kopieren, Bild herunterladen. Freigabe im Chat, je Posting ein „passt“ oder ein Satz, was nicht stimmt.</p>
  </div></section>

  <section class="e2-sek"><div class="e2-wrap">
    <div class="ig">
      <div class="ig-kopf"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><p>Persönliches LinkedIn-Profil · Strategie in Wirkung bringen<br>Start Di 20.10., jeweils 8:30 Uhr über Buffer</p></div></div>
      <div class="ig-filter" id="mke-filter" role="group" aria-label="Nach Themenfeld filtern"></div>
      <div class="ig-raster" id="mke-raster"></div>
      <div class="ig-plan"><span><b>KW 43:</b> Di 20. · Mi 21. · Do 22.10.</span><span><b>Ab KW 44:</b> montags bis freitags, 8:30 Uhr</span><span><b>Ohne Link</b> im Beitrag</span></div>
      <div class="ig-paket"><p><b>Alles auf einmal:</b> Bilder in 1080 × 1350, das Dokument als PDF und alle Texte.</p><a class="e2-knopf" href="/assets/projekte/medienkonzept/postings/Postings-Daniel.zip" download>Paket herunterladen</a></div>
    </div>

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
</div></dialog>'''
    open(os.path.join(SITE, "projekte", "medienkonzept-entwuerfe.html"), "w", encoding="utf-8").write(kopf + main_html + fuss)
    print("Seite, Daten und Paket gebaut:", len(posts), "Postings")


if __name__ == "__main__":
    main(sys.argv[1])
