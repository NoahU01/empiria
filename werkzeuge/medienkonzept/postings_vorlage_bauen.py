#!/usr/bin/env python3
"""Baut postings-vorlage.html – die Vorlage für Daniels Posting-Bilder (1080 × 1350).

Maßstab: Homepage 2.0 und Volksfest-Seite – große Lora-Headline, ein Wort im gelben Block,
Kicker mit Strich, Markenzeichen »» (Richtung) ✕ (Durchsetzung) ○ (Zukunft), Karten abgerundet,
Flächen Weiß, Gelb, Schwarz. Nie Weiß auf Gelb oder Gelb auf Weiß.

    python3 werkzeuge/medienkonzept/postings_vorlage_bauen.py
    python3 werkzeuge/medienkonzept/postings_rendern.py
"""
import os, re

HIER = os.path.dirname(os.path.abspath(__file__))
SITE = os.path.abspath(os.path.join(HIER, "..", "..", "site"))
B = "/assets/projekte/medienkonzept/"

# Markenzeichen aus dem Symbol-Satz der Seiten
_sprite = open(os.path.join(HIER, "seiten-vorlage.html"), encoding="utf-8").read()


def zeichen_svg(name):
    m = re.search(r'<symbol id="ic-%s" viewBox="([^"]+)">(.*?)</symbol>' % name, _sprite, re.S)
    return '<svg viewBox="%s" aria-hidden="true">%s</svg>' % (m.group(1), m.group(2).strip())


F, X, O = zeichen_svg("forward"), zeichen_svg("kreuz"), zeichen_svg("kreis")

