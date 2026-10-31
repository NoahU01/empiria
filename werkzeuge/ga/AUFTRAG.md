# Geschäftsausstattung – Entwürfe (Daniel, 10.10.2026)

Daniel will für jede Vorlage einen ersten Entwurf sehen, ohne vorher Rückfragen. Maßstab: die Gestaltung von www.empiria.de (empiria 2.0) und die Volksfest-Seite `site/projekte/vofe-umzug-schulen.html` – ruhig, reduziert, perfekt ausgerichtet, wenig Text.

## Gestaltungssystem (verbindlich)
- Farben: Weiß #ffffff (Grundfläche), Schwarz #1a1817, Gelb #fff400, Grau #f3f1ee. Sekundärfarben nur als Akzent oder Vollfläche für Themen: Magenta #C51F5D, Violett #8613A1, Cyan #0B9FBD. Auf Gelb nur Schwarz; auf Schwarz Gelb als Akzent; nie Weiß auf Gelb.
- Schriften: Lora 700 für Überschriften (letter-spacing -.02em), Poppins 300/400/600/700 für Text. Fonts: `/assets/fonts/fonts.local.css`.
- Bausteine: Kicker mit kurzem Strich davor (Großbuchstaben, gesperrt), gelber Highlight-Kasten in Überschriften (`background:#fff400; padding:0 .12em .07em; border-radius:.14em`, nie über zwei Zeilen), Doppelpfeil (Form `FORM["forward"]` aus `werkzeuge/e2_bauen.py`, viewBox "2.83 31.08 226.78 170.29"), weitere Formen dort: kreis, kreuz, quadrat, raute, stern, blitz, blase. Lucide-Icons: `from e2_lucide import ICONS`.
- Logo: `/assets/empiria-logo.svg` (schwarz), `/assets/empiria-logo-weiss.svg` (weiß). „empiria“ immer klein.
- Personen/Kontakt: Daniel Ströbel · Geschäftsführer / Strategiehandwerker · daniel.stroebel@empiria.de · +49 176 3134 7217 · www.empiria.de · empiria GmbH, Kapellengasse 6, 74564 Crailsheim. Kerstin Christ (Expertin HR & Weiterbildung) und Noah Hermanns (Experte Performance Marketing): für sie E-Mail/Telefon als Platzhalter „vorname.nachname@empiria.de“ / „+49 …“ und das kenntlich machen. Porträts: `/assets/ansprechpartner-{daniel,kerstin,noah}.webp`, Teamfoto `/assets/team-portrait.webp`.
- Claim/Texte: „Strategie, die wirkt.“ ist der Claim. Keine erfundenen Fakten; Platzhalter klar als solche.

## Seiten
- Seitenrahmen (Kopf mit Entwicklungsmenü, Fuß): aus `site/projekte/powerpoint-master.html` übernehmen (alles außer `<main>…</main>`), Titel anpassen, robots noindex lassen. Seitenaufbau wie powerpoint-master: Kicker „Geschäftsausstattung“, H1 mit gelbem Highlight, Lead, dann Abschnitte mit Entwürfen in echten Seitenverhältnissen (container-type + cqw-Einheiten, damit alles maßstäblich skaliert), Beschriftung unter jedem Entwurf (Format + Maße).
- Je Thema mindestens 2 Varianten (z. B. hell/schwarz/gelb), damit Daniel wählen kann. Kurz beschreiben, worin sie sich unterscheiden.
- Wo sinnvoll, echte Dateien in Originalgröße als PNG exportieren (Puppeteer: `site/node_modules/puppeteer-core`, Chrome `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`) nach `site/projekte/ga/<thema>/…png` und auf der Seite als Download-Link anbieten. Pflicht bei Hintergrundbildern und LinkedIn-Bannern.
- Je Thema ein eigenes Python-Skript `werkzeuge/ga/<thema>.py`, das die Seite `site/projekte/<seitenname>.html` (und ggf. PNGs) erzeugt.
- Nach dem Bauen: jede Seite per Screenshot (Desktop 1280 und Handy 390) ansehen und nachbessern, bis sauber. Lokaler Server: http://localhost:4599 (läuft).
- NICHT ändern: `werkzeuge/entwicklung-menu.html`, `site/projekte/geschaeftsausstattung.html`, andere bestehende Seiten. Nichts committen. Am Ende kurz berichten: Seitenname(n), Varianten, offene Punkte.
