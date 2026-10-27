"""Experimentierfeld Runde 3 (Daniel, 27.10.2026): Ton kalibrieren – drei Themen, je vier Stufen.
Stufe 1 = bisheriger Lehrbuch-Ton · 2 = Real Talk mit Learning · 3 = Real Talk + Mensch + tiefes Learning · 4 = zu viel.
Alles aus Daniels Antworten (Rohantworten 12.–15.10., Diktate 27.10.); Offenes steht je Thema unter „offen“.
"""

STUFEN = [("1", "Bisher", "Lehrbuch-Ton der aktuellen Serie – zum Vergleich"),
          ("2", "Real Talk", "direkt, auf den Punkt, mit klarem Learning"),
          ("3", "Real Talk + Mensch", "dein eigener Moment, dein Gefühl, ein Learning als echtes Werkzeug"),
          ("4", "Zu viel", "bewusst drüber, damit die Grenze sichtbar wird")]

THEMEN = [
    dict(titel="KI-Schnellboote", baustein="Geschäftsmodell und Innovation",
         quelle="Diktat 27.10. (Verbote von oben, Schnellboote erwartet) · Rohantworten 12.10. (KI im eigenen Haus) und 13.10. (KI selbst beigebracht)",
         offen="Stufe 2–4: Die beiden Sätze aus Vorstandsrunde und IT-Mail sind typisch zugespitzt, nicht wörtlich erlebt. Hast du einen echten Satz aus einem Haus, ersetzt er sie.",
         texte=[
"""KI-Strategie im Versicherungsunternehmen: Rahmen und Freiraum in Balance bringen

Viele Versicherer haben klare Regeln für den Einsatz von KI definiert. Das ist wichtig, denn Datenschutz und Regulierung setzen Grenzen.

Gleichzeitig erwarten Vorstände Innovation und neue Ideen von ihren Mitarbeitenden.

Damit beides zusammenpasst, braucht es drei Dinge:

• eine klare KI-Strategie
• definierte Experimentierräume
• klare Verantwortlichkeiten

So entsteht Innovation im sicheren Rahmen.""",
"""In der Vorstandsrunde heißt es: „Wir brauchen bei KI mehr Mut. Denkt quer, baut Schnellboote, kommt mit Ideen.“

In der nächsten Mail aus der IT steht: „Die Nutzung externer KI-Tools ist bis auf Weiteres untersagt.“

Ich kenne gerade kaum ein Haus, in dem es nicht genau so läuft. Und es nervt mich gewaltig.

Ihr könnt nicht alles verbieten und gleichzeitig erwarten, dass eure Leute innovativ sind.

Was dann passiert, sehe ich überall: Die Leute nutzen privat, was dienstlich verboten ist. Abends, am eigenen Laptop. Und schicken sich das Ergebnis per Mail ins Büro.

Damit habt ihr genau das, was ihr verhindern wolltet. Nur ohne jede Kontrolle.

Was funktioniert, ist erstaunlich einfach:

• Eine klare Ansage, wofür KI im Haus da sein soll. In zwei Sätzen.
• Ein abgegrenzter Raum, in dem ausprobiert werden darf. Mit echten Tools, ohne Kundendaten.
• Eine Person, die entscheidet, was aus diesem Raum in den Alltag wandert.

Dafür braucht es keine Taskforce.

Wer Schnellboote will, muss ihnen erst einmal Wasser geben.""",
"""Ich habe mir im letzten Jahr KI komplett selbst beigebracht. Abends, beim Bauen, mit vielen Nerven, die auf der Strecke geblieben sind.

Gelernt habe ich dabei vor allem eines: KI lernst du nur im Tun.

Und genau das verbieten gerade viele Häuser.

In der Vorstandsrunde heißt es: „Denkt quer, baut Schnellboote.“ In der nächsten Mail aus der IT: „Externe KI-Tools sind bis auf Weiteres untersagt.“

Das nervt mich, ehrlich gesagt, gewaltig. Weil ich sehe, was dann passiert: Die Leute machen es trotzdem. Privat, abends, am eigenen Laptop. Und schicken sich das Ergebnis per Mail ins Büro.

So sieht ein Schnellboot aus, das tatsächlich fährt:

1. Ein Satz vom Vorstand: Wofür soll KI bei uns da sein? Mehr Tempo im Service? Bessere Entscheidungen? Weniger Routine?
2. Ein Spielfeld mit klaren Linien: Diese Tools sind erlaubt. Diese Daten nie. Alles dazwischen darf ausprobiert werden.
3. Vier Wochen, drei echte Fälle aus dem Alltag. Am Ende zählt, was schneller oder besser geworden ist.
4. Ein Termin, an dem jemand entscheidet: Was davon geht in den Regelbetrieb?

Damit gebt ihr Freiraum und behaltet trotzdem die Kontrolle.

Und an alle, die gerade heimlich privat ausprobieren: Ihr zeigt jeden Tag, dass der Bedarf längst da ist.""",
"""LIEBE VORSTÄNDE,

ihr wollt KI-Schnellboote? Dann hört auf, sie im Trockendock festzuketten.

„Denkt quer!“ – aber bitte nur mit Tools, die die IT vor 2019 freigegeben hat.
„Seid mutig!“ – aber bitte erst nach Taskforce, Arbeitskreis und Lenkungsausschuss.
„Kommt mit Ideen!“ – aber bitte nichts ausprobieren.

Wisst ihr, was eure besten Leute gerade machen? Sie bauen eure Schnellboote. Nachts. Am Küchentisch. Auf dem privaten Handy.

Herzlichen Glückwunsch: Eure Innovation findet statt. Nur eben ohne euch.

Entweder ihr gebt das Wasser frei. Oder ihr hört auf, Boote zu bestellen.""",
         ]),
    dict(titel="Vorstandsvorlage", baustein="Komplexe Themen strukturieren und kommunizieren",
         quelle="Rohantworten 12.10. (drei Fragen eines Vorstands; Vorstandsklausuren bei der SV; „falsche Flugebene“) · Stufe 1 = ursprünglicher Entwurf, Stufe 2 = veröffentlicht am 21.10.",
         offen="Stufe 3: „Seitdem gehe ich vor jeder Vorlage drei Fragen durch“ ist meine Ableitung aus deinen Klausur-Erfahrungen – stimmt das so?",
         texte=[
"""Viele Vorstandsvorlagen sind vollständig und trotzdem nicht entscheidbar.

Wer ein Fachthema einbringt, präsentiert meist bis ins letzte Detail. Der Vorstand weiß danach viel, nur nicht, was das Thema für das Unternehmen bedeutet.

Dann geht es in die nächste Schleife.

Drei Fragen reichen, in dieser Reihenfolge:

Why. Welche Bedeutung hat dieses Thema für uns und unser Unternehmen? Kurz und auf den Punkt.

How. Wie gehen wir grundsätzlich vor? Grundsätzlich heißt: ohne die Einzelprobleme, solange die Gesamtwirkung nicht klar ist.

What next. Was ist der konkrete nächste Schritt, damit es vorangeht?

Das klingt einfach, und trotzdem lässt es sich sehr ungeschickt aufbauen.

Prüfe deine nächste Vorlage gegen diese drei Fragen, bevor du an den Folien feilst.""",
"""„Danke. Bitte bereiten Sie das noch einmal auf.“

Drei Wochen Arbeit. Zwanzig Minuten Vorstand. Ein Satz.

Und du gehst raus und fragst dich, was du falsch gemacht hast.

Ich sage es dir ehrlich: Am Thema lag es nicht. Du hast zu viel gewusst. Und alles erzählt.

Wer sein Thema richtig gut kennt, kann am schlechtesten weglassen. Jedes Detail fühlt sich wichtig an. Ist es auch. Nur nicht für diese eine Entscheidung.

Der Vorstand denkt in dem Moment nicht: schwaches Thema. Er denkt: Was soll ich damit jetzt machen?

Er will drei Dinge wissen. Mehr nicht.

Why?
Was bedeutet das Thema für unser Unternehmen?

How?
Wie gehen wir grundsätzlich vor, um das Ergebnis zu erreichen? Die Details will er erst sehen, wenn er Ja gesagt hat.

What next?
Was muss heute entschieden werden, damit es weitergeht?

Drei Fragen, drei Sätze. Bekommst du die nicht hin, retten dich auch keine vierzig Folien.""",
"""Ich habe jahrelang Vorstandsklausuren vorbereitet. Mehrtägig, sechs Vorstände, sechs Charaktere. Alle hochintelligent, alle hocherfahren.

Was mich bis heute beeindruckt: wie schnell diese Runde erfasst hat, worum es geht. Wenn die Vorbereitung stimmte.

Und wie schnell es gekippt ist, wenn sie nicht stimmte. Je mehr ein Fachbereich auf Details gepocht hat, die keine Rolle spielten, desto zäher wurde es. Bis der Satz fiel: „Auf der Ebene brauchen wir nicht weiterzudiskutieren.“

Das Gegenteil habe ich auch erlebt. Bei wichtigen Themen hat oft einer einen einzigen klaren Satz als Grundrichtung gesagt. Dieser eine Satz war besser als jedes Management Summary. Weil danach alle wussten, woran sie sich messen.

Seitdem gehe ich vor jeder Vorlage drei Fragen durch:

Why?
Was bedeutet das Thema für unser Unternehmen? Kannst du es in einem Satz sagen, ohne Fachbegriff?

How?
Wie gehen wir grundsätzlich vor, um das Ergebnis zu erreichen? Steht da ein Weg oder eine Liste von Einzelproblemen?

What next?
Was muss heute entschieden werden, damit es weitergeht? Steht die Frage, über die entschieden wird, wörtlich auf der Seite?

Und ein letzter Test: Welcher eine Satz bleibt übrig, wenn der Vorstand deine Vorlage zuklappt? Findest du ihn nicht, findet ihn der Vorstand auch nicht.""",
"""Deine Vorstandsvorlage hat 47 Folien? Glückwunsch. Du hast gerade eine Entscheidung verhindert.

Der Vorstand liest Folie 1. Blättert zu Folie 12. Fragt nach Folie 3. Und vertagt.

Weißt du, wie viele Folien ein Vorstand für eine Entscheidung braucht? Eine. Mit einem Satz darauf.

Alles andere ist Selbstschutz. Damit hinterher keiner sagen kann, du hättest etwas vergessen.

Herzlichen Glückwunsch, du hast nichts vergessen. Nur das Wichtigste: dass jemand entscheiden kann.

Lösche 46 Folien. Heute noch.""",
         ]),
    dict(titel="Bereich neu gründen", baustein="Strategie in den Alltag überführen",
         quelle="Rohantworten 12.10. (Strategie: Wie läuft es bei dir ab? – Zukunftsbild, Team nicht zu früh einbinden, drei Gespräche, Spiegeln) · Themenliste 30 · Stufe 1 = früherer Firmenprofil-Entwurf",
         offen="Stufe 3: „Das ist der Moment, auf den ich jedes Mal hinarbeite“ – passt das zu deinem Gefühl im Spiegelgespräch?",
         texte=[
"""Wie würdest du deinen Bereich aufbauen, wenn du ihn heute neu gründen würdest?

Mit dieser Frage beginnen wir, wenn es um das Geschäftsmodell der Zukunft geht. Dazu gehören drei Unterfragen: Würdest du die Aufgaben noch genauso zuschneiden? Würdest du dich an derselben Stelle der Wertschöpfung positionieren? Würdest du dieselben Zielgruppen bedienen?""",
"""Wenn ich mit einer Führungskraft über die Zukunft ihres Bereichs rede, stelle ich ziemlich früh eine Frage, die alles durcheinanderbringt: Wie würdest du deinen Bereich bauen, wenn du ihn heute neu gründen würdest?

Die meisten Bereiche sind nicht gebaut. Sie sind gewachsen. Zuständigkeiten, Schnittstellen, Abläufe: irgendwann entstanden, weil es gerade gebraucht wurde. Und dann geblieben.

Wer neu gründet, darf all das infrage stellen. Genau da wird es spannend.

Ohne dieses Bild gibt es keine gescheite Strategie. Mit ihm ergibt sie sich fast von allein, als Weg von heute dorthin.

Damit daraus keine Wunschliste wird, drei Prüffragen:

• Welches Problem hat dein Kunde wirklich?
• Wie löst du es?
• Und ist er überhaupt bereit, es zu lösen?

Und ein Rat: Beantworte die Frage zuerst allein. Stellst du sie gleich deinem Team, fragt sich jeder zuerst, ob es seinen Job danach noch gibt. Mit dieser Sorge im Kopf denkt keiner frei.""",
"""Die meisten Führungskräfte denken bei „Strategie“ sofort an zwei Tage Workshop, Moderationskoffer und ein Team, das Kärtchen an die Wand klebt.

Ich fange anders an. Mit einer Frage: Wie würdest du deinen Bereich bauen, wenn du ihn heute neu gründen würdest?

Dafür brauche ich keine zwei Tage. Ich brauche dich, zwei, drei Mal eine Stunde, am Telefon reicht. Du bereitest nichts vor. Keine Folien. Du erzählst, was dir durch den Kopf geht, und ich frage, unterbreche, frage weiter.

Danach lege ich dir hin, was ich gehört habe. Strukturiert, neben der Logik des Geschäftsmodells Versicherung. Das ist der Moment, auf den ich jedes Mal hinarbeite: wenn mein Gegenüber merkt, dass da plötzlich ein Bild steht, das er die ganze Zeit im Kopf hatte, aber nie ausgesprochen hat.

Warum ich das Team am Anfang bewusst draußen lasse? Das Zukunftsbild sieht immer anders aus als das heutige. Wer es zu früh im Team diskutiert, erzeugt Unsicherheit. Viele fragen sich dann zuerst, ob es ihren Job danach noch gibt. Mit dieser Sorge denkt keiner frei.

Zum Mitnehmen, auch ohne mich:

1. Nimm dir eine Stunde und beantworte die Frage allein. Laut, am besten vor jemandem, dem du vertraust.
2. Prüfe dein Bild an drei Fragen: Welches Problem hat dein Kunde wirklich? Wie löst du es? Ist er bereit, es zu lösen?
3. Erst dann: Wen brauchst du, damit es Wirklichkeit wird? Das ist der Moment fürs Team.""",
"""Dein Bereich ist ein Museum.

Jede Zuständigkeit hat eine Geschichte. Jede Schnittstelle einen Grund, den keiner mehr kennt. Jeder Ablauf ist so, weil er schon immer so war.

Und du verwaltest das. Mit Hingabe. Seit Jahren.

Mache ein Gedankenexperiment: Morgen früh ist alles weg. Kein Organigramm, keine Prozesse, keine Regeltermine. Nur deine Kunden und ihr Problem.

Was würdest du wieder aufbauen? Ehrlich? Wahrscheinlich die Hälfte.

Und die andere Hälfte? Die verteidigst du gerade in jedem Meeting.

Schließe das Museum. Gründe neu.""",
         ]),
]

