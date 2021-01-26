from django.db.models import CASCADE, CharField, ForeignKey

from microblot.cms.models import Author, Blog
from microblot.core.models import TimestampedModel


class SlackModel(TimestampedModel):
    slack_id = CharField(max_length=16)
    icon = CharField(max_length=512)

    class Meta:
        abstract = True


class SlackWorkspace(SlackModel):
    bot_user_id = CharField(max_length=128)
    bot_access_token = CharField(max_length=128)
    blog = ForeignKey(Blog, on_delete=CASCADE)


class SlackUser(SlackModel):
    slack_username = CharField(max_length=128)
    real_name = CharField(max_length=128)
    display_name = CharField(max_length=128)
    avatar = CharField(max_length=512)
    workspace = ForeignKey(SlackWorkspace, on_delete=CASCADE)
    author = ForeignKey(Author, on_delete=CASCADE)
