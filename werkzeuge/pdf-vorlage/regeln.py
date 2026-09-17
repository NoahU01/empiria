#!/usr/bin/env python3
"""Prueft die Layoutregeln der PDF-Seiten - macht den Gestaltungsstandard messbar.

Die PDFs wurden vorher je Seite nach Gefuehl zusammengesetzt. Das Ergebnis waren
Seiten mit drei getoenten Flaechen, reine Textseiten und halb leere Seiten.
Diese Regeln sind die Gegenmassnahme; sie gelten fuer jede Inhaltsseite
(Deckblatt ausgenommen):

R1  Hoechstens EINE getoente Flaeche je Seite (helles Band ODER dunkler Kasten
    ODER gelbe Aussage). Nie grau auf grau.
R2  Keine Seite ohne gestaltendes Element - reiner Fliesstext ist unzulaessig.
R3  Kein Ueberlauf.
R4  Nicht mehr als LEER_MAX mm freier Raum am Seitenende. Seiten mit
    abschliessendem Band (stage--boden) oder Kontaktblock sind ausgenommen,
    dort fuellt das Band bzw. der Block den Rest.

Aufruf:  python3 regeln.py [datei.html ...]      (ohne Angabe: alle in _build/)
"""
import glob, os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
BUILD = os.path.abspath(os.path.join(HERE, "..", "pdf-seiten", "_build"))
LEER_MAX = 55.0

sys.path.insert(0, HERE)
from messen import measure  # noqa: E402

# Klassen, die eine getoente Flaeche aufspannen (jeweils genau einmal gezaehlt)
FLAECHEN = ["stage", "band", "mdl", "bubbles", "stein", "mocks-box", "feat", "paket", "vgl"]
# Klassen, die eine Seite gestaltet machen (Grafik, Kasten, Bild, Raster)
GESTALTEND = FLAECHEN + ["cards", "raster", "bilder", "baustein", "opts", "stations", "pakete",
                         "inline-sketch", "quotes", "cases", "chips", "bm"]


def _seiten(html):
    return re.findall(r'<section class="page([^"]*)">(.*?)</section>', html, re.S)


def pruefen(pfad):
    html = open(pfad, encoding="utf-8").read()
    mess = {m["page"]: m for m in measure(pfad)}
    befunde = []
    for i, (klassen, inhalt) in enumerate(_seiten(html), 1):
        if "cover" in klassen:
            continue
        # class="stage stage--boden" darf nicht doppelt zaehlen: auf das
        # Klassen-Attribut schauen, nicht auf Teilstrings im Markup.
        attrs = re.findall(r'class="([^"]*)"', inhalt)
        gestaltet = any(k in a.split() for a in attrs for k in GESTALTEND)
        # Nur NEBENEINANDER liegende Flaechen zaehlen. Ein dunkler Kasten in
        # einem hellen Band ist die Schichtung der Website und gewollt; zwei
        # Flaechen hintereinander auf einer Seite sind der Fehler.
        anzahl, vorhanden = 0, set()
        tiefe, flaeche_ab = 0, None
        for m in re.finditer(r'<div\b([^>]*)>|</div>', inhalt):
            if m.group(0) == "</div>":
                tiefe -= 1
                if flaeche_ab is not None and tiefe <= flaeche_ab:
                    flaeche_ab = None
                continue
            kl = re.search(r'class="([^"]*)"', m.group(1) or "")
            treffer = set(kl.group(1).split()) & set(FLAECHEN) if kl else set()
            if treffer and flaeche_ab is None:
                anzahl += 1
                vorhanden |= treffer
                flaeche_ab = tiefe
            tiefe += 1

        if anzahl > 1:
            befunde.append((i, "R1", f"{anzahl} getoente Flaechen ({', '.join(sorted(vorhanden))})"))
        if not gestaltet:
            befunde.append((i, "R2", "reine Textseite ohne gestaltendes Element"))
        m = mess.get(i)
        if m:
            if m["frei_mm"] < 0:
                befunde.append((i, "R3", f"Ueberlauf {m['frei_mm']} mm"))
            elif m["frei_mm"] > LEER_MAX and "stage--boden" not in inhalt and 'class="contact"' not in inhalt:
                befunde.append((i, "R4", f"{m['frei_mm']} mm leer"))
    return befunde


if __name__ == "__main__":
    dateien = sys.argv[1:] or sorted(glob.glob(os.path.join(BUILD, "_pdfsrc_*.html")))
    gesamt = 0
    for f in dateien:
        b = pruefen(f)
        name = os.path.basename(f)[len("_pdfsrc_"):-5]
        if b:
            print(f"== {name}")
            for seite, regel, text in b:
                print(f"   S{seite}  {regel}  {text}")
            gesamt += len(b)
        else:
            print(f"== {name}  ok")
    print(f"\n{gesamt} Regelverstoss/-verstoesse")
