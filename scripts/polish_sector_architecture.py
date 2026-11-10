#!/usr/bin/env python3
"""Polish the existing sector directory and address evidenced Axe contrast issues."""
from pathlib import Path
import re
from html import escape

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {".agents",".content","assets","content","scripts","_next",".artifacts"}
css = """
/* Contrast corrections identified by desktop/mobile Axe audit. */
.brand b{color:#a84d18!important}
.breadcrumbs,.breadcrumbs a,.breadcrumbs span,.page-hero .shell>p,
.hero-copy>p,.section-heading>p,.air-label,.sector-list>a>p,
.cta-band .shell>p{color:#4b5e59!important}
.directory-grid>a>span,.problem-strip a>i,.finder-step>span,
.sector-list>a>span{color:#23635f!important}
.process-section.inverse h2 em,.inverse h2 em{color:#b9e8d9!important}
.inverse p a{color:#ffffff!important;text-decoration:underline}
.result-line>i{color:#ffffff!important}
"""
marker="/* Contrast corrections identified by desktop/mobile Axe audit. */"
edited=0
for p in ROOT.rglob("index.html"):
    rel=p.relative_to(ROOT)
    if any(part.startswith(".") or part in EXCLUDE for part in rel.parts[:-1]):
        continue
    s=p.read_text(encoding="utf-8")
    if 'id="sector-architecture-css"' not in s:continue
    if marker in s:continue
    start=s.index('<style id="sector-architecture-css">')
    close=s.index("</style>",start)
    s=s[:close]+css+s[close:]
    p.write_text(s,encoding="utf-8")
    edited+=1

p=ROOT/"secteurs/index.html"
s=p.read_text(encoding="utf-8")
start=s.index('<div class="sector-catalogue">')
end=s.index('<section class="section shell" aria-labelledby="secteurs-analyse"',start)
before=s[start:end]
ordinal=0
def enhance(match):
    global ordinal
    slug,inside=match.group(1),match.group(2)
    ordinal+=1
    assert re.search(r'<h3>[^<]+</h3>',inside),"Missing card heading "+slug
    inside=re.sub(r'<span>\d+</span>',f'<span>{ordinal:02d}</span>',inside,count=1)
    if '<img ' not in inside:
        asset=ROOT/f"assets/generated/secteurs-traitement-air-{slug}-editorial.webp"
        assert asset.is_file(),"Missing BFL image for "+slug
        label=re.search(r'<h3>([^<]+)</h3>',inside).group(1)
        img=(f'<img class="directory-thumb" src="/assets/generated/secteurs-traitement-air-{slug}-editorial.webp" '
             f'alt="Illustration du secteur {escape(label,quote=True)}" loading="lazy" decoding="async" '
             'width="1024" height="672">')
        inside=img+inside
    return f'<a href="/secteurs/traitement-air-{slug}/">'+inside+'</a>'
after=re.sub(r'<a href="/secteurs/traitement-air-([^/]+)/">([\s\S]*?)</a>',enhance,before)
assert ordinal==26, f"Expected 26 cards, found {ordinal}"
s=s[:start]+after+s[end:]
p.write_text(s,encoding="utf-8")
print(f"Polished {edited} HTML pages for contrast; 26 sector cards now numbered and illustrated.")
