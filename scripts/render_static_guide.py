#!/usr/bin/env python3
"""Render one explicit guide from its body/meta, preserving its existing static shell.

The repository contains an exported Next shell without its React source. Its old
hydration payload must not restore placeholder content over the editorial source.
No other route, sitemap or indexing setting is modified.
"""
import argparse
from html import escape, unescape
import json
from pathlib import Path
import re

ROOT = Path(__file__).resolve().parents[1]
parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument('--route', required=True)
args = parser.parse_args()
route = args.route.strip('/')
if not re.fullmatch(r'guides/[a-z0-9-]+', route):
    parser.error('Expected one existing guides/<slug> route')
source = ROOT / 'content' / route
page = ROOT / route / 'index.html'
meta = json.loads((source / 'meta.json').read_text())
body = (source / 'body.html').read_text().strip()
html = page.read_text()
assert re.fullmatch(r'<article\b[^>]*>.*</article>', body, re.S), 'Expected one article'
assert len(re.findall(r'<article\b', html)) == 1, 'Expected one existing article'
html = re.sub(r'<article\b[^>]*>.*?</article>', lambda _: body, html, count=1, flags=re.S)
html = re.sub(r'<script\b[^>]*>.*?</script>', '', html, flags=re.S)
html = re.sub(r'<link\b(?=[^>]*\bas="script")[^>]*>', '', html)
html = re.sub(r'<title>.*?</title>', lambda _: '<title>'+escape(meta['title'])+' | traitement-air.fr</title>', html)
html = re.sub(r'<meta\b[^>]*name="(?:description|robots)"[^>]*>', '', html)
html = re.sub(r'<link\b[^>]*rel="canonical"[^>]*>', '', html)
canonical = 'https://traitement-air.fr/'+route+'/'
schema = {'@context':'https://schema.org','@type':'Article','headline':meta['h1'],'inLanguage':'fr-FR','mainEntityOfPage':canonical,'publisher':{'@type':'Organization','name':'traitement-air.fr'}}
head = '<meta name="description" content="'+escape(meta['description'],quote=True)+'"/><meta name="robots" content="noindex,follow"/><link rel="canonical" href="'+canonical+'"/><script type="application/ld+json">'+json.dumps(schema,ensure_ascii=False)+'</script>'
html = html.replace('</head>',head+'</head>')
html = re.sub(r'<h1>.*?</h1>\s*<p>.*?</p>',lambda _: '<h1>'+escape(meta['h1'])+'</h1><p>'+escape(meta['intro'])+'</p>',html,count=1,flags=re.S)
sections = re.findall(r'<section\b[^>]*id="([^"]+)"[^>]*>.*?<h2>(.*?)</h2>',body,re.S)
links = ''.join('<a href="#'+ident+'">'+escape(unescape(re.sub('<[^>]+>','',title)))+'</a>' for ident,title in sections)
html = re.sub(r'<aside>.*?</aside>',lambda _: '<aside><span>Sur cette page</span>'+links+'</aside>',html,count=1,flags=re.S)
# Retain the existing responsive menu with plain static navigation.
menu = '''<script>const toggle=document.querySelector('.menu-toggle');const nav=document.querySelector('.nav-links');if(toggle&&nav){toggle.addEventListener('click',()=>{const open=toggle.getAttribute('aria-expanded')!=='true';toggle.setAttribute('aria-expanded',String(open));toggle.setAttribute('aria-label',open?'Fermer le menu':'Ouvrir le menu');nav.classList.toggle('is-open',open);});document.addEventListener('keydown',event=>{if(event.key==='Escape'){toggle.setAttribute('aria-expanded','false');toggle.setAttribute('aria-label','Ouvrir le menu');nav.classList.remove('is-open');}});}</script>'''
assert '.nav-links.is-open' in ''.join(p.read_text() for p in (ROOT/'_next/static/css').glob('*.css')), 'Menu class not supported by existing stylesheet'
page.write_text(html.replace('</body>',menu+'</body>'))
print('Rendered /'+route+'/ only; noindex retained')

# Next navigation from an unchanged page reads index.txt rather than index.html.
# Synchronize that existing payload as well, using native HTML elements only.
from html.parser import HTMLParser
class Fragment(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.nodes = []
        self.stack = [self.nodes]
    def handle_starttag(self, tag, attrs):
        props = {('className' if key == 'class' else key): value for key,value in attrs}
        children = []
        props['children'] = children
        self.stack[-1].append(['$',tag,None,props])
        if tag not in {'br','hr','img','input','meta','link'}:
            self.stack.append(children)
    def handle_endtag(self, tag):
        if len(self.stack)>1:
            self.stack.pop()
    def handle_data(self, text):
        self.stack[-1].append(text.replace('$','$$') if text.startswith('$') else text)
fragment = Fragment()
fragment.feed(body)
article = fragment.nodes[0]
aside_fragment = Fragment()
aside_fragment.feed('<aside><span>Sur cette page</span>'+links+'</aside>')

def sync(node):
    if isinstance(node,list):
        if len(node)==4 and node[0]=='$' and isinstance(node[3],dict):
            props=node[3]
            if node[1]=='article':
                return article
            if node[1]=='aside':
                return aside_fragment.nodes[0]
            if node[1]=='section' and props.get('className')=='page-hero':
                hero=Fragment()
                hero.feed(re.search(r'<section class="page-hero">.*?</section>',html,re.S)[0])
                return hero.nodes[0]
        return [sync(child) for child in node]
    if isinstance(node,dict):
        return {key:sync(value) for key,value in node.items()}
    return node

payload = ROOT / route / 'index.txt'
lines=[]
for line in payload.read_text().splitlines():
    prefix, separator, raw=line.partition(':')
    if prefix in {'6','a'}:
        data=json.loads(raw)
        if prefix=='6':
            data=sync(data)
        else:
            data['metadata']=[['$','title','0',{'children':meta['title']+' | traitement-air.fr'}],['$','meta','1',{'name':'description','content':meta['description']}],['$','meta','2',{'name':'robots','content':'noindex,follow'}],['$','link','3',{'rel':'canonical','href':canonical}]]
        line=prefix+':'+json.dumps(data,ensure_ascii=False,separators=(',',':'))
    lines.append(line)
payload.write_text('\n'.join(lines)+'\n')
print('Synchronized existing client-navigation payload for /'+route+'/')
