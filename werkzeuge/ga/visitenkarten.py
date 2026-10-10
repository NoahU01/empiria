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
    teile = []
    for kurz, titel, text, fv, fh in VARIANTEN:
        d = PERSONEN["daniel"]
        f1 = figur(vorne(fv, d, "daniel", f"{kurz}-vorderseite-daniel"), "<b>Vorderseite</b> · 85 × 55 mm · Daniel",
                   download(f"ga/visitenkarten/{kurz}-vorderseite-daniel.png", f"PNG · {PX[0]} × {PX[1]} px"))
        f2 = figur(fh(f"{kurz}-rueckseite"), "<b>Rückseite</b> · 85 × 55 mm · für alle gleich",
                   download(f"ga/visitenkarten/{kurz}-rueckseite.png", f"PNG · {PX[0]} × {PX[1]} px"))
        weitere = [figur(vorne(fv, PERSONEN[k], k), f"<b>Vorderseite</b> · {PERSONEN[k]['name']}") for k in ("kerstin", "noah")]
        teile.append(abschnitt(titel, text, raster([f1, f2]) + '<p class="ga-unter">Weitere Personen</p>' + raster(weitere)))

    # Aufbau
    d = PERSONEN["daniel"]
    aufbau = raster([
        figur(vorne_a(d).replace('class="vk ', 'class="vk vk--raster ', 1), "<b>Satzspiegel</b> · Sicherheitsabstand 5 mm (gestrichelt)"),
        '<div class="vk-mass">' + "".join(f'<p><b>{a}</b><span>{b}</span></p>' for a, b in [
            ("Endformat", "85 × 55 mm, quer"),
            ("Anschnitt", "+ 3 mm rundum für die Druckdaten (noch anzulegen)"),
            ("Abstand", "Text und Logo mindestens 5 mm vom Rand"),
            ("Name", "Lora Bold 11 pt"),
            ("Rolle", "Poppins SemiBold 5,5 pt, Großbuchstaben, gesperrt"),
            ("Kontakt", "Poppins Regular 6,5 pt"),
            ("Farben", "Weiß, Schwarz #1A1817, Gelb #FFF400"),
        ]) + '</div>'])
    teile.append(abschnitt("Aufbau &amp; Maße", "Gilt für alle drei Varianten. Die PNGs zeigen das Endformat ohne Anschnitt – zum Ansehen und Abstimmen, "
                           "nicht als Druckdaten.", aufbau))
    hinweis = (f'<p class="ga-hinweis">{ph("gestrichelt")}<span>= Platzhalter. E-Mail-Adressen und Telefonnummern von Kerstin und Noah '
               f'sind angenommen bzw. noch offen und müssen vor dem Druck bestätigt werden.</span></p>')
    return hinweis + "".join(teile)


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
.vk-claim { position: absolute; left: [6.5]; bottom: [6]; font: 700 [17pt]/1.18 'Lora', Georgia, serif; letter-spacing: -.02em; }
.vk-pfeil-a { position: absolute; right: [6.5]; top: [6.5]; width: [17]; }
.vk-pfeil-a svg, .vk-pfeil-b svg, .vk-pfeil-c svg { width: 100%; height: auto; display: block; }
.vk-pfeil-b { position: absolute; right: [-15]; top: 50%; transform: translateY(-50%); width: [58]; }
.vk-logo--b { top: auto; bottom: [5]; }
.vk-claim-klein { position: absolute; left: [6.5]; top: [6.5]; font: 600 [5.5pt]/1 'Poppins', sans-serif; letter-spacing: .14em; text-transform: uppercase; color: #fff400; }
.vk-pfeil-c { position: absolute; left: 50%; top: [12.5]; transform: translateX(-50%); width: [22]; }
.vk-logo--c { top: auto; bottom: [7]; left: 50%; transform: translateX(-50%); height: [6]; }
/* Satzspiegel */
.vk--raster::after { content: ""; position: absolute; inset: [5]; border: 1px dashed #C51F5D; pointer-events: none; }
.vk-mass { align-self: center; }
.vk-mass p { display: grid; grid-template-columns: 7.5rem 1fr; gap: 1rem; margin: 0; padding: .7rem 0; border-bottom: 1px solid #e4e0db; font-size: .92rem; line-height: 1.45; }
.vk-mass b { font-weight: 600; }
""", B)


def bauen(mit_png=True):
    seite_schreiben(DATEI, "Visitenkarten",
                    'Visiten<span class="hl">karten</span>',
                    "Drei Entwürfe im Format 85 × 55 mm, jeweils mit Vorder- und Rückseite. Die Vorderseite trägt die Person, die Rückseite die Marke – "
                    "einmal weiß, einmal schwarz, einmal gelb. Alle Entwürfe sind maßstäblich; die PNGs haben 300 dpi.",
                    ["Entwurf 1", "85 × 55 mm", "Vorder- &amp; Rückseite", "3 Varianten", "Daniel · Kerstin · Noah"],
                    inhalt(), CSS)
    if mit_png:
        png_export(DATEI, "visitenkarten")


if __name__ == "__main__":
    bauen("--ohne-png" not in sys.argv)
