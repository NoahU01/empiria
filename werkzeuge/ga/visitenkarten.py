#!/usr/bin/env python3
"""Visitenkarten 85 × 55 mm – Entwürfe (Daniel, 10.10.2026).

Drei Varianten, je Vorder- und Rückseite, für Daniel, Kerstin und Noah:
  A · Weiß   – klassische Vorderseite, Rückseite weiß mit Claim und Doppelpfeil
  B · Schwarz – Name oben, Logo unten rechts; Rückseite schwarz mit gelbem, angeschnittenem Doppelpfeil
  C · Gelb   – Vorderseite mit Porträt; Rückseite gelb mit Doppelpfeil und Logo
PNG-Export (Daniel, 300 dpi = 1004 × 650 px) nach site/projekte/ga/visitenkarten/.

Aufruf: python3 werkzeuge/ga/visitenkarten.py [--ohne-png]
"""
import sys

from ga_basis import (GELB, PERSONEN, SCHWARZ, FIRMA, abschnitt, download, figur, ico, logo, masse, ph, png_export,
                      raster, seite_schreiben, zeichen)

DATEI = "ga-visitenkarten.html"
B, H = 85, 55
PX = (1004, 650)  # 300 dpi


def kontakt(p, mit_adresse=True):
    z = [(ico("phone"), ph(p["tel"], p["ph"])), (ico("mail"), ph(p["mail"], p["ph"])), (ico("globe"), FIRMA["web"])]
    if not mit_adresse:
        z.append((ico("map-pin"), f'{FIRMA["strasse"]} · {FIRMA["ort"]}'))
    links = "".join(f'<p>{i}<span>{t}</span></p>' for i, t in z)
    rechts = f'<p>{FIRMA["name"]}</p><p>{FIRMA["strasse"]}</p><p>{FIRMA["ort"]}</p>' if mit_adresse else ""
    return f'<div class="vk-kontakt"><div>{links}</div><div class="vk-adr">{rechts}</div></div>'


def rolle(p):
    return p["rolle"] + (f' · {p["rolle2"]}' if p["rolle2"] else "")


def karte(inhalt, bg, fg, cls="", png=None):
    attr = f' data-png="ga/visitenkarten/{png}.png" data-pw="{PX[0]}"' if png else ""
    return f'<div class="vk ga-blatt {cls}" style="--bg:{bg};--fg:{fg}"{attr}><div class="vk-in">{inhalt}</div></div>'


# ---------- Vorderseiten ----------
def vorne_a(p, png=None):
    return karte(logo(cls="vk-logo") +
                 f'<div class="vk-person"><p class="vk-name">{p["name"]}</p><p class="vk-rolle">{rolle(p)}</p></div>' +
                 kontakt(p), "#fff", SCHWARZ, "vk--a", png)


def vorne_b(p, png=None):
    return karte(f'<div class="vk-person vk-person--oben"><p class="vk-rolle">{rolle(p)}</p><p class="vk-name">{p["name"]}</p></div>' +
                 kontakt(p, False) + logo(cls="vk-logo vk-logo--unten"), "#fff", SCHWARZ, "vk--b", png)


def vorne_c(p, key, png=None):
    return karte(logo(cls="vk-logo") +
                 f'<img class="vk-foto" src="/assets/ansprechpartner-{key}.webp" alt="">'
                 f'<div class="vk-person"><p class="vk-name">{p["name"]}</p><p class="vk-rolle">{rolle(p)}</p></div>' +
                 kontakt(p), "#fff", SCHWARZ, "vk--c", png)


# ---------- Rückseiten ----------
def hinten_a(png=None):
    return karte(f'<p class="vk-claim">Strategie,<br>die <span class="vk-hl">wirkt.</span></p>'
                 f'<span class="vk-pfeil-a">{zeichen("forward", SCHWARZ)}</span>', "#fff", SCHWARZ, "vk--ra", png)


def hinten_b(png=None):
    return karte(f'<span class="vk-pfeil-b">{zeichen("forward", GELB)}</span>' + logo(True, "vk-logo vk-logo--b") +
                 f'<p class="vk-claim-klein">Strategie, die wirkt.</p>', SCHWARZ, "#fff", "vk--rb", png)


def hinten_c(png=None):
    return karte(f'<span class="vk-pfeil-c">{zeichen("forward", SCHWARZ)}</span>' + logo(cls="vk-logo vk-logo--c"),
                 GELB, SCHWARZ, "vk--rc", png)


