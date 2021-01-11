from sqlalchemy import Column, String

from core import Base, IdMixin, TimestampMixin


class Blog(Base, IdMixin, TimestampMixin):
    slug = Column(String)
    name = Column(String)
