#!/usr/bin/env python3
"""Lokaler Dev-Server mit "Clean URL"-Fallback.

Ersetzt `python3 -m http.server 4599`: gleicher Port, gleiches Verzeichnis,
aber mit einer Zusatzfunktion, die genau das nachbildet, was `vercel.json`
im echten Deployment über die "rewrites" macht: eine Anfrage auf
/sofort-sichtbar (ohne .html) wird automatisch auf sofort-sichtbar.html
umgeleitet, wenn diese Datei existiert. Ohne das bleiben alle "schönen"
Menü-Links (und damit auch die Archiv-Links) lokal tot, weil der eingebaute
http.server ausschließlich exakte Dateinamen inkl. Endung kennt.

Aufruf identisch wie bisher:
    cd site
    python3 dev-server.py
    # -> http://localhost:4599
"""
import http.server
import os
import socketserver

PORT = 4599


class CleanUrlHandler(http.server.SimpleHTTPRequestHandler):
    def translate_path(self, path):
        clean = path.split('?', 1)[0].split('#', 1)[0]
        fs_path = super().translate_path(clean)
        if not os.path.exists(fs_path) and not clean.endswith('/'):
            candidate = fs_path + '.html'
            if os.path.exists(candidate):
                return candidate
        return fs_path


if __name__ == '__main__':
    socketserver.TCPServer.allow_reuse_address = True
    # ThreadingTCPServer: sonst blockiert eine offene Keep-Alive-Verbindung (z. B. Chrome/Puppeteer) alle weiteren Requests
    with socketserver.ThreadingTCPServer(('', PORT), CleanUrlHandler) as httpd:
        print(f'-> http://localhost:{PORT}  (Clean-URLs wie /sofort-sichtbar funktionieren jetzt auch lokal)')
        try:
            httpd.serve_forever()
        except KeyboardInterrupt:
            pass
