import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
from pda.modulos.transacciones.aplicacion.servicios import ServicioTransaccion

import pda.seedwork.presentacion.api as api

bp = api.crear_blueprint('transacciones', '/transacciones')

@bp.route('/transaccion', methods=('POST',))
def crear_transaccion():
    try:
        #transaccion_dict = request.json

        servicio = ServicioTransaccion()
        dto_final = servicio.crear_transaccion()

        return "done"
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
