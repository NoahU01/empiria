"""Test 1: verlustfreie Uebersetzung. Aufruf: python3 werkzeuge/test_roundtrip.py"""
import os, sys, difflib
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_lib import *

tpl = intern_template(open(os.path.join(SANDBOX, "index.html"), encoding="utf-8").read())
def html_exists(p): return os.path.exists(os.path.join(SANDBOX, p + ".html")) or os.path.exists(os.path.join(SITE, p + ".html"))

def walk(base):
    for dp, dn, fs in os.walk(base):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in fs:
            rel = os.path.relpath(os.path.join(dp, f), base).replace(os.sep, "/")
            if not ignored(rel) and rel.endswith(".html"):
                yield rel, open(os.path.join(dp, f), encoding="utf-8").read()

fail = 0
stats = {"identisch": 0, "gleichwertige Linkschreibweise": 0, "internes Menue an Startseite angeglichen": 0}
for rel, t in walk(SANDBOX):
    back = render_sandbox(normalize(t, rel), rel, tpl, html_exists)
    if back == t: stats["identisch"] += 1; continue
    if to_absolute(back, rel_dir_of(rel)) == to_absolute(t, rel_dir_of(rel)): stats["gleichwertige Linkschreibweise"] += 1; continue
    if normalize(back, rel) == normalize(t, rel):
        stats["internes Menue an Startseite angeglichen"] += 1; print("  Info: internes Menue weicht von Startseite ab:", rel); continue
    fail += 1
    d = list(difflib.unified_diff(t.split("\n"), back.split("\n"), lineterm="", n=0)); print("FEHLER Sandbox:", rel); print("\n".join(d[:14]))
print("Sandbox:", stats)
ok = 0; n = 0
for rel, t in walk(SITE):
    n += 1
    back = render_site(normalize(t, rel), rel, link_style(t), html_exists)
    if back == t or to_absolute(back, rel_dir_of(rel)) == to_absolute(t, rel_dir_of(rel)): ok += 1; continue
    fail += 1
    d = list(difflib.unified_diff(t.split("\n"), back.split("\n"), lineterm="", n=0)); print("FEHLER site:", rel); print("\n".join(d[:14]))
print(f"site: {ok}/{n} gleichwertig")
print("TEST 1 BESTANDEN" if fail == 0 else f"TEST 1 FEHLGESCHLAGEN ({fail})")
sys.exit(1 if fail else 0)
