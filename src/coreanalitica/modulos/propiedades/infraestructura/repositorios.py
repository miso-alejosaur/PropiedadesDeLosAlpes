from uuid import UUID
from src.coreanalitica.modulos.propiedades.dominio.objetos_valor import Pais, Valor
from src.coreanalitica.config.db import db
from src.coreanalitica.modulos.propiedades.dominio.entidades import Metricas
from src.coreanalitica.modulos.propiedades.dominio.fabricas import FabricaMetricas
from src.coreanalitica.modulos.propiedades.dominio.repositorios import RepositorioMetricas
from src.coreanalitica.modulos.propiedades.infraestructura.dto import Metricas as MetricaDTO
from src.coreanalitica.modulos.propiedades.infraestructura.mapeadores import MapeadorMetrica
from src.coreanalitica.seedwork.dominio.excepciones import ExcepcionNoEncontrado

class RepositorioMetricasPostgreSQL(RepositorioMetricas):
    def __init__(self):
        self.fabrica_metricas: FabricaMetricas = FabricaMetricas()

    def obtener_por_id(self, id: UUID) -> Metricas:
        metricas_dto = db.session.query(MetricaDTO).filter(MetricaDTO.id==str(id)).one_or_none()
        if not metricas_dto:
            raise ExcepcionNoEncontrado()
        return self.fabrica_metricas.crear_objeto(metricas_dto, MapeadorMetrica())

    def obtener_todos(self) -> list[Metricas]:
        # TODO
        raise NotImplementedError

    def agregar(self, entity: Metricas):
        metricas_dto = self.fabrica_metricas.crear_objeto(entity, MapeadorMetrica())
        db.session.add(metricas_dto)
        db.session.commit()

        metrica = self.fabrica_metricas.crear_objeto(metricas_dto, MapeadorMetrica())
        return metrica

    def actualizar(self, entity: Metricas):
        metricas_dto = db.session.query(MetricaDTO).filter(MetricaDTO.pais==str(entity.pais.nombre)).one_or_none()
        # Añadir query para suma y AVG desde la BD, añadir funcion de si no existe se crea
        if not metricas_dto:
            return self.agregar(entity)
    
        metricas_dto.valor_arrendamiento_avg = ((metricas_dto.valor_arrendamiento_avg * metricas_dto.current_count) + entity.valor.valor_arrendamiento) / (metricas_dto.current_count + 1)
        metricas_dto.valor_compra_avg = ((metricas_dto.valor_compra_avg * metricas_dto.current_count) + entity.valor.valor_compra) / (metricas_dto.current_count + 1)
        metricas_dto.current_count = metricas_dto.current_count + 1

        #Valida las reglas de negocio nuevamente
        metrica = self.fabrica_metricas.crear_objeto(metricas_dto, MapeadorMetrica())
        db.session.commit()
        return metrica

    def eliminar(self, entity_id: UUID):
        ...
