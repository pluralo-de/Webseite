# Marketing

Interne Arbeitsdokumente. Kein Teil der öffentlichen Website, per `robots.txt` von
der Indexierung ausgenommen.

## social-media-strategie.html

Aufbauplan für Instagram und Facebook: Kachel-System, Content-Säulen, Formate und
Maße, die ersten 30 Beiträge, Profil-Setup, Produktionsablauf.

Die Datei ist die Quelle für ein veröffentlichtes Artifact und deshalb bewusst ohne
`<!doctype>`, `<html>`, `<head>` und `<body>` geschrieben. Diese Hülle wird beim
Veröffentlichen ergänzt. Wer die Datei lokal im Browser prüfen will, muss sie also
vorher einpacken:

```sh
{ printf '<!doctype html><html lang=de><head><meta charset=utf-8>'; \
  cat marketing/social-media-strategie.html; printf '</body></html>'; } > /tmp/vorschau.html
```

Die Schriften (Space Grotesk, Inter, IBM Plex Mono) liegen als Base64 im
`<style>`-Block, weil das Artifact keine externen Ressourcen laden darf. Sie stammen
aus `webfonts/` und sind damit identisch mit denen der Website.
