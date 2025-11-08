# 🧩 Androdri API — Backend de mensajería WhatsApp

**Androdri API** es un backend modular y escalable desarrollado con **FastAPI**, diseñado para enviar mensajes de **WhatsApp** mediante **Twilio** (o un simulador local).  
Incluye autenticación mediante **JWT**, limitador de peticiones por IP y una arquitectura limpia y desacoplada basada en buenas prácticas de ingeniería de software.

---

## 🚀 Características principales

- **API RESTful con FastAPI** — endpoints claros, tipados y autodocumentados.  
- **Autenticación JWT** — emisión y validación de tokens con expiración configurable.  
- **Rate Limiting** — limitador de peticiones por IP (en memoria).  
- **Integración con Twilio (Adapter Pattern)** — desacoplado, fácilmente sustituible por un simulador local.  
- **Configuración centralizada** — mediante `Pydantic BaseSettings` y variables `.env`.  
- **Pruebas unitarias e integración** — con `pytest`.  
- **Listo para Docker y despliegue en entornos productivos** 🐳  

---

## 🧱 Estructura del proyecto

```bash
androdri_api/
├── app/
│   ├── config/
│   │   └── settings.py           # Configuración global (Pydantic BaseSettings)
│   ├── models/
│   │   ├── whatsapp_model.py     # DTOs para requests/responses de WhatsApp
│   │   └── token_model.py        # DTOs para emisión y validación de JWT
│   ├── routers/
│   │   ├── token_router.py       # Endpoint de emisión de token
│   │   └── whatsapp_router.py    # Endpoint de envío (JWT + rate limiter)
│   ├── services/
│   │   └── whatsapp_service.py   # Integración con Twilio (o simulador)
│   ├── utils/
│   │   ├── jwt_utils.py          # Generación y verificación de JWT
│   │   └── rate_limiter.py       # Limitador de solicitudes por IP (en memoria)
│   └── main.py                   # Punto de entrada: configuración de CORS, routers y handlers globales
│
├── dash_test/
│   └── coverage_dashboard.py     # Placeholder para dashboards o monitoreo
│
├── tests/
│   └── test_whatsapp_api.py      # Pruebas unitarias e integración
│
├── .env.example                  # Variables de entorno de ejemplo
├── Dockerfile
├── requirements.txt
└── README.md
```

---

## 🧠 Patrones de diseño aplicados

| Patrón | Descripción | Ubicación |
|--------|--------------|-----------|
| **Separation of Concerns (SoC)** | Separación clara entre routers, servicios, modelos y utilidades. | Estructura general |
| **Dependency Injection (DI)** | Uso de dependencias de FastAPI (autenticación, rate limiter). | `whatsapp_router.py` |
| **Adapter Pattern** | Abstracción de Twilio para permitir simulación local. | `whatsapp_service.py` |
| **Singleton (práctico)** | Configuración centralizada mediante `settings`. | `config/settings.py` |
| **DTOs / Validation** | Modelos Pydantic como contratos de entrada/salida. | `models/` |
| **Fail-safe / Graceful degradation** | Simulación si Twilio no está configurado. | `whatsapp_service.py` |
| **Anti-Corruption Layer (ACL)** | Aislamiento de la lógica interna frente a detalles del proveedor externo. | `services/` |

---

## 🔐 Seguridad y autenticación JWT

### 🔸 Endpoint de emisión de token

**Ruta:**  
`POST /api/token-whatsapp/v1/`

**Request**
```json
{
  "api_key": "<valor>"
}
```

**Response**
```json
{
  "access_token": "<jwt>",
  "token_type": "bearer",
  "expires_in": 3600
}
```

> ⚠️ El campo `api_key` debe coincidir con el valor configurado en `JWT_SECRET_WHATSAP` dentro del archivo `.env`.  
> En producción se recomienda implementar un flujo con `client_id` + `client_secret` o bien OAuth2 Client Credentials.

---

## 💬 Endpoint de envío de mensajes

**Ruta:**  
`POST /api/whatsapp/v1/send`

**Headers**
```
Authorization: Bearer <JWT>
```

**Body**
```json
{
  "to": "+1234567890",
  "message": "Hola desde Androdri API!"
}
```

**Características:**
- Verificación de JWT ✅  
- Limitación de tasa por IP 🧠  
- Integración con Twilio o simulador local ⚙️  

---

## ⚙️ Configuración del entorno

1. Copia el archivo de ejemplo:
   ```bash
   cp .env.example .env
   ```
2. Configura las variables necesarias:
   ```bash
   JWT_SECRET_WHATSAP=tu_clave_jwt
   TWILIO_ACCOUNT_SID=<opcional>
   TWILIO_AUTH_TOKEN=<opcional>
   TWILIO_PHONE_NUMBER=<opcional>
   ```

---

## Ejecutra requerimientos

compilar librerias necesarias

```bash
pip install -r requirements.txt
pip install -r requirements.txt --upgrade
```

## Ejecutar aplicacion.

Ejecutar la aplicacion 

```bash
uvicorn app.main:app --reload 
```


## 🧪 Pruebas.

Ejecuta las pruebas unitarias y el dashboard de cobertura:

```bash
python dash_test/run_coverage_dashboard.py
pytest -v
```


## 🐳 Despliegue con Docker

### 📦 Construcción de imágenes

```bash
docker build -t japipe05/androdri-backend-pub001-whatsapp-messages:dev-v1.0.0-20251107 .
docker push japipe05/androdri-backend-pub001-whatsapp-messages:dev-v1.0.0-20251107
```

---

### ▶️ Ejecución local

```bash
docker run -d   --name androdri-backend-pub001-whatsapp-messages   --env-file .env   -p 8000:8000   japipe05/androdri-backend-pub001-whatsapp-messages:dev-v1.0.0-20251107
```

Una vez corriendo, accede a la documentación interactiva en:  
👉 **http://localhost:8000/docs**

---

## 📊 Pruebas rápidas

```bash
curl -X POST http://localhost:8000/api/token-whatsapp/v1/   -H "Content-Type: application/json"   -d '{"api_key": "tu_clave_jwt"}'
```

Luego usa el token devuelto para enviar un mensaje:

```bash
curl -X POST http://localhost:8000/api/whatsapp/v1/send   -H "Authorization: Bearer <token>"   -H "Content-Type: application/json"   -d '{"to": "+1234567890", "message": "Hola desde FastAPI 🚀"}'
```

---

## 🧾 Licencia

Proyecto bajo licencia **MIT**.  
Desarrollado con ❤️ por **[tu nombre o tu equipo]**.
