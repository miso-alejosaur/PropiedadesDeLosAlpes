import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
import requests
import os

import src.traductor.seedwork.presentacion.api as api

bp = api.crear_blueprint('traductor-json', '/traductor-json')
HOSTNAME_ENV: str = 'PDA_ADDRESS'
REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:80'

@bp.route('/contrato-comando', methods=('POST',))
def crear_contrato_asincrono():
    body = request.json
    r = requests.post(f'{REST_API_HOST}/contratos/contrato-comando', json=body)
    if r.status_code == 202:
        return Response('{}', status=202, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')


@bp.route('/transaccion-comando', methods=('POST',))
def crear_transaccion_asincrona():
    body = request.json
    r = requests.post(f'{REST_API_HOST}/transacciones/transaccion-comando', json=body)
    if r.status_code == 202:
        return Response('{}', status=202, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')

@bp.route('/transaccion', methods=('POST',))
def crear_transaccion():
    body = request.json
    r = requests.post(f'{REST_API_HOST}/transacciones/transaccion', json=body)
    if r.status_code == 200:
        return Response(r.content, status=200, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')
    