"""Kopfbilder für alle Seiten – Darstellungsart Mono als strenges System (Daniel, 10.10.2026).

Warum ein System: Einzelstücke mit zehn Aufbauten und skalierten Strichen wirkten ungleich und unprofessionell.
Regeln, die für jedes Bild gelten:
  · eine Icon-Familie (Lucide, Linien-Icons) mit IDENTISCHER Strichstärke – unabhängig von der Icon-Größe
  · nur drei Aufbauten mit festem Raster:  Trio (Kern + zwei Begleiter) · Reihe (drei Schritte/Teile) · Zahl (Kennzahl trägt)
  · nur zwei Icon-Größen je Bild, feste Positionen, gleiche Ränder
  · Mono: nur Linien, KEINE Farbflächen – Farbe nur über ein Icon in Akzentfarbe
  · Beschriftung nur in der Reihe, immer gleiche Schrift
"""
from e2_lucide import ICONS

K, G3 = "#1a1817", "#b9b3ab"
MT = "#C51F5E"            # Akzent als Linie (wird je Farbwelt ersetzt; bei Gelb → Schwarz)
MK = "#C51F6A"            # Marker-Fläche (wird je Farbwelt ersetzt; bei Gelb → Gelb)
SERIF, SANS = "Lora, Georgia, serif", "Poppins, Arial, sans-serif"
STRICH = 5.2              # Strichstärke in Bildeinheiten – für ALLE Icons gleich


def _svg(inhalt):
    return f'<svg class="hv-bild" viewBox="0 0 440 400" role="img" font-family="{SANS}">{inhalt}</svg>'


def icon(name, x, y, g, farbe=K):
    return (f'<g transform="translate({x} {y}) scale({g/24:.4f})" fill="none" stroke="{farbe}" stroke-width="{STRICH*24/g:.3f}" '
            f'stroke-linecap="round" stroke-linejoin="round">{ICONS[name]}</g>')


def marker(x, y, w, h):
    """Mono: keine Farbflächen (Daniel) – Marker bleibt leer."""
    return ""


def trio(haupt, akzent, neben):
    # Kern 196 links, zwei Begleiter 84 rechts – oben/unten bündig mit dem Kern
    return _svg(marker(96, 168, 176, 150) + icon(haupt, 40, 104, 196) + icon(akzent, 316, 104, 84, MT) + icon(neben, 316, 216, 84))


def reihe(icons, labels, pfeile=True, doppel=False, oben="", y0=116):
    o = oben
    dy = y0 - 116
    for k, (n, l) in enumerate(zip(icons, labels)):
        cx = 80 + k * 140
        if k == (2 if pfeile else 0):
            o += marker(cx - 44, 158, 104, 84)
        o += icon(n, cx - 50, 116 + dy, 100, MT if k == (2 if pfeile else 0) else K)
        o += f'<text x="{cx}" y="{286 + dy}" font-size="14" font-weight="600" letter-spacing="1.6" fill="{K}" text-anchor="middle" font-family="{SANS}">{l}</text>'
        if pfeile and k < 2:
            ax = cx + 58
            if doppel:   # Doppelpfeil der Marke statt einfachem Pfeil (Startseite, Daniel)
                o += f'<path d="M{ax} {154+dy}l11 12-11 12M{ax+12} {154+dy}l11 12-11 12" fill="none" stroke="{K}" stroke-width="{STRICH}" stroke-linecap="round" stroke-linejoin="round"/>'
            else:
                o += f'<path d="M{ax} {166+dy}h24m-8-8 8 8-8 8" fill="none" stroke="{G3}" stroke-width="3.4" stroke-linecap="round" stroke-linejoin="round"/>'
    return _svg(o)