CSS = """
:root { --ink:#1a1817; --ink2:#3d3a37; --gelb:#fff400; --grau:#6b6762; --hell:#f3f1ee; --linie:#e4e0db; }
* { box-sizing:border-box; margin:0; padding:0; }
html, body { width:1080px; background:#fff; }
.p { display:none; position:relative; width:1080px; height:1350px; overflow:hidden; font-family:"Poppins",sans-serif; color:var(--ink); background:#fff; padding:84px 84px 0; }
.p:target { display:block; }
@media print { @page { size:1080px 1350px; margin:0; } body.druck .p { display:block; break-after:page; } }
.k { display:flex; align-items:center; gap:18px; font:600 24px/1.2 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; }
.k::before { content:""; width:44px; height:3px; background:currentColor; }
.h { font:700 96px/1.06 "Lora",Georgia,serif; letter-spacing:-.015em; margin-top:34px; }
.h.m { font-size:84px; }
.hl { background:var(--gelb); border-radius:18px; padding:0 .14em; margin:0 -.04em; -webkit-box-decoration-break:clone; box-decoration-break:clone; }
.text { margin-top:30px; font:400 34px/1.5 "Poppins",sans-serif; color:var(--ink2); max-width:860px; }
.fuss { position:absolute; left:84px; right:84px; bottom:70px; display:flex; justify-content:space-between; align-items:center; font:500 24px/1 "Poppins",sans-serif; color:var(--grau); }
.fuss > img { height:34px; display:block; }
.zeichen { position:absolute; color:var(--ink); }
.zeichen svg { width:100%; height:100%; display:block; }
.karte { height:600px; border-radius:28px; overflow:hidden; margin-bottom:58px; }
.karte img { width:100%; height:100%; object-fit:cover; object-position:var(--pos,50% 50%); display:block; }
.sw img { filter:grayscale(1) contrast(1.06); }
.gelbgrund { background:var(--gelb); }
.rund { width:300px; height:300px; border-radius:50%; overflow:hidden; border:8px solid var(--ink); }
.rund img { width:100%; height:100%; object-fit:cover; object-position:50% 30%; filter:grayscale(1) contrast(1.06); display:block; }
.zitat { margin-top:72px; font:700 80px/1.13 "Lora",Georgia,serif; letter-spacing:-.01em; }
.quelle { margin-top:40px; font:500 30px/1.4 "Poppins",sans-serif; }
.schwarz { background:var(--ink); color:#fff; }
.schwarz .k { color:var(--gelb); }
.schwarz .fuss { color:#a8a39c; }
.liste { margin-top:70px; }
.liste div { display:flex; align-items:baseline; gap:40px; padding:34px 0; border-top:2px solid #3a3734; font:700 88px/1 "Lora",Georgia,serif; }
.liste div:last-child { border-bottom:2px solid #3a3734; }
.liste small { font:600 26px/1 "Poppins",sans-serif; color:#a8a39c; width:44px; }
.nr { font:700 30px/1 "Lora",Georgia,serif; color:#b5b0a9; }
.seitenkopf { display:flex; justify-content:space-between; align-items:center; }
.frage { margin-top:64px; background:var(--ink); color:#fff; border-radius:28px; padding:52px 150px 58px 56px; position:relative; }
.frage small { display:block; font:600 22px/1 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--gelb); margin-bottom:24px; }
.frage p { font:700 58px/1.16 "Lora",Georgia,serif; }
.frage .zeichen { right:48px; top:44px; width:64px; height:64px; color:var(--gelb); }
.block { margin-top:72px; }
.block > small { display:block; font:600 22px/1 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; color:var(--grau); margin-bottom:24px; }
.block li { list-style:none; padding:18px 0; border-top:2px solid var(--linie); font:400 34px/1.4 "Poppins",sans-serif; }
.block li:last-child { border-bottom:2px solid var(--linie); }
.oeffnen { background:var(--hell); border-radius:24px; padding:36px 42px; font:500 34px/1.5 "Poppins",sans-serif; }
.check li { list-style:none; display:flex; gap:32px; align-items:flex-start; padding:30px 0; border-top:3px solid var(--ink); font:600 34px/1.3 "Poppins",sans-serif; }
.check li:last-child { border-bottom:3px solid var(--ink); }
.check li::before { content:""; flex:0 0 46px; height:46px; border:4px solid var(--ink); border-radius:10px; margin-top:2px; }
.autor { display:flex; align-items:center; gap:22px; }
.autor .rund { width:96px; height:96px; border-width:4px; }
.autor .rund img { object-position:25% 15%; }
.autor b { display:block; color:var(--ink); font-weight:600; margin-bottom:8px; }

/* Serien-Beispiele (12.10.2026): Foto vollflächig mit einem Satz, ohne Rahmen und Logo */
.vollbild { padding:0; }
.vollbild > img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; object-position:var(--pos,50% 50%); }
.vollbild .verlauf { position:absolute; inset:auto 0 0 0; height:62%; background:linear-gradient(180deg, rgba(26,24,23,0) 0%, rgba(26,24,23,.82) 55%, rgba(26,24,23,.92) 100%); }
.vollbild .unten { position:absolute; left:80px; right:80px; bottom:86px; color:#fff; }
.vollbild .satz { font:700 66px/1.14 "Lora",Georgia,serif; letter-spacing:-.01em; }
.vollbild .wer { margin-top:30px; font:500 28px/1.4 "Poppins",sans-serif; color:#d9d5cf; }
.vollbild .zahl { font:700 230px/.9 "Lora",Georgia,serif; color:var(--gelb); letter-spacing:-.02em; }
.vollbild .oben { position:absolute; left:80px; top:76px; color:#fff; }
.vollbild .oben.k::before { background:#fff; }

/* Postingtypen ohne Foto (13.10.2026): Frage, Modell, Zahl, Satz */
.karte-frage { padding:96px 88px; }
.karte-frage .h { font-size:96px; line-height:1.16; margin-top:70px; }
.namezeile { position:absolute; left:88px; right:88px; bottom:72px; font:500 24px/1 "Poppins",sans-serif; color:var(--grau); }
.schwarz .namezeile { color:#a8a39c; }
.modell { margin-top:64px; display:grid; gap:22px; }
.modell .stufe { display:grid; grid-template-columns:200px 1fr; gap:28px; align-items:start; padding:44px 40px; border-radius:24px; background:var(--hell); }
.modell .stufe b { font:700 64px/1 "Lora",Georgia,serif; }
.modell .stufe p { font:500 34px/1.35 "Poppins",sans-serif; color:var(--ink2); }
.modell .stufe small { display:block; margin-top:10px; font:500 24px/1.4 "Poppins",sans-serif; color:var(--grau); }
.modell .stufe.gelb-b { background:var(--gelb); }
.modell .stufe.gelb-b p, .modell .stufe.gelb-b small { color:var(--ink); }
.zahlkarte .zahl { margin-top:110px; font:700 300px/.9 "Lora",Georgia,serif; color:var(--gelb); letter-spacing:-.03em; }
.zahlkarte .satz { margin-top:40px; font:700 64px/1.15 "Lora",Georgia,serif; color:#fff; }
.zahlkarte .quelle2 { margin-top:34px; font:500 26px/1.4 "Poppins",sans-serif; color:#a8a39c; }
.satzkarte .zitat { margin-top:210px; font:700 104px/1.1 "Lora",Georgia,serif; }
.satzkarte .quelle { margin-top:44px; }

/* Varianten je Postingtyp (13.10.2026) */
.luc { fill:none; stroke:currentColor; stroke-width:1.5; stroke-linecap:round; stroke-linejoin:round; display:block; }
.grau { background:#ece9e5; }
/* Satz V3 – die Nachricht */
.chat-zeit { text-align:center; margin-top:40px; font:600 26px/1 "Poppins",sans-serif; color:#8a857e; }
.chat-blase { margin-top:30px; max-width:800px; padding:40px 46px; border-radius:40px 40px 40px 10px; background:#fff; font:500 52px/1.28 "Poppins",sans-serif; color:var(--ink); box-shadow:0 2px 0 rgba(0,0,0,.06); }
.chat-blase.du { margin-left:auto; border-radius:40px 40px 10px 40px; background:var(--ink); color:#fff; }
.chat-blase small { display:block; margin-top:14px; font:500 24px/1 "Poppins",sans-serif; color:#8a857e; text-align:right; }
.chat-fuss { position:absolute; left:84px; right:84px; bottom:96px; font:700 84px/1.08 "Lora",Georgia,serif; color:var(--ink); }
/* Frage V2 – schwarz mit Icon */
.frage-schwarz { flex-direction:column; padding-bottom:96px; }\n.frage-schwarz:target { display:flex; }
.frage-schwarz .riesig { width:380px; height:380px; color:var(--gelb); margin-top:70px; }
.frage-schwarz .h { color:#fff; margin-top:auto; font-size:100px; line-height:1.16; }
/* Modell V2 – drei Icons */
.drei { margin-top:90px; display:grid; gap:0; }
.drei div { display:grid; grid-template-columns:170px 1fr; gap:40px; align-items:center; padding:52px 0; border-top:4px solid var(--ink); }
.drei div:last-child { border-bottom:4px solid var(--ink); }
.drei svg { width:150px; height:150px; }
.drei b { display:block; font:700 80px/1 "Lora",Georgia,serif; }
.drei span { display:block; margin-top:16px; font:500 36px/1.3 "Poppins",sans-serif; }
/* Modell V3 – vorher / nachher */
.vn { margin-top:80px; display:grid; grid-template-columns:1fr 1fr; gap:26px; height:760px; }
.vn > div { padding:48px 40px; border-radius:28px; }
.vn .vor { background:var(--hell); }
.vn .nach { background:var(--gelb); }
.vn small { display:block; font:700 24px/1 "Poppins",sans-serif; letter-spacing:.14em; text-transform:uppercase; }
.vn ul { list-style:none; margin-top:50px; display:grid; gap:56px; }
.vn li { font:600 44px/1.22 "Poppins",sans-serif; }
.vn .vor li { color:#8a857e; text-decoration:line-through; text-decoration-thickness:3px; }
/* Werkzeug V2 – Checkliste */
.check2 { margin-top:110px; list-style:none; }
.check2 li { display:flex; gap:40px; align-items:center; padding:62px 0; border-top:4px solid var(--ink); font:700 62px/1.12 "Lora",Georgia,serif; }
.check2 li:last-child { border-bottom:4px solid var(--ink); }
.check2 li::before { content:""; flex:0 0 76px; height:76px; border:6px solid var(--ink); border-radius:12px; }
/* Eingeordnet V2 – Schlagzeile */
.news { margin-top:90px; padding:52px 50px 56px; border-radius:28px; background:#fff; color:var(--ink); }
.news small { display:block; font:600 24px/1 "Poppins",sans-serif; color:#8a857e; }
.news b { display:block; margin-top:24px; font:700 68px/1.14 "Lora",Georgia,serif; }
.news-frage { position:absolute; left:84px; right:84px; bottom:110px; font:700 92px/1.12 "Lora",Georgia,serif; color:#fff; }
.news-frage .hl { color:var(--ink); }

/* Anschnitt und Raster (13.10.2026): Markenzeichen zeigt den Baustein – »» 01 · ✕ 02 · ○ 03 */
.an { position:absolute; z-index:0; pointer-events:none; }
.an svg { width:100%; height:100%; display:block; }
.p > *:not(.an) { position:relative; z-index:1; }
.p > .namezeile, .p > .fuss, .p > .chat-fuss, .p > .news-frage, .p > .nfuss, .p > .verlauf, .p > .unten, .p > .oben, .p > .zeichen { position:absolute; }
.p.vollbild > img { position:absolute; }
.p > .verlauf { z-index:1; } .p > .unten, .p > .oben { z-index:2; }
.fr-gross { font:700 104px/1.12 "Lora",Georgia,serif; letter-spacing:-.015em; }
.raster { display:grid; grid-template-columns:repeat(10, 44px); gap:10px 40px; margin-top:48px; }
.raster svg { width:44px; height:44px; display:block; color:#3a3632; }
.raster svg.an-ja { color:var(--gelb); }

/* Modell und Nachricht neu (13.10.2026) */
.wort { font:700 200px/.92 "Lora",Georgia,serif; letter-spacing:-.03em; }
.wortzeile { display:grid; grid-template-columns:auto 1fr; gap:40px; align-items:end; margin-top:80px; }
.wortzeile em { font-style:normal; padding-bottom:22px; font:500 34px/1.3 "Poppins",sans-serif; color:#d9d5cf; }
.wort.hl { color:var(--ink); }
.icons3 { display:grid; grid-template-columns:1fr 1fr 1.35fr; gap:30px; margin-top:120px; }
.icons3 div { display:flex; flex-direction:column; gap:30px; }
.icons3 svg { width:220px; height:220px; stroke-width:1.2; }
.icons3 b { font:700 50px/1 "Lora",Georgia,serif; }
.icons3 span { font:500 28px/1.35 "Poppins",sans-serif; }
.band2 { padding:0; grid-template-rows:1fr 1fr; }
.band2:target { display:grid; }
.band2 > div { padding:70px 84px; display:flex; flex-direction:column; justify-content:center; }
.band2 .oben { background:var(--hell); }
.band2 .unten { background:var(--gelb); }
.band2 small { font:700 26px/1 "Poppins",sans-serif; letter-spacing:.16em; text-transform:uppercase; }
.band2 p { margin-top:30px; font:700 74px/1.12 "Lora",Georgia,serif; }
.band2 .oben p { color:#a8a39c; text-decoration:line-through; text-decoration-thickness:6px; }
.nachricht { flex-direction:column; }
.nachricht:target { display:flex; }
.nz { font:700 30px/1 "Poppins",sans-serif; color:#8a857e; }
.nfuss { position:absolute; left:84px; right:84px; bottom:90px; font:700 66px/1.1 "Lora",Georgia,serif; color:#fff; }
.nb1 { margin-top:24px; max-width:720px; padding:34px 40px; border-radius:36px 36px 36px 10px; background:#2b2826; color:#d9d5cf; font:500 40px/1.3 "Poppins",sans-serif; }
.nzeit { margin-top:90px; font:700 120px/1 "Lora",Georgia,serif; color:var(--gelb); }
.nb2 { margin-top:28px; align-self:flex-start; padding:48px 58px; border-radius:46px 46px 46px 12px; background:var(--gelb); color:var(--ink); font:700 92px/1.02 "Lora",Georgia,serif; }

/* Fünf Varianten je Typ (13.10.2026) */
.wort .hl { color:var(--ink); }
.foto-voll { padding:0; }
.foto-voll > img { position:absolute; inset:0; width:100%; height:100%; object-fit:cover; }
.chip { position:absolute; left:64px; top:64px; z-index:2; padding:16px 26px; border-radius:999px; background:rgba(26,24,23,.82); color:#fff; font:600 28px/1 "Poppins",sans-serif; }
.gelbbalken { position:absolute; left:0; right:0; bottom:0; z-index:2; padding:54px 84px 60px; background:var(--gelb); font:700 70px/1.1 "Lora",Georgia,serif; color:var(--ink); }
.riesen-anf { position:absolute; left:-30px; top:-700px; font:700 1300px/1 "Lora",Georgia,serif; color:var(--gelb); z-index:0; }
.zitat-w { position:absolute; left:84px; right:84px; bottom:180px; font:700 76px/1.14 "Lora",Georgia,serif; color:#fff; }
.zitat-quelle { position:absolute; left:84px; bottom:110px; font:500 30px/1 "Poppins",sans-serif; color:#a8a39c; }
.tisch { background:#2b2826; }
.postit { position:absolute; left:140px; top:250px; width:800px; height:800px; padding:90px 80px; background:var(--gelb); transform:rotate(-3deg); box-shadow:0 40px 80px rgba(0,0,0,.45); }
.postit p { font:700 92px/1.1 "Lora",Georgia,serif; color:var(--ink); }
.postit small { display:block; margin-top:50px; font:500 32px/1.3 "Poppins",sans-serif; color:var(--ink); }
.riesen-frage { position:absolute; right:-60px; bottom:-200px; font:700 1100px/1 "Lora",Georgia,serif; color:var(--ink); z-index:0; }
.jn { margin-top:90px; display:grid; gap:28px; }
.jn div { display:flex; align-items:center; gap:36px; padding:40px 44px; border:5px solid var(--ink); border-radius:24px; font:700 58px/1 "Lora",Georgia,serif; }
.jn div::before { content:""; flex:0 0 70px; height:70px; border:6px solid var(--ink); border-radius:14px; }
.skala { display:grid; grid-template-columns:repeat(10,1fr); gap:14px; margin-top:110px; }
.skala span { display:grid; place-items:center; aspect-ratio:1; border:4px solid #4a4642; border-radius:50%; font:700 40px/1 "Poppins",sans-serif; color:#fff; }
.skala-l { display:flex; justify-content:space-between; margin-top:26px; font:500 28px/1.3 "Poppins",sans-serif; color:#a8a39c; }
.weg { display:grid; grid-template-columns:1fr 330px 1fr; align-items:center; gap:24px; margin-top:110px; }
.weg .box { padding:70px 30px; border-radius:28px; text-align:center; font:700 70px/1 "Lora",Georgia,serif; }
.weg .heute { border:6px solid #fff; color:#fff; }
.weg .vision { background:var(--gelb); color:var(--ink); }
.weg .mitte { color:var(--gelb); text-align:center; }
.weg .mitte svg { width:300px; height:300px; display:block; margin:0 auto; }
.weg .mitte b { display:block; margin-top:16px; font:700 44px/1 "Lora",Georgia,serif; color:#fff; }
.dach { margin-top:90px; padding:36px; background:var(--ink); color:var(--gelb); text-align:center; font:700 60px/1 "Lora",Georgia,serif; border-radius:20px 20px 0 0; }
.saeulen { display:grid; grid-template-columns:repeat(3,1fr); gap:26px; margin-top:26px; }
.saeulen div { height:560px; padding:40px 26px; display:flex; align-items:flex-end; background:var(--ink); color:#fff; font:700 46px/1.15 "Lora",Georgia,serif; }
.karte-schief { position:absolute; left:110px; top:230px; width:860px; height:900px; padding:80px 76px; background:#fff; transform:rotate(2.5deg); box-shadow:0 36px 70px rgba(0,0,0,.22); }
.karte-schief small { font:700 26px/1 "Poppins",sans-serif; letter-spacing:.14em; text-transform:uppercase; color:#6b6762; }
.karte-schief p { margin-top:26px; font:700 70px/1.12 "Lora",Georgia,serif; }
.karte-schief ol { margin-top:56px; padding-left:0; list-style:none; counter-reset:n; }
.karte-schief li { counter-increment:n; display:flex; gap:28px; padding:28px 0; border-top:3px solid var(--linie); font:500 36px/1.3 "Poppins",sans-serif; }
.karte-schief li::before { content:counter(n); flex:0 0 56px; height:56px; display:grid; place-items:center; border-radius:50%; background:var(--gelb); font:700 28px/1 "Poppins",sans-serif; }
.zeitleiste { margin-top:90px; }
.zeitleiste div { display:grid; grid-template-columns:200px 1fr; gap:30px; align-items:baseline; padding:44px 0; border-top:2px solid #3a3734; }
.zeitleiste div:last-child { border-bottom:2px solid #3a3734; }
.zeitleiste b { font:700 64px/1 "Lora",Georgia,serif; color:var(--gelb); }
.zeitleiste span { font:600 44px/1.2 "Poppins",sans-serif; color:#fff; }
.nicht { margin-top:90px; list-style:none; }
.nicht li { display:flex; gap:40px; align-items:center; padding:46px 0; border-top:4px solid var(--ink); font:700 56px/1.15 "Lora",Georgia,serif; }
.nicht li:last-child { border-bottom:4px solid var(--ink); }
.nicht li svg { flex:0 0 90px; width:90px; height:90px; }
.zahl-riesig { position:absolute; left:-40px; top:30px; font:700 980px/.85 "Lora",Georgia,serif; letter-spacing:-.04em; color:var(--gelb); z-index:0; }
.balken { margin-top:80px; display:grid; gap:56px; }
.balken div p { font:600 36px/1.3 "Poppins",sans-serif; color:#fff; }
.balken i { display:block; height:110px; margin-top:22px; border-radius:12px; }
.balken b { display:block; margin-top:18px; font:700 90px/1 "Lora",Georgia,serif; }
.datum { margin-top:110px; font:700 210px/.9 "Lora",Georgia,serif; letter-spacing:-.02em; color:var(--gelb); }

.p > .chip, .p > .gelbbalken, .p > .riesen-anf, .p > .zitat-w, .p > .zitat-quelle, .p > .postit, .p > .riesen-frage, .p > .karte-schief, .p > .zahl-riesig { position:absolute; }
.p.foto-voll > img { position:absolute; z-index:0; }
.p.foto-voll > .an { z-index:1; }
.schwarz .hl, .frage-schwarz .h .hl { color:var(--ink); }
.skala { margin-top:200px !important; gap:16px; }
.skala span { font-size:44px; }
.skala-l { font-size:32px !important; margin-top:34px !important; }
.weg { margin-top:170px !important; }
.balken { margin-top:120px !important; gap:90px !important; }
.balken i { height:140px !important; }

/* Große Zahlen, Daten, Uhrzeiten in Poppins Bold (13.10.2026): Lora-Ziffern wirken bei Displaygröße unruhig */
.zahlkarte .zahl, .vollbild .zahl, .zahl-riesig, .datum, .nzeit, .balken b, .zeitleiste b { font-family:"Poppins",sans-serif !important; font-weight:700 !important; letter-spacing:-.04em !important; }
.zahl-riesig { letter-spacing:-.06em !important; }

/* Feedback 13.10.2026 */
.weg .mitte { position:relative; }
.weg .mitte b { position:absolute; left:0; right:0; top:100%; }
.venn { display:block; width:100%; margin-top:30px; }
.erfolg2 { display:block; width:100%; margin-top:40px; }
.wz5-liste { margin-top:250px !important; }
.seite-hell { background:#f3f1ee; }
.seite-hell .oeffnen { background:#fff; }
.seite-schwarz { background:var(--ink); color:#fff; }
.seite-schwarz .k { color:var(--gelb); }
.seite-schwarz .frage { background:var(--gelb); color:var(--ink); }
.seite-schwarz .frage small, .seite-schwarz .frage .zeichen { color:var(--ink); }
.seite-schwarz .block > small, .seite-schwarz .fuss { color:#a8a39c; }
.seite-schwarz .block li { border-color:#3a3734; color:#fff; }
.seite-schwarz .oeffnen { background:#2b2826; color:#fff; }
.seite-gelb { background:var(--gelb); }
.seite-gelb .block > small, .seite-gelb .fuss, .seite-gelb .nr { color:var(--ink); }
.seite-gelb .block li { border-color:rgba(26,24,23,.25); }
.seite-gelb .oeffnen { background:#fff; }
.p > .nein-block { position:absolute !important; }
.nein-block { position:absolute; left:84px; bottom:110px; right:84px; z-index:2; }
.nein-block p { font:700 64px/1.12 "Lora",Georgia,serif; color:#fff; }
.nein-block b { display:inline-block; margin-top:24px; padding:6px 30px 14px; border-radius:22px; background:var(--gelb); color:var(--ink); font:700 170px/1 "Lora",Georgia,serif; }

/* Posting im Posting (13.10.2026) – Aufbau der Volksfest-Kästen */
.kt { background:#ece9e5; padding:64px; }
.kt:target { display:block; }
.kt-karte { position:relative; height:100%; display:flex; flex-direction:column; border-radius:34px; background:#fff; border:2px solid #ddd8d2; overflow:hidden; }
.kt-kopf { display:flex; align-items:center; gap:22px; padding:28px 34px; }
.kt-av { width:72px; height:72px; flex:0 0 72px; border-radius:50%; overflow:hidden; display:grid; place-items:center; background:#ece9e5; }
.kt-av img { width:100%; height:100%; object-fit:cover; }
.kt-av svg { width:40px; height:40px; color:#6b6762; }
.kt-kopf b { display:block; font:600 32px/1.2 "Poppins",sans-serif; color:var(--ink); }
.kt-kopf small { display:block; margin-top:4px; font:400 24px/1.2 "Poppins",sans-serif; color:#8a857e; }
.kt-farbe { position:relative; flex:1; display:flex; flex-direction:column; justify-content:space-between; padding:52px 54px; }
.kt-farbe small { font:700 24px/1 "Poppins",sans-serif; letter-spacing:.14em; text-transform:uppercase; }
.kt-farbe p { max-width:76%; font:700 80px/1.08 "Lora",Georgia,serif; letter-spacing:-.02em; }
.kt-farbe .kt-z { position:absolute; right:44px; bottom:44px; width:130px; height:130px; }
.kt-farbe .kt-z svg { width:100%; height:100%; }
.kt-gelb { background:var(--gelb); color:var(--ink); }
.kt-schwarz { background:var(--ink); color:#fff; }
.kt-schwarz small, .kt-schwarz .kt-z { color:var(--gelb); }
.kt-hell { background:#f3f1ee; color:var(--ink); }
.kt-text { padding:30px 34px 36px; font:400 30px/1.45 "Poppins",sans-serif; color:#3d3a37; }
"""


