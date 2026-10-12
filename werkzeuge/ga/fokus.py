#!/usr/bin/env python3
"""LinkedIn „Im Fokus“ – quadratische PDFs je Leistungsthema (Daniel, 12.10.2026).

Ein Aufbau für alle sechs Dokumente, je Seite eine Fläche und eine Aussage (1080 × 1080):
  1 Deckblatt (Weiß)   – Thema groß + Themenzeichen; Aussage in der Mitte der Höhe, weil die Fokus-Vorschau
                         nur einen waagrechten Streifen zeigt. Logo/Fuß am Rand gehören zur geöffneten Seite.
  2 Der Moment (Gelb)  – das Problem in einem Satz
  3 Der Ansatz (Weiß)  – drei Bausteine (bei Überblicks-Themen: die Formate)
  4 Denkanstoß (Schwarz) – etwas zum Selbermachen
  5 Das Ergebnis (Weiß) – positiv, ein Satz
  6 Gespräch (Schwarz) – Daniel, Kontakt, Link zur Seite

Aufruf: python3 werkzeuge/ga/fokus.py
Ergebnis: site/projekte/ga-linkedin-fokus.html, site/projekte/ga/fokus/<thema>.pdf + Seiten-PNGs
"""
import re
import subprocess
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from e2_lucide import ICONS  # noqa: E402
from ga_export import (CHROME, FORM, PUPPETEER, SEITE_CSS, SITE, download, exportieren, kopf,  # noqa: E402
                       px_fn, seite)

ORDNER = SITE / "projekte" / "ga" / "fokus"
WEB = "/projekte/ga/fokus"
G = 1080
p = px_fn(G)
S, Y = "#1a1817", "#fff400"


def zeichen(name, breite, farbe):
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg viewBox="{vb}" style="display:block;width:{p(breite)};height:auto;color:{farbe}" aria-hidden="true">{FORM[name]}</svg>'


def ico(n, farbe="currentColor", gr=56):
    return (f'<svg viewBox="0 0 24 24" style="width:{p(gr)};height:{p(gr)};display:block" fill="none" stroke="{farbe}" '
            f'stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>')


THEMEN = {
    "strategie": dict(
        bereich="Strategiehandwerk", zeichen="forward", url="empiria.de/leistungen/strategie",
        titel=["Strategie in den", '<span class="hl">Alltag</span>', "überführen."],
        fuer="Für Abteilungs- und Bereichsleiter",
        karte="Die Strategie steht – aber was heißt sie für deinen Bereich? Wir übersetzen sie mit dir in Rolle, Richtung und Alltag.",
        # 2 · Kennst du das?
        problem_h="Die Strategie steht. Aber was heißt sie für deinen Bereich?",
        problem_text="Du leitest deinen Bereich, weil du fachlich überzeugt hast. Strategisches Denken stand nie auf dem Lehrplan – "
                     "trotzdem wird es ab dem ersten Tag vorausgesetzt. Die Folge: harte Gespräche mit dem eigenen Team.",
        problem_fehlt=["die klare Richtung", "die eigene Rolle", "das Handwerkszeug für den Alltag"],
        # 3 · Was macht ihr?
        weg_h='Wir übersetzen die Strategie in <span class="hl">deinen Bereich.</span>',
        weg_text="Gemeinsam mit dir, in vier Schritten – vom Selbstverständnis bis in den Alltag deines Teams.",
        weg=[("Selbstverständnis", "Wofür stehen wir – und für wen?"),
             ("Vision", "Wie wollen wir wahrgenommen werden?"),
             ("Strategie", "Welchen Weg gehen wir, mit welchen Schwerpunkten?"),
             ("Alltag", "Wie führen, erklären und positionieren wir uns?")],
        # 4 · Was habe ich davon?
        gewinn_h="Du führst dein Team, statt es zu vertrösten.",
        gewinn_text="Du kannst jederzeit erklären, wofür dein Bereich steht und wohin er will. Dein Team zieht mit, weil die Richtung geklärt ist.",
        gewinn=[("flag", "Rolle", "Ein klares Selbstverständnis deines Bereichs"),
                ("compass", "Richtung", "Ein Zielbild und die Schwerpunkte dorthin"),
                ("wrench", "Handwerkszeug", "Für Führung, Strategiekommunikation und Pitch")],
        # 5 · Probier es aus
        denk_h="Wie sähe die Homepage deines Bereichs aus?",
        denk_text="Stell dir vor, dein Bereich wäre ein eigenes Unternehmen. Kannst du diese fünf Fragen beantworten – und würde dein Team dasselbe sagen?",
        denk_url="www.dein-bereich-gmbh.de",
        denk=["Welche Zielgruppe sprechen wir an?", "Welches Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
              "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"],
        denk_schluss='Wenn nicht: <span class="hl">Genau hier fangen wir an.</span>',
        # 6 · Wie geht's weiter?
        so=[("Direkt mit Daniel", "Du arbeitest mit mir – ehrlich, direkt, auf Augenhöhe."),
            ("Dein Einsatz", "Ein bis zwei Stunden pro Woche. Die Umsetzung bleibt bei dir."),
            ("Im Rhythmus", "Regelmäßig abstimmen, flexibel umsteuern, stringent umsetzen.")],
    ),
}

