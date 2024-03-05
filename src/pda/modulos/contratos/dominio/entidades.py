"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.pda.modulos.contratos.dominio.objetos_valor as ov
from src.pda.seedwork.dominio.entidades import AgregacionRaiz
from src.pda.modulos.contratos.dominio.eventos import AbonoContratoActualizado, ContratoCreado

@dataclass
class Contrato(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fechas: ov.Fechas = field(default_factory=ov.Fechas)
    tipo_contrato: ov.TipoContrato = field(default_factory=ov.TipoContrato)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    pais: ov.Pais = field(default_factory=ov.Pais)
    id_propiedad: ov.Propiedad = field(default_factory=ov.Propiedad)
    
    def actualizar_abono_contrato(self, contrato: Contrato, abono: float):
        self.valor = ov.Valor(monto=contrato.valor.monto, abono=contrato.valor.abono + abono)
        self.fechas = contrato.fechas
        self.divisa = contrato.divisa
        self.tipo_contrato = contrato.tipo_contrato
        self.pais = contrato.pais

        self.agregar_evento(AbonoContratoActualizado(id_contrato=self.id, valor=self.valor.monto, valor_abonado=self.valor.abono, divisa=self.divisa.codigo))
    
    def crear_contrato(self, contrato: Contrato):
        self.valor = contrato.valor
        self.fechas = contrato.fechas
        self.divisa = contrato.divisa
        self.tipo_contrato = contrato.tipo_contrato
        self.pais = contrato.pais
        self.id_propiedad = contrato.id_propiedad

        self.agregar_evento(ContratoCreado(id_contrato=self.id, valor=self.valor.monto, valor_abonado=self.valor.abono, fecha_inicio=self.fechas.fecha_inicio, 
                                           fecha_vencimiento=self.fechas.fecha_vencimiento, pais=self.pais.nombre, divisa=self.divisa.codigo, tipo_contrato=self.tipo_contrato.tipo_contrato,
                                           id_propiedad=self.id_propiedad.id_propiedad))