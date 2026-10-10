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

---
# Runde 2 (Daniel, 10.10.2026) – Überarbeitung ALLER PDFs

## Grundsätze (gelten vor allem anderen)
1. **Inhalt = die aktuelle 2.0-Seite.** Das PDF gibt die Seite sehr gut wieder – mit allen aktuellen Überschriften, Kopftexten, Abschnitten in derselben Reihenfolge und Logik. Die Seiten wurden in den letzten Tagen stark umgebaut: alles logisch neu gegen `site/projekte/empiria-2/<slug>.html` prüfen.
2. **Plus Details aus Pop-ups/Fenstern:** Alles, was auf der Seite erst nach Klick sichtbar ist (`<dialog class="e2-dialog">`, `.modal-overlay`, „Mehr lesen“, „Module & Ergebnis“, Erklär-Knöpfe, Akkordeons), gehört ausführlich ins PDF. Das PDF ist die ausführliche Fassung.
3. **Preise dürfen genannt werden** (so wie auf den Seiten).
4. **Alte PDF-Texte (pages.py) nicht 1:1 übernehmen** – nur, wo sie zur aktuellen Seite passen. Lieber weglassen als Altes behalten, das der Seite widerspricht (z. B. „Für wen“-Listen nur, wenn sie zur Seite passen).
5. **Alle PDFs gleich gebaut** – gleiche Bausteine, gleiche Reihenfolge-Logik, gleiche Abstände, gleiche Typografie. Kein PDF darf aus der Reihe fallen (die Strategiehandwerk-PDFs müssen genauso aussehen wie die übrigen).

## Einheitlicher Aufbau (Pflicht, in dieser Reihenfolge, Abschnitte nur wenn die Seite sie hat)
1. Titelseite: `titelseite()` – Kicker = Unterzeile der Seite, H1 exakt wie auf der Seite (gleiche Hervorhebung), Kopftext der Seite, Bild (Strategiehandwerk: großes Themen-Zeichen, sonst `kopfbild`), Faktenzeile mit 3–4 Fakten aus der Seite.
2. Problem (falls Seite eins hat): Text oben + darunter gelbes Band „Die Lösung“ mit `punkte` – ODER bei Seiten ohne Problem: gelbes Band „Das bekommst Du/Unser Ansatz“ mit `punkte`.
3. Inhaltsseiten in der Reihenfolge der Website-Abschnitte; Schritte immer als `zeitstrahl`, Module/Details als `liste`, Zwischenergebnisse/Hinweise als schwarzer `kasten`.
4. Preise/Formate/Pakete: Vergleichstabelle wie `ki_varianten.formate_tabelle` (gelbe Spalte = auf der Seite hervorgehobenes Paket, sonst keine gelbe Spalte), darunter optional schwarzer Kasten „In jedem … enthalten“.
5. Beispiele/Anwendungsfälle/FAQ: `liste` wie `ki_varianten.beispiele_liste` auf `seite--hell`; hervorgehobener Fall („Im Fokus“/„Sonderthema“) als schwarzes Band.
6. Schluss: Kicker „Jetzt loslegen“, H2 = Kontakt-Überschrift der Seite mit Highlight, Lead, `zeitstrahl` 3 Schritte (Kurz schildern / Vorschlag erhalten / Festzurren), gelbes Band Kicker „Dein direkter Draht zu uns“ + H2 „Aus Gespräch wird Klarheit.“ + Team (Personen genau wie im Kontakt der 2.0-Seite) + `kontaktdaten()`.

## Einheitliche Maße (nicht abweichen)
- Innenseiten beginnen mit `kopf(Thema)`, Inhalt mit `'<div class="rand" style="padding-top:16mm">'` bzw. Bänder mit `margin-top:10mm` direkt unter dem Kopf.
- H2 in Bändern und Seiten nur über das Standard-`<h2>` (keine eigenen Schriftgrößen). Kein eigenes `extra_css` für Typografie; extra_css nur für echte Sonderbausteine.
- Fußzeile automatisch (Thema + Seitenzahl). Thema = kurzer Seitenname (z. B. „Strategie in den Alltag“, „Teams befähigen“).

## Festlegungen zu Einzelfragen
- Impulsvorträge: „Strategie für Aufsichtsräte“ als schwarzes Sonderthema-Band aufnehmen (Inhalt aus pages.py P["strategie-fuer-aufsichtsraete"] verdichten).
- Sprint: „48“ nur einmal (im Titelbild); Schluss-Überschrift ohne Zahl.
- Workshops-Übersicht: Preise aller drei Formate wie auf den Detailseiten; keine gelbe Spalte, solange die Seite keinen Favoriten markiert.
- Paid Ads: Kanäle so nennen, wie es die Paid-Ads-Seite tut.

---
# Runde 3 (Daniel, 10.10.2026) – Übersichts-PDFs mit Kapiteln
Workshops, Marketing 2.0 und Training & Sparring fassen Unterseiten zusammen. Ihr PDF muss deshalb **je Unterseite ein eigenes Kapitel** enthalten, sonst steht kaum etwas drin.
- Aufbau: Titel · Ansatz (gelbes Band) · **Überblick** (die Wege/Formate als Vergleichstabelle oder Liste, mit Preisen) · **Kapitel je Unterseite** · Schluss.
- Kapitel-Einstieg: eigene Seite oder Seitenanfang mit großer Kapitelnummer („01“), Kicker = Name der Unterseite, H2 = Kopfzeile der Unterseite mit Highlight, Lead = Kopftext der Unterseite. Danach 1–2 Seiten Kerninhalt der Unterseite: Problem/Ansatz als `punkte`, Ablauf als `zeitstrahl`, Preise/Pakete als Tabelle, 2–3 stärkste Beispiele als `liste`. Nicht das ganze Unter-PDF kopieren – verdichten, das Wesentliche, damit der Leser alles Wichtige auf einen Blick hat.
- Zum Wiederverwenden: Die Module der Unterseiten (z. B. ki_zum_anfassen.py, sprint_landingpage.py …) enthalten die Inhalte bereits; Texte gern von dort übernehmen. Inhaltlich gilt die aktuelle 2.0-Seite.
- Am Schluss eines Kapitels ein kleiner Hinweis „Alle Details: eigenes PDF ‚<Name>‘ auf empiria.de“ (als Notiz, kein Kasten).
- Nach dem Einbau: das ganze PDF Seite für Seite als Bild prüfen – Highlights dürfen keine Buchstaben der Zeile darüber verdecken, nichts ragt heraus, keine Löcher, gleiche Abstände wie in den anderen PDFs.
