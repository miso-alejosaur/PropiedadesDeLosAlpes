from uuid import UUID
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
        metricas_dto = self.fabrica_propiedades.crear_objeto(entity, MapeadorMetrica())
        db.session.add(metricas_dto)
        db.session.commit()

    def actualizar(self, id: UUID, valor_arrendamiento: float, valor_compra: float):
        metricas_dto = db.session.query(MetricaDTO).filter(MetricaDTO.id==str(id)).one_or_none()
        if not metricas_dto:
            raise ExcepcionNoEncontrado()
        metricas_dto.valor_arrendamiento_avg = valor_arrendamiento
        metricas_dto.valor_compra_avg = valor_compra
        #Valida las reglas de negocio nuevamente
        metrica = self.fabrica_metricas.crear_objeto(metricas_dto, MapeadorMetrica())
        db.session.commit()
        return metrica

    def eliminar(self, entity_id: UUID):
        ...
