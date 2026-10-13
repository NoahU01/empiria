#!/usr/bin/env python3
"""Baut postings-vorlage.html – die Vorlage für Daniels Posting-Bilder (1080 × 1350).

Maßstab: Homepage 2.0 und Volksfest-Seite – große Lora-Headline, ein Wort im gelben Block,
Kicker mit Strich, Markenzeichen »» (Richtung) ✕ (Durchsetzung) ○ (Zukunft), Karten abgerundet,
Flächen Weiß, Gelb, Schwarz. Nie Weiß auf Gelb oder Gelb auf Weiß.

    python3 werkzeuge/medienkonzept/postings_vorlage_bauen.py
    python3 werkzeuge/medienkonzept/postings_rendern.py
"""
import os, re

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
B = "/assets/projekte/medienkonzept/"

# Markenzeichen aus dem Symbol-Satz der Seiten
_sprite = open(os.path.join(SITE, "projekte", "medienkonzept-beitragsarten.html"), encoding="utf-8").read()


def zeichen_svg(name):
    m = re.search(r'<symbol id="ic-%s" viewBox="([^"]+)">(.*?)</symbol>' % name, _sprite, re.S)
    return '<svg viewBox="%s" aria-hidden="true">%s</svg>' % (m.group(1), m.group(2).strip())


F, X, O = zeichen_svg("forward"), zeichen_svg("kreuz"), zeichen_svg("kreis")

