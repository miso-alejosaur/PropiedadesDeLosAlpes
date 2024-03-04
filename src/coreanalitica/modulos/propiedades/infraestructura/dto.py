from sqlalchemy import Column, String, DateTime, Integer, Float
from src.coreanalitica.config.db import db

Base = db.declarative_base()

class Metricas(db.Model):
    __tablename__ = "metricas"
    id = db.Column(String, primary_key=True)
    valor_compra_avg =  db.Column(Float, nullable=False)
    valor_arrendamiento_avg =  db.Column(Float, nullable=False)
    current_count = db.Column(Integer, nullable=False)
    pais = db.Column(String, nullable=False)
