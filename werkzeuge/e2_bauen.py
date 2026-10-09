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
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).parent))
import e2_bilder
import e2_runde5

SITE = Path(__file__).resolve().parent.parent / "site"
ZIEL = SITE / "projekte" / "empiria-2"
CSS = '<link rel="stylesheet" href="/assets/projekte/empiria-2/e2.css">\n<link rel="stylesheet" href="/assets/projekte/empiria-2/e2-seiten.css">\n<link rel="stylesheet" href="/assets/projekte/empiria-2/e2-runde5.css">'

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
    a = html.rfind("<section", 0, a + 8)
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
def seite(original, main, titel_zusatz="empiria 2.0 · Entwurf", h=None):
    h = h or (SITE / original).read_text(encoding="utf-8")
    a, b = h.index("<main"), h.index("</main>") + 7
    kopf, fuss = h[:a], h[b:]
    kopf = kopf.replace('<link rel="stylesheet" href="/styles.css">', '<link rel="stylesheet" href="/styles.css">\n' + CSS, 1)
    kopf = re.sub(r"<body([^>]*)>", lambda m: (m.group(0).replace('class="', 'class="e2 ') if 'class="' in m.group(1) else f'<body{m.group(1)} class="e2">'), kopf, 1)
    kopf = re.sub(r"<title>(.*?)</title>", lambda m: f"<title>{m.group(1)} · {titel_zusatz}</title>", kopf, 1)
    kopf = kopf.replace('<meta name="robots" content="index', '<meta name="robots" content="noindex')
    out = links_umbiegen(absolut(kopf, original)) + "<main>\n" + links_umbiegen(main) + "\n</main>" + links_umbiegen(absolut(fuss, original))
    return mit_strategie2(out)


def mit_strategie2(html):
    return html   # Runde 23: Strategie 2 ist jetzt die Strategie-Seite


def _alt_mit_strategie2(html):
    """Menüeinträge für „Strategie in den Alltag überführen 2“ (Entwurf im Workshop-Aufbau, Daniel Runde 12)."""
    l = '/projekte/empiria-2/strategie.html'
    html = html.replace(f'<a href="{l}">Strategie in den Alltag überführen</a>',
                        f'<a href="{l}">Strategie in den Alltag überführen</a>\n<a href="/projekte/empiria-2/strategie-2.html">Strategie in den Alltag überführen 2</a>')
    html = html.replace(f'<a href="{l}" class="mobile-submenu-link">Strategie in den Alltag überführen</a>',
                        f'<a href="{l}" class="mobile-submenu-link">Strategie in den Alltag überführen</a>\n<a href="/projekte/empiria-2/strategie-2.html" class="mobile-submenu-link">Strategie in den Alltag überführen 2</a>')
    html = re.sub(r'(<a href="[^"]*projekte/empiria-2/strategie\.html" class="dev-dd-link">.*?</a>\n)',
                  lambda m: m.group(1) + m.group(1).replace("strategie.html", "strategie-2.html").replace("<b>Strategie in den Alltag überführen</b>", "<b>Strategie in den Alltag überführen 2</b>").replace(">1<", ">1b<").replace("<small>Strategiehandwerk</small>", "<small>im Aufbau der Workshop-Seiten</small>"), html, count=1)
    return html





# ---------- Formensprache der empiria-Startseite (kräftige geometrische Formen, viewBox 232.44) ----------
def _sprite(name):
    t = (SITE / "index.html").read_text(encoding="utf-8")
    return re.search(rf'<symbol id="ic-{name}"[^>]*>\s*(.*?)\s*</symbol>', t, re.S).group(1)


FORM = {n: _sprite(n) for n in ("forward", "kreis", "kreuz", "quadrat", "raute")}
FORM.update({
    "stern": '<path fill="currentColor" d="M116.22 6c9 64 46 101 110 110-64 9-101 46-110 110-9-64-46-101-110-110 64-9 101-46 110-110z"/>',
    "blitz": '<path fill="currentColor" d="M142 6 36 134h70L88 226l108-134h-68z"/>',
    "blase": '<path fill="currentColor" fill-rule="evenodd" d="M38 26h156c13 0 24 11 24 24v94c0 13-11 24-24 24h-80l-52 48v-48H38c-13 0-24-11-24-24V50c0-13 11-24 24-24zm8 20v104h48v24l26-24h66V46z"/>',
})
KOMPOSITION = {"strategie": ("forward", "raute"), "komplexe-themen": ("kreuz", "kreis"), "innovation": ("kreis", "quadrat"),
               "workshops": ("quadrat", "forward"), "ki-zum-anfassen": ("stern", "kreis"),
               "sprint-landingpage": ("blitz", "quadrat"), "workshop-moderation": ("blase", "raute")}


