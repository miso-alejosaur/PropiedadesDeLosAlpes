import src.pda.seedwork.presentacion.api as api
import json
from src.pda.modulos.contratos.aplicacion.servicios import ServicioContrato

from src.pda.modulos.contratos.aplicacion.mapeadores import MapContratoDTOJson
from src.pda.modulos.contratos.aplicacion.queries.obtener_contrato import ObtenerContrato
from src.pda.seedwork.aplicacion.queries import ejecutar_query

bp = api.crear_blueprint('contratos', '/contratos')

@bp.route('/contrato-query/<id>', methods=('GET',))
def dar_contrato_usando_query(id=None):
    if id:
        query_resultado = ejecutar_query(ObtenerContrato(id))
        map_contrato = MapContratoDTOJson()
        
        return map_contrato.dto_a_externo(query_resultado.resultado)
    else:
        return [{'message': 'GET!'}]