CSS = """
.fk { position: relative; width: 100%; aspect-ratio: 1; container-type: inline-size; overflow: hidden; background: var(--bg, #fff);
  color: var(--fg, #1a1817); font-family: 'Poppins', sans-serif; }
.fk > * { position: absolute; }
.fk p, .fk h1, .fk h2, .fk ol, .fk ul { margin: 0; padding: 0; list-style: none; }
.fk h1, .fk h2, .fk .fk-l { font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.025em; }
.fk .hl { background: #fff400; color: #1a1817; padding: 0 .1em .05em; border-radius: .12em; white-space: nowrap; }
.fk-k { display: flex; align-items: center; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; line-height: 1; }
.fk-fuss { left: 0; right: 0; display: flex; justify-content: space-between; align-items: center; }
.fk-fuss img { display: block; width: auto; }
"""


def kicker(text, farbe=None):
    st = f"color:{farbe};" if farbe else ""
    return (f'<p class="fk-k" style="{st}font-size:{p(19)};gap:{p(16)}"><i style="display:block;width:{p(40)};height:{p(4)};'
            f'background:currentColor"></i>{text}</p>')


def fuss(t, nr, hell=False):
    logo = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    return (f'<div class="fk-fuss" style="bottom:{p(64)};padding:0 {p(80)}">'
            f'<img src="{logo}" alt="empiria" style="height:{p(30)}">'
            f'<span style="font-size:{p(17)};letter-spacing:.06em;opacity:.7">{t["bereich"]} · {nr} / 6</span></div>')


def rahmen(inhalt, bg="#fff", fg=S):
    return f'<div class="fk" style="--bg:{bg};--fg:{fg}">{inhalt}</div>'


# ---------- Seiten: Frage (Kicker) · Antwort (Überschrift) · Erklärung · Bildelement ----------
def kopfblock(frage, h, text, farbe_k=None, h_farbe=None, h_gr=66, text_farbe="#3d3a37", top=130):
    hf = f"color:{h_farbe};" if h_farbe else ""
    return (f'<div style="left:{p(80)};right:{p(80)};top:{p(top)}">{kicker(frage, farbe_k)}'
            f'<h2 style="margin-top:{p(30)};font-size:{p(h_gr)};line-height:1.24;{hf}">{h}</h2>'
            f'<p style="margin-top:{p(26)};max-width:{p(860)};font-size:{p(27)};line-height:1.55;font-weight:300;color:{text_farbe}">{text}</p></div>')


