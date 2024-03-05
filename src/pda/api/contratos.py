import src.pda.seedwork.presentacion.api as api
import json
from src.pda.seedwork.dominio.excepciones import ExcepcionNoEncontrado
from src.pda.modulos.contratos.aplicacion.mapeadores import MapContratoDTOJson
from src.pda.modulos.contratos.aplicacion.queries.obtener_contrato import ObtenerContrato
from src.pda.seedwork.aplicacion.queries import ejecutar_query
from src.pda.modulos.contratos.infraestructura.despachadores import Despachador
from src.pda.seedwork.dominio.excepciones import ExcepcionDominio
from flask import redirect, render_template, request, session, url_for
from flask import Response

bp = api.crear_blueprint('contratos', '/contratos')

@bp.route('/contrato-query/<id>', methods=('GET',))
def dar_contrato_usando_query(id=None):
    try:
        if id:
            query_resultado = ejecutar_query(ObtenerContrato(id))
            map_contrato = MapContratoDTOJson()
            
            return map_contrato.dto_a_externo(query_resultado.resultado)
        else:
            return [{'message': 'GET!'}]
    except ExcepcionNoEncontrado:
        return Response(json.dumps(dict(error='Contrato no encontrado.')), status=404, mimetype='application/json')
    except Exception as e:
        print(str(e))
        return Response(json.dumps(dict(error='Internal server error.')), status=500, mimetype='application/json')

@bp.route('/contrato-comando', methods=('POST',))
def crear_contrato_asincrono():
    try:
        contrato_dict = request.json

        map_transaccion = MapContratoDTOJson()
        contrato_dto = map_transaccion.externo_a_dto(contrato_dict)

        despachador = Despachador()
        despachador.publicar_comando(contrato_dto, 'comandos-crear-contrato')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')