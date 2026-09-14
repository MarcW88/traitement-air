#!/usr/bin/env python3
"""Machine-detectable publication blockers for active editorial routes.

This validator deliberately does not score editorial quality with word counts,
heading quotas, link quotas, source quotas, FAQ requirements or mandatory page
shapes. Those questions belong to air-treatment-analysis-workflow / PUBLISH_REVIEW.
"""
from pathlib import Path
import html as html_lib
import json
import re
from urllib.parse import urlsplit

ROOT = Path(__file__).resolve().parents[1]
CONTENT = ROOT / "content"
SITE = json.loads((CONTENT / "site.json").read_text(encoding="utf-8"))
SITE_ORIGIN = SITE["base_url"].rstrip("/")
EXPECTED_ROBOTS = "index,follow" if SITE.get("indexing_enabled", False) else "noindex,follow"

ARTICLE_RE = re.compile(
    r'<article\b[^>]*class="[^"]*article-main[^"]*"[^>]*>(.*?)</article>',
    re.S | re.I,
)
H1_RE = re.compile(r'<h1\b[^>]*>(.*?)</h1>', re.S | re.I)
TITLE_RE = re.compile(r'<title>(.*?)</title>', re.S | re.I)
META_DESCRIPTION_RE = re.compile(
    r'<meta\b[^>]*name="description"[^>]*content="([^"]*)"[^>]*>', re.I
)
CANONICAL_RE = re.compile(
    r'<link\b[^>]*rel="canonical"[^>]*href="([^"]+)"[^>]*>', re.I
)
ROBOTS_RE = re.compile(
    r'<meta\b[^>]*name="robots"[^>]*content="([^"]+)"[^>]*>', re.I
)
ID_RE = re.compile(r'\bid="([^"]+)"', re.I)
HREF_RE = re.compile(r'<a\b[^>]*href="([^"]+)"', re.I)
TAG_RE = re.compile(r"<[^>]+>", re.S)

PLACEHOLDER_PATTERNS = (
    "<!-- Contenu à rédiger -->",
    "<!-- Inhoud nog te schrijven -->",
    "Lorem ipsum",
    "TODO_CONTENT",
    "CONTENT_PLACEHOLDER",
)


def clean_text(raw: str) -> str:
    raw = TAG_RE.sub(" ", raw)
    raw = html_lib.unescape(raw)
    return re.sub(r"\s+", " ", raw).strip()


def route_for_body(body: Path) -> str:
    return body.parent.relative_to(CONTENT).as_posix()


def generated_page(route: str) -> Path:
    return ROOT / route / "index.html"


def expected_canonical(route: str) -> str:
    return f"{SITE_ORIGIN}/{route.strip('/')}/"


def local_target_exists(href: str) -> bool:
    parsed = urlsplit(href)
    path = parsed.path
    if not path or not path.startswith("/") or path.startswith("//"):
        return True
    if path == "/":
        return (ROOT / "index.html").exists()
    target = ROOT / path.lstrip("/")
    if target.is_dir():
        target = target / "index.html"
    return target.exists()


def active_bodies() -> list[Path]:
    bodies = []
    for body in CONTENT.glob("**/body.html"):
        # Only route content is in nested route directories. Ignore accidental
        # root-level fragments if they are ever introduced later.
        if body.parent == CONTENT:
            continue
        bodies.append(body)
    return sorted(bodies)


def inspect(route: str, body_path: Path) -> list[str]:
    issues = []
    body_html = body_path.read_text(encoding="utf-8")
    page_path = generated_page(route)

    article_matches = ARTICLE_RE.findall(body_html)
    if len(article_matches) != 1:
        issues.append(
            f"source article.article-main count={len(article_matches)} (expected 1)"
        )
        article = article_matches[0] if article_matches else ""
    else:
        article = article_matches[0]

    if not clean_text(article):
        issues.append("source article.article-main empty")

    for marker in PLACEHOLDER_PATTERNS:
        if marker.lower() in body_html.lower():
            issues.append(f"placeholder present in source: {marker}")

    if not page_path.exists():
        issues.append(f"generated page missing: {page_path.relative_to(ROOT)}")
        return issues

    page_html = page_path.read_text(encoding="utf-8")

    title = TITLE_RE.findall(page_html)
    if len(title) != 1 or not clean_text(title[0]):
        issues.append("missing or empty <title>")

    descriptions = META_DESCRIPTION_RE.findall(page_html)
    if len(descriptions) != 1 or not descriptions[0].strip():
        issues.append("missing or empty meta description")

    h1s = H1_RE.findall(page_html)
    if len(h1s) != 1 or not clean_text(h1s[0]):
        issues.append(f"H1 count={len(h1s)} (expected one non-empty H1)")

    robots = ROBOTS_RE.findall(page_html)
    normalized = [
        ",".join(part.strip().lower() for part in value.split(","))
        for value in robots
    ]
    if EXPECTED_ROBOTS not in normalized:
        issues.append(
            f"robots publication state mismatch: expected {EXPECTED_ROBOTS}"
        )

    canonicals = CANONICAL_RE.findall(page_html)
    canonical = expected_canonical(route)
    if len(canonicals) != 1:
        issues.append(f"canonical count={len(canonicals)} (expected 1)")
    elif canonicals[0] != canonical:
        issues.append(f"canonical mismatch: {canonicals[0]} != {canonical}")

    ids = ID_RE.findall(body_html)
    duplicates = sorted({value for value in ids if ids.count(value) > 1})
    if duplicates:
        issues.append("duplicate source IDs: " + ", ".join(duplicates))
    id_set = set(ids)

    for href in HREF_RE.findall(article):
        if href.startswith("#"):
            anchor = href[1:]
            if anchor and anchor not in id_set:
                issues.append(f"broken in-page anchor: {href}")
            continue
        if href.startswith("/") and not local_target_exists(href):
            issues.append(f"broken internal link: {href}")

    return issues


def main() -> None:
    bodies = active_bodies()
    if not bodies:
        print("PASS: no active content sources; static routes remain unchanged")
        return

    failures = {}
    for body in bodies:
        route = route_for_body(body)
        issues = inspect(route, body)
        if issues:
            failures[route] = issues

    if failures:
        for route, issues in failures.items():
            print(f"FAIL /{route}/")
            for issue in issues:
                print(f"  - {issue}")
        raise SystemExit(1)

    print(
        f"PASS: {len(bodies)} active editorial routes have no machine-detectable "
        "publication blockers"
    )
    print(
        "NOTE: machine validation does not replace air-treatment-analysis-workflow / "
        "PUBLISH_REVIEW or human editorial judgment."
    )


if __name__ == "__main__":
    main()
