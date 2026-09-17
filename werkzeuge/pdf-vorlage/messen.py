#!/usr/bin/env python3
"""Misst je PDF-Seite, wie viel Platz unten frei bleibt (bzw. ueberlaeuft).

Ersetzt die Messung aus der alten render.js (Playwright), nutzt aber Chrome
direkt - Node/Playwright sind auf dem Rechner nicht vorhanden.

Aufruf:  python3 messen.py <datei.html>
Ausgabe: je Seite "frei <mm>" - negative Werte bedeuten Ueberlauf.
"""
import json, os, re, subprocess, sys, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"

JS = """
<script>
window.addEventListener('load', function () { setTimeout(function () {
  var MM = 3.7795275591;          // px pro mm bei 96dpi
  var out = [];
  document.querySelectorAll('.page').forEach(function (pg, i) {
    var r = pg.getBoundingClientRect();
    var padBottom = parseFloat(getComputedStyle(pg).paddingBottom);
    var limit = r.height - padBottom;   // Unterkante des Satzspiegels
    // Sitzt unten ein absolut positionierter Kontaktblock (oder eine Skizze),
    // endet der Satzspiegel dort - sonst laeuft der Text unsichtbar darunter.
    var c = pg.querySelector('.contact') || pg.querySelector('.sketch');
    if (c) {
      var ct = c.getBoundingClientRect().top - r.top - 6 * MM;
      if (ct < limit) limit = ct;
    }
    var bottom = 0, over = [];
    // Absolut positionierte Bloecke (Deckblatt-Skizze, Kontakt, Footer, Fussnote)
    // samt ihrer Kinder ausklammern - sie sitzen bewusst am Seitenrand.
    var skip = '.contact, .footer, .head, .sketch, .facts';
    pg.querySelectorAll('*').forEach(function (e) {
      var b = e.getBoundingClientRect();
      if (b.height <= 0 || b.width <= 0) return;
      if (e.closest(skip)) return;
      if (getComputedStyle(e).position === 'absolute') return;
      var rel = b.bottom - r.top;
      if (rel > bottom) bottom = rel;
      // .stage ist bewusst randlos (negative Margins) - dort ist ein Ueberstand
      // nach rechts gewollt und keine Meldung wert. Die Hoehe zaehlt weiter mit.
      if (e.closest('.stage')) return;
      // SVG-Elemente haben kein String-className (SVGAnimatedString) - sonst
      // steht in der Meldung nur "{}".
      if (b.right - r.left > r.width + 1)
        over.push((typeof e.className === 'string' && e.className) || e.tagName);
    });
    out.push({ page: i + 1, frei_mm: +(((limit - bottom) / MM).toFixed(1)),
               rechts_ueber: over.slice(0, 3) });
  });
  document.title = 'MESS:' + JSON.stringify(out);
}, 60); });
</script>
"""


def measure(path):
    html = open(path, encoding="utf-8").read()
    tmp = os.path.join(os.path.dirname(os.path.abspath(path)), "_mess_tmp.html")
    open(tmp, "w", encoding="utf-8").write(html.replace("</body>", JS + "</body>"))
    try:
        res = subprocess.run(
            [CHROME, "--headless=new", "--disable-gpu", "--virtual-time-budget=6000",
             "--window-size=794,1123", "--dump-dom", "file://" + tmp],
            capture_output=True, text=True, timeout=120)
        m = re.search(r"<title>MESS:(.*?)</title>", res.stdout, re.S)
        if not m:
            print("Messung fehlgeschlagen - kein Ergebnis im DOM.")
            return []
        return json.loads(m.group(1))
    finally:
        os.path.exists(tmp) and os.remove(tmp)


if __name__ == "__main__":
    for p in sys.argv[1:]:
        print(f"== {os.path.basename(p)}")
        for row in measure(p):
            flag = "  << UEBERLAUF" if row["frei_mm"] < 0 else ("  < eng" if row["frei_mm"] < 8 else "")
            extra = f"  rechts raus: {row['rechts_ueber']}" if row["rechts_ueber"] else ""
            print(f"   Seite {row['page']}: frei {row['frei_mm']:6.1f} mm{flag}{extra}")
