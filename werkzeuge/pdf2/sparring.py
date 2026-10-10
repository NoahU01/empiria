"""PDF „Sparring für Führungskräfte“ im Muster KI zum Anfassen – Runde 2 (10.10.2026).
Quelle: site/projekte/empiria-2/sparring.html (Abschnitte in derselben Reihenfolge), ergänzend P["sparring"] im alten PDF.
„1:1“ steht nur einmal – im Kopfbild der Titelseite."""
from lib import (titelseite, kopfbild, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, check, dokument, ico)

TITEL = "Sparring für Führungskräfte – empiria"
T = "Sparring für Führungskräfte"
N = 4

CSS = """
h2, h3, .lead, .punkte p, .zs p, .kasten p { text-wrap: pretty; }
.wann { display: grid; grid-template-columns: repeat(4, 1fr); gap: 5mm; margin-top: 5mm; }
.wann > div { border-top: 1.6px solid #1a1817; padding-top: 3.6mm; display: flex; align-items: center; gap: 2.6mm; }
.wann svg { width: 5.6mm; height: 5.6mm; flex: 0 0 auto; }
.wann b { font-family: 'Lora', Georgia, serif; font-size: 10pt; line-height: 1.2; display: block; }
.turbo .punkte > div { display: flex; align-items: center; gap: 3.5mm; padding-top: 4mm; }
.turbo .punkte svg { margin: 0; flex: 0 0 auto; width: 6mm; height: 6mm; }
.turbo .punkte h3 { font-size: 11pt; line-height: 1.3; }
.ueber { margin-top: 5mm; columns: 2; column-gap: 9mm; list-style: none; border-top: 1.6px solid #1a1817; }
.ueber li { break-inside: avoid; position: relative; padding: 1.8mm 0 1.8mm 7mm; border-bottom: 1px solid #dcd8d1; font-size: 9.2pt; line-height: 1.45; }
.ueber li::before { content: ""; position: absolute; left: 0; top: 3.9mm; width: 3mm; height: 1.6mm; border-left: 1.6px solid #1a1817; border-bottom: 1.6px solid #1a1817; transform: rotate(-45deg); }
.turbo h2 { color: #fff; }
.turbo .lead { color: rgba(255,255,255,.85); max-width: 165mm; }
.turbo .schluss { margin-top: 6mm; padding-top: 0; border-top: 0; display: grid; grid-template-columns: 1fr 1fr; gap: 9mm; }
.turbo .schluss p { font-size: 9.2pt; line-height: 1.6; color: rgba(255,255,255,.82); }
.turbo .schluss p b { color: #fff; font-weight: 600; }
"""


