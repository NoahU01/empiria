"""Gemeinsame Bausteine für die Geschäftsausstattungs-Entwürfe (Visitenkarten, Roll-up, Word, One-Pager).

- Seitenrahmen aus site/projekte/powerpoint-master.html (alles außer <main>…</main>)
- Maßeinheiten: In den Format-CSS-Blöcken steht [6] für 6 mm und [9pt] für 9 Punkt. masse() rechnet das
  in cqw um, bezogen auf die Breite des Formats. So skaliert jeder Entwurf maßstäblich.
- png_export(): rendert Elemente mit data-png="ga/<thema>/datei.png" data-pw="<Breite px>" in Originalgröße.
"""
import json
import re
import subprocess
import sys
from pathlib import Path

GA = Path(__file__).resolve().parent
WERKZEUGE = GA.parent
SITE = WERKZEUGE.parent / "site"
PROJEKTE = SITE / "projekte"
sys.path.insert(0, str(WERKZEUGE))
from e2_bauen import FORM  # noqa: E402
from e2_lucide import ICONS  # noqa: E402

ICONS = dict(ICONS, globe='<circle cx="12" cy="12" r="10"/><path d="M12 2a14.5 14.5 0 0 0 0 20 14.5 14.5 0 0 0 0-20"/><path d="M2 12h20"/>')

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PUPPETEER = SITE / "node_modules" / "puppeteer-core"
SERVER = "http://localhost:4599"

SCHWARZ, GELB, GRAU, WEISS = "#1a1817", "#fff400", "#f3f1ee", "#ffffff"
MAGENTA, VIOLETT, CYAN = "#C51F5D", "#8613A1", "#0B9FBD"

# Personen (Kerstin/Noah: Kontaktdaten sind Platzhalter, ph=True)
PERSONEN = {
    "daniel": dict(name="Daniel Ströbel", rolle="Geschäftsführer", rolle2="Strategiehandwerker",
                   mail="daniel.stroebel@empiria.de", tel="+49 176 3134 7217", ph=False),
    "kerstin": dict(name="Kerstin Christ", rolle="Expertin HR &amp; Weiterbildung", rolle2="",
                    mail="kerstin.christ@empiria.de", tel="+49 …", ph=True),
    "noah": dict(name="Noah Hermanns", rolle="Experte Performance Marketing", rolle2="",
                 mail="noah.hermanns@empiria.de", tel="+49 …", ph=True),
}
FIRMA = dict(name="empiria GmbH", strasse="Kapellengasse 6", ort="74564 Crailsheim", web="www.empiria.de",
             gf="Daniel Ströbel", gericht="Amtsgericht Ulm", hrb="HRB 750146", ust="DE 281217286")


def masse(css, breite_mm):
    """[6] → 6 mm, [9pt] → 9 pt, jeweils als cqw relativ zur Formatbreite."""
    def ersetzen(m):
        wert = float(m.group(1)) * (0.3528 if m.group(2) else 1)
        return f"{wert * 100 / breite_mm:.4f}cqw"
    return re.sub(r"\[(-?\d+(?:\.\d+)?)(pt)?\]", ersetzen, css)


def zeichen(name, farbe, cls=""):
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg class="{cls}" viewBox="{vb}" fill="{farbe}" color="{farbe}" aria-hidden="true">{FORM[name]}</svg>'


def ico(n, farbe="currentColor", sw=1.6):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="{sw}" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>')


def logo(hell=False, cls="logo"):
    return f'<img class="{cls}" src="/assets/empiria-logo{"-weiss" if hell else ""}.svg" alt="empiria">'


def ph(text, aktiv=True):
    """Platzhalter sichtbar kennzeichnen (gestrichelter Rahmen)."""
    return f'<span class="ga-ph">{text}</span>' if aktiv else text


