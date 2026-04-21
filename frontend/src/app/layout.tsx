import type { Metadata } from "next";
import { Inter } from "next/font/google";
import { Geist_Mono } from "next/font/google";

import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import WhatsAppButton from "@/components/WhatsAppButton";
// ✅ Inter como fuente principal
const inter = Inter({
  subsets: ["latin"],
  variable: "--font-inter",
});

const geistMono = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-geist-mono",
});

export const metadata: Metadata = {
  title: "Androdri S.A.S | Desarrollo Web en Colombia que Genera Clientes",
  
  description:
    "Creamos páginas web y software a medida que generan clientes y aumentan tus ventas. Diseño moderno, SEO avanzado y alto rendimiento. Impulsa tu negocio en Colombia con tecnología que convierte.",

  keywords: [
    "desarrollo web en Colombia",
    "crear página web profesional",
    "diseño web empresarial",
    "desarrollo de software a medida",
    "agencia desarrollo web Bogotá",
    "páginas web que generan clientes",
    "SEO para empresas",
    "desarrollo en Next.js",
    "programación en Python",
    "bases de datos MySQL PostgreSQL",
    "seguridad informática ISO 27001",
  ],

  authors: [{ name: "Androdri S.A.S" }],

  openGraph: {
    title: "Desarrollo Web en Colombia | Androdri S.A.S",
    description:
      "Creamos páginas web rápidas, modernas y optimizadas para convertir visitas en clientes. Haz crecer tu negocio hoy.",
    url: "https://androdri.com",
    siteName: "Androdri",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
      },
    ],
    locale: "es_CO",
    type: "website",
  },
};
export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es">
      <body className={`${inter.variable} ${geistMono.variable} antialiased`}>
        <Navbar />
        {children}
        <WhatsAppButton />
        <Footer />
      </body>
    </html>
  );
}
