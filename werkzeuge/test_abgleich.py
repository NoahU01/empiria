#!/usr/bin/env python3
"""Test 2: Noahs Beispiel in einer Wegwerf-Kopie (nie im echten Ordner).

Aufruf: python3 werkzeuge/test_abgleich.py [TESTORDNER]   (Standard: ~/abgleich-test)
"""
import os, sys, shutil, subprocess, hashlib, json

REAL = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
T = os.path.abspath(sys.argv[1]) if len(sys.argv) > 1 else os.path.expanduser("~/abgleich-test")
ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0", GIT_AUTHOR_NAME="Test", GIT_AUTHOR_EMAIL="t@t",
           GIT_COMMITTER_NAME="Test", GIT_COMMITTER_EMAIL="t@t")
ok = True


def run(*a, cwd=None, check=True):
    r = subprocess.run(list(a), cwd=cwd or T, capture_output=True, text=True, env=ENV)
    if check and r.returncode != 0:
        print(r.stdout, r.stderr); raise SystemExit(f"Befehl fehlgeschlagen: {a}")
    return r.stdout


def check(name, cond):
    global ok
    print(("  OK    " if cond else "  FEHLER") + "  " + name)
    ok = ok and cond


def h(p):
    return hashlib.sha1(open(p, "rb").read()).hexdigest() if os.path.exists(p) else None


def rd(p):
    return open(p, encoding="utf-8").read()


def replace(p, old, new, count=1):
    s = rd(p)
    assert s.count(old) >= 1, f"Testvorbereitung: '{old[:40]}' nicht in {p}"
    open(p, "w", encoding="utf-8").write(s.replace(old, new, count))


if T.startswith(REAL):
    raise SystemExit("Testordner darf nicht im Projektordner liegen.")
if os.path.exists(T):
    shutil.rmtree(T)
print("Kopie anlegen …")
run("git", "clone", "-q", "--no-hardlinks", REAL, T, cwd=os.path.dirname(T))
shutil.copytree(os.path.join(REAL, "cowork-vorschau"), os.path.join(T, "cowork-vorschau"),
                ignore=shutil.ignore_patterns(".DS_Store"))
os.makedirs(os.path.join(T, "werkzeuge"), exist_ok=True)
for f in ("sync_lib.py", "abgleich.py", "sandbox_zu_github.py", "test_roundtrip.py", "entwicklung-menu.html", "entwicklung-menu.css", "entwicklung-menu.js"):
    shutil.copy(os.path.join(REAL, "werkzeuge", f), os.path.join(T, "werkzeuge", f))
S, G = os.path.join(T, "cowork-vorschau"), os.path.join(T, "site")
A = ["python3", os.path.join(T, "werkzeuge", "abgleich.py")]
run(*A, "start", "HEAD")
base = json.load(open(os.path.join(T, "werkzeuge", "abgleich-stand.json")))["ausgangspunkt"]

# ---- Daniel arbeitet in der Sandbox (nicht gepusht)
MARK_D = "<!-- TEST Daniel: neues Element auf Paid Ads -->"
replace(os.path.join(S, "paid-ads.html"), '  <section class="produkt-section pdf-dl-section">',
        f'  {MARK_D}\n  <section class="produkt-section test-daniel"><div class="container"><h2>Neu von Daniel</h2></div></section>\n  <section class="produkt-section pdf-dl-section">')
replace(os.path.join(S, "sparring.html"), "Volle Wirkung.</h1>", "Daniels Fassung.</h1>")

# ---- Noah pusht auf GitHub (hier: Commit im Test-Repo)
MARK_N = "Über KI wird geredet – TEST Noah hat diesen Satz geändert."
replace(os.path.join(G, "ki-zum-anfassen.html"), "Über KI wird geredet – oft von Menschen", MARK_N + " Oft von Menschen")
replace(os.path.join(G, "paid-ads.html"), '<a href="/paid-ads">Paid Ads</a>', '<a href="/paid-ads">Paid Ads (Noah)</a>')
replace(os.path.join(G, "sparring.html"), "Volle Wirkung.</h1>", "Noahs Fassung.</h1>")
open(os.path.join(G, "styles.css"), "a", encoding="utf-8").write("\n/* TEST Noah: neue Regel */\n.test-noah { color: red; }\n")
run("git", "commit", "-qam", "TEST Noah: KI, Paid-Ads-Menue, Sparring-Headline, styles.css")

