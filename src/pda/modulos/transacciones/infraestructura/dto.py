from sqlalchemy import Column, String, DateTime, Integer, Float, ForeignKey
from sqlalchemy.orm import relationship
from src.pda.config.db import db

Base = db.declarative_base()


class Divisa(db.Model):
    __tablename__ = "divisa"
    id = db.Column(String, primary_key=True)
    pais = db.Column(String, nullable=False)
    nombre = db.Column(String, nullable=False)

    #transacciones = db.relationship("Transaccion", backref="divisa_id")

class Transaccion(db.Model):
    __tablename__ = "transaccion"
    id = db.Column(String, primary_key=True)
    valor = db.Column(Float, nullable=False)
    fecha = db.Column(String, nullable=False)
    divisa_id = db.Column(String, nullable=False)
    id_contrato = db.Column(String, nullable=False)
