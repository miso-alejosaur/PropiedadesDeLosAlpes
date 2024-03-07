import typing
import strawberry
import uuid
import requests
import os

COREANALITICA_ADDRESS = os.getenv("COREANALITICA_ADDRESS", default="localhost")
ID="COL"

def obtener_promedio(root) ->  typing.List["Reserva"]:
    metrica_json = requests.get(f'http://{COREANALITICA_ADDRESS}:6161/obetener-metricas-pais/{ID}').json()


     metrica = Metrica(
            pais=metrica_json.pais, 
            valor_compra=metrica_json.valor_compra, 
            valor_arrendamiento=metrica_json.valor_arrendamiento
            )

    return metrica


@strawberry.type
class Metrica:
    id: str
    pais: str
    valor_compra: float
    valor_arrendamiento: float