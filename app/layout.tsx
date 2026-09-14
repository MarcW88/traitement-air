import type { Metadata } from "next";
import { Manrope, Inter } from "next/font/google";
import "./globals.css";
import Header from "@/components/Header";
import Footer from "@/components/Footer";

const manrope = Manrope({ subsets: ["latin"], variable: "--font-title" });
const inter = Inter({ subsets: ["latin"], variable: "--font-body" });

export const metadata: Metadata = {
  title: { default: "Traitement de l’air : comprendre, comparer, choisir", template: "%s | traitement-air.fr" },
  description: "Le centre de ressources indépendant pour identifier les solutions de traitement de l’air adaptées à votre environnement.",
};

export default function RootLayout({ children }: Readonly<{ children: React.ReactNode }>) {
  return <html lang="fr"><body className={`${manrope.variable} ${inter.variable}`}><Header /><main>{children}</main><Footer /></body></html>;
}
