#!/usr/bin/env python3
"""Refresh static navigation, sector directory and relevant internal links.

Idempotent: every inserted block is explicitly marked and replaced on reruns.
Run only on an editorial branch. No deployment.
"""
from pathlib import Path
from html import escape
import re

ROOT = Path(__file__).resolve().parents[1]
EXCLUDE = {"_next", ".agents", ".content", "assets", "content", "scripts", ".artifacts"}
GROUPS = [
    ("transformation", "Industries de transformation", [
        ("metallurgie", "Métallurgie et fonderie"),
        ("plasturgie", "Plasturgie"),
        ("industrie-chimique", "Industrie chimique"),
        ("industrie-textile", "Industrie textile"),
        ("industrie-caoutchouc", "Industrie du caoutchouc"),
        ("industrie-bois", "Industrie du bois"),
        ("industrie-papier", "Industrie du papier"),
        ("imprimerie", "Imprimerie"),
    ]),
    ("fabrication", "Fabrication et procédés", [
        ("industrie-automobile", "Industrie automobile"),
        ("fabrication-composites", "Fabrication de composites"),
        ("fabrication-batteries", "Fabrication de batteries"),
        ("soudage-chaudronnerie", "Soudage et chaudronnerie"),
        ("traitement-surface", "Traitement de surface"),
        ("cabine-peinture", "Cabines de peinture"),
        ("electronique", "Électronique"),
    ]),
    ("environnement", "Déchets et matériaux", [
        ("recyclage-industriel", "Recyclage industriel"),
        ("dechets-organiques", "Traitement des déchets organiques"),
        ("cimenteries-carrieres", "Cimenteries et carrières"),
    ]),
    ("sensibles", "Bâtiments et environnements sensibles", [
        ("agroalimentaire", "Agroalimentaire"),
        ("pharmaceutique", "Pharmaceutique"),
        ("laboratoires-recherche", "Laboratoires de recherche"),
        ("salle-blanche", "Salles blanches"),
        ("hopital", "Hôpitaux"),
        ("data-center", "Data centers"),
        ("stockage", "Stockage industriel"),
        ("entrepots-logistiques", "Entrepôts logistiques"),
    ]),
]
GROUP_MAP = {slug:(gid,heading) for gid,heading,items in GROUPS for slug,_ in items}
ALL = [(slug,label) for _,_,items in GROUPS for slug,label in items]
assert len(ALL)==26 and len({slug for slug,_ in ALL})==26
url = lambda slug: "/secteurs/traitement-air-"+slug+"/"

# Important links chosen for reader relevance; not an arbitrary 26-link footer.
TOPICS = {
    "transformation":[("/problemes/poussieres-industrielles/","Poussières industrielles"),
                      ("/solutions-traitement-air/depoussierage-industriel/","Dépoussiérage industriel")],
    "fabrication":[("/polluants/cov/","Composés organiques volatils"),
                  ("/solutions-traitement-air/ventilation-industrielle/","Ventilation industrielle")],
    "environnement":[("/problemes/odeurs-gaz/","Odeurs et gaz"),
                     ("/polluants/poussieres/","Poussières")],
    "sensibles":[("/problemes/contamination-particulaire/","Contamination particulaire"),
                ("/solutions-traitement-air/ventilation-industrielle/","Ventilation industrielle")],
}
NAV_EXACT = '<a href="/secteurs/">Secteurs</a>'
menu = [
  '<details class="nav-explore sector-nav"><summary>Secteurs</summary>',
  '<div class="nav-explore-links sector-nav-links" role="group" aria-label="Explorer les secteurs">',
  '<div class="sector-nav-all"><a href="/secteurs/">Voir les 26 secteurs</a></div>',
]
nav_picks = {
 "transformation":["metallurgie","plasturgie","industrie-chimique","industrie-caoutchouc"],
 "fabrication":["industrie-automobile","fabrication-composites","fabrication-batteries","soudage-chaudronnerie"],
 "environnement":["recyclage-industriel","dechets-organiques","cimenteries-carrieres"],
 "sensibles":["agroalimentaire","laboratoires-recherche","salle-blanche","entrepots-logistiques"],
}
for gid,heading,items in GROUPS:
    labels=dict(items)
    menu.append('<div class="sector-nav-group"><strong>'+escape(heading)+'</strong>')
    for slug in nav_picks[gid]:
        menu.append('<a href="'+url(slug)+'">'+escape(labels[slug])+'</a>')
    menu.append('</div>')
