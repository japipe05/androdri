"use client";
import { motion } from "framer-motion";
import { MessageCircle } from "lucide-react"; 

export default function WhatsAppButton() {
  const phoneNumber = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER;

  // 🔥 Mensaje más orientado a conversión
  const message = "Hola, quiero una página web para mi negocio y recibir más información";

  // Validación simple
  if (!phoneNumber) {
    console.warn("⚠️ Falta NEXT_PUBLIC_WHATSAPP_NUMBER en .env");
    return null;
  }

  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;

  return (
    <motion.a
      href={whatsappUrl}
      target="_blank"
      rel="noopener noreferrer"
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      whileHover={{ 
        scale: 1.1,
        boxShadow: "0px 0px 20px rgba(37, 211, 102, 0.6)" 
      }}
      whileTap={{ scale: 0.9 }}
      className="fixed bottom-6 right-6 z-50 bg-[#25D366] text-white p-4 rounded-full shadow-2xl flex items-center justify-center hover:bg-[#20ba5a] transition-colors"
      aria-label="Contactar por WhatsApp"
    >
      <MessageCircle size={28} />
    </motion.a>
  );
}