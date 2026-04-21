from sqlalchemy.orm import Session
from app.models.user import User
from app.core.security import hash_password, verify_password, create_access_token


class AuthService:

    @staticmethod
    def register(db: Session, username: str, email: str, password: str):

        user = User(
            username=username,
            email=email,
            password=hash_password(password)
        )

        db.add(user)
        db.commit()
        db.refresh(user)

        return user


    @staticmethod
    def login(db: Session, username: str, password: str):

        user = db.query(User).filter(User.username == username).first()

        if not user:
            return None

        if not verify_password(password, user.password):
            return None

        token = create_access_token({"sub": user.username})

        return token


    @staticmethod
    def change_password(db: Session, username: str, new_password: str):

        user = db.query(User).filter(User.username == username).first()

        user.password = hash_password(new_password)

        db.commit()

        return True