def fuss(links="Daniel Ströbel", weiss=False, seite=""):
    logo = "/assets/empiria-logo-weiss.svg" if weiss else "/assets/empiria-logo.svg"
    rechts = '<span>%s</span>' % seite if seite else '<img src="%s" alt="empiria">' % logo
    return '<div class="fuss"><span>%s</span>%s</div>' % (links, rechts)


def zeichen(svg, right=None, top=None, size=None):
    stil = ' style="right:%dpx;top:%dpx;width:%dpx;height:%dpx"' % (right, top, size, size) if size else ""
    return '<div class="zeichen"%s>%s</div>' % (stil, svg)


def foto_posting(pid, bild, pos, kicker, headline, sym, sw=False, links="Daniel Ströbel"):
    return """<section class="p" id="%s">
  <div class="karte%s" style="--pos:%s"><img src="%s%s" alt=""></div>
  <p class="k">%s</p>
  <p class="h m">%s</p>
  %s
  %s
</section>""" % (pid, " sw" if sw else "", pos, B, bild, kicker, headline, zeichen(sym, 84, 720, 92), fuss(links))


def doc_seite(nr, titel, frage, einwaende, eroeffnung):
    lis = "".join("<li>%s</li>" % e for e in einwaende)
    return """<section class="p" id="d%d">
  <div class="seitenkopf"><p class="k">%s</p><span class="nr">0%d / 04</span></div>
  <div class="frage"><small>Die Frage</small><p>%s</p>%s</div>
  <div class="block"><small>Typische Einwände</small><ul>%s</ul></div>
  <div class="block"><small>So eröffnest du</small><p class="oeffnen">%s</p></div>
  %s
</section>""" % (nr + 1, titel, nr, frage, zeichen(X), lis, eroeffnung, fuss("Ein Thema. Vier Gegenüber.", seite="%d / 6" % (nr + 1)))


