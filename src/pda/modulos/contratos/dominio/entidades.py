"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.pda.modulos.contratos.dominio.objetos_valor as ov
from src.pda.seedwork.dominio.entidades import AgregacionRaiz
from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado

@dataclass
class Contrato(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fechas: ov.Fechas = field(default_factory=ov.Fechas)
    tipo_contrato: ov.TipoContrato = field(default_factory=ov.TipoContrato)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    pais: ov.Pais = field(default_factory=ov.Pais)
    
    def actualizar_abono_contrato(self, contrato: Contrato, abono: float):
        self.valor = ov.Valor(monto=contrato.valor.monto, abono=contrato.valor.abono + abono)
        self.fechas = contrato.fechas
        self.divisa = contrato.divisa
        self.tipo_contrato = contrato.tipo_contrato
        self.pais = contrato.pais

        self.agregar_evento(AbonoContratoActualizado(id_contrato=self.id, valor=self.valor.monto, valor_abonado=self.valor.abono, divisa=self.divisa.codigo))