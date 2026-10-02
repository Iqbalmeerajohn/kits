"""Copy tools/sitekit.js into every template between the SITEKIT markers.
Each template stays a single standalone file for the buyer."""
import pathlib, re
ROOT = pathlib.Path(__file__).resolve().parent.parent
kit = (ROOT / "tools" / "sitekit.js").read_text(encoding="utf-8").strip()
pat = re.compile(r"/\* SITEKIT:BEGIN.*?/\* SITEKIT:END \*/", re.S)
for f in sorted((ROOT / "products" / "local-business-templates").glob("*/index.html")):
    src = f.read_text(encoding="utf-8")
    if not pat.search(src):
        raise SystemExit(f"no SITEKIT markers in {f}")
    f.write_text(pat.sub(lambda m: kit, src, count=1), encoding="utf-8")
    print("injected", f.parent.name)
