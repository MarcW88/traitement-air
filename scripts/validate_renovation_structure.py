from pathlib import Path
from html.parser import HTMLParser

ROOT = Path(__file__).resolve().parents[1]
CATEGORIES = [
    'renovatie-plannen',
    'renovatieprojecten',
    'verduurzamen',
    'problemen-oplossen',
    'vakman-en-offertes',
    'doe-het-zelf',
]

class PageParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.html_lang = None
        self.h1 = 0
        self.title = 0
        self._in_title = False
        self.title_text = []
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == 'html':
            self.html_lang = attrs.get('lang')
        elif tag == 'h1':
            self.h1 += 1
        elif tag == 'title':
            self.title += 1
            self._in_title = True
    def handle_endtag(self, tag):
        if tag == 'title':
            self._in_title = False
    def handle_data(self, data):
        if self._in_title:
            self.title_text.append(data.strip())

errors = []
pages = []
for category in CATEGORIES:
    folder = ROOT / category
    if not folder.is_dir():
        errors.append(f'Ontbrekende hoofdmap: {category}/')
        continue
    index = folder / 'index.html'
    if not index.exists():
        errors.append(f'Ontbrekende categoriepagina: {category}/index.html')
    pages.extend(folder.rglob('index.html'))

seen_titles = {}
for page in sorted(set(pages)):
    parser = PageParser()
    parser.feed(page.read_text(encoding='utf-8'))
    rel = page.relative_to(ROOT)
    if parser.html_lang != 'nl':
        errors.append(f'{rel}: html lang moet nl zijn')
    if parser.h1 != 1:
        errors.append(f'{rel}: verwacht exact 1 H1, gevonden {parser.h1}')
    if parser.title != 1:
        errors.append(f'{rel}: verwacht exact 1 title, gevonden {parser.title}')
    title = ' '.join(x for x in parser.title_text if x).strip()
    if title:
        if title in seen_titles:
            errors.append(f'{rel}: dubbele title met {seen_titles[title]}: {title}')
        else:
            seen_titles[title] = rel

if errors:
    print('\n'.join(errors))
    raise SystemExit(1)
print(f'PASS: {len(set(pages))} renovatiepagina\'s hebben geldige NL-basisstructuur')
