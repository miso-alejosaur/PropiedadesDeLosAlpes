from pda.config.db import db

Base = db.declarative_base()

class Contrato(db.Model):
    __tablename__ = "contrato"
    id = db.Column(db.String, primary_key=True)
    valor =  db.Column(db.Float, nullable=False)
    fecha_inicio =  db.Column(db.DateTime, nullable=False)
    fecha_vencimiento =  db.Column(db.DateTime, nullable=True)
    tipo_contrato = db.Column(db.Integer, nullable=False)
    pais = db.Column(db.String, nullable=False)
    divisa = db.Column(db.String, nullable=False)
