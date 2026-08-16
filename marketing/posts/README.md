# Die ersten neun Instagram-Beiträge

Fertige Kacheln in 1080 × 1350 px, gebaut nach dem Kachel-System aus
`marketing/social-media-strategie.html`.

## Aufbau

| Datei | Zweck |
| --- | --- |
| `posts.py` | Inhalt aller Beiträge: Slide-Texte und Bildunterschriften. Hier wird redigiert. |
| `build.py` | Rendert die Kacheln nach `png/`. |
| `sheet.py` | Erzeugt `captions.md` und `uebersicht.html` aus demselben Inhalt. |
| `quellen/` | Eigene Fotos und Screenshots. Nicht im Repository. |
| `png/` | Die fertigen Bilder. Nicht im Repository. |
| `captions.md` | Alle Bildunterschriften zum Nachschlagen. |
| `uebersicht.html` | Quelle für das veröffentlichte Artifact. Nicht im Repository. |

## Warum Bilder hier nicht eingecheckt werden

Dieses Repository ist öffentlich und wird über GitHub Pages ausgeliefert. Portraits,
Ortsfotos und Kundenscreenshots wären damit unter `pluralo.de` abrufbar, unabhängig
davon, ob sie später auf Instagram erscheinen. Sie bleiben deshalb lokal und werden
per ZIP weitergegeben. Versioniert ist nur, was die Bilder erzeugt: Texte und Code.
Wer die Kacheln neu herstellen will, legt die Dateien aus `quellen/README.md` an
und ruft die beiden Skripte auf.

## Dateinamen

* `post-NN-M-…png` ist fertig und kann so hochgeladen werden.
* `VORLAGE_…png` entsteht nur, solange das zugehörige Bild in `quellen/` fehlt.
  Sie zeigt die Gestaltung mit markiertem Platzhalter und wird nicht hochgeladen.
* `AUFLAGE_…png` ist dieselbe Kachel freigestellt auf transparentem Grund, falls
  ein Bild lieber von Hand untergelegt werden soll.

## Neu erzeugen

```sh
pip install Pillow
python3 marketing/posts/build.py     # Kacheln
python3 marketing/posts/sheet.py     # Texte und Übersicht
```

`build.py` sucht Chromium unter den Pfaden in `CHROME_CANDIDATES`. Gerendert wird
mit doppelter Pixeldichte und anschließend auf 1080 × 1350 px heruntergerechnet,
damit Schrift und Verläufe sauber bleiben.

## Schreibweisen in `posts.py`

* `*Wort*` hebt das Wort im Farbverlauf hervor
* `|` erzwingt einen Zeilenumbruch
