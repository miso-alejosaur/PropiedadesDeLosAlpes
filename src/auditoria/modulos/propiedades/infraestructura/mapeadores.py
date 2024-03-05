from datetime import datetime
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.modulos.propiedades.dominio.objetos_valor import Divisa, Fechas, Valor, TipoPropiedad, Pais, IndiceConfiabilidad
from src.auditoria.modulos.propiedades.infraestructura.dto import Propiedad as PropiedadDTO
from src.auditoria.seedwork.dominio.repositorios import Mapeador

class MapeadorPropiedad(Mapeador):
    def obtener_tipo(self) -> type:
        return Propiedad.__class__

    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO()
        propiedad_dto.id = str(entidad.id)
        propiedad_dto.valor_compra = entidad.valor.valor_compra
        propiedad_dto.valor_arrendamiento = entidad.valor.valor_arrendamiento
        propiedad_dto.fecha_ultima_compra = datetime(entidad.fechas.fecha_ultima_compra.year, 
                                                     entidad.fechas.fecha_ultima_compra.month, 
                                                     entidad.fechas.fecha_ultima_compra.day) if entidad.fechas.fecha_ultima_compra else None
        propiedad_dto.fecha_ultimo_arrendamiento = datetime(entidad.fechas.fecha_ultimo_arrendamiento.year, 
                                                            entidad.fechas.fecha_ultimo_arrendamiento.month, 
                                                            entidad.fechas.fecha_ultimo_arrendamiento.day) if entidad.fechas.fecha_ultimo_arrendamiento else None
        propiedad_dto.divisa = entidad.divisa.codigo
        propiedad_dto.pais = entidad.pais.nombre
        propiedad_dto.tipo_propiedad = entidad.tipo_propiedad.tipo_propiedad
        propiedad_dto.indice_confiabilidad = entidad.indice_confiabilidad.indice

        return propiedad_dto

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:
        propiedad = Propiedad(id=dto.id, 
                              valor=Valor(valor_compra=dto.valor_compra, valor_arrendamiento=dto.valor_arrendamiento),
                              fechas=Fechas(fecha_ultima_compra=dto.fecha_ultima_compra, fecha_ultimo_arrendamiento=dto.fecha_ultimo_arrendamiento),
                              tipo_propiedad=TipoPropiedad(tipo_propiedad=dto.tipo_propiedad),
                              divisa=Divisa(codigo=dto.divisa),
                              pais=Pais(nombre=dto.pais),
                              indice_confiabilidad=IndiceConfiabilidad(indice=dto.indice_confiabilidad))

        return propiedad
