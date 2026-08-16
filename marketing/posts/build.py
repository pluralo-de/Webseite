#!/usr/bin/env python3
"""Rendert die Instagram-Beitraege aus marketing/posts/posts.py als PNG.

Jede Kachel entsteht als HTML-Seite von exakt 1080 x 1350 px, wird von Chromium
mit doppelter Pixeldichte fotografiert und anschliessend auf 1080 x 1350
heruntergerechnet. Der Umweg ueber die doppelte Aufloesung ist der Grund fuer die
sauberen Kanten an Schrift und Verlauf.

Aufruf aus dem Repository-Wurzelverzeichnis:

    python3 marketing/posts/build.py
"""

from __future__ import annotations

import base64
import html
import io
import re
import shutil
import subprocess
import sys
from pathlib import Path

from PIL import Image

from posts import POSTS

ROOT = Path(__file__).resolve().parents[2]
HERE = Path(__file__).resolve().parent
OUT = HERE / "png"
WORK = HERE / ".work"
QUELLEN = HERE / "quellen"

WIDTH, HEIGHT = 1080, 1350
SCALE = 2
# Der sichtbare Bereich in Chromium ist rund 90 px niedriger als das angeforderte
# Fenster. Wir rendern deshalb mit Reserve und schneiden anschliessend exakt zu.
PAD = 200

CHROME_CANDIDATES = [
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/opt/pw-browsers/chromium/chrome-linux/chrome",
    shutil.which("chromium") or "",
    shutil.which("google-chrome") or "",
]

FONT_FILES = [
    ("Space Grotesk", 500, "webfonts/space-grotesk-latin-500-normal.woff2"),
    ("Space Grotesk", 600, "webfonts/space-grotesk-latin-600-normal.woff2"),
    ("Space Grotesk", 700, "webfonts/space-grotesk-latin-700-normal.woff2"),
    ("Inter", 400, "webfonts/inter-latin-400-normal.woff2"),
    ("Inter", 500, "webfonts/inter-latin-500-normal.woff2"),
    ("IBM Plex Mono", 500, "webfonts/ibm-plex-mono-latin-500-normal.woff2"),
]

LOGO = """<svg class="mark" viewBox="275 270 450 460" aria-hidden="true">
<defs><linearGradient id="g{uid}" x1="360" y1="300" x2="640" y2="700" gradientUnits="userSpaceOnUse">
<stop offset="0" stop-color="#00FCA8"/><stop offset="1" stop-color="#1CDAFF"/></linearGradient></defs>
<g fill="url(#g{uid})">
<path d="M406.5 298.05H578.66c5.523 0 8.746 4.477 7.2 10l-47.078 168.14c-1.547 5.523-7.277 10-12.8 10h-172.16c-5.523 0-8.747-4.477-7.2-10L393.7 308.05c1.546-5.523 7.277-10 12.8-10Z"/>
<path d="M594.68 379.784h88.88c5.523 0 8.746 4.477 7.2 10l-24.192 86.4c-1.546 5.523-7.277 10-12.8 10h-88.88c-5.522 0-8.746-4.477-7.2-10l24.192-86.4c1.546-5.523 7.277-10 12.8-10Z"/>
<path d="M345.9 513.932h89.7c5.523 0 8.746 4.477 7.2 10l-24.203 86.44c-1.546 5.523-7.277 10-12.8 10h-89.7c-5.523 0-8.746-4.477-7.2-10l24.203-86.44c1.546-5.523 7.277-10 12.8-10Z"/>
<path d="M473.74 513.932H646.1c5.523 0 8.746 4.477 7.2 10l-47.056 168.06c-1.546 5.523-7.277 10-12.8 10h-172.36c-5.523 0-8.746-4.477-7.2-10l47.056-168.06c1.546-5.523 7.277-10 12.8-10Z"/>
</g></svg>"""

