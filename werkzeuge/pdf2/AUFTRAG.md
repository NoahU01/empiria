# PDFs 2.0 – Auftrag für die Umsetzung (Stand 10.10.2026)

Daniel hat das Muster **KI zum Anfassen** freigegeben. Alle PDFs der 2.0-Seiten werden in genau diesem Stil neu gebaut.

## Maßstab
- Qualität und Darstellungsart der Volksfest-Seite (`site/projekte/vofe-umzug-schulen.html`): ruhig, reduziert, perfekt ausgerichtet, wenig Text, farbige Bänder, schwarze Kästen, gleiche Elemente auf gleicher Höhe.
- **Schwarz – Weiß – Gelb.** Keine Sekundärfarben (kein Magenta, Cyan, Lila, Grün). Auf Gelb nur Schwarz, auf Weiß kein Gelb als Schrift/Linie/Punkt, auf Schwarz Gelb als Akzent (Labels, Punkte, Icons).
- Highlight in Überschriften: gelber Kasten (`<span class="hl">…</span>`), nie über zwei Zeilen.
- Kicker immer mit kurzem Strich davor (`kicker("…")`). Problem-Abschnitte nie nummeriert.
- Icons: Lucide-Linien-Icons über `ico(name)` (Namen in `werkzeuge/e2_lucide.py`, ICONS). Keine farbigen Kacheln außer der gelben Symbol-Kachel in Fall-Karten. Keine Skizzen, keine alten SVG-Zeichnungen.
- Kein Text darf über Ränder oder Kästen hinausragen; Seiten sollen gefüllt, aber nicht gedrängt wirken (eine Seite = ein Thema).

## Vorbild (unbedingt lesen und nachahmen)
- `werkzeuge/pdf2/ki_zum_anfassen.py` (fertiges Muster, 5 Seiten)
- `werkzeuge/pdf2/ki_varianten.py` → `formate_tabelle()` (Preise/Formate als Vergleichstabelle mit gelber Mitte + schwarzer Kasten darunter) und `beispiele_liste()` (Beispiele als Liste: Titel links, zwei Sätze rechts, Sonderthema als schwarzes Band)
- `werkzeuge/pdf2/lib.py` → alle Bausteine: `titelseite`, `kopfbild(titel)`, `seite`, `kopf`, `kicker`, `punkte`, `posts`, `faelle`, `zeitstrahl`, `team`, `kontaktdaten`, `check`, `dokument`, CSS-Klassen `band band--gelb`, `band--hell`, `band--schwarz`, `kasten`, `zwei`, `tabelle`, `liste`, `seite--hell`.
- Ansehen: `werkzeuge/pdf2/_build/ki-zum-anfassen-seiten/seite-*.png`

## Festgelegter Aufbau (Daniels Wahl)
1. **Titelseite** (`titelseite(...)`): Kicker, H1 mit gelbem Highlight (wie auf der 2.0-Seite), ein Absatz, Kopfbild der Homepage (`kopfbild("<Titel aus e2_kopfbilder.SEITEN>")`), unten Faktenzeile mit 3–4 Fakten.
2. **Das bekommst Du / Ansatz**: gelbes Band mit Kicker, H2, Lead und `punkte([...])` (3 Punkte mit Linie).
3. Inhalte der Seite (Lösung, Ablauf als `zeitstrahl`, Module …) – je Seite ein Thema.
4. **Preise/Formate/Pakete**: als Vergleichstabelle wie `formate_tabelle` (gelbe Mitte = empfohlenes Paket), darunter ggf. schwarzer `kasten` „In jedem Paket enthalten“ o. ä. – nur wenn inhaltlich gedeckt.
5. **Beispiele/Anwendungsfälle**: als Liste wie `beispiele_liste` (volle Texte sinnvoll auf 2 Sätze gekürzt, nichts erfinden), Sonderfall als schwarzes Band.
6. **Schluss**: drei Schritte als `zeitstrahl` + gelbes Band mit Team (`team([...])` – Personen wie auf der 2.0-Seite im Kontakt) und `kontaktdaten()`.
- Kopf/Fuß sind automatisch: oben nur Logo, unten Thema + Seitenzahl (`kopf("<Thema>")` auf jeder Innenseite aufrufen, `seite(inhalt, nr, gesamt)`).

## Inhalte
- Quelle 1 (aktuell, maßgeblich): die 2.0-Seite `site/projekte/empiria-2/<slug>.html` – Überschriften, Kopftexte, Preise, Pakete, Beispiele so übernehmen, wie sie dort stehen (Du-Form, „empiria“ klein).
- Quelle 2 (ergänzend): das alte PDF in `werkzeuge/pdf-seiten/pages.py` (`P["<slug>"]`) – dort stehen Texte, die im PDF zusätzlich vorkommen.
- **Nichts erfinden** (keine Zahlen, Kunden, Preise, Leistungen, die nicht in den Quellen stehen). Kürzen und gliedern ist erlaubt.
- Personen im Team: `PERSONEN` in lib.py (daniel, noah_ki, noah_pm, kerstin_hr, kerstin_content). Fehlt eine Person/Rolle, im eigenen Modul ergänzen: `lib.PERSONEN["key"] = (bild, name, rolle)`.

## Technik
- Je PDF eine eigene Datei `werkzeuge/pdf2/<slug_mit_unterstrich>.py` mit `TITEL` und `def bauen(): return dokument(TITEL, [seiten…], extra_css="")`.
  Optional `DATEI = "dateiname"` (sonst `empiria-<slug>`).
- **lib.py, bauen.py, ki_*.py NICHT ändern.** Eigene CSS-Ergänzungen nur über `extra_css` im eigenen Modul.
- Bauen + prüfen: `python3 werkzeuge/pdf2/bauen.py <slug>` → schreibt das PDF nach `site/assets/downloads/2.0/` und Seitenbilder nach `werkzeuge/pdf2/_build/<slug>-seiten/seite-N.png`; meldet, ob etwas herausragt.
- **Jede Seite als Bild ansehen** (Read auf die PNGs) und so lange nachbessern, bis alles sauber ist: nichts ragt heraus, keine Löcher, keine verwaisten Einzelwörter, gleiche Höhen, Farbregeln eingehalten.
- Nichts committen, nichts pushen, keine Website-Dateien ändern.
