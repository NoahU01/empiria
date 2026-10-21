/* Medienkonzept empiria › Entwürfe – Raster und Großansicht (Aufbau wie AVRG › Social Media). */
(function () {
  var $ = function (s, r) { return (r || document).querySelector(s); };
  var $$ = function (s, r) { return Array.prototype.slice.call((r || document).querySelectorAll(s)); };
  var P = window.MK_ENTWUERFE || [], FE = window.MK_FELDER || {};
  var PFAD = '/assets/projekte/medienkonzept/postings/', BV = '?v=64';
  var raster = $('#mke-raster');
  if (!raster) return;
  function nr(i) { return (i + 1 < 10 ? '0' : '') + (i + 1); }
  function esc(t) { return t.replace(/&/g, '&amp;').replace(/</g, '&lt;'); }

  var W = window.MK_WOCHEN || [];
  var STATUS = { entwurf: ['offen', 'Zur Freigabe'], freigegeben: ['frei', 'Freigegeben'], geplant: ['buffer', 'In Buffer'], veroeffentlicht: ['archiv', 'Veröffentlicht'] };
  function status(p) { return STATUS[p.status] || STATUS.entwurf; }
  // Kennzahlen (Daniel, 14.10.2026): jeder tägliche Messpunkt der ersten 7 Tage (Impressionen), dazu Reaktionen/Kommentare zuletzt
  function zahlen(p) {
    var k = p.kennzahlen || [];
    if (!k.length) return '';
    var f = function (n) { return n == null ? '–' : Number(n).toLocaleString('de-DE'); }, last = k[k.length - 1];
    var wann = function (h) { return h < 20 ? Math.round(h) + ' h' : 'Tag ' + Math.round(h / 24); };
    return '<p class="mke-zahlen"><span class="mke-zahlen__titel">Impressionen</span>' +
      k.map(function (x) { return '<span><b>' + f(x.impressionen) + '</b> ' + wann(x.stunden) + '</span>'; }).join('') +
      '<span class="mke-zahlen__rest">' + f(last.reaktionen) + (last.reaktionen === 1 ? ' Reaktion · ' : ' Reaktionen · ') + f(last.kommentare) + (last.kommentare === 1 ? ' Kommentar' : ' Kommentare') + '</span></p>';
  }
  function tag(t) {
    var kopf = '<span class="mke-tag__datum">' + t.tag + '</span>';
    if (t.i != null) {
      var p = P[t.i], st = status(p);
      return '<div class="mke-tag">' + '<div class="mke-tag__kopf">' + kopf + '<span class="mke-status mke-status--' + st[0] + '">' + st[1] + '</span></div>' +
        '<button type="button" class="ig-kachel mke-k" data-i="' + t.i + '" aria-label="' + t.tag + ' öffnen">' +
        '<img src="' + PFAD + p.bild + '.jpg' + BV + '" alt="" loading="lazy"></button>' +
        zahlen(p) + '<p class="mke-tag__typ">' + (p.url ? '<a href="' + p.url + '" target="_blank" rel="noopener">auf LinkedIn ↗</a> · ' : '') + esc(p.format) + '</p></div>';
    }
    if (t.plan) {
      return '<div class="mke-tag">' + '<div class="mke-tag__kopf">' + kopf + '<span class="mke-status mke-status--plan">' + (t.plan.interview ? 'Interview mit dir' : 'Zu schreiben') + '</span></div>' +
        '<div class="mke-platz"><p>' + esc(t.plan.aussage) + '</p></div>' +
        '<p class="mke-tag__typ">' + esc(t.plan.typ) + '</p></div>';
    }
    return '<div class="mke-tag">' + '<div class="mke-tag__kopf">' + kopf + '</div><div class="mke-platz mke-platz--leer"><p>kein Posting</p></div><p class="mke-tag__typ">&nbsp;</p></div>';
  }
  function woche(w) {
    return '<section class="mke-woche"><h2 class="mke-woche__kopf">' + w.kw + '<span>' + w.spanne + '</span></h2>' +
      '<div class="mke-tage">' + w.tage.map(tag).join('') + '</div></section>';
  }
  raster.innerHTML = W.map(woche).join('');
  var rasterFirma = null;
  var archiv = $('#mke-archiv'), A = window.MK_ARCHIV || [];
  if (archiv) archiv.innerHTML = A.length ? A.map(woche).join('') : '<p class="mke-archiv__leer">Noch nichts veröffentlicht. Sobald alle Postings einer Woche erschienen sind, wandert die Woche hierher – mit Bild, Text und Link zu LinkedIn.</p>';

  var modal = $('#mke-modal'), jetzt = 0, variante = 'bild';
  function sichtbar() {
    return $$('.ig-kachel').filter(function (k) { return !k.hidden; }).map(function (k) { return +k.dataset.i; });
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
    $('#mke-format').textContent = firma ? 'Firmenprofil · ' + p.termin + ' · 9:00 Uhr' : p.termin + ' · ' + '7:45' + ' Uhr · ' + status(p)[1];
    $('#mke-text').textContent = p.text;
    $('#mke-meta').innerHTML = '<dt>Themenfeld</dt><dd>' + p.feld + ' · ' + p.art + '</dd><dt>Format</dt><dd>' + p.format + '</dd>' +
      '<dt>Was bleibt</dt><dd>' + esc(p.kern) + '</dd>' + (p.offen ? '<dt>Noch offen</dt><dd>' + esc(p.offen) + '</dd>' : '');
    $('#mke-laden').setAttribute('download', (firma ? 'firma-' : 'posting-') + nr(i) + '.jpg');
    bildZeigen();
    var pdf = $('#mke-pdf'); pdf.hidden = !p.pdf; if (p.pdf) { pdf.href = PFAD + p.pdf; pdf.setAttribute('download', p.pdf); }
    var k = $('#mke-kopieren'); k.classList.remove('ist-kopiert'); k.textContent = 'Text kopieren';
    if (!modal.open) modal.showModal();
  }
  [raster, archiv].forEach(function (r) { if (r) r.addEventListener('click', function (e) { var k = e.target.closest('.ig-kachel'); if (k) oeffne(+k.dataset.i); }); });
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
