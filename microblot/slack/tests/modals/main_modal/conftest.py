from dataclasses import dataclass

import pytest

from microblot.slack.modals import POST_ROW_MAX


@dataclass
class FakePost:
    title: str
    id: str


@pytest.fixture(scope="module")
def no_drafts_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Your unpublished drafts (0)",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "You have no unpublished drafts.",
            },
        },
    ]
    return group


@pytest.fixture(scope="module")
def no_posts_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Your published posts (0)",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "You have no published posts.",
            },
        },
    ]
    return group


@pytest.fixture(scope="module")
def one_draft_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": "Your unpublished drafts (1)",
                "emoji": True,
            },
        },
        {
            "type": "section",
            "text": {
                "type": "mrkdwn",
                "text": "title 1",
            },
            "accessory": {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "Edit :pencil2:",
                    "emoji": True,
                },
                "value": "id 1",
                "action_id": "edit_post_button",
            },
        },
    ]
    return group


@pytest.fixture(scope="module")
def max_posts_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your published posts ({POST_ROW_MAX})",
                "emoji": True,
            },
        },
        *[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"title {idx}",
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Edit :pencil2:",
                        "emoji": True,
                    },
                    "value": f"id {idx}",
                    "action_id": "edit_post_button",
                },
            }
            for idx in range(POST_ROW_MAX)
        ],
    ]
    return group


@pytest.fixture(scope="module")
def more_drafts_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your unpublished drafts ({POST_ROW_MAX + 1})",
                "emoji": True,
            },
        },
        *[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"title {idx}",
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Edit :pencil2:",
                        "emoji": True,
                    },
                    "value": f"id {idx}",
                    "action_id": "edit_post_button",
                },
            }
            for idx in range(POST_ROW_MAX)
        ],
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "See all your unpublished drafts :notebook:",
                        "emoji": True,
                    },
                    "value": "",
                    "action_id": "all_drafts_button",
                }
            ],
        },
    ]
    return group


@pytest.fixture(scope="module")
def more_posts_group():
    group = [
        {
            "type": "header",
            "text": {
                "type": "plain_text",
                "text": f"Your published posts ({POST_ROW_MAX + 1})",
                "emoji": True,
            },
        },
        *[
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": f"title {idx}",
                },
                "accessory": {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "Edit :pencil2:",
                        "emoji": True,
                    },
                    "value": f"id {idx}",
                    "action_id": "edit_post_button",
                },
            }
            for idx in range(POST_ROW_MAX)
        ],
        {
            "type": "actions",
            "elements": [
                {
                    "type": "button",
                    "text": {
                        "type": "plain_text",
                        "text": "See all your published posts :notebook_with_decorative_cover:",
                        "emoji": True,
                    },
                    "value": "",
                    "action_id": "all_posts_button",
                }
            ],
        },
    ]
    return group


def main_modal(drafts, posts):
    modal = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "Microblot",
            "emoji": True,
        },
        "close": {
            "type": "plain_text",
            "text": "Close",
            "emoji": True,
        },
        "blocks": [
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "foo: <bar|baz>",
                },
            },
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "New post :page_facing_up:",
                            "emoji": True,
                        },
                        "value": "",
                        "action_id": "new_post_button",
                    }
                ],
            },
            *drafts,
            *posts,
        ],
    }
    return modal


@pytest.fixture(scope="module")
def one_post():
    post = FakePost("title 1", "id 1")
    return post


@pytest.fixture(scope="module")
def max_posts():
    posts = [FakePost(f"title {idx}", f"id {idx}") for idx in range(POST_ROW_MAX)]
    return posts


@pytest.fixture(scope="module")
def more_posts():
    posts = [FakePost(f"title {idx}", f"id {idx}") for idx in range(POST_ROW_MAX + 1)]
    return posts


@pytest.fixture(scope="module")
def main_modal_empty(no_drafts_group, no_posts_group):
    modal = main_modal(no_drafts_group, no_posts_group)
    return modal


@pytest.fixture(scope="module")
def main_modal_up_to_max(one_draft_group, max_posts_group):
    modal = main_modal(one_draft_group, max_posts_group)
    return modal


@pytest.fixture(scope="module")
def main_modal_more(more_drafts_group, more_posts_group):
    modal = main_modal(more_drafts_group, more_posts_group)
    return modal
