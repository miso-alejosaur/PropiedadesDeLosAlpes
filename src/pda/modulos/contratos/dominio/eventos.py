from __future__ import annotations
from dataclasses import dataclass, field
from src.pda.seedwork.dominio.eventos import (EventoDominio)
from datetime import datetime
import uuid

@dataclass
class AbonoContratoActualizado(EventoDominio):
    id_contrato: uuid.UUID = None
    valor: float = None
    valor_abonado: float = None
    divisa: str = None

