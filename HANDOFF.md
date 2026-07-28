# empiria – Website · Handoff

Stand: 2026-07-28

Marketing-One-Pager für **empiria** (Strategieberatung für Führungskräfte in der
Versicherungsbranche, GF Daniel Ströbel). 1:1 nachgebaut aus dem Kunden-Mockup
`00_Homepage empiria.pdf`, mit voll ausgearbeiteter Mobile-Variante.

---

## 1. Live & Repository

- **Repository:** https://github.com/NoahU01/empiria (Branch `main`)
- **Hosting:** Vercel (mit dem Repo verbunden → jeder Push auf `main` deployt automatisch)
- **Root-`vercel.json`** leitet alle Requests nach `site/` um (die Website liegt im
  Unterordner). Alternativ ginge in Vercel: *Settings → Root Directory = `site`*.
- Lokaler Projektordner ist bereits mit dem Remote verbunden (`main` trackt `origin/main`).

## 2. Tech-Stack

Bewusst **ohne Framework/Build-Step** – statisches HTML/CSS/Vanilla-JS, damit es
langfristig wartbar und deploybar bleibt.

- `site/index.html` – gesamte Seitenstruktur + inline SVG-Icon-Symbole
- `site/styles.css` – alles Styling (ein File, Desktop-first mit Mobile-Media-Queries)
- `site/script.js` – Logo-Marquee, Popups/Modals, Mobile-Menü, Header-Scroll-State,
  Logo→Top, Marquee-Drag
- `site/assets/` – Fonts (self-hosted), Logos, Portrait(s), abgeleitete WebPs
- Fonts: **Lora** (Serif, Headlines) + **Poppins** (Sans, Fließtext/UI), self-hosted
  unter `site/assets/fonts/` (kein externer CDN-Call).

## 3. Lokal starten / entwickeln

```bash
cd site
python3 -m http.server 4599
# -> http://localhost:4599
```

**Screenshot-/Verifikations-Workflow** (so wurde die ganze Zeit gearbeitet: bauen →
screenshotten → mit PDF/Referenz abgleichen → erst dann committen):

```bash
cd site
npm install                 # einmalig: installiert puppeteer-core (nutzt System-Chrome)
node shot.mjs               # rendert Desktop 1440x900 + Mobile 375x812 + ein Modal
                            # -> Bilder landen in site/_shots/ (gitignored)
# optional: BASE=... OUT=... CHROME=... als Env-Vars überschreibbar
node measure.mjs            # misst Live-DOM-Geometrie (Zeilen, Boxen etc.)
```

> Voraussetzung: Google Chrome installiert (Pfad in `shot.mjs` ggf. anpassen bzw.
> `CHROME=/pfad node shot.mjs`).

## 4. Seitenaufbau (Sektionen)

