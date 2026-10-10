"""PDF „Komplexe Themen strukturieren & kommunizieren“ – im Muster „KI zum Anfassen“ (10.10.2026)."""
from lib import (check, titelseite, seite, kopf, kicker, punkte, zeitstrahl, team, kontaktdaten, dokument)

TITEL = "Komplexe Themen strukturieren & kommunizieren – empiria"
T = "Komplexe Themen"
N = 6


def zeichen(name):
    """Großes, gefülltes Themen-Zeichen der Homepage (e2_bauen.FORM / THEMEN_ZEICHEN), schwarz."""
    import e2_bauen
    vb = "2.83 31.08 226.78 170.29" if name == "forward" else "2.83 2.83 226.78 226.78"
    return f'<svg class="zeichen" viewBox="{vb}" aria-hidden="true" fill="#1a1817" color="#1a1817">{e2_bauen.FORM[name]}</svg>'


CSS = """
h2, h3, .lead, .punkte p, .zs p, .liste p, .kasten p, .sub, .text { text-wrap: pretty; }
.titel .bild svg.zeichen { width: 76mm; }
.zs--gleich h3 { min-height: 2.4em; }
.zitate { display: grid; grid-template-columns: repeat(3, 1fr); gap: 8mm; margin-top: 5mm; }
.zitate > div { border-top: 1.6px solid #1a1817; padding-top: 4mm; font-family: 'Lora', Georgia, serif; font-weight: 700; font-size: 12.5pt; line-height: 1.25; }
.label-s { font-size: 7pt; font-weight: 700; letter-spacing: .16em; text-transform: uppercase; margin-top: 9mm; }
.text { font-size: 9.6pt; line-height: 1.6; margin-top: 7mm; max-width: 150mm; }
.text + .text { margin-top: 3mm; }
.satz { font-size: 9.6pt; line-height: 1.6; margin-top: 9mm; max-width: 140mm; }
.anlaesse { display: grid; grid-template-columns: repeat(2, 1fr); gap: 0 9mm; margin-top: 5mm; }
.anlaesse span { position: relative; padding: 4mm 0 4mm 6mm; border-bottom: 1px solid rgba(255,255,255,.22); font-family: 'Lora', Georgia, serif; font-size: 13pt; font-weight: 700; color: #fff; }
.anlaesse span::before { content: ""; position: absolute; left: 0; top: 6.4mm; width: 1.6mm; height: 1.6mm; border-radius: 50%; background: #fff400; }
.liste .unter { display: block; font-family: 'Poppins', Arial, sans-serif; font-size: 6.8pt; font-weight: 700; letter-spacing: .14em; text-transform: uppercase; margin-bottom: 1.6mm; }
.schluss .zwei { grid-template-columns: 99mm 1fr; gap: 8mm; }
.schluss .team { gap: 3mm; }
.schluss .person { width: 31mm; }
.schluss .person img { width: 24mm; height: 24mm; }
"""


