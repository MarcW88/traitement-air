# Lot 1 — Approfondissement éditorial et QA ciblée
Date : 2026-10-29
Branche : `editorial/dehumidification-deepening-20261029`
Statut : **Prêt pour revue humaine ; non certifié pour publication**.

## Périmètre
Trois pages approfondies dans les deux emplacements, sources `content/<route>/body.html` et HTML publiable `<route>/index.html`. Aucun changement du hub, ni modification des autres pages existantes.

## Sources / preuves
- ASHRAE 2024, chapitre 24 : https://handbook.ashrae.org/Handbooks/S24/SI/S24_Ch24/S24_Ch24_si.aspx — fonctionnement dessiccant, régénération, configurations et conditions de service.
- ASHRAE 2024, chapitre 25 : https://handbook.ashrae.org/Handbooks/S24/SI/S24_Ch25/S24_Ch25_si.aspx — fonctionnement mécanique, faibles points de rosée et procédés combinés.
- CIBSE Journal CPD, février 2026 : https://www.cibsejournal.com/cpd/modules/2026-02-cdd/ — contraintes thermiques, efficacité conditionnelle, intégration et comparaison.
- Engineering Toolbox, ratio d'humidité : https://www.engineeringtoolbox.com/humidity-ratio-air-d_686.html — `w=0.62198 pv/(P-pv)`, base des exemples.

## Fact-check des exemples
Pression 101325 Pa ; pression de saturation approximée par Magnus : `psat=610.94*exp(17.625*T/(T+243.04))` en Pa, T en °C. `pv=HR*psat` où HR est une fraction.
- 20 °C / 60 % HR : 8,715 g/kg air sec ; 20 °C / 40 % HR : 5,783 g/kg. Pour 1000 kg air sec/h, différence 2,932 kg eau/h soit environ 70,4 kg/24h.
- 25 °C / 65 % HR : 12,877 g/kg ; 25 °C / 50 % HR : 9,858 g/kg. Pour 1000 kg air sec/h : 3,019 kg eau/h soit environ 72,5 kg/24h.
- Exemple énergétique **explicitement fictif** : 3 kg/h * 2000 h = 6000 kg/an ; consommations totales supposées 1 et 2 kWh/kg = 6000 et 12000 kWh/an ; tarif fictif uniforme 0,20 €/kWh = 1200 et 2400 €/an. A et B ne correspondent pas aux technologies en concurrence. Ne pas présenter ce modèle comme un devis ni un TCO réel.
- Les résultats supposent des états d'air constants et ne remplacent pas courbes fabricant, bilan dynamique, fuites, besoins de chaleur, dégivrage ou régulation.

## Valeur ajoutée
- Dessiccation : flux de procédé/régénération illustrés, bilan d'eau, grille de consultation.
- Condensation : parcours de l'air et de l'eau, bilan d'eau, contrôles du choix d'équipement.
- Comparatif : matrice multi-critères, méthode énergétique, montage hybride représenté.
- Tout schéma est original et conceptuel, non un plan d'installation. Les hypothèses sont signalées et aucune expérience terrain n'est prétendue.

## QA accessible réellement exécutée
- Six fichiers modifiés sur la branche (trois sources et trois HTML), lisibles depuis GitHub.
- HTML des trois pages : 1 seul H1, 8 sections, absence d'ID dupliqués, canonical attendu.
- Chaque page présente au moins un schéma SVG avec `role=img`, légende, et un tableau orienté décision.
- Vérification arithmétique indépendante des exemples avec équation documentée.
- Relecture de la distinction entre hypothèse et résultat observé.
- Les liens SEO et maillage existants ont été conservés, pas d'ajout de nouvelles routes.

## Limites des contrôles
- Pas de tests Playwright desktop/mobile, capture de rendu, axe ou Lighthouse ; les SVG et tableaux doivent être vérifiés sur mobile.
- Pas de build complet, validation HTML automatisée ni crawl sur une copie locale.
- Les états d'air et hypothèses de calcul ne constituent pas des performances produits.
- Revue par un ingénieur CVC qualifié non réalisée.
- Recherche SERP exhaustive et signaux Search Console non disponibles.

## Décision recommandée
**READY FOR HUMAN CONTENT REVIEW — NOT READY TO MERGE**. Demander autorisation explicite avant fusion et déploiement, idéalement après QA navigateur et vérification technique spécialisée.
