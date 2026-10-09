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
def perspektive(sek):
    kicker = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="pv-head">.*?<p class="lead">(.*?)</p>', sek)
    browser = _eins(r'(<div class="perspektive-browser".*?</ol>\s*</div>\s*</div>)', sek)
    tag = _eins(r'<p class="pv-tag">(.*?)</p>', sek)
    exp = _eins(r'<p class="pv-exp">(.*?)</p>', sek)
    frage = _eins(r'<p class="pv-q">(.*?)</p>', sek)
    wirkung = _eins(r'<div class="pv-end[^"]*">\s*<p class="lead">(.*?)</p>', sek)
    punch = _ohne_tags(_eins(r'<p class="pv-punch[^"]*">(.*?)</p>', sek))
    return f'''<section class="e2-pv" id="perspektive"><div class="container">
  <div class="e2-pv__oben">
    <div><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p></div>
    <div class="e2-pv__browser">{browser}</div>
  </div>
  <div class="e2-pv__kette">
    <div class="e2-pv__glied"><p class="e2-pv__tag">{tag}</p><p>{exp} <b>{frage}</b></p></div>
    <span class="e2-pv__pfeil">{DOPPEL}</span>
    <div class="e2-pv__glied"><p class="e2-pv__tag">Die Wirkung</p><p>{wirkung}</p></div>
    <span class="e2-pv__pfeil">{DOPPEL}</span>
    <div class="e2-pv__glied e2-pv__glied--ergebnis"><p class="e2-pv__tag">Ergebnis</p><p class="e2-pv__punch">{punch}</p></div>
  </div>
</div></section>'''


# ---------- Komplexe Themen: Problem ohne Nummern ----------
def problem_kt(sek):
    kicker = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    ps = re.findall(r"<p>(.*?)</p>", _eins(r'<div class="problem-card">(.*?)</div>', sek), re.S)
    reflexe = re.findall(r"<li>(.*?)</li>", sek, re.S)
    # „Wer sitzt im Raum, wie gewinnst du …, in welchen Schritten …? Mit diesen Fragen …“ → drei Fragen + Schlusssatz
    fragen_satz, schluss = ps[2].split("?", 1)
    fragen = [f.strip() for f in fragen_satz.split(",")]
    fragen = [f[0].upper() + f[1:] + "?" for f in fragen]
    folien = "".join(f'<div class="e2-folie e2-folie--{i}"><span class="e2-folie__kopf"><i></i><i></i><i></i></span><p>{t}</p></div>' for i, t in enumerate(reflexe))
    return f'''<section class="section section--grey e2-pkt" id="problem"><div class="container">
  <div class="e2-pkt__raster">
    <div class="e2-pkt__kopf"><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2></div>
    <div class="e2-pkt__reflex"><p class="e2-pkt__label">{ps[0]}</p><div class="e2-folien">{folien}</div></div>
  </div>
  <div class="e2-pkt__folge">
    <div class="e2-pkt__aber"><p>{ps[1]}</p></div>
    <div class="e2-pkt__fragen"><ul>{"".join(f"<li><span>?</span>{f}</li>" for f in fragen)}</ul><p>{schluss.strip()}</p></div>
  </div>
</div></section>'''


# ---------- Komplexe Themen: Lösung in zwei Phasen ----------
def loesung_kt(sek):
    kopf = _eins(r'(<div class="leistung-stufen-head">.*?</div>)', sek)
    items = []
    for m in re.finditer(r'<div class="stufen-timeline-item', sek):
        block = div_block(sek, m.start())
        nr = _eins(r'<span class="stl-icon">(\d+)</span>', block)
        inhalt = div_block(block, block.index('<div class="stufe-content'))
        items.append((nr, inhalt))
    assert len(items) == 4, len(items)
    pause = _eins(r'(<div class="stufe-break[^"]*">.*?</div>)\s*<div class="stufen-timeline stufen-timeline--bottom">', sek)
    p_tag = _eins(r'<p class="stufe-interim-tag">(.*?)</p>', pause)
    p_h = _ohne_tags(_eins(r"<h3>(.*?)</h3>", pause))
    p_ps = re.findall(r"<p>(.*?)</p>", pause, re.S)
    spoiler_kopf, spoiler = p_ps[1].split("<br>", 1)

    def karte(nr, inhalt):
        h3 = _eins(r"<h3>(.*?)</h3>", inhalt)
        rest = re.sub(r"<h3>.*?</h3>", "", inhalt, count=1, flags=re.S)
        rest = re.sub(r'^<div class="stufe-content[^"]*">|</div>$', "", rest.strip())
        return f'<article class="e2-lk"><div class="e2-lk__kopf"><span class="e2-lk__nr">{nr}</span><h3>{h3}</h3></div><div class="e2-lk__inhalt">{rest}</div></article>'

    # Business Story: Why / How / What next als drei Zeilen
    def story(html):
        if 'class="story-accordion"' not in html:
            return html
        alt = div_block(html, html.index('<div class="story-accordion"'))
        neu = '<dl class="e2-story">' + "".join(f"<div><dt>{t}</dt><dd>{d}</dd></div>" for t, d in re.findall(r'<span class="story-acc-title">(.*?)</span>.*?<p>(.*?)</p>', alt, re.S)) + "</dl>"
        return html.replace(alt, neu)

    k = [karte(nr, story(inh)) for nr, inh in items]
    return f'''<section class="section e2-lkt" id="loesung-baustein"><div class="container">
  <div class="e2-lkt__kopf">{kopf}</div>
  <p class="e2-lkt__phase"><b>Erst klären</b> – bevor eine Folie entsteht</p>
  <div class="e2-lkt__paar">{k[0]}{k[1]}</div>
  <div class="e2-lkt__pause">
    <div><p class="e2-lkt__tag">{p_tag}</p><h3>{p_h}</h3><p>{p_ps[0]}</p></div>
    <div class="e2-lkt__spoiler"><b>{_ohne_tags(spoiler_kopf)}</b><span>{spoiler.strip()}</span></div>
  </div>
  <p class="e2-lkt__phase"><b>Dann umsetzen</b> – gezielt für den Termin</p>
  <div class="e2-lkt__paar">{k[2]}{k[3]}</div>
</div></section>'''


# ---------- Download: Hervorhebung bleibt als Kasten ----------
def download_hl(main, magenta):
    zus = " e2-dl-hl--magenta" if magenta else ""
    return re.sub(r'(<h2 class="pdf-dl-h">.*?)<span class="hl-acc">(.*?)</span>', rf'\1<span class="e2-dl-hl{zus}">\2</span>', main, flags=re.S)
