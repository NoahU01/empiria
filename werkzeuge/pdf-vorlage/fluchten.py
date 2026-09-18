#!/usr/bin/env python3
"""Prueft, ob gleichartige Elemente nebeneinanderliegender Kaesten fluchten.

Hintergrund: In einer Reihe aus Karten, Bildern oder Preiskaesten muessen
Ueberschrift, Text und Zusatz jeweils auf derselben Hoehe beginnen. Sobald eine
Ueberschrift zweizeilig wird, rutscht sonst alles darunter - das faellt beim
Durchsehen nur zufaellig auf. Hier wird es gemessen: fuer jede Gruppe wird die
Oberkante jedes n-ten Kindes ueber alle Geschwister verglichen.

Aufruf:  python3 fluchten.py [datei.html ...]   (ohne Angabe: alle in _build/)
"""
import glob, json, os, re, subprocess, sys

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.abspath(os.path.join(HERE, "..", "pdf-seiten", "_build"))
TOLERANZ_MM = 0.6          # darunter ist es Rundung, kein Versatz

JS = """
<script>
window.addEventListener('load', function () { setTimeout(function () {
  var MM = 3.7795275591, out = [];
  // Gruppen aus gleichartigen Kaesten nebeneinander
  var GRUPPEN = ['.cards', '.bilder', '.mocks', '.opts', '.raster', '.tools', '.cases'];
  document.querySelectorAll('.page').forEach(function (pg, pi) {
    GRUPPEN.forEach(function (sel) {
      pg.querySelectorAll(sel).forEach(function (grp) {
        var kinder = [].slice.call(grp.children).filter(function (e) {
          return e.getBoundingClientRect().height > 0;
        });
        if (kinder.length < 2) return;
        // nur Kaesten derselben Reihe vergleichen (gleiche Oberkante des Kastens)
        var reihen = {};
        kinder.forEach(function (k) {
          var y = Math.round(k.getBoundingClientRect().top / 4);
          (reihen[y] = reihen[y] || []).push(k);
        });
        Object.keys(reihen).forEach(function (y) {
          var reihe = reihen[y];
          if (reihe.length < 2) return;
          var n = Math.min.apply(null, reihe.map(function (k) { return k.children.length; }));
          for (var i = 0; i < n; i++) {
            var tops = reihe.map(function (k) {
              return k.children[i].getBoundingClientRect().top;
            });
            var spanne = (Math.max.apply(null, tops) - Math.min.apply(null, tops)) / MM;
            if (spanne > %TOL%) {
              out.push({ page: pi + 1, gruppe: sel, kind: i + 1,
                         tag: (reihe[0].children[i].className || reihe[0].children[i].tagName).toString().slice(0, 28),
                         versatz: +spanne.toFixed(1) });
            }
          }
        });
      });
    });
  });
  document.title = 'FLU:' + JSON.stringify(out);
}, 80); });
</script>
"""


def pruefen(pfad):
    html = open(pfad, encoding="utf-8").read()
    tmp = os.path.join(os.path.dirname(os.path.abspath(pfad)), "_flucht_tmp.html")
    js = JS.replace("%TOL%", str(TOLERANZ_MM))
    open(tmp, "w", encoding="utf-8").write(html.replace("</body>", js + "</body>"))
    try:
        res = subprocess.run([CHROME, "--headless=new", "--disable-gpu",
                              "--virtual-time-budget=6000", "--dump-dom", "file://" + tmp],
                             capture_output=True, text=True, timeout=180)
        m = re.search(r"<title>FLU:(.*?)</title>", res.stdout, re.S)
        return json.loads(m.group(1)) if m else []
    finally:
        os.path.exists(tmp) and os.remove(tmp)


if __name__ == "__main__":
    dateien = sys.argv[1:] or sorted(glob.glob(os.path.join(BUILD, "_pdfsrc_*.html")))
    gesamt = 0
    for f in dateien:
        b = pruefen(f)
        name = os.path.basename(f)[len("_pdfsrc_"):-5]
        if b:
            print(f"== {name}")
            for x in b:
                print(f"   S{x['page']}  {x['gruppe']:8s} Kind {x['kind']} ({x['tag']})"
                      f"  {x['versatz']} mm Versatz")
            gesamt += len(b)
    print(f"\n{gesamt} Stelle(n), an denen gleichartige Elemente nicht fluchten "
          f"(Toleranz {TOLERANZ_MM} mm)")
