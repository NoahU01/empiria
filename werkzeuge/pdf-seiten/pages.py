from lib import *
import sketches as S

P = {}  # slug -> (theme, title, pages)

# ---------------------------------------------------------------- Strategie
P["strategie"] = ("strategie", "Strategie in den Alltag überführen – empiria", [
  cover("Strategiehandwerk", 'Strategie in den Alltag <span class="hl">überführen.</span>',
        "Deine Strategie ist da – aber was bedeutet sie für Deinen Verantwortungsbereich? Wir machen sie greifbar und wirksam im Alltag.",
        S.strategie(),
        [("Für wen", "Abteilungs- &amp; Bereichsleiter"), ("Fokus", "Rolle, Richtung, Handwerkszeug"), ("Begleitung", "Direkt mit Daniel"), ("Ergebnis", "Handlungsklarheit")]),
  page(
    sec("Das Problem", 'Strategisches Denken wird vorausgesetzt. Dir hat es aber <span class="hl">keiner beigebracht.</span>',
        "Du bist Abteilungs- oder Bereichsleiter, weil Du fachlich überzeugt hast. Strategisches Denken stand nie auf dem Lehrplan – trotzdem wird es ab dem ersten Tag vorausgesetzt.",
        "Was danach oft folgt, sind harte Gespräche mit dem eigenen Team. Hart, weil das Fundament fehlt: die klare Richtung, die eigene Rolle, das Handwerkszeug für den Alltag."),
    sec("Die Lösung", 'Rolle, Richtung, Handwerkszeug <span class="hl">für Deinen Bereich.</span>',
        "Wir arbeiten an drei Dingen, die Dir als Führungskraft Handlungsklarheit verschaffen:", style="margin-top:14mm"),
    cards([("user", "Rolle", "Wofür stehe ich und mein Bereich?"),
           ("eye", "Wahrnehmung", "Wie wollen wir wahrgenommen werden?"),
           ("route", "Weg", "Wie kommen wir dort hin?")], 3),
    statement(None, "Dazu gehört das praktische Handwerkszeug, mit dem Du als Führungskraft im Alltag <b>wirklich vorankommst.</b>", style="margin-top:10mm"),
  ),
  page(
    sec("Das Modell", 'Wofür Ihr steht, wohin Ihr wollt – <span class="hl">und wie Ihr hinkommt.</span>',
        "Dieselbe Struktur, mit der wir im Sparring arbeiten: vom Selbstverständnis des Bereichs über das Zielbild bis zu den Schritten, die im Alltag tatsächlich gegangen werden."),
    # Das Strategiemodell ist eine dichte Zeichnung (900x1060). In einer
    # 78-mm-Spalte sind seine Beschriftungen unlesbar, deshalb bekommt es die
    # volle Satzbreite und diese Seite fuer sich - eine getoente Flaeche, sonst
    # nichts.
    mdl("Unser Strategiemodell", "Vom Selbstverständnis bis in den Alltag Deines Bereichs.",
        S.load("strategiemodell"),
        "Am Anfang steht die Frage, wofür Dein Bereich steht – Euer <b>Selbstverständnis</b>. Dann der Blick nach vorn: Wie wollt Ihr wahrgenommen werden? Das ist die <b>Vision</b>. Der ehrliche Abgleich mit der Ausgangssituation zeigt, welche <b>Strategie</b> dorthin führt.",
        style="margin-top:8mm", cls="mdl--seite"),
  ),
  page(
    sec("Perspektivwechsel", 'Wie sieht die Homepage <span class="hl">Deiner Abteilung</span> aus?',
        "Ziemlich wahrscheinlich hast Du keine – die meisten haben keine. Also warum die Frage? Weil hier sofort klar wird, ob Du den Mehrwert Deines Bereichs sauber erklären kannst. Und wenn Du das nicht kannst, kann auch keiner in Deinem Team aktiv zu Deiner Strategie beitragen."),
    '<div class="medien-zwei">' +
      '<div><p class="lead">Fünf Fragen, die eine Homepage in Sekunden beantwortet – und die Dein Bereich genauso klar beantworten können muss. Wer sie nicht beantworten kann, überlässt die Wahrnehmung seines Bereichs dem Zufall.</p></div>' +
      '<div class="bm bm--schmal"><div class="bm-bar"><i></i><i></i><i></i><span>www.deine-abteilung-gmbh.de</span></div>' +
      "".join(f'<div class="bm-row"><span class="n">{i+1:02d}</span><span>{q}</span><em>?</em></div>' for i, q in enumerate([
          "Welche Zielgruppe sprechen wir an?", "Welches konkrete Problem lösen wir?", "Welcher Nutzen entsteht daraus?",
          "Was macht uns einzigartig?", "Wie läuft die Zusammenarbeit ab?"])) + '</div>' +
    '</div>',
    band("Gedankenexperiment", "Stell Dir vor, wir gründen morgen Deine Abteilung als GmbH.",
         "Und verkaufen Eure Dienstleistungen an Deinen aktuellen Arbeitgeber. Wie sähe die Homepage aus? Auf einmal versteht jeder im Team, wofür Dein Bereich da ist und wie das Zielbild aussieht. Dann kann auch jeder aktiv dazu beitragen – <b>und Du bestimmst die Wahrnehmung Deines Bereichs.</b>"),
  ),
  page(
    sec("Das Ergebnis", 'Du führst Dein Team, <span class="hl">statt es zu vertrösten.</span>',
        "Du kannst jederzeit erklären, wofür Dein Bereich steht und wie das Zielbild aussieht. Dein Team zieht mit, weil die Richtung geklärt ist – nicht, weil Du sie ständig neu erklären musst."),
    who("Für wen das gemacht ist", [
      "Abteilungs- und Bereichsleitungen, die fachlich überzeugt haben",
      "Führungskräfte, die ihrem Bereich Richtung geben müssen",
    ], style="margin-top:7mm"),
    stage("Zusammenarbeit", 'So arbeiten wir wirklich zusammen.', wm="forward", boden=True,
          inhalt=rows([("Direkter Draht, klare Worte", "Du arbeitest direkt mit mir – Daniel – zusammen. Die Verantwortung bleibt durchgehend bei mir. Und ich sage, was ich denke: ehrliches, direktes Feedback, um den Fokus zu schärfen."),
          ("Dein Einsatz entscheidet", "Eine Strategie lässt sich nicht von außen hineintragen. Wir unterstützen Dich maximal – die Umsetzung bleibt Deine Aufgabe. Plane dafür ein bis zwei Stunden pro Woche ein."),
          ("Dranbleiben, klar planen, umsetzen", "Regelmäßig abstimmen statt punktuell, klares Vorgehen, flexibel bei Engpässen – und ab einem gewissen Punkt zählt schnelle Umsetzung mehr als eine weitere Abstimmungsschleife.")], style="margin-top:2mm")),
    ),
  page(
    sec("Kontakt", 'Lass uns über <span class="hl">Deinen Bereich sprechen.</span>',
        "Kein Pitch, kein Angebot von der Stange: ein offenes Gespräch über Deinen Verantwortungsbereich – und was ihn gerade ausbremst."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel"])),
])

# ---------------------------------------------------------------- Komplexe Themen
P["komplexe-themen"] = ("strategie", "Komplexe Themen strukturieren & kommunizieren – empiria", [
  cover("Strategiehandwerk", 'Komplexe Themen strukturieren &amp; <span class="hl">kommunizieren.</span>',
        ["Überall dort, wo Du als Führungskraft in der Versicherungsbranche Menschen von Deinem Thema überzeugen willst, sorgen wir dafür, dass Deine Botschaft wirkt.", "<b>Klar. Fokussiert. Mit dem Ergebnis, das Du willst.</b>"],
        S.komplexe(),
        [("Gremien", "Vorstand &amp; Aufsichtsrat"), ("Intern", "Lenkungsausschuss &amp; Betriebsrat"), ("Vertrieb", "Tagung &amp; Kundenpitch"), ("Partner", "Rückversicherer &amp; Kooperationen")]),
  # Seitengrammatik: weisse Headline -> dunkler Kasten -> helles Band mit
  # Icon-Wasserzeichen. Jede Seite hat genau eine dominante Darstellung,
  # nie zwei Textsektionen uebereinander.
  page(
    sec("Das Problem", 'Deine Präsentation ist vollständig. <span class="hl">Und wirkungslos.</span>'),
    # Eine getoente Flaeche je Seite: der dunkle Dialogkasten liegt IM hellen
    # Band, so wie auf der Website - nicht daneben.
    stage("Die Fragen, die keiner stellt", "Damit hat sich vorher kaum jemand beschäftigt.",
          wm="kreuz", boden=True,
          inhalt=bubbles("Vor jedem wichtigen Termin derselbe Reflex",
                         ["„Wir brauchen eine Präsentation.“", "„Noch eine Folie.“", "„Noch ein Punkt, ja nichts vergessen.“"],
                         "Am Ende funktioniert es trotzdem nicht – weil die ganze Energie in die Präsentation floss und <b>nicht in die Taktik, mit der Du zum Erfolg kommst.</b>")
                 + raster([("01", "Wer sitzt<br>im Raum?", True),
                           ("02", "Wie gewinnst Du<br>diese Entscheider?"),
                           ("03", "In welchen Schritten<br>erreichst Du Dein Ziel?")], cols=3)),
  ),
  page(
    sec("Die Lösung", 'Die Präsentation ist nie das Ziel. <span class="hl">Das Ergebnis ist es.</span>',
        "Wir sind keine Medienagentur: Neben Kommunikation verstehen wir vor allem Strategie und das Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber. <b>Ein kurzes Briefing, ein paar gezielte Rückfragen, und Du kannst Dir sicher sein, dass es ab hier läuft.</b>"),
    stage("Unser Vorgehen", "In vier Schritten zum Ergebnis.", wm="kreuz", boden=True, inhalt=stations([
      (None, "Ergebnis &amp; Zielgruppe", "Wir strukturieren Dein Thema so, dass es in der Welt Deines Gesprächspartners ankommt. Die zentrale Frage: <b>Welche Bedeutung hat Dein Thema für die Zielgruppe?</b>"),
      (None, "Business Story", "Verdichtet zu einer klaren Kernbotschaft – unabhängig vom Medium: <b>Why</b> (warum ist das Thema für die Zielgruppe wichtig), <b>How</b> (wie gehen wir vor) und <b>What next</b> (was passiert als Nächstes)."),
      (None, "Medien", "Aus der Business Story entstehen professionelle Medien – gezielt für den jeweiligen Einsatz und weit über die klassische PowerPoint hinaus."),
      (None, "Taktisches Briefing", "Einstieg, Moderation und wie Du im Raum Dein Ergebnis bekommst – als Briefing oder als ausführliches Storyboard."),
    ])),
  ),
  page(
    sec("Medien", 'Aus der Business Story entstehen <span class="hl">professionelle Medien.</span>',
        "Gezielt für den jeweiligen Einsatz – und weit über die klassische PowerPoint hinaus. Welches Medium trägt, entscheidet der Termin, nicht die Gewohnheit."),
    # Dieselbe Schichtung wie auf der Landingpage: heller Grund, Icon als
    # Wasserzeichen, darauf der schwarze Kasten mit den echten Mockups.
    stage("Zwischenergebnis", "Jetzt weißt Du schon, wie Du gewinnst.",
          "Der Weg zum Ziel und Deine Business Story sind geklärt, bevor überhaupt eine Folie entsteht. <b>Spoiler Alert:</b> Oftmals kommt etwas anderes heraus, als Du am Anfang gedacht hast.",
          wm="kreuz", boden=True, inhalt=mocks([
        (S.load("medium-powerpoint"), "PowerPoint",
         "Eine Präsentation, die Deine Business Story trägt – klar strukturiert und startklar für den großen Moment im Raum."),
        (S.load("medium-landingpage"), "Landingpage",
         "Eine auf Deine Zielgruppe zugeschnittene Seite, die ein zentrales Problem löst und gezielt zum nächsten Schritt führt."),
        (S.load("medium-rollup"), "Roll-up",
         "Der Gesamtzusammenhang in einem Bild – dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist."),
    ])),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Führungskräfte, die ein Thema im Vorstand durchbringen müssen",
      "Vorbereitung auf Aufsichtsrat und Projektlenkungsausschuss",
      "Vertriebstagungen und Gespräche mit Kooperationspartnern",
      "Termine mit Rückversicherern und wichtige Kundenpitches",
    ], style="margin-top:11mm"),
    sec("Das Ergebnis", 'Eine Botschaft, die bleibt und Dein <span class="hl">Ziel erreicht.</span>',
        "Du gehst bestens vorbereitet in entscheidende Termine. Deine Themen kommen dort an, wo sie ankommen müssen.",
        "Und die richtigen Entscheidungen werden getroffen – <b>deshalb werden wir für wichtige Themen immer wieder gebucht.</b>"),
    cards([("target", "Klares Ziel", "Du weißt, welches Ergebnis Du im Raum brauchst – und wie Du es erreichst."),
           ("chat", "Starke Story", "Eine Business Story, die in der Welt Deines Gegenübers ankommt."),
           ("slides", "Wirksame Medien", "Unterlagen, die Deine Story tragen – statt 40 Folien Detailwissen.")], 3, style="margin-top:9mm"),
    contact_html=contact("Welches Thema muss als Nächstes sitzen?", ["daniel"])),
])

