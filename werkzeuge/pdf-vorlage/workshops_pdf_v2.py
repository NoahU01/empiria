#!/usr/bin/env python3
"""Workshops-PDF, ueberarbeitete Fassung (Muster fuer alle weiteren PDFs).

Aenderungen gegenueber v1:
- 6 statt 3 Seiten: jeder Workshop bekommt eine eigene Seite mit "worum geht es",
  "fuer wen", Ablauf/Inhalt und Preis - statt drei Zeilen Text plus Preiskasten.
- Uebersichtstabelle auf Seite 2: Entscheider sehen Formate, Dauer und
  Investition auf einen Blick, bevor es in die Tiefe geht.
- Mehr Weissraum und Sektionsrhythmus (heller/dunkler Block) wie auf der Homepage.
- Kontakt bekommt eine eigene Seite statt ans Ende der Preisseite gequetscht zu werden.

Inhalte stammen aus den Produktseiten (site/ki-zum-anfassen.html,
site/sprint-landingpage.html, site/workshop-moderation.html); die verbindende
Rahmen-Copy ist neu und von Daniel zu pruefen.
"""
import sys, os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from pdf_vorlage import build, icon, head, FOOTER, CSS
import pdf_vorlage
from pdf_bausteine import CSS_EXTRA, band, who, steps, price_row, overview

theme = sys.argv[1] if len(sys.argv) > 1 else "magenta"
pdf_vorlage.CSS = CSS + CSS_EXTRA

SKETCH = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), "ws-sketch.svg")).read()
NOTE = ("Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen. "
        "Vorbereitung und Dokumentation der Ergebnisse sind enthalten.")

# ---------------------------------------------------------------- Seite 1: Cover
p1 = f'''<section class="page cover">
  <img src="assets/empiria-logo.svg" alt="empiria" style="height:10mm">
  <p class="kicker">Workshops</p>
  <h1>Workshops, <span class="hl">die wirken.</span><br>Nicht nur Theorie.</h1>
  <p class="sub">Formate aus unzähligen Projekten, die Du direkt buchen kannst – mit echten Tools, echten Ergebnissen und einer Moderation, die Dein Team ans Ziel bringt.</p>
  <div class="sketch">{SKETCH}</div>
  <div class="facts" style="grid-template-columns:repeat(3,1fr)">
    <div><span class="label">Format 01</span><b>KI zum Anfassen</b></div>
    <div><span class="label">Format 02</span><b>Sprint Landingpage</b></div>
    <div><span class="label">Format 03</span><b>Moderation Deines Workshops</b></div>
  </div>
</section>'''

# ------------------------------------------------- Seite 2: Ansatz + Überblick
p2 = f'''<section class="page">
  {head(2, 6)}
  <p class="kicker">Unser Ansatz</p>
  <h2>Workshops, die nicht bei der Theorie bleiben.</h2>
  <p class="lead">Wir gehen direkt in die Anwendung – mit echten Tools, echten Ergebnissen und einer Moderation, die trägt. Jeder Workshop ist auf einen konkreten Anwendungsfall aus Deinem Haus zugeschnitten.</p>
  <div class="cards" style="grid-template-columns:repeat(3,1fr);margin-top:6mm">
    <div class="card"><div class="ic">{icon("tool")}</div><h3>Direkt anwendbar</h3><p>Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag.</p></div>
    <div class="card"><div class="ic">{icon("team")}</div><h3>Auf Dein Team zugeschnitten</h3><p>Jeder Workshop passt zu Deinem Anwendungsfall und Deinem Team – nicht von der Stange.</p></div>
    <div class="card"><div class="ic">{icon("target")}</div><h3>Professionell moderiert</h3><p>Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.</p></div>
  </div>

  <div style="margin-top:9mm">
    <p class="kicker">Drei Formate im Überblick</p>
    <h2>Wähle die Tiefe, die zu Deinem Vorhaben passt.</h2>
  </div>
  {overview([
    ("KI zum Anfassen", "KI-Tools an echten Fällen aus der Versicherungsbranche erproben", "½ – 2 Tage", "ab 2.500 €"),
    ("Sprint Landingpage", "In 48 Stunden zur fokussierten, live geschalteten Landingpage", "2 Tage + Onboarding", "15.850 €"),
    ("Moderation Deines Workshops", "Dein Thema, souverän moderiert – von Strukturen bis Kreativformat", "nach Thema", "individuell"),
  ])}
  <p class="pagenote">{NOTE}</p>
</section>'''

