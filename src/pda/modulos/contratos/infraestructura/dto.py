from sqlalchemy import Column, String, DateTime, Integer, Float
from src.pda.config.db import db

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contrato"
    id = db.Column(String, primary_key=True)
    valor =  db.Column(Float, nullable=False)
    fecha_inicio =  db.Column(DateTime, nullable=False)
    fecha_vencimiento =  db.Column(DateTime, nullable=True)
    tipo_contrato = db.Column(Integer, nullable=False)
    pais = db.Column(String, nullable=False)
    divisa = db.Column(String, nullable=False)
    valor_abonado = db.Column(Float, nullable=False)
