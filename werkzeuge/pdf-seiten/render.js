const { chromium } = require('playwright');
(async()=>{const b=await chromium.launch({executablePath:'/opt/pw-browsers/chromium'});
for (const s of process.argv.slice(2)) { const p=await b.newPage({viewport:{width:794,height:1123}});
 await p.goto('file:///home/claude/w/cowork-vorschau/_pdfsrc_'+s+'.html',{waitUntil:'networkidle'}); await p.evaluate(()=>document.fonts.ready);
 const issues = await p.evaluate(()=>{const mm=3.7795;const out=[];
  document.querySelectorAll('.page').forEach((pg,i)=>{const r=pg.getBoundingClientRect();
   const kids=[...pg.children].filter(c=>!c.matches('.contact,.footer,.head,.sketch,.facts'));
   let bottom=0; kids.forEach(k=>{bottom=Math.max(bottom,k.getBoundingClientRect().bottom-r.top); k.querySelectorAll('*').forEach(e=>{const b=e.getBoundingClientRect(); if(b.height>0) bottom=Math.max(bottom,b.bottom-r.top); if(b.right-r.left>r.width-10) out.push(`p${i+1} right overflow ${e.className||e.tagName} ${Math.round(b.right-r.left)}`)})});
   const c=pg.querySelector('.contact'), sk=pg.querySelector('.sketch'), f=pg.querySelector('.facts');
   let limit = c ? c.getBoundingClientRect().top-r.top-6*mm : (sk? sk.getBoundingClientRect().top-r.top-4*mm : r.height-14*mm);
   if (c) { const ft=pg.querySelector('.footer'); if(ft && c.getBoundingClientRect().bottom > ft.getBoundingClientRect().top-8*mm) out.push(`p${i+1} contact hits footer`);}
   out.push(`p${i+1} free ${((limit-bottom)/mm).toFixed(1)}mm`);
  }); return out;});
 console.log(s, issues.join(' | '));
 await p.pdf({path:'/home/claude/w/out/empiria-'+s+'.pdf',format:'A4',printBackground:true,preferCSSPageSize:true}); await p.close(); }
await b.close();})();
