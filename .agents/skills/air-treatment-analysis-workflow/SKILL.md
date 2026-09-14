---
name: air-treatment-analysis-workflow
description: Workflow d'analyse SEO/GEO pour traitement-air.fr. Audite une URL ou un cluster, impose une recherche SERP/content-gap pour les reconstructions, contrôle preuves, intention, cannibalisation, sécurité, fraîcheur et valeur, puis décide KEEP, LIGHT_UPDATE, DEEP_REWRITE, MERGE ou NOINDEX. Sert aussi de PUBLISH_REVIEW final.
provenance: custom
metadata:
  engine_version: 2
  adapted_for: traitement-air.fr
  source_engine: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-analysis-workflow
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "orchestration + SERP/content-gap gates + air-treatment cluster integrity + safety + freshness"
---

# Air Treatment Analysis Workflow v2

## Rôle

C'est le **seul workflow d'analyse éditoriale** à utiliser pour les contenus de traitement-air.fr.

Il ne rédige pas. Il doit **lire et appliquer les skills spécialisés du dépôt**, dans leur version complète, puis ajouter uniquement les contrôles propres au site : frontières entre clusters de traitement de l’air, sécurité, fraîcheur des règles/performances/normes, similarité inter-pages et gates de recherche.

Séparation stricte :

- `air-treatment-analysis-workflow` = recherche, diagnostic, décision, cluster audit et publish review ;
- `air-treatment-content-workflow` = brief, production/correction et post-write gap check après handoff valide.

Un nom de route (`PLAN`, `PROJECT`, etc.) définit une frontière éditoriale. Il ne définit jamais un template, une longueur, un nombre de sections ou un ordre de H2.

---

# 1. Modes

## `AUDIT`

Pour une URL existante. Retourne une décision **sans réécrire la page**.

## `CLUSTER_AUDIT`

Analyse plusieurs URLs ensemble : ownership des intentions, overlap SERP, cannibalisation, fragmentation, trous utiles, maillage et clonage structurel. Ne déclenche aucune réécriture automatiquement.

## `PUBLISH_REVIEW`

Gate final après `air-treatment-content-workflow`.

Résultats autorisés :

- `PASS — READY_FOR_HUMAN_VALIDATION`
- `FAIL — KEEP_NOINDEX`

Un PASS n'autorise jamais l'indexation ou une action structurelle sans instruction humaine explicite.

---

# 2. Sources à lire avant de décider

Selon le périmètre :

- `AGENTS.md` ;
- page rendue et `content/<route>/body.html` ;
- brief, research artifacts et reviews existants ;
- pages voisines et pages d'autres clusters susceptibles de partager l'intention ;
- analyse sémantique, GSC, logs ou données disponibles ;
- **SERP actuelle** lorsque la décision dépend de la demande ou du format qui gagne ;
- sources actuelles pour les faits instables.

Ne jamais remplacer une donnée manquante par la mémoire du modèle. Un manque qui peut changer la décision devient un **data gap explicite**.

---

# 3. Exécution des skills existants

Le workflow n'en résume pas la méthode : il doit ouvrir et appliquer leurs `SKILL.md` complets.

## 3.1 Audit de la page

Exécuter `seo-content-audit` pour décider si l'URL mérite conservation, update, consolidation ou retrait du cluster.

## 3.2 Keyword / intent

Exécuter `seo-keyword` avec les données réellement disponibles. Utiliser ses étapes de discovery, inspection SERP, intent et clustering lorsque le scope l'exige.

Exécuter `search-intent` pour préciser :

- la tâche exacte ;
- le résultat attendu ;
- les sous-intentions ;
- la maturité ;
- ce qui appartient à une autre URL.

`jtbd-framing` est utilisé quand le job ou le contexte de décision reste ambigu.

## 3.3 Compétition SERP

Exécuter `seo-competitor` sur l'angle **SERP overlap + content depth** pour :

- tout `DEEP_REWRITE` ;
- toute nouvelle page stratégique ;
- toute décision où l'intention ou le niveau de couverture est contestable ;
- toute cannibalisation potentielle entre deux URLs.

Ne pas transformer l'analyse concurrentielle en imitation. Le but est d'identifier ce que la SERP exige, ce qui est facultatif et où une meilleure réponse est possible.

## 3.4 Refresh / preuves

