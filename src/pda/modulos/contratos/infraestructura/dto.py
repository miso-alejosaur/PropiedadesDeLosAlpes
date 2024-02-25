from sqlalchemy import Column, String, DateTime, Integer, Float

from src.pda.config.base import Base

class Contrato(Base):
    __tablename__ = "contrato"
    id = Column(String, primary_key=True)
    valor =  Column(Float, nullable=False)
    fecha_inicio =  Column(DateTime, nullable=False)
    fecha_vencimiento =  Column(DateTime, nullable=True)
    tipo_contrato = Column(Integer, nullable=False)
    pais = Column(String, nullable=False)
    divisa = Column(String, nullable=False)
