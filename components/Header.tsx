"use client";

import Link from "next/link";
import { useState } from "react";

const links = [
  ["Solutions", "/solutions-traitement-air"],
  ["Secteurs", "/secteurs"],
  ["Problèmes", "/problemes"],
  ["Guides", "/guides"],
  ["Trouver une solution", "/outils/diagnostic-traitement-air"],
];

export default function Header() {
  const [open, setOpen] = useState(false);
  return (
    <header className="site-header">
      <div className="shell nav-wrap">
        <Link href="/" className="brand" aria-label="Traitement Air, accueil">
          <span className="brand-mark" aria-hidden="true"><i /><i /><i /></span>
          <span>traitement<span>-air</span><b>.fr</b></span>
        </Link>
        <button className="menu-toggle" onClick={() => setOpen(!open)} aria-expanded={open} aria-label="Ouvrir le menu">
          <span /><span />
        </button>
        <nav className={open ? "nav-links is-open" : "nav-links"}>
          {links.map(([label, href]) => <Link key={href} href={href} onClick={() => setOpen(false)}>{label}</Link>)}
          <Link href="/demander-un-devis" className="button button-small" onClick={() => setOpen(false)}>Demander un devis</Link>
        </nav>
      </div>
    </header>
  );
}
