"""Gemeinsame Bausteine fuer den Abgleich Sandbox <-> GitHub (site/).

Drei Formate derselben Seite:
  sandbox    relative Links (file://), mit internen Menuepunkten (Impulsvortraege, capiamo, Archiv)
  normal     absolute Links, ohne interne Menuepunkte  -> hier wird verglichen und zusammengefuehrt
  site       wie auf GitHub: je nach Datei absolute ODER relative Links, ohne interne Menuepunkte
"""
import os, re, posixpath, hashlib

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SANDBOX = os.path.join(ROOT, "cowork-vorschau")
SITE = os.path.join(ROOT, "site")

KEEP_HTML = {"index", "datenschutz", "impressum", "kontakt"}
INTERN_LABELS = ("Impulsvorträge", "capiamo", "Archiv")

# Dateien, die nur in der Sandbox leben und nie nach site/ uebertragen werden
SANDBOX_ONLY = [
    r"^capiamo\.html$",
    r"^assets/downloads/empiria-capiamo[^/]*$",
    r"^assets/ansprechpartner-rick\.webp$",
    r"^strategie-aufsichtsrat\.html$",
    r"^assets/downloads/empiria-strategie-fuer-aufsichtsraete[^/]*$",
]
# Nie anfassen (weder holen noch uebertragen)
IGNORE = [r"(^|/)\.DS_Store$", r"(^|/)\.git(/|$)", r"(^|/)node_modules(/|$)", r"^_pdfsrc_", r"^_pdf_"]


def ignored(rel):
    return any(re.search(p, rel) for p in IGNORE)


def sandbox_only(rel):
    return any(re.search(p, rel) for p in SANDBOX_ONLY)


def is_text(rel):
    return rel.lower().endswith((".html", ".css", ".js", ".mjs", ".json", ".txt", ".xml", ".svg", ".md", ".py"))


def sha(data):
    return hashlib.sha1(data).hexdigest()


# ---------------------------------------------------------------- Menue
_divider = re.compile(r'^\s*<div class="(nav-dropdown-divider|mobile-submenu-divider)"></div>\s*$')
_opener = re.compile(r'^\s*<div class="(nav-item--subdropdown|mobile-submenu-group)">\s*$')
_label = re.compile(r">\s*(Impulsvorträge|capiamo|Archiv)\s*</(a|span)>")


def find_intern_blocks(lines):
    """Liefert [(start, ende_exklusiv, art)] der internen Menueblöcke (Trenner + Gruppe)."""
    blocks, i = [], 0
    while i < len(lines):
        m = _divider.match(lines[i])
        if m and i + 1 < len(lines) and _opener.match(lines[i + 1]):
            depth, j = 0, i + 1
            while j < len(lines):
                depth += len(re.findall(r"<div\b", lines[j])) - len(re.findall(r"</div>", lines[j]))
                if depth <= 0:
                    break
                j += 1
            if _label.search("\n".join(lines[i + 1:i + 4])):
                kind = "desktop" if m.group(1) == "nav-dropdown-divider" else "mobile"
                blocks.append((i, j + 1, kind))
                i = j + 1
                continue
        i += 1
    return blocks


def remove_intern_blocks(text):
    """Entfernt alles, was nur in die Sandbox gehoert: den Menuepunkt "/ Entwicklung /"
    und (Altbestand) interne Gruppen Impulsvortraege/capiamo/Archiv im Leistungen-Menue."""
    lines = remove_entwicklung(text.split("\n"))
    out, last = [], 0
    for s, e, _ in find_intern_blocks(lines):
        out += lines[last:s]
        last = e
    out += lines[last:]
    return "\n".join(out)


_desktop_end = re.compile(r"^\s*</nav>\s*$")
_mobile_start = re.compile(r'<nav class="mobile-menu"')
_mobile_end = re.compile(r'^\s*<a class="btn btn--dark"')


def _anchor(lines, kind):
    """Zeilenindex des Ankers: erstes </nav> (Desktop) bzw. Kontakt-Button im mobilen Menue."""
    if kind == "desktop":
        for k, l in enumerate(lines):
            if _desktop_end.match(l):
                return k
        return None
    start = next((k for k, l in enumerate(lines) if _mobile_start.search(l)), None)
    if start is None:
        return None
    for k in range(start, len(lines)):
        if _mobile_end.match(lines[k]):
            return k
    return None


WERKZEUGE = os.path.dirname(os.path.abspath(__file__))
ENTW_START = "<!-- ENTWICKLUNG:START (nur Sandbox – wird beim Push automatisch entfernt) -->"
ENTW_END = "<!-- ENTWICKLUNG:END -->"
_entw_start = re.compile(r"<!-- ENTWICKLUNG:START")
_entw_end = re.compile(r"<!-- ENTWICKLUNG:END -->")
_nav_cta = re.compile(r'class="[^"]*\bnav-cta\b')


def remove_entwicklung(lines):
    out, skip = [], False
    for l in lines:
        if _entw_start.search(l):
            skip = True
        if not skip:
            out.append(l)
        if skip and _entw_end.search(l):
            skip = False
    return out


