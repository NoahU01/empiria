/* Medienkonzept empiria › Entwürfe – Raster und Großansicht (Aufbau wie AVRG › Social Media). */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var P = window.MK_ENTWUERFE || [], FE = window.MK_FELDER || {};
  var PFAD = '/assets/projekte/medienkonzept/postings/';
  var raster = $('#mke-raster');
  if (!raster) return;
  function nr(i) { return (i + 1 < 10 ? '0' : '') + (i + 1); }
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  raster.innerHTML = P.map(function (p, i) {
    return '<button type="button" class="ig-kachel" data-i="' + i + '" data-feld="' + p.feld + '" aria-label="Posting ' + nr(i) + ' öffnen">' +
      '<img src="' + PFAD + p.bild + '.jpg" alt="" loading="lazy">' +
      (p.seiten ? '<span class="mke-doc" aria-hidden="true">PDF · ' + p.seiten.length + '</span>' : '') +
      '<span class="ig-kachel__info">' + nr(i) + ' · ' + p.termin + '<small>' + p.feld + ' · ' + p.art + '</small></span></button>';
  }).join('');

  var filter = $('#mke-filter');
  var felder = Object.keys(FE).filter(function (k) { return P.some(function (p) { return p.feld === k; }); });
  filter.innerHTML = '<button type="button" aria-pressed="true" data-feld="">Alle ' + P.length + '</button>' +
    felder.map(function (k) { return '<button type="button" aria-pressed="false" data-feld="' + k + '">' + FE[k] + '</button>'; }).join('');
  $$('button', filter).forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.feld;
      $$('button', filter).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('.ig-kachel', raster).forEach(function (k) { k.hidden = f && k.dataset.feld !== f; });
    });
  });

  var modal = $('#mke-modal'), jetzt = 0;
  function sichtbar() { return $$('.ig-kachel', raster).filter(function (k) { return !k.hidden; }).map(function (k) { return +k.dataset.i; }); }
  function oeffne(i) {
    jetzt = i; var p = P[i];
    $('#mke-bild').innerHTML = p.seiten
      ? '<div class="mke-seiten">' + p.seiten.map(function (s, n) { return '<img src="' + PFAD + s + '.jpg" alt="Seite ' + (n + 1) + '">'; }).join('') + '</div><p class="mke-hinweis">Seiten zur Seite wischen · ' + p.seiten.length + ' Seiten</p>'
      : '<img src="' + PFAD + p.bild + '.jpg" alt="">';
    $('#mke-format').textContent = 'Posting ' + nr(i) + ' · ' + p.termin + ' · 8:30 Uhr';
    $('#mke-text').textContent = p.text;
    $('#mke-meta').innerHTML = '<dt>Themenfeld</dt><dd>' + p.feld + ' · ' + p.art + '</dd><dt>Format</dt><dd>' + p.format + '</dd>' +
      '<dt>Was bleibt</dt><dd>' + esc(p.kern) + '</dd><dt>Noch offen</dt><dd>' + esc(p.offen) + '</dd>';
    $('#mke-laden').href = PFAD + p.bild + '.jpg';
    $('#mke-laden').setAttribute('download', 'posting-' + nr(i) + '.jpg');
    var pdf = $('#mke-pdf'); pdf.hidden = !p.pdf; if (p.pdf) { pdf.href = PFAD + p.pdf; pdf.setAttribute('download', p.pdf); }
    var k = $('#mke-kopieren'); k.classList.remove('ist-kopiert'); k.textContent = 'Text kopieren';
    if (!modal.open) modal.showModal();
  }
  raster.addEventListener('click', function (e) { var k = e.target.closest('.ig-kachel'); if (k) oeffne(+k.dataset.i); });
  function blaettere(d) { var l = sichtbar(), pos = l.indexOf(jetzt); oeffne(l[(pos + d + l.length) % l.length]); }
  $('#mke-zurueck').addEventListener('click', function () { blaettere(-1); });
  $('#mke-vor').addEventListener('click', function () { blaettere(1); });
  $('#mke-zu').addEventListener('click', function () { modal.close(); });
  $('#mke-kopieren').addEventListener('click', function () {
    var t = P[jetzt].text, k = this;
    (navigator.clipboard ? navigator.clipboard.writeText(t) : Promise.reject()).then(function () { k.classList.add('ist-kopiert'); k.textContent = 'Kopiert ✓'; }, function () { k.textContent = 'Bitte markieren und kopieren'; });
  });
  modal.addEventListener('click', function (e) { if (e.target === modal) modal.close(); });
  modal.addEventListener('keydown', function (e) { if (e.key === 'ArrowRight') blaettere(1); if (e.key === 'ArrowLeft') blaettere(-1); });
  if (/^#posting-\d+$/.test(location.hash)) { var n = +location.hash.slice(9) - 1; if (P[n]) oeffne(n); }
})();
