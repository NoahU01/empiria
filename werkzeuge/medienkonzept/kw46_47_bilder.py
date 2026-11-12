"""Bilder KW 46/47 (09.–22.11.2026), Texte in kw46_47_texte.py. Bildlogik: Geschichte = echtes Foto, Szene ohne Daniel = nachgebauter Bildschirm, Satzkarte höchstens einmal pro Woche."""
LORA = "font:700 %dpx/1.1 Lora,Georgia,serif;letter-spacing:-.015em"


def sektionen(NAME, vb, SYS):
    weiss_name = '<p class="namezeile" style="color:#d9d5cf">Daniel Ströbel</p>'

    def foto(pid, bild, pos, satz, wer="", groesse=88, verlauf="52%"):
        w = '<p class="wer">%s</p>' % wer if wer else ""
        return """<section class="p vollbild" id="%s">%s<div class="verlauf" style="height:%s"></div><div class="unten"><p class="satz" style="font-size:%dpx">%s</p>%s</div></section>""" % (pid, vb(bild, pos), verlauf, groesse, satz, w)

    # 11.11. Folien-Übersicht: eine neue Seite vorn, alles andere im Backup
    daumen = "".join("""<div style="height:112px;border-radius:8px;background:#f3f1ee;border:2px solid #e4e0db;padding:16px 16px 0">
      <i style="display:block;width:%d%%;height:12px;border-radius:6px;background:#cfcac4"></i>
      <i style="display:block;margin-top:12px;width:88%%;height:8px;border-radius:4px;background:#e0dcd6"></i>
      <i style="display:block;margin-top:8px;width:72%%;height:8px;border-radius:4px;background:#e0dcd6"></i>
      <i style="display:block;margin-top:8px;width:80%%;height:8px;border-radius:4px;background:#e0dcd6"></i></div>""" % w for w in [62, 48, 70, 55, 66, 44, 58, 72, 50, 64, 46, 60])
    rp31 = """<section class="p" id="rp31" style="background:#e9e7e3;padding:70px 56px 0">
<div style="border-radius:22px;background:#fff;box-shadow:0 24px 60px rgba(0,0,0,.12);overflow:hidden">
  <div style="display:flex;align-items:center;gap:12px;padding:26px 30px;border-bottom:1px solid #e6e3df">
    <i style="width:16px;height:16px;border-radius:50%%;background:#d9d5cf"></i><i style="width:16px;height:16px;border-radius:50%%;background:#d9d5cf"></i><i style="width:16px;height:16px;border-radius:50%%;background:#d9d5cf"></i>
    <span style="margin-left:18px;font:600 28px/1 %s;color:#4a4642">Vorstandstermin.pptx</span></div>
  <div style="padding:30px 34px 36px">
    <p style="font:600 24px/1 %s;letter-spacing:.06em;text-transform:uppercase;color:#1a1817">Folie 1</p>
    <div style="margin-top:18px;height:330px;border-radius:12px;background:#fff400;padding:34px 40px;position:relative">
      <p style="font:700 54px/1.1 Lora,Georgia,serif;color:#1a1817">Das Gesamtbild</p>
      <svg viewBox="0 0 860 170" style="position:absolute;left:40px;right:40px;bottom:30px;width:calc(100%% - 80px)" fill="none" stroke="#1a1817" stroke-width="5" stroke-linecap="round">
        <rect x="10" y="40" width="200" height="100" rx="14"/><rect x="330" y="10" width="200" height="70" rx="14"/><rect x="330" y="100" width="200" height="60" rx="14"/><rect x="650" y="40" width="200" height="100" rx="14"/>
        <path d="M210 90h120M530 45l120 45M530 130l120-40"/></svg></div>
    <p style="margin-top:34px;font:600 24px/1 %s;letter-spacing:.06em;text-transform:uppercase;color:#8a857f">Backup · 38 Folien</p>
    <div style="margin-top:18px;display:grid;grid-template-columns:repeat(4,1fr);gap:14px;opacity:.75">%s</div>
  </div></div>
<p style="position:absolute;left:56px;right:56px;bottom:150px;%s;color:#1a1817">Der Rest: <span class="hl">Backup.</span></p>%s</section>""" % (SYS, SYS, SYS, daumen, LORA % 84, NAME)

    # 12.11. Zwei Sätze derselben Person
    rp32 = """<section class="p" id="rp32" style="padding:100px 84px 0">
  <p style="font:600 26px/1 Poppins,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#8a857f">Termin 1</p>
  <p style="margin-top:28px;%s;color:#8a857f">„Ich bin Projektleiter, keine Führungskraft.“</p>
  <div style="margin:76px 0 70px;height:4px;background:#1a1817;width:120px"></div>
  <p style="font:600 26px/1 Poppins,sans-serif;letter-spacing:.16em;text-transform:uppercase;color:#1a1817">Termin 4</p>
  <p style="margin-top:28px;%s;color:#1a1817">„In meiner Rolle als <span class="hl">Führungskraft</span> …“</p>
  %s</section>""" % (LORA % 74, LORA % 100, NAME)

    # 15.11. Anruf
    rp34 = """<section class="p" id="rp34" style="background:linear-gradient(180deg,#2c2a28 0%%,#141312 100%%);padding:110px 84px 0;color:#fff;text-align:center">
  <div style="margin:0 auto;width:190px;height:190px;border-radius:50%%;background:#4a4642;display:grid;place-items:center">
    <svg viewBox="0 0 24 24" style="width:110px;height:110px" fill="#8a857f"><circle cx="12" cy="8.5" r="4.5"/><path d="M3.5 21c.8-4.4 4.3-7 8.5-7s7.7 2.6 8.5 7z"/></svg></div>
  <p style="margin-top:40px;font:600 64px/1.1 %s">Vorstand</p>
  <p style="margin-top:16px;font:400 34px/1.2 %s;color:#a8a39c">ruft an …</p>
  <p style="margin-top:110px;%s;color:#f3f1ee">„Daniel, ich brauche dich mal nur ganz kurz.“</p>
  <p style="position:absolute;left:84px;right:84px;bottom:150px;%s;color:#fff">Daraus wurden <span class="hl" style="color:#1a1817">18&nbsp;Monate.</span></p>
  %s</section>""" % (SYS, SYS, LORA % 76, LORA % 96, weiss_name)

    # 16.11. Videokonferenz
    kacheln = "".join("""<div style="position:relative;height:250px;border-radius:16px;background:#2c2a28;%s">
      <span style="position:absolute;left:50%%;top:44%%;transform:translate(-50%%,-50%%);display:grid;place-items:center;width:108px;height:108px;border-radius:50%%;background:%s;font:600 40px/1 %s;color:#fff">%s</span>
      <span style="position:absolute;left:16px;bottom:14px;padding:6px 12px;border-radius:8px;background:rgba(0,0,0,.55);font:500 22px/1 %s;color:#e4e0db">%s</span></div>""" % (
        "outline:5px solid #fff400;outline-offset:-5px" if n == "Du" else "", f, SYS, k, SYS, n) for k, n, f in [
        ("AB", "Bereichsleitung", "#5a5652"), ("CK", "Projektleitung", "#4a4642"), ("FM", "Fachbereich", "#5a5652"),
        ("TS", "IT", "#4a4642"), ("JW", "Controlling", "#5a5652"), ("DS", "Du", "#1a1817")])
    rp35 = """<section class="p" id="rp35" style="background:#1b1a19;padding:70px 56px 0">
  <div style="display:grid;grid-template-columns:repeat(3,1fr);gap:14px">%s</div>
  <p style="margin-top:46px;text-align:center"><span style="display:inline;padding:10px 20px;background:rgba(0,0,0,.8);-webkit-box-decoration-break:clone;box-decoration-break:clone;font:500 44px/1.75 %s;color:#fff">Kann mir einer kurz einordnen, mit welchem Ergebnis wir heute rausgehen wollen?</span></p>
  <p style="position:absolute;left:56px;right:56px;bottom:150px;%s;color:#fff">Und dann: <span class="hl" style="color:#1a1817">Stille.</span></p>
  %s</section>""" % (kacheln, SYS, LORA % 104, weiss_name)

    # 17.11. Zwei Mitteilungen am selben Morgen
    def mitteilung(app, titel, text):
        return """<div style="margin-top:22px;padding:28px 30px;border-radius:34px;background:rgba(243,241,238,.94);text-align:left">
      <p style="display:flex;align-items:center;gap:14px;font:500 24px/1 %s;color:#6b6762"><i style="width:40px;height:40px;border-radius:10px;background:#1a1817"></i>%s<span style="margin-left:auto">jetzt</span></p>
      <p style="margin-top:16px;font:600 34px/1.25 %s;color:#1a1817">%s</p>
      <p style="margin-top:6px;font:400 32px/1.35 %s;color:#3d3a37">%s</p></div>""" % (SYS, app, SYS, titel, SYS, text)
    rp36 = """<section class="p" id="rp36" style="background:linear-gradient(160deg,#3d3a37 0%%,#1a1817 70%%);padding:96px 64px 0;text-align:center;color:#fff">
  <p style="font:500 34px/1 %s;color:#d9d5cf">Dienstag, 17. November</p>
  <p style="margin-top:8px;font:300 170px/1 %s">08:14</p>
  <div style="margin-top:46px">%s%s</div>
  <p style="position:absolute;left:84px;right:84px;bottom:150px;text-align:left;%s;color:#fff">Beides <span class="hl" style="color:#1a1817">am&nbsp;selben&nbsp;Morgen.</span></p>
  %s</section>""" % (SYS, SYS,
        mitteilung("Rundschreiben IT-Sicherheit", "Nutzung von KI-Anwendungen", "Externe KI-Tools dürfen bis auf Weiteres nicht genutzt werden."),
        mitteilung("Vorstandsinformation", "Mut zur Innovation", "Wir erwarten aus allen Bereichen Ideen für KI-Schnellboote. Denkt groß!"),
        LORA % 96, weiss_name)

    # 18.11. Management Summary mit einer Zeile, die zählt
    breiten = [92, 86, 95, 78, None, 90, 83, 94, 71, 88, 92, 64]
    zeilen = "".join('<i style="display:block;margin-top:26px;width:%d%%;height:18px;border-radius:9px;background:#e0dcd6"></i>' % b if b else
                     '<p style="margin-top:22px;font:600 38px/1.3 %s;color:#1a1817"><span style="background:#fff400;padding:2px 10px;border-radius:8px;-webkit-box-decoration-break:clone;box-decoration-break:clone">Ein Satz, der die Richtung vorgibt.</span></p>' % SYS for b in breiten)
    rp37 = """<section class="p" id="rp37" style="background:#e9e7e3;padding:80px 110px 0">
  <div style="height:880px;border-radius:14px;background:#fff;box-shadow:0 24px 60px rgba(0,0,0,.12);padding:62px 64px">
    <p style="font:600 24px/1 %s;letter-spacing:.06em;text-transform:uppercase;color:#8a857f">Vorlage für die Vorstandsklausur</p>
    <p style="margin-top:18px;font:700 50px/1.1 Lora,Georgia,serif;color:#1a1817">Management Summary</p>
    <div style="margin-top:20px">%s</div></div>
  <p style="position:absolute;left:84px;right:84px;bottom:150px;%s;color:#1a1817">Gebraucht wurde <span class="hl">eine Zeile.</span></p>
  %s</section>""" % (SYS, zeilen, LORA % 92, NAME)

    # 21.11. Drei Wochen statt nächstes Jahr
    rp40 = """<section class="p" id="rp40" style="padding:96px 84px 0">
  <div style="display:grid;grid-template-columns:auto 1fr auto;align-items:center;gap:26px">
    <span style="font:600 30px/1.2 Poppins,sans-serif;color:#1a1817">Tag 1<small style="display:block;font:500 24px/1.3 Poppins,sans-serif;color:#6b6762">Termin mit dem Vorstand</small></span>
    <i style="height:4px;background:#1a1817;border-radius:2px"></i>
    <span style="font:600 30px/1.2 Poppins,sans-serif;color:#1a1817;text-align:right">Tag 21<small style="display:block;font:500 24px/1.3 Poppins,sans-serif;color:#6b6762">Landingpage live</small></span></div>
  <div style="margin-top:56px;border-radius:26px;background:#1a1817;overflow:hidden">
    <div style="display:flex;align-items:center;gap:12px;padding:22px 26px">
      <i style="width:16px;height:16px;border-radius:50%%;background:#4a4642"></i><i style="width:16px;height:16px;border-radius:50%%;background:#4a4642"></i><i style="width:16px;height:16px;border-radius:50%%;background:#4a4642"></i>
      <span style="margin-left:18px;flex:1;padding:12px 22px;border-radius:30px;background:#2c2a28;font:500 24px/1 %s;color:#a8a39c">www.ihr-neues-thema.de</span>
      <span style="padding:10px 18px;border-radius:30px;background:#fff400;font:700 22px/1 %s;color:#1a1817">LIVE</span></div>
    <div style="margin:0 14px 14px;border-radius:16px;background:#fff;height:520px;padding:56px 54px">
      <i style="display:block;width:70%%;height:44px;border-radius:10px;background:#1a1817"></i>
      <i style="display:block;margin-top:18px;width:52%%;height:44px;border-radius:10px;background:#1a1817"></i>
      <i style="display:block;margin-top:38px;width:84%%;height:16px;border-radius:8px;background:#e0dcd6"></i>
      <i style="display:block;margin-top:14px;width:76%%;height:16px;border-radius:8px;background:#e0dcd6"></i>
      <i style="display:block;margin-top:14px;width:80%%;height:16px;border-radius:8px;background:#e0dcd6"></i>
      <span style="display:inline-block;margin-top:44px;padding:22px 40px;border-radius:40px;background:#fff400;font:700 28px/1 Poppins,sans-serif;color:#1a1817">Gespräch vereinbaren</span>
      <div style="margin-top:44px;display:grid;grid-template-columns:repeat(3,1fr);gap:18px"><i style="height:70px;border-radius:12px;background:#f3f1ee"></i><i style="height:70px;border-radius:12px;background:#f3f1ee"></i><i style="height:70px;border-radius:12px;background:#f3f1ee"></i></div></div></div>
  <p style="position:absolute;left:84px;right:84px;bottom:150px;%s;color:#1a1817">Nächstes Jahr? <span class="hl">Drei Wochen.</span></p>
  %s</section>""" % (SYS, SYS, LORA % 100, NAME)

    # 22.11. Satzkarte der Woche
    rp41 = """<section class="p schwarz" id="rp41" style="padding:84px">
  <p style="position:absolute;left:84px;right:84px;top:430px;%s;color:#fff">Seit Jahren bekannt.<br><span class="hl" style="color:#1a1817">Seit Jahren geduldet.</span></p>
  %s</section>""" % (LORA % 112, NAME)

    return [
        foto("rp30", "foto-seminar-selfie.jpg", "32% 50%", "„Welches Seminar leiten Sie <span class=\"hl\" style=\"color:#1a1817\">heute?</span>“",
             "", 96),
        rp31, rp32,
        foto("rp33", "foto-skizze.jpg", "50% 35%", "„Hat dein Papa wieder einen <span class=\"hl\" style=\"color:#1a1817\">coolen&nbsp;Trick?</span>“",
             "Die Freundinnen meiner Tochter", 90),
        # Grundform-Prüfung 11.11.2026: echte Fotos statt Grafiken, höchstens eine Grafik pro Woche (rp36)
        foto("rp34", "foto-anzug-fenster.jpg", "50% 30%", "Daraus wurden <span class=\"hl\" style=\"color:#1a1817\">18&nbsp;Monate.</span>", "", 100, "40%"),
        foto("rp35", "foto-videoraum.jpg", "40% 50%", "Und dann: <span class=\"hl\" style=\"color:#1a1817\">Stille.</span>", "", 110, "40%"),
        rp36,
        foto("rp37", "foto-konferenztisch.jpg", "30% 50%", "Ein Satz. <span class=\"hl\" style=\"color:#1a1817\">Die&nbsp;Richtung.</span>", "", 110, "40%"),
        """<section class="p vollbild" id="rp38">%s<div class="verlauf" style="height:14%%"></div>%s</section>""" % (vb("foto-nein.jpg", "12% 50%"), weiss_name),
        foto("rp39", "foto-saal.jpg", "46% 50%", "Die besten fünf Minuten <span class=\"hl\" style=\"color:#1a1817\">hatten&nbsp;keine&nbsp;Folie.</span>", "", 92),
        foto("rp40", "foto-zeigt.jpg", "62% 50%", "Nächstes Jahr? <span class=\"hl\" style=\"color:#1a1817\">Drei&nbsp;Wochen.</span>", "", 110, "40%"),
        # 23.11. Strategisches Kaffeetrinken – Platzhalterfoto, bis Daniel ein Foto mit Kaffeetasse liefert
        foto("rp42", "foto-buero-polo.jpg", "22% 35%", "Entschieden wird <span class=\"hl\" style=\"color:#1a1817\">vor&nbsp;dem&nbsp;Gremium.</span>", "", 96, "40%"),
        # 26.11. Probleme wegnehmen statt machen (Satz eines Bereichsleiters, Daniel 12.11.2026)
        foto("rp43", "foto-brille-buero.jpg", "50% 30%", "Nimmst du Probleme weg – <span class=\"hl\" style=\"color:#1a1817\">oder machst du welche?</span>", "", 92, "45%"),
        foto("rp41", "foto-sw-nachdenklich.jpg", "50% 30%", "Seit Jahren bekannt.<br><span class=\"hl\" style=\"color:#1a1817\">Seit Jahren geduldet.</span>", "", 92, "45%"),
    ]
