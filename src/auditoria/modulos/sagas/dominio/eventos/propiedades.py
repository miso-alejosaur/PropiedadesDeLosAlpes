from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.eventos import EventoDominio
from datetime import datetime
import uuid

class EventoPropiedad(EventoDominio):
    ...

@dataclass
class IndiceConfiabilidadActualizado(EventoPropiedad):
    id_propiedad: uuid.UUID = None
    id_correlacion: str = None
    valor_compra: float = None
    valor_arrendamiento: float = None
    pais: str = None
    divisa: str = None
    indice_confiabilidad: float = None

@dataclass
class IndiceActualizacionFallida(EventoPropiedad):
    id_propiedad: uuid.UUID = None
    id_correlacion: str = None
    valor_compra: float = None
    valor_arrendamiento: float = None
    fecha_ultima_compra: datetime = None
    fecha_ultimo_arrendamiento: datetime = None
    pais: str = None
    divisa: str = None
    indice_confiabilidad: float = None