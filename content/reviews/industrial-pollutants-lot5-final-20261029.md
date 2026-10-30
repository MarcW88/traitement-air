# Lot 5 — Bilan avant publication — 29 octobre 2026

## Statut et périmètre
PR #6 brouillon, branche `editorial/industrial-pollutants-lot5-20261029`. Les six articles et leurs images BFL sont validés éditorialement par le propriétaire. Aucune fusion ni déploiement n'est autorisé.

1. `/solutions-traitement-air/traitement-cov-charbon-actif/`
2. `/solutions-traitement-air/traitement-odeurs-industrielles/`
3. `/solutions-traitement-air/traitement-ammoniac-industriel/`
4. `/solutions-traitement-air/traitement-h2s-industriel/`
5. `/solutions-traitement-air/destruction-ozone-industriel/`
6. `/solutions-traitement-air/lavage-gaz-acides-industriels/`

Six sources de corps d'article HTML, six pages statiques, six demandes BFL `GENERATED`, six WebP intégrés, schémas et tableaux spécifiques.

## Contrôles
Contrôles statiques sur chaque page : H1=1, canonical correct, marqueurs d'image intégrés, attribut alt, ancres de la table des matières résolues. Premier Playwright ciblé run #40897762993 : 12 couples (6 pages × desktop/mobile) effectivement capturés ; HTTP, images, erreurs console et H1 sans défaut remonté par le garde-fou. Défaut confirmé : `horizontalOverflow` sur les six vues mobiles. Chaque rendu possède un résultat axe avec une violation, dont la cause doit être qualifiée avant conclusion. Corrections ciblées sur les six sources/pages : `min-width:0; max-width:100%; overflow-wrap:anywhere; overflow-x:clip` appliqués aux articles et conteneurs de tableaux rendus scrollables.

Second run #40898259036 : relance ciblée pour vérifier les corrections, avec identification précise des violations axe. Sa conclusion doit être lue avant déclaration de QA finale satisfaisante.

Audit général Chromium au dernier commit de la version initiale du lot : run #40896820959 en cours à la dernière vérification. D'autres audits intermédiaires avaient réussi, mais ne portent pas sur les corrections finales.

## Réserves
Les échecs de contrôles `Validate editorial engine` / `Verify exact shared agents` sont historiquement récurrents sur ce dépôt et nécessitent qualification distincte des défauts visuels.
Les calculs de charge sont pédagogiques et ne constituent ni une garantie d'abattement ni une consigne de sûreté.
Les sources externes fournissent des principes généraux; la conformité est spécifique à chaque site et juridiction.
**Ne pas merger ni publier sans accord explicite.**
