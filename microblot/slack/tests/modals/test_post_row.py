from microblot.slack.modals import block_post_row


def test_block_post_row():
    block = block_post_row("foo", "bar")
    assert block == {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "foo",
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Edit :pencil2:",
                "emoji": True,
            },
            "value": "bar",
            "action_id": "edit_post_button",
        },
    }
