"use client";
import { motion } from "framer-motion";
import { MessageCircle } from "lucide-react"; 

export const WhatsAppButton = () => {
  const phoneNumber = process.env.NEXT_PUBLIC_WHATSAPP_NUMBER;
  
  // Mensaje personalizado
  const message = "Hola! Me gustaría contactar un asesor de Androdri S.A.S";
  
  // Buena práctica: codificar el mensaje para URLs seguras
  const whatsappUrl = `https://wa.me/${phoneNumber}?text=${encodeURIComponent(message)}`;

  // Evita renderizar si no hay número configurado
  if (!phoneNumber) return null;

  return (
    <motion.a
      href={whatsappUrl}
      target="_blank"
      rel="noopener noreferrer"
      initial={{ scale: 0, opacity: 0 }}
      animate={{ scale: 1, opacity: 1 }}
      whileHover={{ 
        scale: 1.1,
        boxShadow: "0px 0px 15px rgba(37, 211, 102, 0.5)" 
      }}
      whileTap={{ scale: 0.9 }}
      className="fixed bottom-6 right-6 z-50 bg-[#25D366] text-white p-4 rounded-full shadow-2xl flex items-center justify-center hover:bg-[#20ba5a] transition-colors"
      aria-label="Contactar a un asesor por WhatsApp"
    >
      <MessageCircle size={28} />
      {/* Opcional: Un pequeño tooltip o texto que aparezca al hacer hover */}
    </motion.a>
  );
};