def form(name, cls="e2-form"):
    return f'<svg class="{cls}" viewBox="0 0 232.44 232.44" aria-hidden="true">{FORM[name]}</svg>'

# ---------- Einheitliche, einfache Symbole (eine Farbe, kräftiger Strich) ----------
# Ersetzen die filigranen Zeichnungen der alten Seiten (Daniel, 09.10.2026).
SYMBOL = {
    "strategie": '<path d="M4.5 5.5 11 12l-6.5 6.5M12.5 5.5 19 12l-6.5 6.5"/>',
    "komplexe-themen": '<path d="M6 6l12 12M18 6 6 18"/>',
    "innovation": '<circle cx="12" cy="12" r="7.5"/>',
    "workshops": '<rect x="3.5" y="3.5" width="17" height="11" rx="1.5"/><path d="M7.5 7.5h9M7.5 10.5h5.5M9 20.5l1.6-6M15 20.5l-1.6-6"/>',
    "ki-zum-anfassen": '<path d="M11 3.5l1.9 5.1 5.1 1.9-5.1 1.9L11 17.5l-1.9-5.1L4 10.5l5.1-1.9z"/><path d="M18 15.5l.8 2.2 2.2.8-2.2.8-.8 2.2-.8-2.2-2.2-.8 2.2-.8z"/>',
    "sprint-landingpage": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8.5h18M13 11l-3 4h3.5l-2.5 3.5"/>',
    "workshop-moderation": '<path d="M3.5 5h11v7.5H8.5L5 15.5V12.5H3.5z"/><path d="M14.5 9h6v7.5h-1.5v3l-3.5-3h-4.5v-4"/>',
    "powerpoint": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8 20.5h8M7 12.5l3-3 2.5 2 4-4"/>',
    "landingpage": '<rect x="5" y="2.5" width="14" height="19" rx="2"/><path d="M8.5 6.5h7M8.5 9.5h4.5M8.5 13h7v3.5h-7z"/>',
    "rollup": '<path d="M6.5 3.5h11v15h-11zM12 18.5v2.5M7.5 21h9M9 7.5h6M9 10.5h4"/>',
}
AKZENT_SEITE = {"strategie": "gelb", "strategie-2": "gelb", "komplexe-themen": "gelb", "innovation": "gelb",
                "workshops": "magenta", "ki-zum-anfassen": "magenta", "sprint-landingpage": "magenta", "workshop-moderation": "magenta"}


# Formate auf der Startseite: Kernaussage je Format (aus den Originaltexten verdichtet) und ein Symbol je Unterformat
FORMAT_SATZ = {
    "Workshops": "Hands-on an echten Tools und Fällen aus Eurem Alltag – Ihr geht mit klaren Ergebnissen raus.",
    "Marketing 2.0": "Deine digitalen Kanäle an einem Ort – als Marketingabteilung im Abo oder als einzelnes Format.",
    "Training & Sparring": "Begleiten statt nur schulen – für Dein Team und für Dich als Führungskraft.",
}
FORMAT_SYM = {
    "KI": '<path d="M11 3.5l1.9 5.1 5.1 1.9-5.1 1.9L11 17.5l-1.9-5.1L4 10.5l5.1-1.9z"/><path d="M18.5 15l.7 1.8 1.8.7-1.8.7-.7 1.8-.7-1.8-1.8-.7 1.8-.7z"/>',
    "Sprint": '<rect x="3" y="4" width="18" height="16" rx="2"/><path d="M3 8.5h18M13 11l-3 4h3.5l-2.5 3.5"/>',
    "Moderation": '<path d="M3.5 5h11v7.5H8.5L5 15.5V12.5H3.5z"/><path d="M14.5 9h6v7.5h-1.5v3l-3.5-3h-4.5v-4"/>',
    "Marketing": '<rect x="3" y="3.5" width="18" height="17" rx="2"/><path d="M7 16v-3M11 16V9.5M15 16v-5"/>',
    "sofort": '<path d="M3.5 10v4h3l6 4V6l-6 4z"/><path d="M16 9.5a3.5 3.5 0 0 1 0 5M18.5 7a7 7 0 0 1 0 10"/>',
    "Paid": '<circle cx="12" cy="12" r="8.5"/><circle cx="12" cy="12" r="4.5"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
    "Medien": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8 20.5h8M7 12.5l3-3 2.5 2 4-4"/>',
    "Teams": '<circle cx="8" cy="8.5" r="3"/><circle cx="16.5" cy="9.5" r="2.5"/><path d="M2.5 19.5c.6-3.4 2.8-5.5 5.5-5.5s4.9 2.1 5.5 5.5M14 14.6c.8-.4 1.6-.6 2.5-.6 2.4 0 4.2 1.9 4.8 5"/>',
    "1:1": '<circle cx="9" cy="8" r="3.5"/><path d="M2.5 20c.6-3.8 3.2-6 6.5-6s5.9 2.2 6.5 6"/><path d="M15.5 4.5h6v4.5h-2l-2 2v-2h-2z"/>',
}


