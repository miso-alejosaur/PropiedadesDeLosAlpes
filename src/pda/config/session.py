from sqlalchemy.orm import sessionmaker
from src.pda.config.engine import engine

Session = sessionmaker(bind=engine())