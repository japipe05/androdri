"use client";

import Link from "next/link";
import { motion } from "framer-motion";
import {
  Facebook,
  Instagram,
  Linkedin,
  ShieldCheck,
  Lock,
  Globe,
  Mail,
  ExternalLink,
  MessageCircle,
  ChevronRight
} from "lucide-react";

// Constantes centralizadas
const WHATSAPP_NUMBER = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER || "573224612382";
const EMAIL = "servicios@androdri.com";

const TikTokIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="w-5 h-5">
    <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5" />
  </svg>
);

const FOOTER_LINKS = {
  empresa: [
    { name: "Inicio", href: "/" },
    { name: "Servicios", href: "/servicios" },
    { name: "Proyectos", href: "/proyectos" },
    { name: "Contacto", href: "/contacto" },
  ],
  legal: [
    { name: "Política de Privacidad", href: "/politica-privacidad", icon: <ShieldCheck size={16} /> },
    { name: "Términos de Servicio", href: "/terminos", icon: <Globe size={16} /> },
  ]
};

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="relative w-full mt-24 bg-slate-950 text-white pt-20 pb-8 border-t border-white/5 overflow-hidden">
      {/* 🌌 EFECTO DE FONDO (Radial Glow) */}
      <div className="absolute top-0 left-1/2 -translate-x-1/2 w-full h-[500px] bg-[#2874A6]/5 blur-[120px] rounded-full pointer-events-none" />

      <div className="max-w-7xl mx-auto px-6 lg:px-12 relative z-10">
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-16 mb-20">
          
          {/* COLUMNA 1: BRANDING & MISSION */}
          <div className="space-y-8">
            <div className="space-y-4">
              <h2 className="text-2xl font-black tracking-tighter">
                ANDRODRI<span className="text-[#2874A6]"> S.A.S</span>
              </h2>
              <p className="text-slate-400 text-sm leading-relaxed font-medium">
                Arquitectura de software de alto impacto y soluciones de ciberseguridad diseñadas para la escala global.
              </p>
            </div>
            
            <div className="flex gap-3">
              {[
                { icon: <Facebook size={18} />, href: "#" },
                { icon: <Instagram size={18} />, href: "#" },
                { icon: <TikTokIcon />, href: "#" },
                { icon: <Linkedin size={18} />, href: "#" }
              ].map((social, i) => (
                <Link 
                  key={i} 
                  href={social.href} 
                  className="p-2.5 bg-white/5 rounded-xl hover:bg-[#2874A6] hover:shadow-[0_0_15px_rgba(40,116,166,0.4)] transition-all text-slate-400 hover:text-white border border-white/5"
                >
                  {social.icon}
                </Link>
              ))}
            </div>
          </div>

          {/* COLUMNA 2: NAVEGACIÓN INTELIGENTE */}
          <div className="space-y-8">
            <h3 className="text-xs font-black uppercase tracking-[0.3em] text-[#2874A6]">Explorar</h3>
            <ul className="space-y-4">
              {FOOTER_LINKS.empresa.map((link) => (
                <li key={link.name}>
                  <Link 
                    href={link.href} 
                    className="group flex items-center gap-2 text-sm font-bold text-slate-400 hover:text-white transition-all"
                  >
                    <ChevronRight size={14} className="text-[#2874A6] opacity-0 -ml-4 group-hover:opacity-100 group-hover:ml-0 transition-all" />
                    {link.name}
                  </Link>
                </li>
              ))}
            </ul>
          </div>

          {/* COLUMNA 3: COMPLIANCE & TRUST */}
          <div className="space-y-8">
            <h3 className="text-xs font-black uppercase tracking-[0.3em] text-[#2874A6]">Compliance</h3>
            <div className="space-y-6">
              <ul className="space-y-4">
                {FOOTER_LINKS.legal.map((link) => (
                  <li key={link.name}>
                    <Link href={link.href} className="flex items-center gap-3 text-sm font-bold text-slate-400 hover:text-white transition-colors">
                      <span className="text-[#2874A6]">{link.icon}</span>
                      {link.name}
                    </Link>
                  </li>
                ))}
              </ul>
              <div className="p-4 bg-gradient-to-br from-white/5 to-transparent rounded-2xl border border-white/10 backdrop-blur-sm">
                <div className="flex items-center gap-3 mb-2">
                  <Lock size={18} className="text-[#2874A6]" />
                  <span className="text-[11px] font-black uppercase tracking-widest text-blue-400">Security Grade</span>
                </div>
                <p className="text-[13px] text-white font-bold">ISO/IEC 27001 Certified</p>
              </div>
            </div>
          </div>

          {/* COLUMNA 4: CANALES DIRECTOS */}
          <div className="space-y-8">
            <h3 className="text-xs font-black uppercase tracking-[0.3em] text-[#2874A6]">Soporte Élite</h3>
            <div className="space-y-4">
              <a href={`mailto:${EMAIL}`} className="flex items-center gap-4 group">
                <div className="p-2.5 bg-white/5 rounded-xl group-hover:bg-[#2874A6] transition-all border border-white/5">
                  <Mail size={18} className="text-slate-400 group-hover:text-white" />
                </div>
                <span className="text-sm font-bold text-slate-300 group-hover:text-white transition-colors">{EMAIL}</span>
              </a>
              
              <a href={`https://wa.me/${WHATSAPP_NUMBER}`} className="flex items-center gap-4 group">
                <div className="p-2.5 bg-white/5 rounded-xl group-hover:bg-green-500 transition-all border border-white/5">
                  <MessageCircle size={18} className="text-slate-400 group-hover:text-white" />
                </div>
                <span className="text-sm font-bold text-slate-300 group-hover:text-white transition-colors">WhatsApp Directo</span>
              </a>

              <div className="pt-4">
                <button className="group relative w-full py-4 bg-slate-900 border border-white/10 rounded-2xl text-[10px] font-black tracking-[0.2em] hover:border-[#2874A6]/50 transition-all overflow-hidden">
                  <div className="relative z-10 flex items-center justify-center gap-2">
                    ESTADO DEL SERVICIO 
                    <div className="w-2 h-2 bg-green-500 rounded-full animate-pulse shadow-[0_0_8px_#22c55e]" />
                  </div>
                  <div className="absolute inset-0 bg-[#2874A6]/5 opacity-0 group-hover:opacity-100 transition-opacity" />
                </button>
              </div>
            </div>
          </div>

        </div>

        {/* ⚡ BOTTOM BAR: FINAL TOUCH */}
        <div className="pt-10 border-t border-white/5 flex flex-col lg:flex-row justify-between items-center gap-8">
          <div className="flex flex-col items-center lg:items-start gap-2">
            <p className="text-[10px] font-black text-slate-500 uppercase tracking-[0.2em]">
              © {currentYear} <span className="text-slate-300">Androdri S.A.S.</span>
            </p>
            <p className="text-[9px] text-slate-600 font-bold uppercase tracking-widest">
              Bogotá, Colombia • All Rights Reserved
            </p>
          </div>

          <div className="flex flex-wrap justify-center items-center gap-8 py-4 px-8 bg-white/[0.02] rounded-3xl border border-white/5 backdrop-blur-md">
             <div className="flex items-center gap-4 opacity-40 hover:opacity-100 transition-opacity">
                <ShieldCheck size={20} className="text-[#2874A6]" />
                <div className="flex flex-col leading-none">
                  <span className="text-[8px] font-black text-slate-500 uppercase tracking-tighter">Infraestructura</span>
                  <span className="text-[10px] font-black text-white italic">SECURE_CORE 2.0</span>
                </div>
             </div>
             <div className="h-8 w-px bg-white/10 hidden sm:block"></div>
             <div className="text-[10px] font-black text-slate-500 uppercase tracking-widest flex items-center gap-2">
                <div className="w-1.5 h-1.5 bg-[#2874A6] rounded-full" />
                Ingeniería de Software de Élite
             </div>
          </div>
        </div>

      </div>
    </footer>
  );
}