import puppeteer from "puppeteer-core";
import fs from "fs";

const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const BASE = process.env.BASE || "http://localhost:4599/index.html";
const OUT = process.env.OUT || "./_shots";
fs.mkdirSync(OUT, { recursive: true });

const targets = [
  { name: "desktop", width: 1440, height: 900, dsf: 1, full: true },
  { name: "mobile", width: 375, height: 812, dsf: 2, full: true },
];

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: "new",
  args: ["--no-sandbox", "--force-color-profile=srgb", "--hide-scrollbars"],
});

const errors = [];
for (const t of targets) {
  const page = await browser.newPage();
  page.on("console", (m) => { if (m.type() === "error") errors.push(`[${t.name}] console: ${m.text()}`); });
  page.on("pageerror", (e) => errors.push(`[${t.name}] pageerror: ${e.message}`));
  await page.setViewport({ width: t.width, height: t.height, deviceScaleFactor: t.dsf });
  await page.goto(BASE, { waitUntil: "networkidle0", timeout: 30000 });
  await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });
  await new Promise((r) => setTimeout(r, 350));
  await page.screenshot({ path: `${OUT}/shot-${t.name}.png`, fullPage: !!t.full });
  await page.close();
}

// Optional: open a modal on desktop and screenshot it
{
  const page = await browser.newPage();
  await page.setViewport({ width: 1440, height: 900, deviceScaleFactor: 1 });
  await page.goto(BASE, { waitUntil: "networkidle0" });
  await page.evaluate(async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; });
  await page.evaluate(() => document.querySelector('[data-modal="komplex"]').click());
  await new Promise((r) => setTimeout(r, 450));
  await page.screenshot({ path: `${OUT}/shot-modal.png` });
  await page.close();
}

if (errors.length) {
  console.log("=== PAGE ERRORS ===");
  errors.forEach((e) => console.log(e));
} else {
  console.log("No console/page errors.");
}
await browser.close();
