#!/usr/bin/env python3
"""Build a complete sitemap from published static routes and real Git edit dates."""
from datetime import datetime, timezone
from pathlib import Path
from subprocess import run
import re
import xml.etree.ElementTree as ET

ROOT = Path(__file__).resolve().parents[1]
HOST = "https://traitement-air.fr"
EXCLUDED = {"404", "_next", ".agents", ".content", "assets", "docs", "scripts", "content"}
ET.register_namespace("", "http://www.sitemaps.org/schemas/sitemap/0.9")
NS = "http://www.sitemaps.org/schemas/sitemap/0.9"

def published_pages():
    for page in sorted(ROOT.rglob("index.html")):
        rel = page.relative_to(ROOT)
        if any(part.startswith(".") or part in EXCLUDED for part in rel.parts[:-1]):
            continue
        html = page.read_text(encoding="utf-8")
        canonical = re.search(r'<link[^>]+rel=["\']canonical["\'][^>]+href=["\']([^"\']+)', html, re.I)
        if not canonical:
            raise ValueError(f"Missing canonical: {rel}")
        url = canonical.group(1)
        expected = HOST + "/" + ("" if rel == Path("index.html") else rel.parent.as_posix() + "/")
        if url != expected:
            raise ValueError(f"Unexpected canonical: {rel}: {url} != {expected}")
        if re.search(r'<meta[^>]+name=["\']robots["\'][^>]+content=["\'][^"\']*noindex', html, re.I):
            continue
        yield rel, url

def last_modified(rel):
    result = run(["git", "log", "-1", "--format=%cs", "--", rel.as_posix()],
                 cwd=ROOT, capture_output=True, text=True, check=False)
    value = result.stdout.strip()
    if not re.fullmatch(r"\d{4}-\d{2}-\d{2}", value):
        raise RuntimeError(f"No Git last-modified date for {rel}; fetch full history (fetch-depth: 0)")
    return value

def main():
    pages = list(published_pages())
    urls = [url for _, url in pages]
    if len(urls) != len(set(urls)):
        raise ValueError("Duplicate canonicals in published pages")
    root = ET.Element(f"{{{NS}}}urlset")
    for rel, url in pages:
        node = ET.SubElement(root, f"{{{NS}}}url")
        ET.SubElement(node, f"{{{NS}}}loc").text = url
        ET.SubElement(node, f"{{{NS}}}lastmod").text = last_modified(rel)
    ET.indent(root, space="  ")
    ET.ElementTree(root).write(ROOT / "sitemap.xml", encoding="utf-8", xml_declaration=True)
    print(f"Sitemap: {len(urls)} canonical indexable pages with Git lastmod")

if __name__ == "__main__":
    main()
