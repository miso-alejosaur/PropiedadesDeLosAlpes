import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.coreanalitica.modulos.propiedades.aplicacion.mapeadores import MapMetricaDTOJson
from src.coreanalitica.seedwork.dominio.excepciones import ExcepcionDominio
from src.coreanalitica.modulos.propiedades.infraestructura.despachadores import Despachador
from src.coreanalitica.modulos.propiedades.aplicacion.queries.obtener_metrica import ObtenerMetrica
from src.coreanalitica.seedwork.aplicacion.queries import ejecutar_query
from src.coreanalitica.seedwork.dominio.excepciones import ExcepcionNoEncontrado

import src.coreanalitica.seedwork.presentacion.api as api

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
@bp.route('/obtener-metricas-pais/<id>', methods=('GET',))
def obtener_metricas_pais(id=None):
    try:
        if id:
            query_resultado = ejecutar_query(ObtenerMetrica(id))
            map_metrica = MapMetricaDTOJson()
            
            return map_metrica.dto_a_externo(query_resultado.resultado)
        else:
            return [{'message': 'GET!'}]
    except ExcepcionNoEncontrado:
        return Response(json.dumps(dict(error='Metrica no encontrada.')), status=404, mimetype='application/json')
    except Exception as e:
        print(str(e))
        return Response(json.dumps(dict(error='Internal server error.')), status=500, mimetype='application/json')
