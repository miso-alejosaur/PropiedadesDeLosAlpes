"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import pda.modulos.transacciones.dominio.objetos_valor as ov
from pda.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Transaccion(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fecha: ov.Fecha = field(default_factory=ov.Fecha)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    