def deckblatt(t):
    titel = "<br>".join(t["titel"])
    return rahmen(
        f'<img src="/assets/empiria-logo.svg" alt="empiria" style="left:{p(80)};top:{p(72)};height:{p(34)}">'
        f'<p style="right:{p(80)};top:{p(80)};font-size:{p(17)};letter-spacing:.06em;opacity:.7">LinkedIn · Im Fokus</p>'
        f'<div style="left:{p(80)};top:50%;transform:translateY(-50%)">{kicker(t["bereich"])}'
        f'<h1 style="margin-top:{p(26)};font-size:{p(98)};line-height:1.22">{titel}</h1></div>'
        f'<div style="right:{p(80)};top:50%;transform:translateY(-12%)">{zeichen(t["zeichen"], 230, S)}</div>'
        f'<p style="left:{p(80)};bottom:{p(72)};font-size:{p(20)};font-weight:600">{t["fuer"]} · {t["url"]}</p>'
        f'<p style="right:{p(80)};bottom:{p(72)};font-size:{p(17)};letter-spacing:.06em;opacity:.7">1 / 6</p>')


def moment(t):
    fehlt = "".join(f'<li style="display:flex;align-items:center;gap:{p(18)};padding:{p(16)} 0;border-top:{p(3)} solid #1a1817">'
                    f'<i style="display:block;width:{p(22)};height:{p(4)};background:#1a1817"></i>{x}</li>' for x in t["problem_fehlt"])
    return rahmen(
        kopfblock("Kennst du das?", t["problem_h"], t["problem_text"], text_farbe="#1a1817", h_gr=62, top=110)
        + f'<div style="left:{p(80)};width:{p(600)};bottom:{p(130)}"><p style="font-size:{p(22)};font-weight:700;letter-spacing:.1em;'
          f'text-transform:uppercase;margin-bottom:{p(14)}">Was fehlt</p><ul style="font-size:{p(28)};font-weight:500">{fehlt}</ul></div>'
        + fuss(t, 2), Y, S)


def ansatz(t):
    schritte = "".join(
        f'<li style="position:relative;display:grid;grid-template-columns:{p(84)} 1fr;align-items:start;padding:{p(18)} 0">'
        f'<span style="position:relative;z-index:1;display:grid;place-items:center;width:{p(58)};height:{p(58)};border-radius:50%;'
        f'background:{"#fff400" if i == 3 else "#1a1817"};color:{"#1a1817" if i == 3 else "#fff"};font-size:{p(21)};font-weight:700">0{i + 1}</span>'
        f'<div><p class="fk-l" style="font-size:{p(38)};line-height:1.2">{w}</p><p style="margin-top:{p(4)};font-size:{p(24)};color:#3d3a37">{f}</p></div></li>'
        for i, (w, f) in enumerate(t["weg"]))
    return rahmen(
        kopfblock("Was macht ihr?", t["weg_h"], t["weg_text"], h_gr=60, top=110)
        + f'<ol style="left:{p(80)};right:{p(80)};bottom:{p(120)}">'
          f'<i style="position:absolute;left:{p(28)};top:{p(48)};bottom:{p(48)};width:{p(3)};background:#e4e0db"></i>{schritte}</ol>'
        + fuss(t, 3))


def ergebnis(t):
    karten = "".join(
        f'<div style="padding:{p(28)} {p(26)};border-radius:{p(18)};background:#fff">'
        f'<span style="display:grid;place-items:center;width:{p(64)};height:{p(64)};border-radius:{p(16)};background:#1a1817;color:#fff400">{ico(i, gr=34)}</span>'
        f'<p class="fk-l" style="margin-top:{p(22)};font-size:{p(32)}">{w}</p><p style="margin-top:{p(8)};font-size:{p(21)};line-height:1.45;color:#3d3a37">{f}</p></div>'
        for i, w, f in t["gewinn"])
    return rahmen(
        kopfblock("Was habe ich davon?", t["gewinn_h"], t["gewinn_text"], h_gr=68)
        + f'<div style="left:{p(80)};right:{p(80)};bottom:{p(140)}"><p style="font-size:{p(20)};font-weight:700;letter-spacing:.1em;'
          f'text-transform:uppercase;margin-bottom:{p(18)}">Am Ende hast du in der Hand</p>'
          f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:{p(18)}">{karten}</div></div>'
        + fuss(t, 4), "#f3f1ee", S)