menu.append('</div></details>')
MENU="".join(menu)
CSS="""<style id="sector-architecture-css">
/* Grouped, keyboard-operable sector navigation; preserves the site's existing details menu. */
.sector-nav{position:relative}
.sector-nav .sector-nav-links{
  display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:12px 22px;
  width:min(700px,calc(100vw - 40px));max-width:calc(100vw - 40px);
  padding:18px;right:-150px;left:auto;box-sizing:border-box;z-index:120
}
.sector-nav-all{grid-column:1/-1;border-bottom:1px solid #d8e1e7;padding-bottom:6px}
.sector-nav-all a{font-weight:700}
.sector-nav-group{min-width:0}
.sector-nav-group strong{display:block;font-size:.86rem;color:#173b42;margin:5px 8px}
.sector-nav-group a{white-space:normal;line-height:1.4}
.sector-nav summary:focus-visible,.sector-nav a:focus-visible,
.sector-jump a:focus-visible,.sector-group a:focus-visible,.sector-crosslinks a:focus-visible{
  outline:3px solid #b96325;outline-offset:3px
}
.sector-jump{display:flex;flex-wrap:wrap;gap:9px;margin:0 0 24px}
.sector-jump a{display:inline-block;padding:9px 13px;border:1px solid #c9d8da;
 border-radius:999px;background:#f4f8f7;color:#173b42;font-weight:600;text-decoration:none}
.sector-group{margin:0 0 44px;scroll-margin-top:90px}
.sector-group>h2{font-size:clamp(1.35rem,2vw,1.8rem);margin:0 0 8px;color:#173b42}
.sector-group>p{margin:0 0 18px;color:#52615d;max-width:72ch}
.sector-group .directory-grid h3{font-size:1.13rem;line-height:1.35;margin:.3rem 0;color:#173b42}
.sector-crosslinks{max-width:1120px;margin:26px auto;padding:24px;border:1px solid #d8e1e7;
 border-radius:15px;background:#f7faf9}
.sector-crosslinks h2{font-size:1.35rem;margin:0 0 10px;color:#173b42}
.sector-crosslinks p{margin:0 0 12px;color:#52615d}
.sector-crosslinks ul{display:flex;flex-wrap:wrap;gap:10px 22px;margin:0;padding:0;list-style:none}
.sector-crosslinks li{margin:0}
.sector-crosslinks a{font-weight:600;color:#175865;text-decoration:underline;text-underline-offset:3px}
@media(max-width:900px){
 .sector-nav .sector-nav-links{position:static;width:100%;max-width:100%;
 grid-template-columns:1fr;padding:12px;box-shadow:none;overflow:visible;gap:9px}
 .sector-nav-all{grid-column:auto}
 .sector-crosslinks{margin:18px auto;padding:18px}
 .sector-jump{gap:7px}
}
</style>"""
def validated_link(path):
    assert (ROOT/path.lstrip("/")/"index.html").is_file(), "Broken internal URL: "+path
def link(path,title):
    validated_link(path)
    return '<li><a href="'+path+'">'+escape(title)+'</a></li>'
def insert_after_main(html,block):
    assert "</main>" in html
    return html.replace("</main>",block+"</main>",1)
def related_block(heading,intro,items):
    items=list(dict((u,t) for u,t in items).items())
    return '<section class="sector-crosslinks" aria-label="'+escape(heading,quote=True)+'"><h2>'+escape(heading)+'</h2><p>'+escape(intro)+'</p><ul>'+''.join(link(u,t) for u,t in items)+'</ul></section>'
def update_nav(html):
    if '<nav class="nav-links">' not in html:
        return html
    assert NAV_EXACT in html, "Missing sector nav link"
    html=html.replace(NAV_EXACT,MENU,1)
    if 'id="sector-architecture-css"' not in html:
        html=html.replace("</head>",CSS+"</head>",1)
    return html

# Shared navigation on every published static HTML page, not just the top-level hubs.
pages=[]
for path in ROOT.rglob("index.html"):
    rel=path.relative_to(ROOT)
    if any(p.startswith(".") or p in EXCLUDE for p in rel.parts[:-1]):continue
    pages.append(path)
changed=0
for path in pages:
    html=path.read_text(encoding="utf-8")
    out=update_nav(html)
    if out!=html:
        path.write_text(out,encoding="utf-8")
        changed+=1

# Reorganize existing 26 cards: preserve original images, descriptions, and URLs.
p=ROOT/"secteurs/index.html"
h=p.read_text(encoding="utf-8")
start=h.index('<div class="directory-grid">')
end=h.index('</div></section>',start)
old=h[start:end+6]
cards=re.findall(r'(<a href="/secteurs/traitement-air-([^/]+)/">[\s\S]*?</a>)',old)
assert len(cards)==26, "Expected exactly 26 original sector cards"
by_slug={slug:card for card,slug in cards}
assert set(by_slug)==set(dict(ALL)), "Sector list changed unexpectedly"
intro={
 "transformation":"Procédés thermiques, mélange, transformation de matières et émissions propres aux ateliers.",
 "fabrication":"Assemblage, revêtements, opérations de finition et captage au poste.",
 "environnement":"Gestion des matières, traitement de déchets et poussières ou odeurs associées.",
 "sensibles":"Qualité de l'air, conditions d'ambiance et protection des environnements sensibles."
}
jump='<nav class="sector-jump" aria-label="Familles de secteurs">'+''.join(
 '<a href="#'+gid+'">'+escape(heading)+'</a>' for gid,heading,_ in GROUPS)+'</nav>'
