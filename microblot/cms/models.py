import uuid

import markdown

from django.conf import settings
from django.contrib.sites.models import Site
from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    Manager,
    OneToOneField,
    TextField,
)

from microblot.core.models import TimestampedModel, SlugifiedModel


class BlogManager(Manager):
    @classmethod
    def create_blog(cls, slug, name):
        site = Site.objects.create(domain=f"{slug}.{settings.MAIN_DOMAIN}", name=name)
        blog = Blog.objects.create(slug=slug, site=site)
        return blog

    # TODO delete Site on Blog deletion as well


class Blog(TimestampedModel, SlugifiedModel):
    site = OneToOneField(Site, on_delete=CASCADE)

    objects = BlogManager()


class Author(TimestampedModel, SlugifiedModel):
    name = CharField(max_length=128)

    blog = ForeignKey(Blog, on_delete=CASCADE)


class Category(TimestampedModel, SlugifiedModel):
    pass


class PostManager(Manager):
    @classmethod
    def create_post(cls, title, body, author_id, category_id):
        html = markdown.markdown(body)

        # TODO ensure short_code is unique
        # TODO maybe use SlugifiedModel.slug for short_code?
        short_code = str(uuid.uuid4()).replace("-", "")[: settings.SHORT_CODE_LENGTH]

        author = Author.objects.get(pk=author_id)

        post = Post.objects.create(
            title=title,
            body_markdown=markdown,
            body_html=html,
            short_code=short_code,
            blog_id=author.blog_id,
            author_id=author_id,
            category_id=category_id,
        )
        return post


class Post(TimestampedModel):
    title = CharField(max_length=128)
    body_markdown = TextField()
    body_html = TextField()
    short_code = CharField(max_length=16)

    blog = ForeignKey(Blog, on_delete=CASCADE)
    author = ForeignKey(Author, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)

    objects = PostManager()
