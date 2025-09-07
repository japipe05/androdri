import { NextResponse } from "next/server";
import jwt from "jsonwebtoken";
import axios from "axios";

export async function POST(req: Request) {
  try {
    const body = await req.json();
    console.log("📩 Body recibido en API Route:", body);
console.log("process.env.JWT_SECRET:", process.env.JWT_SECRET);
    // Generar el JWT en el servidor (seguro)
    const token = jwt.sign(
      { service: "contact-form" }, // payload opcional
      process.env.JWT_SECRET as string,
      {
        algorithm: "HS256",
        expiresIn: "1h",
      }
    );
    console.log("🔑 JWT generado:", token);

    const backendUrl = `${process.env.CONTACT_API_URL}/api/contact/v1`;
    console.log("🌍 URL backend destino:", backendUrl);

    // Hacer la llamada al backend real
    const response = await axios.post(backendUrl, body, {
      headers: {
        Authorization: `Bearer ${token}`,
        "Content-Type": "application/json",
      },
    });

    console.log("✅ Respuesta backend status:", response.status);
    console.log("📦 Respuesta backend data:", response.data);

    return NextResponse.json(response.data);
  } catch (error: any) {
    console.error("❌ Error en API Route:");
    if (error.response) {
      console.error("Status:", error.response.status);
      console.error("Data:", error.response.data);
    } else {
      console.error("Message:", error.message);
    }

    return NextResponse.json(
      { error: error.response?.data || "Error interno" },
      { status: error.response?.status || 500 }
    );
  }
}
