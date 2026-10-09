"""Versuch „alles Schwarz-Weiß-Gelb“ (Daniel, Runde 37).

Statt jede Regel einzeln umzuschreiben, werden die Sekundärfarben (Magenta, Cyan, Lila samt ihrer dunklen Töne)
in den Stylesheets und in den Seiten nach einer festen Regel ersetzt:
  · Flächen (background, border, box-shadow, outline, Variablen) → Gelb #fff400
  · Schrift, Linien, Icons (color, stroke, fill)                    → Schwarz #1a1817
  · Wird in einer Regel eine Fläche gelb, wird weiße Schrift derselben Regel schwarz.
  · Weiße Schrift auf den früheren Farbstreifen (Regeln für .e2-alt--magenta/cyan/violett) → schwarz.
Die Originaldateien bleiben unverändert; die umgefärbten Stylesheets liegen in assets/projekte/empiria-2/sg/.
"""
import re

GELB, SCHWARZ = "#fff400", "#1a1817"
HEX = ["#c51f5d", "#0b9fbd", "#8613a1", "#7a1339", "#086a80", "#5c0d70", "#0a8aa4", "#c51f5e", "#c51f6a",
       "#e2457f", "#d0306d", "#a3164b", "#8e1543", "#c25be0", "#591064", "#0a3b44", "#06333b", "#059669", "#037a54"]   # hellere/dunklere Töne
_HEX = re.compile("|".join(HEX), re.I)
_RGB = re.compile(r"rgba?\(\s*(197\s*,\s*31\s*,\s*93|11\s*,\s*159\s*,\s*189|134\s*,\s*19\s*,\s*161)\s*(,\s*[\d.]+)?\s*\)")
_VAR = re.compile(r"var\(--(?:bf|e2-akzent|e2-magenta|hl)(?![-\w])(?:[^()]|\([^()]*\))*\)")   # Klammern ausgeglichen
_WEISS = re.compile(r"#fff\b|#ffffff\b|\bwhite\b", re.I)
DUNKEL = re.compile(r"pdf-dl")          # Schrift auf Schwarz: Akzent wird Gelb statt Schwarz
SCHRIFT = {"color", "stroke", "fill", "caret-color", "-webkit-text-fill-color", "text-decoration-color"}
STREIFEN = re.compile(r"e2-alt--(magenta|cyan|violett)|produkt-grid|tools-row|e2-gg|section--grey|featured|vorschau-split-card|pa-pc|vergleich-rocket|produkt-vorschau")


def _flaeche(v):
    v = _HEX.sub(GELB, v)
    return _RGB.sub(lambda m: f"rgba(255,244,0{m.group(2) or ''})" if m.group(2) else GELB, v)


def _schrift(v):
    return _VAR.sub(SCHWARZ, _RGB.sub(SCHWARZ, _HEX.sub(SCHWARZ, v)))


def _regel(sel, body):
    teile = re.split(r"(;)", body)
    decl = []
    gelb_flaeche = False
    for t in teile:
        m = re.match(r"(\s*)([-\w]+)(\s*:\s*)(.*)$", t, re.S)
        if not m:
            decl.append(t); continue
        ws, prop, sep, val = m.groups()
        p = prop.lower()
        if p == "--bf-text":
            val = _WEISS.sub(SCHWARZ, val)
        elif p.startswith("--"):
            val = _flaeche(val)
        elif p in SCHRIFT:
            val = _flaeche(val) if DUNKEL.search(sel) else _schrift(val)
        elif re.search(r"li::(before|after)|-foot::before|pa-check::before", sel) and p.startswith("background") and not re.search(r"--top|kasten|featured", sel):
            neu = _schrift(val)   # Aufzählungspunkte auf Weiß/Hellgrau: schwarz statt gelb
            val = neu
        else:
            neu = _flaeche(val)
            if p.startswith("background") and (neu != val or _VAR.search(val)):
                gelb_flaeche = True
            val = neu
        decl.append(ws + prop + sep + val)
    if gelb_flaeche or (STREIFEN.search(sel) and not re.search(r"btn|knopf|e2-s2-kasten|__mehr", sel)):   # schwarze Knöpfe/Kästen behalten weiße Schrift
        decl = [re.sub(r"(^\s*(?:color|stroke|border(?:-top|-bottom|-left|-right)?(?:-color)?)\s*:\s*)([^;]*)",
                       lambda m: m.group(1) + re.sub(r"rgba\(\s*255\s*,\s*255\s*,\s*255", "rgba(26,24,23", _WEISS.sub(SCHWARZ, m.group(2))) if "color" in m.group(1) or "stroke" in m.group(1) or "rgba" in m.group(2) else m.group(0), d, flags=re.I) for d in decl]
        if re.search(r"::(before|after)", sel):   # Striche/Punkte auf gelber Fläche
            decl = [re.sub(r"(^\s*background(?:-color)?\s*:\s*)([^;]*)", lambda m: m.group(1) + _WEISS.sub(SCHWARZ, m.group(2)), d, flags=re.I) for d in decl]
    return "".join(decl)


def css(text):
    """Innerste Regeln { … } umfärben (auch in @media)."""
    return re.sub(r"([^{}]*)\{([^{}]*)\}", lambda m: m.group(1) + "{" + _regel(m.group(1), m.group(2)) + "}", text)


def html(text):
    """<style>-Blöcke wie CSS, style-Attribute nach Eigenschaft, übrige Farbangaben (SVG fill/stroke) → Schwarz.
    Das Entwicklungsmenü bleibt unberührt."""
    def seite(t):
        t = re.sub(r"(<style[^>]*>)(.*?)(</style>)", lambda m: m.group(1) + css(m.group(2)) + m.group(3), t, flags=re.S)
        t = re.sub(r'style="([^"]*)"', lambda m: 'style="' + _regel("", m.group(1)) + '"', t)
        return re.sub(r'((?:fill|stroke|color|stop-color)=")([^"]*)(")', lambda m: m.group(1) + _schrift(m.group(2)) + m.group(3), t)
    teile = re.split(r"(<!-- ENTWICKLUNG:START -->.*?<!-- ENTWICKLUNG:END -->)", text, flags=re.S)
    return "".join(t if t.startswith("<!-- ENTWICKLUNG:START") else seite(t) for t in teile)
