# Publish gate — traitement-air.fr

Gebruik deze checklist alleen wanneer een pagina als inhoudelijk afgewerkt wordt beschouwd. Ze vervangt `air-treatment-analysis-workflow / PUBLISH_REVIEW` niet, maar helpt de review traceerbaar te maken.

## Machine gate

- [ ] `python3 scripts/validate_content_quality.py` = PASS
- [ ] geldige title, meta description, H1, canonical en robots
- [ ] geen placeholders
- [ ] geen gebroken interne links of anchors in de actieve content
- [ ] bronbestand bestaat in `content/<route>/body.html`

## Intentie en clusterrol

- [ ] primaire taak/intentie is duidelijk
- [ ] routefamilie is de juiste eigenaar van die intentie
- [ ] overlap met nabije pagina's is onderzocht
- [ ] geen onopgeloste cannibalisatie
- [ ] architectuur is eigen aan de pagina en niet gekopieerd uit een cluster-template

## Bewijs en actualiteit

- [ ] belangrijke claims zijn via `fact-check` beoordeeld
- [ ] prijzen/kosten zijn actueel, gedateerd en contextueel indien genoemd
- [ ] subsidies, vergunningen, regelgeving en normen steunen op actuele passende bronnen
- [ ] territorium is duidelijk waar regels of steunmaatregelen lokaal verschillen
- [ ] prestatie-, rendement- en besparingsclaims bevatten de nodige voorwaarden/aannames
- [ ] onzekerheden zijn zichtbaar in plaats van opgevuld

## Veiligheid

- [ ] risicovol werk is niet als gewone DIY genormaliseerd
- [ ] stopcondities zijn aanwezig waar nodig
- [ ] er wordt geen diagnose of inspectie gesimuleerd
- [ ] latere stijlpasses hebben waarschuwingen of beperkingen niet afgezwakt

## Affiliate- en leadintegriteit

- [ ] pagina blijft nuttig zonder affiliate links of formulier
- [ ] nadelen, uitsluitingen en alternatieven zijn niet verborgen
- [ ] CTA past bij de beslisfase
- [ ] geen kunstmatige urgentie, gegarandeerde besparing of commissiegestuurde ranking
- [ ] geen merchant rewrite of fictieve hands-on ervaring

## Redactionele afwerking

- [ ] `internal-linking-audit` uitgevoerd waar relevant
- [ ] `humanizer` uitgevoerd op zichtbare content
- [ ] `general-writing` uitgevoerd met minimale noodzakelijke wijzigingen
- [ ] `anti-ai-slop` review zonder onopgelost HIGH-signaal
- [ ] `seo-onpage` uitgevoerd
- [ ] `seo-technical` uitgevoerd waar relevant
- [ ] `seo-best-practices` alleen toegepast waar passend
- [ ] `editorial-qa` uitgevoerd
- [ ] volledige rendered page nagelezen indien rendering beschikbaar is

## PUBLISH_REVIEW

Resultaat van `air-treatment-analysis-workflow / PUBLISH_REVIEW`:

- `PASS — READY_FOR_HUMAN_VALIDATION`
- of `FAIL — KEEP_NOINDEX`

## Menselijke beslissing

- [ ] menselijke validatie expliciet verkregen
- [ ] eventuele structurele actie (merge/redirect/noindex) expliciet goedgekeurd
- [ ] indexatie alleen gewijzigd na expliciete instructie

Een machine PASS of PUBLISH_REVIEW PASS activeert de indexatie nooit automatisch.
