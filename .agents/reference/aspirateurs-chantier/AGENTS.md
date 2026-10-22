# Instructions du dépôt

Ce dépôt contient aspirateurs-chantier.fr.

## Maintenance éditoriale

Suivre `docs/content-maintenance.md` et `maintenance.config.json`. Préparer avec `python scripts/maintenance_orchestrator.py prepare --max-pages 10`. La préparation n’est pas un audit IA.

Réutiliser exclusivement les paires analysis/content-workflow existantes sous `.agents/skills/` : guides → guide, comparatifs → comparison, marques → brand, usages → usage, modeles → model. Lire intégralement le workflow pertinent et les skills spécialisés appelés. AUDIT avant correction, puis content-workflow seulement pour LIGHT_UPDATE/DEEP_REWRITE, et PUBLISH_REVIEW avant validation humaine. KEEP ne déclenche aucune modification éditoriale.

**Modèles : audit uniquement.** Respecter la phase 1 de model-content-workflow : pas de modification automatique des pages ni de `_generate_model_overrides.py`. Les corrections et la migration du renderer nécessitent une tâche séparée.

Persister les vrais rapports, preuves et run-evidence ; ne pas inventer de recherche, de test produit, de certification, de prix ou de PASS. Vérifier les claims de sécurité avec des sources adaptées. Préserver les sources de génération existantes et les plans propres aux pages ; aucun nouveau template éditorial.

Conserver URLs, canonical et état robots. MERGE/NOINDEX, suppression, redirection et indexation nécessitent une décision humaine. Ouvrir une PR avec rapports, registre, historique et corrections ; aucun merge automatique.

## Design

Lire DESIGN.md et `.agents/skills/site-design-review/SKILL.md` avant toute intervention sur l’interface. Préserver les composants et tokens existants.


## Shared agents — canonical routing (installation 2026-10-22)

Read `.agents/site-context.shared.md` and `.agents/shared-routing.json` before any editorial or design task. Use the full original files in `.agents/skills/` listed there, including every required specialist, phase and gate. Bloc-notes numérique is canonical for shared methods; Aspirateurs chantier supplies complementary model/recovery workflows. Do not substitute a shortened local workflow. This routing supersedes earlier workflow selections in this file; existing factual, safety, preservation, source-of-truth and indexation constraints remain mandatory. More specific site paths are resolved through the shared context.

Read workflows in full: existing-page AUDIT first, then only the correction justified by its handoff, then PUBLISH_REVIEW and actual evidence. A machine integrity PASS is not an editorial or visual PASS. Model workflows retain their original phase/audit-only limits. Read the original site-design-review for design/CSS/Playwright tasks. Do not create an absent page family merely because its agent is installed.

Original source workflows, configs, scripts and Actions are retained intact in `.agents/reference/`. Those French site generators/Actions are reference dependencies, not commands to run blindly on this site's content. Resolve theme, language, routes and native commands through the site context; record a missing required adapter as BLOCKED, never as PASS.

Run `python3 scripts/verify_site_agents.py` to verify all pinned original files.
