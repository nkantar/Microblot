from microblot.slack.modals import block_post_input


def test_block_post_input():
    block = block_post_input(
        initial_value="foo",
        label="bar",
        placeholder="baz",
        action_id="barf",
        multiline=True,
    )
    assert block == {
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "action_id": "barf",
            "multiline": True,
            "placeholder": {
                "type": "plain_text",
                "text": "baz",
            },
            "initial_value": "foo",
        },
        "label": {
            "type": "plain_text",
            "text": "bar",
            "emoji": True,
        },
    }
