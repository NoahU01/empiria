#!/usr/bin/env python3
"""empiria PDF-Vorlage (hell) – eine Vorlage, mehrere Farbwelten.

THEMES steuert Akzentfarbe (Vorüberschriften, Icons, Nummern, Verlaufs-Kasten)
und Highlight (Markierung in Headlines). Für Strategie-Seiten: theme="strategie"
(gelbe Markierung mit dunkler Schrift, Akzent in Dunkelgrau).
"""
THEMES = {
  "magenta":   dict(acc="#C51F5D", acc2="#7a1339", hl_bg="#C51F5D", hl_fg="#fff"),
  "cyan":      dict(acc="#0B9FBD", acc2="#086a80", hl_bg="#0B9FBD", hl_fg="#fff"),
  "violet":    dict(acc="#8613A1", acc2="#56106a", hl_bg="#8613A1", hl_fg="#fff"),
  "emerald":   dict(acc="#059669", acc2="#037a54", hl_bg="#059669", hl_fg="#fff"),
  "capiamo":   dict(acc="#063755", acc2="#04263b", hl_bg="#063755", hl_fg="#fff"),
  "strategie": dict(acc="#1a1817", acc2="#2e2d2c", hl_bg="#fff400", hl_fg="#1a1817", feat_bg="#fff400", feat_fg="#1a1817"),
}

ICONS = {
 "check": '<path d="M5 12.5l4.5 4.5L19 7.5"/>',
 "team": '<circle cx="9" cy="8" r="3.2"/><path d="M3 19c.6-3.4 3-5.2 6-5.2s5.4 1.8 6 5.2"/><circle cx="17" cy="9" r="2.4"/><path d="M16 13.9c2.6.2 4.4 1.8 5 4.6"/>',
 "tool": '<path d="M4 20l7-7"/><path d="M14.5 3.5a4.5 4.5 0 0 0-3.9 6.7L4 16.8 7.2 20l6.6-6.6a4.5 4.5 0 0 0 6.7-3.9l-2.8 2.8-3.2-.9-.9-3.2z"/>',
 "target": '<circle cx="12" cy="12" r="8"/><circle cx="12" cy="12" r="4.2"/><circle cx="12" cy="12" r="1" fill="currentColor"/>',
 "mail": '<rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.8 7l8.2 6 8.2-6"/>',
}
def icon(n): return f'<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.7" stroke-linecap="round" stroke-linejoin="round">{ICONS[n]}</svg>'