teile = [
    foto_posting("p1", "entwurf-e1.jpg", "50% 38%", "Vor jeder Vorstandsvorlage",
                 'Erst drei Fragen, dann die <span class="hl">Folie.</span>', X, sw=True),
    foto_posting("p2", "entwurf-e2.jpg", "35% 40%", "Strategie im Alltag",
                 'Was entscheidest du diese Woche <span class="hl">anders?</span>', F),
    """<section class="p gelbgrund" id="p3">
  <div class="rund" style="margin-top:60px"><img src="%sentwurf-e3.jpg" alt=""></div>
  <p class="zitat">„Er stellt Fragen, zeichnet, dreht das iPad um und sagt: Eigentlich ist es doch so.“</p>
  <p class="quelle">Ein befreundeter Vorstand über meine Arbeit</p>
  %s
</section>""" % (B, fuss().replace('<div class="fuss">', '<div class="fuss" style="color:#1a1817">')),
    foto_posting("p4", "entwurf-e4.jpg", "30% 75%", "Die Neugründungs-Frage",
                 'Was würdest du heute nicht mehr <span class="hl">machen?</span>', O),
    """<section class="p schwarz" id="p5">
  <p class="k">Am Ende jeder Abstimmung</p>
  <div class="liste"><div><small>01</small>Wer?</div><div><small>02</small>Bis wann?</div><div><small>03</small>In welcher Form?</div></div>
  <p class="text" style="color:#d9d5cf;margin-top:56px">Zwei Minuten, damit das Thema beim nächsten Termin eine Stufe weiter ist.</p>
  %s
</section>""" % fuss(weiss=True),
    """<section class="p" id="d1">
  <p class="k">Dokument · 6 Seiten</p>
  <p class="h" style="font-size:118px;margin-top:60px">Ein Thema.<br>Vier <span class="hl">Gegenüber.</span></p>
  <p class="text">Was Vorstand, Aufsichtsrat, Vertrieb und dein Team von dir wissen wollen – und wie du das Gespräch eröffnest.</p>
  %s
  <div class="fuss"><span class="autor"><span class="rund"><img src="%sentwurf-e6.jpg" alt=""></span><span><b>Daniel Ströbel</b>Strategie in Wirkung bringen</span></span><img src="/assets/empiria-logo.svg" alt="empiria"></div>
</section>""" % (zeichen(X, 84, 860, 230), B),
    doc_seite(1, "Der Vorstand", "Welche Entscheidung brauchst du von mir, und was riskiere ich damit?",
              ["„Warum gerade jetzt?“", "„Was passiert, wenn wir es lassen?“"],
              "„Ich brauche heute eine Entscheidung zu einer Frage. Meine Empfehlung ist …, das Risiko begrenzen wir auf …“"),
    doc_seite(2, "Der Aufsichtsrat", "Passt das zu unserer Strategie, und bleibt es steuerbar?",
              ["„Woran messen wir, ob es wirkt?“", "„Wer trägt die Verantwortung?“"],
              "„Das Vorhaben zahlt auf unsere Stoßrichtung … ein. Verantwortlich ist …, berichtet wird quartalsweise an drei Kennzahlen.“"),
    doc_seite(3, "Der Vertrieb", "Was habe ich davon, und wie erkläre ich es meinem Kunden in einem Satz?",
              ["„Noch ein Thema mehr.“", "„Das versteht mein Kunde nicht.“"],
              "„Ab … hast du im Kundengespräch ein Argument mehr, und es passt in einen Satz: …“"),
    doc_seite(4, "Dein Team", "Was ändert sich ab Montag für mich?",
              ["„Wann sollen wir das auch noch machen?“", "„Das hatten wir doch schon mal.“"],
              "„Ab Montag ändert sich für euch genau eine Sache: … Dafür fällt … weg.“"),
    """<section class="p gelbgrund" id="d6">
  <p class="k">Vor deiner nächsten Vorlage</p>
  <p class="h m">Hast du alle vier Fragen beantwortet?</p>
  <ul class="check" style="margin-top:64px"><li>Welche Entscheidung brauche ich vom Vorstand?</li><li>Wie bleibt es für den Aufsichtsrat steuerbar?</li><li>Welchen Satz sagt der Vertrieb seinem Kunden?</li><li>Was ändert sich für mein Team ab Montag?</li></ul>
  <div class="fuss" style="color:#1a1817"><span>Daniel Ströbel · Strategie in Wirkung bringen</span><span>6 / 6</span></div>
</section>""",
]


