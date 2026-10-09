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
    if not mit_schritten:
        # Strategie 2 (Runde 17): Gedankenexperiment gehört zum Perspektivwechsel – ohne die Frage zu wiederholen;
        # das Ergebnis als schwarzes Band unten in derselben Sektion.
        return f'''<section class="e2-pv e2-pv--ruhig e2-pv--s2" id="perspektive"><div class="container">
  <div class="e2-pv__oben">
    <div class="e2-pv__text"><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p>
      <div class="e2-pv__schritt"><p class="e2-pv__tag">{tag}</p><p>{exp} Was stünde darauf – und würde jeder im Team dasselbe hineinschreiben?</p></div></div>
    <div class="e2-pv__browser">{browser}</div>
  </div>
  <div class="e2-pv__band"><p class="e2-pv__band-tag">Ergebnis</p><p class="e2-pv__band-satz">{ergebnis}</p></div>
</div></section>'''
    return f'''<section class="e2-pv e2-pv--ruhig" id="perspektive"><div class="container">
  <div class="e2-pv__oben">
    <div class="e2-pv__text"><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p>
      {schritte}</div>
    <div class="e2-pv__browser">{browser}</div>
  </div>
</div></section>'''


# ---------- Innovation: Problem wie Strategie 2 (Runde 23) ----------
def problem_inno(sek):
    kicker = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = re.sub(r'<span class="hl">(.*?)</span>', r"\1", _eins(r"<h2[^>]*>(.*?)</h2>", sek))
    ps = re.findall(r"<p>(.*?)</p>", sek, re.S)
    lis = re.findall(r"<li>(.*?)</li>", sek, re.S)
    return f'''<section class="section e2-s2-problem" id="problem"><div class="container"><div class="e2-s2-split">
<div><p class="kicker">{kicker}</p><h2 class="h-serif">{h2}</h2><p class="e2-s2-text">{ps[0]}</p></div>
<div class="e2-s2-kasten"><p class="e2-s2-kasten__label" style="margin-top:0!important;padding-top:0;border-top:0">Dabei bleibt offen:</p>
<ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul><p class="e2-s2-kasten__label">{ps[-1]}</p></div>
</div></div></section>'''


# ---------- Innovation: Lösung im Volksfest-Aufbau (Runde 25) ----------
def loesung_inno(sek):
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek)
    h2 = re.sub(r'<span class="hl">(.*?)</span>', r"\1", _eins(r"<h2[^>]*>(.*?)</h2>", sek))
    leads = re.findall(r'<p class="lead">(.*?)</p>', sek, re.S)
    stein = _eins(r'(<div class="inno-stein[^"]*"[^>]*>.*?</div>)', sek)
    titel = [re.sub(r"<br>", " ", t) for t in re.findall(r'<span class="inno-einsatz-title">(.*?)</span>', sek, re.S)]
    scope = _eins(r'<p class="inno-scope">(.*?)</p>', sek)
    ansatz_tag = _eins(r'<p class="inno-greenfield-tag">(.*?)</p>', sek)
    ansatz = re.sub(r'<span class="hl">(.*?)</span>', r'<span class="e2-gelb-text">\1</span>', _eins(r'<p class="inno-greenfield-text">(.*?)</p>', sek))
    sym = ["trending-up", "handshake", "blocks", "puzzle", "sparkles"]
    def ic(n):
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="#1a1817" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
    karten = "".join(f'<li><span class="e2-in-sym">{ic(sym[i])}</span><b>{t}</b></li>' for i, t in enumerate(titel))
    return f'''<section class="section e2-in-loesung" id="loesung-baustein"><div class="container">
  <div class="e2-s2-split e2-in-oben"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2><p class="lead">{leads[0]}</p><p class="lead">{leads[1]}</p></div>{stein}</div>
  <div class="e2-in-einsatz"><p class="e2-in-label">Einsatzmöglichkeiten</p><p class="lead">{leads[2]}</p><ul class="e2-in-karten">{karten}</ul><p class="e2-in-scope">{scope}</p></div>
  <div class="e2-s2-split e2-in-methode"><div><p class="e2-in-label">Unsere Methoden</p><p class="lead">{leads[3]}</p><p class="lead">{leads[4]}</p></div>
    <div class="e2-in-ansatz"><p class="e2-in-ansatz__tag">{ansatz_tag}</p><p class="e2-in-ansatz__satz">{ansatz}</p></div></div>
</div></section>'''


