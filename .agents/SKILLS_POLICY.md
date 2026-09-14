# Skill policy — 80/20

Thuisrenovatie Gids gebruikt dezelfde orkestratiegedachte als `bloc-notes-numerique`: generieke expertise komt uit bestaande GitHub-skills; custom code blijft beperkt tot domeinspecifieke routing, veiligheid, clustergrenzen en publicatiegates.

## Huidige verdeling

- Upstream/reused skills: **44**
- Custom skills: **4**
- Totaal: **48**
- Upstream/reused: **95,7%**
- Custom: **8,3%**

De CI faalt zodra custom skills meer dan 20% van het totaal vormen.

## Verbatim upstream — RampStack

De volgende **14** directories worden volledig en ongewijzigd gevendord uit `rampstackco/claude-skills`, inclusief hun `references/` en andere bestanden wanneer aanwezig:

- `seo-keyword`
- `seo-content-audit`
- `seo-onpage`
- `seo-technical`
- `content-brief-authoring`
- `content-and-copy`
- `editorial-qa`
- `evidence-based-reviews`
- `information-architecture`
- `jtbd-framing`
- `cro-optimization`
- `seo-competitor`
- `seo-aeo-geo`
- `brand-voice`

De exacte broncommit en Git blob hashes staan in `.agents/UPSTREAM_SOURCES.json`. `scripts/validate_upstream_skills.py` controleert dat deze directories lokaal **byte-for-byte overeenkomen** met de gepinde GitHub-bron. Domeinaanpassingen zijn in deze directories verboden.

## Reused repository skills — bloc-notes-numerique

De volgende **30** skills komen uit het bestaande repository/editorial engine van `bloc-notes-numerique`. Bestaande Thuisrenovatie-versies blijven behouden; ontbrekende skills worden toegevoegd vanuit de gepinde broncommit. Domeinspecifieke aanpassingen zijn toegestaan wanneer de verantwoordelijkheid van het skill gelijk blijft.

- `search-intent`
- `content-refresh`
- `fact-check`
- `affiliate-value`
- `internal-linking-audit`
- `humanizer`
- `general-writing`
- `anti-ai-slop`
- `seo-drift`
- `seo-best-practices`
- `academic-voice`
- `better-usage`
- `brand-analysis-workflow`
- `brand-content-workflow`
- `comparison-analysis-workflow`
- `comparison-content-workflow`
- `content-audit`
- `deal-analysis-workflow`
- `deal-content-workflow`
- `editorial-image-planner`
- `guide-analysis-workflow`
- `guide-content-workflow`
- `jobs-to-be-done`
- `natural-writing`
- `non-autoregressive-writing-pass`
- `site-design-review`
- `trust-content-workflow`
- `usage-analysis-workflow`
- `usage-content-workflow`
- `writing-cadence`

## Custom catalogus

| Skill | Waarom custom? |
|---|---|
| `renovation-analysis-workflow` | sitebrede audit/cluster/publish orchestration, renovatiegrenzen, SERP/content-gap gates, safety en structurele similariteit |
| `renovation-content-workflow` | upstream bronworkflow, volledig behouden |
| `air-treatment-analysis-workflow` | sitespecifieke audit/cluster/publish orchestration voor traitement-air.fr |
| `air-treatment-content-workflow` | productie, research-handoff, veiligheid en post-write validation voor traitement-air.fr |

## Verplichte architectuur

De custom workflows mogen geen tweede versie bevatten van methodes die al in de reused/upstream skills bestaan. Ze mogen alleen:

1. de juiste skills in de juiste volgorde routeren;
2. beslissingen mappen naar `KEEP / LIGHT_UPDATE / DEEP_REWRITE / MERGE / NOINDEX`;
3. grenzen tussen renovatieclusters bewaken;
4. renovatiespecifieke veiligheids- en actualiteitsrisico's bewaken;
5. clusterbrede structurele cloning detecteren;
6. research-artefacten en post-write coverage gates verplichten;
7. `PUBLISH_REVIEW` en handoff naar menselijke validatie organiseren.

## Deep rewrite-regel

Een `DEEP_REWRITE` mag niet rechtstreeks van audit naar tekst gaan. Vereist zijn:

`SERP coverage matrix → evidence/brief → draft → post-write gap check → PUBLISH_REVIEW`.

Als actuele SERP- of brondata nodig is maar niet beschikbaar is, wordt het datagat expliciet vastgelegd. Het mag niet worden ingevuld met modelgeheugen of aannames.

## Anti-template regel

`PLAN`, `PROJECT`, `SUSTAINABILITY`, `TROUBLESHOOTING`, `DIY`, `LEAD`, `CHOICE`, `EXPLAINER` en `HOW_TO` zijn classificaties of risicogrids. Ze mogen nooit een verplicht redactioneel template worden.

Geen nieuwe custom skill toevoegen tenzij de taak werkelijk sitespecifieke orkestratie vereist én de 80/20-regel na toevoeging nog steeds slaagt.
