from src.coreanalitica.seedwork.aplicacion.queries import Query, QueryHandler, QueryResultado
from src.coreanalitica.seedwork.aplicacion.queries import ejecutar_query as query
from src.coreanalitica.modulos.propiedades.infraestructura.repositorios import RepositorioMetricas
from dataclasses import dataclass
from .base import MetricasQueryBaseHandler
from src.coreanalitica.modulos.propiedades.aplicacion.mapeadores import MapeadorMetrica
import uuid

@dataclass
class ObtenerMetrica(Query):
    id: str

class ObtenerMetricaHandler(MetricasQueryBaseHandler):

    def handle(self, query: ObtenerMetrica) -> QueryResultado:
        repositorio = self.fabrica_repositorio.crear_objeto(RepositorioMetricas.__class__)
        metrica =  self.fabrica_metrica.crear_objeto(repositorio.obtener_por_id(query.id), MapeadorMetrica())
        return QueryResultado(resultado=metrica)

@query.register(ObtenerMetrica)
def ejecutar_query_obtener_metrica(query: ObtenerMetrica):
    handler = ObtenerMetricaHandler()
    return handler.handle(query)