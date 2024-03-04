"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.coreanalitica.modulos.propiedades.dominio.objetos_valor as ov
from src.coreanalitica.seedwork.dominio.entidades import AgregacionRaiz
from src.coreanalitica.modulos.propiedades.dominio.eventos import PromediosValoresActualizados

@dataclass
class Metricas(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    pais: ov.Pais = field(default_factory=ov.Pais)
    
    def actualizar_valores(self, metrica: Metricas, arrendamiento: float, compra: float):
        self.valor = metrica.valor
        self.pais = metrica.pais

        self.agregar_evento(PromediosValoresActualizados(id=self.pais,
                                                         self = ov.Valor(valor_arrendamiento=metrica.valor.valor_arrendamiento + arrendamiento,
                                                                         valor_compra=metrica.valor.valor_compra + compra)))