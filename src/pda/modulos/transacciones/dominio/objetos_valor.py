from dataclasses import dataclass, field
from datetime import date, time
import uuid

from pda.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Valor(ObjetoValor):
    monto: float

@dataclass(frozen=True)
class Fecha():
    fecha: date
    hora: time

@dataclass(frozen=True)
class Divisa():
    codigo: str
    nombre: str
    pais: str
