from dataclasses import dataclass, field
from src.pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ContratoDTO(DTO):
    id: str
    valor: float
    fecha_inicio: str = field(default_factory=str)
    fecha_vencimiento: str = field(default_factory=str)
    tipo_contrato: int
    pais: str
    divisa:str
    valor_abonado: float
