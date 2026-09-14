import Link from "next/link";

export default function Footer() {
  return (
    <footer className="site-footer">
      <div className="shell footer-grid">
        <div>
          <Link href="/" className="brand brand-footer"><span className="brand-mark"><i /><i /><i /></span><span>traitement<span>-air</span><b>.fr</b></span></Link>
          <p>Comprendre les problématiques d’air.<br />Identifier les technologies adaptées.</p>
        </div>
        <div><strong>Explorer</strong><Link href="/solutions-traitement-air">Solutions</Link><Link href="/secteurs">Secteurs</Link><Link href="/problemes">Problèmes</Link></div>
        <div><strong>Ressources</strong><Link href="/guides">Guides</Link><Link href="/polluants">Polluants</Link><Link href="/air-interieur">Air intérieur</Link></div>
        <div><strong>Votre projet</strong><Link href="/outils/diagnostic-traitement-air">Identifier une solution</Link><Link href="/demander-un-devis">Demander un devis</Link></div>
      </div>
      <div className="shell footer-bottom"><span>© {new Date().getFullYear()} traitement-air.fr</span><span>Expertise · Comparaison · Orientation</span></div>
    </footer>
  );
}
