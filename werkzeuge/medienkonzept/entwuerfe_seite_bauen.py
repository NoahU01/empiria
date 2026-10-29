#!/usr/bin/env python3
"""Baut die Unterseite Medienkonzept › Entwürfe (Aufbau wie AVRG › Social Media: Raster, Großansicht,
Text kopieren, Bild herunterladen) und die Datendatei entwuerfe.js.

    python3 werkzeuge/medienkonzept/entwuerfe_seite_bauen.py beitraege.json
beitraege.json = Export der Supabase-Tabelle beitraege:
    ~/AlwaysOn/supabase/sql.py -c "select id, art, feld, geplant_am, kanal, kernaussage, text, status, bild, linkedin_url
      from beitraege where kanal not ilike '%Firmenprofil%' and status in ('entwurf','freigegeben','geplant','veroeffentlicht')
      and geplant_am >= '2026-10-14' order by geplant_am" > beitraege.json
Export samt Kennzahlen: ~/AlwaysOn/pruefung/redaktionsplan.py (EXPORT).
Status-Abfolge: entwurf (Zur Freigabe) → freigegeben → geplant (in Buffer) → veroeffentlicht (Archiv, mit linkedin_url).
Raster beginnt mit der laufenden Woche; Seite nach jeder Statusänderung neu bauen und pushen.
"""
import datetime, json, os, sys, zipfile

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
MK = os.path.join(SITE, "assets", "projekte", "medienkonzept")
V = "81"  # Versionsnummer für CSS/JS

# Ergänzungen je Beitrag (Supabase-ID → Darstellung)
EXTRA = {
    36: dict(bild="rp01", termin="Di 20.10.", format="Szene · B Foto mit Satz", offen=""),
    37: dict(bild="rp02", termin="Mi 21.10.", format="Modell · A Why · How · Next", offen=""),
    38: dict(bild="rp03", termin="Do 22.10.", format="Szene · B Foto mit Satz (Porträt)", offen=""),
    39: dict(bild="rp04", termin="Mo 19.10.", format="Frage · E Skala", offen=""),
    40: dict(bild="rp05", termin="Fr 16.10.", format="Szene · A Foto pur (Flipchart)", offen=""),
    41: dict(bild="mo5", termin="Mi 14.10.", format="Modell · E Erfolgsmap", offen=""),
    42: dict(bild="rp07", termin="Do 15.10.", format="Szene · F Foto mit Verlauf und Wort", offen=""),
    66: dict(bild="rp09", termin="Sa 17.10.", format="Weitergedacht · Gelbe Satzkarte mit Kreis", offen=""),
    68: dict(bild="rp11", termin="Sa 24.10.", format="Weitergedacht · Gelbe Satzkarte", offen="Aktuelles Erlebnis – im Text steht „letzte Woche“."),
    67: dict(bild="rp10", termin="So 18.10.", format="Satz · B Anführungszeichen", offen=""),
    43: dict(bild="rp08", termin="Fr 23.10.", format="Eingeordnet · B Zahl auf Foto", offen=""),
    75: dict(bild="rp12", termin="So 25.10.", format="Aufgegriffen · Foto mit Satz", offen="Bezug „gestern“ setzt voraus, dass der 24.10. erscheint. Bitte bestätigen: „Genau das erlebe ich in den Häusern auch nach innen.“"),
    76: dict(bild="rp13", termin="Mo 26.10.", format="Frage · C Fragezeichen", offen=""),
    77: dict(bild="rp14", termin="Di 27.10.", format="Szene · A Foto mit Satz", offen="Bitte prüfen: Stimmt „Ich dachte: Wenn die Logik stimmt, läuft der Rest“ so für dich – und war es die Abteilung Leben (rund 40 Leute, zwei Standorte)?"),
    79: dict(bild="rp15", termin="Mi 28.10.", format="Modell · D Drei Kreise", offen=""),
    80: dict(bild="rp16", termin="Do 29.10.", format="Du als Person · Foto", offen="Foto vom Juni 2025 vor dem Lloyd's Building – im Text so benannt."),
    81: dict(bild="rp17", termin="Fr 30.10.", format="Werkstatt · Foto", offen=""),
    82: dict(bild="rp18", termin="Sa 31.10.", format="Weitergedacht · Foto", offen=""),
    83: dict(bild="rp19", termin="So 01.11.", format="Aufgegriffen · Zitatkarte", offen="Zitat im Original geprüft (VWheute, 21.10.2026)."),
    84: dict(bild="rp27", termin="Mo 02.11.", format="Szene · Postfach-Nachbau", offen=""),
    85: dict(bild="rp21", termin="Di 03.11.", format="Szene · B Foto mit Satz", offen=""),
    86: dict(bild="ka1", termin="Mi 04.11.", format="Werkzeug · Dokument-Karussell (5 Seiten)", offen="", seiten=["ka1", "ka2", "ka3", "ka4", "ka5"], pdf="ka-strategie-drei-gespraeche.pdf"),
    87: dict(bild="rp23", termin="Do 05.11.", format="Geschichte · Foto", offen=""),
    88: dict(bild="rp24", termin="Fr 06.11.", format="Zum Mitnehmen · Gedankenexperiment", offen=""),
    89: dict(bild="rp25", termin="Sa 07.11.", format="Weitergedacht · Foto", offen=""),
    90: dict(bild="rp26", termin="So 08.11.", format="Aufgegriffen · Zitatkarte", offen="Zitat vom April 2026 (im Original geprüft) – kommt in KW 45 eine frische Stimme der Woche, tauschen wir."),
}
FELDER = {"01 Strategie im Alltag": "01 Strategie im Alltag", "02 Komplexe Themen": "02 Komplexe Themen", "Branche eingeordnet": "Branche eingeordnet"}

