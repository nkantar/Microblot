from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from blog import Blog
from core import Base, IdMixin, TimestampMixin


class Author(Base, IdMixin, TimestampMixin):
    name = Column(String)
    blog_id = Column(Integer, ForeignKey("blog.id"))

    blog = relationship("Blog", back_populates="authors")


Blog.authors = relationship("Author", order_by=Author.id, back_populates="blog")
