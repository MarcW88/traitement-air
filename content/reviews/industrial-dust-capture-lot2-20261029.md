# Lot 2 — preuves et QA avant publication

Date : 29 octobre 2026
Branche : `editorial/industrial-dust-capture-lot2-20261029`
Statut : **REVIEW REQUIRED — no merge/deploy**.

## Livrables
Cinq nouvelles routes avec `content/<route>/body.html` et `<route>/index.html`; trois hubs existants ont reçu des liens entrants.
- /solutions-traitement-air/depoussierage-industriel/ — 737 mots environ.
- /solutions-traitement-air/extraction-fumees-soudage/ — 709 mots environ.
- /problemes/poussieres-en-suspension-atelier/ — 695 mots environ.
- /polluants/poussieres-bois/ — 663 mots environ.
- /polluants/fumees-soudage/ — 703 mots environ.

## Evidence
- INRS ED 668 : https://www.inrs.fr/media.html?refINRS=ED+668 — captage à la source, ventilation générale complémentaire, transport, entretien et contrôles.
- INRS poussières de bois : https://www.inrs.fr/risques/poussieres-bois/ce-qu-il-faut-retenir — exposition, prévention, risques ATEX ; les valeurs limites citées concernent la France et ne sont pas transposées automatiquement à la Belgique.
- INRS soudage de métaux : https://www.inrs.fr/metiers/soudage-metal — procédés moins émissifs, captage, ventilation générale et rejet.
- HSE guidance : https://www.hse.gov.uk/welding/protect-your-workers/avoid-reduce-exposure.htm — hiérarchie de prévention et équipements de captage.
- HSE WL3 : https://www.hse.gov.uk/pubns/guidance/wl3.pdf — variantes de procédés et contrôle.
Les sources servent de références de sécurité; les conditions réglementaires propres au pays et au site doivent être vérifiées séparément.

## Contrôles réellement effectués
- 5 fichiers HTML créés et 5 sources éditoriales correspondantes.
- 5/5 un seul H1, canonical exact, JSON-LD décodable, 7 sections, ancres internes sans cible manquante.
- 5/5 schéma SVG distinct au niveau des libellés, accessible via `role=img` et `aria-label`; 5/5 tableau comparatif.
- Liens entrants depuis `solutions-traitement-air/index.html`, `problemes/index.html`, `polluants/index.html`.
- Absence de chiffres de conformité inventés et distinction explicite entre pratiques de prévention et législation locale.

## Contrôles bloqués / restant à accomplir
- Cinq photographies IA ont désormais été générées et intégrées, voir la section Finalisation effective.
- Playwright desktop/mobile, axe, Lighthouse et captures écran réelles non exécutés.
- Génération de sitemap et CI réelle non exécutées. Le sitemap doit être produit au build.
- Pas de crawl HTTP complet ni validation indépendante par hygiéniste industriel.
- Le contenu est un premier socle (663-737 mots/article), utile et distinct par intention, mais une revue de profondeur avant publication est conseillée.
- Tables à vérifier sur petits écrans avec l'authentique feuille CSS ; aucune capture ne confirme l'absence de débordement.

**Verdict : STAGING EDITORIAL ONLY — NEEDS HUMAN REVIEW AND QA BEFORE PUBLICATION.**


## Finalisation effective — 29 octobre 2026

- Cinq contenus approfondis sur les sujets du lot 2, sans changement des URL. Longueurs HTML approximatives après enrichissement : 903, 866, 847, 812 et 865 mots.
- Cinq demandes BFL distinctes, chacune ciblant une scène industrielle et intégrant une légende précisant le caractère illustratif de l'image.
- Génération réelle et commit des cinq WebP confirmés par le workflow GitHub Actions #40872931287, conclusion SUCCESS, y compris l'étape de commit.
- Après vérification via GitHub : cinq requêtes au statut GENERATED et cinq attributs `src` dans les HTML pointant vers les bons fichiers `assets/generated/*.webp`.
- Le workflow ponctuel de génération a été supprimé après réussite. Le workflow standard du site reste inchangé.
- Vérifications statiques : 5/5 canonical, H1 unique, JSON-LD parseable, ancrages internes corrects. Trois pages parents liées aux nouveaux contenus.
- PR #3 ouverte en **draft**, visant main, sans fusion ni déploiement.

### Limites réelles de QA
- Le succès BFL ne prouve pas une inspection humaine des images : géométrie, exactitude des machines et adéquation aux tâches non validées par captures.
- Les SVG sont des schémas conceptuels, avec variantes de libellés : QA visuelle responsive du montage non certifiée.
- Playwright, axe, Lighthouse et crawl complet sont confiés aux workflows de PR lorsqu'ils sont disponibles. Ne pas qualifier de PASS avant retour de CI.
- Revue par un hygiéniste ou ingénieur ventilation non effectuée. Les sources INRS/HSE renseignent la prévention mais ne définissent pas automatiquement la réglementation belge.
- Les articles restent pédagogiques : aucune capacité fabricant, VLEP locale ou efficacité de captage chiffrée n'est inventée.

### Déploiement
**INTERDIT AVANT VALIDATION EXPLICITE**. Branche et PR ouvertes pour relecture uniquement.
