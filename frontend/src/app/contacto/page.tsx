"use client";

import { useState } from "react";
import { motion, AnimatePresence } from "framer-motion";

type Status = "idle" | "loading" | "success" | "error";

export default function ContactoPage() {
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

  const handleSubmit = async (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();

    setStatus("loading");
    setErrorMessage(null);
    setSuccessMessage(null);

    try {
      const response = await fetch("/api/email/v1", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          nombre: form.name,
          correo: form.email,
          mensaje: form.message,
        }),
      });

      const data = await response.json();

      if (!response.ok) {
        throw new Error(data.message);
      }

      setStatus("success");
      setSuccessMessage("Mensaje enviado correctamente.");

      setForm({
        name: "",
        email: "",
        message: "",
      });
    } catch (error: unknown) {
      setStatus("error");
      setErrorMessage(
        error instanceof Error
          ? error.message
          : "Error inesperado"
      );
    }
  };

  return (
    <main className="min-h-screen flex justify-center items-center px-4">
      <motion.div
        initial={{ opacity: 0, y: 40 }}
        animate={{ opacity: 1, y: 0 }}
        className="w-full max-w-2xl space-y-6"
      >
        <h1 className="text-3xl font-bold text-center text-[#2874A6]">
          Contáctanos
        </h1>

        <form onSubmit={handleSubmit} className="space-y-4">
          <input
            type="text"
            name="name"
            placeholder="Nombre"
            value={form.name}
            onChange={handleChange}
            required
            className="w-full border rounded-lg px-4 py-2"
          />

          <input
            type="email"
            name="email"
            placeholder="Correo"
            value={form.email}
            onChange={handleChange}
            required
            className="w-full border rounded-lg px-4 py-2"
          />

          <textarea
            name="message"
            placeholder="Mensaje"
            value={form.message}
            onChange={handleChange}
            required
            className="w-full border rounded-lg px-4 py-2 h-32"
          />

          <button
            type="submit"
            disabled={status === "loading"}
            className="bg-[#2874A6] text-white px-6 py-3 rounded-lg w-full"
          >
            {status === "loading" ? "Enviando..." : "Enviar mensaje"}
          </button>
        </form>

        <AnimatePresence>
          {status === "success" && successMessage && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="text-green-600 text-center"
            >
              {successMessage}
            </motion.p>
          )}

          {status === "error" && errorMessage && (
            <motion.p
              initial={{ opacity: 0 }}
              animate={{ opacity: 1 }}
              exit={{ opacity: 0 }}
              className="text-red-600 text-center"
            >
              {errorMessage}
            </motion.p>
          )}
        </AnimatePresence>
      </motion.div>
    </main>
  );
}
