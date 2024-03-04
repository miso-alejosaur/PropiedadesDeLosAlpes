from dataclasses import dataclass, field
from datetime import date
from enum import Enum
from src.coreanalitica.seedwork.dominio.objetos_valor import ObjetoValor

@dataclass(frozen=True)
class Valor(ObjetoValor):
    valor_compra: float
    valor_arrendamiento: float

@dataclass(frozen=True)
class Pais(ObjetoValor):
    nombre: str 