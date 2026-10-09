"""empiria 2.0 · Runde 5 (Daniel, 10.10.2026): Sektionen, die nicht mehr nur umgestylt, sondern neu gedacht sind.
Alle Texte kommen weiterhin aus den Originalseiten (nur sinnvoll gekürzt bzw. neu gegliedert).

- Strategie › Perspektivwechsel: Kopf + Browser nebeneinander, darunter eine Kette
  Gedankenexperiment » Wirkung » Ergebnis („Du bestimmst die Wahrnehmung Deines Bereichs“).
- Komplexe Themen › Problem: ohne Nummern – Folienstapel (der Reflex), Folge, offene Fragen.
- Komplexe Themen › Lösung: zwei Phasen als Karten (Erst klären · Dann umsetzen), dazwischen das Zwischenergebnis.
- Download-Kästen: Kicker in der Farbe der Seite, Hervorhebung als Kasten in der Überschrift.
"""
import re

PFEIL = '<svg class="e2-pfeil" viewBox="0 0 24 24" aria-hidden="true"><path d="M5 12h14M13 6l6 6-6 6"/></svg>'
DOPPEL = '<svg class="e2-doppel" viewBox="0 0 24 24" aria-hidden="true"><path d="M4.5 5.5 11 12l-6.5 6.5M12.5 5.5 19 12l-6.5 6.5"/></svg>'


def _eins(muster, html):
    m = re.search(muster, html, re.S)
    assert m, muster[:60]
    return m.group(1).strip()


def _ohne_tags(t):
    return re.sub(r"<[^>]+>", "", t).strip()


def div_block(html, a):
    """Das vollständige <div …>…</div> ab Position a (verschachtelte divs berücksichtigt)."""
    tiefe, i = 0, a
    for m in re.finditer(r"<div\b|</div>", html[a:]):
        tiefe += 1 if m.group(0) == "<div" else -1
        if tiefe == 0:
            return html[a:a + m.end()]
    raise ValueError("div ohne Ende")


# ---------- Strategie: Perspektivwechsel ----------
def perspektive(sek, mit_schritten=True):
    kicker = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="pv-head">.*?<p class="lead">(.*?)</p>', sek)
    browser = _eins(r'(<div class="perspektive-browser".*?</ol>\s*</div>\s*</div>)', sek)
    tag = _eins(r'<p class="pv-tag">(.*?)</p>', sek)
    exp = _eins(r'<p class="pv-exp">(.*?)</p>', sek)
    frage = _eins(r'<p class="pv-q">(.*?)</p>', sek)
    wirkung = _eins(r'<div class="pv-end[^"]*">\s*<p class="lead">(.*?)</p>', sek)
    punch = _ohne_tags(_eins(r'<p class="pv-punch[^"]*">(.*?)</p>', sek))
    # Runde 10 (Daniel): ruhiger – keine Kästen, Wirkung und Ergebnis zu einem kurzen Satz zusammengefasst
    ergebnis = "Jeder im Team versteht, wofür Dein Bereich da ist – und Du bestimmst seine Wahrnehmung."
    schritte = (f'<div class="e2-pv__schritt"><p class="e2-pv__tag">{tag}</p><p>{exp} <b>{frage}</b></p></div>'
                f'<div class="e2-pv__schritt"><p class="e2-pv__tag">Ergebnis</p><p class="e2-pv__punch">{ergebnis}</p></div>') if mit_schritten else ""
    return f'''<section class="e2-pv e2-pv--ruhig" id="perspektive"><div class="container">
  <div class="e2-pv__oben">
    <div class="e2-pv__text"><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p>
      {schritte}</div>
    <div class="e2-pv__browser">{browser}</div>
  </div>
</div></section>'''


