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

    # Problem (Runde 14, wie die Idee-Sektion der Volksfest-Seite): links Aussage, rechts schwarzer Kasten – Texte aus dem Original
    pr = _abschnitt(sm, 'id="problem"')
    pr_k = _eins(r'<p class="kicker">(.*?)</p>', pr)
    pr_h = re.sub(r'<span class="hl">(.*?)</span>', r"\1", _eins(r"<h2[^>]*>(.*?)</h2>", pr))
    problem = f'''<section class="section e2-s2-problem" id="problem"><div class="container"><div class="e2-s2-split">
<div><p class="kicker">{pr_k}</p><h2 class="h-serif">{pr_h}</h2>
<p class="e2-s2-text">Du bist Abteilungs- oder Bereichsleiter, weil du fachlich überzeugt hast. Was danach oft folgt, sind harte Gespräche mit dem eigenen Team.</p></div>
<div class="e2-s2-kasten"><p class="e2-s2-kasten__satz">Strategisches Denken stand nie auf dem Lehrplan – trotzdem wird es ab dem ersten Tag vorausgesetzt.</p>
<p class="e2-s2-kasten__label">Hart, weil das Fundament fehlt:</p>
<ul><li>die klare Richtung</li><li>die eigene Rolle</li><li>das Handwerkszeug für den Alltag</li></ul></div>
</div></div></section>'''

    # Lösung (Runde 13): links die drei Fragen als ruhige Zeilen mit Symbol, rechts groß das Strategiemodell (wie Original)
    lo = _abschnitt(sm, 'id="loesung-baustein"')
    lo_k, lo_h = _eins(r'<p class="kicker">(.*?)</p>', lo), re.sub(r'<span class="hl">(.*?)</span>', r"\1", _eins(r"<h2[^>]*>(.*?)</h2>", lo))
    lo_ps = re.findall(r'<p class="lead">(.*?)</p>', lo, re.S)
    fragen = [re.sub(r"<[^>]+>", "", f).strip() for f in re.findall(r"<li[^>]*>(.*?)</li>", lo, re.S)]
    modell = _eins(r'(<div class="loesung-modell">.*?</div>\s*</div>\s*</div>)\s*</div>\s*</div>', lo)
    titel = ["Rolle", "Richtung", "Handwerkszeug"]
    symbole = ["flag", "compass", "wrench"]
    zeilen = "".join(f'<li><span class="e2-s2-sym">{_sym(symbole[i])}</span><div><b>{titel[i]}</b><span>{fragen[i]}</span></div></li>' for i in range(3))
    loesung = f'''<section class="section e2-s2-loesung" id="loesung-baustein"><div class="container"><div class="e2-s2-split">
<div><p class="kicker">{lo_k}</p><h2 class="h-serif">{lo_h}</h2><p class="lead">{lo_ps[0]}</p><ul class="e2-s2-liste">{zeilen}</ul><p class="lead e2-s2-schluss">{lo_ps[-1]}</p></div>
{modell}</div></div></section>'''

    # Perspektivwechsel, Ergebnis, Download, Kontakt: Originalabschnitte (werden von e2 wie auf der Strategie-Seite umgesetzt)
    persp = _abschnitt(sm, 'id="perspektive"')
    alt_erg = _abschnitt(sm, 'id="ergebnis"')
    erg_h = _eins(r"<h2[^>]*>(.*?)</h2>", alt_erg)
    erg_p = " ".join(re.findall(r"<p>(.*?)</p>", alt_erg, re.S)) or _eins(r'<p class="lead">(.*?)</p>', alt_erg)
    exp = _eins(r'<p class="pv-exp">(.*?)</p>', persp)
    frage = _eins(r'<p class="pv-q">(.*?)</p>', persp)
    tag = _eins(r'<p class="pv-tag">(.*?)</p>', persp)
    # Schwarzer Streifen (Runde 16): Gedankenexperiment + sein Ergebnis
    ergebnis = f'''<section class="e2-s2-gedanke" id="gedankenexperiment"><div class="container"><div class="e2-s2-split">
<div><p class="e2-s2-gedanke__tag">{tag}</p><p class="e2-s2-gedanke__exp">{exp}</p><p class="e2-s2-gedanke__frage">{frage}</p></div>
<div class="e2-s2-gedanke__erg"><p class="e2-s2-gedanke__tag">Ergebnis</p><p class="e2-s2-gedanke__satz">Jeder im Team versteht, wofür Dein Bereich da ist – und Du bestimmst seine Wahrnehmung.</p></div>
</div></div></section>'''
    download = _abschnitt(sm, 'pdf-dl-section')
    kontakt = _abschnitt(sm, 'id="kontakt"')

    # Zusammenarbeit → Aufklapp-Liste wie „Konkrete Use Cases“
    za = _abschnitt(sm, 'id="zusammenarbeit"')
    za_k, za_h = _eins(r'<p class="kicker">(.*?)</p>', za), _eins(r"<h2[^>]*>(.*?)</h2>", za)
    za_lead = re.findall(r'<p class="lead">(.*?)</p>', za, re.S)
    eintraege = re.findall(r'<summary><span>(.*?)</span></summary>\s*<div class="formate-acc-body">(.*?)</div>\s*</details>', za, re.S)
    # Zusammenarbeit (Runde 16): wie die Schritte der Volksfest-Seite – je ein Satz, der volle Text im Fenster
    kurz = ["Du arbeitest direkt mit mir – und bekommst ehrliches, direktes Feedback.",
            'Die Umsetzung bleibt Deine Aufgabe. Plane <mark class="e2-s2-mark">ein bis zwei Stunden pro Woche</mark> ein.',
            "Regelmäßig abstimmen, flexibel umsteuern – und dann stringent umsetzen."]
    symbole = ["messages-square", "target", "refresh-cw"]
    karten = ""
    for i, (t, b) in enumerate(eintraege):
        karten += (f'<article class="e2-s2-karte"><span class="e2-s2-sym">{_sym(symbole[i])}</span><span class="e2-s2-karte__nr">0{i+1}</span>'
                   f'<h3>{t}</h3><p>{kurz[i]}</p><button type="button" class="e2-s2-karte__mehr" data-e2-auf="za{i}">Mehr lesen →</button>'
                   f'<dialog class="e2-dialog" id="za{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><h3>{t}</h3>{b.strip()}</dialog></article>')
    zusammen = f'''<section class="section e2-s2-zusammen" id="zusammenarbeit"><div class="container">
<p class="kicker">{za_k}</p><h2 class="h-serif">{za_h}</h2>
<div class="e2-s2-karten">{karten}</div></div></section>'''

    main = "\n".join([kopf, problem, loesung, persp, ergebnis, zusammen, download, kontakt])
    i = st.index('<div class="modal-overlay" id="strategiemodellModal"')
    tiefe, j = 0, i
    for mm in re.finditer(r"<div\b|</div>", st[i:]):
        tiefe += 1 if mm.group(0) == "<div" else -1
        if tiefe == 0:
            j = i + mm.end(); break
    modal = st[i:j]
    erg = (f'<div class="e2-s2-modal-erg"><p class="e2-s2-modal-erg__tag">Das Ergebnis</p><p class="e2-s2-modal-erg__satz">{erg_h}</p><p class="modal-structure-note">{erg_p}</p></div>')
    k = modal.rindex("</div>\n      </div>\n    </div>")
    modal = modal[:k] + erg + modal[k:]
    rahmen = rahmen.replace("</footer>", "</footer>\n" + modal, 1)
    a, b = rahmen.index("<main"), rahmen.index("</main>")
    html = rahmen[:a] + "<main>\n" + main + "\n" + rahmen[b:]
    html = re.sub(r"<title>.*?</title>", "<title>Strategie in den Alltag überführen 2 · empiria</title>", html, count=1, flags=re.S)
    return html.replace("produktseite--ki-zum-anfassen", "produktseite--strategie-2")
