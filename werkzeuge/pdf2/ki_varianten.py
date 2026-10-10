"""Varianten B zum Muster „KI zum Anfassen“ – zum Vergleich mit A (Daniel, 10.10.2026)."""
import lib
from lib import (kopfbild, seite, kopf, kicker, punkte, posts, team, kontaktdaten, dokument, ico)

T = "KI zum Anfassen"
FAKTEN = [("Format", "½ bis 2 Tage"), ("Tools", "ChatGPT, Claude, Gemini &amp; mehr"), ("Fokus", "Echte Usecases"), ("Investition", "ab 2.500 €")]
TOOLS = [("chatgpt", "ChatGPT"), ("claude", "Claude"), ("perplexity", "Perplexity"), ("gemini", "Gemini"), ("notebooklm", "NotebookLM"), ("nanobanana", "Nano Banana")]


def titel_b():
    f = "".join(f'<div><span>{l}</span><b>{v}</b></div>' for l, v in FAKTEN)
    return seite('<div class="titel-b"><div class="oben"><img class="logo" src="assets/empiria-logo.svg" alt="empiria">' + kicker(T)
                 + '<h1>Deine KI.<br><span class="hl" style="background:#1a1817;color:#fff">Zum Anfassen.</span><br>Volle Wirkung.</h1>'
                 + '<p class="sub">Über KI wird geredet – oft von Menschen, die sie selbst noch nie genutzt haben. Wir gehen direkt in die Anwendung: '
                   'verschiedene KI-Tools, echte Fälle aus Eurem Alltag, Erkenntnisse, die sofort etwas bringen.</p></div>'
                 + f'<div class="unten"><div class="bild">{kopfbild(T)}</div>'
                 + f'<div class="fakten" style="grid-template-columns:repeat(4,1fr)">{f}</div></div></div>')


def seite2_b(nr):
    return seite(kopf(T)
        + '<div class="band band--gelb" style="margin-top:10mm;padding-top:14mm;padding-bottom:14mm">' + kicker("Das bekommst Du")
        + '<h2>Anwendung statt Vortrag.</h2><p class="lead">Wir reden nicht über KI – wir nutzen sie, gemeinsam mit Dir und Deinem Team.</p>'
        + punkte([("zap", "Direkt in die Anwendung", "Kein weiterer Arbeitskreis, keine Theorie – wir starten sofort, mit direktem Mehrwert für Dein Unternehmen."),
                  ("layers", "Tools im Vergleich", "Mehrere KI-Tools gleichzeitig – live erleben, wie unterschiedlich sie denken und welche Ergebnisse sie liefern."),
                  ("target", "Echte Usecases", "Anwendungsfälle, die für Versicherer wirklich relevant sind – mit direkt verwertbaren Erkenntnissen.")])
        + '</div><div class="rand" style="padding-top:16mm">' + kicker("Die Werkzeuge")
        + '<h2>Mehrere Tools im direkten Vergleich.</h2><p class="lead">Wir zeigen an Euren Fällen, wie unterschiedlich die Tools denken und liefern.</p>'
        + '<div class="logos" style="grid-template-columns:repeat(3,1fr);row-gap:12mm;margin-top:14mm">' + "".join(
            f'<div><img src="assets/tools/{d}-magenta.png" alt="" style="height:15mm"><b style="font-size:9.5pt">{t}</b></div>' for d, t in TOOLS)
        + '</div></div>', nr, 5)


def formate_tabelle(nr, kasten=""):
    cols = [("½ Tag", "KI-Einstieg", "2.500 €", False), ("1 Tag", "KI-Sprint", "3.900 €", True), ("2 Tage", "KI-Deep-Dive", "7.350 €", False)]
    head = '<th></th>' + "".join(f'<th class="{"mitte" if m else ""}">{"<em>Meistgewählt</em><br>" if m else ""}<small>{d}</small><b>{n}</b></th>' for d, n, _, m in cols)
    def zeile(label, werte, cls=""):
        return f'<tr><td class="zeile">{label}</td>' + "".join(f'<td class="{"mitte " if cols[i][3] else ""}{cls}">{w}</td>' for i, w in enumerate(werte)) + '</tr>'
    ja, nein = '<span class="ja"></span>', '<span class="nein">–</span>'
    body = (zeile("Investition", [c[2] for c in cols], "preis")
            + zeile("Ziel", ["KI-Tools ausprobieren, erste Erfahrungen sammeln", "Tools kennenlernen, kompakte Fragestellung bearbeiten", "Direkter Einstieg in einen konkreten Usecase"])
            + zeile("Tools kennenlernen", [ja, ja, ja])
            + zeile("Eigene Fragestellung", [nein, "kompakt", "konkreter Usecase"])
            + zeile("Abschlussbesprechung", [nein, ja, ja])
            + zeile("Geeignet für", ["Ohne Vorkenntnisse", "Kompakter Anwendungsfall", "Konkretes Projekt"]))
    return seite(kopf(T) + '<div class="rand" style="padding-top:16mm">' + kicker("Formate")
        + '<h2>Drei Formate für jeden Anspruch.</h2><p class="lead">Vom ersten Ausprobieren bis zur konkreten Fallbearbeitung – wähle die Tiefe, die zu Deinem Team passt.</p>'
        + f'<table class="tabelle"><thead><tr>{head}</tr></thead><tbody>{body}</tbody></table>'
        + ('<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen.</p>' + kasten if kasten else
           '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen – inklusive Vorbereitung und Dokumentation der Ergebnisse.</p>')
        + '</div>', nr, 5)


