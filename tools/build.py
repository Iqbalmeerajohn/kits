"""Build everything that is generated:
  1. inject the shared engine into each template
  2. copy templates to preview/<name>/ with a storefront banner + noindex (not shipped in the zip)
  3. screenshots of each template at 1440 and 390 -> img/*.webp   (python tools/build.py --shots)
  4. dist/ zips and PDFs
Run from anywhere:  python tools/build.py [--shots]"""
import pathlib, shutil, subprocess, sys, zipfile, io, time

ROOT = pathlib.Path(__file__).resolve().parent.parent
TPL = ROOT / "products" / "local-business-templates"
PREVIEW = ROOT / "preview"
DIST = ROOT / "dist"
NAMES = ["dental-clinic", "beauty-salon", "hair-studio", "fitness-studio", "strength-gym"]

BANNER = """<style>.kits-bar{position:fixed;left:0;right:0;bottom:0;z-index:9990;display:flex;flex-wrap:wrap;gap:6px 14px;align-items:center;justify-content:center;padding:10px 16px calc(10px + env(safe-area-inset-bottom,0px));background:#111214;color:#f4f4f5;font:500 13.5px/1.4 system-ui,sans-serif;text-align:center}.kits-bar a{color:#9fb0ff;font-weight:600}body{padding-bottom:64px}</style>
<div class="kits-bar" role="note"><span>Template preview. The business, reviews and contact details are fictional.</span><a href="../../#templates">Get this template pack</a></div>
"""

def run(cmd):
    print("$", " ".join(cmd)); subprocess.run(cmd, check=True, cwd=ROOT)

def previews():
    # no rmtree: on Windows a just-deleted folder can't be recreated immediately
    for n in NAMES:
        dst = PREVIEW / n
        shutil.copytree(TPL / n, dst, dirs_exist_ok=True)
        f = dst / "index.html"; s = f.read_text(encoding="utf-8")
        s = s.replace('<meta charset="utf-8">', '<meta charset="utf-8">\n<meta name="robots" content="noindex">', 1)
        s = s.replace("</body>", BANNER + "</body>", 1)
        for attempt in range(10):  # Windows antivirus can briefly lock freshly copied files
            try: f.write_text(s, encoding="utf-8"); break
            except PermissionError: time.sleep(0.5)
        else: raise
    print("previews ->", PREVIEW)

