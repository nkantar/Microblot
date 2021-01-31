from microblot.slack.modals import block_post_category


def test_block_post_category():
    block = block_post_category("foo")
    assert block == {
        "dispatch_action": True,
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "dispatch_action_config": {
                "trigger_actions_on": ["on_character_entered"],
            },
            "action_id": "post_category",
            "initial_value": "foo",
        },
        "label": {
            "type": "plain_text",
            "text": "Category",
            "emoji": True,
        },
    }