before = {}
for dp, dn, fs in os.walk(S):
    for f in fs:
        p = os.path.join(dp, f); before[os.path.relpath(p, S)] = h(p)

print("\nLauf 1: holen")
out = run(*A, "holen", "--lokal")
print("\n".join("    " + l for l in out.splitlines()))
pa, ki, sp, css = (rd(os.path.join(S, f)) for f in ("paid-ads.html", "ki-zum-anfassen.html", "sparring.html", "styles.css"))
check("Paid Ads: Daniels neues Element ist noch da", MARK_D in pa and "Neu von Daniel" in pa)
check("Paid Ads: Noahs Menueaenderung ist angekommen", "Paid Ads (Noah)</a>" in pa)
check("Paid Ads: interne Menuepunkte (Impulsvortraege/capiamo/Archiv) noch da", pa.count(">capiamo<") == 2 and pa.count(">Archiv<") == 2)
check("Paid Ads: Links weiter relativ (file://)", 'href="styles.css"' in pa and 'href="/paid-ads"' not in pa)
check("KI zum Anfassen: Noahs Textaenderung ist angekommen", MARK_N in ki)
check("KI zum Anfassen: Daniels Download-Box (nicht gepusht) ist noch da", "pdf-dl-section" in ki)
check("Sparring: Konflikt erkannt, Sandbox-Datei unveraendert", "Daniels Fassung.</h1>" in sp and "Noahs Fassung" not in sp)
check("Sparring: Konfliktdatei mit beiden Fassungen abgelegt",
      os.path.exists(os.path.join(T, "_abgleich-konflikte", "sparring.html.konflikt.txt")))
check("styles.css: Noahs Regel ist drin", ".test-noah" in css)
check("styles.css: Daniels Download-Box-Regeln sind noch drin", ".pdf-dl--yellow" in css)
changed = {r for r in before if before[r] != h(os.path.join(S, r))}
check(f"Sonst keine Sandbox-Datei veraendert (geaendert: {sorted(changed)})",
      changed <= {"paid-ads.html", "ki-zum-anfassen.html", "styles.css"})
st = json.load(open(os.path.join(T, "werkzeuge", "abgleich-stand.json")))
check("Ausgangspunkt wegen Konflikt nicht weitergesetzt", st["ausgangspunkt"] == base)
check("Sicherung der Sandbox angelegt", os.path.isdir(os.path.join(T, "_sicherungen")) and os.listdir(os.path.join(T, "_sicherungen")))

print("\nLauf 2: holen erneut, Daniel entscheidet sich bei Sparring fuer seine Fassung")
out = run(*A, "holen", "--lokal", "--behalten", "sparring.html")
print("\n".join("    " + l for l in out.splitlines()))
st = json.load(open(os.path.join(T, "werkzeuge", "abgleich-stand.json")))
head = run("git", "rev-parse", "HEAD").strip()
check("Ausgangspunkt jetzt auf Noahs Commit", st["ausgangspunkt"] == head)
check("Paid Ads/KI unveraendert seit Lauf 1 (nichts doppelt eingefuegt)",
      rd(os.path.join(S, "paid-ads.html")) == pa and rd(os.path.join(S, "ki-zum-anfassen.html")) == ki)

