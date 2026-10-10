#!/usr/bin/env python3
"""Gemeinsame Helfer für die Geschäftsausstattungs-Entwürfe (LinkedIn, Hintergründe …).

- seite(): baut eine Entwicklungsseite im Rahmen von site/projekte/powerpoint-master.html (alles außer <main>).
- exportieren(): rendert HTML-Entwürfe in Originalgröße als PNG (Puppeteer + Chrome).
  Ein kleiner lokaler Server liefert dabei site/ aus, damit Schriften, Logo und Porträts geladen werden.
- px(): Maße in Originalpixeln → cqw, damit Vorschau und Export dieselbe Gestaltung zeigen.
"""
import functools
import http.server
import json
import re
import socketserver
import subprocess
import sys
import tempfile
import threading
from pathlib import Path

HERE = Path(__file__).resolve().parent
WERKZEUGE = HERE.parent
SITE = WERKZEUGE.parent / "site"
sys.path.insert(0, str(WERKZEUGE))
from e2_bauen import FORM  # noqa: E402

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PUPPETEER = SITE / "node_modules" / "puppeteer-core"

SCHWARZ, GELB, WEISS, GRAU = "#1a1817", "#fff400", "#ffffff", "#f3f1ee"


def form(name, farbe):
    """Markenform als Inline-SVG (füllt die Breite des Elternelements)."""
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return (f'<svg viewBox="{vb}" style="display:block;width:100%;height:auto;color:{farbe};fill:{farbe}" '
            f'aria-hidden="true">{FORM[name]}</svg>')


PFEIL_VERH = 170.29 / 226.78  # Höhe : Breite des Doppelpfeils


def px_fn(breite):
    """Liefert eine Funktion, die Originalpixel in cqw (bezogen auf die Entwurfsbreite) umrechnet."""
    return lambda v: f"{v / breite * 100:.4f}cqw"


def seite(dateiname, titel, main_inhalt):
    """Schreibt site/projekte/<dateiname> im Rahmen der PowerPoint-Master-Seite."""
    rahmen = (SITE / "projekte" / "powerpoint-master.html").read_text(encoding="utf-8")
    a, b = rahmen.index("<main"), rahmen.index("</main>") + 7
    html = rahmen[:a] + main_inhalt + rahmen[b:]
    html = re.sub(r"<title>.*?</title>", f"<title>{titel} – empiria (intern)</title>", html, count=1, flags=re.S)
    (SITE / "projekte" / dateiname).write_text(html, encoding="utf-8")
    print(f"gebaut: site/projekte/{dateiname}")


NODE = r"""
const p = require(process.argv[2]);
const jobs = JSON.parse(require('fs').readFileSync(process.argv[3], 'utf8'));
(async () => {
  const b = await p.launch({executablePath: process.argv[4], headless: 'new'});
  const pg = await b.newPage();
  await pg.goto(process.argv[5], {waitUntil: 'networkidle0'});
  for (const j of jobs) {
    await pg.setViewport({width: j.w, height: j.h, deviceScaleFactor: 1});
    await pg.evaluate((html, w, h) => {
      const c = document.getElementById('c');
      c.style.width = w + 'px'; c.style.height = h + 'px'; c.innerHTML = html;
    }, j.html, j.w, j.h);
    await pg.evaluate(async () => {
      await document.fonts.ready;
      await Promise.all([...document.images].map(i => i.complete ? 0 : new Promise(r => { i.onload = i.onerror = r; })));
    });
    await pg.screenshot({path: j.pfad, clip: {x: 0, y: 0, width: j.w, height: j.h}});
    process.stdout.write('.');
  }
  await b.close();
  process.stdout.write('\n');
})().catch(e => { console.error(e); process.exit(1); });
"""


