#!/usr/bin/env python3
"""Abgleich zwischen Sandbox (cowork-vorschau/) und GitHub (site/ im Branch Daniel).

  python3 werkzeuge/abgleich.py status              zeigt nur an, was passieren wuerde
  python3 werkzeuge/abgleich.py holen               GitHub -> Sandbox  ("Hol den aktuellen Stand")
  python3 werkzeuge/abgleich.py push-vorbereiten    Sandbox -> site/   ("Bereite den Push vor")
  python3 werkzeuge/abgleich.py start <commit>      Ausgangspunkt einmalig setzen

Optionen:
  --lokal            kein git fetch/merge, mit dem aktuellen lokalen Stand arbeiten
  --behalten <datei> bei einem Konflikt bewusst die Sandbox-Version behalten (mehrfach moeglich)

Regeln (pro Datei, gegen den Ausgangspunkt = letzter abgeglichener GitHub-Commit):
  nur GitHub geaendert   -> Sandbox wird aktualisiert
  nur Sandbox geaendert  -> Sandbox bleibt unangetastet
  beide geaendert        -> zeilengenau zusammenfuehren; gleiche Stelle -> Konflikt, nichts wird ueberschrieben
Es wird nie etwas geloescht und nie gepusht.
"""
import os, sys, json, subprocess, tempfile, tarfile, datetime, difflib, shutil
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from sync_lib import *

BRANCH = os.environ.get("ABGLEICH_BRANCH", "Daniel")
REMOTE = os.environ.get("ABGLEICH_REMOTE", "origin")
STATE = os.path.join(ROOT, "werkzeuge", "abgleich-stand.json")
BACKUPS = os.path.join(ROOT, "_sicherungen")
KONFLIKTE = os.path.join(ROOT, "_abgleich-konflikte")
BERICHT = os.path.join(ROOT, "werkzeuge", "abgleich-letzter-bericht.txt")
ENV = dict(os.environ, GIT_OPTIONAL_LOCKS="0")


# ---------------------------------------------------------------- Hilfen
def git(*args, check=True, binary=False):
    r = subprocess.run(["git", "-C", ROOT, *args], capture_output=True, env=ENV)
    if check and r.returncode != 0:
        raise SystemExit(f"git {' '.join(args)} fehlgeschlagen:\n{r.stderr.decode(errors='replace')}")
    return r.stdout if binary else r.stdout.decode("utf-8", errors="replace").strip()


def git_ok(*args):
    return subprocess.run(["git", "-C", ROOT, *args], capture_output=True, env=ENV).returncode == 0


def show(commit, rel):
    r = subprocess.run(["git", "-C", ROOT, "show", f"{commit}:site/{rel}"], capture_output=True, env=ENV)
    return r.stdout if r.returncode == 0 else None


def read(path):
    try:
        with open(path, "rb") as f:
            return f.read()
    except FileNotFoundError:
        return None


def write(path, data, probe):
    if probe:
        return
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "wb") as f:
        f.write(data)


def dec(b):
    return None if b is None else b.decode("utf-8")


def load_state():
    if not os.path.exists(STATE):
        raise SystemExit("Kein Ausgangspunkt gesetzt. Einmalig: python3 werkzeuge/abgleich.py start <commit>")
    return json.load(open(STATE, encoding="utf-8"))


def save_state(st, probe):
    if not probe:
        st["aktualisiert"] = datetime.datetime.now().isoformat(timespec="seconds")
        json.dump(st, open(STATE, "w", encoding="utf-8"), indent=2, ensure_ascii=False)


def html_exists(p):
    return os.path.exists(os.path.join(SANDBOX, p + ".html")) or os.path.exists(os.path.join(SITE, p + ".html"))


