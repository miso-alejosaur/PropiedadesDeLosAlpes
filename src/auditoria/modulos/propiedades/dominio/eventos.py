from __future__ import annotations
from dataclasses import dataclass, field
from src.auditoria.seedwork.dominio.eventos import EventoDominio, EventoIntegracion
from datetime import datetime
import uuid

@dataclass
class PropiedadDisponible(EventoIntegracion):
    id_propiedad: uuid.UUID = None
    valor_compra: float = None
    valor_arrendamiento: float = None
    fecha_ultima_compra: datetime = None
    fecha_ultimo_arrendamiento: datetime = None
    pais: str = None
    divisa: str = None
    indice_confiabilidad: float = None

@dataclass
class IndiceConfiabilidadActualizado(EventoDominio):
    id_propiedad: uuid.UUID = None
    valor_compra: float = None
    valor_arrendamiento: float = None
    fecha_ultima_compra: datetime = None
    fecha_ultimo_arrendamiento: datetime = None
    pais: str = None
    divisa: str = None
    indice_confiabilidad: float = None