# ---------- Vorderseiten · Entwurf 2: nur Text, keine Icons, kein Foto ----------
def kontakt_text(p):
    return (f'<div class="vk2-kontakt"><p>{ph(p["mail"], p["ph"])}</p><p>{ph(p["tel"], p["ph"])}</p>'
            f'<p>{FIRMA["web"]}</p></div>')


def name_zwei(p, hl=True):
    vor, nach = p["name"].split(" ", 1)
    return f'<p class="vk2-name">{vor}<br>{f"<span class=vk-hl>{nach}</span>" if hl else nach}</p>'


def kicker(p):
    return f'<p class="vk2-kicker">{p["rolle2"] or p["rolle"]}</p>'


def v_highlight(p, png=None):
    return karte(kicker(p) + name_zwei(p) + kontakt_text(p), "#fff", SCHWARZ, "vk2 vk2--hl", png)


def v_gelb(p, png=None):
    return karte(kicker(p) + name_zwei(p, False) + kontakt_text(p) + f'<span class="vk2-pfeil">{zeichen("forward", SCHWARZ)}</span>',
                 GELB, SCHWARZ, "vk2 vk2--gelb", png)


def v_schwarz(p, png=None):
    return karte(kicker(p) + name_zwei(p) + kontakt_text(p), SCHWARZ, "#fff", "vk2 vk2--schwarz", png)



def v_logo(p, png=None):
    return karte(logo(cls="vk2-logo") + f'<div class="vk2-unten"><div><p class="vk2-name vk2-name--eins">{p["name"]}</p>{kicker(p)}</div>'
                 f'{kontakt_text(p)}</div>', "#fff", SCHWARZ, "vk2 vk2--logo", png)


FRONTEN = [
    ("highlight", "1 · Highlight", "Der Name steht wie die Überschrift der Homepage: groß, zweizeilig, der Nachname im gelben Highlight. Kein Logo – das steht hinten.",
     v_highlight, hinten_b, "Rückseite Schwarz"),
    ("gelb", "2 · Gelb mit Anschnitt", "Vollfläche Gelb, rechts läuft der Doppelpfeil groß aus der Karte. Name und Kontakt links, alles schwarz.",
     v_gelb, hinten_a, "Rückseite Weiß"),
    ("schwarz", "3 · Schwarz", "Schwarze Karte, weißer Name, der Nachname im gelben Highlight. Kräftig und edel – dazu die gelbe Rückseite.",
     v_schwarz, hinten_c, "Rückseite Gelb"),
    ("logo", "4 · Ruhig mit Logo", "Die zurückhaltende Variante: Logo oben, unten Name und Funktion links, Kontakt rechts. Für alle, die das Logo vorne möchten.",
     v_logo, hinten_b, "Rückseite Schwarz"),
]


# ---------- Hochformat 55 × 85 mm ----------
PX_HOCH = (650, 1004)


def karte_hoch(inhalt, bg, fg, cls="", png=None):
    attr = f' data-png="ga/visitenkarten/{png}.png" data-pw="{PX_HOCH[0]}"' if png else ""
    return f'<div class="vkh ga-blatt {cls}" style="--bg:{bg};--fg:{fg}"{attr}><div class="vk-in">{inhalt}</div></div>'


def h_highlight(p, png=None):
    return karte_hoch(kicker(p) + name_zwei(p) + kontakt_text(p), "#fff", SCHWARZ, "vkh--hl", png)


def h_gelb(p, png=None):
    return karte_hoch(f'<span class="vkh-pfeil">{zeichen("forward", SCHWARZ)}</span>' + kicker(p) + name_zwei(p, False) + kontakt_text(p),
                      GELB, SCHWARZ, "vkh--gelb", png)


def h_schwarz(p, png=None):
    return karte_hoch(kicker(p) + name_zwei(p) + kontakt_text(p), SCHWARZ, "#fff", "vkh--schwarz", png)



def hh_schwarz(png=None):
    return karte_hoch(f'<span class="vkh-pfeil-r">{zeichen("forward", GELB)}</span>' + logo(True, "vkh-logo"), SCHWARZ, "#fff", "vkh--rs", png)


def hh_gelb(png=None):
    return karte_hoch(f'<span class="vkh-pfeil-m">{zeichen("forward", SCHWARZ)}</span>' + logo(cls="vkh-logo vkh-logo--m"), GELB, SCHWARZ, "vkh--rg", png)


