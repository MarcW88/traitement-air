# traitement-air.fr — règles agents

## Langue et positionnement
- Écrire par défaut en français de France (fr-FR).
- Centre d’expertise indépendant : comprendre, mesurer et comparer avant d’orienter vers une technologie ou un spécialiste.
- Ton précis, pédagogique, neutre et technique. Aucun discours fabricant, urgence artificielle ou performance non étayée.
- Préserver les URL, le design et le fonctionnement HTML statique.

## Clusters et ownership
| Type | Répertoire | Rôle |
|---|---|---|
| SOLUTION | solutions-traitement-air/ | technologies, critères, limites, dimensionnement |
| SECTOR | secteurs/ | exigences et risques d’un environnement |
| PROBLEM | problemes/ | symptôme, causes, mesure, solutions |
| POLLUTANT | polluants/ | source, exposition, mesure, traitement |
| INDOOR | air-interieur/ | habitat, séparé du B2B |
| GUIDE | guides/ | définitions et comparaisons |
| TOOL | outils/ | diagnostic, calcul, orientation |
| LEAD | demander-un-devis/ | qualification et mise en relation |

Ces types fixent les frontières et risques, jamais un plan, une longueur ou un nombre de sections.

## Workflow obligatoire
1. air-treatment-analysis-workflow / AUDIT ou CLUSTER_AUDIT.
2. Décision KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX.
3. Pour LIGHT_UPDATE ou DEEP_REWRITE : air-treatment-content-workflow.
4. air-treatment-analysis-workflow / PUBLISH_REVIEW.
5. Validation humaine avant indexation ou action structurelle.

Un DEEP_REWRITE exige une SERP actuelle inspectée et content/research/<route>/serp-coverage.md avant le brief. Après rédaction, créer content/reviews/<route>/post-write-gap-check.md. Un MUST = MISSING force FAIL — KEEP_NOINDEX.

## Skills à exécuter complètement
Ouvrir les SKILL.md pertinents, notamment seo-content-audit, seo-keyword, search-intent, seo-competitor, content-refresh, fact-check, evidence-based-reviews, affiliate-value, content-brief-authoring, brand-voice, content-and-copy, information-architecture, internal-linking-audit, jtbd-framing, cro-optimization, seo-aeo-geo, seo-onpage, seo-technical, seo-best-practices, seo-drift, humanizer, general-writing, anti-ai-slop et editorial-qa. Les workflows custom orchestrent ces méthodes, ils ne les résument pas.

## Profondeur, preuves et sécurité
- Documenter intentions, MUST/SHOULD/OPTIONAL, MISSING/PARTIAL/COVERED, information gain, overlap et data gaps.
- Ne jamais reconstruire de mémoire SERP, normes, seuils, classes de filtration, rendements, débits, pertes de charge, coûts ou mesures.
- Les faits instables portent source, date, territoire, portée et conditions.
- Distinguer principe physique, mesure, hypothèse, exemple, recommandation et exigence réglementaire.
- Ne jamais simuler inspection, test ou diagnostic.
- Pour risques sanitaires, gaz toxiques, ATEX, incendie, contamination critique, pression de salle propre ou intervention réglementée, expliciter les limites et l’escalade professionnelle.
- Comparer les pages voisines : cannibalisation, fragmentation et clonage structurel.
- Aucun quota de mots, H2, FAQ, liens ou sources comme proxy de qualité.

## SEO/GEO et maillage
Construire les relations SECTEUR → PROBLÈME → PARAMÈTRE/POLLUANT → SOLUTION → TECHNOLOGIE. Favoriser des réponses directes, définitions nécessaires, faits atomiques contextualisés et vraies comparaisons. Pas de FAQ artificielle. Chaque lien répond à la prochaine question logique.

## Source de vérité
- content/<route>/body.html
- content/briefs/<route>.md
- content/research/<route>/serp-coverage.md
- content/reviews/<route>/
- content/brand/voice.md

Les index.html sont des sorties publiées. PUBLISH_REVIEW retourne seulement PASS — READY_FOR_HUMAN_VALIDATION ou FAIL — KEEP_NOINDEX. Aucun PASS n’indexe automatiquement.
