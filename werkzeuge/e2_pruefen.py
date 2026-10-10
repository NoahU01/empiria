#!/usr/bin/env python3
"""Prüft, dass im Entwurf „empiria 2.0“ kein Text der Originalseite fehlt (Wortvergleich der <main>-Bereiche)."""
import html, re, sys
from collections import Counter
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent)); from e2_bauen import SITE, ZIEL, SEITEN

def worte(t):
    t = t[t.index("<main"):t.index("</main>")]
    # „Weitere Leistungen“ hat Daniel auf den Unterseiten gestrichen (10.10.2026)
    a = t.find('id="weitere-leistungen"')
    if a > 0:
        a = t.rfind("<section", 0, a); t = t[:a] + t[t.index("</section>", a) + 10:]
    t = re.sub(r"<(svg|script|style|template)\b.*?</\1>", " ", t, flags=re.S)
    t = re.sub(r"<[^>]+>", " ", t)
    return Counter(w.lower() for w in re.findall(r"[\wÄÖÜäöüß+:&%€.-]+", html.unescape(t)) if w.strip(".-"))

fehler = 0
for orig, neu in SEITEN.items():
    if not (ZIEL / neu).exists():
        continue
    a, b = worte((SITE / orig).read_text(encoding="utf-8")), worte((ZIEL / neu).read_text(encoding="utf-8"))
    fehlt = {w: n - b[w] for w, n in a.items() if b[w] < n}
    neu_ = {w: n - a[w] for w, n in b.items() if a[w] < n}
    print(f"{neu}: {sum(a.values())} Wörter im Original · fehlt: {fehlt or '–'} · zusätzlich: {neu_ or '–'}")
    fehler += bool(fehlt)
sys.exit(1 if fehler else 0)
