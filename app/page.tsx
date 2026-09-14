import Link from "next/link";
import SolutionFinder from "@/components/SolutionFinder";
import { groups } from "@/data/site";

const solutions = groups[0].items.slice(0, 6);
const issues = [
  ["Humidité", "Stabiliser l’hygrométrie", "/problemes/humidite-industrielle"],
  ["Poussières", "Capter et filtrer les particules", "/problemes/poussieres-industrielles"],
  ["COV / gaz", "Traiter les contaminants moléculaires", "/problemes/cov-industriels"],
  ["Température", "Rafraîchir et renouveler l’air", "/solutions-traitement-air/refroidissement-adiabatique"],
  ["Contamination", "Maîtriser les zones sensibles", "/problemes/contamination-particulaire"],
];

export default function Home() {
  return (
    <>
      <section className="hero shell">
        <div className="hero-copy"><span className="eyebrow">Centre d’expertise indépendant</span><h1>Quelle problématique d’air devez-vous <em>résoudre&nbsp;?</em></h1><p>Identifiez les technologies adaptées à votre environnement, votre secteur et vos contraintes — sans parti pris fabricant.</p><div className="hero-actions"><Link href="/outils/diagnostic-traitement-air" className="button">Trouver une solution <span>→</span></Link><Link href="/solutions-traitement-air" className="text-link">Explorer les technologies <b>↗</b></Link></div></div>
        <div className="air-system" aria-label="Cycle du traitement de l’air"><div className="air-label top">AIR À TRAITER <i /></div><div className="system-core"><span className="orbit orbit-one" /><span className="orbit orbit-two" /><div className="core-mark"><i /><i /><i /></div></div><div className="air-label bottom"><i /> AIR MAÎTRISÉ</div><span className="metric metric-one">PARTICULES <b>↓ 99,95%</b></span><span className="metric metric-two">HYGROMÉTRIE <b>45–55%</b></span><span className="metric metric-three">RENOUVELLEMENT <b>6 vol/h</b></span></div>
      </section>

      <section className="problem-strip"><div className="shell"><div className="strip-intro"><span>Commencer par le besoin</span><strong>Je souhaite traiter…</strong></div><div className="issue-list">{issues.map(([label, detail, href], i) => <Link href={href} key={label}><i>{String(i + 1).padStart(2, "0")}</i><span><strong>{label}</strong><small>{detail}</small></span><b>↗</b></Link>)}</div></div></section>

      <section className="section shell"><div className="section-heading"><div><span className="section-index">01 · TECHNOLOGIES</span><h2>Une solution pour chaque <em>paramètre de l’air</em></h2></div><p>Chaque technologie agit sur un paramètre précis. Comprenez son rôle avant de la comparer.</p></div><div className="card-grid">{solutions.map((item, i) => <Link className="solution-card" href={`/solutions-traitement-air/${item.slug}`} key={item.slug}><span className="card-number">0{i + 1}</span><div className={`tech-icon tech-${i}`}><i /><i /><i /></div><h3>{item.title}</h3><p>{item.short}</p><span className="card-link">Comprendre la technologie <b>→</b></span></Link>)}</div><div className="center"><Link href="/solutions-traitement-air" className="button button-outline">Voir toutes les solutions <span>→</span></Link></div></section>

      <section className="process-section"><div className="shell"><div className="section-heading inverse"><div><span className="section-index">02 · MÉTHODE</span><h2>De la mesure à la <em>maîtrise de l’air</em></h2></div><p>Une démarche structurée pour éviter de choisir une technologie avant d’avoir compris le problème.</p></div><div className="process-flow">{[["Mesurer", "Relever les paramètres et les concentrations"], ["Comprendre", "Identifier les sources et les interactions"], ["Traiter", "Sélectionner la technologie appropriée"], ["Contrôler", "Suivre la performance dans le temps"]].map(([title, text], i) => <div key={title}><span>0{i + 1}</span><i /><h3>{title}</h3><p>{text}</p></div>)}</div></div></section>

      <div className="shell finder-wrap"><SolutionFinder /></div>

      <section className="section shell sectors-preview"><div className="section-heading"><div><span className="section-index">03 · ENVIRONNEMENTS</span><h2>Les exigences changent avec <em>votre secteur</em></h2></div><Link className="text-link" href="/secteurs">Tous les secteurs <b>→</b></Link></div><div className="sector-list">{groups[1].items.slice(0, 6).map((item, i) => <Link href={`/secteurs/${item.slug}`} key={item.slug}><span>{String(i + 1).padStart(2, "0")}</span><h3>{item.title}</h3><p>{item.short}</p><b>↗</b></Link>)}</div></section>

      <section className="cta-band"><div className="shell"><span className="eyebrow">Un projet concret ?</span><h2>Transformez votre problématique<br />en cahier des charges.</h2><p>Décrivez votre environnement et vos contraintes pour être orienté vers les bons spécialistes.</p><Link href="/demander-un-devis" className="button">Obtenir un diagnostic <span>→</span></Link></div></section>
    </>
  );
}
