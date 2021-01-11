from sqlalchemy import Column, DateTime, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.sql import func


Base = declarative_base()


class IdMixin:
    id = Column(Integer, primary_key=True)


class TimestampMixin:
    created_at = Column(DateTime(timezone=True), default=func.now())
    modified_at = Column(DateTime(timezone=True), onupdate=func.utc_timestamp())
