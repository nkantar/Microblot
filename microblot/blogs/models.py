from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.sites.models import Site
from django.db.models import CASCADE, CharField, Manager, OneToOneField

from microblot.core.models import SlugifiedModel, TimestampedModel


class BlogManager(Manager):
    def create(self, *args, **kwargs):
        kwargs["site_id"] = Site.objects.create(
            domain=f"{kwargs['slug']}.{settings.MAIN_DOMAIN}", name=self.name
        ).id
        super(BlogManager, self).create(*args, **kwargs)


class Blog(SlugifiedModel, TimestampedModel):
    name = CharField(max_length=128)
    site = OneToOneField(Site, on_delete=CASCADE)

    # structure differs per platform
    platform = JSONField()  # TODO #43

    objects = BlogManager()  # The default manager.
