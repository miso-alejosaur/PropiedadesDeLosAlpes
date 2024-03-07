import strawberry
import typing

from strawberry.types import Info
from bff_web import utils
from bff_web.despachadores import Despachador

from .esquemas import *

@strawberry.type
class Mutation:

    # TODO Agregue objeto de itinerarios o reserva
    @strawberry.mutation
    async def actualizar_indice_confiabilidad(self, id:str) -> ReservaRespuesta:
        payload = dict(
            indice_confiabilidad = indice_confiabilidad,
        )
        comando = dict(
            id = str(uuid.uuid4()),
            time=utils.time_millis(),
            specversion = "v1",
            type = "ComandoReserva",
            ingestion=utils.time_millis(),
            datacontenttype="AVRO",
            service_name = "BFF Web",
            data = payload
        )
        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando, "actualizar-confiabilidad-comando", "public/default/actualizar-confiabilidad-comando")
        
        return ReservaRespuesta(mensaje="Procesando Mensaje", codigo=203)