from django.conf import settings
from django.contrib.postgres.fields import JSONField
from django.contrib.sites.models import Site
from django.db.models import CASCADE, CharField, Manager, OneToOneField

from microblot.core.models import SlugifiedModel, TimestampedModel


class BlogManager(Manager):
    def update_or_create(self, *args, **kwargs):
        domain = f"{kwargs['defaults']['slug']}.{settings.MAIN_DOMAIN}"
        site, site_created = Site.objects.update_or_create(
            blog__slack_id=kwargs["slack_id"],
            defaults={"domain": domain, "name": kwargs["defaults"]["name"]},
        )
        kwargs["site_id"] = site.id
        return super(BlogManager, self).update_or_create(*args, **kwargs)


class Blog(SlugifiedModel, TimestampedModel):
    name = CharField(max_length=128)
    site = OneToOneField(Site, on_delete=CASCADE)
    slack_id = CharField(max_length=128)

    # structure differs per platform
    # platform = JSONField()  # TODO #43

    bot_user_id = CharField(max_length=128)
    bot_access_token = CharField(max_length=128)

    objects = BlogManager()

    def __str__(self):
        return f"{self.slug} [{self.name}]"
