"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import { Send, Mail, User, MessageSquare, Sparkles, CheckCircle2, AlertCircle } from "lucide-react";

type Status = "idle" | "loading" | "success" | "error";

export default function ContactoPage() {
  const [form, setForm] = useState({ name: "", email: "", message: "" });
  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm((prev) => ({ ...prev, [e.target.name]: e.target.value }));
  };

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setStatus("loading");
    setErrorMessage(null);
    setSuccessMessage(null);

    try {
      const response = await fetch("/api/email/v1", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          nombre: form.name,
          correo: form.email,
          mensaje: form.message,
        }),
      });

      const data = await response.json();
      if (!response.ok) throw new Error(data.message);

      setStatus("success");
      setSuccessMessage("¡Tu mensaje ha sido enviado con éxito!");
      setForm({ name: "", email: "", message: "" });
    } catch (error: unknown) {
      setStatus("error");
      setErrorMessage(error instanceof Error ? error.message : "Error inesperado");
    }
  };

  return (
    <main className="min-h-screen bg-white text-slate-900 flex items-center justify-center p-6 relative overflow-hidden">
      {/* Elementos decorativos de fondo */}
      <div className="absolute top-0 left-0 w-full h-full bg-[radial-gradient(#e2e8f0_1px,transparent_1px)] [background-size:24px_24px] opacity-50 -z-10" />
      <div className="absolute top-1/4 -right-20 w-96 h-96 bg-blue-50 rounded-full blur-3xl -z-10 opacity-60" />

      <motion.div
        initial={{ opacity: 0, y: 30 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8 }}
        className="w-full max-w-5xl grid lg:grid-cols-12 bg-white rounded-[3rem] shadow-[0_50px_100px_-20px_rgba(40,116,166,0.15)] border border-slate-100 overflow-hidden"
      >

        {/* COLUMNA IZQUIERDA: INFORMACIÓN E IMPACTO */}
        <div className="lg:col-span-5 bg-slate-900 p-12 text-white flex flex-col justify-between relative">
          <div className="space-y-6 relative z-10">
            <motion.div
              initial={{ scale: 0.8 }}
              animate={{ scale: 1 }}
              className="w-12 h-12 bg-[#2874A6] rounded-2xl flex items-center justify-center mb-8"
            >
              <Sparkles className="text-white w-6 h-6" />
            </motion.div>
            <h1 className="text-4xl md:text-5xl font-black tracking-tighter leading-tight">
              ¿Listo para <br /> <span className="text-[#2874A6]">innovar?</span>
            </h1>
            <p className="text-slate-400 text-lg">
              Cuéntanos tu idea o proyecto. Nuestro equipo técnico se pondrá en contacto contigo para trazar la hoja de ruta hacia tu éxito digital.
            </p>
          </div>

          <div className="space-y-6 pt-12 relative z-10">
            <div className="flex items-center gap-4 text-sm font-medium group">
              <div className="w-10 h-10 rounded-full bg-white/5 flex items-center justify-center group-hover:bg-[#2874A6] transition-colors">
                <Mail className="w-4 h-4" />
              </div>
              servicios@androdri.com
            </div>
          </div>

          {/* Círculo decorativo interior */}
          <div className="absolute -bottom-20 -left-20 w-64 h-64 bg-[#2874A6]/20 rounded-full blur-3xl" />
        </div>

        {/* COLUMNA DERECHA: FORMULARIO */}
        <div className="lg:col-span-7 p-12 bg-white">
          <form onSubmit={handleSubmit} className="space-y-6">
            <div className="grid md:grid-cols-2 gap-6">
              <div className="space-y-2">
                <label className="text-xs font-black uppercase tracking-widest text-slate-400 ml-1">Tu Nombre</label>
                <div className="relative">
                  <User className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300" />
                  <input
                    type="text"
                    name="name"
                    placeholder="Nombre"
                    value={form.name}
                    onChange={handleChange}
                    required
                    className="w-full bg-slate-50 border-none rounded-2xl px-12 py-4 focus:ring-2 focus:ring-[#2874A6]/20 transition-all outline-none text-slate-900 font-medium"
                  />
                </div>
              </div>
              <div className="space-y-2">
                <label className="text-xs font-black uppercase tracking-widest text-slate-400 ml-1">Correo Electrónico</label>
                <div className="relative">
                  <Mail className="absolute left-4 top-1/2 -translate-y-1/2 w-5 h-5 text-slate-300" />
                  <input
                    type="email"
                    name="email"
                    placeholder="correo@ejemplo.com"
                    value={form.email}
                    onChange={handleChange}
                    required
                    className="w-full bg-slate-50 border-none rounded-2xl px-12 py-4 focus:ring-2 focus:ring-[#2874A6]/20 transition-all outline-none text-slate-900 font-medium"
                  />
                </div>
              </div>
            </div>

            <div className="space-y-2">
              <label className="text-xs font-black uppercase tracking-widest text-slate-400 ml-1">¿En qué podemos ayudarte?</label>
              <div className="relative">
                <MessageSquare className="absolute left-4 top-5 w-5 h-5 text-slate-300" />
                <textarea
                  name="message"
                  placeholder="Describe brevemente tu proyecto o consulta..."
                  value={form.message}
                  onChange={handleChange}
                  required
                  className="w-full bg-slate-50 border-none rounded-2xl px-12 py-4 h-40 focus:ring-2 focus:ring-[#2874A6]/20 transition-all outline-none text-slate-900 font-medium resize-none"
                />
              </div>
            </div>

            <button
              type="submit"
              disabled={status === "loading"}
              className="relative w-full bg-[#2874A6] text-white px-8 py-5 rounded-2xl font-black text-lg overflow-hidden group transition-all hover:bg-slate-900 shadow-xl shadow-blue-100 disabled:opacity-50"
            >
              <span className="relative z-10 flex items-center justify-center gap-3">
                {status === "loading" ? (
                  "Enviando..."
                ) : (
                  <>
                    Enviar mensaje <Send className="w-5 h-5 group-hover:translate-x-1 group-hover:-translate-y-1 transition-transform" />
                  </>
                )}
              </span>
            </button>
          </form>

          {/* NOTIFICACIONES DE ESTADO */}
          <AnimatePresence>
            {status === "success" && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0 }}
                className="mt-6 p-4 rounded-2xl bg-green-50 border border-green-100 flex items-center gap-3 text-green-700 font-bold"
              >
                <CheckCircle2 className="w-5 h-5" /> {successMessage}
              </motion.div>
            )}

            {status === "error" && (
              <motion.div
                initial={{ opacity: 0, y: 10 }}
                animate={{ opacity: 1, y: 0 }}
                exit={{ opacity: 0 }}
                className="mt-6 p-4 rounded-2xl bg-red-50 border border-red-100 flex items-center gap-3 text-red-700 font-bold"
              >
                <AlertCircle className="w-5 h-5" /> {errorMessage}
              </motion.div>
            )}
          </AnimatePresence>
        </div>
      </motion.div>
    </main>
  );
}