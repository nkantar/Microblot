from microblot.slack.modals import main_button


def test_main_button():
    button = main_button("foo")
    assert button == {
        "type": "plain_text",
        "text": "foo",
        "emoji": True,
    }
