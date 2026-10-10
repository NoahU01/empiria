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

# Variante: Name, Hintergrund, Schrift, Pfeil, Highlight-Fläche, Highlight-Schrift, Logo hell?, Beschreibung
VARIANTEN = {
    "weiss": ("Weiß", WEISS, SCHWARZ, SCHWARZ, GELB, SCHWARZ, False,
              "Ruhig wie die Website: weiße Fläche, Claim mit gelbem Highlight, schwarzer Doppelpfeil rechts."),
    "gelb": ("Gelb", GELB, SCHWARZ, SCHWARZ, SCHWARZ, GELB, False,
             "Maximal auffällig im Feed: Vollfläche Gelb, alles darauf schwarz – das Highlight wird zum schwarzen Kasten."),
    "schwarz": ("Schwarz", SCHWARZ, WEISS, GELB, GELB, SCHWARZ, True,
                "Edel und kontrastreich: schwarze Fläche, weiße Schrift, Gelb nur als Akzent (Highlight und Doppelpfeil)."),
    "formen": ("Formen", GRAU, SCHWARZ, SCHWARZ, GELB, SCHWARZ, False,
               "Spielerischer: graue Fläche, rechts ein Raster aus den Markenformen, eine Kachel gelb."),
}

FORMEN_P = ["forward", "kreis", "kreuz", "quadrat", "stern", "raute", "blase", "blitz"]

CSS = """
.lb { position: relative; width: 100%; container-type: inline-size; overflow: hidden; background: var(--bg); color: var(--fg); font-family: 'Poppins', sans-serif; }
.lb > * { position: absolute; }
.lb-text { top: 50%; transform: translateY(-50%); }
.lb-kicker { display: flex; align-items: center; margin: 0; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; line-height: 1; }
.lb-kicker::before { content: ""; background: currentColor; flex: 0 0 auto; }
.lb h2 { margin: 0; font-family: 'Lora', Georgia, serif; font-weight: 700; letter-spacing: -.02em; line-height: 1.2; color: var(--fg); white-space: nowrap; }
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
.li-banner { position: relative; }
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
@media (max-width: 800px) { .lg-raster { grid-template-columns: 1fr; } }
"""


def person_banner(var, wer):
    """Personenbanner 1584 × 396. Profilfoto deckt ca. x 45–350, y 175–396 ab → Inhalt beginnt bei x 470."""
    _, bg, fg, pf, hlbg, hlfg, hell, _ = VARIANTEN[var]
    W, H = 1584, 396
    p = px_fn(W)
    kicker = PERSONEN[wer][2]
    logo = f'/assets/empiria-logo{"-weiss" if hell else ""}.svg'
    text = (f'<div class="lb-text" style="left:{p(470)}">'
            f'<p class="lb-kicker" style="font-size:{p(15)};gap:{p(14)};margin-bottom:{p(24)}">{kicker}</p>'
            f'<h2 style="font-size:{p(86)}">Strategie,<br>die <span class="hl">wirkt.</span></h2>'
            f'<p class="lb-fuss" style="margin-top:{p(30)};gap:{p(16)};font-size:{p(16)}"><img src="{logo}" alt="empiria" style="height:{p(30)}">www.empiria.de</p>'
            f'</div>')
    if var == "formen":
        zelle, gap = 104, 16
        breite = 4 * zelle + 3 * gap
        hoehe = 2 * zelle + gap
        kacheln = "".join(
            f'<span class="{"gelb" if n == "forward" else ""}" style="border-radius:{p(18)}"><i style="display:block;width:{p(54 if n == "forward" else 50)}">{form(n, SCHWARZ)}</i></span>'
            for n in FORMEN_P)
        rechts = (f'<div class="lb-raster" style="right:{p(90)};top:{p((H - hoehe) / 2)};width:{p(breite)};'
                  f'grid-template-columns:repeat(4,1fr);gap:{p(gap)};grid-auto-rows:{p(zelle)}">{kacheln}</div>')
    else:
        pb = 280
        rechts = f'<div style="right:{p(110)};top:{p((H - pb * PFEIL_VERH) / 2)};width:{p(pb)}">{form("forward", pf)}</div>'
    kstrich = f'<style>.lb-k-{var}-{wer} .lb-kicker::before{{width:{p(30)};height:{p(3)}}}</style>'
    return (f'{kstrich}<div class="lb lb-k-{var}-{wer}" style="aspect-ratio:{W}/{H};--bg:{bg};--fg:{fg};--hlbg:{hlbg};--hlfg:{hlfg}">'
            f'{text}{rechts}</div>')