def intern_template(_unused=None):
    """Menuepunkt "/ Entwicklung /" aus werkzeuge/entwicklung-menu.(html|css|js), im Normalformat (absolute Links)."""
    rd = lambda n: open(os.path.join(WERKZEUGE, n), encoding="utf-8").read().strip("\n")
    html, css, js = rd("entwicklung-menu.html"), rd("entwicklung-menu.css"), rd("entwicklung-menu.js")
    desk = html.replace('class="dev-dd"', 'class="dev-dd dev-dd--desktop"', 1)
    mob = html.replace('class="dev-dd"', 'class="dev-dd dev-dd--mobile"', 1)
    return {
        "desktop": [ENTW_START, *desk.split("\n"), "<style>", *css.split("\n"), "</style>",
                    "<script>", *js.split("\n"), "</script>", ENTW_END],
        "mobile": [ENTW_START, *mob.split("\n"), ENTW_END],
    }


def entwicklung_anchor(lines, kind):
    """Desktop: vor dem Kontakt-Button im Menueband. Mobil: vor dem Kontakt-Button im mobilen Menue."""
    if kind == "desktop":
        return next((k for k, l in enumerate(lines) if _nav_cta.search(l)), None)
    return _anchor(lines, "mobile")


def insert_intern_blocks(norm_text, tpl):
    lines = norm_text.split("\n")
    for kind in ("mobile", "desktop"):
        if kind == "mobile" and "mobile-submenu" not in norm_text:
            continue
        a = entwicklung_anchor(lines, kind)
        if a is None:
            continue
        lines[a:a] = tpl[kind]
    return "\n".join(lines)


# ---------------------------------------------------------------- Links
_attr = re.compile(r'\b(href|src)="([^"]*)"')
_skip = re.compile(r"^([a-z][a-z0-9+.-]*:|#|\{|//)", re.I)


def to_absolute(text, rel_dir):
    def fix(m):
        attr, url = m.group(1), m.group(2)
        if url == "" or _skip.match(url) or url.startswith("/"):
            return m.group(0)
        path, sep, frag = url.partition("#")
        path, qsep, query = path.partition("?")
        if path == "":
            return m.group(0)
        absp = posixpath.normpath(posixpath.join("/" + rel_dir, path))
        if path.endswith("/") and not absp.endswith("/"):
            absp += "/"
        base = posixpath.basename(absp)
        if attr == "href" and absp.endswith(".html") and base[:-5] not in KEEP_HTML:
            absp = absp[:-5]
        return f'{attr}="{absp}{qsep}{query}{sep}{frag}"'
    return _attr.sub(fix, text)


def to_relative(text, rel_dir, html_exists):
    """Umkehrung von to_absolute. html_exists(pfad_ohne_slash) -> gibt es pfad.html?"""
    here = "/" + rel_dir if rel_dir else "/"

    def fix(m):
        attr, url = m.group(1), m.group(2)
        if not url.startswith("/") or url.startswith("//"):
            return m.group(0)
        path, sep, frag = url.partition("#")
        path, qsep, query = path.partition("?")
        target = path
        if attr == "href" and not path.endswith("/") and "." not in posixpath.basename(path) and path != "/":
            if html_exists(path.lstrip("/")):
                target = path + ".html"
        rel = posixpath.relpath(target, here)
        if path.endswith("/") and not rel.endswith("/"):
            rel += "/"
        return f'{attr}="{rel}{qsep}{query}{sep}{frag}"'
    return _attr.sub(fix, text)


def rel_dir_of(rel):
    d = posixpath.dirname(rel)
    return d


def link_style(text):
    """'absolute' oder 'relative' – so, wie die Datei auf GitHub geschrieben ist."""
    local_abs = len(re.findall(r'\b(?:href|src)="/(?!/)', text))
    local_rel = len(re.findall(r'\b(?:href|src)="(?![a-z][a-z0-9+.-]*:|/|#|\{|data:)[^"]+"', text, re.I))
    return "relative" if local_rel > local_abs else "absolute"


# ---------------------------------------------------------------- Formate
def is_archiv(rel):
    # archiv/ = statische Schnappschuesse: Menue bleibt wie es ist (wie in sandbox_zu_github.py)
    return rel.startswith("archiv/")


def normalize(text, rel):
    if not rel.endswith(".html"):
        return text
    if is_archiv(rel):
        return to_absolute(text, rel_dir_of(rel))
    return to_absolute(remove_intern_blocks(text), rel_dir_of(rel))


def render_sandbox(norm_text, rel, tpl, html_exists):
    if not rel.endswith(".html"):
        return norm_text
    if is_archiv(rel):
        return to_relative(norm_text, rel_dir_of(rel), html_exists)
    return to_relative(insert_intern_blocks(norm_text, tpl), rel_dir_of(rel), html_exists)


def render_site(norm_text, rel, style, html_exists):
    if not rel.endswith(".html") or style == "absolute":
        return norm_text
    return to_relative(norm_text, rel_dir_of(rel), html_exists)


def intern_in_menu(text):
    if _entw_start.search(text) or "data-dev-dd" in text:
        return True
    return bool(re.search(r'(sub-trigger|submenu-label)[^>]*>\s*(Impulsvorträge|capiamo|Archiv)\s*<', text))
