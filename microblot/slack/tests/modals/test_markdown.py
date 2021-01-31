from microblot.slack.modals import block_markdown


def test_block_markdown():
    block = block_markdown("foo _bar_ baz")
    assert block == {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": "foo _bar_ baz",
        },
    }
