from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from microblot.constants import DATABASE, DEBUG

from .core import Base


def db_connect():
    engine = create_engine(DATABASE, echo=DEBUG)
    return engine


def create_schema(engine):
    Base.metadata.create_all(engine)


Session = sessionmaker(bind=db_connect())
session = Session()
