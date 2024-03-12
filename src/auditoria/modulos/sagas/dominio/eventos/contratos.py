from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

class EventoContrato(EventoDominio):
    ...

@dataclass
class ContratoCreado(EventoContrato):
    id_contrato: uuid.UUID = None
    id_correlacion: str = None
    valor: float = None
    valor_abonado: float = None
    fecha_inicio: datetime = None
    fecha_vencimiento: datetime = None
    pais: str = None
    tipo_contrato: int = None
    divisa: str = None
    id_propiedad: uuid.UUID = None

@dataclass
class CreacionContratoFallido(EventoContrato):
    id_contrato: uuid.UUID = None
    id_correlacion: str = None
    valor: float = None
    valor_abonado: float = None
    fecha_inicio: datetime = None
    fecha_vencimiento: datetime = None
    pais: str = None
    tipo_contrato: int = None
    divisa: str = None
    id_propiedad: uuid.UUID = None
