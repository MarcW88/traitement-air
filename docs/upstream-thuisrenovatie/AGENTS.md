# Thuisrenovatie Gids — agentregels

## Taal en positionering

- Schrijf standaard in helder Nederlands (`nl`).
- De site helpt woningeigenaars betere renovatiebeslissingen nemen en pas daarna vakmensen, offertes, producten of oplossingen vergelijken.
- De toon is praktisch, onafhankelijk, rustig en deskundig. Geen verkooppraat, kunstmatige urgentie of overdreven claims.
- Behoud de bestaande visuele richting en routes. Genereer geen nieuwe pagina's buiten de afgesproken informatiearchitectuur zonder expliciete opdracht.

## Clusters en eigenaarschap

| Cluster | Map | Primaire rol |
|---|---|---|
| PLAN | `renovatie-plannen/` | scope, volgorde, budget, fasering, vergunningen, voorbereiding, rendement |
| PROJECT | `renovatieprojecten/` | concrete renovatieprojecten en projectkeuzes |
| SUSTAINABILITY | `verduurzamen/` | energie, isolatie, installaties, comfort en besparing |
| TROUBLESHOOTING | `problemen-oplossen/` | symptomen, veilige diagnose, oorzaken en oplossingen |
| DIY | `doe-het-zelf/` | alleen werkelijk uitvoerbare en veilige DIY-taken |
| LEAD | `vakman-en-offertes/` | vakman kiezen, scope bepalen, offerte controleren en vergelijken |

Deze types bepalen **de grens en risico's van een pagina, nooit de artikelstructuur**. Er bestaat geen vast PLAN-, PROJECT-, DIY- of LEAD-template.

## Verplichte workflow

Voor een bestaande pagina:

1. `renovation-analysis-workflow / AUDIT`
2. beslissing: `KEEP`, `LIGHT_UPDATE`, `DEEP_REWRITE`, `MERGE` of `NOINDEX`
3. alleen bij `LIGHT_UPDATE` of `DEEP_REWRITE`: `renovation-content-workflow`
4. `renovation-analysis-workflow / PUBLISH_REVIEW`
5. menselijke validatie vóór indexatie of structurele actie

Voor een volledige clusteranalyse gebruik je `renovation-analysis-workflow / CLUSTER_AUDIT`. Dit mode analyseert overlap, cannibalisatie, gaten en structurele cloning zonder automatisch te herschrijven.

Voor een nieuwe URL gebruikt `renovation-content-workflow` eerst intentie, onderzoek, bewijs en brief vóór de redactie, gevolgd door `PUBLISH_REVIEW`.

## Skills eerst, custom orchestration daarna

De twee custom workflows zijn alleen orkestratie. Generieke taken moeten door bestaande skills worden uitgevoerd, met name:

- `seo-content-audit`, `seo-keyword`, `search-intent`, `content-refresh`;
- `fact-check`, `evidence-based-reviews`, `affiliate-value`;
- `content-brief-authoring`, `content-and-copy`;
- `internal-linking-audit`, `humanizer`, `general-writing`, `anti-ai-slop`;
- `seo-onpage`, `seo-technical`, `seo-best-practices`, `seo-drift` waar relevant;
- `editorial-qa`;
- `information-architecture`, `jtbd-framing` en `cro-optimization` wanneer de taak dat nodig maakt.

Maak geen nieuwe custom SEO-, research-, copy-, CRO- of QA-skill zolang een bestaande skill het probleem afdekt.

## Geen template-editorialiteit

- Bouw de structuur pas na intentie, clusterrol, bronnen en bewijs.
- Geen verplicht aantal H2/H3, woorden, tabellen, FAQ's, stappen, links of bronnen.
- Een type (`PLAN`, `PROJECT`, `CHOICE`, `EXPLAINER`, `HOW_TO`, enz.) is een risicogrid, geen schrijfmal.
- Vergelijk tijdens audit/review met nabije pagina's en flag dezelfde H2-functies, dezelfde tabellen, dezelfde CTA's, dezelfde conclusies of hetzelfde ritme wanneer dat inhoudelijk niet gerechtvaardigd is.
- Herbruikbare visuele componenten zijn normaal; herbruikbare denkstructuren zijn dat niet automatisch.

## Betrouwbaarheid bij renovatiecontent

- Verzin nooit prijzen, premies, subsidies, normen, rendementen, terugverdientijden, vergunningseisen, certificaten of garanties.
- Tijd- of plaatsgebonden informatie moet een land/regio en controledatum hebben.
- Gebruik bandbreedtes alleen wanneer aannames, context en bronbasis duidelijk zijn.
- Onderscheid feit, aanname, voorbeeld, ervaringssignaal en advies.
- Een plausibele claim zonder passende bron blijft onverifieerd.
- Geef nooit de indruk dat Thuisrenovatie Gids een woning, schade, vakman of installatie zelf heeft geïnspecteerd wanneer dat niet zo is.

## Veiligheid

Bij elektriciteit, gas, draagconstructies, funderingen, asbest, dakwerk op hoogte en andere risicovolle of gereglementeerde werkzaamheden:

- maak stopcondities expliciet;
- normaliseer hoog-risicowerk niet als gewone DIY;
- verwijs naar een gekwalificeerde vakman wanneer dat nodig is;
- formuleer geen zekere diagnose zonder inspectie.

Een humanizer- of style-pass mag waarschuwingen, voorwaarden of veiligheidsgrenzen nooit verwijderen of afzwakken.

## Lead- en offertepagina's

`vakman-en-offertes/` is conversion-first maar trust-first:

- leg uit wat in een goede offerte moet staan;
- maak scope, uitsluitingen, timing, betaalmomenten en garanties vergelijkbaar;
- geef concrete vragen voor de vakman;
- benoem red flags zonder angstmarketing;
- CTA's moeten passen bij de beslisfase;
- geen kunstmatige schaarste, gegarandeerde besparing of commissiegestuurde ranking.

De pagina moet nuttig blijven wanneer alle lead- of affiliatelinks worden verwijderd.

## Bron van waarheid en generatie

- Bewerk inhoud in `content/<route>/body.html`.
- Bewaar briefs in `content/briefs/<route>.md`.
- Bewaar reviews waar nodig in `content/reviews/<route>.md`.
- Gebruik `generate_pages.py` om de gegenereerde HTML opnieuw op te bouwen.
- Bewerk niet alleen gegenereerde `index.html`-bestanden.

Content wordt route per route geactiveerd. Routes zonder gecontroleerd `body.html` behouden hun skeleton.

## PUBLISH_REVIEW en machine gate

Voer voor afgewerkte actieve content uit:

```bash
python3 scripts/validate_content_quality.py
```

Deze validator controleert alleen machine-detecteerbare blockers. Hij beoordeelt geen diepgang via woord-, heading-, link- of bronquota.

`PUBLISH_REVIEW` retourneert exact één van beide statussen:

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Een PASS activeert nooit automatisch indexatie.

## Indexatie

De globale status staat in `content/site.json` en wordt door `generate_pages.py` gebruikt. `indexing_enabled` mag alleen worden gewijzigd na expliciete menselijke instructie, nadat de relevante content een PUBLISH_REVIEW PASS heeft gekregen.
