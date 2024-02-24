import uuid
from dataclasses import dataclass, field
from pda.seedwork.dominio.reglas import IdEntidadEsInmutable


@dataclass
class Entidad:
    _id: uuid.UUID = field(init=False, repr=False, hash=True)

    @classmethod
    def siguiente_id(self) -> uuid.UUID:
        return uuid.uuid4()

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self) -> None:
        if not IdEntidadEsInmutable(self).es_valido():
            raise Exception('El identificador de la entidad debe ser Inmutable')
        self._id = self.siguiente_id()
        
@dataclass
class AgregacionRaiz(Entidad):
    ...
