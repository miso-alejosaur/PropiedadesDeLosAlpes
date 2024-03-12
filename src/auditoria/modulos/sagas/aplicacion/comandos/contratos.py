from src.auditoria.seedwork.aplicacion.comandos import Comando
from dataclasses import dataclass, field

@dataclass
class CrearContrato(Comando):
    valor: float
    valor_abonado: float
    fecha_inicio: str
    fecha_vencimiento: str
    divisa: str
    pais: str
    tipo_contrato: int
    id_propiedad: str

class EliminarContrato(Comando):
    ...