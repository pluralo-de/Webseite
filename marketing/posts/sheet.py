#!/usr/bin/env python3
"""Erzeugt aus posts.py die Textfassung und die Uebersichtsseite.

    python3 marketing/posts/sheet.py

Schreibt captions.md (zum Nachschlagen im Repository) und uebersicht.html
(Quelle fuer das veroeffentlichte Artifact, deshalb ohne doctype und body).
"""

from __future__ import annotations

import base64
import html
import io
from pathlib import Path

from PIL import Image

from build import fonts_css
from posts import POSTS

HERE = Path(__file__).resolve().parent
PNG = HERE / "png"
PREVIEW_WIDTH = 420


def slide_files(post: dict) -> list[tuple[Path, bool]]:
    """Alle Kacheln eines Beitrags in Reihenfolge, mit Vorlagen-Kennzeichen."""
    found = []
    for index, slide in enumerate(post["slides"], start=1):
        prefix = "VORLAGE_" if slide.get("slot") else ""
        name = f'{prefix}post-{post["nr"]:02d}-{index}-{post["slug"]}.png'
        found.append((PNG / name, bool(slide.get("slot"))))
    return found


def preview(path: Path) -> str:
    with Image.open(path) as img:
        img = img.convert("RGB")
        height = round(PREVIEW_WIDTH * img.height / img.width)
        img = img.resize((PREVIEW_WIDTH, height), Image.LANCZOS)
        buf = io.BytesIO()
        img.save(buf, "JPEG", quality=78, optimize=True, progressive=True)
    return "data:image/jpeg;base64," + base64.b64encode(buf.getvalue()).decode()


def write_captions() -> None:
    lines = [
        "# Die ersten neun Beiträge",
        "",
        "Erzeugt aus `posts.py`. Änderungen dort vornehmen und",
        "`python3 marketing/posts/sheet.py` erneut ausführen.",
        "",
    ]
    for post in POSTS:
        lines += [
            f'## {post["nr"]:02d} · {post["titel"]}',
            "",
            f'Kacheltyp {post["typ"]} · Säule {post["saeule"]} · '
            f'{len(post["slides"])} Bild{"er" if len(post["slides"]) > 1 else ""}'
            + (" · anpinnen" if post.get("pin") else ""),
            "",
        ]
        if post.get("braucht"):
            lines += [f'**Wird noch gebraucht:** {post["braucht"]}', ""]
        if post.get("hinweis"):
            lines += [f'**Hinweis:** {post["hinweis"]}', ""]
        lines += ["Dateien:", ""]
        for path, is_template in slide_files(post):
            lines.append(f'- `{path.name}`' + (" (Platzhalter ersetzen)" if is_template else ""))
        lines += ["", "Bildunterschrift:", "", "```", post["caption"], "```", ""]
    (HERE / "captions.md").write_text("\n".join(lines), encoding="utf-8")


