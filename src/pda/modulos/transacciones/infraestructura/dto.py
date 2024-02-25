from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship

from src.pda.config.base import Base

class Divisa(Base):
    __tablename__ = "divisa"
    id = Column(String, primary_key=True)
    pais = Column(String, nullable=False)
    nombre = Column(String, nullable=False)

    transacciones = relationship("Transaccion", backref="divisa")

class Transaccion(Base):
    __tablename__ = "transaccion"
    id = Column(String, primary_key=True)
    valor = Column(Float, nullable=False)
    fecha = Column(DateTime, nullable=False)
    divisa_id = Column(String, ForeignKey("divisa.id"))
    id_contrato = Column(String, nullable=False)
