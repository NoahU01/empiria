import puppeteer from 'puppeteer-core';import fs from 'fs';
const dir=process.argv[2];const fs2=fs.readdirSync(dir).filter(f=>f.startsWith('u-')).sort();
const html='<body style="margin:0;display:grid;grid-template-columns:repeat(5,1fr);gap:6px;font:13px sans-serif">'+fs2.map(f=>`<div><img src="file://${dir}/${f}" style="width:100%;height:200px;object-fit:cover;display:block"><div>${f.slice(2,15)}</div></div>`).join('')+'</body>';
fs.writeFileSync(dir+'/m.html',html);
const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:'new',args:['--allow-file-access-from-files']});
const p=await b.newPage();await p.setViewport({width:1400,height:800});await p.goto('file://'+dir+'/m.html');await new Promise(r=>setTimeout(r,1500));await p.screenshot({path:dir+'/montage.png',fullPage:true});await b.close();