CSS = """
:root{
  --ground:#06090b; --raised:#0d1417; --raised-2:#111c21; --line:#1b262b; --line-soft:#151f24;
  --text:#eaf3f2; --muted:#8aa0aa; --dim:#5c6a71; --accent:#0aefc0; --accent-2:#1cd4ff;
  --accent-ink:#06090b; --accent-soft:rgba(10,239,192,.10);
  --skew:polygon(14px 0, 100% 0, 100% calc(100% - 14px), calc(100% - 14px) 100%, 0 100%, 0 14px);
  --skew-sm:polygon(8px 0, 100% 0, 100% calc(100% - 8px), calc(100% - 8px) 100%, 0 100%, 0 8px);
  --sans:'Inter',system-ui,sans-serif; --display:'Space Grotesk','Inter',sans-serif;
  --mono:'IBM Plex Mono',ui-monospace,monospace;
}
@media (prefers-color-scheme: light){
  :root:not([data-theme="dark"]){
    --ground:#eff4f3; --raised:#ffffff; --raised-2:#f7fbfa; --line:#d2dedb; --line-soft:#e3ebe9;
    --text:#06090b; --muted:#4e6069; --dim:#71838a; --accent:#046c58; --accent-2:#0a6b8b;
    --accent-ink:#ffffff; --accent-soft:rgba(4,108,88,.08);
  }
}
:root[data-theme="light"]{
  --ground:#eff4f3; --raised:#ffffff; --raised-2:#f7fbfa; --line:#d2dedb; --line-soft:#e3ebe9;
  --text:#06090b; --muted:#4e6069; --dim:#71838a; --accent:#046c58; --accent-2:#0a6b8b;
  --accent-ink:#ffffff; --accent-soft:rgba(4,108,88,.08);
}
*{box-sizing:border-box}
body{margin:0;background:var(--ground);color:var(--text);font-family:var(--sans);
  font-size:1.02rem;line-height:1.66;-webkit-font-smoothing:antialiased}
::selection{background:var(--accent);color:var(--accent-ink)}
h1,h2,h3{font-family:var(--display);font-weight:700;margin:0;text-wrap:balance}
p{margin:0}
.eyebrow{font-family:var(--mono);font-weight:500;font-size:.68rem;letter-spacing:.16em;
  text-transform:uppercase;color:var(--muted)}

.cover{background:#06090b;color:#eaf3f2;position:relative;overflow:hidden;border-bottom:1px solid #162126}
.cover::before{content:"";position:absolute;inset:0;
  background:radial-gradient(58% 88% at 84% 6%, rgba(28,212,255,.13), transparent 64%),
             radial-gradient(50% 78% at 6% 96%, rgba(10,239,192,.10), transparent 60%)}
.cover-inner{position:relative;max-width:1160px;margin:0 auto;
  padding:clamp(38px,6vw,76px) clamp(20px,4vw,44px) clamp(32px,4vw,52px);
  display:flex;flex-direction:column;gap:clamp(18px,2.4vw,26px)}
.cover .eyebrow{color:#7d949e}
.cover h1{font-size:clamp(2.1rem,5.4vw,3.5rem);line-height:1.03;letter-spacing:-.034em;max-width:17ch}
.cover h1 em{font-style:normal;background:linear-gradient(135deg,#0aefc0,#1cd4ff);
  -webkit-background-clip:text;background-clip:text;color:transparent}
.cover p.lead{color:#a7bcc4;max-width:62ch}
.facts{display:flex;flex-wrap:wrap;gap:10px}
.facts span{background:#0d1417;color:#c8d9dd;font-family:var(--mono);font-size:.7rem;
  letter-spacing:.08em;text-transform:uppercase;padding:9px 14px;clip-path:var(--skew-sm)}
.facts b{color:#0aefc0;font-weight:500}

.shell{max-width:1160px;margin:0 auto;padding:clamp(30px,4vw,56px) clamp(20px,4vw,44px) 90px;
  display:grid;gap:clamp(38px,5vw,64px)}
.intro{display:grid;gap:14px;max-width:70ch}
.intro p{color:var(--muted)}
.intro strong{color:var(--text);font-weight:600}

.post{display:grid;gap:18px;scroll-margin-top:24px}
.post-head{display:flex;flex-wrap:wrap;gap:10px 18px;align-items:baseline;
  border-bottom:1px solid var(--line);padding-bottom:14px}
.post-nr{font-family:var(--mono);font-size:1.05rem;color:var(--accent);font-variant-numeric:tabular-nums}
.post-head h2{font-size:1.32rem;letter-spacing:-.02em;flex:1;min-width:12ch}
.tag{font-family:var(--mono);font-size:.63rem;letter-spacing:.11em;text-transform:uppercase;
  color:var(--muted);background:var(--raised-2);padding:5px 9px;white-space:nowrap}
.tag-pin{color:var(--accent-ink);background:var(--accent)}
.tag-todo{color:var(--accent);background:var(--accent-soft)}

.strip{display:flex;gap:12px;overflow-x:auto;padding-bottom:6px}
.shot{flex:none;width:min(232px,44vw);display:grid;gap:7px}
.shot img{width:100%;height:auto;display:block;clip-path:var(--skew-sm);background:var(--raised)}
.shot span{font-family:var(--mono);font-size:.62rem;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
.shot.todo span{color:var(--accent)}

.needs{background:var(--accent-soft);border-left:2px solid var(--accent);
  padding:13px 16px;clip-path:var(--skew-sm);font-size:.94rem}
.needs b{font-family:var(--mono);font-size:.63rem;letter-spacing:.13em;text-transform:uppercase;
  color:var(--accent);font-weight:500;display:block;margin-bottom:3px}

.cap{background:var(--raised);clip-path:var(--skew);display:grid;gap:12px;padding:18px clamp(16px,2vw,22px)}
.cap-top{display:flex;justify-content:space-between;align-items:center;gap:12px}
.cap pre{margin:0;font-family:var(--mono);font-size:.83rem;line-height:1.72;color:var(--text);
  white-space:pre-wrap;overflow-x:auto}
.copy{font-family:var(--mono);font-size:.65rem;letter-spacing:.12em;text-transform:uppercase;
  background:var(--raised-2);color:var(--muted);border:0;cursor:pointer;padding:8px 13px;
  clip-path:var(--skew-sm);transition:color .18s ease,background .18s ease}
.copy:hover{color:var(--text)}
.copy[data-done="1"]{background:var(--accent);color:var(--accent-ink)}
.copy:focus-visible{outline:2px solid var(--accent-2);outline-offset:2px}

.files{display:flex;flex-wrap:wrap;gap:7px}
.files code{font-family:var(--mono);font-size:.68rem;color:var(--muted);background:var(--raised-2);padding:5px 9px}

footer.doc{border-top:1px solid var(--line);padding-top:20px;display:flex;flex-wrap:wrap;
  gap:10px;justify-content:space-between}
footer.doc p{font-family:var(--mono);font-size:.66rem;letter-spacing:.1em;text-transform:uppercase;color:var(--dim)}
@media (prefers-reduced-motion: reduce){*{transition:none!important}}
"""