# ---------- Teams befähigen: lange Timeline → Phasen + drei Inhalts-Karten (Runde 29) ----------
def loesung_teams(sek):
    from e2_lucide import ICONS
    kopf = div_block(sek, sek.index('<div class="leistung-stufen-head">'))
    kopf = re.sub(r'<span class="hl">(.*?)</span>', r"\1", kopf)
    leads = re.findall(r'<p class="lead">(.*?)</p>', kopf, re.S)
    k = _eins(r'<p class="kicker">(.*?)</p>', kopf); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", kopf)
    phasen = re.findall(r'<span class="onboarding-step-title">(.*?)</span>\s*<span class="onboarding-step-duration">(.*?)</span>', sek, re.S)
    knopf = re.search(r'(<button type="button" class="btn btn--dark js-onboarding-open">.*?</button>)', sek, re.S)
    items = []
    for m in re.finditer(r'<div class="stufen-timeline-item', sek):
        block = div_block(sek, m.start())
        nr = _eins(r'<span class="stl-icon">(\d+)</span>', block)
        inhalt = div_block(block, block.index('<div class="stufe-content'))
        items.append((nr, inhalt))
    sym = ["message-square-text", "presentation", "refresh-cw", "users"]
    def ic(n, farbe="#fff"):
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
    phasen_html = "".join(f'<li><span class="e2-ph__nr">{i+1}</span><b>{t}</b><small>{d}</small></li>' for i, (t, d) in enumerate(phasen))
    karten = ""
    for i, (nr, inh) in enumerate(items):
        h3 = _eins(r"<h3>(.*?)</h3>", inh)
        ms = re.search(r"<h3>.*?</h3>.*?<p>(.*?)</p>", inh, re.S)
        satz = ms.group(1) if ms else ""
        rest = re.sub(r'^<div class="stufe-content[^"]*">|</div>$', "", inh.strip())
        karten += (f'<article class="e2-schritt"><div class="e2-schritt__kopf"><span class="e2-schritt__sym">{ic(sym[i % 4])}</span><span class="e2-schritt__nr">{nr}</span></div>'
                   f'<h3>{h3}</h3><p>{satz}</p><button type="button" class="e2-schritt__mehr" data-e2-auf="tm{i}">Module &amp; Ergebnis →</button>'
                   f'<dialog class="e2-dialog e2-dialog--breit" id="tm{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><div class="e2-lk__inhalt">{rest}</div></dialog></article>')
    return f'''<section class="section e2-teams-loesung" id="loesung-baustein"><div class="container">
  <div class="e2-s2-split e2-in-oben"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2><p class="lead">{leads[0]}</p></div>
    <div>{"".join(f'<p class="lead">{x}</p>' for x in leads[1:])}</div></div>
  <p class="e2-in-label" style="margin-top:4rem!important">Ablauf</p>
  <ol class="e2-phasen">{phasen_html}</ol>
  {('<p class="e2-phasen__knopf">' + knopf.group(1) + '</p>') if knopf else ""}
  <p class="e2-in-label" style="margin-top:4rem!important">Inhalte</p>
  <div class="e2-schritte e2-schritte--3">{karten}</div>
</div></section>'''


# ---------- 1:1 Sparring: Themen und Umsetzungsturbo im Volksfest-Aufbau (Runde 30) ----------
def sparring_themen(sek):
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    wann = re.findall(r'<div class="tc-row[^"]*">.*?<span>(.*?)</span>', sek, re.S)
    worueber = re.findall(r'<li class="reveal"><svg.*?</svg><span>(.*?)</span></li>', sek, re.S)
    sym = ["coffee", "mountain", "car", "message-circle"]
    def ic(n):
        n = n if n in ICONS else "message-circle"
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
    wege = "".join(f'<li><span class="e2-sp2-sym">{ic(sym[i])}</span><b>{t}</b></li>' for i, t in enumerate(wann))
    themen = "".join(f"<li>{t}</li>" for t in worueber)
    return f'''<section class="produkt-section e2-sp-themen e2-sp2"><div class="container">
  <div class="e2-s2-split e2-faelle__kopf"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div><p class="lead">{lead}</p></div>
  <div class="e2-sp2-wann"><p class="e2-sp2-label">Wann wir sprechen</p><ul>{wege}</ul></div>
  <div class="e2-sp2-worueber"><p class="e2-sp2-label">Worüber wir sprechen</p><ul>{themen}<li class="e2-sp2-mehr">… und vieles mehr</li></ul></div>
</div></section>'''