def denkanstoss(t):
    felder = "".join(
        f'<li style="display:grid;grid-template-columns:{p(54)} 1fr {p(44)};align-items:center;padding:{p(11)} {p(26)};'
        f'border-top:{p(2)} solid #e4e0db"><span style="font-size:{p(17)};font-weight:700;letter-spacing:.12em">0{n + 1}</span>'
        f'<span style="font-size:{p(24)}">{f}</span><b class="fk-l" style="font-size:{p(32)};color:#1a1817;background:#fff400;'
        f'border-radius:{p(8)};text-align:center;line-height:1.25">?</b></li>' for n, f in enumerate(t["denk"]))
    browser = (f'<div style="border-radius:{p(18)};background:#fff;color:#1a1817;overflow:hidden">'
               f'<div style="display:flex;align-items:center;gap:{p(10)};padding:{p(14)} {p(22)};background:#efece8">'
               + "".join(f'<i style="display:block;width:{p(12)};height:{p(12)};border-radius:50%;background:#cfcac3"></i>' for _ in range(3))
               + f'<span style="margin-left:{p(14)};padding:{p(5)} {p(18)};border-radius:99px;background:#fff;font-size:{p(17)};color:#6b6762">{t["denk_url"]}</span></div>'
               f'<ol>{felder}</ol></div>')
    return rahmen(
        kopfblock("Probier es aus", t["denk_h"], t["denk_text"], Y, "#fff", 54, "#d8d3cc", top=96)
        + f'<div style="left:{p(80)};right:{p(80)};bottom:{p(124)}">{browser}'
          f'<p class="fk-l" style="margin-top:{p(24)};font-size:{p(34)};line-height:1.3;color:#fff">{t["denk_schluss"]}</p></div>'
        + fuss(t, 5, hell=True), S, "#fff")


def gespraech(t):
    so = "".join(f'<div style="padding-top:{p(18)};border-top:{p(3)} solid #fff400"><p class="fk-l" style="font-size:{p(28)};color:#fff">{w}</p>'
                 f'<p style="margin-top:{p(8)};font-size:{p(20)};line-height:1.45;color:#d8d3cc">{f}</p></div>' for w, f in t["so"])
    return rahmen(
        f'<div style="left:{p(80)};right:{p(80)};top:{p(130)}">{kicker("Wie geht es weiter?", Y)}'
        f'<h2 style="margin-top:{p(30)};font-size:{p(84)};line-height:1.24;color:#fff">Aus Gespräch<br>wird <span class="hl">Klarheit.</span></h2>'
        f'<p style="margin-top:{p(26)};font-size:{p(27)};font-weight:300;line-height:1.55;color:#d8d3cc;max-width:{p(820)}">'
        f'Erzähl mir, was dich gerade bewegt. Im ersten Gespräch klären wir, ob und wie ich dir weiterhelfen kann.</p>'
        f'<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:{p(28)};margin-top:{p(46)}">{so}</div></div>'
        f'<div style="left:{p(80)};right:{p(80)};bottom:{p(140)};display:flex;align-items:center;gap:{p(28)}">'
        f'<img src="/assets/ansprechpartner-daniel.webp" alt="" style="width:{p(120)};height:{p(120)};border-radius:50%;object-fit:cover">'
        f'<div style="color:#fff"><p class="fk-l" style="font-size:{p(36)}">Daniel Ströbel</p>'
        f'<p style="margin-top:{p(6)};font-size:{p(21)};line-height:1.55;color:#d8d3cc">daniel.stroebel@empiria.de<br>+49 176 3134 7217</p></div>'
        f'<p style="margin-left:auto;text-align:right;font-size:{p(19)};line-height:1.5;color:#d8d3cc">Mehr zum Thema<br>'
        f'<b style="color:#fff400;font-weight:600">{t["url"]}</b></p></div>'
        + fuss(t, 6, hell=True), S, "#fff")


