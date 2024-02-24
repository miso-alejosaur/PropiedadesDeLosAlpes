class IdEntidadEsInmutable():

    entidad: object

    def __init__(self, entidad):
        self.entidad = entidad

    def es_valido(self) -> bool:
        try:
            if self.entidad._id:
                return False
            return True
        except AttributeError:
            return True