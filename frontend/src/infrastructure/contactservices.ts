
export interface SendEmailDTO {
  nombre: string;
  correo: string;
  mensaje: string;
}

export interface SendEmailResponse {
  message: string;
}

const BASE_URL = process.env.EMAIL_API_URL;
const API_KEY = process.env.EMAIL_API_KEY;
const EMISOR_EMAIL = process.env.EMISOR_EMAIL ;

export async function sendEmailService(
  payload: SendEmailDTO
): Promise<SendEmailResponse> {
  if (!BASE_URL) {
    throw new Error("EMAIL_API_URL no está configurada");
  }

  if (!API_KEY) {
    throw new Error("EMAIL_API_KEY no está configurada");
  }

  const response = await fetch(`${BASE_URL}/api/v1/emails/send`, {
    method: "POST",
    headers: {
      Accept: "application/json",
      "Content-Type": "application/json",
      "x-api-key": API_KEY,
    },
    body: JSON.stringify({
      receptor: payload.correo ,
      emisor: EMISOR_EMAIL,
      asunto: `Escribir: ${payload.nombre}`,
      mensaje: `Correo: ${payload.correo}
                Mensaje:${payload.mensaje}`,}),
    cache: "no-store",
  });

 if (!response.ok) {
  let errorMessage = "No fue posible enviar el mensaje.";

  try {
    const errorData = await response.json();

    if (errorData?.error?.message) {
      errorMessage = errorData.error.message;
    } else if (errorData?.message) {
      errorMessage = errorData.message;
    }
  } catch {
    // La respuesta no contiene JSON válido.
  }

  throw new Error(errorMessage);
}

  return response.json();
}