FORMAT_GROSS = {  # weiße Linien-Symbole für die farbige Mitte (Variante A)
    "Workshops": '<svg viewBox="0 0 24 24"><rect x="3" y="3.5" width="18" height="11.5" rx="1.5"/><path d="M7 7.5h6M7 10.5h9M9 20.5l1.6-5.5M15 20.5l-1.6-5.5"/></svg>',
    "Marketing 2.0": '<svg viewBox="0 0 24 24"><path d="M3.5 10v4h3l7 4.5v-13l-7 4.5z"/><path d="M17 9a4 4 0 0 1 0 6M19.5 6.5a7.5 7.5 0 0 1 0 11"/></svg>',
    "Training & Sparring": '<svg viewBox="0 0 24 24"><path d="M3 5h11v7.5H8L4.5 15.5V12.5H3z"/><path d="M14 9h7v7.5h-1.5v3l-3.5-3H11v-3.5"/></svg>',
}
UNTER_LINK = {"KI": "/ki-zum-anfassen", "Sprint": "/sprint-landingpage", "Moderation": "/workshop-moderation", "Marketing": "/dashboard-digitales-marketing",
              "sofort": "/sofort-sichtbar", "Paid": "/paid-ads", "Medien": "/medien", "Teams": "/praesentationsseminar", "1:1": "/sparring"}


def unter_link(titel):
    for k, v in UNTER_LINK.items():
        if titel.startswith(k):
            return link(v)
    return "#"


def format_sym(titel):
    for k, v in FORMAT_SYM.items():
        if titel.startswith(k):
            return f'<svg viewBox="0 0 24 24" aria-hidden="true">{v}</svg>'
    return '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="7"/></svg>'


def symbol(name, cls="e2-sym"):
    return f'<svg class="{cls}" viewBox="0 0 24 24" aria-hidden="true">{SYMBOL[name]}</svg>'


KOPFBILD_SEITE = {"index": "Startseite", "strategie": "Strategie in den Alltag überführen", "strategie-2": "Strategie in den Alltag überführen", "komplexe-themen": "Komplexe Themen strukturieren & kommunizieren",
                  "innovation": "Innovation & Geschäftsmodell neu denken", "workshops": "Workshops", "ki-zum-anfassen": "KI zum Anfassen",
                  "sprint-landingpage": "Sprint Landingpage", "workshop-moderation": "Moderation deines Workshops"}


def kopfbild(name, chips=""):
    """Rechts im Kopfbereich: das freigegebene Mono-Kopfbild der Seite (e2_kopfbilder.py, Daniel 10.10.2026), darunter ggf. die Anlass-Chips."""
    import e2_kopfbilder as kb
    from e2_header import farbig
    seite = next(x for x in kb.SEITEN if x[0] == KOPFBILD_SEITE[name])
    bild = farbig(kb.bild(seite)[0], seite[2], "kopf").replace('class="hv-bild"', 'class="e2-bild"')
    return f'<div class="e2-kopfbild">{bild}{chips}</div>'


