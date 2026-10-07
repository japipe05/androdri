# FastAPI androdri – Emails públicos 📧

Envío de correos HTML (con emojis) por Amazon SES SMTP.

## Arquitectura hexagonal

```
app/
├── domain/          # Entidades y excepciones (sin dependencias externas)
├── application/     # Puertos (interfaces) + caso de uso SendEmailUseCase
├── infrastructure/  # Adaptadores de salida: SES SMTP, renderer HTML, rate limiter, settings
├── interfaces/api/  # Adaptador de entrada: rutas FastAPI, schemas, errores, seguridad
├── container.py     # Composition root (inyección de dependencias)
└── main.py          # Application factory
tests/
```


## 1️⃣ Crear el archivo .env

```bash
cp .env.example .env

# App meta
#ENVIRONMENT="development"
#ENVIRONMENT="testing"
ENVIRONMENT="production"

APP_NAME="FastAPI Androdri"
APP_VERSION="1.0.0"
APP_DESCRIPTION="Backend para la aplicación Androdri"
APP_FECHAMOD="2026/10/05 9:35:01"

# CORS
ALLOWED_ORIGINS=http://127.0.0.1:8000,http://localhost:3000,https://apipub.androdri.com,https://www.androdri.com,https://androdri.com

# Amazon SES (SMTP)
SMTP_HOST=
SMTP_PORT=587
SMTP_USERNAME=
SMTP_PASSWORD=#
SMTP_TIMEOUT_SECONDS=10

# Seguridad
# Si se deja vacío, el endpoint queda sin API key (solo desarrollo).
API_KEY=""
# Dominios permitidos para "emisor" (deben estar verificados en SES). Vacío = sin restricción.
ALLOWED_SENDER_DOMAINS=

# Límite de envíos: 3 correos por ventana de 1 hora (3600 s) por cliente
RATE_LIMIT_MAX_EMAILS=3
RATE_LIMIT_WINDOW_SECONDS=3600
```

## 💻 Instalación local

```bash
pip install -r requirements-dev.txt
uvicorn app.main:create_app --factory --reload
```


## 🧪 Pruebas
```bash
pytest -q
pytest --cov=app --cov-report=term-missing --cov-report=html:tests\html
```

## Seguridad

1. Instala las herramientas recomendadas
Ejecuta estos comandos en la terminal de VS Code, desde la carpeta Backend:

```bash
python -m pip install bandit pip-audit
```
1. Bandit — analiza tu código Python
Busca posibles vulnerabilidades, uso inseguro de funciones y errores de programación relacionados con seguridad.
```bash
python -m bandit -r app -ll
```
2. pip-audit — revisa dependencias vulnerables
Comprueba si las librerías instaladas tienen vulnerabilidades conocidas publicadas.
```bash
python -m pip_audit -r requirements.txt
```

🐳 Despliegue con Docker

```bash
docker build -t japipe05/androdri-backend:1.0.0-prod .

docker push japipe05/androdri-backend:1.0.0-prod

docker run -d `
  --name androdri-backend `
  --env-file .env `
  -p 8000:8000 `
  japipe05/androdri-backend:1.0.0-prod

```


Docs: http://127.0.0.1:8000/docs (deshabilitadas con ENVIRONMENT=production)

## Ejemplo

```bash
curl -X POST http://127.0.0.1:8000/api/v1/emails/send \
  -H "Content-Type: application/json" -H "X-API-Key: <tu_api_key>" \
  -d '{"receptor":"cliente@example.com","emisor":"no-reply@androdri.com","asunto":"Hola 🎉","mensaje":"Bienvenido 👋"}'
```

ver varibles
> docker exec androdri-backend printenv API_KEY