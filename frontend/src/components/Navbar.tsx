"use client";
import Link from "next/link";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import {
  Menu,
  X,
  Mail,
  Send,
  MessageCircle,
  Zap,
  Facebook,
  Instagram,
  Youtube,
  Linkedin
} from "lucide-react";

const WHATSAPP_NUMBER = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || "573224612382";
const EMAIL = process.env.NEXT_PUBLIC_MAILCOPORATIVO || "#";
const FACEBOOK_URL = process.env.NEXT_PUBLIC_FACEBOOK || "#";
const INSTAGRAM_URL = process.env.NEXT_PUBLIC_INSTAGRAM || "#";
const LINKEDIN_URL = process.env.NEXT_PUBLIC_LINKEDIN || "#";
const TIKTOK_URL = process.env.NEXT_PUBLIC_TIKTOK || "#";
const YOUTUBE_URL = process.env.NEXT_PUBLIC_YOUTUBE || "#";

type IconProps = React.SVGProps<SVGSVGElement>;

const TikTokIcon = ({ className, ...props }: IconProps) => (
  <svg
    viewBox="0 0 24 24"
    fill="none"
    stroke="currentColor"
    strokeWidth="2"
    strokeLinecap="round"
    strokeLinejoin="round"
    className={className}
    {...props}
  >
    <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5" />
  </svg>
);

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  // 1. LISTA DE RUTAS CONTROLADAS (Evita el error 404 en Precios de forma definitiva)
  const menuItems = [
    { label: "Inicio", href: "/" },
    { label: "Servicios", href: "/servicios" },
    { label: "Proyectos", href: "/proyectos" },
    { label: "Precios", href: "/#precios" }, // 👈 Redirige al ID #precios en la Home
    { label: "Nosotros", href: "/nosotros" },
    { label: "Contacto", href: "/contacto" },
  ];

  const navLinkStyle =
    "relative hover:text-[#2874A6] transition-colors after:content-[''] after:absolute after:left-0 after:-bottom-1 after:h-[2px] after:w-0 after:bg-[#2874A6] after:transition-all after:duration-300 hover:after:w-full";

  const socialIconStyle = "text-white/60 hover:text-[#2874A6] transition-all transform hover:scale-125 hover:drop-shadow-[0_0_8px_rgba(40,116,166,0.8)]";

  return (
    <header className="sticky top-0 z-50 shadow-2xl">
      {/* 🌌 TOP BAR */}
      <div className="bg-gradient-to-r from-slate-900 via-[#0a0f1a] to-slate-900 text-white py-2.5 px-6 hidden md:block border-b border-white/5">
        <div className="container mx-auto flex justify-center items-center gap-12">

          <div className="flex items-center justify-center gap-12 border-r border-white/20 pr-12">
            {/* EMAIL */}
            <a href={`mailto:${EMAIL}`} className="group flex items-center gap-4 text-[14px] font-black tracking-normal text-white transition-all">
              <div className="bg-white/10 p-2.5 rounded-2xl border border-white/20 group-hover:bg-[#2874A6] transition-all duration-300">
                <Mail className="w-4 h-4" />
              </div>
              <div className="flex flex-col">
                <span className="text-[9px] uppercase tracking-[0.2em] text-[#2874A6] font-black">Soporte</span>
                <span className="font-bold">{EMAIL}</span>
              </div>
            </a>

            {/* WHATSAPP */}
            <a href={`https://wa.me/${WHATSAPP_NUMBER}`} target="_blank" rel="noreferrer" className="group flex items-center gap-4 text-[14px] font-black tracking-normal text-white transition-all">
              <div className="bg-white/10 p-2.5 rounded-2xl border border-white/20 group-hover:bg-green-500 transition-all duration-300">
                <MessageCircle className="w-4 h-4" />
              </div>
              <div className="flex flex-col">
                <span className="text-[9px] uppercase tracking-[0.2em] text-green-400 font-black">Online</span>
                <span className="font-bold">+{WHATSAPP_NUMBER}</span>
              </div>
            </a>
          </div>

          {/* REDES SOCIALES DESKTOP */}
          <div className="flex items-center gap-6">
            <span className="flex items-center gap-2 text-[9px] font-black uppercase tracking-[0.3em] text-[#2874A6] animate-pulse">
              <Zap className="w-3 h-3 fill-current" /> Connect
            </span>
            <div className="flex gap-4">
              <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" aria-label="Facebook" className={socialIconStyle}>
                <Facebook className="w-4 h-4" />
              </a>
              <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer" aria-label="Instagram" className={socialIconStyle}>
                <Instagram className="w-4 h-4" />
              </a>
              <a href={TIKTOK_URL} target="_blank" rel="noopener noreferrer" aria-label="TikTok" className={socialIconStyle}>
                <TikTokIcon className="w-4 h-4" />
              </a>
              <a href={LINKEDIN_URL} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className={socialIconStyle}>
                <Linkedin className="w-4 h-4" />
              </a>
              <a href={YOUTUBE_URL} target="_blank" rel="noopener noreferrer" aria-label="Youtube" className={socialIconStyle}>
                <Youtube className="w-4 h-4" />
              </a>
            </div>
          </div>
        </div>
      </div>

      {/* 🧭 MAIN NAVBAR */}
      <nav className="bg-white/95 backdrop-blur-md p-4 border-b border-slate-100">
        <div className="container mx-auto flex items-center justify-between">
          <Link href="/" className="group relative">
            <h1 className="text-xl md:text-2xl font-black tracking-tighter text-slate-900">
              ANDRODRI<span className="text-[#2874A6]"> S.A.S</span>
            </h1>
          </Link>

          {/* DESKTOP MENU */}
          <ul className="hidden md:flex gap-8 text-[12px] font-black items-center text-slate-600 uppercase tracking-widest">
            {menuItems.map((item) => (
              <li key={item.label}>
                <Link className={navLinkStyle} href={item.href}>
                  {item.label}
                </Link>
              </li>
            ))}
            <li>
              <Link href="/contacto" className="bg-[#2874A6] text-white px-6 py-2.5 rounded-full font-black hover:bg-slate-900 transition-all shadow-lg flex items-center gap-2 group">
                COTIZAR <Send className="w-3 h-3 group-hover:translate-x-1 transition-transform" />
              </Link>
            </li>
          </ul>

          {/* MOBILE BUTTON */}
          <button onClick={() => setIsOpen(!isOpen)} className="md:hidden p-2 rounded-xl bg-slate-900 text-white z-50 relative">
            {isOpen ? <X size={20} /> : <Menu size={20} />}
          </button>
        </div>

        {/* MOBILE MENU CON ANIMACIÓN */}
        <AnimatePresence>
          {isOpen && (
            <motion.div
              key="mobile-menu-container"
              initial={{ opacity: 0, height: 0 }}
              animate={{ opacity: 1, height: "auto" }}
              exit={{ opacity: 0, height: 0 }}
              transition={{ duration: 0.3, ease: "easeInOut" }}
              className="md:hidden overflow-hidden bg-white w-full"
            >
              <div className="py-8">
                <ul className="flex flex-col gap-6 text-lg font-black text-slate-900 uppercase tracking-tighter">
                  {menuItems.map((item) => (
                    <li key={item.label} className="px-4">
                      <Link
                        onClick={() => setIsOpen(false)}
                        href={item.href} // 👈 Ahora usa el objeto mapeado correctamente en mobile
                      >
                        {item.label}
                      </Link>
                    </li>
                  ))}
                </ul>

                {/* REDES SOCIALES MOBILE */}
                <div className="mt-10 border-t border-slate-200 pt-6 px-4">
                  <div className="flex items-center justify-center gap-6">
                    <a href={FACEBOOK_URL} target="_blank" rel="noopener noreferrer" aria-label="Facebook" className={socialIconStyle}>
                      <Facebook className="w-5 h-5 text-slate-700 hover:text-[#2874A6]" />
                    </a>
                    <a href={INSTAGRAM_URL} target="_blank" rel="noopener noreferrer" aria-label="Instagram" className={socialIconStyle}>
                      <Instagram className="w-5 h-5 text-slate-700 hover:text-[#2874A6]" />
                    </a>
                    <a href={TIKTOK_URL} target="_blank" rel="noopener noreferrer" aria-label="TikTok" className={socialIconStyle}>
                      <TikTokIcon className="w-5 h-5 text-slate-700 hover:text-[#2874A6]" />
                    </a>
                    <a href={LINKEDIN_URL} target="_blank" rel="noopener noreferrer" aria-label="LinkedIn" className={socialIconStyle}>
                      <Linkedin className="w-5 h-5 text-slate-700 hover:text-[#2874A6]" />
                    </a>
                    <a href={YOUTUBE_URL} target="_blank" rel="noopener noreferrer" aria-label="Youtube" className={socialIconStyle}>
                      <Youtube className="w-5 h-5 text-slate-700 hover:text-[#2874A6]" />
                    </a>
                  </div>
                </div>
              </div>
            </motion.div>
          )}
        </AnimatePresence>
      </nav>
    </header>
  );
};

export default Navbar;