def kopf_neu(held, name):
    """Kopfbereich der Unterseiten wie bei den Wagenpaten: links Kicker, Überschrift, Text, Chips, Knopf – rechts das Kopfbild."""
    kicker = re.search(r'<p class="kicker"[^>]*>(.*?)</p>', held, re.S)
    if not kicker and name in ("komplexe-themen", "innovation"):
        kicker = re.search(r"(Strategiehandwerk)", "Strategiehandwerk")   # Unterzeile wie bei Strategie (Daniel)
    h1 = re.search(r"<h1[^>]*>(.*?)</h1>", held, re.S).group(1)
    if 'class="hero-copy' in held:
        inhalt = re.search(r'<div class="hero-copy[^"]*">(.*)</div>\s*</div>\s*<div class="hero-cta">', held, re.S).group(1)
    else:
        t = re.search(r'<div class="produkt-hero-text">(.*?)</div>\s*<div class="produkt-hero-visual">', held, re.S).group(1)
        inhalt = re.sub(r'<p class="kicker"[^>]*>.*?</p>|<h1[^>]*>.*?</h1>', "", t, count=2, flags=re.S)
    knoepfe = re.findall(r'<a class="btn[^"]*" href="([^"]+)">(.*?)</a>', held)
    chips = ""
    m = re.search(r'<div class="hero-anlaesse".*?</div>', inhalt, re.S)
    if m:
        chips = m.group(0); inhalt = inhalt.replace(chips, "")
    if name == "komplexe-themen":
        chips = ""   # Zielgruppen stehen jetzt im Kopfbild (Daniel, Runde 11)
    return f'''<section class="e2-kopf" id="intro"><div class="e2-wrap e2-kopf__raster">
  <div class="e2-kopf__text">{f'<p class="e2-kicker">{kicker.group(1)}</p>' if kicker else ""}<h1>{h1}</h1>
    <div class="e2-kopf__inhalt">{inhalt}</div>
    <div class="e2-knoepfe">{"".join(f'<a class="e2-knopf" href="{hr}">{tx} {PFEIL}</a>' for hr, tx in knoepfe)}</div></div>
  {kopfbild(name, chips)}
</div></section>'''


DIALOG_JS = """<script>document.addEventListener("click",function(e){var a=e.target.closest("[data-e2-auf]");if(a){document.getElementById(a.getAttribute("data-e2-auf")).showModal();return;}
var z=e.target.closest(".e2-dialog__zu");if(z){z.closest("dialog").close();return;}if(e.target.tagName==="DIALOG")e.target.close();});</script>"""


# ---------- Bausteine, die auf mehreren Seiten vorkommen ----------
def kontakt_teile(ko):
    wege = alle(r'<a class="(ks-pill[^"]*)" href="([^"]+)"([^>]*)>\s*<span class="ks-pill-icon">(.*?)</span>\s*(.*?)\s*</a>', ko)
    return dict(
        kicker=eins(r'<p class="kicker">(.*?)</p>', ko), h2=ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", ko)),
        lead=eins(r'<p class="lead">(.*?)</p>', ko), notiz=eins(r'<p class="kontakt-standalone-note">(.*?)</p>', ko),
        wege="".join(f'<a class="e2-pille{" e2-pille--rand" if "ghost" in cl else ""}" href="{hr}"{rest}><i>{ico}</i>{txt}</a>' for cl, hr, rest, ico, txt in wege),
        foto=eins(r'(<img class="ks-photo"[^>]*>)', ko).replace(' loading="lazy"', ''),
        logos=eins(r'(<div class="ks-marquee">.*?</div>\s*</div>\s*</div>)', ko))


def kontakt_start(ko):
    """Startseite: Kontakt 1:1 wie auf der Live-Startseite (Daniel, Runde 10) – nur die Unterzeile im 2.0-Stil mit Strich."""
    k = re.sub(r'<p class="kicker">(.*?)</p>', r'<p class="e2-kicker">\1</p>', ko, count=1)
    k = k.replace("Wir sind <span class=\"hl\">", "Wir sind<br><span class=\"hl\" style=\"white-space:nowrap\">", 1)   # „für Dich“ in die zweite Zeile (Daniel)
    return k.replace(" reveal", "").replace('loading="lazy"', "")


TEAM = [("daniel", "Daniel Ströbel", "Strategiehandwerker"), ("kerstin", "Kerstin Christ", "Expertin HR &amp; Weiterbildung"),
        ("noah", "Noah Hermanns", "Experte Performance Marketing")]


def kontakt(ko):
    """Detailseiten: Aufbau wie bei KI zum Anfassen – Überschrift, Personen im Kreis, EIN Knopf zur Kontaktseite (Daniel, Runde 10)."""
    k = kontakt_teile(ko)
    personen = "".join(f'<div class="ansprechpartner-card"><div class="ansprechpartner-photo"><img src="/assets/ansprechpartner-{d}.webp" alt="{n}" width="132" height="132"></div>'
                       f'<p class="ansprechpartner-name">{n}</p><p class="ansprechpartner-role">{r}</p></div>' for d, n, r in TEAM)
    return f'''<section class="produkt-cta produkt-team-cta e2-kontakt-team" id="kontakt"><div class="container">
  <p class="kicker">{k["kicker"]}</p><h2>{k["h2"]}</h2><p class="produkt-team-cta-sub">{k["lead"]}</p>
  <div class="ansprechpartner-grid">{personen}</div>
  <div class="produkt-cta-actions"><a class="btn btn--dark" href="/kontakt.html">Kontakt aufnehmen</a></div>
</div></section>'''


FARBEN = ["gelb", "schwarz", "hell"]


