from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from src.auditoria.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Valor(ObjetoValor):
    valor_compra: float
    valor_arrendamiento: float

@dataclass(frozen=True)
class Fechas(ObjetoValor):
    fecha_ultima_compra: date
    fecha_ultimo_arrendamiento: date

@dataclass(frozen=True)
class Divisa(ObjetoValor):
    codigo: str

@dataclass(frozen=True)
class TipoPropiedad(ObjetoValor):
    tipo_propiedad: int

@dataclass(frozen=True)
class Pais(ObjetoValor):
    nombre: str 

@dataclass(frozen=True)
class IndiceConfiabilidad(ObjetoValor):
    indice: float 

class TipoPropiedadEnum(Enum):
    VIVIENDA = 1
    COMERCIO = 2