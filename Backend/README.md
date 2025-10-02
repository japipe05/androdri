androdri-fastapi/
├── app/
│   ├── main.py
│   ├── api/
│   │   └── __init__.py
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── email_router.py
│   │   └── auth_router.py
│   ├── services/
│   │   ├── __init__.py
│   │   └── email_service.py
│   ├── config/
│   │   ├── __init__.py
│   │   └── settings.py
│   ├── models/
│   │   ├── __init__.py
│   │   └── schemas.py
│   ├── utils/
│   │   ├── __init__.py
│   │   ├── compress.py
│   │   ├── security.py
│   │   └── exceptions.py
│   └── tests/
│       └── test_email.py
├── requirements.txt
├── .env.example
└── README.md

pip install -r requirements.txt
pip install -r requirements.txt --upgrade

uvicorn app.main:app --reload --port 8000

: todo
poner contraseña y validar como el auth combinarlo cuando envie el correo




probar en desarrollo

docker build -t japipe05/androdri-backend:dev .
docker push japipe05/androdri-backend:dev
docker-compose -f docker-compose.override.yml up --build -d 
