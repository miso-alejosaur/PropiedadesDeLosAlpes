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
    
    def actualizar_valores(self, metrica: Metricas, id_propiedad, exito, indice_confiabilidad):
        self.valor = metrica.valor
        self.pais = metrica.pais

        self.agregar_evento(PromediosValoresActualizados(pais =self.pais.nombre,
                                                         valor_arrendamiento=self.valor.valor_arrendamiento,
                                                         valor_compra=self.valor.valor_compra, id_propiedad=id_propiedad, exito=exito, indice_confiabilidad=indice_confiabilidad))