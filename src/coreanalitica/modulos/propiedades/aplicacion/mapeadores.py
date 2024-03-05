from src.coreanalitica.modulos.propiedades.aplicacion.dto import MetricaDTO
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.modulos.propiedades.dominio.objetos_valor import Valor, Pais
from src.coreanalitica.seedwork.dominio.repositorios import Mapeador as RepMap
from src.coreanalitica.seedwork.aplicacion.dto import Mapeador as AppMap

class MapeadorMetrica(RepMap):

    def obtener_tipo(self) -> type:
        return Metricas.__class__


    def entidad_a_dto(self, entidad: Metricas) -> MetricaDTO:

        return MetricaDTO(entidad.valor.valor_compra,
                            entidad.valor.valor_arrendamiento,
                            entidad.pais.nombre)

    def dto_a_entidad(self, dto: MetricaDTO) -> Metricas:

        metrica = Metricas(valor=Valor(dto.valor_compra, dto.valor_arrendamiento),
                              pais = Pais(dto.pais))

        return metrica

class MapMetricaDTOJson(AppMap):
    def externo_a_dto(self, externo: dict) -> MetricaDTO:
        propiedad_dto = MetricaDTO(externo["valor"], externo["pais"])

        return propiedad_dto

    def dto_a_externo(self, dto: MetricaDTO) -> dict:
        return dto.__dict__