# ---------------------------------------------------------------- Innovation
P["innovation"] = ("strategie", "Innovation & Geschäftsmodell neu denken – empiria", [
  cover("Strategiehandwerk", 'Innovation &amp; Geschäftsmodell <span class="hl">neu denken.</span>',
        "Neue Ideen, neues Geschäftsmodell: Was davon hat in zehn Jahren noch Bestand? Wir hinterfragen und strukturieren es mit Dir.",
        S.innovation(),
        [("Zukunft", "Des Geschäftsmodells"), ("Partner", "Kooperationen &amp; Fusionen"), ("Invest", "Beteiligungen"), ("Angebot", "Neue Zusatzservices")]),
  page(
    sec("Das Problem", 'Du entwickelst weiter. Bevor die Grundfrage <span class="hl">geklärt ist.</span>',
        "Eine Idee für ein neues Geschäftsmodell oder Produkt entsteht, und sofort wird an Features, Prozessen und der Umsetzung gefeilt."),
    quotes(["Welches Problem hat der Kunde eigentlich?", "Wie löst Du es?", "Ist er überhaupt bereit, es zu lösen?"]),
    '<div class="sec" style="margin-top:6mm"><p class="lead">… diese Fragen bleiben unbeantwortet, während längst weitergebaut wird.</p></div>',
    sec("Die Lösung", 'Nichts davon ist <span class="hl">in Stein gemeißelt.</span>',
        "Wer sein Geschäftsmodell wirklich hinterfragt, stößt schnell an eine Grenze: Vieles gilt als gegeben, nur weil es schon immer so war – dabei ist es oft längst nicht mehr in Stein gemeißelt.",
        "Genau hier gehen wir mit Dir grundlegend ran, sei es für das gesamte Unternehmen oder für einzelne Bereiche.", style="margin-top:14mm"),
    # Das staerkste Element der Landingpage: die durchgestrichenen Denkmuster.
    stein("Gilt als gegeben",
          ["„Das war schon immer so.“", "„Das ist bei uns gesetzt.“", "„Das macht man in unserer Branche nicht.“"],
          "Und was, wenn nicht?"),
  ),
  page(
    sec("Einsatzmöglichkeiten", "Für das gesamte Unternehmen oder für einzelne Bereiche.",
        "Dies gilt für die Zukunft Eures Geschäftsmodells genauso wie für konkrete Fragen zu Kooperationen, Fusionen, Beteiligungen oder neuen Zusatzservices."),
    raster([("01", "Zukunft des<br>Geschäftsmodells", True), ("02", "Kooperationen"), ("03", "Fusionen"),
            ("04", "Beteiligungen"), ("05", "Neue<br>Zusatzservices")]),
    # Der Business Model Canvas war hier reine Dekoration ohne Aussage und
    # daher zu gross. Statt der Grafik der Gedanke, der die Seite traegt.
    sec("Unsere Methoden", "Methoden schaffen Erkenntnis. Nicht umgekehrt.",
        "Wir bringen eigene Methoden und Frameworks mit und helfen Dir, Dich von alten Denkmustern zu lösen.",
        "<b>Wir nutzen Methoden, um Erkenntnisse zu schaffen. Wir wenden sie nicht unreflektiert an.</b>",
        style="margin-top:12mm"),
    stage(None, None, wm="kreis", boden=True,
          inhalt=feat("Ein bewährter Ansatz", "Wir denken mit Dir so, als würdet Ihr Euer Thema morgen als eigenes Unternehmen neu gründen – ganz ohne Altlasten.", style="margin-top:0")),
    contact_html=None),
  page(
    who("Für wen das gemacht ist", [
      "Vorstände, die das Geschäftsmodell grundlegend hinterfragen wollen",
      "Bereiche vor Entscheidungen zu Kooperationen oder Fusionen",
      "Strategie und Business Development bei Beteiligungsfragen",
      "Teams, die neue Zusatzservices ernsthaft prüfen wollen",
    ], style="margin-top:11mm"),
    sec("Das Ergebnis", 'Du weißt, ob die Idee <span class="hl">trägt.</span>',
        "Du verstehst, worauf es in Eurem Geschäftsmodell wirklich ankommt – heute und in Zukunft. Ihr trefft Entscheidungen zu Innovation, Kooperationen oder Investitionen mit echter Substanz dahinter.",
        "<b>Und Ihr traut Euch, auch mal ganz neu zu denken.</b>"),
    cards([("search", "Grundfragen geklärt", "Kundenproblem, Lösung und Zahlungsbereitschaft – bevor weitergebaut wird."),
           ("puzzle", "Altlasten hinterfragt", "Was wirklich gesetzt ist und was nur so aussieht."),
           ("compass", "Klare Entscheidungen", "Mit Substanz für Innovation, Kooperation oder Investition.")], 3, style="margin-top:9mm"),
    contact_html=contact("Welche Idee soll auf den Prüfstand?", ["daniel"])),
])

# ---------------------------------------------------------------- KI zum Anfassen
P["ki-zum-anfassen"] = ("magenta", "KI zum Anfassen – empiria", [
  cover("KI zum Anfassen", 'Deine KI. <span class="hl">Zum Anfassen.</span> Volle Wirkung.',
        "Über KI wird geredet – oft von Menschen, die sie selbst noch nie genutzt haben. Wir gehen direkt in die Anwendung, testen verschiedene KI-Tools an echten Fällen aus Eurem Alltag und sorgen für Erkenntnisse, die sofort etwas bringen.",
        S.load("ki-zum-anfassen"),
        [("Format", "½ bis 2 Tage"), ("Tools", "ChatGPT, Claude, Gemini &amp; mehr"), ("Fokus", "Echte Usecases"), ("Investition", "ab 2.500 €")]),
  page(
    sec("Das bekommst Du", "Anwendung statt Vortrag.", "Wir reden nicht über KI – wir nutzen sie, gemeinsam mit Dir und Deinem Team."),
    cards([("bolt", "Direkt in die Anwendung", "Kein weiterer Arbeitskreis, keine Theorie – wir starten sofort, mit direktem Mehrwert."),
           ("layers", "Tools im Vergleich", "Mehrere KI-Tools gleichzeitig – live erleben, wie unterschiedlich sie denken und liefern."),
           ("target", "Echte Usecases", "Anwendungsfälle, die für Versicherer wirklich relevant sind – mit verwertbaren Erkenntnissen.")], 3),
    stage("Die Werkzeuge", "Mehrere Tools im direkten Vergleich.",
          "Wir arbeiten nicht mit einem Werkzeug, sondern zeigen an Euren Fällen, wie unterschiedlich die Tools denken und liefern.",
          wm="layers", boden=True,
          inhalt=chips(["ChatGPT", "Claude", "Perplexity", "Gemini", "NotebookLM", "Nano Banana"], style="margin-top:6mm")),
  ),
  # Eigene Seite fuer die Formate: die Preiskarten brauchen Luft, gedraengt
  # wirken sie billig.
  page(
    stage("Formate", 'Drei Formate für jeden Anspruch.',
          "Vom ersten Ausprobieren bis zum konkreten Usecase Eures Unternehmens – Du wählst die Tiefe.",
          wm="grid", boden=True, inhalt=
    # Aufbau und Texte 1:1 wie die Preiskarten auf ki-zum-anfassen.html:
    # Die Einordnung ("Kompakter Anwendungsfall") ist die Unterschrift zum Preis,
    # kein Listenpunkt.
    opts([dict(sub="½ Tag", name="KI-Einstieg", text="KI-Tools ausprobieren und erste eigene Erfahrungen sammeln.",
               price="2.500 €", pnote="Ohne Vorkenntnisse startklar.",
               list=["Ausprobieren verschiedener KI-Tools", "Erste eigene Erfahrungen sammeln"]),
          dict(sub="1 Tag", badge="Meistgewählt", name="KI-Sprint", text="Tools kennenlernen und eine kompakte Fragestellung bearbeiten.",
               price="3.900 €", pnote="Kompakter Anwendungsfall", feat=True,
               list=["Kennenlernen verschiedener Tools", "Bearbeitung einer kompakten Fragestellung des Unternehmens", "Abschlussbesprechung zum internen, weiteren Vorgehen"]),
          dict(sub="2 Tage", name="KI-Deep-Dive", text="Direkter Einstieg in einen konkreten Usecase Eures Unternehmens.",
               price="7.350 €", pnote="Konkreter Usecase",
               list=["Kennenlernen der Tools", "Bearbeitung eines konkreten Usecases des Unternehmens", "Abschlussbesprechung zum internen, weiteren Vorgehen"])])
    + '<p class="note">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe und zzgl. Spesen – inklusive Vorbereitung und Dokumentation der Ergebnisse.</p>'),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Vorstände, die im Haus mehr Tempo bei neuen Ideen wollen",
      "Grundsatz- und Strategieabteilungen mit Analysebedarf",
      "Marketing und Kommunikation für schnellere Inhalte",
      "Führungskräfte, die selbst schlagkräftiger werden wollen",
    ], style="margin-top:9mm"),
    stage("Beispiele", "Konkrete Use Cases aus der Praxis.",
          "Eine Auswahl der Themen, die wir mit unseren Kunden bereits umsetzen durften.",
          wm="bulb", boden=True,
          inhalt=cases([("Sparring zu Zielgruppen", "Produktentwicklung und Marketing nutzen KI als Sparringspartner für Zielgruppenprofile im Versicherungsvertrieb – inklusive passender Ansprache.", "team"),
           ("Generierung von Produktideen", "Auftrag vom Vorstand: eingefahrene Denkmuster aufbrechen, einen Impuls setzen und die Diskussion im Team neu in Gang bringen.", "bulb"),
           ("KI im Führungsalltag", "Wie Führungskräfte schnell und schlagkräftig mit KI agieren – Tools, Alltagstipps und Sparring, ganz ohne Unternehmensdetails.", "user"),
           ("Ideen für Marketingkampagnen", "Auf der grünen Wiese ausprobieren, was KI heute wirklich kann – mit konkreten Impulsen für die Arbeit im eigenen Haus.", "megaphone"),
           ("Content für Social Media", "Text und Grafik live erstellt – am Ende stand eine Entscheidungsvorlage, welche Tools das Team im Alltag wirklich braucht.", "phone"),
           ("HTML-Seiten für Homepage &amp; Intranet", "Wie sich Seiten mit KI am geschicktesten entwickeln lassen – inklusive Automatisierungen, Agents und Tool-Stärken.", "browser")])),
    ),
  page(
    sec("Kontakt", 'Bereit, KI <span class="hl">wirklich anzufassen?</span>',
        "Sag uns, welche Fragestellung bei Euch ansteht und wer dabei sein soll – wir schlagen Dir das passende Format vor."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "noah_ki"])),
])

