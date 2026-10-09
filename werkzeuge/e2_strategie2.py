"""„Strategie in den Alltag überführen 2“ (Daniel, 10.10.2026): derselbe Inhalt wie die Strategie-Seite,
aber im Aufbau der Workshop-Seiten (KI zum Anfassen) – damit alle Unterseiten dieselbe Logik haben:
Kopf · „Das bekommst Du“ mit drei Karten · Perspektivwechsel · Ergebnis · Zusammenarbeit als Aufklapp-Liste · Download · Kontakt.

quelle() liefert eine vollständige Seite im Markup der Produktseiten (Rahmen von ki-zum-anfassen.html, Inhalt aus
leistungen/strategie.html). e2_bauen.unterseite() macht daraus die 2.0-Fassung.
"""
import re
from pathlib import Path
from e2_lucide import ICONS

SITE = Path(__file__).resolve().parent.parent / "site"


def _abschnitt(html, marker):
    a = html.rfind("<section", 0, html.find(marker) + 8)
    tiefe, i = 0, a
    while True:
        o, c = html.find("<section", i + 1), html.find("</section>", i + 1)
        if o != -1 and o < c:
            tiefe += 1; i = o
        else:
            if tiefe == 0:
                return html[a:c + 10]
            tiefe -= 1; i = c


def _eins(m, h):
    x = re.search(m, h, re.S)
    assert x, m[:50]
    return x.group(1).strip()


def _sym(n):
    return f'<svg viewBox="0 0 24 24" fill="none" stroke="#1a1817" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'


def quelle():
    st = (SITE / "leistungen" / "strategie.html").read_text(encoding="utf-8")
    sm = st[st.index("<main"):st.index("</main>")]
    rahmen = (SITE / "ki-zum-anfassen.html").read_text(encoding="utf-8")

    # Kopf (Inhalt der Strategie-Seite, Aufbau der Produktseiten)
    held = _abschnitt(sm, 'leistung-hero')
    h1 = _eins(r"<h1[^>]*>(.*?)</h1>", held)
    lead = re.sub(r"<[^>]+>", "", _eins(r'<div class="hero-copy[^"]*">(.*?)</div>', held)).strip()
    kopf = f'''<section class="produkt-hero"><div class="container"><div class="produkt-hero-grid"><div class="produkt-hero-text">
<p class="kicker">Strategiehandwerk</p><h1 class="h-serif">{h1}</h1><p class="lead">{lead}</p></div><div class="produkt-hero-visual"></div></div>
<div class="produkt-hero-actions produkt-hero-actions--center"><a class="btn btn--dark" href="#problem">Mehr erfahren</a></div></div></section>'''

    # Problem → Abschnitt mit Kopf und Text (wie „Das bekommst Du“, ohne Karten)
    pr = _abschnitt(sm, 'id="problem"')
    pr_k, pr_h = _eins(r'<p class="kicker">(.*?)</p>', pr), _eins(r"<h2[^>]*>(.*?)</h2>", pr)
    pr_ps = re.findall(r"<p>(.*?)</p>", pr, re.S)
    problem = f'''<section class="produkt-grid" id="problem"><div class="container"><div class="produkt-section-head">
<p class="kicker">{pr_k}</p><h2 class="h-serif">{pr_h}</h2>{"".join(f"<p>{p}</p>" for p in pr_ps)}</div></div></section>'''

    # Lösung → „Das bekommst Du“-Karten: Rolle · Richtung · Handwerkszeug mit ihren Fragen
    lo = _abschnitt(sm, 'id="loesung-baustein"')
    lo_k, lo_h = _eins(r'<p class="kicker">(.*?)</p>', lo), _eins(r"<h2[^>]*>(.*?)</h2>", lo)
    lo_ps = re.findall(r"<p(?: class=\"lead\")?>(.*?)</p>", lo, re.S)
    fragen = [re.sub(r"<[^>]+>", "", f).strip() for f in re.findall(r"<li[^>]*>(.*?)</li>", lo, re.S)]
    titel = ["Rolle", "Richtung", "Handwerkszeug"]
    symbole = ["flag", "compass", "wrench"]
    karten = "".join(f'<div class="produkt-glass"><div class="feature-icon">{_sym(symbole[i])}</div><h3>{titel[i]}</h3><p>{fragen[i]}</p></div>' for i in range(3))
    loesung = f'''<section class="produkt-grid" id="loesung-baustein"><div class="container"><div class="produkt-section-head">
<p class="kicker">{lo_k}</p><h2 class="h-serif">{lo_h}</h2><p>{lo_ps[0] if lo_ps else ""}</p></div>
<div class="produkt-grid-cards">{karten}</div>{f'<p class="e2-s2-notiz">{lo_ps[-1]}</p>' if len(lo_ps) > 1 else ""}</div></section>'''

    # Perspektivwechsel, Ergebnis, Download, Kontakt: Originalabschnitte (werden von e2 wie auf der Strategie-Seite umgesetzt)
    persp = _abschnitt(sm, 'id="perspektive"')
    ergebnis = _abschnitt(sm, 'id="ergebnis"')
    download = _abschnitt(sm, 'pdf-dl-section')
    kontakt = _abschnitt(sm, 'id="kontakt"')

    # Zusammenarbeit → Aufklapp-Liste wie „Konkrete Use Cases“
    za = _abschnitt(sm, 'id="zusammenarbeit"')
    za_k, za_h = _eins(r'<p class="kicker">(.*?)</p>', za), _eins(r"<h2[^>]*>(.*?)</h2>", za)
    za_lead = re.findall(r'<p class="lead">(.*?)</p>', za, re.S)
    eintraege = re.findall(r'<summary><span>(.*?)</span></summary>\s*<div class="formate-acc-body">(.*?)</div>\s*</details>', za, re.S)
    liste = "".join(f'<details class="produkt-faq-item" name="produkt-faq"><summary>{t}</summary>{b.strip()}</details>' for t, b in eintraege)
    zusammen = f'''<section class="produkt-section produkt-faq" id="zusammenarbeit"><div class="container"><div class="produkt-section-head">
<p class="kicker">{za_k}</p><h2 class="h-serif">{za_h}</h2>{"".join(f"<p>{p}</p>" for p in za_lead[:1])}</div><div class="produkt-faq-list">{liste}</div></div></section>'''

    main = "\n".join([kopf, problem, loesung, persp, ergebnis, zusammen, download, kontakt])
    a, b = rahmen.index("<main"), rahmen.index("</main>")
    html = rahmen[:a] + "<main>\n" + main + "\n" + rahmen[b:]
    html = re.sub(r"<title>.*?</title>", "<title>Strategie in den Alltag überführen 2 · empiria</title>", html, count=1, flags=re.S)
    return html.replace("produktseite--ki-zum-anfassen", "produktseite--strategie-2")
