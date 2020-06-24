from django.db.models import CASCADE, ForeignKey

from microblot.core.models import SlugifiedModel, TimestampedModel
from microblot.blogs.models import Blog


class Category(SlugifiedModel, TimestampedModel):
    blog = ForeignKey(Blog, on_delete=CASCADE)

    class Meta:
        verbose_name_plural = "Categories"
        unique_together = ["slug", "blog"]

    def __str__(self):
        return f"{self.slug} [{self.blog}]"
