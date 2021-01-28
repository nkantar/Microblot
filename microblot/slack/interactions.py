from django.conf import settings

from microblot.cms.models import Post, PostPreview
from microblot.core.queue import enqueue_in

from .models import SlackUser


def new_post(team_id, user_id, interaction_type, modal_data, private_metadata=None):
    user = SlackUser.objects.get(slack_id=user_id)
    author = user.author

    # if submission
    if interaction_type == "view_submission":
        Post.objects.create_post(
            title=modal_data["post_title"],
            body=modal_data["post_body"],
            author_id=author.id,
            category_slug=modal_data["post_category"],
        )

    # if preview
    elif interaction_type == "block_actions":
        # generate preview
        post_review = PostPreview.objects.create_post_preview(
            title=modal_data["post_title"],
            body=modal_data["post_body"],
            author_id=author.id,
            category_slug=modal_data["post_category"],
        )

        # schedule preview deletion
        enqueue_in(settings.PREVIEW_TTL, post_review.delete)

        # update modal with link
        # TODO


def edit_post(team_id, user_id, interaction_type, modal_data, private_metadata=None):
    ...  # TODO
