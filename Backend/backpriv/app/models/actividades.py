from sqlalchemy import Column, Integer, String, Date, Time, DateTime
from sqlalchemy.sql import func
from app.database.base import Base


class Actividad(Base):

    __tablename__ = "actividades"

    id_act = Column(Integer, primary_key=True, index=True)

    tipo_nit = Column(String(50))
    nit = Column(String(50))

    area = Column(String(100))
    tipo = Column(String(100))

    id_ot = Column(String(100))

    descripcion = Column(String(500))

    fecha = Column(Date)
    hora = Column(Time)

    usuario = Column(String(100))

    fecha_creacion = Column(DateTime, server_default=func.now())