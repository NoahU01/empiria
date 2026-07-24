---
name: design
description: Design-Regeln + Arbeitsablauf für jede UI-/Design-Änderung an der AdMemory-Website — Marken-Farben, Layout-Regeln, und der verpflichtende Screenshot-Loop (bauen → screenshotten → messen → erst nach Okay pushen). Verwenden bei JEDER sichtbaren Änderung: neue Sektionen, Farb-/Layout-Anpassungen, Design-Varianten, Mobile-Fixes.
---

# AdMemory Design-Skill

Dark-only Marketing-Site (Next.js + Tailwind). Dieser Skill bündelt die Regeln,
die sich über die Sessions bewährt haben. Verifikations-Werkzeug ist der
`run-app`-Skill (Dev-Server Port 3001, puppeteer-core + gecachtes Chromium).

## 1. Der Ablauf (nicht verhandelbar)

**Nie „fertig" sagen ohne Beweis.** Jede sichtbare Änderung durchläuft diesen Loop:

1. **Bauen** — Änderung umsetzen (bei Mobile: hinter `sm:`/`md:`-Guards, siehe unten).
2. **Screenshot zwischendrin** — nach jedem nennenswerten Schritt über den
   `run-app`-Skill screenshotten und das Bild WIRKLICH ansehen:
   Desktop 1440×900 **und** Mobile 375×812 (iPhone 13 mini, deviceScaleFactor 2).
   Bei rotierenden/animierten Elementen mehrere Shots zeitversetzt (alle Zustände).
3. **Messen statt schätzen** — Zeilenumbrüche, Box-Höhen, Textbreiten immer
   programmatisch im Live-DOM messen (`getBoundingClientRect`, `lineHeight`),
   nie aus Zeichenzahlen raten. Console-Errors + Pageerrors bei jedem Lauf
   mitlesen (Hydration-Bugs sieht man sonst nicht).
4. **Zeigen** — bei Design-Varianten ("mach das mal, will sehen wie das aussieht"):
   Variante bauen, Screenshot zeigen, **erst nach Okay pushen**.
5. **Sparring-Protokoll** — der User gibt nummeriertes Feedback pro Sektion:
   alle Punkte umsetzen, jeden einzeln visuell verifizieren, pushen (nur auf
   Zuruf bzw. am Runden-Ende), dann Punkt für Punkt mit ✓ berichten und
   markieren, was nur am echten Gerät testbar ist. Wenn er "was denkst du?"
   fragt: erst Empfehlung geben, nicht blind umsetzen.

**Bugs bis zur Wurzel:** reproduzieren → Hypothese → im Live-DOM messen
(Computed Styles die Ancestor-Kette hoch, A/B-Toggle im Browser) → Ursache
fixen, nicht Symptom. Kurz erklären, WARUM der Bug auftrat (ein Absatz).

## 2. Farben

- **Marken-Verlauf `#9B99FE → #4EC9F1`** ist der rote Faden: Hero-Gradient-Text,
  Underline, Farbnebel, Lead-Button-Füllungen (`linear-gradient(135deg, #9B99FE, #4EC9F1)`).
- **Akzent:** `#4EC9F1` (Häkchen, Chips, Fokus-Ringe, Erfolgs-Zustände).
- **Box-Rahmen:** `#7AA8F8`/15 · **Glow:** `rgba(122,168,248,0.35)`.
- **Gelb `#FFD600`: NUR als Glow, Strich/Underline oder kleines Detail.**
  NIE als Flächenfüllung, Button-Hintergrund oder Datenfarbe (mehrfach explizit
  abgelehnt: "bocken nicht in diesem gelb").
- **Dark-only.** Es gibt keinen Light Mode, keine `dark:`-Klassen nötig.
- Altes Icon-Gradient `#9B99FE→#2BC8B7` lebt bewusst in BrandAvatar + BorderBeams.
- Plattform-/Fremdmarken (Google-Buchstabenfarben, Meta-Blau `#0081FB`,
  Instagram-Verlauf) nur innerhalb von Ad-Mockups.
- Bei Palette-Wechseln: Hexcodes greppen (`grep -rn "9B99FE\|4EC9F1\|7AA8F8" components app`).

## 3. Layout-Regeln (aus Feedback destilliert)

- **Desktop nie anfassen, wenn Mobile gefixt wird:** Base-Klassen = Mobile,
  `sm:`/`md:`/`lg:` stellen den abgenommenen Desktop-Zustand wieder her.
- **Headlines max. 2 Zeilen** (H1 im Hero, Section-H2s, Section-Subs) — auf
  Desktop 1440 UND Mobile 375 messen. H1-Größen sind ausgemessene Maxima
  (z.B. paid-ads: 31px ab 375px, 29px darunter — 32px bricht).
- **Boxen einer Gruppe gleich hoch** (z.B. Prozess-Schritte): Beschreibungen
  auf gleiche Zeilenzahl trimmen, Tag-Pills dürfen NICHT umbrechen (Labels
  kürzen statt wrappen). Höhen programmatisch pro Zustand messen.
- **Buttons gleicher Reihe gleich hoch** (explizite h-Klassen, border-box).
- **Keine Waisenwörter:** einzelnes Wort allein in der letzten Headline-Zeile
  vermeiden (Umformulieren oder Umbruch verschieben).
- Anker-Sections brauchen mobil `scroll-mt-20` (fixe Navi).
- Rotierende Elemente (Wort + Mockup) laufen über EINEN gelifteten State,
  nie parallele Intervals.

## 4. Komponenten & Assets

- `cn()` aus `@/lib/utils` für Klassen-Merging; CVA-Button-Varianten nutzen.
- **Shared Components** (PaidAdsPersonal, SectionTag-Kopien, PlatformAdMockup,
  BookingSection, die per Props überschreibbaren PaidAds-Sektionen …) werden
  auf mehreren Seiten genutzt: bei Änderungen IMMER sagen, welche anderen
  Seiten betroffen sind, und dort gegentesten.
- **Neue Bilder:** vorab mit sharp verkleinern + WebP (max ~1200px, quality
  78–82), `loading="lazy" decoding="async"` (Ausnahme: Logo-Marquee).
- Sektions-IDs vergeben (Tracking `section_view_*` läuft automatisch darüber,
  und sie dienen als Sitelink-Anker).

## 5. Git

- Push nur auf Zuruf ("push mal") oder am Runden-Ende. Beschreibende Commits
  (pro Sektion aufgelistet). Unversionierte Alt-Experimente des Users nie
  ungefragt committen.
