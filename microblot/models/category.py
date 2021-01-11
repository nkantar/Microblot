from sqlalchemy import Column, String

from .core import Base


class Category(Base):
    title = Column(String)
    name = Column(String)