Utiliser `content-refresh` pour intent drift, obsolescence, thin value, generic prose, trust gaps, cannibalisation et structural cloning.

Utiliser `fact-check` pour toute affirmation vérifiable qui peut influencer une décision : performances, normes, obligations, réglementation, normes, performances, rendement, garanties, sécurité, disponibilité.

Utiliser `evidence-based-reviews` uniquement pour une conclusion réellement expérientielle. Ne jamais simuler un test, une inspection ou du hands-on.

## 3.5 Valeur et architecture

- `affiliate-value` si la page influence une dépense, un devis, un professionnel ou un achat ;
- `information-architecture` si l'ownership ou le rôle de la page est incertain ;
- `internal-linking-audit` pour vérifier le prochain besoin logique du lecteur.

## 3.6 SEO/GEO et QA

Lors du review :

- `seo-onpage` ;
- `seo-technical` ;
- `seo-aeo-geo` pour extractabilité/citation worthiness, sans fabriquer de FAQ ;
- `anti-ai-slop` ;
- `editorial-qa` ;
- `seo-drift` seulement si un baseline utile existe.

---

# 4. Gate obligatoire avant `DEEP_REWRITE`

Un `DEEP_REWRITE` **ne peut pas** être handoff vers la rédaction sur la seule base d'une intuition éditoriale.

Créer et persister :

`content/research/<route>/serp-coverage.md`

à partir de `references/serp-coverage-matrix-template.md`.

La matrice doit contenir au minimum :

1. requête principale, variantes proches et sous-intentions ;
2. résultats réellement inspectés et type de page qui gagne ;
3. SERP features pertinentes ;
4. questions/besoins récurrents ;
5. données, exemples, outils ou preuves utilisés par les meilleurs résultats ;
6. état de la page actuelle : `MISSING / PARTIAL / COVERED` ;
7. priorité : `MUST / SHOULD / OPTIONAL` ;
8. opportunités réelles d'information gain ;
9. opportunités GEO/citation fondées sur des faits ou explications utiles ;
10. overlap avec nos autres URLs ;
11. data gaps.

### Règles

- Le SERP doit être **actuel et observé**, pas reconstruit de mémoire.
- `MUST` ne signifie pas copier tous les concurrents : il signifie que l'intention choisie ne peut pas être correctement satisfaite sans cet élément.
- Une opportunité d'information gain doit apporter une donnée, une synthèse, une distinction, un outil, un exemple ou une règle de décision utile. `Faire plus long` n'est pas un gain.
- Si la SERP ou une source nécessaire n'est pas disponible, consigner le gap. Si ce gap empêche de confirmer l'intention ou un MUST central, **ne pas rédiger**.

### Handoff requis

`DEEP_REWRITE` peut passer à `air-treatment-content-workflow` seulement si :

- la matrice existe ;
- l'ownership de l'intention est clair ;
- les MUST sont explicites ;
- les data gaps bloquants sont résolus ou reconnus comme bloquants.

---

# 5. Frontières entre clusters

- `/guides/` = décisions transversales : démarrage, ordre, phases, budget, coûts, permis, aides, rendement ;
- `/secteurs/` = décision/préparation d'un chantier concret ;
- `/solutions-traitement-air/` = énergie, confort, installations et conditions de pertinence ;
- `/problemes/` = symptôme, causes possibles, contrôles sûrs et prochaine action ;
- `/air-interieur/` = uniquement tâches réellement exécutables et sûres pour le public ;
- `/demander-un-devis/` = sélection, scope, comparaison, contractualisation et conversion.

### Test pratique

Si deux URLs peuvent garder la même réponse centrale, les mêmes critères et les mêmes sections en remplaçant quelques mots, leur séparation est probablement insuffisante.

---

# 6. Sécurité et fraîcheur

La page est jugée sur sa capacité à rendre une chose **plus claire, faisable, sûre ou décidable**, pas sur sa longueur.

Fraîcheur proportionnée :

- principe physique stable → exactitude ;
- prix/main-d'œuvre/disponibilité → source actuelle + date ;
- norme/réglementation/seuil d’exposition/certification → source officielle + territoire + date ;
- performance/rendement/économie → hypothèses et conditions explicites.

Escalade vers un professionnel qualifié lorsque la tâche implique notamment structure/fondations, gaz, électricité à risque, amiante, toiture/hauteur, dommage potentiellement structurel ou intervention réglementée.

