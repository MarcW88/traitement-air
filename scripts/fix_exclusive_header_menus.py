#!/usr/bin/env python3
"""Apply exclusive-opening behavior to the four header <details> menus on static pages."""
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
EXCLUDE={"404","_next",".agents",".content","assets","content","scripts",".artifacts","docs"}
HOOK="""<script id="header-exclusive-menu">
(()=>{
const nav=document.querySelector('.nav-links.header-slim');
if(!nav)return;
const menus=Array.from(nav.querySelectorAll(':scope > details.header-menu'));
if(menus.length!==4)return;
const closeOthers=(current)=>{
 for(const menu of menus)if(menu!==current)menu.open=false;
};
for(const menu of menus){
 // The native toggle event also covers Enter/Space, click, touch and programmatic opens.
 menu.addEventListener('toggle',()=>{if(menu.open)closeOthers(menu);});
 menu.querySelector('summary').addEventListener('click',()=>closeOthers(menu));
}
document.addEventListener('click',(event)=>{
 if(!(event.target instanceof Element))return;
 if(!event.target.closest('.nav-links.header-slim > details.header-menu'))closeOthers(null);
});
document.addEventListener('keydown',(event)=>{
 if(event.key!=='Escape')return;
 const active=menus.find(menu=>menu.open);
 if(!active)return;
 closeOthers(null);
 active.querySelector('summary')?.focus();
});
const mobileToggle=document.querySelector('.menu-toggle');
mobileToggle?.addEventListener('click',()=>closeOthers(null));
})();
</script>"""
modified=0
for path in ROOT.rglob("index.html"):
 rel=path.relative_to(ROOT)
 if any(part.startswith(".") or part in EXCLUDE for part in rel.parts[:-1]):continue
 html=path.read_text(encoding="utf-8")
 if "nav-links header-slim" not in html:continue
 assert "header-exclusive-menu" not in html,path
 assert "</body>" in html,path
 html=html.replace("</body>",HOOK+"</body>",1)
 path.write_text(html,encoding="utf-8")
 modified+=1
assert modified>=109,modified
print(f"Exclusive header menu behavior installed on {modified} pages")