def bauen():
    s1 = seite(titelseite(
        T, 'Offen sprechen.<br><span class="hl">Klar entscheiden.</span><br>Volle Wirkung.',
        "Seit vielen Jahren begleite ich Vorstandsmitglieder und Führungskräfte vertrauensvoll bei strategischen Themen, "
        "Ideen zum Geschäftsmodell oder Führungsfragen.",
        kopfbild("1:1 Sparring"),
        [("Branche", "Versicherungsbranche"), ("Ebene", "Abteilung bis Vorstand"), ("Themen", "Strategie &amp; Führung")]))

    s2 = seite(
        kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:12mm;padding-bottom:13mm">' + kicker("Das bekommst Du")
        + '<h2>Ein Gegenüber, das mitdenkt <br>und mitgestaltet.</h2>'
        + '<p class="lead">Offen über Themen sprechen, für die es intern oft nicht die passende Distanz oder Erfahrung gibt – und Lösungswege klar definieren.</p>'
        + punkte([("lock", "Offen &amp; vertraulich", "Ein Raum, in dem Themen wirklich offen besprochen werden können – ohne interne Rücksichten."),
                  ("star", "Erfahrung, die trägt", "Viele Jahre Sparring mit Vorstandsmitgliedern, Hauptabteilungs- und Abteilungsleitern in der Versicherungsbranche."),
                  ("eye", "Mehrere Perspektiven", "Komplexe Situationen werden aus unterschiedlichen Blickwinkeln betrachtet – für Lösungswege, die wirklich passen.")])
        + punkte([("compass", "Klarheit &amp; Handlungssicherheit", "Am Ende steht nicht nur eine Einschätzung, sondern eine Richtung, mit der sich weiterarbeiten lässt."),
                  ("rocket", "Vom Gespräch zur Umsetzung", "Wenn es ans Vorantreiben geht, entsteht daraus schnell ein einsatzbereites Konzept – kommunikativ oder inhaltlich."),
                  ("megaphone", "Schlagkräftig nach außen", "Ob gegenüber dem Vorstand oder anderen Bereichen: Sparring macht Positionierung und Auftreten sichtbar stärker.")])
        + '</div><div class="rand" style="padding-top:11mm">' + kicker("Für wen das gemacht ist")
        + check(["Vorstandsmitglieder, die ein vertrauliches Gegenüber brauchen", "Hauptabteilungs- und Abteilungsleitungen in der Versicherungsbranche",
                 "Führungskräfte vor strategischen Weichenstellungen", "Alle, die Positionierung und Auftreten spürbar stärken wollen"])
        + '</div>', 2, N)

    wann = [("users", "Persönliches Treffen"), ("map-pin", "Offsite"), ("car", "Telefonat aus dem Auto"), ("message-circle", "Kurznachricht")]
    ueber = ["Strategische Themen und Geschäftsmodellfragen", "Führungsfragen", "Betrachtung komplexer Situationen aus unterschiedlichen Perspektiven",
             "Abwägen von Lösungswegen und Vorgehensweisen", "Positionierung gegenüber Vorstand und anderen Bereichen", "Umgang mit dem Aufsichtsrat",
             "Steuerung von Konzernunternehmen", "Konzeption von Kommunikation nach außen", "… und vieles mehr"]
    s3 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Themen")
        + '<h2>So flexibel, wie es <span class="hl">für Dich passt.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Der Alltag hält sich oftmals nicht an planbare Termine. Ich richte mich immer danach, wie es für Dich als Führungskraft passt. '
          'Oftmals ist ein kurzer Austausch genauso hilfreich wie ein strukturierter Termin – bei Bedarf auch zu Randzeiten.</p>'
        + '<p class="kicker" style="margin-top:8mm">Wann wir sprechen</p>'
        + '<div class="wann">' + "".join(f'<div>{ico(i)}<b>{t}</b></div>' for i, t in wann) + '</div>'
        + '<p class="kicker" style="margin-top:8mm">Worüber wir sprechen</p>'
        + '<ul class="ueber">' + "".join(f"<li>{x}</li>" for x in ueber) + '</ul>'
        + '</div><div class="band band--schwarz wachsen turbo" style="margin-top:10mm;padding-top:10mm">' + kicker("Mehr als nur Sparring")
        + '<h2>Umsetzungsturbo!</h2>'
        + '<p class="lead">In unseren Gesprächen entstehen oft Ideen, die Du am liebsten sofort vorantreiben würdest. '
          'Dabei fehlt intern meist immer einer der drei Erfolgsbausteine:</p>'
        + '<div class="dunkel kasten" style="padding:0;background:transparent">'
        + '<div class="punkte" style="margin-top:6mm;grid-template-columns:repeat(3,1fr)">' + "".join(
            f'<div>{ico(i)}<h3>{t}</h3></div>' for i, t in [("user-round", "Jemand, der das Thema versteht"),
                                                             ("timer", "Die Kapazität für die Umsetzung"), ("wrench", "Die Skills für die Umsetzung")]) + '</div>'
        + '</div><div class="schluss"><p>Genau hier finde ich oftmals direkt eine Lösung, wie es schnell gehen kann. Ganz ohne weiteres Briefing, '
          'denn wir kennen die Hintergründe bereits aus dem Sparring.</p>'
          '<p><b>Wir liefern das Ergebnis:</b> Egal, ob wir es komplett konzipieren und erstellen oder Dein Team direkt mit einbinden.</p></div>'
        + '</div>', 3, N, hell_fuss=True)

    s4 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Bereit für ein offenes Sparring <span class="hl">auf Augenhöhe?</span></h2>'
        + '<p class="lead">Sag mir, worüber Du offen sprechen willst – wir finden das Format, das in Deinen Alltag passt.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, und was steht gerade an? Eine Mail, ein Anruf oder eine Kurznachricht reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Rhythmus, Umfang und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr"]) + kontaktdaten() + '</div></div>', 4, N)
    return dokument(TITEL, [s1, s2, s3, s4], extra_css=CSS)
