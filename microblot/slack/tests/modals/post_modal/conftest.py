import pytest


def post_modal(
    modal_title,
    post_title,
    post_body,
    post_category,
    private_metadata,
    draft_button,
    delete_button,
):
    modal = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "Microblot",
            "emoji": True,
        },
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True,
        },
        "submit": {
            "type": "plain_text",
            "text": "Publish",
            "emoji": True,
        },
        "private_metadata": private_metadata,
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": modal_title,
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "post_title",
                    "multiline": False,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Hello, World!",
                    },
                    "initial_value": post_title,
                },
                "label": {
                    "type": "plain_text",
                    "text": "Title",
                    "emoji": True,
                },
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "post_body",
                    "multiline": True,
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Write something _amazing!_",
                    },
                    "initial_value": post_body,
                },
                "label": {
                    "type": "plain_text",
                    "text": "Body (Markdown)",
                    "emoji": True,
                },
            },
            {
                "dispatch_action": True,
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "dispatch_action_config": {
                        "trigger_actions_on": ["on_character_entered"],
                    },
                    "action_id": "post_category",
                    "initial_value": post_category,
                },
                "label": {
                    "type": "plain_text",
                    "text": "Category",
                    "emoji": True,
                },
            },
        ],
    }
    if draft_button:
        modal["blocks"].append(
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Save draft :floppy_disk:",
                            "emoji": True,
                        },
                        "value": "",
                        "action_id": "save_draft_button",
                    }
                ],
            }
        )

    if delete_button:
        modal["blocks"].append(
            {
                "type": "actions",
                "elements": [
                    {
                        "type": "button",
                        "text": {
                            "type": "plain_text",
                            "text": "Delete :no_entry_sign:",
                            "emoji": True,
                        },
                        "value": "",
                        "action_id": "delete_button",
                    }
                ],
            }
        )

    return modal


@pytest.fixture(scope="module")
def post_modal_new():
    modal = post_modal(
        modal_title="New post",
        post_title="",
        post_body="",
        post_category="",
        private_metadata="",
        draft_button=True,
        delete_button=False,
    )
    return modal


@pytest.fixture(scope="module")
def post_modal_draft():
    modal = post_modal(
        modal_title="Edit draft post",
        post_title="foo",
        post_body="bar",
        post_category="baz",
        private_metadata="asdf",
        draft_button=True,
        delete_button=True,
    )
    return modal


@pytest.fixture(scope="module")
def post_modal_published():
    modal = post_modal(
        modal_title="Edit published post",
        post_title="foo",
        post_body="bar",
        post_category="baz",
        private_metadata="asdf",
        draft_button=False,
        delete_button=True,
    )
    return modal
