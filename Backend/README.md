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

## Ejecutar

```bash
python -m venv .venv && source .venv/bin/activate   # Windows: .venv\Scripts\activate
pip install -r requirements-dev.txt
cp .env.example .env        # y completa SMTP_USERNAME / SMTP_PASSWORD
uvicorn app.main:create_app --factory --reload
pytest -q
pytest --cov=app --cov-report=term-missing --cov-report=html:tests\html
```

Docs: http://127.0.0.1:8000/docs (deshabilitadas con ENVIRONMENT=production)

## Ejemplo

```bash
curl -X POST http://127.0.0.1:8000/api/v1/emails/send \
  -H "Content-Type: application/json" -H "X-API-Key: <tu_api_key>" \
  -d '{"receptor":"cliente@example.com","emisor":"no-reply@androdri.com","asunto":"Hola 🎉","mensaje":"Bienvenido 👋"}'
```
