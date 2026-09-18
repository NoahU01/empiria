#!/usr/bin/env python3
"""Nimmt ein echtes Element einer Website-Seite als hochaufloesendes Bild ab.

Hintergrund: Die stark gestalteten Bausteine der Produktseiten (Kanal-Check,
Potenzialcheck, Anzeigen-Mockups, Vergleichsgrafiken) bestehen aus HTML + CSS +
SVG-Sprites. Sie im PDF-Generator nachzubauen fuehrt zu Abweichungen - genau das
war das Problem. Stattdessen wird hier das Original im Browser gerendert und
exakt der Bereich des Elements abgefotografiert. Was im PDF landet, ist damit
identisch zur Seite.

Aufruf:
    python3 baustein_bild.py <seite.html> <css-selektor> <zielname> [--breite 1200] [--skala 3]

Ergebnis: site/assets/pdf-bausteine/<zielname>.png
"""
import argparse, contextlib, functools, http.server, json, os, re, socketserver
import subprocess, sys, threading

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SITE = os.path.join(ROOT, "site")
OUT = os.path.join(SITE, "assets", "pdf-bausteine")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

# Das Zielelement wird freigestellt: alles andere ausgeblendet, das Element
# selbst an den Nullpunkt gesetzt. Danach genuegt ein Vollbild-Screenshot in
# genau der Elementgroesse. Animationen/Reveals werden zwangsweise sichtbar
# gemacht, sonst bleibt der Baustein transparent.
JS = """
<script>
window.__ziel = %s;
window.__ohne = %s;
window.__keinSchatten = %s;
window.addEventListener('load', function () { setTimeout(function () {
  var el = document.querySelector(window.__ziel);
  if (!el) { document.title = 'BB:ERR:nicht gefunden'; return; }
  // Teile ausblenden, die im PDF keinen Sinn haben (z. B. "Mehr erfahren").
  (window.__ohne || []).forEach(function (s) {
    el.querySelectorAll(s).forEach(function (e) { e.style.display = 'none'; });
  });
  document.querySelectorAll('.reveal, [class*="reveal"]').forEach(function (e) {
    e.classList.add('is-visible', 'revealed', 'in-view');
    e.style.opacity = '1'; e.style.transform = 'none'; e.style.visibility = 'visible';
  });
  // Bausteine, die auf der Seite erst per Klick aktiv werden (z. B. die
  // Meta-/LinkedIn-Anzeige im Karussell), sonst unsichtbar abgenommen wuerden.
  el.classList.add('is-active');
  el.style.opacity = '1'; el.style.visibility = 'visible';
  el.style.transform = 'none';
  // position NICHT pauschal auf static setzen: Bausteine mit position:relative
  // verlieren sonst den Bezugspunkt fuer ihre ::before-Elemente (z. B. der
  // farbige Balken am Rand des Kanal-Checks) samt deren Rundung.
  var pos = getComputedStyle(el).position;
  if (pos === 'absolute' || pos === 'fixed') { el.style.position = 'relative'; el.style.inset = 'auto'; }
  el.removeAttribute('hidden');
  // Ein Schlagschatten des Originals endet an der Bildkante und wird im PDF
  // als hartes Viereck sichtbar - auf Wunsch vorher abschalten.
  if (window.__keinSchatten) {
    el.style.boxShadow = 'none';
    el.querySelectorAll('*').forEach(function (e) { e.style.boxShadow = 'none'; });
  }
  var r = el.getBoundingClientRect();
  var st = document.createElement('style');
  st.textContent = 'body > * { display: none !important; } ' +
    '#__bbhost { display: block !important; position: absolute; left: 0; top: 0; margin: 0; }' +
    'html, body { margin:0 !important; padding:0 !important; background: transparent !important; }';
  document.head.appendChild(st);
  var host = document.createElement('div');
  host.id = '__bbhost';
  host.style.width = r.width + 'px';
  document.body.appendChild(host);
  host.appendChild(el);
  el.style.margin = '0';
  var r2 = el.getBoundingClientRect();
  document.title = 'BB:' + JSON.stringify({ w: Math.ceil(r2.width), h: Math.ceil(r2.height) });
}, 400); });
</script>
"""


