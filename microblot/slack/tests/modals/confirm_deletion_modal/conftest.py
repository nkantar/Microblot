import pytest


@pytest.fixture(scope="module")
def modal_confirm_deletion():
    modal = {
        "type": "modal",
        "title": {
            "type": "plain_text",
            "text": "Microblot",
            "emoji": True,
        },
        "private_metadata": "baz",
        "close": {
            "type": "plain_text",
            "text": "Cancel",
            "emoji": True,
        },
        "submit": {
            "type": "plain_text",
            "text": "Delete",
            "emoji": True,
        },
        "blocks": [
            {
                "type": "header",
                "text": {
                    "type": "plain_text",
                    "text": "Confirm post deletion",
                    "emoji": True,
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "Are you sure you want to delete *foo bar*?",
                },
            },
            {
                "type": "section",
                "text": {
                    "type": "mrkdwn",
                    "text": "This action is irreversible!",
                },
            },
        ],
    }
    return modal