CSS = """
:root { --ink:#1a1817; --ink2:#3d3a37; --gelb:#fff400; --grau:#6b6762; --hell:#f3f1ee; --linie:#e4e0db; }
* { box-sizing:border-box; margin:0; padding:0; }
html, body { width:1080px; background:#fff; }
.p { display:none; position:relative; width:1080px; height:1350px; overflow:hidden; font-family:"Poppins",sans-serif; color:var(--ink); background:#fff; padding:84px 84px 0; }
.p:target { display:block; }
@media print { @page { size:1080px 1350px; margin:0; } body.druck .p { display:block; break-after:page; } }
.k { display:flex; align-items:center; gap:18px; font:600 24px/1.2 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; }
.k::before { content:""; width:44px; height:3px; background:currentColor; }
.h { font:700 96px/1.06 "Lora",Georgia,serif; letter-spacing:-.015em; margin-top:34px; }
.h.m { font-size:84px; }
.hl { background:var(--gelb); border-radius:18px; padding:0 .14em; margin:0 -.04em; -webkit-box-decoration-break:clone; box-decoration-break:clone; }
.text { margin-top:30px; font:400 34px/1.5 "Poppins",sans-serif; color:var(--ink2); max-width:860px; }
.fuss { position:absolute; left:84px; right:84px; bottom:70px; display:flex; justify-content:space-between; align-items:center; font:500 24px/1 "Poppins",sans-serif; color:var(--grau); }
.fuss > img { height:34px; display:block; }
.zeichen { position:absolute; color:var(--ink); }
.zeichen svg { width:100%; height:100%; display:block; }
.karte { height:600px; border-radius:28px; overflow:hidden; margin-bottom:58px; }
.karte img { width:100%; height:100%; object-fit:cover; object-position:var(--pos,50% 50%); display:block; }
.sw img { filter:grayscale(1) contrast(1.06); }
.gelbgrund { background:var(--gelb); }
.rund { width:300px; height:300px; border-radius:50%; overflow:hidden; border:8px solid var(--ink); }
.rund img { width:100%; height:100%; object-fit:cover; object-position:50% 30%; filter:grayscale(1) contrast(1.06); display:block; }
.zitat { margin-top:72px; font:700 80px/1.13 "Lora",Georgia,serif; letter-spacing:-.01em; }
.quelle { margin-top:40px; font:500 30px/1.4 "Poppins",sans-serif; }
.schwarz { background:var(--ink); color:#fff; }
.schwarz .k { color:var(--gelb); }
.schwarz .fuss { color:#a8a39c; }
.liste { margin-top:70px; }
.liste div { display:flex; align-items:baseline; gap:40px; padding:34px 0; border-top:2px solid #3a3734; font:700 88px/1 "Lora",Georgia,serif; }
.liste div:last-child { border-bottom:2px solid #3a3734; }
.liste small { font:600 26px/1 "Poppins",sans-serif; color:#a8a39c; width:44px; }
.nr { font:700 30px/1 "Lora",Georgia,serif; color:#b5b0a9; }
.seitenkopf { display:flex; justify-content:space-between; align-items:center; }
.frage { margin-top:40px; background:var(--ink); color:#fff; border-radius:28px; padding:52px 150px 58px 56px; position:relative; }
.frage small { display:block; font:600 22px/1 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--gelb); margin-bottom:24px; }
.frage p { font:700 58px/1.16 "Lora",Georgia,serif; }
.frage .zeichen { right:48px; top:44px; width:64px; height:64px; color:var(--gelb); }
.block { margin-top:50px; }
.block > small { display:block; font:600 22px/1 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--grau); margin-bottom:16px; }
.block li { list-style:none; padding:18px 0; border-top:2px solid var(--linie); font:400 34px/1.4 "Poppins",sans-serif; }
.block li:last-child { border-bottom:2px solid var(--linie); }
.oeffnen { background:var(--hell); border-radius:24px; padding:36px 42px; font:500 34px/1.5 "Poppins",sans-serif; }
.check li { list-style:none; display:flex; gap:32px; align-items:flex-start; padding:30px 0; border-top:3px solid var(--ink); font:600 34px/1.3 "Poppins",sans-serif; }
.check li:last-child { border-bottom:3px solid var(--ink); }
.check li::before { content:""; flex:0 0 46px; height:46px; border:4px solid var(--ink); border-radius:10px; margin-top:2px; }
.autor { display:flex; align-items:center; gap:22px; }
.autor .rund { width:96px; height:96px; border-width:4px; }
.autor .rund img { object-position:25% 15%; }
.autor b { display:block; color:var(--ink); font-weight:600; margin-bottom:8px; }

/* Serien-Beispiele (12.10.2026): Foto vollflächig mit einem Satz, ohne Rahmen und Logo */
.vollbild { padding:0; }
.vollbild > img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:var(--pos,50% 50%); }
.vollbild .verlauf { position:absolute; inset:auto 0 0 0; height:62%; background:linear-gradient(180deg, rgba(26,24,23,0) 0%, rgba(26,24,23,.82) 55%, rgba(26,24,23,.92) 100%); }
.vollbild .unten { position:absolute; left:80px; right:80px; bottom:86px; color:#fff; }
.vollbild .satz { font:700 66px/1.14 "Lora",Georgia,serif; letter-spacing:-.01em; }
.vollbild .wer { margin-top:30px; font:500 28px/1.4 "Poppins",sans-serif; color:#d9d5cf; }
.vollbild .zahl { font:700 230px/.9 "Lora",Georgia,serif; color:var(--gelb); letter-spacing:-.02em; }
.vollbild .oben { position:absolute; left:80px; top:76px; color:#fff; }
.vollbild .oben.k::before { background:#fff; }

/* Postingtypen ohne Foto (13.10.2026): Frage, Modell, Zahl, Satz */
.karte-frage { padding:96px 88px; }
.karte-frage .h { font-size:96px; line-height:1.16; margin-top:70px; }
.namezeile { position:absolute; left:88px; right:88px; bottom:72px; font:500 24px/1 "Poppins",sans-serif; color:var(--grau); }
.schwarz .namezeile { color:#a8a39c; }
.modell { margin-top:64px; display:grid; gap:22px; }
.modell .stufe { display:grid; grid-template-columns:200px 1fr; gap:28px; align-items:start; padding:44px 40px; border-radius:24px; background:var(--hell); }
.modell .stufe b { font:700 64px/1 "Lora",Georgia,serif; }
.modell .stufe p { font:500 34px/1.35 "Poppins",sans-serif; color:var(--ink2); }
.modell .stufe small { display:block; margin-top:10px; font:500 24px/1.4 "Poppins",sans-serif; color:var(--grau); }
.modell .stufe.gelb-b { background:var(--gelb); }
.modell .stufe.gelb-b p, .modell .stufe.gelb-b small { color:var(--ink); }
.zahlkarte .zahl { margin-top:110px; font:700 300px/.9 "Lora",Georgia,serif; color:var(--gelb); letter-spacing:-.03em; }
.zahlkarte .satz { margin-top:40px; font:700 64px/1.15 "Lora",Georgia,serif; color:#fff; }
.zahlkarte .quelle2 { margin-top:34px; font:500 26px/1.4 "Poppins",sans-serif; color:#a8a39c; }
.satzkarte .zitat { margin-top:210px; font:700 104px/1.1 "Lora",Georgia,serif; }
.satzkarte .quelle { margin-top:44px; }
"""


def fuss(links="Daniel Ströbel", weiss=False, seite=""):
    logo = "/assets/empiria-logo-weiss.svg" if weiss else "/assets/empiria-logo.svg"
    rechts = '<span>%s</span>' % seite if seite else '<img src="%s" alt="empiria">' % logo
    return '<div class="fuss"><span>%s</span>%s</div>' % (links, rechts)


