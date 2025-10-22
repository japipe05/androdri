prompt
Hola buen día ¿Cómo está?

Creame una fast api que envie mensajes por whatsapp teniendo encuenta lo siguiente

1. utiliza authorization beares r token  mediente el .env 
2. parametros phone_number message
3. utiliza patrones de software y dime cuales utiliza
4. utiliza manejo de errores
5. utiliza estas veriones para el desarrollo PS D:\Github\androdri> python --version 
Python 3.13.9
PS D:\Github\androdri> node --version
v22.21.0
6. agrega una opcion que un computador no permita enviar mas de 10 solicitudes despues de 60 segundos le permita enviar 

7. utiliza esta estrucutra de capetas o recomiendame una y define porque por favo

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
