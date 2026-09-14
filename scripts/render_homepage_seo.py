from pathlib import Path
from html import escape
import json
import re

R = Path(__file__).resolve().parents[1]
SITE = json.loads((R / "content" / "site.json").read_text(encoding="utf-8"))

SITE_URL = SITE["base_url"].rstrip("/")
SITE_NAME = SITE["site_name"]
SITE_LANGUAGE = SITE.get("language", "nl-NL")
INDEXING_ENABLED = bool(SITE.get("indexing_enabled", False))
ROBOTS_DIRECTIVE = "index,follow" if INDEXING_ENABLED else "noindex,follow"

HOME = SITE["homepage"]
TITLE = HOME["title"]
DESCRIPTION = HOME["description"]
CANONICAL = f"{SITE_URL}/"

schema = json.dumps(
    {
        "@context": "https://schema.org",
        "@graph": [
            {
                "@type": "Organization",
                "@id": f"{SITE_URL}/#organization",
                "name": SITE_NAME,
                "url": CANONICAL,
            },
            {
                "@type": "WebSite",
                "@id": f"{SITE_URL}/#website",
                "url": CANONICAL,
                "name": SITE_NAME,
                "inLanguage": SITE_LANGUAGE,
                "publisher": {"@id": f"{SITE_URL}/#organization"},
            },
            {
                "@type": "WebPage",
                "@id": f"{SITE_URL}/#webpage",
                "url": CANONICAL,
                "name": TITLE,
                "description": DESCRIPTION,
                "inLanguage": SITE_LANGUAGE,
                "isPartOf": {"@id": f"{SITE_URL}/#website"},
                "about": {"@id": f"{SITE_URL}/#organization"},
            },
        ],
    },
    ensure_ascii=False,
    separators=(",", ":"),
)

head = f'''<head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="robots" content="{ROBOTS_DIRECTIVE}"><meta name="theme-color" content="#24483D"><link rel="icon" href="/favicon.svg" type="image/svg+xml"><title>{escape(TITLE)}</title><meta name="description" content="{escape(DESCRIPTION, quote=True)}"><link rel="canonical" href="{CANONICAL}"><meta property="og:locale" content="nl_NL"><meta property="og:type" content="website"><meta property="og:site_name" content="{escape(SITE_NAME, quote=True)}"><meta property="og:title" content="{escape(TITLE, quote=True)}"><meta property="og:description" content="{escape(DESCRIPTION, quote=True)}"><meta property="og:url" content="{CANONICAL}"><link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin><link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600&family=Manrope:wght@500;600;700;800&display=optional" rel="stylesheet"><link rel="stylesheet" href="/css/style.css"><link rel="stylesheet" href="/css/audit-fixes.css"><script type="application/ld+json">{schema}</script><script src="/js/site.js" defer></script></head>'''


def neutralize_comparison_ctas(html):
    html = html.replace(
        '>Zo werkt vergelijken ↗</a>',
        '>Zo vergelijk je offertes ↗</a>',
    )
    html = html.replace(
        '<a class="button small" href="/vakman-en-offertes/offertes-vergelijken/">Vergelijk vakmensen ↗</a>',
        '<a class="button small" href="/vakman-en-offertes/vakman-kiezen/">Vakman kiezen ↗</a>',
    )
    html = html.replace(
        '<small>Vergelijk ervaring, aanpak en offertes voor jouw project.</small>',
        '<small>Leer waar je op let bij ervaring, aanpak en offertes.</small>',
    )
    html = html.replace(
        '<a href="/vakman-en-offertes/offertes-vergelijken/">Vergelijk vakmensen →</a>',
        '<a href="/vakman-en-offertes/vakman-kiezen/">Zo kies je een vakman →</a>',
    )
    html = html.replace(
        '<p>Vergelijk vakmensen die ervaring hebben met jouw type project.</p>',
        '<p>Lees waar je op let bij een vakman voor jouw type project.</p>',
    )
    html = html.replace(
        '<a class="button accent" href="/vakman-en-offertes/offertes-vergelijken/">Vergelijk vakmensen →</a>',
        '<a class="button accent" href="/vakman-en-offertes/vakman-kiezen/">Vakman kiezen →</a>',
    )
    return html


homepage = R / "index.html"
html = neutralize_comparison_ctas(homepage.read_text(encoding="utf-8"))
updated, count = re.subn(r"<head>.*?</head>", head, html, count=1, flags=re.DOTALL)
if count != 1:
    raise SystemExit("Could not replace homepage <head>")
homepage.write_text(updated, encoding="utf-8")

for page in R.rglob("index.html"):
    if page == homepage or ".git" in page.parts:
        continue
    current = page.read_text(encoding="utf-8")
    revised = neutralize_comparison_ctas(current)
    if revised != current:
        page.write_text(revised, encoding="utf-8")

print("Updated homepage SEO and neutralized comparison CTAs with", ROBOTS_DIRECTIVE)