SEITEN_CSS = """
.ga { padding: 6rem 0 5rem; }
.ga-kicker { display: flex; align-items: center; gap: .75rem; margin: 0 0 1.1rem; font: 700 .8rem/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; }
.ga-kicker::before { content: ""; width: 1.6rem; height: 2px; background: #1a1817; }
.ga h1 { font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.2; font-size: clamp(2.4rem, 5vw, 4rem); margin: 0; color: #1a1817; }
.ga .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; box-decoration-break: clone; -webkit-box-decoration-break: clone; }
.ga-lead { max-width: 46rem; margin: 1.2rem 0 0; font-size: 1.1rem; line-height: 1.6; font-weight: 300; color: #3d3a37; }
.ga-chips { display: flex; gap: .5rem; flex-wrap: wrap; margin-top: 1.6rem; }
.ga-chips span { padding: .45rem .9rem; border-radius: 999px; border: 1px solid #d9d5ce; font: 500 .8rem/1 'Poppins', sans-serif; color: #6f6a64; }
.ga-chips span.aktiv { background: #1a1817; color: #fff; border-color: #1a1817; }
.ga-abschnitt { margin-top: 4.5rem; }
.ga-abschnitt > h2 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 1.7rem; margin: 0; letter-spacing: -.01em; }
.ga-abschnitt > p { max-width: 50rem; margin: .6rem 0 0; color: #3d3a37; line-height: 1.6; }
.ga-unter { margin: 2.2rem 0 0; font: 700 .72rem/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; display: flex; align-items: center; gap: .6rem; }
.ga-unter::before { content: ""; width: 1.2rem; height: 2px; background: #fff400; }
.ga-raster { display: grid; grid-template-columns: repeat(var(--sp, 2), minmax(0, 1fr)); gap: 2rem 1.6rem; margin-top: 1.4rem; align-items: start; }
.ga-wrap { margin: 0; min-width: 0; }
.ga-blatt { box-shadow: 0 0 0 1px #e4e0db, 0 14px 34px rgba(26,24,23,.08); }
.ga-label { margin-top: .75rem; font: 600 .72rem/1.45 'Poppins', sans-serif; letter-spacing: .1em; text-transform: uppercase; color: #8a847c; }
.ga-label b { color: #1a1817; font-weight: 700; }
.ga-dl { display: inline-flex; align-items: center; gap: .4rem; margin-top: .45rem; font: 600 .78rem/1 'Poppins', sans-serif; color: #1a1817; text-decoration: none; border-bottom: 2px solid #fff400; padding-bottom: .2rem; }
.ga-dl:hover { background: #fff400; }
.ga-dl svg { width: .95rem; height: .95rem; }
.ga-hinweis { margin-top: 1.2rem; display: flex; gap: .7rem; align-items: flex-start; max-width: 50rem; font-size: .88rem; line-height: 1.55; color: #6f6a64; }
.ga-hinweis .ga-ph { flex: 0 0 auto; }
.ga-ph { outline: 1px dashed #8a847c; outline-offset: .12em; border-radius: .1em; }
.ga-export { box-shadow: none !important; border-radius: 0 !important; }
.ga-export .ga-ph { outline: none; }
@media (max-width: 800px) {
  .ga { padding: 4rem 0 3.5rem; }
  .ga-raster { grid-template-columns: repeat(var(--sp-m, 1), minmax(0, 1fr)); gap: 1.6rem 1rem; }
  .ga-abschnitt { margin-top: 3.2rem; }
  .ga-abschnitt > h2 { font-size: 1.45rem; }
}
"""

DL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round"><path d="M12 15V3"/><path d="m7 10 5 5 5-5"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/></svg>')


def download(pfad, text):
    return f'<a class="ga-dl" href="/projekte/{pfad}" download>{DL_ICON}{text}</a>'


def figur(inhalt, label, dl=""):
    return f'<figure class="ga-wrap">{inhalt}<figcaption class="ga-label">{label}</figcaption>{dl}</figure>'


