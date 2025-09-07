"use client";
import { useState } from "react";
import { motion } from "framer-motion";
import axios from "axios";

export const dynamic = "force-dynamic";

export default function Contacto() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [status, setStatus] = useState<"idle" | "loading" | "success" | "error">("idle");

  const handleChange = (e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("loading");

    if (form.name.trim().length < 2 || form.message.trim().length < 10) {
      alert("El nombre debe tener al menos 2 letras y el mensaje mínimo 10.");
      setStatus("idle");
      return;
    }

    try {
      // Ahora el cliente solo llama al proxy local
      await axios.post("/api/contact", form);

      setStatus("success");
      setForm({ name: "", email: "", message: "" });
    } catch (error) {
      console.error("Error al enviar el mensaje:", error);
      setStatus("error");
    }
  };

  return (
    <main className="min-h-screen bg-[var(--color-background)] text-[var(--color-foreground)] px-4 py-16 flex justify-center">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        transition={{ duration: 0.8, ease: "easeOut" }}
        className="w-full max-w-3xl space-y-10"
      >
        <h1 className="text-3xl md:text-4xl font-bold text-[#2874A6] text-center">
          Contáctanos
        </h1>

        <p className="text-center text-base sm:text-lg text-[var(--color-foreground)]/90">
          ¿Tienes un proyecto o deseas más información? Escríbenos y te responderemos lo antes posible.
        </p>

        <form onSubmit={handleSubmit} className="space-y-6">
          <div className="flex flex-col">
            <label className="mb-1 font-medium">Nombre</label>
            <input
              type="text"
              name="name"
              value={form.name}
              onChange={handleChange}
              placeholder="Tu nombre"
              required
              className="border border-gray-300 rounded-lg px-4 py-2 text-[var(--color-foreground)] bg-white focus:outline-none focus:ring-2 focus:ring-[#2874A6]"
            />
          </div>

          <div className="flex flex-col">
            <label className="mb-1 font-medium">Correo electrónico</label>
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              placeholder="correo@ejemplo.com"
              required
              className="border border-gray-300 rounded-lg px-4 py-2 text-[var(--color-foreground)] bg-white focus:outline-none focus:ring-2 focus:ring-[#2874A6]"
            />
          </div>

          <div className="flex flex-col">
            <label className="mb-1 font-medium">Mensaje</label>
            <textarea
              name="message"
              value={form.message}
              onChange={handleChange}
              placeholder="¿Cómo podemos ayudarte?"
              required
              className="border border-gray-300 rounded-lg px-4 py-2 h-32 text-[var(--color-foreground)] bg-white resize-none focus:outline-none focus:ring-2 focus:ring-[#2874A6]"
            ></textarea>
          </div>

          <button
            type="submit"
            disabled={status === "loading"}
            className="bg-[#2874A6] text-white px-6 py-3 rounded-lg hover:bg-[#1f5e87] transition-colors font-semibold"
          >
            {status === "loading" ? "Enviando..." : "Enviar mensaje"}
          </button>
        </form>

        {status === "success" && (
          <p className="text-green-600 text-center font-medium">✅ ¡Mensaje enviado correctamente!</p>
        )}
        {status === "error" && (
          <p className="text-red-600 text-center font-medium">❌ Hubo un error al enviar el mensaje.</p>
        )}
      </motion.div>
    </main>
  );
}