def weitere(se):
    """„Weitere Leistungen“: die Kacheln als Karten mit weißem Kopf, farbiger Mitte, weißem Fuß."""
    kicker = eins(r'<p class="kicker">(.*?)</p>', se)
    h2 = ohne_hl(eins(r"<h2[^>]*>(.*?)</h2>", se))
    kacheln = alle(r'<a class="related-leistung" href="([^"]+)">\s*<div class="related-leistung-face">\s*<div class="icon">(.*?)</div>\s*<h3>(.*?)</h3>\s*</div>\s*<div class="related-leistung-hover">\s*<p>(.*?)</p>\s*<span class="link-more">(.*?)</span>', se)
    karten = "".join(f'<a class="e2-karte" href="{link(hr)}"><div class="e2-karte__kopf"><span class="e2-karte__nr">0{i+1}</span></div><div class="e2-karte__bild e2-karte__bild--{FARBEN[i % 3]}"><div class="e2-karte__ico e2-karte__ico--einfach">{ico}</div><h3>{t}</h3></div><div class="e2-karte__text"><p>{p}</p><span class="e2-karte__mehr">{mehr} {PFEIL}</span></div></a>' for i, (hr, ico, t, p, mehr) in enumerate(kacheln))
    return f'''<section class="e2-sek" id="weitere-leistungen"><div class="e2-wrap">
  <p class="e2-kicker">{kicker}</p><h2 class="e2-h2">{h2}</h2>
  <div class="e2-karten">{karten}</div>
</div></section>'''


def ohne_hl_ausser_h1(html):
    """Hervorhebungen nur im Kopfbereich (h1); in allen späteren Überschriften und Sätzen weg."""
    teile = re.split(r"(<h1\b.*?</h1>)", html, flags=re.S)
    return "".join(t if t.startswith("<h1") else re.sub(r'<span class="(?:hl|hl-acc)(?: [^"]*)?">(.*?)</span>', r"\1", t, flags=re.S) for t in teile)


def workshop_karten(main):
    """Workshops-Übersicht (Daniel, Runde 21): statt der filigranen Skizzen die Kopfbilder der jeweiligen Unterseite – weiß auf Magenta."""
    import e2_kopfbilder as kb
    from e2_header import farbig
    ziel = {"ki-zum-anfassen": "KI zum Anfassen", "sprint-landingpage": "Sprint Landingpage", "workshop-moderation": "Moderation deines Workshops"}

    def ersetze(m):
        block = m.group(0)
        name = re.search(r'href="[^"]*?/?(ki-zum-anfassen|sprint-landingpage|workshop-moderation)(?:\.html)?"', block).group(1)
        seite = next(x for x in kb.SEITEN if x[0] == ziel[name])
        bild = kb.bild(seite)[0].replace("#1a1817", "#ffffff").replace("#C51F5E", "#ffd0e0").replace("#b9b3ab", "#f2a9c3")
        bild = farbig(bild, "magenta", "wk" + name[:3]).replace('class="hv-bild"', 'class="e2-wk-bild"')
        return re.sub(r'<div class="media-box-thumb media-box-thumb--mock">.*?</svg>\s*</div>\s*</div>',
                      f'<div class="media-box-thumb e2-wk-thumb">{bild}</div>', block, count=1, flags=re.S)
    return re.sub(r'<a class="media-box sprint-structure-card media-box--icon".*?</a>', ersetze, main, flags=re.S)


