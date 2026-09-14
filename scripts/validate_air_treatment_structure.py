#!/usr/bin/env python3
from pathlib import Path
import json,re
ROOT=Path(__file__).resolve().parents[1]
CLUSTERS={"solutions-traitement-air":8,"secteurs":11,"problemes":9,"polluants":6,"air-interieur":6,"guides":11,"outils":3}
def fail(m): raise SystemExit("FAIL: "+m)
def main():
 site=json.loads((ROOT/"content/site.json").read_text(encoding="utf-8"))
 if site.get("base_url")!="https://traitement-air.fr" or site.get("language")!="fr-FR": fail("site identity mismatch")
 for name in ("index.html","AGENTS.md","sitemap.xml","robots.txt"):
  if not (ROOT/name).exists(): fail(name+" missing")
 errors=[];total=0
 for cluster,minimum in CLUSTERS.items():
  if not (ROOT/cluster/"index.html").exists(): errors.append("missing hub "+cluster)
  children=list((ROOT/cluster).glob("*/index.html"));total+=len(children)
  if len(children)<minimum: errors.append(f"{cluster}: {len(children)} child routes; expected >= {minimum}")
 for path in {ROOT/"index.html",*ROOT.glob("**/index.html")}:
  html=path.read_text(encoding="utf-8",errors="replace")
  if not re.search(r"<title>.+?</title>",html,re.I|re.S): errors.append("missing title "+str(path.relative_to(ROOT)))
  if len(re.findall(r"<h1\\b",html,re.I))!=1: errors.append("invalid H1 count "+str(path.relative_to(ROOT)))
 if errors: fail("\n".join(errors))
 print(f"PASS: {len(CLUSTERS)} clusters and {total} child routes validated")
if __name__=="__main__": main()
