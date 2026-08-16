# Pluralo

Digitalagentur aus Andernach (Runi Ahmad). Leistungen: Webdesign und
Website-Relaunch, SEO und Google-Sichtbarkeit, Social Media und Content, Branding
und Werbung. Zielgruppe: Unternehmen, Selbstständige und Vereine in Andernach, der
Region und deutschlandweit.

Dieses Repository ist **öffentlich** und wird über GitHub Pages unter pluralo.de
ausgeliefert. Alles, was hier eingecheckt wird, ist abrufbar.

## Marke

| | |
| --- | --- |
| Grund | `#06090b`, erhöht `#0d1417`, Linie `#1b262b` |
| Akzent | Verlauf Teal `#0aefc0` nach Azur `#1cd4ff` |
| Hell | `#eaf3f2`, Grautöne `#8aa0aa` und `#566269` |
| Schrift | Space Grotesk (Überschriften), Inter (Fließtext), IBM Plex Mono (Labels) |
| Form | Abgeschrägte Ecke oben links und unten rechts, nie runde Ecken |
| Ansprache | Sie, auf Website und in Social Media gleich |

Schriften liegen lokal in `webfonts/`. Keine externen Font-Anbieter einbinden.

## Social Media

**Bei jeder Anfrage nach Instagram- oder Facebook-Beiträgen gilt das hier
beschriebene System, solange nichts anderes gesagt wird.** Nicht neu erfinden,
nicht neu gestalten, sondern fortsetzen.

### Wo alles liegt

* `marketing/social-media-strategie.html` — Strategie: Kachel-System, fünf
  Content-Säulen, Formate und Maße, Frequenz, Facebook, die zehn Feed-Gesetze.
* `marketing/posts/posts.py` — Inhalt aller Beiträge, Slide-Texte und
  Bildunterschriften. Hier wird redigiert.
* `marketing/posts/build.py` — rendert die Kacheln nach `png/`.
* `marketing/posts/sheet.py` — erzeugt `captions.md` und `uebersicht.html`.
* `marketing/posts/README.md` — Aufrufe, Dateinamen, Details.

Ablauf: `pip install Pillow`, dann `python3 marketing/posts/build.py` und
`python3 marketing/posts/sheet.py`. Ausgeliefert wird als ZIP plus Artifact.

### Kachel-System

Jede Kachel ist 1080 × 1350 px und gehört zu genau einem von fünf Typen: A
Statement, B Arbeit, C Wissen, D Mensch und Ort, E Luft (hell). Konstant über
alle: abgeschrägter Konturrahmen 40 px innen, Mono-Label oben links mit
Verlaufspunkt, Zähler oben rechts bei Karussells, `pluralo.de` unten links,
Logo unten rechts, 96 px Sicherheitsrand.

Regeln, die den Feed langfristig tragen: höchstens sechs Wörter pro Cover,
der Verlauf hebt genau ein Wort hervor, nie zwei helle Kacheln nebeneinander,
mindestens zwei Typ B je neun Kacheln, nichts mit Datum ins Raster.

Das Profil-Raster schneidet 4:5 auf 3:4. Reels-Cover 1080 × 1920, im Raster
sichtbar ist nur das mittlere Band von 1080 × 1440.

### Bilder

* Fotos laufen formatfüllend über die ganze Kachel, mit Abdunklung von allen
  Rändern nach innen und stärker nach unten zur Überschrift (`.scrim`).
* Screenshots liegen als Karte auf dunklem Grund (`"karte"`), weil Querformat
  formatfüllend beschnitten unlesbar wird.
* Eigene Bilder gehören nach `marketing/posts/quellen/`, Dateinamen stehen in
  `posts.py`. Ausschnitt über `"bildlage"`, Verlaufsstärke über `"verlauf"`.
* **Bilder werden nicht eingecheckt.** `png/`, `quellen/` und `uebersicht.html`
  stehen in `.gitignore`, weil das Repository öffentlich ist.

### Bereits geliefert

Beiträge 1 bis 9, die Startsequenz, alle fertig gerendert:

| Nr | Titel | Typ | Bilder |
| --- | --- | --- | --- |
| 01 | Wofür Pluralo steht | A | 1, angepinnt |
| 02 | Was wir machen | C | 3 |
| 03 | Ihre Website bringt keine Anfragen | C | 3 |
| 04 | Vorher und nachher, Fahrschule Berisha | B | 2, angepinnt |
| 05 | Wer dahintersteht, Runi Ahmad | D | 1 |
| 06 | Ihr Google-Profil ist Ihre zweite Startseite | A und C | 3 |
| 07 | So arbeiten wir | C | 3 |
| 08 | Standort Andernach | D | 1 |
| 09 | Kostenloses Erstgespräch | E | 2, angepinnt |

Bei neuen Beiträgen dort fortsetzen: Beitrag 10 folgt auf 9, die Wissensreihe
zählt weiter (`Wissen · 02`), und Themen aus 1 bis 9 nicht wiederholen. Die
Strategie enthält einen ausgearbeiteten Plan für die Beiträge 10 bis 30.

### Bildunterschriften

Erste 125 Zeichen sind die Überschrift und tragen das Keyword. Aufbau: Hook,
zwei bis vier Sätze Kontext, konkreter Nutzen, ein klarer nächster Schritt.
Danach drei bis acht gezielte Hashtags, gemischt aus lokal (#andernach
#koblenz #neuwied #mayen), fachlich (#webdesign #lokalesseo
#googleunternehmensprofil) und Zielgruppe (#handwerk #gastronomie).

### Facebook

Kein eigener Content. Beiträge über die Meta Business Suite spiegeln, dort
längeren Text und Links ergänzen. Instagram ist die Bühne, Facebook das
Adressbuch.

## Website

Statische Seite ohne Build-Schritt: `index.html`, `style.css`, `script.js`.
Kontaktformular über EmailJS (`vendor/emailjs.min.js`). Dunkel- und Hellmodus
über `data-theme` am `html`-Element, Auswahl liegt in `localStorage`.

Nach Änderungen an CSS oder JS die Versionsangaben in `index.html`
(`style.css?v=…`, `script.js?v=…`) mitziehen, sonst laden Besucher alte Dateien.

Keine Gedankenstriche in Texten verwenden, das ist im ganzen Projekt so gehalten.

## Technische Eigenheit

Chromium liefert im Kopflosbetrieb einen Sichtbereich, der rund 90 px niedriger
ist als das über `--window-size` angeforderte Fenster. `build.py` rendert deshalb
mit Reserve und schneidet danach exakt auf 1080 × 1350 zu. Wer das übersieht,
bekommt einen weißen Streifen am unteren Rand.
