# Bildquellen

Hierher kommen die eigenen Fotos und Screenshots. `build.py` erkennt sie an den
Dateinamen aus `posts.py` und setzt sie automatisch in die Kacheln ein. Solange
eine Datei fehlt, rendert der Beitrag als `VORLAGE_…` mit markiertem Platzhalter.

| Datei | Beitrag | Inhalt |
| --- | --- | --- |
| `vorher.png` | 04 | Screenshot der alten Website |
| `nachher.png` | 04 | Screenshot der neuen Website |
| `runi.jpg` | 05 | Portrait, hochkant |
| `andernach.jpg` | 08 | Ortsfoto, hochkant |

Der Bildausschnitt lässt sich je Kachel über `"bildlage"` in `posts.py` steuern,
zum Beispiel `"center 28%"`, damit ein Gesicht im oberen Drittel sitzt.
