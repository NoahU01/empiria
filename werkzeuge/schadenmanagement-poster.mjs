// Erzeugt das Poster (Variante 4) der Seite projekte/schadenmanagement.html als SVG.
// Läuft im Browser gegen den lokalen Server, damit Lora/Poppins geladen sind und jeder
// Text mit der echten Schrift vermessen und umbrochen wird. Ergebnis wird zwischen
// <!-- POSTER:START --> und <!-- POSTER:END --> in die Seite geschrieben.
//
//   cd site && python3 dev-server.py   (läuft)
//   node ../werkzeuge/schadenmanagement-poster.mjs
import fs from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';
import puppeteer from '../site/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js';

const HIER = path.dirname(fileURLToPath(import.meta.url));
const SEITE = path.join(HIER, '../site/projekte/schadenmanagement.html');
const CHROME = process.env.CHROME || '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';
const BASE = process.env.BASE || 'http://localhost:4599';

function bauen() {
  const INK = '#1a1817', GELB = '#fff400', GRAU = '#6f6a64', HELL = '#f4f3f0', LINIE = '#dcd7d0', SUB = '#d8d3cc', GRAU2 = '#b9b3ab';
  const W = 850, X0 = 120, XR = 790, SP = 76;           // Breite, Inhaltskanten, Leitlinie
  const COL = [120, 350, 580], CW = 210;                 // drei gleiche Spalten
  const cx = i => COL[i] + CW / 2;
  const ctx = document.createElement('canvas').getContext('2d');
  const FAM = { P: 'Poppins', L: 'Lora' };
  const esc = s => String(s).replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');

  function setFont(o) { ctx.font = `${o.w || 400} ${o.s}px ${FAM[o.f || 'P']}`; ctx.letterSpacing = (o.ls || 0) + 'px'; }
  function breite(t, o) { setFont(o); return ctx.measureText(t).width; }
  // Umbruch auf Breite; "|" erzwingt einen Umbruch
  function umbruch(text, o, max) {
    const out = [];
    for (const absatz of String(text).split('|')) {
      let zeile = '';
      for (const wort of absatz.split(' ')) {
        const probe = zeile ? zeile + ' ' + wort : wort;
        if (breite(probe, o) <= max || !zeile) zeile = probe; else { out.push(zeile); zeile = wort; }
      }
      out.push(zeile);
    }
    out.forEach(z => { if (breite(z, o) > max + 0.5) throw new Error('Zu breit: ' + z); });
    return out;
  }
  function t(x, y, s, o) {
    const a = o.a ? ` text-anchor="${o.a}"` : '';
    const ls = o.ls ? ` letter-spacing="${o.ls}"` : '';
    return `<text x="${x}" y="${y}" font-family="${FAM[o.f || 'P']}, sans-serif" font-size="${o.s}" font-weight="${o.w || 400}" fill="${o.c || INK}"${a}${ls}>${esc(s)}</text>`;
  }
  function passt(s, o, max) { if (breite(s, o) > max) throw new Error('Zu breit: ' + s); return s; }
  function zeilen(x, y, lines, o, lh) { return lines.map((z, i) => t(x, y + i * lh, z, o)).join(''); }
  const rect = (x, y, w, h, o = {}) => `<rect x="${x}" y="${y}" width="${w}" height="${h}" rx="${o.r ?? 12}" fill="${o.fill || '#fff'}"${o.stroke ? ` stroke="${o.stroke}" stroke-width="${o.sw || 1.5}"` : ''}/>`;
  const linie = (x1, y1, x2, y2, o = {}) => `<line x1="${x1}" y1="${y1}" x2="${x2}" y2="${y2}" stroke="${o.c || INK}" stroke-width="${o.sw || 2}"${o.dash ? ` stroke-dasharray="${o.dash}"` : ''} stroke-linecap="round"/>`;
  const pfeilRunter = (x, y) => `<path d="M${x - 5.5} ${y - 8} L${x} ${y} L${x + 5.5} ${y - 8} Z" fill="${INK}"/>`;
  const pfeilLinks = (x, y) => `<path d="M${x + 8} ${y - 5.5} L${x} ${y} L${x + 8} ${y + 5.5} Z" fill="${INK}"/>`;

  // Schriftstufen
  const EYE = { s: 10, w: 700, ls: 1.6, c: GRAU };       // Kleinlabel (Versalien)
  const TXT = { s: 12.5, w: 400, c: '#3d3a37' };          // Fließtext
  const FRAGE = { s: 12, w: 600, c: INK };                // Fragen
  const TIT = { f: 'L', s: 17, w: 700 };                  // Kartentitel

  let svg = '';
  const knoten = [];

  // ---------- Kopf ----------
  svg += t(X0, 92, 'SV SPARKASSENVERSICHERUNG · ARBEITSDOKUMENT', { ...EYE, s: 11, ls: 2.2 });
  svg += t(X0 - 3, 158, 'Schadenmanagement.', { f: 'L', s: 60, w: 700 });
  svg += t(X0, 194, 'Vom Geschäftsmodell zum Zielbild – der Gesamtzusammenhang.', { s: 16.5, c: GRAU });
  let lx = X0;
  for (const [fill, stroke, label] of [[INK, null, 'nicht verhandelbar'], [GELB, INK, 'hier wirkt das Schadenmanagement'], ['#fff', GRAU2, 'Sachverhalt']]) {
    svg += rect(lx, 226, 12, 12, { r: 3, fill, stroke, sw: 1.3 });
    svg += t(lx + 19, 236.5, label, { s: 11.5, c: GRAU });
    lx += 19 + breite(label, { s: 11.5 }) + 26;
  }
  svg += linie(X0, 270, XR, 270, { c: LINIE, sw: 1 });

  function station(nr, label, kopf, y) {
    knoten.push(y);
    svg += t(X0, y + 4, label, { ...EYE, s: 11, ls: 2.2 });
    svg += t(X0 - 1, y + 40, kopf, { f: 'L', s: 28, w: 700 });
    return y + 66;
  }

  // ---------- 01 Geschäftsmodell ----------
  let y = station('01', 'DAS GESCHÄFTSMODELL', 'Versicherung gleicht Risiken aus.', 330);
  svg += rect(X0, y, XR - X0, 90, { fill: INK });
  svg += t(X0 + 26, y + 30, 'DIE BASIS VON ALLEM', { ...EYE, c: GELB });
  svg += t(X0 + 26, y + 57, 'Risikoausgleich im Kollektiv und in der Zeit.', { f: 'L', s: 22, w: 700, c: '#fff' });
  svg += t(X0 + 26, y + 77, 'berechnet · vertraglich geregelt · erfüllbar im Normal- und im Extremjahr', { s: 12.5, c: SUB });
  y += 90;
  for (let i = 0; i < 3; i++) svg += linie(cx(i), y, cx(i), y + 22);
  y += 22;
  const schritte = [
    ['RISIKOTRANSFER', 'Übernehmen', 'Viele einzelne Risiken werden ein Kollektiv. Das Versprechen steht.', false],
    ['RISIKOTRANSFORMATION', 'Ausgleichen', 'Das Gesamtrisiko steuern – Rückstellungen, Rückversicherung, Kapitalanlage.', false],
    ['SCHADENKOMPENSATION', 'Einlösen', 'Im Schadenfall wird das Versprechen eingelöst.|Hier liegt das Projekt.', true],
  ];
  const sl = schritte.map(s => umbruch(s[2], TXT, CW - 44));
  const hS = 84 + (Math.max(...sl.map(l => l.length)) - 1) * 18 + 24;
  schritte.forEach((s, i) => {
    const x = COL[i];
    svg += rect(x, y, CW, hS, s[3] ? { fill: GELB, stroke: INK } : { stroke: LINIE });
    svg += t(x + 22, y + 30, s[0], { ...EYE, c: s[3] ? INK : GRAU });
    svg += t(x + 22, y + 57, passt(s[1], TIT, CW - 42), TIT);
    svg += zeilen(x + 22, y + 83, sl[i], { ...TXT, c: s[3] ? INK : TXT.c }, 18);
    if (i) svg += `<path d="M${COL[i] - 13} ${y + hS / 2 - 6} l6 6 l-6 6" fill="none" stroke="${INK}" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"/>`;
  });
  y += hS;

  // ---------- 02 Grundlogik ----------
  y = station('02', 'DIE GRUNDLOGIK', 'Was daraus für den Schaden folgt.', y + 76);
  const gruende = [
    ['Das Versprechen hält.', 'Nur für das Vereinbarte wurde Beitrag gezahlt.'],
    ['Es ist fair für alle.', 'Mehr zu zahlen als vereinbart erhöht den Beitrag für alle.'],
    ['Die BaFin achtet darauf.', 'Die Verpflichtungen bleiben langfristig erfüllbar.'],
  ];
  const gl = gruende.map(g => umbruch(g[1], { s: 12, c: SUB }, CW - 52));
  const hG = 150 + (Math.max(...gl.map(l => l.length)) - 1) * 17 + 26;
  svg += rect(X0, y, XR - X0, hG, { fill: INK });
  svg += t(X0 + 26, y + 32, 'GRUNDLOGIK · NICHT VERHANDELBAR', { ...EYE, c: GELB });
  svg += t(X0 + 25, y + 76, 'Entschädigt wird, was vereinbart ist.', { f: 'L', s: 34, w: 700, c: '#fff' });
  svg += linie(X0 + 26, y + 100, XR - 26, y + 100, { c: '#3d3a37', sw: 1 });
  const GI = (XR - X0 - 52) / 3;                         // drei gleiche Innenspalten im Block
  gruende.forEach((g, i) => {
    const x = X0 + 26 + i * GI;
    svg += t(x, y + 131, String(i + 1), { s: 13, w: 700, c: GELB });
    svg += t(x + 18, y + 131, passt(g[0], { s: 12.5, w: 600 }, CW - 52), { s: 12.5, w: 600, c: '#fff' });
    svg += zeilen(x + 18, y + 150, gl[i], { s: 12, c: SUB }, 17);
  });
  y += hG;

  // ---------- 03 Oberziele ----------
  y = station('03', 'DREI OBERZIELE', 'Worauf jede Strategie eine Antwort braucht.', y + 76);
  svg += t(COL[0], y + 4, 'VOR DEM VORHANG', { ...EYE, c: INK });
  svg += t(COL[1], y + 4, 'HINTER DEM VORHANG', { ...EYE, c: INK });
  y += 20;
  const ziele = [
    ['Kundenorientierung', 'Was nimmt der Kunde wahr – und wie schnell schaffen wir Gewissheit?'],
    ['Schadenkosten', 'Was davon kann das Schadenmanagement aktiv beeinflussen?'],
    ['Prozesskosten', 'Wie arbeiten wir eigentlich?'],
  ];
  const ql = ziele.map(z => umbruch(z[1], FRAGE, CW - 66));
  const GH = 168;                                          // Grafikfläche, überall gleich
  const hZ = 70 + GH + 18 + 28 + (Math.max(...ql.map(l => l.length)) - 1) * 17 + 22;
  ziele.forEach((z, i) => {
    const x = COL[i];
    svg += rect(x, y, CW, hZ, { stroke: LINIE });
    svg += t(x + 22, y + 30, 'OBERZIEL', EYE);
    if (i === 0) {
      const bx = x + 22 + breite('OBERZIEL', EYE) + 10, bw = breite('GRÖSSTER HEBEL', { ...EYE, s: 9, ls: 1.2 }) + 14;
      svg += rect(bx, y + 19, bw, 16, { r: 4, fill: GELB, stroke: INK, sw: 1.2 });
      svg += t(bx + 7, y + 30.5, 'GRÖSSTER HEBEL', { ...EYE, s: 9, ls: 1.2, c: INK });
    }
    svg += t(x + 22, y + 57, passt(z[0], TIT, CW - 42), TIT);
    const gy = y + 70;
    if (i === 0) {
      // Dreieck: die untere Kante (Schnelligkeit – Transparenz) ist der Hebel
      const top = [x + 105, gy + 30], bl = [x + 36, gy + 128], br = [x + 174, gy + 128];
      svg += `<path d="M${bl[0]} ${bl[1]} L${top[0]} ${top[1]} L${br[0]} ${br[1]} Z" fill="${HELL}"/>`;
      svg += `<path d="M${bl[0]} ${bl[1]} L${top[0]} ${top[1]} L${br[0]} ${br[1]}" fill="none" stroke="${INK}" stroke-width="1.5" stroke-linejoin="round"/>`;
      svg += linie(bl[0], bl[1], br[0], br[1], { c: GELB, sw: 7 });
      for (const p of [top, bl, br]) svg += `<circle cx="${p[0]}" cy="${p[1]}" r="4.5" fill="${INK}"/>`;
      svg += t(top[0], gy + 18, 'Erstattungsumfang', { s: 11, w: 600, a: 'middle' });
      svg += t(x + 22, gy + 150, 'Schnelligkeit', { s: 11, w: 600 });
      svg += t(x + CW - 22, gy + 150, 'Transparenz', { s: 11, w: 600, a: 'end' });
      svg += t(top[0], gy + 95, 'Kunden-', { s: 10, w: 500, c: GRAU, a: 'middle' });
      svg += t(top[0], gy + 108, 'zufriedenheit', { s: 10, w: 500, c: GRAU, a: 'middle' });
    } else if (i === 1) {
      // Risikotreppe als abnehmende Balken
      const stufen = [['Gesamtrisiko', 54, '#8d867e'], ['Vermeiden', 45, '#cfcac3'], ['Vermindern', 36, '#cfcac3'], ['Begrenzen', 27, GELB], ['Tragen/versichern', 18, '#cfcac3']];
      stufen.forEach(([n, w, f], k) => {
        const ry = gy + 16 + k * 29;
        svg += t(x + 22, ry + 12, passt(n, { s: 11, w: k ? 500 : 700 }, 108), { s: 11, w: k ? 500 : 700, c: INK });
        svg += rect(x + 134, ry, w, 16, { r: 3, fill: f, stroke: f === GELB ? INK : null, sw: 1.2 });
      });
    } else {
      const punkte = ['Automatisierung und KI', 'Abläufe', 'Zuständigkeiten', 'Schnittstellen', 'Summengrenzen', 'Gutachter', 'Drohnen und Satellit'];
      punkte.forEach((n, k) => {
        const ry = gy + 12 + k * 22;
        svg += rect(x + 22, ry + 4, 5, 5, { r: 1, fill: INK });
        svg += t(x + 34, ry + 10, n, { s: 11, w: 500 });
        if (k < punkte.length - 1) svg += linie(x + 22, ry + 17, x + CW - 22, ry + 17, { c: '#ece9e4', sw: 1 });
      });
    }
    const fy = gy + GH + 18;
    svg += linie(x, fy - 18, x + CW, fy - 18, { c: LINIE, sw: 1.5 });
    svg += `<circle cx="${x + 30}" cy="${fy + 6}" r="8" fill="${INK}"/>` + t(x + 30, fy + 10, '?', { s: 10.5, w: 700, c: '#fff', a: 'middle' });
    svg += zeilen(x + 46, fy + 10, ql[i], FRAGE, 17);
  });
  svg += linie(COL[1] - 10, y - 26, COL[1] - 10, y + hZ, { c: INK, sw: 1.5, dash: '4 5' });
  y += hZ;

  // ---------- 04 Zielbild als Strategiemodell ----------
  y = station('04', 'DAS ZIELBILD', 'Als würden wir es morgen neu gründen.', y + 76);
  // Querbalken „Wofür stehen wir?“
  const eingaben = [
    ['UNTERNEHMENSSTRATEGIE', 'Kundenzufriedenheit ist ein großer Bestandteil.'],
    ['FÜHRUNGSVERSTÄNDNIS', 'offen'],
    ['ZIELGRUPPE|„WHAT’S IN FOR ME?“', 'Kunde · Vertrieb · Vertriebsvorstand|Vorstand · Controlling'],
  ];
  const EYE2 = { ...EYE, s: 9, ls: 1.2 };
  const SV = { x: 580, w: 190 };
  const svTitel = umbruch('Entschädigt wird, was vereinbart ist.', { f: 'L', s: 15, w: 700 }, SV.w - 36);
  const svPunkte = ['Leistung spürbar machen – größter Hebel: Schnelligkeit und Transparenz.', 'Erstattungsumfang: im Kleinen großzügig.', 'Schaden- und Prozesskosten klein halten ist unser Job.'].map(p => umbruch(p, { s: 10.5, c: SUB }, SV.w - 50));
  let hSV = 50 + svTitel.length * 19 + 6;
  svPunkte.forEach(p => { hSV += p.length * 14 + 6; });
  hSV += 12;
  const hA = 48 + hSV + 20;
  svg += rect(X0, y, XR - X0, hA, { fill: HELL, r: 16 });
  svg += t(X0 + 20, y + 30, 'WOFÜR STEHEN WIR?', { ...EYE, c: INK });
  const iy = y + 48;
  // drei gleich hohe Zeilen links, rechts das Selbstverständnis
  const EX = 140, EW = 548 - 140, rh = (hSV - 2 * 8) / 3;
  eingaben.forEach((e, i) => {
    const ry = iy + i * (rh + 8);
    svg += rect(EX, ry, EW, rh, { stroke: LINIE, r: 10 });
    const el = umbruch(e[0], EYE2, 160), bl = umbruch(e[1], { s: 11.5 }, EW - 200);
    svg += zeilen(EX + 16, ry + rh / 2 - (el.length - 1) * 6 + 3.5, el, EYE2, 12);
    svg += zeilen(EX + 184, ry + rh / 2 - (bl.length - 1) * 7.75 + 4, bl, { s: 11.5, c: INK }, 15.5);
  });
  svg += linie(552, iy + hSV / 2, 566, iy + hSV / 2) + `<path d="M${566} ${iy + hSV / 2 - 5.5} L${574} ${iy + hSV / 2} L${566} ${iy + hSV / 2 + 5.5} Z" fill="${INK}"/>`;
  svg += rect(SV.x, iy, SV.w, hSV, { fill: INK });
  svg += t(SV.x + 18, iy + 26, 'SELBSTVERSTÄNDNIS', { ...EYE, c: GELB });
  svg += zeilen(SV.x + 18, iy + 50, svTitel, { f: 'L', s: 15, w: 700, c: '#fff' }, 19);
  let py = iy + 50 + svTitel.length * 19 + 6;
  svg += linie(SV.x + 18, py - 8, SV.x + SV.w - 18, py - 8, { c: '#3d3a37', sw: 1 });
  svPunkte.forEach(p => {
    svg += `<circle cx="${SV.x + 22}" cy="${py + 6}" r="3" fill="${GELB}"/>`;
    svg += zeilen(SV.x + 32, py + 10, p, { s: 10.5, c: SUB }, 14);
    py += p.length * 14 + 6;
  });
  // Pfeil vom Selbstverständnis in die rechte Spalte
  const yB = y + hA + 34;
  svg += linie(cx(2), iy + hSV, cx(2), yB - 6) + pfeilRunter(cx(2), yB);

  // 2/3 · 1/3
  const boxA = [
    ['HEUTIGES GESCHÄFTS- UND ORGANISATIONSMODELL', 'Wie arbeitet das Schadenmanagement heute?'],
    ['STOSSRICHTUNGEN & HANDLUNGSFELDER', 'Der Weg vom Heute zum Zielbild.'],
    ['ZUKÜNFTIGES GESCHÄFTS- UND ORGANISATIONSMODELL', 'Neue Hauptabteilung oder eigenständige GmbH?'],
  ];
  const boxB = [
    ['FÜHRUNGS- UND ARBEITSALLTAG', 'Wie sichern wir die Zielerreichung?', null],
    ['STRATEGIEKOMMUNIKATION', 'Wie erklären wir die Strategie intern?', null],
    ['POSITIONIERUNG & PITCH', 'Welches Problem lösen wir – und was macht uns einzigartig?', 'Der Test: die Homepage deiner Abteilung.'],
  ];
  const BW = CW - 20;
  const aL = boxA.map(b => [umbruch(b[0], EYE2, BW - 28), umbruch(b[1], { s: 11.5 }, BW - 28)]);
  const hBA = 22 + Math.max(...aL.map(([e, b]) => e.length * 12 + 10 + b.length * 15.5)) + 12;
  const bL = boxB.map(b => [umbruch(b[0], EYE2, BW - 28), umbruch(b[1], { s: 11.5, w: 600 }, BW - 46), b[2] ? umbruch(b[2], { s: 11 }, BW - 28) : []]);
  const hBB = 22 + Math.max(...bL.map(([e, q, x]) => e.length * 12 + 12 + q.length * 15.5 + (x.length ? 8 + x.length * 15 : 0))) + 14;

  const rA = yB + 140, rB = rA + hBA + 40, unten = rB + hBB + 22;
  svg += rect(COL[0], yB, COL[1] + CW - COL[0], unten - yB, { fill: HELL, r: 16 });
  svg += rect(COL[2], yB, CW, unten - yB, { fill: HELL, r: 16 });
  svg += t((COL[0] + COL[1] + CW) / 2, yB + 28, 'WIE KOMMEN WIR DORTHIN?', { ...EYE, c: INK, a: 'middle' });
  svg += t(cx(2), yB + 28, 'WIE WOLLEN WIR', { ...EYE, c: INK, a: 'middle' });
  svg += t(cx(2), yB + 42, 'WAHRGENOMMEN WERDEN?', { ...EYE, c: INK, a: 'middle' });
  const ky = yB + 86;
  // 1 → 2 über die Strategie hinweg, 2 → 3 als Mission
  svg += `<path d="M${cx(0)} ${ky - 17} V${yB + 60} H${cx(2)} V${ky - 25}" fill="none" stroke="${INK}" stroke-width="2" stroke-linejoin="round"/>` + pfeilRunter(cx(2), ky - 17);
  svg += linie(cx(2) - 26, ky, cx(1) + 27, ky) + pfeilLinks(cx(1) + 19, ky);
  svg += t((COL[1] + CW + COL[2]) / 2, ky - 7, 'Mission', { s: 10.5, w: 600, c: GRAU, a: 'middle' });
  [['1', 0, 'Ausgangssituation'], ['3', 1, 'Strategie'], ['2', 2, 'Vision']].forEach(([n, i, name]) => {
    svg += `<circle cx="${cx(i)}" cy="${ky}" r="16" fill="${INK}"/>` + t(cx(i), ky + 4.5, n, { s: 13, w: 700, c: '#fff', a: 'middle' });
    svg += t(cx(i), ky + 42, name, { f: 'L', s: 17, w: 700, a: 'middle' });
  });
  aL.forEach(([e, b], i) => {
    const x = COL[i] + 10;
    svg += rect(x, rA, BW, hBA, { stroke: LINIE });
    svg += zeilen(x + 14, rA + 22, e, EYE2, 12);
    svg += zeilen(x + 14, rA + 22 + e.length * 12 + 10, b, { s: 11.5, c: INK }, 15.5);
  });
  // Detaillierung der Strategie: von 3 nach unten auf beide linken Spalten
  const dy = rA + hBA + 20;
  svg += linie(cx(1), rA + hBA, cx(1), dy) + linie(cx(0), dy, cx(1), dy) + linie(cx(0), dy, cx(0), rB - 6) + pfeilRunter(cx(0), rB) + linie(cx(1), dy, cx(1), rB - 6) + pfeilRunter(cx(1), rB);
  svg += t((cx(0) + cx(1)) / 2, dy - 6, 'Detaillierung der Strategie', { s: 10.5, w: 600, c: GRAU, a: 'middle' });
  svg += linie(cx(2), rA + hBA, cx(2), rB - 6) + pfeilRunter(cx(2), rB);
  const maxE = Math.max(...bL.map(b => b[0].length));
  bL.forEach(([e, q, x2], i) => {
    const x = COL[i] + 10, gelb = i === 2;
    svg += rect(x, rB, BW, hBB, gelb ? { fill: GELB, stroke: INK } : { stroke: LINIE });
    svg += zeilen(x + 14, rB + 22, e, { ...EYE2, c: gelb ? INK : GRAU }, 12);
    let qy = rB + 22 + maxE * 12 + 14;
    svg += `<circle cx="${x + 21}" cy="${qy - 4}" r="7" fill="${INK}"/>` + t(x + 21, qy - 0.5, '?', { s: 9.5, w: 700, c: '#fff', a: 'middle' });
    svg += zeilen(x + 34, qy, q, { s: 11.5, w: 600 }, 15.5);
    if (x2.length) svg += zeilen(x + 14, qy + q.length * 15.5 + 8, x2, { s: 11, c: INK }, 15);
  });

  // ---------- Fuß ----------
  const fy = unten + 56;
  svg += linie(X0, fy - 26, XR, fy - 26, { c: LINIE, sw: 1 });
  svg += t(X0, fy, 'empiria · Strategie in den Alltag überführen', { s: 11.5, c: GRAU });
  svg += t(XR, fy, 'Stand 15.10.2026', { s: 11.5, c: GRAU, a: 'end' });
  const H = fy + 50;

  // Leitlinie mit Stationen
  let lead = linie(SP, knoten[0], SP, knoten[knoten.length - 1], { c: LINIE, sw: 2 });
  knoten.forEach((ky2, i) => {
    lead += `<circle cx="${SP}" cy="${ky2}" r="17" fill="${INK}"/>` + t(SP, ky2 + 4.5, '0' + (i + 1), { s: 12, w: 700, c: GELB, a: 'middle' });
  });

  return `<svg class="sm-poster-svg" viewBox="0 0 ${W} ${H}" xmlns="http://www.w3.org/2000/svg" role="img" aria-label="Poster Schadenmanagement: vom Geschäftsmodell über die Grundlogik und die drei Oberziele zum Zielbild">
<rect width="${W}" height="${H}" fill="#fff"/>
${lead}
${svg}
</svg>`;
}

const browser = await puppeteer.launch({ executablePath: CHROME });
const page = await browser.newPage();
await page.goto(BASE + '/projekte/schadenmanagement.html', { waitUntil: 'networkidle0' });
await page.evaluate(async () => {
  for (const f of ['400 12px Poppins', '500 12px Poppins', '600 12px Poppins', '700 12px Poppins', '700 12px Lora']) await document.fonts.load(f);
});
const svg = await page.evaluate(bauen);
await browser.close();

let html = fs.readFileSync(SEITE, 'utf8');
const a = html.indexOf('<!-- POSTER:START -->'), b = html.indexOf('<!-- POSTER:END -->');
if (a < 0 || b < 0) throw new Error('POSTER-Marker fehlen');
html = html.slice(0, a + '<!-- POSTER:START -->'.length) + '\n' + svg + '\n' + html.slice(b);
fs.writeFileSync(SEITE, html);
console.log('Poster geschrieben, Höhe', svg.match(/viewBox="0 0 \d+ (\d+(\.\d+)?)"/)[1]);
