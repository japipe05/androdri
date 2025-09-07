fastapi-contact-app/
│── app/
│   ├── api/                     
│   │   ├── v1/
│   │   │   ├── contact_route.py
│   │   │   └── __init__.py
│   │   └── __init__.py
│   │
│   ├── config/                  
│   │   ├── settings.py          # Configuración general (SMTP, DB URIs, Redis)
│   │   └── __init__.py
│   │
│   ├── models/                  
│   │   ├── contact_model.py     # Pydantic models
│   │   └── __init__.py
│   │
│   ├── services/                
│   │   ├── contact_service.py
│   │   └── __init__.py
│   │
│   ├── utils/                   
│   │   ├── email_sender.py
│   │   └── __init__.py
│   │
│   ├── db/                      # Capa de persistencia múltiple
│   │   ├── mysql/               # SQLAlchemy con MySQL
│   │   │   ├── base.py
│   │   │   ├── session.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── mongo/               # Conexión con MongoDB
│   │   │   ├── mongo_client.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── redis/               # Cliente Redis
│   │   │   ├── redis_client.py
│   │   │   └── __init__.py
│   │   │
│   │   ├── repository/          # Patrón Repository (independiente del motor)
│   │   │   └── contact_repository.py
│   │   │
│   │   └── __init__.py
│   │
│   ├── main.py                  
│   └── __init__.py
│
├── tests/                       
│   ├── test_contact.py
│   └── __init__.py
│
├── .env                         
├── requirements.txt
└── README.md


# ejecutra librerias
pip install -r requirements.txt

# Ejecutar en local
python -m uvicorn app.main:app --reload

# Ejecutar en Test
python -m pytest -v
python -m pytest --cov=app --cov-report=html
