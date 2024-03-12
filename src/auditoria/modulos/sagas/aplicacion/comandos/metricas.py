from src.auditoria.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field


@dataclass
class ActualizarPromedios(Comando):
    pais: str
    valor_arrendamiento: float
    valor_compra: float
    id_propiedad: str
    indice_confiabilidad: float

class RevertirPromedios():
    ...