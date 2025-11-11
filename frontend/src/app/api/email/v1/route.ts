// app/api/contact/route.ts
import { NextRequest, NextResponse } from "next/server";

const TOKEN_URL = process.env.TOKEN_URL || ""; // ⚠️ Se guarda en .env.local
const EMAIL_URL = process.env.EMAIL_URL || ""; // ⚠️ Se guarda en .env.local
const API_KEY = process.env.EMAIL_API_KEY || ""; // ⚠️ Se guarda en .env.local

export async function POST(req: NextRequest) {
  try {
    const { name, email, message } = await req.json();

    // Validaciones mínimas
    if (!name || !email || !message)
      return NextResponse.json({ error: "Campos incompletos" }, { status: 400 });

    // 1️⃣ Obtener token seguro desde backend
    const tokenRes = await fetch(TOKEN_URL, {
      method: "POST",
      headers: { "Content-Type": "application/json", accept: "application/json" },
      body: JSON.stringify({ api_key: API_KEY }),
    });

    if (!tokenRes.ok) {
      console.error("Error al obtener el token:", await tokenRes.text());
      return NextResponse.json({ error: "Error al autenticar con API externa" }, { status: 500 });
    }

    const tokenData = await tokenRes.json();
    const token = tokenData.access_token;

    // 2️⃣ Enviar correo a la API protegida
    const formData = new FormData();
    formData.append("asunto", `Contactanos ${name}`);
    formData.append("mensaje", `De: <${email}>\n\n${message}`);
    formData.append("comprimir", "false");
    formData.append("password", "");

    const emailRes = await fetch(EMAIL_URL, {
      method: "POST",
      headers: {
        Authorization: `Bearer ${token}`,
        accept: "application/json",
      },
      body: formData,
    });

    if (!emailRes.ok) {
      console.error("Error al enviar correo:", await emailRes.text());
      return NextResponse.json({ error: "Error al enviar correo" }, { status: 500 });
    }

    const result = await emailRes.json();
    return NextResponse.json({ success: true, message: result.message });
  } catch (error) {
    console.error("Error en /api/contact:", error);
    return NextResponse.json({ error: "Error interno del servidor" }, { status: 500 });
  }
}