# ------------------------------------------- Seite 3: Format 01 – KI zum Anfassen
p3 = f'''<section class="page fmt">
  {head(3, 6)}
  <div class="fmt-head"><span class="fmt-no">Format 01</span><span class="fmt-meta">½ Tag · 1 Tag · 2 Tage</span></div>
  <h2>KI zum Anfassen.<br><span class="hl">Anwendung statt Vortrag.</span></h2>
  <p class="lead">Über KI wird viel geredet – oft von Menschen, die sie selbst noch nie genutzt haben. Wir gehen direkt in die Anwendung: mehrere Tools gleichzeitig, an Fällen, die für ein Versicherungsunternehmen wirklich relevant sind.</p>

  {who("Für wen das gemacht ist", [
    "Vorstände, die im Haus spürbar mehr Tempo bei neuen Ideen wollen",
    "Grundsatz- und Strategieabteilungen mit Recherche- und Analysebedarf",
    "Marketing und Kommunikation für schnellere Kampagnen und Inhalte",
    "Produktentwicklung, die KI als Sparringspartner testen will",
  ])}

  <div class="prices">
    {price_row("KI-Einstieg", "½ Tag", "KI-Tools ausprobieren und erste eigene Erfahrungen sammeln. Ohne Vorkenntnisse startklar.",
               ["Ausprobieren verschiedener KI-Tools", "Erste eigene Erfahrungen sammeln"], "2.500 €")}
    {price_row("KI-Sprint", "1 Tag", "Tools kennenlernen und eine kompakte Fragestellung aus Deinem Haus bearbeiten.",
               ["Kennenlernen verschiedener Tools", "Bearbeitung einer kompakten Fragestellung",
                "Abschlussbesprechung zum weiteren Vorgehen"], "3.900 €")}
    {price_row("KI-Deep-Dive", "2 Tage", "Direkter Einstieg in einen konkreten Usecase Eures Unternehmens.",
               ["Kennenlernen der Tools", "Bearbeitung eines konkreten Usecases",
                "Abschlussbesprechung zum weiteren Vorgehen"], "7.350 €")}
  </div>
  <p class="pagenote">{NOTE}</p>
</section>'''

# --------------------------------------- Seite 4: Format 02 – Sprint Landingpage
p4 = f'''<section class="page fmt">
  {head(4, 6)}
  <div class="fmt-head"><span class="fmt-no">Format 02</span><span class="fmt-meta">Onboarding · 2 Tage vor Ort · Review</span></div>
  <h2>Sprint Landingpage.<br><span class="hl">Live in 48 Stunden.</span></h2>
  <p class="lead">Eine Homepage ist oft ein Sammelsurium an Themen. Eine Landingpage funktioniert anders: eine klar definierte Zielgruppe, ein zentrales Problem, ein nächster Schritt. Genau das bauen wir im Sprint – sauber, mobil optimiert und technisch startklar.</p>

  {steps([
    ("Onboarding", "2–3 Std. · online", "Zielgruppe, Ziel und Rahmen werden geschärft, damit der Sprint sofort losgehen kann."),
    ("Sprint-Workshop", "2 Tage · Präsenz bei Dir vor Ort", "Sparring und parallele Entwicklung der Rohversion, danach Vorstellung, Feedback, Feinschliff und Go-live."),
    ("Review", "im Nachgang", "Kurzes Fazit: Hat alles gepasst, wie war das Feedback – und wo gibt es noch gezielten Anpassungsbedarf?"),
  ])}

  {who("Typische Anlässe", [
    "Eine Marktchance oder ein kurzfristiger Vertriebspush, etwa im Endjahresgeschäft",
    "Ein wichtiger Termin steht an – Messe, Event, Vertriebstagung",
    "Ergebnisse aus einem Kreativworkshop sollen direkt sichtbar weitergehen",
    "Der Beweis, dass es im Haus auch schnell und sauber geht",
  ])}

  <div class="prices">
    {price_row("Leistungspaket", "ein Paket, ein Preis",
               "Klar kalkuliert statt versteckter Zusatzkosten – durchgeführt von zwei Beraterinnen und Beratern von empiria.",
               ["Konzeption, Text &amp; Design Deiner vollständigen Landingpage",
                "Umsetzung im zweitägigen Sprint-Workshop bei Dir vor Ort",
                "Feedbackrunde &amp; Feinschliff direkt im Workshop",
                "Live-Schaltung im Anschluss an den Sprint",
                "Review im Nachgang, damit alles wie gewünscht läuft"], "15.850 €")}
  </div>
  <p class="pagenote">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe sowie zzgl. Spesen (Anfahrt und zwei Übernachtungen für je zwei Personen).</p>
</section>'''

