#!/usr/bin/env python3
"""Legt alle PDFs durchnummeriert in den Download-Ordner - in Menuereihenfolge.

Zum Durchsehen sollen die PDFs in derselben Reihenfolge liegen wie im Menue der
Website: erst das uebergreifende PDF einer Kategorie, dann die Detailseiten
darunter. Die Reihenfolge wird aus dem Hauptmenue von index.html gelesen, damit
sie nicht doppelt gepflegt werden muss; die Seiten aus dem Entwicklungsmenue
(Kategorie "Unterseiten") haengen hinten an.

Aufruf:  python3 werkzeuge/pdfs_exportieren.py [zielordner]
         ohne Angabe: ~/Downloads/empiria-pdfs
"""
import os, re, shutil, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
DL = os.path.join(ROOT, "site", "assets", "downloads")

# Seiten aus dem Entwicklungsmenue, Kategorie "Unterseiten" - Archiv bleibt aussen vor
UNTERSEITEN = ["impulsvortraege", "vortrag-1", "vortrag-2", "vortrag-3",
               "strategie-fuer-aufsichtsraete", "capiamo"]


def menue_reihenfolge():
    nav = re.search(r"(?s)<nav.*?</nav>",
                    open(os.path.join(ROOT, "site", "index.html"), encoding="utf-8").read())
    gesehen, folge = set(), []
    for l in re.findall(r'href="(/[a-z0-9/-]+)"', nav.group(0)):
        slug = l.rstrip("/").split("/")[-1]
        if slug and slug not in gesehen:
            gesehen.add(slug); folge.append(slug)
    return folge


def titel():
    """Lesbare Namen aus den PDF-Titeln in pages.py."""
    q = open(os.path.join(HERE, "pdf-seiten", "pages.py"), encoding="utf-8").read()
    raus = {}
    for m in re.finditer(r'P\["([a-z0-9-]+)"\]\s*=\s*\("[a-z]+",\s*"([^"]+)"', q):
        raus[m.group(1)] = m.group(2).split(" – empiria")[0].split(" - empiria")[0].strip()
    # Die Vortraege entstehen ueber eine Hilfsfunktion und haben keinen
    # Titel-String - hier traegt die Headline den Namen.
    for m in re.finditer(r'P\["([a-z0-9-]+)"\]\s*=\s*vortrag\(\s*"[a-z0-9-]+",\s*\'([^\']+)\'', q):
        kopf = re.sub(r"<[^>]+>", "", m.group(2)).replace("&amp;", "&")
        raus[m.group(1)] = re.sub(r"\s+", " ", kopf).strip().rstrip(".")
    return raus


def dateiname(s):
    for a, b in [("ä","ae"),("ö","oe"),("ü","ue"),("Ä","Ae"),("Ö","Oe"),("Ü","Ue"),("ß","ss")]:
        s = s.replace(a, b)
    s = re.sub(r"[^A-Za-z0-9]+", "-", s).strip("-")
    return s


def main(ziel):
    namen = titel()
    folge = [s for s in menue_reihenfolge() if os.path.exists(os.path.join(DL, f"empiria-{s}.pdf"))]
    folge += [s for s in UNTERSEITEN if s not in folge]

    fehlend = [s for s in namen if s not in folge]
    os.makedirs(ziel, exist_ok=True)
    for alt in os.listdir(ziel):
        if re.match(r"^\d{2}_.*\.pdf$", alt):
            os.remove(os.path.join(ziel, alt))      # alten Stand entfernen

    for i, slug in enumerate(folge, 1):
        quelle = os.path.join(DL, f"empiria-{slug}.pdf")
        if not os.path.exists(quelle):
            print(f"  {i:02d}  FEHLT: {slug}")
            continue
        name = f"{i:02d}_{dateiname(namen.get(slug, slug))}.pdf"
        shutil.copy2(quelle, os.path.join(ziel, name))
        print(f"  {i:02d}  {name}")

    print(f"\n{len(folge)} PDFs nach {ziel}")
    if fehlend:
        print("Nicht einsortiert (weder im Menue noch unter Unterseiten):",
              ", ".join(sorted(fehlend)))


if __name__ == "__main__":
    ziel = sys.argv[1] if len(sys.argv) > 1 else os.path.expanduser("~/Downloads/empiria-pdfs")
    main(ziel)
