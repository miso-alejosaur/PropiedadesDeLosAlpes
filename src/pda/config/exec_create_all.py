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

def engine(username=os.getenv("DB_USER"),
       host=os.getenv("DB_HOST"),
       database=os.getenv("DB_NAME"),
       password=os.getenv("DB_PASSWORD"),
       port=os.getenv("DB_PORT")
       ):
    
    engine = create_engine(
        url_postgresql_for_create_engine(username, host, database, password, port)
    )
    
    return engine