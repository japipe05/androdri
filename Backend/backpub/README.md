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

# App meta
APP_NAME=nombre
APP_VERSION="1.0.0"
APP_DESCRIPTION=descripcion
APP_FECHAMOD=fecha
# CORS
ALLOWED_ORIGINS=urls

SENDGRID_API_KEY=hasch twillo
EMAIL_FROM=correo emisor
EMAIL_TO=correo receptor
```

## 💻 Instalación local

```bash
pip install -r requirements.txt
pip install -r requirements.txt --upgrade

uvicorn app.main:app --reload

uvicorn app.main:app --host 0.0.0.0 --port 8000
```

## 🧪 Pruebas

Ejecutar pruebas unitarias:

```bash
pytest -v

python dash_test/run_coverage_dashboard.py
```

---

## 🐳 Despliegue con Docker

```bash

docker build -t japipe05/androdri-backend-pub:1.0.0-prod .

docker push japipe05/androdri-backend-pub:1.0.0-prod

docker run -d `
  --name androdri-backend-pub `
  --env-file .env `
  -p 8000:8000 `
  japipe05/androdri-backend-pub:1.0.0-prod
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
