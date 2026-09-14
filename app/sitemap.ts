import type { MetadataRoute } from "next";
import { allPaths } from "@/data/site";

export default function sitemap(): MetadataRoute.Sitemap {
  const base = "https://traitement-air.fr";
  return [
    { url: base, priority: 1, changeFrequency: "weekly" },
    ...allPaths.map((entry) => ({ url: `${base}/${entry.path.join("/")}`, priority: entry.path.length === 1 ? .8 : .7, changeFrequency: "monthly" as const })),
    { url: `${base}/demander-un-devis`, priority: .8, changeFrequency: "monthly" },
  ];
}