CSS = """
@page { size: A4; margin: 0; }
:root { --ink:#1a1817; --ink2:#2e2d2c; --g70:#58564f; --g50:#8a8783; --line:#e7e2df; --bg:#ededed;
        --serif:"Lora",Georgia,serif; --sans:"Poppins",sans-serif; }
* { box-sizing: border-box; margin: 0; padding: 0; }
body { font-family: var(--sans); color: var(--ink); -webkit-print-color-adjust: exact; print-color-adjust: exact; }
.page { width: 210mm; height: 297mm; position: relative; overflow: hidden; page-break-after: always; padding: 20mm 22mm 18mm; background: #fff; }
.page:last-child { page-break-after: auto; }
.hl { position: relative; z-index: 0; display: inline-block; color: var(--hl-fg); font-weight: 700; }
.hl::before { content:""; position:absolute; z-index:-1; left:-.08em; right:-.08em; top:.1em; bottom:-.02em; background: var(--hl-bg); border-radius: 4px; }
.head { display:flex; justify-content: space-between; align-items:center; margin-bottom: 16mm; }
.head img { height: 6mm; }
.page-no { font-size: 8pt; color: var(--g50); font-weight: 500; }
.kicker { font-weight: 500; font-size: 11pt; color: var(--acc); margin: 0 0 2mm; }
h1 { font-family: var(--serif); font-weight: 700; font-size: 44pt; line-height: 1.08; letter-spacing: -.01em; }
h2 { font-family: var(--serif); font-weight: 700; font-size: 24pt; line-height: 1.18; margin: 0 0 5mm; }
h3 { font-family: var(--serif); font-weight: 700; font-size: 13pt; line-height: 1.25; }
p.lead { font-size: 10.5pt; line-height: 1.75; color: var(--ink2); max-width: 150mm; }
p.lead + p.lead { margin-top: 3mm; }
.label { font-size: 6.8pt; letter-spacing: .12em; text-transform: uppercase; color: var(--g50); font-weight: 600; }
/* Deckblatt (hell) */
.cover .kicker { margin-top: 26mm; }
.cover h1 { margin: 3mm 0 7mm; max-width: 160mm; }
.cover .sub { font-size: 12pt; line-height: 1.6; color: var(--g70); max-width: 140mm; }
.cover .sketch { position: absolute; left: 22mm; right: 22mm; bottom: 48mm; height: 76mm; display: flex; justify-content: center; }
.cover .sketch svg { height: 100%; width: auto; filter: invert(1) contrast(1.6); }
.cover .facts { position: absolute; left: 22mm; right: 22mm; bottom: 20mm; display: grid; gap: 8mm; }
.cover .facts b { display:block; font-family: var(--serif); font-size: 12pt; margin-top: 1.5mm; }
/* Kacheln */
.cards { display: grid; gap: 5mm; margin-top: 10mm; }
.card { border: 0.6pt solid var(--line); border-radius: 4mm; padding: 6mm 5.5mm; background: #fff; }
.card .ic { width: 8mm; height: 8mm; color: var(--acc); margin-bottom: 4mm; }
.card .ic svg { width: 100%; height: 100%; }
.card h3 { font-size: 11.5pt; margin-bottom: 2mm; }
.card p { font-size: 9pt; line-height: 1.6; color: var(--g70); }
/* Liste nummeriert */
.rows { margin-top: 4mm; }
.row { display: grid; grid-template-columns: 12mm 1fr; column-gap: 4mm; padding: 3.5mm 0; }
.row .n { font-family: var(--serif); font-weight: 700; font-size: 12pt; color: var(--acc); }
.row h3 { margin-bottom: 1.5mm; }
.row p { font-size: 9.5pt; line-height: 1.6; color: var(--g70); }
/* Preis-/Detailblöcke */
.detail { padding: 5mm 0; }
.detail-head { display: flex; justify-content: space-between; align-items: baseline; gap: 6mm; margin-bottom: 3mm; }
.detail-head p { font-size: 9pt; color: var(--g70); }
.opts { display: grid; gap: 4mm; }
.opt { background: var(--bg); border-radius: 3mm; padding: 4mm 4.5mm; }
.opt b { display:block; font-family: var(--serif); font-size: 10.5pt; }
.opt small { display:block; font-size: 8pt; color: var(--g70); margin: .8mm 0 2mm; }
.opt .price { font-family: var(--serif); font-weight: 700; font-size: 13pt; color: var(--ink); }
.opt--feat { background: var(--feat-bg); color: var(--feat-fg); }
.opt--feat small, .opt--feat .price { color: var(--feat-fg); }
.note { font-size: 7.5pt; color: var(--g50); margin-top: 3mm; line-height: 1.5; }
/* Kontakt + Footer */
.contact { position: absolute; left: 22mm; right: 22mm; bottom: 30mm; }
.contact h2 { font-size: 17pt; margin-bottom: 7mm; }
.people { display: grid; grid-template-columns: repeat(3, 1fr); gap: 6mm; align-items: center; }
.person { display: flex; align-items: center; gap: 3.5mm; }
.person img { width: 15mm; height: 15mm; border-radius: 50%; object-fit: cover; border: 0.6pt solid #d6d2cd; }
.person b { display:block; font-family: var(--serif); font-size: 10pt; }
.person span { display:block; font-size: 7.8pt; line-height: 1.35; color: var(--g50); margin-top: .5mm; }
.direct { margin-top: 6mm; display: flex; gap: 10mm; font-size: 9.5pt; }
.direct .label { margin-right: 2.5mm; }
.footer { position: absolute; left: 0; right: 0; bottom: 0; background: #000; color: #cfcecc; padding: 6mm 22mm; display: flex; justify-content: space-between; align-items: center; font-size: 9pt; }
.footer a { color: #cfcecc; text-decoration: none; }
.footer .sep { margin: 0 3mm; }
"""

def build(theme, pages_html, title):
    th = THEMES[theme]
    feat_bg = th.get('feat_bg', f"linear-gradient(155deg, {th['acc']} 0%, {th['acc2']} 100%)"); feat_fg = th.get('feat_fg', '#fff')
    vars_ = f":root{{--acc:{th['acc']};--acc2:{th['acc2']};--hl-bg:{th['hl_bg']};--hl-fg:{th['hl_fg']};--feat-bg:{feat_bg};--feat-fg:{feat_fg};}}"
    return f'<!doctype html><html lang="de"><head><meta charset="utf-8"><title>{title}</title><link rel="stylesheet" href="assets/fonts/fonts.local.css"><style>{CSS}{vars_}</style></head><body>{pages_html}</body></html>'

FOOTER = '<div class="footer"><span>empiria GmbH 2026</span></div>'
def head(no, total): return f'<div class="head"><img src="assets/empiria-logo.svg" alt="empiria"><span class="page-no">Seite {no} / {total}</span></div>'
