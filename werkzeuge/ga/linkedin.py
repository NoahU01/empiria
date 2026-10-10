#!/usr/bin/env python3
"""Geschäftsausstattung · LinkedIn-Banner (Entwurf, Daniel 10.10.2026).

Personenprofil 1584 × 396 px (links unten liegt das runde Profilfoto – dort nichts Wichtiges),
Firmenprofil 1128 × 191 px (links unten liegt das Firmenlogo). Je vier Varianten: Weiß, Gelb, Schwarz, Formen.
Alle Maße werden in Originalpixeln geplant und in cqw umgerechnet – Vorschau und PNG sind dieselbe Gestaltung.

Aufruf: python3 werkzeuge/ga/linkedin.py           → Seite + PNGs
        python3 werkzeuge/ga/linkedin.py --ohne-png → nur Seite
Ergebnis: site/projekte/ga-linkedin.html, site/projekte/ga/linkedin/*.png
"""
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from ga_export import (FORM, GELB, GRAU, PFEIL_VERH, SCHWARZ, SEITE_CSS, SITE, WEISS, download, exportieren,  # noqa: E402
                       form, kopf, px_fn, seite)

ORDNER = SITE / "projekte" / "ga" / "linkedin"
WEB = "/projekte/ga/linkedin"

PERSONEN = {
    "daniel": ("Daniel Ströbel", "Geschäftsführer / Strategiehandwerker", "Strategiehandwerker"),
    "kerstin": ("Kerstin Christ", "Expertin HR &amp; Weiterbildung", "HR &amp; Weiterbildung"),
    "noah": ("Noah Hermanns", "Experte Performance Marketing", "Performance Marketing"),
}

# Varianten (nur Daniel und die Unternehmensseite, bis die Gestaltung steht)
# Schlüssel: Name, Beschreibung
VARIANTEN = {
    "weiss": ("Weiß", "Ruhig wie die Startseite: weiße Fläche, der Claim mit gelbem Highlight, rechts der Doppelpfeil."),
    "schwarz": ("Schwarz mit Anschnitt", "Weißer Claim auf Schwarz, gelbes Highlight, gelber Doppelpfeil im Anschnitt."),
    "logos-start": ("Kundenlogos", "Der Claim groß, darunter alle 14 Kundenlogos in Originalfarbe auf Weiß. "
                    "Rechts läuft ein großer schwarzer Doppelpfeil aus dem Bild."),
}
FARBEN = {  # Hintergrund, Schrift, Highlight-Fläche, Highlight-Schrift, Pfeil
    "weiss": (WEISS, SCHWARZ, GELB, SCHWARZ, SCHWARZ),
    "schwarz": (SCHWARZ, WEISS, GELB, SCHWARZ, GELB),
    "logos-start": (WEISS, SCHWARZ, GELB, SCHWARZ, SCHWARZ),
}


def treppe(p, W, H, groesse, rechts, oben, versatz_x, versatz_y):
    kacheln = [(GELB, "forward", SCHWARZ), (SCHWARZ, "kreuz", GELB), ("#f3f1ee", "kreis", SCHWARZ)]
    x0 = W - rechts - groesse - 2 * versatz_x
    out = ""
    for i, (bg, z, f) in enumerate(kacheln):
        out += (f'<div style="left:{p(x0 + i * versatz_x)};top:{p(oben + i * versatz_y)};width:{p(groesse)};height:{p(groesse)};'
                f'background:{bg};border-radius:{p(groesse * .12)};display:flex;align-items:center;justify-content:center">'
                f'<span style="display:block;width:{p(groesse * .52)}">{form(z, f)}</span></div>')
    return out


