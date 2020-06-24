from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.sites.models import Site
from django.db.models import CASCADE, CharField, Manager, OneToOneField

from microblot.core.models import SlugifiedModel, TimestampedModel


class BlogManager(Manager):
    def create(self, *args, **kwargs):
        domain = f"{kwargs['slug']}.{settings.MAIN_DOMAIN}"
        site = Site.objects.create(domain=domain, name=self.name)

        kwargs["site_id"] = site.id
        super(BlogManager, self).create(*args, **kwargs)


class Blog(SlugifiedModel, TimestampedModel):
    name = CharField(max_length=128)
    site = OneToOneField(Site, on_delete=CASCADE)

    # structure differs per platform
    platform = JSONField()  # TODO #43

    objects = BlogManager()

    def __str__(self):
        return f"{self.slug} [{self.name}]"
