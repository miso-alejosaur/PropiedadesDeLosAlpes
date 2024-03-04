import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.coreanalitica.modulos.propiedades.aplicacion.mapeadores import MapMetricaDTOJson
from src.coreanalitica.seedwork.dominio.excepciones import ExcepcionDominio
from src.coreanalitica.modulos.propiedades.infraestructura.despachadores import Despachador

import src.auditoria.seedwork.presentacion.api as api

bp = api.crear_blueprint('coreanalitica', '/coreanalitica')
    
@bp.route('/actualizar-valores-comando/<id>', methods=('PUT',))
def actualizar_valores_asincrono(id=None):
    try:
        request_dict = request.json

        map_transaccion = MapMetricaDTOJson()
        actualizacion_dto = map_transaccion.externo_a_dto(request_dict, id)

        despachador = Despachador()
        despachador.publicar_comando(actualizacion_dto, 'comandos-metricas')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

  #Completar GET  
@bp.route('/obetener-metricas-pais/<id>', methods=('GET',))
def obetener_metricas_pais(id=None):
    try:
        request_dict = request.json

        map_transaccion = MapMetricaDTOJson()
        actualizacion_dto = map_transaccion.externo_a_dto(request_dict, id)

        despachador = Despachador()
        despachador.publicar_comando(actualizacion_dto, 'comandos-metricas')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