def raster(figuren, sp=2, sp_m=1, extra=""):
    return f'<div class="ga-raster" style="--sp:{sp};--sp-m:{sp_m};{extra}">{"".join(figuren)}</div>'


def abschnitt(titel, text, inhalt):
    return f'<div class="ga-abschnitt"><h2>{titel}</h2><p>{text}</p>{inhalt}</div>'


def seite_schreiben(datei, titel, h1, lead, chips, inhalt, css):
    rahmen = (PROJEKTE / "powerpoint-master.html").read_text(encoding="utf-8")
    a, b = rahmen.index("<main"), rahmen.index("</main>") + 7
    akt = ' class="aktiv"'
    chips_html = "".join(f'<span{akt if i == 0 else ""}>{c}</span>' for i, c in enumerate(chips))
    main = f'''<main>
<section class="ga"><div class="container">
  <p class="ga-kicker">Geschäftsausstattung</p>
  <h1>{h1}</h1>
  <p class="ga-lead">{lead}</p>
  <div class="ga-chips">{chips_html}</div>
  {inhalt}
</div></section>
<style>{SEITEN_CSS}{css}</style>
</main>'''
    seite = rahmen[:a] + main + rahmen[b:]
    seite = re.sub(r"<title>.*?</title>", f"<title>{titel} – empiria (intern)</title>", seite, count=1, flags=re.S)
    (PROJEKTE / datei).write_text(seite, encoding="utf-8")
    print(f"gebaut: site/projekte/{datei}")


EXPORT_JS = r"""
const puppeteer = require(process.argv[2]);
const [chrome, url, ziel] = process.argv.slice(3);
(async () => {
  const b = await puppeteer.launch({ executablePath: chrome, headless: 'new' });
  const p = await b.newPage();
  await p.setViewport({ width: 3600, height: 2000, deviceScaleFactor: 1 });
  await p.goto(url, { waitUntil: 'networkidle0' });
  await p.evaluate(() => document.fonts.ready);
  const n = await p.evaluate(() => {
    const els = [...document.querySelectorAll('[data-png]')];
    const stage = document.createElement('div');
    stage.id = 'ga-stage';
    stage.style.cssText = 'position:absolute;left:0;top:0;z-index:2147483647;background:#fff;display:flex;flex-direction:column;align-items:flex-start;gap:40px;padding:0';
    els.forEach((el, i) => {
      const c = el.cloneNode(true);
      c.classList.add('ga-export');
      c.style.width = el.dataset.pw + 'px';
      c.style.maxWidth = 'none';
      c.id = 'ga-ex-' + i;
      stage.appendChild(c);
    });
    [...document.body.children].forEach(k => { if (k.tagName !== 'MAIN' && k.tagName !== 'SCRIPT') k.style.display = 'none'; });
    document.querySelector('main section').style.display = 'none';
    document.body.appendChild(stage);
    return els.length;
  });
  await p.evaluate(() => Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; }))));
  await new Promise(r => setTimeout(r, 600));
  const pfade = await p.evaluate(() => [...document.querySelectorAll('[data-png]')].filter(e => e.id.startsWith('ga-ex-')).map(e => e.dataset.png));
  const els = await p.$$('#ga-stage > [data-png]');
  for (let i = 0; i < els.length; i++) {
    await els[i].screenshot({ path: ziel + '/' + pfade[i] });
    console.log('png:', pfade[i]);
  }
  await b.close();
})();
"""


def png_export(datei, thema):
    """Exportiert alle [data-png]-Elemente der Seite in Originalgröße nach site/projekte/ga/<thema>/."""
    (PROJEKTE / "ga" / thema).mkdir(parents=True, exist_ok=True)
    js = GA / ".export.js"
    js.write_text(EXPORT_JS, encoding="utf-8")
    try:
        subprocess.run(["node", str(js), str(PUPPETEER), CHROME, f"{SERVER}/projekte/{datei}", str(PROJEKTE)], check=True)
    finally:
        js.unlink(missing_ok=True)
