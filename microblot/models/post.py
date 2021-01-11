from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from .author import Author
from .blog import Blog
from .category import Category
from .core import Base


class Post(Base):
    title = Column(String)
    body_markdown = Column(String)
    body_html = Column(String)
    blog_id = Column(Integer, ForeignKey("blog.id"))
    author_id = Column(Integer, ForeignKey("author.id"))
    category_id = Column(Integer, ForeignKey("category.id"))

    blog = relationship("Blog", back_populates="posts")
    author = relationship("Author", back_populates="posts")
    category = relationship("Category", back_populates="posts")


Blog.posts = relationship("Post", order_by=Post.id, back_populates="blog")
Author.posts = relationship("Post", order_by=Post.id, back_populates="author")
Category.posts = relationship("Post", order_by=Post.id, back_populates="category")