def unterseite(original, ziel, html=None):
    """Unterseiten: Originalinhalt bleibt vollständig erhalten, die Gestaltung übersetzt e2-seiten.css.
    Ersetzt werden nur Kontakt und „Weitere Leistungen“ durch die e2-Bausteine (gleicher Text)."""
    h = html or (SITE / original).read_text(encoding="utf-8")
    main = h[h.index("<main"):h.index("</main>")]
    main = main[main.index(">") + 1:]
    name = ziel[:-5]
    held_marker = '<section class="hero leistung-hero"' if '<section class="hero leistung-hero"' in main else '<section class="produkt-hero"'
    held = abschnitt(main, held_marker)
    main = main.replace(held, kopf_neu(held, name))
    # Medien (Komplexe Themen): einfache Symbole statt Skizzen – je Kachel nur das Bild tauschen
    def medien(m):
        block = m.group(0)
        label = re.search(r'<span class="medien-sketch-label">(.*?)</span>', block).group(1)
        sym = {"PowerPoint": "powerpoint", "Landingpage": "landingpage", "Roll-up": "rollup"}.get(label)
        if not sym:
            return block
        a = block.index('<div class="medien-sketch-thumb">'); e = block.index("</svg>", a) + 6
        e = block.index("</div>", e) + 6
        return block[:a] + '<div class="medien-sketch-thumb">' + symbol(sym, "e2-medien-sym") + "</div>" + block[e:]
    main = re.sub(r'<div class="medien-sketch" tabindex="0">.*?<span class="medien-sketch-label">.*?</span>', medien, main, flags=re.S)
    if 'id="kontakt"' in main:
        k = abschnitt(main, 'id="kontakt"'); main = main.replace(k, kontakt(k))
    if 'id="weitere-leistungen"' in main:
        w = abschnitt(main, 'id="weitere-leistungen"'); main = main.replace(w, "")  # Daniel: nicht mehr unter dem Kontakt
    # Runde 5: neu gedachte Sektionen und Download mit Hervorhebung
    if name in ("strategie", "strategie-2"):
        sek = abschnitt(main, 'id="perspektive"'); main = main.replace(sek, e2_runde5.perspektive(sek, name != "strategie-2"))
    if name == "innovation":
        sek = abschnitt(main, 'id="problem"'); main = main.replace(sek, e2_runde5.problem_inno(sek))
    if name == "komplexe-themen":
        sek = abschnitt(main, 'id="problem"'); main = main.replace(sek, e2_runde5.problem_kt(sek))
        sek = abschnitt(main, 'id="loesung-baustein"'); main = main.replace(sek, e2_runde5.loesung_kt(sek))
    main = e2_runde5.download_hl(main, AKZENT_SEITE[name] == "magenta")
    main = ohne_hl_ausser_h1(main)
    # Zusammenarbeit & Co.: gleich hohe Karten (Nummer + Titel), der Text öffnet sich in einem Fenster
    zaehler = iter(range(1, 100))
    def karte_acc(m):
        i = next(zaehler)
        titel, koerper = m.group(1), m.group(2)
        return (f'<article class="e2-zk"><span class="e2-zk__nr">0{i}</span><h3>{titel}</h3>'
                f'<button type="button" class="e2-zk__mehr" data-e2-auf="zk{i}">Mehr lesen {PFEIL}</button>'
                f'<dialog class="e2-dialog" id="zk{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><h3>{titel}</h3>{koerper}</dialog></article>')
    main = re.sub(r'<details class="formate-acc-item[^"]*"[^>]*>\s*<summary><span>(.*?)</span></summary>\s*<div class="formate-acc-body">(.*?)</div>\s*</details>', karte_acc, main, flags=re.S)
    main = main.replace('<div class="formate-accordion">', '<div class="e2-zk-raster">')
    # Problem: Absätze als zwei Schritte statt Kasten
    def problem(m):
        teile = re.findall(r'<(p|ul)\b[^>]*>.*?</\1>', m.group(1), re.S)
        bloecke = re.findall(r'(<(?:p|ul)\b[^>]*>.*?</(?:p|ul)>)', m.group(1), re.S)
        return '<ol class="e2-problem">' + "".join(f"<li>{x}</li>" for x in bloecke) + "</ol>"
    main = re.sub(r'<div class="problem-card[^"]*">(.*?)</div>\s*</div>\s*</div>\s*</section>', lambda m: problem(m) + "</div></div></section>", main, count=1, flags=re.S)
    if name == "workshops":
        main = workshop_karten(main)
    main += DIALOG_JS
    return seite(original, f'<div class="e2-alt e2-alt--{AKZENT_SEITE[name]} e2-seite--{name}">{main}</div>', h=html)


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

    AKZENT = {"magenta": "#C51F5D", "cyan": "#0B9FBD", "gruen": "#6e9a2c", "green": "#6e9a2c", "olive": "#8a9a3a", "lime": "#8613A1"}
    farben = ["gelb", "schwarz", "hell"]

    # Runde 12 (Daniel): Aufbau wie die Volksfest-Seite – großer Kopf mit Kennzahlen und Doppelpfeil, Logo-Band,
    # Problem auf Gelb mit schwarzem Kasten, Lösung als drei Schritte, Leistungen auf Schwarz, Formate, Kontakt wie live.
    from e2_lucide import ICONS as LU
    def lu(n, farbe="#1a1817"):
        return f'<svg class="e2v-ico" viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{LU[n]}</svg>'
    m = []
    m.append(f'''<section class="e2v-held" id="hero"><div class="e2-wrap e2v-held__raster">
  <div class="e2v-held__text-oben"><h1>{h1}</h1>
    <div class="e2v-held__text">{''.join(f'<p>{p}</p>' for p in texte)}</div></div>
  <div class="e2v-held__pfeil"><svg viewBox="2.83 31.08 226.78 170.29" aria-hidden="true" fill="#1a1817" color="#1a1817">{FORM["forward"]}</svg></div>
  <div class="e2-knoepfe e2v-held__knoepfe"><a class="e2-knopf" href="{knopf.group(1)}">{knopf.group(2)} {PFEIL}</a><a class="e2-knopf e2-knopf--rand" href="#kontakt">Kontakt aufnehmen</a></div>
</div><div class="e2-wrap"><div class="e2-logos">{marquee}</div></div></section>''')
    problem_html = lambda sid, band: f'''<section class="e2-sek e2-sek--gelb" id="{sid}"><div class="e2-wrap">{band}</div><div class="e2-wrap e2v-zwei">
  <div><p class="e2-kicker">{pr_kicker}</p><h2 class="e2-h2">{pr_h2}</h2><p class="e2v-text">{pr_ps[0]}</p></div>
  <div class="e2v-zitat"><ul>{''.join(f'<li>{x}</li>' for x in pr_lis)}</ul><p>{pr_ps[-1]}</p></div>
</div></section>'''
    # Runde 18 (Daniel): Variation B gewählt – Problem gelb · Lösung hell · Formate als schmales Band vor dem Kontakt
    # Runde 16 (Daniel): Lösung und Leistungen gehören zusammen – eine Sektion auf Schwarz.
    # Unterzeile „Lösung“, Überschrift „Wir übersetzen Deine Strategie in Wirkung“, dazu der Handwerk-Satz und die Leitplanken.
    themen_form = ["forward", "kreuz", "kreis"]
    pass  # Lösung auf Schwarz: gesichert in „Startseite alt 2“
    farben = ["gelb", "schwarz", "hell"]
    # Runde 19 (Daniel): Lösung klar wie die Volksfest-Seite – Kopf einspaltig (Unterzeile, Überschrift, ein Satz),
    # dann die Kästen, darunter das Ergebnis mit dem Kontakt-Knopf. Kein Pop-up-Link mehr.
    loesung_hell = f'''<section class="e2-sek" id="loesung"><div class="e2-wrap">
  <p class="e2-kicker">{lo_kicker}</p><h2 class="e2-h2 e2v-loesung3__h">{lo_h2.strip()} {lo_h2_2}</h2>
  <p class="e2-lead e2v-loesung3__lead">{le_lead.replace("sondern Handwerk", "<b>sondern Handwerk</b>")}</p>
  <div class="e2-karten">{''.join(f'<a class="e2-karte" href="{link(hr)}"><div class="e2-karte__kopf"><span class="e2-karte__nr">0{i+1}</span></div><div class="e2-karte__bild e2-karte__bild--{farben[i]}"><div class="e2-karte__ico">{ico}</div><h3>{t}</h3></div><div class="e2-karte__text"><p>{pp}</p><span class="e2-karte__mehr">{mehr} {PFEIL}</span></div></a>' for i, (ico, t, pp, hr, mehr) in enumerate(karten))}</div>
  <div class="e2v-ergebnis2"><div><p class="e2v-ergebnis2__tag">Das Ergebnis</p><p class="e2v-ergebnis2__satz">Du steuerst Deine Themen, statt auf Überraschungen zu reagieren. Die Zusammenhänge sind klar – Deine Themen kommen voran.</p></div>
    <a class="e2-knopf" href="{le_btn.group(1)}">{le_btn.group(2)} {PFEIL}</a></div>
</div></section>'''
    # Formate: Variante A (Daniel, Runde 10) – wie die Leistungs-Karten. Symbole nur in der Akzentfarbe, ohne Fläche/Rahmen.
    # Die Unterformate sind selbst die Links – kein zweiter „Formate ansehen“-Knopf mehr.
    fo_daten = []
    for farbe, titel, koerper in formate:
        ps = alle(r"^\s*<p>(.*?)</p>", koerper, re.S | re.M)
        karten = []
        for stueck in koerper.split('<div class="formate-preview-card')[1:]:
            bild = re.search(r'<svg.*?</svg>|<img[^>]*>', stueck, re.S).group(0).replace(' loading="lazy"', '').replace('class="formate-preview-card-photo" ', '')
            karten.append((bild, eins(r'<div class="formate-preview-title">(.*?)</div>', stueck), eins(r'<p class="formate-preview-desc">(.*?)</p>', stueck)))
        btn = re.search(r'<a class="btn btn--dark btn--sm" href="([^"]+)">(.*?)</a>', koerper)
        fo_daten.append(dict(farbe=farbe, titel=titel, ps=ps, akz=AKZENT.get(farbe, "#1a1817"), href=link(btn.group(1)), knopf=btn.group(2),
                             satz=FORMAT_SATZ.get(re.sub(r"&amp;", "&", titel), ""), sym=FORMAT_GROSS.get(re.sub(r"&amp;", "&", titel), ""),
                             unter=[dict(skizze=sk, titel=t, text=d, href=unter_link(t)) for sk, t, d in karten]))
    fo_kopf = f'''<div class="e2-kopfzeile"><div><p class="e2-kicker">{fo_kicker}</p><h2 class="e2-h2">{fo_h2}</h2></div><div>{''.join(f'<p class="e2-lead">{p}</p>' for p in fo_leads)}</div></div>'''
    va = "".join(f'''<article class="e2-fa" style="--e2-akzent:{d['akz']}"><div class="e2-karte__kopf"><span class="e2-karte__nr">0{i+1}</span></div>
<div class="e2-fa__mitte"><span class="e2-fa__sym">{d['sym']}</span><h3>{d['titel']}</h3></div>
<p class="e2-fa__satz">{d['satz']}</p>
<ul class="e2-fa__liste">{"".join(f'<li><a href="{u["href"]}"><i>{format_sym(u["titel"])}</i>{u["titel"]}{PFEIL}</a></li>' for u in d['unter'])}</ul>
<div class="e2-fa__fuss"><a class="e2-knopf" href="{d['href']}">{d['knopf']} {PFEIL}</a></div></article>''' for i, d in enumerate(fo_daten))
    # Formate als große Kästen: gesichert in „Startseite alt 2“
    # Variante B (Daniel): Formate komplett schwarz wie die Leistungen in Variante A – Farbe nur im Symbol und Strich
    vb = "".join(f'''<article class="e2v-format" style="--e2-akzent:{d['akz']}"><span class="e2v-format__sym">{d['sym']}</span><h3>{d['titel']}</h3>
<p>{d['satz']}</p>
<ul>{"".join(f'<li><a href="{u["href"]}"><i>{format_sym(u["titel"])}</i>{u["titel"]}{PFEIL}</a></li>' for u in d['unter'])}</ul>
<a class="e2v-format__mehr" href="{d['href']}">{d['knopf']} {PFEIL}</a></article>''' for d in fo_daten)
    m.append(problem_html("problem", ""))
    m.append(loesung_hell)
    # Formate: zweite Ebene – schmal, ruhig, ohne Karten und Farbflächen; klar als „andere Qualität“ formuliert
    links = "".join(f'<a href="{d["href"]}" style="--e2-akzent:{d["akz"]}"><i>{d["sym"]}</i><b>{d["titel"]}</b><span>{d["satz"]}</span>{PFEIL}</a>' for d in fo_daten)
    m.append(f'''<section class="e2v-formate-band" id="formate"><div class="e2-wrap e2v-zwei">
  <div><p class="e2-kicker">{fo_kicker}</p><h2 class="e2v-formate-band__h">Außerdem: unsere Erfahrung als fertige Formate.</h2>
    <p class="e2v-formate-band__text">Seit 2012 haben wir mit Versicherern in zahlreichen Projekten gearbeitet. Was sich dabei bewährt hat, gibt es als klar umrissene Formate zum direkten Einsatz – kompakt, ohne langen Vorlauf.</p></div>
  <nav class="e2v-formate-band__links" aria-label="Formate">{links}</nav>
</div></section>''')
    m.append(kontakt_start(abschnitt(h, 'id="kontakt"')))
    return seite("index.html", "\n".join(m))


def main():
    ZIEL.mkdir(parents=True, exist_ok=True)
    (ZIEL / "index.html").write_text(startseite(), encoding="utf-8")
    for orig, ziel in SEITEN.items():
        if orig != "index.html":
            (ZIEL / ziel).write_text(unterseite(orig, ziel), encoding="utf-8")
    import e2_strategie2
    # Runde 23 (Daniel): „Strategie 2“ ist die neue Strategie-Seite; die vorherige Fassung bleibt als strategie-alt.html
    (ZIEL / "strategie-alt.html").write_text((ZIEL / "strategie.html").read_text(encoding="utf-8"), encoding="utf-8")
    neu = unterseite("ki-zum-anfassen.html", "strategie-2.html", e2_strategie2.quelle())
    (ZIEL / "strategie.html").write_text(neu, encoding="utf-8")
    alt = ZIEL / "strategie-2.html"
    if alt.exists():
        alt.unlink()
    print("gebaut:", ", ".join(SEITEN.values()), "+ strategie-alt.html")


if __name__ == "__main__":
    main()
