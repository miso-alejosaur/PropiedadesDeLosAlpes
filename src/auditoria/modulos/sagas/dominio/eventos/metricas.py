from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

class EventoMetricas(EventoDominio):
    ...

@dataclass
class PromediosValoresActualizados(EventoMetricas):
    valor_compra: float = None
    id_correlacion: str = None
    valor_arrendamiento: float = None
    pais: str = None
    id_propiedad: str = None

@dataclass
class PromediosActualizacionFallida(EventoMetricas):
    id_propiedad: str = None
    valor_compra: float = None
    id_correlacion: str = None
    valor_arrendamiento: float = None
    pais: str = None
    indice_confiabilidad: float = None