SEITEN = [deckblatt, moment, ansatz, ergebnis, denkanstoss, gespraech]


# ---------- PDF ----------
PDF_JS = r"""
const p = require(process.argv[2]);
(async () => {
  const b = await p.launch({executablePath: process.argv[3], headless: 'new'});
  const pg = await b.newPage();
  await pg.goto(process.argv[4], {waitUntil: 'networkidle0'});
  await pg.evaluate(async () => { await document.fonts.ready; });
  await pg.pdf({path: process.argv[5], width: '1080px', height: '1080px', printBackground: true, pageRanges: ''});
  await b.close();
})().catch(e => { console.error(e); process.exit(1); });
"""


def pdf(name, t):
    druck = (f'<!doctype html><html><head><meta charset="utf-8"><link rel="stylesheet" href="/assets/fonts/fonts.local.css">'
             f'<style>@page {{ size: 1080px 1080px; margin: 0 }} html,body {{ margin:0; padding:0 }} '
             f'.blatt {{ width:1080px; height:1080px; page-break-after: always; overflow:hidden }} {CSS}</style></head><body>'
             + "".join(f'<div class="blatt">{fn(t)}</div>' for fn in SEITEN) + '</body></html>')
    datei = ORDNER / f"_druck_{name}.html"
    datei.write_text(druck, encoding="utf-8")
    try:
        with tempfile.TemporaryDirectory() as tmp:
            js = Path(tmp) / "pdf.js"
            js.write_text(PDF_JS, encoding="utf-8")
            subprocess.run(["node", str(js), str(PUPPETEER), CHROME,
                            f"http://localhost:4599/projekte/ga/fokus/{datei.name}", str(ORDNER / f"empiria-fokus-{name}.pdf")], check=True)
    finally:
        datei.unlink(missing_ok=True)


