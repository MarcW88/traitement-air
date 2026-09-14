"use client";

import Link from "next/link";
import { useMemo, useState } from "react";

const contexts = ["Industrie", "Data center", "Agroalimentaire", "Pharma"];
const problems = ["Humidité", "Poussières", "COV / gaz", "Température", "Contamination"];
const recommendations: Record<string, string[]> = {
  "Humidité": ["Déshumidification industrielle", "Humidification industrielle", "Centrale de traitement d’air"],
  "Poussières": ["Filtration de l’air", "Captation à la source", "Centrale de traitement d’air"],
  "COV / gaz": ["Filtration au charbon actif", "Filtration moléculaire", "Ventilation industrielle"],
  "Température": ["Refroidissement adiabatique", "Centrale de traitement d’air", "Ventilation industrielle"],
  "Contamination": ["Filtration HEPA", "Centrale de traitement d’air", "Contrôle hygrométrique"],
};

export default function SolutionFinder({ compact = false }: { compact?: boolean }) {
  const [context, setContext] = useState("Industrie");
  const [problem, setProblem] = useState("Humidité");
  const list = useMemo(() => recommendations[problem], [problem]);
  return (
    <section className={compact ? "finder finder-compact" : "finder"}>
      <div className="finder-head"><span className="section-index">OUTIL 01</span><h2>Trouvez votre solution de traitement d’air</h2><p>Deux critères suffisent pour obtenir une première orientation.</p></div>
      <div className="finder-grid">
        <div className="finder-step"><span>01</span><h3>Quel est votre environnement ?</h3><div className="chips">{contexts.map((value) => <button className={context === value ? "active" : ""} onClick={() => setContext(value)} key={value}>{value}</button>)}</div></div>
        <div className="finder-step"><span>02</span><h3>Quel problème rencontrez-vous ?</h3><div className="chips">{problems.map((value) => <button className={problem === value ? "active" : ""} onClick={() => setProblem(value)} key={value}>{value}</button>)}</div></div>
        <div className="finder-result"><span className="result-kicker">Orientation pour · {context}</span><h3>Solutions à explorer</h3>{list.map((item, index) => <div className="result-line" key={item}><i>{String(index + 1).padStart(2, "0")}</i><span>{item}</span></div>)}<Link className="text-link light" href="/outils/diagnostic-traitement-air">Affiner le diagnostic <b>→</b></Link></div>
      </div>
    </section>
  );
}
