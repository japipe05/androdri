# 📧 Androdri Mail API — Backend de Correo Electrónico (FastAPI)

[![FastAPI](https://img.shields.io/badge/FastAPI-005571?logo=fastapi&logoColor=white)](https://fastapi.tiangolo.com/)
[![Python](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/)
[![Docker](https://img.shields.io/badge/Docker-ready-blue?logo=docker&logoColor=white)](https://hub.docker.com/r/japipe05/androdri-backend-pub002-mails)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![Build Status](https://img.shields.io/badge/tests-passing-brightgreen)]()
[![Coverage](https://img.shields.io/badge/coverage-100%25-success)]()

---

## 🧩 Descripción

**Androdri Mail API** es un backend modular y escalable desarrollado con **FastAPI**, diseñado para **enviar correos electrónicos seguros y comprimidos**.  
Implementa autenticación **JWT**, limitación de peticiones (**Rate Limiter**), y una arquitectura **desacoplada y mantenible** basada en patrones de diseño profesionales.

---

## 🚀 Características principales

- ⚡ **FastAPI** — framework moderno, rápido y tipado.  
- 🔐 **JWT Auth** — autenticación segura por token Bearer.  
- 📦 **Compresión ZIP protegida** — adjuntos comprimidos con contraseña opcional.  
- 📬 **Service Layer Pattern** — lógica de negocio modular y desacoplada.  
- 🧠 **Rate Limiter** — evita abusos de IPs con control de frecuencia.  
- ⚙️ **Configuración centralizada** — mediante `Pydantic BaseSettings` y `.env`.  
- 🧪 **Testing & Coverage Dashboard** — automatización con `pytest`.  
- 🐳 **Optimizado para Docker** — listo para despliegue productivo.  

---

## 🧱 Estructura del proyecto

```bash
androdri_api/
├── app/
│   ├── config/
│   │   └── settings.py          # Configuración global (Factory Pattern)
│   ├── models/
│   │   ├── email_model.py       # DTOs para requests/responses
│   │   └── token_model.py       # Modelos de autenticación JWT
│   ├── routers/
│   │   ├── token_router.py      # Endpoint de emisión de token
│   │   └── email_router.py      # Endpoint principal de envío de correos
│   ├── services/
│   │   └── email_service.py     # Lógica de envío de correos (Service Layer)
│   ├── utils/
│   │   ├── jwt_utils.py         # Utilidades para tokens JWT
│   │   └── rate_limiter.py      # Limitador de solicitudes por IP
│   └── main.py                  # Punto de entrada principal de la aplicación
│
├── tests/
│   └── test_email_api.py        # Pruebas unitarias e integración
│
├── .env.example                 # Variables de entorno de ejemplo
├── Dockerfile                   # Imagen optimizada para producción
├── requirements.txt             # Dependencias del proyecto
└── README.md                    # Documentación 📘
```

---

## 🧠 Patrones de diseño aplicados

| Patrón | Descripción | Archivo/Ubicación |
|--------|--------------|-------------------|
| **Factory Pattern** | Inicialización de configuración global | `config/settings.py` |
| **Service Layer Pattern** | Capa de negocio separada del controlador | `services/email_service.py` |
| **Utility Pattern** | Reutilización de funciones utilitarias | `utils/` |
| **Router Pattern** | Modularización de endpoints REST | `routers/` |

---

## ⚙️ Configuración del entorno

### 1️⃣ Crear el archivo `.env`

```bash
cp .env.example .env
```

### 2️⃣ Configurar variables principales

```bash
APP_NAME=Androdri Mail API
JWT_SECRET_KEY=tu_clave_jwt_segura
MAIL_USERNAME=tu_correo@gmail.com
MAIL_PASSWORD=tu_token_o_clave_app
MAIL_FROM=tu_correo@gmail.com
MAIL_PORT=587
MAIL_SERVER=smtp.gmail.com
```

> 💡 Compatible con Gmail, Outlook, SendGrid, Amazon SES, etc.

---

## 💻 Instalación local

```bash
pip install -r requirements.txt
pip install -r requirements.txt --upgrade
```

Ejecutar en modo desarrollo:

```bash
uvicorn app.main:app --reload
```

Modo servidor (para Docker u orquestadores):

```bash
uvicorn app.main:app --host 0.0.0.0 --port 8001
```

---

## 🔐 Endpoints principales

### 🔸 Generar token JWT

**Ruta:**  
`POST /api/token-email/v1/`

**Request**
```json
{
  "api_key": "tu_clave_jwt"
}
```

**Response**
```json
{
  "access_token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9...",
  "token_type": "bearer"
}
```

---

### 🔸 Enviar correo

**Ruta:**  
`POST /api/email/v1/`

**Headers**
```
Authorization: Bearer <JWT>
```

**Body (multipart/form-data)**  
| Campo | Tipo | Descripción |
|-------|------|-------------|
| `asunto` | string | Asunto del correo |
| `mensaje` | string | Cuerpo del mensaje |
| `comprimir` | bool | Si se debe comprimir los adjuntos |
| `password` | string | Contraseña del ZIP (opcional) |
| `archivos` | file[] | Archivos adjuntos |

**Response**
```json
{
  "message": "Correo enviado correctamente 🚀"
}
```

---

## 🧪 Pruebas

Ejecutar pruebas unitarias:

```bash
pytest -v
```

Generar cobertura visual (dashboard):

```bash
python dash_test/run_coverage_dashboard.py
```

---

## 🐳 Despliegue con Docker

### 📦 Construcción de la imagen

```bash
docker build -t japipe05/androdri-backend-pub002-mails:dev-v1.0.0-20251107 .
```

### ☁️ Subir imagen a Docker Hub

```bash
docker push japipe05/androdri-backend-pub002-mails:dev-v1.0.0-20251107
```

---

### ▶️ Ejecutar en contenedor local

```bash
docker run -d `
  --name androdri-backend-pub002-mails `
  --env-file .env `
  --network androdri-net `
  -p 8001:8000 `
  japipe05/androdri-backend-pub002-mails:dev-v1.0.0-20251107

```

Documentación interactiva:  
👉 [http://localhost:8001/docs](http://localhost:8001/docs)

---

## 🔍 Pruebas rápidas (cURL)

### 1️⃣ Generar Token
```bash
curl -X POST http://localhost:8001/api/token-email/v1/ \
-H "Content-Type: application/json" \
-d '{"api_key": "tu_clave_jwt"}'
```

### 2️⃣ Enviar Correo
```bash
curl -X POST http://localhost:8001/api/email/v1/ \
-H "Authorization: Bearer <token>" \
-F "asunto=Correo de prueba 📧" \
-F "mensaje=Este correo fue enviado desde Androdri API" \
-F "archivos=@./archivo.txt"
```

---

## 🧩 Dependencias clave

| Librería | Propósito |
|-----------|------------|
| **FastAPI** | Framework principal |
| **Uvicorn** | Servidor ASGI |
| **Pydantic** | Validación de datos |
| **python-jose** | Manejo de JWT |
| **smtplib / email.message** | Envío de correos |
| **aiofiles** | Manejo asíncrono de archivos |
| **pytest** | Testing automatizado |

---

## 📊 Métricas y CI/CD

| Tipo | Descripción |
|------|--------------|
| **CI/CD** | Preparado para pipelines de GitHub Actions / GitLab |
| **Linting** | Soporta `flake8` y `black` para estilo de código |
| **Docker Healthcheck** | Configurable para entornos productivos |
| **Testing** | 100% cobertura con pytest dashboard |

---

## 📜 Licencia

Proyecto bajo licencia **MIT**.  
Desarrollado con ❤️ por **Andres Felipe Rodríguez Roa**.

---

## 🧠 Recomendaciones de despliegue

- Utilizar un **reverse proxy** como **NGINX** o **Traefik**.  
- Configurar **auto-restart** en contenedor Docker (`--restart=always`).  
- En producción, usar variables seguras gestionadas por **Docker Secrets** o **Vault**.  
- Integrar con **Prometheus/Grafana** para monitoreo en tiempo real.  

---

> 🚀 *Androdri Mail API — simple, modular y productiva.*
