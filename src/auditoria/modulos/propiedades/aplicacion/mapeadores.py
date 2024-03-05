from datetime import date, time, datetime
from src.auditoria.modulos.propiedades.aplicacion.dto import PropiedadDTO, IndiceConfiabilidadDTO
from src.auditoria.modulos.propiedades.dominio.entidades import Propiedad
from src.auditoria.modulos.propiedades.dominio.objetos_valor import IndiceConfiabilidad, Fechas, Valor, TipoPropiedad, Divisa, Pais
from src.auditoria.seedwork.dominio.repositorios import Mapeador as RepMap
from src.auditoria.seedwork.aplicacion.dto import Mapeador as AppMap

class MapeadorPropiedad(RepMap):
    _FORMATO_FECHA = '%Y-%m-%dT%H:%M:%SZ'

    def obtener_tipo(self) -> type:
        return Propiedad.__class__


    def entidad_a_dto(self, entidad: Propiedad) -> PropiedadDTO:

        return PropiedadDTO(entidad.valor.valor_compra,
                            entidad.valor.valor_arrendamiento,
                            entidad.fechas.fecha_ultima_compra.strftime(self._FORMATO_FECHA) if entidad.fechas.fecha_ultima_compra else '',
                            entidad.fechas.fecha_ultimo_arrendamiento.strftime(self._FORMATO_FECHA) if entidad.fechas.fecha_ultimo_arrendamiento else '',
                            entidad.tipo_propiedad.tipo_propiedad,
                            entidad.pais.nombre,
                            entidad.divisa.codigo,
                            entidad.indice_confiabilidad.indice)

    def dto_a_entidad(self, dto: PropiedadDTO) -> Propiedad:

        fecha_string_compra = datetime.strptime(dto.fecha_ultima_compra, self._FORMATO_FECHA)
        fecha_string_arrendamiento = datetime.strptime(dto.fecha_ultimo_arrendamiento, self._FORMATO_FECHA)

        propiedad = Propiedad(valor=Valor(dto.valor_compra, dto.valor_arrendamiento),
                              fechas=Fechas(fecha_ultima_compra=fecha_string_compra.date(),
                                            fecha_ultimo_arrendamiento=fecha_string_arrendamiento.date()),
                              tipo_propiedad=TipoPropiedad(dto.tipo_propiedad),
                              pais = Pais(dto.pais),
                              divisa=Divisa(dto.divisa),
                              indice_confiabilidad=IndiceConfiabilidad(dto.indice_confiabilidad))

        return propiedad

class MapPropiedadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> PropiedadDTO:
        propiedad_dto = PropiedadDTO(externo["valor"], externo["fechas"], externo["tipo_propiedad"], externo["pais"], externo["divisa"], externo["indice_confiabilidad"])

        return propiedad_dto

    def dto_a_externo(self, dto: PropiedadDTO) -> dict:
        return dto.__dict__

class MapIndiceConfiabilidadDTOJson(AppMap):
    def externo_a_dto(self, externo: dict, id: float) -> IndiceConfiabilidadDTO:
        propiedad_dto = IndiceConfiabilidadDTO(id, externo["indice_confiabilidad"])

        return propiedad_dto

    def dto_a_externo(self, dto: IndiceConfiabilidadDTO) -> dict:
        return dto.__dict__