# ---------------------------------------------------------------- Sprint Landingpage
P["sprint-landingpage"] = ("magenta", "Sprint Landingpage – empiria", [
  cover("Sprint Landingpage", 'Live in nur 48 Stunden. Sauber gebaut, <span class="hl">volle Wirkung.</span>',
        "Wenn es schnell gehen muss: In nur 48 Stunden entwickeln wir Deine fokussierte Landingpage – ohne Abstriche bei Qualität, Layout und Wirkung.",
        S.sprint(),
        [("Tempo", "Live in 48 Stunden"), ("Umfang", "Fix &amp; fokussiert"), ("Technik", "Mobile-First"), ("Investition", "15.850 €")]),
  page(
    # Umbruch fest gesetzt: sonst faellt das hervorgehobene "optimal." allein
    # in die zweite Zeile.
    sec("Erfolgsfaktor", 'So funktioniert Deine<br>Landingpage <span class="hl">optimal.</span>',
        "Eine Homepage ist oft ein Sammelsurium an Themen – zum Unternehmen, zum Team, zu Produkten. Besucher müssen sich zurechtfinden und selbst suchen, was sie wollen.",
        "Eine Landingpage funktioniert anders: Sie richtet sich an eine klar definierte Zielgruppe und löst genau ein zentrales Problem – mit vertrieblichem Ziel."),
    # Das Mockup von der Landingpage statt einer reinen Aufzaehlung.
    mdl("Hier bin ich richtig.", "Was eine Landingpage von einer Homepage unterscheidet.",
        S.load("sprint-lp-optimal"),
        figw="56mm",
        steps=[("01", "Ein Fokus", "Eine Zielgruppe, ein Problem, eine Lösung – keine Ablenkung durch andere Themen."),
               ("02", "Zugeschnitten", "Visualisierung, Ansprache und Argumente exakt auf diese Zielgruppe."),
               ("03", "Ein klares Ziel", "Nie alles erklären – der Fokus liegt auf dem nächsten Schritt: Kontaktdaten, Webinar-Anmeldung oder Download mit echtem Mehrwert.")]),
    sec("Das Versprechen", "Tempo ohne Kompromisse.", style="margin-top:9mm"),
    cards([("clock", "Schneller Start", "Kein monatelanger Prozess – wir starten in den Sprint, sobald der Rahmen steht."),
           ("grid", "Fokussierter Umfang", "Ein klar begrenztes Set an Inhalten und Elementen, damit der Sprint hält, was er verspricht."),
           ("check", "Ohne Kompromisse", "Trotz Tempo: sauber gebaut, mobil optimiert und technisch startklar.")], 3, style="margin-top:5mm"),
  ),
  page(
    sec("Ablauf", 'Drei Schritte zur <span class="hl">fertigen Landingpage.</span>', "So läuft der Sprint konkret ab – von der Vorbereitung bis zum Go-live."),
    stations([("2–3 Std. · online", "Onboarding", "Wir klären Zielgruppe, Problem und Ziel – damit der Sprint vom ersten Moment an sitzt."),
              ("2 Tage · Präsenz", "Sprint-Workshop", "<b>Tag 1:</b> Sparring &amp; parallele Entwicklung der Rohversion. <b>Tag 2:</b> Vorstellung, Feedback, Feinschliff &amp; Go-live."),
              ("Im Nachgang", "Review", "Kurzes Fazit: Hat alles gepasst, wie war das Feedback – und wo gibt es noch gezielten Anpassungsbedarf?")]),
    sec("Investition", "Ein Paket, ein Preis.", style="margin-top:11mm"),
    paket("Dein Leistungspaket",
          ["Konzeption, Text &amp; Design der Landingpage", "Umsetzung im Sprint-Workshop bei Dir vor Ort",
           "Feedbackrunde &amp; Feinschliff im Workshop", "Live-Schaltung direkt im Anschluss",
           "Review im Nachgang", "Durchgeführt von 2 Beraterinnen und Beratern"],
          "Investition", "15.850 €", "Ein Paket, ein Preis – ohne versteckte Zusatzkosten."),
    '<p class="note">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe sowie zzgl. Spesen (Anfahrt und zwei Übernachtungen für je zwei Personen).</p>',
  ),
  page(
    who("Für wen das gemacht ist", [
      "Bereiche mit kurzfristigem Vertriebspush, etwa im Endjahresgeschäft",
      "Teams vor Messe, Event oder Vertriebstagung",
      "Marketing, dem jemand ausgefallen ist und der Termin trotzdem steht",
      "Alle, die zeigen wollen, dass es auch schnell und sauber geht",
    ], style="margin-top:9mm"),
    sec("Anwendungsfälle", 'So setzen Unternehmen <span class="hl">den Sprint ein.</span>'),
    cases([("Dynamik im Kreativworkshop", "Direkt weitermachen, statt Ergebnisse im Nachgang untergehen zu lassen.", "bolt"),
           ("Auf den Vertrieb reagieren", "Marktchance nutzen oder kurzfristig einen Push setzen – etwa im Endjahresgeschäft.", "trend"),
           ("Eine Situation retten", "Messe, Event oder Produktlaunch steht an – und etwas wurde schlicht vergessen.", "shield"),
           ("Zum Wachrütteln", "Wenn Diskussionen sich ziehen: Der Sprint beweist, dass es schnell und professionell geht.", "spark"),
           ("Methodiktraining im Marketing", "Eine schlagkräftige Methodik kennenlernen und fürs eigene Team nutzbar machen.", "tool"),
           ("Kunden &amp; Partner begeistern", "In kürzester Zeit eine einsetzbare Lösung – etwa für Makler, Bank- oder Kooperationspartner.", "handshake")]),
    contact_html=contact("Deine Landingpage in 48 Stunden?", ["daniel", "noah_pm"])),
])

P["workshop-moderation"] = ("magenta", "Moderation Deines Workshops – empiria", [
  cover("Moderation Deines Workshops", 'Dein Workshop. Souverän moderiert. <span class="hl">Volle Wirkung.</span>',
        "Wir aktivieren die Beteiligten gezielt, wechseln bewusst die Perspektive und führen alles so strukturiert zusammen, dass Handlungsklarheit entsteht – mit Ergebnissen, mit denen sich direkt weiterarbeiten lässt.",
        S.load("workshop-moderation"),
        [("Themen", "Strukturen, Prozesse &amp; Rollen"), ("Formate", "Kreativ- &amp; Vertriebsworkshops"), ("Ergebnis", "Handlungsklarheit")]),
  page(
    sec("Moderation", 'Erfahrung aus <span class="hl">unzähligen Workshops.</span>',
        "Egal ob Strukturen, Prozesse und Rollen oder Kreativworkshops, Vertriebsansätze und mehr – wir bringen Deinen Workshop sicher ans Ziel."),
    cards([("chats", "Gute Stimmung", "Eine Atmosphäre, in der offen gesprochen wird – die Voraussetzung für jedes gute Ergebnis."),
           ("route", "Workshops, die funktionieren", "Klare Steuerung durch den Tag, damit Energie und Zeit dort ankommen, wo sie etwas bringen."),
           ("grid", "Klare Strukturen", "Wir ordnen Diskussionen, statt sie laufen zu lassen – am Ende steht Struktur, keine losen Enden."),
           ("target", "Ergebnisse, die tragen", "Ergebnisse, mit denen Dein Team direkt weiterarbeiten kann – nicht nur ein Protokoll zum Ablegen."),
           ("layers", "Hohe Methodenvielfalt", "Von Kreativformaten bis zur klaren Entscheidungsrunde – die Methode, die zum Thema passt."),
           ("slides", "Top Visualisierungen", "Ergebnisse werden sichtbar festgehalten statt nur besprochen – und sauber zusammengefasst.")], 3),
    feat(None, "Wir aktivieren. Wir wechseln die Perspektive. Wir führen zusammen.", "Genau so entsteht Handlungsklarheit – statt einer weiteren Runde, in der alle reden und nichts passiert.", style="margin-top:10mm"),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Neustrukturierungen mit neuen oder geteilten Rollen",
      "Abteilungen mit vielen Themen, aber ohne klaren Weg nach vorn",
      "Rollenklärung zwischen Führungskraft und neuer Stelle",
      "Führungswechsel, die mit einem Umbau zusammenfallen",
    ], style="margin-top:9mm"),
    stage("Beispiele", "Konkrete Usecases aus der Praxis.",
          "Ein Ausschnitt möglicher Workshopmoderationen – so vielfältig wie die Themen, die uns Teams mitbringen.",
          wm="grid", boden=True,
          inhalt=rows([("Restrukturierung mit geteilter Führung", "Neue Rollen bis hin zu einer geteilten Führungsrolle: Der Workshop hat Rollen, Prozesse und Zuständigkeiten so konkret gemacht, dass sie sich direkt in den Alltag übertragen ließen."),
          ("Klarheit nach zwei Strategieworkshops", "Jede Menge Themen gesammelt, aber kein klarer Weg nach vorn: Der Workshop brachte klare Schwerpunkte, klare Priorität und ein klares weiteres Vorgehen."),
          ("Einarbeitung einer neu geschaffenen Rolle", "Über mehrere Sequenzen wurde die neue Rolle ins Gesamtgefüge integriert und an den Schnittstellen geschärft – mit konkreten Methoden für den Alltag."),
          ("Neustart nach Führungswechsel", "Erst Vertrauen über mehrere Ebenen, dann Inhalte: Am Ende stand eine Abteilung, die schlagkräftiger in die Zukunft startete als zuvor."),
          ("Prozess- und Strukturworkshop im Team", "Gewachsene Strukturen, laufend neue Themen – aber nie die Frage, was wegfallen kann. Erst die Klärung, wofür die Abteilung steht, dann Prozesse, die im Alltag tragen statt dokumentiert abgelegt zu werden.")])),
    ),
  page(
    sec("Kontakt", 'Welcher Workshop soll <span class="hl">wirklich etwas bewegen?</span>',
        "Schildere uns Dein Thema und wen Du im Raum hast – wir sagen Dir, wie wir den Workshop aufsetzen würden und was er kostet."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_hr"])),
])

