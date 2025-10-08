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
├── tests/
│   ├── test_contact_api.py
│
├── .env
└── requirements.txt

# Patrones
✔️ Factory Pattern → para inicializar la configuración (settings.py)
✔️ Service Layer Pattern → separación de la lógica de negocio en services/email_service.py
✔️ Utility Pattern → para funciones reutilizables (utils/compress_utils.py, utils/jwt_utils.py)
✔️ Router Pattern (FastAPI Modularization) → para organizar endpoints (routers/contact_router.py)

# ejecutra requerimientos
pip install -r requirements.txt
pip install -r requirements.txt --upgrade

# Ejecutar aplicacion
uvicorn app.main:app --reload

# test
coverage run -m pytest; coverage json -o reports/coverage.json; python tools/coverage_dashboard.py; coverage report -m; coverage html


To do:
Crear contenedores y probarlo

docker build -t japipe05/androdri-backend:dev .
docker push japipe05/androdri-backend:dev

docker-compose -f docker-compose.override.yml up --build -d 
