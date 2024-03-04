from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.eventos import EventoDominio, EventoIntegracion
from datetime import datetime
import uuid

@dataclass
class PromediosValoresActualizados(EventoDominio):
    valor_compra: float = None
    valor_arrendamiento: float = None
    pais: str = None
