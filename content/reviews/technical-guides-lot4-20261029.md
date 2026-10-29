# Lot 4 — QA et preuves (29 octobre 2026)

## Livrables
Six nouvelles pages sur une branche indépendante : trois guides (perte de charge, débit, classes ISO 16890/EN 1822), deux comparatifs (captage / ventilation ; HEPA / filtre fin), et un outil de calcul volumique avec saisie et résultat côté navigateur. Six sources `content/<route>/body.html` et six pages `<route>/index.html`.
Maillage entrant depuis `guides/index.html`, `comparatifs/index.html`, `outils/index.html`.

## Photographies
Six demandes BFL ciblées et six fichiers `assets/generated/*.webp` effectivement intégrés ; workflow #40877928616 SUCCESS après une première tentative dont le push avait été refusé pendant des commits concurrents. Demandes toutes vérifiées GENERATED. Le workflow de génération temporaire a été supprimé.

## Fact-check
- ISO : https://www.iso.org/standard/85672.html — ISO 16890-1 édition 2 en cours de publication au 29/10/2026 ; ne pas prétendre qu'elle est déjà en vigueur.
- EN 1822 : https://www.iteh.fr/catalog/standards/cen/cd503f07-b90d-4742-bb9d-357323796239/pren-1822-1 — seuils H13 99,95 % et H14 99,995 % à la MPPS, attention au statut projet pour la révision 2026.
- HSE LEV : https://www.hse.gov.uk/lev/ — captage à la source et limites d'une ventilation générale.
- HSE Ventilation : https://www.hse.gov.uk/ventilation/ — renouvellement, ventilation et précautions d'interprétation.
- DOE fan systems : https://www.energy.gov/eere/amo/articles/improving-fan-system-performance-sourcebook-industry — puissance aéraulique, ventilateur et pertes de charge.

## Vérification réalisée
Les six fichiers HTML ont un H1 unique, JSON-LD parsable, ancres valides, une image et un SVG par page. Les longueurs de texte sont de 527 à 636 mots, hors code et en approximation.
Exemples calculés et contrôlés à la main : 4 000 m³/h × 150 Pa / 3 600 = 166,7 W ; /0,55 = 303 W ; × 2 000 h ≈ 606 kWh. 20 × 12 × 5 = 1 200 m³ ; ×4/h = 4 800 m³/h.

## Réserves obligatoires
Ces contenus constituent un socle technique, non un rapport d'ingénierie. Les schémas sont conceptuels et les photographies générées ne prouvent pas une installation réelle.
Le calculateur contient un script client et doit être essayé dans Chromium, particulièrement pour vérifier son activation, l'absence de blocage du navigateur et les saisies invalides.
Aucune QA Playwright/axe/Lighthouse n'est qualifiée de réussie avant lecture des résultats du workflow PR. L'intégrité des agents partagés est historiquement en échec ; ne pas confondre avec les changements éditoriaux. Aucun déploiement autorisé sans validation.
