/* VVDE – Projektseite. Beide Ansichten („Alle Fakten“, „Infografik“) werden aus
   derselben Quelle window.VVDE_MODELL (in projekte/vvde.html) erzeugt – so können
   sie nicht auseinanderlaufen. Leerer Baustein (inhalt: []) bleibt leer – noch keine Inhalte. */
(function () {
  var M = window.VVDE_MODELL;
  if (!M) return;

  var C = false, D = false, E = false, F = false;   /* Variante C · D (baut auf C auf) · E (Homepage-Gestaltung, nutzt C und D) */
  var FENSTER = {};   /* Inhalte der hellen Fenster, Schlüssel = data-fenster */
  function esc(s) { return String(s).replace(/[&<>"]/g, function (c) { return { "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;" }[c]; }); }
  /* Kanäle als Strichzeichnungen ohne Beschriftung: Homepage · Social Media · One-Pager */
  var KANAL = {
    homepage: { name: "Homepage", svg: '<svg viewBox="0 0 64 48"><rect x="1" y="1" width="62" height="46" rx="5"/><path d="M1 11h62"/><circle cx="7" cy="6" r="1.4" class="f"/><circle cx="12" cy="6" r="1.4" class="f"/><circle cx="17" cy="6" r="1.4" class="f"/><rect x="8" y="17" width="48" height="12" rx="2" class="b"/><path d="M8 35h30M8 40h22"/></svg>' },
    social: { name: "Social Media", svg: '<svg viewBox="0 0 44 48"><rect x="1" y="1" width="42" height="46" rx="5"/><circle cx="9" cy="9" r="3.5" class="b"/><path d="M16 8h18M16 11h11"/><rect x="6" y="17" width="32" height="20" rx="2" class="b"/><path d="M6 42h14"/></svg>' },
    onepager: { name: "One-Pager", svg: '<svg viewBox="0 0 36 48"><rect x="1" y="1" width="34" height="46" rx="3"/><rect x="6" y="6" width="24" height="9" rx="1.5" class="b"/><path d="M6 21h24M6 26h24M6 31h18M6 37h24M6 42h14"/></svg>' }
  };
  /* Perspektivwechsel aus „Strategie in den Alltag überführen“ – übertragen von der Abteilung auf das Unternehmen */
  FENSTER["k:homepage"] = { kicker: "Perspektivwechsel", titel: "Wie sieht die Homepage des Unternehmens aus?", breit: true, html:
    '<div class="vv-pv"><div class="vv-pv__oben"><div>' +
      '<p class="vv-pv__lead">Warum diese Frage? Weil sich hier sofort zeigt, ob sich der Mehrwert des Unternehmens klar erklären lässt. Gelingt das nicht, kann auch niemand im Team aktiv zur Strategie beitragen.</p>' +
      '<div class="e2-pv__schritt"><p class="e2-pv__tag">Gedankenexperiment</p><p>Angenommen, das Unternehmen würde morgen neu gegründet: Was stünde auf seiner Homepage – und würde jeder im Team dasselbe hineinschreiben?</p></div></div>' +
      '<div class="perspektive-browser" role="img" aria-label="Skizze einer leeren Homepage des Unternehmens mit fünf offenen Fragen">' +
        '<div class="pb-bar"><span class="pb-dots" aria-hidden="true"><i></i><i></i><i></i></span><span class="pb-url">www.unternehmen.de<span class="pb-caret" aria-hidden="true"></span></span></div>' +
        '<div class="pb-page"><ol class="pb-rows">' +
          ["Welche Zielgruppe sprechen wir an?", "Welches konkrete Problem lösen wir?", "Welcher Nutzen entsteht daraus?", "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"]
            .map(function (q, i) { return '<li><span class="pb-num">0' + (i + 1) + '</span><span class="pb-q">' + q + '</span><span class="pb-mark">?</span></li>'; }).join("") +
        "</ol></div></div></div>" +
    '<div class="vv-pv__band"><p class="vv-pv__band-tag">Ergebnis</p><p class="vv-pv__band-satz">Jeder im Team versteht, wofür das Unternehmen steht – und das Unternehmen bestimmt selbst, wie es wahrgenommen wird.</p></div></div>' };
  function kanaele(b) {
    if (!(b.kanaele || []).length) return "";
    return '<button type="button" class="vv-auf vv-kanaele" data-fenster="k:homepage" aria-label="Auf allen Kanälen: ' + b.kanaele.map(function (k) { return KANAL[k].name; }).join(", ") + ' – Perspektivwechsel öffnen">' +
      b.kanaele.map(function (k) { return '<span class="vv-kanal">' + KANAL[k].svg + "</span>"; }).join("") + "</button>";
  }

  /* Fokusfeld unter den Teilstrategien: fett und etwas dickere schwarze Linie */
  function hervor(b, s) { return (b.teilHervor || []).indexOf(s) > -1 ? ' class="vv-teile__hervor"' : ""; }
  function liste(xs, cls) { return '<ul class="' + cls + '">' + xs.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>"; }
  /* Ein Thema ausgeschrieben: Titel, Text, Einleitung + Punkte, Hinweis */
  function thema(t) {
    return '<div class="vv-thema"><p class="vv-thema__t">' + esc(t.titel) + "</p>" +
      (t.text ? "<p>" + esc(t.text) + "</p>" : "") +
      (t.einleitung ? '<p class="vv-einleitung">' + esc(t.einleitung) + "</p>" : "") +
      ((t.punkte || []).length ? liste(t.punkte, "vv-punkte") : "") +
      (t.hinweis ? '<p class="vv-hinweis">' + esc(t.hinweis) + "</p>" : "") + "</div>";
  }
  /* Inhalt eines Bausteins: Kernaussage + Themen.
     modus "kurz" (Infografik): nur die Kurzzeile je Thema; sonst alles ausgeschrieben. */
  function text(b, modus) {
    /* kernZeilen: feste Sinnzeilen, damit nichts unglücklich umbricht */
    var h = b.kern ? '<p class="vv-kern">' + (b.kernZeilen ? b.kernZeilen.map(function (z) { return '<span class="vv-kern__z">' + esc(z) + "</span>"; }).join(" ") : esc(b.kern)) + "</p>" : "";
    h += kanaele(b);
    if (b.swot && modus !== "kurz") h += '<p class="vv-swot-titel">SWOT-Analyse</p>' + swot(b.swot) + '<p class="vv-hinweis vv-swot-hinweis">Die vollständige SWOT-Analyse steht in einem separaten Dokument.</p>';
    if (b.zeitplan && modus !== "kurz") h += '<p class="vv-swot-titel">Geschäftsstrategie · drei strategische Stoßrichtungen</p>' + zeitplanBild(b) +
      ((b.teilstrategien || []).length ? '<p class="vv-swot-titel">Daraus abgeleitet · Teilstrategien</p>' + ('<ul class="vv-teile">' + b.teilstrategien.map(function (s) { return "<li" + hervor(b, s) + ">" + esc(s.replace("|", " ")) + "</li>"; }).join("") + "</ul>") : "");
    var th = b.themen || [];
    var kurz = th.filter(function (t) { return t.kurz; }).map(function (t) { return t.kurz; });
    /* Variante D: Steckbrief (Merkmal · Inhalt) statt loser Zeilen */
    var kv = []; th.forEach(function (t) { if (t.kv) kv = kv.concat(t.kv); else if (t.k) kv.push([t.k, t.w]); });
    if (th.length && modus === "kurz" && D && kv.length) h += '<dl class="vv-kv">' + kv.map(function (r) { return "<dt>" + esc(r[0]) + "</dt><dd>" + esc(r[1]) + "</dd>"; }).join("") + "</dl>";
    else if (th.length) h += modus === "kurz" ? (kurz.length ? liste(kurz, "vv-punkte") : "") : th.map(thema).join("");
    var z = b.inhalt || [];
    if (z.length === 1) h += "<p>" + esc(z[0]) + "</p>";
    else if (z.length) h += liste(z, "");
    return h;
  }
  function leer(b) { return !b.kern && !b.swot && !b.zeitplan && !(b.themen || []).length && !(b.inhalt || []).length; }

  /* SWOT-Matrix: 3 × 3, links oben leer. Oben Chancen · Risiken, links Stärken · Schwächen,
     in den Schnittpunkten die vier Strategien. modus "mini" deutet nur an (Linien statt Text). */
  var SWOT_FELDER = [
    ["", ""], ["chancen", "Chancen"], ["risiken", "Risiken"],
    ["staerken", "Stärken"], ["sc", "Stärken-Chancen-Strategie"], ["sr", "Stärken-Risiken-Strategie"],
    ["schwaechen", "Schwächen"], ["wc", "Schwächen-Chancen-Strategie"], ["wr", "Schwächen-Risiken-Strategie"]
  ];
  function swot(s, modus) {
    return '<div class="vv-swot' + (modus === "mini" ? " vv-swot--mini" : "") + '"' + (modus === "mini" ? ' aria-hidden="true"' : "") + ">" +
      SWOT_FELDER.map(function (f, i) {
        if (!f[0]) return '<div class="vv-swot__leer"></div>';
        var kopf = i < 3 || i % 3 === 0, xs = s[f[0]] || [];
        if (modus === "mini") return '<div class="vv-swot__' + (kopf ? "kopf" : "feld") + '">' + (kopf ? esc(f[1]) : "<i></i><i></i><i></i>") + "</div>";
        return '<div class="vv-swot__' + (kopf ? "kopf" : "feld") + '"><p class="vv-swot__t">' + esc(f[1]) + "</p>" + (xs.length ? liste(xs, "vv-punkte") : "") + "</div>";
      }).join("") + "</div>";
  }

  /* ---------------- Variante 1 · Alle Fakten ---------------- */
  function zeile(b, art) {
    if (!art && ((b.themen || []).length || b.swot || b.zeitplan)) art = "voll";
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
  var A = M.ausgangssituation, V = M.vision, St = M.strategie;
  function lab(normal) { return C ? "Mehr erfahren" : normal; }
  function karte(b, cls, extra, frage) {
    return '<div class="vv-g-karte ' + (cls || "") + '">' + (extra || "") + "<small>" + (b.titelGrafik ? b.titelGrafik.map(esc).join("<br>") : esc(b.titel)) + '</small>' + (leer(b) ? "" : (text(b, "kurz") ? '<div class="vv-g-text">' + text(b, "kurz") + "</div>" : "") + swotMini(b) + strategieEbenen(b) + details(b, frage)) +
      (!E && b.frage && cls && cls.indexOf("vv-g-aus") > -1 ? '<p class="vv-g-frage"><span class="vv-sr">Ergebnis: </span>' + (F && b.frageZeilen ? b.frageZeilen.map(function (z) { return '<span class="vv-g-frage__z">' + esc(z) + "</span>"; }).join(" ") : esc(b.frage)) + "</p>" : "") + "</div>";
  }
  /* Helles Fenster: jeder Leitsatz-Schritt und jeder Baustein mit Themen bekommt eines (Register FENSTER) */
  function knopf(key, label, f) { FENSTER[key] = f; return '<button type="button" class="vv-auf" data-fenster="' + esc(key) + '">' + esc(label) + "</button>"; }
  function auf(s) {
    if (!(s.saetze || []).length) return "";
    return knopf("s:" + s.titel, lab(s.titel + " lesen"), { kicker: s.frage, titel: s.fensterTitel || s.titel,
      html: s.saetze.map(function (x) { return '<div class="vv-fenster__block"><p class="vv-fenster__label">' + esc(x.label) + '</p><p class="vv-fenster__satz">' + esc(x.text) + "</p></div>"; }).join("") +
        ((s.werte || []).length ? '<div class="vv-fenster__block"><p class="vv-fenster__label">Unsere Werte</p>' + liste(s.werte, "vv-werte") + "</div>" : "") });
  }
  /* SWOT in der Infografik nur angedeutet – die vollständige Analyse steht in einem separaten Dokument */
  function swotMini(b) { return b.swot ? '<div class="vv-swot-mini">' + swot(b.swot, "mini") + "</div>" : ""; }
  /* Zeitplan der Stoßrichtungen: Streifen laufen nach rechts über die Betrachtungsjahre */
  function zeitplanBild(b, modus) {
    var z = b.zeitplan; if (!z) return "";
    var jahre = []; for (var i = 0; i < z.jahre; i++) jahre.push(z.start + i);
    return '<div class="vv-zeit' + (modus === "mini" ? " vv-zeit--mini" : "") + '" style="--n:' + z.jahre + '">' +
      jahre.map(function (y) { return '<span class="vv-zeit__jahr">' + y + "</span>"; }).join("") +
      z.stossrichtungen.map(function (s) { return '<div class="vv-zeit__streifen"><span>' + esc(s) + "</span></div>"; }).join("") +
      "</div>";
  }
  /* Strategie in zwei Ebenen: Geschäftsstrategie (Zeitstrahl) → abgeleitet die Teilstrategien */
  function strategieEbenen(b) {
    if (!b.zeitplan) return "";
    return '<div class="vv-ebenen"><p class="vv-ebenen__t">Geschäftsstrategie</p>' + zeitplanBild(b, "mini") +
      ((b.teilstrategien || []).length ? '<span class="vv-ebenen__pfeil" aria-hidden="true"></span><p class="vv-ebenen__t">Teilstrategien</p><ul class="vv-teile">' +
        b.teilstrategien.map(function (s) { return "<li" + hervor(b, s) + "><span>" + s.split("|").map(esc).join("<br>") + "</span></li>"; }).join("") + "</ul>" : "") + "</div>";
  }
  function details(b, frage) {
    if (!(b.themen || []).length) return "";
    if (D && !F && !b.themen.some(function (t) { return t.kurz; })) return "";   /* F behält den Verweis: der Detailtext ist sonst nicht erreichbar */   /* D: kein Verweis, wenn das Fenster nur die sichtbare Aussage wiederholt */
    /* visionOben: das Fenster nennt zuerst die übergeordnete Vision (Vorgabe Daniel) */
    var vo = b.visionOben && (V.saetze || [])[0];
    return knopf("b:" + b.titel, lab("Details lesen"), { kicker: frage, titel: b.titel,
      html: (vo ? '<div class="vv-fenster__block"><p class="vv-fenster__label">' + esc(vo.label) + '</p><p class="vv-fenster__satz">' + esc(vo.text) + "</p></div>" : "") +
        (b.kern ? '<div class="vv-fenster__block">' + (vo ? '<p class="vv-fenster__label">Geschäftsmodell</p>' : "") + '<p class="vv-fenster__satz">' + esc(b.kern) + "</p></div>" : "") +
        b.themen.map(function (t) { return '<div class="vv-fenster__block vv-fenster__text">' + thema(t) + "</div>"; }).join("") });
  }
  function kopf(s) { return '<span class="vv-g-mobilkopf"><i>' + s.nr + "</i>" + esc(s.titel) + "</span>" + ((s.saetze || []).length ? '<span class="vv-g-mobilauf">' + auf(s) + "</span>" : ""); }
  /* Ein einziges Raster: Spalten c1 · Lücke · c2 · Lücke · c3 (wie im Modell:
     links „Wie kommen wir dorthin?“ mit 1 und 3, rechts „Wie wollen wir wahrgenommen werden?“ mit 2) */
  function baueGrafik() { return (
    '<div class="vv-g">' +
      '<div class="vv-g-flaeche vv-g-flaeche--oben" aria-hidden="true"></div>' +
      '<div class="vv-g-flaeche vv-g-flaeche--links" aria-hidden="true"></div><div class="vv-g-flaeche vv-g-flaeche--rechts" aria-hidden="true"></div>' +
      '<p class="vv-g-zone__t vv-g-t0">' + esc(sv.frage) + "</p>" +
      (F ? "" : '<div class="vv-g-zufluss"><p>' + (M.zufluss.zeilen || [M.zufluss.titel]).concat([M.zufluss.frage]).map(function (z) { return "<span>" + esc(z) + "</span>"; }).join("") + '</p><span class="vv-g-pfeil" aria-hidden="true"></span></div>') +
      (C && !E ? '<p class="vv-g-svtitel">' + esc(sv.titel) + "</p>" : "") +
      '<div class="vv-g-karte vv-g-sv">' + (E ? '<p class="vv-g-svname">' + esc(sv.titel) + "</p>" : C ? "" : "<small>" + esc(sv.titel) + "</small>") + '<div class="vv-g-text">' +
        (D && (sv.saetze || []).length ? '<p class="vv-g-svsatz">' + esc(sv.saetze[0].text) + "</p>" : "") +
        ((sv.werte || []).length ? '<ul class="vv-g-werte">' + sv.werte.map(function (x) { return "<li>" + esc(x) + "</li>"; }).join("") + "</ul>" : "") + (D ? "" : auf(sv)) + "</div></div>" +
      '<span class="vv-g-abwaerts" aria-hidden="true"></span>' +
      '<p class="vv-g-zone__t vv-g-t1">' + esc(A.zone) + '</p><p class="vv-g-zone__t vv-g-t2">' + esc(V.zone) + "</p>" +
      '<span class="vv-g-linie vv-g-linie--a" aria-hidden="true"></span><span class="vv-g-linie vv-g-linie--b" aria-hidden="true"><em>Mission</em></span>' +
      [["k1", A], ["k3", St], ["k2", V]].map(function (x) { return '<div class="vv-g-kreis vv-g-' + x[0] + '"><i aria-hidden="true">' + x[1].nr + "</i><b>" + esc(x[1].titel) + "</b>" + auf(x[1]) + "</div>"; }).join("") +
      karte(A.bausteine[0], "vv-g-a1", kopf(A), A.frage) +
      karte(St.bausteine[0], "vv-g-a3", kopf(St), St.frage) +
      karte(V.bausteine[0], "vv-g-a2", kopf(V), V.frage) +
      '<div class="vv-g-klammer" aria-hidden="true"><em>Detaillierung der Strategie</em></div><div class="vv-g-strich" aria-hidden="true"></div>' +
      karte(St.folgt[0], "vv-g-aus vv-g-b1") +
      karte(St.folgt[1], "vv-g-aus vv-g-b2") +
      karte(V.folgt[0], "vv-g-aus vv-g-b3") +
    "</div>" +
    /* E: die drei Ergebnisfragen als schwarzes Band am Ende – gelbe Dreiecke wie im Original-Modell */
    (E ? '<div class="vv-g-erg"><p class="vv-g-erg__tag">Ergebnis</p>' +
      [["b1", St.folgt[0]], ["b2", St.folgt[1]], ["b3", V.folgt[0]]].map(function (x) {
        return '<p class="vv-g-erg__f vv-g-erg__f--' + x[0] + '"><small>' + esc(x[1].titel) + "</small>" + esc(x[1].frage) + "</p>"; }).join("") + "</div>" : "")); }
  document.querySelectorAll(".vv-grafik").forEach(function (el) {
    C = !!el.closest(".vv-inhalt--c"); E = !!el.closest(".vv-inhalt--e"); F = !!el.closest(".vv-inhalt--f"); D = E || F || !!el.closest(".vv-inhalt--d");
    el.innerHTML = baueGrafik();
  });
  C = false; D = false; E = false; F = false;

  /* ---------------- Helles Fenster (Inhalte aus FENSTER) ---------------- */
  var fenster = document.createElement("dialog");
  fenster.className = "vv-fenster";
  fenster.innerHTML = '<button type="button" class="vv-fenster__zu" aria-label="Schließen">&times;</button><p class="vv-fenster__kicker"></p><h3 class="vv-fenster__titel"></h3><div class="vv-fenster__inhalt"></div>';
  document.body.appendChild(fenster);
  document.addEventListener("click", function (e) {
    var k = e.target.closest(".vv-auf");
    if (k) {
      var f = FENSTER[k.dataset.fenster];
      fenster.querySelector(".vv-fenster__kicker").textContent = f.kicker;
      fenster.querySelector(".vv-fenster__titel").textContent = f.titel;
      fenster.querySelector(".vv-fenster__inhalt").innerHTML = f.html;
      fenster.classList.toggle("vv-fenster--breit", !!f.breit);
      fenster.showModal();
      fenster.scrollTop = 0;
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
