#!/usr/bin/env python3
"""Eine Abnahme fuer alle PDFs. Vor jeder Meldung "fertig" auszufuehren.

Hintergrund: Wiederholt sind Fehler durchgerutscht, die beim Ansehen eines
Screenshots nicht auffallen - ein Versatz von vier Millimetern, ein falscher
Schriftschnitt, ein Wasserzeichen ohne Kontrast. Augenmass reicht dafuer nicht.
Jede Korrektur, die Daniel melden musste, ist hier als Pruefung hinterlegt,
damit derselbe Fehler nicht zweimal passieren kann.

Geprueft wird:
  1 Ueberlauf          keine Seite laeuft ueber den Satzspiegel hinaus
  2 Layoutregeln       eine getoente Flaeche je Seite, kein reiner Fliesstext,
                       keine halb leeren Seiten            (regeln.py)
  3 Fluchten           gleichartige Elemente nebeneinander beginnen auf
                       derselben Hoehe                     (fluchten.py)
  4 Typografie         Corporate Design: Headline in Medium (600),
                       Highlight-Wort in Bold (700), Fliesstext in Light (300)
  5 Seitenzahlen       nur zwischen Deckblatt und Schlussseite

Aufruf:  python3 werkzeuge/pdf_pruefen.py [--bauen]
         --bauen erzeugt die HTML-Quellen vorher neu.
"""
import glob, os, re, subprocess, sys

HERE = os.path.dirname(os.path.abspath(__file__))
SEITEN = os.path.join(HERE, "pdf-seiten")
VORLAGE = os.path.join(HERE, "pdf-vorlage")
BUILD = os.path.join(SEITEN, "_build")
sys.path.insert(0, VORLAGE)


def _quellen():
    return sorted(glob.glob(os.path.join(BUILD, "_pdfsrc_*.html")))


def typografie():
    """Manual 01: Headline Lora Medium, Highlight-Wort Bold."""
    fehler = []
    for f in _quellen():
        css = open(f, encoding="utf-8").read().split("<style>")[1].split("</style>")[0]
        def gewicht(sel):
            """Nur INNERHALB der Regel suchen - ein fester Zeichenabstand
            rutscht sonst in die naechste Regel und meldet deren Wert."""
            i = css.find(sel)
            if i < 0:
                return 0
            ende = css.find("}", i)
            m = re.search(r"font-weight:\s*(\d+)", css[i:ende])
            return int(m.group(1)) if m else 0
        h, hl = gewicht("h2 {"), gewicht(".hl {")
        koerper, fett = gewicht("body {"), gewicht("b, strong {")
        if h != 600 or hl != 700:
            fehler.append(f"{os.path.basename(f)}: Headline {h}, Highlight {hl} "
                          f"(erwartet 600 / 700)")
        # Manual 01: Fliesstext in Light. b/strong braucht ein eigenes Gewicht -
        # "bolder" wuerde relativ zu 300 nur 400 ergeben.
        if koerper != 300 or fett != 600:
            fehler.append(f"{os.path.basename(f)}: Fliesstext {koerper}, b/strong {fett} "
                          f"(erwartet 300 / 600)")
    return fehler


def reihenfolge():
    """Nummerierte Abfolgen duerfen nicht zurueckspringen.

    Zweimal ist mir derselbe Fehler passiert: In "Komplexe Themen" stand das
    Zwischenergebnis nach Stufe 3 statt nach Stufe 2, im Seminar-PDF folgte auf
    "Baustein 01 und 02" eine Seite ueber Baustein 01. Beim Ansehen faellt so
    etwas kaum auf, im Text ist es eindeutig messbar.
    """
    muster = re.compile(r"(Baustein|Lösung|Format|Modul|Schritt|Vortrag|Stufe)\s*(?:0)?(\d)")
    fehler = []
    for f in _quellen():
        roh = open(f, encoding="utf-8").read()
        text = re.sub(r"<[^>]+>", " ", roh)
        letzte = {}
        for m in muster.finditer(text):
            wort, nr = m.group(1), int(m.group(2))
            vor = letzte.get(wort)
            if nr == 1:
                # Ein Deckblatt listet oft alle Stufen, danach beginnt die
                # Abfolge legitim wieder bei 1. Das ist ein Neustart, kein Bruch.
                letzte[wort] = 1
                continue
            if vor is not None and nr < vor:
                fehler.append(f"{os.path.basename(f)}: {wort} {vor} -> {wort} {nr} "
                              f"(Abfolge springt zurueck)")
            letzte[wort] = nr
    # je Datei und Wort nur einmal melden
    gesehen, knapp = set(), []
    for z in fehler:
        s = z.split("(")[0]
        if s not in gesehen:
            gesehen.add(s); knapp.append(z)
    return knapp


def seitenzahlen():
    """Nur zwischen Deckblatt und Schlussseite."""
    fehler = []
    for f in _quellen():
        t = open(f, encoding="utf-8").read()
        seiten = len(re.findall(r'<section class="page', t))
        zahlen = len(re.findall(r'class="page-no"', t))
        if zahlen != max(0, seiten - 2):
            fehler.append(f"{os.path.basename(f)}: {zahlen} Seitenzahlen bei "
                          f"{seiten} Seiten (erwartet {max(0, seiten - 2)})")
    return fehler


def main(bauen=False):
    if bauen:
        subprocess.run([sys.executable, "build.py"], cwd=SEITEN, capture_output=True)

    from messen import measure
    import regeln, fluchten

    befunde = {}

    ueber = []
    for f in _quellen():
        for r in measure(f):
            if r["frei_mm"] < 0:
                ueber.append(f"{os.path.basename(f)} S{r['page']}: {r['frei_mm']} mm")
    befunde["Ueberlauf"] = ueber

    regel = []
    for f in _quellen():
        for seite, r, txt in regeln.pruefen(f):
            regel.append(f"{os.path.basename(f)} S{seite}: {r} {txt}")
    befunde["Layoutregeln"] = regel

    flu = []
    for f in _quellen():
        for x in fluchten.pruefen(f):
            flu.append(f"{os.path.basename(f)} S{x['page']}: {x['gruppe']} "
                       f"Kind {x['kind']}, {x['versatz']} mm Versatz")
    befunde["Fluchten"] = flu

    befunde["Typografie"] = typografie()
    befunde["Reihenfolge"] = reihenfolge()
    befunde["Seitenzahlen"] = seitenzahlen()

    gesamt = 0
    for name, liste in befunde.items():
        zeichen = "ok  " if not liste else "FEHL"
        print(f"[{zeichen}] {name:14s} {len(liste)} Befund(e)")
        for z in liste[:12]:
            print(f"        {z}")
        if len(liste) > 12:
            print(f"        ... und {len(liste) - 12} weitere")
        gesamt += len(liste)

    print()
    print(f"{len(_quellen())} PDFs geprueft - "
          + ("ABNAHME BESTANDEN" if gesamt == 0 else f"{gesamt} Befund(e), NICHT abgenommen"))
    return 1 if gesamt else 0


if __name__ == "__main__":
    sys.exit(main(bauen="--bauen" in sys.argv))