def zeichen(svg, right=None, top=None, size=None):
    stil = ' style="right:%dpx;top:%dpx;width:%dpx;height:%dpx"' % (right, top, size, size) if size else ""
    return '<div class="zeichen"%s>%s</div>' % (stil, svg)


def foto_posting(pid, bild, pos, kicker, headline, sym, sw=False, links="Daniel Ströbel"):
    return """<section class="p" id="%s">
  <div class="karte%s" style="--pos:%s"><img src="%s%s" alt=""></div>
  <p class="k">%s</p>
  <p class="h m">%s</p>
  %s
  %s
</section>""" % (pid, " sw" if sw else "", pos, B, bild, kicker, headline, zeichen(sym, 84, 720, 92), fuss(links))


def doc_seite(nr, titel, frage, einwaende, eroeffnung):
    lis = "".join("<li>%s</li>" % e for e in einwaende)
    return """<section class="p" id="d%d">
  <div class="seitenkopf"><p class="k">%s</p><span class="nr">0%d / 04</span></div>
  <div class="frage"><small>Die Frage</small><p>%s</p>%s</div>
  <div class="block"><small>Typische Einwände</small><ul>%s</ul></div>
  <div class="block"><small>So eröffnest du</small><p class="oeffnen">%s</p></div>
  %s
</section>""" % (nr + 1, titel, nr, frage, zeichen(X), lis, eroeffnung, fuss("Ein Thema. Vier Gegenüber.", seite="%d / 6" % (nr + 1)))


teile = [
    foto_posting("p1", "entwurf-e1.jpg", "50% 38%", "Vor jeder Vorstandsvorlage",
                 'Erst drei Fragen, dann die <span class="hl">Folie.</span>', X, sw=True),
    foto_posting("p2", "entwurf-e2.jpg", "35% 40%", "Strategie im Alltag",
                 'Was entscheidest du diese Woche <span class="hl">anders?</span>', F),
    """<section class="p gelbgrund" id="p3">
  <div class="rund" style="margin-top:60px"><img src="%sentwurf-e3.jpg" alt=""></div>
  <p class="zitat">„Er stellt Fragen, zeichnet, dreht das iPad um und sagt: Eigentlich ist es doch so.“</p>
  <p class="quelle">Ein befreundeter Vorstand über meine Arbeit</p>
  %s
</section>""" % (B, fuss().replace('<div class="fuss">', '<div class="fuss" style="color:#1a1817">')),
    foto_posting("p4", "entwurf-e4.jpg", "30% 75%", "Die Neugründungs-Frage",
                 'Was würdest du heute nicht mehr <span class="hl">machen?</span>', O),
    """<section class="p schwarz" id="p5">
  <p class="k">Am Ende jeder Abstimmung</p>
  <div class="liste"><div><small>01</small>Wer?</div><div><small>02</small>Bis wann?</div><div><small>03</small>In welcher Form?</div></div>
  <p class="text" style="color:#d9d5cf;margin-top:56px">Zwei Minuten, damit das Thema beim nächsten Termin eine Stufe weiter ist.</p>
  %s
</section>""" % fuss(weiss=True),
    """<section class="p" id="d1">
  <p class="k">Dokument · 6 Seiten</p>
  <p class="h" style="font-size:118px;margin-top:60px">Ein Thema.<br>Vier <span class="hl">Gegenüber.</span></p>
  <p class="text">Was Vorstand, Aufsichtsrat, Vertrieb und dein Team von dir wissen wollen – und wie du das Gespräch eröffnest.</p>
  %s
  <div class="fuss"><span class="autor"><span class="rund"><img src="%sentwurf-e6.jpg" alt=""></span><span><b>Daniel Ströbel</b>Strategie in Wirkung bringen</span></span><img src="/assets/empiria-logo.svg" alt="empiria"></div>
</section>""" % (zeichen(X, 84, 860, 230), B),
    doc_seite(1, "Der Vorstand", "Welche Entscheidung brauchst du von mir, und was riskiere ich damit?",
              ["„Warum gerade jetzt?“", "„Was passiert, wenn wir es lassen?“"],
              "„Ich brauche heute eine Entscheidung zu einer Frage. Meine Empfehlung ist …, das Risiko begrenzen wir auf …“"),
    doc_seite(2, "Der Aufsichtsrat", "Passt das zu unserer Strategie, und bleibt es steuerbar?",
              ["„Woran messen wir, ob es wirkt?“", "„Wer trägt die Verantwortung?“"],
              "„Das Vorhaben zahlt auf unsere Stoßrichtung … ein. Verantwortlich ist …, berichtet wird quartalsweise an drei Kennzahlen.“"),
    doc_seite(3, "Der Vertrieb", "Was habe ich davon, und wie erkläre ich es meinem Kunden in einem Satz?",
              ["„Noch ein Thema mehr.“", "„Das versteht mein Kunde nicht.“"],
              "„Ab … hast du im Kundengespräch ein Argument mehr, und es passt in einen Satz: …“"),
    doc_seite(4, "Dein Team", "Was ändert sich ab Montag für mich?",
              ["„Wann sollen wir das auch noch machen?“", "„Das hatten wir doch schon mal.“"],
              "„Ab Montag ändert sich für euch genau eine Sache: … Dafür fällt … weg.“"),
    """<section class="p gelbgrund" id="d6">
  <p class="k">Vor deiner nächsten Vorlage</p>
  <p class="h m">Hast du alle vier Fragen beantwortet?</p>
  <ul class="check" style="margin-top:64px"><li>Welche Entscheidung brauche ich vom Vorstand?</li><li>Wie bleibt es für den Aufsichtsrat steuerbar?</li><li>Welchen Satz sagt der Vertrieb seinem Kunden?</li><li>Was ändert sich für mein Team ab Montag?</li></ul>
  <div class="fuss" style="color:#1a1817"><span>Daniel Ströbel · Strategie in Wirkung bringen</span><span>6 / 6</span></div>
</section>""",
]


