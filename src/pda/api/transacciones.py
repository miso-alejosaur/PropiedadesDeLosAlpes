import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from src.pda.modulos.transacciones.aplicacion.mapeadores import MapTransaccionDTOJson
from src.pda.modulos.transacciones.aplicacion.servicios import ServicioTransaccion

import src.pda.seedwork.presentacion.api as api

bp = api.crear_blueprint('transacciones', '/transacciones')

@bp.route('/transaccion', methods=('POST',))
def crear_transaccion():
    try:
        transaccion_dict = request.json

        map_transaccion = MapTransaccionDTOJson()
        transaccion_dto = map_transaccion.externo_a_dto(transaccion_dict)

        servicio = ServicioTransaccion()
        dto_final = servicio.crear_transaccion(transaccion_dto)

        return map_transaccion.dto_a_externo(dto_final)
    except Exception as e:
        return Response(json.dumps(dict(error=str(e))), status=400, mimetype='application/json')

'''
@bp.route('/reserva', methods=('GET',))
@bp.route('/reserva/<id>', methods=('GET',))
def dar_reserva(id=None):
    if id:
        sr = ServicioReserva()
        
        return sr.obtener_reserva_por_id(id)
    else:
        return [{'message': 'GET!'}]
        '''
