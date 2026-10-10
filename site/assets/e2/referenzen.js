/* empiria 2.0 · Kundenlogos mobil (Daniel 10.10.2026, Variante A):
   eine ruhige Reihe, die nach rechts ausläuft, darunter „Alle Referenzen ansehen →“ – öffnet ein schwarzes Fenster mit allen Logos. */
(function () {
  "use strict";
  function bauen() {
    var spuren = document.querySelectorAll("main .marquee .marquee-track");
    if (!spuren.length) return;
    var alle = [], gesehen = {};
    spuren[0].querySelectorAll("img").forEach(function (img) {
      if (!gesehen[img.src]) { gesehen[img.src] = 1; alle.push([img.src, img.alt]); }
    });
    if (!alle.length) return;
    var dlg = document.createElement("dialog");
    dlg.className = "e2-ref-dialog";
    dlg.setAttribute("aria-label", "Alle Referenzen");
    dlg.innerHTML = '<button type="button" class="e2-ref-dialog__zu" aria-label="Schließen">×</button>' +
      '<p class="e2-ref-dialog__kicker">Referenzen</p><h3>Für diese Unternehmen arbeiten wir.</h3>' +
      '<div class="e2-ref-dialog__raster">' + alle.map(function (l) {
        return '<span><img src="' + l[0] + '" alt="' + l[1] + '" loading="lazy"></span>';
      }).join("") + "</div>";
    document.body.appendChild(dlg);
    dlg.querySelector(".e2-ref-dialog__zu").addEventListener("click", function () { dlg.close(); });
    dlg.addEventListener("click", function (e) { if (e.target === dlg) dlg.close(); });
    document.querySelectorAll("main .marquee").forEach(function (m) {
      if (m.parentNode.querySelector(".e2-ref-knopf")) return;
      m.classList.add("e2-ref-reihe");
      var k = document.createElement("button");
      k.type = "button"; k.className = "e2-ref-knopf";
      k.innerHTML = "Alle Referenzen ansehen <span aria-hidden=\"true\">→</span>";
      k.addEventListener("click", function () { dlg.showModal(); });
      m.insertAdjacentElement("afterend", k);
      // Knopf bündig mit dem ersten Logo (Seiten ohne Innenabstand um das Logoband)
      function ausrichten() {
        var img = m.querySelector(".marquee-track img"), mb = m.getBoundingClientRect();
        k.style.marginLeft = img ? Math.max(0, Math.round(img.getBoundingClientRect().left - k.parentNode.getBoundingClientRect().left)) + "px" : "";
      }
      ausrichten(); window.addEventListener("resize", ausrichten);
    });
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", bauen); else bauen();
})();