# Serien-Beispiele für die Strategie-Seite
teile += [
    """<section class="p vollbild" id="s1">
  <img src="%sentwurf-e3.jpg" alt="" style="filter:grayscale(1) contrast(1.06);--pos:50%% 20%%">
  <div class="verlauf"></div>
  <div class="unten"><p class="satz">„Er stellt Fragen, zeichnet, dreht das iPad um und sagt: Eigentlich ist es doch so.“</p><p class="wer">— ein befreundeter Vorstand über meine Arbeit</p></div>
</section>""" % B,
    """<section class="p vollbild" id="n1">
  <img src="%sentwurf-e6.jpg" alt="" style="--pos:30%% 30%%">
  <div class="verlauf" style="height:72%%"></div>
  <p class="k oben">Eingeordnet</p>
  <div class="unten"><p class="zahl">77 %%</p><p class="satz" style="margin-top:18px">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p><p class="wer">Quelle: Wieselhuber · Was das für deinen Bereich heißt, im Text</p></div>
</section>""" % B,
]

# Postingtypen ohne Foto (13.10.2026) – Inhalte aus dem Interview
teile += [
    """<section class="p karte-frage" id="k1">
  <p class="k">Die Frage</p>
  <p class="h">Kann jeder in deinem Bereich sagen, wie ihr <span class="hl">erfolgreich</span> seid?</p>
  <p class="text" style="margin-top:44px">Und was sein eigener Beitrag dazu ist.</p>
  %s
  <p class="namezeile">Daniel Ströbel</p>
</section>""" % zeichen(F, 88, 1040, 110),
    """<section class="p" id="m1">
  <p class="k">Das Modell</p>
  <p class="h m" style="margin-top:28px">Was ein Vorstand wissen <span class="hl">muss.</span></p>
  <div class="modell">
    <div class="stufe"><b>Why</b><div><p>Warum beschäftigen wir uns damit?</p><small>Ausgangssituation · Problem · Lösung</small></div></div>
    <div class="stufe"><b>How</b><div><p>Wie gehen wir grundsätzlich vor?</p><small>Grundsätzlich, nicht im Detail</small></div></div>
    <div class="stufe gelb-b"><b>Next</b><div><p>Was ist der konkrete nächste Schritt?</p><small>Damit es vorangeht</small></div></div>
  </div>
  <p class="namezeile">Daniel Ströbel</p>
</section>""",
    """<section class="p schwarz zahlkarte" id="z1">
  <p class="k">Eingeordnet</p>
  <p class="zahl">77&nbsp;%</p>
  <p class="satz">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p>
  <p class="quelle2">Quelle: Wieselhuber · Was das für einen Bereich heißt, steht im Text.</p>
  <p class="namezeile">Daniel Ströbel</p>
</section>""",
    """<section class="p gelbgrund satzkarte" id="t1">
  <p class="k">Der Satz</p>
  <p class="zitat">„Es hilft doch nichts, wenn nur ich das hier verstanden habe.“</p>
  <p class="quelle">— ein Vorstand</p>
  <p class="namezeile" style="color:#1a1817">Daniel Ströbel</p>
</section>""",
]

html = """<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Postings empiria – Vorlage</title>
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<style>/* Erzeugt von postings_vorlage_bauen.py – nicht von Hand ändern. */%s</style></head>
<body>
%s
</body></html>""" % (CSS, "\n\n".join(teile))

open(os.path.join(HIER, "postings-vorlage.html"), "w", encoding="utf-8").write(html)
print("Vorlage gebaut")
