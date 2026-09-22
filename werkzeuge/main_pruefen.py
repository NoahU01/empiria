#!/usr/bin/env python3
"""Prueft, ob ein Stand auf main darf - der Entwicklungsteil darf es nie.

Hintergrund: Am 18.09.2026 ist ein Merge nach main gelaufen, der das
Entwicklungsmenue und zwei interne Seiten in die Produktion gebracht hat. Der
Merge selbst war sauber; geprueft wurde nur, ob etwas von Noah verloren geht -
nicht, ob ueberhaupt alles nach main gehoert. Diese Pruefung schliesst genau
diese Luecke und ist mechanisch, nicht nach Augenmass.

Ursache war, dass site/ den Sandbox-Stand samt Entwicklungsmenue enthielt,
obwohl site/ die saubere Fassung sein soll. Entfernt wird das ueber
sync_lib.remove_intern_blocks(); hier wird nur kontrolliert.

Geprueft wird:
  1 Entwicklungsmenue   keine ENTWICKLUNG-Marker, kein dev-dd-Markup
  2 Interne Seiten      capiamo.html und strategie-aufsichtsrat.html fehlen
  3 Rewrites            vercel.json fuehrt nicht auf interne Seiten
  4 Tote Verweise       keine Links auf entfernte interne Seiten
  5 Menueband           kein interner Menuepunkt auf irgendeiner Seite

Aufruf:
    python3 werkzeuge/main_pruefen.py               # Arbeitsverzeichnis
    python3 werkzeuge/main_pruefen.py origin/main   # ein Git-Stand
Rueckgabe: 0 = darf auf main, 1 = darf nicht.
"""
import json, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, ".."))

# Seiten, die es auf main nicht geben darf. Bewusst als feste Liste: was
# intern ist, entscheidet nicht ein Muster, sondern eine Absprache.
INTERNE_SEITEN = ["site/capiamo.html", "site/strategie-aufsichtsrat.html",
                  "site/budget-retter.html",
                  "site/xmas.html", "site/xmas-1.html", "site/xmas-2.html",
                  "site/xmas-4.html",
                  "site/xmas-5.html", "site/xmas-6.html",
                  "site/xmas-8.html",
                  "site/xmas-9.html", "site/xmas-10.html",
                  "site/xmas-11.html", "site/xmas-12.html",
                  "site/xmas-13.html"]
INTERNE_PFADE = ["/capiamo", "/strategie-aufsichtsrat", "/xmas", "/budget-retter"]
# Woerter, die im Menueband nichts zu suchen haben. Das Menue zeigt in der
# Produktion ausschliesslich Problem, Loesung und Leistungen.
MENUE_VERBOTEN = ["Entwicklung", "Archiv", "capiamo", "Aufsichtsräte", "Sandbox",
                  "X-Mas", "Budget-Retter"]


def _lauf(*args):
    return subprocess.run(args, cwd=ROOT, capture_output=True, text=True)


class Quelle:
    """Liest Dateien entweder aus dem Arbeitsverzeichnis oder aus einem Git-Stand."""

    def __init__(self, ref=None):
        self.ref = ref

    def dateien(self, unter="site", endung=".html"):
        if self.ref:
            r = _lauf("git", "ls-tree", "-r", "--name-only", self.ref, "--", unter)
            namen = r.stdout.split("\n")
        else:
            namen = []
            for dp, dn, fs in os.walk(os.path.join(ROOT, unter)):
                dn[:] = [d for d in dn if d not in (".git", "node_modules")]
                for f in fs:
                    namen.append(os.path.relpath(os.path.join(dp, f), ROOT).replace(os.sep, "/"))
        return [n for n in namen if n and n.endswith(endung)]

    def lesen(self, pfad):
        if self.ref:
            r = _lauf("git", "show", f"{self.ref}:{pfad}")
            return r.stdout if r.returncode == 0 else None
        p = os.path.join(ROOT, pfad)
        return open(p, encoding="utf-8").read() if os.path.exists(p) else None


def pruefen(q):
    befunde = {}

    # 1 Entwicklungsmenue
    menue = []
    for f in q.dateien():
        t = q.lesen(f) or ""
        if "ENTWICKLUNG:START" in t:
            menue.append(f"{f}: ENTWICKLUNG-Marker")
        elif "dev-dd" in t:
            menue.append(f"{f}: dev-dd-Markup")
    befunde["Entwicklungsmenue"] = menue

    # 2 Interne Seiten
    befunde["Interne Seiten"] = [f"{s} liegt im Stand" for s in INTERNE_SEITEN
                                 if q.lesen(s) is not None]

    # 3 Rewrites
    rew = []
    roh = q.lesen("vercel.json")
    if roh:
        try:
            for r in json.loads(roh).get("rewrites", []):
                if r.get("source") in INTERNE_PFADE:
                    rew.append(f"vercel.json: {r['source']} -> {r.get('destination')}")
        except json.JSONDecodeError as e:
            rew.append(f"vercel.json ist kein gueltiges JSON: {e}")
    befunde["Rewrites"] = rew

    # 4 Tote Verweise auf entfernte Seiten - Archiv ausgenommen, das ist Altbestand
    tot = []
    muster = re.compile(r'href="(' + "|".join(re.escape(p) for p in INTERNE_PFADE) + r')"')
    for f in q.dateien():
        if f.startswith("site/archiv/"):
            continue
        for m in muster.finditer(q.lesen(f) or ""):
            tot.append(f"{f}: Verweis auf {m.group(1)}")
    befunde["Tote Verweise"] = tot

    # 5 Menueband aller Seiten: es darf nichts Internes anbieten.
    #    Bewusst ueber Wortlaut UND Ziele geprueft - ein umbenannter Menuepunkt
    #    faellt sonst durch, und ein Link ohne Beschriftung ebenso.
    men = []
    for f in q.dateien():
        if f.startswith("site/archiv/"):
            continue
        t = q.lesen(f) or ""
        for nav in re.findall(r"(?s)<nav\b.*?</nav>", t):
            roh = re.sub(r"<[^>]+>", " ", nav)
            for wort in MENUE_VERBOTEN:
                if re.search(rf"\b{re.escape(wort)}\b", roh, re.I):
                    men.append(f"{f}: Menuepunkt {wort!r}")
            for p in INTERNE_PFADE:
                if f'href="{p}"' in nav:
                    men.append(f"{f}: Menue verlinkt {p}")
    befunde["Menueband"] = sorted(set(men))

    return befunde


def main(ref=None):
    q = Quelle(ref)
    befunde = pruefen(q)
    gesamt = 0
    print(f"Geprueft: {ref or 'Arbeitsverzeichnis'}")
    for name, liste in befunde.items():
        print(f"[{'ok  ' if not liste else 'FEHL'}] {name:18s} {len(liste)} Befund(e)")
        for z in liste[:10]:
            print(f"        {z}")
        if len(liste) > 10:
            print(f"        ... und {len(liste) - 10} weitere")
        gesamt += len(liste)
    print()
    print("DARF AUF MAIN" if gesamt == 0
          else f"{gesamt} Befund(e) - DARF NICHT AUF MAIN")
    return 1 if gesamt else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1] if len(sys.argv) > 1 else None))
