from pda.config.db import db

Base = db.declarative_base()

class Divisa(db.Model):
    __tablename__ = "divisas"
    id = db.Column(db.String, primary_key=True)
    pais = db.Column(db.String, nullable=False)
    nombre = db.Column(db.String, nullable=False)

    transacciones = db.relationship("Transaccion", backref="divisa")

class Transaccion(db.Model):
    __tablename__ = "transacciones"
    id = db.Column(db.String, primary_key=True)
    valor =  db.Column(db.Float, nullable=False)
    fecha =  db.Column(db.DateTime, nullable=False)
    divisa_id = db.Column(db.String, db.ForeignKey("divisa.id"))
