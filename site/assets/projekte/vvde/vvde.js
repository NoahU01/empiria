/* VVDE – Projektseite. Beide Ansichten („Alle Fakten“, „Infografik“) werden aus
   derselben Quelle window.VVDE_MODELL (in projekte/vvde.html) erzeugt – so können
   sie nicht auseinanderlaufen. Leerer Baustein (inhalt: []) bleibt leer – noch keine Inhalte. */
(function () {
  var M = window.VVDE_MODELL;
  if (!M) return;

  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  /* Inhalt eines Bausteins: Kernaussage, Einleitung + Punkte, weitere Sätze.
     modus "kurz" (Infografik) nimmt die Kurzfassung der Punkte, sonst die volle Formulierung. */
  function text(b, modus) {
    var h = "";
    if (b.kern) h += '<p class="vv-kern">' + esc(b.kern) + "</p>";
    if (b.punkte && b.punkte.length) {
      if (b.einleitung && modus !== "kurz") h += '<p class="vv-einleitung">' + esc(b.einleitung) + "</p>";
      h += '<ul class="vv-punkte">' + b.punkte.map(function (x) { return "<li>" + esc(modus === "kurz" ? x.kurz : x.lang) + "</li>"; }).join("") + "</ul>";
    }
    var z = b.inhalt || [];
    if (z.length === 1) h += "<p>" + esc(z[0]) + "</p>";
    else if (z.length) h += "<ul>" + z.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>";
    return h;
  }
  function leer(b) { return !b.kern && !(b.punkte || []).length && !(b.inhalt || []).length; }

  /* ---------------- Variante 1 · Alle Fakten ---------------- */
  function zeile(b, art) {
    return '<div class="vv-f-zeile' + (art ? " vv-f-zeile--" + art : "") + '"><div class="vv-f-zeile__kopf"><b>' + esc(b.titel) + "</b>" +
      (b.frage ? "<span>" + esc(b.frage) + "</span>" : "") + '</div><div class="vv-f-zeile__text">' + text(b) + "</div></div>";
  }
  /* Kopf eines Blocks: hängende Ziffer links neben dem Titel (Basis ohne Ziffer, wie im Modell) */
  function block(nr, frage, titel, zeilen) {
    return '<section class="vv-f-block"><div class="vv-f-marke">' + (nr ? '<span class="vv-f-zahl" aria-hidden="true">' + nr + "</span>" : "") +
      '<p class="vv-f-frage">' + esc(frage) + "</p><h3>" + (nr ? '<span class="vv-sr">Schritt ' + nr + ": </span>" : "") + esc(titel) + '</h3></div><div class="vv-f-inhalt">' + zeilen + "</div></section>";
  }
  /* Leitsatz: kleine Überschrift + Aussage mit Strich (Selbstverständnis, Vision) */
  function aussage(label, satz) {
    return '<div class="vv-f-aussage"><p class="vv-f-mini">' + esc(label) + '</p><p class="vv-f-aussage__satz">' + esc(satz) + "</p></div>";
  }
  function schritt(s, folgtTitel) {
    return block(s.nr, s.frage, s.titel,
      (s.saetze || []).map(function (x) { return aussage(x.label, x.text); }).join("") +
      s.bausteine.map(function (b) { return zeile(b); }).join("") +
      ((s.folgt || []).length ? '<p class="vv-f-mini">' + esc(folgtTitel) + "</p>" + s.folgt.map(function (b) { return zeile(b); }).join("") : ""));
  }
  var sv = M.selbstverstaendnis;
  var fakten =
    block(0, "Basis · " + sv.frage, sv.titel,
      (sv.saetze || []).map(function (x) { return aussage(x.label, x.text); }).join("") +
      ((sv.werte || []).length ? '<p class="vv-f-mini">Unsere Werte</p><ul class="vv-werte">' + sv.werte.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" : "") +
      '<p class="vv-f-mini">Was einfließt</p>' + zeile(M.zufluss)) +
    schritt(M.ausgangssituation) +
    schritt(M.vision, "Daraus folgt") +
    schritt(M.strategie, "Detaillierung der Strategie");
  document.querySelectorAll(".vv-fakten").forEach(function (el) { el.innerHTML = fakten; });

  /* ---------------- Variante 2 · Infografik ---------------- */
  function karte(b, cls, extra) {
    return '<div class="vv-g-karte ' + (cls || "") + '">' + (extra || "") + "<small>" + esc(b.titel) + '</small>' + (leer(b) ? "" : '<div class="vv-g-text">' + text(b, "kurz") + "</div>") +
      (b.frage && cls && cls.indexOf("vv-g-aus") > -1 ? '<p class="vv-g-frage"><span class="vv-sr">Ergebnis: </span>' + esc(b.frage) + "</p>" : "") + "</div>";
  }
  function auf(s) { return (s.saetze || []).length ? '<button type="button" class="vv-auf" data-satz="' + esc(s.titel) + '">' + esc(s.titel) + " lesen</button>" : ""; }
  function kopf(s) { return '<span class="vv-g-mobilkopf"><i>' + s.nr + "</i>" + esc(s.titel) + "</span>" + ((s.saetze || []).length ? '<span class="vv-g-mobilauf">' + auf(s) + "</span>" : ""); }
  var A = M.ausgangssituation, V = M.vision, St = M.strategie;
  /* Ein einziges Raster: Spalten c1 · Lücke · c2 · Lücke · c3 (wie im Modell:
     links „Wie kommen wir dorthin?“ mit 1 und 3, rechts „Wie wollen wir wahrgenommen werden?“ mit 2) */
  var grafik =
    '<div class="vv-g">' +
      '<div class="vv-g-flaeche vv-g-flaeche--oben" aria-hidden="true"></div>' +
      '<div class="vv-g-flaeche vv-g-flaeche--links" aria-hidden="true"></div><div class="vv-g-flaeche vv-g-flaeche--rechts" aria-hidden="true"></div>' +
      '<p class="vv-g-zone__t vv-g-t0">' + esc(sv.frage) + "</p>" +
      '<div class="vv-g-zufluss"><p><span>' + esc(M.zufluss.titel) + "</span><span>" + esc(M.zufluss.frage) + '</span></p><span class="vv-g-pfeil" aria-hidden="true"></span></div>' +
      '<div class="vv-g-karte vv-g-sv"><small>' + esc(sv.titel) + '</small><div class="vv-g-text">' +
        ((sv.werte || []).length ? '<ul class="vv-g-werte">' + sv.werte.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" : "") + auf(sv) + "</div></div>" +
      '<span class="vv-g-abwaerts" aria-hidden="true"></span>' +
      '<p class="vv-g-zone__t vv-g-t1">' + esc(A.zone) + '</p><p class="vv-g-zone__t vv-g-t2">' + esc(V.zone) + "</p>" +
      '<span class="vv-g-linie vv-g-linie--a" aria-hidden="true"></span><span class="vv-g-linie vv-g-linie--b" aria-hidden="true"><em>Mission</em></span>' +
      [["k1", A], ["k3", St], ["k2", V]].map(function (x) { return '<div class="vv-g-kreis vv-g-' + x[0] + '"><i aria-hidden="true">' + x[1].nr + "</i><b>" + esc(x[1].titel) + "</b>" + auf(x[1]) + "</div>"; }).join("") +
      karte(A.bausteine[0], "vv-g-a1", kopf(A)) +
      karte(St.bausteine[0], "vv-g-a3", kopf(St)) +
      karte(V.bausteine[0], "vv-g-a2", kopf(V)) +
      '<div class="vv-g-klammer" aria-hidden="true"><em>Detaillierung der Strategie</em></div><div class="vv-g-strich" aria-hidden="true"></div>' +
      karte(St.folgt[0], "vv-g-aus vv-g-b1") +
      karte(St.folgt[1], "vv-g-aus vv-g-b2") +
      karte(V.folgt[0], "vv-g-aus vv-g-b3") +
    "</div>";
  document.querySelectorAll(".vv-grafik").forEach(function (el) { el.innerHTML = grafik; });

  /* ---------------- Helles Fenster für Leitsätze (z. B. Vision) ---------------- */
  var fenster = document.createElement("dialog");
  fenster.className = "vv-fenster";
  fenster.innerHTML = '<button type="button" class="vv-fenster__zu" aria-label="Schließen">&times;</button><p class="vv-fenster__kicker"></p><h3 class="vv-fenster__titel"></h3><div class="vv-fenster__inhalt"></div>';
  document.body.appendChild(fenster);
  document.addEventListener("click", function (e) {
    var k = e.target.closest(".vv-auf");
    if (k) {
      var s = [sv, A, V, St].filter(function (x) { return x.titel === k.dataset.satz; })[0];
      fenster.querySelector(".vv-fenster__kicker").textContent = s.frage;
      fenster.querySelector(".vv-fenster__titel").textContent = s.fensterTitel || s.titel;
      fenster.querySelector(".vv-fenster__inhalt").innerHTML = s.saetze.map(function (x) {
        return '<div class="vv-fenster__block"><p class="vv-fenster__label">' + esc(x.label) + '</p><p class="vv-fenster__satz">' + esc(x.text) + "</p></div>"; }).join("") +
        ((s.werte || []).length ? '<div class="vv-fenster__block"><p class="vv-fenster__label">Unsere Werte</p><ul class="vv-werte">' + s.werte.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul></div>" : "");
      fenster.showModal();
      return;
    }
    if (e.target.closest(".vv-fenster__zu") || e.target === fenster) fenster.close();
  });

  /* ---------------- Umschalter – je Sektion eigenständig ---------------- */
  document.querySelectorAll(".vv-inhalt").forEach(function (sek) {
    var knoepfe = sek.querySelectorAll(".sm-schalter button");
    function zeige(v) {
      sek.querySelectorAll(".sm-v").forEach(function (el) { el.hidden = el.dataset.variante !== v; });
      knoepfe.forEach(function (k) { k.setAttribute("aria-pressed", k.dataset.v === v ? "true" : "false"); });
    }
    knoepfe.forEach(function (k) { k.addEventListener("click", function () { zeige(k.dataset.v); }); });
    if (location.hash === "#infografik") zeige("2");
  });
})();
