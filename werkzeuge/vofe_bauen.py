#!/usr/bin/env python3
"""Baut die Entwurfsseiten „Patenwagen – Volksfestumzug der Schulen“ (site/projekte/vofe-*.html).
Inhalte (Wagenliste) stehen hier; Gestaltung in site/assets/projekte/vofe/vofe.css. Nur Entwicklung."""
from pathlib import Path
Z = Path(__file__).resolve().parent.parent / "site" / "projekte"

SYMBOLE = '''<svg width="0" height="0" style="position:absolute" aria-hidden="true"><defs>
<symbol id="v-horaff" viewBox="0 0 120 120"><circle cx="60" cy="60" r="58" fill="#fff400"/><circle cx="60" cy="60" r="52" fill="none" stroke="#1a1817" stroke-width="2.5"/>
 <path d="M27 46c0 22 7 34 17 34 9 0 13-10 16-22 3 12 7 22 16 22 10 0 17-12 17-34" fill="none" stroke="#1a1817" stroke-width="9" stroke-linecap="round" stroke-linejoin="round"/>
 <circle cx="60" cy="27" r="3.2" fill="#1a1817"/><circle cx="48" cy="29" r="2.2" fill="#1a1817"/><circle cx="72" cy="29" r="2.2" fill="#1a1817"/></symbol>
<symbol id="i-brezel" viewBox="0 0 24 24"><path d="M12 19.5c-1.6 1-3.5 1.3-5.3.6C3.8 19 2.5 15.8 3.5 12.6 4.6 9 8.2 6.8 10.6 8.4c1.9 1.3 1.7 4.2.3 6.3"/><path d="M12 19.5c1.6 1 3.5 1.3 5.3.6 2.9-1.1 4.2-4.3 3.2-7.5-1.1-3.6-4.7-5.8-7.1-4.2-1.9 1.3-1.7 4.2-.3 6.3"/><path d="M7.5 17.5 13 11.2M16.5 17.5 11 11.2"/></symbol>
<symbol id="i-riesenrad" viewBox="0 0 24 24"><circle cx="12" cy="10" r="7"/><circle cx="12" cy="10" r="1.2"/><path d="M12 3v14M5 10h14M7 5l10 10M17 5 7 15"/><path d="M8.5 22 12 11l3.5 11M7 22h10"/></symbol>
<symbol id="i-ballon" viewBox="0 0 24 24"><path d="M12 15.5c3.4 0 6-3 6-6.6C18 5.3 15.3 2.5 12 2.5S6 5.3 6 8.9c0 3.6 2.6 6.6 6 6.6z"/><path d="m11 15.5-.6 1.4h3.2l-.6-1.4"/><path d="M12 17c-1.4 1.6 1.4 2.6 0 4.5"/><path d="M9.2 6.5c.5-1 1.4-1.6 2.3-1.8"/></symbol>
<symbol id="i-herz" viewBox="0 0 24 24"><path d="M12 20.5S3 15 3 8.8C3 6 5 4 7.5 4c1.9 0 3.5 1.1 4.5 2.7C13 5.1 14.6 4 16.5 4 19 4 21 6 21 8.8c0 6.2-9 11.7-9 11.7z"/><path d="M6.6 9.3c1 1 1.9-.9 2.9 0s1.9-1 2.9 0 1.9-1 2.9 0 1.9-1 2.9 0"/><path d="M9 4.6c1-2.4 5-2.4 6 0"/></symbol>
<symbol id="i-bonbon" viewBox="0 0 24 24"><ellipse cx="12" cy="12" rx="5" ry="3.8"/><path d="M7.1 11 3 8v8l4.1-3M16.9 11 21 8v8l-4.1-3"/><path d="M10 9.2c.8 1.6.8 4 0 5.6M13.6 9.1c.8 1.7.8 4.1 0 5.8"/></symbol>
<symbol id="i-dirndl" viewBox="0 0 24 24"><path d="M9 3.5 8 8l-3.5 12.5h15L16 8l-1-4.5"/><path d="M8 8h8M9.3 3.5c.8 1.7 4.6 1.7 5.4 0"/><path d="M13.5 8.5 15 20.5" /><path d="M10 12.5h4"/></symbol>
<symbol id="i-lederhose" viewBox="0 0 24 24"><path d="M6.5 9h11l1 11.5h-5L12 14l-1.5 6.5h-5z"/><path d="M8 9 6.5 2.5M16 9l1.5-6.5M7.4 5.2h9.2"/><circle cx="9.3" cy="12" r=".6"/><circle cx="14.7" cy="12" r=".6"/></symbol>
<symbol id="i-wagen" viewBox="0 0 24 24"><path d="M3 15.5h15.5l1-6H5.5z"/><path d="M5.5 9.5 7 5.5h9l1.5 4M19.5 12.5H22"/><circle cx="7" cy="18" r="2.2"/><circle cx="16" cy="18" r="2.2"/><path d="M9 5.5 10 3l1.3 2.5L12.5 3l1.2 2.5"/></symbol>
<symbol id="i-hand" viewBox="0 0 24 24"><path d="M8 12V5.5a1.5 1.5 0 0 1 3 0V11M11 10.5V4a1.5 1.5 0 0 1 3 0v6.5M14 10.5V5.5a1.5 1.5 0 0 1 3 0V13c0 4.4-2.7 8-7 8-3.2 0-4.8-1.6-6.4-4.8L2.4 13.6a1.5 1.5 0 0 1 2.5-1.6L8 15"/></symbol>
<symbol id="i-sonne" viewBox="0 0 24 24"><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M4.6 4.6l1.4 1.4M18 18l1.4 1.4M2.5 12h2M19.5 12h2M4.6 19.4 6 18M18 6l1.4-1.4"/></symbol>
<symbol id="i-handy" viewBox="0 0 24 24"><rect x="6.5" y="2.5" width="11" height="19" rx="2.2"/><path d="M10.5 5h3M9.5 10.8l1.8 1.8 3.4-3.4"/><path d="M11 18.5h2"/></symbol>
<symbol id="i-pfeil" viewBox="0 0 24 24"><path d="m6 9 6 6 6-6"/></symbol>
<symbol id="i-weiter" viewBox="0 0 24 24"><path d="M5 12h14M13 6l6 6-6 6"/></symbol>
<symbol id="i-regen" viewBox="0 0 24 24"><path d="M7 16.5h10.5a4 4 0 0 0 .6-8 6 6 0 0 0-11.6 1A3.5 3.5 0 0 0 7 16.5z"/><path d="M9 19.5l-.8 2M13 19.5l-.8 2M17 19.5l-.8 2"/></symbol>
</defs></svg>'''

