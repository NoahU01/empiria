#!/usr/bin/env python3
"""Rendert die Posting-Bilder aus postings-vorlage.html (1080 × 1350, JPG) und das Dokument als PDF.
    python3 werkzeuge/medienkonzept/postings_rendern.py
Ziel: site/assets/projekte/medienkonzept/postings/
"""
import os, shutil, subprocess, threading, http.server, functools, socketserver
HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
ZIEL = os.path.join(SITE, "assets", "projekte", "medienkonzept", "postings")
CHROME = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
BILDER = ["p1", "p2", "p3", "p4", "p5", "d1", "d2", "d3", "d4", "d5", "d6", "s1", "n1", "k1", "m1", "z1", "t1", "c1", "k2", "m2", "m3", "w2", "z2", "sz3", "sz4", "sz5", "sa3", "sa4", "sa5", "fr3", "fr4", "fr5", "mo3", "mo4", "mo5", "wz3", "wz4", "wz5", "ei3", "ei4", "ei5", "dk2", "dk3", "dk4", "dk5", "sz6", "kt1", "kt2", "kt3"]

def main():
    os.makedirs(ZIEL, exist_ok=True)
    tmp = os.path.join(SITE, "_postings_tmp.html")
    shutil.copy(os.path.join(HIER, "postings-vorlage.html"), tmp)
    class Leise(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    h = functools.partial(Leise, directory=SITE)
    srv = socketserver.TCPServer(("127.0.0.1", 0), h); port = srv.server_address[1]
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    try:
        for b in BILDER:
            png = os.path.join(ZIEL, b + ".png")
            subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--hide-scrollbars",
                            "--window-size=1080,1350", "--virtual-time-budget=6000",
                            f"--screenshot={png}", f"http://127.0.0.1:{port}/_postings_tmp.html#{b}"],
                           capture_output=True, timeout=120)
            subprocess.run(["sips", "-s", "format", "jpeg", "-s", "formatOptions", "88", png,
                            "--out", os.path.join(ZIEL, b + ".jpg")], capture_output=True)
            os.remove(png)
            print(b, "ok")
        # Dokument als PDF (LinkedIn-Dokumentbeitrag): Seiten d1–d6
        open(tmp, "w", encoding="utf-8").write(open(os.path.join(HIER, "postings-vorlage.html"), encoding="utf-8").read()
            .replace("<body>", '<body class="druck">')
            .replace("</style>", ".druck section[id^=p],.druck section[id^=s],.druck section[id^=n],.druck section[id^=k],.druck section[id^=m],.druck section[id^=z],.druck section[id^=t],.druck section[id^=c],.druck section[id^=w],.druck section[id^=sz],.druck section[id^=sa],.druck section[id^=fr],.druck section[id^=mo],.druck section[id^=wz],.druck section[id^=ei],.druck section[id^=dk],.druck section[id^=kt]{display:none!important}</style>"))
        pdf = os.path.join(ZIEL, "Ein-Thema-vier-Gegenueber.pdf")
        subprocess.run([CHROME, "--headless=new", "--disable-gpu", "--no-pdf-header-footer",
                        "--virtual-time-budget=6000", f"--print-to-pdf={pdf}",
                        f"http://127.0.0.1:{port}/_postings_tmp.html"], capture_output=True, timeout=120)
        print("pdf", os.path.getsize(pdf) // 1024, "KB")
    finally:
        srv.shutdown(); os.remove(tmp)

if __name__ == "__main__":
    main()
