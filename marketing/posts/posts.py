"""Inhalt der ersten neun Instagram-Beitraege von Pluralo.

Reihenfolge ist Absicht: Die neun Beitraege beantworten zusammen, wer Pluralo ist,
was es kann, fuer wen, warum, und wie man in Kontakt kommt. Sie gehoeren innerhalb
der ersten zwei bis drei Wochen online, damit das Profil nie halb leer aussieht.

Schreibweisen in den Slide-Texten:
    *Wort*  hebt das Wort im Farbverlauf hervor
    |       erzwingt einen Zeilenumbruch
"""

URL = "pluralo.de"
MAIL = "kontakt@pluralo.de"

POSTS = [
    # ------------------------------------------------------------------ 01
    {
        "nr": 1,
        "slug": "wofuer-pluralo-steht",
        "titel": "Wofür Pluralo steht",
        "typ": "A · Statement",
        "saeule": "Haltung",
        "pin": True,
        "slides": [
            {
                "eyebrow": "Digitalagentur · Andernach",
                "h1": "Websites, die *gefunden werden* und überzeugen.",
                "hsize": 94,
                "align": "end",
            },
        ],
        "caption": """Websites, die gefunden werden und überzeugen.

Wir sind Pluralo, eine Digitalagentur aus Andernach. Wir entwickeln professionelle Websites, überarbeiten bestehende Webauftritte und sorgen dafür, dass Unternehmen, Selbstständige und Vereine bei Google sichtbar werden.

Eine schöne Website nützt wenig, wenn sie niemand findet. Und Sichtbarkeit allein reicht nicht, wenn der Auftritt kein Vertrauen schafft. Deshalb denken wir Design, Technik, Inhalte und Auffindbarkeit von Anfang an zusammen.

Hier zeigen wir ab jetzt, woran wir arbeiten, wie wir dabei vorgehen und was Sie an Ihrem eigenen Auftritt sofort verbessern können.

Schön, dass Sie da sind.

#webdesign #seo #andernach #koblenz #rheinlandpfalz #digitalagentur #websiteerstellen""",
        "hinweis": "Nach dem Posten anpinnen. Das ist dauerhaft die erste Kachel im Profil.",
    },
    # ------------------------------------------------------------------ 02
    {
        "nr": 2,
        "slug": "was-wir-machen",
        "titel": "Was wir machen",
        "typ": "C · Wissen",
        "saeule": "Angebot",
        "slides": [
            {
                "eyebrow": "Leistungen",
                "counter": "01 / 03",
                "h1": "Was wir *machen*",
                "hsize": 118,
                "lead": "Vier Bereiche. Einzeln buchbar|oder sinnvoll kombiniert.",
                "align": "end",
                "swipe": True,
            },
            {
                "eyebrow": "Leistungen",
                "counter": "02 / 03",
                "align": "center",
                "items": [
                    ("Webdesign & Relaunch",
                     "Neue Websites und die Überarbeitung bestehender Auftritte. Klar strukturiert, schnell, auf Anfragen ausgerichtet."),
                    ("SEO & Google-Sichtbarkeit",
                     "SEO-Analyse, Onpage-Optimierung, Google-Unternehmensprofil und echte Bewertungen."),
                ],
            },
            {
                "eyebrow": "Leistungen",
                "counter": "03 / 03",
                "align": "center",
                "start": 3,
                "items": [
                    ("Social Media & Content",
                     "Professionelle Auftritte, eine klare Content-Linie, Foto- und Videoproduktion."),
                    ("Branding & Werbung",
                     "Logo und Corporate Design, Online-Anzeigen, Flyer, Plakate, Speisekarten."),
                ],
                "note": "Kostenloses Erstgespräch auf pluralo.de",
            },
        ],
        "caption": """Vier Bereiche, mit denen wir Unternehmen sichtbar machen.

01 Webdesign und Website-Relaunch
Neue Websites und die Überarbeitung bestehender Auftritte. Klar strukturiert, schnell und darauf ausgelegt, aus Besuchern Anfragen zu machen.

02 SEO und Google-Sichtbarkeit
SEO-Analyse, technische und inhaltliche Onpage-Optimierung, Google-Unternehmensprofil, Bewertungslinks und QR-Code-Lösungen.

03 Social Media und Content
Professionelle Social-Media-Auftritte, eine klare Content-Linie sowie Foto- und Videoproduktion.

04 Branding und Werbung
Logo und Corporate Design, Online-Werbeanzeigen, Flyer, Plakate, Speisekarten und Preislisten.

Sie können mit einer einzelnen Leistung starten oder mehrere Bausteine verbinden. Im kostenlosen Erstgespräch klären wir, was für Ihr aktuelles Ziel wirklich sinnvoll ist.

Schreiben Sie uns eine Nachricht oder rufen Sie an.

#webdesign #seo #branding #socialmedia #andernach #mittelrhein #digitalagentur""",
    },
    # ------------------------------------------------------------------ 03
    {
        "nr": 3,
        "slug": "keine-anfragen",
        "titel": "5 Gründe, warum Ihre Website keine Anfragen bringt",
        "typ": "C · Wissen",
        "saeule": "Wissen",
        "slides": [
            {
                "eyebrow": "Wissen · 01",
                "counter": "01 / 03",
                "h1": "Ihre Website bringt|*keine Anfragen*?|5 häufige Gründe",
                "hsize": 80,
                "align": "end",
                "swipe": True,
            },
            {
                "eyebrow": "Wissen · 01",
                "counter": "02 / 03",
                "align": "center",
                "items": [
                    ("Niemand versteht sofort, was Sie anbieten",
                     "Besucher entscheiden in wenigen Sekunden. Wenn die erste Zeile nicht klar sagt, was Sie tun und für wen, sind sie weg."),
                    ("Der nächste Schritt fehlt",
                     "Kein sichtbarer Kontaktweg, kein Formular, keine Nummer im Blick. Interesse allein wird nicht zur Anfrage."),
                    ("Auf dem Handy ist sie mühsam",
                     "Über die Hälfte der Besucher kommt vom Smartphone. Was dort hakt, ist verloren."),
                ],
            },
            {
                "eyebrow": "Wissen · 01",
                "counter": "03 / 03",
                "align": "center",
                "start": 4,
                "items": [
                    ("Sie lädt zu langsam",
                     "Jede zusätzliche Sekunde kostet Besucher. Zu große Bilder sind die häufigste Ursache."),
                    ("Google zeigt sie nicht",
                     "Ohne gepflegtes Unternehmensprofil und lokale Signale tauchen Sie in der Umgebungssuche nicht auf."),
                ],
                "note": "Welcher Punkt trifft bei Ihnen zu?",
            },
        ],
        "caption": """Fünf Gründe, warum eine Website keine Anfragen bringt.

01 Niemand versteht sofort, was Sie anbieten
02 Der nächste Schritt fehlt
03 Auf dem Handy ist sie mühsam
04 Sie lädt zu langsam
05 Google zeigt sie nicht

Das Gute daran: Keiner dieser fünf Punkte ist ein Grundsatzproblem. Alle lassen sich an einer bestehenden Website beheben, in den meisten Fällen ohne kompletten Relaunch.

Welcher Punkt trifft bei Ihnen am ehesten zu? Schreiben Sie es in die Kommentare oder per Nachricht, dann schauen wir kurz darauf.

#webdesign #website #seo #onlinemarketing #andernach #koblenz #handwerk""",
    },
    # ------------------------------------------------------------------ 04
    {
        "nr": 4,
        "slug": "vorher-nachher",
        "titel": "Vorher und nachher",
        "typ": "B · Arbeit",
        "saeule": "Beweis",
        "pin": True,
        "braucht": "Zwei Screenshots aus einem abgeschlossenen Projekt, jeweils 1080 × 1350 px.",
        "slides": [
            {
                "eyebrow": "Referenz",
                "counter": "01 / 02",
                "h1": "Vorher",
                "hsize": 104,
                "align": "end",
                "swipe": True,
                "slot": "Screenshot vorher|hier einsetzen|1080 × 1350 px",
                "foto": "vorher.png",
            },
            {
                "eyebrow": "Referenz",
                "counter": "02 / 02",
                "h1": "Nachher",
                "hsize": 104,
                "align": "end",
                "slot": "Screenshot nachher|hier einsetzen|1080 × 1350 px",
                "foto": "nachher.png",
            },
        ],
        "caption": """[Branche] aus [Ort]: vorher und nachher.

Die Ausgangslage: [was an der alten Website nicht funktioniert hat, ein bis zwei Sätze].

Was wir geändert haben:
· [Punkt 1]
· [Punkt 2]
· [Punkt 3]

Das Ergebnis: [eine belastbare Zahl, zum Beispiel Ladezeit von 6,2 auf 1,4 Sekunden, oder mehr Anfragen pro Monat].

Ohne Zahl ist ein Vorher-Nachher nur Geschmackssache. Mit Zahl ist es ein Beweis. Nennen Sie deshalb immer mindestens eine.

Sie sind unsicher, ob sich ein Relaunch bei Ihnen lohnt? Wir schauen im kostenlosen Erstgespräch drauf.

#relaunch #webdesign #vorhernachher #seo #andernach #koblenz #mittelrhein""",
        "hinweis": "Nach dem Posten anpinnen. Die Platzhalter in eckigen Klammern vorher ersetzen.",
    },
    # ------------------------------------------------------------------ 05
    {
        "nr": 5,
        "slug": "wer-dahintersteht",
        "titel": "Wer dahintersteht",
        "typ": "D · Mensch",
        "saeule": "Mensch",
        "braucht": "Ein Portraitfoto von Runi, hochkant, ruhiger Hintergrund, kein Blitz.",
        "slides": [
            {
                "eyebrow": "Wer dahintersteht",
                "h1": "Runi Ahmad",
                "hsize": 100,
                "lead": "Gründer von Pluralo",
                "align": "end",
                "slot": "Portrait|hier einsetzen|1080 × 1350 px",
                "foto": "runi.jpg",
                "bildlage": "center 28%",
            },
        ],
        "caption": """Hinter Pluralo steht ein Mensch, kein Kundenportal.

Ich bin Runi Ahmad und habe Pluralo in Andernach gegründet. Angefangen hat es mit einer einfachen Beobachtung: Viele gute Betriebe in der Region haben eine Website, die ihrer Arbeit nicht gerecht wird. Nicht, weil ihnen die Qualität fehlt, sondern weil ihnen niemand zugehört hat.

Genau da setzen wir an. Wir fragen zuerst nach Ihrem Ziel und Ihrer Zielgruppe. Erst danach reden wir über Design, Technik oder Suchmaschinen.

Was das für Sie bedeutet: kurze Wege, verständliche Abstimmungen und eine Ansprechperson, die Ihr Projekt kennt.

Wenn Sie etwas vorhaben, schreiben Sie mir einfach.

#andernach #digitalagentur #webdesign #selbstständig #mittelrhein #rheinlandpfalz""",
    },
    # ------------------------------------------------------------------ 06
    {
        "nr": 6,
        "slug": "google-profil",
        "titel": "Das Google-Unternehmensprofil",
        "typ": "A + C",
        "saeule": "Wissen",
        "slides": [
            {
                "eyebrow": "Lokale Sichtbarkeit",
                "counter": "01 / 03",
                "h1": "Ihr Google-Profil ist Ihre *zweite Startseite*.",
                "hsize": 82,
                "align": "end",
                "swipe": True,
            },
            {
                "eyebrow": "Was meistens fehlt",
                "counter": "02 / 03",
                "align": "center",
                "items": [
                    ("Leistungen sind nicht eingetragen",),
                    ("Fotos fehlen oder sind Jahre alt",),
                    ("Öffnungszeiten stimmen nicht",),
                    ("Auf Bewertungen antwortet niemand",),
                ],
            },
            {
                "eyebrow": "Was das bringt",
                "counter": "03 / 03",
                "align": "center",
                "items": [
                    ("Sie erscheinen in der Umgebungssuche",
                     "Bei „in meiner Nähe“ entscheidet vor allem das Profil, nicht die Website."),
                    ("Anrufe und Routen ohne Umweg",
                     "Viele Interessenten melden sich direkt aus dem Suchergebnis heraus."),
                    ("Bewertungen schaffen Vertrauen",
                     "Antworten zeigen, dass jemand zuhört. Das lesen auch alle anderen."),
                ],
                "note": "Wir richten es ein und pflegen es",
            },
        ],
        "caption": """Ihr Google-Unternehmensprofil ist Ihre zweite Startseite.

Für lokale Betriebe ist es oft sogar die erste. Wer „Elektriker in der Nähe“ oder „Restaurant Andernach“ sucht, sieht zuerst die Einträge in Karte und Suchergebnis, nicht Ihre Website.

Was uns dort am häufigsten begegnet:
· Die Leistungen sind gar nicht eingetragen
· Die Fotos sind Jahre alt oder fehlen
· Die Öffnungszeiten stimmen nicht
· Auf Bewertungen antwortet niemand

Jeder dieser Punkte ist in einer halben Stunde behoben und wirkt sofort. Das ist der schnellste Hebel, den lokale Betriebe haben, und er kostet nichts außer Aufmerksamkeit.

Wenn Sie möchten, richten wir das Profil ein, pflegen die Inhalte und sorgen dafür, dass echte Bewertungen dazukommen.

#googleunternehmensprofil #lokalesseo #seo #andernach #koblenz #handwerk #gastronomie""",
    },
    # ------------------------------------------------------------------ 07
    {
        "nr": 7,
        "slug": "so-arbeiten-wir",
        "titel": "So arbeiten wir",
        "typ": "C · Wissen",
        "saeule": "Angebot",
        "slides": [
            {
                "eyebrow": "Arbeitsweise",
                "counter": "01 / 03",
                "h1": "So arbeiten *wir*",
                "hsize": 104,
                "lead": "Vier Schritte von der ersten Frage|bis zum Launch.",
                "align": "end",
                "swipe": True,
            },
            {
                "eyebrow": "Arbeitsweise",
                "counter": "02 / 03",
                "align": "center",
                "items": [
                    ("Kennenlernen",
                     "Wir klären Ziele, Zielgruppe, aktuellen Stand und welche Leistungen wirklich sinnvoll sind."),
                    ("Analyse & Konzept",
                     "Wir entwickeln Struktur, Inhalte und einen transparenten Plan für die Umsetzung."),
                ],
            },
            {
                "eyebrow": "Arbeitsweise",
                "counter": "03 / 03",
                "align": "center",
                "start": 3,
                "items": [
                    ("Umsetzung",
                     "Design, Technik und Inhalte entstehen abgestimmt auf Ihr Unternehmen."),
                    ("Launch & Betreuung",
                     "Nach Ihrer Freigabe geht das Projekt online. Auf Wunsch entwickeln wir es weiter."),
                ],
                "note": "Sie wissen jederzeit, wo das Projekt steht",
            },
        ],
        "caption": """Wie ein Projekt bei uns abläuft.

01 Kennenlernen
Wir klären Ziele, Zielgruppe, den aktuellen Stand und welche Leistungen wirklich sinnvoll sind. Kostenlos und unverbindlich.

02 Analyse und Konzept
Wir entwickeln Struktur, Inhalte und einen transparenten Plan für die Umsetzung. Sie erhalten ein Angebot mit klar beschriebenem Leistungsumfang.

03 Umsetzung
Design, Technik und Inhalte entstehen abgestimmt auf Ihr Unternehmen und Ihre Zielgruppe. Zwischenstände sehen Sie, bevor etwas fertig ist.

04 Launch und Betreuung
Nach Ihrer Freigabe geht das Projekt online. Auf Wunsch entwickeln wir es laufend weiter.

Der häufigste Grund, warum Betriebe ein Website-Projekt vor sich herschieben, ist nicht der Preis. Es ist die Unsicherheit darüber, was auf sie zukommt. Deshalb machen wir den Ablauf vorher transparent.

#webdesign #ablauf #projekt #andernach #koblenz #selbstständig #digitalagentur""",
    },
    # ------------------------------------------------------------------ 08
    {
        "nr": 8,
        "slug": "andernach",
        "titel": "Standort Andernach",
        "typ": "D · Ort",
        "saeule": "Region",
        "braucht": "Ein Foto aus Andernach, hochkant. Rheinufer, Altstadt oder Geysir funktionieren gut.",
        "slides": [
            {
                "eyebrow": "Standort",
                "h1": "Andernach",
                "hsize": 116,
                "lead": "Regional verwurzelt, digital flexibel.",
                "align": "end",
                "slot": "Foto aus Andernach|hier einsetzen|1080 × 1350 px",
                "foto": "andernach.jpg",
            },
        ],
        "caption": """Wir arbeiten von Andernach aus.

Das ist kein Zufall und kein reines Adressdetail. Wer die Betriebe in einer Region kennt, weiß auch, wonach hier gesucht wird, welche Konkurrenz es gibt und was einen Handwerksbetrieb vom Mittelrhein von einer Agenturbroschüre unterscheidet.

Wir begleiten Unternehmen, Selbstständige und Vereine aus Andernach, aus Koblenz, Neuwied und Mayen und darüber hinaus deutschlandweit. Die Zusammenarbeit läuft persönlich vor Ort oder vollständig digital, je nachdem, was Ihnen lieber ist.

Wenn Sie aus der Region sind: Melden Sie sich gerne. Ein Gespräch vor Ort ist bei uns kein Sonderfall.

#andernach #koblenz #neuwied #mayen #mittelrhein #rheinlandpfalz #regional""",
    },
    # ------------------------------------------------------------------ 09
    {
        "nr": 9,
        "slug": "erstgespraech",
        "titel": "Kostenloses Erstgespräch",
        "typ": "E · Luft",
        "saeule": "Angebot",
        "pin": True,
        "slides": [
            {
                "theme": "light",
                "eyebrow": "Nächster Schritt",
                "counter": "01 / 02",
                "h1": "Kostenloses *Erstgespräch*",
                "hsize": 92,
                "lead": "30 Minuten. Unverbindlich.|Mit einer konkreten Empfehlung.",
                "align": "end",
                "swipe": True,
            },
            {
                "theme": "light",
                "eyebrow": "Was passiert",
                "counter": "02 / 02",
                "align": "center",
                "items": [
                    ("Wir schauen uns Ihren Auftritt an",
                     "Website, Google-Profil und Sichtbarkeit in Ihrer Region."),
                    ("Wir sagen, was wir ändern würden",
                     "Auch dann, wenn das kein Auftrag für uns ist."),
                    ("Sie erhalten ein klares Angebot",
                     "Mit beschriebenem Leistungsumfang, oder eben keines."),
                ],
                "note": "kontakt@pluralo.de · +49 176 79920971",
            },
        ],
        "caption": """Wie sichtbar ist Ihr Unternehmen heute?

Im kostenlosen Erstgespräch schauen wir uns gemeinsam an, wo Sie stehen: Ihre Website, Ihr Google-Unternehmensprofil und Ihre Auffindbarkeit in der Region.

Was Sie danach haben:
· Eine ehrliche Einschätzung, was gut läuft und was nicht
· Zwei bis drei konkrete Empfehlungen, die Sie auch selbst umsetzen können
· Ein transparentes Angebot, falls Sie mit uns arbeiten möchten

Was Sie nicht haben: eine Verpflichtung. Wenn wir der Meinung sind, dass Sie uns nicht brauchen, sagen wir das.

Das Gespräch dauert etwa 30 Minuten, telefonisch, digital oder bei Ihnen vor Ort.

Schreiben Sie uns eine Nachricht, eine E-Mail an kontakt@pluralo.de oder rufen Sie an unter +49 176 79920971.

#erstgespräch #webdesign #seo #andernach #koblenz #mittelrhein #digitalagentur""",
        "hinweis": "Nach dem Posten anpinnen. Damit steht der Kontaktweg dauerhaft oben im Profil.",
    },
]
