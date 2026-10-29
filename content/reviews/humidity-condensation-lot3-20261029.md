# Lot 3 — Humidité et condensation industrielles : contrôle avant publication

Date : 29 octobre 2026. Statut : PR #4 en brouillon ; ne pas fusionner ni déployer sans accord explicite.

## Objectifs et intentions
- `/problemes/condensation-tuyauterie-industrielle/` : distinguer condensation, fuite et pont thermique ; point de rosée, isolation et continuité du pare-vapeur ; critères de consultation.
- `/problemes/humidite-entrepot/` : diagnostiquer les apports de vapeur et d'eau dans un entrepôt, puis hiérarchiser infiltration, déshumidification et traitement des parois froides.
- Ces intentions se distinguent des pages génériques `/problemes/condensation-industrielle/` et `/problemes/humidite-industrielle/` : il s'agit de cas d'usage localisés.

## Sources utilisées
- ASHRAE Handbook, Mechanical Dehumidifiers and Related Components : https://handbook.ashrae.org/Handbooks/S20/IP/S20_Ch25/S20_ch25_ip.aspx (ventilation, infiltration, apports internes et activités).
- U.S. Department of Energy, Building Science Education : https://bsesc.energy.gov/energy-basics/hvac-sealed-and-insulated-metal-ducts (isolation continue et contrôle de vapeur sur conduits froids ; principe à adapter aux conduites industrielles).
- U.S. Department of Energy, Building Science Education : https://bsesc.energy.gov/energy-basics/pipes-exterior-walls (isolation de canalisations froides lorsque la condensation est possible).
Les exemples chiffrés sont théoriques, non des mesures industrielles ni des retours de chantier. Vérifier les exigences propres à la juridiction et au procédé avant mise en oeuvre.

## Livrables vérifiés
- Deux fichiers `content/problemes/<slug>/body.html`, deux `problemes/<slug>/index.html`.
- Maillage entrant depuis `problemes/index.html` et `solutions-traitement-air/deshumidification-industrielle/index.html`.
- Schémas SVG originaux, un tableau de diagnostic par page, 1 H1 par page, canonicals corrects, ancres internes vérifiées.
- Environ 965 mots pour la condensation sur conduite et 1 163 mots pour l'humidité en entrepôt (articles HTML, approximation).
- Deux demandes BFL distinctes générées et intégrées : `assets/generated/problemes-condensation-tuyauterie-industrielle-editorial.webp` et `assets/generated/problemes-humidite-entrepot-editorial.webp`.
- Génération et commit des images : GitHub Actions #40874886813, SUCCESS. Workflow ponctuel supprimé de la branche après réussite.

## Réserves
- Les photos sont des illustrations générées par IA et non des installations réelles ; l'exactitude physique des détails visibles ne constitue pas une preuve.
- Inspection humaine des clichés et revue d'ingénierie indépendante non réalisées.
- Contrôles visuels Chromium / Playwright de la PR et autres validations CI à lire avant décision finale ; les échecs historiques des vérifications d'agents ne doivent pas être attribués aux deux articles sans examen des logs.
- Aucune fusion ni aucun déploiement effectués pour ce lot.
