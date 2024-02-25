from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from pda.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Valor(ObjetoValor):
    monto: float

@dataclass(frozen=True)
class Fechas():
    fecha_inicio: date
    fecha_vencimiento: date

@dataclass(frozen=True)
class Divisa():
    codigo: str

@dataclass(frozen=True)
class TipoContrato():
    tipo_contrato: int

@dataclass(frozen=True)
class Pais():
    nombre: str

class TipoContratoEnum(Enum):
    COMPRA_VENTA = 1
    ARRENDAMIENTO = 2