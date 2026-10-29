# Lot 1 — rapport final d'intégration, 29 octobre 2026

Branche : `editorial/dehumidification-cluster-lot1-20261029`
Décision : **NE PAS FUSIONNER / NE PAS DÉPLOYER** tant que les tests complémentaires et la validation humaine ne sont pas terminés.

## Modifications sur la branche

- Trois brouillons sources : `content/solutions-traitement-air/deshumidification-par-dessiccation/body.html`, `content/solutions-traitement-air/deshumidification-par-condensation/body.html`, `content/comparatifs/deshumidification-condensation-vs-dessiccation/body.html`.
- Trois pages HTML correspondantes dans les chemins publics statiques (leurs `index.html`).
- Nouveau hub `comparatifs/index.html` pointant vers le comparatif.
- Recherche / evidence : `content/research/dehumidification-lot1/evidence.md`.
- Pages produites en reprenant l'enveloppe HTML, le header, le footer et les feuilles CSS d'une page actuellement présente dans le dépôt. Aucune modification des routes existantes.

## QA effectivement exécutée via GitHub (4 pages)

| Vérification | Résultat |
|---|---|
| Quatre fichiers HTML présents sur la branche | PASS |
| Un seul H1 et un seul main par page | PASS |
| Canonical égal à la route attendue avec / final | PASS |
| JSON-LD parsable : WebPage/CollectionPage + BreadcrumbList | PASS |
| Toutes les ancres locales de l'aside correspondent à un ID | PASS |
| Références CSS du site incluses dans les pages | PASS |
| Absence de noindex dans les quatre pages statiques | PASS (constat seulement) |
| Liens sortants internes principaux vers la page mère, les outils et les guides ciblés | PASS, chemins vérifiés dans GitHub |
| Hub comparatifs lié à son premier comparatif | PASS |

## Sitemap prévisionnel

Le fichier `scripts/build_sitemap.py` détecte les `index.html` éligibles, refuse les canoniques inattendus et génère `lastmod` à partir de Git. Il doit donc découvrir ces quatre nouvelles routes lors du prochain build :
- https://traitement-air.fr/comparatifs/
- https://traitement-air.fr/comparatifs/deshumidification-condensation-vs-dessiccation/
- https://traitement-air.fr/solutions-traitement-air/deshumidification-par-condensation/
- https://traitement-air.fr/solutions-traitement-air/deshumidification-par-dessiccation/

Le sitemap de production et celui de `main` n'ont pas été modifiés. **Simulation raisonnée depuis le script, pas exécution réelle du générateur**.

## Points bloquants ou non certifiés

1. Playwright desktop/mobile, captures réelles, axe-core et Lighthouse **non exécutés** : rendu visuel et responsive non certifiés.
2. Pas de build Next.js ni serveur de prévisualisation exécuté. Les pages sont des copies de l'enveloppe statique existante ; le bon comportement JS/Next et l'intégration CSS réelle restent à tester.
3. HTML Validate et contrôle exhaustif du maillage de tout le site **non exécutés**.
4. Les anciennes pages/hubs ne pointent pas encore vers les nouvelles routes : découverte par maillage entrant insuffisante avant publication.
5. Aucune recherche exhaustive des SERP françaises, ni données Search Console ; cannibalisation non tranchée.
6. Revue technique indépendante des contenus non réalisée.
7. Le hub Comparatifs existe sur la branche, mais son entrée dans la navigation globale n'est pas implémentée.
8. Le sitemap prévisionnel n'est pas un sitemap testé en CI.
9. Vérifier le balisage HTML et l'affichage du tableau comparatif avec le thème effectif avant publication.

## Statut

**Intégration GitHub effectuée, contrôle structurel ponctuel PASS, QA complète BLOQUÉE.**
Attendre la validation humaine et les contrôles non exécutés avant toute fusion / déploiement.


## QA finale complémentaire — 29 octobre 2026

Deux pages existantes ont reçu un maillage entrant ciblé, sans réécriture de leurs contenus :
- `solutions-traitement-air/deshumidification-industrielle/index.html` relie les deux procédés et le comparatif ;
- `solutions-traitement-air/index.html` relie le hub Comparatifs et le comparatif.
Le hub Comparatifs pointe vers son article et le comparatif pointe vers ses deux fiches sœurs.

### Contrôles réellement exécutés par lecture du contenu GitHub (six fichiers HTML)
- 6/6 un seul H1, un title, une meta description, canonical conforme au chemin.
- 6/6 JSON-LD décodable et aucune ancre interne locale sans ID correspondant.
- Deux pages parentes et quatre nouvelles pages possèdent des liens entrants/sortants vérifiés textuellement.
- Le code de `scripts/build_sitemap.py` parcourt les `index.html`, filtre les pages noindex et vérifie les canoniques; les 4 nouvelles pages répondent à ses préconditions observables. Le script n'a pas été exécuté: sitemap **prévisionnel**, non certifié par CI.
- Aucun changement apporté au sitemap de `main`.

### Contrôles non exécutés
- Playwright desktop/mobile et axe : environnement d'exécution avec navigateur/clone local indisponible ici.
- html-validate, Lighthouse, build complet, crawl exhaustif du site et vérification HTTP des liens.
- Contrôle scientifique indépendant et analyse GSC/SERP.

### Réserve QA
Le HTML réutilise les CSS du site; aucune capture réelle ne certifie l'adaptation de la table comparative aux petits écrans. Avant fusion, exécuter le workflow de QA dans un environnement capable de cloner la branche et de lancer un serveur local, avec captures à 375px, 768px et 1440px, contrôle du débordement horizontal et navigation clavier.

**Verdict : PASS statique ciblé / BLOCKED QA navigateur et CI / PAS READY FOR MERGE.**
