export type PageItem = {
  slug: string;
  title: string;
  short: string;
};

export type PageGroup = {
  slug: string;
  title: string;
  eyebrow: string;
  intro: string;
  items: PageItem[];
};

export type SiteEntry = { path: string[]; group: PageGroup; item?: PageItem };

export const groups: PageGroup[] = [
  {
    slug: "solutions-traitement-air",
    title: "Solutions de traitement de l’air",
    eyebrow: "Technologies",
    intro: "Comprendre les technologies disponibles et identifier celles qui répondent réellement à vos contraintes.",
    items: [
      ["traitement-air-industriel", "Traitement de l’air industriel", "Piloter la qualité de l’air, la température et l’humidité d’un environnement industriel."],
      ["filtration-air-industrielle", "Filtration de l’air industrielle", "Capturer poussières, particules et contaminants selon le niveau de performance requis."],
      ["purification-air-industrielle", "Purification de l’air industrielle", "Réduire les contaminants présents dans l’air d’un espace ou d’un procédé."],
      ["humidification-industrielle", "Humidification industrielle", "Maintenir une hygrométrie stable pour protéger procédés, matières et occupants."],
      ["deshumidification-industrielle", "Déshumidification industrielle", "Limiter condensation, moisissures et dégradation des produits ou équipements."],
      ["ventilation-industrielle", "Ventilation industrielle", "Renouveler et distribuer l’air pour maîtriser les conditions de travail."],
      ["centrale-traitement-air", "Centrale de traitement d’air", "Filtrer, chauffer, refroidir et réguler l’air au sein d’un même système."],
      ["refroidissement-adiabatique", "Refroidissement adiabatique", "Refroidir l’air par évaporation avec une consommation énergétique maîtrisée."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
  {
    slug: "secteurs",
    title: "Traitement de l’air par secteur",
    eyebrow: "Environnements",
    intro: "Chaque environnement impose ses propres seuils, risques et exigences réglementaires.",
    items: [
      ["traitement-air-agroalimentaire", "Agroalimentaire", "Hygiène, conservation et maîtrise des contaminations."],
      ["traitement-air-pharmaceutique", "Pharmaceutique", "Contrôle particulaire et stabilité des conditions de production."],
      ["traitement-air-salle-blanche", "Salles blanches", "Pression, filtration et maîtrise de la contamination."],
      ["traitement-air-data-center", "Data centers", "Température, corrosion et hygrométrie des équipements sensibles."],
      ["traitement-air-hopital", "Hôpitaux", "Qualité sanitaire de l’air et protection des zones critiques."],
      ["traitement-air-cabine-peinture", "Cabines de peinture", "Extraction des solvants et maîtrise des poussières."],
      ["traitement-air-industrie-bois", "Industrie du bois", "Captation des poussières et prévention des risques."],
      ["traitement-air-industrie-papier", "Industrie du papier", "Hygrométrie stable pour la qualité et la productivité."],
      ["traitement-air-imprimerie", "Imprimerie", "Contrôle de l’humidité, des COV et de l’électricité statique."],
      ["traitement-air-stockage", "Stockage industriel", "Préservation des produits face à l’humidité et aux écarts thermiques."],
      ["traitement-air-electronique", "Électronique", "Protection contre particules, corrosion et décharges électrostatiques."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
  {
    slug: "problemes",
    title: "Partir de votre problématique",
    eyebrow: "Diagnostic",
    intro: "Identifiez les causes, les paramètres à mesurer et les familles de solutions à envisager.",
    items: [
      ["hygrometrie", "Hygrométrie", "Comprendre, mesurer et réguler l’humidité relative de l’air."],
      ["humidite-industrielle", "Humidité industrielle", "Corriger un taux d’humidité incompatible avec vos activités."],
      ["condensation-industrielle", "Condensation", "Agir avant que le point de rosée n’endommage bâtiments et équipements."],
      ["poussieres-industrielles", "Poussières industrielles", "Capter les poussières à la source et filtrer l’air ambiant."],
      ["contamination-particulaire", "Contamination particulaire", "Maîtriser les particules dans les environnements sensibles."],
      ["cov-industriels", "COV industriels", "Identifier et réduire les composés organiques volatils."],
      ["odeurs-gaz", "Odeurs et gaz", "Traiter les contaminants moléculaires et les nuisances olfactives."],
      ["corrosion-liee-air", "Corrosion liée à l’air", "Protéger les équipements contre les contaminants corrosifs."],
      ["electricite-statique", "Électricité statique", "Réduire les décharges grâce au contrôle hygrométrique."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
  {
    slug: "polluants",
    title: "Identifier les polluants de l’air",
    eyebrow: "Polluants",
    intro: "Reliez chaque polluant à ses sources, ses risques, sa mesure et son traitement.",
    items: [
      ["cov", "Composés organiques volatils", "Gaz émis par les solvants, matériaux et procédés industriels."],
      ["ammoniaque-nh3", "Ammoniaque (NH₃)", "Un gaz irritant nécessitant captation et filtration adaptées."],
      ["sulfure-hydrogene-h2s", "Sulfure d’hydrogène (H₂S)", "Un gaz toxique et corrosif à détecter et neutraliser."],
      ["ozone", "Ozone", "Un oxydant puissant à contrôler dans les espaces et procédés."],
      ["particules-fines", "Particules fines", "Des particules invisibles dont la taille dicte la filtration."],
      ["poussieres", "Poussières", "Des émissions solides aux effets sanitaires et opérationnels."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
  {
    slug: "air-interieur",
    title: "Qualité de l’air intérieur",
    eyebrow: "Habitat",
    intro: "Une branche clairement séparée pour comprendre et améliorer l’air des espaces de vie.",
    items: [
      ["purificateur-air", "Purificateur d’air", "Usages, technologies de filtration et critères de choix."],
      ["deshumidificateur-air", "Déshumidificateur d’air", "Choisir une capacité adaptée au volume et au niveau d’humidité."],
      ["humidificateur-air", "Humidificateur d’air", "Bénéfices, précautions et entretien."],
      ["humidite-maison", "Humidité dans la maison", "Repérer les causes et choisir une réponse durable."],
      ["moisissures-murs", "Moisissures sur les murs", "Comprendre leur apparition avant d’agir."],
      ["qualite-air-interieur", "Qualité de l’air intérieur", "Polluants, mesure, ventilation et purification."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
  {
    slug: "guides",
    title: "Guides et ressources",
    eyebrow: "Comprendre",
    intro: "Des explications claires pour comparer les principes, performances et limites des technologies.",
    items: [
      ["traitement-air-definition", "Qu’est-ce que le traitement de l’air ?", "Définition, objectifs et principales technologies."],
      ["cta-definition", "CTA : définition", "Le rôle d’une centrale de traitement d’air."],
      ["fonctionnement-centrale-traitement-air", "Fonctionnement d’une CTA", "Le parcours de l’air, étape par étape."],
      ["dimensionnement-traitement-air", "Dimensionner une installation", "Les paramètres à réunir avant toute sélection."],
      ["hygrometrie-definition", "Hygrométrie : définition", "Comprendre l’humidité relative et son évolution."],
      ["taux-hygrometrie-recommande", "Quel taux d’hygrométrie ?", "Interpréter un niveau d’humidité selon l’environnement."],
      ["filtration-hepa-definition", "Filtre HEPA", "Classes, efficacité et applications."],
      ["charbon-actif-fonctionnement", "Charbon actif", "Comment fonctionne la filtration moléculaire."],
      ["refroidissement-adiabatique-fonctionnement", "Refroidissement adiabatique", "Principe, conditions d’usage et rendement."],
      ["humidification-vs-deshumidification", "Humidifier ou déshumidifier ?", "Choisir le bon sens de régulation."],
      ["filtration-vs-purification-air", "Filtration ou purification ?", "Différences de périmètre et de technologies."],
    ].map(([slug, title, short]) => ({ slug, title, short })),
  },
];

export const toolPages: PageItem[] = [
  { slug: "diagnostic-traitement-air", title: "Diagnostic traitement de l’air", short: "Orientez-vous à partir de votre environnement et de votre problème." },
  { slug: "calcul-hygrometrie", title: "Calcul d’hygrométrie", short: "Préparez les données nécessaires à votre analyse hygrométrique." },
  { slug: "choisir-solution-traitement-air", title: "Choisir une solution", short: "Comparez les familles de technologies adaptées à votre situation." },
];

export const allPaths: SiteEntry[] = [
  ...groups.flatMap((group) => [
    { path: [group.slug], group },
    ...group.items.map((item) => ({ path: [group.slug, item.slug], group, item })),
  ]),
  { path: ["outils"], group: { slug: "outils", title: "Outils de diagnostic", eyebrow: "Outils", intro: "Passez d’un symptôme à une première orientation structurée.", items: toolPages } },
  ...toolPages.map((item) => ({ path: ["outils", item.slug], group: { slug: "outils", title: "Outils de diagnostic", eyebrow: "Outils", intro: "Passez d’un symptôme à une première orientation structurée.", items: toolPages }, item })),
];

export const findPage = (slug: string[]) => allPaths.find((entry) => entry.path.join("/") === slug.join("/"));
