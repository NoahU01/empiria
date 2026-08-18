# empiria – Website · Handoff

Stand: 2026-08-18

Marketing-One-Pager für **empiria** (Strategieberatung für Führungskräfte in der
Versicherungsbranche, GF Daniel Ströbel). 1:1 nachgebaut aus dem Kunden-Mockup
`00_Homepage empiria.pdf`, mit voll ausgearbeiteter Mobile-Variante.

---

## 1. Live & Repository

- **Repository:** https://github.com/NoahU01/empiria (Branch `main`)
- **Hosting:** Vercel (mit dem Repo verbunden → jeder Push auf `main` deployt automatisch)
- **Root-`vercel.json`** leitet alle Requests nach `site/` um (die Website liegt im
  Unterordner). Alternativ ginge in Vercel: *Settings → Root Directory = `site`*.
- **`main` = Produktion.** Nur was hier liegt, erscheint auf `www.empiria.de`.
  Jeder andere Branch bekommt eine eigene Vorschau — siehe Abschnitt 10.
- Root-`vercel.json` enthält außerdem **301-Weiterleitungen** für die Legal-URLs
  der WordPress-Vorgängerseite (`/impressum/`, `/datenschutz/`).
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
- **Legal-Seiten linksbündig zum Logo:** `.legal .container` behält die normale
  Container-Breite (linke Kante = Logo-Kante); begrenzt wird stattdessen die
  Textspalte über `max-width: calc(840px - 2 * var(--pad-x))`. Das `calc` ist
  Absicht: Es reproduziert exakt die Zeilenlänge der früheren zentrierten
  840px-Box, weil `--pad-x` fluid ist. Ein fester Wert würde die Zeilen bei
  mittleren Breiten unbemerkt verkürzen. **Nicht durch `max-width: 840px` am
  Container ersetzen** — dann rutscht der Text wieder ~200px nach rechts.
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

## 9. Tracking, Consent & SEO

Kanonische Domain ist **`https://www.empiria.de`** (Apex macht 308 → www). Alle
absoluten URLs (Sitemap, canonical, OG, JSON-LD) müssen die www-Variante nennen.

**Reihenfolge im `<head>` ist kritisch** und in allen drei HTML-Seiten identisch:

1. Inline: `gtag('consent','default', …)` – **alles `denied`**, `wait_for_update: 500`
2. Cookiebot `uc.js` (cbid `54835321-…`, `data-blockingmode="auto"`, `data-culture="de"`)
3. Google Tag `gtag.js` (GA4 **G-3VJ6JRK18C**) + `gtag('config', …)`,
   **gekapselt in eine Hostname-Prüfung** (s. u.)

Der Consent-Default muss **vor** dem CMP laufen, sonst überschreibt er dessen
Update. Die Google-Tags tragen `data-cookieconsent="ignore"` – ohne das würde
Cookiebots Auto-Blocking `gtag.js` komplett blockieren und Consent Mode könnte
gar nicht greifen (dann keine cookielosen Pings, keine Modellierung).

- `site/tracking.js` – zentraler Event-Helper (`window.gtag` mit dataLayer-Fallback,
  also GTM-kompatibel ohne Umbau) + Sektions-Tracking per IntersectionObserver.
  **Event-Namen sind das Vertragsstück Richtung GA4/Ads – nie umbenennen.**
  Katalog steht als Kommentar oben in der Datei.
- Footer hat auf allen Seiten einen **„Cookie-Einstellungen"**-Button
  (`[data-cookie-settings]` → `Cookiebot.renew()`), Pflicht für den Widerruf.
- `site/robots.txt` + `site/sitemap.xml` (3 URLs). KI-Crawler sind bewusst
  **nicht** geblockt (GPTBot, ClaudeBot, Google-Extended) – das ist der halbe
  „von KI gefunden werden"-Hebel.
- `site/assets/og-image.png` (1200×630) wird von `site/og.mjs` erzeugt
  (`python3 -m http.server 4599 &` … `node og.mjs`). Nur neu rendern, wenn sich
  Markenbild oder Claim ändern.