# Serien-Beispiele für die Strategie-Seite
teile += [
    """<section class="p vollbild" id="s1">
  <img src="%sentwurf-e3.jpg" alt="" style="filter:grayscale(1) contrast(1.06);--pos:50%% 20%%">
  <div class="verlauf"></div>
  <div class="unten"><p class="satz">„Er stellt Fragen, zeichnet, dreht das iPad um und sagt: Eigentlich ist es doch so.“</p><p class="wer">— ein befreundeter Vorstand über meine Arbeit</p></div>
</section>""" % B,
    """<section class="p vollbild" id="n1">
  <img src="%sentwurf-e6.jpg" alt="" style="--pos:30%% 30%%">
  <div class="verlauf" style="height:72%%"></div>
  <p class="k oben">Eingeordnet</p>
  <div class="unten"><p class="zahl">77 %%</p><p class="satz" style="margin-top:18px">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p><p class="wer">Quelle: Wieselhuber · Was das für deinen Bereich heißt, im Text</p></div>
</section>""" % B,
]

# Postingtypen ohne Foto (13.10.2026) – Inhalte aus dem Interview
teile += [
    """<section class="p karte-frage" id="k1">
  <p class="k">Die Frage</p>
  <p class="h">Kann jeder in deinem Bereich sagen, wie ihr <span class="hl">erfolgreich</span> seid?</p>
  <p class="text" style="margin-top:44px">Und was sein eigener Beitrag dazu ist.</p>
  %s
  <p class="namezeile">Daniel Ströbel</p>
</section>""" % zeichen(F, 88, 1040, 110),
    """<section class="p" id="m1">
  <p class="k">Das Modell</p>
  <p class="h m" style="margin-top:28px">Was ein Vorstand wissen <span class="hl">muss.</span></p>
  <div class="modell">
    <div class="stufe"><b>Why</b><div><p>Warum beschäftigen wir uns damit?</p><small>Ausgangssituation · Problem · Lösung</small></div></div>
    <div class="stufe"><b>How</b><div><p>Wie gehen wir grundsätzlich vor?</p><small>Grundsätzlich, nicht im Detail</small></div></div>
    <div class="stufe gelb-b"><b>Next</b><div><p>Was ist der konkrete nächste Schritt?</p><small>Damit es vorangeht</small></div></div>
  </div>
  <p class="namezeile">Daniel Ströbel</p>
</section>""",
    """<section class="p schwarz zahlkarte" id="z1">
  <p class="k">Eingeordnet</p>
  <p class="zahl">77&nbsp;%</p>
  <p class="satz">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p>
  <p class="quelle2">Quelle: Wieselhuber · Was das für einen Bereich heißt, steht im Text.</p>
  <p class="namezeile">Daniel Ströbel</p>
</section>""",
    """<section class="p gelbgrund satzkarte" id="t1">
  <p class="k">Der Satz</p>
  <p class="zitat">„Es hilft doch nichts, wenn nur ich das hier verstanden habe.“</p>
  <p class="quelle">— ein Vorstand</p>
  <p class="namezeile" style="color:#1a1817">Daniel Ströbel</p>
</section>""",
]

# Varianten je Postingtyp (13.10.2026) – Inhalte aus Interview und Postings
import sys as _sys
_sys.path.insert(0, os.path.join(HIER, ".."))
from e2_lucide import ICONS as _LUC
def luc(name):
    return '<svg class="luc" viewBox="0 0 24 24" aria-hidden="true">%s</svg>' % _LUC[name]

teile += [
    """<section class="p grau" id="c1">
  <p class="chat-zeit" style="margin-top:20px">Freitag · 14:20 · Anfrage eines Vorstands</p>
  <div class="chat-blase">Kannst du dir die Folien bis morgen früh ansehen? Es muss sitzen.</div>
  <p class="chat-zeit" style="margin-top:44px">22:25</p>
  <div class="chat-blase du">Vielen Dank!<br>Passt. Lass es so.<small>Vorstand</small></div>
  <p class="chat-fuss">Aus vier Folien wurde eine.</p>
</section>""",
    """<section class="p schwarz frage-schwarz" id="k2">
  <p class="k">Strategie im Alltag</p>
  <div class="riesig">%s</div>
  <p class="h">Was entscheidest du diese Woche wegen der Strategie <span class="hl">anders?</span></p>
</section>""" % luc("compass"),
    """<section class="p gelbgrund" id="m2">
  <p class="k">Strategie im Alltag</p>
  <p class="h">Was jeder Bereich braucht.</p>
  <div class="drei">
    <div>%s<p><b>Rolle</b><span>Wofür stehe ich und mein Bereich?</span></p></div>
    <div>%s<p><b>Richtung</b><span>Wie wollen wir wahrgenommen werden?</span></p></div>
    <div>%s<p><b>Handwerkszeug</b><span>Wie kommen wir dort hin?</span></p></div>
  </div>
</section>""" % (luc("flag"), luc("compass"), luc("wrench")),
    """<section class="p" id="m3">
  <p class="k">Strategie im Alltag</p>
  <p class="h m">Woran du ein Zielbild <span class="hl">erkennst.</span></p>
  <div class="vn">
    <div class="vor"><small>Ohne</small><ul><li>Agendapunkte werden aufgezählt</li><li>Jeder verteidigt sein Thema</li><li>Am Ende ein Kompromiss</li></ul></div>
    <div class="nach"><small>Mit</small><ul><li>Das Ziel in einem Satz</li><li>Jeder kennt das Warum</li><li>Am Ende eine Entscheidung</li></ul></div>
  </div>
</section>""",
    """<section class="p gelbgrund" id="w2">
  <p class="k">Vor jeder Vorstandsvorlage</p>
  <ul class="check2"><li>Wen brauche ich?</li><li>Wen habe ich übersehen?</li><li>An wem richte ich es aus?</li></ul>
  <p class="text" style="color:#1a1817;margin-top:70px;font-size:40px;font-weight:600">Erst diese drei Fragen. Dann die Folie.</p>
</section>""",
    """<section class="p schwarz" id="z2">
  <p class="k">Branche eingeordnet</p>
  <div class="news"><small>Branche · 2026</small><b>Versicherer planen kein Personalwachstum. Die Effizienz soll mit KI kommen.</b></div>
  <p class="news-frage">Was heißt das für deinen <span class="hl">Bereich?</span></p>
</section>""",
]

