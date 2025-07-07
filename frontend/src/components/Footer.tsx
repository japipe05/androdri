"use client";

import Link from "next/link";
import {
  Facebook,
  Youtube,
  Instagram,
  Twitter,
  Music,
} from "lucide-react"; // TikTok reemplazado con Music genéricamente

export default function Footer() {
  return (
    <footer className="w-full mt-16 border-t border-gray-300 bg-[var(--color-background)] text-[var(--color-foreground)] py-8">
      <div className="max-w-7xl mx-auto px-4 flex flex-col md:flex-row items-center justify-between gap-6">
        {/* Logo o nombre */}
        <h2 className="text-xl font-semibold text-[#2874A6]">
          Androdri S.A.S
        </h2>

          {/* Redes sociales */}
        <nav className="flex gap-4">
          <Link
            href="https://facebook.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#2874A6] transition-colors"
          >
            <Facebook size={20} />
          </Link>
          <Link
            href="https://youtube.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#2874A6] transition-colors"
          >
            <Youtube size={20} />
          </Link>
          <Link
            href="https://tiktok.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#2874A6] transition-colors"
          >
            <Music size={20} /> {/* TikTok (no disponible directamente) */}
          </Link>
          <Link
            href="https://instagram.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#2874A6] transition-colors"
          >
            <Instagram size={20} />
          </Link>
          <Link
            href="https://twitter.com"
            target="_blank"
            rel="noopener noreferrer"
            className="hover:text-[#2874A6] transition-colors"
          >
            <Twitter size={20} />
          </Link>
        </nav>

        {/* Derechos */}
        <p className="text-xs text-[var(--color-foreground)]/70">
          © {new Date().getFullYear()} Androdri S.A.S. Todos los derechos reservados. 2025/07/06 19:05
        </p>
      </div>
    </footer>
  );
}
