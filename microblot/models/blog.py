from sqlalchemy import Column, String

from .core import Base


class Blog(Base):
    slug = Column(String)
    name = Column(String)
