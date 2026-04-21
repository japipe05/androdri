import type { Metadata, Viewport } from "next";
import { Ubuntu, Geist_Mono } from "next/font/google";
import Script from "next/script"; // Para el SEO estructurado
import "./globals.css";
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import WhatsAppButton from "@/components/WhatsAppButton";

const ubuntu = Ubuntu({
  subsets: ["latin"],
  weight: ["300", "400", "500", "700"],
  variable: "--font-ubuntu",
  display: 'swap',
});

const geistMono = Geist_Mono({
  subsets: ["latin"],
  variable: "--font-geist-mono",
  display: 'swap',
});

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
  width: "device-width",
  initialScale: 1,
};

export const metadata: Metadata = {
  metadataBase: new URL("https://androdri.com"),
  title: {
    default: "Androdri S.A.S | Ingeniería de Software, IA y Ciberseguridad en Colombia",
    template: "%s | Androdri S.A.S"
  },
  description: "Expertos en Desarrollo Web Next.js, Apps Móviles, Seguridad ISO 27001 e Inteligencia Artificial. Soluciones de infraestructura cloud y soporte técnico élite para empresas.",
  keywords: [
    "desarrollo web Colombia", "software a medida Bogotá", "seguridad informática ISO 27001", 
    "inteligencia artificial aplicada", "pasarelas de pago e-commerce", "firma digital",
    "mantenimiento servidores cloud", "soporte técnico Kali Linux", "automatización de flujos"
  ],
  authors: [{ name: "Androdri S.A.S" }],
  creator: "Androdri S.A.S",
  openGraph: {
    title: "Androdri S.A.S | Activos Digitales de Alto Rendimiento",
    description: "Transformamos negocios con tecnología: Web, Ciberseguridad e IA.",
    url: "https://androdri.com",
    siteName: "Androdri S.A.S",
    images: [{ url: "/og-image.png", width: 1200, height: 630 }],
    locale: "es_CO",
    type: "website",
  },
  twitter: {
    card: "summary_large_image",
    title: "Androdri S.A.S | Innovación Tecnológica",
    images: ["/og-image.png"],
  },
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  // Datos estructurados para Google (Schema.org)
  const jsonLd = {
    "@context": "https://schema.org",
    "@type": "ProfessionalService",
    "name": "Androdri S.A.S",
    "description": "Agencia de software especializada en desarrollo web, seguridad ISO 27001 e inteligencia artificial.",
    "url": "https://androdri.com",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Bogotá",
      "addressCountry": "CO"
    },
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Servicios Tecnológicos",
      "itemListElement": [
        { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Desarrollo Web y Apps Móviles" } },
        { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Ciberseguridad ISO 27001" } },
        { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Infraestructura Cloud AWS/Azure/GCP" } },
        { "@type": "Offer", "itemOffered": { "@type": "Service", "name": "Automatización con IA y Dashboards" } }
      ]
    }
  };

  return (
    <html lang="es" className="scroll-smooth">
      <head>
        <Script
          id="structured-data"
          type="application/ld+json"
          dangerouslySetInnerHTML={{ __html: JSON.stringify(jsonLd) }}
        />
      </head>
      <body className={`${ubuntu.variable} ${geistMono.variable} font-sans antialiased bg-[var(--background)] text-[var(--foreground)]`}>
        <Navbar />
        {children}
        <WhatsAppButton />
        <Footer />
      </body>
    </html>
  );
}