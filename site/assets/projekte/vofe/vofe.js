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
