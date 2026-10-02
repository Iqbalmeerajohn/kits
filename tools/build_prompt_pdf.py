"""Build products/prompt-pack/prompts.html and dist PDF from prompts.md."""
import pathlib, re, markdown
from playwright.sync_api import sync_playwright

ROOT = pathlib.Path(__file__).resolve().parent.parent
SRC = ROOT / "products" / "prompt-pack" / "prompts.md"
OUT_HTML = ROOT / "products" / "prompt-pack" / "prompts.html"
OUT_PDF = ROOT / "products" / "prompt-pack" / "AI-Marketing-Prompt-Pack-India.pdf"

md = SRC.read_text(encoding="utf-8")
title_block, body_md = md.split("---", 1)
body = markdown.markdown(body_md, extensions=["tables", "fenced_code"])
# wrap each prompt (h3 + following blocks until next h3/h2/hr) in an article so it never splits across pages
body = re.sub(r"(<h3>.*?)(?=<h3>|<h2>|<hr />|\Z)", r'<article class="p">\1</article>', body, flags=re.S)
# section headings start new pages
sections = re.findall(r"<h2>(.*?)</h2>", body)
toc = "".join(f"<li>{s}</li>" for s in sections if s.startswith("Section"))
body = body.replace("<h2>Section A", '<h2 class="brk">Section A', 1)
for s in sections:
    if s.startswith("Section") and not s.startswith("Section A"):
        body = body.replace(f"<h2>{s}</h2>", f'<h2 class="brk">{s}</h2>', 1)

CSS = """
@page{size:A4;margin:18mm 16mm 18mm 16mm}
:root{--ink:#16181d;--mute:#575d68;--line:#dfe2e8;--accent:#2340d8;--tint:#f1f3fb}
*{box-sizing:border-box}
body{font:10.5pt/1.55 "Geist","Noto Sans Telugu","Noto Sans Devanagari","Nirmala UI",system-ui,sans-serif;color:var(--ink);margin:0}
.cover{height:257mm;display:flex;flex-direction:column;justify-content:space-between;page-break-after:always;border-left:6mm solid var(--accent);padding:12mm 0 4mm 12mm}
.cover .k{font:600 10pt "Geist Mono",monospace;color:var(--accent);letter-spacing:.08em;text-transform:uppercase}
.cover h1{font-size:40pt;line-height:1.02;letter-spacing:-.02em;margin:10mm 0 6mm;max-width:15ch}
.cover p{font-size:13pt;color:var(--mute);max-width:42ch;margin:0}
.cover .n{font:700 64pt/1 "Geist",sans-serif;color:var(--accent)}
.cover .who{font-size:10pt;color:var(--mute)}
.toc{page-break-after:always}
.toc h2{font-size:20pt;margin:0 0 6mm}
.toc ol{padding-left:5mm;font-size:12pt;line-height:2}
h2{font-size:19pt;letter-spacing:-.01em;margin:0 0 3mm;color:var(--ink)}
h2.brk{page-break-before:always;border-top:3px solid var(--accent);padding-top:4mm}
h3{font-size:11.5pt;margin:0 0 2mm}
article.p{break-inside:avoid;page-break-inside:avoid;margin:0 0 5mm;padding-top:1mm}
pre{background:var(--tint);border:1px solid #d9def0;border-radius:6px;padding:3mm 4mm;margin:0 0 2mm;white-space:pre-wrap;word-wrap:break-word;font:9.6pt/1.5 "Geist Mono","Consolas",monospace;color:#1d2433}
code{font-family:"Geist Mono","Consolas",monospace;font-size:.92em}
blockquote{margin:2mm 0 0;padding:2.5mm 4mm;border-left:3px solid var(--accent);background:#fafbfd;color:#2a2f38;font-size:10pt}
blockquote p{margin:0 0 1.5mm}
table{border-collapse:collapse;width:100%;margin:2mm 0 4mm;font-size:10pt}
th,td{border-bottom:1px solid var(--line);padding:1.8mm 2mm;text-align:left;vertical-align:top}
th{color:var(--mute);font-weight:600}
hr{border:0;margin:0}
p{margin:0 0 2.5mm}
ul{margin:0 0 3mm;padding-left:5mm}
em{color:var(--mute)}
"""
html = f"""<!doctype html><html lang="en"><head><meta charset="utf-8">
<title>Small Business AI Marketing Prompt Pack: India Edition</title>
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Geist:wght@400;600;700&family=Geist+Mono:wght@400;600&family=Noto+Sans+Telugu:wght@400;600&family=Noto+Sans+Devanagari:wght@400;600&display=swap" rel="stylesheet">
<style>{CSS}</style></head><body>
<section class="cover">
 <div class="k">India edition · Version 1.0</div>
 <div><div class="n">126</div><h1>Small Business AI Marketing Prompts</h1>
 <p>Copy, fill in the brackets, paste into ChatGPT, Gemini or Claude. Google Business posts, WhatsApp broadcasts, Instagram captions, festival offers, review replies and Telugu and Hindi versions.</p></div>
 <div class="who">By Sheik Iqbal Meera John · iqbalmeerajohn.github.io/portfolio</div>
</section>
<section class="toc"><h2>Contents</h2><ol style="list-style:none;padding:0"><li>How to use this pack</li>{toc}<li>Final checklist before you post</li></ol></section>
{body}
</body></html>"""
OUT_HTML.write_text(html, encoding="utf-8")
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page()
    pg.goto(OUT_HTML.as_uri(), wait_until="networkidle"); pg.wait_for_timeout(800)
    pg.pdf(path=str(OUT_PDF), format="A4", print_background=True, prefer_css_page_size=True,
           display_header_footer=True, header_template="<span></span>",
           footer_template='<div style="font:8px sans-serif;color:#888;width:100%;padding:0 16mm;display:flex;justify-content:space-between"><span>AI Marketing Prompt Pack: India Edition</span><span><span class="pageNumber"></span> / <span class="totalPages"></span></span></div>')
    b.close()
print("wrote", OUT_PDF, OUT_PDF.stat().st_size)
