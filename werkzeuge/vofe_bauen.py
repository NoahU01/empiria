#!/usr/bin/env python3
"""Baut die Entwurfsseiten „Wagenpaten – Volksfestumzug der Schulen“ (site/projekte/vofe-*.html).
Inhalte (Wagenliste) stehen hier; Gestaltung in site/assets/projekte/vofe/vofe.css. Nur Entwicklung."""
from pathlib import Path
Z = Path(__file__).resolve().parent.parent / "site" / "projekte"

SYMBOLE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="v-horaff" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff400"/>
 <g transform="translate(28 27)" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#1a1817" stroke-width="15"/><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#fff" stroke-width="8.5"/></g>
 <text x="60" y="99" text-anchor="middle" font-family="Poppins, sans-serif" font-size="11" font-weight="700" letter-spacing="1.5" fill="#1a1817">2027</text></symbol>
<symbol id="v-horaff-pur" viewBox="-2 -2 68 56"><g transform="" fill="none" stroke-linecap="round" stroke-linejoin="round"><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#1a1817" stroke-width="15"/><path d="M8 8v22a12 12 0 0 0 24 0V20M32 20v10a12 12 0 0 0 24 0V8" stroke="#fff" stroke-width="8.5"/></g></symbol>
<symbol id="i-brezel" viewBox="0 0 24 24"><circle cx="15.5" cy="9" r="5.5" class="tupfer"/><path d="M12 20.2c-2 1-4.4 1-6.3-.2-2.8-1.8-3.6-5.6-1.8-8.7 1.7-3 5.6-4.6 7.6-2.4 1.6 1.8.9 4.6-.5 6.4"/><path d="M12 20.2c2 1 4.4 1 6.3-.2 2.8-1.8 3.6-5.6 1.8-8.7-1.7-3-5.6-4.6-7.6-2.4-1.6 1.8-.9 4.6.5 6.4"/><path d="m7 18.6 6.5-6.8M17 18.6l-6.5-6.8"/><path d="M8 6.2h.01M11 4.8h.01M14 5.3h.01" stroke-width="2.4"/></symbol>
<symbol id="i-riesenrad" viewBox="0 0 24 24"><circle cx="12" cy="10" r="7.5" class="tupfer"/><circle cx="12" cy="10" r="7"/><circle cx="12" cy="10" r="1.3"/><path d="M12 3v5.7M12 11.3V17M5 10h5.7M13.3 10H19M7 5l4 4M13 11l4 4M17 5l-4 4M11 11l-4 4"/><path d="m8 22 4-10.5L16 22M6.5 22h11"/><rect x="10.8" y="1.4" width="2.4" height="2" rx=".6"/><rect x="3.6" y="9" width="2" height="2.4" rx=".6"/><rect x="18.4" y="9" width="2" height="2.4" rx=".6"/></symbol>
<symbol id="i-ballon" viewBox="0 0 24 24"><path d="M12 15.5c3.4 0 6-3 6-6.6C18 5.3 15.3 2.5 12 2.5S6 5.3 6 8.9c0 3.6 2.6 6.6 6 6.6z" class="tupfer"/><path d="M12 15.5c3.4 0 6-3 6-6.6C18 5.3 15.3 2.5 12 2.5S6 5.3 6 8.9c0 3.6 2.6 6.6 6 6.6z"/><path d="m11 15.5-.7 1.5h3.4l-.7-1.5"/><path d="M12 17c-1.6 1.6 1.6 2.8 0 4.8"/><path d="M9 6.8c.5-1.2 1.4-1.9 2.4-2.1"/></symbol>
<symbol id="i-herz" viewBox="0 0 24 24"><path d="M12 20.5S3 15 3 8.8C3 6 5 4 7.5 4c1.9 0 3.5 1.1 4.5 2.7C13 5.1 14.6 4 16.5 4 19 4 21 6 21 8.8c0 6.2-9 11.7-9 11.7z" class="tupfer"/><path d="M12 20.5S3 15 3 8.8C3 6 5 4 7.5 4c1.9 0 3.5 1.1 4.5 2.7C13 5.1 14.6 4 16.5 4 19 4 21 6 21 8.8c0 6.2-9 11.7-9 11.7z"/><path d="M6.2 9.4c.9.9 1.8-.9 2.8 0s1.9-.9 2.9 0 1.9-.9 2.9 0 1.9-.9 2.8 0"/><path d="M9.5 12.6h5M10.5 15h3"/><path d="M8.5 4.3c1.5-3 5.5-3 7 0"/></symbol>
<symbol id="i-bonbon" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="5" ry="3.8" class="tupfer"/><ellipse cx="12" cy="12" rx="5" ry="3.8"/><path d="M7.1 11 3 7.8v8.4l4.1-3.2M16.9 11 21 7.8v8.4l-4.1-3.2"/><path d="M10 9.2c.8 1.6.8 4 0 5.6M13.6 9.1c.8 1.7.8 4.1 0 5.8"/></symbol>
<symbol id="i-dirndl" viewBox="0 0 24 24"><path d="M9 3.5 8 8l-3.5 12.5h15L16 8l-1-4.5"/><path d="M8 8h8M9.3 3.5c.8 1.7 4.6 1.7 5.4 0"/><path d="M13.5 8.5 15 20.5" /><path d="M10 12.5h4"/></symbol>
<symbol id="i-lederhose" viewBox="0 0 24 24"><path d="M6.5 9h11l1 11.5h-5L12 14l-1.5 6.5h-5z"/><path d="M8 9 6.5 2.5M16 9l1.5-6.5M7.4 5.2h9.2"/><circle cx="9.3" cy="12" r=".6"/><circle cx="14.7" cy="12" r=".6"/></symbol>
<symbol id="i-wagen" viewBox="0 0 24 24"><path d="M3 15.5h15.5l1-6H5.5z" class="tupfer"/><path d="M3 15.5h15.5l1-6H5.5z"/><path d="M6 9.5 7.5 5.5h8l2 4M19.5 12.5H22"/><circle cx="7" cy="18" r="2.3"/><circle cx="16" cy="18" r="2.3"/><path d="M9.5 5.5 10.5 3l1.2 2.5L13 3l1.1 2.5"/></symbol>
<symbol id="i-engel" viewBox="0 0 24 24"><path d="M10.2 11.4C7.8 8 4 6.3 1.8 7c-.1 4.7 2.5 8.6 6.8 9.7zM13.8 11.4C16.2 8 20 6.3 22.2 7c.1 4.7-2.5 8.6-6.8 9.7z" class="tupfer"/><path d="M10.2 11.4C7.8 8 4 6.3 1.8 7c-.1 4.7 2.5 8.6 6.8 9.7M13.8 11.4C16.2 8 20 6.3 22.2 7c.1 4.7-2.5 8.6-6.8 9.7"/><path d="M4.8 10.3c.9 1.7 2.3 3 4 3.8M19.2 10.3c-.9 1.7-2.3 3-4 3.8"/><ellipse cx="12" cy="2.3" rx="3.2" ry="1"/><circle cx="12" cy="6.4" r="2.1"/><path d="M10.3 9.7h3.4l3.4 11.3H6.9z"/></symbol>
<symbol id="i-hand" viewBox="0 0 24 24"><circle cx="16" cy="8" r="5" class="tupfer"/><path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10.5V4a1.5 1.5 0 0 1 3 0v6.5M14 10.5V5.5a1.5 1.5 0 0 1 3 0V13c0 4.4-2.7 8-7 8-3.2 0-4.8-1.6-6.4-4.8L2.4 13.6a1.5 1.5 0 0 1 2.5-1.6L8 15"/></symbol>
<symbol id="i-sonne" viewBox="0 0 24 24"><circle cx="12" cy="12" r="5.5" class="tupfer"/><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/><path d="M10.4 12.6c.9.9 2.3.9 3.2 0"/></symbol>
<symbol id="i-handy" viewBox="0 0 24 24"><rect x="6.5" y="2.5" width="11" height="19" rx="2.2" class="tupfer"/><rect x="6.5" y="2.5" width="11" height="19" rx="2.2"/><path d="M10.5 5h3M9.5 10.8l1.8 1.8 3.4-3.4"/><path d="M11 18.5h2"/></symbol>
<symbol id="i-pfeil" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-weiter" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-regen" viewBox="0 0 24 24"><path d="M7 16.5h10.5a4 4 0 0 0 .6-8 6 6 0 0 0-11.6 1A3.5 3.5 0 0 0 7 16.5z" class="tupfer"/><path d="M7 16.5h10.5a4 4 0 0 0 .6-8 6 6 0 0 0-11.6 1A3.5 3.5 0 0 0 7 16.5z"/><path d="M9 19.5l-.8 2M13 19.5l-.8 2M17 19.5l-.8 2"/></symbol>
</defs></svg>'''

def i(name, cls="ico"): return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def kopf(seite):
    nav = [("vofe-umzug-schulen.html", "Start"), ("vofe-festzug.html", "Der Festzug"), ("vofe-ueber-uns.html", "Über uns")]
    return (f'''<div class="dev"><div class="wrap"><span>Entwurf · nur in der Entwicklungsumgebung sichtbar · Volksfestumzug 2027 (Wagenliste: Stand 2024)</span><a href="../index.html">← zurück zu empiria</a></div></div>
