from dataclasses import dataclass, field
from src.pda.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class ContratoDTO(DTO):
    valor: float
    fecha_inicio: str = field(default_factory=str)
    fecha_vencimiento: str = field(default_factory=str)
    tipo_contrato: int = field(default_factory=int)
    pais: str = field(default_factory=str)
    divisa: str = field(default_factory=str)
    valor_abonado: float = field(default_factory=int)
    id_propiedad: str = field(default_factory=str)
