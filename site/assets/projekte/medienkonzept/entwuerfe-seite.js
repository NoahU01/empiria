/* Medienkonzept empiria › Entwürfe – Raster und Großansicht (Aufbau wie AVRG › Social Media). */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var P = window.MK_ENTWUERFE || [], FE = window.MK_FELDER || {};
  var PFAD = '/assets/projekte/medienkonzept/postings/', BV = '?v=47';
  var raster = $('#mke-raster');
  if (!raster) return;
  function nr(i) { return (i + 1 < 10 ? '0' : '') + (i + 1); }
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  function kachel(p, i) {
    return '<button type="button" class="ig-kachel" data-i="' + i + '" data-feld="' + p.feld + '" aria-label="Posting ' + nr(i) + ' öffnen">' +
      '<img src="' + PFAD + p.bild + '.jpg' + BV + '" alt="" loading="lazy">' +
      (p.seiten ? '<span class="mke-doc" aria-hidden="true">PDF · ' + p.seiten.length + '</span>' : '') +
      '<span class="ig-kachel__info">' + (p.kanal === 'firma' ? 'Firma · ' : nr(i) + ' · ') + p.termin + '<small>' + p.feld + ' · ' + p.art + '</small></span></button>';
  }
  var D = [], FI = [];
  P.forEach(function (p, i) { (p.kanal === 'firma' ? FI : D).push(i); });
  raster.innerHTML = D.map(function (i) { return kachel(P[i], i); }).join('');
  var rasterFirma = $('#mke-raster-firma');
  if (rasterFirma) rasterFirma.innerHTML = FI.map(function (i) { return kachel(P[i], i); }).join('');

  var filter = $('#mke-filter');
  var felder = Object.keys(FE).filter(function (k) { return D.some(function (i) { return P[i].feld === k; }); });
  filter.innerHTML = '<button type="button" aria-pressed="true" data-feld="">Alle ' + D.length + '</button>' +
    felder.map(function (k) { return '<button type="button" aria-pressed="false" data-feld="' + k + '">' + FE[k] + '</button>'; }).join('');
  $$('button', filter).forEach(function (b) {
    b.addEventListener('click', function () {
      var f = b.dataset.feld;
      $$('button', filter).forEach(function (x) { x.setAttribute('aria-pressed', x === b ? 'true' : 'false'); });
      $$('.ig-kachel', raster).forEach(function (k) { k.hidden = f && k.dataset.feld !== f; });
    });
  });

  var modal = $('#mke-modal'), jetzt = 0, variante = 'bild';
  function sichtbar() {
    var r = P[jetzt].kanal === 'firma' ? rasterFirma : raster;
    return $$('.ig-kachel', r).filter(function (k) { return !k.hidden; }).map(function (k) { return +k.dataset.i; });
  }
  function bildZeigen() {
    var p = P[jetzt], b = (variante === 'alt' && p.alt) ? p.alt : p.bild;
    if (!p.seiten) $('#mke-bild').innerHTML = '<img src="' + PFAD + b + '.jpg' + BV + '" alt="">';
    $('#mke-laden').href = PFAD + b + '.jpg';
    $$('#mke-variante button').forEach(function (x) { x.setAttribute('aria-pressed', x.dataset.v === variante ? 'true' : 'false'); });
  }
  function oeffne(i) {
    jetzt = i; var p = P[i], firma = p.kanal === 'firma';
    if (!p.alt) variante = 'bild';
    $('#mke-avatar').src = firma ? '/assets/empiria-logo.svg' : '/assets/ansprechpartner-daniel.webp';
    $('#mke-avatar').classList.toggle('mke-avatar-logo', firma);
    $('#mke-name').textContent = firma ? 'empiria GmbH' : 'Daniel Ströbel';
    $('#mke-variante').hidden = !p.alt;
    $('#mke-bild').innerHTML = p.seiten
      ? '<div class="mke-seiten">' + p.seiten.map(function (s, n) { return '<img src="' + PFAD + s + '.jpg' + BV + '" alt="Seite ' + (n + 1) + '">'; }).join('') + '</div><p class="mke-hinweis">Seiten zur Seite wischen · ' + p.seiten.length + ' Seiten</p>'
      : '<img src="' + PFAD + p.bild + '.jpg" alt="">';
    $('#mke-format').textContent = firma ? 'Firmenprofil · ' + p.termin + ' · 9:00 Uhr' : 'Posting ' + nr(i) + ' · ' + p.termin + ' · 8:30 Uhr';
    $('#mke-text').textContent = p.text;
    $('#mke-meta').innerHTML = '<dt>Themenfeld</dt><dd>' + p.feld + ' · ' + p.art + '</dd><dt>Format</dt><dd>' + p.format + '</dd>' +
      '<dt>Was bleibt</dt><dd>' + esc(p.kern) + '</dd><dt>Noch offen</dt><dd>' + esc(p.offen) + '</dd>';
    $('#mke-laden').setAttribute('download', (firma ? 'firma-' : 'posting-') + nr(i) + '.jpg');
    bildZeigen();
    var pdf = $('#mke-pdf'); pdf.hidden = !p.pdf; if (p.pdf) { pdf.href = PFAD + p.pdf; pdf.setAttribute('download', p.pdf); }
    var k = $('#mke-kopieren'); k.classList.remove('ist-kopiert'); k.textContent = 'Text kopieren';
    if (!modal.open) modal.showModal();
  }
  [raster, rasterFirma].forEach(function (r) { if (r) r.addEventListener('click', function (e) { var k = e.target.closest('.ig-kachel'); if (k) oeffne(+k.dataset.i); }); });
  $$('#mke-variante button').forEach(function (b) { b.addEventListener('click', function () { variante = b.dataset.v; bildZeigen(); }); });
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
