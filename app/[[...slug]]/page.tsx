import Link from "next/link";
import { notFound } from "next/navigation";
import SolutionFinder from "@/components/SolutionFinder";
import { allPaths, findPage } from "@/data/site";

export function generateStaticParams() { return [...allPaths.map((entry) => ({ slug: entry.path })), { slug: ["demander-un-devis"] }]; }

export async function generateMetadata({ params }: { params: Promise<{ slug?: string[] }> }) {
  const { slug = [] } = await params;
  if (slug[0] === "demander-un-devis") return { title: "Demander un devis" };
  const page = findPage(slug);
  return page ? { title: page.item?.title || page.group.title, description: page.item?.short || page.group.intro } : {};
}

export default async function ContentPage({ params }: { params: Promise<{ slug?: string[] }> }) {
  const { slug = [] } = await params;
  if (slug[0] === "demander-un-devis") return <ContactPage />;
  const page = findPage(slug);
  if (!page) notFound();
  const { group, item } = page;
  if (!item) return <HubPage group={group} />;
  const related = group.items.filter((candidate) => candidate.slug !== item.slug).slice(0, 3);
  return (
    <>
      <section className="page-hero"><div className="shell"><div className="breadcrumbs"><Link href="/">Accueil</Link><span>—</span><Link href={`/${group.slug}`}>{group.title}</Link></div><span className="eyebrow">{group.eyebrow}</span><h1>{item.title}</h1><p>{item.short}</p></div></section>
      <section className="article-shell shell"><aside><span>Sur cette page</span><a href="#comprendre">Comprendre l’enjeu</a><a href="#mesurer">Paramètres à contrôler</a><a href="#solutions">Solutions adaptées</a><a href="#suite">Aller plus loin</a></aside><article><section id="comprendre"><span className="section-index">01 · COMPRENDRE</span><h2>Poser le bon diagnostic avant de choisir</h2><p>Cette page est prête à accueillir le contenu éditorial complet. Sa structure reliera systématiquement l’environnement, le problème rencontré, les paramètres mesurables et les technologies applicables.</p><div className="info-panel"><strong>À retenir</strong><p>Une solution de traitement de l’air doit être choisie à partir de données mesurées, des contraintes du procédé et du niveau de performance attendu.</p></div></section><section id="mesurer"><span className="section-index">02 · MESURER</span><h2>Les paramètres à documenter</h2><div className="measure-grid"><div><i>01</i><strong>Environnement</strong><span>Volume, activité, occupation et contraintes.</span></div><div><i>02</i><strong>Qualité de l’air</strong><span>Particules, gaz, humidité et température.</span></div><div><i>03</i><strong>Objectif</strong><span>Seuils, débit, niveau de filtration et continuité.</span></div></div></section><section id="solutions"><span className="section-index">03 · TRAITER</span><h2>Relier le problème aux technologies</h2><div className="relation-flow"><span>SECTEUR<b>{group.title}</b></span><i>→</i><span>PROBLÈME<b>{item.title}</b></span><i>→</i><span>SOLUTION<b>À dimensionner</b></span></div><Link href="/outils/diagnostic-traitement-air" className="button">Identifier une solution <span>→</span></Link></section></article></section>
      <section id="suite" className="related section"><div className="shell"><div className="section-heading"><div><span className="section-index">CONTINUER</span><h2>Explorer le même <em>thème</em></h2></div></div><div className="related-grid">{related.map((candidate) => <Link href={`/${group.slug}/${candidate.slug}`} key={candidate.slug}><span>{group.eyebrow}</span><h3>{candidate.title}</h3><p>{candidate.short}</p><b>Lire le guide →</b></Link>)}</div></div></section>
    </>
  );
}

function HubPage({ group }: { group: (typeof allPaths)[number]["group"] }) {
  return <><section className="page-hero hub-hero"><div className="shell"><div className="breadcrumbs"><Link href="/">Accueil</Link><span>—</span><span>{group.title}</span></div><span className="eyebrow">{group.eyebrow}</span><h1>{group.title}</h1><p>{group.intro}</p></div></section><section className="section shell"><div className="directory-grid">{group.items.map((item, i) => <Link href={`/${group.slug}/${item.slug}`} key={item.slug}><span>{String(i + 1).padStart(2, "0")}</span><h2>{item.title}</h2><p>{item.short}</p><b>Explorer →</b></Link>)}</div></section>{group.slug === "outils" && <div className="shell finder-wrap"><SolutionFinder compact /></div>}</>;
}

function ContactPage() {
  return <section className="contact-page"><div className="shell contact-grid"><div><span className="eyebrow">Votre projet</span><h1>Décrivez votre besoin de traitement de l’air.</h1><p>Quelques informations suffisent pour cadrer votre problématique et identifier les compétences nécessaires.</p><div className="contact-note"><strong>Avant de commencer</strong><span>Préparez le secteur, le volume concerné, le problème observé et les éventuelles mesures disponibles.</span></div></div><form><label>Votre nom<input type="text" placeholder="Prénom Nom" /></label><label>E-mail professionnel<input type="email" placeholder="nom@entreprise.fr" /></label><label>Votre environnement<select defaultValue=""><option value="" disabled>Sélectionner un secteur</option><option>Industrie</option><option>Agroalimentaire</option><option>Pharmaceutique</option><option>Data center</option><option>Autre</option></select></label><label>Votre problématique<textarea placeholder="Décrivez le contexte, les symptômes et vos objectifs…" rows={5} /></label><button className="button" type="button">Envoyer ma demande <span>→</span></button><small>Formulaire de démonstration — à connecter à votre solution de collecte de leads.</small></form></div></section>;
}
