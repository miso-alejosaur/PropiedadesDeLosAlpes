class ExcepcionDominio(Exception):
    ...

class ExcepcionNoEncontrado(Exception):
    ...

class IdDebeSerInmutableExcepcion(ExcepcionDominio):
    def __init__(self, mensaje='El identificador debe ser inmutable'):
        self.__mensaje = mensaje
    def __str__(self):
        return str(self.__mensaje)