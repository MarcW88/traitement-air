from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
CONTENT_ROOT = ROOT / 'content'
CATEGORIES = [
    'renovatie-plannen', 'renovatieprojecten', 'verduurzamen',
    'problemen-oplossen', 'vakman-en-offertes', 'doe-het-zelf'
]

errors = []
active = 0
empty = 0

for category in CATEGORIES:
    for page in (ROOT / category).rglob('index.html'):
        relative_page = page.relative_to(ROOT)
        route = relative_page.parent
        content_file = CONTENT_ROOT / route / 'body.html'
        text = page.read_text(encoding='utf-8')
        has_skeleton = 'class="skeleton"' in text and 'aria-label="Lege contentruimte"' in text

        if content_file.exists():
            active += 1
            if has_skeleton:
                errors.append(f'{relative_page}: contentbron bestaat maar gegenereerde pagina is nog leeg')
            if 'class="content-page"' not in text:
                errors.append(f'{relative_page}: actieve contentpagina mist content-page marker')
        else:
            empty += 1
            if not has_skeleton:
                errors.append(f'{relative_page}: geen contentbron maar pagina bevat geen lege content-shell')

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)

print(f'PASS: {active} actieve contentpagina\'s, {empty} routes blijven bewust leeg')