def sparring_gegenueber(sek):
    """Runde 35: sechs Eigenschaften ohne Kästen – weiße Icons, weiße Linien auf der Bereichsfarbe (wie die Volksfest-Seite)."""
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    items = re.findall(r"<h3>(.*?)</h3><p>(.*?)</p>", sek, re.S)
    sym = ["lock", "award", "layers", "compass", "rocket", "megaphone"]
    def ic(n):
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
    li = "".join(f'<li><span class="e2-gg__sym">{ic(sym[i % 6])}</span><h3>{t}</h3><p>{x}</p></li>' for i, (t, x) in enumerate(items))
    return f'''<section class="produkt-grid e2-gg"><div class="container">
  <div class="e2-s2-split e2-faelle__kopf"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div><p class="lead">{lead}</p></div>
  <ul class="e2-gg__liste">{li}</ul>
</div></section>'''


def sparring_turbo(sek):
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    ps = re.findall(r"<p>(.*?)</p>", sek, re.S)
    lis = re.findall(r"<li><svg.*?</svg><span>(.*?)</span></li>", sek, re.S)
    return f'''<section class="produkt-section e2-sp-turbo"><div class="container"><div class="e2-s2-split">
  <div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2><p class="lead">{ps[0]}</p></div>
  <div class="e2-s2-kasten"><ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul>
    <p class="e2-s2-kasten__label">{ps[1]}</p><p class="e2-sp-turbo__satz">{ps[2] if len(ps) > 2 else ""}</p></div>
</div></div></section>'''


# ---------- Praxisfälle als Karten statt Akkordeon (Runde 32) ----------
def faelle(sek, symbole, sonder=None, kurz=False, kurztexte=None, sonder_kurz=None, sonder_label="Sonderthema"):
    """kurztexte (Runde 34, Daniel): je Karte ein eigener kurzer Satz – „Mehr lesen“ öffnet den vollen Text im Fenster."""
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    items = re.findall(r'<summary>(.*?)</summary>(.*?)</details>', sek, re.S)
    def ic(n, farbe="#fff"):
        return f'<svg viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>'
    karten, sonder_html, j = "", "", 0
    for i, (titel, body) in enumerate(items):
        ps = re.findall(r"<p>(.*?)</p>", body, re.S)
        if sonder is not None and i == sonder:
            sonder_html = (f'<div class="e2-fall-sonder"><div><p class="e2-fall-sonder__tag">{sonder_label}</p><h3>{titel.strip()}</h3></div>'
                           f'<div><p>{sonder_kurz or ps[0]}</p><button type="button" class="e2-fall__mehr e2-fall__mehr--hell" data-e2-auf="fs{i}">Mehr lesen →</button></div>'
                           f'<dialog class="e2-dialog" id="fs{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><h3>{titel.strip()}</h3>{"".join(f"<p>{x}</p>" for x in ps)}</dialog></div>')
            continue
        erster = kurztexte[j] if kurztexte else (re.split(r"(?<=[.!?])\s", ps[0])[0] if ps else "")
        text = "".join(f"<p>{x}</p>" for x in ps) if kurz else f"<p>{erster}</p>"
        mehr = "" if kurz else (f'<button type="button" class="e2-fall__mehr" data-e2-auf="fl{i}">Mehr lesen →</button>'
                                f'<dialog class="e2-dialog" id="fl{i}"><button type="button" class="e2-dialog__zu" aria-label="Schließen">×</button><h3>{titel.strip()}</h3>{"".join(f"<p>{x}</p>" for x in ps)}</dialog>')
        karten += f'<article class="e2-fall"><span class="e2-fall__sym">{ic(symbole[j % len(symbole)])}</span><h3>{titel.strip()}</h3>{text}{mehr}</article>'
        j += 1
    return f'''<section class="produkt-section e2-faelle"><div class="container">
  <div class="e2-s2-split e2-faelle__kopf"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div><p class="lead">{lead}</p></div>
  <div class="e2-faelle__raster{" e2-faelle__raster--4" if j == 4 else ""}">{karten}</div>{sonder_html}
</div></section>'''


