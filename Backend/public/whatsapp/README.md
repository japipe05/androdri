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

# Patrones

| Patrón                               | Dónde se usa          | Propósito principal                        |
| ------------------------------------ | --------------------- | ------------------------------------------ |
| **Factory Pattern**                  | `settings.py`         | Crear configuraciones centralizadas        |
| **Service Layer Pattern**            | `whatsapp_service.py` | Separar lógica de negocio de controladores |
| **Router Pattern**                   | `whatsapp_router.py`  | Modularizar endpoints por dominio          |
| **Dependency Injection (implícito)** | Router → Servicio     | Desacoplar dependencias                    |
| **Exception Handling Pattern**       | Servicio              | Manejar errores externos con consistencia  |

# ejecutra requerimientos
pip install -r requirements.txt
pip install -r requirements.txt --upgrade

# Ejecutar aplicacion
uvicorn app.main:app --reload

# test
coverage run -m pytest; coverage json -o reports/coverage.json; python dash_test/coverage_dashboard.py; coverage report -m; coverage html

# subir a docker
docker build -t japipe05/androdri-backend-whatsapp:dev .
docker push japipe05/androdri-backend-whatsapp:dev

# probarlo en docker local
docker run -d -p 8000:8000 --name androdri-backend-whatsapp `
  -e TWILIO_ACCOUNT_SID=AC2e8a12693e513dab18627e6a491184fe `
  -e TWILIO_AUTH_TOKEN=82c96cfd3d134ac4163ef6fe85ec09e3 `
  -e TWILIO_WHATSAPP_NUMBER=+14155238886 `
  japipe05/androdri-backend-whatsapp:dev


