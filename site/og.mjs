/* Generates assets/og-image.png (1200x630) for OpenGraph/Twitter cards.
   Run from site/ with a local server on :4599 so the fonts/logo resolve:
     python3 -m http.server 4599 &   node og.mjs
   Re-run only when the brand mark or claim changes. */
import puppeteer from "puppeteer-core";

const CHROME = process.env.CHROME || "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome";
const BASE = process.env.BASE || "http://localhost:4599/";

const html = `<!doctype html><html lang="de"><head><meta charset="utf-8">
<link rel="stylesheet" href="assets/fonts/fonts.css">
<style>
  html,body{margin:0}
  body{width:1200px;height:630px;background:#fff;font-family:Poppins,sans-serif;
       display:flex;flex-direction:column;justify-content:center;padding:0 92px;box-sizing:border-box}
  .logo{width:340px;margin-bottom:56px}
  h1{font-family:Lora,serif;font-weight:600;font-size:82px;line-height:1.08;
     letter-spacing:-.01em;color:#1a1817;margin:0 0 28px}
  .hl{background:linear-gradient(#fff400,#fff400) 0 76%/100% 42% no-repeat;font-weight:700}
  p{font-size:27px;line-height:1.45;color:#2e2d2c;margin:0;max-width:830px}
  .bar{position:absolute;left:0;bottom:0;width:100%;height:16px;background:#fff400}
</style></head><body>
  <img class="logo" src="assets/empiria-logo.svg" alt="">
  <h1>Strategie,<br>die <span class="hl">wirkt.</span></h1>
  <p>Strategieberatung f&uuml;r F&uuml;hrungskr&auml;fte in der Versicherungsbranche.</p>
  <div class="bar"></div>
</body></html>`;

const browser = await puppeteer.launch({
  executablePath: CHROME,
  headless: "new",
  args: ["--no-sandbox", "--force-color-profile=srgb", "--hide-scrollbars"],
});
const page = await browser.newPage();
await page.setViewport({ width: 1200, height: 630, deviceScaleFactor: 1 });
// goto first so the relative asset paths in `html` resolve against the server
await page.goto(BASE, { waitUntil: "domcontentloaded" });
await page.setContent(html, { waitUntil: "networkidle0" });
await page.evaluate(async () => { if (document.fonts) await document.fonts.ready; });
await new Promise((r) => setTimeout(r, 300));
await page.screenshot({ path: "assets/og-image.png" });
await browser.close();
console.log("wrote assets/og-image.png");
