from dataclasses import dataclass, field
from src.auditoria.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class MetricaDTO(DTO):
    valor_compra: float = field(default_factory=float)
    valor_arrendamiento: float = field(default_factory=float)
    pais: str = field(default_factory=str)