def firma_banner(var):
    """Firmenbanner 1128 × 191. Firmenlogo deckt ca. x 30–165, y 110–191 ab → Inhalt beginnt bei x 250."""
    _, bg, fg, pf, hlbg, hlfg, hell, _ = VARIANTEN[var]
    W, H = 1128, 191
    p = px_fn(W)
    text = (f'<div class="lb-text" style="left:{p(250)}">'
            f'<p class="lb-kicker" style="font-size:{p(12)};gap:{p(11)};margin-bottom:{p(16)}">Strategiehandwerk · Crailsheim</p>'
            f'<h2 style="font-size:{p(52 if var != "formen" else 46)}">Strategie, die <span class="hl">wirkt.</span></h2>'
            f'</div>')
    if var == "formen":
        zelle, gap = 76, 12
        breite = 3 * zelle + 2 * gap
        kacheln = "".join(
            f'<span class="{"gelb" if n == "forward" else ""}" style="border-radius:{p(14)}"><i style="display:block;width:{p(40 if n == "forward" else 36)}">{form(n, SCHWARZ)}</i></span>'
            for n in ["kreis", "forward", "stern"])
        rechts = (f'<div class="lb-raster" style="right:{p(64)};top:{p((H - zelle) / 2)};width:{p(breite)};'
                  f'grid-template-columns:repeat(3,1fr);gap:{p(gap)};grid-auto-rows:{p(zelle)}">{kacheln}</div>')
    else:
        pb = 136
        rechts = f'<div style="right:{p(72)};top:{p((H - pb * PFEIL_VERH) / 2)};width:{p(pb)}">{form("forward", pf)}</div>'
    kstrich = f'<style>.lb-f-{var} .lb-kicker::before{{width:{p(24)};height:{p(2.4)}}}</style>'
    return (f'{kstrich}<div class="lb lb-f-{var}" style="aspect-ratio:{W}/{H};--bg:{bg};--fg:{fg};--hlbg:{hlbg};--hlfg:{hlfg}">'
            f'{text}{rechts}</div>')


def attrappe_person(var, wer):
    name, rolle, _ = PERSONEN[wer]
    return (f'<div class="li"><div class="li-banner">{person_banner(var, wer)}'
            f'<span class="li-foto" style="background-image:url(/assets/ansprechpartner-{wer}.webp)"></span></div>'
            f'<div class="li-info"><div><p class="li-name">{name}</p><p class="li-rolle">{rolle} · empiria GmbH</p>'
            f'<p class="li-ort">Crailsheim, Baden-Württemberg</p>'
            f'<div class="li-knoepfe"><span>Vernetzen</span><span>Nachricht</span></div></div>'
            f'<div class="li-firma"><i><img src="/assets/empiria-logo.svg" alt=""></i>empiria GmbH</div></div></div>')


def attrappe_firma(var):
    return (f'<div class="li"><div class="li-banner">{firma_banner(var)}'
            f'<span class="li-logo"><img src="/assets/empiria-logo.svg" alt="empiria"></span></div>'
            f'<div class="li-info li-info--firma"><div><p class="li-name">empiria GmbH</p><p class="li-rolle">Strategie, die wirkt.</p>'
            f'<p class="li-ort">Crailsheim, Baden-Württemberg</p>'
            f'<div class="li-knoepfe"><span>+ Folgen</span><span>Website ansehen</span></div></div></div></div>')


