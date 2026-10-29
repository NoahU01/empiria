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

/* Postingtyp „Die Skizze“ (13.10.2026) */
.sk-post { display:none; }
.sk-post:target { display:flex; flex-direction:column; }
.sk-post .sk { display:block; width:100%; margin-top:auto; }
.sk-post .h { font-size:80px; line-height:1.1; }
.sk-c { background:#f3f1ee; }
.sk-mark { background:linear-gradient(transparent 55%, var(--gelb) 55%, var(--gelb) 92%, transparent 92%); padding:0 .06em; }

/* Skizzen (13.10.2026) */
@font-face { font-family:"Caveat"; font-weight:700; src:url(/assets/projekte/medienkonzept/caveat-700.woff2) format("woff2"); }
.sk2 { padding:0; }
.sk2:target { display:block; }
.p.sk2 > div { position:absolute; }

.vollbild .satz .hl { color:var(--ink); }
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
    fill = "#fff400" if gelb else "#1a1817"  # gefüllt, damit die Verbindungslinien im Kreis verschwinden
    col = "#1a1817" if gelb else "#fff"
    return ('<circle cx="%d" cy="%d" r="88" fill="%s" stroke="%s" stroke-width="5"%s/>' % (x, y, fill, "#fff400" if gelb else "#fff", ' stroke-dasharray="14 12"' if gelb else "")
            + '<g transform="translate(%d %d) scale(3.2)" fill="none" stroke="%s" stroke-width="1.6" stroke-linecap="round" stroke-linejoin="round">%s</g>' % (x - 38, y - 38, col, _LUC[ic])
            + '<text x="%d" y="%d" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="32" fill="#fff">%s</text>' % (x, y + 136, label))
ERFOLG2 = ("""<svg class="erfolg2" viewBox="0 0 912 820"><g stroke="#4a4642" stroke-width="4"><line x1="456" y1="400" x2="150" y2="130"/><line x1="456" y1="400" x2="762" y2="130"/><line x1="456" y1="400" x2="150" y2="620"/><line x1="456" y1="400" x2="762" y2="620"/></g>"""
   + _knoten(150, 130, "briefcase", "Vorstand") + _knoten(762, 130, "users", "Team") + _knoten(150, 620, "handshake", "Vertrieb") + _knoten(762, 620, "search", "Übersehen?", True)
   + """<circle cx="456" cy="400" r="118" fill="#fff400"/><text x="456" y="420" text-anchor="middle" font-family="Lora" font-weight="700" font-size="60" fill="#1a1817">Du</text></svg>""")
ersetze("mo4", """<section class="p" id="mo4"><p class="h m">Worauf eine Führungsrolle steht.</p>%s%s</section>""" % (VENN, NAME))
ersetze("mo5", """<section class="p schwarz" id="mo5"><p class="h m" style="color:#fff;font-size:64px">Wen brauchst du –<br><span style="white-space:nowrap">und wen hast du <span class="hl">übersehen?</span></span></p>%s%s</section>""" % (ERFOLG2, NAME))
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

# Postingtyp „Die Skizze“ (13.10.2026): sechs Darstellungsarten, erzeugt von skizzen/skizzen_bauen.cjs
# (Open Peeps CC0 · rough.js MIT · Caveat OFL) – Ergebnis liegt in skizzen-sektionen.html
teile.append(open(os.path.join(HIER, "skizzen-sektionen.html"), encoding="utf-8").read())

# Redaktionsplan KW 43/44 (13.10.2026): Bilder je Posting
teile += [
    """<section class="p foto-voll vollbild" id="rp01">%s<div class="verlauf" style="height:62%%"></div><div class="unten"><p class="satz" style="font-size:84px">Die Strategie gibt der Chef vor.</p><p class="satz" style="font-size:84px;margin-top:10px"><span class="hl">Das ist sein Job.</span></p></div></section>""" % vb("voll-e2.jpg", "30% 40%"),
    """<section class="p schwarz" id="rp02">
  <p class="k">Was ein Vorstand wissen muss</p>
  <div style="margin-top:70px">
    <div class="wortzeile"><p class="wort">Why.</p><em>Welche Bedeutung hat das Thema für uns?</em></div>
    <div class="wortzeile"><p class="wort">How.</p><em>Wie gehen wir grundsätzlich vor?</em></div>
    <div class="wortzeile"><p class="wort"><span class="hl" style="padding:0 .08em">Next.</span></p><em>Was ist der nächste Schritt?</em></div>
  </div>
  <p class="namezeile">Daniel Ströbel</p>
</section>""",
    """<section class="p vollbild" id="rp03">
  <img src="%sentwurf-e3.jpg" alt="" style="filter:grayscale(1) contrast(1.06);--pos:50%% 20%%">
  <div class="verlauf"></div>
  <div class="unten"><p class="satz">„Führung macht einsam. Je höher du kommst, desto weniger sagt dir jemand die Wahrheit.“</p><p class="wer">— ein ehemaliger Vorstand</p></div>
</section>""" % B,
    """<section class="p schwarz" id="rp04"><p class="fr-gross" style="margin-top:40px;color:#fff;font-size:92px">Wie viel deiner Woche zahlt auf die <span class="hl">Strategie</span> ein?</p>
  <div style="position:relative;margin-top:150px;height:150px">
    <div style="position:absolute;left:0;right:0;top:61px;height:28px;border-radius:14px;background:#4a4642"></div>
    <div style="position:absolute;left:50%%;top:0;width:150px;height:150px;margin-left:-75px;border-radius:50%%;background:#fff400;display:grid;place-items:center;font:700 96px/1 Lora,Georgia,serif;color:#1a1817;box-shadow:0 0 0 12px #1a1817">?</div>
  </div>
  <div style="display:flex;justify-content:space-between;margin-top:30px;font:600 44px/1 Poppins,sans-serif;color:#fff"><span>0&nbsp;%%</span><span>100&nbsp;%%</span></div>%s%s</section>""" % (anschnitt(F, 560, -180, -170, "#fff400"), NAME),
    """<section class="p foto-voll" id="rp05">%s</section>""" % vb("entwurf-e6.jpg", "50% 40%"),
    """<section class="p vollbild" id="rp08">
  <img src="%svoll-b1.jpg" alt="" style="--pos:0%% 45%%">
  <div class="verlauf" style="height:72%%"></div>
  <div class="unten"><p class="zahl">77 %%</p><p class="satz" style="margin-top:18px">sagen: Das Tagesgeschäft verdrängt die strategischen Projekte.</p><p class="wer">Quelle: Wieselhuber, branchenübergreifend</p></div>
</section>""" % B,
    """<section class="p foto-voll vollbild" id="rp07">%s<div class="verlauf" style="height:60%%"></div><div class="nein-block"><p>Dein Vorstand gibt kein Zielbild vor?</p><b>Chance.</b></div></section>""" % vb("voll-e1.jpg", "35% 40%"),
]

# Redaktionsplan Wochenende 17./18.10.2026 (7-Tage-Rhythmus)
teile += [
    """<section class="p gelbgrund" id="rp09"><p class="h" style="margin-top:60px;font-size:96px;line-height:1.24;max-width:900px;color:#1a1817">Die meisten sehen nur die Grenzen, die <span class="hl" style="background:#1a1817;color:#fff400">heute gesteckt</span> sind.</p>%s%s</section>""" % (anschnitt(O, 700, -220, -190, "#1a1817"), NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"')),
    """<section class="p gelbgrund" id="rp11">
  <div class="an" style="width:820px;height:820px;right:-210px;top:-150px;color:#1a1817;transform:rotate(-14deg)">%s</div>
  <p class="k" style="position:relative;color:#1a1817">Anwaltshotline</p>
  <p class="zitat" style="position:absolute;left:84px;right:84px;bottom:390px;margin:0;font-size:150px;line-height:1.04;color:#1a1817">„Das kommt darauf&nbsp;an.“</p>
  <p style="position:absolute;left:84px;right:84px;bottom:190px;margin:0;font:600 42px/1.45 Poppins,sans-serif;color:#1a1817">Wenn das gut gemeinte Feature nach hinten <span class="hl" style="background:#1a1817;color:#fff400">losgeht.</span></p>
  %s
</section>""" % (luc("phone").replace('class="luc"', 'class="luc" style="stroke-width:1.1"'), NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"')),
    """<section class="p schwarz" id="rp10"><span class="riesen-anf">„</span>
  <p class="zitat-w" style="font-size:70px">„Das habe ich noch nicht richtig verstanden. Können Sie mir das mal in Ihren eigenen Worten erklären?“</p><p class="zitat-quelle">— (m)ein Vorstand</p></section>""",
]

# Redaktionsplan 25.–27.10.2026 (Sprache näher an Daniel, 19.10.2026)
teile += [
    """<section class="p vollbild" id="rp12">%s<div class="verlauf" style="height:46%%"></div><div style="position:absolute;inset:0 0 auto 0;height:280px;background:linear-gradient(180deg,rgba(26,24,23,.6),rgba(26,24,23,0))"></div><p class="oben k">Aufgegriffen</p><div class="unten"><p class="satz" style="font-size:84px">Bis zur Grenze darfst du <span class="hl">klar sein.</span></p></div></section>""" % vb("foto-anzug.jpg", "50% 22%"),
    """<section class="p gelbgrund" id="rp13"><span class="riesen-frage">?</span><p class="fr-gross" style="margin-top:40px;max-width:840px;position:relative;line-height:1.2;color:#1a1817">Wie würdest du deinen Bereich heute <span class="hl" style="background:#1a1817;color:#fff400">neu gründen?</span></p>%s</section>""" % NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"'),
    """<section class="p foto-voll vollbild" id="rp14">%s<div class="verlauf" style="height:34%%"></div><div class="unten" style="bottom:70px"><p class="satz" style="font-size:84px">Logik allein verändert</p><p class="satz" style="font-size:84px;margin-top:6px"><span class="hl" style="color:#1a1817">wenig.</span></p></div></section>""" % vb("voll-e5.jpg", "50% 30%"),
]

OBENSCHATTEN = '<div style="position:absolute;inset:0 0 auto 0;height:260px;background:linear-gradient(180deg,rgba(26,24,23,.55),rgba(26,24,23,0))"></div>'
# Redaktionsplan 28.10.–08.11.2026 (Daniel, 21.10.2026: mehr echte Fotos, Abwechslung, Text ≠ Bild)
GELBNAME = NAME.replace('class="namezeile"', 'class="namezeile" style="color:#1a1817"')
KREISE = """<svg viewBox="0 0 912 760" style="width:100%;display:block;margin-top:70px">
<g stroke="#1a1817" stroke-width="5"><circle cx="300" cy="270" r="230" fill="#fff"/><circle cx="612" cy="270" r="230" fill="#fff"/><circle cx="456" cy="520" r="230" fill="#fff"/></g>
<g stroke="#1a1817" stroke-width="5" fill="none"><circle cx="300" cy="270" r="230"/><circle cx="612" cy="270" r="230"/><circle cx="456" cy="520" r="230"/></g>
<circle cx="456" cy="352" r="86" fill="#fff400" stroke="#1a1817" stroke-width="5"/>
<g font-family="Poppins" font-weight="600" font-size="34" text-anchor="middle" fill="#1a1817">
<text x="250" y="230">Fach-</text><text x="250" y="272">expertise</text>
<text x="662" y="250">Führung</text>
<text x="456" y="640">Geschäftsmodell</text>
<text x="456" y="364" font-family="Lora" font-weight="700" font-size="40">Rolle</text></g></svg>"""
ZEIT = """<div style="margin-top:100px;display:grid;gap:52px">""" + "".join(
    """<div style="display:grid;grid-template-columns:150px 1fr;gap:40px;align-items:start"><b style="display:grid;place-items:center;width:150px;height:150px;border-radius:50%%;background:%s;color:%s;font:700 78px/1 Poppins,sans-serif">%s</b><p style="padding-top:8px"><span style="display:block;font:700 68px/1.15 Lora,Georgia,serif;color:#1a1817">%s</span><span style="display:block;margin-top:12px;font:500 36px/1.4 Poppins,sans-serif;color:#4a4642">%s</span></p></div>""" % (bg, fg, n, t, u)
    for n, t, u, bg, fg in [("1", "Erzählen", "Ohne Vorbereitung, ohne Folien.", "#1a1817", "#fff400"),
                            ("2", "Spiegeln", "Die Grundstory steht.", "#1a1817", "#fff400"),
                            ("3", "Vorgehen", "Wer ist betroffen? Wie ticken sie?", "#fff400", "#1a1817")]) + "</div>"
BROWSER = """<div style="margin-top:80px;border-radius:26px;background:#1a1817;overflow:hidden">
<div style="display:flex;align-items:center;gap:14px;padding:26px 30px;border-bottom:2px solid #3a3633"><i style="width:18px;height:18px;border-radius:50%;background:#5a5550"></i><i style="width:18px;height:18px;border-radius:50%;background:#5a5550"></i><i style="width:18px;height:18px;border-radius:50%;background:#5a5550"></i>
<span style="margin-left:18px;flex:1;padding:12px 24px;border-radius:40px;background:#2c2926;font:500 26px/1 Poppins,sans-serif;color:#a8a39c">deine-abteilung-gmbh.de</span></div>
<div style="padding:56px 56px 64px"><p style="font:700 66px/1.12 Lora,Georgia,serif;color:#fff">Wofür sind <span class="hl" style="color:#1a1817">wir da?</span></p>
<p style="margin-top:34px;height:22px;width:86%;border-radius:12px;background:#3a3633"></p><p style="margin-top:20px;height:22px;width:70%;border-radius:12px;background:#3a3633"></p><p style="margin-top:20px;height:22px;width:78%;border-radius:12px;background:#3a3633"></p>
<p style="margin-top:44px;display:inline-block;padding:18px 34px;border-radius:40px;background:#fff400;font:600 28px/1 Poppins,sans-serif;color:#1a1817">Leistung anfragen</p></div></div>"""
teile += [
    """<section class="p" id="rp15"><p class="k">Vor dem ersten Tag</p><p class="fr-gross" style="margin-top:40px;font-size:92px">Was eine Führungskraft ab Tag eins <span class="hl">braucht.</span></p>%s%s</section>""" % (KREISE, NAME),
    """<section class="p vollbild" id="rp16">%s<div style="position:absolute;inset:0 0 auto 0;height:62%%;background:linear-gradient(180deg,rgba(26,24,23,.92) 0%%,rgba(26,24,23,.78) 45%%,rgba(26,24,23,0) 100%%)"></div><p class="oben k">London</p><div class="unten" style="top:150px;bottom:auto"><p class="satz" style="font-size:80px">Lernen nach Feierabend. <span class="hl">Mitten in der City.</span></p></div></section>""" % vb("foto-london.jpg", "50% 100%"),
    """<section class="p vollbild" id="rp17">%s<div class="verlauf" style="height:46%%"></div><div style="position:absolute;inset:0 0 auto 0;height:280px;background:linear-gradient(180deg,rgba(26,24,23,.6),rgba(26,24,23,0))"></div><p class="oben k">Werkstatt</p><div class="unten"><p class="satz" style="font-size:96px">Erst benutzen. <span class="hl">Dann mitreden.</span></p></div></section>""" % vb("foto-laptop.jpg", "28% 40%"),
    """<section class="p vollbild" id="rp18">%s<div class="verlauf" style="height:48%%"></div><div style="position:absolute;inset:0 0 auto 0;height:280px;background:linear-gradient(180deg,rgba(26,24,23,.6),rgba(26,24,23,0))"></div><p class="oben k">Weitergedacht</p><div class="unten"><p class="satz" style="font-size:80px">Wenn sie nicht zu uns kommen, <span class="hl">gehen wir zu ihnen.</span></p></div></section>""" % vb("foto-macromedia.jpg", "50% 30%"),
    """<section class="p" id="rp19"><p class="k">Aufgegriffen</p>
  <p class="zitat" style="margin-top:220px;font-size:100px;line-height:1.15;max-width:910px">„Welche Maklerleistungen brauchen Kunden <span class="hl">in zehn Jahren</span> noch?“</p>
  <p class="quelle" style="color:#6b6762">— Tobias Knörrer, Geschäftsführer der bbg (DKM), im Interview mit VWheute</p>%s%s</section>""" % (anschnitt(F, 520, -170, -170, "#1a1817"), NAME),
    """<section class="p schwarz" id="rp20"><p class="k">Wenn ein Team nicht mitzieht</p><p class="fr-gross" style="margin-top:60px;color:#fff;font-size:104px;max-width:880px;position:relative">Würdest du an ihrer Stelle <span class="hl">anders</span> entscheiden?</p>%s%s</section>""" % (anschnitt(O, 700, -220, -190, "#fff400"), NAME),
    """<section class="p vollbild" id="rp21">%s<div class="verlauf" style="height:52%%"></div><div class="unten"><p class="satz" style="font-size:96px">Was verdient <span class="hl">der Partner daran?</span></p></div></section>""" % vb("foto-tisch.jpg", "12% 40%"),
    """<section class="p" id="rp22"><p class="k">Der Einstieg in die Strategie</p><p class="fr-gross" style="margin-top:40px;font-size:96px">Drei Gespräche. <span class="hl">Je&nbsp;eine&nbsp;Stunde.</span></p>%s%s</section>""" % (ZEIT, NAME),
    """<section class="p vollbild" id="rp23">%s<div class="verlauf" style="height:42%%"></div><div class="unten"><p class="satz" style="font-size:96px">„Eigentlich<br>ist es <span class="hl">doch so.“</span></p></div></section>""" % vb("foto-flipchart.jpg", "18% 40%"),
    """<section class="p gelbgrund" id="rp24"><p class="k" style="color:#1a1817">Gedankenexperiment</p><p class="fr-gross" style="margin-top:40px;font-size:92px;color:#1a1817">Deine Abteilung ist ab morgen eine GmbH.</p>%s%s</section>""" % (BROWSER, GELBNAME),
    """<section class="p vollbild" id="rp25">%s<div class="verlauf" style="height:44%%"></div><div style="position:absolute;inset:0 0 auto 0;height:280px;background:linear-gradient(180deg,rgba(26,24,23,.6),rgba(26,24,23,0))"></div><p class="oben k">Weitergedacht</p><div class="unten"><p class="satz" style="font-size:110px">Und was, <span class="hl">wenn nicht?</span></p></div></section>""" % vb("foto-zeigen.jpg", "62% 40%"),
    """<section class="p schwarz" id="rp26"><p class="k" style="position:relative">Aufgegriffen</p>
  <p style="position:absolute;left:84px;right:84px;top:300px;font:700 112px/1.1 Lora,Georgia,serif;letter-spacing:-.015em;color:#fff">„… es braucht insgesamt mehr <span class="hl">Mut, Führung und Tempo.</span>“</p>
  <p style="position:absolute;left:84px;right:84px;bottom:110px;padding-top:28px;border-top:4px solid #fff400;font:600 32px/1.4 Poppins,sans-serif;color:#d9d5cf">Peter Stockhorst, Digitalvorstand der Zurich Gruppe Deutschland</p></section>""",
]

# Experimentierfeld Persönliches Profil (Daniel, 23.10.2026): bewusst aus dem Raster
FOLIE = """<div style="position:relative;margin:130px 10px 0;transform:rotate(-4deg);border-radius:10px;background:#fff;box-shadow:0 30px 60px rgba(0,0,0,.18);padding:44px 48px 52px">
<p style="font:600 22px/1.2 Poppins,sans-serif;color:#9a958f">Folie 3 von 27</p>
<p style="margin-top:14px;max-width:600px;font:700 38px/1.2 Poppins,sans-serif;color:#2c2926">Ausgangslage und Detailanalyse im Überblick</p>
<div style="margin-top:30px;display:grid;grid-template-columns:1fr 1fr;gap:16px 40px">""" + "".join('<p style="height:16px;border-radius:8px;background:#d9d5cf;width:%d%%"></p>' % w for w in [92, 80, 70, 95, 85, 60, 90, 75, 65, 88]) + """</div>
<div style="margin-top:30px;display:flex;gap:14px;align-items:flex-end;height:110px">""" + "".join('<i style="flex:1;height:%d%%;background:#c9c4bd;border-radius:4px 4px 0 0"></i>' % h for h in [40, 70, 55, 90, 35, 65, 80]) + """</div>
<svg viewBox="0 0 100 60" preserveAspectRatio="none" style="position:absolute;inset:0;width:100%;height:100%"><path d="M4 56 L96 4" stroke="#1a1817" stroke-width="2.4" stroke-linecap="round" fill="none"/><path d="M5 5 L95 55" stroke="#1a1817" stroke-width="2.4" stroke-linecap="round" fill="none"/></svg>
<span style="position:absolute;right:-24px;top:-30px;transform:rotate(6deg);padding:14px 30px;border-radius:12px;background:#fff400;font:700 40px/1 Poppins,sans-serif;color:#1a1817">→ Backup</span></div>"""
teile += [
    """<section class="p foto-voll" id="ex1">%s</section>""" % vb("foto-klartext.jpg", "14% 40%"),
    """<section class="p grau" id="ex2"><p class="fr-gross" style="margin-top:30px;font-size:96px">Erst das Bild. <span class="hl">Dann die Details.</span></p>%s%s</section>""" % (FOLIE, NAME),
    """<section class="p schwarz" id="ex3"><p class="k">Landingpage</p>
  <p style="margin-top:400px;font:700 120px/1.05 Lora,Georgia,serif;color:#8a857f;text-decoration:line-through;text-decoration-thickness:10px;text-decoration-color:#fff400">Nächstes Jahr.</p>
  <p style="margin-top:50px;font:700 150px/1.05 Lora,Georgia,serif;color:#fff">In drei <span class="hl">Wochen.</span></p>%s</section>""" % NAME,
]

# Experimentierfeld Runde 2 (Daniel, 23.10.2026): Stufenleiter – vom nächsten Schritt bis „zu wild“
HAND = 'font:700 %dpx/1.05 Caveat,cursive;color:%s'
def kseite(nr, kopf, satz, stempel=True):
    return """<section class="p" id="st3%s" style="background:#f3f1ee"><p class="k">Folien, die ich als Erstes lösche · %s/5</p>
  <div style="position:relative;margin-top:120px;border-radius:12px;background:#fff;box-shadow:0 30px 60px rgba(0,0,0,.14);padding:60px 56px;min-height:520px">
    <p style="font:700 64px/1.15 Poppins,sans-serif;color:#2c2926">%s</p>
    %s
  </div>
  <p style="margin-top:70px;font:700 64px/1.18 Lora,Georgia,serif;color:#1a1817">%s</p>%s</section>""" % (nr, {"b": "2", "c": "3", "d": "4"}[nr], kopf,
        '<span style="position:absolute;right:30px;bottom:-34px;transform:rotate(-8deg);padding:16px 34px;border:6px solid #1a1817;border-radius:14px;background:#fff400;font:700 46px/1 Poppins,sans-serif;color:#1a1817">→ BACKUP</span>' if stempel else "",
        satz, NAME)
teile += [
    # Stufe 1 – nächster Schritt: echtes Foto, eine handschriftliche Notiz
    """<section class="p foto-voll" id="st1">%s<p style="position:absolute;right:70px;top:120px;transform:rotate(-5deg);%s;text-align:right;text-shadow:0 2px 14px rgba(0,0,0,.25)">Folien?<br>Ab ins<br>Backup.</p>
  <svg viewBox="0 0 200 200" style="position:absolute;right:260px;top:440px;width:180px;height:180px"><path d="M170 20 C 120 40, 70 90, 40 170" stroke="#fff400" stroke-width="9" fill="none" stroke-linecap="round"/><path d="M40 170 L 30 120 M40 170 L 85 150" stroke="#fff400" stroke-width="9" fill="none" stroke-linecap="round"/></svg></section>""" % (vb("foto-showdonttell.jpg", "22% 40%"), HAND % (104, "#fff400")),
    # Stufe 2 – mutig: Plakat mit harter Zahl
    """<section class="p schwarz" id="st2"><p class="k">Vorstandsvorlage</p>
  <p style="margin-top:330px;font:700 200px/1 Lora,Georgia,serif;color:#6b6762;text-decoration:line-through;text-decoration-thickness:16px;text-decoration-color:#fff400">27 Folien.</p>
  <p style="margin-top:60px;font:700 250px/1 Lora,Georgia,serif;color:#fff"><span class="hl">1 Bild.</span></p>
  <p style="margin-top:70px;font:600 44px/1.3 Poppins,sans-serif;color:#a8a39c">Der Rest: Backup.</p>%s</section>""" % NAME,
    # Stufe 3 – grenzwertig: Dokument-Karussell mit Augenzwinkern
    """<section class="p gelbgrund" id="st3a"><p class="k" style="color:#1a1817">Hitliste</p>
  <p style="margin-top:160px;font:700 132px/1.02 Lora,Georgia,serif;color:#1a1817">Folien, die ich als Erstes lösche.</p>
  <p style="margin-top:80px;font:600 46px/1.3 Poppins,sans-serif;color:#1a1817">Platz 3 bis 1. Wischen →</p>%s</section>""" % GELBNAME,
    kseite("b", "Agenda<br><span style='display:block;margin-top:18px;columns:2;column-gap:40px;font-weight:500;font-size:34px;line-height:1.55;color:#6b6762'>1. Begrüßung<br>2. Ausgangslage<br>3. Rückblick<br>4. Detailanalyse<br>5. Optionen<br>6. Bewertung<br>7. Risiken<br>8. Zeitplan<br>9. Budget<br>10. Nächste Schritte<br>11. Sonstiges</span>", "Platz 3: Elf Punkte Agenda. Wer elf Punkte braucht, weiß noch nicht, worum es geht."),
    kseite("c", "Organigramm Hauptabteilung<br><span style='font-weight:500;font-size:40px;color:#6b6762'>Stand: wie immer</span>", "Platz 2: Das Organigramm. Jeder im Raum kennt es. Seit Jahren."),
    kseite("d", "<span style='display:block;margin-top:120px;text-align:center;font-size:150px'>Fragen?</span>", "Platz 1: „Fragen?“ Die echte Frage stellt der Vorstand sowieso. Auf Folie 3."),
    """<section class="p schwarz" id="st3e"><p class="k">Was bleibt</p>
  <p style="margin-top:260px;font:700 120px/1.08 Lora,Georgia,serif;color:#fff">Ein Bild.<br><span class="hl">Eine Entscheidung.</span></p>%s</section>""" % NAME,
    # Stufe 4 – zu wild: Stempel, Großbuchstaben, Lautstärke
    """<section class="p vollbild" id="st4">%s<div style="position:absolute;inset:0;background:rgba(26,24,23,.55)"></div>
  <p style="position:absolute;left:50px;right:50px;top:330px;transform:rotate(-12deg);padding:30px 0;border:14px solid #fff400;border-radius:28px;text-align:center;font:800 170px/1 Poppins,sans-serif;letter-spacing:.04em;color:#fff400">GELÖSCHT.</p>
  <p style="position:absolute;left:70px;right:70px;bottom:120px;font:800 74px/1.08 Poppins,sans-serif;text-transform:uppercase;color:#fff">Alle 27 Folien.<br><span class="hl">Auch deine Lieblingsfolie.</span></p></section>""" % vb("foto-zeigen.jpg", "62% 40%"),
]

# Experimentierfeld Runde 2b (Daniel, 23.10.2026): mehr Beispiele je Stufe, „zu wild“ wilder
def kal():
    tage = ["Mo", "Di", "Mi", "Do", "Fr"]
    raster = [["Jour fixe", "Abstimmung IT", "Regeltermin", "Steuerkreis", "Jour fixe"],
              ["Team-Runde", "Regeltermin", "Bereichsrunde", "Regeltermin", "Projekt-Update"],
              ["Regeltermin", "Steuerkreis", "", "Abstimmung", "Regeltermin"],
              ["Projekt-Update", "Jour fixe", "Regeltermin", "Team-Runde", "Wochenabschluss"]]
    z = '<div style="display:grid;grid-template-columns:repeat(5,1fr);gap:10px;margin-top:80px">'
    z += "".join('<p style="font:600 30px/1 Poppins,sans-serif;color:#6b6762;padding-bottom:6px">%s</p>' % t for t in tage)
    for zeile in raster:
        for c in zeile:
            if c:
                z += '<p style="height:150px;border-radius:12px;background:#d9d5cf;padding:14px;font:500 22px/1.2 Poppins,sans-serif;color:#4a4642">%s</p>' % c
            else:
                z += '<p style="height:150px;border-radius:12px;background:#fff400;padding:14px;font:700 22px/1.2 Poppins,sans-serif;color:#1a1817">Strategie<br>30 Min.</p>'
    return z + "</div>"
BINGO = ["Wir müssen alle mitnehmen.", "Quick Win", "Lass uns das offline klären.", "Parkplatz", "Low hanging fruit", "Das haben wir schon immer so gemacht.", "Synergien heben", "Erst einmal sammeln.", "Next Steps – ohne Namen"]
teile += [
    """<section class="p" id="s1b"><p class="k">Kalender einer neuen Führungskraft</p><p class="fr-gross" style="margin-top:40px;font-size:84px">Wo ist hier die <span class="hl">Strategie?</span></p>%s%s</section>""" % (kal(), NAME),
    """<section class="p foto-voll" id="s1c">%s<div style="position:absolute;inset:auto 0 0 0;height:58%%;background:linear-gradient(180deg,rgba(26,24,23,0),rgba(26,24,23,.88))"></div>
  <p style="position:absolute;left:70px;right:70px;bottom:120px;transform:rotate(-3deg);%s">„Wenn ich mit euch zusammenarbeite, weiß ich einfach, dass es läuft.“</p>
  <p style="position:absolute;left:74px;bottom:66px;font:500 26px/1 Poppins,sans-serif;color:#d9d5cf">— ein Kunde, sinngemäß</p></section>""" % (vb("foto-seminarraum.jpg", "10% 40%"), HAND % (92, "#fff")),
    """<section class="p gelbgrund" id="s2b"><p class="k" style="color:#1a1817">Angebotsanfrage</p>
  <p style="margin-top:260px;font:700 136px/1.02 Lora,Georgia,serif;color:#1a1817">Ihr braucht kein <span class="hl" style="background:#1a1817;color:#fff400">Konflikt&shy;seminar.</span></p>
  <p style="margin-top:70px;font:600 46px/1.3 Poppins,sans-serif;color:#1a1817">Ihr braucht ein Zielbild.</p>%s</section>""" % GELBNAME,
    """<section class="p vollbild" id="s2c">%s<div class="verlauf" style="height:40%%"></div><div class="unten"><p class="satz" style="font-size:84px">Nein ist auch eine <span class="hl">Leistung.</span></p></div></section>""" % vb("voll-e4.jpg", "28% 30%"),
    """<section class="p" id="s3b"><p class="k">Workshop-Bingo</p><p class="fr-gross" style="margin-top:30px;font-size:96px">Bingo? Dann wurde heute <span class="hl">nichts entschieden.</span></p>
  <div style="margin-top:60px;display:grid;grid-template-columns:repeat(3,1fr);gap:14px">""" + "".join('<p style="position:relative;display:grid;place-items:center;height:190px;padding:16px;border:4px solid #1a1817;border-radius:16px;text-align:center;font:600 28px/1.2 Poppins,sans-serif;color:#1a1817;background:%s">%s%s</p>' % ("#fff400" if i in (0, 4, 8) else "#fff", t, '<b style="position:absolute;inset:0;display:grid;place-items:center;font:700 150px/1 Lora,serif;color:rgba(26,24,23,.55)">×</b>' if i in (0, 4, 8) else "") for i, t in enumerate(BINGO)) + """</div>%s</section>""" % NAME,
    """<section class="p grau" id="s3c"><div style="margin-top:20px;border-radius:18px;background:#fff;padding:60px 60px 70px;box-shadow:0 20px 50px rgba(0,0,0,.08)">
  <p style="font:600 26px/1 Poppins,sans-serif;letter-spacing:.14em;text-transform:uppercase;color:#6b6762">Stellenanzeige · Vorstandsebene</p>
  <p style="margin-top:30px;font:700 84px/1.08 Lora,Georgia,serif;color:#1a1817">Gesucht: Ein Mensch, der dem Vorstand die <span class="hl">Wahrheit</span> sagt.</p>
  <p style="margin-top:44px;font:700 30px/1 Poppins,sans-serif;color:#1a1817">Ihre Aufgaben</p>
  <p style="margin-top:14px;font:500 32px/1.5 Poppins,sans-serif;color:#4a4642">• widersprechen, wenn alle nicken<br>• Fragen stellen, die unbequem sind<br>• Zusammenhänge zeigen, die keiner sehen wollte</p>
  <p style="margin-top:34px;font:700 30px/1 Poppins,sans-serif;color:#1a1817">Wir bieten</p>
  <p style="margin-top:14px;font:500 32px/1.5 Poppins,sans-serif;color:#4a4642">einen Vorstand, der endlich wieder etwas Neues hört.</p></div>%s</section>""" % NAME,
    """<section class="p" id="s4b" style="background:#fff"><div style="margin-top:40px;border:16px solid #1a1817;padding:70px 60px;text-align:center;min-height:1040px">
  <p style="font:700 34px/1 Poppins,sans-serif;letter-spacing:.2em;text-transform:uppercase;color:#1a1817">In stiller Trauer</p>
  <p style="margin-top:50px;font:700 96px/1.08 Lora,Georgia,serif;color:#1a1817">Unsere Strategie</p>
  <p style="margin-top:20px;font:500 40px/1.3 Lora,Georgia,serif;font-style:italic;color:#4a4642">* Klausur 2019 &nbsp; † im Alltag, kurz danach</p>
  <p style="margin:60px auto 0;max-width:760px;font:500 38px/1.5 Poppins,sans-serif;color:#1a1817">84 Folien. Sieben Werte. Ein Plakat im Flur.<br>Montags hat sie nie jemand gesehen.</p>
  <p style="margin-top:70px;font:700 40px/1.3 Poppins,sans-serif;color:#1a1817">Statt Blumen: Macht es beim nächsten Mal <span class="hl">anders.</span></p></div></section>""",
    """<section class="p gelbgrund" id="s4c"><div style="margin-top:20px;border:10px solid #1a1817;padding:50px 50px 60px;text-align:center;min-height:1080px;background:#fff400">
  <p style="font:800 158px/.9 Lora,Georgia,serif;letter-spacing:.02em;color:#1a1817">GESUCHT</p>
  <p style="margin-top:20px;font:700 34px/1 Poppins,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#1a1817">Tot oder lebendig</p>
  <div style="margin:50px auto 0;width:520px;height:330px;border:8px solid #1a1817;display:grid;place-items:center;font:700 64px/1.1 Lora,Georgia,serif;color:#1a1817;background:#fff">Die<br>Entscheidung</div>
  <p style="margin-top:44px;font:600 36px/1.45 Poppins,sans-serif;color:#1a1817">Zuletzt gesehen: Vorstandssitzung im Frühjahr.<br>Seitdem dreimal vertagt.</p>
  <p style="margin-top:44px;font:800 60px/1 Poppins,sans-serif;color:#1a1817">BELOHNUNG:</p>
  <p style="margin-top:12px;font:600 38px/1.3 Poppins,sans-serif;color:#1a1817">ein Bereich, der wieder vorankommt.</p></div></section>""",
]

# KW 45 Bildlogik (Daniel, 28.10.2026): Montag = nachgebautes Mail-Postfach (Szene), Mittwoch = Dokument-Karussell (Werkzeug)
SYS = "-apple-system,BlinkMacSystemFont,'Segoe UI',Helvetica,Arial,sans-serif"
def mailzeile(tag, zeit, text, offen=False):
    return """<div style="display:grid;grid-template-columns:64px 1fr auto;gap:18px;align-items:start;padding:26px 30px;border-bottom:1px solid #e6e3df;background:%s">
<span style="display:grid;place-items:center;width:64px;height:64px;border-radius:50%%;background:#1a1817;color:#fff;font:600 26px/1 %s">Du</span>
<span><b style="display:block;font:600 30px/1.2 %s;color:#1a1817">Du <span style="font-weight:400;color:#6b6762">an Team Vertriebssteuerung</span></b>
<span style="display:block;margin-top:8px;font:400 28px/1.35 %s;color:#4a4642">%s</span></span>
<span style="font:400 24px/1.2 %s;color:#8a857f;white-space:nowrap">%s, %s</span></div>""" % ("#fff" if offen else "#faf9f7", SYS, SYS, SYS, text, SYS, tag, zeit)
MAIL = """<section class="p" id="rp27" style="background:#e9e7e3;padding:70px 56px 0">
<div style="border-radius:22px;background:#fff;box-shadow:0 24px 60px rgba(0,0,0,.12);overflow:hidden">
<div style="padding:34px 30px 26px;border-bottom:1px solid #e6e3df">
<p style="font:600 22px/1 %s;letter-spacing:.06em;text-transform:uppercase;color:#8a857f">Gesendete Elemente</p>
<p style="margin-top:16px;font:700 44px/1.2 %s;color:#1a1817">AW: AW: AW: Unterstützung für das Projekt</p></div>
%s%s%s
<div style="padding:30px;font:400 26px/1.3 %s;color:#8a857f">Gelesen · keine Antwort</div></div>
<p style="position:absolute;left:56px;right:56px;bottom:150px;font:700 84px/1.12 Lora,Georgia,serif;color:#1a1817">Die vierte Mail <span class="hl">hilft auch nicht.</span></p>%s</section>""" % (
    SYS, SYS,
    mailzeile("Mo", "09:12", "Hallo zusammen, kurze Erinnerung an unser Thema von letzter Woche …"),
    mailzeile("Mi", "17:48", "Ich wollte noch einmal nachhaken. Bis Freitag bräuchten wir eure Rückmeldung …"),
    mailzeile("Do", "16:42", "Gibt es hierzu schon einen Stand? Sonst kommen wir nicht weiter.", True),
    SYS, NAME)
def kseite2(nr, kopf, text, gross=None, dunkel=False):
    bg, fg, sub = ("#1a1817", "#fff", "#cfcac4") if dunkel else ("#fff", "#1a1817", "#4a4642")
    zahl = '<p style="font:700 300px/.85 Poppins,sans-serif;color:#fff400;-webkit-text-stroke:6px %s">%s</p>' % (fg, gross) if gross else ""
    return """<section class="p" id="ka%s" style="background:%s"><p class="k" style="color:%s">Strategie in drei Gesprächen · %s/5</p>
<div style="margin-top:%dpx">%s<p style="margin-top:40px;font:700 96px/1.08 Lora,Georgia,serif;color:%s">%s</p>
<p style="margin-top:44px;max-width:880px;font:500 48px/1.45 Poppins,sans-serif;color:%s">%s</p></div>%s</section>""" % (
        nr, bg, fg, nr, 160 if gross else 300, zahl, fg, kopf, sub, text, NAME)
teile += [MAIL]

# Karussell „Strategie in drei Gesprächen“ v2 (Daniel, 28.10.2026: Folien auf CD-Niveau) – Flächenwechsel Gelb/Schwarz/Weiß,
# angeschnittenes Vorwärts-Zeichen läuft über die Seitengrenze 1→2, durchgehende Fortschrittsleiste auf den Schritt-Seiten.
GELB, INK = "#fff400", "#1a1817"
def leiste(aktiv, dunkel):
    farbe_an = GELB if dunkel else INK
    farbe_aus = "#4a4642" if dunkel else "#cfcac4"
    text_an = "#fff" if dunkel else INK
    text_aus = "#8a857f"
    knoten = ""
    for i, wort in enumerate(["Erzählen", "Spiegeln", "Vorgehen"]):
        an = i + 1 <= aktiv
        knoten += '<div style="position:absolute;left:%dpx;top:-14px;text-align:center;width:200px;margin-left:-100px"><i style="display:block;margin:0 auto;width:%dpx;height:%dpx;border-radius:50%%;background:%s;%s"></i><b style="display:block;margin-top:18px;font:%s 26px/1 Poppins,sans-serif;color:%s">%s</b></div>' % (
            170 + i * 370, 34 if i + 1 == aktiv else 28, 34 if i + 1 == aktiv else 28, farbe_an if an else (INK if dunkel else "#fff"),
            "" if an else "border:5px solid %s;box-sizing:border-box" % farbe_aus, "700" if i + 1 == aktiv else "500", text_an if i + 1 == aktiv else text_aus, wort)
    breite = 170 + (aktiv - 1) * 370
    return '<div style="position:absolute;left:-20px;right:-20px;bottom:170px;height:6px;background:%s"><div style="position:absolute;left:0;top:0;height:6px;width:%dpx;background:%s"></div>%s</div>' % (farbe_aus, breite + 20, farbe_an, knoten)
def schritt(nr, wort, saetze, dunkel):
    bg, fg, sub, zahl = (INK, "#fff", "#cfcac4", GELB) if dunkel else ("#fff", INK, "#4a4642", INK)
    return """<section class="p" id="ka%d" style="background:%s;padding:84px">
  <p class="k" style="color:%s">Strategie in drei Gesprächen</p>
  <p style="position:absolute;left:66px;top:150px;font:800 560px/.8 Poppins,sans-serif;letter-spacing:-.04em;color:%s">%d</p>
  <div style="position:absolute;left:84px;right:84px;top:640px">
    <p style="font:700 128px/1 Lora,Georgia,serif;letter-spacing:-.02em;color:%s">%s</p>
    <p style="margin-top:36px;max-width:860px;font:500 46px/1.4 Poppins,sans-serif;color:%s">%s</p></div>
  %s</section>""" % (nr + 1, bg, fg, zahl, nr, fg, wort, sub, saetze, leiste(nr, dunkel))
ZEICHEN_GROSS = 780
teile += [
    """<section class="p gelbgrund" id="ka1" style="padding:84px">
  <p class="k" style="color:#1a1817">Strategie-Einstieg</p>
  <p style="margin-top:150px;font:700 104px/1.08 Lora,Georgia,serif;letter-spacing:-.02em;color:#1a1817">Strategie in<br>drei Gesprächen.</p>
  <p style="margin-top:50px;max-width:560px;font:600 46px/1.3 Poppins,sans-serif;color:#1a1817">Statt zwei Tage Workshop und Kärtchen an der Wand.</p>
  <div class="an" style="width:%dpx;height:%dpx;right:-%dpx;top:700px;color:#1a1817">%s</div>
  <p style="position:absolute;left:84px;bottom:84px;font:600 30px/1 Poppins,sans-serif;color:#1a1817">Daniel Ströbel</p></section>""" % (ZEICHEN_GROSS, ZEICHEN_GROSS, ZEICHEN_GROSS // 2, F),
    schritt(1, "Erzählen.", "Eine Stunde, am Telefon. Ohne Vorbereitung, ohne Folien. Du erzählst – ich frage.", True),
    schritt(2, "Spiegeln.", "Ich lege hin, was ich gehört habe. Plötzlich steht das Bild, das du die ganze Zeit im Kopf hattest.", False),
    schritt(3, "Vorgehen.", "Wen braucht es? Wie ticken die Betroffenen? Erst dann geht es los.", True),
    """<section class="p gelbgrund" id="ka5" style="padding:84px">
  <p class="k" style="color:#1a1817">Dein erster Schritt</p>
  <p style="margin-top:130px;font:700 118px/1.05 Lora,Georgia,serif;letter-spacing:-.02em;color:#1a1817">Heute.<br>Eine Stunde.<br>Ohne Folien.</p>
  <p style="margin-top:50px;max-width:540px;font:500 40px/1.42 Poppins,sans-serif;color:#1a1817">Erzähle jemandem, dem du vertraust, wo dein Bereich hin soll. Und bitte ihn, dir zu spiegeln, was er verstanden hat.</p>
  <img src="/assets/daniel.webp" alt="" style="position:absolute;right:-70px;bottom:0;height:960px;width:auto">
  <p style="position:absolute;left:84px;bottom:84px"><b style="display:block;font:700 40px/1.1 Poppins,sans-serif;color:#1a1817">Daniel Ströbel</b><span style="display:block;margin-top:8px;font:500 30px/1.2 Poppins,sans-serif;color:#1a1817">Strategie in Wirkung bringen</span></p></section>""",
]

# Posting „Der Spion“ – Vertrieb und Beratung (Daniel, 29.10.2026): Zitatkarte mit Originalsatz, gelbe Fläche
teile += [
    """<section class="p" id="rp28" style="background:#000;padding:0">
  <p style="position:absolute;left:84px;top:96px;font:600 26px/1 Poppins,sans-serif;letter-spacing:.18em;text-transform:uppercase;color:#8a857f">Der Spion · 2020</p>
  <div style="position:absolute;left:0;right:0;top:200px;height:900px;background:radial-gradient(ellipse at 50% 40%,#34312e 0%,#1b1a19 75%)">
    <p style="position:absolute;left:84px;right:84px;top:150px;font:700 100px/1.1 Lora,Georgia,serif;letter-spacing:-.01em;color:#f3f1ee">„I just listen. You tell me what your problems are.“</p>
    <p style="position:absolute;left:60px;right:60px;bottom:130px;text-align:center"><span style="display:inline;padding:8px 18px;background:rgba(0,0,0,.72);-webkit-box-decoration-break:clone;box-decoration-break:clone;font:600 46px/1.6 Poppins,sans-serif;color:#fff400">Ich höre einfach zu. Ihr sagt mir, wo eure Probleme liegen.</span></p>
    <div style="position:absolute;left:84px;right:84px;bottom:52px;display:flex;align-items:center;gap:26px">
      <span style="display:flex;gap:9px"><i style="width:11px;height:34px;background:#f3f1ee;border-radius:2px"></i><i style="width:11px;height:34px;background:#f3f1ee;border-radius:2px"></i></span>
      <span style="position:relative;flex:1;height:7px;border-radius:4px;background:#4a4642"><i style="position:absolute;left:0;top:0;bottom:0;width:41%;border-radius:4px;background:#fff400"></i><i style="position:absolute;left:41%;top:50%;width:24px;height:24px;margin:-12px 0 0 -12px;border-radius:50%;background:#fff400"></i></span>
    </div>
  </div>
  <p style="position:absolute;left:84px;bottom:110px;font:600 32px/1.3 Poppins,sans-serif;color:#d9d5cf">Benedict Cumberbatch als Geschäftsmann Greville Wynne</p>
  <p style="position:absolute;left:84px;bottom:62px;font:500 24px/1 Poppins,sans-serif;color:#6b6762">Daniel Ströbel</p></section>""",
]

# DKM-Lückentext (Daniel, 29.10.2026): anonymer Messebericht als Vorlage, die leere Stelle ist die Pointe
def kaestchen(worte):
    return " ".join('<span style="white-space:nowrap"><i style="display:inline-block;width:30px;height:30px;margin:0 8px -3px 0;border:3px solid #1a1817;border-radius:6px"></i>%s</span>' % w for w in worte)
teile += [
    """<section class="p schwarz" id="rp29" style="padding:84px">
  <div style="display:flex;align-items:center;gap:22px;padding:26px 34px;border-radius:60px;background:#fff">
    <svg viewBox="0 0 24 24" style="width:46px;height:46px;flex:none" fill="none" stroke="#1a1817" stroke-width="2.6" stroke-linecap="round"><circle cx="10.5" cy="10.5" r="7"/><path d="M16 16l5.5 5.5"/></svg>
    <span style="font:600 46px/1 %s;color:#1a1817">DKM Highlight</span></div>
  <div style="margin-top:44px;display:grid;gap:22px">""" % SYS + "".join("""
    <div style="padding:26px 30px;border-radius:18px;background:#2c2a28"><p style="font:400 38px/1.45 %s;color:#cfcac4">%s</p></div>""" % (SYS, z) for z in [
        'Was für ein <span style="background:#fff400;color:#1a1817;padding:0 6px;border-radius:6px">toller Austausch</span> auf der DKM!',
        'Danke für die <span style="background:#fff400;color:#1a1817;padding:0 6px;border-radius:6px">super Impulse</span> in Dortmund.',
        'Zwei Tage voller <span style="background:#fff400;color:#1a1817;padding:0 6px;border-radius:6px">Highlights</span>. Bis nächstes Jahr!',
        '<span style="background:#fff400;color:#1a1817;padding:0 6px;border-radius:6px">Inspirierende Gespräche</span> – danke an alle!']) + """</div>
  <div style="position:absolute;left:84px;right:84px;bottom:150px;display:flex;align-items:flex-end;gap:36px">
    <p style="font:800 330px/.78 Poppins,sans-serif;color:#fff400">0</p>
    <p style="padding-bottom:14px;font:700 60px/1.12 Lora,Georgia,serif;color:#fff">konkrete Highlights gefunden.</p></div>
  <p class="namezeile">Daniel Ströbel</p></section>""",
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

