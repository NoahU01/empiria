#!/usr/bin/env python3
"""Bringt den Stand von Branch Daniel nach main - ohne den Entwicklungsteil.

Der einzige vorgesehene Weg in die Produktion. Von Hand zu mergen ist genau
einmal schiefgegangen (18.09.2026): der Merge war sauber, brachte aber das
Entwicklungsmenue und zwei interne Seiten live, weil niemand geprueft hat, ob
ueberhaupt alles nach main gehoert.

Ablauf:
  1 Arbeitsbaum in einem eigenen Worktree auf den Stand von Daniel setzen.
    Bewusst per read-tree statt merge: nach einem Revert haelt Git den Branch
    fuer "bereits gemerged" und ein merge waere wirkungslos.
  2 Entwicklungsteil entfernen (sync_lib.remove_intern_blocks ueber alle
    Seiten, interne Seiten loeschen, ihre Rewrites aus vercel.json nehmen).
  3 main_pruefen.py laufen lassen. Schlaegt es an, bricht der Lauf ab -
    ohne Ausnahme und ohne Schalter, der das uebergeht.
  4 Einen Commit mit zwei Eltern schreiben (main und Daniel), damit spaetere
    Laeufe die Abstammung kennen.

Aufruf:
    python3 werkzeuge/nach_main.py            # nur vorbereiten und zeigen
    python3 werkzeuge/nach_main.py --push     # zusaetzlich nach main pushen
"""
import json, os, shutil, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
from main_pruefen import INTERNE_SEITEN, INTERNE_PFADE, INTERNE_ORDNER  # noqa: E402

QUELLE, ZIEL = "origin/Daniel", "main"


def git(*args, cwd=ROOT, pruefen=True):
    r = subprocess.run(("git",) + args, cwd=cwd, capture_output=True, text=True)
    if pruefen and r.returncode:
        raise SystemExit(f"git {' '.join(args)}\n{r.stderr.strip()}")
    return r.stdout.strip()


def entwicklungsteil_entfernen(baum):
    """Alles entfernen, was nur intern ist. Gibt zurueck, was passiert ist."""
    sys.path.insert(0, os.path.join(baum, "werkzeuge"))
    import importlib, sync_lib
    importlib.reload(sync_lib)

    bericht = []
    seiten = 0
    for dp, dn, fs in os.walk(os.path.join(baum, "site")):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in sorted(fs):
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8").read()
            neu = sync_lib.remove_intern_blocks(t)
            if neu != t:
                open(p, "w", encoding="utf-8").write(neu)
                seiten += 1
    bericht.append(f"Entwicklungsmenue aus {seiten} Seiten entfernt")

    weg = []
    for s in INTERNE_SEITEN:
        p = os.path.join(baum, s)
        if os.path.exists(p):
            os.remove(p)
            weg.append(s)
    for ordner in INTERNE_ORDNER:
        p = os.path.join(baum, ordner)
        if os.path.isdir(p):
            shutil.rmtree(p)
            weg.append(ordner)
    if weg:
        bericht.append("interne Seiten geloescht: " + ", ".join(weg))

    vj = os.path.join(baum, "vercel.json")
    d = json.load(open(vj, encoding="utf-8"))
    vorher = len(d.get("rewrites", []))
    d["rewrites"] = [r for r in d.get("rewrites", []) if r.get("source") not in INTERNE_PFADE]
    if len(d["rewrites"]) != vorher:
        with open(vj, "w", encoding="utf-8") as fh:
            json.dump(d, fh, indent=2, ensure_ascii=False)
            fh.write("\n")
        bericht.append(f"Rewrites: {vorher} -> {len(d['rewrites'])}")
    bericht += nur_verlinkte_seiten(baum)
    return bericht


# Daniel 10.10.2026: Auf main nur, was die Website wirklich zeigt – Startseite, alle Leistungsseiten,
# Kontakt, Impressum, Datenschutz. Nicht verlinkte Seiten (Archiv, Vorträge, alte Fassungen …) fliegen raus.
START = ["site/index.html", "site/kontakt.html", "site/impressum.html", "site/datenschutz.html"]
# Weggefallene Adressen leiten dauerhaft auf die passende Seite weiter (Suchmaschinen, alte Links)
WEITERLEITUNG = {"/leistungen/teams": "/praesentationsseminar", "/der-beste-workshop": "/workshops",
                 "/impulsvortraege": "/training-sparring", "/vortrag-1": "/training-sparring", "/vortrag-2": "/training-sparring",
                 "/vortrag-3": "/training-sparring", "/digitale-tools": "/marketing", "/powerpoint": "/medien",
                 "/landingpage": "/medien", "/rollup": "/medien", "/video": "/medien"}


def erreichbare_seiten(baum):
    import posixpath, re
    gesehen, offen = set(), list(START)
    while offen:
        f = offen.pop()
        pfad = os.path.join(baum, f)
        if f in gesehen or not os.path.exists(pfad):
            continue
        gesehen.add(f)
        for h in re.findall(r'href="([^"]+)"', open(pfad, encoding="utf-8").read()):
            h = h.split("#")[0].split("?")[0]
            if not h or h.startswith(("http", "mailto", "tel", "javascript")):
                continue
            if not h.startswith("/"):
                h = "/" + posixpath.normpath(posixpath.join(posixpath.dirname(f[5:]), h))
            if h == "/":
                offen.append("site/index.html"); continue
            p = "site" + h.rstrip("/")
            if p.endswith(".html"):
                offen.append(p)
            elif "." not in p.split("/")[-1]:
                offen.append(p + ".html")
    return gesehen


