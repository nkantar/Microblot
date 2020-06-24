import json

import requests

from django.conf import settings
from django.db.models import (
    CASCADE,
    CharField,
    ForeignKey,
    PositiveIntegerField,
    TextField,
)

from microblot.authors.models import Author
from microblot.blogs.models import Blog
from microblot.categories.models import Category
from microblot.core.models import TimestampedModel


class Post(TimestampedModel):
    title = CharField(max_length=128)
    body_md = TextField()
    body_html = TextField()

    blog = ForeignKey(Blog, on_delete=CASCADE)
    category = ForeignKey(Category, on_delete=CASCADE)
    author = ForeignKey(Author, on_delete=CASCADE)

    def save(self, *args, **kwargs):
        self.body_html = self.render_body()
        super(Post, self).save(*args, **kwargs)

    def render_body(self):
        response = requests.post(
            settings.GITHUB_MARKDOWN_API_URL, data=json.dumps({"text": self.body_md}),
        )
        return response.text

    def __str__(self):
        return f"[{self.id}] {self.title} [{self.blog}]"
