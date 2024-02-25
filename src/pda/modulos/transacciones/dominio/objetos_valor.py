from dataclasses import dataclass
from datetime import date, time

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
