from dataclasses import dataclass
from datetime import date, time, timezone

@dataclass(frozen=True)
class Valor():
    monto: float
    
@dataclass(frozen=True)
class Fecha():
    fecha: date
    hora: time
    zona_horaria: timezone

@dataclass(frozen=True)
class Divisa():
    nombre: str
    pais: str