def preis_sprint(sek):
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    betrag = _eins(r'<span class="price-note-amount">(.*?)</span>', sek); einheit = _eins(r'<span class="price-note-unit">(.*?)</span>', sek)
    lis = re.findall(r"<li>(.*?)</li>", sek, re.S); fuss = _eins(r'<p class="pricing-footnote[^"]*">(.*?)</p>', sek)
    return f'''<section class="produkt-section e2-preis"><div class="container"><div class="e2-s2-split">
  <div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p><p class="e2-preis__fuss">{fuss}</p></div>
  <div class="e2-preis__box"><p class="e2-preis__label">{einheit}</p><p class="e2-preis__betrag">{betrag}</p>
    <ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul></div>
</div></div></section>'''


# ---------- Sprint: Ablauf + Vorteile in einer Sektion (Runde 34) ----------
def ablauf_vorteile(ablauf, vorteile):
    """Die drei Vorteils-Kästen stehen rechts neben der Zeitleiste statt verloren darunter."""
    karten = [div_block(vorteile, m.start()) for m in re.finditer(r'<div class="produkt-glass', vorteile)]
    rechts = "".join(re.sub(r'^<div class="[^"]*">', '<div class="e2-ablauf__vorteil">', k) for k in karten)
    tl = ablauf.index('<div class="sprint-timeline')
    tl_ende = div_block(ablauf, tl)
    zeit = tl_ende.replace(' style="max-width:760px;margin:0 auto;"', "")
    neu = f'<div class="e2-ablauf">{zeit}<div class="e2-ablauf__vorteile">{rechts}</div></div>'
    return ablauf.replace(tl_ende, neu).replace('<section class="produkt-section">', '<section class="produkt-section e2-ablauf-sek">', 1)


# ---------- Problem als Text + schwarzer Kasten (wie Strategie/Innovation, Runde 38) ----------
def problem_kasten(sek):
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lis = re.findall(r"<li>([^<]*(?:<(?!/?li\b)[^<]*)*)</li>", sek.split("<ul>", 1)[1].split("</ul>", 1)[0]) if "<ul>" in sek else []
    schluss = re.findall(r"<p>(.*?)</p>", sek, re.S)
    return f'''<section class="section e2-s2-problem" id="problem"><div class="container"><div class="e2-s2-split">
<div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div>
<div class="e2-s2-kasten"><ul>{"".join(f"<li>{x.strip()}</li>" for x in lis)}</ul>{f'<p class="e2-s2-kasten__label">{schluss[-1]}</p>' if schluss else ""}</div>
</div></div></section>'''


# ---------- Teams: „Das Konzept zum Nachlesen“ als Text + schwarzer Kasten (Runde 38) ----------
def teams_download(sek):
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek); lead = _eins(r'<p class="lead">(.*?)</p>', sek)
    titel = _eins(r'<p class="leadmagnet-title">(.*?)</p>', sek)
    knopf = re.search(r'<a class="btn btn--dark leadmagnet-cta" href="([^"]*)">(.*?)</a>', sek)
    tag = re.search(r'<span class="leadmagnet-tag">(.*?)</span>', sek)
    ico = f'<svg viewBox="0 0 24 24" fill="none" stroke="#fff400" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS["file-text"]}</svg>'
    return f'''<section class="section e2-teams-dl" id="austausch"><div class="container"><div class="e2-s2-split">
  <div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2><p class="lead">{lead}</p></div>
  <div class="e2-s2-kasten e2-teams-dl__kasten"><span class="e2-teams-dl__ico">{ico}</span><p class="e2-teams-dl__titel">{titel}</p>
    <a class="e2-teams-dl__knopf" href="{knopf.group(1)}">{knopf.group(2)}</a>{f'<p class="e2-teams-dl__tag">{tag.group(1)}</p>' if tag else ""}</div>
</div></div></section>'''


