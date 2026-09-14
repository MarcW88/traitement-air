---
name: air-treatment-content-workflow
description: Workflow de production/correction SEO/GEO pour traitement-air.fr. Consomme une décision d'analyse, une matrice SERP/content-gap et un brief, puis orchestre les skills GitHub complets de voice, copy, preuves, GEO, humanisation, SEO et QA. Un DEEP_REWRITE ne peut pas être rédigé sans research artifact et doit produire un post-write gap check.
provenance: custom
metadata:
  engine_version: 2
  adapted_for: traitement-air.fr
  source_engine: https://github.com/MarcW88/bloc-notes-numerique/tree/main/.agents/skills/guide-content-workflow
  orchestration_target: ">=80% existing GitHub skills"
  custom_scope: "research handoff + air-treatment routing/safety + source-of-truth + post-write coverage gate"
---

# Air Treatment Content Workflow v2

## Rôle

C'est le **seul workflow de production/correction** du site.

Séquence normale pour une page existante :

`AUDIT / CLUSTER_AUDIT → décision → research gate → brief → draft → factual/GEO/style/SEO passes → post-write gap check → PUBLISH_REVIEW`.

Décisions :

- `KEEP` → ne pas réécrire ;
- `LIGHT_UPDATE` → corriger uniquement le scope identifié ;
- `DEEP_REWRITE` → reconstruire en préservant la valeur identifiée, **uniquement après le gate de recherche** ;
- `MERGE / NOINDEX` → aucune nouvelle version sans décision humaine sur le rôle de l'URL.

Le workflow ne change jamais l'indexation de lui-même.

---

# 1. Entrées obligatoires

Lire :

- `AGENTS.md` ;
- `.agents/skills/air-treatment-analysis-workflow/SKILL.md` ;
- audit/cluster audit et décision ;
- page existante + `content/<route>/body.html` ;
- pages voisines ;
- `content/brand/voice.md` ;
- sources/preuves disponibles.

Pour `DEEP_REWRITE`, lire obligatoirement :

- `content/research/<route>/serp-coverage.md` ;
- le brief associé lorsque disponible.

Si la matrice manque, si elle n'a pas inspecté une SERP actuelle ou si un data gap empêche de confirmer un MUST central : **STOP — retourner au workflow d'analyse**. Ne pas improviser la recherche pendant la rédaction.

---

# 2. Les skills doivent être réellement exécutés

Un nom dans ce fichier n'est pas une validation. À chaque étape, ouvrir le `SKILL.md` complet correspondant et appliquer sa méthode pertinente.

Les upstream RampStack listés dans `.agents/UPSTREAM_SOURCES.json` sont vendored verbatim. Les règles spécifiques au traitement de l’air restent dans ce workflow et dans `AGENTS.md`, jamais dans les copies upstream.

---

# 3. Étape 1 — convertir la recherche en brief

Utiliser :

- `seo-keyword` et `search-intent` pour confirmer le query set/tâche ;
- `seo-competitor` pour relire les conclusions SERP/content-depth d'un `DEEP_REWRITE` ;
- `jtbd-framing` si le job doit être formulé plus précisément ;
- `information-architecture` si le rôle de l'URL est encore ambigu ;
- `content-brief-authoring` comme méthode principale du brief.

Le brief est persisté dans `content/briefs/<route>.md` et porte :

`workflow_version: 2`

Il doit traduire la matrice en choix éditoriaux, pas la remplacer.

Minimum requis :

- primary query + tâche ;
- audience/maturité ;
- ownership et exclusions ;
- MUST/SHOULD issus de la matrice ;
- angle/thèse ;
- preuves/faits nécessaires ;
- data gaps ;
- information gain choisi ;
- contraintes sécurité/fraîcheur ;
- valeur existante à préserver ;
- prochaines questions/liens ;
- structure proposée **après** recherche.

Aucune architecture imposée par `PLAN`, `PROJECT`, `CHOICE`, etc.

---

# 4. Étape 2 — voice avant copy

Utiliser le skill complet `brand-voice` avec `content/brand/voice.md` comme système de voix du site.

Le draft doit rester : pratique sans simplisme, expert sans ton scolaire, direct sans brutalité, indépendant sans cynisme.

Si un passage doit être plus prudent pour des raisons de sécurité ou de réglementation, le tone shift approprié prime sur le style marketing.

---

# 5. Étape 3 — rédaction pour la substance

Utiliser le skill complet `content-and-copy`.

Le draft doit :

- répondre assez tôt à la tâche centrale ;
- couvrir chaque MUST avec la profondeur nécessaire, pas avec un quota de mots ;
- apporter les chiffres, distinctions, exemples, règles de décision ou synthèses décidés dans le brief ;
- expliciter les trade-offs importants ;
- distinguer fait, interprétation, hypothèse et inconnue ;
- éviter le remplissage et les répétitions ;
- utiliser tableau/liste/étapes uniquement lorsque le format aide réellement ;
- préserver les passages valides identifiés par l'audit ;
- ne jamais inventer test, mesure, inspection, prix, économie, règle, procédure ou disponibilité.