class _Leise(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


def exportieren(css, jobs):
    """jobs: Liste von dicts {html, w, h, pfad}. Jedes html wird in einem Kasten w×h px gerendert."""
    handler = functools.partial(_Leise, directory=str(SITE))
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as srv:
        port = srv.server_address[1]
        threading.Thread(target=srv.serve_forever, daemon=True).start()
        with tempfile.TemporaryDirectory() as tmp:
            tmp = Path(tmp)
            render = SITE / "projekte" / "ga" / f"_render_{port}.html"
            render.parent.mkdir(parents=True, exist_ok=True)
            render.write_text(
                '<!doctype html><html><head><meta charset="utf-8">'
                '<link rel="stylesheet" href="/assets/fonts/fonts.local.css">'
                f'<style>html,body{{margin:0;padding:0;overflow:hidden}} #c{{position:relative;overflow:hidden}} {css}</style>'
                '</head><body><div id="c"></div></body></html>', encoding="utf-8")
            try:
                for j in jobs:
                    Path(j["pfad"]).parent.mkdir(parents=True, exist_ok=True)
                (tmp / "jobs.json").write_text(json.dumps([{**j, "pfad": str(j["pfad"])} for j in jobs]), encoding="utf-8")
                (tmp / "export.js").write_text(NODE, encoding="utf-8")
                subprocess.run(["node", str(tmp / "export.js"), str(PUPPETEER), str(tmp / "jobs.json"), CHROME,
                                f"http://127.0.0.1:{port}/projekte/ga/{render.name}"], check=True)
            finally:
                render.unlink(missing_ok=True)
        srv.shutdown()
    print(f"exportiert: {len(jobs)} PNG")


# Seitenrahmen-CSS (wie powerpoint-master): Kicker, H1 mit Highlight, Lead, Abschnitte, Beschriftungen, Download-Chips
SEITE_CSS = """
.pm { padding: 6rem 0 5rem; }
.pm-kicker { display: flex; align-items: center; gap: .75rem; margin: 0 0 1.1rem; font: 700 .8rem/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; }
.pm-kicker::before { content: ""; width: 1.6rem; height: 2px; background: #1a1817; }
.pm h1 { font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.2; font-size: clamp(2.2rem, 5vw, 4rem); margin: 0; color: #1a1817; }
.pm .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; }
.pm-lead { max-width: 46rem; margin: 1.2rem 0 0; font-size: 1.1rem; line-height: 1.6; font-weight: 300; color: #3d3a37; }
.pm-abschnitt { margin-top: 4.5rem; }
.pm-abschnitt h2 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 1.7rem; letter-spacing: -.01em; margin: 0; color: #1a1817; }
.pm-abschnitt h3 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 1.25rem; margin: 3rem 0 0; color: #1a1817; }
.pm-abschnitt p.pm-text { max-width: 50rem; margin: .6rem 0 0; color: #3d3a37; line-height: 1.6; }
.pm-label { margin: .7rem 0 0; font: 600 .72rem/1.4 'Poppins', sans-serif; letter-spacing: .1em; text-transform: uppercase; color: #8a847c; }
.pm-dl { display: flex; flex-wrap: wrap; gap: .45rem; margin-top: .9rem; }
.pm-dl a { display: inline-flex; align-items: center; gap: .4rem; padding: .42rem .8rem; border-radius: 999px; border: 1px solid #d9d5ce; font: 500 .78rem/1 'Poppins', sans-serif; color: #1a1817; text-decoration: none; background: #fff; }
.pm-dl a:hover { border-color: #1a1817; }
.pm-dl a svg { width: .9rem; height: .9rem; }
.pm-hinweis { display: inline-block; margin-top: .4rem; font-size: .8rem; color: #8a847c; }
"""

DL_ICON = ('<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" '
           'stroke-linejoin="round" aria-hidden="true"><path d="M12 15V3"/><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4"/>'
           '<path d="m7 10 5 5 5-5"/></svg>')


def kopf(titel_html, lead):
    return (f'<p class="pm-kicker">Geschäftsausstattung</p><h1>{titel_html}</h1><p class="pm-lead">{lead}</p>')


def download(pfad_web, text):
    return f'<a href="{pfad_web}" download>{DL_ICON}{text}</a>'
