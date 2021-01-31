from microblot.slack.modals import confirm_deletion_modal


def test_confirm_deletion_modal(modal_confirm_deletion):
    modal = confirm_deletion_modal(
        post_title="foo bar",
        post_id="baz",
    )
    assert modal == modal_confirm_deletion