parts=['<div class="sector-catalogue">',jump]
for gid,heading,items in GROUPS:
    parts.append('<section class="sector-group" id="'+gid+'" aria-labelledby="heading-'+gid+'">')
    parts.append('<h2 id="heading-'+gid+'">'+escape(heading)+'</h2><p>'+escape(intro[gid])+'</p>')
    parts.append('<div class="directory-grid">')
    for slug,_ in items:
        card=by_slug[slug].replace("<h2>","<h3>").replace("</h2>","</h3>")
        parts.append(card)
    parts.append('</div></section>')
parts.append('</div>')
h=h[:start]+"".join(parts)+h[end+6:]
assert h.count('class="sector-group"')==4
p.write_text(h,encoding="utf-8")

# Additional internal links on category hubs, from topical intent to matching sectors.
hub_links={
 "solutions-traitement-air/index.html":(
  "Secteurs concernés par ces technologies",
  "Le choix d'un procédé dépend des activités et des émissions réellement présentes.",
  [("industrie-automobile","Industrie automobile"),("metallurgie","Métallurgie et fonderie"),("recyclage-industriel","Recyclage industriel"),("dechets-organiques","Déchets organiques")]),
 "problemes/index.html":(
  "Exemples de secteurs confrontés à ces problèmes",
  "Une même problématique prend des formes différentes selon les matières et les procédés.",
  [("cimenteries-carrieres","Cimenteries et carrières"),("fabrication-composites","Fabrication de composites"),("industrie-caoutchouc","Industrie du caoutchouc"),("dechets-organiques","Déchets organiques")]),
 "polluants/index.html":(
  "Dans quels secteurs retrouve-t-on ces émissions ?",
  "Associez le polluant aux sources de votre activité avant de choisir une protection.",
  [("soudage-chaudronnerie","Soudage et chaudronnerie"),("industrie-chimique","Industrie chimique"),("laboratoires-recherche","Laboratoires de recherche"),("recyclage-industriel","Recyclage industriel")]),
}
for rel,(heading,intro,items) in hub_links.items():
    p=ROOT/rel;html=p.read_text(encoding="utf-8")
    block=related_block(heading,intro,[(url(slug),title) for slug,title in items])
    assert heading not in html
    p.write_text(insert_after_main(html,block),encoding="utf-8")

# Home: supplement the historic six-sector preview with a cross-sector entry panel.
p=ROOT/"index.html";html=p.read_text(encoding="utf-8")
heading="Explorer les secteurs industriels"
block=related_block(heading,"Accédez aux activités de fabrication, de transformation et de traitement des matières.",[
    (url("industrie-automobile"),"Industrie automobile"),
    (url("fabrication-composites"),"Fabrication de composites"),
    (url("metallurgie"),"Métallurgie"),
    (url("cimenteries-carrieres"),"Cimenteries et carrières"),
    (url("dechets-organiques"),"Traitement des déchets organiques"),
    ("/secteurs/","Les 26 secteurs"),
])
assert heading not in html
p.write_text(insert_after_main(html,block),encoding="utf-8")

# Each of the 26 industry pages receives concise contextual related links.
for gid,heading,items in GROUPS:
    for slug,label in items:
        p=ROOT/("secteurs/traitement-air-"+slug+"/index.html")
        html=p.read_text(encoding="utf-8")
        peers=[(s,n) for s,n in items if s!=slug]
        peers=peers[:3]
        c=related_block("À explorer également",
          "Autres environnements à comparer et problématiques techniques associées.",
          [(url(s),title) for s,title in peers]+TOPICS[gid]+[("/secteurs/","Tous les secteurs")])
        html=insert_after_main(html,c)
        p.write_text(html,encoding="utf-8")

# Hard assertions for output consistency and non-invention.
assert len(pages)>=100, "Unusually few site pages"
hub=(ROOT/"secteurs/index.html").read_text(encoding="utf-8")
assert hub.count('class="sector-group"')==4
assert len(re.findall(r'<a href="/secteurs/traitement-air-[^/]+/">',hub))>=26
for slug,_ in ALL:
    p=ROOT/("secteurs/traitement-air-"+slug+"/index.html")
    text=p.read_text(encoding="utf-8")
    assert 'class="sector-crosslinks"' in text and 'sector-nav-links' in text,slug
print(f"Modified {changed} shared nav pages, 26 sector pages and four category/home panels")
