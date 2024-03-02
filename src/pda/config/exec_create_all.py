from src.pda.config.base import Base
from src.pda.config.engine import engine

#from src.pda.modulos.transacciones.infraestructura.dto import Transaccion, Divisa
#from src.pda.modulos.contratos.infraestructura.dto import  Contrato

#table_objects = [Transaccion.__table__, Divisa.__table__, Contrato.__table__]

if __name__ == "__main2__":
    Base.metadata.create_all(
        bind = engine(), 
        tables=table_objects,
        checkfirst=True
    )