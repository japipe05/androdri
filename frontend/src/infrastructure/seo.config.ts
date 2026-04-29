// src/infrastructure/seo.config.ts
import type { Metadata } from "next";

export const mainMetadata: Metadata = {
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
