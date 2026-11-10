#!/usr/bin/env python3
"""Simplify the header on every published static HTML page without altering content or URLs."""
from pathlib import Path
import re

ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={"404","_next",".agents",".content","assets","content","scripts",".artifacts","docs"}
sector_links=[
 ("Industries de transformation",[("Métallurgie","metallurgie"),("Plasturgie","plasturgie"),("Industrie chimique","industrie-chimique"),("Caoutchouc","industrie-caoutchouc")]),
 ("Fabrication et procédés",[("Automobile","industrie-automobile"),("Composites","fabrication-composites"),("Soudage et chaudronnerie","soudage-chaudronnerie")]),
 ("Déchets et matériaux",[("Recyclage","recyclage-industriel"),("Déchets organiques","dechets-organiques"),("Cimenteries et carrières","cimenteries-carrieres")]),
 ("Environnements sensibles",[("Agroalimentaire","agroalimentaire"),("Laboratoires","laboratoires-recherche"),("Salles blanches","salle-blanche")])
]
def group(name, links):
 return '<div class="header-menu-group"><strong>'+name+'</strong>'+''.join('<a href="'+url+'">'+text+'</a>' for text,url in links)+'</div>'
def drop(name,body,kind,all_link):
 return '<details class="nav-explore header-menu '+kind+'"><summary>'+name+'</summary><div class="nav-explore-links header-menu-panel" aria-label="'+name+'">'+body+'<a class="header-menu-all" href="'+all_link[0]+'">'+all_link[1]+' →</a></div></details>'
solutions=drop("Solutions",
 group("Technologies",[
  ("Ventilation industrielle","/solutions-traitement-air/ventilation-industrielle/"),
  ("Filtration","/solutions-traitement-air/filtration-air-industrielle/"),
  ("Dépoussiérage","/solutions-traitement-air/depoussierage-industriel/"),
  ("Purification","/solutions-traitement-air/purification-air-industrielle/")])+
 group("Pour vous orienter",[
  ("Faire un diagnostic","/outils/diagnostic-traitement-air/"),
  ("Choisir une solution","/outils/choisir-solution-traitement-air/")]),
 "header-solutions",("/solutions-traitement-air/","Toutes les solutions"))
sector=drop("Secteurs",''.join(group(name,[(title,"/secteurs/traitement-air-"+slug+"/") for title,slug in members]) for name,members in sector_links),
 "header-sectors",("/secteurs/","Les 26 secteurs"))
problems=drop("Problèmes",
 group("Identifier un problème",[
  ("Poussières industrielles","/problemes/poussieres-industrielles/"),
  ("Odeurs et gaz","/problemes/odeurs-gaz/"),
  ("COV industriels","/problemes/cov-industriels/"),
  ("Humidité industrielle","/problemes/humidite-industrielle/"),
  ("Contamination particulaire","/problemes/contamination-particulaire/")]),
 "header-problems",("/problemes/","Toutes les problématiques"))
resources=drop("Ressources",
 group("Comprendre",[
  ("Guides techniques","/guides/"),
  ("Fiches polluants","/polluants/"),
  ("Air intérieur","/air-interieur/")])+
 group("Outils",[
  ("Tous les outils","/outils/"),
  ("Calculer l'hygrométrie","/outils/calcul-hygrometrie/")]),
 "header-resources",("/guides/","Tous les guides"))
NAV='<nav class="nav-links header-slim" aria-label="Navigation principale">'+solutions+sector+problems+resources+'<a class="button button-small header-quote" href="/demander-un-devis/">Demander un devis</a></nav>'
CSS="""<style id="header-slim-css">
/* Four clear choices and a single action; native details work by mouse, touch and keyboard. */
.site-header .header-slim{gap:clamp(10px,1.6vw,27px);align-items:center}
.site-header .header-slim>.header-menu>summary{font-weight:650;cursor:pointer;list-style:none;white-space:nowrap}
.site-header .header-slim>.header-menu>summary::-webkit-details-marker{display:none}
.site-header .header-slim>.header-menu>summary::after{content:" ▾";font-size:.75em}
.site-header .header-slim>.header-menu[open]>summary{color:#175865}
.site-header .header-slim .header-menu-panel{
 display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:15px 22px;
 position:absolute;top:calc(100% + 12px);right:0;left:auto;
 width:min(530px,calc(100vw - 32px));max-width:calc(100vw - 32px);
 padding:18px;background:#fff;border:1px solid #d8e1e7;
 border-radius:12px;box-shadow:0 16px 36px #10263825;box-sizing:border-box;z-index:150
}
.site-header .header-slim .header-menu-group{display:flex;flex-direction:column;min-width:0}
.site-header .header-slim .header-menu-group strong{display:block;color:#173b42;font-size:.85rem;margin:4px 10px 8px}
.site-header .header-slim .header-menu-panel a{color:#173b42!important;white-space:normal;line-height:1.35}
.site-header .header-slim .header-menu-panel a:hover{background:#edf4f6}
.site-header .header-slim .header-menu-all{grid-column:1/-1;border-top:1px solid #d8e1e7;margin-top:3px;padding-top:14px!important;font-weight:700}
.site-header .header-slim .header-problems .header-menu-panel{grid-template-columns:1fr;width:min(330px,calc(100vw - 32px))}
.site-header .header-slim .header-problems .header-menu-all{grid-column:auto}
.site-header .header-slim .header-sectors .header-menu-panel{width:min(670px,calc(100vw - 32px))}
.site-header .header-slim>.header-quote{white-space:nowrap}
.site-header .header-slim summary:focus-visible,.site-header .header-slim a:focus-visible{
 outline:3px solid #b96325;outline-offset:3px
}
@media(min-width:901px){
 .site-header .header-slim{margin-left:auto}
 .site-header .menu-toggle{display:none!important}
}
@media(max-width:900px){
 .site-header .header-slim{align-items:stretch;gap:0}
 .site-header .header-slim .header-menu{position:static;width:100%;align-self:stretch}
 .site-header .header-slim .header-menu>summary{padding:11px 0;white-space:normal}
 .site-header .header-slim .header-menu-panel{
   position:static;display:grid;grid-template-columns:1fr;width:100%;
   max-width:100%;padding:10px 12px;gap:6px;border:0;
   box-shadow:none;background:transparent
 }
 .site-header .header-slim .header-menu-all{grid-column:auto}
 .site-header .header-slim .header-menu-group strong{margin:9px 10px 3px}
 .site-header .header-slim>.header-quote{margin-top:9px;text-align:center}
}
</style>"""
pages=[]
for p in ROOT.rglob("index.html"):
 rel=p.relative_to(ROOT)
 if any(x.startswith(".") or x in EXCLUDE for x in rel.parts[:-1]): continue
 pages.append(p)
assert len(pages)>=108,len(pages)
for p in pages:
 s=p.read_text(encoding="utf-8")
 match=re.search(r'<nav class="nav-links">[\s\S]*?</nav>',s)
 assert match, f"Navigation missing: {p}"
 s=s[:match.start()]+NAV+s[match.end():]
 assert 'id="header-slim-css"' not in s,p
 s=s.replace("</head>",CSS+"</head>",1)
 p.write_text(s,encoding="utf-8")
print("Updated header on",len(pages),"static pages")
