#!/usr/bin/env python3
"""Plan one distinct BFL editorial image for each published informational article.

Runs in the existing image-generation workflow before generation. Does not overwrite
completed image requests or rewrite editorial paragraphs.
"""
from pathlib import Path
import json
import re
import html as html_module
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
REQUESTS = ROOT / ".content/image-requests"
CATEGORIES = ("guides", "secteurs", "solutions-traitement-air", "problemes", "polluants", "air-interieur")

SCENES = {
 "guides": "believable industrial air handling equipment in an accessible mechanical plant room, documentary architectural context",
 "secteurs": "realistic specialized industrial workplace, production room and ceiling air treatment distribution in the background, documentary architectural context",
 "solutions-traitement-air": "generic industrial HVAC equipment installation in a plausible working mechanical plant room, contextual rather than schematic view",
 "problemes": "ordinary industrial workspace showing environmental conditions and ventilation infrastructure, avoiding a fabricated diagnosis",
 "polluants": "realistic industrial ventilation and air extraction context illustrating environmental monitoring, no visible pollutant simulation",
 "air-interieur": "realistic lived-in interior space with unobtrusive ventilation details and natural window light",
}
KEYWORDS = {
 "pharmaceutique": "generic pharmaceutical production room with stainless equipment and clean surfaces",
 "salle-blanche": "controlled-environment industrial cleanroom with credible air supply ceiling and workstations",
 "agroalimentaire": "food processing facility with stainless preparation lines and ventilation",
 "data-center": "data center server aisles with raised floor and overhead cooling infrastructure",
 "electronique": "electronics production workbenches and local ventilation in a realistic workshop",
 "hopital": "hospital clinical corridor and ventilation diffusers, no patients",
 "imprimerie": "industrial printing press workshop with extraction ducts",
 "bois": "woodworking production hall with dust extraction pipework",
 "papier": "paper manufacturing plant with industrial rolls and air management equipment",
 "stockage": "warehouse storage racks and ceiling ventilation infrastructure",
 "filtration": "industrial dust collection and filter housing connected to metal ductwork",
 "humidification": "industrial HVAC plant room with service-accessible humidification equipment",
 "deshumidification": "industrial drying room with compact air-handling system",
 "refroidissement": "industrial climate conditioning plant room with air handling units",
 "ventilation": "industrial extraction ducts and local capture hood above workbench",
 "centrale": "realistic air handling unit and ductwork inside industrial technical room",
 "particules": "industrial air sampling equipment on workshop bench with extraction duct in background",
 "poussieres": "workshop dust extraction hood and ductwork in realistic scale",
 "cov": "industrial paint or solvent-handling room ventilation, no active chemical handling",
 "odeurs": "industrial building air extraction outlets and ventilation equipment",
 "moisissures": "subtle moisture discoloration on an ordinary interior wall, no diagnostic claim",
 "hygrometrie": "small unbranded humidity meter in a realistic industrial room, unreadable display",
 "charbon-actif": "generic industrial activated-carbon filter housing with air duct connections",
 "hepa": "generic ventilation filtration assembly in mechanical plant room without visible performance claims",
 "condensation": "subtle condensation on a cold metal surface in a workshop, without asserting a cause",
 "ammoniaque": "industrial ventilation context around generic refrigerated storage equipment, without visible chemical",
 "ozone": "unbranded industrial air monitoring unit in a clean production space",
 "sulfure": "industrial extraction infrastructure in utility plant room",
 "corrosion": "aged industrial metal infrastructure with natural surface wear, not a causal diagnosis",
 "cabine-peinture": "automotive spray booth interior with safe idle ventilation equipment, no operators",
}
def plain(value):
 return html_module.unescape(re.sub(r"<[^>]*>", "", value)).strip()
def get_first_h1(page):
 m = re.search(r"<h1[^>]*>(.*?)</h1>",page,re.I|re.S)
 return plain(m.group(1)) if m else "Traitement de l'air"
def topic_for(route):
 for key,scene in sorted(KEYWORDS.items(),key=lambda p:-len(p[0])):
  if key in route:return scene
 return SCENES[route.split("/")[0]]
def slugid(route):
 return route.replace("/","-")+"-editorial"
def insert_marker(content,marker):
 if marker in content:return content
 article = re.search(r"<article\b[^>]*>[\s\S]*?<section\b[^>]*>[\s\S]*?</p>",content)
 if article:return content[:article.end()]+marker+content[article.end():]
 # No article: add after the introduction inside main, never outside it.
 intro=re.search(r"<main\b[^>]*>[\s\S]*?</p>",content)
 if intro:return content[:intro.end()]+marker+content[intro.end():]
 raise RuntimeError("Cannot find safe article insertion point")

def main():
 REQUESTS.mkdir(parents=True,exist_ok=True)
 existing={}
 for f in REQUESTS.glob("*.json"):
  if f.name=="_template.json":continue
  q=json.loads(f.read_text())
  existing[q.get("page")]=q
 counts={"new":0,"existing":0}
 for group in CATEGORIES:
  for index in sorted((ROOT/group).glob("*/index.html")):
   route=index.parent.relative_to(ROOT).as_posix()
   rel=index.relative_to(ROOT).as_posix()
   page=index.read_text(encoding="utf-8")
   if rel in existing:
    counts["existing"]+=1
    continue
   topic=get_first_h1(page)
   name=slugid(route)
   marker=f"<!-- EDITORIAL_IMAGE:{name} -->"
   scene=topic_for(route)
   prompt=(f"Photorealistic editorial landscape photograph for an independent French informational article titled '{topic}'. "
    f"Subject: {scene}. The visual must be relevant to this precise topic, not generic stock imagery. "
    "Believable European building geometry, mechanically plausible industrial details, subdued natural or industrial lighting, "
    "candid architectural documentary photography, horizontal 1024 by 672 framing, natural textures, no surreal lighting, "
    "no logos or brands, no text or readable labels, no diagrams, no charts, no made-up equipment certifications, no watermark.")
   req={"id":name,"page":rel,"slot":"editorial","required":True,
     "reason":f"Illustration contextuelle distinctive pour {topic}, choisie par l'agent éditorial.",
     "allow_ai_generation":True,"truth_risk":"LOW","status":"PENDING",
     "marker":marker,"placement":"replace","output_path":f"assets/generated/{name}.webp",
     "prompt":prompt,"alt":f"Vue éditoriale illustrant : {topic}",
     "caption":"","width":1024,"height":672,"prompt_upsampling":True,"seed":None,"generated_at":None}
   source=ROOT/"content"/route/"body.html"
   if source.exists():
    body=source.read_text(encoding="utf-8")
    source.write_text(insert_marker(body,marker),encoding="utf-8")
   index.write_text(insert_marker(page,marker),encoding="utf-8")
   (REQUESTS/(name+".json")).write_text(json.dumps(req,ensure_ascii=False,indent=2)+"\n",encoding="utf-8")
   counts["new"]+=1
 print(json.dumps(counts))
if __name__=="__main__":main()