# ---------- Preise als „Post-Karten“ wie Social Media auf der Volksfest-Seite (Runde 39, Test KI zum Anfassen) ----------
def preise_posts(sek, symbole):
    """weißer Kopf (Kurzsatz + ggf. „Meistgewählt“) · Farbfläche (Dauer, Name, Preis, Symbol; grau – gelb – grau) · weißer Fuß (Beschreibung + Inhalte)."""
    from e2_lucide import ICONS
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    karten = ""
    for i, m in enumerate(re.finditer(r'<div class="produkt-glass price-card([^"]*)"', sek)):
        b = div_block(sek, m.start()); top = "featured" in m.group(1)
        name = _eins(r"<h3>(.*?)<span", b); dauer = _eins(r'<span class="price-name-sub">(.*?)</span>', b)
        desc = _eins(r'<p class="price-desc[^"]*">(.*?)</p>', b); preis = _eins(r'<span class="price-amount">(.*?)</span>', b)
        note = _eins(r'<p class="price-note">(.*?)</p>', b); lis = re.findall(r"<li>(.*?)</li>", b, re.S)
        ico = f'<svg class="e2-post__ico" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true">{ICONS[symbole[i % len(symbole)]]}</svg>'
        karten += (f'<article class="e2-post{" e2-post--top" if top else ""}">'
                   f'<div class="e2-post__kopf"><span>{note}</span>{"<em>Meistgewählt</em>" if top else ""}</div>'
                   f'<div class="e2-post__bild"><small>{dauer}</small><div class="e2-post__unten"><div><b>{name}</b><span class="e2-post__preis">{preis}</span></div>{ico}</div></div>'
                   f'<div class="e2-post__text"><p>{desc}</p><ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul></div></article>')
    fuss = re.search(r'<p class="pricing-footnote[^"]*">(.*?)</p>', sek, re.S)
    return f'''<section class="produkt-grid produkt-pricing e2-posts-sek"><div class="container">
  <div class="e2-s2-split e2-faelle__kopf"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div><p class="lead">{lead}</p></div>
  <div class="e2-posts">{karten}</div>{f'<p class="e2-preis__fuss e2-posts__fuss">{fuss.group(1)}</p>' if fuss else ""}
</div></section>'''


# ---------- Pakete als saubere Karten (Runde 34) ----------
def pakete(sek):
    k = _eins(r'<p class="kicker">(.*?)</p>', sek); h2 = _eins(r"<h2[^>]*>(.*?)</h2>", sek)
    lead = _eins(r'<div class="produkt-section-head[^"]*">.*?<p>(.*?)</p>', sek)
    karten = ""
    for m in re.finditer(r'<div class="produkt-glass price-card([^"]*)"', sek):
        block = div_block(sek, m.start())
        top = "price-card--featured" in m.group(1)
        badge = re.search(r'<span class="price-badge">(.*?)</span>', block)
        titel = _eins(r"<h3>(.*?)</h3>", block)
        desc = _eins(r'<p class="price-desc[^"]*">(.*?)</p>', block)
        betrag = _eins(r'<span class="price-amount">(.*?)</span>', block)
        einheit = re.search(r'<span class="price-unit">(.*?)</span>', block).group(1).strip()
        lis = re.findall(r"<li>(.*?)</li>", block, re.S)
        ideal = re.sub(r"<br\s*/?>", " ", _eins(r'<p class="price-ideal">(.*?)</p>', block)) if "price-ideal" in block else ""
        knopf = re.search(r'(<button type="button" class="btn[^"]*price-more-btn"[^>]*>.*?</button>)', block, re.S)
        knopf = knopf.group(1).replace('class="btn btn--outline btn--sm price-more-btn"', 'class="e2-paket__mehr"') if knopf else ""
        karten += (f'<article class="e2-paket{" e2-paket--top" if top else ""}">'
                   f'<p class="e2-paket__badge">{badge.group(1) if badge else "&nbsp;"}</p><h3>{titel}</h3>'
                   f'<p class="e2-paket__preis">{betrag}<small>{einheit}</small></p><p class="e2-paket__desc">{desc}</p>'
                   f'<ul>{"".join(f"<li>{x}</li>" for x in lis)}</ul><p class="e2-paket__ideal">{ideal}</p>{knopf}</article>')
    fuss = re.search(r'<p class="pricing-footnote[^"]*">(.*?)</p>', sek, re.S)
    return f'''<section class="produkt-grid e2-pakete" id="pakete"><div class="container">
  <div class="e2-s2-split e2-faelle__kopf"><div><p class="kicker">{k}</p><h2 class="h-serif">{h2}</h2></div><p class="lead">{lead}</p></div>
  <div class="e2-pakete__raster">{karten}</div>{f'<p class="e2-preis__fuss">{fuss.group(1)}</p>' if fuss else ""}
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
