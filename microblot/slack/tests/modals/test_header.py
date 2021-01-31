from microblot.slack.modals import block_header


def test_block_header():
    block = block_header("foo")
    assert block == {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": "foo",
            "emoji": True,
        },
    }