# ---------- Vorschauseite ----------
SEITE_EXTRA = """
.fk-auf { display: block; width: 100%; padding: 0; border: 0; background: none; cursor: zoom-in; border-radius: 6px; }
.fk-auf:focus-visible { outline: 3px solid #1a1817; outline-offset: 3px; }
.fk-auf .fk { transition: transform .15s ease; }
.fk-auf:hover .fk { transform: translateY(-3px); }
.fk-blaettern { display: inline-flex; margin: 1.2rem 0 .4rem; padding: .75rem 1.3rem; border: 0; border-radius: 999px; background: #1a1817;
  color: #fff; font: 600 .95rem/1 'Poppins', sans-serif; cursor: pointer; }
.fk-blaettern:hover { background: #3a3632; }
.fk-lb { position: fixed; inset: 0; z-index: 1000; display: none; align-items: center; justify-content: center; background: rgba(20,19,18,.92); }
.fk-lb.offen { display: flex; }
.fk-lb__bild { width: min(86vh, 88vw); aspect-ratio: 1; border-radius: 8px; box-shadow: 0 30px 80px rgba(0,0,0,.5); background: #fff; display: block; }
.fk-lb__knopf { position: absolute; top: 50%; transform: translateY(-50%); width: 56px; height: 56px; border: 0; border-radius: 50%;
  background: #fff; color: #1a1817; font-size: 26px; line-height: 1; cursor: pointer; }
.fk-lb__knopf:disabled { opacity: .25; cursor: default; }
.fk-lb__zurueck { left: 24px; } .fk-lb__vor { right: 24px; }
.fk-lb__zu { position: absolute; top: 18px; right: 22px; width: 46px; height: 46px; border: 0; border-radius: 50%; background: rgba(255,255,255,.12);
  color: #fff; font-size: 26px; cursor: pointer; }
.fk-lb__zahl { position: absolute; bottom: 18px; left: 0; right: 0; text-align: center; color: #d8d3cc; font: 600 .9rem/1 'Poppins', sans-serif; letter-spacing: .08em; }
@media (max-width: 700px) { .fk-lb__knopf { top: auto; bottom: 54px; transform: none; width: 50px; height: 50px; } .fk-lb__zurueck { left: 18px; } .fk-lb__vor { right: 18px; } }

.fk-reihe { display: grid; width: 100%; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.4rem; margin-top: 2.4rem; }
.fk-reihe .fk { border-radius: 6px; box-shadow: 0 0 0 1px #e4e0db; }
.fk-karte { width: 100%; max-width: 360px; border-radius: 10px; overflow: hidden; background: #fff; box-shadow: 0 0 0 1px #d9d5cf;
  font-family: -apple-system, 'Segoe UI', 'Poppins', sans-serif; }
.fk-karte__bild { position: relative; aspect-ratio: 466 / 320; overflow: hidden; }
.fk-karte__bild .fk { position: absolute; left: 0; top: 50%; transform: translateY(-50%); }
.fk-karte__bild small { position: absolute; left: 14px; top: 10px; z-index: 2; font-size: 14px; color: #666; background: rgba(255,255,255,.9); padding: 0 4px; }
.fk-karte__text { padding: .7rem .9rem 1rem; background: #f3f2ef; }
.fk-karte__text b { display: block; font-size: 1.05rem; color: #1d1d1d; white-space: nowrap; overflow: hidden; text-overflow: ellipsis; }
.fk-karte__text p { margin: .3rem 0 0; font-size: .98rem; line-height: 1.35; color: #1d1d1d; }
.fk-oben { display: grid; width: 100%; grid-template-columns: minmax(0, 360px) minmax(0, 1fr); gap: 2.4rem; align-items: start; margin-top: 1.6rem; }
@media (max-width: 800px) { .fk-reihe { grid-template-columns: repeat(2, minmax(0, 1fr)); } .fk-oben { grid-template-columns: 1fr; } }
"""


def lightbox():
    import time
    v = int(time.time())
    docs = "{" + ",".join(f'"{n}":[' + ",".join(f'"{WEB}/{n}-{i + 1}.png?v={v}"' for i in range(len(SEITEN))) + "]" for n in THEMEN) + "}"
    return ('<div class="fk-lb" id="fk-lb" role="dialog" aria-modal="true" aria-label="Seitenvorschau">'
            '<button class="fk-lb__zu" type="button" aria-label="Schließen">×</button>'
            '<button class="fk-lb__knopf fk-lb__zurueck" type="button" aria-label="Vorherige Seite">‹</button>'
            '<img class="fk-lb__bild" alt="">'
            '<button class="fk-lb__knopf fk-lb__vor" type="button" aria-label="Nächste Seite">›</button>'
            '<p class="fk-lb__zahl"></p></div>'
            f"""<script>(function(){{
  var DOCS={docs}, lb=document.getElementById('fk-lb'), bild=lb.querySelector('.fk-lb__bild'), zahl=lb.querySelector('.fk-lb__zahl'),
      zu=lb.querySelector('.fk-lb__zu'), zur=lb.querySelector('.fk-lb__zurueck'), vor=lb.querySelector('.fk-lb__vor'), doc=null, i=0, x0=null;
  function zeig(){{ var s=DOCS[doc]; bild.src=s[i]; bild.alt='Seite '+(i+1); zahl.textContent='Seite '+(i+1)+' / '+s.length;
    zur.disabled=i===0; vor.disabled=i===s.length-1; (s[i+1]&&(new Image().src=s[i+1])); }}
  function auf(d,n){{ doc=d; i=n; zeig(); lb.classList.add('offen'); document.body.style.overflow='hidden'; vor.focus(); }}
  function schliessen(){{ lb.classList.remove('offen'); document.body.style.overflow=''; }}
  function geh(d){{ var n=i+d; if(n>=0&&n<DOCS[doc].length){{ i=n; zeig(); }} }}
  document.querySelectorAll('[data-doc]').forEach(function(b){{ b.addEventListener('click',function(){{ auf(b.dataset.doc,+b.dataset.seite); }}); }});
  zu.onclick=schliessen; zur.onclick=function(){{ geh(-1); }}; vor.onclick=function(){{ geh(1); }};
  bild.onclick=function(){{ geh(1); }};
  lb.addEventListener('click',function(e){{ if(e.target===lb) schliessen(); }});
  document.addEventListener('keydown',function(e){{ if(!lb.classList.contains('offen')) return;
    if(e.key==='Escape') schliessen(); else if(e.key==='ArrowRight') geh(1); else if(e.key==='ArrowLeft') geh(-1); }});
  lb.addEventListener('touchstart',function(e){{ x0=e.touches[0].clientX; }},{{passive:true}});
  lb.addEventListener('touchend',function(e){{ if(x0===null) return; var dx=e.changedTouches[0].clientX-x0; if(Math.abs(dx)>40) geh(dx<0?1:-1); x0=null; }});
}})();</script>""")


