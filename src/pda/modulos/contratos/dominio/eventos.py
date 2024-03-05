from __future__ import annotations
from dataclasses import dataclass, field
from src.pda.seedwork.dominio.eventos import EventoDominio, EventoIntegracion
from datetime import datetime
import uuid

@dataclass
class AbonoContratoActualizado(EventoDominio):
    id_contrato: uuid.UUID = None
    valor: float = None
    valor_abonado: float = None
    divisa: str = None

@dataclass
class ContratoCreado(EventoIntegracion):
    id_contrato: uuid.UUID = None
    valor: float = None
    valor_abonado: float = None
    fecha_inicio: datetime = None
    fecha_vencimiento: datetime = None
    pais: str = None
    tipo_contrato: int = None
    divisa: str = None
    id_propiedad: uuid.UUID = None
