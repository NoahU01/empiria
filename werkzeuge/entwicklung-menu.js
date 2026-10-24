(function(){
function init(){
var here=location.href.split('#')[0].split('?')[0];
document.querySelectorAll('[data-dev-dd]').forEach(function(d){
var b=d.querySelector('.dev-dd-toggle'),t;
function desk(){return window.innerWidth>900;}
function set(o){d.classList.toggle('is-open',o);b.setAttribute('aria-expanded',String(o));
if(!o)d.querySelectorAll('.is-auf').forEach(function(x){x.classList.remove('is-auf');});}
b.addEventListener('click',function(e){e.stopPropagation();set(desk()&&d.matches(':hover')?true:!d.classList.contains('is-open'));});
d.addEventListener('mouseenter',function(){if(desk()){clearTimeout(t);set(true);}});
d.addEventListener('mouseleave',function(){if(desk()){t=setTimeout(function(){set(false);},180);}});
document.addEventListener('click',function(e){if(!d.contains(e.target))set(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false);});
d.querySelectorAll('.dev-dd-link').forEach(function(a){if(a.href&&a.href.split('#')[0]===here)a.classList.add('is-current');});

var panel=d.querySelector('.dev-dd-panel');

// ---- Antippen statt Hover (iPad quer, Touch-Laptops) ---------------------
// Ohne Maus gibt es kein Hover: der Tipp auf eine Zeile mit Unterseiten
// sprang sofort auf deren Seite, die Unterseiten waren nie zu sehen.
// Jetzt klappt der erste Tipp die naechste Ebene auf, erst der zweite Tipp
// auf dieselbe Zeile oeffnet die Seite. Ob die Ebene schon offen war, wird
// beim pointerdown gemerkt - das kommt vor dem simulierten mouseenter.
function antippen(a,offen,oeffnen){
var tipp=false,war=false;
a.addEventListener('pointerdown',function(e){tipp=e.pointerType!=='mouse';war=offen();});
a.addEventListener('click',function(e){
if(!tipp||!desk()||war)return;
e.preventDefault();oeffnen();
});
}

// ---- Zweite Ebene -------------------------------------------------------
// Das Panel muss scrollen, seit es vier Kategorien hat (gemessen: 834px
// Inhalt bei 680px Platz auf einem 900er Bildschirm). Ein Flyout darin wuerde
// mitgeschnitten. position:fixed hilft nicht - die Kopfzeile hat einen
// backdrop-filter und wird dadurch zum Bezugsrahmen fuer fixed. Das Flyout
// haengt sich beim Oeffnen deshalb unter .dev-dd um: dort ist es absolut
// positioniert, aber ausserhalb des scrollenden Panels.
// Weil :hover dort nicht mehr traegt, steuert eine Klasse die Sichtbarkeit.
panel&&panel.querySelectorAll(':scope>.dev-dd-sub').forEach(function(s){
var f=s.querySelector(':scope>.dev-dd-flyout');if(!f)return;
var heim=f.parentNode,nachbar=f.nextSibling,t2;
f._kinder=[];
function kinderZu(){f._kinder.forEach(function(k){k();});}
function heimholen(){
clearTimeout(t2);f.classList.remove('is-auf');s.classList.remove('is-auf');kinderZu();
if(f.parentNode!==heim){heim.insertBefore(f,nachbar);f.removeAttribute('style');}
}
function auf(){
if(!desk()){heimholen();return;}
clearTimeout(t2);
if(f.parentNode!==d)d.appendChild(f);
var z=s.getBoundingClientRect(),dr=d.getBoundingClientRect(),
    k=f.firstElementChild.getBoundingClientRect();
// Rechts daneben, wenn Platz ist - sonst nach links gekippt.
if(z.right+10+k.width>window.innerWidth-12){
f.style.left=(z.left-dr.left-10-k.width)+'px';
f.style.paddingLeft='0';f.style.paddingRight='10px';
}else{
f.style.left=(z.right-dr.left)+'px';
f.style.paddingLeft='';f.style.paddingRight='';
}
// Senkrecht an der Zeile, aber nie unter den Fensterrand.
var oben=z.top-dr.top-10,grenze=window.innerHeight-12-k.height-dr.top;
f.style.top=Math.max(-dr.top+12,Math.min(oben,grenze))+'px';
f.classList.add('is-auf');s.classList.add('is-auf');
}
function zu(){t2=setTimeout(function(){f.classList.remove('is-auf');s.classList.remove('is-auf');kinderZu();},180);}
f._halten=function(){clearTimeout(t2);};f._zu=zu;
s.addEventListener('mouseenter',auf);
s.addEventListener('focusin',auf);
s.addEventListener('mouseleave',zu);
f.addEventListener('mouseenter',function(){clearTimeout(t2);});
f.addEventListener('mouseleave',zu);
panel.addEventListener('scroll',function(){if(f.classList.contains('is-auf'))auf();});
antippen(s.querySelector(':scope>a.dev-dd-link--parent'),
function(){return f.classList.contains('is-auf');},
function(){d.querySelectorAll(':scope>.dev-dd-flyout.is-auf').forEach(function(x){if(x!==f)x.classList.remove('is-auf');});
panel.querySelectorAll(':scope>.dev-dd-sub.is-auf').forEach(function(x){if(x!==s)x.classList.remove('is-auf');});
auf();});
window.addEventListener('resize',heimholen);
});

// ---- Dritte Ebene -------------------------------------------------------
// Die zweite Ebene scrollt jetzt selbst, wenn sie hoeher ist als das Fenster
// (Daniel, 24.10.2026). Eine dritte Ebene darin wuerde mitgeschnitten - sie
// haengt sich deshalb wie die zweite beim Oeffnen unter .dev-dd um.
d.querySelectorAll('.dev-dd-flyout .dev-dd-sub').forEach(function(s){
var f=s.querySelector(':scope>.dev-dd-flyout');if(!f)return;
var heim=f.parentNode,nachbar=f.nextSibling,eltern=s.closest('.dev-dd-flyout'),t3;
function heimholen(){
clearTimeout(t3);f.classList.remove('is-auf');s.classList.remove('is-auf');
if(f.parentNode!==heim){heim.insertBefore(f,nachbar);f.removeAttribute('style');}
}
if(eltern&&eltern._kinder)eltern._kinder.push(heimholen);
function auf(){
if(!desk()){heimholen();return;}
clearTimeout(t3);
if(eltern&&eltern._kinder)eltern._kinder.forEach(function(k){if(k!==heimholen)k();});
if(f.parentNode!==d)d.appendChild(f);
var z=s.getBoundingClientRect(),dr=d.getBoundingClientRect(),
    k=f.firstElementChild.getBoundingClientRect();
if(z.right+10+k.width>window.innerWidth-12){
f.style.left=(z.left-dr.left-10-k.width)+'px';
f.style.paddingLeft='0';f.style.paddingRight='10px';
}else{
f.style.left=(z.right-dr.left)+'px';
f.style.paddingLeft='';f.style.paddingRight='';
}
var oben=z.top-dr.top-10,grenze=window.innerHeight-12-k.height-dr.top;
f.style.top=Math.max(-dr.top+12,Math.min(oben,grenze))+'px';
f.classList.add('is-auf');s.classList.add('is-auf');
}
function zu(){t3=setTimeout(heimholen,180);}
s.addEventListener('mouseenter',auf);
s.addEventListener('focusin',auf);
s.addEventListener('mouseleave',zu);
f.addEventListener('mouseenter',function(){clearTimeout(t3);if(eltern&&eltern._halten)eltern._halten();});
f.addEventListener('mouseleave',function(){zu();if(eltern&&eltern._zu)eltern._zu();});
if(eltern)eltern.firstElementChild.addEventListener('scroll',heimholen);
antippen(s.querySelector(':scope>a.dev-dd-link--parent'),
function(){return f.classList.contains('is-auf');},auf);
window.addEventListener('resize',heimholen);
});
});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
