from sqlalchemy import Column, String

from core import Base, IdMixin, TimestampMixin


class Category(Base, IdMixin, TimestampMixin):
    title = Column(String)
    name = Column(String)
