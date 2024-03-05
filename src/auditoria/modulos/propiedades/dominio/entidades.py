"""Entidades del dominio de transacciones

"""

from __future__ import annotations
from dataclasses import dataclass, field
import src.auditoria.modulos.propiedades.dominio.objetos_valor as ov
from src.auditoria.seedwork.dominio.entidades import AgregacionRaiz
from src.auditoria.modulos.propiedades.dominio.eventos import PropiedadDisponible, IndiceConfiabilidadActualizado

@dataclass
class Propiedad(AgregacionRaiz):
    valor: ov.Valor = field(default_factory=ov.Valor)
    fechas: ov.Fechas = field(default_factory=ov.Fechas)
    tipo_propiedad: ov.TipoPropiedad = field(default_factory=ov.TipoPropiedad)
    divisa: ov.Divisa = field(default_factory=ov.Divisa)
    pais: ov.Pais = field(default_factory=ov.Pais)
    indice_confiabilidad: ov.IndiceConfiabilidad = field(default_factory=ov.IndiceConfiabilidad)
    
    def actualizar_indice_confiabilidad(self, propiedad: Propiedad):
        self.valor = propiedad.valor
        self.fechas = propiedad.fechas
        self.divisa = propiedad.divisa
        self.tipo_propiedad = propiedad.tipo_propiedad
        self.pais = propiedad.pais
        self.indice_confiabilidad = propiedad.indice_confiabilidad

        if self.indice_confiabilidad.indice >= 0.8:
            self.agregar_evento(PropiedadDisponible(id_propiedad=self.id, 
                                                    valor_compra=self.valor.valor_compra, 
                                                    valor_arrendamiento=self.valor.valor_arrendamiento,
                                                    fecha_ultima_compra=self.fechas.fecha_ultima_compra,
                                                    fecha_ultimo_arrendamiento=self.fechas.fecha_ultimo_arrendamiento, 
                                                    divisa=self.divisa.codigo,
                                                    pais=self.pais.nombre,
                                                    indice_confiabilidad=self.indice_confiabilidad.indice))
        else:
            self.agregar_evento(IndiceConfiabilidadActualizado(id_propiedad=self.id, 
                                                    valor_compra=self.valor.valor_compra, 
                                                    valor_arrendamiento=self.valor.valor_arrendamiento,
                                                    fecha_ultima_compra=self.fechas.fecha_ultima_compra,
                                                    fecha_ultimo_arrendamiento=self.fechas.fecha_ultimo_arrendamiento, 
                                                    divisa=self.divisa.codigo,
                                                    pais=self.pais.nombre,
                                                    indice_confiabilidad=self.indice_confiabilidad.indice))
