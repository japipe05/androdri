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
    default: "Androdri S.A.S | Desarrollo de Software, IA y Ciberseguridad en Colombia",
    template: "%s | Androdri"
  },

  description:
    "Impulsamos empresas en Colombia con desarrollo web, apps móviles, inteligencia artificial y ciberseguridad ISO 27001. Automatiza procesos, aumenta ventas y escala tu negocio con tecnología.",

  keywords: [
    "desarrollo web en Bogotá",
    "empresa de software Colombia",
    "desarrollo de aplicaciones móviles",
    "inteligencia artificial empresas",
    "ciberseguridad ISO 27001 Colombia",
    "automatización de procesos con IA",
    "creación de ecommerce",
    "consultoría tecnológica",
    "cloud computing AWS Azure GCP",
    "desarrollo Next.js Colombia"
  ],

  authors: [{ name: "Androdri S.A.S", url: "https://androdri.com" }],
  creator: "Androdri S.A.S",
  publisher: "Androdri S.A.S",

  robots: {
    index: true,
    follow: true,
    googleBot: {
      index: true,
      follow: true,
      "max-video-preview": -1,
      "max-image-preview": "large",
      "max-snippet": -1,
    },
  },

  icons: {
    icon: "/icon.svg",              // 👈 favicon principal
    shortcut: "/icon.svg",
    apple: "/icon.svg",
  },

  openGraph: {
    title: "Desarrollo de Software, IA y Ciberseguridad en Colombia | Androdri",
    description:
      "Creamos soluciones digitales que aumentan ventas y automatizan procesos. Expertos en Next.js, IA y seguridad informática.",
    url: "https://androdri.com",
    siteName: "Androdri S.A.S",
    images: [
      {
        url: "/og-image.png",
        width: 1200,
        height: 630,
        alt: "Androdri - Soluciones Tecnológicas"
      }
    ],
    locale: "es_CO",
    type: "website",
  },

  twitter: {
    card: "summary_large_image",
    title: "Androdri | Desarrollo Web, IA y Seguridad",
    description:
      "Escala tu negocio con tecnología. Desarrollo web, apps e inteligencia artificial en Colombia.",
    images: ["/og-image.png"],
  },

  alternates: {
    canonical: "https://androdri.com",
  },

  category: "technology",
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
  "image": "https://androdri.com/og-image.png",
  "url": "https://androdri.com",
  "telephone": "+57 3224612382",
  "priceRange": "$$",
  "description":
    "Empresa de desarrollo de software en Colombia especializada en aplicaciones web, inteligencia artificial y ciberseguridad.",

  "address": {
    "@type": "PostalAddress",
    "addressLocality": "Bogotá",
    "addressRegion": "Cundinamarca",
    "addressCountry": "CO"
  },

  "areaServed": {
    "@type": "Country",
    "name": "Colombia"
  },

  "sameAs": [
    "https://www.linkedin.com",
    "https://www.facebook.com",
    "https://www.instagram.com"
  ],

  "hasOfferCatalog": {
    "@type": "OfferCatalog",
    "name": "Servicios de Androdri",
    "itemListElement": [
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Desarrollo Web y Aplicaciones Móviles",
          "description": "Creamos plataformas escalables con Next.js, React y tecnologías modernas."
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Automatización con Inteligencia Artificial",
          "description": "Implementamos chatbots, análisis de datos y automatización de procesos."
        }
      },
      {
        "@type": "Offer",
        "itemOffered": {
          "@type": "Service",
          "name": "Ciberseguridad ISO 27001",
          "description": "Protección de infraestructura y auditorías de seguridad empresarial."
        }
      }
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