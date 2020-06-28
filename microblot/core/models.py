from django.db.models import DateTimeField, Model, SlugField
from django.utils.functional import cached_property
from django.utils.text import slugify


class TimestampedModel(Model):
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    @cached_property
    def created_at_pretty(self):
        return self.created_at.strftime("%a %Y-%m-%d")


class SlugifiedModel(Model):
    slug = SlugField(max_length=128, unique=True)

    class Meta:
        abstract = True
