(function () {
  "use strict";

  /* ---------- Marquee (client logos) ---------- */
  // Desktop marquee order = Freigabe-Ordner (01–12). Mobile grid re-orders via CSS.
  var logos = [
    ["logo-01-sv.svg", "SV SparkassenVersicherung"],
    ["logo-02-vgh.svg", "VGH"],
    ["logo-03-devk-re.svg", "DEVK RE"],
    ["logo-04-vh.svg", "Vereinigte Hagelversicherung"],
    ["logo-05-svs.svg", "SV SparkassenVersicherung Sachsen"],
    ["logo-06-gartenbau.svg", "Gartenbau-Versicherung"],
    ["logo-07-sv-bav.svg", "SV bAV Consulting GmbH"],
    ["logo-08-devk-am.svg", "DEVK AM"],
    ["logo-09-oerag.svg", "ÖRAG Rechtsschutz"],
    ["logo-10-svp.svg", "SV Pensionsfonds"],
    ["logo-11-cominia.svg", "cominia"],
    ["logo-12-zeitsprung.svg", "zeitsprung"]
  ];
  var track = document.getElementById("marqueeTrack");
  if (track) {
    var html = "";
    for (var pass = 0; pass < 2; pass++) {
      for (var i = 0; i < logos.length; i++) {
        // eager load: marquee width must be correct up-front or the -50% loop seams
        html += '<img src="assets/logos/' + logos[i][0] + '" alt="' + logos[i][1] +
          '" decoding="async">';
      }
    }
    track.innerHTML = html;
  }

  /* ---------- Header scroll state ---------- */
  var header = document.querySelector(".site-header");
  function onScroll() {
    if (window.scrollY > 12) header.classList.add("scrolled");
    else header.classList.remove("scrolled");
  }
  window.addEventListener("scroll", onScroll, { passive: true });
  onScroll();

  /* ---------- Mobile menu ---------- */
  var toggle = document.getElementById("navToggle");
  var menu = document.getElementById("mobileMenu");
  if (toggle && menu) {
    toggle.addEventListener("click", function () {
      var open = menu.classList.toggle("open");
      toggle.setAttribute("aria-expanded", open ? "true" : "false");
    });
    menu.querySelectorAll("a").forEach(function (a) {
      a.addEventListener("click", function () {
        menu.classList.remove("open");
        toggle.setAttribute("aria-expanded", "false");
      });
    });
  }

  /* ---------- Modals (Pop-up texts) ---------- */
  var P = function () { return Array.prototype.slice.call(arguments); };
  var MODALS = {
    loesung: {
      icon: "ic-forward",
      title: "Wir übersetzen Deine Strategie in Wirkung",
      body: P(
        "Wir begleiten Dich bei der Umsetzung Deiner Fokusthemen und bei der strategischen Kommunikation nach innen und außen. Denn dort liegen oft die entscheidenden Hebel, ob ein Thema wirklich vorankommt.",
        "@Das Ergebnis:",
        "Du steuerst Deine Themen, statt auf Überraschungen zu reagieren. Die Zusammenhänge sind klar. Deine Themen kommen voran.",
        "Und irgendwann merkst Du, dass Dich auch die anderen längst als jemanden wahrnehmen, der seinen Verantwortungsbereich im Griff hat."
      )
    },
    strategie: {
      icon: "ic-forward",
      title: "Strategie in den Alltag überführen",
      body: P(
        "Wir erarbeiten mit dir das Selbstverständnis deines Verantwortungsbereichs, das Zielbild für euren Alltag von morgen – und den Weg dorthin, ausgehend von eurer heutigen Situation.",
        "Im Zentrum stehen drei Fragen: Wofür stehst du? Wie kommst du dorthin? Und wie setzt du das im Alltag um?",
        "Dafür stellen wir die richtigen Fragen, wechseln bewusst die Perspektive und skizzieren gemeinsam mit dir, bis aus vagen Gedanken ein klares Bild wird – oft eines, das du selbst so noch nicht in Worte fassen konntest.",
        "Im laufenden Sparring bleibt dein Thema aktiv im Kopf. Diesen Blick von außen bekommst du weder im eigenen Team noch bei den Führungskräften über dir.",
        "@Das Ergebnis:",
        "Du hast deinen Bereich wirklich im Griff. Die Zusammenhänge sind klar, Entscheidungen sind belastbar.",
        "Du gibst Orientierung, auch bei neuen Themen – und dein Team weiß, wohin die Reise geht."
      )
    },
    komplex: {
      icon: "ic-kreuz",
      title: "Komplexe Themen strukturieren & kommunizieren",
      body: P(
        "Es geht um die Momente, in denen es zählt: Aufsichtsrats- und Vorstandssitzungen, Projektlenkungsausschüsse, Vertriebstagungen, Betriebsratssitzungen – aber auch Termine mit Kooperationspartnern, Rückversicherern oder bei wichtigen Kundenpitches.",
        "Überall dort, wo du Entscheider von deinem Thema überzeugen musst.",
        "Wir strukturieren dein Thema so, dass es in der Welt deines Gesprächspartners ankommt – die zentrale Frage lautet immer: „Welche Bedeutung hat dein Thema für die Zielgruppe?“",
        "Dazu kommt taktisches Vorgehen vor, während und nach dem Termin, professionelle Unterlagen weit über die klassische PowerPoint hinaus, und eine gezielte Vorbereitung auf Basis unserer jahrelangen Erfahrung mit genau solchen Situationen.",
        "@Das Ergebnis:",
        "Du gehst bestens vorbereitet in entscheidende Termine. Deine Themen kommen dort an, wo sie ankommen müssen.",
        "Und die richtigen Entscheidungen werden getroffen – deshalb werden wir für wichtige Themen immer wieder gebucht."
      )
    },
    innovation: {
      icon: "ic-kreis",
      title: "Innovation & Geschäftsmodell neu denken",
      body: P(
        "Wer sein Geschäftsmodell wirklich hinterfragt, stößt schnell an eine Grenze: Vieles gilt als gegeben, nur weil es schon immer so war – dabei ist es oft längst nicht mehr in Stein gemeißelt.",
        "Genau hier gehen wir mit dir grundlegend ran, sei es für das gesamte Unternehmen oder für einzelne Bereiche.",
        "Das gilt für die Zukunft eures Geschäftsmodells genauso wie für konkrete Fragen zu Kooperationen, Fusionen, Beteiligungen oder neuen Zusatzservices.",
        "Wir bringen dafür eigene Methoden und Frameworks mit und helfen dir, dich von genau diesen alten Denkmustern zu lösen.",
        "Ein bewährter Ansatz dabei: Wir denken mit dir so, als würdet ihr euer Thema morgen als eigenes Unternehmen neu gründen – ganz ohne Altlasten.",
        "@Das Ergebnis:",
        "Ihr versteht, worauf es in eurem Geschäftsmodell wirklich ankommt – heute und in Zukunft. Ihr trefft Entscheidungen zu Innovation, Kooperationen oder Investitionen mit echter Substanz dahinter.",
        "Und ihr traut euch, auch mal ganz neu zu denken."
      )
    },
    teams: {
      icon: "ic-raute",
      title: "Teams befähigen, professionell zu kommunizieren",
      body: P(
        "Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft trotzdem ins Leere.",
        "Oder es steht selbst vor dem Aufsichtsrat, im Projektlenkungsausschuss oder beim Kunden, und hinterher denkst du: Das hätte besser laufen können. Die Story trägt nicht, die Unterlagen überzeugen nicht, und im Raum fehlt die Ruhe, auf Fragen und Gegenwind gut zu reagieren.",
        "Wir bringen deinem Team bei, wie das geht – und lassen es danach nicht allein.",
        "Wir arbeiten an echten Themen aus eurem Alltag: dem nächsten Kundenpitch, dem nächsten Gespräch mit dem Rückversicherer, der nächsten wichtigen Runde im eigenen Haus.",
        "Vor dem Termin, beim letzten Schliff, danach beim Nachdenken, was gut lief und was nicht – genau dann sind wir da. So baut sich etwas auf, das ein einzelner Workshop nie schafft.",
        "@Das Ergebnis:",
        "Dein Team bereitet Themen so auf, dass sie überzeugen, und tritt sicher auf, wenn es zählt.",
        "Du bekommst Themen, mit denen du wirklich arbeiten kannst. Und dein Team hat die Sicherheit, die es dafür braucht."
      )
    }
  };

  var overlay = document.getElementById("modalOverlay");
  var mTitle = document.getElementById("modalTitle");
  var mBody = document.getElementById("modalBody");
  var mIcon = document.getElementById("modalIcon");
  var lastFocus = null;

  function openModal(key) {
    var d = MODALS[key];
    if (!d) return;
    mTitle.textContent = d.title;
    mIcon.innerHTML = '<use href="#' + d.icon + '"/>';
    var frag = "";
    d.body.forEach(function (para) {
      if (para.charAt(0) === "@") {
        frag += '<p class="result-label">' + para.slice(1) + "</p>";
      } else {
        frag += "<p>" + para + "</p>";
      }
    });
    mBody.innerHTML = frag;
    lastFocus = document.activeElement;
    overlay.classList.add("open");
    document.body.style.overflow = "hidden";
    document.getElementById("modalClose").focus();
  }
  function closeModal() {
    overlay.classList.remove("open");
    document.body.style.overflow = "";
    if (lastFocus) lastFocus.focus();
  }

  document.querySelectorAll("[data-modal]").forEach(function (el) {
    el.addEventListener("click", function () { openModal(el.getAttribute("data-modal")); });
  });
  document.getElementById("modalClose").addEventListener("click", closeModal);
  overlay.addEventListener("click", function (e) {
    if (e.target === overlay) closeModal();
  });
  document.addEventListener("keydown", function (e) {
    if (e.key === "Escape" && overlay.classList.contains("open")) closeModal();
  });
})();
