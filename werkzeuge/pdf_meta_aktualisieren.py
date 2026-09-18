#!/usr/bin/env python3
"""Haelt die Angaben in den Download-Kaesten synchron zu den echten PDFs.

In jeder Seite steht:  <div class="pdf-dl-meta"><span>PDF</span><span>N Seiten</span><span>X,Y MB</span>
Seitenzahl und Groesse driften, sobald ein PDF neu gebaut wird - dieses Skript
liest beides aus der verlinkten PDF-Datei und schreibt es zurueck.

Aufruf:  python3 pdf_meta_aktualisieren.py [--pruefen]
         --pruefen aendert nichts, meldet nur Abweichungen.
"""
import os, re, sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
SITE = os.path.join(ROOT, "site")
META = re.compile(r'(<div class="pdf-dl-meta"><span>PDF</span><span>)(\d+)(\s*Seiten</span><span>)([^<]+)(</span>)')


def pdf_seiten(path):
    """Seitenzahl aus dem PDF (Anzahl /Type /Page, ohne /Type /Pages)."""
    data = open(path, "rb").read()
    return len(re.findall(rb"/Type\s*/Page(?![s])", data))


def pdf_groesse(path):
    mb = os.path.getsize(path) / 1_000_000
    return f"{mb:.1f}".replace(".", ",") + " MB"


def main(pruefen=False):
    geaendert = abweichungen = 0
    for dirpath, _, files in os.walk(SITE):
        if os.sep + "archiv" in dirpath:
            continue            # Archivseiten sind bewusst eingefrorene Schnappschuesse
        for name in sorted(f for f in files if f.endswith(".html")):
            p = os.path.join(dirpath, name)
            t = open(p, encoding="utf-8").read()
            m = META.search(t)
            if not m:
                continue
            link = re.search(r'assets/downloads/(empiria-[a-z0-9-]+\.pdf)', t)
            if not link:
                print(f"{name:34s} Download-Kasten ohne PDF-Link - uebersprungen")
                continue
            pdf = os.path.join(SITE, "assets", "downloads", link.group(1))
            if not os.path.exists(pdf):
                print(f"{name:34s} PDF fehlt: {link.group(1)}")
                continue
            seiten, groesse = pdf_seiten(pdf), pdf_groesse(pdf)
            if m.group(2) == str(seiten) and m.group(4).strip() == groesse:
                continue
            abweichungen += 1
            print(f"{name:34s} {m.group(2)} Seiten/{m.group(4).strip():>7s}"
                  f"  ->  {seiten} Seiten/{groesse}")
            if not pruefen:
                t = META.sub(lambda mm: mm.group(1) + str(seiten) + mm.group(3) + groesse + mm.group(5), t, count=1)
                open(p, "w", encoding="utf-8").write(t)
                geaendert += 1
    print(f"\n{abweichungen} Abweichung(en)" + ("" if pruefen else f", {geaendert} Datei(en) aktualisiert"))


if __name__ == "__main__":
    main(pruefen="--pruefen" in sys.argv)
