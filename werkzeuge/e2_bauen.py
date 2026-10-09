#!/usr/bin/env python3
"""Baut den Entwurf „empiria 2.0“ (nur Entwicklung, Branch Daniel – nie auf main).

Daniels Auftrag (09.10.2026): Startseite, Strategiehandwerk (+3 Unterseiten) und Workshops (+3 Unterseiten)
grafisch in die Klarheit der Wagenpaten-Seite übersetzen. Texte und Abschnitte bleiben 1:1 – deshalb werden alle
Inhalte hier aus den Originalseiten gelesen, nicht abgetippt. Kopf, Menü, Fuß, Detailfenster und Skripte kommen
unverändert aus der jeweiligen Originalseite; nur <main> wird neu gesetzt (Gestaltung: assets/projekte/empiria-2/e2.css).

    python3 werkzeuge/e2_bauen.py
"""
import posixpath
import re
from pathlib import Path

SITE = Path(__file__).resolve().parent.parent / "site"
ZIEL = SITE / "projekte" / "empiria-2"
CSS = '<link rel="stylesheet" href="/assets/projekte/empiria-2/e2.css">\n<link rel="stylesheet" href="/assets/projekte/empiria-2/e2-seiten.css">'

# Originalseite -> Seite im Entwurf; Links darauf werden im Entwurf auf die 2.0-Fassung umgebogen
SEITEN = {
    "index.html": "index.html",
    "leistungen/strategie.html": "strategie.html",
    "leistungen/komplexe-themen.html": "komplexe-themen.html",
    "leistungen/innovation.html": "innovation.html",
    "workshops.html": "workshops.html",
    "ki-zum-anfassen.html": "ki-zum-anfassen.html",
    "sprint-landingpage.html": "sprint-landingpage.html",
    "workshop-moderation.html": "workshop-moderation.html",
}
LINKS = {"/": "index.html", "/index.html": "index.html", "/leistungen/strategie": "strategie.html",
         "/leistungen/komplexe-themen": "komplexe-themen.html", "/leistungen/innovation": "innovation.html",
         "/workshops": "workshops.html", "/ki-zum-anfassen": "ki-zum-anfassen.html",
         "/sprint-landingpage": "sprint-landingpage.html", "/workshop-moderation": "workshop-moderation.html"}
PFEIL = '<svg class="e2-pfeil" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'


# ---------- kleine Lese-Helfer (Inhalte immer aus dem Original) ----------
def abschnitt(html, marker):
    a = html.find(marker)
    assert a >= 0, marker
    a = html.rfind("<section", 0, a)
    tiefe, i = 0, a
    while True:
        o, c = html.find("<section", i + 1), html.find("</section>", i + 1)
        if o != -1 and o < c:
            tiefe += 1; i = o
        else:
            if tiefe == 0:
                return html[a:c + 10]
            tiefe -= 1; i = c


def alle(muster, html, flags=re.S):
    return re.findall(muster, html, flags)


def eins(muster, html, flags=re.S):
    m = re.search(muster, html, flags)
    assert m, muster[:60]
    return m.group(1).strip()


def ohne_hl(t):
    """Überschriften nach dem Kopfbereich: ohne gelbe Hervorhebung (Daniel), Text bleibt gleich."""
    return re.sub(r'<span class="hl">(.*?)</span>', r"\1", t, flags=re.S)


def link(href):
    roh = href[:-5] if href.endswith(".html") and href != "/index.html" else href
    return "/projekte/empiria-2/" + LINKS[roh] if roh in LINKS else href


def absolut(html, original):
    """Relative Pfade der Originalseite absolut machen – der Entwurf liegt in einem anderen Ordner."""
    basis = "/" + posixpath.dirname(original)
    def ersetze(m):
        attr, wert = m.group(1), m.group(2)
        if re.match(r"(/|#|[a-z]+:|data:)", wert) or not wert:
            return m.group(0)
        return f'{attr}="{posixpath.normpath(posixpath.join(basis, wert))}"'
    return re.sub(r'\b(href|src)="([^"]*)"', ersetze, html)


def links_umbiegen(html):
    return re.sub(r'href="(/[^"#?]*)"', lambda m: f'href="{link(m.group(1))}"', html)