# Runde 3b (27.10.2026): Stufe 3 gekürzt nach Ton-Regler – Vorschau in iPhone-Breite
GEKUERZT = [
    ("KI-Schnellboote", """Ich habe mir im letzten Jahr KI komplett selbst beigebracht. Abends, beim Bauen, mit vielen Nerven.

Meine Erkenntnis: KI lernst du nur im Tun.

Genau das verbieten gerade viele Häuser.

Im Vorstand heißt es: „Denkt quer, baut Schnellboote.“
Aus der IT kommt: „Externe KI-Tools sind untersagt.“

Das nervt mich gewaltig.

Denn was passiert? Die Leute machen es trotzdem. Privat, abends, am eigenen Laptop.

So fährt ein Schnellboot wirklich:

1. Ein Satz vom Vorstand, wofür KI da sein soll.
2. Ein Spielfeld: diese Tools ja, diese Daten nie.
3. Vier Wochen, drei echte Fälle aus dem Alltag.
4. Ein Termin, an dem jemand entscheidet, was bleibt.

Freiraum und Kontrolle. Beides geht."""),
    ("Vorstandsvorlage", """Deine Vorstandsvorlage hat 47 Folien? Glückwunsch. Du hast gerade eine Entscheidung verhindert.

Ich habe jahrelang Vorstandsklausuren vorbereitet. Sechs Vorstände, sechs Charaktere, alle hocherfahren.

Stimmte die Vorbereitung, war in Minuten klar, worum es geht.

Pochte ein Fachbereich auf Details, kippte es. Bis der Satz fiel: „Auf der Ebene brauchen wir nicht weiterzudiskutieren.“

Richtig gut lief es, wenn einer einen einzigen klaren Satz als Richtung sagte. Der war mehr wert als jedes Management Summary.

Seitdem prüfe ich jede Vorlage mit drei Fragen:

Why?
Was bedeutet das Thema für unser Unternehmen? In einem Satz.

How?
Wie gehen wir grundsätzlich vor? Ein Weg, keine Liste von Einzelproblemen.

What next?
Was muss heute entschieden werden? Wörtlich auf der Seite.

Und der letzte Test: Welcher Satz bleibt, wenn der Vorstand zuklappt?"""),
    ("Bereich neu gründen", """Wenn Führungskräfte „Strategie“ hören, denken sie an zwei Tage Workshop und Kärtchen an der Wand.

Ich fange mit einer Frage an: Wie würdest du deinen Bereich bauen, wenn du ihn heute neu gründen würdest?

Dafür brauche ich keine zwei Tage. Zwei, drei Gespräche à eine Stunde. Ohne Vorbereitung, ohne Folien.

Du erzählst. Ich frage, unterbreche, frage weiter.

Dann lege ich dir hin, was ich gehört habe. Und plötzlich steht da ein Bild, das du die ganze Zeit im Kopf hattest.

Das Team kommt bewusst später. Wer zu früh über die Zukunft diskutiert, erzeugt Angst um den eigenen Job. Und mit Angst denkt keiner frei.

Zum Mitnehmen:

1. Beantworte die Frage allein, laut, vor jemandem, dem du vertraust.
2. Prüfe dein Bild: Welches Problem hat dein Kunde? Wie löst du es? Will er es lösen?
3. Erst dann: Wen brauchst du dafür?"""),
]
