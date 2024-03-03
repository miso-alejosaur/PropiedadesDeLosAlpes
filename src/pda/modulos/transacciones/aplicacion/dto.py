
from dataclasses import dataclass, field

from src.pda.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class TransaccionDTO(DTO):
    valor: float = field(default_factory=float)
    fecha: str = field(default_factory=str)
    divisa: str = field(default_factory=str)
    contrato: str = field(default_factory=str)
