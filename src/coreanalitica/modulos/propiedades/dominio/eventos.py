from __future__ import annotations
from dataclasses import dataclass, field
from src.coreanalitica.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

@dataclass
class PromediosValoresActualizados(EventoDominio):
    valor_compra: float = None
    valor_arrendamiento: float = None
    pais: str = None
    id_propiedad: str = None
    exito: int = None
    indice_confiabilidad: float = None
