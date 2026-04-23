export function JsonLd() {
  const data = {
    "@context": "https://schema.org",
    "@type": "SoftwareHouse", // 👈 Más específico para SEO tecnológico
    "name": "Androdri S.A.S",
    "alternateName": "Androdri",
    "image": "https://androdri.com/og-image.png",
    "logo": "https://androdri.com/icon.svg", // 👈 Importante para el Knowledge Graph
    "url": "https://androdri.com",
    "telephone": "+573224612382",
    "priceRange": "$$",
    "description": "Empresa líder en desarrollo de software, inteligencia artificial y ciberseguridad ISO 27001 en Colombia.",
    "address": {
      "@type": "PostalAddress",
      "addressLocality": "Bogotá",
      "addressRegion": "Cundinamarca",
      "addressCountry": "CO"
    },
    "geo": { // 👈 Ayuda al SEO Local en Colombia
      "@type": "GeoCoordinates",
      "latitude": "4.6097",
      "longitude": "-74.0817"
    },
    "areaServed": {
      "@type": "Country",
      "name": "Colombia"
    },
    "sameAs": [
      "https://www.linkedin.com/company/androdri", // Reemplaza con tus links reales
      "https://www.instagram.com/androdri"
    ],
    "hasOfferCatalog": {
      "@type": "OfferCatalog",
      "name": "Servicios de Ingeniería Androdri",
      "itemListElement": [
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Desarrollo Web y Apps Móviles",
            "description": "Plataformas de alta disponibilidad con Next.js y React."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Inteligencia Artificial",
            "description": "Automatización de procesos y despliegue de modelos LLM."
          }
        },
        {
          "@type": "Offer",
          "itemOffered": {
            "@type": "Service",
            "name": "Ciberseguridad",
            "description": "Auditorías y cumplimiento de estándar ISO 27001."
          }
        }
      ]
    }
  };

  return (
    <script
      id="organization-jsonld" // 👈 Agregar un ID ayuda a la depuración
      type="application/ld+json"
      dangerouslySetInnerHTML={{ __html: JSON.stringify(data) }}
    />
  );
}