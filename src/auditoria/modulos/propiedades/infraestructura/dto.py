from sqlalchemy import Column, String, DateTime, Integer, Float
from src.auditoria.config.db import db

Base = db.declarative_base()

class Propiedad(db.Model):
    __tablename__ = "propiedad"
    id = db.Column(String, primary_key=True)
    valor_compra =  db.Column(Float, nullable=False)
    valor_arrendamiento =  db.Column(Float, nullable=False)
    fecha_ultima_compra =  db.Column(DateTime)
    fecha_ultimo_arrendamiento =  db.Column(DateTime)
    tipo_propiedad = db.Column(Integer, nullable=False)
    pais = db.Column(String, nullable=False)
    divisa = db.Column(String, nullable=False)
    indice_confiabilidad = db.Column(Float, nullable=False)
