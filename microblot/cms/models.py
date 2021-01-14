from django.db.models import CASCADE, CharField, ForeignKey, TextField

from microblot.core.models import TimestampedModel, SlugifiedModel


class Blog(TimestampedModel, SlugifiedModel):
    name = CharField(max_length=128)


class Author(TimestampedModel, SlugifiedModel):
    name = CharField(max_length=128)
    blog = ForeignKey(Blog, on_delete=CASCADE)


class Category(TimestampedModel, SlugifiedModel):
    pass


class Post(TimestampedModel):
    title = CharField(max_length=128)
    body_markdown = TextField()
    body_html = TextField()
    blog = ForeignKey(Blog, on_delete=CASCADE)
    author = ForeignKey(Author, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