FRONTEN_HOCH = [
    ("highlight", "Highlight", h_highlight, hh_schwarz), ("gelb", "Gelb mit Anschnitt", h_gelb, hh_schwarz),
    ("schwarz", "Schwarz", h_schwarz, hh_gelb),
]

CSS_HOCH = masse("""
.vkh { position: relative; aspect-ratio: 55 / 85; container-type: inline-size; background: var(--bg); color: var(--fg); overflow: hidden;
  border-radius: 6px; font-family: 'Poppins', sans-serif; }
.vkh * { box-sizing: border-box; }
.vkh p { margin: 0; }
.vkh .vk-in { position: absolute; inset: 0; }
.vkh .vk2-kicker { position: absolute; left: [6]; top: [7]; display: flex; align-items: center; gap: [1.6]; font: 600 [5.2pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.vkh .vk2-kicker::before { content: ""; width: [3.6]; height: [0.35]; background: currentColor; }
.vkh .vk2-name { position: absolute; left: [6]; top: [11.5]; margin: 0; font: 700 [20pt]/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; }
.vkh .vk2-name .vk-hl { color: #1a1817; }
.vkh .vk2-kontakt { position: absolute; left: [6]; bottom: [6.5]; font: 400 [6.3pt]/1.6 'Poppins', sans-serif; }
.vkh--schwarz .vk2-kicker { color: #fff400; }
.vkh--schwarz .vk2-kontakt { color: rgba(255,255,255,.85); }
.vkh--gelb .vk2-kicker { top: [37.5]; }
.vkh--gelb .vk2-name { top: [42]; }
.vkh-pfeil { position: absolute; right: [-10]; top: [6.5]; width: [36]; }
.vkh-pfeil svg, .vkh-pfeil-r svg, .vkh-pfeil-m svg { display: block; width: 100%; height: auto; }
.vkh-pfeil-r { position: absolute; left: [6]; bottom: [-10]; width: [62]; }
.vkh-logo { position: absolute; left: [5]; top: [7]; height: [5.2]; width: auto; display: block; }
.vkh-pfeil-m { position: absolute; left: 50%; top: [30]; transform: translateX(-50%); width: [26]; }
.vkh-logo--m { top: auto; bottom: [12]; left: 50%; transform: translateX(-50%); height: [5.6]; }
.ga-raster--vkh { grid-template-columns: repeat(4, minmax(0, 1fr)) !important; }
@media (max-width: 800px) { .ga-raster--vkh { grid-template-columns: repeat(2, minmax(0, 1fr)) !important; } }
""", 55)


VARIANTEN = [
    ("a", "Variante A · Weiß", "Ruhig und klassisch. Vorderseite: Logo oben, Name und Rolle in der Mitte, Kontakt unten in zwei Spalten. "
     "Rückseite weiß mit dem Claim und dem gelben Highlight – wie die Startseite der Website.", vorne_a, hinten_a),
    ("b", "Variante B · Schwarz", "Name und Rolle stehen oben, das Logo wandert nach unten rechts. Rückseite schwarz, der gelbe Doppelpfeil "
     "läuft groß aus dem Anschnitt – die stärkste Signalwirkung, wenn die Karte auf dem Tisch liegt.", vorne_b, hinten_b),
    ("c", "Variante C · Gelb mit Porträt", "Vorderseite mit rundem Porträt – persönlich, gut für Netzwerk-Termine. Rückseite gelb, "
     "nur Doppelpfeil und Logo. Braucht für jede Person ein Porträt in Druckqualität.", vorne_c, hinten_c),
]


def vorne(fn, p, key, png=None):
    return fn(p, key, png) if fn is vorne_c else fn(p, png)