Header/Nav → Hero → Logo-Leiste (Kunden) → Problem → Lösung → Leistungen (2×2 mit
Popups) → Stats („Verstehen. Strukturieren. Umsetzen.") → Kontakt → Footer.

- **Texte** stammen 1:1 aus dem PDF; die **Popup-Texte** (Lösung + 4 Leistungen)
  wortwörtlich aus den DOCX-Dateien `05_`–`09_` und liegen als `MODALS`-Objekt in
  `script.js`.
- **Marken-Elemente:** Highlight-Gelb (immer **fett**), Serif-Headlines mit
  gelbem Marker, Brand-Icons (Forward »/Kreis/Kreuz/Raute) als Inline-SVG-Symbole,
  auch als dezente Hintergrund-Wasserzeichen.

## 5. Design-Tokens (Auszug, siehe `:root` in `styles.css`)

- Highlight-Gelb `--hl / --hl-solid: #fff400` (knallig; die markierten Wörter sind fett)
- Text/Ink `#1a1817`, Grau-90 `#2e2d2c`, Problem-Section-BG `#ededed`, Schwarz `#000`
- Marken-Gold `#998675` (Logo/Icons-Herkunft)
- Fonts: `--font-serif: Lora`, `--font-sans: Poppins`
- Container `max-width: 1240px` (Leistungen etwas breiter: 1340px)

## 6. Assets

- **Kundenlogos:** `site/assets/logos/logo-01…12-*.svg` – der **Freigabe-Satz (12 Logos)**
  aus `02_Logos_Farbe_Freigabe/`. Reihenfolge:
  Desktop-Laufband = Ordner-Reihenfolge (01→12); Mobile-Raster = abweichende
  Reihenfolge (per CSS `order`, cominia/DEVK AM getauscht). Logo-Liste steht in
  `script.js`.
- **Daniel Portrait:** Desktop = Freisteller `assets/daniel.webp`; Mobile = rundes
  Porträt `assets/daniel-round.webp` (gerendert aus `Bild Daniel für mobile Version_2.0.svg`).
- **Icons:** Telefon + LinkedIn aus `EMP_15…`/`EMP_14…` (Outline, `currentColor`).
- Quell-Materialien (PDF-Mockup, Design-Manual, DOCX, Original-SVGs, Referenz-JPEGs)
  liegen im Projekt-Root und sind mitversioniert.

## 7. Besondere technische Lösungen (falls jemand ranmuss)

- **Logo-Laufband** (`.marquee`): **natives horizontales Scrollen** (`overflow-x`),
  Auto-Lauf per JS über `scrollLeft`, zwei identische Logo-Kopien → nahtloser Wrap um
  genau eine Kopie. Auf **Touch/iPad** von Haus aus swipe-/verschiebbar, auf **Desktop**
  zusätzlich Maus-Klick-Drag. Rand-Fade über **Gradient-Overlays** (nicht `mask-image`).
  → Wichtig: Diese Umsetzung war nötig, weil unter iOS Safari ein JS-`transform`
  innerhalb einer `mask-image`-Fläche nicht zuverlässig repaintet (fror ein) und
  `loading="lazy"` an den Logos die `max-content`-Breite verfälschte. **Logos daher
  eager laden.** Unter `640px` wird die Leiste zum **statischen Icon-Raster** (3/Reihe).
- **Logo → Startseite:** `.brand`-Klick scrollt per JS nach ganz oben. (Ein `#top`-Anker
  auf dem `position: sticky`-Header funktioniert nicht, weil das Element ohnehin oben klebt.)
- **Popups:** ein einziges Modal-Markup, Inhalt wird aus `MODALS` in `script.js` befüllt.
- **Sektions-Overflow:** `.leistungen { overflow: visible }`, damit der Kreis ins Modul
  darüber hineinläuft; die schwarze Stats-Section darunter deckt den Überlauf ab,
  `body { overflow-x: hidden }` verhindert horizontales Scrollen.

## 8. Responsive / Breakpoints

- `> 900px` – Desktop (Full-Nav, mehrspaltig).
- `≤ 900px` – „Mobile"-Layout (Hamburger, einspaltig, u. a. die schwarze Daniel-Karte
  ersetzt den Desktop-Kontaktbereich).
- `≤ 640px` – zusätzlich: Logo-Leiste wird statisches Raster (Phones). iPads/Tablets
  (641–900+) behalten das laufende Laufband.

## 9. Offene Punkte / TODO

1. **Impressum & Datenschutz** im Footer sind noch `href="#"` (Platzhalter) – echte
   Seiten/Links eintragen (`site/index.html`, Zeile ~264). Rechtlich vor „richtigem"
   Livegang nötig.
2. **LinkedIn** des Buttons/Badges zeigt auf `https://www.linkedin.com/in/daniel-stroebel/`
   – vom Kunden final bestätigen lassen.
3. Optional **Repo verschlanken:** die großen Quell-SVGs (2× ~7,6 MB Daniel-SVG) und
   WhatsApp-Referenz-JPEGs sind mitversioniert. Wenn das Repo schlank sein soll, können
   diese aus der Versionierung genommen werden (die ausgelieferte WebP bleibt).
4. **Favicon** ist aktuell ein Inline-SVG (Forward-Icon) – bei Bedarf durch das
   echte empiria-Favicon ersetzen.
5. Analytics/Tracking, `sitemap.xml`, echte Meta-/OG-Tags sind noch nicht gesetzt.

---

Fragen zur Umsetzung? Der komplette Verlauf steckt in der Git-History (aussagekräftige
Commits pro Änderung).
