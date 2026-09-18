"""Erzeugt die HTML-Quellen der PDFs nach _build/ (frueher: fester Cloud-Pfad)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pages import P
from lib import build

OUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "_build")
os.makedirs(OUT, exist_ok=True)

# Fusszeile: Strich links, Seitenzahl rechts. Gilt fuer alle PDFs; zum
# Einschraenken einzelne Slugs eintragen.
FUSSZEILE = set(P)   # alle PDFs


only = sys.argv[1:] or list(P)
for slug in only:
    th, title, pages = P[slug]
    path = os.path.join(OUT, f"_pdfsrc_{slug}.html")
    open(path, "w", encoding="utf-8").write(
        build(th, pages, title, fusszeile=slug in FUSSZEILE))
print(" ".join(only))
