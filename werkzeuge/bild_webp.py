#!/usr/bin/env python3
"""PNG -> WebP mit erhaltenem Seitenverhaeltnis.

png_to_webp aus der PDF-Werkzeugkiste skaliert fest auf A4 - fuer
Bildschirmfotos und hohe Dokumentstreifen verzerrt das. Hier bleibt das
Verhaeltnis, begrenzt wird nur die laengere Kante.

Aufruf: python3 werkzeuge/bild_webp.py quelle.png ziel.webp [max_kante]
"""
import base64, os, re, subprocess, sys, tempfile

CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"


def masse(pfad):
    with open(pfad, "rb") as f:
        kopf = f.read(24)
    return int.from_bytes(kopf[16:20], "big"), int.from_bytes(kopf[20:24], "big")


def wandeln(png, webp, max_kante=1600, guete=0.86):
    b, h = masse(png)
    f = min(1.0, max_kante / max(b, h))
    bz, hz = max(1, round(b * f)), max(1, round(h * f))
    b64 = base64.b64encode(open(png, "rb").read()).decode()
    html = f"""<!doctype html><meta charset="utf-8"><body><img id="s" src="data:image/png;base64,{b64}">
<script>
var img=document.getElementById('s');
function go(){{var c=document.createElement('canvas');c.width={bz};c.height={hz};
var x=c.getContext('2d');x.fillStyle='#fff';x.fillRect(0,0,c.width,c.height);
x.drawImage(img,0,0,c.width,c.height);
document.title='IMG:'+c.toDataURL('image/webp',{guete});}}
if(img.complete)go();else img.onload=go;
</script></body>"""
    with tempfile.TemporaryDirectory() as d:
        quelle = os.path.join(d, "q.html")
        open(quelle, "w", encoding="utf-8").write(html)
        r = subprocess.run([CHROME, "--headless", "--disable-gpu", "--virtual-time-budget=20000",
                            "--dump-dom", "file://" + quelle],
                           capture_output=True, text=True)
    m = re.search(r"IMG:data:image/webp;base64,([A-Za-z0-9+/=]+)", r.stdout)
    if not m:
        raise RuntimeError("Chrome hat kein WebP geliefert")
    open(webp, "wb").write(base64.b64decode(m.group(1)))
    return bz, hz, os.path.getsize(webp)


if __name__ == "__main__":
    q, z = sys.argv[1], sys.argv[2]
    k = int(sys.argv[3]) if len(sys.argv) > 3 else 1600
    b, h, g = wandeln(q, z, k)
    print(f"{os.path.basename(z)}: {b}x{h}, {g // 1024} KB")
