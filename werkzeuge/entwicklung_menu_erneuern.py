#!/usr/bin/env python3
"""Spielt das Entwicklungsmenue aus der Vorlage in alle Seiten zurueck.

Das Menue steht in jeder Seite als Kopie zwischen den ENTWICKLUNG-Markern -
30 Dateien von Hand zu aendern waere fehleranfaellig. Quelle ist immer
werkzeuge/entwicklung-menu.(html|css|js); hier wird der alte Block entfernt
und der aktuelle eingesetzt, Desktop- und Mobilfassung getrennt.

Es wird nur angefasst, was schon ein Menueband hat (Seiten mit .nav-cta).
Das Archiv bleibt aussen vor.

Aufruf:
    python3 werkzeuge/entwicklung_menu_erneuern.py            # anwenden
    python3 werkzeuge/entwicklung_menu_erneuern.py --probe    # nur zeigen
"""
import os, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from sync_lib import (SITE, intern_template, remove_intern_blocks,  # noqa: E402
                      entwicklung_anchor, to_relative, rel_dir_of, ignored, is_archiv)

_nav_cta = re.compile(r'class="[^"]*\bnav-cta\b')


def html_exists(p):
    return os.path.exists(os.path.join(SITE, p + ".html"))


def main(probe=False):
    tpl = intern_template()
    geaendert, uebersprungen = 0, 0
    for dp, dn, fs in os.walk(SITE):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(dp, f), SITE).replace(os.sep, "/")
            if not rel.endswith(".html") or ignored(rel) or is_archiv(rel):
                continue
            p = os.path.join(dp, f)
            t = open(p, encoding="utf-8").read()
            if not _nav_cta.search(t):
                uebersprungen += 1
                continue
            lines = remove_intern_blocks(t).split("\n")
            fehlt = []
            for kind in ("mobile", "desktop"):
                if kind == "mobile" and "mobile-submenu" not in t:
                    continue
                a = entwicklung_anchor(lines, kind)
                if a is None:
                    fehlt.append(kind)
                    continue
                block = to_relative("\n".join(tpl[kind]), rel_dir_of(rel), html_exists)
                lines[a:a] = block.split("\n")
            if fehlt:
                print(f"  KEIN ANKER ({', '.join(fehlt)}): {rel}")
            neu = "\n".join(lines)
            if neu != t:
                geaendert += 1
                if not probe:
                    open(p, "w", encoding="utf-8").write(neu)
    print(("[Probe] " if probe else "")
          + f"{geaendert} Seiten erneuert, {uebersprungen} ohne Menueband uebersprungen")
    return 0


if __name__ == "__main__":
    sys.exit(main("--probe" in sys.argv))
