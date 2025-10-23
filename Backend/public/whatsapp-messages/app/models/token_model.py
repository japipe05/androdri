# ------------------------
# File: app/models/token_model.py
# ------------------------
from pydantic import BaseModel

class TokenRequest(BaseModel):
    api_key: str

class TokenResponse(BaseModel):
    access_token: str
    token_type: str = "bearer"