# Überarbeitung 13.10.2026: angeschnittenes Markenzeichen je Baustein, Raster als Datengrafik
def anschnitt(svg, groesse, rechts, unten, farbe):
    return '<div class="an" style="width:%dpx;height:%dpx;right:%dpx;bottom:%dpx;color:%s">%s</div>' % (groesse, groesse, rechts, unten, farbe, svg)

def ersetze(pid, html):
    for i, t in enumerate(teile):
        if 'id="%s"' % pid in t:
            teile[i] = html
            return
    raise KeyError(pid)

NAME = '<p class="namezeile">Daniel Ströbel</p>'
ersetze("k1", """<section class="p" id="k1">
  <p class="fr-gross" style="margin-top:40px">Kann jeder in deinem Bereich sagen, wie ihr <span class="hl">erfolgreich</span> seid?</p>
  <p class="text" style="margin-top:40px;font-size:38px">Und was sein eigener Beitrag dazu ist.</p>
  %s%s
</section>""" % (anschnitt(F, 880, -300, -250, "#1a1817"), NAME))
ersetze("k2", """<section class="p schwarz frage-schwarz" id="k2">
  %s
  <p class="h">Was entscheidest du diese Woche wegen der Strategie <span class="hl">anders?</span></p>
</section>""" % anschnitt(F, 820, -330, 560, "#fff400"))
ersetze("t1", """<section class="p gelbgrund satzkarte" id="t1">
  <p class="zitat" style="margin-top:60px">„Es hilft doch nichts, wenn nur ich das hier verstanden habe.“</p>
  <p class="quelle">— ein Vorstand</p>
  %s
  <p class="namezeile" style="color:#1a1817">Daniel Ströbel</p>
</section>""" % anschnitt(F, 700, -220, -190, "#1a1817"))
zellen = "".join('<svg viewBox="0 0 232.44 232.44" class="%s">%s</svg>' % ("an-ja" if i < 77 else "", F[F.index(">") + 1:F.rindex("</svg>")]) for i in range(100))
ersetze("z1", """<section class="p schwarz zahlkarte" id="z1">
  <p class="zahl" style="margin-top:20px">77&nbsp;%</p>
  <p class="satz" style="margin-top:24px">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p>
  <div class="raster">""" + zellen + """</div>
  <p class="quelle2" style="position:absolute;left:84px;bottom:70px">Quelle: Wieselhuber · Was das für deinen Bereich heißt, steht im Text.</p>
</section>""")
ersetze("p5", """<section class="p schwarz" id="p5">
  <p class="k">Am Ende jeder Abstimmung</p>
  <div class="liste"><div><small>01</small>Wer?</div><div><small>02</small>Bis wann?</div><div><small>03</small>In welcher Form?</div></div>
  <p class="text" style="color:#d9d5cf;margin-top:56px;max-width:640px">Zwei Minuten, damit das Thema beim nächsten Termin eine Stufe weiter ist.</p>
  %s
  <p class="namezeile">Daniel Ströbel</p>
</section>""" % anschnitt(X, 560, -170, -150, "#fff400"))
ersetze("w2", """<section class="p gelbgrund" id="w2">
  <p class="k">Vor jeder Vorstandsvorlage</p>
  <ul class="check2"><li>Wen brauche ich?</li><li>Wen habe ich übersehen?</li><li>An wem richte ich es aus?</li></ul>
  <p class="text" style="color:#1a1817;margin-top:60px;font-size:40px;font-weight:600;max-width:560px">Erst diese drei Fragen. Dann die Folie.</p>
  %s
</section>""" % anschnitt(X, 520, -150, -150, "#1a1817"))

# Modell und Nachricht neu (13.10.2026)
ersetze("m1", """<section class="p schwarz" id="m1">
  <p class="k">Was ein Vorstand wissen muss</p>
  <div style="margin-top:70px">
    <div class="wortzeile"><p class="wort">Why.</p><em>Warum beschäftigen wir uns damit?</em></div>
    <div class="wortzeile"><p class="wort">How.</p><em>Wie gehen wir grundsätzlich vor?</em></div>
    <div class="wortzeile"><p class="wort"><span class="hl" style="padding:0 .08em">Next.</span></p><em>Was ist der nächste Schritt?</em></div>
  </div>
  <p class="namezeile">Daniel Ströbel</p>
</section>""")
ersetze("m2", """<section class="p gelbgrund" id="m2">
  <p class="h" style="margin-top:20px">Was jeder Bereich braucht.</p>
  <div class="icons3">
    <div>%s<b>Rolle</b><span>Wofür stehen wir?</span></div>
    <div>%s<b>Richtung</b><span>Wohin wollen wir?</span></div>
    <div>%s<b>Handwerkszeug</b><span>Wie kommen wir hin?</span></div>
  </div>
  %s
  <p class="namezeile" style="color:#1a1817">Daniel Ströbel</p>
</section>""" % (luc("flag"), luc("compass"), luc("wrench"), anschnitt(F, 620, -230, -230, "#1a1817")))
ersetze("m3", """<section class="p band2" id="m3">
  <div class="oben"><small>Ohne Zielbild</small><p>Jeder verteidigt sein Thema. Am Ende ein Kompromiss.</p></div>
  <div class="unten"><small>Mit Zielbild</small><p>Jeder kennt das Warum. Am Ende eine Entscheidung.</p></div>
</section>""")
ersetze("c1", """<section class="p schwarz nachricht" id="c1">
  <p class="nz">14:20 · Anfrage eines Vorstands</p>
  <div class="nb1">Kannst du dir die Folien bis morgen früh ansehen? Es muss sitzen.</div>
  <p class="nzeit">22:25</p>
  <div class="nb2">Passt. Lass es so.</div>
  <p class="nfuss">Aus vier Folien wurde eine.</p>
</section>""")

# Fünf Varianten je Typ (13.10.2026)
def vb(bild, pos="50% 50%", sw=False):
    return '<img src="%s%s" alt="" style="object-position:%s;%s">' % (B, bild, pos, "filter:grayscale(1) contrast(1.06);" if sw else "")