def preserve(candidate, original, rel):
    """Uebernimmt Zeilen, die inhaltlich gleich geblieben sind, in ihrer bisherigen Schreibweise."""
    if original is None:
        return candidate
    rd = rel_dir_of(rel)
    key = (lambda l: to_absolute(l, rd)) if rel.endswith(".html") else (lambda l: l)
    c, o = candidate.split("\n"), original.split("\n")
    sm = difflib.SequenceMatcher(None, [key(x) for x in c], [key(x) for x in o], autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        out += o[j1:j2] if tag == "equal" else c[i1:i2]
    return "\n".join(out)


def same(a, b):
    """Gleich bis auf Leerzeilen und Leerzeichen am Zeilenende."""
    if a is None or b is None:
        return a is b
    k = lambda t: [l.rstrip() for l in t.split("\n") if l.strip()]
    return k(a) == k(b)


def resolve_additions(merged):
    """Konflikte, bei denen beide Seiten an derselben Stelle nur etwas HINZUGEFUEGT haben
    (z. B. neue Regeln am Ende von styles.css), werden aufgeloest: erst Sandbox, dann GitHub."""
    out, rest, lines, i = [], 0, merged.split("\n"), 0
    while i < len(lines):
        if lines[i].startswith("<<<<<<< "):
            j = i + 1
            ours, base, theirs, part = [], [], [], "ours"
            while j < len(lines) and not lines[j].startswith(">>>>>>> "):
                l = lines[j]
                if l.startswith("||||||| "): part = "base"
                elif l == "=======": part = "theirs"
                else: {"ours": ours, "base": base, "theirs": theirs}[part].append(l)
                j += 1
            if not any(x.strip() for x in base):
                out += ours + theirs
            else:
                out += lines[i:j + 1]
                rest += 1
            i = j + 1
            continue
        out.append(lines[i])
        i += 1
    return rest, "\n".join(out)


def merge3(ours, base, theirs, rel=""):
    with tempfile.TemporaryDirectory() as d:
        paths = []
        for name, t in (("sandbox", ours), ("ausgangspunkt", base or ""), ("github", theirs)):
            p = os.path.join(d, name)
            open(p, "w", encoding="utf-8").write(t)
            paths.append(p)
        r = subprocess.run(["git", "merge-file", "-p", "--diff3", "-L", "Sandbox (Daniel)", "-L", "Ausgangspunkt", "-L", "GitHub",
                            *paths], capture_output=True, env=ENV)
        rc, merged = r.returncode, r.stdout.decode("utf-8")
        if rc > 0 and rel.endswith((".css", ".js")):
            rc, merged = resolve_additions(merged)
        return rc, merged


def backup(probe):
    if probe:
        return None
    os.makedirs(BACKUPS, exist_ok=True)
    name = os.path.join(BACKUPS, "sandbox-" + datetime.datetime.now().strftime("%Y%m%d-%H%M%S") + ".tar.gz")
    with tarfile.open(name, "w:gz") as tar:
        tar.add(SANDBOX, arcname="cowork-vorschau", filter=lambda ti: None if ".DS_Store" in ti.name else ti)
    return name


class Report:
    def __init__(self, title):
        self.title, self.groups = title, {}

    def add(self, group, rel, note=""):
        self.groups.setdefault(group, []).append((rel, note))

    def text(self):
        lines = [self.title, ""]
        for g, items in self.groups.items():
            lines.append(f"{g} ({len(items)}):")
            lines += [f"  - {r}" + (f"  – {n}" if n else "") for r, n in items]
            lines.append("")
        return "\n".join(lines)


# ---------------------------------------------------------------- holen: GitHub -> Sandbox
def holen(probe, lokal, behalten):
    st = load_state()
    base = st["ausgangspunkt"]
    if not lokal:
        if git("rev-parse", "--abbrev-ref", "HEAD") != BRANCH:
            raise SystemExit(f"Im Repo ist nicht der Branch {BRANCH} ausgecheckt – abgebrochen.")
        if git("status", "--porcelain", "--", "site"):
            raise SystemExit("site/ hat uncommittete Aenderungen (vorbereiteter Push?) – erst committen, dann holen.")
        git("fetch", REMOTE, BRANCH)
        if not probe and not git_ok("merge", "--ff-only", f"{REMOTE}/{BRANCH}"):
            raise SystemExit(f"Lokaler Branch und {REMOTE}/{BRANCH} sind auseinandergelaufen "
                             "(lokale Commits noch nicht gepusht?). Erst pushen lassen, dann holen.")
    head = git("rev-parse", f"{REMOTE}/{BRANCH}") if (probe and not lokal) else git("rev-parse", "HEAD")
    rep = Report(f"Abgleich GitHub -> Sandbox   Ausgangspunkt {base[:7]} -> GitHub {head[:7]}" + ("   [NUR ANZEIGE]" if probe else ""))
    if base == head:
        rep.add("Nichts Neues auf GitHub", "–")
        return finish(rep, st, probe, advance=None)

    diff = git("diff", "--no-renames", "--name-status", base, head, "--", "site")
    files = []
    for line in diff.splitlines():
        status, path = line.split("\t", 1)
        files.append((status, path[len("site/"):]))
    if not files:
        rep.add("GitHub hat nichts an site/ geaendert", "–")
        return finish(rep, st, probe, advance=head)

    bk = backup(probe)
    if bk:
        rep.add("Sicherung angelegt", os.path.relpath(bk, ROOT))
    tpl = intern_template(dec(read(os.path.join(SANDBOX, "index.html"))))
    konflikt = False

    for status, rel in sorted(files, key=lambda x: x[1]):
        if ignored(rel):
            continue
        spath = os.path.join(SANDBOX, rel)
        b_base, b_theirs, b_ours = show(base, rel), show(head, rel), read(spath)
        if b_theirs is None:
            rep.add("Auf GitHub geloescht – in der Sandbox bewusst stehen gelassen", rel)
            continue
        if is_text(rel):
            base_n = normalize(dec(b_base), rel) if b_base is not None else None
            theirs_n = normalize(dec(b_theirs), rel)
            ours = dec(b_ours)
            ours_n = normalize(ours, rel) if ours is not None else None
            if same(base_n, theirs_n):
                rep.add("Nur Schreibweise geaendert – nichts zu tun", rel)
            elif ours is None:
                write(spath, render_sandbox(theirs_n, rel, tpl, html_exists).encode(), probe)
                rep.add("Neu von GitHub uebernommen", rel)
            elif same(ours_n, theirs_n):
                rep.add("Bereits gleich", rel)
            elif same(ours_n, base_n):
                write(spath, preserve(render_sandbox(theirs_n, rel, tpl, html_exists), ours, rel).encode(), probe)
                rep.add("Von GitHub uebernommen (Sandbox war unveraendert)", rel)
            elif rel in behalten:
                rep.add("Sandbox-Version bewusst behalten", rel)
            else:
                rc, merged = merge3(ours_n, base_n, theirs_n, rel)
                if rc == 0:
                    write(spath, preserve(render_sandbox(merged, rel, tpl, html_exists), ours, rel).encode(), probe)
                    rep.add("Zusammengefuehrt (Daniel + GitHub, verschiedene Stellen)", rel)
                else:
                    konflikt = True
                    kp = os.path.join(KONFLIKTE, rel + ".konflikt.txt")
                    write(kp, merged.encode(), probe)
                    write(os.path.join(KONFLIKTE, rel + ".github" + os.path.splitext(rel)[1]),
                          render_sandbox(theirs_n, rel, tpl, html_exists).encode(), probe)
                    rep.add("KONFLIKT – Sandbox NICHT veraendert, bitte entscheiden", rel,
                            f"{rc} Stelle(n), siehe {os.path.relpath(kp, ROOT)}")
        else:
            if b_ours == b_theirs:
                rep.add("Bereits gleich", rel)
            elif b_ours is None or b_ours == b_base:
                write(spath, b_theirs, probe)
                rep.add("Von GitHub uebernommen (Datei)", rel)
            elif rel in behalten:
                rep.add("Sandbox-Version bewusst behalten", rel)
            else:
                konflikt = True
                write(os.path.join(KONFLIKTE, rel + ".github" + os.path.splitext(rel)[1]), b_theirs, probe)
                rep.add("KONFLIKT – Datei in beiden geaendert, Sandbox NICHT veraendert", rel,
                        f"GitHub-Version unter {os.path.relpath(KONFLIKTE, ROOT)}/")
    if konflikt:
        rep.add("Ausgangspunkt NICHT weitergesetzt", "–",
                "nach der Entscheidung erneut holen (ggf. mit --behalten <datei>)")
    return finish(rep, st, probe, advance=None if konflikt else head)


# ---------------------------------------------------------------- push-vorbereiten: Sandbox -> site/
def push_vorbereiten(probe, lokal):
    st = load_state()
    base = st["ausgangspunkt"]
    if not lokal:
        git("fetch", REMOTE, BRANCH)
        remote = git("rev-parse", f"{REMOTE}/{BRANCH}")
        if not git_ok("merge-base", "--is-ancestor", remote, base):
            raise SystemExit("Auf GitHub gibt es Neues, das noch nicht in der Sandbox ist.\n"
                             "Erst: python3 werkzeuge/abgleich.py holen   – dann erneut vorbereiten.")
        if not git_ok("merge-base", "--is-ancestor", remote, "HEAD"):
            raise SystemExit(f"Lokaler Branch enthaelt {REMOTE}/{BRANCH} nicht – erst holen.")
    rep = Report("Push vorbereiten: Sandbox -> site/" + ("   [NUR ANZEIGE]" if probe else ""))
    seen = set()
    for dp, dn, fs in os.walk(SANDBOX):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in sorted(fs):
            rel = os.path.relpath(os.path.join(dp, f), SANDBOX).replace(os.sep, "/")
            if ignored(rel):
                continue
            seen.add(rel)
            if sandbox_only(rel):
                rep.add("Nur Sandbox – nicht uebertragen", rel)
                continue
            tpath = os.path.join(SITE, rel)
            b_ours, b_site = read(os.path.join(dp, f)), read(tpath)
            if is_text(rel):
                ours_n = normalize(dec(b_ours), rel)
                site_txt = dec(b_site)
                if b_site is not None and same(normalize(site_txt, rel), ours_n):
                    continue
                if is_archiv(rel) and b_site is not None and same(remove_intern_blocks(normalize(site_txt, rel)),
                                                                   remove_intern_blocks(ours_n)):
                    continue  # nur das (interne) Menue im Archiv-Schnappschuss weicht ab
                bad = sandbox_links(ours_n if not is_archiv(rel) else ours_n)
                if rel.endswith(".html") and bad:
                    rep.add("NICHT uebertragen – verlinkt eine reine Sandbox-Seite, bitte klaeren", rel, ", ".join(bad))
                    continue
                style = link_style(site_txt) if site_txt else "absolute"
                out = preserve(render_site(ours_n, rel, style, html_exists), site_txt, rel)
                if rel.endswith(".html") and not is_archiv(rel) and intern_in_menu(out):
                    raise SystemExit(f"SICHERHEITSSTOPP: interne Menuepunkte in {rel} – nichts geschrieben.")
                write(tpath, out.encode(), probe)
            else:
                if b_ours == b_site:
                    continue
                write(tpath, b_ours, probe)
            rep.add("Neu in site/" if b_site is None else "Geaendert in site/", rel)
    for dp, dn, fs in os.walk(SITE):
        dn[:] = [d for d in dn if d not in (".git", "node_modules")]
        for f in fs:
            rel = os.path.relpath(os.path.join(dp, f), SITE).replace(os.sep, "/")
            if not ignored(rel) and rel not in seen:
                rep.add("Nur auf GitHub (nicht angefasst)", rel)
    if "Geaendert in site/" not in rep.groups and "Neu in site/" not in rep.groups:
        rep.add("Keine Aenderungen zu uebertragen", "–")
    elif not probe:
        rep.add("Naechster Schritt", "–", "Aenderungen pruefen, committen; Daniel pusht selbst in VS Code (git push origin Daniel)")
    return finish(rep, st, probe, advance=None)


def sandbox_links(norm_text):
    pages = [p[1:].replace("\\.html$", "").replace("\\", "") for p in SANDBOX_ONLY if p.endswith(".html$")]
    found = []
    for p in pages:
        if re.search(r'href="/' + re.escape(p) + r'(\.html)?["#?]', norm_text):
            found.append("/" + p)
    return found


def finish(rep, st, probe, advance):
    if advance and not probe:
        st["ausgangspunkt"] = advance
        save_state(st, probe)
        rep.add("Neuer Ausgangspunkt", advance[:7])
    txt = rep.text()
    print(txt)
    if not probe:
        open(BERICHT, "w", encoding="utf-8").write(txt)
    return rep


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return
    cmd = args[0]
    lokal = "--lokal" in args
    behalten = {args[i + 1] for i, a in enumerate(args) if a == "--behalten" and i + 1 < len(args)}
    if cmd == "start":
        commit = git("rev-parse", args[1])
        save_state({"ausgangspunkt": commit, "branch": BRANCH}, False)
        print("Ausgangspunkt gesetzt:", commit[:7])
    elif cmd == "status":
        holen(True, lokal, behalten)
        print("-" * 60)
        push_vorbereiten(True, True)
    elif cmd == "holen":
        holen(False, lokal, behalten)
    elif cmd == "push-vorbereiten":
        push_vorbereiten(False, lokal)
    else:
        raise SystemExit(__doc__)


if __name__ == "__main__":
    main()
