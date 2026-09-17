"""empiria PDF-Zusammenfassungen – Bausteine (hell, eine Akzentfarbe je Seite)."""
import html as _h

THEMES = {
  "magenta":   dict(acc="#C51F5D", acc2="#7a1339", hl_bg="#C51F5D", hl_fg="#fff", tint="#fbeef3"),
  "cyan":      dict(acc="#0B9FBD", acc2="#086a80", hl_bg="#0B9FBD", hl_fg="#fff", tint="#e9f6f9"),
  "violet":    dict(acc="#8613A1", acc2="#5c0d70", hl_bg="#8613A1", hl_fg="#fff", tint="#f5ecf7"),
  # Lime ist die Highlight-Farbe aus dem Corporate Design (wie auf der Website:
  # #A3E635 mit dunkler Schrift, Verlauf nach #6b9422). Das fruehere #4d7c0f als
  # Flaechenfarbe wirkte zu dunkel/waldig.
  "green":     dict(acc="#6b9422", acc2="#4d7c0f", hl_bg="#A3E635", hl_fg="#1c2b0e", tint="#f0f5e9",
                    feat_bg="linear-gradient(150deg, #A3E635 0%, #6b9422 100%)", feat_fg="#1c2b0e"),
  "emerald":   dict(acc="#059669", acc2="#037a54", hl_bg="#059669", hl_fg="#fff", tint="#e8f6f1"),
  "capiamo":   dict(acc="#063755", acc2="#04263b", hl_bg="#063755", hl_fg="#fff", tint="#eaf0f4"),
  "strategie": dict(acc="#1a1817", acc2="#2e2d2c", hl_bg="#fff400", hl_fg="#1a1817", tint="#f3f2ef",
                    feat_bg="#fff400", feat_fg="#1a1817", num="#1a1817"),
}

