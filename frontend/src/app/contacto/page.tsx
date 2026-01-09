"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";
import axios from "axios";

export const dynamic = "force-dynamic";

type Status = "idle" | "loading" | "success" | "error";

export default function Contacto() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    message: "",
  });

  const [status, setStatus] = useState<Status>("idle");
  const [errorMessage, setErrorMessage] = useState<string | null>(null);
  const [successMessage, setSuccessMessage] = useState<string | null>(null);

  const handleChange = (
    e: React.ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setForm((prev) => ({
      ...prev,
      [e.target.name]: e.target.value,
    }));
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setStatus("loading");
    setErrorMessage(null);
    setSuccessMessage(null);

    if (form.name.trim().length < 2 || form.message.trim().length < 10) {
      alert("El nombre debe tener al menos 2 letras y el mensaje mínimo 10.");
      setStatus("idle");
      return;
    }

    try {
      const { data } = await axios.post("/api/email/v1", form);

      // ✅ ÉXITO SI NO HUBO ERROR
      setStatus("success");
      setSuccessMessage(
        data?.message || " enviado correctamente."
      );
      setForm({ name: "", email: "", message: "" });

    } catch (error: unknown) {
      let message = "Error al enviar el mensaje.";

      if (axios.isAxiosError(error)) {
        message =
          error.response?.data?.message ||
          error.message ||
          "No se pudo enviar el mensaje.";
      }

      console.error("Error al enviar el mensaje:", message);
      setErrorMessage(message);
      setStatus("error");
    } finally {
      setTimeout(() => {
        setStatus("idle");
        setErrorMessage(null);
        setSuccessMessage(null);
      }, 4000);
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
              required
              className="border border-gray-300 rounded-lg px-4 py-2 bg-white focus:ring-2 focus:ring-[#2874A6]"
            />
          </div>

          <div className="flex flex-col">
            <label className="mb-1 font-medium">Correo electrónico</label>
            <input
              type="email"
              name="email"
              value={form.email}
              onChange={handleChange}
              required
              className="border border-gray-300 rounded-lg px-4 py-2 bg-white focus:ring-2 focus:ring-[#2874A6]"
            />
          </div>

          <div className="flex flex-col">
            <label className="mb-1 font-medium">Mensaje</label>
            <textarea
              name="message"
              value={form.message}
              onChange={handleChange}
              required
              className="border border-gray-300 rounded-lg px-4 py-2 h-32 bg-white resize-none focus:ring-2 focus:ring-[#2874A6]"
            />
          </div>

          <button
            type="submit"
            disabled={status === "loading"}
            className={`${
              status === "loading"
                ? "bg-[#1f5e87] cursor-not-allowed"
                : "bg-[#2874A6] hover:bg-[#1f5e87]"
            } text-white px-6 py-3 rounded-lg transition-colors font-semibold flex justify-center`}
          >
            {status === "loading" ? "Enviando..." : "Enviar mensaje"}
          </button>
        </form>

        <AnimatePresence>
          {status === "success" && successMessage && (
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="text-green-600 text-center font-medium"
            >
              ✅ {successMessage}
            </motion.p>
          )}

          {status === "error" && errorMessage && (
            <motion.p
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              exit={{ opacity: 0, y: -20 }}
              className="text-red-600 text-center font-medium"
            >
              ❌ {errorMessage}
            </motion.p>
          )}
        </AnimatePresence>
      </motion.div>
    </main>
  );
}
