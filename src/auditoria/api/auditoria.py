import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.auditoria.modulos.propiedades.aplicacion.mapeadores import MapIndiceConfiabilidadDTOJson
from src.auditoria.seedwork.dominio.excepciones import ExcepcionDominio
from src.auditoria.modulos.propiedades.infraestructura.despachadores import Despachador

import src.auditoria.seedwork.presentacion.api as api

bp = api.crear_blueprint('auditoria', '/auditoria')
    
@bp.route('/actualizar-confiabilidad-comando/<id>', methods=('PUT',))
def actualizar_indice_confiabilidad_asincrono(id=None):
    try:
        request_dict = request.json

        map_transaccion = MapIndiceConfiabilidadDTOJson()
        actualizacion_dto = map_transaccion.externo_a_dto(request_dict, id)

        despachador = Despachador()
        despachador.publicar_comando(actualizacion_dto, 'comandos-auditoria')
        
        return Response('{}', status=202, mimetype='application/json')
    except ExcepcionDominio as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')
