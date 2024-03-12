import strawberry
from .esquemas import *

@strawberry.type
class Query:
    @strawberry.field
    def country(self, name: str) -> Metrica:
        return obtener_promedio(name)