def bauen():
    s1 = seite(titelseite(
        "Strategiehandwerk", 'Komplexe Themen strukturieren &amp; <span class="hl">kommunizieren.</span>',
        "Überall dort, wo Du als Führungskraft in der Versicherungsbranche Menschen von Deinem Thema überzeugen willst, sorgen wir dafür, dass Deine Botschaft wirkt.",
        zeichen("kreuz"),
        [("Gremien", "Vorstand &amp; Aufsichtsrat"), ("Intern", "Lenkungsausschuss &amp; Betriebsrat"),
         ("Vertrieb", "Tagung &amp; Kundenpitch"), ("Partner", "Rückversicherer &amp; Kooperationen")]))

    s2 = seite(
        kopf(T) + '<div class="rand" style="padding-top:14mm">' + kicker("Das Problem")
        + '<h2>Deine Präsentation ist vollständig. <span class="hl">Und wirkungslos.</span></h2>'
        + '<p class="label-s">Vor jedem wichtigen Termin derselbe Reflex</p>'
        + '<div class="zitate"><div>„Wir brauchen eine Präsentation.“</div><div>„Noch eine Folie.“</div><div>„Noch ein Punkt, ja nichts vergessen.“</div></div>'
        + '<p class="text">Am Ende funktioniert es trotzdem nicht – weil die ganze Energie in die Präsentation floss und nicht in die Taktik, mit der Du zum Erfolg kommst. '
          'Wer sitzt im Raum, wie gewinnst Du diese Entscheider, in welchen Schritten erreichst Du Dein Ziel? Mit diesen Fragen hat sich vorher kaum jemand beschäftigt.</p>'
        + '</div><div class="band band--gelb wachsen mitte" style="margin-top:12mm">' + kicker("Die Lösung")
        + '<h2>Die Präsentation ist nie das Ziel.<br>Das Ergebnis ist es.</h2>'
        + '<p class="lead" style="max-width:150mm">Wir sind keine Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber.</p>'
        + punkte([("target", "Klares Ziel", "Du weißt, welches Ergebnis Du im Raum brauchst – und wie Du es erreichst."),
                  ("message-square-text", "Starke Story", "Eine Business Story, die in der Welt Deines Gegenübers ankommt."),
                  ("presentation", "Wirksame Medien", "Unterlagen, die Deine Story tragen – statt 40 Folien Detailwissen.")])
        + '<p class="satz">Ein kurzes Briefing, ein paar gezielte Rückfragen, und Du kannst Dir sicher sein, dass es ab hier läuft.</p>'
        + '</div>', 2, N)

    s3 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("So gehen wir vor")
        + '<h2>Vier Schritte bis zum <span class="hl">Ergebnis.</span></h2>'
        + '<p class="lead">Erst die Taktik, dann die Folien: Der Weg zum Ziel steht, bevor ein Medium entsteht.</p>'
        + zeitstrahl([("01", "Ergebnis &amp; Zielgruppe", "Welches Ergebnis willst Du – und welche Bedeutung hat Dein Thema für die Zielgruppe?"),
                      ("02", "Business Story", "Warum? Wie? Was jetzt? – verdichtet zu einer klaren Kernbotschaft."),
                      ("03", "Medien", "Aus der Business Story entstehen Medien – gezielt für den jeweiligen Einsatz."),
                      ("04", "Taktisches Briefing", "Dein Vorgehen vor, während und nach dem Termin – bis zum Ergebnis.")]).replace('class="zs"', 'class="zs zs--gleich"')
        + '</div><div class="band band--hell wachsen" style="margin-top:12mm;padding-top:12mm">' + kicker("Schritt 02 · Die Business Story")
        + punkte([("compass", "Why", "Warum ist dieses Thema für die Zielgruppe wichtig?"),
                  ("route", "How", "Wie gehen wir dabei grundsätzlich vor?"),
                  ("signpost", "What next?", "Was muss als Nächstes gemacht werden?")]).replace('<div class="punkte" style="', '<div class="punkte" style="margin-top:6mm;')
        + '<div class="kasten" style="margin-top:auto;padding:7mm 8mm 8mm"><div class="zwei"><div><p class="label">Zwischenergebnis · nach Schritt 2</p>'
        + '<h3>Jetzt weißt Du schon, wie Du gewinnst.</h3></div>'
        + '<div><p style="margin-top:0">Der Weg zum Ziel und Deine Business Story sind geklärt, bevor überhaupt eine Folie entsteht. An dieser Stelle hast Du absolute Handlungsklarheit.</p>'
        + '<p><b style="color:#fff">Spoiler Alert:</b> Oftmals kommt etwas anderes heraus, als Du am Anfang gedacht hast.</p></div></div></div>'
        + '</div>', 3, N)

    medien = [
        ("Schritt 03 · Medium", "PowerPoint", "Eine Präsentation, die Deine Business Story trägt – klar strukturiert, professionell gestaltet und startklar für den nächsten großen Moment im Raum."),
        ("Schritt 03 · Medium", "Landingpage", "Eine klar auf Deine Zielgruppe zugeschnittene Seite, die genau ein zentrales Problem löst und Interessierte gezielt zum nächsten Schritt führt."),
        ("Schritt 03 · Medium", "Roll-up", "Der Gesamtzusammenhang aus Sicht Deiner Zielgruppe – in einem Bild visualisiert und dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist."),
        ("Schritt 04 · Briefing", "Framework", "Briefing auf Basis unseres Frameworks für den optimalen Ablauf eines Termins: Einstieg, Moderation und wie Du im Raum dafür sorgst, dass Du Dein Ergebnis bekommst."),
        ("Schritt 04 · Briefing", "Storyboard", "Ausführliches Storyboard mit Ablauf, Zeitplan, Sprechtext und Folienvorschau."),
    ]
    s4 = seite(
        kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Medien &amp; Taktik")
        + '<h2>Weit über die klassische PowerPoint hinaus.</h2>'
        + '<p class="lead">Aus der Business Story entstehen professionelle Medien – und Dein taktisches Vorgehen unmittelbar vor, während und nach dem Termin.</p>'
        + '<div class="liste">' + "".join(f'<div><h3><span class="unter">{u}</span>{t}</h3><p>{p}</p></div>' for u, t, p in medien) + '</div>'
        + '<div class="kasten" style="margin-top:8mm"><div class="zwei"><div><p class="label">Gut zu wissen</p><h3>Bessere KI-Folien allein sind kein Qualitätsmaßstab.</h3></div>'
        + '<p>Da reicht es nicht aus, dass die Folien Deiner KI besser aussehen als das, was Du selbst erstellen kannst – entscheidend sind Story und Taktik dahinter.</p></div></div>'
        + '</div>', 4, N, klasse="seite--hell")

    s5 = seite(
        kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Das Ergebnis")
        + '<h2>Eine Botschaft, die bleibt und Dein <span class="hl">Ziel erreicht.</span></h2>'
        + '<p class="lead" style="max-width:150mm">Du gehst bestens vorbereitet in entscheidende Termine. Deine Themen kommen dort an, wo sie ankommen müssen. '
          'Und die richtigen Entscheidungen werden getroffen – deshalb werden wir für wichtige Themen immer wieder gebucht.</p>'
        + kicker("Für wen das gemacht ist").replace('class="kicker"', 'class="kicker" style="margin-top:13mm"')
        + check(["Führungskräfte, die ein Thema im Vorstand durchbringen müssen", "Vorbereitung auf Aufsichtsrat und Projektlenkungsausschuss",
                 "Vertriebstagungen und Gespräche mit Kooperationspartnern", "Termine mit Rückversicherern und wichtige Kundenpitches"])
        + '</div><div class="band band--schwarz wachsen mitte" style="margin-top:14mm">' + kicker("Überall dort, wo es zählt")
        + '<h2 style="color:#fff">Wenn Du Menschen von Deinem Thema überzeugen willst.</h2>'
        + '<div class="anlaesse" style="margin-top:9mm">' + "".join(f'<span>{a}</span>' for a in
            ["Vorstand", "Aufsichtsrat", "Projektlenkungsausschuss", "Vertriebstagung", "Betriebsrat", "Kooperationspartner", "Rückversicherer", "Kundenpitch"]) + '</div>'
        + '</div>', 5, N, hell_fuss=True)

    s6 = seite(
        kopf(T) + '<div class="rand weiss" style="padding-top:16mm">' + kicker("Jetzt loslegen")
        + '<h2>Welches Thema muss als <span class="hl">Nächstes sitzen?</span></h2>'
        + '<p class="lead">Lass uns darüber sprechen, welche Themen Dich aktuell bewegen. Gemeinsam klären wir, ob und wie wir Dir weiterhelfen können.</p>'
        + zeitstrahl([("01", "Kurz schildern", "Worum geht es, wer ist beteiligt, bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
                      ("02", "Vorschlag erhalten", "Wir melden uns zeitnah mit Rückfragen und einem konkreten Vorschlag."),
                      ("03", "Festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht.")])
        + '</div><div class="band band--gelb wachsen mitte schluss" style="margin-top:14mm">' + kicker("Dein direkter Draht zu uns")
        + '<h2>Aus Gespräch wird Klarheit.</h2>'
        + '<div class="zwei" style="margin-top:9mm">' + team(["daniel", "kerstin_hr", "noah_pm"]) + kontaktdaten() + '</div></div>', 6, N)
    return dokument(TITEL, [s1, s2, s3, s4, s5, s6], extra_css=CSS)
