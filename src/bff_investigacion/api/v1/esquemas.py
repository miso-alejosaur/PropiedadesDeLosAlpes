import typing
import strawberry
import uuid
import requests
import os

COREANALITICA_ADDRESS = os.getenv("COREANALITICA_ADDRESS", default="localhost")
ID="Colombia"

def obtener_promedio(name):
    print(name)
    
    metrica_json = requests.get(f'http://{COREANALITICA_ADDRESS}:80/coreanalitica/obtener-metricas-pais/{name}').json()

    metrica = Metrica(
            pais=metrica_json["pais"], 
            valor_compra=metrica_json["valor_compra"], 
            valor_arrendamiento=metrica_json["valor_arrendamiento"]
            )

    return metrica

@strawberry.type
class Metrica:
    pais: str
    valor_compra: float
    valor_arrendamiento: float