# Der abgeschraegte Rahmen ist die Formsignatur der Website, hier als Kontur
# gezeichnet, damit die Ecken nicht wie bei clip-path abgeschnitten werden.
FRAME = (
    '<svg class="frame" viewBox="0 0 1080 1350" preserveAspectRatio="none" aria-hidden="true">'
    '<path d="M80 40 H1040 V1270 L1000 1310 H40 V80 Z" fill="none" '
    'stroke="var(--frame)" stroke-width="2"/></svg>'
)


def fonts_css() -> str:
    out = []
    for family, weight, rel in FONT_FILES:
        data = base64.b64encode((ROOT / rel).read_bytes()).decode()
        out.append(
            f"@font-face{{font-family:'{family}';font-style:normal;font-weight:{weight};"
            f"src:url(data:font/woff2;base64,{data}) format('woff2');}}"
        )
    return "".join(out)


CSS = """
*{box-sizing:border-box;margin:0;padding:0}
html,body{width:1080px;height:1350px;overflow:hidden}
body{background:transparent}

.slide{
  position:relative;width:1080px;height:1350px;overflow:hidden;
  display:flex;flex-direction:column;padding:96px;
  font-family:'Inter',sans-serif;
}
.slide.dark{
  --bg:#06090b; --plate:#0b1316; --text:#eaf3f2; --muted:#93a8b1; --dim:#5f6f76;
  --frame:rgba(234,243,242,.13); --accent:#0aefc0;
  background:var(--bg);color:var(--text);
}
.slide.light{
  --bg:#eaf3f2; --plate:#ffffff; --text:#06090b; --muted:#4d6069; --dim:#7d8f96;
  --frame:rgba(6,9,11,.16); --accent:#046c58;
  background:var(--bg);color:var(--text);
}
/* Grundschein in der Markenfarbe, damit die Flaeche nicht tot wirkt. */
.slide.dark::before{
  content:"";position:absolute;inset:0;
  background:
    radial-gradient(58% 46% at 86% 4%, rgba(28,212,255,.15), transparent 66%),
    radial-gradient(52% 42% at 4% 100%, rgba(10,239,192,.11), transparent 64%);
}
.slide.light::before{
  content:"";position:absolute;inset:0;
  background:radial-gradient(60% 44% at 92% 2%, rgba(10,239,192,.20), transparent 68%);
}
/* Freigestellte Auflage: nur Verlauf, Text und Rahmen, kein Untergrund. */
.slide.overlay{background:transparent}
.slide.overlay::before{
  background:linear-gradient(180deg, rgba(6,9,11,.30) 0%, rgba(6,9,11,0) 32%,
    rgba(6,9,11,.84) 76%, rgba(6,9,11,.96) 100%);
}
.frame{position:absolute;inset:0;width:1080px;height:1350px;z-index:3;pointer-events:none}

.top,.body,.bot{position:relative;z-index:4}
.top{display:flex;justify-content:space-between;align-items:center;gap:24px}
.eyebrow{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;
  letter-spacing:.19em;text-transform:uppercase;color:var(--muted);
  display:flex;align-items:center;gap:14px;
}
.eyebrow .dot{width:10px;height:10px;flex:none;background:linear-gradient(135deg,#0aefc0,#1cd4ff)}
.slide.light .eyebrow .dot{background:#046c58}
.counter{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;
  letter-spacing:.16em;color:var(--dim);font-variant-numeric:tabular-nums;
}

.body{flex:1;display:flex;flex-direction:column;gap:34px;padding:56px 0 24px}
.body.end{justify-content:flex-end}
.body.center{justify-content:center}
.body.start{justify-content:flex-start}

h1{
  font-family:'Space Grotesk',sans-serif;font-weight:700;
  line-height:1.04;letter-spacing:-.032em;color:var(--text);
}
h1 em{
  font-style:normal;
  background:linear-gradient(120deg,#0aefc0,#1cd4ff);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}
.slide.light h1 em{background:linear-gradient(120deg,#048f6e,#0a7fa6);-webkit-background-clip:text;background-clip:text;color:transparent}
.lead{font-size:31px;line-height:1.48;color:var(--muted);max-width:26ch}

.items{display:flex;flex-direction:column;gap:44px}
.item{display:grid;grid-template-columns:74px 1fr;column-gap:8px}
.item .n{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:23px;
  color:var(--accent);padding-top:12px;font-variant-numeric:tabular-nums;
}
.item h2{
  font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:38px;
  line-height:1.2;letter-spacing:-.018em;color:var(--text);
}
.item p{font-size:25px;line-height:1.48;color:var(--muted);margin-top:10px}
.items.tight{gap:34px}
.items.tight .item h2{font-size:36px}

.big{
  font-family:'Space Grotesk',sans-serif;font-weight:700;font-size:210px;
  line-height:.9;letter-spacing:-.05em;
  background:linear-gradient(120deg,#0aefc0,#1cd4ff);
  -webkit-background-clip:text;background-clip:text;color:transparent;
}

.rule{height:2px;background:var(--frame);margin:6px 0}

.note{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:23px;
  letter-spacing:.12em;text-transform:uppercase;color:var(--accent);
}

/* Eigenes Foto oder Screenshot, formatfuellend beschnitten. */
.media{position:absolute;inset:0;z-index:1;overflow:hidden}
.media img{width:100%;height:100%;object-fit:cover;object-position:var(--pos,center);display:block}
/* Zwei Lagen: eine Abdunklung von allen Raendern nach innen, darunter der
   Verlauf nach unten, auf dem die Ueberschrift steht. */
.scrim{
  position:absolute;inset:0;
  background:
    radial-gradient(118% 82% at 50% 40%,
      rgba(6,9,11,0) 34%, rgba(6,9,11,.30) 66%, rgba(6,9,11,.62) 86%, rgba(6,9,11,.82) 100%),
    linear-gradient(180deg,
      rgba(6,9,11,.62) 0%, rgba(6,9,11,.14) 24%, rgba(6,9,11,.20) 46%,
      rgba(6,9,11,.74) 72%, rgba(6,9,11,.93) 88%, rgba(6,9,11,.97) 100%);
}
/* Sanfte Stufe fuer Screenshots: der Inhalt soll lesbar bleiben, abgedunkelt
   wird nur so weit, dass Kopfzeile und Ueberschrift sicher stehen. */
.scrim.sanft{
  background:
    radial-gradient(126% 92% at 50% 44%,
      rgba(6,9,11,0) 52%, rgba(6,9,11,.20) 78%, rgba(6,9,11,.44) 100%),
    linear-gradient(180deg,
      rgba(6,9,11,.60) 0%, rgba(6,9,11,.10) 16%, rgba(6,9,11,0) 42%,
      rgba(6,9,11,.55) 74%, rgba(6,9,11,.92) 90%, rgba(6,9,11,.97) 100%);
}
/* Ueber einem Foto brauchen die kleinen Zeilen mehr Helligkeit, sonst
   verschwinden sie in hellen Bildbereichen wie Himmel oder Fenster. */
.slide.mitbild .eyebrow{color:#e4eef0}
.slide.mitbild .counter{color:#c2d2d7}
.slide.mitbild .url{color:#b3c2c8}
.slide.mitbild .lead{color:#cfdde1}

/* Screenshot als Karte auf dunklem Grund. Ein Screenshot ist quer und wuerde
   formatfuellend beschnitten unlesbar, als Karte bleibt die ganze Seite sichtbar. */
.card{
  width:100%;background:#0b1316;overflow:hidden;
  clip-path:polygon(22px 0,100% 0,100% calc(100% - 22px),calc(100% - 22px) 100%,0 100%,0 22px);
  box-shadow:0 46px 100px -44px rgba(0,0,0,.95);
}
.card img{width:100%;height:auto;display:block}

/* Platzhalterflaeche, solange das Bild noch fehlt. */
.slot{
  position:absolute;inset:0;z-index:1;
  background:
    linear-gradient(180deg, rgba(6,9,11,.30) 0%, rgba(6,9,11,.05) 34%, rgba(6,9,11,.86) 78%, rgba(6,9,11,.96) 100%),
    repeating-linear-gradient(135deg,#0c1519 0 34px,#0a1216 34px 68px);
}
.slot .hintbox{
  position:absolute;left:50%;top:42%;transform:translate(-50%,-50%);
  border:2px dashed rgba(10,239,192,.55);padding:26px 34px;text-align:center;
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:22px;
  letter-spacing:.14em;text-transform:uppercase;color:#0aefc0;line-height:1.9;
}

.bot{display:flex;justify-content:space-between;align-items:flex-end;gap:24px}
.url{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;
  letter-spacing:.14em;color:var(--dim);
}
.swipe{
  font-family:'IBM Plex Mono',monospace;font-weight:500;font-size:24px;
  letter-spacing:.14em;text-transform:uppercase;color:var(--accent);
}
.mark{width:62px;height:62px;flex:none}
.slide.light .mark{filter:saturate(.85) brightness(.72)}
"""


