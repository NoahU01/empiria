"""Kopfbilder für alle Seiten – Darstellungsart Mono (Daniel, 10.10.2026).

Je Seite ist der Aufbau (1–10 aus e2_varianten.AUFBAU) gezielt nach dem Inhalt gewählt:
  Prozess  → wenn die Seite einen Weg beschreibt     Raster → Übersichtsseiten mit mehreren Formaten
  Kreis    → wenn Dinge ineinandergreifen             Typo   → wenn eine Zahl die Aussage trägt
  Trio     → ein Kern mit zwei Begleitern             Rahmen → ein Ergebnis/Produkt im Mittelpunkt
  Beschriftet → wenn drei Bausteine benannt werden    Gestapelt → ein Paket aus mehreren Teilen
  Auf einer Linie → Dinge/Menschen nebeneinander      Ein Icon → eine einzige, klare Sache
"""
import e2_varianten as va

A = {f.__name__: (f, n) for f, n in va.AUFBAU}

# (Titel, Bereich, Farbwelt, Überschrift live, Aufbau, Icons [Haupt, Akzent, …], Beschriftungen, Kennwort, Begründung)
SEITEN = [
    ("Startseite", "Strategie, die wirkt.", "gelb", "Strategie, die wirkt.", "a_reihe",
     ["magnifying-glass", "puzzle-piece", "trend-up", "flag-banner"], ["ERKENNEN", "EINORDNEN", "VERÄNDERN", ""], "Wirkung",
     "Der Dreischritt der Startseite: Schmerz erkennen, ins Geschäftsmodell einordnen, Veränderung bewirken."),
    ("Strategie in den Alltag überführen", "Strategiehandwerk", "gelb", "Strategie in den Alltag überführen.", "a_beschriftet",
     ["flag-banner", "compass", "wrench", "user-focus"], ["ROLLE", "RICHTUNG", "HANDWERKSZEUG", ""], "Alltag",
     "Die Lösung hat drei benannte Bausteine – Rolle, Richtung, Handwerkszeug – rund um das Ziel."),
    ("Komplexe Themen strukturieren & kommunizieren", "Strategiehandwerk", "gelb", "Komplexe Themen strukturieren & kommunizieren.", "a_reihe",
     ["stack", "funnel", "target", "presentation"], ["FOLIENBERG", "STRUKTUR", "BOTSCHAFT", ""], "Botschaft",
     "Ein Weg: vom Folienberg über die Struktur zu einer Botschaft, die ankommt."),
    ("Innovation & Geschäftsmodell neu denken", "Strategiehandwerk", "gelb", "Innovation & Geschäftsmodell neu denken.", "a_trio",
     ["lightbulb", "arrows-clockwise", "puzzle-piece", "cube"], ["", "", "", ""], "Neu",
     "Ein Kern (die Idee) mit zwei Begleitern: neu denken, Bausteine neu zusammensetzen."),
    ("Teams befähigen, professionell zu kommunizieren", "Strategiehandwerk / Training", "gelb", "Teams befähigen, professionell zu kommunizieren.", "a_boden",
     ["chalkboard-teacher", "users-three", "check-circle", "chats-circle"], ["", "", "", ""], "Team",
     "Menschen nebeneinander: wer präsentiert, das Team, das Ergebnis."),
    ("Workshops", "Formate", "magenta", "Workshops, die wirken. Nicht nur Theorie.", "a_raster",
     ["sparkle", "browser", "chats-circle", "check-circle"], ["KI ZUM ANFASSEN", "SPRINT LANDINGPAGE", "MODERATION", "ERGEBNIS"], "Workshops",
     "Übersichtsseite: die drei Formate auf einen Blick, plus das gemeinsame Ziel Ergebnis."),
    ("KI zum Anfassen", "Workshops", "magenta", "Deine KI. Zum Anfassen. Volle Wirkung.", "a_kreis",
     ["chat-text", "sparkle", "cards", "users-three"], ["", "", "", ""], "KI",
     "Im Zentrum der eigene Fall, ringsum Tools im Vergleich und das Team – alles greift ineinander."),
    ("Sprint Landingpage", "Workshops", "magenta", "Live in nur 48 Stunden. Sauber gebaut, volle Wirkung.", "a_typo",
     ["browser", "timer", "device-mobile", "rocket-launch"], ["", "", "", ""], "48h",
     "Die Zahl ist das Versprechen – 48 Stunden trägt die Seite."),
    ("Moderation deines Workshops", "Workshops", "magenta", "Dein Workshop. Souverän moderiert. Volle Wirkung.", "a_trio",
     ["chats-circle", "check-circle", "kanban", "users-three"], ["", "", "", ""], "Klarheit",
     "Ein Kern (das Gespräch) mit zwei Begleitern: das Board und die Handlungsklarheit."),
    ("Der beste Workshop", "Workshops", "magenta", "Dein Workshop. Mit Ergebnis. Volle Wirkung.", "a_rahmen",
     ["target", "star", "users-three", "check-circle"], ["EIN ZIEL", "", "", ""], "1 Ziel",
     "Ein Ergebnis im Mittelpunkt: ein Ziel pro Workshop, ausgezeichnet."),
    ("Marketing 2.0", "Formate", "cyan", "Marketing für Versicherer anders gedacht.", "a_raster",
     ["presentation-chart", "eye", "target", "stack"], ["MES", "SOFORT SICHTBAR", "PAID ADS", "MEDIEN"], "Marketing",
     "Übersichtsseite: die vier Wege auf einen Blick."),
    ("MarketingEcoSystem (MES)", "Marketing 2.0", "cyan", "Du konzentrierst Dich nicht auf Marketing, sondern auf Dein Business.", "a_kreis",
     ["presentation-chart", "trend-up", "browser", "megaphone"], ["", "", "", ""], "MES",
     "Ein Ökosystem: das Dashboard in der Mitte, Seite, Kanäle und Wirkung greifen ineinander."),
    ("sofort sichtbar", "Marketing 2.0", "cyan", "Digital sichtbar. Ohne Briefing. Sofort einsatzbereit.", "a_gestapelt",
     ["device-mobile", "browser", "envelope-simple", "eye"], ["", "", "", ""], "Sofort",
     "Ein fertiges Paket aus drei Teilen: Postings, Landingpage, E-Mail-Funnel."),
    ("Paid Ads", "Marketing 2.0", "cyan", "Google Ads für Deine Zielgruppe. Zur richtigen Zeit.", "a_reihe",
     ["magnifying-glass", "megaphone", "envelope-simple", "target"], ["SUCHE", "ANZEIGE", "ANFRAGE", ""], "Anfragen",
     "Ein Weg: jemand sucht, sieht die Anzeige, fragt an."),
    ("Medien, die Ergebnisse liefern", "Marketing 2.0", "cyan", "Deine Botschaft. Auf den Punkt. Volle Wirkung.", "a_boden",
     ["presentation", "browser", "film-strip", "stack"], ["", "", "", ""], "Medien",
     "Die Medien stehen nebeneinander: Präsentation, Landingpage, Video."),
    ("PowerPoint", "Medien", "cyan", "Deine Folien. Ein Auftritt. Volle Wirkung.", "a_rahmen",
     ["presentation", "star", "chalkboard-teacher", "check-circle"], ["EINE BOTSCHAFT JE FOLIE", "", "", ""], "Folie",
     "Ein Produkt im Mittelpunkt: die eine Folie, die trägt."),
    ("Landingpage", "Medien", "cyan", "Deine Botschaft. Eine Seite. Volle Wirkung.", "a_trio",
     ["browser", "device-mobile", "lightning", "target"], ["", "", "", ""], "Eine Seite",
     "Ein Kern (die Seite) mit zwei Begleitern: mobil zuerst, schnell geladen."),
    ("Roll-up", "Medien", "cyan", "Dein Auftritt. Ein Blick. Volle Wirkung.", "a_boden",
     ["image-square", "users-three", "chats-circle", "eye"], ["", "", "", ""], "Auftritt",
     "Nebeneinander im Raum: das Roll-up, die Besucher, das Gespräch, das es eröffnet."),
    ("Video", "Medien", "cyan", "Deine Botschaft. Bewegt. Volle Wirkung.", "a_einzel",
     ["play-circle", "video-camera", "film-strip", "eye"], ["", "", "", ""], "Video",
     "Eine einzige, klare Sache: das Video."),
    ("Digitale Tools", "Marketing 2.0", "cyan", "Digitale Tools, die den Alltag einfacher machen.", "a_kreis",
     ["squares-four", "presentation-chart", "device-mobile", "browser"], ["", "", "", ""], "Tools",
     "Tools, die zusammenspielen: ein Ort in der Mitte, die Systeme ringsum."),
    ("Training & Sparring", "Formate", "violett", "Begleitung, die wirkt. Kein Seminar von der Stange.", "a_trio",
     ["handshake", "trend-up", "users-three", "chats-circle"], ["", "", "", ""], "Begleitung",
     "Ein Kern (Begleitung) mit zwei Begleitern: Wirkung im Alltag und das Team."),
    ("1:1 Sparring", "Training & Sparring", "violett", "Offen sprechen. Klar entscheiden. Volle Wirkung.", "a_typo",
     ["chats-circle", "lightbulb", "handshake", "check-circle"], ["", "", "", ""], "1:1",
     "Die Zahl ist das Format: eins zu eins, auf Augenhöhe."),
    ("Impulsvorträge", "Einzelseite", "violett", "Impulse, die nachwirken. Nicht nur unterhalten.", "a_einzel",
     ["microphone-stage", "lightbulb", "users-three", "chats-circle"], ["", "", "", ""], "Impuls",
     "Eine einzige, klare Sache: der Vortrag mit einer These."),
]


def bild(seite):
    titel, bereich, welt, h1, aufbau, icons, labels, wort, warum = seite
    f, name = A[aufbau]
    sz = dict(titel=titel, icons=icons, labels=labels, wort=wort, welt=welt)
    return f(sz, "mono"), name
