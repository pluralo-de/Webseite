# Pluralo veröffentlichen

Die Hauptadresse der Website ist `https://www.pluralo.de`. Wenn die unten
aufgeführten DNS-Einträge gesetzt sind, leitet GitHub Pages
`https://pluralo.de` automatisch auf die Hauptadresse um.

## Vor dem öffentlichen Start

1. Angaben im Impressum prüfen:
   - vollständiger und richtig geschriebener Name
   - ladungsfähige Anschrift
   - Telefonnummer und E-Mail-Adresse
   - Kleinunternehmerregelung
2. Die zwei eckigen Platzhalter in der Datenschutzerklärung ersetzen.
3. Im EmailJS-Dashboard `https://www.pluralo.de` und
   `https://pluralo.de` als erlaubte Ursprünge eintragen.
4. Das Kontaktformular nach der Veröffentlichung einmal selbst testen.

## Dateien auf GitHub

Alle Dateien und Ordner aus diesem Paket müssen direkt im Hauptverzeichnis des
Pluralo-Repositorys liegen. Besonders wichtig sind:

- `index.html`
- `style.css`
- `script.js`
- `CNAME`
- `assets/`, `vendor/` und `webfonts/`

Anschließend im Repository:

1. `Settings` öffnen.
2. Links `Pages` wählen.
3. Unter `Build and deployment` die Quelle `Deploy from a branch` wählen.
4. Branch `main` und Ordner `/(root)` auswählen und speichern.
5. Unter `Custom domain` zuerst `www.pluralo.de` eintragen und speichern.

## DNS-Einträge bei IONOS

Im IONOS-Konto `Domains & SSL` öffnen, bei `pluralo.de` auf die drei Punkte
und dann auf `DNS` klicken.

Für die Hauptdomain vier A-Records anlegen:

| Typ | Hostname | Zeigt auf |
| --- | --- | --- |
| A | `@` oder leer | `185.199.108.153` |
| A | `@` oder leer | `185.199.109.153` |
| A | `@` oder leer | `185.199.110.153` |
| A | `@` oder leer | `185.199.111.153` |

Für die www-Adresse einen CNAME-Record anlegen:

| Typ | Hostname | Zeigt auf |
| --- | --- | --- |
| CNAME | `www` | `pluralo-de.github.io` |

Nur A-/AAAA-Einträge der Hauptdomain oder einen vorhandenen, widersprechenden
`www`-Eintrag ersetzen. MX-, SPF-, DKIM- und andere E-Mail-Einträge nicht
löschen.

## HTTPS aktivieren

Nach erfolgreicher DNS-Prüfung im GitHub-Bereich `Settings > Pages`
`Enforce HTTPS` aktivieren. Bis DNS und Zertifikat vollständig verfügbar sind,
können bis zu 24 Stunden vergehen.

Offizielle Anleitungen:

- https://docs.github.com/en/pages/configuring-a-custom-domain-for-your-github-pages-site/managing-a-custom-domain-for-your-github-pages-site
- https://www.ionos.de/hilfe/domains/dns-einstellungen/