def muster(p, W, H, x_start, zelle, breite):
    out = ""
    spalten = int((W - x_start) // zelle)
    zeilen = int(H // zelle)
    oy = (H - zeilen * zelle) / 2
    for r in range(zeilen):
        for c in range(spalten):
            an = (c, r) == (spalten - 3, zeilen // 2)
            out += pfeil(p, breite, x_start + (c + .5) * zelle, oy + (r + .5) * zelle, GELB if an else "#2e2b28")
    return out


CSS = """
.lb { position: relative; width: 100%; container-type: inline-size; overflow: hidden; background: var(--bg); color: var(--fg); font-family: 'Poppins', sans-serif; }
.lb > * { position: absolute; }
.lb-text { top: 50%; transform: translateY(-50%); }
.lb-kicker { display: flex; align-items: center; margin: 0; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; line-height: 1; }
.lb-kicker::before { content: ""; background: currentColor; flex: 0 0 auto; }
.lb h2 { margin: 0; font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.3; color: var(--fg); white-space: nowrap; }
.lb .hl { background: var(--hlbg); color: var(--hlfg); padding: 0 .12em .07em; border-radius: .14em; }
.lb-fuss { display: flex; align-items: center; margin: 0; font-weight: 400; line-height: 1; opacity: .8; }
.lb-fuss img { display: block; width: auto; }
.lb-raster { display: grid; }
.lb-raster > span { display: flex; align-items: center; justify-content: center; background: #fff; }
.lb-raster > span.gelb { background: #fff400; }
"""

# ----- LinkedIn-Attrappe (nur Seite) -----
SEITE_EXTRA = """
.li { background: #fff; border-radius: 12px; overflow: hidden; box-shadow: 0 0 0 1px #e4e0db, 0 12px 30px rgba(26,24,23,.06); container-type: inline-size; font-family: -apple-system, 'Segoe UI', 'Poppins', sans-serif; }
.li-banner { position: relative; border-bottom: 1px solid #e4e0db; }
.li-foto { position: absolute; left: 3cqw; top: 11cqw; width: 18.9cqw; aspect-ratio: 1; border-radius: 50%; border: .55cqw solid #fff; background: #ddd center/cover; }
.li-logo { position: absolute; left: 2.6cqw; top: 9.6cqw; width: 12cqw; aspect-ratio: 1; border-radius: .8cqw; border: .45cqw solid #fff; background: #fff; box-shadow: 0 0 0 1px #e4e0db; display: flex; align-items: center; justify-content: center; }
.li-logo img { width: 78%; height: auto; }
.li-info { display: flex; justify-content: space-between; gap: 3cqw; padding: 7.2cqw 3cqw 3cqw; }
.li-info--firma { padding-top: 6cqw; }
.li-name { margin: 0; font-size: 2.9cqw; font-weight: 600; color: #1d1d1d; line-height: 1.2; }
.li-rolle { margin: .5cqw 0 0; font-size: 1.85cqw; color: #1d1d1d; line-height: 1.35; }
.li-ort { margin: .7cqw 0 0; font-size: 1.6cqw; color: #666; }
.li-knoepfe { display: flex; gap: 1cqw; margin-top: 1.8cqw; }
.li-knoepfe span { padding: .75cqw 1.9cqw; border-radius: 99px; font-size: 1.6cqw; font-weight: 600; border: .14cqw solid #0a66c2; color: #0a66c2; }
.li-knoepfe span:first-child { background: #0a66c2; color: #fff; }
.li-firma { display: flex; align-items: center; gap: 1cqw; font-size: 1.6cqw; font-weight: 600; color: #1d1d1d; white-space: nowrap; }
.li-firma i { width: 3.6cqw; height: 3.6cqw; border-radius: .4cqw; background: #fff400; display: flex; align-items: center; justify-content: center; }
.li-firma i img { width: 82%; }
.lz { position: relative; }
.lz-foto { position: absolute; border-radius: 50%; border: 2px dashed #C51F5D; background: repeating-linear-gradient(45deg, rgba(197,31,93,.16) 0 6px, rgba(197,31,93,.05) 6px 12px); }
.lz-text { position: absolute; font: 600 .78rem/1.3 'Poppins', sans-serif; color: #C51F5D; }
.lg-raster { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 1.2rem; margin-top: 1.4rem; }
.lg-raster .lb { box-shadow: 0 0 0 1px #e4e0db; border-radius: 6px; }
.lg-gross { margin-top: 1.4rem; max-width: 860px; }
.lg-gross > .lb { box-shadow: 0 0 0 1px #e4e0db; border-radius: 6px; }
.lg-raster--2 { grid-template-columns: repeat(2, minmax(0, 1fr)); gap: 2rem 1.4rem; }
.lg-raster--li { grid-template-columns: minmax(0, 1.25fr) minmax(0, 1fr); gap: 1.6rem; align-items: start; }
@media (max-width: 800px) { .lg-raster, .lg-raster--2, .lg-raster--li { grid-template-columns: 1fr; } }
"""


def pfeil(p, breite, cx, cy, farbe):
    return (f'<div style="position:absolute;left:{p(cx - breite / 2)};top:{p(cy - breite * PFEIL_VERH / 2)};width:{p(breite)}">'
            f'{form("forward", farbe)}</div>')


def claim(p, groesse, zweizeilig=False):
    return f'<h2 style="font-size:{p(groesse)}">Strategie,{"<br>" if zweizeilig else " "}die <span class="hl">wirkt.</span></h2>'


def rahmen(cls, var, W, H, inhalt):
    bg, fg, hlbg, hlfg, _ = FARBEN[var]
    return (f'<div class="lb {cls}" style="aspect-ratio:{W}/{H};--bg:{bg};--fg:{fg};--hlbg:{hlbg};--hlfg:{hlfg}">{inhalt}</div>')


def kicker_html(p, text, groesse, gap, strich, dicke, extra=""):
    return (f'<p class="lb-kicker" style="font-size:{p(groesse)};gap:{p(gap)};{extra}">'
            f'<i style="display:block;width:{p(strich)};height:{p(dicke)};background:currentColor"></i>{text}</p>')


def wechsel_flaechen(p, W, H, g, b, cx):
    """Oben Gelb, unten Schwarz; der Pfeil sitzt auf der Kante und wechselt die Farbe."""
    return (f'<div style="left:0;top:0;width:100%;height:{p(g)};overflow:hidden;background:{GELB}">{pfeil(p, b, cx, g, SCHWARZ)}</div>'
            f'<div style="left:0;top:{p(g)};width:100%;height:{p(H - g)};overflow:hidden;background:{SCHWARZ}">'
            f'<div style="position:absolute;left:0;top:{p(-g)};width:100%;height:{p(H)}">{pfeil(p, b, cx, g, GELB)}</div></div>')


def person_banner(var):
    """Personenbanner 1584 × 396. Das Profilfoto deckt links unten ca. x 45–350 ab → Inhalt beginnt bei x 470."""
    W, H = 1584, 396
    p = px_fn(W)
    _, _, _, _, pf = FARBEN[var]
    x = 470
    k = lambda extra="": kicker_html(p, "Strategiehandwerker", 18, 14, 36, 3.5, "margin:0 0 " + p(16) + ";" + extra)
    if var.startswith("logos"):
        return rahmen("", var, W, H, person_logos(var.split("-")[1]))
    if var == "weiss":
        inhalt = (f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k()}{claim(p, 70)}</div>'
                  + pfeil(p, 210, W - 110 - 105, H / 2, pf))
    elif var == "schwarz":
        b = .9 * H / PFEIL_VERH
        inhalt = (f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k()}{claim(p, 72, True)}</div>'
                  + pfeil(p, b, W - .3 * b, H / 2, pf))
    elif var == "treppe":
        inhalt = (f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k()}{claim(p, 72, True)}</div>'
                  + treppe(p, W, H, 104, 84, 46, 124, 100))
    elif var == "muster":
        inhalt = (muster(p, W, H, 1000, 112, 66)
                  + f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k()}{claim(p, 72, True)}</div>')
    else:  # wechsel
        g = .62 * H
        b = 1.5 * (H - g) / PFEIL_VERH
        inhalt = (wechsel_flaechen(p, W, H, g, b, W - 100 - b / 2)
                  + f'<div style="left:{p(x)};top:{p(g / 2)};transform:translateY(-50%)">{k()}{claim(p, 60)}</div>')
    return rahmen("", var, W, H, inhalt)


