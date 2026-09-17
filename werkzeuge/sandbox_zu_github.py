#!/usr/bin/env python3
"""Erzeugt aus der Sandbox (cowork-vorschau/) die saubere GitHub-Version.

1. Entfernt die internen Menuepunkte "Impulsvortraege" und "Archiv"
   (Desktop-Dropdown + mobiles Menue) aus allen HTML-Seiten.
2. Wandelt relative Links (fuer den Browser per file://) in absolute
   "schoene" Links fuer Vercel um (z. B. marketing.html -> /marketing).

Aufruf:  python3 werkzeuge/sandbox_zu_github.py [ZIELORDNER]
Standard-Ziel: ./github-build  (danach nach site/ uebernehmen)
Hinweis: fuer den taeglichen Ablauf gibt es werkzeuge/abgleich.py (holen / push-vorbereiten).
"""
import os, re, shutil, sys, posixpath
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_lib import remove_intern_blocks as _remove_sandbox_only

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "cowork-vorschau")
_args = [a for a in sys.argv[1:] if not a.startswith("--")]
OUT = os.path.abspath(_args[0]) if _args else os.path.join(ROOT, "github-build")

INTERN = ("Impulsvorträge", "capiamo", "Archiv")
# Seiten, deren Links ihre .html-Endung behalten
KEEP_HTML = {"index", "datenschutz", "impressum", "kontakt"}


def remove_intern_blocks(text):
    lines = text.split("\n")
    out, i = [], 0
    divider = re.compile(r'^\s*<div class="(nav-dropdown-divider|mobile-submenu-divider)"></div>\s*$')
    opener = re.compile(r'^\s*<div class="(nav-item--subdropdown|mobile-submenu-group)">\s*$')
    while i < len(lines):
        if divider.match(lines[i]) and i + 1 < len(lines) and opener.match(lines[i + 1]):
            # Block ab i+1 bis zum passenden </div> finden
            depth, j = 0, i + 1
            while j < len(lines):
                depth += len(re.findall(r"<div\b", lines[j])) - len(re.findall(r"</div>", lines[j]))
                if depth <= 0:
                    break
                j += 1
            head = "\n".join(lines[i + 1:i + 4])
            m = re.search(r">\s*(Impulsvorträge|capiamo|Archiv)\s*</(a|span)>", head)
            if m:
                i = j + 1
                continue
        out.append(lines[i])
        i += 1
    return "\n".join(out)


def to_absolute(text, rel_dir):
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if re.match(r"^([a-z]+:|/|#|\{|data:)", url, re.I) or url == "":
            return m.group(0)
        path, sep, frag = url.partition("#")
        path, qsep, query = path.partition("?")
        absp = posixpath.normpath(posixpath.join("/" + rel_dir, path))
        if path.endswith("/"):
            absp += "/"
        base = posixpath.basename(absp)
        if attr == "href" and absp.endswith(".html") and base[:-5] not in KEEP_HTML:
            absp = absp[:-5]
        return f'{attr}="{absp}{qsep}{query}{sep}{frag}"'
    return re.sub(r'\b(href|src)="([^"]*)"', fix, text)


def pruefe_abgleich():
    """Sicherung: nicht uebertragen, solange auf GitHub Neues liegt, das die Sandbox noch nicht hat."""
    if "--ohne-pruefung" in sys.argv:
        return
    import json, subprocess
    state = os.path.join(ROOT, "werkzeuge", "abgleich-stand.json")
    if not os.path.exists(state):
        return
    base = json.load(open(state, encoding="utf-8"))["ausgangspunkt"]
    env = dict(os.environ, GIT_OPTIONAL_LOCKS="0")
    subprocess.run(["git", "-C", ROOT, "fetch", "origin", "Daniel"], capture_output=True, env=env)
    r = subprocess.run(["git", "-C", ROOT, "merge-base", "--is-ancestor", "origin/Daniel", base], capture_output=True, env=env)
    if r.returncode != 0:
        print("ABBRUCH: Auf GitHub gibt es Neues, das noch nicht in der Sandbox ist.\n"
              "Erst: python3 werkzeuge/abgleich.py holen")
        sys.exit(1)


def main():
    pruefe_abgleich()
    if os.path.exists(OUT):
        shutil.rmtree(OUT)
    shutil.copytree(SRC, OUT, ignore=shutil.ignore_patterns(".DS_Store", ".git"))
    for dp, _, files in os.walk(OUT):
        for f in files:
            if not f.endswith(".html"):
                continue
            p = os.path.join(dp, f)
            rel_dir = os.path.relpath(dp, OUT).replace(os.sep, "/")
            rel_dir = "" if rel_dir == "." else rel_dir
            t = open(p, encoding="utf-8").read()
            # archiv/ = statische Schnappschuesse, Menue dort unveraendert lassen
            if rel_dir.startswith("archiv"):
                t2 = to_absolute(t, rel_dir)
            else:
                t2 = to_absolute(_remove_sandbox_only(t), rel_dir)
            if t2 != t:
                open(p, "w", encoding="utf-8").write(t2)
    # Sicherheitspruefung: keine internen Menuepunkte mehr im Menue
    bad = []
    for dp, _, files in os.walk(OUT):
        for f in files:
            if f.endswith(".html") and "/archiv" not in dp.replace(os.sep, "/"):
                t = open(os.path.join(dp, f), encoding="utf-8").read()
                if "ENTWICKLUNG:START" in t or "data-dev-dd" in t or re.search(r'sub-trigger[^>]*>\s*(Impulsvorträge|capiamo|Archiv)\s*<|submenu-label[^>]*>\s*(Impulsvorträge|capiamo|Archiv)\s*<', t):
                    bad.append(os.path.relpath(os.path.join(dp, f), OUT))
    if bad:
        print("FEHLER: interne Menuepunkte noch vorhanden in:", *bad, sep="\n  ")
        sys.exit(1)
    print("OK ->", OUT)


if __name__ == "__main__":
    main()
