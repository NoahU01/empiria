#!/usr/bin/env python3
"""Erzeugt die WebP-Vorschaubilder einer PDF-Seite aus der HTML-Quelle.

Hintergrund: Auf dem Rechner gibt es weder cwebp noch Pillow, und sips kann
kein WebP schreiben. Chrome kann es aber ueber Canvas (toDataURL) - genau das
nutzt dieses Skript, zusammen mit dem Screenshot der jeweiligen Seite.

Aufruf:
    python3 vorschaubilder.py <quelle.html> <ziel-praefix> [seiten...]
Beispiel:
    python3 vorschaubilder.py workshops.html assets/downloads/empiria-workshops 1 2
"""
import base64, os, re, subprocess, sys, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
PAGE_W, PAGE_H = 794, 1123          # A4 bei 96dpi
OUT_W, OUT_H = 744, 1053            # Zielmass der bestehenden Vorschaubilder
QUALITY = 0.86


def _run(args, **kw):
    return subprocess.run(args, capture_output=True, text=True, timeout=180, **kw)


def screenshot_pages(html_path, pages, tmpdir):
    """Screenshot je Seite einzeln.

    Bewusst NICHT ueber einen Gesamt-Screenshot mit anschliessendem sips-Crop:
    --cropOffset rechnet nicht verlaesslich ab Oberkante, dabei entstanden
    Vorschaubilder, die den Uebergang zweier Seiten zeigten. Stattdessen wird
    je Durchgang alles ausser der Zielseite ausgeblendet.
    """
    html = open(html_path, encoding="utf-8").read()
    # Die Temp-HTML muss NEBEN der Quelle liegen, sonst laufen die relativen
    # Asset-Pfade (Fonts, Logo, Portraits) ins Leere.
    src_dir = os.path.dirname(os.path.abspath(html_path))
    out = {}
    for p in pages:
        # Wichtig: .page--stretch ist eine Flex-Spalte (abschliessendes Band
        # fuellt den Restplatz). Ein pauschales display:block wuerde das
        # ueberschreiben - das Vorschaubild zeigte dann etwas anderes als das PDF.
        css = (f"<style>.page{{display:none !important}}"
               f".page:nth-of-type({p}){{display:block !important}}"
               f".page--stretch:nth-of-type({p}){{display:flex !important}}</style>")
        tmp_html = os.path.join(src_dir, f"_vorschau_tmp{p}.html")
        open(tmp_html, "w", encoding="utf-8").write(html.replace("</body>", css + "</body>"))
        shot = os.path.join(tmpdir, f"p{p}.png")
        _run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
              f"--window-size={PAGE_W},{PAGE_H}", f"--screenshot={shot}",
              "--virtual-time-budget=6000", "file://" + tmp_html])
        os.path.exists(tmp_html) and os.remove(tmp_html)
        if not os.path.exists(shot):
            raise RuntimeError(f"Screenshot fehlgeschlagen fuer Seite {p}")
        out[p] = shot
    return out


def png_to_webp(png_path, webp_path):
    """Konvertiert per Chrome-Canvas nach WebP (skaliert auf OUT_W x OUT_H)."""
    with open(png_path, "rb") as fh:
        b64 = base64.b64encode(fh.read()).decode()
    html = f"""<!doctype html><meta charset="utf-8"><body><img id="s" src="data:image/png;base64,{b64}">
<script>
var img = document.getElementById('s');
function go() {{
  var c = document.createElement('canvas');
  c.width = {OUT_W}; c.height = {OUT_H};
  var x = c.getContext('2d');
  x.fillStyle = '#fff'; x.fillRect(0, 0, c.width, c.height);
  x.drawImage(img, 0, 0, c.width, c.height);
  document.title = 'IMG:' + c.toDataURL('image/webp', {QUALITY});
}}
if (img.complete) go(); else img.onload = go;
</script></body>"""
    d = os.path.dirname(os.path.abspath(webp_path))
    tmp = os.path.join(d, "_webp_tmp.html")
    open(tmp, "w", encoding="utf-8").write(html)
    try:
        res = _run([CHROME, "--headless=new", "--disable-gpu",
                    "--virtual-time-budget=8000", "--dump-dom", "file://" + tmp])
        m = re.search(r"<title>IMG:data:image/webp;base64,([^<]+)</title>", res.stdout)
        if not m:
            raise RuntimeError(f"WebP-Konvertierung fehlgeschlagen fuer {png_path}")
        open(webp_path, "wb").write(base64.b64decode(m.group(1)))
    finally:
        os.path.exists(tmp) and os.remove(tmp)


if __name__ == "__main__":
    src, prefix = sys.argv[1], sys.argv[2]
    pages = [int(x) for x in (sys.argv[3:] or ["1", "2"])]
    with tempfile.TemporaryDirectory() as td:
        shots = screenshot_pages(src, pages, td)
        for i, p in enumerate(pages, 1):
            target = f"{prefix}-{i}.webp"
            png_to_webp(shots[p], target)
            print(f"{target}  ({os.path.getsize(target) // 1024} KB)")
