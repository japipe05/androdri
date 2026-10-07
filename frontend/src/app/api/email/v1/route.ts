
import { NextRequest, NextResponse } from "next/server";
import {
  sendEmailService,
  SendEmailDTO,
} from "@/infrastructure/contactservices";

export async function POST(request: NextRequest) {
  try {
    const body = await request.json();

    const payload: SendEmailDTO = {
      nombre: String(body.nombre ?? "").trim(),
      correo: String(body.correo ?? "").trim(),
      mensaje: String(body.mensaje ?? "").trim(),
    };

    if (!payload.nombre) {
      return NextResponse.json(
        { message: "El nombre es obligatorio." },
        { status: 400 }
      );
    }

    if (!payload.correo) {
      return NextResponse.json(
        { message: "El correo es obligatorio." },
        { status: 400 }
      );
    }

    if (!payload.mensaje) {
      return NextResponse.json(
        { message: "El mensaje es obligatorio." },
        { status: 400 }
      );
    }

    const result = await sendEmailService(payload);

    return NextResponse.json(
      {
        message: result.message || "Correo enviado correctamente.",
      },
      { status: 200 }
    );
  } catch (error: unknown) {
    console.error("Error enviando correo:", error);

    return NextResponse.json(
      {
        message:
          error instanceof Error
            ? error.message
            : "No fue posible enviar el correo.",
      },
      { status: 500 }
    );
  }
}

