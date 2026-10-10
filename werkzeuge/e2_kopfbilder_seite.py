#!/usr/bin/env python3
"""Entwicklungsseite „Kopfbilder“ (Daniel, 10.10.2026): nur die 23 Kopfbilder, sonst nichts.
Bilder kommen aus e2_kopfbilder.py, Darstellung wie auf der Header-Seite. Nur Entwicklung, nie auf main.

    python3 werkzeuge/e2_kopfbilder_seite.py
"""
import re
from e2_header import QUELLE, SITE, CSS4, kopfbilder

ZIEL = SITE / "projekte" / "kopfbilder.html"


def main():
    h = QUELLE.read_text(encoding="utf-8")
    a, b = h.index("<main>"), h.index("</main>") + 7
    inhalt = '<div style="height:2.5rem"></div>' + kopfbilder() + '<div style="height:5rem"></div>'
    seite = h[:a] + "<main>\n" + CSS4 + '<div class="e2-alt e2-alt--magenta">' + inhalt + "</div>\n</main>" + h[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>Kopfbilder · Entwicklung</title>", seite, count=1, flags=re.S)
    ZIEL.write_text(seite, encoding="utf-8")
    print("gebaut:", ZIEL.relative_to(SITE.parent))


if __name__ == "__main__":
    main()
