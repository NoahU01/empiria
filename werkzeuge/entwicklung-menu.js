(function(){
function init(){
var here=location.href.split('#')[0].split('?')[0];
document.querySelectorAll('[data-dev-dd]').forEach(function(d){
var b=d.querySelector('.dev-dd-toggle'),t;
function desk(){return window.innerWidth>900;}
function set(o){d.classList.toggle('is-open',o);b.setAttribute('aria-expanded',String(o));}
b.addEventListener('click',function(e){e.stopPropagation();set(desk()&&d.matches(':hover')?true:!d.classList.contains('is-open'));});
d.addEventListener('mouseenter',function(){if(desk()){clearTimeout(t);set(true);}});
d.addEventListener('mouseleave',function(){if(desk()){t=setTimeout(function(){set(false);},180);}});
document.addEventListener('click',function(e){if(!d.contains(e.target))set(false);});
document.addEventListener('keydown',function(e){if(e.key==='Escape')set(false);});
d.querySelectorAll('.dev-dd-link').forEach(function(a){if(a.href.split('#')[0]===here)a.classList.add('is-current');});
// Flyouts platzieren. Zwei Faelle:
// 1. Senkrecht: ein Flyout weit unten in der Liste rutscht sonst unter den
//    Fensterrand (gemessen: 925px bei 813px Fensterhoehe). Es wird beim
//    Oeffnen genau um den Ueberstand nach oben geschoben.
// 2. Waagerecht: seit das Archiv eine eigene Ebene hat, gibt es eine dritte.
//    Die passt rechts nicht mehr neben die zweite und klappt dann nach links
//    auf. Gilt auch fuer die zweite Ebene in schmalen Fenstern.
// ':scope>' ist wichtig: ein verschachteltes Flyout liegt ebenfalls unter
// seinem Elternteil und wuerde sonst mitgemessen.
d.querySelectorAll('.dev-dd-sub').forEach(function(s){
var f=s.querySelector(':scope>.dev-dd-flyout');
if(!f)return;
function zuruecksetzen(){f.style.top='';f.style.left='';f.style.right='';f.style.paddingLeft='';f.style.paddingRight='';}
function platzieren(){
if(!desk()){zuruecksetzen();return;}
zuruecksetzen();
f.style.top='-10px';
var r=f.getBoundingClientRect();
var u=r.bottom-(window.innerHeight-12);
if(u>0)f.style.top=(-10-u)+'px';
if(r.right>window.innerWidth-12){
f.style.left='auto';f.style.right='100%';
f.style.paddingLeft='0';f.style.paddingRight='10px';
}
}
s.addEventListener('mouseenter',platzieren);
s.addEventListener('focusin',platzieren);
window.addEventListener('resize',zuruecksetzen);
});
});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