PLAN = [  # KW 44/45 seit 21.10.2026 vollständig als Entwürfe in Supabase
]


def main(pfad):
    daten = sorted(json.load(open(pfad, encoding="utf-8")), key=lambda e: e["geplant_am"])
    posts = []
    for e in daten:
        if "Firmenprofil" in e["kanal"]:
            continue
        datum = e["geplant_am"][:10]
        x = dict(EXTRA.get(e["id"]) or dict(bild=(e.get("bild") or "").replace(".jpg", ""), format=e["art"], offen=""))
        b = (e.get("bild") or "")
        if b.endswith(".jpg") and " " not in b:   # Bild aus Supabase gilt immer (Daniel, 28.10.2026: Plan zeigte altes Bild)
            x["bild"] = b[:-4]
        x["termin"] = "%s %s." % (["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"][datetime.date.fromisoformat(datum).weekday()], datum[8:10] + "." + datum[5:7])
        x["url"] = e.get("linkedin_url") or ""
        posts.append(dict(id=e["id"], kanal="firma" if "Firmenprofil" in e["kanal"] else "daniel",
                          feld=e["feld"], art=e["art"], kern=e["kernaussage"], text=e["text"],
                          status=e.get("status", "entwurf"), datum=e["geplant_am"][:10], kennzahlen=e.get("kennzahlen") or [], **x))
    # Wochenraster Mo–So (seit 15.10.2026 sieben Tage): fertiges Posting, geplantes Thema oder kein Posting.
    # Eine Woche wandert als ganze Zeile ins Archiv, sobald alle ihre Postings veröffentlicht sind (Daniel, 13.10.2026).
    TAGE = ["Mo", "Di", "Mi", "Do", "Fr", "Sa", "So"]
    nach_datum = {p["datum"]: i for i, p in enumerate(posts)}
    plan = {}
    for kw, tag, aussage, typ in PLAN:
        d, m = tag.split()[1].strip(".").split(".")
        plan["2026-%s-%s" % (m, d)] = dict(aussage=aussage, typ=typ, interview=False)
    heute = datetime.date.today()
    daten_alle = [datetime.date.fromisoformat(k) for k in list(plan) + list(nach_datum)]
    montag = min(daten_alle + [heute]); montag -= datetime.timedelta(days=montag.weekday())
    letzter = max(daten_alle + [heute])
    wochen, archiv = [], []
    while montag <= letzter:
        tage, im_plan = [], False
        for n in range(7):
            d = montag + datetime.timedelta(days=n); k = d.isoformat()
            t = dict(tag="%s %s" % (TAGE[n], d.strftime("%d.%m.")))
            if k in nach_datum:
                t["i"] = nach_datum[k]
                im_plan = im_plan or posts[nach_datum[k]]["status"] != "veroeffentlicht"
            elif k in plan:
                t["plan"] = plan[k]; im_plan = True
            tage.append(t)
        fr = montag + datetime.timedelta(days=6)
        w = dict(kw="KW %d" % montag.isocalendar()[1], spanne="%s–%s" % (montag.strftime("%d.%m."), fr.strftime("%d.%m.")), tage=tage)
        if any("i" in t for t in tage) and not im_plan:
            archiv.insert(0, w)                      # neueste Woche oben
        elif im_plan or montag >= heute - datetime.timedelta(days=heute.weekday()):
            wochen.append(w)
        montag += datetime.timedelta(days=7)
    open(os.path.join(MK, "entwuerfe.js"), "w", encoding="utf-8").write(
        "/* Medienkonzept empiria – Entwürfe für Daniels LinkedIn-Profil (aus Supabase beitraege, Stand 12.10.2026). */\n"
        "window.MK_ENTWUERFE = " + json.dumps(posts, ensure_ascii=False, indent=1) + ";\n"
        "window.MK_FELDER = " + json.dumps(FELDER, ensure_ascii=False) + ";\n"
        "window.MK_WOCHEN = " + json.dumps(wochen, ensure_ascii=False) + ";\n"
        "window.MK_ARCHIV = " + json.dumps(archiv, ensure_ascii=False) + ";\n")
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
    _ = "".join('<tr><td style="white-space:nowrap">%s<br><b>%s</b></td><td>%s<br><span style="color:#6b6661">%s</span></td></tr>' % z for z in PLAN)
    main_html = '''<main class="ak">

  <section class="e2-kopf ak-kopfbereich"><div class="e2-wrap">
      <p class="ak-wo"><a href="/projekte/medienkonzept.html">&#8592; Medienkonzept</a><span aria-hidden="true">&rsaquo;</span><span aria-current="page">Entwürfe</span></p>
      <p class="e2-kicker">Medienkonzept empiria &middot; LinkedIn Daniel Ströbel</p>
      <h1>Der Redaktionsplan. Woche für <span class="hl">Woche.</span></h1>
      <p class="e2-lead">Jede Zeile ist eine Woche, Montag bis Sonntag – jeden Tag um 7:45 Uhr über Buffer. Bild antippen zum Lesen. Gelb heißt: wartet auf deine Freigabe – „passt“ oder ein Satz, was nicht stimmt. Freigegebene Postings plane ich in Buffer ein und prüfe, ob sie erschienen sind. Ist eine Woche komplett veröffentlicht, wandert sie ins Archiv unten.</p>
  </div></section>

  <section class="e2-sek"><div class="e2-wrap">
    <div class="ig">
      <div class="ig-kopf"><img src="/assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><p>Persönliches LinkedIn-Profil · Strategie in Wirkung bringen<br>jeden Tag 7:45 Uhr über Buffer · ohne Link</p></div></div>
      <div class="mke-legende"><span class="mke-status mke-status--offen">Zur Freigabe</span><span class="mke-status mke-status--frei">Freigegeben</span><span class="mke-status mke-status--buffer">In Buffer</span><span class="mke-status mke-status--archiv">Veröffentlicht</span><span class="mke-status mke-status--plan">Zu schreiben</span><span class="mke-status mke-status--plan">Interview mit dir</span></div>
      <div class="mke-wochen" id="mke-raster"></div>
      <section class="mke-archiv" id="archiv"><h2 class="mke-archiv__kopf">Archiv · veröffentlicht</h2><div id="mke-archiv"></div></section>
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