# ---------- Komplexe Themen: Problem ohne Nummern ----------
def problem_kt(sek):
    """Runde 11 (Daniel): Dramaturgie wie im schwarzen Kasten der Live-Seite – ein Kasten, von oben nach unten lesbar."""
    kicker = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    ps = re.findall(r"<p>(.*?)</p>", _eins(r'<div class="problem-card">(.*?)</div>', sek), re.S)
    reflexe = re.findall(r"<li>(.*?)</li>", sek, re.S)
    return f'''<section class="section section--grey e2-pkt2" id="problem"><div class="container e2-zwei">
  <div><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2></div>
  <div class="e2-kasten e2-pkt2__kasten"><p class="e2-pkt2__auftakt">{ps[0]}</p>
    <ul>{"".join(f"<li>{r}</li>" for r in reflexe)}</ul>
    <p class="e2-pkt2__folge">{ps[1]}</p><p class="e2-pkt2__fragen">{ps[2]}</p></div>
</div></section>'''


# ---------- Komplexe Themen: Lösung in zwei Phasen ----------
def loesung_kt(sek):
    """Runde 11 (Daniel): ruhig wie die Wagenpaten-Seite – vier gleiche Schritte mit Kurzsatz, Details zum Aufklappen (Fenster),
    darunter das Zwischenergebnis."""
    from e2_lucide import ICONS
    kopf = _eins(r'(<div class="leistung-stufen-head">.*?</div>)', sek)
    items = []
    for m in re.finditer(r'<div class="stufen-timeline-item', sek):
        block = div_block(sek, m.start())
        nr = _eins(r'<span class="stl-icon">(\d+)</span>', block)
        items.append((nr, div_block(block, block.index('<div class="stufe-content'))))
    pause = _eins(r'(<div class="stufe-break[^"]*">.*?</div>)\s*<div class="stufen-timeline stufen-timeline--bottom">', sek)
    p_tag = _eins(r'<p class="stufe-interim-tag">(.*?)</p>', pause)
    p_h = _ohne_tags(_eins(r"<h3>(.*?)</h3>", pause))
    p_ps = re.findall(r"<p>(.*?)</p>", pause, re.S)
    kurz = ["Welches Ergebnis willst Du – und welche Bedeutung hat Dein Thema für die Zielgruppe?",
            "Warum? Wie? Was jetzt? – verdichtet zu einer klaren Kernbotschaft.",
            "Aus der Business Story entstehen Medien – gezielt für den jeweiligen Einsatz.",
            "Dein Vorgehen vor, während und nach dem Termin – bis zum Ergebnis."]
    symbole = ["target", "message-square-text", "presentation", "clipboard-list"]

    def sym(n):
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="#fff" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'

    karten = ""
    for i, (nr, inh) in enumerate(items):
        h3 = _eins(r"<h3>(.*?)</h3>", inh)
        rest = re.sub(r"<h3>.*?</h3>", "", inh, count=1, flags=re.S)
        rest = re.sub(r'^<div class="stufe-content[^"]*">|</div>$', "", rest.strip())
        karten += (f'<article class="e2-schritt"><div class="e2-schritt__kopf"><span class="e2-schritt__sym">{sym(symbole[i])}</span><span class="e2-schritt__nr">{nr}</span></div>'
                   f'<h3>{h3}</h3><p>{kurz[i]}</p><button type="button" class="e2-schritt__mehr" data-e2-auf="ls{i}">Mehr dazu {PFEIL}</button>'
                   f'<dialog class="e2-dialog e2-dialog--breit" id="ls{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><h3>{h3}</h3><div class="e2-lk__inhalt">{rest}</div></dialog></article>')
    spoiler_kopf, spoiler = p_ps[1].split("<br>", 1)
    return f'''<section class="section e2-lkt2" id="loesung-baustein"><div class="container">
  <div class="e2-lkt__kopf">{kopf}</div>
  <div class="e2-schritte">{karten}</div>
  <div class="e2-zwischen"><p class="e2-zwischen__tag">{p_tag} · nach Schritt 2</p><h3>{p_h}</h3><p>{p_ps[0]} <b>{_ohne_tags(spoiler_kopf)}</b> {spoiler.strip()}</p></div>
</div></section>'''


# ---------- Download: Hervorhebung bleibt als Kasten ----------
def download_hl(main, magenta):
    zus = " e2-dl-hl--magenta" if magenta else ""
    return re.sub(r'(<h2 class="pdf-dl-h">.*?)<span class="hl-acc">(.*?)</span>', rf'\1<span class="e2-dl-hl{zus}">\2</span>', main, flags=re.S)
