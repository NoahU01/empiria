/* ============================================================================
   empiria – Tracking
   ----------------------------------------------------------------------------
   Zentraler Helper für alle GA4-Events. Sendet über window.gtag (direkt) mit
   dataLayer-Fallback -> bleibt GTM-kompatibel, falls später ein Tag Manager
   dazukommt (kein Umbau nötig).

   GA4 ist schemalos: jeder hier gesendete Event-Name legt sich beim ersten
   Eintreffen automatisch in GA4 an. Nichts muss vorher in GA4 definiert werden.

   ACHTUNG: Die Event-Namen sind das Vertragsstück Richtung GA4 / Google Ads.
   Einmal festgelegt – nie wieder ändern, sonst brechen Berichte und importierte
   Conversions. Neue Namen: immer klein, mit Unterstrich.

   Consent: Der Google Tag läuft im Consent Mode v2 (Default = alles denied).
   Ohne Einwilligung gehen cookielose Pings raus, mit Einwilligung volle Events.
   Hier muss deshalb NICHT zusätzlich auf Consent geprüft werden.
   ========================================================================== */
(function () {
  "use strict";

  /* ---------- Event-Katalog (die "Vertragsliste") ----------
     kontakt_email_klick    – Klick auf eine mailto-Adresse      [Conversion]
     kontakt_telefon_klick  – Klick auf eine tel-Nummer          [Conversion]
     linkedin_klick         – Klick auf LinkedIn (Badge / Card)
     cta_kontakt            – Klick auf einen "Kontakt"-Button
     cta_mehr_erfahren      – Hero-Button "mehr erfahren"
     cta_loesungen          – "konkrete Lösungen anzeigen"
     popup_<key>            – Leistungs-/Lösungs-Popup geöffnet (Interessen-Signal)
     section_view_<id>      – Sektion wurde gesehen (Absprung-Analyse)
     cookie_einstellungen   – Cookie-Banner erneut geöffnet
  */

  function track(name, params) {
    if (!name) return;
    try {
      if (typeof window.gtag === "function") {
        window.gtag("event", name, params || {});
      } else {
        // Fallback: GTM/dataLayer, falls der Google Tag mal über einen
        // Tag Manager statt direkt eingebunden wird.
        window.dataLayer = window.dataLayer || [];
        window.dataLayer.push(Object.assign({ event: name }, params || {}));
      }
    } catch (e) { /* Tracking darf die Seite nie kaputtmachen */ }
  }
  window.empiriaTrack = track; // für Ad-hoc-Tests in der Konsole

  /* ---------- Kontakt-Klicks (die eigentlichen Conversions) ---------- */
  document.addEventListener("click", function (e) {
    var a = e.target.closest && e.target.closest("a[href]");
    if (!a) return;
    var href = a.getAttribute("href") || "";

    // Unterseiten verlinken Anker als "/index.html#kontakt" statt "#kontakt" ->
    // per Endswith matchen, damit dieselben CTAs seitenübergreifend getrackt werden.
    if (href.indexOf("mailto:") === 0) {
      track("kontakt_email_klick", { link_url: href });
    } else if (href.indexOf("tel:") === 0) {
      track("kontakt_telefon_klick", { link_url: href });
    } else if (href.indexOf("linkedin.com") > -1) {
      track("linkedin_klick", { link_url: href });
    } else if (/#kontakt$/.test(href)) {
      track("cta_kontakt", { link_text: (a.textContent || "").trim() });
    } else if (/#problem$/.test(href) && a.classList.contains("btn")) {
      track("cta_mehr_erfahren");
    } else if (/#leistungen$/.test(href) && a.classList.contains("btn")) {
      track("cta_loesungen");
    }
  }, true);

  /* ---------- Popups: welches Thema zieht? ---------- */
  document.querySelectorAll("[data-modal]").forEach(function (el) {
    el.addEventListener("click", function () {
      track("popup_" + el.getAttribute("data-modal"));
    });
  });

  /* ---------- Cookie-Einstellungen erneut öffnen ---------- */
  document.querySelectorAll("[data-cookie-settings]").forEach(function (el) {
    el.addEventListener("click", function (e) {
      e.preventDefault();
      track("cookie_einstellungen");
      if (window.Cookiebot && typeof window.Cookiebot.renew === "function") {
        window.Cookiebot.renew();
      }
    });
  });

  /* ---------- Sektions-Tracking (Phase 10: "wo springen sie ab?") ----------
     GA4 sieht von Haus aus nur Seiten. Bei einem One-Pager ist das wertlos –
     deshalb feuert jede Sektion einmal pro Pageload ein eigenes Event.
     Die Sektion steckt im NAMEN (nicht als Parameter), damit in GA4 keine
     Custom Dimension angelegt werden muss.

     Zwei Schwellen, weil eine allein nicht reicht: sehr hohe Sektionen füllen
     den Viewport komplett, erreichen aber nie eine hohe intersectionRatio. */
  (function () {
    if (!("IntersectionObserver" in window)) return;
    var sections = document.querySelectorAll("section[id]");
    if (!sections.length) return;

    var seen = {};
    var vh = window.innerHeight || document.documentElement.clientHeight;

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        if (seen[id]) return;

        var ratio = entry.intersectionRatio;
        var fillsViewport = entry.intersectionRect.height / vh > 0.3;
        if (!entry.isIntersecting || (ratio < 0.15 && !fillsViewport)) return;

        seen[id] = true;
        track("section_view_" + id);
        io.unobserve(entry.target);
      });
    }, { threshold: [0.15, 0.5] });

    sections.forEach(function (s) { io.observe(s); });
    window.addEventListener("resize", function () {
      vh = window.innerHeight || document.documentElement.clientHeight;
    }, { passive: true });
  })();
})();
