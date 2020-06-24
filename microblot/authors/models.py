from django.db.models import CASCADE, CharField, ForeignKey, SlugField

from microblot.core.models import SlugifiedModel, TimestampedModel
from microblot.blogs.models import Blog


class Author(SlugifiedModel, TimestampedModel):
    name = CharField(max_length=128)
    slack_id = CharField(max_length=64, unique=True)
    blog = ForeignKey(Blog, on_delete=CASCADE)

    class Meta:
        unique_together = ["slug", "blog"]

    def __str__(self):
        return f"{self.name} [{self.blog}]"