def firma_banner(var):
    """Firmenbanner 1128 × 191. Das Firmenlogo deckt links unten ca. x 30–165 ab → Inhalt beginnt bei x 250."""
    W, H = 1128, 191
    p = px_fn(W)
    _, _, _, _, pf = FARBEN[var]
    x = 250
    k = kicker_html(p, "Strategiehandwerk · Crailsheim", 12, 10, 24, 2.4, "margin:0 0 " + p(12) + ";")
    if var.startswith("logos"):
        return rahmen("", var, W, H, firma_logos(var.split("-")[1]))
    if var == "weiss":
        inhalt = f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k}{claim(p, 46)}</div>' + pfeil(p, 112, W - 64 - 56, H / 2, pf)
    elif var == "schwarz":
        b = .9 * H / PFEIL_VERH
        inhalt = f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k}{claim(p, 46)}</div>' + pfeil(p, b, W - .3 * b, H / 2, pf)
    elif var == "treppe":
        inhalt = (f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k}{claim(p, 46)}</div>'
                  + treppe(p, W, H, 50, 56, 22, 60, 48))
    elif var == "muster":
        inhalt = (muster(p, W, H, 760, 62, 36)
                  + f'<div style="left:{p(x)};top:50%;transform:translateY(-50%)">{k}{claim(p, 46)}</div>')
    else:
        g = .64 * H
        b = 1.5 * (H - g) / PFEIL_VERH
        inhalt = (wechsel_flaechen(p, W, H, g, b, W - 56 - b / 2)
                  + f'<div style="left:{p(x)};top:{p(g / 2)};transform:translateY(-50%)">{claim(p, 40)}</div>')
    return rahmen("", var, W, H, inhalt)


