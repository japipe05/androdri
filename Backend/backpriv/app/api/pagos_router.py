from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.models.pagos import Pago

router = APIRouter(prefix="/pagos")


@router.post("/")
def create_pago(pago: dict, db: Session = Depends(get_db)):

    p = Pago(**pago)

    db.add(p)

    db.commit()

    db.refresh(p)

    return p


@router.get("/")
def get_pagos(db: Session = Depends(get_db)):

    return db.query(Pago).all()


@router.put("/{id_pag}")
def update_pago(id_pag: int, data: dict, db: Session = Depends(get_db)):

    pago = db.query(Pago).get(id_pag)

    for key, value in data.items():
        setattr(pago, key, value)

    db.commit()

    return pago


@router.delete("/{id_pag}")
def delete_pago(id_pag: int, db: Session = Depends(get_db)):

    pago = db.query(Pago).get(id_pag)

    db.delete(pago)

    db.commit()

    return {"message": "deleted"}