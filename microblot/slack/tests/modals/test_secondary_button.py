from microblot.slack.modals import block_secondary_button


def test_block_secondary_markdown():
    block = block_secondary_button("foo", "bar")
    assert block == {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": "foo",
                    "emoji": True,
                },
                "value": "",
                "action_id": "bar",
            }
        ],
    }