def zielgruppe(namen, icons, labels):
    """Reihe mit Doppelpfeil, darüber die Zielgruppen als ruhiger Text – die Story beginnt bei der Zielgruppe (Komplexe Themen)."""
    zeilen, z = [], ""
    for n in namen:                       # Namen auf Zeilen verteilen (ca. 34 Zeichen je Zeile)
        if len(z) + len(n) > 34 and z:
            zeilen.append(z); z = ""
        z = (z + "  ·  " if z else "") + n.upper()
    zeilen.append(z)
    o = "".join(f'<text x="220" y="{40 + i*22}" font-size="12.5" font-weight="600" letter-spacing="1.4" fill="#8a847c" text-anchor="middle" font-family="{SANS}">{t}</text>' for i, t in enumerate(zeilen))
    return reihe(icons, labels, doppel=True, oben=o, y0=96 + len(zeilen) * 14)


def zahl(wort, akzent):
    breite = len(wort) * 96
    return _svg(marker(30, 214, breite + 20, 84)
                + f'<text x="36" y="282" font-size="196" font-weight="700" letter-spacing="-6" fill="{K}" font-family="{SERIF}">{wort}</text>'
                + icon(akzent, 320, 60, 84, MT))


# (Titel, Bereich, Farbwelt, Überschrift live, Aufbau, Daten, Begründung)
SEITEN = [
    ("Startseite", "Startseite", "gelb", "Strategie, die wirkt.", "reihe_dp", (["search", "puzzle", "trending-up"], ["ERKENNEN", "EINORDNEN", "VERÄNDERN"]), "Der Dreischritt der Startseite."),
    ("Strategie in den Alltag überführen", "Strategiehandwerk", "gelb", "Strategie in den Alltag überführen.", "trio", ("flag", "compass", "wrench"), "Ziel, Richtung, Handwerkszeug."),
    ("Komplexe Themen strukturieren & kommunizieren", "Strategiehandwerk", "gelb", "Komplexe Themen strukturieren & kommunizieren.", "reihe_pur",
     (["users", "puzzle", "trophy"], ["", "", ""]), "Zielgruppe » ihr Problem » ihr Erfolg – nur Icons, einfache Pfeile (Daniel)."),
    ("Innovation & Geschäftsmodell neu denken", "Strategiehandwerk", "gelb", "Innovation & Geschäftsmodell neu denken.", "trio", ("lightbulb", "refresh-cw", "blocks"), "Die Idee, neu gedacht, neu zusammengesetzt."),
    ("Teams befähigen, professionell zu kommunizieren", "Strategiehandwerk / Training", "gelb", "Teams befähigen, professionell zu kommunizieren.", "trio", ("presentation", "users", "circle-check"), "Präsentieren, Team, Ergebnis."),
    ("Workshops", "Formate", "magenta", "Workshops, die wirken. Nicht nur Theorie.", "reihe_o", (["sparkles", "app-window", "messages-square"], ["KI", "LANDINGPAGE", "MODERATION"]), "Übersicht: die drei Formate."),
    ("KI zum Anfassen", "Workshops", "magenta", "Deine KI. Zum Anfassen. Volle Wirkung.", "trio", ("message-square-text", "sparkles", "users"), "Eigener Fall, KI, Team."),
    ("Sprint Landingpage", "Workshops", "magenta", "Live in nur 48 Stunden. Sauber gebaut, volle Wirkung.", "zahl", ("48h", "timer"), "Die Zahl ist das Versprechen."),
    ("Moderation deines Workshops", "Workshops", "magenta", "Dein Workshop. Souverän moderiert. Volle Wirkung.", "trio", ("messages-square", "circle-check", "users"), "Gespräch, Klarheit, Team."),
    ("Der beste Workshop", "Workshops", "magenta", "Dein Workshop. Mit Ergebnis. Volle Wirkung.", "trio", ("goal", "star", "users"), "Ein Ziel, ausgezeichnet, alle dabei."),
    ("Marketing 2.0", "Formate", "cyan", "Marketing für Versicherer anders gedacht.", "reihe_o", (["layout-dashboard", "eye", "megaphone"], ["DASHBOARD", "SICHTBARKEIT", "KAMPAGNEN"]), "Übersicht: die Wege."),
    ("MarketingEcoSystem (MES)", "Marketing 2.0", "cyan", "Du konzentrierst Dich nicht auf Marketing, sondern auf Dein Business.", "trio", ("layout-dashboard", "trending-up", "megaphone"), "Dashboard, Wirkung, Kanäle."),
    ("sofort sichtbar", "Marketing 2.0", "cyan", "Digital sichtbar. Ohne Briefing. Sofort einsatzbereit.", "reihe", (["smartphone", "app-window", "mail"], ["POSTING", "LANDINGPAGE", "E-MAIL"]), "Das fertige Paket."),
    ("Paid Ads", "Marketing 2.0", "cyan", "Google Ads für Deine Zielgruppe. Zur richtigen Zeit.", "reihe", (["search", "megaphone", "mail"], ["SUCHE", "ANZEIGE", "ANFRAGE"]), "Vom Suchen zur Anfrage."),
    ("Medien, die Ergebnisse liefern", "Marketing 2.0", "cyan", "Deine Botschaft. Auf den Punkt. Volle Wirkung.", "reihe_o", (["presentation", "app-window", "film"], ["POWERPOINT", "LANDINGPAGE", "VIDEO"]), "Übersicht: die Medien."),
    ("PowerPoint", "Medien", "cyan", "Deine Folien. Ein Auftritt. Volle Wirkung.", "trio", ("presentation", "star", "users"), "Die Folie, die trägt."),
    ("Landingpage", "Medien", "cyan", "Deine Botschaft. Eine Seite. Volle Wirkung.", "trio", ("app-window", "smartphone", "zap"), "Eine Seite, mobil, schnell."),
    ("Roll-up", "Medien", "cyan", "Dein Auftritt. Ein Blick. Volle Wirkung.", "trio", ("image", "users", "message-circle"), "Auftritt, Besucher, Gespräch."),
    ("Video", "Medien", "cyan", "Deine Botschaft. Bewegt. Volle Wirkung.", "trio", ("circle-play", "video", "film"), "Video, Dreh, Schnitt."),
    ("Digitale Tools", "Marketing 2.0", "cyan", "Digitale Tools, die den Alltag einfacher machen.", "trio", ("layout-grid", "chart-column", "smartphone"), "Ein Ort, Zahlen, App."),
    ("Training & Sparring", "Formate", "violett", "Begleitung, die wirkt. Kein Seminar von der Stange.", "trio", ("handshake", "trending-up", "users"), "Begleitung, Wirkung, Team."),
    ("1:1 Sparring", "Training & Sparring", "violett", "Offen sprechen. Klar entscheiden. Volle Wirkung.", "zahl", ("1:1", "messages-square"), "Die Zahl ist das Format."),
    ("Impulsvorträge", "Einzelseite", "violett", "Impulse, die nachwirken. Nicht nur unterhalten.", "trio", ("mic-vocal", "lightbulb", "users"), "Vortrag, These, Publikum."),
]

