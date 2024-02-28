"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.pda.modulos.transacciones.dominio.objetos_valor as ov
from src.pda.seedwork.dominio.entidades import AgregacionRaiz
from src.pda.modulos.transacciones.dominio.eventos import TransaccionCreada

@dataclass
class Transaccion(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fecha: ov.Fecha = field(default_factory=ov.Fecha)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    contrato: ov.Contrato = field(default_factory=ov.Contrato)

    def crear_transaccion(self, transaccion: Transaccion):
        self.valor = transaccion.valor
        self.fecha = transaccion.fecha
        self.divisa = transaccion.divisa
        self.contrato = transaccion.contrato

        self.agregar_evento(TransaccionCreada(id_transaccion=self.id, valor=self.valor, fecha=self.fecha.fecha, divisa=self.divisa.codigo, contrato=self.contrato.id_contrato))
    