def i(name, cls="ico"): return f'<svg class="{cls}" aria-hidden="true"><use href="#i-{name}"/></svg>'

def kopf(seite):
    nav = [("vofe-umzug-schulen.html", "Start"), ("vofe-festzug.html", "Der Festzug"), ("vofe-ueber-uns.html", "Über uns")]
    return (f'''<div class="dev"><div class="wrap"><span>Entwurf · nur in der Entwicklungsumgebung sichtbar · Daten: Festzug der Schulen 2024</span><a href="../index.html">← zurück zu empiria</a></div></div>
<header class="kopf"><div class="wrap">
<a class="marke" href="vofe-umzug-schulen.html"><svg class="marke__zeichen" aria-hidden="true"><use href="#v-horaff"/></svg><span><b>Patenwagen</b><small>Volksfestumzug der Schulen</small></span></a>
<div class="stadtlogo" title="Platzhalter – Nutzung des Stadtlogos vor Veröffentlichung mit der Stadt klären"><span>CR</span>Mit freundlicher<br>Unterstützung (Logo Stadt)</div>
<nav class="nav" aria-label="Seiten">''' + "".join(f'<a href="{h}"' + (' aria-current="page"' if h == seite else "") + f'>{t}</a>' for h, t in nav) +
            '<a class="knopf" href="vofe-festzug.html">Wagen aussuchen</a></nav></div></header>')

FUSS = '''<footer class="fuss"><div class="wrap">
<div><b>Patenwagen</b><p style="margin-top:.4rem">Eine Initiative von Crailsheimern für Crailsheim.<br>Kontakt: daniel.stroebel@empiria.de</p></div>
<nav><a href="vofe-umzug-schulen.html">Start</a><a href="vofe-festzug.html">Der Festzug</a><a href="vofe-ueber-uns.html">Über uns</a></nav>
</div></footer>'''

