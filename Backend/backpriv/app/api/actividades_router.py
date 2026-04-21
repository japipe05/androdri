from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.actividades import Actividad

router = APIRouter(prefix="/actividades")


@router.post("/")
def create(data: dict, db: Session = Depends(get_db)):

    obj = Actividad(**data)

    db.add(obj)

    db.commit()

    db.refresh(obj)

    return obj


@router.get("/")
def list_all(db: Session = Depends(get_db)):

    return db.query(Actividad).all()


@router.put("/{id_act}")
def update(id_act: int, data: dict, db: Session = Depends(get_db)):

    obj = db.query(Actividad).get(id_act)

    for key, value in data.items():
        setattr(obj, key, value)

    db.commit()

    return obj


@router.delete("/{id_act}")
def delete(id_act: int, db: Session = Depends(get_db)):

    obj = db.query(Actividad).get(id_act)

    db.delete(obj)

    db.commit()

    return {"message": "deleted"}