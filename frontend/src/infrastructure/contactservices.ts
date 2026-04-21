// infraestructure/contactservices.ts

export interface SendEmailDTO {
  nombre: string;
  correo: string;
  mensaje: string;
}

export interface SendEmailResponse {
  message: string;
}

const BASE_URL =
  process.env.EMAIL_API_URL ;

export async function sendEmailService(
  payload: SendEmailDTO
): Promise<SendEmailResponse> {
  const response = await fetch(`${BASE_URL}/send-email`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: JSON.stringify(payload),
    cache: "no-store", // importante en Next 15
  });

  if (!response.ok) {
    const errorText = await response.text();
    throw new Error(errorText || "Email service error");
  }

  return response.json();
}