Source de vérité :

`content/<route>/body.html`

Le HTML généré n'est jamais la source éditoriale primaire.

---

# 6. Étape 4 — preuves et factualité

Après rédaction, exécuter `fact-check` sur **les claims réellement écrits**.

Pour les claims instables : source, date, territoire, scope et conditions à côté ou suffisamment près du claim.

`evidence-based-reviews` est conditionnel et ne permet jamais de simuler une expérience.

Les passages sécurité (structure, fondations, gaz, électricité, amiante, hauteur/toiture, risque structurel, travail réglementé) sont relus séparément avant toute passe stylistique.

---

# 7. Étape 5 — GEO/AEO sans slop

Exécuter le skill complet `seo-aeo-geo` **après** que les faits ont été vérifiés.

Appliquer seulement les principes qui améliorent aussi la page humaine :

- réponse directe au début d'une section si elle répond à une vraie question ;
- faits atomiques et contexte/source adjacents ;
- définitions lorsque nécessaires ;
- tableaux pour vraies données/comparaisons ;
- étapes numérotées pour une procédure réellement séquentielle ;
- dates/méthodologie pour les données sensibles.

Interdits : FAQ artificielle, répétition de la même réponse sous plusieurs formes, sous-titres en question uniquement pour les bots, `snippet blocks` qui cassent la lecture.

L'objectif GEO est la **citation worthiness**, pas un style robotique.

---

# 8. Étape 6 — maillage et conversion

Exécuter `internal-linking-audit`. Un lien existe parce qu'il répond à la prochaine question logique, jamais pour atteindre un quota.

Exécuter `affiliate-value` lorsque la page influence une dépense/devis/choix de professionnel.

Pour `LEAD`, `cro-optimization` intervient seulement après que la valeur et la confiance sont établies.

---

# 9. Étape 7 — finition éditoriale séparée

Exécuter séparément, dans cet ordre :

1. `humanizer` sur tout le contenu visible ;
2. `general-writing` ;
3. `anti-ai-slop` en review/detection ;
4. `seo-drift` uniquement si un baseline utile existe.

Après chaque passe, préserver : faits, sources, nuance, sécurité, MUST coverage et information gain. Une passe de style ne peut pas supprimer la substance qui justifie la page.

---

# 10. Étape 8 — SEO et QA

Exécuter :

1. `seo-onpage` ;
2. `seo-technical` ;
3. `seo-best-practices` pour les règles applicables ;
4. `editorial-qa` ;
5. lecture rendue desktop/mobile lorsque possible.

Vérifier que title/H1/description correspondent à l'intention réellement traitée, pas seulement au mot-clé primaire.

---

# 11. Étape 9 — post-write gap check obligatoire

Pour chaque `DEEP_REWRITE` v2, créer :

`content/reviews/<route>/post-write-gap-check.md`

à partir de `references/post-write-gap-check-template.md`.

Reporter **chaque MUST et SHOULD pertinent** de la matrice pré-write :

- statut `COVERED / PARTIAL / MISSING` ;
- emplacement dans la page ;
- preuve/source préservée ;
- justification si PARTIAL.

Puis vérifier :

- les opportunités GEO réellement utiles sont présentes ;
- l'information gain choisie a survécu au style pass ;
- brand voice, humanizer, general-writing et anti-ai-slop ont été exécutés séparément ;
- aucune nouvelle structure clonée n'a été créée.

Un `MUST = MISSING`, claim central non vérifié ou data gap central non résolu force :

`FAIL — KEEP_NOINDEX`

Le workflow ne peut pas transformer ce FAIL en PASS en ajoutant une note.

---

# 12. Handoff vers PUBLISH_REVIEW

Une fois le gap check terminé, passer la main à :

`air-treatment-analysis-workflow / PUBLISH_REVIEW`.

Ne pas auto-valider dans ce workflow.

Statuts possibles dans les artefacts : `BRIEF_READY`, `DRAFT_READY`, `QA_IN_PROGRESS`, `REVISION_REQUIRED`, `HUMAN_APPROVED`, `PUBLISHABLE`.

`PUBLISHABLE` exige : PUBLISH_REVIEW PASS + validation humaine + contrôles techniques. L'indexation reste une instruction distincte.

---

# 13. Interdits

Ne pas utiliser comme proxy de qualité : quota de mots, nombre minimum de H2/H3, quota de liens/sources, nombre obligatoire d'étapes, FAQ/tableau obligatoire, score qualité artificiel ou structure fixe par cluster/type.

Ne pas recopier dans ce workflow les frameworks maintenus dans les upstream skills. Sa valeur est l'orchestration, les frontières du traitement de l’air, la sécurité, les gates research/post-write et l'intégration dans la source de vérité.
