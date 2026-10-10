#!/usr/bin/env python3
"""PowerPoint-/Keynote-Master – Entwicklungsseite (Daniel, 10.10.2026).

Stufe 1: Grundsystem. Hintergründe (Weiß als Grundseite, Schwarz, Gelb, Grau, Magenta, Violett, Cyan),
drei Header-Ideen, Schriften, Designelemente der Homepage, Hervorhebung mit Sekundärfarben.
Folien sind 16:9-Attrappen in HTML; daraus werden später die echten Master in PowerPoint und Keynote gebaut.

Aufruf: python3 werkzeuge/ppt_master.py  → site/projekte/powerpoint-master.html
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SITE = HERE.parent / "site"
sys.path.insert(0, str(HERE))
from e2_bauen import FORM  # noqa: E402
from e2_lucide import ICONS  # noqa: E402

FARBEN = {  # Name, Hex, Schrift auf der Fläche, Akzent auf der Fläche
    "weiss": ("Weiß", "#ffffff", "#1a1817", "#fff400"),
    "schwarz": ("Schwarz", "#1a1817", "#ffffff", "#fff400"),
    "gelb": ("Gelb", "#fff400", "#1a1817", "#1a1817"),
    "grau": ("Grau", "#f3f1ee", "#1a1817", "#fff400"),
    "magenta": ("Magenta", "#C51F5D", "#ffffff", "#fff400"),
    "violett": ("Violett", "#8613A1", "#ffffff", "#fff400"),
    "cyan": ("Cyan", "#0B9FBD", "#ffffff", "#fff400"),
}


def zeichen(name, farbe):
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg viewBox="{vb}" fill="{farbe}" color="{farbe}" aria-hidden="true">{FORM[name]}</svg>'


def ico(n, farbe="currentColor"):
    return (f'<svg viewBox="0 0 24 24" fill="none" stroke="{farbe}" stroke-width="1.6" stroke-linecap="round" '
            f'stroke-linejoin="round" aria-hidden="true">{ICONS[n]}</svg>')


def logo(hell):
    return f'<img class="f-logo" src="/assets/empiria-logo{"-weiss" if hell else ""}.svg" alt="empiria">'


def folie(farbe, inhalt, header="A", thema="Strategie in den Alltag", nr="04", fuss=True, cls="", label=None):
    name, bg, fg, akz = FARBEN[farbe]
    hell = fg == "#ffffff"
    kopf = {
        # A: Logo links, Thema rechts als Kicker – ruhig, wie die Website
        "A": f'<div class="f-kopf f-kopf--a">{logo(hell)}<span class="f-thema">{thema}</span></div>',
        # B: gelber Balken links oben + Thema, Logo rechts
        "B": f'<div class="f-kopf f-kopf--b"><span class="f-balken"></span><span class="f-thema">{thema}</span>{logo(hell)}</div>',
        # C: kein Kopf – Doppelpfeil klein rechts oben, Logo im Fuß
        "C": f'<div class="f-kopf f-kopf--c"><span class="f-mini">{zeichen("forward", fg if farbe != "weiss" else "#1a1817")}</span></div>',
        "-": "",
    }[header]
    fussz = ""
    if fuss:
        links = logo(hell) if header == "C" else '<span class="f-strich"></span>'
        fussz = f'<div class="f-fuss">{links}<span>empiria GmbH</span><span>{nr}</span></div>'
    return (f'<figure class="f-wrap"><div class="folie {cls}" style="--bg:{bg};--fg:{fg};--akz:{akz}"><div class="f-innen">{kopf}{inhalt}</div>{fussz}</div>'
            f'<figcaption class="f-label">{label or name}</figcaption></figure>')


def kicker(t):
    return f'<p class="f-kicker">{t}</p>'


def stufe1():
    s = []
    # 1 · Hintergründe
    flaechen = []
    flaechen.append(folie("weiss", f'<div class="f-titel">{kicker("Strategiehandwerk")}<h1>Strategie,<br>die <span class="hl">wirkt.</span></h1>'
                                   f'<p class="f-sub">Titelfolie · Grundseite Weiß</p></div><span class="f-gross">{zeichen("forward", "#1a1817")}</span>', header="-", fuss=False, cls="f--titel"))
    flaechen.append(folie("schwarz", f'<div class="f-titel">{kicker("Kapitel 01")}<h1>Das Problem.</h1><p class="f-sub">Kapitelfolie · Schwarz</p></div>'
                                     f'<span class="f-gross f-gross--klein">{zeichen("forward", "#fff400")}</span>', header="-", fuss=False))
    flaechen.append(folie("gelb", f'<div class="f-titel">{kicker("Kapitel 02")}<h1>Die Lösung.</h1><p class="f-sub">Kapitelfolie · Gelb</p></div>'
                                  f'<span class="f-gross f-gross--klein">{zeichen("forward", "#1a1817")}</span>', header="-", fuss=False))
    flaechen.append(folie("grau", f'<div class="f-titel">{kicker("Kapitel 03")}<h1>Das Vorgehen.</h1><p class="f-sub">Kapitelfolie · Grau</p></div>'
                                  f'<span class="f-gross f-gross--klein">{zeichen("forward", "#1a1817")}</span>', header="-", fuss=False))
    for f, t in (("magenta", "Workshops"), ("violett", "Training &amp; Sparring"), ("cyan", "Marketing 2.0")):
        flaechen.append(folie(f, f'<div class="f-titel">{kicker("Themenfarbe")}<h1>{t}.</h1><p class="f-sub">Vollfläche · {FARBEN[f][0]}</p></div>'
                                 f'<span class="f-gross f-gross--klein">{zeichen("forward", "#ffffff")}</span>', header="-", fuss=False))
    s.append(("1 · Hintergründe", "Weiß ist die Grundseite. Schwarz, Gelb und Grau gliedern. Magenta, Violett und Cyan als Vollfläche für Themen, Kapitel oder Statements.",
              flaechen))

    # 2 · Header-Ideen
    inhalt = (kicker("Ausgangslage") + '<h2>Drei Fragen, die jede Führungskraft <span class="hl">kennt.</span></h2>'
              '<div class="f-punkte">' + "".join(f'<div>{ico(i)}<b>{t}</b><p>{p}</p></div>' for i, t, p in
                                                 [("flag", "Rolle", "Was erwartet man von mir – und was nicht?"),
                                                  ("compass", "Richtung", "Wohin entwickelt sich mein Bereich?"),
                                                  ("wrench", "Handwerk", "Wie übersetze ich das in den Alltag?")]) + '</div>')
    s.append(("2 · Header – drei Ideen", "A: Logo links, Thema als Kicker rechts (wie die Website). B: gelber Balken + Thema links, Logo rechts. C: kein Kopf – kleiner Doppelpfeil oben rechts, Logo wandert in den Fuß.",
              [folie("weiss", inhalt, header="A", label="Idee A · Logo links, Thema rechts"), folie("weiss", inhalt, header="B", label="Idee B · gelber Balken + Thema, Logo rechts"),
               folie("weiss", inhalt, header="C", label="Idee C · Doppelpfeil oben, Logo im Fuß")]))

    # 3 · Hervorhebung mit Sekundärfarben (auf Weiß)
    hervor = []
    for f in ("magenta", "violett", "cyan"):
        _, bg, _, _ = FARBEN[f]
        hervor.append(folie("weiss", kicker("Hervorhebung") + f'<h2>Ein Thema bekommt <span class="hl" style="background:{bg};color:#fff">seine Farbe.</span></h2>'
                                      f'<div class="f-zwei"><div class="f-kasten" style="background:{bg}"><b>Kernaussage</b><p>Kasten in der Themenfarbe für die eine Botschaft, die hängen bleiben soll.</p></div>'
                                      f'<div class="f-liste">' + "".join(f'<p><span style="background:{bg}"></span>{x}</p>' for x in ["Punkte in der Themenfarbe", "Linien und Icons in Schwarz", "Gelb bleibt das empiria-Highlight"]) + '</div></div>',
                            header="A", thema=FARBEN[f][0]))
    s.append(("3 · Sekundärfarben als Hervorhebung", "Auf der weißen Grundseite markieren Magenta, Violett und Cyan ein Thema: Highlight, Kasten, Aufzählungspunkte. Gelb bleibt das empiria-Highlight für alles andere.", hervor))

    # 4 · Designelemente der Homepage
    elem = [
        folie("weiss", kicker("Designelement") + '<h2>Gelbes Band mit <span class="hl">Punkten.</span></h2>'
                       '<div class="f-band"><div class="f-punkte f-punkte--klein">' + "".join(f'<div><b>{t}</b><p>{p}</p></div>' for t, p in
                                                                                             [("Klar", "Eine Botschaft je Folie."), ("Ruhig", "Viel Weißraum, wenig Text."), ("Wirksam", "Ergebnis statt Aufzählung.")]) + '</div></div>'),
        folie("weiss", kicker("Designelement") + '<h2>Ablauf als <span class="hl">Zeitstrahl.</span></h2>'
                       '<ol class="f-zs">' + "".join(f'<li><span></span><small>0{i+1}</small><b>{t}</b></li>' for i, t in enumerate(["Verstehen", "Ordnen", "Entscheiden", "Umsetzen"])) + '</ol>'),
        folie("weiss", '<div class="f-zwei f-zwei--mitte"><div>' + kicker("Designelement") + '<h2>Schwarzer Kasten für die <span class="hl">Kernaussage.</span></h2></div>'
                       '<div class="f-kasten" style="background:#1a1817"><b style="color:#fff400">Das Ergebnis</b><p>Du führst Dein Team, statt es zu vertrösten.</p></div></div>'),
        folie("schwarz", kicker("Zitat") + '<p class="f-zitat">„Strategie ist keine Zauberei, sondern <span class="hl">Handwerk.</span>“</p><p class="f-sub">Daniel Ströbel</p>', header="A"),
    ]
    s.append(("4 · Designelemente der Homepage", "Kicker mit Strich, gelber Highlight-Kasten, gelbes Band mit Punkten, Zeitstrahl, schwarzer Kasten, Doppelpfeil – dieselben Bausteine wie auf www.empiria.de.", elem))

    # 5 · Schrift & Farben
    typo = folie("weiss", '<div class="f-zwei"><div>' + kicker("Schriften") +
                 '<p class="f-typo1">Lora Bold</p><p class="f-typo-info">Überschriften · 28–60 pt</p>'
                 '<p class="f-typo2">Poppins Regular / Light</p><p class="f-typo-info">Text · 14–20 pt</p>'
                 '<p class="f-typo3">POPPINS BOLD · KICKER</p><p class="f-typo-info">Kicker · 10–12 pt, Großbuchstaben, gesperrt</p></div>'
                 '<div>' + kicker("Farben") + '<div class="f-farben">' + "".join(
                     f'<div><span style="background:{bg};border:1px solid #e4e0db"></span><b>{n}</b><small>{bg.upper()}</small></div>' for n, bg, _, _ in FARBEN.values()) + '</div></div></div>')
    s.append(("5 · Schriften & Farben", "Was im Master hinterlegt wird: Lora für Überschriften, Poppins für Text, sieben Farben im Farbschema.", [typo]))
    return s


CSS = """
.pm { padding: 6rem 0 5rem; }
.pm-kicker { display: flex; align-items: center; gap: .75rem; margin: 0 0 1.1rem; font: 700 .8rem/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #1a1817; }
.pm-kicker::before { content: ""; width: 1.6rem; height: 2px; background: #1a1817; }
.pm h1 { font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.2; font-size: clamp(2.4rem, 5vw, 4rem); margin: 0; color: #1a1817; }
.pm .hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; }
.pm-lead { max-width: 46rem; margin: 1.2rem 0 0; font-size: 1.1rem; line-height: 1.6; font-weight: 300; color: #3d3a37; }
.pm-stufen { display: flex; gap: .5rem; flex-wrap: wrap; margin-top: 1.6rem; }
.pm-stufen span { padding: .45rem .9rem; border-radius: 999px; border: 1px solid #d9d5ce; font: 500 .8rem/1 'Poppins', sans-serif; color: #6f6a64; }
.pm-stufen span.aktiv { background: #1a1817; color: #fff; border-color: #1a1817; }
.pm-abschnitt { margin-top: 4rem; }
.pm-abschnitt h2 { font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 1.7rem; margin: 0; }
.pm-abschnitt > p { max-width: 50rem; margin: .6rem 0 0; color: #3d3a37; line-height: 1.6; }
.pm-raster { display: grid; grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 1.4rem; margin-top: 1.6rem; }
@media (max-width: 800px) { .pm-raster { grid-template-columns: 1fr; } }

/* Folie 16:9 – Maße relativ zur Folienbreite (cqw), damit jede Größe stimmt */
.folie { position: relative; aspect-ratio: 16 / 9; container-type: inline-size; background: var(--bg); color: var(--fg); border-radius: 10px; overflow: hidden;
  box-shadow: 0 0 0 1px #e4e0db, 0 12px 30px rgba(26,24,23,.06); font-family: 'Poppins', sans-serif; }
.f-innen { position: absolute; inset: 0; padding: 9.5cqw 6cqw 8cqw; }
.f-wrap { margin: 0; }
.f-label { margin-top: .7rem; font: 600 .72rem/1.4 'Poppins', sans-serif; letter-spacing: .1em; text-transform: uppercase; color: #8a847c; }
.f-logo { height: 2.2cqw; width: auto; display: block; }
.f-kopf { position: absolute; top: 3cqw; left: 6cqw; right: 6cqw; display: flex; align-items: center; justify-content: space-between; }
.f-thema { font: 700 1.05cqw/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; display: flex; align-items: center; gap: .8cqw; }
.f-kopf--a .f-thema::before { content: ""; width: 2cqw; height: .18cqw; background: currentColor; }
.f-kopf--b { justify-content: flex-start; gap: 1.4cqw; }
.f-kopf--b .f-logo { margin-left: auto; }
.f-balken { width: .7cqw; height: 3cqw; background: #fff400; border-radius: .2cqw; }
.f-kopf--c { justify-content: flex-end; }
.f-mini svg { width: 4.2cqw; height: auto; display: block; }
.f-fuss { position: absolute; left: 6cqw; right: 6cqw; bottom: 2.6cqw; display: flex; align-items: center; gap: 1.4cqw; font-size: .95cqw; opacity: .7; }
.f-fuss span:last-child { margin-left: auto; }
.f-fuss .f-logo { height: 1.6cqw; }
.f-strich { width: 2cqw; height: .18cqw; background: currentColor; }
.f-kicker { display: flex; align-items: center; gap: .8cqw; margin: 0 0 1.4cqw; font: 700 1.1cqw/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.f-kicker::before { content: ""; width: 2cqw; height: .18cqw; background: currentColor; }
.folie h1 { margin: 0; font: 700 6.2cqw/1.18 'Lora', Georgia, serif; letter-spacing: -.02em; color: var(--fg); }
.folie h2 { margin: 0; max-width: 70cqw; font: 700 3.6cqw/1.25 'Lora', Georgia, serif; letter-spacing: -.015em; color: var(--fg); }
.folie .hl { background: var(--akz); color: #1a1817; padding: 0 .12em .07em; border-radius: .14em; }
.f-sub { margin: 2cqw 0 0; font-size: 1.5cqw; opacity: .75; }
.f-titel { position: absolute; left: 6cqw; bottom: 8cqw; max-width: 60cqw; }
.f-gross { position: absolute; right: 6cqw; top: 50%; transform: translateY(-50%); width: 28cqw; }
.f-gross--klein { width: 14cqw; top: auto; bottom: 8cqw; transform: none; }
.f-gross svg { width: 100%; height: auto; display: block; }
.f--titel .f-titel { bottom: auto; top: 50%; transform: translateY(-50%); }
.f-punkte { display: grid; grid-template-columns: repeat(3, 1fr); gap: 3cqw; margin-top: 3.6cqw; }
.f-punkte > div { border-top: .16cqw solid currentColor; padding-top: 1.6cqw; }
.f-punkte svg { width: 2.6cqw; height: 2.6cqw; display: block; margin-bottom: 1cqw; }
.f-punkte b { display: block; font: 700 1.9cqw/1.2 'Lora', serif; }
.f-punkte p { margin: .7cqw 0 0; font-size: 1.3cqw; line-height: 1.5; opacity: .8; }
.f-zwei { display: grid; grid-template-columns: 1fr 1fr; gap: 4cqw; margin-top: 3.4cqw; align-items: start; }
.f-zwei--mitte { align-items: center; margin-top: 4cqw; }
.f-kasten { border-radius: 1.4cqw; padding: 2.6cqw 2.8cqw; color: #fff; }
.f-kasten b { font: 700 1.1cqw/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.f-kasten p { margin: 1.2cqw 0 0; font: 700 2.1cqw/1.35 'Lora', serif; }
.f-liste p { display: flex; align-items: center; gap: 1.2cqw; margin: 0; padding: 1.3cqw 0; border-bottom: .1cqw solid #e4e0db; font-size: 1.45cqw; }
.f-liste span { width: 1cqw; height: 1cqw; border-radius: 50%; flex: 0 0 auto; }
.f-band { margin: 3.4cqw -6cqw 0; padding: 3cqw 6cqw; background: #fff400; color: #1a1817; }
.f-band .f-punkte { margin-top: 0; }
.f-zs { list-style: none; display: grid; grid-template-columns: repeat(4, 1fr); position: relative; margin: 6cqw 0 0; padding: 0; }
.f-zs::before { content: ""; position: absolute; left: 0; right: 0; top: .6cqw; height: .16cqw; background: #1a1817; }
.f-zs li span { display: block; width: 1.4cqw; height: 1.4cqw; border-radius: 50%; background: #1a1817; box-shadow: 0 0 0 .5cqw #fff400; position: relative; margin-bottom: 2.2cqw; }
.f-zs small { font: 700 1cqw/1 'Poppins', sans-serif; letter-spacing: .14em; }
.f-zs b { display: block; margin-top: .8cqw; font: 700 2cqw/1.2 'Lora', serif; }
.f-zitat { margin: 2cqw 0 0; max-width: 72cqw; font: 700 4.4cqw/1.3 'Lora', serif; }
.f-typo1 { margin: 0; font: 700 4.2cqw/1.1 'Lora', serif; }
.f-typo2 { margin: 2.4cqw 0 0; font: 400 2.4cqw/1.2 'Poppins', sans-serif; }
.f-typo3 { margin: 2.4cqw 0 0; font: 700 1.3cqw/1 'Poppins', sans-serif; letter-spacing: .14em; }
.f-typo-info { margin: .6cqw 0 0; font-size: 1.1cqw; opacity: .6; }
.f-farben { display: grid; grid-template-columns: repeat(4, 1fr); gap: 1.6cqw; }
.f-farben span { display: block; height: 5cqw; border-radius: .8cqw; }
.f-farben b { display: block; margin-top: .7cqw; font-size: 1.15cqw; }
.f-farben small { font-size: 1cqw; opacity: .6; }
"""


def bauen():
    rahmen = (SITE / "projekte" / "corporate-design.html").read_text(encoding="utf-8")
    a, b = rahmen.index("<main"), rahmen.index("</main>") + 7
    abschnitte = "".join(
        f'<div class="pm-abschnitt"><h2>{t}</h2><p>{p}</p><div class="pm-raster">{"".join(f)}</div></div>' for t, p, f in stufe1())
    main = f'''<main>
<section class="pm"><div class="container">
  <p class="pm-kicker">Geschäftsausstattung</p>
  <h1>PowerPoint- &amp; Keynote-<span class="hl">Master</span></h1>
  <p class="pm-lead">Wir arbeiten uns in Stufen heran. Erst das Grundsystem – Hintergründe, Header, Schriften, Farben und Designelemente –, dann die einzelnen Folientypen, dann die Darstellungsvarianten. Am Ende entstehen daraus die echten Vorlagen in PowerPoint und Keynote.</p>
  <div class="pm-stufen"><span class="aktiv">Stufe 1 · Grundsystem</span><span>Stufe 2 · Folientypen</span><span>Stufe 3 · Darstellungsvarianten</span><span>Stufe 4 · PowerPoint &amp; Keynote</span></div>
  {abschnitte}
</div></section>
<style>{CSS}</style>
</main>'''
    seite = rahmen[:a] + main + rahmen[b:]
    seite = re.sub(r"<title>.*?</title>", "<title>PowerPoint- &amp; Keynote-Master – empiria (intern)</title>", seite, count=1, flags=re.S)
    (SITE / "projekte" / "powerpoint-master.html").write_text(seite, encoding="utf-8")
    print("gebaut: site/projekte/powerpoint-master.html")


if __name__ == "__main__":
    bauen()
