from datetime import datetime
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.modulos.propiedades.dominio.objetos_valor import Valor, Pais
from src.coreanalitica.modulos.propiedades.infraestructura.dto import Metricas as MetricasDTO
from src.coreanalitica.seedwork.dominio.repositorios import Mapeador

class MapeadorMetrica(Mapeador):
    def obtener_tipo(self) -> type:
        return Metricas.__class__

    def entidad_a_dto(self, entidad: Metricas) -> MetricasDTO:
        metricas_dto = MetricasDTO()
        metricas_dto.id = str(entidad.id)
        metricas_dto.current_count = 1
        metricas_dto.valor_compra_avg = entidad.valor.valor_compra_avg
        metricas_dto.valor_arrendamiento_avg = entidad.valor.valor_arrendamiento_avg
        metricas_dto.pais = entidad.pais.nombre

        return metricas_dto

    def dto_a_entidad(self, dto: MetricasDTO) -> Metricas:
        metricas = Metricas(id=dto.id, 
                              valor=Valor(valor_compra=dto.valor_compra_avg, valor_arrendamiento=dto.valor_arrendamiento_avg),
                              pais=Pais(nombre=dto.pais))

        return metricas