ERFOLG = """<svg viewBox="0 0 912 700" style="width:100%;margin-top:60px;display:block">
<g stroke="#1a1817" stroke-width="4" fill="none"><line x1="456" y1="350" x2="160" y2="120"/><line x1="456" y1="350" x2="760" y2="120"/><line x1="456" y1="350" x2="130" y2="560"/><line x1="456" y1="350" x2="780" y2="560"/><line x1="456" y1="350" x2="456" y2="620" stroke-dasharray="14 14"/></g>
<g font-family="Poppins" font-weight="600" font-size="30" text-anchor="middle" fill="#1a1817">
<circle cx="160" cy="120" r="92" fill="#fff" stroke="#1a1817" stroke-width="5"/><text x="160" y="130">Vorstand</text>
<circle cx="760" cy="120" r="92" fill="#fff" stroke="#1a1817" stroke-width="5"/><text x="760" y="130">Team</text>
<circle cx="130" cy="560" r="92" fill="#fff" stroke="#1a1817" stroke-width="5"/><text x="130" y="570">Vertrieb</text>
<circle cx="780" cy="560" r="92" fill="#fff" stroke="#1a1817" stroke-width="5"/><text x="780" y="560">Nachbar-</text><text x="780" y="596">bereich</text>
<circle cx="456" cy="620" r="70" fill="#fff400" stroke="#1a1817" stroke-width="5" stroke-dasharray="12 10"/><text x="456" y="630" font-size="44">?</text>
<circle cx="456" cy="350" r="120" fill="#1a1817"/><text x="456" y="368" fill="#fff400" font-family="Lora" font-weight="700" font-size="56">Du</text></g></svg>"""
X_IC = '<svg viewBox="0 0 232.44 232.44" aria-hidden="true">' + X[X.index(">") + 1:X.rindex("</svg>")] + '</svg>'
teile += [
    """<section class="p foto-voll" id="sz3">%s<span class="chip">Dienstag, 7:40 · Workshopraum</span></section>""" % vb("voll-b1.jpg", "0% 45%"),
    """<section class="p foto-voll" id="sz4">%s%s</section>""" % (vb("voll-e2.jpg", "30% 40%"), anschnitt(F, 560, -170, -140, "#fff400")),
    """<section class="p foto-voll" id="sz5">%s<p class="gelbbalken">Das wichtigste Wort in jeder Strategie.</p></section>""" % vb("voll-e4.jpg", "28% 30%"),
    """<section class="p schwarz" id="sa3"><span class="riesen-anf">„</span>
  <p class="zitat-w">„Bei uns kommen viel zu oft Themen auf der falschen&nbsp;Flugebene&nbsp;an.“</p><p class="zitat-quelle">— ein Vorstand</p></section>""",
    """<section class="p tisch" id="sa4"><div class="postit"><p>„Daniel, ich brauche dich mal nur ganz kurz.“</p><small>Wenn ein Vorstand so anruft, brennt es.</small></div></section>""",
    """<section class="p" id="sa5">%s<p class="zitat" style="margin-top:430px">„Führung macht einsam. Je höher du kommst, desto weniger sagt dir jemand die <span class="hl">Wahrheit.</span>“</p><p class="quelle">— ein ehemaliger Vorstand</p>%s</section>""" % (anschnitt(F, 520, -170, 960, "#1a1817"), NAME),
    """<section class="p gelbgrund" id="fr3"><span class="riesen-frage">?</span><p class="fr-gross" style="margin-top:40px;max-width:820px">Wie würdest du deinen Bereich heute neu gründen?</p>%s</section>""" % NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"'),
    """<section class="p" id="fr4"><p class="fr-gross" style="margin-top:40px;font-size:88px">Weiß jeder in deinem Team, was er diese Woche für die Strategie tut?</p>
  <div class="jn"><div>Ja.</div><div>Ehrlich gesagt: nein.</div></div>%s%s</section>""" % (anschnitt(F, 520, -170, -170, "#1a1817"), NAME),
    """<section class="p schwarz" id="fr5"><p class="fr-gross" style="margin-top:40px;color:#fff;font-size:92px">Wie sehr kommt eure Strategie im <span class="hl">Alltag</span> an?</p>
  <div class="skala">""" + "".join("<span>%d</span>" % i for i in range(1, 11)) + """</div><div class="skala-l"><span>steht auf der Folie</span><span>prägt den Montag</span></div>%s</section>""" % NAME,
    """<section class="p schwarz" id="mo3"><p class="h m" style="color:#fff">Strategie ist die <span class="hl">Verbindung.</span></p>
  <div class="weg"><div class="box heute">Heute</div><div class="mitte">%s<b>Strategie</b></div><div class="box vision">Vision</div></div>
  <p class="text" style="color:#fff;margin-top:150px;font:700 54px/1.2 Lora,Georgia,serif">Ist klar, wo du hinwillst und wo du stehst, ergibt sich der Weg fast von allein.</p>%s</section>""" % (F, NAME),
    """<section class="p" id="mo4"><p class="h m">Worauf eine Führungsrolle steht.</p><div class="dach">Die Rolle</div>
  <div class="saeulen"><div>Fach&shy;expertise</div><div>Führungs&shy;kompetenz</div><div>Geschäfts&shy;modell verstehen</div></div>%s</section>""" % NAME,
    """<section class="p" id="mo5"><p class="h m">Wen brauchst du – und wen hast du <span class="hl">übersehen?</span></p>%s%s</section>""" % (ERFOLG, NAME),
    """<section class="p gelbgrund" id="wz3"><div class="karte-schief"><small>Die Neugründungs-Frage</small><p>Wie würdest du deinen Bereich heute neu aufbauen?</p>
  <ol><li>Würdest du die Aufgaben noch genauso zuschneiden?</li><li>Säßest du an derselben Stelle der Wertschöpfung?</li><li>Würdest du dieselben Zielgruppen bedienen?</li></ol></div></section>""",
    """<section class="p schwarz" id="wz4"><p class="h m" style="color:#fff">Die ersten drei Minuten jedes Termins.</p>
  <div class="zeitleiste"><div><b>0:00</b><span>Worum geht es heute?</span></div><div><b>1:00</b><span>Mit welchem Ergebnis gehen wir raus?</span></div><div><b>2:00</b><span>Was müssen wir dafür entscheiden?</span></div></div>%s</section>""" % NAME,
    """<section class="p gelbgrund" id="wz5"><p class="k">Gehört nicht in die Vorstandsvorlage</p>
  <ul class="nicht"><li>%sJedes Detail, das du kennst</li><li>%sDie Geschichte des Projekts</li><li>%sFünf Optionen ohne Empfehlung</li></ul>%s</section>""" % (X_IC, X_IC, X_IC, NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"')),
    """<section class="p schwarz" id="ei3"><span class="zahl-riesig">11</span>
  <p style="position:absolute;left:84px;right:84px;bottom:210px;font:700 76px/1.12 Lora,Georgia,serif;color:#fff">Prozent sagen: Die Mitarbeitenden verstehen die Strategie.</p>
  <p class="quelle2" style="position:absolute;left:84px;bottom:110px">Quelle: Wieselhuber, branchenübergreifend</p></section>""",
    """<section class="p schwarz" id="ei4"><p class="h m" style="color:#fff">Strategie gegen Tagesgeschäft.</p>
  <div class="balken"><div><p>Das Tagesgeschäft verdrängt strategische Projekte</p><i style="width:77%;background:#fff400"></i><b style="color:#fff400">77 %</b></div>
  <div><p>Die Mitarbeitenden verstehen die Strategie</p><i style="width:11%;background:#fff"></i><b style="color:#fff">11 %</b></div></div>
  <p class="quelle2" style="position:absolute;left:84px;bottom:110px">Quelle: Wieselhuber, branchenübergreifend</p></section>""",
    """<section class="p schwarz" id="ei5"><p class="k">AI Act · vorläufiger Termin</p><p class="datum">02.12.<br>2027</p>
  <p style="margin-top:60px;font:700 64px/1.14 Lora,Georgia,serif;color:#fff">Ab dann gelten die Hochrisiko-Pflichten – auch für KI in der Tarifierung.</p>
  <p class="text" style="color:#d9d5cf">Wer ist in deinem Bereich dafür zuständig?</p></section>""",
    """<section class="p gelbgrund" id="dk2"><p class="k">Dokument · 6 Seiten</p><p class="h" style="font-size:118px;margin-top:60px">Ein Thema.<br>Vier Gegenüber.</p>
  <p class="text" style="color:#1a1817">Was Vorstand, Aufsichtsrat, Vertrieb und Team wissen wollen.</p>%s</section>""" % anschnitt(X, 620, -190, -180, "#1a1817"),
    """<section class="p schwarz" id="dk3"><p class="k">Dokument · 6 Seiten</p><p class="h" style="font-size:118px;margin-top:60px;color:#fff">Ein Thema.<br>Vier <span class="hl">Gegenüber.</span></p>
  <p class="text" style="color:#d9d5cf">Was Vorstand, Aufsichtsrat, Vertrieb und Team wissen wollen.</p>%s</section>""" % anschnitt(X, 620, -190, -180, "#fff400"),
    """<section class="p foto-voll vollbild" id="dk4">%s<div class="verlauf" style="height:58%%"></div><div class="unten"><p class="k" style="color:#fff">Dokument · 6 Seiten</p><p class="satz" style="font-size:96px;margin-top:24px">Ein Thema. Vier Gegenüber.</p></div></section>""" % vb("entwurf-e6.jpg", "40% 30%"),
    """<section class="p" id="dk5"><span class="zahl-riesig" style="color:#1a1817;left:auto;right:-40px;top:auto;bottom:-140px;font-size:900px">4</span>
  <p class="k">Dokument · 6 Seiten</p><p class="h" style="margin-top:50px;max-width:600px">Gegenüber, die du überzeugen musst.</p>
  <p class="text" style="max-width:520px">Vorstand, Aufsichtsrat, Vertrieb, Team – und was jedes davon wissen will.</p></section>""",
]

# Feedback 13.10.2026: Modell D/E neu, Werkzeug E mittig, Dokument-Innenseiten im Wechsel, Szene F
VENN = """<svg class="venn" viewBox="0 0 912 860"><g fill="none" stroke="#1a1817" stroke-width="7">
<circle cx="330" cy="330" r="245"/><circle cx="582" cy="330" r="245"/><circle cx="456" cy="548" r="245"/></g>
<g font-family="Lora" font-weight="700" font-size="38" fill="#1a1817" text-anchor="middle">
<text x="225" y="250">Fach-</text><text x="225" y="296">expertise</text>
<text x="690" y="250">Führungs-</text><text x="690" y="296">kompetenz</text>
<text x="456" y="690">Geschäftsmodell</text><text x="456" y="740">verstehen</text></g>
<rect x="356" y="370" width="200" height="74" rx="18" fill="#fff400"/>
<text x="456" y="420" font-family="Poppins" font-weight="700" font-size="34" text-anchor="middle" fill="#1a1817">Die Rolle</text></svg>"""
def _knoten(x, y, ic, label, gelb=False):
    fill = "#fff400" if gelb else "none"
    col = "#1a1817" if gelb else "#fff"
    return ('<circle cx="%d" cy="%d" r="88" fill="%s" stroke="%s" stroke-width="5"%s/>' % (x, y, fill, "#fff400" if gelb else "#fff", ' stroke-dasharray="14 12"' if gelb else "")
            + '<g transform="translate(%d %d) scale(3.2)" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (x - 38, y - 38, col, _LUC[ic])
            + '<text x="%d" y="%d" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="32" fill="#fff">%s</text>' % (x, y + 136, label))
ERFOLG2 = ("""<svg class="erfolg2" viewBox="0 0 912 820"><g stroke="#4a4642" stroke-width="4"><line x1="456" y1="400" x2="150" y2="130"/><line x1="456" y1="400" x2="762" y2="130"/><line x1="456" y1="400" x2="150" y2="620"/><line x1="456" y1="400" x2="762" y2="620"/></g>"""
   + _knoten(150, 130, "briefcase", "Vorstand") + _knoten(762, 130, "users", "Team") + _knoten(150, 620, "handshake", "Vertrieb") + _knoten(762, 620, "search", "Übersehen?", True)
   + """<circle cx="456" cy="400" r="118" fill="#fff400"/><text x="456" y="420" text-anchor="middle" font-family="Lora" font-weight="700" font-size="60" fill="#1a1817">Du</text></svg>""")
ersetze("mo4", """<section class="p" id="mo4"><p class="h m">Worauf eine Führungsrolle steht.</p>%s%s</section>""" % (VENN, NAME))
ersetze("mo5", """<section class="p schwarz" id="mo5"><p class="h m" style="color:#fff">Wen brauchst du – und wen hast du <span class="hl">übersehen?</span></p>%s%s</section>""" % (ERFOLG2, NAME))
for i, t in enumerate(teile):
    if 'id="wz5"' in t:
        teile[i] = t.replace('<ul class="nicht">', '<ul class="nicht wz5-liste">')
    for pid, kl in (("d3", "seite-hell"), ("d4", "seite-schwarz"), ("d5", "seite-gelb")):
        if '<section class="p" id="%s">' % pid in teile[i]:
            teile[i] = teile[i].replace('<section class="p" id="%s">' % pid, '<section class="p %s" id="%s">' % (kl, pid))
teile.append("""<section class="p foto-voll vollbild" id="sz6">%s<div class="verlauf" style="height:60%%"></div><div class="nein-block"><p>Das wichtigste Wort in jeder Strategie?</p><b>Nein.</b></div></section>""" % vb("voll-e4.jpg", "28% 30%"))

# Posting im Posting (13.10.2026)
def kt(pid, av, name, unter, farbe, label, satz, zeichen_svg, text):
    return """<section class="p kt" id="%s"><div class="kt-karte">
  <div class="kt-kopf"><span class="kt-av">%s</span><span><b>%s</b><small>%s</small></span></div>
  <div class="kt-farbe kt-%s"><small>%s</small><p>%s</p><span class="kt-z">%s</span></div>
  <p class="kt-text">%s</p></div></section>""" % (pid, av, name, unter, farbe, label, satz, zeichen_svg, text)
teile += [
    kt("kt1", luc("user-round"), "Ein Vorstand", "Versicherer · im Gespräch", "gelb", "Der Satz",
       "„Es hilft doch nichts, wenn nur ich das hier verstanden habe.“", F,
       "Ein Vorstand allein bewegt nichts. Wie die Strategie in die Organisation kommt – im Text."),
    kt("kt2", luc("megaphone"), "Branchenmeldung", "Versicherungswirtschaft · 2026", "schwarz", "Eingeordnet",
       "Versicherer planen kein Personal&shy;wachstum.", F,
       "Die Effizienz soll mit KI kommen. Was das für deinen Bereich heißt – drei Fragen im Text."),
    kt("kt3", '<img src="/assets/ansprechpartner-daniel.webp" alt="">', "Daniel Ströbel", "Strategie in Wirkung bringen", "hell", "Die Frage",
       "Wie würdest du deinen Bereich heute neu gründen?", O,
       "Die Frage, mit der ich jedes Gespräch über die Zukunft eines Bereichs beginne."),
]

html = """<!doctype html>
<html lang="de"><head><meta charset="utf-8"><title>Postings empiria – Vorlage</title>
<link rel="stylesheet" href="/assets/fonts/fonts.local.css">
<style>/* Erzeugt von postings_vorlage_bauen.py – nicht von Hand ändern. */%s</style></head>
<body>
%s
</body></html>""" % (CSS, "\n\n".join(teile))

open(os.path.join(HIER, "postings-vorlage.html"), "w", encoding="utf-8").write(html)
print("Vorlage gebaut")
