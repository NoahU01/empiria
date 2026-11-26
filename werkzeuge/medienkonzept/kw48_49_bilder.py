"""Bilder KW 48/49 (23.11.–06.12.2026), Texte in Supabase beitraege 145–157 (aus dem Kurzinterview KW 46, Ticket 273).
Bildlogik wie KW 46/47: echte Fotos aus „02 Bilder“, höchstens eine Satzkarte pro Woche (24.11. und 06.12.),
Text im Bild nie gleich dem ersten Satz des Beitrags."""
LORA = "font:700 %dpx/1.1 Lora,Georgia,serif;letter-spacing:-.015em"


def sektionen(NAME, vb, SYS):
    weiss_name = '<p class="namezeile" style="color:#d9d5cf">Daniel Ströbel</p>'

    def pur(pid, bild, pos, sw=False):
        return '<section class="p vollbild" id="%s">%s<div class="verlauf" style="height:14%%"></div>%s</section>' % (pid, vb(bild, pos, sw), weiss_name)

    def wort(pid, bild, pos, wort_):
        # Foto mit Verlauf und einem Wort unten
        return """<section class="p vollbild" id="%s">%s<div class="verlauf" style="height:40%%"></div><div class="unten"><p class="satz" style="font-size:112px">%s</p></div></section>""" % (pid, vb(bild, pos), wort_)

    def uhr(pid, bild, pos, chip):
        return '<section class="p vollbild" id="%s">%s<span class="chip">%s</span><div class="verlauf" style="height:14%%"></div>%s</section>' % (pid, vb(bild, pos), chip, weiss_name)

    def kritzel(pid, bild, pos, text, links=520, oben=150, breite=500, durchgestrichen=False, groesse=92):
        strich = ('<svg viewBox="0 0 1080 1350" style="position:absolute;inset:0" fill="none" stroke="#e8261c" stroke-width="9" stroke-linecap="round">'
                  '<path d="M%d %d C %d %d, %d %d, %d %d"/></svg>' % (links - 20, oben + 70, links + 160, oben + 40, links + 330, oben + 80, links + breite - 30, oben + 50)) if durchgestrichen else ""
        return """<section class="p vollbild" id="%s">%s
  <p style="position:absolute;left:%dpx;top:%dpx;width:%dpx;transform:rotate(-4deg);font:700 %dpx/1.02 Caveat,cursive;color:#1a1817">%s</p>%s
</section>""" % (pid, vb(bild, pos), links, oben, breite, groesse, text, strich)

    def satz_oben(pid, bild, pos, satz):
        return """<section class="p vollbild" id="%s">%s<div style="position:absolute;inset:0 0 auto 0;height:46%%;background:linear-gradient(180deg,rgba(26,24,23,.82),rgba(26,24,23,0))"></div>
  <p style="position:absolute;left:80px;right:80px;top:60px;font:700 58px/1.12 Poppins,sans-serif;letter-spacing:-.01em;color:#fff">%s</p></section>""" % (pid, vb(bild, pos), satz)

    def satz_unten(pid, bild, pos, satz):
        # Foto mit einem Satz unten, ohne Markierung (Daniel 20.11.2026: weiße Satzkarte „sieht nach nichts aus“)
        return """<section class="p vollbild" id="%s">%s<div class="verlauf" style="height:42%%"></div><div class="unten"><p class="satz" style="font-size:66px">%s</p></div></section>""" % (pid, vb(bild, pos), satz)

    def frage_gross(pid, bild, pos, satz):
        # große Frage in Poppins unten auf dunklem Verlauf, ohne Markierung (Daniel 22.11.2026: stärker als Handschrift)
        return """<section class="p vollbild" id="%s">%s<div class="verlauf" style="height:50%%"></div>
  <p style="position:absolute;left:72px;right:72px;bottom:96px;font:800 84px/1.06 Poppins,sans-serif;letter-spacing:-.02em;color:#fff">%s</p></section>""" % (pid, vb(bild, pos), satz)

    def satzkarte(pid, satz, groesse=104):
        # Satzkarte der Woche: Schwarz auf Weiß, ohne Markierung
        return """<section class="p" id="%s" style="padding:84px;background:#fff">
  <p style="position:absolute;left:84px;right:84px;top:420px;%s;color:#1a1817">%s</p>
  %s</section>""" % (pid, LORA % groesse, satz, NAME)

    return [
        satz_unten("rp44", "foto-seminarraum-hemd.jpg", "20% 50%", "Manchmal sind 70 Prozent genau richtig."),  # 24.11. neues Thema (Daniel 20.11.2026: Strategieberater-Thema raus)
        uhr("rp45", "foto-fenster-anzug.jpg", "40% 40%", "Tag 1 nach dem Strategiebeschluss"),  # Daniel 22.11.2026: „Danach.“ sinnbefreit                        # 25.11. (146) Strategie in der Schublade
        frage_gross("rp46", "foto-vorschlaghammer.jpg", "50% 30%", "Wie fahren wir unsere Strategie bewusst gegen die Wand?"),  # 26.11. (147) Daniel 26.11.2026: Text dreht sich um Strategie, nicht Projekt; Daniel 22.11.2026: Foto mit kaputtem Vorschlaghammer
        pur("rp47", "foto-buero-flagge.jpg", "75% 40%"),  # foto-schreiben lief schon am 27.10.                         # 27.11. (148) drei Abende
        pur("rp48", "foto-sw-hoodie.jpg", "50% 30%"),                                        # 28.11. (149) bis Daniels Foto der gelben E-Gitarre kommt
        satz_oben("rp49", "foto-gold.jpg", "50% 30%", "Regeln biegen,<br>ohne sie zu brechen."),  # 29.11. (150) Monopoly – Porträt statt Spielbrett
        wort("rp50", "foto-arena.jpg", "40% 50%", "Vollgas."),                               # 30.11. (151) Mannschaft, die gewinnt
        kritzel("rp51", "foto-konferenz-lang.jpg", "35% 50%", "Kickoff", 580, 220, 420, True, 120),  # 01.12. (152) gestrichener Kickoff
        pur("rp52", "foto-unterwegs-laptop.jpg", "45% 50%"),                                 # 02.12. (153) Entwurf zum Anfassen
        pur("rp53", "foto-praesentation.jpg", "35% 50%"),                                    # 03.12. (154) „sehr anstrengend“ – Satz bleibt im Text
        uhr("rp54", "foto-tagungsort.jpg", "45% 50%", "Mittwoch, 14:21 · nach der Mittagspause"),  # 04.12. (155) echte Aufnahmezeit
        pur("rp55", "foto-buero-stehend.jpg", "55% 50%"),                                    # 05.12. (156) Selbstständigkeit
        satzkarte("rp56", "„Da geht mir das Herz auf.“", 112),                              # 06.12. (157)
    ]
