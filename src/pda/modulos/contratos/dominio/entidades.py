"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.pda.modulos.contratos.dominio.objetos_valor as ov
from src.pda.seedwork.dominio.entidades import AgregacionRaiz

@dataclass
class Contrato(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fechas: ov.Fechas = field(default_factory=ov.Fechas)
    tipo_contrato: ov.TipoContrato = field(default_factory=ov.TipoContrato)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    pais: ov.Pais = field(default_factory=ov.Divisa)
    