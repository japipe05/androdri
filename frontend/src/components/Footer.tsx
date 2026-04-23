"use client";

import Link from "next/link";
import {
  Facebook,

  Instagram,
  Linkedin,
  ShieldCheck,
  Lock,
  Globe,
  Mail,
  ExternalLink
} from "lucide-react";

const TikTokIcon = () => (
  <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" strokeLinecap="round" strokeLinejoin="round" className="w-5 h-5">
    <path d="M9 12a4 4 0 1 0 4 4V4a5 5 0 0 0 5 5" />
  </svg>
);

export default function Footer() {
  const currentYear = new Date().getFullYear();

  return (
    <footer className="w-full mt-24 bg-slate-900 text-white pt-16 pb-8 border-t-4 border-[#2874A6]">
      <div className="max-w-7xl mx-auto px-6 lg:px-12">
        
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-16">
          
          {/* COLUMNA 1: BRANDING */}
          <div className="space-y-6">
            <h2 className="text-2xl font-black tracking-tighter">
              ANDRODRI<span className="text-[#2874A6]"> S.A.S</span>
            </h2>
            <p className="text-slate-400 text-sm leading-relaxed font-medium">
              Liderando la transformación digital con ingeniería de precisión y seguridad de grado empresarial.
            </p>
            <div className="flex gap-4">
              <Link href="#" className="p-2 bg-white/5 rounded-lg hover:bg-[#2874A6] transition-all text-slate-400 hover:text-white">
                <Facebook size={18} />
              </Link>
              <Link href="#" className="p-2 bg-white/5 rounded-lg hover:bg-[#2874A6] transition-all text-slate-400 hover:text-white">
                <Instagram size={18} />
              </Link>
              <Link href="#" className="p-2 bg-white/5 rounded-lg hover:bg-[#2874A6] transition-all text-slate-400 hover:text-white">
                <TikTokIcon />
              </Link>
              <Link href="#" className="p-2 bg-white/5 rounded-lg hover:bg-[#2874A6] transition-all text-slate-400 hover:text-white">
                <Linkedin size={18} />
              </Link>
            </div>
          </div>

          {/* COLUMNA 2: NAVEGACIÓN */}
          <div className="space-y-6">
            <h3 className="text-sm font-black uppercase tracking-[0.2em] text-[#2874A6]">Empresa</h3>
            <ul className="space-y-4 text-sm font-bold text-slate-300">
              <li><Link href="/" className="hover:text-white transition-colors">Inicio</Link></li>
              <li><Link href="/servicios" className="hover:text-white transition-colors">Servicios</Link></li>
              <li><Link href="/proyectos" className="hover:text-white transition-colors">Proyectos</Link></li>
              <li><Link href="/contacto" className="hover:text-white transition-colors">Contacto</Link></li>
            </ul>
          </div>

          {/* COLUMNA 3: LEGAL & ISO */}
          <div className="space-y-6">
            <h3 className="text-sm font-black uppercase tracking-[0.2em] text-[#2874A6]">Legal & Seguridad</h3>
            <ul className="space-y-4 text-sm font-bold text-slate-300">
              <li>
                <Link href="/politica-privacidad" className="flex items-center gap-2 hover:text-white transition-colors">
                  <ShieldCheck size={16} className="text-[#2874A6]" />
                  Política de Privacidad
                </Link>
              </li>
              <li>
                <Link href="/terminos" className="flex items-center gap-2 hover:text-white transition-colors">
                  <Globe size={16} className="text-[#2874A6]" />
                  Términos de Servicio
                </Link>
              </li>
              <li className="pt-2">
                <div className="flex items-start gap-2 p-3 bg-white/5 rounded-xl border border-white/10">
                  <Lock size={20} className="text-[#2874A6] mt-1" />
                  <div>
                    <p className="text-[10px] text-blue-400 font-black uppercase tracking-tighter">Estándar Internacional</p>
                    <p className="text-[12px] text-white">ISO/IEC 27001 Compliant</p>
                  </div>
                </div>
              </li>
            </ul>
          </div>

          {/* COLUMNA 4: CONTACTO RÁPIDO */}
          <div className="space-y-6">
            <h3 className="text-sm font-black uppercase tracking-[0.2em] text-[#2874A6]">Soporte Global</h3>
            <div className="space-y-4">
              <a href="mailto:servicios@androdri.com" className="flex items-center gap-3 text-sm font-bold text-slate-300 hover:text-white transition-colors group">
                <div className="p-2 bg-[#2874A6]/10 rounded-lg group-hover:bg-[#2874A6]">
                  <Mail size={16} />
                </div>
                servicios@androdri.com
              </a>
              <div className="pt-4">
                 <button className="w-full py-3 bg-gradient-to-r from-slate-800 to-slate-900 border border-white/10 rounded-xl text-xs font-black tracking-widest hover:border-[#2874A6] transition-all flex items-center justify-center gap-2">
                   ESTADO DEL SERVICIO <ExternalLink size={14} className="text-green-500" />
                 </button>
              </div>
            </div>
          </div>

        </div>

        {/* BOTTOM BAR */}
        <div className="pt-8 border-t border-white/5 flex flex-col md:flex-row justify-between items-center gap-6">
          <p className="text-[10px] font-black text-slate-500 uppercase tracking-widest">
            © {currentYear} Androdri S.A.S. • Ingeniería de Software de Alto Impacto
          </p>
          <div className="flex items-center gap-6 grayscale opacity-50 hover:grayscale-0 hover:opacity-100 transition-all">
             <span className="text-[10px] font-black text-slate-500">SEGURIDAD GARANTIZADA POR</span>
             <div className="h-6 w-px bg-white/10"></div>
             <div className="flex items-center gap-2">
                <ShieldCheck size={18} className="text-[#2874A6]" />
                <span className="text-xs font-black italic tracking-tighter">SECURE_DATA ARCHITECTURE</span>
             </div>
          </div>
        </div>

      </div>
    </footer>
  );
}