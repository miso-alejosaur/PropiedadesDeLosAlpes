import strawberry
import typing

from pulsar.schema import *
from strawberry.types import Info
from src.bff_investigacion import utils
from src.bff_investigacion.despachadores import Despachador

from src.bff_investigacion.api.v1.esquemas import ComandoActualizarIndiceConfiabilidad, ActualizarIndiceConfiabilidadPayload, ConfiabilidadRespuesta

@strawberry.type
class Mutation:
    @strawberry.mutation
    async def actualizar_indice_confiabilidad(self, id:str, indice_confiabilidad: float, info: Info) -> ConfiabilidadRespuesta:
        payload = ActualizarIndiceConfiabilidadPayload(
            id_propiedad=id,
            indice_confiabilidad=indice_confiabilidad
        )
        
        comando_integracion = ComandoActualizarIndiceConfiabilidad(data=payload)

        despachador = Despachador()
        info.context["background_tasks"].add_task(despachador.publicar_mensaje, comando_integracion, "comandos-auditoria", AvroSchema(ComandoActualizarIndiceConfiabilidad))
        
        return ConfiabilidadRespuesta(mensaje="Procesando Mensaje", codigo=203)