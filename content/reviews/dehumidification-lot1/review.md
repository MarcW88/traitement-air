# Lot 1 — revue éditoriale et QA prépublication

Date: 2026-10-29
Branche: editorial/dehumidification-cluster-lot1-20261029
Statut: **FAIL — KEEP_NOINDEX / validation humaine requise** (non publiable en l'état)

## Éléments réalisés
- Trois nouvelles sources `content/<route>/body.html`, une par intention.
- Références ASHRAE/CIBSE explicites; claims vérifiables et prudents.
- Aucun chiffre inventé, aucune expérience pratique fictive ni promesse commerciale.
- Maillage contextuel vers la page mère, les pages sœurs, l'hygrométrie et le dimensionnement.
- Relecture de formulations génériques / anti-IA-slop et suppression des superlatifs sans preuves.
- Table de comparaison qualitative sur la page décisionnelle.
- Distinction visible des exemples théoriques et des résultats mesurés.

## QA restant à exécuter — bloquant pour publication
- Les trois fichiers HTML de sortie `<route>/index.html` ne sont pas générés : les sources ne sont pas des pages publiées.
- Aucun rendu navigateur ni captures Playwright du nouveau contenu; impossible de certifier responsive/accessibilité.
- Aucun test local HTML Validate, liens, audit JS, Lighthouse ou build de production exécuté.
- Aucun contrôle complet des SERP françaises / cannibalisation Search Console.
- Revue technique indépendante non réalisée.
- La route `/comparatifs/` n'a pas de hub publié; prévoir une page parent avant publication du comparatif.
- Ajouter au générateur/site la prise en charge de ces trois nouvelles sources sans remplacer les pages existantes.
- Contrôler H1 unique, canonical, robots, données structurées, sitemap, maillage réel après génération.

## Résultat
Sources éditoriales prêtes pour relecture, mais **pas** prêtes à fusionner ou déployer. L'évaluation positive du contenu ne vaut pas PASS technique ou visuel.