def markup(text: str) -> str:
    """*Wort* wird zum Verlaufswort, | wird zum Zeilenumbruch."""
    escaped = html.escape(text).replace("|", "<br>")
    return re.sub(r"\*(.+?)\*", r"<em>\1</em>", escaped)


def photo_path(slide: dict) -> Path | None:
    """Das eigene Bild einer Kachel, sobald es in quellen/ liegt."""
    name = slide.get("foto")
    if not name:
        return None
    path = QUELLEN / name
    return path if path.exists() else None


def embed(path: Path) -> str:
    """Bild als Datenzeile einbetten, damit Chromium keine Datei laden muss."""
    with Image.open(path) as img:
        img = img.convert("RGB")
        # Grosszuegig auf die doppelte Kachelbreite begrenzen, mehr bringt nichts.
        if img.width > WIDTH * SCALE:
            img = img.resize((WIDTH * SCALE, round(img.height * WIDTH * SCALE / img.width)),
                             Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=94, optimize=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def slide_html(slide: dict, uid: int) -> str:
    theme = slide.get("theme", "dark")
    if slide.get("_overlay"):
        theme += " overlay"
    parts = []

    photo = photo_path(slide)
    if photo:
        theme += " mitbild"
        pos = slide.get("bildlage", "center")
        parts.append(
            f'<div class="media" style="--pos:{pos}"><img src="{embed(photo)}" alt="">'
            f'<div class="scrim {slide.get("verlauf", "")}"></div></div>'
        )
    elif slide.get("slot"):
        label = slide["slot"].replace("|", "<br>")
        parts.append(f'<div class="slot"><div class="hintbox">{label}</div></div>')

    top_left = ""
    if slide.get("eyebrow"):
        top_left = f'<span class="eyebrow"><i class="dot"></i>{html.escape(slide["eyebrow"])}</span>'
    top_right = ""
    if slide.get("counter"):
        top_right = f'<span class="counter">{html.escape(slide["counter"])}</span>'
    parts.append(f'<header class="top">{top_left}{top_right}</header>')

    body = []
    karte = slide.get("karte")
    if karte and (QUELLEN / karte).exists():
        body.append(f'<div class="card"><img src="{embed(QUELLEN / karte)}" alt=""></div>')
    if slide.get("big"):
        body.append(f'<p class="big">{html.escape(slide["big"])}</p>')
    if slide.get("h1"):
        size = slide.get("hsize", 92)
        body.append(f'<h1 style="font-size:{size}px">{markup(slide["h1"])}</h1>')
    if slide.get("lead"):
        body.append(f'<p class="lead">{markup(slide["lead"])}</p>')
    if slide.get("items"):
        cls = "items tight" if len(slide["items"]) > 3 else "items"
        rows = []
        for i, it in enumerate(slide["items"], start=slide.get("start", 1)):
            text = f'<p>{markup(it[1])}</p>' if len(it) > 1 and it[1] else ""
            rows.append(
                f'<div class="item"><span class="n">{i:02d}</span>'
                f'<div><h2>{markup(it[0])}</h2>{text}</div></div>'
            )
        body.append(f'<div class="{cls}">{"".join(rows)}</div>')
    if slide.get("note"):
        body.append(f'<p class="note">{markup(slide["note"])}</p>')

    align = slide.get("align", "end")
    parts.append(f'<div class="body {align}">{"".join(body)}</div>')

    swipe = '<span class="swipe">Wischen &rarr;</span>' if slide.get("swipe") else ""
    parts.append(
        f'<footer class="bot"><span class="url">pluralo.de</span>{swipe}'
        f'{LOGO.format(uid=uid)}</footer>'
    )
    parts.append(FRAME)

    return (
        "<!doctype html><html lang=de><head><meta charset=utf-8><style>"
        + fonts_css()
        + CSS
        + "</style></head><body>"
        + f'<div class="slide {theme}">{"".join(parts)}</div>'
        + "</body></html>"
    )


def find_chrome() -> str:
    for path in CHROME_CANDIDATES:
        if path and Path(path).exists():
            return path
    sys.exit("Kein Chromium gefunden. Pfad in CHROME_CANDIDATES ergaenzen.")


def render(chrome: str, source: Path, target: Path, transparent: bool = False) -> None:
    cmd = [
        chrome, "--headless", "--disable-gpu", "--no-sandbox", "--hide-scrollbars",
        f"--window-size={WIDTH},{HEIGHT + PAD}", f"--force-device-scale-factor={SCALE}",
        "--virtual-time-budget=5000", f"--screenshot={target}", f"file://{source}",
    ]
    if transparent:
        cmd.insert(-1, "--default-background-color=00000000")
    subprocess.run(cmd, check=True, capture_output=True)

    with Image.open(target) as img:
        img = img.convert("RGBA" if transparent else "RGB")
        if img.height < HEIGHT * SCALE:
            sys.exit(f"{target.name}: nur {img.height}px hoch, PAD erhoehen.")
        img = img.crop((0, 0, WIDTH * SCALE, HEIGHT * SCALE))
        img = img.resize((WIDTH, HEIGHT), Image.LANCZOS)
        img.save(target, "PNG", optimize=True)


def main() -> None:
    chrome = find_chrome()
    # Leeren, weil sich Dateinamen aendern, sobald ein eigenes Bild dazukommt:
    # aus VORLAGE_ und AUFLAGE_ wird dann die fertige Kachel.
    shutil.rmtree(OUT, ignore_errors=True)
    OUT.mkdir(parents=True, exist_ok=True)
    WORK.mkdir(parents=True, exist_ok=True)

    made = []
    uid = 0
    for post in POSTS:
        for index, slide in enumerate(post["slides"], start=1):
            uid += 1
            offen = bool(slide.get("slot")) and not photo_path(slide)
            prefix = "VORLAGE_" if offen else ""
            name = f'{prefix}post-{post["nr"]:02d}-{index}-{post["slug"]}.png'
            source = WORK / f"{uid:03d}.html"
            source.write_text(slide_html(slide, uid), encoding="utf-8")
            target = OUT / name
            render(chrome, source, target)
            made.append(name)
            print("  ", name)

            # Fuer Foto- und Screenshot-Kacheln zusaetzlich eine freigestellte
            # Auflage, die sich in jedem Bildprogramm ueber das eigene Bild legen laesst.
            if offen:
                overlay = {k: v for k, v in slide.items() if k != "slot"}
                overlay["_overlay"] = True
                source_o = WORK / f"{uid:03d}-overlay.html"
                source_o.write_text(slide_html(overlay, uid), encoding="utf-8")
                name_o = f'AUFLAGE_post-{post["nr"]:02d}-{index}-{post["slug"]}.png'
                render(chrome, source_o, OUT / name_o, transparent=True)
                made.append(name_o)
                print("  ", name_o)

    shutil.rmtree(WORK, ignore_errors=True)
    print(f"\n{len(made)} Dateien in {OUT.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