<header class="kopf"><div class="wrap">
<a class="marke" href="vofe-umzug-schulen.html"><svg class="marke__zeichen" aria-hidden="true"><use href="#v-horaff"/></svg><span><b>Wagenpaten</b><small>Volksfestumzug der Schulen 2027</small></span></a>
<div class="stadtlogo" title="Platzhalter – Nutzung des Stadtlogos vor Veröffentlichung mit der Stadt klären"><span>CR</span>Mit freundlicher<br>Unterstützung (Logo Stadt)</div>
<nav class="nav" aria-label="Seiten">''' + "".join(f'<a href="{h}"' + (' aria-current="page"' if h == seite else "") + f'>{t}</a>' for h, t in nav) +
            '<a class="knopf" href="vofe-festzug.html">Wagen aussuchen</a></nav></div></header>')

FUSS = '''<footer class="fuss"><div class="wrap">
<div><b>Wagenpaten</b><p style="margin-top:.4rem">Eine Initiative von Crailsheimern für Crailsheim.<br>Kontakt: daniel.stroebel@empiria.de</p></div>
<nav><a href="vofe-umzug-schulen.html">Start</a><a href="vofe-festzug.html">Der Festzug</a><a href="vofe-ueber-uns.html">Über uns</a></nav>
</div></footer>'''

def seite(datei, titel, rumpf):
    html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} · Wagenpaten (Entwurf)</title>
<meta name="robots" content="noindex, nofollow">
<link rel="stylesheet" href="/assets/fonts/fonts.css">
<link rel="stylesheet" href="/assets/projekte/vofe/vofe.css">
</head>
<body>
{SYMBOLE}
{kopf(datei)}
<main>
{rumpf}
</main>
{FUSS}
<script src="/assets/projekte/vofe/vofe.js"></script>
</body>
</html>
'''
    (Z / datei).write_text(html, encoding="utf-8")

