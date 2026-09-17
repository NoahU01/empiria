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
     popup_<key>            – Popup geöffnet (Interessen-Signal); key aus data-modal,
                              data-modal-target (mesModalLandingpage -> mes_landingpage)
                              oder fest: pdf_vorschau, zeitplan, struktur, angebot_formular
     section_view_<id>      – Sektion wurde gesehen (Reichweite / Absprung-Analyse)
     section_time_<id>      – Sekunden im Viewport, als `value` (Verweildauer je Sektion)
     cookie_einstellungen   – Cookie-Banner erneut geöffnet

     --- seit 18.09.2026 (Multi-Page-Ausbau) ---
     cta_anfrage            – Klick auf "… anfragen"/"Jetzt beraten lassen" -> /kontakt
                              (Param cta_text)                 [weiche Conversion, kein Schlüsselereignis]
     cta_hero               – Hero-Button "… kennenlernen" (Scroll-Anker, Param cta_text)
     formular_sprint_angebot – Sprint-Landingpage: Angebotsformular abgeschickt  [Conversion]
     potentialcheck_submit  – Paid Ads: Potentialcheck abgeschickt (paid-ads.html) [Conversion]
     download_<datei>       – PDF-Download, datei = Dateiname ohne Präfix/Endung
                              (empiria-workshops.pdf -> download_workshops)
     extern_klick           – Klick auf externe Domain (Param link_url)
     akkordeon_oeffnen      – Akkordeon/FAQ aufgeklappt (Param frage -> Custom Dimension "frage")
     kanalcheck_*, paid_ads_mockup_* – siehe paid-ads.html
  */

  function slug(str) {
    return String(str || "").toLowerCase()
      .replace(/ä/g, "ae").replace(/ö/g, "oe").replace(/ü/g, "ue").replace(/ß/g, "ss")
      .replace(/[^a-z0-9]+/g, "_").replace(/^_+|_+$/g, "");
  }
  // mesModalLandingpage -> mes_landingpage, jobProfileModal -> job_profile
  function modalKey(id) {
    return slug(String(id || "").replace(/Modal|Overlay/g, "").replace(/([a-z0-9])([A-Z])/g, "$1_$2"));
  }

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
    } else if (/\/kontakt(\.html)?(\?.*)?$/.test(href)) {
      // "Workshop anfragen", "Jetzt beraten lassen" ... -> Kontaktseite
      track("cta_anfrage", { cta_text: (a.textContent || "").trim().slice(0, 60) });
    } else if (/\.pdf(\?|$)/i.test(href) || a.hasAttribute("download")) {
      var datei = href.split("?")[0].split("/").pop().replace(/\.pdf$/i, "")
        .replace(/^(empiria[-_]|EMP_\d+_)/i, "");
      track("download_" + slug(datei), { link_url: href });
    } else if (/^https?:\/\//.test(href) && !/(^|\.)empiria\.de(\/|$)/.test(href.replace(/^https?:\/\//, ""))) {
      track("extern_klick", { link_url: href });
    } else if (/^#|\/#/.test(href) && a.classList.contains("btn") && a.closest(".produkt-hero, .hero, .leistung-hero")) {
      // "KI zum Anfassen kennenlernen" & Co.: Scroll-Anker im Hero
      track("cta_hero", { cta_text: (a.textContent || "").trim().slice(0, 60) });
    }
  }, true);

  /* ---------- Popups: welches Thema zieht? ----------
     Drei Auslöser-Arten, ein Event: data-modal (Startseite), data-modal-target
     (generische Vorschau-Modals) und die fest verdrahteten Öffner-Klassen. */
  document.addEventListener("click", function (e) {
    var t = e.target.closest && e.target.closest("[data-modal], [data-modal-target], .js-pdf-open, .js-onboarding-open, .js-form-open, .sprint-structure-card, .sprint-structure-cta");
    if (!t) return;
    var key = t.getAttribute("data-modal")
      || (t.getAttribute("data-modal-target") && modalKey(t.getAttribute("data-modal-target")))
      || (t.classList.contains("js-pdf-open") && "pdf_vorschau")
      || (t.classList.contains("js-onboarding-open") && "zeitplan")
      || (t.classList.contains("js-form-open") && "angebot_formular")
      || "struktur";
    track("popup_" + key);
  }, true);

  /* ---------- Sprint Landingpage: Angebotsformular abgeschickt ---------- */
  document.addEventListener("submit", function (e) {
    var f = e.target;
    if (f && f.classList && f.classList.contains("contact-form")) {
      track("formular_sprint_angebot");
    }
  }, true);

  /* ---------- Akkordeons: welche Frage wird aufgeklappt? ---------- */
  document.addEventListener("toggle", function (e) {
    var d = e.target;
    if (!d || d.tagName !== "DETAILS" || !d.open) return;
    var sum = d.querySelector("summary");
    track("akkordeon_oeffnen", { frage: (sum ? sum.textContent : "").replace(/\s+/g, " ").trim().slice(0, 100) });
  }, true);

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

  /* ---------- Sektions-Tracking: Reichweite + Verweildauer ----------
     GA4 sieht von Haus aus nur Seiten. Bei einem One-Pager ist das wertlos –
     deshalb misst jede Sektion zwei Dinge (identisch zu admemory.de,
     components/ui/section-tracker.tsx):

     1. section_view_<id>  – einmal pro Pageload, sobald die Sektion sichtbar
        war. Das ist die Reichweite: bis wohin wird gescrollt.
     2. section_time_<id>  – die im Viewport verbrachte Zeit in Sekunden, als
        `value` mitgegeben. GA4 summiert das zur Metrik eventValue.
        Ø Verweildauer = eventValue / Anzahl section_view_<id> (NICHT durch
        eventCount teilen: Zeit-Events können pro Besuch mehrfach feuern,
        section_view genau einmal).

     Die Sektion steckt im NAMEN (nicht als Parameter), damit in GA4 keine
     Custom Dimension angelegt werden muss.

     Zwei Sichtbarkeits-Schwellen, weil eine allein nicht reicht: sehr hohe
     Sektionen füllen den Viewport komplett, erreichen aber nie eine hohe
     intersectionRatio.

     Die Zeit läuft nur, solange der Tab sichtbar ist (visibilitychange) und
     wird beim Verlassen (pagehide) bzw. Tab-Wechsel per Beacon gesendet. */
  (function () {
    if (!("IntersectionObserver" in window)) return;
    var sections = document.querySelectorAll("section[id]");
    if (!sections.length) return;

    var VISIBLE_RATIO = 0.15;
    var VIEWPORT_FILL = 0.3;   // Anteil des Viewports, den eine hohe Sektion füllen muss
    var MAX_SECONDS = 600;     // Deckel gegen Tabs, die stundenlang offen liegen
    var MIN_SECONDS = 1;       // unter einer Sekunde ist Durchscrollen, keine Aufmerksamkeit

    var seen = {};      // id -> true, section_view schon gesendet
    var visible = {};   // id -> true, gerade im Viewport
    var since = {};     // id -> performance.now() beim Sichtbarwerden
    var totals = {};    // id -> aufsummierte Millisekunden, noch nicht gesendet
    var vh = window.innerHeight || document.documentElement.clientHeight;

    function now() { return performance.now(); }

    // Laufende Timer stoppen und aufaddieren (Tab-Wechsel, Seite verlassen).
    function pauseAll() {
      for (var id in since) {
        totals[id] = (totals[id] || 0) + (now() - since[id]);
      }
      since = {};
    }
    // Timer für alles wieder starten, was gerade sichtbar ist. Nur wenn der
    // Tab vorn ist: send() ruft das auch beim Wechsel in den Hintergrund auf,
    // und ohne diese Prüfung liefe die Uhr dort weiter und zählte beim nächsten
    // Vordergrund die gesamte Hintergrundzeit mit.
    function resumeAll() {
      if (document.visibilityState !== 'visible') return;
      for (var id in visible) {
        if (!(id in since)) since[id] = now();
      }
    }

    function send() {
      pauseAll();
      for (var id in totals) {
        // Erst gegen die Rohzeit prüfen: Math.round machte aus 0,6 s eine 1 s
        // und ließ Durchscrollen als Verweildauer durchgehen.
        if (totals[id] < MIN_SECONDS * 1000) continue;
        var seconds = Math.round(totals[id] / 1000);
        track("section_time_" + id, {
          value: Math.min(seconds, MAX_SECONDS),
          transport_type: "beacon"
        });
      }
      totals = {};
      // Sichtbares läuft weiter, falls der Nutzer zurückkommt.
      resumeAll();
    }

    var io = new IntersectionObserver(function (entries) {
      entries.forEach(function (entry) {
        var id = entry.target.id;
        if (!id) return;

        var isVisible = entry.isIntersecting &&
          (entry.intersectionRatio >= VISIBLE_RATIO ||
           entry.intersectionRect.height / vh > VIEWPORT_FILL);

        if (isVisible) {
          if (!seen[id]) {
            seen[id] = true;
            track("section_view_" + id);
          }
          visible[id] = true;
          if (document.visibilityState === "visible" && !(id in since)) since[id] = now();
        } else {
          delete visible[id];
          if (id in since) {
            totals[id] = (totals[id] || 0) + (now() - since[id]);
            delete since[id];
          }
        }
      });
    }, { threshold: [0, VISIBLE_RATIO, 0.5] });

    sections.forEach(function (s) { io.observe(s); });

    document.addEventListener("visibilitychange", function () {
      if (document.visibilityState === "hidden") send();
      else resumeAll();
    });
    window.addEventListener("pagehide", send);
    window.addEventListener("resize", function () {
      vh = window.innerHeight || document.documentElement.clientHeight;
    }, { passive: true });
  })();
})();
