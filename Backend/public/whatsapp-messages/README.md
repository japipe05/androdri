prompt
Hola buen día ¿Cómo está?

Creame una fast api 3 apis donde el mas importante es que envie mensajes por whatsapp teniendo encuenta lo siguiente:
http://127.0.0.1:8000/
http://127.0.0.1:8000/api/token-whatsapp/v1/
http://127.0.0.1:8000/api/whatsapp/v1/

1. utiliza authorization JWT Bearer

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

.env
JWT_SECRET_WHATSAP=your_jwt_secret_here
#y TWILIO el servicio de envio
TWILIO_ACCOUNT_SID=AC2e8a12693e513dab18627e6a491184fe
TWILIO_AUTH_TOKEN=82c96cfd3d134ac4163ef6fe85ec09e3
TWILIO_WHATSAPP_NUMBER=+14155238886
APP_NAME=FastAPI Androdri
APP_VERSION=1.0.0
APP_DESCRIPTION=Backend para la aplicación Androdri
APP_FECHAMOD=2025/10/08 9:27:01
RATE_LIMIT_MAX=10
RATE_LIMIT_WINDOW_SECONDS=60


--------------------

# test
coverage run -m pytest; coverage json -o reports/coverage.json; python dash_test/coverage_dashboard.py; coverage report -m; coverage html

# subir a docker
docker build -t japipe05/androdri-backend-contactanos:dev .
docker push japipe05/androdri-backend-contactanos:dev

# probarlo en docker local

docker run -d `
  --name androdri-backend-contactanos `
  -p 8000:8000 `
  -e SMTP_HOST="smtp.gmail.com" `
  -e SMTP_PORT="587" `
  -e SMTP_USER="felipehuchija@gmail.com" `
  -e SMTP_PASSWORD="yhjmdvmcvqidtxep" `
  -e JWT_SECRET_KEY="mi_clave_secreta_jwt_androdri1236546" `
  japipe05/androdri-backend-contactanos:dev

Estructura de carpetas (lo que implementé y qué hace cada carpeta)

androdri_api/ (raíz del repo)

app/

config/ – settings.py: configuración central (Pydantic BaseSettings). Lee .env.

models/ – Pydantic models (DTOs) para requests/responses (whatsapp_model.py, token_model.py).

routers/ – rutas / endpoints (separadas por responsabilidad):

token_router.py — endpoint de emisión de token

whatsapp_router.py — endpoint de envío (aplica verificación JWT + rate limiter)

services/ – lógica de negocio, integración con proveedores:

whatsapp_service.py — adapter para Twilio (o simulador)

utils/

jwt_utils.py — creación/verificación de JWT

rate_limiter.py — limitador por IP (in-memory)

main.py — arranque de la aplicación, CORS, inclusión de routers y handlers globales

dash_test/ — (placeholder) para dashboards/monitoring (dejé coverage_dashboard.py como marcador)

tests/ — pruebas unitarias/integración básicas (test_whatsapp_api.py)

.env.example, Dockerfile, requirements.txt, README.md



Patrones de software utilizados (y dónde)

Separation of Concerns (SoC) — routers / services / utils / models están separados para mantener responsabilidades claras.

Dependency Injection (DI) — uso de las dependencias de FastAPI (p. ej. dependencia para verificar JWT) para inyectar comportamiento (autenticación, rate limiter).

Adapter Pattern — whatsapp_service.py actúa como adaptador para Twilio; en desarrollo puede simular sin cambiar el router.

Singleton (práctico) — settings (Pydantic BaseSettings) usado centralmente como única fuente de configuración.

DTOs / Validation — Pydantic models como contratos (entrada/salida) (Data Transfer Objects).

Fail-safe / graceful degradation — si Twilio no está configurado la capa de servicio devuelve una respuesta simulada para permitir desarrollo local y testing.

Anti-Corruption Layer (ACL) idea ligera — la capa services protege al resto de la app de detalles del proveedor (Twilio).

Seguridad y JWT

Endpoint /api/token-whatsapp/v1/ devuelve JWT (HS256) cuando posteas { "api_key": "<valor>" } y el valor coincide con JWT_SECRET_WHATSAP en .env (esto es para simplificar pruebas). El token es emitido con exp.

En producción se recomienda un mecanismo con client_id + client_secret o OAuth2 client credentials, y no usar la misma clave como api_key.


# test

coverage run -m pytest
coverage json -o reports/coverage.json
coverage html -d reports/htmlcov
python dash_test/coverage_dashboard_plotly.py


pip install -r requirements.txt
uvicorn app.main:app --reload


# subir a docker
docker build -t japipe05/androdri-backend--pub-whatsapp-messages:dev .
docker push japipe05/androdri-backend--pub-whatsapp-messages:dev

docker run -d `
  --name androdri-whatsapp-backend `
  --env-file .env `
  -p 8000:8000 `
  japipe05/androdri-backend--pub-whatsapp-messages:dev