class _Still(http.server.SimpleHTTPRequestHandler):
    def log_message(self, *a):
        pass


@contextlib.contextmanager
def _server(wurzel):
    """Die Seiten verlinken Stylesheets absolut ("/styles.css"). Unter file://
    greifen diese Pfade ins Dateisystem-Wurzelverzeichnis und laden nicht -
    die Aufnahme haette dann die falsche Typografie. Darum ueber HTTP."""
    handler = functools.partial(_Still, directory=wurzel)
    with socketserver.TCPServer(("127.0.0.1", 0), handler) as srv:
        t = threading.Thread(target=srv.serve_forever, daemon=True)
        t.start()
        try:
            yield f"http://127.0.0.1:{srv.server_address[1]}"
        finally:
            srv.shutdown()


def abnehmen(seite, selektor, name, breite=1200, skala=3, ohne=None, kein_schatten=False):
    pfad = seite if os.path.isabs(seite) else os.path.join(SITE, seite)
    html = open(pfad, encoding="utf-8").read()
    tmp = os.path.join(os.path.dirname(pfad), "_bb_tmp.html")
    open(tmp, "w", encoding="utf-8").write(
        html.replace("</body>", (JS % (json.dumps(selektor), json.dumps(ohne or []),
                                     json.dumps(bool(kein_schatten)))) + "</body>"))
    try:
        rel = os.path.relpath(tmp, SITE).replace(os.sep, "/")
        with _server(SITE) as basis:
            url = f"{basis}/{rel}"
            # 1. Durchlauf: Groesse des freigestellten Elements ermitteln
            res = subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                 f"--window-size={breite},2000", "--virtual-time-budget=8000",
                 "--dump-dom", url],
                capture_output=True, text=True, timeout=180)
            m = re.search(r"<title>BB:(.*?)</title>", res.stdout, re.S)
            if not m:
                raise RuntimeError(f"kein Ergebnis fuer {selektor}")
            if m.group(1).startswith("ERR"):
                raise RuntimeError(f"{selektor}: {m.group(1)}")
            masse = json.loads(m.group(1))
            # Ohne diese Pruefung startet Chrome mit --window-size=0,0 und
            # haengt bis zum Timeout. Tritt auf, wenn das Element zum
            # Messzeitpunkt noch keine Ausdehnung hat (Animation, lazy SVG).
            if masse["w"] < 2 or masse["h"] < 2:
                raise RuntimeError(f"{selektor}: Element ohne Ausdehnung "
                                   f"({masse['w']}x{masse['h']}) - anderer Selektor noetig")

            # 2. Durchlauf: Screenshot in exakt dieser Groesse, hochaufloesend
            os.makedirs(OUT, exist_ok=True)
            ziel = os.path.join(OUT, name + ".png")
            subprocess.run(
                [CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                 "--default-background-color=00000000",
                 f"--force-device-scale-factor={skala}",
                 f"--window-size={masse['w']},{masse['h']}",
                 "--virtual-time-budget=8000", f"--screenshot={ziel}", url],
                capture_output=True, timeout=180)
        if not os.path.exists(ziel):
            raise RuntimeError(f"Screenshot fehlgeschlagen: {selektor}")
        kb = os.path.getsize(ziel) // 1024
        print(f"{name:34s} {masse['w']}x{masse['h']} px @{skala}x  {kb} KB")
        return ziel
    finally:
        os.path.exists(tmp) and os.remove(tmp)


if __name__ == "__main__":
    ap = argparse.ArgumentParser()
    ap.add_argument("seite")
    ap.add_argument("selektor")
    ap.add_argument("name")
    ap.add_argument("--breite", type=int, default=1200)
    ap.add_argument("--skala", type=int, default=3)
    ap.add_argument("--ohne", action="append", default=[],
                    help="CSS-Selektor innerhalb des Elements, der ausgeblendet wird")
    ap.add_argument("--kein-schatten", action="store_true",
                    help="box-shadow abschalten - sonst endet der Schatten als "
                         "hartes Viereck an der Bildkante")
    a = ap.parse_args()
    abnehmen(a.seite, a.selektor, a.name, a.breite, a.skala, a.ohne, a.kein_schatten)