def attrappe_person(var):
    name, rolle, _ = PERSONEN["daniel"]
    return (f'<div class="li"><div class="li-banner">{person_banner(var)}'
            f'<span class="li-foto" style="background-image:url(/assets/ansprechpartner-daniel.webp)"></span></div>'
            f'<div class="li-info"><div><p class="li-name">{name}</p><p class="li-rolle">{rolle} · empiria GmbH</p>'
            f'<p class="li-ort">Crailsheim, Baden-Württemberg</p>'
            f'<div class="li-knoepfe"><span>Vernetzen</span><span>Nachricht</span></div></div>'
            f'<div class="li-firma"><i><span style="display:block;width:64%">{form("forward", SCHWARZ)}</span></i>empiria GmbH</div></div></div>')


def attrappe_firma(var):
    return (f'<div class="li"><div class="li-banner">{firma_banner(var)}'
            f'<span class="li-logo"><img src="/assets/empiria-logo.svg" alt="empiria"></span></div>'
            f'<div class="li-info li-info--firma"><div><p class="li-name">empiria GmbH</p><p class="li-rolle">Strategie, die wirkt.</p>'
            f'<p class="li-ort">Crailsheim, Baden-Württemberg</p>'
            f'<div class="li-knoepfe"><span>+ Folgen</span><span>Website ansehen</span></div></div></div></div>')


# ----- Mit Kundenlogos -----
# Alle Kundenlogos in der Reihenfolge der Website (site/script.js)
KUNDEN = [("logo-01-sv.svg", "SV SparkassenVersicherung"), ("logo-02-vgh.svg", "VGH"), ("logo-03-devk-re.svg", "DEVK RE"),
          ("logo-04-vh.svg", "Vereinigte Hagelversicherung"), ("logo-05-svs.svg", "SV SparkassenVersicherung Sachsen"),
          ("logo-msk.svg", "Meyerthole Siems Kohlruss"), ("logo-voev.jpg", "Verband öffentlicher Versicherer"),
          ("logo-06-gartenbau.svg", "Gartenbau-Versicherung"), ("logo-07-sv-bav.svg", "SV bAV Consulting"),
          ("logo-08-devk-am.svg", "DEVK AM"), ("logo-09-oerag.svg", "ÖRAG Rechtsschutz"), ("logo-10-svp.svg", "SV Pensionsfonds"),
          ("logo-11-cominia.svg", "cominia"), ("logo-12-zeitsprung.svg", "zeitsprung")]
