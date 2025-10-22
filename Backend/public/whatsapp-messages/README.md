prompt
Hola buen día ¿Cómo está?

Creame una fast api que envie mensajes por whatsapp teniendo encuenta lo siguiente:

1. utiliza authorization beares token  mediente el .env JWT_SECRET_WHATSAP
y TWILIO el servicio de envio
TWILIO_ACCOUNT_SID=AC2e8a12693e513dab18627e6a491184fe
TWILIO_AUTH_TOKEN=82c96cfd3d134ac4163ef6fe85ec09e3
TWILIO_WHATSAPP_NUMBER=+14155238886
APP_NAME=FastAPI Androdri
APP_VERSION=1.0.0
APP_DESCRIPTION=Backend para la aplicación Androdri
APP_FECHAMOD=2025/10/08 9:27:01

# CORS
ALLOWED_ORIGINS=["http://127.0.0.1:8000","http://localhost:3000","https://api.androdri.com"]

2. parametros de entrada phone_number message
3. utiliza patrones de software y dime cuales utiliza
4. utiliza manejo de errores
5. utiliza estas veriones python Python 3.13.9
6. agrega una opcion que un computador no permita enviar mas de 10 solicitudes despues de 60 segundos le permita enviar 
7. utiliza esta estrucutra de capetas o recomiendame una y define que hace cada carpeta

# Estructuras Carpetas
androdri_api/
│
├── app/
│   ├── config/
│   │   ├── settings.py
│   │
│   ├── models/
│   │   ├── email_model.py
│   │
│   ├── routers/
│   │   ├── contact_router.py
│   │
│   ├── services/
│   │   ├── email_service.py
│   │
│   ├── utils/
│   │   ├── compress_utils.py
│   │   ├── jwt_utils.py
│   │
│   ├── main.py
│
├── dash_test/
│   ├── coverage_dashboard.py
├── tests/
│   ├── test_contact_api.py
│
├── .dockerignore
├── .env
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt
-----------------
androdri_api/
│
├── app/
│   ├── config/
│   │   └── settings.py
│   │
│   ├── models/
│   │   └── message_model.py
│   │
│   ├── routers/
│   │   └── whatsapp_router.py
│   │
│   ├── services/
│   │   └── whatsapp_service.py
│   │
│   ├── utils/
│   │   ├── jwt_utils.py
│   │   └── rate_limiter.py
│   │
│   ├── main.py
│
├── dash_test/
│   └── coverage_dashboard.py
├── tests/
│   └── test_whatsapp_api.py
│
├── .dockerignore
├── .env.example
├── .gitignore
├── Dockerfile
├── README.md
└── requirements.txt


Qué hace cada carpeta / archivo

app/config/settings.py — carga variables de entorno (.env) y expone configuración (Singleton).

app/models/message_model.py — modelos Pydantic para la API (entrada/salida).

app/routers/whatsapp_router.py — rutas / endpoints (separación de responsabilidades).

app/services/whatsapp_service.py — capa de servicio que habla con Twilio (Adapter pattern).

app/utils/jwt_utils.py — manejo de creación/validación de JWT Bearer.

app/utils/rate_limiter.py — limitador por "computador" (IP) permitiendo max 10 solicitudes en 60s.

app/main.py — arranque de FastAPI, CORS, dependencias globales y handlers.

tests/test_whatsapp_api.py — pruebas básicas usando httpx y pytest.

dash_test/coverage_dashboard.py — (placeholder) script de ejemplo para integraciones de dashboard.

Dockerfile, requirements.txt, .env.example — despliegue.

Patrones de software utilizados

Dependency Injection — FastAPI Depends para inyectar comprobaciones (auth, rate-limit, servicios). ✔️

Service Layer / Adapter — whatsapp_service.py encapsula Twilio (mapea API externa a interfaz local). ✔️

Singleton (Configuration) — settings.py carga .env una vez y reutiliza la instancia. ✔️

DTOs (Data Transfer Objects) — Pydantic models para validar entrada/salida. ✔️

Rate Limiter (Decorator/Dependency pattern) — lógica separada como dependencia reutilizable. ✔️

Exception Handling / Centralized HTTP Errors — uso de HTTPException, manejo de errores en servicio. ✔️

Fail Fast — validación temprana de payloads y permisos. ✔️



pip install -r requirements.txt
uvicorn app.main:app --reload