def formate_ohne_kasten(nr):
    return seite(kopf(T) + '<div class="rand" style="padding-top:20mm">' + kicker("Formate")
        + '<h2>Drei Formate für jeden Anspruch.</h2><p class="lead">Vom ersten Ausprobieren bis zur konkreten Fallbearbeitung – wähle die Tiefe, die zu Deinem Team passt.</p>'
        + posts([
            dict(kopf="Ohne Vorkenntnisse startklar", label="½ Tag", name="KI-Einstieg", preis="2.500 €", ico="sparkles",
                 text="KI-Tools ausprobieren und erste eigene Erfahrungen sammeln.", liste=["Ausprobieren verschiedener KI-Tools", "Erste eigene Erfahrungen sammeln"]),
            dict(kopf="Kompakter Fall", badge="Meistgewählt", top=True, label="1 Tag", name="KI-Sprint", preis="3.900 €", ico="zap",
                 text="Tools kennenlernen und eine kompakte Fragestellung bearbeiten.",
                 liste=["Kennenlernen verschiedener Tools", "Bearbeitung einer kompakten Fragestellung des Unternehmens", "Abschlussbesprechung zum weiteren Vorgehen"]),
            dict(kopf="Konkreter Usecase", label="2 Tage", name="KI-Deep-Dive", preis="7.350 €", ico="target",
                 text="Direkter Einstieg in einen konkreten Usecase Eures Unternehmens.",
                 liste=["Kennenlernen der Tools", "Bearbeitung eines konkreten Usecases des Unternehmens", "Abschlussbesprechung zum weiteren Vorgehen"]),
        ]).replace('class="posts"', 'class="posts posts--hoch"')
        + '<p class="notiz">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen – inklusive Vorbereitung und Dokumentation der Ergebnisse.</p></div>', nr, 5)


def beispiele_liste(nr):
    faelle = [
        ("Sparring zu Zielgruppen", "Produktentwicklung und Marketing nutzen KI-Tools als Sparringspartner für Zielgruppenprofile im Versicherungsvertrieb – inklusive passender Ansprache. Bewusst auch mit ungewöhnlichen Zielgruppen, um die Grenzen der Tools auszuloten."),
        ("Generierung von Produktideen", "Der Auftrag kam vom Vorstand: Es fehlte an neuen Ideen. Ziel war nicht die Umsetzbarkeit, sondern eingefahrene Denkmuster aufzubrechen und die Diskussion im Team neu in Gang zu bringen."),
        ("Ideen für Marketingkampagnen", "Ein Marketingbereich hat auf eigenen Geräten und ohne Unternehmensdaten ausprobiert, was KI heute wirklich kann – mit konkreten Impulsen für die Arbeit im eigenen Haus."),
        ("Content für Social Media", "Ein Social-Media-Team hat Text und Grafik live mit verschiedenen Tools erstellt. Am Ende stand eine Entscheidungsvorlage, welche Tools es im Alltag wirklich braucht."),
        ("HTML-Seiten für Homepage &amp; Intranet", "Wie sich Seiten mit KI am geschicktesten entwickeln lassen – inklusive Automatisierungen und Agents. HTML-Seiten sind PDFs überlegen: leichter weiterzuentwickeln und auswertbar."),
        ("Geschäftsmodell hinterfragen", "Vorstand und Strategieeinheit wollten wissen, wie sich das eigene Geschäftsmodell mit KI hinterfragen lässt: Prompts, die tragen, Recherche, Dokumentenanalyse und eigene Studien."),
    ]
    zeilen = "".join(f'<div><h3>{t}</h3><p>{p}</p></div>' for t, p in faelle)
    return seite(kopf(T) + '<div class="band wachsen" style="padding-top:16mm">' + kicker("Beispiele")
        + '<h2>Konkrete Use Cases aus der Praxis.</h2>'
        + f'<div class="liste">{zeilen}</div>'
        + '<div class="kasten" style="margin-top:7mm"><div class="zwei"><div><p class="label">Sonderthema</p><h3>Persönliche KI-Nutzung für Führungskräfte im Alltag</h3></div>'
        + '<p>Wie Du als Führungskraft KI im Alltag schnell und klug nutzt – welche Tools sich wofür eignen und welche Tipps wirklich weiterhelfen, ganz ohne Unternehmensdaten preiszugeben.</p></div></div>'
        + '</div>', nr, 5, klasse="seite--hell")


def schluss_gelb(nr):
    return seite(kopf(T) + '<div class="band wachsen mitte" style="background:transparent">' + kicker("Jetzt loslegen")
        + '<h1 style="font-size:34pt">Bereit, KI<br><span class="hl" style="background:#1a1817;color:#fff">wirklich anzufassen?</span></h1>'
        + '<p class="lead" style="max-width:140mm">Sag uns, welche Fragestellung bei Euch ansteht und wer dabei sein soll – wir melden uns zeitnah mit einem konkreten Vorschlag.</p>'
        + '<div class="zwei" style="margin-top:16mm">' + team(["daniel", "noah_ki"]) + kontaktdaten() + '</div></div>', nr, 5, klasse="seite--gelb")


def bauen_b():
    seiten = [titel_b(), seite2_b(2), formate_tabelle(3), formate_ohne_kasten(3), beispiele_liste(4), schluss_gelb(5)]
    return dokument("Varianten B – KI zum Anfassen", seiten)


def bauen_kopffuss():
    import ki_zum_anfassen
    return ki_zum_anfassen.bauen()
