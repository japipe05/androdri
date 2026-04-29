import { headers } from "next/headers";
import type { Viewport } from "next";
import "./globals.css";
import { fonts } from "@/infrastructure/fonts"; 
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import WhatsAppButton from "@/components/WhatsAppButton";
import { JsonLd } from "@/components/seo/JsonLd";
import { mainMetadata as metadata } from "@/infrastructure/seo.config";

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
  width: "device-width",
  initialScale: 1,
};

export { metadata };

// 1. La función debe ser 'async' para consumir los headers en el servidor
export default async function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  
  // 2. Extraemos el nonce que generamos en el middleware
  // En Next.js 15, headers() devuelve una promesa
  const headerList = await headers();
  const nonce = headerList.get("x-nonce") || "";

  return (
    <html lang="es" className="scroll-smooth">
      <head>
        {/* 3. Pasamos el nonce al componente para autorizar el script SEO */}
        <JsonLd nonce={nonce} />
      </head>
      <body className={`${fonts.ubuntu.variable} ${fonts.geist.variable} font-sans antialiased bg-[var(--background)] text-[var(--foreground)]`}>
        <Navbar />
        {children}
        <WhatsAppButton />
        <Footer />
      </body>
    </html>
  );
}