def inhalt():
    d = PERSONEN["daniel"]
    dl = lambda n: download(f"ga/visitenkarten/{n}.png", f"PNG · {PX[0]} × {PX[1]} px")
    teile = []
    for kurz, titel, text, fv, fh, hinten_name in FRONTEN:
        f1 = figur(fv(d, f"vorne-{kurz}"), "<b>Vorderseite</b> · 85 × 55 mm", dl(f"vorne-{kurz}"))
        f2 = figur(fh(), f"<b>{hinten_name}</b> · Vorschlag")
        teile.append(abschnitt(titel, text, raster([f1, f2])))
    rueck = raster([figur(fh(f"{k}-rueckseite"), f"<b>{t}</b>", dl(f"{k}-rueckseite"))
                    for k, t, fh in (("a", "Rückseite Weiß · Claim", hinten_a), ("b", "Rückseite Schwarz · Anschnitt", hinten_b),
                                     ("c", "Rückseite Gelb · Doppelpfeil und Logo", hinten_c))], 3, 1)
    hoch = []
    for kurz, titel, fv, fh in FRONTEN_HOCH:
        hoch.append(figur(fv(d, f"hoch-vorne-{kurz}"), f"<b>{titel}</b> · Vorderseite", dl(f"hoch-vorne-{kurz}").replace(f"{PX[0]} × {PX[1]}", f"{PX_HOCH[0]} × {PX_HOCH[1]}")))
    hoch_r = [figur(hh_schwarz("hoch-hinten-schwarz"), "<b>Rückseite Schwarz</b>", dl("hoch-hinten-schwarz").replace(f"{PX[0]} × {PX[1]}", f"{PX_HOCH[0]} × {PX_HOCH[1]}")),
              figur(hh_gelb("hoch-hinten-gelb"), "<b>Rückseite Gelb</b>", dl("hoch-hinten-gelb").replace(f"{PX[0]} × {PX[1]}", f"{PX_HOCH[0]} × {PX_HOCH[1]}"))]
    teile.append(abschnitt("Hochformat · 55 × 85 mm", "Dieselben Ideen hochkant: Name groß oben, Kontakt unten. Beim Gelb läuft der Doppelpfeil oben rechts "
                           "aus der Karte.",
                           f'<div class="ga-raster ga-raster--vkh">{"".join(hoch)}</div>'
                           f'<p class="ga-unter">Rückseiten hoch</p><div class="ga-raster ga-raster--vkh">{"".join(hoch_r)}</div>'))
    teile.append(abschnitt("Rückseiten", "Unverändert aus Entwurf 1 – jede Vorderseite lässt sich mit jeder Rückseite kombinieren.", rueck))
    alt = raster([figur(vorne(fv, d, "daniel"), f"<b>{titel}</b> · Entwurf 1") for _, titel, _, fv, _ in VARIANTEN], 3, 1)
    teile.append(abschnitt("Archiv · Vorderseiten Entwurf 1", "Zum Vergleich – mit Icons und Foto, wird nicht weiterverfolgt.", alt))
    return "".join(teile)


