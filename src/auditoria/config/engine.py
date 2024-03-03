from sqlalchemy import create_engine
from sqlalchemy.engine import URL
import os
from dotenv import load_dotenv

load_dotenv()

def url_postgresql_for_create_engine(username, host, database, password, port):
    url = URL.create(
        drivername="postgresql",
        username=username,
        host=host,
        database=database,
        password=password,
        port=port
    )
    print(url) 
    return url

def engine(username=os.getenv("DB_USER_PROPIEDADES"),
       host=os.getenv("DB_HOST_PROPIEDADES"),
       database=os.getenv("DB_NAME_PROPIEDADES"),
       password=os.getenv("DB_PASSWORD_PROPIEDADES"),
       port=os.getenv("DB_PORT_PROPIEDADES")
       ):
    
    engine = create_engine(
        url_postgresql_for_create_engine(username, host, database, password, port)
    )
    
    return engine