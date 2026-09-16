# empiria.de – Mobile-Optimierung

**Stand:** 16. September 2026 · **Branch:** `Noah` (Vorschau: `https://empiria-git-noah-empiria-gmb-h.vercel.app`)
**Geprüft auf:** iPhone-Format 375 × 812 und 390 × 844, alle 16 Seiten aus dem Menü plus Impressum und Datenschutz.

Die Website ist auf dem Desktop fertig gestaltet; auf dem Smartphone wirkten viele Seiten
noch wie eine verkleinerte Desktop-Ansicht. Ziel dieser Runde: **Die Kernbotschaft steht
auf jeder Seite sofort im Bild, Texte und Bedienelemente sind auf Handy-Größe abgestimmt,
und jede Seite verhält sich gleich.** Der Desktop bleibt dabei unverändert.

---

## 1. Was wir umgesetzt haben

### Auf allen Seiten

| Thema | Vorher | Jetzt |
|---|---|---|
| **Überschrift sichtbar** | Auf den Produktseiten kam erst eine Grafik, die Überschrift begann erst nach 440–610 px (unterhalb des ersten Bildschirms) | Überschrift auf jeder Seite ab 126–172 px sichtbar, also im ersten Bildschirm |
| **Grafiken im Kopfbereich** | Skizzen mit 6–9 px kleinen Beschriftungen, auf dem Handy nicht lesbar | Auf dem Handy ausgeblendet. Ausnahmen: MES-Dashboard, Paid-Ads-Anzeigen und das Portrait auf 1:1 Sparring bleiben, stehen aber unter Text und Button |
| **Buttons** | 53 px hoch, wirkten sperrig; lange Beschriftungen brachen in zwei Zeilen | Einheitlich 44 px wie „konkrete Lösungen anzeigen" auf der Startseite |
| **Vorüberschriften (z. B. „Leistungen", „Ablauf")** | 18,4 px, so groß wie Fließtext | Eine Stufe kleiner (16 px), auf Desktop und Handy |
| **Fließtext** | In den Modulen 18 px, im Kopfbereich 16 px | Einheitlich 16 px |
| **Abstand Text → Button** im Kopfbereich | ~46 px | Halbiert |
| **Schlagwort-Pills** (z. B. „Live in 48 Stunden") | 12,5 px, relativ groß und viel Platz | Deutlich kompakter |
| **Akkordeons** (Zusammenarbeit, Beispiele, Anwendungsfälle, FAQ) | Hohe Boxen, Text 14,7 px | Flacher, Text eine Stufe kleiner |
| **Burger-Menü** | Unterpunkte unter „Leistungen" wirkten fetter und größer als die Hauptpunkte | Normale Schriftstärke, eine Stufe kleiner |
| **Preis-Karten** | Karten ohne „Meistgewählt"-Badge hatten oben eine große Leerfläche | Leerfläche entfällt, Hinweis „Alle Preise zzgl. …" eine Stufe kleiner |
| **Popups** | Titel lief unter den Schließen-Button | Schließen-Button kompakter, Titel hat Platz |

### Kacheln, die direkt zur Unterseite springen

„Weitere Leistungen" (Leistungsseiten) und die Medien-Kacheln PowerPoint / Landingpage /
Roll-up (Komplexe Themen) öffneten beim Antippen sofort die Unterseite. Auf dem Desktop
zeigt erst das Überfahren mit der Maus die Beschreibung, dieses Überfahren gibt es auf dem
Handy nicht. **Jetzt:** Erster Tipp öffnet die Beschreibung mit „mehr erfahren", erst der
zweite Tipp führt zur Unterseite. Die Medien-Kacheln stehen außerdem zu dritt nebeneinander
statt untereinander.

### Einzelne Seiten

- **Startseite:** Kopfbereich 15 px höher. Kontakt-Modul: Abstand Text → Buttons halbiert und
  exakt gleich dem Abstand Buttons → Kundenlogos (je 22 px). Kundenlogos im Kontakt-Modul
  waren links abgeschnitten, jetzt vollständig.
- **Leistungsseiten (Strategie, Komplexe Themen, Innovation):** Überschrift linksbündig statt
  rechtsbündig. „Zwischenergebnis" als normale Vorüberschrift statt fett und groß.
- **KI zum Anfassen, Sprint Landingpage, Moderation, Medien, Training & Sparring,
  Präsentationsseminar, Workshops, Marketing:** Grafik im Kopf ausgeblendet, Regeln von oben.
- **Sprint Landingpage:** Popup „Aufbau der Landingpage" zeigt die Skizze jetzt groß auf das
  Telefon zugeschnitten (vorher ~95 px breit), das Popup scrollt.
- **MES (Dashboard digitales Marketing):** Text und Button zuerst, dann das Dashboard-Mockup;
  Pills nebeneinander statt untereinander.
- **sofort sichtbar:** Vergleichsgrafik „Klassische Agentur vs. sofort sichtbar" sieht jetzt aus
  wie auf dem Desktop (Beschriftung, Ablauf in einer Reihe, Rakete rechts), nur verkleinert.
  Schrittnummern in den Ablauf-Boxen größer.
- **1:1 Sparring:** Portrait von Daniel bleibt, steht kompakt unter Text und Button.
- **Paid Ads (Desktop und Handy):** Kanalnamen in der Überschrift in den Markenfarben von
  Google, Meta und LinkedIn, Wechsel von Anzeigen und Kanalnamen schneller (2,6 s).

---

## 2. Was noch offen ist

### Braucht Inhalte oder eine Entscheidung von empiria

| Nr. | Thema | Was fehlt |
|---|---|---|
| 1 | **Lead-Magnet auf den drei Leistungsseiten** (Strategie, Komplexe Themen, Innovation) | Dort steht noch „Platzhalter für Leadmagnet … Lorem ipsum herunterladen". Inhalt, Titel und Datei (z. B. PDF) fehlen. Vorschlag: pro Seite ein kurzes Arbeitsblatt, das zum Thema passt. |
| 2 | **Erklärvideos** auf denselben drei Seiten | Platzhalter „Erklärvideo folgt". Videos oder Entscheidung, den Block bis dahin auszublenden. |
| 3 | **MES-Kreislauf-Grafik** (Dashboard-Seite) | Beschriftungen sind auf dem Handy zu klein. Braucht eine Mobil-Variante der Grafik mit größeren Labels (oder ohne Labels, Erklärung als Text darunter). |
| 4 | **Rolle von Kerstin Christ** | Auf Paid Ads und Medien „Expertin Content & Sichtbarkeit", auf Workshops und Präsentationsseminar „Expertin HR & Weiterbildung". Gewollt oder vereinheitlichen? |
| 5 | **Kontakt-Vorüberschrift auf der Startseite in Gold** | Alle anderen Vorüberschriften sind grau. Beibehalten oder angleichen? |
| 6 | **Potentialcheck (Paid Ads)** | Das Formular ist fertig, das Backend, das die Anfrage per E-Mail zustellt, folgt als nächster Schritt. Bis dahin erscheint beim Absenden ein Hinweis mit Mail-Adresse. |

### Für eine spätere Runde vorgemerkt

- **Seitenlänge:** MES-Seite ~9.700 px, sofort sichtbar ~8.900 px, Komplexe Themen ~8.900 px
  (11–12 Bildschirmhöhen). Die Startseite zeigt das Kundenlogo-Raster zweimal. Kürzen wäre
  eine inhaltliche Entscheidung.
- **Startseite, Lösung-Überschrift:** Die senkrechte gelbe Pille hinter „in Wirkung" erzeugt auf
  dem Handy eine große Lücke zwischen den Zeilen. Auf dem Desktop gewollt, mobil eine Frage.
- **Bilder ohne feste Maße:** Kundenlogos und einige Grafiken haben keine width/height-Angabe,
  dadurch springt das Layout beim Laden leicht (wirkt sich auf den Google-PageSpeed-Wert aus).
  Reine Technik, keine sichtbare Änderung.
- **Fußzeilen-Links** (Impressum, Datenschutz, Cookie-Einstellungen) sind 24 px hoch; Apple und
  Google empfehlen 44–48 px für Tipp-Ziele.

---

## 3. So prüfen Sie den Stand

Vorschau-Adresse: `https://empiria-git-noah-empiria-gmb-h.vercel.app` (jede Unterseite wie
gewohnt, z. B. `/paid-ads`, `/ki-zum-anfassen`). Die Vorschau zeigt bewusst keinen
Cookie-Banner und sendet keine Tracking-Daten. Änderungen am Live-Auftritt `www.empiria.de`
erfolgen erst nach Ihrer Freigabe.
