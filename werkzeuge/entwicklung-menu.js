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
// Zweite Ebene: ein Flyout weit unten in der Liste wuerde sonst unter den
// Fensterrand rutschen (gemessen: 925px bei 813px Fensterhoehe). Es wird
// deshalb beim Oeffnen genau um den Ueberstand nach oben geschoben.
d.querySelectorAll('.dev-dd-sub').forEach(function(s){
var f=s.querySelector('.dev-dd-flyout');
if(!f)return;
function platzieren(){
if(!desk()){f.style.top='';return;}
f.style.top='-10px';
var u=f.getBoundingClientRect().bottom-(window.innerHeight-12);
if(u>0)f.style.top=(-10-u)+'px';
}
s.addEventListener('mouseenter',platzieren);
s.addEventListener('focusin',platzieren);
window.addEventListener('resize',function(){f.style.top='';});
});
});
}
if(document.readyState==='loading')document.addEventListener('DOMContentLoaded',init);else init();
})();
