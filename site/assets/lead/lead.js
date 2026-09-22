/* ===== Lead-Dialog der Weihnachtsseiten ======================================
   Jedes Element mit data-lead oeffnet den Dialog statt der Unterseite.
   Erwartete Attribute:
     data-lead        Titel des Themas
     data-text        ein Satz dazu
     data-pdf         Pfad zum PDF
     data-bild        Vorschaubild des PDF (optional)
     data-kicker      Zeile ueber dem Titel (optional, Standard unten)

   WICHTIG, damit hier keine falsche Sicherheit entsteht:
   Es gibt noch KEINE Anbindung. Die Adresse wird nur dann verschickt, wenn
   window.XMAS_LEAD_ENDPOINT gesetzt ist; sonst bleibt sie im Browser. Und das
   PDF liegt oeffentlich unter seiner URL - wer sie kennt, kommt ohne Adresse
   daran. Fuer einen echten Lead-Magneten muss der Download ueber den Server
   laufen, der die Adresse vorher entgegennimmt.
*/
(function () {
  var karte, bg, form, feld, knopf, dl, aktuell = null, letzterAusloeser = null;

  function bauen() {
    bg = document.createElement('div');
    bg.className = 'lead-bg';
    bg.setAttribute('role', 'dialog');
    bg.setAttribute('aria-modal', 'true');
    bg.hidden = false;
    bg.innerHTML =
      '<div class="lead-karte">' +
        '<button class="lead-zu" type="button" aria-label="Schließen">&times;</button>' +
        '<div class="lead-kopf">' +
          '<img class="lead-bild" src="" alt="" hidden>' +
          '<div><p class="lead-kicker"></p>' +
          '<h3 class="lead-h"></h3><p class="lead-txt"></p></div>' +
        '</div>' +
        '<form class="lead-form" novalidate>' +
          '<label class="lead-feld"><span>Deine E-Mail-Adresse</span>' +
            '<input type="email" name="email" required placeholder="name@unternehmen.de" ' +
            'autocomplete="email" inputmode="email"></label>' +
          '<button class="lead-knopf" type="submit">PDF anfordern</button>' +
          '<p class="lead-klein">Wir schicken Dir das PDF und melden uns nur zu diesem Thema. ' +
            'Mehr dazu in der <a href="/datenschutz.html">Datenschutzerklärung</a>.</p>' +
        '</form>' +
        '<div class="lead-fertig">' +
          '<span class="lead-haken"><svg viewBox="0 0 24 24" aria-hidden="true">' +
            '<path d="M5 12.5 10 17.5 19 7"/></svg></span>' +
          '<h4>Da ist es.</h4>' +
          '<p>Der Download startet gleich von selbst. Falls nicht, hier entlang:</p>' +
          '<a class="lead-dl" href="" download>PDF herunterladen</a>' +
        '</div>' +
      '</div>';
    document.body.appendChild(bg);

    karte = bg.querySelector('.lead-karte');
    form = bg.querySelector('.lead-form');
    feld = bg.querySelector('input[name=email]');
    knopf = bg.querySelector('.lead-knopf');
    dl = bg.querySelector('.lead-dl');

    bg.querySelector('.lead-zu').addEventListener('click', zu);
    bg.addEventListener('mousedown', function (e) { if (e.target === bg) zu(); });
    document.addEventListener('keydown', function (e) { if (e.key === 'Escape' && bg.classList.contains('auf')) zu(); });
    form.addEventListener('submit', absenden);
  }

  function auf(daten, ausloeser) {
    if (!bg) bauen();
    aktuell = daten;
    letzterAusloeser = ausloeser || null;
    karte.classList.remove('fertig');
    form.reset();
    knopf.disabled = false;
    knopf.textContent = 'PDF anfordern';
    bg.querySelector('.lead-kicker').textContent = daten.kicker || 'Zum Download';
    bg.querySelector('.lead-h').textContent = daten.titel;
    bg.querySelector('.lead-txt').textContent = daten.text;
    var bild = bg.querySelector('.lead-bild');
    if (daten.bild) { bild.src = daten.bild; bild.hidden = false; } else { bild.hidden = true; }
    dl.href = daten.pdf;
    bg.classList.add('auf');
    setTimeout(function () { feld.focus(); }, 120);
  }

  function zu() {
    bg.classList.remove('auf');
    if (letzterAusloeser) letzterAusloeser.focus();
  }

  function absenden(e) {
    e.preventDefault();
    if (!feld.checkValidity() || feld.value.indexOf('@') < 1) {
      feld.focus();
      feld.reportValidity && feld.reportValidity();
      return;
    }
    knopf.disabled = true;
    knopf.textContent = 'Einen Moment …';

    var nutzlast = { email: feld.value.trim(), thema: aktuell.titel, pdf: aktuell.pdf };
    var fertig = function () {
      karte.classList.add('fertig');
      var a = document.createElement('a');
      a.href = aktuell.pdf; a.download = '';
      document.body.appendChild(a); a.click(); a.remove();
    };

    if (window.XMAS_LEAD_ENDPOINT) {
      fetch(window.XMAS_LEAD_ENDPOINT, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify(nutzlast)
      }).then(fertig, fertig);
    } else {
      // Noch keine Anbindung - siehe Hinweis oben im Kopf dieser Datei.
      console.warn('[xmas-lead] Kein XMAS_LEAD_ENDPOINT gesetzt, Adresse wird nicht verschickt:', nutzlast);
      setTimeout(fertig, 350);
    }
  }

  function start() {
    document.querySelectorAll('[data-lead]').forEach(function (el) {
      el.addEventListener('click', function (e) {
        e.preventDefault();
        auf({
          titel: el.getAttribute('data-lead'),
          text: el.getAttribute('data-text') || '',
          pdf: el.getAttribute('data-pdf'),
          bild: el.getAttribute('data-bild'),
          kicker: el.getAttribute('data-kicker')
        }, el);
      });
    });
  }

  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
