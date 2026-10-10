// node seiten.mjs quelle.html ordner vorschau-präfix  → je Seite ein PNG + die ersten zwei als Vorschau
import puppeteer from "../../site/node_modules/puppeteer-core/lib/esm/puppeteer/puppeteer-core.js";
import fs from "fs";
const [,, src, dir, vorschau] = process.argv;
fs.mkdirSync(dir, { recursive: true });
const b = await puppeteer.launch({ executablePath: "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome", headless: "new", args: ["--allow-file-access-from-files"] });
const p = await b.newPage();
await p.setViewport({ width: 794, height: 1123, deviceScaleFactor: 2 });
await p.goto("file://" + src, { waitUntil: "networkidle0" });
await p.evaluate(() => document.fonts.ready);
const seiten = await p.$$(".seite");
let i = 0;
for (const s of seiten) {
  i++;
  await s.screenshot({ path: `${dir}/seite-${i}.png` });
  if (vorschau && i <= 2) fs.copyFileSync(`${dir}/seite-${i}.png`, `${vorschau}-${i}.png`);
}
// Prüfung: nichts darf über eine Seite hinauslaufen
const fehler = await p.evaluate(() => {
  const out = [];
  document.querySelectorAll(".seite").forEach((s, n) => {
    const r = s.getBoundingClientRect();
    s.querySelectorAll("*").forEach(e => { const q = e.getBoundingClientRect(); if (q.width && (q.right > r.right + 1 || q.bottom > r.bottom + 1)) out.push(`Seite ${n + 1}: ${e.className || e.tagName} ragt heraus`); });
  });
  return [...new Set(out)].slice(0, 20);
});
console.log(i + " Seiten" + (fehler.length ? "\n" + fehler.join("\n") : " · nichts ragt heraus"));
await b.close();
