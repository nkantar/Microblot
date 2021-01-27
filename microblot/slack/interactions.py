from microblot.cms.models import Post

from .models import SlackUser


def new_post(team_id, user_id, modal_data, private_metadata=None):
    user = SlackUser.objects.get(slack_id=user_id)
    author = user.author
    Post.objects.create_post(
        title=modal_data["post_title"],
        body=modal_data["post_body"],
        author_id=author.id,
        category_slug=modal_data["post_category"],
    )


def edit_post(team_id, user_id, modal_data, private_metadata=None):
    ...  # TODO