- **Favicon-Satz** (`favicon.svg`, `favicon.ico` mit 16/32/48 px, `apple-touch-icon.png`)
  wird von `site/favicon.mjs` erzeugt. Das Skript **liest die Pfade des Symbols
  `ic-forward` zur Laufzeit aus `index.html`** — nie von Hand kopieren, sonst
  laufen Icon und Seite auseinander. Es misst außerdem die echte Bounding-Box,
  weil das Symbol in seiner viewBox nicht zentriert sitzt (y ≈ 31–201); stures
  Übernehmen der viewBox versetzt den Pfeil sichtbar nach unten.
  Achtung: **Google cached Favicons in den SERPs wochenlang separat** — ein
  Wechsel schlägt dort erst mit Verzögerung durch.

**GA4 feuert ausschließlich auf der Produktions-Domain:**

```js
if (/^(www\.)?empiria\.de$/.test(location.hostname)) { gtag('config', 'G-…'); }
```

Ohne diese Sperre schicken **Vercel-Preview-Deployments und lokale Tests ihre
Klicks in dieselbe Property** und verfälschen die Zahlen — herausrechnen lässt
sich das hinterher nicht. `gtag.js` lädt weiterhin überall (harmlos, ohne
`config` gehen keine Hits raus); nur der `config`-Aufruf ist gebunden.
Verifiziert: localhost/Preview 0 Treffer an `/g/collect`, Produktion trackt normal.

### Indexierungs-Historie (damit niemand erschrickt)

Auf `empiria.de` lag vorher ein **WordPress einer anderen Firma**. Die Search
Console führt daher noch Alt-URLs (`/kompetenzen/`, `/zielgruppen/…`,
`/kontaktseite/`, `/uber-uns/` …). Die liefern alle **404 — das ist das korrekte
Signal** und löst sich von selbst; die Zahl der „indexierten Seiten" fiel seit
dem Livegang bereits von 15 auf 12 und läuft auf 3 zu.

Bewusst **nicht** umgeleitet wurden diese Altlasten: Eine Sammelumleitung
inhaltsfremder Seiten auf die Startseite wertet Google als **Soft-404**.
Ausnahme sind `/impressum/` und `/datenschutz/` — dort gibt es ein echtes
1:1-Äquivalent, deshalb 301 in der `vercel.json`.
Ebenfalls **nicht** benutzen: das „Entfernen"-Werkzeug der Search Console —
das blendet URLs nur 6 Monate aus, statt sie zu bereinigen.

**Localhost-Falle:** Der Cookiebot-Banner erscheint lokal **nicht**; in der
Konsole steht ein 404 auf `…/localhost/configuration.js`. Das ist erwartet
(`localhost` liegt nicht in der Cookiebot Domain Group) und harmlos – die
Banner-Verifikation muss gegen die Live-Domain laufen.

## 10. Zusammenarbeit & Branch-Workflow

**Grundprinzip:** Vercel baut aus *jedem* Push eine eigene, vollständige Kopie
der Website. Welche Adresse sie bekommt, hängt allein am Branch:

| Push auf | Vercel nennt es | Erreichbar unter |
|---|---|---|
| `main` | Production | `www.empiria.de` |
| jeder andere Branch | Preview | eigene `*.vercel.app`-Adresse |

`www.empiria.de` wird **ausschließlich** aus `main` gebaut. Arbeit auf einem
anderen Branch kann die Live-Seite technisch nicht anfassen.

- Mitarbeiter-Branch **`Daniel`** (großes D), Vorschau:
  `https://empiria-git-daniel-empiria-gmb-h.vercel.app`
  Die URL ist stabil und zeigt immer den neuesten Push auf diesen Branch. Sie
  **entsteht erst mit dem ersten Push** (davor 404). Wird der Branch umbenannt
  oder gelöscht, ändert sich die URL.