def shots():
    from playwright.sync_api import sync_playwright
    from PIL import Image
    import http.server, threading, functools
    class Quiet(http.server.SimpleHTTPRequestHandler):
        def log_message(self, *a): pass
    handler = functools.partial(Quiet, directory=str(TPL))
    srv = http.server.ThreadingHTTPServer(("127.0.0.1", 0), handler)
    threading.Thread(target=srv.serve_forever, daemon=True).start()
    base = f"http://127.0.0.1:{srv.server_address[1]}"
    out = ROOT / "img"; out.mkdir(exist_ok=True)
    with sync_playwright() as p:
        b = p.chromium.launch()
        for n in NAMES:
            for w, h, scale, target in [(1440, 900, 1, 1200), (390, 844, 2, 600)]:
                ctx = b.new_context(viewport={"width": w, "height": h}, device_scale_factor=scale, color_scheme="light", reduced_motion="reduce")
                pg = ctx.new_page(); pg.goto(f"{base}/{n}/", wait_until="networkidle"); pg.wait_for_timeout(1500)
                png = pg.screenshot(); ctx.close()
                im = Image.open(io.BytesIO(png)).convert("RGB")
                im = im.resize((target, round(im.height * target / im.width)), Image.LANCZOS)
                dest = out / f"tpl-{n}-{w}.webp"; im.save(dest, "WEBP", quality=80, method=6)
                print("shot", dest.name, im.size, dest.stat().st_size)
        # checklist thumbnail
        pg = b.new_page(viewport={"width": 794, "height": 1123}, device_scale_factor=1)
        pg.goto((ROOT / "products/checklist/checklist.html").as_uri(), wait_until="networkidle"); pg.emulate_media(media="print"); pg.wait_for_timeout(400)
        im = Image.open(io.BytesIO(pg.screenshot(clip={"x": 0, "y": 0, "width": 794, "height": 790}))).convert("RGB").resize((300, 298), Image.LANCZOS)
        im.save(out / "checklist.webp", "WEBP", quality=82, method=6); pg.close()
        # Open Graph image 1200x630
        d = (out / "tpl-dental-clinic-1440.webp").as_uri(); m = (out / "tpl-beauty-salon-390.webp").as_uri()
        og = f'''<html><head><link href="https://fonts.googleapis.com/css2?family=Geist:wght@500;700&display=swap" rel="stylesheet"><style>
        body{{margin:0;width:1200px;height:630px;background:#f5f5f4;font-family:Geist,sans-serif;display:grid;grid-template-columns:520px 1fr;overflow:hidden}}
        .t{{padding:64px 0 0 64px}} h1{{font-size:58px;line-height:1.04;letter-spacing:-2px;margin:0 0 22px;color:#141518}}
        p{{font-size:24px;color:#565a63;margin:0}} .b{{position:absolute;left:64px;bottom:56px;font:700 26px Geist;color:#141518}} .b span{{color:#2340d8}}
        .d{{position:absolute;left:560px;top:70px;width:600px;border-radius:14px;overflow:hidden;box-shadow:0 30px 60px -30px rgba(20,24,40,.45);border:1px solid #dcdcd8}}
        .m{{position:absolute;left:1000px;top:250px;width:150px;border-radius:20px;overflow:hidden;border:5px solid #141518}} img{{display:block;width:100%}}
        </style></head><body><div class="t"><h1>Website templates and AI prompts for Indian local businesses</h1><p>5 templates with live demos. 126 marketing prompts.</p></div>
        <div class="b">Kits <span>by Iqbal</span></div><div class="d"><img src="{d}"></div><div class="m"><img src="{m}"></div></body></html>'''
        tmp = ROOT / "dist" / "_og.html"; tmp.parent.mkdir(exist_ok=True); tmp.write_text(og, encoding="utf-8")
        pg = b.new_page(viewport={"width": 1200, "height": 630}); pg.goto(tmp.as_uri(), wait_until="networkidle"); pg.wait_for_timeout(500)
        Image.open(io.BytesIO(pg.screenshot())).convert("RGB").save(out / "og.jpg", "JPEG", quality=86); pg.close(); tmp.unlink()
        print("assets: checklist.webp, og.jpg")
        b.close()
    srv.shutdown()

def zips():
    DIST.mkdir(exist_ok=True)
    z1 = DIST / "local-business-templates-v1.zip"
    with zipfile.ZipFile(z1, "w", zipfile.ZIP_DEFLATED) as z:
        root = "local-business-templates-v1/"
        for extra in ["README.md", "LICENSE.txt"]:
            z.write(TPL / extra, root + extra)
        for n in NAMES:
            for f in sorted((TPL / n).rglob("*")):
                if f.is_file(): z.write(f, root + n + "/" + f.relative_to(TPL / n).as_posix())
    pp = ROOT / "products" / "prompt-pack"
    z2 = DIST / "ai-prompt-pack-india-v1.zip"
    with zipfile.ZipFile(z2, "w", zipfile.ZIP_DEFLATED) as z:
        root = "ai-prompt-pack-india-v1/"
        z.write(pp / "AI-Marketing-Prompt-Pack-India.pdf", root + "AI-Marketing-Prompt-Pack-India.pdf")
        z.write(pp / "prompts.md", root + "AI-Marketing-Prompt-Pack-India.md")
        z.writestr(root + "READ-ME-FIRST.txt", "Small Business AI Marketing Prompt Pack: India Edition (v1)\n\n"
            "AI-Marketing-Prompt-Pack-India.pdf  The formatted pack, best for reading and printing.\n"
            "AI-Marketing-Prompt-Pack-India.md   The same prompts as plain text, easy to copy into ChatGPT, Gemini or Claude,\n"
            "                                     or import into Notion / Google Docs.\n\n"
            "Licence: use the prompts in your own business and for clients you serve. Please do not resell or share the files.\n"
            "Questions: iqbalmeerajohn1@gmail.com\n")
    shutil.copy(ROOT / "products" / "checklist" / "website-launch-checklist.pdf", DIST / "website-launch-checklist.pdf")
    for f in sorted(DIST.iterdir()): print(f"{f.name:40s} {f.stat().st_size/1024:8.1f} KB")

if __name__ == "__main__":
    run([sys.executable, "tools/inject_sitekit.py"])
    previews()
    if "--shots" in sys.argv: shots()
    zips()