# ---------- Seitenrahmen ----------
def seite(original, main, titel_zusatz="empiria 2.0 · Entwurf"):
    h = (SITE / original).read_text(encoding="utf-8")
    a, b = h.index("<main"), h.index("</main>") + 7
    kopf, fuss = h[:a], h[b:]
    kopf = kopf.replace('<link rel="stylesheet" href="/styles.css">', '<link rel="stylesheet" href="/styles.css">\n' + CSS, 1)
    kopf = re.sub(r"<body([^>]*)>", lambda m: (m.group(0).replace('class="', 'class="e2 ') if 'class="' in m.group(1) else f'<body{m.group(1)} class="e2">'), kopf, 1)
    kopf = re.sub(r"<title>(.*?)</title>", lambda m: f"<title>{m.group(1)} · {titel_zusatz}</title>", kopf, 1)
    kopf = kopf.replace('<meta name="robots" content="index', '<meta name="robots" content="noindex')
    return links_umbiegen(absolut(kopf, original)) + "<main>\n" + links_umbiegen(main) + "\n</main>" + links_umbiegen(absolut(fuss, original))



# ---------- Bausteine, die auf mehreren Seiten vorkommen ----------
def kontakt(ko):
    ko_kicker = eins(r'<p class="kicker">(.*?)</p>', ko)
    ko_h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", ko))
    ko_lead = eins(r'<p class="lead">(.*?)</p>', ko)
    ko_notiz = eins(r'<p class="kontakt-standalone-note">(.*?)</p>', ko)
    wege = alle(r'<a class="ks-pill[^"]*" href="([^"]+)"([^>]*)>\s*<span class="ks-pill-icon">(.*?)</span>\s*(.*?)\s*</a>', ko)
    foto = eins(r'(<img class="ks-photo"[^>]*>)', ko).replace(' loading="lazy"', '')
    ko_logos = eins(r'(<div class="ks-marquee">.*?</div>\s*</div>\s*</div>)', ko)
    return f'''<section class="e2-sek" id="kontakt"><div class="e2-wrap">
  <div class="e2-kontakt">
    <div><p class="e2-kicker">{ko_kicker}</p><h2 class="e2-h2">{ko_h2}</h2><p class="e2-lead">{ko_lead}</p><p class="e2-kontakt__notiz">{ko_notiz}</p></div>
    <div><ul class="e2-wege">{''.join(f'<li><a href="{hr}"{rest}><i>{ico}</i><span>{txt}</span>{PFEIL}</a></li>' for hr, rest, ico, txt in wege)}</ul><div class="e2-ks-logos">{ko_logos}</div></div>
  </div>
  <div class="e2-foto">{foto}</div>
</div></section>'''


FARBEN = ["gelb", "schwarz", "hell"]


def weitere(se):
    """„Weitere Leistungen“: die Kacheln als Karten mit weißem Kopf, farbiger Mitte, weißem Fuß."""
    kicker = eins(r'<p class="kicker">(.*?)</p>', se)
    h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", se))
    kacheln = alle(r'<a class="related-leistung" href="([^"]+)">\s*<div class="related-leistung-face">\s*<div class="icon">(.*?)</div>\s*<h3>(.*?)</h3>\s*</div>\s*<div class="related-leistung-hover">\s*<p>(.*?)</p>\s*<span class="link-more">(.*?)</span>', se)
    karten = "".join(f'<a class="e2-karte" href="{link(hr)}"><div class="e2-karte__kopf"><img src="/assets/empiria-logo.svg" alt="empiria"></div><div class="e2-karte__bild e2-karte__bild--{FARBEN[i % 3]}"><div class="e2-karte__ico e2-karte__ico--einfach">{ico}</div><h3>{t}</h3></div><div class="e2-karte__text"><p>{p}</p><span class="e2-karte__mehr">{mehr} {PFEIL}</span></div></a>' for i, (hr, ico, t, p, mehr) in enumerate(kacheln))
    return f'''<section class="e2-sek e2-sek--hell" id="weitere-leistungen"><div class="e2-wrap">
  <p class="e2-kicker">{kicker}</p><h2 class="e2-h2">{h2}</h2>
  <div class="e2-karten">{karten}</div>
</div></section>'''


def ohne_hl_ausser_h1(html):
    """Hervorhebungen nur im Kopfbereich (h1); in allen späteren Überschriften und Sätzen weg."""
    teile = re.split(r"(<h1\b.*?</h1>)", html, flags=re.S)
    return "".join(t if t.startswith("<h1") else re.sub(r'<span class="(?:hl|hl-acc)(?: [^"]*)?">(.*?)</span>', r"\1", t, flags=re.S) for t in teile)