print("\nLauf 3: Push vorbereiten")
out = run(*A, "push-vorbereiten", "--lokal")
print("\n".join("    " + l for l in out.splitlines() if not l.startswith("  - assets/downloads/")))
gpa, gki = rd(os.path.join(G, "paid-ads.html")), rd(os.path.join(G, "ki-zum-anfassen.html"))
check("site/paid-ads: Daniels Element + Noahs Menue", MARK_D in gpa and "Paid Ads (Noah)</a>" in gpa)
check("site/paid-ads: keine internen Menuepunkte", ">capiamo<" not in gpa and "Impulsvorträge<" not in gpa)
check("site/paid-ads: Linkschreibweise wie auf GitHub (absolut)", 'href="/styles.css"' in gpa)
check("site/ki: Noahs Satz bleibt erhalten", MARK_N in gki)
check("capiamo.html wird nicht uebertragen", not os.path.exists(os.path.join(G, "capiamo.html")))
check("strategie-aufsichtsrat.html wird nicht uebertragen", not os.path.exists(os.path.join(G, "strategie-aufsichtsrat.html")))
check("Sparring: Daniels Fassung geht raus (bewusst behalten)", "Daniels Fassung.</h1>" in rd(os.path.join(G, "sparring.html")))
check("Archiv-Schnappschuesse nicht nur wegen des internen Menues uebertragen",
      run("git", "diff", "--name-only", "--", "site/archiv").strip() == "")
check("index.html nicht nur wegen Leerzeilen uebertragen", run("git", "diff", "--name-only", "--", "site/index.html").strip() == "")
check("Seiten mit Link auf reine Sandbox-Seiten werden angehalten (impulsvortraege.html)",
      run("git", "diff", "--name-only", "--", "site/impulsvortraege.html").strip() == "" and "impulsvortraege.html" in out)
check("styles.css: in site/ Noahs Regel + Daniels Regeln", ".test-noah" in rd(os.path.join(G, "styles.css")) and ".pdf-dl--yellow" in rd(os.path.join(G, "styles.css")))
nd = run("git", "diff", "--numstat", "--", "site/paid-ads.html")
check(f"site/paid-ads: kleiner Diff statt Neuschreiben ({nd.strip()})", nd and int(nd.split()[0]) < 400)
print("\nDiff-Umfang site/ (Zeilen + / -):")
print("\n".join("    " + l for l in run("git", "diff", "--numstat", "--", "site").splitlines()))


print("\nLauf 4: Sicherung im Push-Weg – Noah pusht, Daniel will ohne Holen uebertragen")
run("git", "checkout", "-q", "--", "site"); run("git", "clean", "-fdq", "--", "site")
BARE, NOAH = T + "-remote.git", T + "-noah"
for p in (BARE, NOAH):
    if os.path.exists(p): shutil.rmtree(p)
run("git", "clone", "-q", "--bare", T, BARE)
run("git", "remote", "add", "test", BARE)
run("git", "fetch", "-q", "test")
run("git", "clone", "-q", "-b", "Daniel", BARE, NOAH, cwd=os.path.dirname(T))
replace(os.path.join(NOAH, "site", "medien.html"), "</title>", " (Noah)</title>")
run("git", "commit", "-qam", "TEST Noah: Medien-Titel", cwd=NOAH)
run("git", "push", "-q", "origin", "Daniel", cwd=NOAH)
ENV["ABGLEICH_REMOTE"] = "test"
r = subprocess.run(A + ["push-vorbereiten"], cwd=T, capture_output=True, text=True, env=ENV)
check("Push-Vorbereitung bricht ab, solange Noahs Stand nicht geholt ist", r.returncode != 0 and "erst" in (r.stdout + r.stderr).lower())
check("site/ dabei unveraendert", run("git", "status", "--porcelain", "--", "site").strip() == "")
out = run(*A, "holen")
check("Holen uebernimmt Noahs Medien-Aenderung in die Sandbox", "(Noah)</title>" in rd(os.path.join(S, "medien.html")))
check("Holen hat Daniels Download-Box auf Medien behalten", "pdf-dl-section" in rd(os.path.join(S, "medien.html")))
r = subprocess.run(A + ["push-vorbereiten"], cwd=T, capture_output=True, text=True, env=ENV)
check("Danach klappt die Push-Vorbereitung", r.returncode == 0 and "(Noah)</title>" in rd(os.path.join(G, "medien.html")))
for p in (BARE, NOAH):
    shutil.rmtree(p, ignore_errors=True)
print("\nTEST 2 BESTANDEN" if ok else "\nTEST 2 FEHLGESCHLAGEN")
sys.exit(0 if ok else 1)
