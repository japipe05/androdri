from sqlalchemy import Column, Integer, String, Date, Float, DateTime
from sqlalchemy.sql import func
from app.database.base import Base


class Pago(Base):

    __tablename__ = "pagos"

    id_pag = Column(Integer, primary_key=True, index=True)

    tipo_nit = Column(String(50))
    nit = Column(String(50))
    nombre = Column(String(200))
    fecha = Column(Date)

    fac = Column(String(100))

    valor_usd = Column(Float)
    valor_peso = Column(Float)

    descripcion = Column(String(500))
    tipo = Column(String(50))

    usuario = Column(String(100))

    fecha_creacion = Column(DateTime, server_default=func.now())