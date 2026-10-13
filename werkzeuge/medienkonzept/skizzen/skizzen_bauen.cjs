// Baut sechs Skizzen-Postings (1080 × 1350) als HTML-Sektionen für postings-vorlage.html.
// Figuren: Open Peeps (Pablo Stanley, CC0) · Handstrich: rough.js (MIT) · Handschrift: Caveat (OFL).
const { execFileSync } = require("child_process");
const fs = require("fs");
const rough = require("roughjs/bundled/rough.cjs.js");
const gen = rough.generator();
const INK = "#1a1817", GELB = "#fff400", HELL = "#f3f1ee", GRAU = "#a8a39c";

function peep(body, head, face, top, beard, x, y, w, flip) {
  let svg = execFileSync("node", [__dirname + "/composer.cjs", body, head, face, top || "#ffffff", beard || ""]).toString();
  svg = svg.replace(/#FF8181/gi, "#ffffff").replace(/fill="silver"/g, 'fill="#e4e0db"').replace(/fill="brown"/g, 'fill="#fff400"');
  const inner = svg.replace(/^<svg[^>]*>/, "").replace(/<\/svg>$/, "");
  const vb = "184.2 210.8 940.3 1130.6";
  const h = w * 1130.6 / 940.3;
  const t = flip ? ` transform="translate(${2 * x + w} 0) scale(-1 1)"` : "";
  return `<g${t}><svg x="${x}" y="${y}" width="${w}" height="${h}" viewBox="${vb}" overflow="visible">${inner}</svg></g>`;
}
function r(drawable, stroke, sw, fill) {
  return gen.toPaths(drawable).map(p => `<path d="${p.d}" fill="${p.fill || "none"}" stroke="${p.stroke === "none" ? "none" : stroke}" stroke-width="${p.strokeWidth || sw}" stroke-linecap="round" stroke-linejoin="round"/>`).join("");
}
const RO = (o) => Object.assign({ roughness: 1.6, bowing: 1.2, strokeWidth: 6, stroke: INK, seed: 3 }, o);
function hand(x, y, text, size, col, anchor, rot) {
  return `<text x="${x}" y="${y}" font-family="Caveat" font-weight="700" font-size="${size}" fill="${col || INK}" text-anchor="${anchor || "start"}"${rot ? ` transform="rotate(${rot} ${x} ${y})"` : ""}>${text}</text>`;
}
function pfeil(x1, y1, x2, y2, col, seed) {
  const a = Math.atan2(y2 - y1, x2 - x1), l = 34;
  let s = r(gen.curve([[x1, y1], [(x1 + x2) / 2 + 20, (y1 + y2) / 2 - 30], [x2, y2]], RO({ stroke: col, seed })), col, 6);
  s += r(gen.linearPath([[x2 - l * Math.cos(a - 0.5), y2 - l * Math.sin(a - 0.5)], [x2, y2], [x2 - l * Math.cos(a + 0.5), y2 - l * Math.sin(a + 0.5)]], RO({ stroke: col, seed: seed + 1 })), col, 6);
  return s;
}
const SVG = (inner, bg) => `<svg viewBox="0 0 1080 1350" width="1080" height="1350" style="position:absolute;inset:0">${bg ? `<rect width="1080" height="1350" fill="${bg}"/>` : ""}${inner}</svg>`;
const HEAD = (k, h, farbe) => `<div style="position:absolute;left:84px;top:84px;right:84px;z-index:2"><p class="k"${farbe ? ` style="color:${farbe}"` : ""}>${k}</p><p class="h" style="font-size:78px;line-height:1.1;margin-top:26px${farbe ? ";color:" + farbe : ""}">${h}</p></div>`;
const NAME = (c) => `<p class="namezeile" style="z-index:2${c ? ";color:" + c : ""}">Daniel Ströbel</p>`;
const out = [];
const sek = (id, cls, html) => out.push(`<section class="p sk2 ${cls}" id="${id}">${html}</section>`);

// 3 · Whiteboard (Handstrich, ohne Menschen): zwei Wege
{
  let g = "";
  const reihe = (y, labels, seed, gelb) => {
    let t = "";
    labels.forEach((l, i) => {
      const x = 84 + i * 340;
      t += r(gen.rectangle(x, y, 232, 150, RO({ seed: seed + i, fill: (gelb && i === 2) ? GELB : undefined, fillStyle: "solid" })), INK, 6);
      t += hand(x + 116, y + 95, l, 58, INK, "middle");
      if (i < 2) t += pfeil(x + 246, y + 75, x + 330, y + 75, INK, seed + 10 + i);
    });
    return t;
  };
  g += hand(84, 470, "So läuft es oft:", 60, GRAU) + reihe(510, ["Thema", "40 Folien", "vertagt"], 70, false);
  g += r(gen.line(84, 760, 996, 760, RO({ seed: 99, strokeWidth: 3, stroke: GRAU })), GRAU, 3);
  g += hand(84, 860, "So wird entschieden:", 60, GRAU) + reihe(900, ["Thema", "1 Seite", "Ja."], 90, true);
  sek("ss3", "", SVG(g, "#ffffff") + HEAD("Am Whiteboard", 'Gleiches Thema. Andere <span class="hl">Struktur.</span>') + NAME());
}
// 4 · Bild-Metapher Eisberg – sauber aufgebaut: Wasserlinie, symmetrische Form, Liste mit Trennlinien
{
  const W = 760; // Wasserlinie
  let g = `<rect y="${W}" width="1080" height="${1350 - W}" fill="${INK}"/>`;
  // Spitze über Wasser
  g += `<path d="M 360 ${W} L 470 560 L 520 610 L 572 470 L 630 590 L 670 555 L 752 ${W} Z" fill="${GELB}"/>`;
  g += `<text x="556" y="${W - 26}" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="46" fill="${INK}">Strategie</text>`;
  // Masse unter Wasser
  g += `<path d="M 380 ${W} L 732 ${W} L 900 880 L 960 1030 L 900 1180 L 700 1290 L 410 1290 L 210 1180 L 150 1030 L 210 880 Z" fill="#33302d"/>`;
  // Wasserlinie als feine Linie
  g += `<line x1="0" y1="${W}" x2="1080" y2="${W}" stroke="${GELB}" stroke-width="4"/>`;
  const zeilen = ["Regeltermine", "Abstimmungsschleifen", "Brände im Tagesgeschäft", "Vorlagen und Eskalationen"];
  zeilen.forEach((t, i) => {
    const y = 900 + i * 92;
    if (i > 0) g += `<line x1="330" y1="${y - 56}" x2="780" y2="${y - 56}" stroke="#4a4642" stroke-width="2"/>`;
    g += `<text x="555" y="${y}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="38" fill="#ffffff">${t}</text>`;
  });
  sek("ss4", "", SVG(g, HELL) + HEAD("Was man sieht – und was darunter liegt", 'Die Strategie ist nur die <span class="hl">Spitze.</span>') + NAME("#a8a39c").replace('class="namezeile"', 'class="namezeile" style="z-index:3"'));
}
// 5 · Isometrische Bausteine: 12 Regeltermine auf der Strategie
{
  const cube = (cx, cy, s, top, left, right, k) => {
    const h = s * 0.58, d = s * 1.05, st = ` stroke="${k}" stroke-width="3" stroke-linejoin="round"`;
    return `<path d="M ${cx} ${cy - h} L ${cx + s} ${cy} L ${cx} ${cy + h} L ${cx - s} ${cy} Z" fill="${top}"${st}/>` +
      `<path d="M ${cx - s} ${cy} L ${cx} ${cy + h} L ${cx} ${cy + h + d} L ${cx - s} ${cy + d} Z" fill="${left}"${st}/>` +
      `<path d="M ${cx + s} ${cy} L ${cx} ${cy + h} L ${cx} ${cy + h + d} L ${cx + s} ${cy + d} Z" fill="${right}"${st}/>`;
  };
  let g = "", s = 66, gap = 1.12;
  const pos = [];
  for (let z = 0; z < 3; z++) for (let a = 0; a < 2; a++) for (let b = 0; b < 2; b++) pos.push([a, b, z]);
  pos.sort((p, q) => (p[2] - q[2]) || ((p[0] + p[1]) - (q[0] + q[1])));
  const basisY = 1020;
  for (const [a, b, z] of pos) {
    const cx = 540 + (a - b) * s * gap, cy = basisY - 200 + (a + b) * s * 0.58 * gap - z * s * 1.05 * gap;
    g += cube(cx, cy, s, "#4a4642", INK, "#2b2826", "#f3f1ee");
  }
  g += cube(540, basisY + 70, 46, GELB, "#d9cf00", "#ebe100", INK);
  g += hand(780, 560, "12 Regel-", 62, INK, "start", -6) + hand(790, 622, "termine", 62, INK, "start", -6);
  g += hand(700, 1220, "die Strategie", 62, INK, "start", -4) + pfeil(700, 1195, 600, 1130, INK, 141);
  sek("ss5", "", SVG(g, HELL) + HEAD("Die Woche einer neuen Führungskraft", 'Zwölf Termine. Die Strategie liegt <span class="hl">daneben.</span>') + NAME());
}
// 6 · Foto mit Kritzelei (Handstrich über deinem Foto)
{
  let g = `<image href="/assets/projekte/medienkonzept/voll-e2.jpg" x="-260" y="0" width="1800" height="1350" preserveAspectRatio="xMidYMid slice"/>`;
  g += `<defs><linearGradient id="vl" x1="0" y1="0" x2="0" y2="1"><stop offset=".5" stop-color="#1a1817" stop-opacity="0"/><stop offset="1" stop-color="#1a1817" stop-opacity=".88"/></linearGradient></defs><rect width="1080" height="1350" fill="url(#vl)"/>`;
  g += r(gen.ellipse(470, 230, 560, 230, RO({ seed: 111, stroke: GELB, strokeWidth: 9 })), GELB, 9);
  g += pfeil(330, 1020, 450, 400, GELB, 120);
  g += hand(84, 1140, "Hier entscheidet sich,", 84, GELB, "start", -3) + hand(90, 1225, "ob sie wirkt.", 84, GELB, "start", -3);
  sek("ss6", "", SVG(g) + NAME("#ffffff"));
}
fs.writeFileSync(process.argv[2], out.join("\n"));
console.log("Skizzen:", out.length);
