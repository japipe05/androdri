"use client";
import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import axios from "axios";

export const dynamic = "force-dynamic";

export default function Contacto() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [status, setStatus] = useState<
    "idle" | "loading" | "success" | "error"
  >("idle");

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
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
      const { data } = await axios.post("/api/contact", form, {
        headers: { "Content-Type": "application/json" },
      });

      if (data.success) {
        setStatus("success");
        setForm({ name: "", email: "", message: "" });
      } else {
        setStatus("error");
      }
    } catch (error) {
      console.error("Error al enviar el mensaje:", error);
      setStatus("error");
    } finally {
      setTimeout(() => setStatus("idle"), 4000);
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
          ¿Tienes un proyecto o deseas más información? Escríbenos y te
          responderemos lo antes posible.
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
            className={`${
              status === "loading"
                ? "bg-[#1f5e87] cursor-not-allowed"
                : "bg-[#2874A6] hover:bg-[#1f5e87]"
            } text-white px-6 py-3 rounded-lg transition-colors font-semibold flex items-center justify-center gap-2`}
          >
            {status === "loading" ? (
              <>
                <svg
                  className="animate-spin h-5 w-5 text-white"
                  xmlns="http://www.w3.org/2000/svg"
                  fill="none"
                  viewBox="0 0 24 24"
                >
                  <circle
                    className="opacity-25"
                    cx="12"
                    cy="12"
                    r="10"
                    stroke="currentColor"
                    strokeWidth="4"
                  ></circle>
                  <path
                    className="opacity-75"
                    fill="currentColor"
                    d="M4 12a8 8 0 018-8v4a4 4 0 00-4 4H4z"
                  ></path>
                </svg>
                Enviando...
              </>
            ) : (
              "Enviar mensaje"
            )}
          </button>
        </form>

        {/* Mensajes dinámicos con animación */}
        <AnimatePresence>
          {status === "success" && (
            <motion.p
              key="success"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="text-green-600 text-center font-medium"
            >
              ✅ ¡Mensaje enviado correctamente!
            </motion.p>
          )}
          {status === "error" && (
            <motion.p
              key="error"
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              transition={{ duration: 0.4 }}
              className="text-red-600 text-center font-medium"
            >
              ❌ Hubo un error al enviar el mensaje.
            </motion.p>
          )}
        </AnimatePresence>
      </motion.div>
    </main>
  );
}
