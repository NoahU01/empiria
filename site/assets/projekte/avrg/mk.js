/* Medienkonzept AVRG: Kapitel, Landingpage-Varianten, Mails, Instagram-Raster mit Großansicht */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };

  /* ---------- Kapitel ---------- */
  var kopf = $('.site-header');
  function setzeOben() { document.documentElement.style.setProperty('--mk-top', (kopf ? kopf.offsetHeight : 84) + 'px'); }
  setzeOben(); window.addEventListener('resize', setzeOben);
  var tabs = $$('.mk-tab'), leiste = $('.mk-kapitel');
  var ALT = {grundidee: 'strategie', zielgruppe: 'strategie', claim: 'strategie', postings: 'social', offen: 'fahrplan'};
  function zeige(id, scrollen) {
    id = ALT[id] || id;
    if (!$('#k-' + id)) id = 'strategie';
    tabs.forEach(function (t) {
      var an = t.dataset.k === id;
      t.setAttribute('aria-selected', an ? 'true' : 'false');
      $('#k-' + t.dataset.k).hidden = !an;
      if (an) t.scrollIntoView({block: 'nearest', inline: 'center'});
    });
    if (scrollen) window.scrollTo({top: leiste.getBoundingClientRect().top + window.scrollY - (kopf ? kopf.offsetHeight : 0) + 1, behavior: 'smooth'});
  }
  tabs.forEach(function (t) {
    t.addEventListener('click', function () { history.replaceState(null, '', '#' + t.dataset.k); zeige(t.dataset.k, true); });
  });
  $$('[data-weiter]').forEach(function (b) {
    b.addEventListener('click', function () { history.replaceState(null, '', '#' + b.dataset.weiter); zeige(b.dataset.weiter, true); });
  });
  $$('.ak-sprung a').forEach(function (a) {
    a.addEventListener('click', function (e) { e.preventDefault(); var k = a.getAttribute('href').slice(1); history.replaceState(null, '', '#' + k); zeige(k, true); });
  });
  zeige(location.hash.slice(1), false);

  /* ---------- Landingpage-Varianten ---------- */
  $$('.mk-variante').forEach(function (b) {
    b.addEventListener('click', function () {
      var v = b.dataset.v;
      $$('.mk-variante').forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $('#mk-lp-bild').src = '/assets/projekte/avrg/lp-vorschau-voll-' + v + '.jpg';
      $('.ak-browser-seite').scrollTop = 0;
      $('#mk-lp-url').textContent = 'agentur-beispiel.de/neue-altersvorsorge' + (v === '1' ? '' : '-' + v);
      $$('.mk-bausteine').forEach(function (l) { l.hidden = l.dataset.v !== v; });
      $('#mk-lp-link').href = '/projekte/avrg-landingpage-' + v + '.html';
      $('#mk-lp-link').firstChild.textContent = 'Variante ' + v + ' öffnen ';
    });
  });

  /* ---------- Mails ---------- */
  var mtabs = $$('.ak-tab');
  mtabs.forEach(function (t) {
    t.addEventListener('click', function () {
      mtabs.forEach(function (x) {
        var an = x === t;
        x.setAttribute('aria-selected', an ? 'true' : 'false');
        document.getElementById(x.getAttribute('aria-controls')).hidden = !an;
      });
    });
  });

  /* ---------- Postings ---------- */
  var P = window.AVRG_POSTINGS || [], TH = window.AVRG_THEMEN || {};
  var LOGO = '/assets/projekte/avrg/sv-owen-logo.svg', FOTO = '/assets/projekte/avrg/fotos/', SANDRA = '/assets/projekte/avrg/sandra.jpg';
  var FORMAT = {feed: 'Feed-Beitrag', karussell: 'Karussell', story: 'Story', reel: 'Reel'};
  var ICON = {
    karussell: '<svg viewBox="0 0 24 24"><rect x="7" y="3" width="14" height="14" rx="2"/><path d="M17 21H5a2 2 0 0 1-2-2V7"/></svg>',
    story: '<svg viewBox="0 0 24 24"><circle cx="12" cy="12" r="9" stroke-dasharray="3 2.4"/><circle cx="12" cy="12" r="4"/></svg>',
    reel: '<svg viewBox="0 0 24 24"><rect x="3" y="3" width="18" height="18" rx="4"/><path d="M10 9v6l5-3z" fill="currentColor"/></svg>'
  };
  function logo(platte) { return platte ? '<span class="cr__platte"><img class="cr__logo" src="' + LOGO + '" alt=""></span>' : '<img class="cr__logo" src="' + LOGO + '" alt="">'; }
  function pill(p, art) { return p.pill ? '<span class="cr__pill' + (art ? ' cr__pill--' + art : '') + '">' + p.pill + '</span>' : ''; }
  function sub(p) { return p.s ? '<p class="cr__sub">' + p.s + '</p>' : ''; }
  function punkte(p) { return p.f === 'karussell' ? '<span class="cr__punkte"><i></i><i></i><i></i><i></i></span>' : ''; }
  function creative(p, hoch) {
    var k = 'cr' + (hoch ? ' cr--hoch' : ''), innen;
    switch (p.t) {
      case 'rot':
        return '<div class="' + k + ' cr--rot"><div class="cr__innen"><p class="cr__label">' + (p.l || '') + '</p><div><p class="cr__h">' + p.h + '</p>' + sub(p) + '</div><div class="cr__fuss">' + logo(true) + pill(p, 'weiss') + '</div></div>' + punkte(p) + '</div>';
      case 'schwarz':
        return '<div class="' + k + ' cr--schwarz"><div class="cr__innen"><p class="cr__label">' + (p.l || '') + '</p><div><p class="cr__h">' + p.h + '</p>' + sub(p) + '</div><div class="cr__fuss">' + logo(true) + pill(p) + '</div></div>' + punkte(p) + '</div>';
      case 'band':
        return '<div class="' + k + ' cr--band"><img class="cr__foto" src="' + FOTO + p.foto + '.jpg" alt="" loading="lazy"><div class="cr__innen"><p class="cr__h">' + p.h + '</p><div class="cr__fuss">' + logo() + pill(p) + '</div></div></div>';
      case 'blase':
        return '<div class="' + k + '"><img class="cr__foto" src="' + FOTO + p.foto + '.jpg" alt="" loading="lazy"><p class="cr__blase">' + p.blase + '</p><span class="cr__wer">' + p.wer + '</span></div>';
      case 'verlauf':
        return '<div class="' + k + ' cr--verlauf"><img class="cr__foto" src="' + FOTO + p.foto + '.jpg" alt="" loading="lazy"><div class="cr__innen">' + logo(true) + '<div><p class="cr__h">' + p.h + '</p>' + sub(p) + '</div></div></div>';
      case 'split':
        return '<div class="' + k + '"><div class="cr__geteilt"><div class="o"><small>Ergebnis A</small><b>Mitnehmen.</b></div><div class="u"><small>Ergebnis B</small><b>Abhaken<span>.</span></b></div></div></div>';
      case 'liste':
        return '<div class="' + k + ' cr--rot"><div class="cr__innen"><p class="cr__label">' + p.l + '</p><div><p class="cr__h">' + p.h + '</p><ul class="cr__liste"><li><i>✓</i>Betrifft mich das?</li><li><i>✓</i>Wenn ja: wie?</li><li><i>✓</i>Habe ich einen Vorteil?</li></ul></div><div class="cr__fuss">' + logo(true) + '</div></div>' + punkte(p) + '</div>';
      case 'nein':
        return '<div class="' + k + '"><div class="cr__innen"><p class="cr__label">' + p.l + '</p><ul class="cr__nein">' + p.items.map(function (x) { return '<li>' + x + '</li>'; }).join('') + '</ul><div class="cr__fuss">' + logo() + pill(p) + '</div></div></div>';
      case 'zahl':
        return '<div class="' + k + '"><div class="cr__innen"><p class="cr__zahl">' + p.z + '</p><p class="cr__h" style="font-size:7cqi">' + p.h + '</p><div class="cr__fuss">' + logo() + pill(p) + '</div></div></div>';
      case 'umfrage':
        return '<div class="' + k + '"><div class="cr__innen"><p class="cr__label">' + p.l + '</p><div><p class="cr__h">' + p.h + '</p><div class="cr__umfrage">' + p.opt.map(function (x) { return '<span>' + x + '</span>'; }).join('') + '</div></div><div class="cr__fuss">' + logo() + '</div></div></div>';
      case 'sandra':
        return '<div class="' + k + ' cr--grau"><div class="cr__innen"><p class="cr__label">Sandra Hild · Owen</p><p class="cr__h" style="max-width:72%">' + p.h + '</p><span></span></div><img class="cr__sandra" src="' + SANDRA + '" alt=""></div>';
      case 'ticket':
        return '<div class="' + k + ' cr--grau"><div class="cr__innen"><p class="cr__label">' + p.l + '</p><p class="cr__h" style="max-width:80%">' + p.h + '</p><span></span></div><div class="cr__mini-ticket"><small>Klarheits-Ticket</small><b>15 Minuten</b><small>Einlösbar bei Sandra Hild</small></div></div>';
      default:
        return '<div class="' + k + '"><div class="cr__innen"><p class="cr__label">' + (p.l || '') + '</p><div><p class="cr__h">' + p.h + '</p>' + sub(p) + '</div><div class="cr__fuss">' + logo() + pill(p) + '</div></div>' + punkte(p) + '</div>';
    }
  }
  var raster = $('#ig-raster');
  if (raster) {
    raster.innerHTML = P.map(function (p, i) {
      return '<button type="button" class="ig-kachel" data-i="' + i + '" data-th="' + p.th + '" aria-label="Posting ' + (i + 1) + ' öffnen">' + creative(p, false) +
        (ICON[p.f] ? '<span class="ig-format">' + ICON[p.f] + '</span>' : '') +
        '<span class="ig-kachel__info">Woche ' + p.w + ' · ' + TH[p.th] + '<small>' + FORMAT[p.f] + '</small></span></button>';
    }).join('');
    /* Filter */
    var zaehle = {}; P.forEach(function (p) { zaehle[p.th] = (zaehle[p.th] || 0) + 1; });
    var filter = $('#ig-filter');
    filter.innerHTML = '<button type="button" aria-pressed="true" data-th="">Alle</button>' + Object.keys(TH).map(function (k) { return '<button type="button" aria-pressed="false" data-th="' + k + '">' + TH[k] + '</button>'; }).join('');
    var aktiv = '';
    $$('button', filter).forEach(function (b) {
      b.addEventListener('click', function () {
        aktiv = b.dataset.th;
        $$('button', filter).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
        $$('.ig-kachel', raster).forEach(function (k) { k.hidden = aktiv && k.dataset.th !== aktiv; });
      });
    });
    /* Großansicht */
    var modal = $('#ig-modal'), jetzt = 0;
    function sichtbar() { return $$('.ig-kachel', raster).filter(function (k) { return !k.hidden; }).map(function (k) { return +k.dataset.i; }); }
    function oeffne(i) {
      jetzt = i; var p = P[i], hoch = p.f === 'story' || p.f === 'reel';
      $('#ig-m-bild').innerHTML = creative(p, hoch);
      $('#ig-m-format').textContent = 'Woche ' + p.w + ' · ' + FORMAT[p.f];
      $('#ig-m-text').innerHTML = p.cap.replace(/</g, '&lt;') + (p.tags ? '\n\n<span class="tags">' + p.tags + '</span>' : '');
      var meta = [['Thema', TH[p.th]], ['Format', FORMAT[p.f]], ['Bild', p.bild], ['Ziel', p.ziel]];
      if (p.folien) meta.push(['Folien', p.folien]);
      $('#ig-m-meta').innerHTML = meta.map(function (m) { return '<dt>' + m[0] + '</dt><dd>' + m[1] + '</dd>'; }).join('');
      if (!modal.open) modal.showModal();
    }
    raster.addEventListener('click', function (e) { var k = e.target.closest('.ig-kachel'); if (k) oeffne(+k.dataset.i); });
    function blaettere(d) { var l = sichtbar(), pos = l.indexOf(jetzt); oeffne(l[(pos + d + l.length) % l.length]); }
    $('#ig-zurueck').addEventListener('click', function () { blaettere(-1); });
    $('#ig-vor').addEventListener('click', function () { blaettere(1); });
    $('#ig-zu').addEventListener('click', function () { modal.close(); });
    modal.addEventListener('click', function (e) { if (e.target === modal) modal.close(); });
    modal.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') blaettere(1); if (e.key === 'ArrowLeft') blaettere(-1); });
  }
})();
