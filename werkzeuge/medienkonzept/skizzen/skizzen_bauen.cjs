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

// 1 · Gezeichnete Szene (Open Peeps): Lenkungsausschuss
{
  let g = "";
  g += r(gen.rectangle(110, 420, 330, 230, RO({ seed: 4 })), INK, 6);
  g += `<text x="275" y="565" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="76" fill="${INK}" letter-spacing="-3">37/40</text>`;
  g += peep("Explaining", "ShortTwo", "Explaining", GELB, "", 470, 420, 400, true);
  g += peep("Coffee", "Bald", "Tired", "#ffffff", "MustacheThin", 40, 830, 360);
  g += peep("Paper", "MediumBangs", "Solemn", "#ffffff", "", 360, 840, 360);
  g += peep("ButtonShirt", "GrayShort", "Suspicious", "#ffffff", "", 680, 830, 360);
  g += `<rect x="0" y="1180" width="1080" height="170" fill="#ffffff"/>` + r(gen.line(30, 1182, 1050, 1182, RO({ seed: 9, strokeWidth: 7 })), INK, 7);
  sek("ss1", "", SVG(g, "#ffffff") + HEAD("Lenkungsausschuss", 'Folie 37 von 40. Entschieden wird <span class="hl">nichts.</span>') + NAME());
}
// 2 · Porträt mit Notizen: Montag nach dem Auftakt
{
  let g = peep("ButtonShirt", "NoHairTwo", "Concerned", "#ffffff", "Goatee", 300, 560, 480);
  g += hand(84, 520, "12 Regeltermine", 60, INK, "start", -6) + pfeil(250, 545, 400, 690, INK, 21);
  g += hand(800, 500, "Mails", 64, INK, "start", 6) + pfeil(850, 525, 740, 680, INK, 31);
  g += hand(84, 1010, "Vorstands-", 58, INK, "start", -4) + hand(90, 1068, "beschwerde", 58, INK, "start", -4) + pfeil(250, 980, 360, 900, INK, 41);
  g += hand(820, 960, "Brand!", 66, INK, "start", 8) + pfeil(860, 990, 760, 920, INK, 51);
  g += r(gen.ellipse(540, 1210, 380, 120, RO({ seed: 61, stroke: INK, fill: GELB, fillStyle: "solid" })), INK, 6) + hand(540, 1228, "Und die Strategie?", 54, INK, "middle", -3);
  sek("ss2", "", SVG(g, "#ffffff") + HEAD("Montag nach dem Auftakt", 'Alles brennt. Nur nicht die <span class="hl">Strategie.</span>'));
}
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
// 4 · Bild-Metapher Eisberg (Fläche, ohne Menschen)
{
  let g = `<rect y="760" width="1080" height="590" fill="${INK}"/>`;
  g += `<path d="M 380 760 L 470 640 L 515 670 L 580 560 L 640 640 L 690 610 L 760 760 Z" fill="${GELB}"/>`;
  g += `<path d="M 330 760 L 800 760 L 930 900 L 960 1060 L 860 1230 L 620 1310 L 360 1270 L 170 1120 L 140 940 Z" fill="#3a3632"/>`;
  g += `<text x="570" y="735" text-anchor="middle" font-family="Poppins" font-weight="700" font-size="42" fill="${INK}">Strategie</text>`;
  ["Regeltermine", "Abstimmungsschleifen", "Brände im Tagesgeschäft", "Mails · Vorlagen · Eskalationen"].forEach((t, i) => {
    g += `<text x="540" y="${880 + i * 90}" text-anchor="middle" font-family="Poppins" font-weight="600" font-size="38" fill="#ffffff">${t}</text>`;
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
