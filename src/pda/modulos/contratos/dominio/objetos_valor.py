from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from src.pda.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Valor(ObjetoValor):
    monto: float
    abono: float

@dataclass(frozen=True)
class Fechas(ObjetoValor):
    fecha_inicio: date
    fecha_vencimiento: date

@dataclass(frozen=True)
class Divisa(ObjetoValor):
    codigo: str

@dataclass(frozen=True)
class TipoContrato(ObjetoValor):
    tipo_contrato: int

@dataclass(frozen=True)
class Pais(ObjetoValor):
    nombre: str 

class TipoContratoEnum(Enum):
    COMPRA_VENTA = 1
    ARRENDAMIENTO = 2