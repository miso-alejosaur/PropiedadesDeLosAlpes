
from dataclasses import dataclass, field

from pda.seedwork.aplicacion.dto import DTO


@dataclass(frozen=True)
class TransaccionDTO(DTO):
    valor: str = field(default_factory=str)
    fecha: str = field(default_factory=str)
    divisa_id: str = field(default_factory=str)