NAMEN = {"zielgruppe": "Zielgruppe zuerst", "reihe_dp": "Reihe mit Doppelpfeil", "trio": "Trio", "reihe": "Reihe (Prozess)", "reihe_o": "Reihe (Übersicht)", "zahl": "Zahl"}


def bild(seite):
    titel, bereich, welt, h1, aufbau, daten, warum = seite
    if aufbau == "trio":
        return trio(*daten), NAMEN[aufbau]
    if aufbau == "reihe":
        return reihe(*daten), NAMEN[aufbau]
    if aufbau == "reihe_pur":
        return reihe(*daten), NAMEN.get(aufbau, "Reihe")
    if aufbau == "zielgruppe":
        return zielgruppe(*daten), NAMEN[aufbau]
    if aufbau == "reihe_dp":
        return reihe(*daten, doppel=True), NAMEN[aufbau]
    if aufbau == "reihe_o":
        return reihe(*daten, pfeile=False), NAMEN[aufbau]
    return zahl(*daten), NAMEN[aufbau]


def eng(seite):
    """Enger Bildausschnitt (viewBox) ohne Rand – für die mobile Darstellung über der Überschrift."""
    a = seite[4]
    if a == "trio":
        return "36 100 368 204"
    if a == "zahl":
        return "28 56 380 246"
    if a == "zielgruppe":
        return "26 108 392 190"
    return "26 112 392 186"   # Reihen
