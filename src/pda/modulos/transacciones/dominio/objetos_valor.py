from dataclasses import dataclass, field
from datetime import date, time
import uuid

@dataclass(frozen=True)
class Valor():
    monto: float

@dataclass(frozen=True)
class Fecha():
    fecha: date
    hora: time

@dataclass(frozen=True)
class Divisa():
    id: uuid.UUID = field(init=False, repr=False, hash=True)
    nombre: str
    pais: str