CSS = masse("""
.vk { position: relative; aspect-ratio: 85 / 55; container-type: inline-size; background: var(--bg); color: var(--fg); overflow: hidden;
  border-radius: 6px; font-family: 'Poppins', sans-serif; }
.vk * { box-sizing: border-box; }
.vk p { margin: 0; }
.vk-in { position: absolute; inset: 0; padding: [6] [6.5]; }
.vk-logo { position: absolute; left: [5.2]; top: [5.4]; height: [5.6]; width: auto; display: block; }
.vk-person { position: absolute; left: [6.5]; top: [19.5]; right: [6.5]; }
.vk-name { font: 700 [11pt]/1.15 'Lora', Georgia, serif; letter-spacing: -.01em; }
.vk-rolle { display: flex; align-items: center; gap: [1.6]; margin-top: [1.6] !important; font: 600 [5.5pt]/1.3 'Poppins', sans-serif;
  letter-spacing: .12em; text-transform: uppercase; }
.vk-rolle::before { content: ""; flex: 0 0 auto; width: [3.4]; height: [0.35]; background: currentColor; }
.vk-kontakt { position: absolute; left: [6.5]; right: [6.5]; bottom: [5.6]; display: flex; justify-content: space-between; gap: [3];
  font: 400 [6.5pt]/1.55 'Poppins', sans-serif; }
.vk-kontakt p { display: flex; align-items: center; gap: [1.4]; white-space: nowrap; }
.vk-kontakt svg { width: [2.3]; height: [2.3]; flex: 0 0 auto; }
.vk-adr { text-align: right; }
.vk-adr p { display: block; }
/* B */
.vk--b .vk-person--oben { top: [6]; }
.vk--b .vk-rolle { margin: 0 0 [1.8] !important; }
.vk--b .vk-name { font-size: [12.5pt]; }
.vk--b .vk-kontakt { right: auto; flex-direction: column; gap: 0; }
.vk--b .vk-adr { display: none; }
.vk-logo--unten { top: auto; left: auto; right: [5.2]; bottom: [5.3]; }
/* C */
.vk-foto { position: absolute; right: [6.5]; top: [6]; width: [15]; height: [15]; border-radius: 50%; object-fit: cover; background: #f3f1ee; }
.vk--c .vk-person { top: [21.5]; }
.vk--c .vk-person::before { content: ""; position: absolute; left: 0; top: [-3.4]; width: [3.4]; height: [1.1]; background: #fff400; border-radius: [0.3]; }
.vk--c .vk-rolle::before { display: none; }
/* Rückseiten */
.vk-hl { background: #fff400; padding: 0 .12em .07em; border-radius: .14em; }
.vk-claim { position: absolute; left: [6.5]; bottom: [6]; font: 700 [17pt]/1.3 'Lora', Georgia, serif; letter-spacing: -.02em; }
.vk-pfeil-a { position: absolute; right: [6.5]; top: [6.5]; width: [17]; }
.vk-pfeil-a svg, .vk-pfeil-b svg, .vk-pfeil-c svg { width: 100%; height: auto; display: block; }
.vk-pfeil-b { position: absolute; right: [-15]; top: 50%; transform: translateY(-50%); width: [58]; }
.vk-logo--b { top: auto; bottom: [5]; }
.vk-claim-klein { position: absolute; left: [6.5]; top: [6.5]; font: 600 [5.5pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }
.vk-pfeil-c { position: absolute; left: 50%; top: [12.5]; transform: translateX(-50%); width: [22]; }
.vk-logo--c { top: auto; bottom: [7]; left: 50%; transform: translateX(-50%); height: [6]; }
/* Entwurf 2 */
.vk2 .vk-in { padding: 0; }
.vk2-kicker { display: flex; align-items: center; gap: [1.6]; font: 600 [5.2pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; }
.vk2-kicker::before { content: ""; width: [3.6]; height: [0.35]; background: currentColor; }
.vk2-name { margin-top: [2.6] !important; font: 700 [19pt]/1.22 'Lora', Georgia, serif; letter-spacing: -.02em; }
.vk2-name .vk-hl { color: #1a1817; }
.vk2-kontakt { position: absolute; left: [6]; bottom: [5.6]; font: 400 [6.3pt]/1.6 'Poppins', sans-serif; }
.vk2--hl .vk2-kicker, .vk2--gelb .vk2-kicker, .vk2--schwarz .vk2-kicker { position: absolute; left: [6]; top: [6.4]; }
.vk2--hl .vk2-name, .vk2--gelb .vk2-name, .vk2--schwarz .vk2-name { position: absolute; left: [6]; top: [10.2]; }
.vk2--schwarz .vk2-kicker { color: #fff400; }
.vk2--schwarz .vk2-kontakt { color: rgba(255,255,255,.85); }
.vk2-pfeil { position: absolute; right: [-13]; top: 50%; transform: translateY(-50%); width: [48]; }
.vk2-pfeil svg { display: block; width: 100%; height: auto; }
.vk2-logo { position: absolute; left: [4.9]; top: [6]; height: [5.2]; width: auto; display: block; }
.vk2-unten { position: absolute; left: [6]; right: [6]; bottom: [5.6]; display: flex; justify-content: space-between; align-items: flex-end; }
.vk2--logo .vk2-kontakt { position: static; text-align: right; }
.vk2-name--eins { margin: 0 0 [1.8] !important; font-size: [11.5pt]; }
.vk2--logo .vk2-kicker { margin-bottom: [0.9] !important; }
.vk2--logo .vk2-kicker::before { display: none; }
/* Satzspiegel */
.vk--raster::after { content: ""; position: absolute; inset: [5]; border: 1px dashed #C51F5D; pointer-events: none; }
.vk-mass { align-self: center; }
.vk-mass p { display: grid; grid-template-columns: 7.5rem 1fr; gap: 1rem; margin: 0; padding: .7rem 0; border-bottom: 1px solid #e4e0db; font-size: .92rem; line-height: 1.45; }
.vk-mass b { font-weight: 600; }
""", B)


def bauen(mit_png=True):
    seite_schreiben(DATEI, "Visitenkarten",
                    'Visiten<span class="hl">karten</span>',
                    "Fünf Vorderseiten im Format 85 × 55 mm – nur Name, Funktion und Kontakt, ohne Icons und ohne Foto. "
                    "Neben jeder Vorderseite die vorgeschlagene Rückseite. Erst wenn die Gestaltung steht, folgen die weiteren Personen.",
                    ["Entwurf 2", "quer 85 × 55 mm", "hoch 55 × 85 mm", "nur Text vorne"],
                    inhalt(), CSS + CSS_HOCH)
    if mit_png:
        png_export(DATEI, "visitenkarten")


if __name__ == "__main__":
    bauen("--ohne-png" not in sys.argv)