def unterseite(original, ziel):
    """Unterseiten: Originalinhalt bleibt vollständig erhalten, die Gestaltung übersetzt e2-seiten.css.
    Ersetzt werden nur Kontakt und „Weitere Leistungen“ durch die e2-Bausteine (gleicher Text)."""
    h = (SITE / original).read_text(encoding="utf-8")
    main = h[h.index("<main"):h.index("</main>")]
    main = main[main.index(">") + 1:]
    if 'id="kontakt"' in main:
        k = abschnitt(main, 'id="kontakt"'); main = main.replace(k, kontakt(k))
    if 'id="weitere-leistungen"' in main:
        w = abschnitt(main, 'id="weitere-leistungen"'); main = main.replace(w, weitere(w))
    main = ohne_hl_ausser_h1(main)
    # Zusammenarbeit/Formate: Akkordeons offen als Kartenreihe, damit alles auf einen Blick lesbar ist
    main = re.sub(r'<details class="formate-acc-item([^"]*)"([^>]*)>', lambda m: '<details class="formate-acc-item' + m.group(1) + '"' + re.sub(r'\s*name="[^"]*"', '', m.group(2)) + ' open>', main)
    return seite(original, f'<div class="e2-alt">{main}</div>')


# ---------- Startseite ----------
def startseite():
    h = (SITE / "index.html").read_text(encoding="utf-8")
    held = abschnitt(h, 'id="hero"')
    h1 = eins(r"<h1>(.*?)</h1>", held)
    pfeil = eins(r'<div class="hero-arrow">(.*?)</div>', held)
    texte = alle(r"<p>(.*?)</p>", eins(r'<div class="hero-copy lead">(.*?)</div>', held))
    knopf = re.search(r'<a class="btn btn--dark" href="([^"]+)">(.*?)</a>', held)
    marquee = eins(r'(<div class="marquee" aria-label="[^"]*">.*?</div>\s*</div>\s*</div>)', h)

    pr = abschnitt(h, 'id="problem"')
    pr_kicker = eins(r'<p class="kicker[^"]*"[^>]*>(.*?)</p>', pr)
    pr_h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", pr))
    pr_box = eins(r'<div class="problem-box[^"]*"[^>]*>(.*?)</div>\s*</div>', pr) if 'problem-box' in pr else None
    pr_ps = alle(r"<p(?: [^>]*)?>(.*?)</p>", pr)[1:]
    pr_lis = alle(r"<li[^>]*>(.*?)</li>", pr)

    lo = abschnitt(h, 'id="loesung"')
    lo_kicker = eins(r'<p class="kicker"[^>]*>(.*?)</p>', lo)
    lo_h2 = eins(r'<h2 class="h-serif">(.*?)<span class="wirkung">', lo)
    lo_h2_2 = re.sub(r"<[^>]+>", "", eins(r'<span class="txt">(.*?)</span>\s*</span>', lo))
    lo_p = eins(r'<div class="loesung-copy lead">\s*<p>(.*?)</p>', lo)
    lo_mehr = re.search(r'<button class="link-more" data-modal="([^"]+)">(.*?)</button>', lo)
    lo_btn = re.search(r'<a class="btn btn--dark" href="([^"]+)">(.*?)</a>', lo)

    le = abschnitt(h, 'id="leistungen"')
    le_kicker = eins(r'<p class="kicker">(.*?)</p>', le)
    le_h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", le))
    le_lead = eins(r'<p class="lead">(.*?)</p>', le)
    karten = alle(r'<article class="lcard">\s*(<div class="lcard-icon">.*?</div>)\s*<h3>(.*?)</h3>\s*<div class="lcard-body">\s*<p>(.*?)</p>\s*<a class="link-more" href="([^"]+)">(.*?)</a>', le)
    le_btn = re.search(r'<div class="leistungen-cta">\s*<a class="btn btn--dark" href="([^"]+)">(.*?)</a>', le)

    fo = abschnitt(h, 'id="formate"')
    fo_kicker = eins(r'<p class="kicker">(.*?)</p>', fo)
    fo_h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", fo))
    fo_leads = alle(r'<p class="lead">(.*?)</p>', fo)
    formate = alle(r'<details class="formate-acc-item formate-acc--(\w+)"[^>]*>\s*<summary><span>(.*?)</span></summary>\s*<div class="formate-acc-body">(.*?)</details>', fo)

    st = abschnitt(h, 'id="arbeitsweise"')
    st_h2 = re.sub(r"<[^>]+>", "", eins(r"<h2[^>]*>(.*?)</h2>", st))
    zahlen = alle(r'<div class="num">(.*?)</div><div class="lbl">(.*?)</div>', st)

    AKZENT = {"magenta": "#C51F5D", "cyan": "#0B9FBD", "gruen": "#6e9a2c", "green": "#6e9a2c", "olive": "#8a9a3a"}
    farben = ["gelb", "schwarz", "hell"]

    m = []
    m.append(f'''<section class="e2-held" id="hero"><div class="e2-wrap">
  <div class="e2-held__raster">
    <div><h1>{h1}</h1><div class="e2-held__pfeil" aria-hidden="true">{pfeil}</div></div>
    <div class="e2-held__text">{''.join(f'<p>{p}</p>' for p in texte)}
      <div class="e2-knoepfe"><a class="e2-knopf" href="{knopf.group(1)}">{knopf.group(2)} {PFEIL}</a></div></div>
  </div>
  <div class="e2-logos">{marquee}</div>
</div></section>''')
    m.append(f'''<section class="e2-sek e2-sek--hell" id="problem"><div class="e2-wrap e2-zwei">
  <div><p class="e2-kicker">{pr_kicker}</p><h2 class="e2-h2">{pr_h2}</h2></div>
  <div class="e2-kasten"><p>{pr_ps[0]}</p><ul>{''.join(f'<li>{x}</li>' for x in pr_lis)}</ul><p>{pr_ps[-1]}</p></div>
</div></section>''')
    m.append(f'''<section class="e2-sek e2-sek--gelb" id="loesung"><div class="e2-wrap e2-mitte">
  <p class="e2-kicker">{lo_kicker}</p><h2 class="e2-h2">{lo_h2.strip()} {lo_h2_2}</h2><p class="e2-lead">{lo_p}</p>
  <div class="e2-knoepfe"><button class="e2-knopf e2-knopf--rand link-more" type="button" data-modal="{lo_mehr.group(1)}">{lo_mehr.group(2)}</button><a class="e2-knopf" href="{lo_btn.group(1)}">{lo_btn.group(2)} {PFEIL}</a></div>
</div></section>''')
    m.append(f'''<section class="e2-sek" id="leistungen"><div class="e2-wrap">
  <p class="e2-kicker">{le_kicker}</p><h2 class="e2-h2">{le_h2}</h2><p class="e2-lead">{le_lead}</p>
  <div class="e2-karten">{''.join(f'<a class="e2-karte" href="{link(hr)}"><div class="e2-karte__kopf"><img src="/assets/empiria-logo.svg" alt="empiria"></div><div class="e2-karte__bild e2-karte__bild--{farben[i]}"><div class="e2-karte__ico">{ico}</div><h3>{t}</h3></div><div class="e2-karte__text"><p>{p}</p><span class="e2-karte__mehr">{mehr} {PFEIL}</span></div></a>' for i, (ico, t, p, hr, mehr) in enumerate(karten))}</div>
  <div class="e2-unten"><a class="e2-knopf" href="{le_btn.group(1)}">{le_btn.group(2)} {PFEIL}</a></div>
</div></section>''')
    spalten = []
    for farbe, titel, koerper in formate:
        ps = alle(r"^\s*<p>(.*?)</p>", koerper, re.S | re.M)
        eintraege = alle(r'<div class="formate-preview-title">(.*?)</div>\s*<p class="formate-preview-desc">(.*?)</p>', koerper)
        btn = re.search(r'<a class="btn btn--dark btn--sm" href="([^"]+)">(.*?)</a>', koerper)
        spalten.append(f'<div class="e2-format" style="--e2-akzent:{AKZENT.get(farbe, "#1a1817")}"><h3>{titel}</h3>{"".join(f"<p>{p}</p>" for p in ps)}'
                       f'<ul class="e2-liste">{"".join(f"<li><div><b>{t}</b><small>{d}</small></div>{PFEIL}</li>" for t, d in eintraege)}</ul>'
                       f'<a class="e2-knopf" href="{link(btn.group(1))}">{btn.group(2)} {PFEIL}</a></div>')
    m.append(f'''<section class="e2-sek e2-sek--hell" id="formate"><div class="e2-wrap">
  <div class="e2-kopfzeile"><div><p class="e2-kicker">{fo_kicker}</p><h2 class="e2-h2">{fo_h2}</h2></div><div>{''.join(f'<p class="e2-lead">{p}</p>' for p in fo_leads)}</div></div>
  <div class="e2-formate">{''.join(spalten)}</div>
</div></section>''')
    m.append(f'''<section class="e2-sek e2-sek--schwarz" id="arbeitsweise"><div class="e2-wrap">
  <h2 class="e2-h2" style="max-width:none">{st_h2}</h2>
  <div class="e2-zahlen">{''.join(f'<div><b>{re.sub(r"<[^>]+>", "", z)}</b><span>{l}</span></div>' for z, l in zahlen)}</div>
</div></section>''')
    m.append(kontakt(abschnitt(h, 'id="kontakt"')))
    return seite("index.html", "\n".join(m))


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    (ZIEL / "index.html").write_text(startseite(), encoding="utf-8")
    for orig, ziel in SEITEN.items():
        if orig != "index.html":
            (ZIEL / ziel).write_text(unterseite(orig, ziel), encoding="utf-8")
    print("gebaut:", ", ".join(SEITEN.values()))


if __name__ == "__main__":
    main()