- **Vercel Deployment Protection ist für dieses Projekt abgeschaltet** (war
  „Standard Protection", die Previews hinter ein Vercel-Login stellt). Alle
  Deployment-URLs sind damit öffentlich erreichbar. Vertretbar, weil statische
  Seite ohne Secrets und `x-robots-tag: noindex` gesetzt bleibt — die URLs sind
  also unauffindbar, aber nicht geheim.
  Achtung: Der Toggle unter *Team → Deployment Protection → „Defaults for New
  Projects"* betrifft **nur künftige** Projekte. Die aktive Einstellung steht in
  der Projektzeile darunter bzw. unter *Projekt → Settings → Deployment Protection*.

**Zwei Dinge sind auf Previews absichtlich anders als live** (kein Bug):

1. **Kein Cookie-Banner** — die `*.vercel.app`-Domain steht nicht in der
   Cookiebot Domain Group (gleiche Falle wie localhost).
2. **Kein Tracking** — s. Hostname-Sperre in Abschnitt 9.

Beides lässt sich nur gegen die Live-Domain testen.

**Ablauf mit Pull Request:**

```
git checkout Daniel && git pull origin main   # erst main einholen
… arbeiten …
git push origin Daniel                        # -> Vercel baut die Preview neu
```
Dann auf GitHub den PR öffnen (macht, wer die Änderung gebaut hat) und den
Reviewer eintragen. Die **Vercel-GitHub-App kommentiert die Preview-URL in den
PR** — das ist dieselbe Integration, die Build-Status als Commit-Status meldet
(darüber wurde seinerzeit auch ein „Deployment was blocked" diagnostiziert).
Nach dem Merge auf `main` deployt Vercel automatisch nach Produktion.

> **Kein technischer Schutz auf `main`:** Branch-Schutzregeln gibt es bei
> privaten Repos im kostenlosen GitHub-Plan nicht. Mitarbeiter mit `write`
> könnten auch direkt auf `main` pushen — der PR-Weg ist eine Absprache, keine
> erzwungene Regel. Sicherheitsnetz ist `git revert`.

> **Commit-Autor muss eine gültige E-Mail sein.** Vercel blockt Deployments von
> Commits mit einer Adresse wie `user@Rechnername.local` („Deployment was
> blocked", kein Build-Fehler). Vor dem ersten Commit:
> `git config --global user.email "<GitHub-Adresse>"`.

## 11. Offene Punkte / TODO

**Erledigt seit dem Tracking-Setup:** Favicon (echtes Brand-Icon), Cookiebot-
Vorauswahl „Statistiken" abgeschaltet (live gegengeprüft), Search Console als
Domain-Property + Bing-Import, Sitemap eingereicht (Status „Erfolgreich",
3 Seiten erkannt), **GA4-Aufbewahrungsdauer auf 14 Monate** gesetzt (Ereignis-
und Nutzerdaten; die Zahl steht jetzt konkret in der Datenschutzerklärung),
**GA4-Schlüsselereignisse angelegt** (18.08.2026):
`kontakt_email_klick` und `kontakt_telefon_klick` — und nur diese beiden.
Bewusst *keine* Schlüsselereignisse sind `cta_kontakt`, `linkedin_klick`,
`popup_*` und `section_view_*`: In GA4 zählen alle Schlüsselereignisse in
dieselbe Conversion-Kennzahl, und dieselbe Liste wandert später nach Google
Ads. Weiche Signale mit aufzunehmen würde die Conversion-Rate aufblähen und
Ads auf Leute optimieren lassen, die nur einen Button geklickt haben.

1. **Datenschutzerklärung juristisch prüfen lassen.** Sie beschreibt aktuell
   Vercel-Hosting, Cookiebot und GA4 mit Consent Mode v2 — inhaltlich passend zu
   dem, was die Seite wirklich lädt. Bei jedem neuen Dienst nachziehen.
   Wir sind keine Anwälte.
2. **LinkedIn** des Buttons/Badges zeigt auf `https://www.linkedin.com/in/daniel-stroebel/`
   – vom Kunden final bestätigen lassen.
3. Optional **Repo verschlanken:** die großen Quell-SVGs (2× ~7,6 MB Daniel-SVG) und
   WhatsApp-Referenz-JPEGs sind mitversioniert. Wenn das Repo schlank sein soll, können
   diese aus der Versionierung genommen werden (die ausgelieferte WebP bleibt).
4. **Nicht gebaut: Reporting-Pipeline.** GA4 Data API + Search Console → monatlicher
   Markdown-Report (Conversions, Quellen, Modul-Scroll-Funnel aus den
   `section_view_*`-Events, GSC-Chancen-Keywords). Referenz-Implementierung liegt
   im AdMemory-Repo (`scripts/report.mjs`). Sinnvoll erst ab 2–4 Wochen Datenlage.
   Fallstricke: Google blockt Dienstkonto-Schlüssel → OAuth-Desktop-Client nötig,
   und die OAuth-App muss auf „In Produktion" veröffentlicht werden, sonst stirbt
   der Refresh-Token nach 7 Tagen.
5. Optional: **`llms.txt` / FAQPage-Schema** als KI-/SERP-Verstärker (ergänzt das
   bestehende JSON-LD `Organization`).

---

Fragen zur Umsetzung? Der komplette Verlauf steckt in der Git-History (aussagekräftige
Commits pro Änderung).