ICONS = {
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "team": '<circle cx="9" cy="8" r="3.2"/><path d="M3 19c.6-3.4 3-5.2 6-5.2s5.4 1.8 6 5.2"/><circle cx="17" cy="9" r="2.4"/><path d="M16 13.9c2.6.2 4.4 1.8 5 4.6"/>',
 "user": '<circle cx="12" cy="8" r="3.6"/><path d="M4.5 20c.8-4 3.7-6.2 7.5-6.2s6.7 2.2 7.5 6.2"/>',
 "tool": '<path d="M4 20l7-7"/><path d="M14.5 3.5a4.5 4.5 0 0 0-3.9 6.7L4 16.8 7.2 20l6.6-6.6a4.5 4.5 0 0 0 6.7-3.9l-2.8 2.8-3.2-.9-.9-3.2z"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4.2"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
 "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.8 7l8.2 6 8.2-6"/>',
 "clock": '<circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/>',
 "bolt": '<path d="M13 3L5.5 13.5H12L11 21l7.5-10.5H12z"/>',
 "chart": '<path d="M4 20V4"/><path d="M4 20h16"/><rect x="7.5" y="12" width="3" height="5" rx=".6"/><rect x="12.5" y="8.5" width="3" height="8.5" rx=".6"/><path d="M18 6v11"/>',
 "trend": '<path d="M3.5 17l5.5-5.5 4 4 7.5-7.5"/><path d="M15 8h5.5v5.5"/>',
 "chat": '<path d="M4 5.5h16a1 1 0 0 1 1 1V15a1 1 0 0 1-1 1h-9l-4.5 3.5V16H4a1 1 0 0 1-1-1V6.5a1 1 0 0 1 1-1z"/><path d="M7.5 9.5h9M7.5 12.5h5.5"/>',
 "chats": '<path d="M3.5 4.5h11a1 1 0 0 1 1 1v6.5a1 1 0 0 1-1 1H9l-3.5 3v-3h-2a1 1 0 0 1-1-1V5.5a1 1 0 0 1 1-1z"/><path d="M18 9h2.5a1 1 0 0 1 1 1v6.5a1 1 0 0 1-1 1h-1.5v3l-3.5-3H11a1 1 0 0 1-1-1V16"/>',
 "layers": '<path d="M12 3.5l8.5 4.5L12 12.5 3.5 8z"/><path d="M3.5 12L12 16.5 20.5 12"/><path d="M3.5 16L12 20.5 20.5 16"/>',
 "lock": '<rect x="5" y="10.5" width="14" height="10" rx="2"/><path d="M8 10.5V7.5a4 4 0 0 1 8 0v3"/>',
 "eye": '<path d="M2.5 12S6 5.5 12 5.5 21.5 12 21.5 12 18 18.5 12 18.5 2.5 12 2.5 12z"/><circle cx="12" cy="12" r="3"/>',
 "compass": '<circle cx="12" cy="12" r="8.5"/><path d="M15.5 8.5l-2 5-5 2 2-5z"/>',
 "flag": '<path d="M5 21V4"/><path d="M5 4.5h12l-2.5 4 2.5 4H5"/>',
 "route": '<circle cx="6" cy="18" r="2.2"/><circle cx="18" cy="6" r="2.2"/><path d="M8.2 18H15a3 3 0 0 0 0-6H9a3 3 0 0 1 0-6h6.8"/>',
 "doc": '<path d="M6.5 3h8l4 4v14h-12z"/><path d="M14.5 3v4h4"/><path d="M9 12h6M9 15.5h6"/>',
 "slides": '<rect x="3" y="4" width="18" height="12" rx="1.5"/><path d="M12 16v4M8 20.5h8"/><path d="M7 12l3-3 2.5 2 4-4"/>',
 "browser": '<rect x="3" y="4.5" width="18" height="15" rx="2"/><path d="M3 8.5h18"/><circle cx="6" cy="6.5" r=".6" fill="currentColor"/><circle cx="8" cy="6.5" r=".6" fill="currentColor"/><path d="M7 13h10M7 16h6"/>',
 "rollup": '<rect x="7" y="3" width="10" height="15" rx="1"/><path d="M5.5 20.5h13"/><path d="M12 18v2.5"/><path d="M9.5 7h5M9.5 10h5M9.5 13h3"/>',
 "mic": '<rect x="9" y="3" width="6" height="11" rx="3"/><path d="M5.5 11a6.5 6.5 0 0 0 13 0"/><path d="M12 17.5V21"/>',
 "spark": '<path d="M12 3v4M12 17v4M3 12h4M17 12h4M5.6 5.6l2.8 2.8M15.6 15.6l2.8 2.8M5.6 18.4l2.8-2.8M15.6 8.4l2.8-2.8"/>',
 "puzzle": '<path d="M5 8h3.2a2 2 0 1 1 3.6 0H15v3.2a2 2 0 1 1 0 3.6V18h-3.2a2 2 0 1 0-3.6 0H5v-3.2a2 2 0 1 0 0-3.6z"/>',
 "cycle": '<path d="M19.5 12a7.5 7.5 0 0 1-13 5.1"/><path d="M4.5 12a7.5 7.5 0 0 1 13-5.1"/><path d="M17.5 3v4h-4"/><path d="M6.5 21v-4h4"/>',
 "shield": '<path d="M12 3l7.5 3v5.5c0 4.5-3.2 8.2-7.5 9.5-4.3-1.3-7.5-5-7.5-9.5V6z"/><path d="M8.5 12l2.5 2.5 4.5-5"/>',
 "search": '<circle cx="10.5" cy="10.5" r="6"/><path d="M15 15l5.5 5.5"/>',
 "phone": '<rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M11 18.5h2"/>',
 "grid": '<rect x="4" y="4" width="7" height="7" rx="1"/><rect x="13" y="4" width="7" height="7" rx="1"/><rect x="4" y="13" width="7" height="7" rx="1"/><rect x="13" y="13" width="7" height="7" rx="1"/>',
 "bulb": '<path d="M9 17.5h6M10 20.5h4"/><path d="M12 3.5a6 6 0 0 0-3.5 10.9c.6.5 1 1.2 1 2V17h5v-.6c0-.8.4-1.5 1-2A6 6 0 0 0 12 3.5z"/>',
 "handshake": '<path d="M2.5 11.5l4-4 3.5 1.5 2-1 5.5 0 4 4"/><path d="M6.5 7.5v6l5 4.5c.8.7 2 .6 2.6-.2l3.4-4.3"/><path d="M11 13.5l2 2M13 11.5l2.5 2.5"/>',
 "megaphone": '<path d="M3.5 10v4h3l7.5 4.5v-13L6.5 10z"/><path d="M17.5 9a4 4 0 0 1 0 6"/><path d="M6.5 14l1.5 5.5h2.5L9.5 14"/>',
 "arrow": '<path d="M4 12h15"/><path d="M13.5 6.5L19 12l-5.5 5.5"/>',
 "star": '<path d="M12 3.5l2.6 5.3 5.9.9-4.3 4.1 1 5.8L12 16.9l-5.2 2.7 1-5.8-4.3-4.1 5.9-.9z"/>',
 "euro": '<path d="M17.5 6.5A7 7 0 1 0 17.5 17.5"/><path d="M4 10.5h9M4 13.5h9"/>',
 "rocket": '<path d="M12 3c3 2.4 4.2 6 4.2 9.6 0 2.4-1.2 4.8-4.2 6.6-3-1.8-4.2-4.2-4.2-6.6C7.8 9 9 5.4 12 3z"/><circle cx="12" cy="10.2" r="1.8"/><path d="M7.8 14.4L5.4 18.6"/><path d="M16.2 14.4l2.4 4.2"/><path d="M10.2 19.2c0 1.8.9 3 1.8 3.6.9-.6 1.8-1.8 1.8-3.6"/>',
}
def icon(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

CSS = r"""
@page { size: A4; margin: 0; }
:root { --ink:#1a1817; --ink2:#2e2d2c; --g70:#58564f; --g50:#8a8783; --g30:#cfcac4; --bg:#f2f1ef;
        --serif:"Lora",Georgia,serif; --sans:"Poppins",sans-serif;
        /* Die Skizzen stammen 1:1 von der Website und referenzieren dort
           var(--font-sans)/var(--font-serif). Ohne diese Aliase fallen alle
           SVG-Beschriftungen auf die Browser-Standardschrift zurueck. */
        --font-sans:"Poppins",sans-serif; --font-serif:"Lora",Georgia,serif; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--sans); color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
b, strong { font-weight: 600; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; padding: 20mm 22mm 18mm; background: #fff; }
.page:last-child { page-break-after: auto; }
.hl { position: relative; z-index: 0; display: inline; color: var(--hl-fg); font-weight: 700; -webkit-box-decoration-break: clone; box-decoration-break: clone; background: var(--hl-bg); border-radius: 4px; padding: 0 .08em; white-space: nowrap; }
.head { display:flex; justify-content: space-between; align-items:center; margin-bottom: 15mm; }
.head img { height: 6mm; }
.page-no { font-size: 8pt; color: var(--g50); font-weight: 500; }
.kicker { font-weight: 500; font-size: 10.5pt; color: var(--acc); margin: 0 0 2mm; }
h1 { font-family: var(--serif); font-weight: 700; font-size: 40pt; line-height: 1.12; letter-spacing: -.01em; }
h2 { font-family: var(--serif); font-weight: 700; font-size: 22pt; line-height: 1.22; margin: 0 0 4.5mm; max-width: 158mm; }
h3 { font-family: var(--serif); font-weight: 700; font-size: 12pt; line-height: 1.28; }
p.lead { font-size: 10pt; line-height: 1.72; color: var(--ink2); max-width: 152mm; }
p.lead + p.lead { margin-top: 2.6mm; }
.label { font-size: 6.6pt; letter-spacing: .12em; text-transform: uppercase; color: var(--g50); font-weight: 600; }
.sec + .sec { margin-top: 12mm; }
.gap { height: 10mm; }
/* Deckblatt */
.cover .logo { height: 10mm; }
.cover .kicker { margin-top: 24mm; }
.cover h1 { margin: 2mm 0 7mm; max-width: 166mm; }
.cover .sub { font-size: 11.5pt; line-height: 1.62; color: var(--g70); max-width: 146mm; }
.cover .sub + .sub { margin-top: 2.5mm; }
.cover .sketch { position: absolute; left: 22mm; right: 22mm; bottom: 46mm; height: 78mm; display: flex; justify-content: center; align-items: flex-end; }
.cover .sketch svg { height: 100%; width: auto; max-width: 100%; filter: invert(1) contrast(1.5); }
.cover .sketch.noinv svg { filter: none; }
.cover .facts { position: absolute; left: 22mm; right: 22mm; bottom: 20mm; display: grid; gap: 7mm; }
.cover .facts b { display:block; font-family: var(--serif); font-weight: 700; font-size: 11pt; line-height: 1.3; margin-top: 1.5mm; }
.cover .brandlogo { height: 4.5mm; margin-top: 24mm; display:block; }  /* Kicker-Groesse, nicht Headline */
.cover .brandlogo + .kicker { margin-top: 6mm; }
.cover .brandlogo + h1 { margin-top: 7mm; }
.inline-sketch { display:flex; justify-content:center; margin-top: 12mm; height: 62mm; }
/* Hochformatige Skizzen (z. B. Strategiemodell 900x1060) brauchen mehr Hoehe,
   sonst werden sie unleserlich schmal. */
.inline-sketch--hoch { height: 150mm; margin-top: 8mm; }
/* Browser-Mockup neben dem Text statt ueber die volle Seitenbreite. */
.bm--schmal { margin-top: 0; }
.bm--schmal .bm-row { grid-template-columns: 8mm 1fr 6mm; padding: 2.4mm 3.5mm; }
.bm--schmal .bm-row span { font-size: 8.4pt; }
.medien-zwei { display: grid; grid-template-columns: 1fr 88mm; gap: 8mm; align-items: start; margin-top: 7mm; }
.inline-sketch svg { height:100%; width:auto; filter: invert(1) contrast(1.5); }

/* ---- Modellkasten ----------------------------------------------------------
   Die Skizzen der Website sind fuer dunklen Grund gezeichnet (weisse Linien,
   Akzent #fff400). Auf weissem Papier musste bisher `filter: invert(1)` helfen
   - das macht aus dem Gelb ein grelles Blau und aus den Kaesten graue Flecken.
   Stattdessen bekommen sie hier ihre native Umgebung: schwarzer Kasten, weisse
   Zeichnung, gelbe Highlights - exakt wie im Pop-up auf der Website. */
.mdl { background:#0f0e0d; border-radius:4mm; padding:7mm; margin-top:7mm; color:#fff;
       display:grid; grid-template-columns: var(--figw,68mm) 1fr; gap:8mm; align-items:center; }
.mdl--breit { grid-template-columns:1fr; }
.mdl-fig svg { display:block; width:100%; height:auto; filter:none; }
.mdl-txt .kicker { color:#fff400; font-size:9pt; margin:0 0 1.6mm; }
.mdl-txt h3 { color:#fff; font-size:13pt; line-height:1.28; margin-bottom:3mm; }
.mdl-txt p { font-size:8.8pt; line-height:1.62; color:rgba(255,255,255,.74); }
.mdl-txt p + p { margin-top:2.6mm; }
.mdl-txt p b { color:#fff; font-weight:600; }
.mdl-steps { margin-top:4mm; display:grid; gap:2.6mm; }
.mdl-step { display:grid; grid-template-columns:5.5mm 1fr; gap:2.5mm; align-items:baseline; }
.mdl-step i { font-style:normal; font-family:var(--serif); font-weight:700; font-size:9.5pt; color:#fff400; }
.mdl-step span { font-size:8.6pt; line-height:1.55; color:rgba(255,255,255,.78); }
.mdl-step span b { color:#fff; font-weight:600; display:block; margin-bottom:.4mm; }

/* ---- Sektion im Landingpage-Look ------------------------------------------
   Heller Grund ueber die volle Seitenbreite, ein grosses Icon als Wasserzeichen
   und darauf der schwarze Kasten - dieselbe Schichtung wie auf den Landingpages. */
.stage { position:relative; margin:9mm -22mm 0; padding:8mm 22mm 9mm; background:var(--bg); overflow:hidden; }
.stage > * { position:relative; z-index:1; }
.stage-wm { position:absolute; z-index:0; right:-18mm; bottom:-24mm; width:98mm; height:98mm;
            color:var(--ink); opacity:.055; }
.stage-wm svg { width:100%; height:100%; stroke-width:.9; }
.stage-head h2 { font-size:19pt; margin-bottom:3mm; }
.stage-head p { font-size:9.4pt; line-height:1.66; color:var(--ink2); max-width:148mm; }
.stage .mdl, .stage .mocks-box { margin-top:6mm; }

/* ---- Ein Paket, ein Preis: Leistungen und Preis als EIN Block --------------
   Zwei getrennte Kaesten mit justify-content:space-between reissen den Preis
   vom Text weg und hinterlassen ein sichtbares Loch. Hier sitzen beide
   Haelften randlos in einem gemeinsamen Rahmen, der Preis mittig. */
.paket { display:grid; grid-template-columns:1fr 60mm; margin-top:6mm;
         border-radius:4mm; overflow:hidden; border:0.7pt solid var(--g30); }
.paket-l { background:var(--bg); padding:6mm; }
.paket-l .kicker { font-size:9pt; margin:0 0 3mm; }
.paket-l ul.checks li { font-size:9pt; padding:1.3mm 0 1.3mm 6.4mm; }
.paket-r { background:var(--feat-bg); color:var(--feat-fg); padding:6mm;
           display:flex; flex-direction:column; justify-content:center; }
.paket-r .kicker { color:var(--feat-fg); opacity:.85; font-size:9pt; margin:0 0 2mm; }
.paket-r .price { font-family:var(--serif); font-weight:700; font-size:25pt; line-height:1.05; }
.paket-r p { font-size:8.6pt; line-height:1.55; margin-top:3.5mm; opacity:.95; }

/* ---- Durchgestrichene Denkmuster (inno-stein von der Landingpage) ----------
   Das staerkste Element der Innovationsseite: Saetze, die als gesetzt gelten,
   sichtbar durchgestrichen - und darunter die Gegenfrage. */
.stein { background:#0f0e0d; border-radius:4mm; padding:7mm; margin-top:7mm; color:#fff; }
.stein .tag { font-size:6.6pt; letter-spacing:.12em; text-transform:uppercase;
              color:rgba(255,255,255,.55); font-weight:600; }
.stein ul { list-style:none; margin:4.5mm 0 0; display:grid; gap:3mm; }
.stein li { font-family:var(--serif); font-weight:700; font-size:13.5pt; line-height:1.25;
            color:rgba(255,255,255,.40); text-decoration:line-through;
            text-decoration-color:#fff400; text-decoration-thickness:1.5pt; }
.stein .foot { margin-top:5.5mm; font-family:var(--serif); font-weight:700; font-size:15pt; color:#fff400; }

/* ---- Nummeriertes Raster (inno-einsatz-grid), erstes Feld hervorgehoben ---- */
.raster { display:grid; gap:3.5mm; margin-top:6mm; }
.raster > div { border:0.7pt solid var(--g30); border-radius:3mm; padding:4.5mm 4mm; background:#fff; }
.raster .num { display:block; font-family:var(--serif); font-weight:700; font-size:11pt;
               color:var(--acc); margin-bottom:2.5mm; }
.raster b { font-family:var(--serif); font-weight:700; font-size:9.6pt; line-height:1.3; display:block; }
.raster > div.main { background:var(--ink); color:#fff; border-color:var(--ink); }
.raster > div.main .num { color:#fff400; }

/* ---- Medien-Mockups nebeneinander (wie die Sketch-Reihe auf der Website) --- */
.mocks-box { background:#0f0e0d; border-radius:4mm; padding:7mm; color:#fff; }
/* align-items:start + feste Figurenhoehe, damit die Beschriftungen aller drei
   Mockups auf einer Linie sitzen - sonst richtet sich jede Spalte nach der
   Hoehe ihrer eigenen Skizze. */
.mocks { display:grid; grid-template-columns:repeat(3,1fr); gap:7mm; align-items:start; }
.mock-fig { height:52mm; display:flex; align-items:flex-end; justify-content:center; }
.mock-fig svg { max-height:100%; width:auto; max-width:100%; display:block; filter:none; }
.mock b { display:block; font-family:var(--serif); font-weight:700; font-size:11pt; color:#fff; margin:4.5mm 0 1.5mm; }
.mock p { font-size:8.2pt; line-height:1.55; color:rgba(255,255,255,.72); }
/* Kacheln */
.cards { display: grid; gap: 4.5mm; margin-top: 7mm; }
.card { border: 0.7pt solid #e6e2de; border-radius: 4mm; padding: 5.5mm 5mm; background: #fff; }
.card .ic { width: 7.5mm; height: 7.5mm; color: var(--acc); margin-bottom: 3.5mm; }
.card .ic svg { width: 100%; height: 100%; }
.card h3 { font-size: 11pt; margin-bottom: 1.8mm; }
.card p { font-size: 8.8pt; line-height: 1.58; color: var(--g70); }
.card .num { font-family: var(--serif); font-weight: 700; font-size: 11pt; color: var(--num); display:block; margin-bottom: 2.5mm; }
.card ul { margin-top: 2.5mm; }
/* nummerierte Zeilen */
.rows { margin-top: 5mm; }
.row { display: grid; grid-template-columns: 11mm 1fr; column-gap: 3mm; padding: 3mm 0; }
.row .n { font-family: var(--serif); font-weight: 700; font-size: 12pt; color: var(--num); line-height: 1.3; }
.row h3 { margin-bottom: 1.2mm; }
.row p { font-size: 9.2pt; line-height: 1.6; color: var(--g70); }
.row .extra { margin-top: 2.5mm; }
/* Stationen */
.stations { position: relative; margin-top: 6mm; }
.stations::before { content:""; position:absolute; left: 11pt; top: 16pt; bottom: 26pt; width: 0.7pt; background: var(--g30); }
.st { position: relative; padding-left: 36pt; margin-bottom: 6.5mm; }
.st:last-child { margin-bottom: 0; }
.st .n { position:absolute; left: 0; top: 0; width: 22pt; height: 22pt; border-radius: 50%; background:#fff; border: 0.9pt solid var(--acc); color: var(--num); font-family: var(--serif); font-weight:700; font-size: 9pt; display:flex; align-items:center; justify-content:center; }
.st small { display:block; font-size: 6.6pt; letter-spacing: .12em; text-transform: uppercase; color: var(--g50); font-weight: 600; }
.st > b { display:block; font-family: var(--serif); font-weight: 700; font-size: 12pt; margin: .6mm 0 1mm; }
.st p { font-size: 9.2pt; line-height: 1.6; color: var(--g70); }
/* Listen */
ul.dots { list-style: none; }
ul.dots li { position: relative; padding: 1.3mm 0 1.3mm 5mm; font-size: 9.4pt; line-height: 1.5; color: var(--ink2); }
ul.dots li::before { content:""; position:absolute; left: 0; top: 3.1mm; width: 1.6mm; height: 1.6mm; border-radius: 50%; background: var(--acc); }
ul.dots.sm li { font-size: 8.6pt; padding: .9mm 0 .9mm 4.2mm; }
ul.dots.sm li::before { top: 2.5mm; width: 1.4mm; height: 1.4mm; }
ul.dots.cols2 { display: grid; grid-template-columns: 1fr 1fr; column-gap: 10mm; }
ul.checks { list-style: none; }
ul.checks li { position: relative; padding: 1.6mm 0 1.6mm 7mm; font-size: 9.6pt; line-height: 1.5; color: var(--ink2); }
ul.checks li svg { position: absolute; left: 0; top: 1.9mm; width: 4.4mm; height: 4.4mm; color: var(--acc); }
ul.checks.cols2 { display: grid; grid-template-columns: 1fr 1fr; column-gap: 10mm; }
/* Aussage */
.statement { font-family: var(--sans); font-weight: 500; font-size: 12pt; line-height: 1.62; color: var(--ink); max-width: 152mm; }
.quotes { margin-top: 5mm; display: grid; gap: 2.2mm; }
.quotes span { display:block; font-weight: 500; font-size: 12pt; line-height: 1.4; color: var(--ink); padding-left: 5mm; position: relative; }
.quotes span::before { content:""; position:absolute; left:0; top: .25em; bottom: .25em; width: 1.2mm; border-radius: 1mm; background: var(--acc); }
/* Band (wichtigster Abschnitt) & Verlaufskasten */
.band { background: var(--bg); border-radius: 4mm; padding: 7mm 7mm; margin-top: 8mm; }
.band h3 { font-size: 14pt; margin-bottom: 2mm; }
.band p { font-size: 9.4pt; line-height: 1.65; color: var(--ink2); }
.band .kicker { font-size: 9.5pt; }
.feat { background: var(--feat-bg); color: var(--feat-fg); border-radius: 4mm; padding: 7mm 7mm; margin-top: 8mm; }
.feat .kicker { color: var(--feat-fg); opacity: .85; font-size: 9.5pt; }
.feat h3 { font-size: 15pt; line-height: 1.3; margin-bottom: 2mm; color: var(--feat-fg); }
.feat p { font-size: 9.4pt; line-height: 1.65; color: var(--feat-fg); opacity: .95; }
/* ---- Preiskarten: exakt die Reihenfolge der Website ----
   Badge, Name + Dauer, Beschreibung, PREIS, Unterschrift, Leistungen.
   Der Preis gehoert nach oben (direkt unter die Beschreibung), nicht an den
   unteren Rand - und die Unterschrift ("Kompakter Anwendungsfall") ist eine
   eigene Zeile zwischen Preis und Bullets, kein Listenpunkt. */
.opts { display: grid; gap: 4mm; margin-top: 7mm; align-items: stretch; }
.opt { background: var(--bg); border-radius: 3.5mm; padding: 4.5mm 4.5mm; display:flex; flex-direction: column; }
/* immer vorhanden, damit die Namen aller Karten auf einer Linie sitzen */
.opt .badgeslot { min-height: 5.4mm; margin-bottom: 1.5mm; }
.opt .badge { display:inline-block; font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase;
              font-weight: 600; padding: 1.1mm 2.6mm; border-radius: 10mm;
              background: var(--acc); color: #fff; }
.opt b { display:block; font-family: var(--serif); font-weight: 700; font-size: 12pt; }
.opt b .sub { font-family: var(--sans); font-weight: 500; font-size: 8pt; color: var(--g50); margin-left: 2mm; }
.opt small { display:block; font-size: 8.4pt; line-height: 1.5; color: var(--g70); margin: 1.2mm 0 0; min-height: 10mm; }
.opt .price { font-family: var(--serif); font-weight: 700; font-size: 17pt; color: var(--ink); display:block; }
.opt .price em { font-style: normal; font-family: var(--sans); font-weight: 500; font-size: 8pt; margin-left: 1mm; color: var(--g70); }
.opt .pnote { display:block; font-size: 8pt; font-weight: 500; color: var(--ink2); margin-top: 1.2mm; line-height: 1.4; }
.opt ul.dots { margin-top: 3.5mm; padding-top: 3.5mm; border-top: 0.7pt solid var(--g30); }
.opt ul.dots li { font-size: 8.3pt; padding: .8mm 0 .8mm 4mm; color: var(--ink2); }
.opt ul.dots li::before { top: 2.3mm; width: 1.3mm; height: 1.3mm; }
.opt--feat { background: var(--feat-bg); color: var(--feat-fg); }
.opt--feat small, .opt--feat .price, .opt--feat .price em, .opt--feat ul.dots li, .opt--feat .pnote,
.opt--feat b, .opt--feat b .sub { color: var(--feat-fg); }
.opt--feat .badge { background: #fff; color: var(--acc2); }
.opt--feat ul.dots { border-top-color: rgba(255,255,255,.34); }
.opt--feat ul.dots li::before { background: var(--feat-fg); }
.note { font-size: 7.4pt; color: var(--g50); margin-top: 3mm; line-height: 1.5; }
/* Fälle */
.cases { display: grid; grid-template-columns: 1fr 1fr; gap: 6mm 10mm; margin-top: 7mm; }
.case h3 { font-size: 10.8pt; margin-bottom: 1.5mm; }
.case p { font-size: 8.8pt; line-height: 1.58; color: var(--g70); }
.case .ic { width: 6mm; height: 6mm; color: var(--acc); margin-bottom: 2mm; }
.case .ic svg { width: 100%; height: 100%; }
/* Chips */
.chips { display:flex; flex-wrap: wrap; gap: 2.2mm; margin-top: 5mm; }
.chips span { font-size: 8.4pt; font-weight: 500; padding: 1.4mm 3.4mm; border-radius: 10mm; background: var(--tint); color: var(--ink2); }
/* Zweispalter */
.two { display: grid; grid-template-columns: 1fr 1fr; gap: 10mm; }
.two-6-4 { display: grid; grid-template-columns: 1.35fr 1fr; gap: 10mm; align-items: start; }
/* Kontakt */
.contact { position: absolute; left: 22mm; right: 22mm; bottom: 30mm; }
.contact h3 { font-family: var(--serif); font-weight: 700; font-size: 17pt; line-height: 1.22; margin: 0 0 7mm; max-width: 150mm; }
.contact .one { display: grid; grid-template-columns: 24mm 56mm 1fr; column-gap: 7mm; align-items: center; }
.contact .ph { width: 24mm; height: 24mm; border-radius: 50%; object-fit: cover; display: block; border: 0.6pt solid #d6d2cd; }
.contact .name { font-family: var(--serif); font-weight: 700; font-size: 12pt; margin: 0 0 1mm; }
.contact .role { font-size: 8.5pt; color: var(--g50); line-height: 1.5; }
.contact dl { display: grid; grid-template-columns: 15mm 1fr; row-gap: 2mm; padding-left: 6mm; border-left: 0.7pt solid var(--acc); }
.contact dt { font-size: 6.6pt; letter-spacing: .12em; text-transform: uppercase; color: var(--g50); font-weight: 600; align-self: center; }
.contact dd { font-size: 9.5pt; color: var(--ink); margin: 0; }
.contact .many .ppl { display: grid; column-gap: 6mm; }
.contact .dlrow { display: flex; gap: 9mm; margin-top: 6mm; padding-left: 4mm; border-left: 0.7pt solid var(--acc); }
.contact .dlrow > span { font-size: 9.5pt; color: var(--ink); }
.contact .dlrow .label { margin-right: 2.5mm; }
.contact .p { display: grid; grid-template-columns: 15mm 1fr; column-gap: 3.5mm; align-items: center; }
.contact .p img { width: 15mm; height: 15mm; border-radius: 50%; object-fit: cover; border: 0.6pt solid #d6d2cd; display:block; }
.contact .p .name { font-size: 10.5pt; margin: 0 0 .5mm; }
.contact .p .role { font-size: 8pt; line-height: 1.35; }
.footer { position: absolute; left: 0; right: 0; bottom: 0; background: #000; color: #cfcecc; padding: 6mm 22mm; font-size: 9pt; }
/* Browser-Mock */
.bm { border: 0.8pt solid var(--g30); border-radius: 3.5mm; background: #fff; overflow: hidden; margin-top: 6mm; }
.bm-bar { display:flex; align-items:center; gap: 1.6mm; padding: 2.6mm 4mm; background: #f6f5f3; }
.bm-bar i { width: 2mm; height: 2mm; border-radius: 50%; background: #d9d5d0; display:block; }
.bm-bar span { margin-left: 3mm; font-size: 7.6pt; color: var(--g50); background:#fff; border-radius: 3mm; padding: .8mm 4mm; }
.bm-row { display:grid; grid-template-columns: 10mm 1fr 7mm; align-items:center; padding: 2.9mm 5mm; }
.bm-row + .bm-row { border-top: 0.6pt solid #eeebe8; }
.bm-row .n { font-family: var(--serif); font-weight: 700; font-size: 10pt; color: var(--num); }
.bm-row span { font-size: 9.6pt; font-weight: 500; }
.bm-row em { font-style: normal; width: 6mm; height: 6mm; border-radius: 50%; border: 0.8pt dashed var(--g50); color: var(--g50); display:flex; align-items:center; justify-content:center; font-size: 8pt; font-weight: 600; }
/* Profil */
.prof { display:grid; grid-template-columns: 22mm 1fr; column-gap: 5mm; }
.prof img { width: 22mm; height: 22mm; border-radius: 50%; object-fit: cover; border: 0.6pt solid #d6d2cd; }
.prof h3 { font-size: 11.5pt; margin-bottom: 1mm; }
.prof small { display:block; font-size: 8pt; color: var(--g50); margin-bottom: 2mm; }
.prof p { font-size: 8.8pt; line-height: 1.58; color: var(--g70); }

/* ---- Loesungsblock: ersetzt die duennen rows() auf Uebersichtsseiten ----
   Statt Name + zwei Zeilen: Name, Einordnung, "fuer wen" und Preis. */
.sols { margin-top: 6mm; border-top: 0.8pt solid var(--line); }
.sol { display: grid; grid-template-columns: 1fr auto; gap: 8mm; align-items: start;
       padding: 5mm 0; border-bottom: 0.8pt solid var(--line); }
.sol-name { display: flex; align-items: baseline; gap: 3.5mm; margin-bottom: 1.6mm; }
.sol-name b { font-family: var(--serif); font-weight: 700; font-size: 12.5pt; }
.sol-tag { font-size: 7.6pt; letter-spacing: .1em; text-transform: uppercase;
           color: var(--acc); font-weight: 600; }
.sol p { font-size: 9.2pt; line-height: 1.6; color: var(--g70); max-width: 112mm; }
.sol .for { display: block; font-size: 8.6pt; line-height: 1.5; color: var(--ink2); margin-top: 1.8mm; }
.sol .for b { font-weight: 600; }
.sol-price { font-family: var(--serif); font-weight: 700; font-size: 15pt;
             white-space: nowrap; text-align: right; }
.sol-price em { font-style: normal; font-family: var(--sans); font-weight: 500;
                font-size: 7.6pt; display: block; color: var(--g50); margin-top: 1mm; }

/* Abstand zwischen Sektionen: .sec + .sec greift nur bei direkter Nachbarschaft.
   Sobald ein Block (who/sols/ov) dazwischensteht, muss die folgende Sektion
   ihren Abstand trotzdem bekommen - sonst klebt die Subheadline am Block davor. */
.who + .sec, .sols + .sec, .ov + .sec, .note + .sec,
.who + .cards, .sols + .cards, .who + .band, .sols + .band { margin-top: 12mm; }
.who + .note, .sols + .note, .pakete + .note, .vgl + .note { margin-top: 5mm; }

/* ---- Anzeigen-Vorschau (Google-SERP-Mockup wie auf der Website) ---- */
.serp { margin-top: 6mm; border: 0.8pt solid var(--g30); border-radius: 3.5mm; padding: 5mm; background: #fff; max-width: 118mm; }
.serp-head { display: flex; align-items: center; gap: 2.5mm; }
.serp-avatar { flex: 0 0 auto; width: 8mm; height: 8mm; border-radius: 50%; border: 0.6pt solid var(--g30);
               display: flex; align-items: center; justify-content: center; font-family: var(--serif);
               font-weight: 700; font-size: 9pt; }
.serp-src { font-size: 7.6pt; line-height: 1.3; }
.serp-src small { display: block; color: var(--g50); }
.serp-tag { margin-left: auto; font-size: 6.8pt; color: var(--g50); }
.serp-title { margin: 3mm 0 1.2mm; font-size: 10.5pt; line-height: 1.3; color: #1a0dab; font-weight: 500; }
.serp-desc { font-size: 7.8pt; line-height: 1.5; color: var(--g70); }
.serp-rating { margin-top: 2.5mm; font-size: 7.2pt; color: var(--g70); }
.serp-stars { color: #e7a600; letter-spacing: .5pt; }
.serp-links { display: grid; grid-template-columns: 1fr 1fr; gap: 2.5mm 5mm; margin-top: 3mm;
              padding-top: 3mm; border-top: 0.6pt solid var(--g30); font-size: 7.6pt; }
.serp-links b { display: block; color: #1a0dab; font-weight: 600; }
.serp-links small { color: var(--g50); font-size: 7pt; }
.serp-note { margin-top: 3mm; font-size: 7.2pt; color: var(--g50); line-height: 1.45; }

/* ---- Vergleichs-Timeline (wie auf der Website: Agentur vs. eigenes Angebot) ----
   Zwei Zeilen mit gleicher Timeline-Geometrie; die zweite ist umrandet und
   endet frueher - der gewonnene Vorsprung wird als eigener Chip gezeigt. */
.vgl { margin-top: 6mm; background: var(--bg); border: 0.8pt solid var(--g30);
       border-radius: 4mm; padding: 5mm; display: grid; gap: 3.5mm; }
.vgl-row { display: grid; grid-template-columns: 26mm 1fr; gap: 4mm; align-items: center; }
.vgl-label { font-size: 8.4pt; font-weight: 700; line-height: 1.25; color: var(--ink); }
.vgl-label img { display: block; width: 100%; max-width: 24mm; height: auto; }
.vgl-line { display: flex; align-items: stretch; gap: 1.8mm; background: #fff;
            border: 0.8pt solid transparent; border-radius: 3mm; padding: 2.2mm; }
.vgl-line--outline { border-color: var(--acc); }
.vgl-pill { flex: 1 1 0; display: flex; align-items: center; justify-content: center;
            text-align: center; background: var(--bg); border: 0.6pt solid var(--g30);
            border-radius: 2mm; padding: 2.4mm 1.5mm; font-size: 7.6pt; line-height: 1.25; }
.vgl-line--outline .vgl-pill { flex: 0 0 34mm; }
.vgl-rocket { flex: 0 0 11mm; display: flex; align-items: center; justify-content: center;
              border-radius: 2mm; background: var(--feat-bg); color: var(--feat-fg); }
.vgl-rocket svg { width: 6mm; height: 6mm; }
.vgl-bonus { flex: 1 1 0; display: flex; align-items: center; justify-content: center; gap: 2mm;
             padding: 2.4mm 3mm; border-radius: 2mm; background: var(--tint);
             font-size: 7.8pt; font-weight: 600; color: var(--ink); text-align: center; }
.vgl-bonus svg { flex: 0 0 auto; width: 4mm; height: 4mm; color: var(--acc); }

/* ---- Preispakete gestapelt (statt drei schmaler, ungleich hoher Karten) ---- */
.pakete { margin-top: 5mm; display: grid; gap: 3mm; }
.pk { display: grid; grid-template-columns: 1fr 42mm; gap: 7mm; align-items: start;
      border: 0.8pt solid var(--g30); border-radius: 3.5mm; padding: 4mm 5mm; background: #fff; }
.pk--feat { border-color: var(--acc); background: var(--tint); }
.pk-head { display: flex; align-items: baseline; gap: 3.5mm; margin-bottom: 1.8mm; }
.pk-head b { font-family: var(--serif); font-weight: 700; font-size: 13pt; }
.pk-badge { font-size: 6.6pt; letter-spacing: .1em; text-transform: uppercase; font-weight: 600;
            color: #fff; background: var(--acc); border-radius: 2mm; padding: .8mm 2.2mm; }
.pk-text { font-size: 9.2pt; line-height: 1.6; color: var(--g70); }
.pk-list { list-style: none; margin-top: 2mm; display: grid; gap: .9mm; }
.pk-list li { position: relative; padding-left: 4.5mm; font-size: 8.8pt; line-height: 1.5; color: var(--ink2); }
.pk-list li::before { content: ""; position: absolute; left: 0; top: 1.5mm; width: 1.6mm; height: 1.6mm;
                      border-radius: 50%; background: var(--acc); }
.pk-fazit { margin-top: 2mm; font-size: 8.6pt; line-height: 1.5; color: var(--g50); font-style: italic; }
.pk-preis { text-align: right; }
.pk-betrag { display: block; font-family: var(--serif); font-weight: 700; font-size: 16pt;
             line-height: 1.1; white-space: nowrap; }
.pk-betrag em { font-style: normal; font-family: var(--sans); font-weight: 500; font-size: 8pt;
                color: var(--g50); margin-left: 1.2mm; }
.pk-hinweis { display: block; margin-top: 2mm; font-size: 7.4pt; line-height: 1.45; color: var(--g50); }

/* ---- "Fuer wen" als eigener Block ---- */
.who { margin-top: 6mm; }
.who-title { font-family: var(--serif); font-weight: 700; font-size: 11.5pt; margin-bottom: 3mm; }
.who ul { list-style: none; display: grid; grid-template-columns: 1fr 1fr; gap: 2mm 7mm; }
.who li { position: relative; padding-left: 5.5mm; font-size: 9.2pt; line-height: 1.55; color: var(--g70); }
.who li::before { content: ""; position: absolute; left: 0; top: 1.7mm; width: 2.2mm; height: 2.2mm;
                  border-radius: 50%; background: var(--acc); }

/* ---- Uebersichtstabelle ---- */
.ov { margin-top: 6mm; width: 100%; border-collapse: collapse; }
.ov th { text-align: left; font-size: 6.8pt; letter-spacing: .12em; text-transform: uppercase;
         color: var(--g50); font-weight: 600; padding: 0 5mm 2.5mm 0; border-bottom: 0.8pt solid var(--line); }
.ov td { padding: 4mm 5mm 4mm 0; border-bottom: 0.8pt solid var(--line); vertical-align: top; }
.ov td:last-child, .ov th:last-child { padding-right: 0; text-align: right; }
.ov .t-name { font-family: var(--serif); font-weight: 700; font-size: 11pt; }
.ov .t-sub { display: block; font-size: 8.5pt; color: var(--g70); line-height: 1.5; margin-top: .8mm; }
.ov .t-dur { font-size: 9pt; color: var(--g70); white-space: nowrap; }
.ov .t-price { font-family: var(--serif); font-weight: 700; font-size: 11.5pt; white-space: nowrap; }
"""

def esc(s): return _h.escape(s, quote=False)

def build(theme, pages, title):
    th = THEMES[theme]
    feat_bg = th.get('feat_bg', f"linear-gradient(150deg, {th['acc']} 0%, {th['acc2']} 100%)")
    feat_fg = th.get('feat_fg', '#fff')
    num = th.get('num', th['acc'])
    vars_ = (f":root{{--acc:{th['acc']};--acc2:{th['acc2']};--hl-bg:{th['hl_bg']};--hl-fg:{th['hl_fg']};"
             f"--feat-bg:{feat_bg};--feat-fg:{feat_fg};--tint:{th['tint']};--num:{num};}}")
    total = len(pages)
    body = "".join(p(i + 1, total) if callable(p) else p for i, p in enumerate(pages))
    return (f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{title}</title>'
            f'<link rel="stylesheet" href="assets/fonts/fonts.local.css"><style>{CSS}{vars_}</style></head><body>{body}</body></html>')

FOOTER = '<div class="footer">empiria GmbH 2026</div>'
def head(no, total): return f'<div class="head"><img src="assets/empiria-logo.svg" alt="empiria"><span class="page-no">Seite {no} / {total}</span></div>'

def cover(kicker, h1, subs, sketch, facts, brandlogo=None, noinv=False):
    subs = subs if isinstance(subs, list) else [subs]
    f = "".join(f'<div><span class="label">{l}</span><b>{v}</b></div>' for l, v in facts)
    bl = f'<img class="brandlogo" src="{brandlogo}" alt="">' if brandlogo else ''
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    sk = f'<div class="sketch{" noinv" if noinv else ""}">{sketch}</div>' if sketch else ''
    return lambda no, total: (f'<section class="page cover"><img class="logo" src="assets/empiria-logo.svg" alt="empiria">{bl}{k}'
        f'<h1>{h1}</h1>' + "".join(f'<p class="sub">{s}</p>' for s in subs) + sk +
        f'<div class="facts" style="grid-template-columns:repeat({len(facts)},1fr)">{f}</div></section>')

def page(*content, contact_html=None):
    def r(no, total):
        c = contact_html or ""
        foot = FOOTER if no == total else ""
        return f'<section class="page">{head(no, total)}{"".join(content)}{c}{foot}</section>'
    return r

def sec(kicker, h2, *leads, style=""):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    h = f'<h2>{h2}</h2>' if h2 else ''
    return f'<div class="sec" style="{style}">{k}{h}' + "".join(f'<p class="lead">{l}</p>' for l in leads) + '</div>'

def open_sec(style=""): return f'<div class="sec" style="{style}">'
def close_sec(): return '</div>'

def cards(items, cols=3, style="", numbered=False):
    out = []
    for i, it in enumerate(items):
        ic, t, p = it[0], it[1], it[2]
        extra = it[3] if len(it) > 3 else ""
        top = f'<span class="num">{i+1:02d}</span>' if numbered else (f'<div class="ic">{icon(ic)}</div>' if ic else '')
        out.append(f'<div class="card">{top}<h3>{t}</h3><p>{p}</p>{extra}</div>')
    return f'<div class="cards" style="grid-template-columns:repeat({cols},1fr);{style}">{"".join(out)}</div>'

def rows(items, start=1, style=""):
    out = []
    for i, it in enumerate(items):
        t, p = it[0], it[1]
        extra = f'<div class="extra">{it[2]}</div>' if len(it) > 2 and it[2] else ""
        out.append(f'<div class="row"><span class="n">{i+start:02d}</span><div><h3>{t}</h3><p>{p}</p>{extra}</div></div>')
    return f'<div class="rows" style="{style}">{"".join(out)}</div>'

def stations(items, style=""):
    out = []
    for i, it in enumerate(items):
        small, t, p = it
        sm = f'<small>{small}</small>' if small else ''
        out.append(f'<div class="st"><span class="n">{i+1}</span>{sm}<b>{t}</b><p>{p}</p></div>')
    return f'<div class="stations" style="{style}">{"".join(out)}</div>'

def dots(items, cls="", style=""):
    return f'<ul class="dots {cls}" style="{style}">' + "".join(f'<li>{x}</li>' for x in items) + '</ul>'

def checks(items, cls="", style=""):
    return f'<ul class="checks {cls}" style="{style}">' + "".join(f'<li>{icon("check")}{x}</li>' for x in items) + '</ul>'

def statement(kicker, text, style=""):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    return f'<div class="sec" style="{style}">{k}<p class="statement">{text}</p></div>'

def quotes(items, style=""):
    return f'<div class="quotes" style="{style}">' + "".join(f'<span>{x}</span>' for x in items) + '</div>'

def band(kicker, h3, *ps, extra="", style=""):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    h = f'<h3>{h3}</h3>' if h3 else ''
    return f'<div class="band" style="{style}">{k}{h}' + "".join(f'<p>{p}</p>' for p in ps) + extra + '</div>'

def feat(kicker, h3, *ps, extra="", style=""):
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    h = f'<h3>{h3}</h3>' if h3 else ''
    return f'<div class="feat" style="{style}">{k}{h}' + "".join(f'<p>{p}</p>' for p in ps) + extra + '</div>'

def opts(items, cols=None, style=""):
    """Preiskarten in der Reihenfolge der Website.

    Felder: name, sub (Dauer, steht neben dem Namen), badge ("Meistgewaehlt"),
    text (Beschreibung), price, unit, pnote (Unterschrift unter dem Preis),
    list (Leistungen), feat (hervorgehobene Karte).
    `tag` wird weiter unterstuetzt und als Dauer gelesen; ein darin enthaltener
    Zusatz nach "·" wird zum Badge.
    """
    out = []
    for it in items:
        d = dict(it)
        sub, badge = d.get("sub"), d.get("badge")
        if not sub and d.get("tag"):
            teile = [t.strip() for t in d["tag"].split("·")]
            sub = teile[0]
            if len(teile) > 1 and not badge:
                badge = teile[1]
        cls = "opt opt--feat" if d.get("feat") else "opt"
        bd = f'<span class="badge">{badge}</span>' if badge else ''
        sb = f'<span class="sub">{sub}</span>' if sub else ''
        sm = f'<small>{d["text"]}</small>' if d.get("text") else ''
        unit = f'<em>{d["unit"]}</em>' if d.get("unit") else ''
        pr = f'<span class="price">{d["price"]}{unit}</span>' if d.get("price") else ''
        pn = f'<span class="pnote">{d["pnote"]}</span>' if d.get("pnote") else ''
        ul = dots(d["list"]) if d.get("list") else ''
        out.append(f'<div class="{cls}"><div class="badgeslot">{bd}</div>'
                   f'<b>{d["name"]}{sb}</b>{sm}{pr}{pn}{ul}</div>')
    cols = cols or len(items)
    return f'<div class="opts" style="grid-template-columns:repeat({cols},1fr);{style}">{"".join(out)}</div>'

def mdl(kicker, titel, svg, *ps, steps=None, figw="68mm", style=""):
    """Skizze im schwarzen Kasten, daneben die Erlaeuterung - wie im Pop-up.

    svg: fertiges SVG-Markup (S.load(...)). Es wird NICHT invertiert, sondern
    auf schwarzem Grund in seinen Originalfarben gezeigt.
    steps: optionale Liste (Nummer, Titel, Text) als gelbe Schritt-Liste.
    """
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    h = f'<h3>{titel}</h3>' if titel else ''
    txt = "".join(f'<p>{p}</p>' for p in ps)
    st = ''
    if steps:
        st = '<div class="mdl-steps">' + "".join(
            f'<div class="mdl-step"><i>{n}</i><span><b>{t}</b>{x}</span></div>'
            for n, t, x in steps) + '</div>'
    return (f'<div class="mdl" style="--figw:{figw};{style}">'
            f'<div class="mdl-fig">{svg}</div>'
            f'<div class="mdl-txt">{k}{h}{txt}{st}</div></div>')


def paket(kicker_l, leistungen, kicker_r, preis, preis_note, style=""):
    """Leistungspaket und Preis als ein zusammenhaengender Block."""
    return (f'<div class="paket" style="{style}">'
            f'<div class="paket-l"><p class="kicker">{kicker_l}</p>{checks(leistungen)}</div>'
            f'<div class="paket-r"><p class="kicker">{kicker_r}</p>'
            f'<span class="price">{preis}</span><p>{preis_note}</p></div></div>')


def stein(tag, items, foot, style=""):
    """Durchgestrichene Denkmuster im schwarzen Kasten - wie auf der Landingpage."""
    lis = "".join(f'<li>{i}</li>' for i in items)
    return (f'<div class="stein" style="{style}"><p class="tag">{tag}</p>'
            f'<ul>{lis}</ul><p class="foot">{foot}</p></div>')


def raster(items, cols=None, style=""):
    """Nummeriertes Raster; ein Eintrag kann per main=True hervorgehoben werden.

    items: Liste (Nummer, Titel) oder (Nummer, Titel, True) fuer das Hauptfeld.
    """
    out = []
    for it in items:
        cls = ' class="main"' if len(it) > 2 and it[2] else ''
        out.append(f'<div{cls}><span class="num">{it[0]}</span><b>{it[1]}</b></div>')
    cols = cols or len(items)
    return f'<div class="raster" style="grid-template-columns:repeat({cols},1fr);{style}">{"".join(out)}</div>'


def stage(kicker, h2, *ps, inhalt="", wm=None, style=""):
    """Sektion im Landingpage-Look: heller Grund, Icon-Wasserzeichen, dunkler Kasten."""
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''
    h = f'<h2>{h2}</h2>' if h2 else ''
    txt = "".join(f'<p>{p}</p>' for p in ps)
    w = f'<div class="stage-wm">{icon(wm)}</div>' if wm else ''
    return (f'<div class="stage" style="{style}">{w}'
            f'<div class="stage-head">{k}{h}{txt}</div>{inhalt}</div>')


def mocks(items, kicker=None, titel=None, style=""):
    """Drei Medien-Mockups nebeneinander im schwarzen Kasten (Website-Sketchreihe).

    items: Liste (svg, Label, Text).
    """
    k = f'<p class="kicker" style="color:#fff400">{kicker}</p>' if kicker else ''
    h = f'<h3 style="color:#fff;font-family:var(--serif);font-size:13pt;margin-bottom:5mm">{titel}</h3>' if titel else ''
    cells = "".join(f'<div class="mock"><div class="mock-fig">{svg}</div><b>{lab}</b><p>{txt}</p></div>'
                    for svg, lab, txt in items)
    return f'<div class="mocks-box" style="{style}">{k}{h}<div class="mocks">{cells}</div></div>'


def cases(items, style="", cols=2):
    out = "".join(f'<div class="case">' + (f'<div class="ic">{icon(c[2])}</div>' if len(c) > 2 else '') + f'<h3>{c[0]}</h3><p>{c[1]}</p></div>' for c in items)
    return f'<div class="cases" style="grid-template-columns:repeat({cols},1fr);{style}">{out}</div>'

def chips(items, style=""):
    return f'<div class="chips" style="{style}">' + "".join(f'<span>{x}</span>' for x in items) + '</div>'

PEOPLE = {
  "daniel": ("assets/ansprechpartner-daniel.webp", "Daniel Ströbel", "Strategiehandwerker<br>Geschäftsführer empiria GmbH"),
  "kerstin_hr": ("assets/ansprechpartner-kerstin.webp", "Kerstin Christ", "Expertin HR &amp; Weiterbildung"),
  "kerstin_content": ("assets/ansprechpartner-kerstin.webp", "Kerstin Christ", "Expertin Content &amp; Sichtbarkeit"),
  "noah_ki": ("assets/ansprechpartner-noah.webp", "Noah Hermanns", "KI Native"),
  "noah_pm": ("assets/ansprechpartner-noah.webp", "Noah Hermanns", "Experte Performance Marketing"),
  "rick": ("assets/ansprechpartner-rick.webp", "Rick-Marcel Richter", "IT &amp; Transformation"),
}
DL = ('<dl><dt>E-Mail</dt><dd>daniel.stroebel@empiria.de</dd><dt>Telefon</dt><dd>+49 176 3134 7217</dd>'
      '<dt>Web</dt><dd>www.empiria.de</dd></dl>')

def contact(h3, people, kicker="Kontakt", bottom=None):
    st = f' style="bottom:{bottom}mm"' if bottom else ''
    if len(people) == 1:
        img, n, r = PEOPLE[people[0]]
        body = f'<div class="one"><img class="ph" src="{img}" alt=""><div><p class="name">{n}</p><p class="role">{r}</p></div>{DL}</div>'
    else:
        ps = "".join(f'<div class="p"><img src="{PEOPLE[k][0]}" alt=""><div><p class="name">{PEOPLE[k][1]}</p><p class="role">{PEOPLE[k][2].split("<br>")[0]}</p></div></div>' for k in people)
        cols = len(people)
        dlrow = '<div class="dlrow"><span><span class="label">E-Mail</span>daniel.stroebel@empiria.de</span><span><span class="label">Telefon</span>+49 176 3134 7217</span><span><span class="label">Web</span>www.empiria.de</span></div>'
        body = f'<div class="many"><div class="ppl" style="grid-template-columns:repeat({cols},1fr)">{ps}</div>{dlrow}</div>'
    k = f'<p class="kicker">{kicker}</p>' if kicker else ''   # leerer Kicker wuerde Luft fressen
    return f'<div class="contact"{st}>{k}<h3>{h3}</h3>{body}</div>'


def sols(items, style=""):
    """Loesungsblock fuer Uebersichtsseiten.

    items: (name, tag, beschreibung, fuer_wen, preis, preis_zusatz)
    tag/fuer_wen/preis/preis_zusatz duerfen leer sein.
    """
    out = ""
    for it in items:
        name, tag, desc, forwhom, price, pnote = (list(it) + [""] * 6)[:6]
        t = f'<span class="sol-tag">{tag}</span>' if tag else ""
        f = f'<span class="for"><b>Für wen:</b> {forwhom}</span>' if forwhom else ""
        if price:
            em = f"<em>{pnote}</em>" if pnote else ""
            right = f'<div class="sol-price">{price}{em}</div>'
        else:
            right = '<div class="sol-price" style="font-size:10.5pt;color:var(--g70)">individuell</div>'
        out += (f'<div class="sol"><div><div class="sol-name"><b>{name}</b>{t}</div>'
                f'<p>{desc}</p>{f}</div>{right}</div>')
    return f'<div class="sols" style="{style}">{out}</div>'


def who(title, items, style=""):
    """Wer profitiert davon - fuellt die bisher leeren Flaechen mit Substanz."""
    lis = "".join(f"<li>{i}</li>" for i in items)
    return f'<div class="who" style="{style}"><p class="who-title">{title}</p><ul>{lis}</ul></div>'


def overview(rows_, style=""):
    """Tabelle: Angebot / Umfang / Investition - Orientierung auf einen Blick.

    rows_: (name, sub, umfang, preis)
    """
    body = ""
    for name, sub, dur, price in rows_:
        body += (f'<tr><td><span class="t-name">{name}</span>'
                 f'<span class="t-sub">{sub}</span></td>'
                 f'<td class="t-dur">{dur}</td>'
                 f'<td class="t-price">{price}</td></tr>')
    return (f'<table class="ov" style="{style}"><thead><tr><th>Angebot</th><th>Umfang</th>'
            f'<th>Investition</th></tr></thead><tbody>{body}</tbody></table>')


def pakete(items, style=""):
    """Preispakete als gestapelte Zeilen statt gequetschter Spalten.

    Drei schmale Spalten erzwingen unterschiedlich hohe Karten, wodurch die
    Preise auf verschiedenen Hoehen sitzen und das Ganze unsauber wirkt.
    Gestapelt bekommt jedes Paket die volle Breite: links Inhalt, rechts Preis.

    items: dict(name, badge, text, bullets, preis, einheit, hinweis, fazit)
    """
    out = ""
    for it in items:
        badge = f'<span class="pk-badge">{it["badge"]}</span>' if it.get("badge") else ""
        bl = ""
        if it.get("bullets"):
            bl = '<ul class="pk-list">' + "".join(f"<li>{b}</li>" for b in it["bullets"]) + "</ul>"
        fazit = f'<p class="pk-fazit">{it["fazit"]}</p>' if it.get("fazit") else ""
        einheit = f'<em>{it["einheit"]}</em>' if it.get("einheit") else ""
        hinweis = f'<span class="pk-hinweis">{it["hinweis"]}</span>' if it.get("hinweis") else ""
        feat = " pk--feat" if it.get("badge") else ""
        out += (f'<div class="pk{feat}"><div class="pk-main">'
                f'<div class="pk-head"><b>{it["name"]}</b>{badge}</div>'
                f'<p class="pk-text">{it["text"]}</p>{bl}{fazit}</div>'
                f'<div class="pk-preis"><span class="pk-betrag">{it["preis"]}{einheit}</span>{hinweis}</div></div>')
    return f'<div class="pakete" style="{style}">{out}</div>'


def vergleich(label_a, pills_a, label_b_logo, pill_b, bonus, style=""):
    """Zeitstrahl-Vergleich wie auf der Website.

    label_a/pills_a: klassischer Weg mit mehreren Phasen
    label_b_logo:    Bildpfad des Produktlogos fuer die zweite Zeile
    pill_b/bonus:    eigener Weg - eine Phase, danach der gewonnene Vorsprung
    """
    r = f'<span class="vgl-rocket">{icon("rocket")}</span>'
    pa = "".join(f'<span class="vgl-pill">{x}</span>' for x in pills_a)
    return (f'<div class="vgl" style="{style}">'
            f'<div class="vgl-row"><div class="vgl-label">{label_a}</div>'
            f'<div class="vgl-line">{pa}{r}</div></div>'
            f'<div class="vgl-row"><div class="vgl-label"><img src="{label_b_logo}" alt=""></div>'
            f'<div class="vgl-line vgl-line--outline"><span class="vgl-pill">{pill_b}</span>{r}'
            f'<span class="vgl-bonus">{icon("clock")}{bonus}</span></div></div></div>')


def anzeige(quelle, url, titel, text, bewertung, links, note=None, initial="e"):
    """Google-Anzeigenvorschau - im PDF war davon vorher nur Flies-Text uebrig.

    links: Liste aus (Titel, Untertitel) fuer die Sitelinks
    """
    ll = "".join(f"<span><b>{a}</b><small>{b}</small></span>" for a, b in links)
    n = f'<p class="serp-note">{note}</p>' if note else ""
    return (f'<div class="serp"><div class="serp-head">'
            f'<span class="serp-avatar">{initial}</span>'
            f'<span class="serp-src"><b>{quelle}</b><small>{url}</small></span>'
            f'<span class="serp-tag">Gesponsert</span></div>'
            f'<p class="serp-title">{titel}</p><p class="serp-desc">{text}</p>'
            f'<p class="serp-rating"><span class="serp-stars">★★★★★</span> {bewertung}</p>'
            f'<div class="serp-links">{ll}</div></div>{n}')