# ---------------------------------------------------------------- Startseite
START = f'''<section class="held"><div class="wrap">
<div>
  <p class="kicker">Volksfestumzug der Schulen 2027 · Crailsheim</p>
  <h1>Süßes für den <em>Umzug.</em></h1>
  <p class="lead">Beim Fränkischen Volksfest 2027 sind wieder die Schulen dran: Übernehmt die Patenschaft für einen Wagen – damit die Kinder ihre Süßigkeiten nicht mehr selbst mitbringen müssen und am Straßenrand alle strahlen.</p>
  <div class="knoepfe"><a class="knopf" href="vofe-festzug.html">Wagen aussuchen {i("weiter")}</a><a class="knopf knopf--rand" href="#so-gehts">So funktioniert’s</a></div>
  <div class="held__fakten"><div><b>23</b>Wagen der Schulen</div><div><b>16</b>Schulen aus Crailsheim und Umgebung</div><div><b>2027</b>Umzug der Schulen</div></div>
</div>
<div class="held__bild" aria-hidden="true">
  <svg class="held__zeichen"><use href="#v-horaff"/></svg>
  <span class="schwebe schwebe--1">{i("brezel")}</span><span class="schwebe schwebe--2">{i("ballon")}</span><span class="schwebe schwebe--3">{i("riesenrad")}</span><span class="schwebe schwebe--4">{i("herz")}</span>
</div>
</div></section>

<section class="sek sek--gelb"><div class="wrap idee">
<div class="idee__text">
  <p class="kicker">Die Idee</p>
  <h2 class="h2">Damit die Kinder einfach nur Spaß haben.</h2>
  <p style="margin-top:1.4rem">Beim Fränkischen Volksfest 2027 gestalten wieder die Schulen den großen Umzug. Hunderte Kinder laufen mit und verteilen Süßigkeiten an die Zuschauer am Straßenrand.</p>
  <p>Bisher bringen die Kinder ihre Süßigkeiten selbst mit. Das wollen wir ändern: Unternehmen aus Crailsheim und Umgebung werden Wagenpaten – zum Wohl aller.</p>
  <p><b>Wagenengel</b> sorgen beim Umzug für die Sicherheit an den Wagen. <b>Wagenpaten</b> sorgen dafür, dass auf dem Wagen ordentlich was zum Verteilen ist.</p>
</div>
<div class="zitat">{i("engel")}<p>„Als Wagenengel habe ich beim letzten Schulumzug gesehen, wie viel Freude die Kinder haben – dass sie dafür aber ihre eigenen Süßigkeiten mitbringen müssen.“</p><small>Daniel Ströbel, Initiator</small></div>
</div></section>

<section class="sek" id="so-gehts"><div class="wrap">
<p class="kicker">So funktioniert’s</p>
<h2 class="h2">In vier Schritten zum Wagenpaten.</h2>
<div class="schritte">
  <div class="schritt"><span class="schritt__ico">{i("wagen")}</span><h3>Wagen aussuchen</h3><p>Im Festzug seht ihr jeden Wagen mit Motto und Schule.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("hand")}</span><h3>Wagenpate werden</h3><p>Ein Klick genügt – wir melden uns und klären alles Weitere.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("bonbon")}</span><h3>Süßes bereitstellen</h3><p>Süßigkeiten oder Kleinigkeiten zum Verteilen – Menge und Übergabe stimmen wir mit der Schule ab.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("sonne")}</span><h3>Alle strahlen</h3><p>Am Umzugstag verteilen die Kinder eure Gaben – und ihr seid Teil des Festes.</p></div>
</div>
</div></section>

<section class="sek sek--schwarz"><div class="wrap">
<p class="kicker">Für Unternehmen</p>
<h2 class="h2">Was bringt das eurem Unternehmen?</h2>
<p class="lead">Eine Patenschaft ist ein Beitrag zu einer Tradition, die Crailsheim ausmacht – und ganz nebenbei gut sichtbar.</p>
<div class="nutzen">
  <div>{i("herz")}<h3>Tradition unterstützen</h3><p>Der Volksfestumzug gehört zu Crailsheim. Mit eurer Patenschaft tragt ihr aktiv dazu bei, dass er so bleibt, wie wir ihn lieben.</p></div>
  <div>{i("riesenrad")}<h3>Ein Erlebnis für alle</h3><p>Ihr macht es möglich, dass alle Beteiligten ein großartiges Erlebnis haben – die Kinder auf den Wagen und alle, die am Straßenrand zuschauen.</p></div>
  <div>{i("handy")}<h3>Ganz nebenbei: sichtbar</h3><p>Euer Logo auf dieser Seite und in der Zeile eures Wagens. Dazu Beiträge auf Instagram und Facebook – vor und nach dem Umzug.</p><p class="nutzen__extra">Social-Media-Paket inklusive</p></div>
</div>
</div></section>

<section class="sek sek--hell"><div class="wrap">
<p class="kicker">Social Media</p>
<h2 class="h2">So erzählen wir es weiter.</h2>
<p class="lead">Jede neue Patenschaft wird zum Beitrag – automatisch gebrandet, in Schwarz und Gelb. Beispiele:</p>
<div class="posts">
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--gelb"><small>Neuer Pate</small><b>Musterfirma wird Wagenpate für „Backhaus“.</b>{i("brezel")}</div><p class="post__text">Danke! Die Reußenbergschule freut sich auf süße Unterstützung. #Volksfest #Crailsheim</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--schwarz"><small>Countdown</small><b>Noch 30 Tage bis zum Umzug.</b>{i("riesenrad")}</div><p class="post__text">15 Wagen haben schon Wagenpaten – wer macht den nächsten möglich?</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>wagenpaten.crailsheim</div><div class="post__bild post__bild--weiss"><small>Danke</small><b>23 Wagen. Ein großes Fest.</b>{i("ballon")}</div><p class="post__text">Danke an alle Wagenpaten, Wagenengel, Schulen und Kinder – das war ein Umzug!</p></article>
</div>
</div></section>

<section class="sek"><div class="wrap">
<div class="ausfall">{i("regen")}<div><h3>Und wenn ein Wagen ausfällt?</h3>
<p class="lead" style="margin-top:.6rem">Krankheit, eine Panne, schlechtes Wetter – es kann immer etwas dazwischenkommen. Dafür haben wir eine faire Regel:</p>
<ul><li><b>Rechtzeitig bekannt:</b> Ihr müsst nichts bereitstellen.</li><li><b>Kurzfristig:</b> Wir finden gemeinsam eine sichtbare Lösung, eure Süßigkeiten trotzdem zu verteilen – wenn ihr das möchtet.</li></ul></div></div>
</div></section>

<section class="sek sek--hell"><div class="wrap">
<p class="kicker">Unsere Paten</p>
<h2 class="h2">Diese Unternehmen sind dabei.</h2>
<p class="lead">Für den Umzug 2027.</p><div class="paten"><span class="beispiel">Musterfirma<br>(Beispiel)</span><span class="beispiel">Beispiel GmbH</span><span class="beispiel">Muster &amp; Co.<br>(Beispiel)</span><span>Euer Logo</span><span>Euer Logo</span><span>Euer Logo</span></div>
</div></section>

<section class="band"><div class="wrap"><h2>Sucht euch euren Wagen aus.</h2><a class="knopf" href="vofe-festzug.html">Zum Festzug {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Festzug
WAGEN = [
 ("Bau der Liebfrauenkapelle, Stadttor &amp; Gräfin Adelheid", "Realschule am Karlsberg", None),
 ("Bischof Burkhard, Begründer der Münsterlinie", "Realschule zur Flügelau und Grundschule Altenmünster", None),
 ("Barbara von Zipplingen und Hammeltanz", "Grundschule Altenmünster", None),
 ("Höfisches Leben auf der Burg Flügelau", "Realschule zur Flügelau", "Beispiel GmbH"),
 ("Freud’ und Leid in alter Zeit", "Albert-Schweitzer-Gymnasium", None),
 ("Adam Weiß und die Reformation in Crailsheim", "Albert-Schweitzer-Gymnasium", None),
 ("Alchimisten im Mittelalter", "Lise-Meitner-Gymnasium", None),
 ("Recht und Gericht in Crailsheim", "Lise-Meitner-Gymnasium", None),
 ("Brand im Spital", "Käthe-Kollwitz-Schule", None),
 ("Der tapfere Burkhard im Gefolge seiner Stadtknechte", "Leonhard-Sachs-Schule", None),
 ("Widder", "Leonhard-Sachs-Schule", None),
 ("Fahnenträger der belagernden Städte", "Leonhard-Sachs-Schule", None),
 ("Angreifende Haufen der Belagerer", "Leonhard-Sachs-Schule", None),
 ("Blide", "Leonhard-Sachs-Schule", None),
 ("Sturm auf die Stadtmauer", "Eichendorffschule", "Muster &amp; Co."),
 ("Bürgermeisterin", "Leonhard-Sachs-Schule", None),
 ("Spielende Kindergruppen", "Sprachheilschule Crailsheim", None),
 ("Bäuerliches Treiben um die Ingersheimer Mühle", "Geschwister-Scholl-Schule", None),
 ("Backhaus", "Reußenbergschule", "Musterfirma"),
 ("Die Gaukler vom Burgberg", "Freie Waldorfschule", None),
 ("Wacholderheide", "Astrid-Lindgren-Schule und Konrad-Biesalski-Schule", None),
 ("Diehlbrunnen von Bronnholzheim", "Fröbelschule Ellrichshausen", None),
 ("Fürstenhochzeit 1537 im Crailsheimer Schloss", "Eugen-Grimminger-Schule", None),
]
def wagen(n, w):
    t, s, p = w
    status = f'<span class="status status--pate">Pate: {p}</span>' if p else '<span class="status status--frei">Noch frei</span>'
    mail = f'mailto:daniel.stroebel@empiria.de?subject=Patenschaft%20Wagen%20{n:02d}'
    unten = (f'<div class="wagen__pate"><span>LOGO</span><div><b>{p}</b> <small>(Beispiel)</small><br><small>ist Pate dieses Wagens – danke!</small></div></div>' if p
             else f'<a class="knopf" href="{mail}">Patenschaft übernehmen {i("weiter")}</a>')
    return (f'<li class="wagen{" wagen--pate" if p else ""}"><span class="wagen__nr">{n:02d}</span><details><summary><div><h3>{t}</h3><p class="wagen__schule">{s}</p></div>{status}{i("pfeil","pfeil")}</summary>'
            f'<div class="wagen__mehr"><dl><dt>Motto</dt><dd>{t}</dd><dt>Schule</dt><dd>{s}</dd><dt>Verteilt wird</dt><dd>Süßigkeiten und Kleinigkeiten – Menge stimmen wir mit der Schule ab</dd></dl>{unten}</div></details></li>')

FESTZUG = f'''<section class="zugkopf"><div class="wrap">
<p class="kicker">Volksfestumzug der Schulen 2027</p>
<h1>Der Festzug.</h1>
<p class="lead">Alle Wagen der Schulen in der Reihenfolge des Umzugs. Klappt einen Wagen auf, um mehr zu sehen – und übernehmt die Patenschaft für einen, der noch frei ist.</p>
<div class="stand"><div class="balken"><i data-balken></i></div><p data-stand></p></div>
<div class="filter" role="group" aria-label="Wagen filtern"><button type="button" data-f="alle" aria-pressed="true">Alle Wagen</button><button type="button" data-f="frei" aria-pressed="false">Noch frei</button><button type="button" data-f="pate" aria-pressed="false">Mit Pate</button></div>
<ol class="zug" data-zug>{"".join(wagen(n+1, w) for n, w in enumerate(WAGEN))}</ol>
<p class="zug__hinweis">Vorschau auf Basis des Festzugs der Schulen 2024 („Luuschd, Laad und Lait – Craalse in alter Zeit“). Die Wagen für 2027 folgen, sobald die Schulen ihre Motive festgelegt haben. Paten sind Beispiele.</p>
</div></section>
<section class="band"><div class="wrap"><h2>Fragen zur Patenschaft?</h2><a class="knopf" href="vofe-ueber-uns.html">Wer dahintersteckt {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Über uns
UEBER = f'''<section class="sek"><div class="wrap ueber">
<div class="ueber__text">
  <p class="kicker">Motivation &amp; über uns</p>
  <h1 class="h2" style="font-size:clamp(2.6rem,6vw,4.6rem)">Weil das Volksfest zu uns gehört.</h1>
  <p style="margin-top:1.6rem">Wir sind Crailsheimer und Hohenloher – seit Kindheitstagen. Das Fränkische Volksfest ist fest in unseren Köpfen verankert: das Riesenrad, die Brezeln, der Umzug, bei dem die ganze Stadt auf den Beinen ist.</p>
  <p>Diese Tradition lebt davon, dass viele mitmachen. Wir haben uns überlegt, wo wir einen kleinen Beitrag leisten können – und sind bei den Kindern gelandet, die den Umzug der Schulen erst möglich machen.</p>
  <p>Die Idee ist einfach: Unternehmen aus der Region werden Wagenpaten. Die Wagenengel kümmern sich um die Sicherheit, die Wagenpaten darum, dass auf dem Wagen ordentlich was zum Verteilen ist. Die Kinder müssen nichts mehr selbst mitbringen – und am Straßenrand freuen sich alle.</p>
</div>
<div class="kopfe">
  <div class="person"><img src="/assets/daniel-round.webp" alt="Daniel Ströbel"><div><b>Daniel Ströbel</b><small>Initiator · beim letzten Schulumzug als Wagenengel dabei</small></div></div>
  <div class="person"><span class="person__platz">+</span><div><b>Mitstreiter gesucht</b><small>Platz für weitere Unterstützer der Idee</small></div></div>
</div>
</div>
<div class="wrap"><div class="werte">
  <div><h3>Für die Kinder</h3><p>Sie machen den Umzug – sie sollen ihn ohne Sorgen genießen.</p></div>
  <div><h3>Für Crailsheim</h3><p>Eine Tradition, die die Stadt zusammenbringt, verdient Unterstützung.</p></div>
  <div><h3>Mit Herz, ohne Aufwand</h3><p>Für Paten so einfach wie möglich: aussuchen, bereitstellen, freuen.</p></div>
</div></div></section>
<section class="band"><div class="wrap"><h2>Macht mit – sucht euch einen Wagen aus.</h2><a class="knopf" href="vofe-festzug.html">Zum Festzug {i("weiter")}</a></div></section>'''

seite("vofe-umzug-schulen.html", "Süßes für den Umzug", START)
seite("vofe-festzug.html", "Der Festzug", FESTZUG)
seite("vofe-ueber-uns.html", "Über uns", UEBER)
print("3 Seiten gebaut")