def seite(datei, titel, rumpf):
    html = f'''<!doctype html>
<html lang="de">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{titel} · Patenwagen (Entwurf)</title>
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,600;12..96,700;12..96,800&family=Inter:wght@400;500;600;700&display=swap">
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
  <p class="kicker">Volksfestumzug der Schulen · Crailsheim</p>
  <h1>Süßes für den <em>Umzug.</em></h1>
  <p class="lead">Übernehmt die Patenschaft für einen Wagen der Schulen – damit die Kinder ihre Süßigkeiten nicht mehr selbst mitbringen müssen und am Straßenrand alle strahlen.</p>
  <div class="knoepfe"><a class="knopf" href="vofe-festzug.html">Wagen aussuchen {i("weiter")}</a><a class="knopf knopf--rand" href="#so-gehts">So funktioniert’s</a></div>
  <div class="held__fakten"><div><b>23</b>Wagen der Schulen</div><div><b>16</b>Schulen aus Crailsheim und Umgebung</div><div><b>1</b>großer Tag für alle Kinder</div></div>
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
  <p style="margin-top:1.4rem">Beim Fränkischen Volksfest gestalten im Dreijahresrhythmus Gewerbe, Landwirtschaft und Schulen den großen Umzug. Wenn die Schulen dran sind, laufen Hunderte Kinder mit – und verteilen Süßigkeiten an die Zuschauer am Straßenrand.</p>
  <p>Bisher bringen die Kinder ihre Süßigkeiten selbst mit. Das wollen wir ändern: Unternehmen aus Crailsheim und Umgebung übernehmen Patenschaften für die Wagen – zum Wohl aller.</p>
</div>
<div class="zitat">{i("wagen")}<p>„Als Wagenengel beim letzten Schulumzug habe ich gesehen, wie viel Freude die Kinder haben – und dass sie dafür ihre eigenen Süßigkeiten mitbringen.“</p><small>Daniel Ströbel, Initiator</small></div>
</div></section>

<section class="sek" id="so-gehts"><div class="wrap">
<p class="kicker">So funktioniert’s</p>
<h2 class="h2">In vier Schritten zum Patenwagen.</h2>
<div class="schritte">
  <div class="schritt"><span class="schritt__ico">{i("wagen")}</span><h3>Wagen aussuchen</h3><p>Im Festzug seht ihr jeden Wagen mit Motto und Schule.</p></div>
  <div class="schritt"><span class="schritt__ico">{i("hand")}</span><h3>Pate werden</h3><p>Ein Klick genügt – wir melden uns und klären alles Weitere.</p></div>
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
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>patenwagen.crailsheim</div><div class="post__bild post__bild--gelb"><small>Neuer Pate</small><b>Musterfirma übernimmt den Wagen „Backhaus“.</b>{i("brezel")}</div><p class="post__text">Danke! Die Reußenbergschule freut sich auf süße Unterstützung. #Volksfest #Crailsheim</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>patenwagen.crailsheim</div><div class="post__bild post__bild--schwarz"><small>Countdown</small><b>Noch 30 Tage bis zum Umzug.</b>{i("riesenrad")}</div><p class="post__text">15 Wagen haben schon einen Paten – wer macht den nächsten möglich?</p></article>
  <article class="post"><div class="post__kopf"><svg aria-hidden="true"><use href="#v-horaff"/></svg>patenwagen.crailsheim</div><div class="post__bild post__bild--weiss"><small>Danke</small><b>23 Wagen. Ein großes Fest.</b>{i("ballon")}</div><p class="post__text">Danke an alle Paten, Schulen und Kinder – das war ein Umzug!</p></article>
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
<div class="paten"><span class="beispiel">Musterfirma<br>(Beispiel)</span><span class="beispiel">Beispiel GmbH</span><span class="beispiel">Muster &amp; Co.<br>(Beispiel)</span><span>Euer Logo</span><span>Euer Logo</span><span>Euer Logo</span></div>
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
<p class="kicker">Luuschd, Laad und Lait – Craalse in alter Zeit</p>
<h1>Der Festzug.</h1>
<p class="lead">Alle Wagen der Schulen in der Reihenfolge des Umzugs. Klappt einen Wagen auf, um mehr zu sehen – und übernehmt die Patenschaft für einen, der noch frei ist.</p>
<div class="stand"><div class="balken"><i data-balken></i></div><p data-stand></p></div>
<div class="filter" role="group" aria-label="Wagen filtern"><button type="button" data-f="alle" aria-pressed="true">Alle Wagen</button><button type="button" data-f="frei" aria-pressed="false">Noch frei</button><button type="button" data-f="pate" aria-pressed="false">Mit Pate</button></div>
<ol class="zug" data-zug>{"".join(wagen(n+1, w) for n, w in enumerate(WAGEN))}</ol>
<p class="zug__hinweis">Stand: Festzug der Schulen 2024. Die Wagen für den nächsten Umzug folgen, sobald die Schulen ihre Motive festgelegt haben. Paten sind Beispiele.</p>
</div></section>
<section class="band"><div class="wrap"><h2>Fragen zur Patenschaft?</h2><a class="knopf" href="vofe-ueber-uns.html">Wer dahintersteckt {i("weiter")}</a></div></section>'''

# ---------------------------------------------------------------- Über uns
UEBER = f'''<section class="sek"><div class="wrap ueber">
<div class="ueber__text">
  <p class="kicker">Motivation &amp; über uns</p>
  <h1 class="h2" style="font-size:clamp(2.6rem,6vw,4.6rem)">Weil das Volksfest zu uns gehört.</h1>
  <p style="margin-top:1.6rem">Wir sind Crailsheimer und Hohenloher – seit Kindheitstagen. Das Fränkische Volksfest ist fest in unseren Köpfen verankert: das Riesenrad, die Brezeln, der Umzug, bei dem die ganze Stadt auf den Beinen ist.</p>
  <p>Diese Tradition lebt davon, dass viele mitmachen. Wir haben uns überlegt, wo wir einen kleinen Beitrag leisten können – und sind bei den Kindern gelandet, die den Umzug der Schulen erst möglich machen.</p>
  <p>Die Idee ist einfach: Unternehmen aus der Region übernehmen Patenschaften für die Wagen. Die Kinder müssen nichts mehr selbst mitbringen – und am Straßenrand freuen sich alle.</p>
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
