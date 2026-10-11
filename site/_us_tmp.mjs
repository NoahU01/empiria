import puppeteer from 'puppeteer-core';
const b=await puppeteer.launch({executablePath:'/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',headless:'new'});
const p=await b.newPage();await p.setViewport({width:1400,height:1400});
await p.setUserAgent('Mozilla/5.0 (Macintosh; Intel Mac OS X 14_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126 Safari/537.36');
for(const q of process.argv.slice(2)){
 await p.goto('https://unsplash.com/s/photos/'+q+'?license=free',{waitUntil:'networkidle2',timeout:60000}).catch(e=>console.log('ERR',e.message));
 await p.evaluate(()=>window.scrollBy(0,1500));await new Promise(r=>setTimeout(r,1500));
 const r=await p.evaluate(()=>[...document.querySelectorAll('figure img[srcset]')].map(i=>({alt:i.alt,src:i.src.split('?')[0]})).filter(x=>/images\.unsplash\.com\/photo-1[456]/.test(x.src)));
 const seen=new Set();console.log('##',q);r.filter(x=>!seen.has(x.src)&&seen.add(x.src)).slice(0,14).forEach(x=>console.log(x.src.replace('https://images.unsplash.com/photo-',''),'|',x.alt.slice(0,80)));
}
await b.close();