def build_page() -> str:
    blocks = []
    for post in POSTS:
        files = slide_files(post)

        tags = [f'<span class="tag">{html.escape(post["typ"])}</span>',
                f'<span class="tag">Säule {html.escape(post["saeule"])}</span>']
        if post.get("pin"):
            tags.append('<span class="tag tag-pin">Anpinnen</span>')
        if post.get("braucht"):
            tags.append('<span class="tag tag-todo">Bild fehlt noch</span>')

        shots = []
        for i, (path, is_template) in enumerate(files, start=1):
            label = f"Bild {i} · Vorlage" if is_template else f"Bild {i}"
            cls = "shot todo" if is_template else "shot"
            shots.append(
                f'<figure class="{cls}"><img src="{preview(path)}" alt="Kachel {i} von Beitrag '
                f'{post["nr"]}" loading="lazy"><span>{label}</span></figure>'
            )

        needs = ""
        if post.get("braucht"):
            needs = f'<p class="needs"><b>Wird noch gebraucht</b>{html.escape(post["braucht"])}</p>'
        elif post.get("hinweis"):
            needs = f'<p class="needs"><b>Hinweis</b>{html.escape(post["hinweis"])}</p>'

        names = "".join(f"<code>{html.escape(p.name)}</code>" for p, _ in files)

        blocks.append(f"""
<article class="post" id="post-{post['nr']}">
  <div class="post-head">
    <span class="post-nr">{post['nr']:02d}</span>
    <h2>{html.escape(post['titel'])}</h2>
    {''.join(tags)}
  </div>
  <div class="strip">{''.join(shots)}</div>
  {needs}
  <div class="cap">
    <div class="cap-top">
      <p class="eyebrow">Bildunterschrift</p>
      <button class="copy" type="button">Kopieren</button>
    </div>
    <pre>{html.escape(post['caption'])}</pre>
  </div>
  <div class="files">{names}</div>
</article>""")

    total = sum(len(p["slides"]) for p in POSTS)
    ready = sum(1 for p in POSTS for s in p["slides"] if not s.get("slot"))

    return f"""<title>Pluralo Startsequenz</title>
<style>{fonts_css()}{CSS}</style>

<header class="cover">
  <div class="cover-inner">
    <p class="eyebrow">Instagram · Beitrag 1 bis 9</p>
    <h1>Die Reihenfolge, in der ein Profil <em>überzeugend wird</em>.</h1>
    <p class="lead">Neun Beiträge, fertig gestaltet in 1080 × 1350 px. Zusammen beantworten sie,
      wer Pluralo ist, was die Agentur kann, für wen, warum, und wie man in Kontakt kommt.</p>
    <div class="facts">
      <span><b>9</b> Beiträge</span>
      <span><b>{total}</b> Kacheln</span>
      <span><b>{ready}</b> sofort verwendbar</span>
      <span><b>3</b> zum Anpinnen</span>
    </div>
  </div>
</header>

<div class="shell">
  <section class="intro">
    <p><strong>Warum diese Reihenfolge.</strong> Ein leeres Profil überzeugt niemanden, ein
      halbvolles auch nicht. Deshalb gehören alle neun Beiträge innerhalb von zwei bis drei
      Wochen online, nicht über Monate verteilt. Wer danach das Profil öffnet, sieht einen
      geschlossenen Block statt einer angefangenen Baustelle.</p>
    <p><strong>Die Logik dahinter.</strong> Beitrag 1 sagt, wofür Pluralo steht. 2 und 3 zeigen
      Kompetenz, bevor irgendetwas verkauft wird. 4 liefert den Beweis, 5 das Gesicht dazu.
      6 und 7 nehmen die zwei häufigsten Unsicherheiten vorweg, 8 verankert die Region,
      9 macht den nächsten Schritt einfach.</p>
    <p><strong>Anpinnen nicht vergessen.</strong> Beitrag 1, 4 und 9 werden nach dem
      Veröffentlichen oben festgesetzt. Damit stehen Identität, Beweis und Kontaktweg dauerhaft
      in der ersten Zeile des Rasters, egal was später dazukommt.</p>
    <p><strong>Drei Beiträge brauchen noch ein Bild von Ihnen.</strong> Für die Kacheln mit
      Portrait, Screenshots und Ortsfoto liegt neben der Vorlage jeweils eine freigestellte
      Auflage im Ordner. Diese Datei legen Sie in einem beliebigen Bildprogramm über Ihr eigenes
      Foto, dann sitzen Rahmen, Text und Logo automatisch richtig.</p>
  </section>
  {''.join(blocks)}
  <footer class="doc">
    <p>Pluralo · Startsequenz Instagram</p>
    <p>1080 × 1350 px · Stand August 2026</p>
  </footer>
</div>

<script>
document.querySelectorAll('.copy').forEach(function (btn) {{
  btn.addEventListener('click', function () {{
    var text = btn.closest('.cap').querySelector('pre').textContent;
    navigator.clipboard.writeText(text).then(function () {{
      btn.textContent = 'Kopiert';
      btn.dataset.done = '1';
      setTimeout(function () {{ btn.textContent = 'Kopieren'; btn.dataset.done = '0'; }}, 1800);
    }});
  }});
}});
</script>
"""


if __name__ == "__main__":
    write_captions()
    page = build_page()
    (HERE / "uebersicht.html").write_text(page, encoding="utf-8")
    print(f"captions.md und uebersicht.html geschrieben ({len(page) / 1024:.0f} KB)")
