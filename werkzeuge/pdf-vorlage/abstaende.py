#!/usr/bin/env python3
"""Findet zu enge Abstaende zwischen Bloecken in den PDF-Quellen.

Hintergrund: Die Regel `.sec + .sec { margin-top }` greift nur bei direkter
Nachbarschaft. Sobald ein Block (who/sols/Tabelle) dazwischensteht, verliert die
folgende Subheadline ihren Abstand und klebt am Block davor. Mit dem Auge faellt
das erst auf, wenn man alle Seiten durchsieht - dieses Skript misst es.

Aufruf:  python3 abstaende.py <datei.html> [...]
Meldet jeden vertikalen Abstand < MIN_MM zwischen zwei aufeinanderfolgenden
Bloecken einer Seite.
"""
import json, os, re, subprocess, sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
MIN_MM = 6.0

JS = """
<script>
window.addEventListener('load', function () { setTimeout(function () {
  var MM = 3.7795275591, out = [];
  document.querySelectorAll('.page').forEach(function (pg, i) {
    var kids = [].slice.call(pg.children).filter(function (e) {
      var cs = getComputedStyle(e);
      if (cs.position === 'absolute' || cs.display === 'none') return false;
      if (e.matches('.head, .footer, .contact')) return false;
      return e.getBoundingClientRect().height > 0;
    });
    for (var k = 1; k < kids.length; k++) {
      var prev = kids[k-1].getBoundingClientRect(), cur = kids[k].getBoundingClientRect();
      var gap = (cur.top - prev.bottom) / MM;
      out.push({ page: i+1, gap: +gap.toFixed(1),
                 zwischen: (kids[k-1].className||kids[k-1].tagName) + ' -> ' + (kids[k].className||kids[k].tagName) });
    }
  });
  document.title = 'GAP:' + JSON.stringify(out);
}, 60); });
</script>
"""


def pruefen(path):
    html = open(path, encoding="utf-8").read()
    tmp = os.path.join(os.path.dirname(os.path.abspath(path)), "_gap_tmp.html")
    open(tmp, "w", encoding="utf-8").write(html.replace("</body>", JS + "</body>"))
    try:
        res = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                              "--virtual-time-budget=6000", "--dump-dom", "file://" + tmp],
                             capture_output=True, text=True, timeout=120)
        m = re.search(r"<title>GAP:(.*?)</title>", res.stdout, re.S)
        return json.loads(m.group(1)) if m else []
    finally:
        os.path.exists(tmp) and os.remove(tmp)


if __name__ == "__main__":
    gesamt = 0
    for p in sys.argv[1:]:
        eng = [g for g in pruefen(p) if g["gap"] < MIN_MM]
        if eng:
            print(f"== {os.path.basename(p)}")
            for g in eng:
                print(f"   S{g['page']}  {g['gap']:5.1f} mm   {g['zwischen'][:70]}")
            gesamt += len(eng)
    print(f"\n{gesamt} zu enge Stelle(n) (< {MIN_MM} mm)")
