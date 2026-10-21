/* Patenwagen (Entwurf): Filter auf der Festzug-Seite und Stand der Patenschaften. */
(function () {
  "use strict";
  var zug = document.querySelector("[data-zug]"); if (!zug) return;
  var wagen = [].slice.call(zug.querySelectorAll(".wagen"));
  var pate = wagen.filter(function (w) { return w.classList.contains("wagen--pate"); }).length;
  var s = document.querySelector("[data-stand]"); if (s) s.textContent = pate + " von " + wagen.length + " Wagen haben schon einen Paten";
  var b = document.querySelector("[data-balken]"); if (b) b.style.width = Math.round(pate / wagen.length * 100) + "%";
  document.querySelectorAll("[data-f]").forEach(function (k) {
    k.addEventListener("click", function () {
      var f = k.getAttribute("data-f");
      document.querySelectorAll("[data-f]").forEach(function (x) { x.setAttribute("aria-pressed", String(x === k)); });
      wagen.forEach(function (w) { var p = w.classList.contains("wagen--pate"); w.hidden = f === "frei" ? p : f === "pate" ? !p : false; });
    });
  });
})();
/* Vorseite: Seitenvorschau scrollt beim Darüberfahren einmal durch. */
document.querySelectorAll(".vs-seite img").forEach(function (img) {
  function setze() { var f = img.parentNode, weg = Math.max(0, img.offsetHeight - f.offsetHeight); f.style.setProperty("--weg", weg + "px"); f.style.setProperty("--dauer", Math.max(4, weg / 260) + "s"); }
  if (img.complete) setze(); img.addEventListener("load", setze); window.addEventListener("resize", setze);
});
/* Vorseite: Kopfbereich zwischen Variante 1 und 2 umschalten (nur Entwurf). */
(function () {
  var knoepfe = document.querySelectorAll("[data-kopf]"); if (!knoepfe.length) return;
  function zeige(v) {
    knoepfe.forEach(function (k) { k.setAttribute("aria-pressed", String(k.getAttribute("data-kopf") === v)); });
    document.querySelectorAll(".vs-v").forEach(function (el) { el.hidden = !el.classList.contains("vs-v--" + v); });
    try { localStorage.setItem("vofe-kopf", v); } catch (e) {}
  }
  knoepfe.forEach(function (k) { k.addEventListener("click", function () { zeige(k.getAttribute("data-kopf")); }); });
  var v = null; try { v = localStorage.getItem("vofe-kopf"); } catch (e) {}
  if (v === "1" || v === "2") zeige(v);
})();