# ------------------------------------------------- Seite 5: Format 03 – Moderation
p5 = f'''<section class="page fmt">
  {head(5, 6)}
  <div class="fmt-head"><span class="fmt-no">Format 03</span><span class="fmt-meta">Umfang nach Deinem Thema</span></div>
  <h2>Moderation Deines Workshops.<br><span class="hl">Souverän ans Ziel.</span></h2>
  <p class="lead">Wir aktivieren die Beteiligten gezielt, wechseln bewusst die Perspektive und stellen die richtigen Fragen. Egal ob Strukturen, Prozesse und Rollen oder Kreativworkshops und Vertriebsansätze – wir bringen Deinen Workshop sicher ans Ziel.</p>

  <div class="cards" style="grid-template-columns:repeat(3,1fr);margin-top:8mm">
    <div class="card"><h3>Klare Steuerung</h3><p>Energie und Zeit kommen dort an, wo sie etwas bringen – statt sich in Diskussionen zu verlieren.</p></div>
    <div class="card"><h3>Ergebnisse, die tragen</h3><p>Ergebnisse, mit denen Dein Team direkt weiterarbeiten kann – nicht nur ein Protokoll zum Ablegen.</p></div>
    <div class="card"><h3>Sichtbar festgehalten</h3><p>Top Visualisierungen und saubere Zusammenfassungen statt loser Enden.</p></div>
  </div>

  {who("Typische Anlässe aus der Praxis", [
    "Neustrukturierung mit neuen Rollen – bis hin zu geteilter Führungsverantwortung",
    "Eine Abteilung hat viele Themen gesammelt, aber keinen klaren Weg nach vorn",
    "Rollenklärung zwischen Führungskraft und neu geschaffener Stelle",
    "Führungswechsel, der mit einer Neustrukturierung zusammenfällt",
  ])}

  {band("Investition", "Umfang und Preis stimmen wir individuell ab.",
        "Weil Themenzuschnitt, Teilnehmerzahl und Vorbereitungsaufwand stark variieren, kalkulieren wir die Moderation nicht pauschal. Schildere uns Dein Thema – Du bekommst zeitnah ein konkretes, unverbindliches Angebot.")}
</section>'''

# ------------------------------------------------------------ Seite 6: Kontakt
p6 = f'''<section class="page">
  {head(6, 6)}
  <p class="kicker">Kontakt</p>
  <h2>Bereit für einen Workshop,<br><span class="hl">der Dich wirklich weiterbringt?</span></h2>
  <p class="lead" style="margin-top:4mm">Dein direkter Draht zu uns. Kurze Wege statt langer Abstimmungsrunden – schildere uns Dein Thema, wir melden uns zeitnah mit einem konkreten Vorschlag.</p>
  <div class="contact" style="position:static;margin-top:14mm">
    <div class="people">
      <div class="person"><img src="assets/ansprechpartner-daniel.webp" alt=""><div><b>Daniel Ströbel</b><span>Strategiehandwerker</span></div></div>
      <div class="person"><img src="assets/ansprechpartner-kerstin.webp" alt=""><div><b>Kerstin Christ</b><span>Expertin HR &amp; Weiterbildung</span></div></div>
      <div class="person"><img src="assets/ansprechpartner-noah.webp" alt=""><div><b>Noah Hermanns</b><span>Experte Performance Marketing</span></div></div>
    </div>
    <div class="direct" style="margin-top:9mm"><span><span class="label">E-Mail</span>daniel.stroebel@empiria.de</span><span><span class="label">Telefon</span>+49 176 3134 7217</span><span><span class="label">Web</span>www.empiria.de</span></div>
  </div>
  {FOOTER}
</section>'''

out = os.path.join(os.getcwd(), f"workshops-v2-{theme}.html")
open(out, "w", encoding="utf-8").write(
    build(theme, p1 + p2 + p3 + p4 + p5 + p6, "Workshops – empiria"))
print(out)
