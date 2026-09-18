"""Einmalig: interne Menuegruppen aus dem Leistungen-Menue in "/ Entwicklung /" verschieben (nur Sandbox)."""
import os, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_lib import *
tpl = intern_template()
def html_exists(p): return os.path.exists(os.path.join(SANDBOX, p + ".html")) or os.path.exists(os.path.join(SITE, p + ".html"))
probe = "--probe" in sys.argv
n = 0
for dp, dn, fs in os.walk(SANDBOX):
    dn[:] = [d for d in dn if d not in (".git", "node_modules")]
    for f in sorted(fs):
        rel = os.path.relpath(os.path.join(dp, f), SANDBOX).replace(os.sep, "/")
        if not rel.endswith(".html") or ignored(rel) or is_archiv(rel):
            continue
        p = os.path.join(dp, f); t = open(p, encoding="utf-8").read()
        if not re.search(r'class="[^"]*\bnav-cta\b', t):
            print("  ohne Menueband (unveraendert):", rel); continue
        legacy = len(find_intern_blocks(t.split("\n")))
        base = remove_intern_blocks(t)
        lines = base.split("\n")
        for kind in ("mobile", "desktop"):
            if kind == "mobile" and "mobile-submenu" not in base: continue
            a = entwicklung_anchor(lines, kind)
            if a is None: print("  KEIN ANKER", kind, rel); continue
            block = to_relative("\n".join(tpl[kind]), rel_dir_of(rel), html_exists).split("\n")
            lines[a:a] = block
        out = "\n".join(lines)
        if out != t:
            n += 1
            if not probe: open(p, "w", encoding="utf-8").write(out)
            print(f"  {rel}: {legacy} alte Gruppen entfernt, Entwicklung eingesetzt")
print(("[Probe] " if probe else "") + f"{n} Seiten angepasst")
