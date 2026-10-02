"""Headless QA: console errors, failed requests, horizontal scroll, stuck-hidden reveals.
Usage: python tools/qa.py BASE_URL path1 path2 ...   (paths relative to BASE_URL)"""
import asyncio, sys
from playwright.async_api import async_playwright

BASE = sys.argv[1].rstrip("/")
PATHS = sys.argv[2:] or ["/"]
VIEWPORTS = [("1440", {"width": 1440, "height": 900}), ("390", {"width": 390, "height": 844})]

async def check(browser, path, tag, vp):
    pg = await browser.new_page(viewport=vp)
    errs, bad = [], []
    pg.on("pageerror", lambda e: errs.append(str(e)[:160]))
    pg.on("console", lambda m: m.type == "error" and errs.append(m.text[:160]))
    pg.on("response", lambda r: r.status >= 400 and bad.append(f"{r.status} {r.url}"))
    await pg.goto(BASE + path, wait_until="networkidle")
    await pg.wait_for_timeout(1200)
    H = await pg.evaluate("document.documentElement.scrollHeight")
    for f in (.25, .5, .75, 1):
        await pg.evaluate(f"window.scrollTo(0, {H}*{f})"); await pg.wait_for_timeout(500)
    await pg.wait_for_timeout(800)
    ov = await pg.evaluate("document.documentElement.scrollWidth - document.documentElement.clientWidth")
    hidden = await pg.evaluate("[...document.querySelectorAll('.reveal,.rv,.r')].filter(e=>getComputedStyle(e).opacity<0.5).length")
    await pg.close()
    ok = not errs and not bad and ov <= 0
    print(f"{'PASS' if ok else 'FAIL'} {path:40s} {tag:>4}px hscroll={ov} console_errors={len(errs)} http_errors={len(bad)} stuck_hidden={hidden} {errs[:2]} {bad[:2]}")
    return ok

async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        results = [await check(b, path, tag, vp) for path in PATHS for tag, vp in VIEWPORTS]
        await b.close()
    print(f"\n{sum(results)}/{len(results)} checks passed")
    sys.exit(0 if all(results) else 1)

asyncio.run(main())