# Logos einfarbig: Schwellwert (Weiß bleibt weiß, alles andere wird schwarz), dann per Mischmodus auf die Fläche gelegt –
# auf Gelb verschwindet das Weiß (multiply), auf Schwarz wird invertiert und das Schwarz verschwindet (screen).
# Die Logos stehen immer in ihren Originalfarben (Vorgabe der Unternehmen) – deshalb nur auf Weiß.
# Optischer Ausgleich je Logo (Faktor auf die Grundhöhe) – die Dateien haben unterschiedlich viel Weißraum und Gewicht
LOGO_SKALA = {"logo-01-sv.svg": 1.0, "logo-02-vgh.svg": .78, "logo-03-devk-re.svg": .82, "logo-04-vh.svg": .9,
              "logo-05-svs.svg": 1.05, "logo-msk.svg": 1.75, "logo-voev.jpg": 1.0, "logo-06-gartenbau.svg": .95,
              "logo-07-sv-bav.svg": 1.45, "logo-08-devk-am.svg": .82, "logo-09-oerag.svg": 1.1, "logo-10-svp.svg": 1.45,
              "logo-11-cominia.svg": .72, "logo-12-zeitsprung.svg": 1.0}
LOGO_CSS = """
.lb-logos { display: grid; grid-template-columns: repeat(7, 1fr); align-items: center; justify-items: center; }
.lb-logos img { display: block; width: auto; object-fit: contain; }
.lb-logos img:nth-child(7n+1) { justify-self: start; }
.lb-logos img:nth-child(7n) { justify-self: end; }
"""


def logo_raster(p, hoehe, zeile, gap_y):
    return "".join(f'<img src="/assets/logos/{d}" alt="{n}" style="height:{p(hoehe * LOGO_SKALA[d])};max-width:86%">'
                   for d, n in KUNDEN), f"grid-auto-rows:{p(zeile)};row-gap:{p(gap_y)}"


WAND_H2 = 'Wir arbeiten unter anderem für diese <span class="hl">Unternehmen.</span>'


def person_logos(art):
    """Personenbanner mit Logos (ab x 470, rechts 84). start: Claim + Doppelpfeil + Logoleiste; wand: Website-Überschrift + große Logos."""
    W = 1584
    p = px_fn(W)
    H = 396
    if art == "start":  # rechts läuft ein großer schwarzer Doppelpfeil aus dem Bild – die Logos bleiben auf Weiß
        b = .8 * H / PFEIL_VERH
        logos, raster = logo_raster(p, 30, 56, 16)
        return (pfeil(p, b, W - .3 * b, H / 2, SCHWARZ)
                + f'<div style="left:{p(470)};top:{p(40)}">{kicker_html(p, "Strategiehandwerker", 18, 14, 36, 3.5, "margin:0 0 " + p(12) + ";")}'
                f'{claim(p, 70)}</div>'
                + f'<div class="lb-logos" style="left:{p(470)};right:{p(W - (W - .3 * b - b / 2) + 60)};top:{p(222)};{raster}">{logos}</div>')
    # unten: Logoleiste oben, Claim groß darunter
    logos, raster = logo_raster(p, 28, 50, 12)
    return (f'<div class="lb-logos" style="left:{p(470)};right:{p(84)};top:{p(36)};{raster}">{logos}</div>'
            f'<div style="left:{p(470)};bottom:{p(40)}">{claim(p, 76)}</div>'
            + pfeil(p, 150, W - 84 - 75, H - 40 - 76 * .65, SCHWARZ))