# ---------------------------------------------------------------- Marketing
P["marketing"] = ("cyan", "Marketing 2.0 – empiria", [
  cover("Marketing 2.0", 'Marketing für Versicherer <span class="hl">anders gedacht.</span>',
        ["Wir sind keine klassische Medienagentur. Neben Kommunikation verstehen wir vor allem Strategie und das Geschäftsmodell Versicherung – und somit Dich und Dein Gegenüber."],
        S.load("marketing"),
        [("Lösung 01", "MarketingEcoSystem"), ("Lösung 02", "sofort sichtbar"), ("Lösung 03", "Paid Ads"), ("Lösung 04", "Medien")]),
  page(
    sec("Unser Ansatz", 'Marketing, das Deine Strategie <span class="hl">zum Erfolg führt.</span>',
        "Unsere langjährige Projekterfahrung und unsere tiefe Kenntnis von Geschäftsmodell, Strategie und Zielgruppen eines Versicherers fließen in jedes Projekt ein. Das macht uns von der ersten Minute an schnell und schlagkräftig."),
    cards([("grid", "Komplett oder einzeln", "Buche uns als klar definierte Marketingabteilung – oder hol Dir gezielt einzelne Medien dazu."),
           ("target", "Auf den Punkt gebracht", "Wir bringen komplexe Themen auf den Punkt und übersetzen sie in die Welt Deiner Zielgruppe."),
           ("check", "Professionell umgesetzt", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – damit sie im entscheidenden Moment wirkt.")], 3),
    band("Der Unterschied", "Ein kurzes Briefing, ein paar gezielte Rückfragen – und es läuft.",
         "Ob als komplette Marketingabteilung im Abo oder bei einzelnen Medien: Du musst uns nicht erklären, wie Versicherung funktioniert. <b>Du kannst Dir sicher sein, dass es ab hier läuft.</b>", style="margin-top:11mm"),
    who("Für wen wir arbeiten", [
      "Versicherer, die Marketing als feste Größe brauchen, ohne eigenes Team aufzubauen",
      "Maklerunternehmen und Versicherungsbüros mit mehreren Mitarbeitenden",
      "Agenturleitungen, die am Vertriebserfolg gemessen werden",
      "Bereiche, die ein einzelnes Thema sichtbar machen müssen – schnell und sauber",
    ], style="margin-top:11mm"),
  ),
  # Die vier Loesungen mit den echten blauen Kaesten der Landingpage.
  page(
    sec("Unsere Lösungen", "Vier Wege. Ein Ergebnis: Sichtbarkeit, die verkauft.",
        "Ob als Gesamtpaket oder einzeln buchbar – Du wählst, wir liefern professionell."),
    # Titel und Beschreibung stehen im Kasten selbst - die Unterschrift traegt
    # daher "fuer wen" und den Preis.
    # Feste Figurenhoehe, damit beide Zeilen auf einer Linie sitzen - die
    # Paid-Ads-Box ist im Original etwas hoeher als die uebrigen drei.
    bilder([
      ("mk-thumb-mes", "Lösung 01",
       "Für Versicherer, Makler und Versicherungsbüros. <b>ab 399 € monatlich</b>"),
      ("mk-thumb-sofort", "Lösung 02",
       "Für Agenturleitungen und Makler im Vertrieb. <b>ab 349 € monatlich</b>"),
      ("mk-thumb-paidads", "Lösung 03",
       "Für alle, die jeden eingesetzten Euro nachvollziehen wollen. <b>Umfang nach Vorhaben</b>"),
      ("mk-thumb-medien", "Lösung 04",
       "Für Themen, die im entscheidenden Moment tragen müssen. <b>Umfang nach Vorhaben</b>"),
    ], cols=2, hoehe="52mm", style="margin-top:8mm"),
    '<p class="note">Preise zzgl. Umsatzsteuer in gesetzlicher Höhe. Bei Paid Ads und Medien hängt der Umfang vom Vorhaben ab – Du bekommst zeitnah ein konkretes Angebot.</p>'),
  # Je Loesung eine eigene Seite mit der Darstellung der zugehoerigen
  # Produktseite - nicht nur Bullets.
  page(
    sec("Lösung 01", 'MarketingEcoSystem <span class="hl">(MES).</span>',
        "Homepage, digitale Kanäle und ein zentrales Dashboard laufen an einem Ort zusammen. Die Kanäle bringen Besucher auf die Landingpage, das Dashboard führt alle Daten zusammen und bewertet sie laufend – die Empfehlungen fließen direkt zurück in die Umsetzung."),
    mdl("Alles greift ineinander", "Ein Kreislauf statt einzelner Aktionen.",
        S.load("mes-ineinander"),
        "Landingpage, Social-Media-Kanäle und Dashboard sind kein Nebeneinander mehr: Daten laufen zusammen, werden bewertet, und der nächste Schritt wird daraus abgeleitet.",
        figw="78mm",
        steps=[("01", "Landingpage &amp; Kanäle", "Content-Kalender, Postings und Umsetzung aus einer Hand."),
               ("02", "Zentrales Dashboard", "Alle Daten an einem Ort, laufend bewertet."),
               ("03", "Optimierung", "Die Empfehlungen fließen zurück in die Kanäle.")]),
    sec("Drei Buchungswege", "Von Eigenregie bis zur vollen Betreuung.", style="margin-top:10mm"),
    raster([("01", "Eigenregie<br><b>ab 399 € mtl.</b>", True),
            ("02", "Marketing as a Service<br><b>ab 3.500 € mtl.</b>"),
            ("03", "Unternehmerische<br>Partnerschaft")], cols=3),
  ),
  page(
    sec("Lösung 02", 'sofort <span class="hl">sichtbar.</span>',
        "Ein fertiges System aus Postings, Landingpage und E-Mail-Funnel – abgestimmt auf Deine Vertriebsschwerpunkte, ohne eigene Content-Produktion und ohne Briefing."),
    # Die Original-Vorschaubilder der Produktseite.
    bilder([
      ("produktseiten/sofort-sichtbar-preview-postings.png", "Social Media Postings",
       "Fertige Postings, genau auf die gewählte Zielgruppe abgestimmt."),
      ("produktseiten/sofort-sichtbar-preview-funnel.png", "E-Mail-Funnel",
       "Aktiviert Bestandskunden und leitet sie auf die passende Landingpage."),
      ("produktseiten/sofort-sichtbar-preview-landingpages.png", "Landingpages",
       "Mit Deinem Logo, Deinen Bildern und Deinen Kontaktdaten."),
    ], hoehe="42mm", rahmen=False, style="margin-top:7mm"),
    stage("Der Vorsprung", "Monate werden zu Tagen.",
          "Online, bevor eine klassische Agentur die Auftragsklärung abgeschlossen hat – ab 349 € monatlich.",
          wm="clock", boden=True,
          inhalt=bild("ss-vergleich", rahmen=False, style="margin-top:6mm")),
  ),
  page(
    sec("Lösung 03", 'Paid <span class="hl">Ads.</span>',
        "Kampagnen auf Google, Meta und LinkedIn, die nicht nur Reichweite bringen, sondern Anfragen. Ziel, Zielgruppe und Budget stehen fest, bevor der erste Euro läuft – und Du siehst jeden Monat, wohin er geflossen ist."),
    # Die echten Anzeigen-Mockups mit den Original-Plattformicons.
    stage("So sieht das aus", "Deine Anzeige im echten Umfeld.", wm="megaphone", boden=True,
          inhalt=bilder([
            ("pa-anzeige-google", "Google Ads", "Sichtbar genau dann, wenn jemand aktiv nach Deiner Lösung sucht."),
            ("pa-anzeige-meta", "Meta Ads", "Die Zielgruppe im Alltag erreichen, bevor sie aktiv sucht."),
            ("pa-anzeige-linkedin", "LinkedIn Ads", "Entscheider nach Branche, Position und Unternehmensgröße."),
          ], hoehe="58mm")),
  ),
  page(
    sec("Lösung 04", 'Medien, die <span class="hl">Ergebnisse liefern.</span>',
        "Wir sind keine typische Medienagentur: Bevor ein einziges Medium entsteht, verstehen wir Geschäftsmodell, Strategie und Zielgruppe. Erst wenn die Botschaft sitzt, folgt die Umsetzung."),
    stage(None, None, wm="slides", boden=True, inhalt=mocks([
        (S.load("medium-powerpoint"), "PowerPoint",
         "Eine Präsentation, die Deine Business Story trägt – klar strukturiert und startklar für den großen Moment im Raum."),
        (S.load("medium-landingpage"), "Landingpage",
         "Eine Seite für eine Zielgruppe, die genau ein zentrales Problem löst und gezielt zum nächsten Schritt führt."),
        (S.load("medium-rollup"), "Roll-up",
         "Der Gesamtzusammenhang in einem Bild – dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist."),
    ])),
  ),
  page(
    sec("Kontakt", 'Welcher Weg passt <span class="hl">zu Deinem Marketing?</span>',
        "Kurze Wege statt langer Abstimmungsrunden: Schildere uns Deine Ausgangslage – wir melden uns zeitnah mit einem konkreten Vorschlag, welcher der vier Wege für Dich am meisten bringt."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_content", "noah_pm"])),
])

# ---------------------------------------------------------------- MES
P["dashboard-digitales-marketing"] = ("cyan", "MarketingEcoSystem (MES) – empiria", [
  cover("MarketingEcoSystem (MES)", 'Du konzentrierst Dich nicht auf Marketing, sondern auf <span class="hl">Dein Business.</span>',
        "Unser MarketingEcoSystem führt Homepage, digitale Kanäle und zentrales Dashboard an einem Ort zusammen – inklusive laufender Schwachstellenanalyse und direkter Optimierung.",
        S.mes(),
        [("Für wen", "Versicherer &amp; Makler"), ("Überblick", "Alle Kanäle auf einen Blick"), ("Analyse", "Schwachstellen inkl. Lösung"), ("Daten", "DSGVO-konform")]),
  page(
    sec("Echter Nutzen statt Pseudo-Reporting", 'Kein Kennzahlenfriedhof. <span class="hl">Ein Ökosystem, das lebt.</span>',
        "Alle Kanäle laufen an einem Ort zusammen – bewertet statt nur gemacht, mit Lösung statt nur Problem."),
    cards([("puzzle", "Kanäle greifen ineinander", "Homepage, Social Media und Content sind kein Nebeneinander einzelner Aktionen mehr – sondern Dein MES: Google Ads, Meta, Website und mehr an einem Ort."),
           ("eye", "Kein Blindflug mehr", "Dein Marketing wird laufend geprüft – Schwachstellen fallen auf, bevor sie zum Problem werden, inklusive konkretem Lösungsvorschlag."),
           ("bolt", "Zurück in die Umsetzung", "Wir sehen, ob etwas funktioniert, wissen, warum wir anpassen – und setzen die nächste Optimierung direkt um, ohne Extra-Auftrag.")], 3),
    stage("Der Unterschied zur Agentur", "Du musst uns nicht briefen.",
          "Bei einer Agentur liegt die Überlegung zu Markterfolg und Marketingstrategie bei Dir – Du musst briefen und sagen, was zu tun ist.",
          "Bei uns nicht: Wir holen die wichtigsten Informationen mit wenigen gezielten Fragen ab und <b>sorgen für die permanente Umsetzung.</b>",
          wm="handshake", boden=True),
  ),
  page(
    sec("MarketingEcoSystem (MES)", "Alles greift ineinander.",
        "Landingpage, Social-Media-Kanäle und Dashboard greifen ineinander: Kanäle bringen Besucher auf die Landingpage, das Dashboard führt alle Informationen zusammen, trackt die Entwicklung und gibt Optimierungsempfehlungen zurück in die Kanäle."),
    stations([("Konzeption &amp; Umsetzung", "Landingpage &amp; Kanäle", "Homepage, LinkedIn, Facebook und Instagram – mit Content-Kalender, Postings und Umsetzung aus einer Hand."),
              ("Tracking &amp; Analyse", "Zentrales Dashboard", "Alle Daten an einem Ort, laufend bewertet – mit klaren Hinweisen, wo es hakt und warum."),
              ("Ableitung des nächsten Schritts", "Optimierung", "Die Empfehlungen fließen direkt zurück in die Kanäle. So bleibt Dein MES in einem fortlaufenden Kreislauf immer aktuell.")], style="margin-top:8mm"),
    '<div class="inline-sketch">' + S.mes() + '</div>',
    who("Für wen das gemacht ist", [
      "Versicherer ohne eigenes Marketingteam",
      "Maklerunternehmen mit mehreren Mitarbeitenden",
      "Versicherungsbüros, die digital sichtbar werden wollen",
      "Alle, die Wirkung sehen wollen statt Pseudo-Reporting",
    ], style="margin-top:8mm"),
  ),
  page(
    sec("Pakete", 'Drei Wege, <span class="hl">uns zu buchen.</span>', "Vom Dashboard in Eigenregie bis zur vollständigen Betreuung."),
    pakete([
      dict(name="Eigenregie", preis="ab 399 €", einheit="mtl.",
           text="Wir verknüpfen Deine Homepage und digitalen Kanäle mit unserem Dashboard inklusive Reporting – die Optimierung übernimmst Du selbst.",
           bullets=["Anbindung an unser Dashboard &amp; Reporting – ohne Eingriff in Homepage oder Kanäle",
                    "Regelmäßiges Reporting zum Status und zu Optimierungsmöglichkeiten"],
           fazit="Wenn Du das Ecosystem nutzen, die Umsetzung aber in der Hand behalten willst.",
           hinweis="Mindestlaufzeit drei Monate, zzgl. einmaliger Setup-Kosten"),
      dict(name="Marketing as a Service", badge="Meistgewählt", preis="ab 3.500 €", einheit="mtl.",
           text="Wir übernehmen die laufende Betreuung und Optimierung von Homepage, Social-Media-Kanälen und Reporting.",
           bullets=["Homepage – von uns betreut und laufend optimiert",
                    "Firmenaccounts &amp; Profile: LinkedIn, Facebook, Instagram",
                    "Content-Kalender, Postings und Umsetzung aus einer Hand",
                    "Monatlicher Austausch plus wöchentliches Reporting"],
           fazit="Für alle, die ihr Marketing nicht mehr selbst stemmen, sondern uns anvertrauen wollen.",
           hinweis="Mindestlaufzeit zwölf Monate, keine einmaligen Setup-Kosten"),
      dict(name="Unternehmertum", preis="Auf Anfrage",
           text="Wir suchen unternehmerische Partnerschaften – wenn die Voraussetzungen für beide Seiten stimmen.",
           bullets=["Wir werden Teil des Teams statt nur Dienstleister",
                    "Kein laufendes Honorar, sondern Beteiligung am Erfolg",
                    "Für Unternehmen mit Potenzial, das wir mit aufbauen wollen",
                    "Langfristig, partnerschaftlich, auf Augenhöhe"],
           fazit="Wenn Du mit einem erfahrenen Partner wachsen und den Markt erobern willst.",
           hinweis="Gemeinsames Gespräch zur Prüfung, ob eine Beteiligung zueinander passt"),
    ]),
    '<p class="note">Der Preis richtet sich nach dem vereinbarten Umfang. Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>',
    ),
  page(
    sec("Kontakt", 'Dein Marketing als <span class="hl">lebendes Ökosystem?</span>',
        "Kurze Wege statt langer Abstimmungsrunden: Schildere uns Deine Ausgangslage – wir sagen Dir, welches Paket zu Deinem Haus passt."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_content", "noah_pm"])),
])

# ---------------------------------------------------------------- sofort sichtbar
P["sofort-sichtbar"] = ("violet", "sofort sichtbar – empiria", [
  cover(None, 'Digital sichtbar. <span class="hl">Ohne Briefing.</span> Sofort einsatzbereit.',
        "Ein fertiges System aus Postings, Landingpage und E-Mail-Funnel für Agenturleiter und Makler, die am Vertriebserfolg gemessen werden und für Marketing weder Zeit noch Nerven übrig haben.",
        S.sofort(),
        [("Start", "Ohne Briefing"), ("Auswahl", "20 Zielgruppenprofile"), ("Paket", "Alles in einem"), ("Auftritt", "In Deinem Design")],
        brandlogo="assets/sofort-sichtbar-logo-violet.svg", subklein=True),
  page(
    sec("Was sofort sichtbar mitbringt", 'Fertig gedacht, <span class="hl">nicht nur fertig gebaut.</span>', "Alles in einem Paket – abgestimmt auf Deine Vertriebsschwerpunkte."),
    # Die freigestellten Original-Vorschaubilder der Produktseite - ohne Rahmen
    # und mit Flaeche, sonst wirken sie wie Briefmarken. Die Aussage zur
    # Individualisierung ist der Kopf des Bandes, kein zweiter Kasten daneben.
    stage("Individualisierung", "Alles in Deinem Corporate Design.",
          "Logo, Bilder, Kontaktdaten und Farbwelt werden eingebunden, damit alles aussieht, als wäre es für Deine Agentur gebaut.",
          wm="phone", boden=True, inhalt=bilder([
      ("produktseiten/sofort-sichtbar-preview-postings.png", "Social Media Postings",
       "Fertige Postings, genau auf Deine Zielgruppe abgestimmt – ohne eigene Content-Produktion."),
      ("produktseiten/sofort-sichtbar-preview-funnel.png", "E-Mail-Funnel",
       "Aktiviert Deine Bestandskunden und leitet sie auf die passende Landingpage weiter."),
      ("produktseiten/sofort-sichtbar-preview-landingpages.png", "Passende Landingpages",
       "Mit Download-Dokument, Podcast-Folge und optimierten Kontaktdaten – fertig für jeden Anlass."),
    ], hoehe="30mm", rahmen=False)),
  ),
  page(
    stage("Preise", 'Die passenden Pakete für Deinen Vertriebsfokus.',
          "Monatlich buchbar, mit Rabatt bei jährlicher Zahlung – jede Vertriebsstrecke mit einer Mindestlaufzeit von drei Monaten.",
          wm="euro", boden=True, inhalt=
    opts([dict(name="Fokus", text="Eine klar definierte Zielgruppe ganzjährig erreichen.", list=["1 digitale Vertriebsstrecke", "Individualisierungspaket", "Contentplan für Social Media"], price="349 €<em>/Monat</em>", pnote="bei jährlicher Zahlung · 435 € monatlich"),
          dict(badge="Beliebt", name="Reichweite", text="Kontakte aus mehreren Zielgruppen gewinnen – ohne eigenen Aufwand.", list=["3 digitale Vertriebsstrecken", "Erweiterte Individualisierung", "Performance-Reporting"], price="499 €<em>/Monat</em>", pnote="bei jährlicher Zahlung · 625 € monatlich", feat=True),
          dict(name="Marktposition", text="Berater positionieren, Stärken zeigen, planbare Neukontakte.", list=["10 digitale Vertriebsstrecken", "Automatisierung der Postings", "Regelmäßige 1:1-Beratung"], price="999 €<em>/Monat</em>", pnote="bei jährlicher Zahlung · 1.250 € monatlich")])
    + '<p class="note">Alle Preise zzgl. Umsatzsteuer in gesetzlicher Höhe.</p>'),
  ),
  # Reihenfolge wie auf der Produktseite: "Monate werden zu Tagen" ist die
  # Aussage ZUR Vergleichsgrafik, danach folgen die vier Ablaufschritte.
  page(
    sec("Ablauf", "Monate werden zu Tagen.",
        "Mit sofort sichtbar bist Du online, bevor eine klassische Agentur die Auftragsklärung abgeschlossen hat."),
    # Die Vergleichsgrafik im Original von der Produktseite abgenommen. Ein
    # Nachbau in PDF-CSS hat die Kernaussage zerstoert: In der sofort-sichtbar-
    # Zeile muss "Auftragsklaerung" schmaler sein als in der Agentur-Zeile.
    bild("ss-vergleich", rahmen=False, style="margin-top:8mm"),
    stage(None, None, wm="clock", boden=True, inhalt=cards([(None, "Auftragsklärung", "Wir klären kurz Deinen Vertriebsfokus – ohne die wochenlange Konzeptphase einer klassischen Agentur."),
           (None, "Zielgruppen auswählen", "Du wählst aus den vorbereiteten Profilen die aus, die zu Deinen Kundinnen und Kunden passen."),
           (None, "Stil &amp; Auftritt festlegen", "Du wählst Deinen Stil und bringst Dein Design ein – Logo, Bilder, Kontaktdaten, Farbwelt."),
           (None, "Live gehen", "Postings, Landingpage und E-Mail-Funnel gehen live – und Du hast mehr Zeit für Kundengespräche.")],
          4, style="gap:3.5mm;margin-top:2mm", numbered=True)),
  ),
  page(
    sec("Häufige Fragen", "Was Agenturleiter uns am häufigsten fragen."),
    cases([("Mehrere Zielgruppen gleichzeitig?", "Ja – parallel buchbar oder eine Lizenz im Jahresverlauf für wechselnde Zielgruppen nutzen."),
           ("Wofür kann ich es einsetzen?", "Neukundengewinnung, Bestandskundenaktivierung und im Beratungsalltag vor und nach Terminen."),
           ("Kommen Anfragen DSGVO-konform an?", "Direkt bei Dir – ohne Umweg über uns, Landingpages auf Servern in der EU."),
           ("Wie hoch ist mein Zeitaufwand?", "Sehr gering: Wir übernehmen die Technik, Du postest und führst Kundengespräche.")], style="gap:5mm 10mm;margin-top:6mm"),
    checks(["Individuelle Landingpages mit Deinem Logo, Deinen Bildern und Kontaktdaten",
            "Mindestlaufzeit drei Monate je Vertriebsstrecke – danach verlängern, wechseln oder kündigen",
            "Für eine komplett individuelle Lösung sprechen wir gerne separat"], style="margin-top:9mm"),
    contact_html=contact("Bereit, sofort sichtbar zu werden?", ["daniel", "kerstin_content", "noah_pm"])),
])

# ---------------------------------------------------------------- Paid Ads
P["paid-ads"] = ("cyan", "Paid Ads – empiria", [
  cover("Performance Marketing", 'Google, Meta &amp; LinkedIn Ads <span class="hl">für Deine Zielgruppe.</span>',
        "Auf dem passenden Kanal erreichen wir genau die Menschen, die zu Deiner Branche und Deinem Angebot passen. Du weißt bei jedem Euro, wohin er fließt und was er auslöst.",
        S.paid_ads(),
        [("Suche", "Google Ads"), ("Social", "Meta Ads"), ("B2B", "LinkedIn Ads"), ("Start", "Kostenloser Potentialcheck")]),
  page(
    sec("Leistungen", 'Der richtige Kanal <span class="hl">für Deine Zielgruppe.</span>', "Wir übernehmen Strategie, Setup und laufende Optimierung. Du konzentrierst Dich auf Dein Unternehmen."),
    # Die echten Anzeigen-Mockups der Produktseite - mit den Original-Icons von
    # Google, Meta und LinkedIn. Drei nebeneinander, bewusst klein gehalten.
    stage("So sieht das aus", "Deine Anzeige im echten Umfeld.",
          "Kein abstraktes Konzept – so begegnet Deine Anzeige der Zielgruppe: Textanzeige in der Suche, Bildanzeige im Feed.",
          wm="megaphone", boden=True,
          inhalt=bilder([
            ("pa-anzeige-google", "Google Ads", "Sichtbar genau dann, wenn jemand aktiv nach Deiner Lösung sucht. Aus Klicks werden Termine."),
            ("pa-anzeige-meta", "Meta Ads", "Facebook und Instagram erreichen Deine Zielgruppe im Alltag, bevor sie aktiv sucht."),
            ("pa-anzeige-linkedin", "LinkedIn Ads", "Entscheider nach Branche, Position und Unternehmensgröße – wer im B2B unterschreibt."),
          ], hoehe="62mm")),
  ),
  page(
    sec("Ablauf", "Vier Schritte zu planbarem Ergebnis.", "So wird aus Deinem Budget ein nachvollziehbares Ergebnis."),
    stations([("", "Analyse &amp; Strategie", "Wir prüfen Dein bestehendes Konto oder starten bei null. Ziel, Zielgruppe und Budget stehen fest, bevor der erste Euro läuft."),
              ("", "Setup &amp; Start", "Kampagnen, Tracking und Anzeigen werden sauber aufgebaut und gehen live. Ab dem ersten Tag misst jedes Ergebnis."),
              ("", "Optimierung", "Wir werten Deine Anzeigen laufend aus und optimieren sie: Was funktioniert, bekommt mehr Budget."),
              ("", "Reporting &amp; Skalierung", "Du siehst jeden Monat, wohin jeder Euro geflossen ist und was er gebracht hat.")], style="margin-top:6mm"),
    # Der Kanal-Check im Original, in ruhiger Groesse statt seitenfuellend.
    # Ueberschrift nicht wiederholen - sie steht bereits im Baustein selbst.
    stage("Kanal-Check", "Nach vier Fragen weißt Du es.",
          "Zielgruppe, heutiger Weg zu Deinen Kunden, Ziel der Kampagne und Wert einer Anfrage – daraus ergibt sich der Kanal, mit dem Du starten solltest.",
          wm="compass", boden=True,
          inhalt=bild("pa-kanalcheck", breite="145mm")),
  ),
  page(
    sec("Häufige Fragen", "Kurz beantwortet."),
    cases([("Was brauche ich, um zu starten?", "Zugriff auf bestehende Konten, falls vorhanden, und Klarheit über Budget und Ziel. Den Rest klären wir im Auftakt."),
           ("Wann sehe ich erste Ergebnisse?", "Erste Daten meist nach wenigen Wochen. Belastbare Aussagen brauchen etwas mehr Zeit, damit Kampagnen lernen."),
           ("Welche Plattformen betreut ihr?", "Google, Meta und LinkedIn – der richtige Start hängt von Zielgruppe und Angebot ab, nicht vom Trend."),
           ("Gibt es Mindestlaufzeiten?", "Ja, mindestens drei Monate für belastbare Daten. Danach läuft die Zusammenarbeit monatlich weiter."),
           ("Woher weiß ich, wie gut es läuft?", "Voller Zugriff auf Dein Konto und jeden Monat eine klare Auswertung: Was hat jeder Euro gebracht?")], style="gap:5.5mm 10mm;margin-top:6mm"),
    # Der Potenzialcheck-Kasten im Original als Einstieg.
    stage("Der Einstieg", "Kostenloser Potentialcheck.", wm="search", boden=True,
          inhalt=bild("pa-potenzialcheck", breite="150mm", rahmen=False, style="margin-top:6mm")),
  ),
  page(
    sec("Kontakt", 'Welcher Kanal bringt Dir <span class="hl">Anfragen?</span>',
        "Sag uns, welche Zielgruppe Du erreichen willst und mit welchem Budget Du rechnest – wir schlagen Dir den passenden Kanal vor."),
    stations([
      ("Schritt 01", "Kurz schildern", "Zielgruppe, Angebot und Budgetrahmen – eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag zum passenden Kanal."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Laufzeit und Investition klären wir gemeinsam, bevor der erste Euro läuft."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_content", "noah_pm"])),
])

# ---------------------------------------------------------------- Medien
P["medien"] = ("cyan", "Medien, die Ergebnisse liefern – empiria", [
  cover("Medien, die Ergebnisse liefern", 'Deine Botschaft. <span class="hl">Auf den Punkt.</span> Volle Wirkung.',
        "Wir sind keine typische Medienagentur. Wir sind Profis in den Themen Geschäftsmodell Versicherung, Strategie und Kommunikation – und übersetzen Deine Themen in die Welt Deiner Zielgruppe.",
        S.medien(),
        [("Medium 01", "PowerPoint"), ("Medium 02", "Landingpage"), ("Medium 03", "Roll-up")]),
  page(
    sec("Unser Ansatz", 'Keine Medienagentur, sondern <span class="hl">Profis für Wirkung.</span>', "Bevor ein einziges Medium entsteht, verstehen wir Dein Geschäftsmodell, Deine Strategie und Deine Zielgruppe."),
    cards([("compass", "Geschäftsmodell &amp; Strategie", "Wir verstehen, wie Dein Geschäftsmodell funktioniert und wohin Deine Strategie steuert – bevor wir über Medien sprechen."),
           ("target", "Auf den Punkt gebracht", "Wir übersetzen komplexe Themen in die Welt Deiner Zielgruppe – der entscheidende Erfolgsfaktor, damit Kommunikation ankommt."),
           ("check", "Professionelle Medien", "Erst wenn die Botschaft sitzt, folgt die Umsetzung – professionell gebaut, damit sie im entscheidenden Moment wirkt.")], 3),
    sec("Medien wirksam einsetzen", "Es geht nicht um Medien, sondern um Deine Ziele.",
        "Wir starten nie mit der Frage PowerPoint, Landingpage oder Roll-up, sondern damit, was Du und Dein Team benötigen, um erfolgreich zu sein. Wenn diese Taktik steht, entwickeln wir zielgerichtete Medien, die genau dieses Ergebnis liefern.", style="margin-top:13mm"),
    cards([("slides", "PowerPoint", "Eine Präsentation, die Deine Business Story trägt – klar strukturiert und startklar für den großen Moment im Raum."),
           ("browser", "Landingpage", "Eine Seite für eine Zielgruppe, die genau ein zentrales Problem löst und gezielt zum nächsten Schritt führt."),
           ("rollup", "Roll-up", "Der Gesamtzusammenhang in einem Bild – dauerhaft im Raum präsent, auch wenn der Beamer längst aus ist.")], 3, style="margin-top:6mm"),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Themen, die im Vorstand oder Gremium tragen müssen",
      "Vertrieb und Messeauftritte mit klarer Botschaft",
      "Bereiche ohne eigene Medienproduktion",
    ], style="margin-top:9mm"),
    stage("Beispiele", "Konkrete Use Cases aus der Praxis.",
          "Eine Auswahl realer Anwendungsfälle, die zeigen, wie unsere Medien wirken.",
          wm="slides", boden=True,
          inhalt=rows([("Der entscheidende Pitch im Konsortium", "Statt Standardfolien mit Interpretationsspielraum Medien, die zu 100 % zeigen: Wir haben den Kunden verstanden – und die Lösung ist maßgeschneidert."),
          ("Neupositionierung eines Konzernunternehmens", "Eine Gesamtlogik, die Kooperations-, Vertriebspartnern und Kunden verständlich macht, wofür das Unternehmen steht – aus einer Hand."),
          ("Produktlaunch oder -relaunch", "Statt Broschüren und 150 Detailfolien eine durchdachte Kombination digitaler Formate, die den Vertrieb wirklich erfolgreich macht."),
          ("Aufsichtsrats- und Gremientermine", "Große Themen kompakt und vertrauensbildend erzählt – übersetzt in die Welt auch fachfremder Gremienmitglieder."),
          ("Gespräche mit dem Rückversicherer", "Die strategische Richtung stringent erzählt, nicht nur in harten Zahlen – für Erneuerungsgespräche, Monte Carlo oder Baden-Baden.")], style="margin-top:3mm")),
    ),
  page(
    sec("Kontakt", 'Welche Botschaft <span class="hl">soll wirken?</span>',
        "Schildere uns Dein Thema und die Zielgruppe – wir sagen Dir, welches Medium dafür trägt und was es braucht."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_content", "noah_pm"])),
])

# ---------------------------------------------------------------- Training & Sparring
P["training-sparring"] = ("green", "Training & Sparring – empiria", [
  cover("Training &amp; Sparring", 'Begleitung, <span class="hl">die wirkt.</span> Kein Seminar von der Stange.',
        "Ob als Trainingsbegleitung für Dein Team oder als vertrauliches 1:1-Sparring für Dich als Führungskraft: Wir begleiten, statt nur zu schulen – zugeschnitten auf die Versicherungsbranche und Deinen Alltag.",
        S.training_sparring(),
        [("Format 01", "Teams befähigen"), ("Format 02", "1:1 Sparring"), ("Branche", "Versicherungen")]),
  page(
    sec("Unser Ansatz", 'Begleitung statt <span class="hl">Seminar von der Stange.</span>', "Ob im Team oder im 1:1: Wir bleiben dran, bis die Wirkung im Alltag ankommt."),
    cards([("target", "Auf Deinen Alltag zugeschnitten", "Keine Vorlage von der Stange – Inhalte und Fälle aus Deiner Praxis in der Versicherungsbranche."),
           ("lock", "Vertraulich &amp; auf Augenhöhe", "Ob im Team oder im 1:1: offen, ehrlich und mit klarer eigener Haltung."),
           ("route", "Begleitung statt Einmal-Termin", "Wir bleiben dran, bis die Wirkung im Alltag messbar ankommt.")], 3),
    # Die Formate-Grafik von der Landingpage statt einer Tabellenzeile.
    mdl("Zwei Formate", "Ein Ziel: Wirkung im Alltag.",
        S.load("ts-formate"),
        "Wähle das Format – wir passen es auf Dich an.",
        figw="86mm", style="margin-top:13mm",
        steps=[("01", "Teams befähigen", "Business Storytelling, Visualisierung und Begleitung über 3–6 Monate."),
               ("02", "1:1 Sparring", "Vertrauliches Gegenüber für Vorstände und Führungskräfte.")]),
  ),
  page(
    sec("Format 01", 'Teams befähigen, <span class="hl">professionell zu kommunizieren.</span>',
        "Dein Team bereitet ein Thema für die Vorstandssitzung vor – und die Diskussion läuft ins Leere. Dann braucht es kein Seminar von der Stange, sondern Befähigung und Begleitung bei der Umsetzung an echten Themen."),
    # Drei Bausteine als Abfolge im Landingpage-Look statt als Textzeilen.
    stage("Die drei Bausteine", "Mindset, Methodik, Anwendung – in dieser Reihenfolge.",
          "Jeder Baustein baut auf dem vorherigen auf. Erst in der Begleitung entsteht die Wirkung, die im Alltag bleibt.",
          wm="route",
          inhalt=cards([
            (None, "Business Storytelling &amp; Gesprächstaktik", "Wer sitzt im Raum, welches Ergebnis wird gebraucht – und wie wird daraus eine Story, die trägt? Mindset, Methodik und Umsetzung bauen aufeinander auf."),
            (None, "Visualisierung &amp; Nutzung Standards", "Aus der Business Story entstehen Folien, die verdichten statt zu überladen – als Vortragsfolien für den Auftritt und als Beraterfolien für die Projektarbeit."),
            (None, "Umsetzungsbegleitung · 3–6 Monate", "Erfolg entsteht nicht im Training, sondern in der Anwendung: Wir begleiten die echten Termine Deines Teams, bis die Wirkung im Alltag ankommt."),
          ], 3, numbered=True)),
    who("Für wen das gemacht ist", [
      "Teams vor Vorstands- und Aufsichtsratssitzungen",
      "Projektlenkungsausschüsse und Vertriebstagungen",
      "Gespräche mit Kooperationspartnern und Rückversicherern",
      "Wichtige Kundenpitches, bei denen es zählt",
    ], style="margin-top:8mm"),
    '<p class="note">Umfang und Investition hängen von Teamgröße und Begleitungszeitraum ab – Du bekommst zeitnah ein konkretes Angebot.</p>',
  ),
  page(
    sec("Format 02", '1:1 Sparring für Vorstände <span class="hl">und Führungskräfte.</span>',
        "Seit vielen Jahren begleiten wir Vorstandsmitglieder und Führungskräfte vertraulich im 1:1 – ein Raum, in dem Themen wirklich offen besprochen werden, ohne interne Rücksichten."),
    # Die Themen als Raster im Landingpage-Look statt als lange Punkteliste.
    stage("Worüber wir sprechen", "Sechs Themen, die im 1:1 wirklich auf den Tisch kommen.",
          wm="lock",
          inhalt=raster([
            ("01", "Strategische Themen &amp;<br>Geschäftsmodellfragen", True),
            ("02", "Komplexe Situationen aus<br>mehreren Perspektiven"),
            ("03", "Lösungswege und<br>Vorgehensweisen abwägen"),
            ("04", "Positionierung gegenüber<br>Vorstand und Bereichen"),
            ("05", "Aufsichtsrat und Steuerung<br>von Konzernunternehmen"),
            ("06", "Konzeption von<br>Kommunikation nach außen"),
          ], cols=3)),
    who("Für wen das gemacht ist", [
      "Vorstandsmitglieder mit Themen ohne internes Gegenüber",
      "Hauptabteilungs- und Abteilungsleitungen",
      "Führungskräfte vor strategischen Weichenstellungen",
      "Alle, die Positionierung und Auftreten stärken wollen",
    ], style="margin-top:10mm"),
    '<p class="note">Rhythmus und Umfang richten sich danach, wie es für Dich passt – vom regelmäßigen Termin bis zur kurzfristigen Rückfrage.</p>',
  ),
  page(
    who("Für wen das gemacht ist", [
      "Führungskräfte, deren Team Themen nicht überzeugend vorbereitet",
      "Führungskräfte, die ein vertrauliches 1:1-Gegenüber suchen",
      "Teams vor wiederkehrenden Gremien- und Vertriebsterminen",
      "Alle, denen ein Seminar von der Stange zu wenig ist",
    ], style="margin-top:9mm"),
    sec("Das Ergebnis", 'Weniger Seminar. <span class="hl">Mehr Wirkung.</span>',
        "Dein Team überzeugt, wenn es zählt – und Du triffst Entscheidungen mit einem Gegenüber, das mitdenkt und mitgestaltet."),
    checks(["Inhalte und Fälle aus Deinem echten Alltag statt austauschbarer Trainer-Folien",
            "Begleitung genau dann, wenn es zählt: vor dem Termin, beim letzten Schliff, im Review",
            "Ein Raum, in dem Themen offen besprochen werden – ohne interne Rücksichten",
            "Aus Gesprächen wird schnell Umsetzung – kommunikativ oder inhaltlich"], style="margin-top:6mm"),
    feat("Unsere Haltung", "Wir begleiten, statt nur zu schulen.", "Mit klarer eigener Haltung statt austauschbarer Trainer-Folien – zugeschnitten auf die Versicherungsbranche und Deinen konkreten Alltag.", style="margin-top:10mm"),
    contact_html=contact("Welches Format passt zu Dir?", ["daniel", "kerstin_hr"])),
])

# ---------------------------------------------------------------- Präsentationsseminar
P["praesentationsseminar"] = ("green", "Teams befähigen, professionell zu kommunizieren – empiria", [
  cover("Befähigung und Begleitung, kein Seminar", 'Teams befähigen, professionell zu <span class="hl">kommunizieren.</span>',
        ["Du bist Führungskraft in der Versicherungsbranche und Dein Team bereitet Themen und Präsentationen vor, die nicht überzeugen?", "Dann braucht Dein Team kein Seminar, sondern <b>professionelle Begleitung bei der Umsetzung.</b>"],
        S.praesentation(),
        [("Baustein 01", "Storytelling &amp; Taktik"), ("Baustein 02", "Visualisierung"), ("Baustein 03", "Umsetzungsbegleitung")]),
  page(
    sec("Das Problem", 'Dein Team bereitet vor. Und erreicht das Ziel <span class="hl">trotzdem nicht.</span>'),
    quotes(["Das Thema für die Vorstandssitzung – und die Diskussion läuft ins Leere.", "Die Präsentation im Lenkungsausschuss – und hinterher denkst Du: Das hätte besser laufen müssen.", "Die Story trägt nicht, die Unterlagen überzeugen nicht, im Raum fehlt die Souveränität."], style="margin-top:6mm"),
    statement(None, "Es wird Zeit, bisherige Denkmuster <b>mit einfachen Logiken zu durchbrechen.</b>", style="margin-top:8mm"),
    stage("Die Lösung", 'Befähigung und Begleitung bei der Umsetzung.',
          "Wir bringen Deinem Team bei, wie das geht – und lassen es danach nicht allein. Wir arbeiten an echten Themen aus Eurem Alltag: dem nächsten Kundenpitch, dem nächsten Gespräch mit dem Rückversicherer, der nächsten wichtigen Abstimmungsrunde.",
          "Vor dem Termin, beim letzten Schliff, danach beim Analysieren – genau dann sind wir da. <b>So baut sich etwas auf, das ein einzelnes Seminar nie schafft.</b>",
          wm="route", boden=True),
  ),
  page(
    sec("Inhalte", "Drei Bausteine, die aufeinander aufbauen."),
    rows([("Business Storytelling &amp; Gesprächstaktik", "Dein Team lernt, bei jedem Termin zuerst zu klären: Wer sitzt im Raum, und welches Ergebnis wird gebraucht?",
           '<div style="display:grid;grid-template-columns:repeat(3,1fr);gap:6mm;margin-top:3mm">' +
             '<div><p class="label" style="margin-bottom:1.2mm">Modul 1 · Mindset</p>' + dots(["Wie Entscheider denken", "Nutzen statt Themenfokus"], "sm") + '</div>' +
             '<div><p class="label" style="margin-bottom:1.2mm">Modul 2 · Methodik</p>' + dots(["Kernlogik der Business Story", "Übertragung aufs eigene Thema"], "sm") + '</div>' +
             '<div><p class="label" style="margin-bottom:1.2mm">Modul 3 · Umsetzung</p>' + dots(["Einstieg mit sofortiger Klarheit", "Präziser nächster Schritt"], "sm") + '</div>' +
           '</div>'),
          ("Visualisierung &amp; Nutzung Standards", "Aufbauend auf der Business Story entstehen professionelle Folien: klare Visualisierung statt Informationsüberladung.",
           '<div class="two" style="gap:5mm">' +
             '<div><p class="label" style="margin-bottom:1mm">Vortragsfolien</p><p style="font-size:8.6pt;color:var(--g70);line-height:1.5">Verdichtet auf Story und Kernbotschaft, sofort erfassbar – in Präsenz und online.</p></div>' +
             '<div><p class="label" style="margin-bottom:1mm">Beraterfolien</p><p style="font-size:8.6pt;color:var(--g70);line-height:1.5">Für Projektarbeit: umfangreicher, aber klar strukturiert und professionell.</p></div></div>'),
          ("Umsetzungsbegleitung · 3–6 Monate", "Erfolg entsteht nicht im Training, sondern in der Anwendung bei echten Themen – individuell abgestimmt auf die Projekte und Termine Deines Teams.")]),
    # Anteilsbalken als eigener Baustein: gleiche Hoehe, Breite = Anteil,
    # Beschriftungen auf einer Linie. Vorher sprangen Balken und Texte.
    stage("Lernlogik &amp; Erfolgsfaktor", "Orientierung an der 70-20-10-Regel.",
          "Ein Seminar allein verändert nichts. Wirkung entsteht dort, wo an echten Themen gearbeitet wird.",
          wm="trend", boden=True,
          inhalt=anteile([("10 %", "Impulse im Seminar"),
                          ("20 %", "Kollegialer Austausch und gezielte Begleitung"),
                          ("70 %", "Lernen durch Anwendung an echten, relevanten Themen", True)])),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Führungskräfte, deren Team Themen vorbereitet, die nicht überzeugen",
      "Teams, die regelmäßig vor Vorstand oder Aufsichtsrat auftreten",
      "Bereiche mit wiederkehrenden Vertriebstagungen und Gremienterminen",
      "Teams, die vor Kundenpitches und Partnergesprächen sicher werden sollen",
    ], style="margin-top:9mm"),
    sec("Vorgehen in der Begleitung", "Schlank und fokussiert."),
    chips(["1 · Auftrag &amp; Zielbild klären", "2 · Storyboard entwickeln", "3 · Präsentation erstellen", "4 · Gesprächstaktik anwenden", "5 · Review &amp; Optimierung"]),
    sec("Das Ergebnis", 'Dein Team überzeugt <span class="hl">ohne Dich.</span>',
        "Dein Team bereitet Themen so auf, dass sie überzeugen, und tritt sicher auf, wenn es zählt. Du bekommst Ergebnisse, mit denen Du wirklich arbeiten kannst.", style="margin-top:11mm"),
    cards([("compass", "Strategisches Verständnis", "Dein Team stellt den Mehrwert für die Zielgruppe in den Mittelpunkt."),
           ("chat", "Überzeugende Story", "Zügig und sicher eine Business Story aufbauen – unabhängig vom Format."),
           ("target", "Souverän im Termin", "Klarer Einstieg, strukturiert aufs Ziel hin und professionelle Folien.")], 3, style="margin-top:7mm"),
    ),
  page(
    sec("Kontakt", 'Soll Dein Team <span class="hl">ohne Dich überzeugen?</span>',
        "Schildere uns, wo Dein Team heute steht und vor welchen Terminen es steht – wir schlagen ein passendes Begleitungskonzept vor."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_hr"])),
])

# ---------------------------------------------------------------- Sparring
P["sparring"] = ("green", "1:1 Sparring – empiria", [
  cover("1:1 Sparring", 'Offen sprechen. <span class="hl">Klar entscheiden.</span> Volle Wirkung.',
        "Seit vielen Jahren begleitet Daniel Ströbel Vorstandsmitglieder und Führungskräfte vertrauensvoll im 1:1 – bei strategischen Themen, Ideen zum Geschäftsmodell oder Führungsfragen.",
        S.sparring(),
        [("Für wen", "Führungskräfte in Versicherungen"), ("Ebene", "Abteilungsleiter bis Vorstand"), ("Themen", "Strategie, Geschäftsmodell, Führung")]),
  page(
    sec("Sparring", 'Ein Gegenüber, das <span class="hl">mitdenkt und mitgestaltet.</span>',
        "Offen über Themen sprechen, für die es intern oft nicht die passende Distanz oder Erfahrung gibt. Komplexe Situationen aus verschiedenen Perspektiven betrachten, Vorgehensweisen abwägen, Lösungswege klar definieren."),
    cards([("lock", "Offen &amp; vertraulich", "Ein Raum, in dem Themen wirklich offen besprochen werden – ohne interne Rücksichten."),
           ("star", "Erfahrung, die trägt", "Viele Jahre Sparring mit Vorständen, Hauptabteilungs- und Abteilungsleitern."),
           ("eye", "Mehrere Perspektiven", "Komplexe Situationen aus unterschiedlichen Blickwinkeln – für Lösungen, die passen."),
           ("compass", "Klarheit", "Am Ende steht nicht nur eine Einschätzung, sondern eine Richtung."),
           ("bolt", "Vom Gespräch zur Umsetzung", "Schnell entsteht ein einsatzbereites Konzept – kommunikativ oder inhaltlich."),
           ("megaphone", "Schlagkräftig nach außen", "Positionierung und Auftreten gegenüber Vorstand und Bereichen werden stärker.")], 3),
    band("Mehr als nur Sparring", "Umsetzungsturbo!",
         "In unseren Gesprächen entstehen oft Ideen, die Du am liebsten sofort vorantreiben würdest. Intern fehlt dabei meist einer der drei Erfolgsbausteine: <b>jemand, der das Thema versteht, die Kapazität oder die Skills für die Umsetzung.</b> Genau hier finden wir oft direkt eine Lösung – ganz ohne weiteres Briefing, denn wir kennen die Hintergründe bereits.", style="margin-top:10mm"),
  ),
  page(
    who("Für wen das gemacht ist", [
      "Vorstandsmitglieder, die ein vertrauliches Gegenüber brauchen",
      "Hauptabteilungs- und Abteilungsleitungen in der Versicherungsbranche",
      "Führungskräfte vor strategischen Weichenstellungen",
      "Alle, die Positionierung und Auftreten spürbar stärken wollen",
    ], style="margin-top:9mm"),
    sec("Themen", "So flexibel, wie es für Dich passt.",
        "Der Alltag hält sich oft nicht an planbare Termine. Ein kurzer Austausch ist oftmals genauso hilfreich wie ein strukturierter Termin – bei Bedarf auch zu Randzeiten."),
    '<div class="two" style="margin-top:6mm"><div><p class="label" style="margin-bottom:2mm">Wann wir sprechen</p>' + chips(["Persönliches Treffen", "Offsite", "Telefonat aus dem Auto", "Kurznachricht"], style="margin-top:0") + '</div>' +
    '<div><p class="label" style="margin-bottom:1mm">Worüber wir sprechen</p>' + dots(["Strategie und Geschäftsmodellfragen", "Führungsfragen", "Lösungswege und Vorgehensweisen abwägen", "Positionierung gegenüber dem Vorstand", "Umgang mit dem Aufsichtsrat", "Steuerung von Konzernunternehmen", "… und vieles mehr"], "sm") + '</div></div>',
    contact_html=contact("Worüber willst Du offen sprechen?", ["daniel", "kerstin_hr"])),
])

# ---------------------------------------------------------------- Impulsvorträge
VORTRAEGE = [("Warum sich niemand für Dein Produkt interessiert.", "Ein Impulsvortrag über Relevanz: warum gute Produkte oft ungehört bleiben – und wie Du das änderst."),
             ("Strategie, die endlich ankommt.", "Wie Strategie aus der Präsentation raus- und im Alltag ankommt."),
             ("Gründe Deinen stärksten Konkurrenten!", "Der Perspektivwechsel, der blinde Flecken sichtbar macht – bevor es die Konkurrenz tut."),
             ("Strategie für Aufsichtsräte", "Impulsvortrag und Halbtagesschulung: wie der Aufsichtsrat eine Strategie einordnet – auf Wunsch mit Praxisthema und Zertifikat.")]
P["impulsvortraege"] = ("emerald", "Impulsvorträge – empiria", [
  cover("Impulsvorträge", 'Impulse, <span class="hl">die nachwirken.</span> Nicht nur unterhalten.',
        "Vorträge aus echter Beratungserfahrung – pointiert, diskussionsstark und mit einer klaren eigenen Haltung. Für Kickoffs, Vertriebstagungen oder Führungskräfte-Events.",
        S.load("impulsvortraege"),
        [("Thema 01", "Relevanz"), ("Thema 02", "Strategie im Alltag"), ("Thema 03", "Perspektivwechsel"), ("Thema 04", "Aufsichtsräte")]),
  page(
    sec("Unser Ansatz", 'Impulse, die <span class="hl">eine Haltung haben.</span>', "Kein Standard-Vortrag von der Stange, sondern eine klare These, die zum Nachdenken und Diskutieren einlädt."),
    cards([("star", "Aus echter Erfahrung", "Jeder Vortrag speist sich aus echten Projekten und Beratungserfahrung – keine austauschbare Theorie."),
           ("target", "Auf Deinen Anlass zugeschnitten", "Ob Kickoff, Vertriebstag oder Führungskräfte-Tagung – der Vortrag passt zu Deinem Anlass."),
           ("chats", "Diskussionsstark", "Pointiert und mit klarer Haltung, damit im Anschluss wirklich diskutiert wird – nicht nur genickt.")], 3),
    who("Für welche Anlässe", [
      "Kickoffs, bei denen der Ton für das Jahr gesetzt wird",
      "Vertriebstagungen mit vielen Teilnehmenden",
      "Führungskräfte-Events, die nachwirken sollen",
      "Strategietage, an denen Denkmuster aufbrechen sollen",
    ], style="margin-top:11mm"),
    band("Für Deinen Anlass", "Wenn ein Impuls mehr bewirken soll als ein weiterer Foliensatz.", extra=chips(["Kickoff", "Vertriebstagung", "Führungskräfte-Event", "Strategietag", "Gremium &amp; Aufsichtsrat"], style="margin-top:4mm"), style="margin-top:11mm"),
  ),
  page(
    stage("Unsere Impulsvorträge", 'Vier Themen. Eine Wirkung.',
          "Wähle das Thema – wir passen den Vortrag auf Deinen Anlass an.",
          wm="mic", boden=True,
          inhalt=cards([
            (None, "Warum sich niemand für Dein Produkt interessiert.",
             "Ein Impulsvortrag über Relevanz: warum gute Produkte oft ungehört bleiben – und wie Du das änderst.<br><br><b>Für Vertriebstagungen und Produktbereiche, die ihre Zielgruppe neu erreichen wollen.</b>"),
            (None, "Strategie, die endlich ankommt.",
             "Wie Strategie aus der Präsentation raus- und im Alltag des Teams ankommt.<br><br><b>Für Führungskräfte-Events und Kickoffs, bei denen eine Strategie getragen werden muss.</b>"),
            (None, "Gründe Deinen stärksten Konkurrenten!",
             "Der Perspektivwechsel, der blinde Flecken sichtbar macht – bevor es die Konkurrenz tut.<br><br><b>Für Strategietage und Führungsrunden, die aus eingefahrenen Mustern herauswollen.</b>"),
            (None, "Strategie für Aufsichtsräte",
             "Impulsvortrag und Halbtagesschulung: wie der Aufsichtsrat eine Strategie einordnet – auf Wunsch mit Zertifikat.<br><br><b>Für Aufsichtsräte und Gremien, die Strategien fundiert beurteilen müssen.</b>"),
          ], 2, numbered=True, style="margin-top:6mm")
          + '<p class="note">Umfang, Dauer und Investition stimmen wir auf Deinen Anlass ab – vom Impuls auf der Tagung bis zur Halbtagesschulung.</p>'),
    ),
  page(
    sec("Kontakt", 'Welcher Impuls passt <span class="hl">zu Deinem Event?</span>',
        "Sag uns, worum es bei Deinem Anlass geht und wen Du im Raum hast – wir schlagen Dir den Vortrag vor, der dort am meisten bewegt."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel"])),
])

def vortrag(slug, h1, lead, sketch, cards3, facts_theme, question, why):
    return ("emerald", "Impulsvortrag – empiria", [
      cover("Impulsvortrag", h1, lead, sketch, [("Format", "Impulsvortrag"), ("Thema", facts_theme), ("Anlass", "Kickoff, Tagung, Event"), ("Referent", "Daniel Ströbel")]),
      page(
        sec("Der Vortrag", question, *why),
        cards(cards3, 3, style="margin-top:9mm"),
        who("Für wen der Vortrag gedacht ist", [
          "Führungskräfte-Tagungen und Kickoffs in der Versicherungsbranche",
          "Vertriebstagungen, die einen echten Impuls statt Folien brauchen",
          "Strategietage, an denen eine Haltung gefragt ist",
          "Runden, in denen danach weitergedacht werden soll",
        ], style="margin-top:10mm"),
        chips(["Kickoff", "Vertriebstagung", "Führungskräfte-Event", "Strategietag"], style="margin-top:9mm"),
        contact_html=contact("Dieser Impuls für Dein Event?", ["daniel"])),
    ])

P["vortrag-1"] = vortrag("vortrag-1", 'Warum sich niemand <span class="hl">für Dein Produkt</span> interessiert.',
    "Ein wachrüttelnder Impuls darüber, warum Qualität allein nicht überzeugt – und was ein Produkt wirklich braucht, damit es gehört, verstanden und gewollt wird.",
    S.vortrag1(), [("eye", "Ehrlich", "Kein Motivations-Bla-Bla – eine klare Analyse, warum Botschaften verpuffen."), ("star", "Nah dran", "Beispiele aus echten Projekten statt austauschbarer Theorie."), ("check", "Umsetzbar", "Konkrete Ansatzpunkte, die am nächsten Tag im Job funktionieren.")],
    "Relevanz", 'Gute Produkte bleiben <span class="hl">oft ungehört.</span>',
    ["Qualität allein überzeugt nicht. Dieser Impuls zeigt, was ein Produkt wirklich braucht, damit es gehört, verstanden und gewollt wird – und wie Du das änderst."])
P["vortrag-2"] = vortrag("vortrag-2", 'Strategie, die <span class="hl">endlich ankommt.</span>',
    "Die beste Strategie nützt nichts, wenn sie in der Schublade landet. Dieser Vortrag zeigt, wie Strategie so kommuniziert wird, dass sie im Alltag Deines Teams tatsächlich ankommt – und wirkt.",
    S.vortrag2(), [("chat", "Verständlich", "Strategie in einer Sprache, die jede Ebene im Unternehmen versteht."), ("route", "Verankert", "Zeigt, wie aus Folien echte Entscheidungen im Alltag werden."), ("spark", "Mitreißend", "Macht Strategie greifbar statt abstrakt – und schafft echte Zustimmung.")],
    "Strategie im Alltag", 'Raus aus der Schublade, <span class="hl">rein in den Alltag.</span>',
    ["Strategie scheitert selten am Inhalt, sondern daran, dass sie im Alltag nicht ankommt. Dieser Impuls zeigt, wie aus Folien echte Entscheidungen werden."])
P["vortrag-3"] = vortrag("vortrag-3", 'Gründe Deinen <span class="hl">stärksten Konkurrenten!</span>',
    "Ein provokanter Perspektivwechsel: Was, wenn Du selbst der schärfste Angreifer auf Dein eigenes Geschäftsmodell wärst? Dieser Vortrag deckt blinde Flecken auf, bevor es jemand anders tut.",
    S.vortrag3(), [("bolt", "Provokant", "Stellt bequeme Wahrheiten über das eigene Geschäftsmodell infrage."), ("tool", "Konkret", "Ein Denkwerkzeug, das Teams direkt selbst anwenden können."), ("eye", "Wachrüttelnd", "Macht sichtbar, wo Angriffsfläche entsteht – bevor es teuer wird.")],
    "Perspektivwechsel", 'Was, wenn Du <span class="hl">Dein eigener Angreifer</span> wärst?',
    ["Wer sein Geschäftsmodell mit den Augen des stärksten Konkurrenten betrachtet, sieht blinde Flecken, bevor es jemand anders tut – und kann rechtzeitig handeln."])

# ---------------------------------------------------------------- capiamo
P["capiamo"] = ("capiamo", "capiamo · Fachbereich & IT – empiria", [
  cover("capiamo · Fachbereich &amp; IT", 'Fachbereich trifft IT. <span class="hl">Und es läuft.</span>',
        ["<b>capiamo</b> – italienisch für „wir verstehen“. Wir übersetzen zwischen Fachbereich und IT, bringen Themen auf den Punkt und steuern die Umsetzung – so lange, bis das Richtige herauskommt."],
        S.load("capiamo"),
        [("Schritt 01", "Strategie verstehen"), ("Schritt 02", "Anforderungen ableiten"), ("Schritt 03", "Umsetzung steuern")]),
  page(
    sec("Das Problem", "„Die verstehen mich einfach nicht – wir reden so oft aneinander vorbei!“",
        "Das hören wir regelmäßig – aus dem Vertrieb, aus den Fachbereichen und aus der IT. Jede Seite hat recht, aus ihrer Sicht. Was fehlt, ist jemand, der beide Sprachen spricht."),
    cards([("clock", "Themen bleiben liegen", "… bis jemand danach fragt. Keiner fühlt sich zuständig, und das Thema verliert an Fahrt."),
           ("target", "Anforderungen verfehlen den Kern", "Die IT setzt um, was aufgeschrieben wurde – aber nicht das, was eigentlich gebraucht wird."),
           ("flag", "Entscheidungen ziehen sich", "Vorstand und Gremien fehlt eine klare Vorlage – also wird vertagt statt entschieden.")], 3),
    feat("Der eigentliche Engpass", "Er sitzt zwischen Fachbereich und IT.",
         "Hier braucht es Verständnis für beide Seiten: sehen, wo der Schmerz wirklich sitzt, den Kern lösen und das Thema so in Richtung IT übersetzen, dass am Ende das Richtige herauskommt.", style="margin-top:10mm"),
    sec("Der Mehrwert", "Sobald wir dabei sind, läuft das Thema.", "Niemand muss mehr nachhaken. Es tut sich etwas – systematisch und in die richtige Richtung.", style="margin-top:12mm"),
    checks(["Themen kommen voran, statt liegen zu bleiben", "Fachbereich, Vertrieb und IT meinen dasselbe", "Vorlagen, auf deren Basis Gremien entscheiden", "Tools und Prozesse für die Zukunft"], "cols2", "margin-top:4mm"),
  ),
  page(
    sec("Unsere Rolle", 'Zuhörer. Übersetzer. <span class="hl">Umsetzungs-Sichersteller.</span>', "Wir fragen aus verschiedenen Perspektiven, skizzieren mit und bringen Themen auf den Punkt – und dann bleiben wir dran, bis sie umgesetzt sind."),
    stations([("", "Strategie und Zielsetzung verstehen", "Wir klären, was das Unternehmen erreichen will und wo der Schmerz wirklich sitzt – nicht nur, was gerade auf dem Tisch liegt."),
              ("", "Fachliche Anforderungen ableiten", "Wir strukturieren das Thema und übersetzen es so in Richtung IT, dass beide Seiten dasselbe darunter verstehen."),
              ("", "(IT-)Umsetzung steuern", "Wir treiben das Projekt voran, nehmen das Team mit und bereiten Themen so auf, dass Vorstand und Gremien entscheiden können.")]),
    sec("Warum wir das können", "Zwei Perspektiven, ein eingespieltes Team.", style="margin-top:12mm"),
    '<div class="two" style="margin-top:6mm">' +
      '<div class="prof"><img src="assets/ansprechpartner-rick.webp" alt=""><div><h3>Rick-Marcel Richter</h3><small>IT &amp; Transformation</small><p>Kennt Versicherer, Vertrieb und Softwareanbieter. Kein Nerd im Hinterzimmer, sondern Umsetzungs- und Projektleitungsprofi.</p></div></div>' +
      '<div class="prof"><img src="assets/ansprechpartner-daniel.webp" alt=""><div><h3>Daniel Ströbel</h3><small>Strategiehandwerker</small><p>Fragt aus verschiedenen Perspektiven, skizziert live mit und bringt komplexe Themen auf eine Seite.</p></div></div>' +
    '</div>',
    band("Ein Vorstand eines anderen Versicherers", None, extra='<p style="margin-top:1mm;font-weight:500;font-size:10.5pt;line-height:1.55;color:var(--ink)">„Eigentlich stellt Daniel viele Fragen aus verschiedenen Perspektiven, skizziert dabei mit – und wenn er es Dir hinterher zeigt, denkst Du: Ja genau, das habe ich gemeint!“</p>', style="margin-top:8mm;padding:5mm 7mm"),
  ),
  page(
    sec("So arbeiten wir", "Erst klären. Dann steuern.",
        "Am Anfang steht eine saubere Auftragsklärung: gewünschtes Ergebnis, Meilensteinplan, Kommunikationsmatrix. Danach übernehmen wir das Projektmanagement, nehmen Dein Team mit – und Vorstand und Gremien erhalten regelmäßig Unterlagen, auf deren Basis sie entscheiden können."),
    who("Für wen das gemacht ist", [
      "Fachbereiche, deren Themen in der IT liegen bleiben",
      "Vorstände und Gremien, denen eine klare Entscheidungsvorlage fehlt",
      "Häuser ohne eigene Übersetzerrolle zwischen beiden Welten",
    ], style="margin-top:9mm"),
    stage("Unsere Themen", "Drei Einstiege. Ein Ziel: Es läuft.", wm="puzzle", boden=True,
          inhalt=cards([("route", "Flaschenhals-Management", "Beauftragung und Koordination zwischen Fachbereich und IT – damit nichts im Nadelöhr stecken bleibt."),
           ("cycle", "Prozessoptimierung", "Abläufe verstehen, Engpässe sichtbar machen, Prozesse so aufsetzen, dass Tools sie unterstützen."),
           ("layers", "(Multi-)Projektbegleitung", "Von der Auftragsklärung bis zur Umsetzung: einzelne Projekte oder ein ganzes Portfolio.")], 3, style="margin-top:5mm")),
    ),
  page(
    sec("Kontakt", 'Wo hakt es zwischen <span class="hl">Fachbereich und IT?</span>',
        "Schildere uns, welches Thema bei Euch feststeckt – wir sagen Dir, wo wir ansetzen würden und wie ein erster Schritt aussieht."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag – kurze Wege statt langer Abstimmungsrunden."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "rick"])),
])

# ---------------------------------------------------------------- Workshops
# Die Uebersichtsseite hatte bisher einen Download-Kasten, aber keine Quelle im
# Generator - das PDF lag nur als fertige Datei im Repo und liess sich nicht
# mitpflegen. Inhalte 1:1 von workshops.html.
P["workshops"] = ("magenta", "Workshops – empiria", [
  cover("Workshops", 'Workshops, die wirken. <span class="hl">Nicht nur Theorie.</span>',
        ["Ob Künstliche Intelligenz, eine neue Landingpage oder die Moderation Deines nächsten Workshops: Aus unzähligen Projekten sind Formate entstanden, die in der Versicherungsbranche wirklich tragen.",
         "<b>Echte Tools, echte Ergebnisse – und eine Moderation, die Dein Team mitnimmt.</b>"],
        S.load("ki-zum-anfassen"),
        [("Format 01", "KI zum Anfassen"), ("Format 02", "Sprint Landingpage"), ("Format 03", "Workshop-Moderation")]),
  page(
    sec("Unser Ansatz", 'Workshops, die nicht bei der <span class="hl">Theorie bleiben.</span>',
        "Wir gehen direkt in die Anwendung – mit echten Tools, echten Fällen aus Deinem Alltag und einer Moderation, die trägt."),
    cards([("bolt", "Direkt anwendbar", "Kein Arbeitskreis ohne Praxis: Wir arbeiten mit echten Tools und echten Fällen aus Deinem Alltag."),
           ("target", "Auf Dein Team zugeschnitten", "Jeder Workshop ist auf Deinen Anwendungsfall und Dein Team zugeschnitten – nicht von der Stange."),
           ("team", "Professionell moderiert", "Klare Strukturen, gute Stimmung und Ergebnisse, mit denen sich weiterarbeiten lässt.")], 3),
    stage("Unsere Workshops", "Drei Formate. Ein Ziel: Ergebnisse.",
          "Wähle das Format – wir bringen Dein Team ans Ziel.",
          wm="grid", boden=True,
          inhalt=cards([
            (None, "KI zum Anfassen",
             "Echte KI-Tools, echte Usecases aus der Versicherungsbranche – Schluss mit Arbeitskreisen ohne Praxis.<br><br><b>½ bis 2 Tage · ab 2.500 €</b>"),
            (None, "Sprint Landingpage",
             "Deine Landingpage in 48 Stunden live – für den Moment, in dem es schnell gehen muss.<br><br><b>2 Tage plus Onboarding · 15.850 €</b>"),
            (None, "Moderation Deines Workshops",
             "Gezielte Aktivierung, Perspektivwechsel und Handlungsklarheit – für Ergebnisse, mit denen sich weiterarbeiten lässt.<br><br><b>Umfang nach Anlass</b>"),
          ], 3, numbered=True, style="margin-top:6mm")),
  ),
  page(
    sec("Für wen das gemacht ist", 'Teams, die weiterkommen wollen – <span class="hl">nicht nur tagen.</span>',
        "Unsere Workshops entstehen aus Projekten in der Versicherungsbranche. Deshalb sitzen die Beispiele, und deshalb kommt Dein Team schneller ins Arbeiten."),
    who("Typische Anlässe", [
      "Teams, die KI endlich praktisch nutzen wollen statt darüber zu reden",
      "Bereiche mit kurzfristigem Vertriebsdruck und einem Thema, das online muss",
      "Neustrukturierungen, Rollenklärungen und Führungswechsel",
      "Strategietage, die zu Ergebnissen führen sollen statt zu Themensammlungen",
    ], style="margin-top:8mm"),
    stage("Was Du bekommst", "Ergebnisse, mit denen sich weiterarbeiten lässt.",
          wm="check", boden=True,
          inhalt=checks(["Ergebnisse aus echten Fällen Deines Hauses, nicht aus Fallstudien",
                         "Eine Dokumentation, die auch Wochen später noch verständlich ist",
                         "Klare nächste Schritte statt einer Liste offener Punkte",
                         "Eine Moderation, die auch bei schwierigen Themen trägt"], style="margin-top:6mm")),
  ),
  page(
    sec("Kontakt", 'Bereit für einen Workshop, <span class="hl">der wirklich weiterbringt?</span>',
        "Kurze Wege statt langer Abstimmungsrunden: Sag uns, worum es geht und wer dabei sein soll – wir schlagen Dir das passende Format vor."),
    stations([
      ("Schritt 01", "Kurz schildern", "Worum geht es, wer ist beteiligt und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Zeitnah Rückmeldung", "Wir melden uns mit Rückfragen und einem konkreten Vorschlag zum passenden Format."),
      ("Schritt 03", "Verbindlich festzurren", "Umfang, Termine und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel", "kerstin_hr", "noah_ki"])),
])

# ------------------------------------------- Strategie für Aufsichtsräte
# Ebenfalls ohne Generator-Quelle im Repo. Inhalte 1:1 von
# strategie-aufsichtsrat.html.
P["strategie-fuer-aufsichtsraete"] = ("strategie", "Strategie für Aufsichtsräte – empiria", [
  cover("Impulsvortrag &amp; Schulung für Aufsichtsräte", 'Strategie für <span class="hl">Aufsichtsräte.</span>',
        "Beraten, hinterfragen, überwachen: Woran erkennt ein Aufsichtsrat, ob eine Strategie trägt – und welche Fragen muss er dem Vorstand stellen?",
        S.strategie(),
        [("Dauer", "Halber Tag"), ("Format", "Vortrag &amp; Schulung"), ("Nachweis", "Mit Zertifikat"), ("Für wen", "Versicherungsunternehmen")]),
  page(
    sec("Der Tag", 'Vier Stationen. <span class="hl">Ein klarer Blick.</span>',
        "Der Aufsichtsrat soll die Strategie des Vorstands beraten und ihre Umsetzung überwachen. Dafür braucht er ein klares Verständnis davon, woran man eine tragfähige Strategie überhaupt erkennt."),
    stage(None, None, wm="compass", boden=True, inhalt=stations([
      ("Impuls", "Wie entsteht Strategie?", "Wie eine Strategie im Versicherungsunternehmen entsteht – und was sie tragfähig macht."),
      ("Rolle", "Beraten oder überwachen?", "Was der Aufsichtsrat bei der Strategie leisten soll – und wo seine Rolle endet."),
      ("Fragen", "Was fragen wir den Vorstand?", "Die Fragen, an denen sich zeigt, ob eine Strategie wirklich durchdacht ist."),
      ("Kennzahlen", "Gelingt die Umsetzung?", "Die Kennzahlen, an denen der Aufsichtsrat erkennt, ob die Strategie ankommt."),
    ], style="margin-top:2mm")),
  ),
  page(
    sec("Aus einem Guss", 'Unser Vortrag. <span class="hl">Eure Strategie.</span>',
        "Besonders wirksam wird der Tag, wenn der Vorstand ein eigenes Praxisthema einbringt – die Unternehmens- oder die Vertriebsstrategie.",
        "Das stimmen wir im Vorfeld mit dem Vorstand ab, damit Vortrag und Praxisthema zusammenpassen und eine Einheit bilden. <b>So diskutiert der Aufsichtsrat nicht über ein Lehrbuchbeispiel, sondern über das eigene Haus.</b>"),
    stage("Aus der Praxis", "Nicht aus dem Lehrbuch.", wm="shield", boden=True,
          inhalt=checks(["Vorstandsklausuren konzipiert",
                         "Strategien auf Konzernebene entwickelt",
                         "Führungskräfte bis auf Aufsichtsratsebene begleitet",
                         "Aufsichtsräte bereits mehrfach geschult",
                         "Zertifikat als Nachweis für jedes Mitglied",
                         "Als Fortbildung anrechenbar"], cls="cols2", style="margin-top:6mm")),
  ),
  page(
    sec("Das Ergebnis", 'Euer Gremium ordnet eine Strategie <span class="hl">fundiert ein.</span>',
        "Ihr stellt die richtigen Fragen und erkennt an Kennzahlen, ob die Umsetzung gelingt – und könnt die Strategie des Vorstands beurteilen, statt sie entgegenzunehmen."),
    stations([
      ("Schritt 01", "Kurz schildern", "Wie viele Mitglieder, welcher Anlass und bis wann soll es stehen? Eine Mail oder ein Anruf reicht."),
      ("Schritt 02", "Praxisthema abstimmen", "Wir klären mit dem Vorstand, welches eigene Thema der Schulung zugrunde liegt."),
      ("Schritt 03", "Verbindlich festzurren", "Termin, Umfang und Investition klären wir gemeinsam, bevor es losgeht."),
    ], style="margin-top:10mm"),
    contact_html=contact("Dein direkter Draht zu uns", kicker="", people=["daniel"])),
])