def main_html():
    teile = []
    for name, t in THEMEN.items():
        titel_rein = re.sub(r"<[^>]+>", "", " ".join(t["titel"]))
        karte = (f'<div class="fk-karte"><div class="fk-karte__bild"><small>Medien</small>{deckblatt(t)}</div>'
                 f'<div class="fk-karte__text"><b>{titel_rein}</b>'
                 f'<p>{t["karte"]}</p></div></div>')
        seiten = "".join(f'<figure style="margin:0"><button class="fk-auf" type="button" data-doc="{name}" data-seite="{i}" '
                         f'aria-label="Seite {i + 1} groß ansehen">{fn(t)}</button><p class="pm-label">Seite {i + 1}</p></figure>'
                         for i, fn in enumerate(SEITEN))
        teile.append(f'<div class="pm-abschnitt"><h2>{t["bereich"]} · {" ".join(t["titel"])}</h2>'
                     f'<div class="fk-oben"><div>{karte}<p class="pm-label">So erscheint das Deckblatt in „Im Fokus“</p></div>'
                     f'<div><p class="pm-text">LinkedIn zeigt vom Deckblatt nur einen waagrechten Streifen. Deshalb steht die Aussage '
                     f'in der Mitte der Höhe; Logo, Adresse und Seitenzahl gehören zur geöffneten Seite und dürfen in der Vorschau wegfallen.'
                     f'</p><button class="fk-blaettern" type="button" data-doc="{name}" data-seite="0">Durchblättern →</button><div class="pm-dl">{download(f"{WEB}/empiria-fokus-{name}.pdf", "PDF · 6 Seiten · 1080 × 1080")}</div></div>'
                     f'<div class="fk-reihe">{seiten}</div></div>')
    return (f'<main>\n<section class="pm"><div class="container">'
            + kopf('LinkedIn <span class="hl">im Fokus</span>',
                   'Sechs Dokumente für den Bereich „Im Fokus“ im LinkedIn-Profil – einheitlich aufgebaut, je Seite eine Aussage. '
                   'Die drei Strategiethemen im Detail, Workshops, Marketing 2.0 und Training &amp; Sparring als Überblick. Begonnen wird mit „Strategie in den Alltag überführen“.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{SEITE_EXTRA}</style>\n{lightbox()}</main>')


if __name__ == "__main__":
    ORDNER.mkdir(parents=True, exist_ok=True)
    seite("ga-linkedin-fokus.html", "LinkedIn im Fokus", main_html())
    for name, t in THEMEN.items():
        pdf(name, t)
        exportieren(CSS, [{"html": fn(t), "w": G, "h": G, "pfad": ORDNER / f"{name}-{i + 1}.png"} for i, fn in enumerate(SEITEN)])
    print("fertig")
