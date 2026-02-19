from pydantic import BaseModel, EmailStr

class ContactMail(BaseModel):
    name: str
    email: EmailStr
    message: str
