from fastapi import FastAPI

from microblot.models.blog import Blog
from microblot.models.author import Author
from microblot.models.utils import db_connect, create_schema, session


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}


@app.get("/create")
async def create():
    result = create_schema(db_connect())
    return {"it": "worked?", "result": result}


@app.get("/blogs")
async def blogs():
    blogs = session.query(Blog).all()
    return {
        "blogs": [
            {"slug": blog.slug, "name": blog.name, "id": blog.id} for blog in blogs
        ]
    }


@app.get("/blogs/<blog_id>")
async def blog(blog_id: int):
    blog = session.query(Blog).get(blog_id)
    return {"blog": blog}


# @app.get("/blogs/<blog_id>/posts")
# async def blog_posts():
#     ...  # TODO


@app.get("/blogs/<blog_id>/authors")
async def blog_authors(blog_id: int):
    authors = session.query(Author).filter(Author.blog_id == blog_id)
    return {"authors": authors}


# @app.get("/blogs/<blog_id>/authors/<author_id>")
# async def blog_author():
#     ...  # TODO


# @app.get("/blogs/<blog_id>/authors/<author_id>/posts")
# async def blog_author_posts():
#     ...  # TODO


# @app.get("/categories")
# async def categories():
#     ...  # TODO


# @app.get("/categories/<category_id>")
# async def category():
#     ...  # TODO


# @app.get("/categories/<category_id>/posts")
# async def category_posts():
#     ...  # TODO
