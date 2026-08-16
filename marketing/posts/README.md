# Die ersten neun Instagram-Beiträge

Fertige Kacheln in 1080 × 1350 px, gebaut nach dem Kachel-System aus
`marketing/social-media-strategie.html`.

## Aufbau

| Datei | Zweck |
| --- | --- |
| `posts.py` | Inhalt aller Beiträge: Slide-Texte und Bildunterschriften. Hier wird redigiert. |
| `build.py` | Rendert die Kacheln nach `png/`. |
| `sheet.py` | Erzeugt `captions.md` und `uebersicht.html` aus demselben Inhalt. |
| `png/` | Die fertigen Bilder. |
| `captions.md` | Alle Bildunterschriften zum Nachschlagen. |
| `uebersicht.html` | Quelle für das veröffentlichte Artifact, deshalb ohne doctype und body. |

## Dateinamen

* `post-NN-M-…png` ist fertig und kann so hochgeladen werden.
* `VORLAGE_…png` zeigt die Gestaltung mit markiertem Platzhalter. Nicht hochladen.
* `AUFLAGE_…png` ist dieselbe Kachel freigestellt, also nur Verlauf, Text, Rahmen
  und Logo auf transparentem Grund. Diese Datei über das eigene Foto legen.

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