def firma_logos(art):
    """Firmenbanner mit Logos (ab x 250, rechts 56)."""
    W = 1128
    p = px_fn(W)
    if art == "start":
        H = 191
        b = .8 * H / PFEIL_VERH
        links_pfeil = W - .3 * b - b / 2
        logos, raster = logo_raster(p, 18, 34, 8)
        return (pfeil(p, b, W - .3 * b, H / 2, SCHWARZ)
                + f'<h2 style="left:{p(250)};top:{p(16)};font-size:{p(38)}">Strategie, die <span class="hl">wirkt.</span></h2>'
                + f'<div class="lb-logos" style="left:{p(250)};right:{p(W - links_pfeil + 36)};top:{p(92)};{raster}">{logos}</div>')
    H = 191
    logos, raster = logo_raster(p, 16, 30, 6)
    return (f'<div class="lb-logos" style="left:{p(250)};right:{p(56)};top:{p(16)};{raster}">{logos}</div>'
            f'<div style="left:{p(250)};bottom:{p(18)}">{claim(p, 40)}</div>'
            + pfeil(p, 70, W - 56 - 35, H - 18 - 40 * .65, SCHWARZ))


def schutzzone():
    """Zeigt, wo Profilfoto bzw. Firmenlogo über dem Banner liegen."""
    def zone(w, h, kreis, text, label):
        l, t, d, rund = kreis
        return (f'<figure style="margin:0"><div class="lz" style="aspect-ratio:{w}/{h};background:#f3f1ee;border-radius:6px;box-shadow:0 0 0 1px #e4e0db;overflow:hidden">'
                f'<span class="lz-foto" style="left:{l / w * 100}%;top:{t / h * 100}%;width:{d / w * 100}%;aspect-ratio:1;{"" if rund else "border-radius:10%"}"></span>'
                f'<span class="lz-text" style="left:{(l + d + 24) / w * 100}%;bottom:12%">{text}</span></div>'
                f'<p class="pm-label">{label}</p></figure>')
    return (f'<div class="lg-raster lg-raster--2">'
            + zone(1584, 396, (47, 175, 300, True), "Profilfoto – hier nichts Wichtiges", "Personenprofil · 1584 × 396 px · Schutzzone")
            + zone(1128, 191, (30, 110, 136, False), "Firmenlogo", "Firmenprofil · 1128 × 191 px · Schutzzone")
            + '</div>')


def jobs():
    j = []
    for var in VARIANTEN:
        j.append({"html": person_banner(var), "w": 1584, "h": 396, "pfad": ORDNER / f"linkedin-person-{var}.png"})
        j.append({"html": firma_banner(var), "w": 1128, "h": 191, "pfad": ORDNER / f"linkedin-firma-{var}.png"})
    return j


def main_html():
    teile = ['<div class="pm-abschnitt"><h2>Wo Foto und Logo liegen</h2>'
             '<p class="pm-text">LinkedIn legt das Profilfoto bzw. das Firmenlogo links unten über das Banner – dort steht deshalb nichts Wichtiges.</p>'
             + schutzzone() + '</div>']
    for i, (var, (name, text)) in enumerate(VARIANTEN.items(), 1):
        teile.append(f'<div class="pm-abschnitt"><h2>{i} · {name}</h2><p class="pm-text">{text}</p>'
                     f'<div class="lg-raster lg-raster--li">'
                     f'<figure style="margin:0">{attrappe_person(var)}<p class="pm-label">Personenprofil · 1584 × 396 px</p>'
                     f'<div class="pm-dl">{download(f"{WEB}/linkedin-person-{var}.png", "PNG laden")}</div></figure>'
                     f'<figure style="margin:0">{attrappe_firma(var)}<p class="pm-label">Unternehmensseite · 1128 × 191 px</p>'
                     f'<div class="pm-dl">{download(f"{WEB}/linkedin-firma-{var}.png", "PNG laden")}</div></figure>'
                     f'</div></div>')
    return (f'<main>\n<section class="pm"><div class="container">'
            + kopf('LinkedIn-<span class="hl">Banner</span>',
                   'Drei Varianten, jeweils für Dein Profil und die Unternehmensseite – gezeigt in der LinkedIn-Ansicht. '
                   'Erst wenn die Gestaltung steht, folgen Kerstin und Noah.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{LOGO_CSS}{SEITE_EXTRA}</style>\n</main>')


if __name__ == "__main__":
    seite("ga-linkedin.html", "LinkedIn-Banner", main_html())
    if "--ohne-png" not in sys.argv:
        exportieren(CSS + LOGO_CSS, jobs())
