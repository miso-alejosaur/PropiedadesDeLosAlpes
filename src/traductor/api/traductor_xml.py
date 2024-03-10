import json
from flask import redirect, render_template, request, session, url_for
from flask import Response
import requests
import os

import xml.etree.ElementTree as E

import src.traductor.seedwork.presentacion.api as api

bp = api.crear_blueprint('traductor-xml', '/traductor-xml')
HOSTNAME_ENV: str = 'PDA_ADDRESS'
REST_API_HOST: str = f'http://{os.getenv(HOSTNAME_ENV, default="localhost")}:80'

def contruir_body(xml):
    root = E.fromstring(xml)
    body = {}
    for child in root:
        body[child.tag] = child.text
    return body


@bp.route('/contrato-comando', methods=('POST',))
def crear_contrato_asincrono():
    body = contruir_body(request.data)
    r = requests.post(f'{REST_API_HOST}/contratos/contrato-comando', json=body)
    if r.status_code == 202:
        return Response('{}', status=202, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')


@bp.route('/transaccion-comando', methods=('POST',))
def crear_transaccion_asincrona():
    body = contruir_body(request.data)
    r = requests.post(f'{REST_API_HOST}/transacciones/transaccion-comando', json=body)
    if r.status_code == 202:
        return Response('{}', status=202, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')

@bp.route('/transaccion', methods=('POST',))
def crear_transaccion():
    body = contruir_body(request.data)
    r = requests.post(f'{REST_API_HOST}/transacciones/transaccion', json=body)
    print(r.content, body)
    if r.status_code == 200:
        return Response(r.content, status=200, mimetype='application/json')
    else:
        return Response('Internal server error', status=500, mimetype='application/json')
    