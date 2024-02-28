from __future__ import annotations
from dataclasses import dataclass, field
from src.pda.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class TransaccionCreada(EventoDominio):
    id_transaccion: uuid.UUID = None
    valor: float = None
    fecha: datetime = None
    divisa: str = None
    contrato: str = None