def nur_verlinkte_seiten(baum):
    bericht = []
    bleibt = erreichbare_seiten(baum)
    weg = []
    for dp, dn, fs in os.walk(os.path.join(baum, "site")):
        for f in fs:
            rel = os.path.relpath(os.path.join(dp, f), baum).replace(os.sep, "/")
            if rel.endswith(".html") and rel not in bleibt:
                os.remove(os.path.join(dp, f)); weg.append(rel)
    if weg:
        bericht.append(f"nicht verlinkte Seiten entfernt ({len(weg)}): " + ", ".join(sorted(weg)))
    # vercel.json: Rewrites auf entfernte Seiten raus, Weiterleitungen für weggefallene Adressen rein
    vj = os.path.join(baum, "vercel.json")
    d = json.load(open(vj, encoding="utf-8"))
    def ziel_da(r):
        z = r.get("destination", "")
        return "$" in z or not z.endswith(".html") or os.path.exists(os.path.join(baum, z.lstrip("/")))
    d["rewrites"] = [r for r in d.get("rewrites", []) if ziel_da(r)]
    vorhanden = {r.get("source") for r in d.get("redirects", [])}
    for alt, neu in WEITERLEITUNG.items():
        if not os.path.exists(os.path.join(baum, "site" + alt + ".html")):
            for quelle in (alt, alt + ".html", alt + "/"):
                if quelle not in vorhanden:
                    d.setdefault("redirects", []).append({"source": quelle, "destination": neu, "permanent": True})
    if not os.path.exists(os.path.join(baum, "site", "archiv", "startseite-v1.html")) and "/archiv/:pfad*" not in vorhanden:
        d.setdefault("redirects", []).append({"source": "/archiv/:pfad*", "destination": "/", "permanent": True})
    with open(vj, "w", encoding="utf-8") as fh:
        json.dump(d, fh, indent=2, ensure_ascii=False); fh.write("\n")
    # sitemap.xml: genau die Seiten, die es gibt (saubere Adressen wie in den Rewrites)
    sauber = {r["destination"].replace("/site", "", 1): r["source"] for r in d.get("rewrites", []) if "$" not in r.get("source", "")}
    urls = []
    for f in sorted(bleibt, key=lambda x: (x != "site/index.html", x)):
        roh = f[4:]
        url = sauber.get(roh, roh)
        if url in ("/index.html",):
            url = "/"
        urls.append(f"  <url><loc>https://www.empiria.de{url}</loc></url>")
    open(os.path.join(baum, "site", "sitemap.xml"), "w", encoding="utf-8").write(
        '<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n' + "\n".join(urls) + "\n</urlset>\n")
    bericht.append(f"sitemap.xml: {len(urls)} Seiten; Weiterleitungen für weggefallene Adressen gesetzt")
    return bericht


def main(pushen=False):
    git("fetch", "--quiet", "origin")
    quelle_sha, ziel_sha = git("rev-parse", QUELLE), git("rev-parse", f"origin/{ZIEL}")

    baum = tempfile.mkdtemp(prefix="nach_main_")
    shutil.rmtree(baum)
    git("worktree", "add", "--quiet", "--detach", baum, f"origin/{ZIEL}")
    try:
        # 1 Arbeitsbaum exakt auf Daniels Stand
        git("read-tree", "-u", "--reset", QUELLE, cwd=baum)

        # 2 Entwicklungsteil raus
        print("Bereinigt:")
        for z in entwicklungsteil_entfernen(baum):
            print(f"  {z}")

        # 3 Abnahme - ohne sie geht nichts nach main
        print()
        r = subprocess.run([sys.executable, os.path.join(baum, "werkzeuge", "main_pruefen.py")],
                           cwd=baum, capture_output=True, text=True)
        print(r.stdout.strip())
        if r.returncode:
            raise SystemExit("\nAbgebrochen - dieser Stand darf nicht auf main.")

        # 4 Commit mit beiden Eltern
        git("add", "-A", cwd=baum)
        tree = git("write-tree", cwd=baum)
        if tree == git("rev-parse", f"origin/{ZIEL}^{{tree}}"):
            print("\nmain ist bereits auf diesem Stand - nichts zu tun.")
            return 0
        botschaft = (f"Website-Stand nach main - ohne Entwicklungsteil\n\n"
                     f"Quelle: {QUELLE} ({quelle_sha[:7]})\n"
                     f"Erzeugt mit werkzeuge/nach_main.py; main_pruefen.py ist "
                     f"durchgelaufen.\n")
        neu = git("commit-tree", tree, "-p", ziel_sha, "-p", quelle_sha,
                  "-m", botschaft, cwd=baum)
        print(f"\nCommit vorbereitet: {neu[:7]}")
        print(git("diff", "--stat", ziel_sha, neu, cwd=baum).split("\n")[-1])

        if pushen:
            git("push", "origin", f"{neu}:{ZIEL}", cwd=baum)
            print(f"\nGepusht: origin/{ZIEL} -> {neu[:7]}")
        else:
            print(f"\nNicht gepusht. Mit --push ausfuehren, oder von Hand:\n"
                  f"  git push origin {neu}:{ZIEL}")
        return 0
    finally:
        git("worktree", "remove", "--force", baum, pruefen=False)


if __name__ == "__main__":
    sys.exit(main("--push" in sys.argv))