def schutzzone():
    """Zeigt, wo Profilfoto bzw. Firmenlogo über dem Banner liegen."""
    def zone(w, h, kreis, text, label):
        l, t, d, rund = kreis
        return (f'<figure style="margin:0"><div class="lz" style="aspect-ratio:{w}/{h};background:#f3f1ee;border-radius:6px;box-shadow:0 0 0 1px #e4e0db;overflow:hidden">'
                f'<span class="lz-foto" style="left:{l / w * 100}%;top:{t / h * 100}%;width:{d / w * 100}%;aspect-ratio:1;{"" if rund else "border-radius:10%"}"></span>'
                f'<span class="lz-text" style="left:{(l + d + 24) / w * 100}%;bottom:12%">{text}</span></div>'
                f'<p class="pm-label">{label}</p></figure>')
    return (f'<div class="lg-raster" style="grid-template-columns:repeat(2,minmax(0,1fr))">'
            + zone(1584, 396, (47, 175, 300, True), "Profilfoto – hier nichts Wichtiges", "Personenprofil · 1584 × 396 px · Schutzzone")
            + zone(1128, 191, (30, 110, 136, False), "Firmenlogo", "Firmenprofil · 1128 × 191 px · Schutzzone")
            + '</div>')


def jobs():
    j = []
    for var in VARIANTEN:
        for wer in PERSONEN:
            j.append({"html": person_banner(var, wer), "w": 1584, "h": 396, "pfad": ORDNER / f"linkedin-person-{var}-{wer}.png"})
        j.append({"html": firma_banner(var), "w": 1128, "h": 191, "pfad": ORDNER / f"linkedin-firma-{var}.png"})
    return j


def main_html():
    teile = []
    # Personenprofil
    teile.append('<div class="pm-abschnitt"><h2>1 · Personenprofil</h2>'
                 '<p class="pm-text">Banner 1584 × 396 px. Links unten liegt das runde Profilfoto über dem Banner – deshalb beginnt der Inhalt erst rechts davon. '
                 'Oben im Kicker steht das Fachgebiet der Person; Name und Rolle zeigt LinkedIn ohnehin darunter (Kicker lässt sich auch weglassen).</p>'
                 + schutzzone())
    for i, (var, v) in enumerate(VARIANTEN.items()):
        buchst = "ABCD"[i]
        teile.append(f'<h3>Variante {buchst} · {v[0]}</h3><p class="pm-text">{v[7]}</p>'
                     f'<div class="lg-gross">{attrappe_person(var, "daniel")}<p class="pm-label">Attrappe Personenprofil · Daniel Ströbel</p></div>'
                     '<div class="lg-raster">'
                     + "".join(f'<figure style="margin:0">{person_banner(var, wer)}<p class="pm-label">{PERSONEN[wer][0]} · 1584 × 396 px</p>'
                               f'<div class="pm-dl">{download(f"{WEB}/linkedin-person-{var}-{wer}.png", "PNG laden")}</div></figure>'
                               for wer in PERSONEN)
                     + '</div>')
    teile.append('</div>')
    # Firmenprofil
    teile.append('<div class="pm-abschnitt"><h2>2 · Firmenprofil</h2>'
                 '<p class="pm-text">Banner 1128 × 191 px mit dem Claim „Strategie, die wirkt.“ – sehr flach, deshalb einzeilig. Links unten liegt das Firmenlogo.</p>')
    for i, (var, v) in enumerate(VARIANTEN.items()):
        buchst = "ABCD"[i]
        teile.append(f'<h3>Variante {buchst} · {v[0]}</h3>'
                     f'<div class="lg-gross">{attrappe_firma(var)}<p class="pm-label">Attrappe Unternehmensseite</p></div>'
                     f'<div class="lg-gross">{firma_banner(var)}<p class="pm-label">Firmenbanner {v[0]} · 1128 × 191 px</p>'
                     f'<div class="pm-dl">{download(f"{WEB}/linkedin-firma-{var}.png", "PNG laden")}</div></div>')
    teile.append('</div>')

    return (f'<main>\n<section class="pm"><div class="container">'
            + kopf('LinkedIn-<span class="hl">Banner</span>',
                   'Vier Varianten für die Personenprofile von Daniel, Kerstin und Noah und für die Unternehmensseite – '
                   'jeweils in der LinkedIn-Attrappe, damit man sieht, wie Foto und Logo über dem Banner liegen. Alle Banner gibt es als PNG in Originalgröße.')
            + "".join(teile)
            + f'</div></section>\n<style>{SEITE_CSS}{CSS}{SEITE_EXTRA}</style>\n</main>')


if __name__ == "__main__":
    seite("ga-linkedin.html", "LinkedIn-Banner", main_html())
    if "--ohne-png" not in sys.argv:
        exportieren(CSS, jobs())
