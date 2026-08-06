/* Erzeugt den Favicon-Satz aus dem echten Brand-Icon `ic-forward`
   (dasselbe Symbol wie der Pfeil in der Hero-Sektion).

   Die Pfade werden aus index.html gelesen — nie von Hand kopieren, sonst
   laufen Icon und Seite auseinander.

   Ausgabe (alle im site/-Root, damit sie unter / erreichbar sind):
     favicon.svg           moderne Browser, skaliert verlustfrei
     favicon.ico           16+32 px, Legacy + Googles SERP-Crawler
     apple-touch-icon.png  180 px, iOS-Homescreen (ohne Radius, iOS maskiert selbst)

   Lauf:  python3 -m http.server 4599 &   node favicon.mjs
   Nur neu erzeugen, wenn sich das Markenicon ändert.

   ACHTUNG: Google cached Favicons in den SERPs wochenlang separat — ein
   Wechsel schlägt dort erst mit Verzögerung durch. */
import puppeteer from "puppeteer-core";
import fs from "fs";

const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const BLACK = "#000000";
const WHITE = "#ffffff";
const MARGIN = 1.171;   // Kanten-Luft: Icon füllt ~85 % der Kachel

/* ---- 1. Pfade des Symbols aus index.html ziehen ---- */
const html = fs.readFileSync("index.html", "utf8");
const sym = /<symbol id="ic-forward"[^>]*>([\s\S]*?)<\/symbol>/.exec(html);
if (!sym) throw new Error("Symbol ic-forward nicht in index.html gefunden");
const paths = [...sym[1].matchAll(/\sd="([^"]+)"/g)].map((m) => m[1]);
if (paths.length !== 2) throw new Error(`Erwartet 2 Pfade, gefunden ${paths.length}`);

const browser = await puppeteer.launch({
  executablePath: CHROME, headless: "new",
  args: ["--no-sandbox", "--force-color-profile=srgb"],
});
const page = await browser.newPage();

/* ---- 2. Echte Bounding-Box messen, damit das Icon exakt zentriert sitzt ----
   Das Symbol ist in seiner viewBox nicht zentriert (y läuft von ~31 bis ~201),
   stures Übernehmen der viewBox würde den Pfeil sichtbar nach unten versetzen. */
await page.setContent(`<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 232.44 232.44">
  <g id="g">${paths.map((d) => `<path d="${d}"/>`).join("")}</g></svg>`);
const bb = await page.evaluate(() => {
  const { x, y, width, height } = document.getElementById("g").getBBox();
  return { x, y, width, height };
});
const side = Math.max(bb.width, bb.height) * MARGIN;
const vb = [
  bb.x - (side - bb.width) / 2,
  bb.y - (side - bb.height) / 2,
  side, side,
].map((n) => +n.toFixed(2)).join(" ");

const tile = (rx, fill) =>
  `<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 100 100">
  <rect width="100" height="100" rx="${rx}" fill="${BLACK}"/>
  <svg viewBox="${vb}" width="100" height="100">
    <g fill="${fill}">${paths.map((d) => `<path d="${d}"/>`).join("")}</g>
  </svg>
</svg>`;

/* ---- 3. favicon.svg ---- */
fs.writeFileSync("favicon.svg", tile(22, WHITE) + "\n");

/* ---- 4. PNGs rendern ---- */
async function png(svg, size) {
  await page.setViewport({ width: size, height: size, deviceScaleFactor: 1 });
  await page.setContent(
    `<body style="margin:0;width:${size}px;height:${size}px">
       <img width="${size}" height="${size}" src="data:image/svg+xml;utf8,${encodeURIComponent(svg)}">
     </body>`
  );
  await new Promise((r) => setTimeout(r, 120));
  return await page.screenshot({ omitBackground: true });
}

const ico16 = await png(tile(22, WHITE), 16);
const ico32 = await png(tile(22, WHITE), 32);
const ico48 = await png(tile(22, WHITE), 48);
fs.writeFileSync("apple-touch-icon.png", await png(tile(0, WHITE), 180)); // iOS maskiert selbst

/* ---- 5. favicon.ico packen (ICO mit eingebetteten PNGs) ----
   Aufbau: ICONDIR (6 B) + n × ICONDIRENTRY (16 B) + Bilddaten. */
function buildIco(images) {
  const dir = Buffer.alloc(6);
  dir.writeUInt16LE(0, 0);              // reserved
  dir.writeUInt16LE(1, 2);              // type 1 = Icon
  dir.writeUInt16LE(images.length, 4);
  let offset = 6 + images.length * 16;
  const entries = [], blobs = [];
  for (const { size, data } of images) {
    const e = Buffer.alloc(16);
    e.writeUInt8(size >= 256 ? 0 : size, 0);   // 0 bedeutet 256
    e.writeUInt8(size >= 256 ? 0 : size, 1);
    e.writeUInt8(0, 2);                        // Farbpalette: keine
    e.writeUInt8(0, 3);                        // reserved
    e.writeUInt16LE(1, 4);                     // color planes
    e.writeUInt16LE(32, 6);                    // bits per pixel
    e.writeUInt32LE(data.length, 8);
    e.writeUInt32LE(offset, 12);
    offset += data.length;
    entries.push(e); blobs.push(data);
  }
  return Buffer.concat([dir, ...entries, ...blobs]);
}
fs.writeFileSync("favicon.ico", buildIco([
  { size: 16, data: ico16 },
  { size: 32, data: ico32 },
  { size: 48, data: ico48 },
]));

await browser.close();
console.log("viewBox:", vb);
for (const f of ["favicon.svg", "favicon.ico", "apple-touch-icon.png"]) {
  console.log(`  ${f.padEnd(22)} ${fs.statSync(f).size} B`);
}
