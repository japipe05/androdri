// app/api/email/v1/route.ts

import { NextResponse } from "next/server";
import {
  sendEmailService,
  SendEmailDTO,
} from "@/infrastructure/contactservices";

export async function POST(request: Request) {
  try {
    const body: SendEmailDTO = await request.json();

    if (!body.nombre || !body.correo || !body.mensaje) {
      return NextResponse.json(
        { message: "Datos incompletos" },
        { status: 400 }
      );
    }

    const result = await sendEmailService(body);

    return NextResponse.json(result, { status: 200 });
  } catch (error) {
    console.error("API Email Error:", error);

    return NextResponse.json(
      { message: "Error enviando el correo" },
      { status: 500 }
    );
  }
}
