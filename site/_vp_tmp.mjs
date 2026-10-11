import puppeteer from 'puppeteer-core';
const [url,out,w,h,...sels]=process.argv.slice(2);
const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:'new'});
const p=await b.newPage();await p.setViewport({width:+w,height:+h});
await p.goto(url,{waitUntil:'networkidle0'});await new Promise(r=>setTimeout(r,1500));
let i=0;for(const s of sels){
 if(s.startsWith('y')){await p.evaluate(y=>window.scrollTo(0,y),+s.slice(1));}
 else if(s!=='top'){await p.evaluate(s=>{const e=document.querySelector(s);window.scrollTo(0,e.getBoundingClientRect().top+scrollY-70)},s);}
 await new Promise(r=>setTimeout(r,1200));await p.screenshot({path:`${out}/v${w}-${i++}.png`});}
await b.close();
