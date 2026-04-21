"use client";
import Link from "next/link";
import { useState } from "react";
import {
  Menu,
  X,
  Mail,
  Phone,
  Facebook,
  Instagram,
  Youtube,
  Linkedin,
  Send,
  MessageCircle,
  Zap
} from "lucide-react";

const TikTokIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="w-4 h-4">
    <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5" />
  </svg>
);

const Navbar = () => {
  const [isOpen, setIsOpen] = useState(false);

  const navLinkStyle =
    "relative hover:text-[#2874A6] transition-colors after:content-[''] after:absolute after:left-0 after:-bottom-1 after:h-[2px] after:w-0 after:bg-[#2874A6] after:transition-all after:duration-300 hover:after:w-full";

  const socialIconStyle = "text-white/60 hover:text-[#2874A6] transition-all transform hover:scale-125 hover:drop-shadow-[0_0_8px_rgba(40,116,166,0.8)]";

  return (
    <header className="sticky top-0 z-50 shadow-2xl">

      {/* 🌌 TOP BAR CENTRADA Y AWESOME */}
      <div className="bg-gradient-to-r from-slate-900 via-[#0a0f1a] to-slate-900 text-white py-2.5 px-6 hidden md:block border-b border-white/5">
        <div className="container mx-auto flex justify-center items-center gap-12">

          {/* Grupo de Contacto Centrado */}
          <div className="flex items-center justify-center gap-12 border-r border-white/20 pr-12">
            {/* EMAIL */}
            <a
              href="mailto:servicios@androdri.com"
              className="group flex items-center gap-4 text-[15px] font-black tracking-normal text-white hover:text-white transition-all"
            >
              <div className="bg-white/10 p-2.5 rounded-2xl border border-white/20 group-hover:bg-[#2874A6] group-hover:border-[#2874A6] group-hover:shadow-[0_0_15px_rgba(40,116,166,0.5)] transition-all duration-300">
                <Mail className="w-5 h-5 text-white group-hover:scale-110 transition-transform" />
              </div>
              <div className="flex flex-col">
                <span className="text-[10px] uppercase tracking-[0.2em] text-[#2874A6] font-black mb-0.5 animate-pulse">Soporte</span>
                <span className="drop-shadow-sm font-bold tracking-tight">
                  servicios@androdri.com
                </span>
              </div>
            </a>

            {/* SEPARADOR VIBRANTE */}
            <div className="h-10 w-px bg-gradient-to-b from-transparent via-white/20 to-transparent"></div>

            {/* WHATSAPP */}
            <a
              href="https://wa.me/573224612382"
              className="group flex items-center gap-4 text-[15px] font-black tracking-normal text-white hover:text-white transition-all"
            >
              <div className="bg-white/10 p-2.5 rounded-2xl border border-white/20 group-hover:bg-green-500 group-hover:border-green-500 group-hover:shadow-[0_0_15px_rgba(34,197,94,0.5)] transition-all duration-300">
                <MessageCircle className="w-5 h-5 text-white group-hover:scale-110 transition-transform" />
              </div>
              <div className="flex flex-col">
                <span className="text-[10px] uppercase tracking-[0.2em] text-green-400 font-black mb-0.5 animate-pulse">Online</span>
                <span className="drop-shadow-sm font-bold tracking-tight">
                  +57 322 461 2382
                </span>
              </div>
            </a>
          </div>

          {/* Grupo de Redes con Efecto Glow */}
          <div className="flex items-center gap-6">
            <span className="flex items-center gap-2 text-[9px] font-black uppercase tracking-[0.3em] text-[#2874A6] animate-pulse">
              <Zap className="w-3 h-3 fill-current" /> Connect
            </span>
            <div className="flex gap-4">
              <a href="#" className={socialIconStyle}><Facebook className="w-4 h-4" /></a>
              <a href="#" className={socialIconStyle}><Instagram className="w-4 h-4" /></a>
              <a href="#" className={socialIconStyle}><TikTokIcon /></a>
              <a href="#" className={socialIconStyle}><Youtube className="w-4 h-4" /></a>
              <a href="#" className={socialIconStyle}><Linkedin className="w-4 h-4" /></a>
            </div>
          </div>

        </div>
      </div>

      {/* 🧭 MAIN NAVBAR */}
      <nav className="bg-white/95 backdrop-blur-md p-5 border-b border-slate-100">
        <div className="container mx-auto flex items-center justify-between">

          {/* LOGO */}
          <Link href="/" className="group relative">
            <h1 className="text-2xl md:text-3xl font-black tracking-tighter text-slate-900">
              ANDRODRI<span className="text-[#2874A6]"> S.A.S</span>
            </h1>
            <div className="absolute -bottom-1 left-0 w-0 h-1 bg-[#2874A6] group-hover:w-full transition-all duration-500 shadow-[0_0_15px_rgba(40,116,166,0.5)]" />
          </Link>

          {/* DESKTOP MENU */}
          <ul className="hidden md:flex gap-8 text-[13px] font-black items-center text-slate-500 uppercase tracking-widest">
            <li><Link className={navLinkStyle} href="/">Inicio</Link></li>
            <li><Link className={navLinkStyle} href="/servicios">Servicios</Link></li>
            <li><Link className={navLinkStyle} href="/proyectos">Proyectos</Link></li>
            <li><Link className={navLinkStyle} href="/#precios">Precios</Link></li>
            <li><Link className={navLinkStyle} href="/contacto">Contacto</Link></li>

            <li>
              <Link
                href="/contacto"
                className="relative overflow-hidden bg-[#2874A6] text-white px-8 py-3 rounded-full font-black hover:bg-slate-900 transition-all shadow-[0_10px_20px_-5px_rgba(40,116,166,0.4)] flex items-center gap-2 group"
              >
                <span className="relative z-10">COTIZAR</span>
                <Send className="w-3.5 h-3.5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform relative z-10" />
                <div className="absolute inset-0 bg-gradient-to-r from-transparent via-white/10 to-transparent -translate-x-full group-hover:translate-x-full transition-transform duration-1000" />
              </Link>
            </li>
          </ul>

          {/* MOBILE BUTTON */}
          <button
            onClick={() => setIsOpen(!isOpen)}
            className="md:hidden p-2 rounded-2xl bg-slate-900 text-white shadow-lg"
          >
            {isOpen ? <X size={24} /> : <Menu size={24} />}
          </button>
        </div>

        {/* MOBILE MENU */}
        {isOpen && (
          <div className="md:hidden absolute top-full left-0 w-full bg-white p-8 shadow-2xl border-t border-slate-50 animate-in fade-in zoom-in duration-300">
            <ul className="flex flex-col gap-8 text-xl font-black text-slate-900 uppercase tracking-tighter">
              <li><Link onClick={() => setIsOpen(false)} href="/">Inicio</Link></li>
              <li><Link onClick={() => setIsOpen(false)} href="/servicios">Servicios</Link></li>
              <li><Link onClick={() => setIsOpen(false)} href="/proyectos">Proyectos</Link></li>
              <li><Link onClick={() => setIsOpen(false)} href="/#precios">Precios</Link></li>
              <li><Link onClick={() => setIsOpen(false)} href="/contacto">Contacto</Link></li>

              <li className="pt-8 border-t border-slate-100 space-y-6">
                <div className="flex justify-around bg-slate-50 p-4 rounded-3xl">
                  <Facebook className="text-[#2874A6]" />
                  <Instagram className="text-[#2874A6]" />
                  <TikTokIcon />
                  <Linkedin className="text-[#2874A6]" />
                </div>
                <Link
                  onClick={() => setIsOpen(false)}
                  href="/contacto"
                  className="bg-[#2874A6] text-white px-4 py-5 rounded-[2rem] text-center block w-full shadow-2xl font-black italic"
                >
                  ¡EMPECEMOS YA!
                </Link>
              </li>
            </ul>
          </div>
        )}
      </nav>
    </header>
  );
};

export default Navbar;