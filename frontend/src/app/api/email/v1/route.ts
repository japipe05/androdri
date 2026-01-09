import { NextRequest, NextResponse } from "next/server";
import axios, { AxiosError } from "axios";
import FormData from "form-data";

const TOKEN_URL = process.env.TOKEN_URL!;
const EMAIL_URL = process.env.EMAIL_URL!;
const API_KEY = process.env.EMAIL_API_KEY!;

interface TokenResponse {
  access_token: string;
}

export async function POST(req: NextRequest) {
  try {
    const body = await req.json();
    const { name, email, message } = body as {
      name?: string;
      email?: string;
      message?: string;
    };

    if (!name || !email || !message) {
      return NextResponse.json(
        { error: "Campos incompletos" },
        { status: 400 }
      );
    }

    /* ======================
       1️⃣ OBTENER TOKEN
    ====================== */
    let access_token: string;

    try {
      const tokenRes = await axios.post<TokenResponse>(
        TOKEN_URL,
        { api_key: API_KEY },
        {
          headers: {
            "Content-Type": "application/json",
            Accept: "application/json",
          },
        }
      );

      access_token = tokenRes.data.access_token;
    } catch (err: unknown) {
      const error = err as AxiosError;

      console.error("===== TOKEN AXIOS ERROR =====");
      console.error("message:", error.message);
      console.error("code:", error.code);
      console.error("status:", error.response?.status);
      console.error("statusText:", error.response?.statusText);
      console.error("response.data:", error.response?.data);
      console.error("response.headers:", error.response?.headers);
      console.error("request.url:", error.config?.url);
      console.error("request.method:", error.config?.method);
      console.error("=============================");

      return NextResponse.json(
        { error: "Error autenticando" },
        { status: 500 }
      );
    }

    /* ======================
       2️⃣ ENVIAR EMAIL
    ====================== */
const formData = new FormData();
formData.append("asunto", `Contacto: ${name}`);
formData.append("mensaje", `De: ${email}\n\n${message}`);

let emailRes;

try {
  emailRes = await axios.post(EMAIL_URL, formData, {
    headers: {
      Authorization: `Bearer ${access_token}`,
      Accept: "application/json",
      ...formData.getHeaders(),
    },
  });
} catch (err: unknown) {
  const error = err as AxiosError;

  console.error(
    "EMAIL ERROR:",
    error.response?.data ?? error.message
  );

  return NextResponse.json(
    { success: false, message: "Error enviando correo" },
    { status: 500 }
  );
}

/* ======================
   3️⃣ RESPUESTA FINAL
====================== */
return NextResponse.json({
  success: true,
  message: emailRes?.data?.message ?? "Correo enviado correctamente",
});


  } catch (err: unknown) {
    const error = err as Error;
    console.error("API EMAIL ERROR:", error.message);

    return NextResponse.json(
      { error: "Error interno" },
      { status: 500 }
    );
  }
}
