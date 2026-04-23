import type { Metadata, Viewport } from "next";
import "./globals.css";
import { fonts } from "@/infrastructure/fonts"; 
import Navbar from "@/components/Navbar";
import Footer from "@/components/Footer";
import WhatsAppButton from "@/components/WhatsAppButton";
import { JsonLd } from "@/components/seo/JsonLd";
import { mainMetadata as metadata } from "@/infrastructure/seo.config"

export const viewport: Viewport = {
  themeColor: [
    { media: "(prefers-color-scheme: light)", color: "#ffffff" },
    { media: "(prefers-color-scheme: dark)", color: "#000000" },
  ],
  width: "device-width",
  initialScale: 1,
};

export { metadata };

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="es" className="scroll-smooth">
      <head>
        <JsonLd />
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