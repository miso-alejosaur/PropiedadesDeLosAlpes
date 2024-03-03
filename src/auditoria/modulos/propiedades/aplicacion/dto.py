from dataclasses import dataclass, field
from src.auditoria.seedwork.aplicacion.dto import DTO

@dataclass(frozen=True)
class PropiedadDTO(DTO):
    valor_compra: float = field(default_factory=float)
    valor_arrendamiento: float = field(default_factory=float)
    fecha_ultima_compra: str = field(default_factory=str)
    fecha_ultimo_arrendamiento: str = field(default_factory=str)
    tipo_propiedad: int = field(default_factory=int)
    divisa: str = field(default_factory=str)
    pais: str = field(default_factory=str)
    indice_confiabilidad: float = field(default_factory=float)

@dataclass(frozen=True)
class IndiceConfiabilidadDTO(DTO):
    id_propiedad: str = field(default_factory=str)
    indice_confiabilidad: float = field(default_factory=float)