Ne jamais transformer une absence d'inspection en diagnostic certain.

---

# 7. Similarité structurelle

En `CLUSTER_AUDIT` et `PUBLISH_REVIEW`, comparer les pages voisines et rechercher :

- mêmes fonctions de H2/H3 dans le même ordre ;
- intro/conclusion avec simple substitution du sujet ;
- tableau ou FAQ systématique ;
- même nombre d'étapes sans nécessité ;
- mêmes CTA comme fin obligatoire ;
- mêmes transitions/cadence ;
- catégories `PLAN/PROJECT/...` ou `CHOICE/EXPLAINER/HOW_TO` utilisées comme squelettes.

Les composants visuels peuvent être réutilisés ; **la pensée éditoriale ne doit pas être préfabriquée**.

---

# 8. Décisions

## `KEEP`

Tâche claire, distincte, actuelle, sûre et suffisamment utile.

## `LIGHT_UPDATE`

Correction limitée : faits, exemples, metadata, maillage, sécurité, sources, passage ou frontière. L'architecture fondamentale reste adaptée.

## `DEEP_REWRITE`

Pour problème structurant : intent drift, mauvaise ownership, incapacité à répondre, preuve centrale insuffisante, forte cannibalisation, faible information gain ou architecture industrialisée. **Déclenche le gate SERP obligatoire de la section 4.**

## `MERGE`

Une autre URL possède essentiellement la même tâche. Recommandation uniquement tant qu'aucune action structurelle n'est demandée.

## `NOINDEX`

Valeur/preuve/sécurité/justification insuffisante. Aucune suppression automatique.

Pour chaque décision : confiance, valeur à préserver, preuves, unknowns, blockers, cannibalisation, fraîcheur/sécurité et prochaine étape.

---

# 9. `PUBLISH_REVIEW` v2

Ne l'exécuter que sur une version considérée terminée.

## Gate A — blockers machine

Exécuter :

```bash
python3 scripts/validate_content_quality.py
python3 scripts/validate_upstream_skills.py
```

Ces scripts ne prouvent pas la qualité sémantique ; ils prouvent seulement les invariants qu'ils savent tester.

## Gate B — traçabilité de recherche

Pour tout contenu produit sous `engine_version: 2` après `DEEP_REWRITE`, vérifier :

- `content/research/<route>/serp-coverage.md` existe ;
- le brief s'appuie explicitement sur ses MUST et data gaps ;
- `content/reviews/<route>/post-write-gap-check.md` existe ;
- chaque MUST a un statut final ;
- aucun `MUST = MISSING` non résolu ;
- un `MUST = PARTIAL` possède une justification explicite et n'affaiblit pas l'intention centrale.

## Gate C — skills substantiels

Réexécuter les skills pertinents et confirmer :

- tâche/intention réellement satisfaite ;
- content gap principal résolu ;
- information gain réel, pas simple allongement ;
- faits importants correctement sourcés ;
- fraîcheur/territoire appropriés ;
- sécurité et limites préservées ;
- pas de faux test/diagnostic/inspection ;
- valeur sans affiliation ;
- cannibalisation résolue ;
- `seo-aeo-geo` : réponses/faits extractibles seulement lorsqu'ils sont utiles et sourçables ;
- pas de signal `HIGH` anti-AI-slop ;
- architecture propre à la tâche ;
- title/H1/canonical/robots/liens/schema cohérents ;
- version rendue relue lorsque disponible.

## Résultat

Tout blocker central, data gap bloquant, `MUST = MISSING`, claim central non vérifié ou intent gap non résolu force :

`FAIL — KEEP_NOINDEX`

Sinon :

`PASS — READY_FOR_HUMAN_VALIDATION`

---

# 10. Indexation

Le workflow ne change jamais `indexing_enabled`. Indexation uniquement après PUBLISH_REVIEW PASS, validation humaine et instruction explicite.

---

# 11. Ce que ce workflow ne doit pas devenir

Interdits comme proxy de qualité : quota de mots, nombre minimum de H2/H3, quota de liens/sources, FAQ/tableau obligatoire, nombre fixe d'étapes, score artificiel ou template imposé par catégorie.

La couche custom orchestre. Les méthodes SEO, compétiteur, brief, voice, copy, GEO, fact-check et QA restent dans leurs skills GitHub spécialisés.
