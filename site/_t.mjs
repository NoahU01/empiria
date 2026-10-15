import puppeteer from 'puppeteer-core';
const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:'new'});
const p=await b.newPage();await p.setViewport({width:1440,height:900});
for(const s of ['hausverwalter','hausverwaltung-1','immobilienverwaltung','hausverwaltungen-1','weg-verwaltung','verwalter','hausverwaltung-sv','hausverwaltungen-owen']){
 const r=await p.goto('https://sv-owen.sofortsichtbar.de/'+s,{waitUntil:'networkidle2',timeout:45000}).catch(e=>null);
 console.log(s, r?r.status():'ERR', (await p.title()).slice(0,80));}
await p.goto('https://sv-owen.sofortsichtbar.de/landwirtschaft',{waitUntil:'networkidle2'});
console.log(await p.evaluate(()=>[...new Set([...document.querySelectorAll('a')].map(a=>a.href))].join('\n')));
await b.close();
