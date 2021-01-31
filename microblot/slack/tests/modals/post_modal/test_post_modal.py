from microblot.slack.modals import post_modal


def test_new_post_modal(post_modal_new):
    modal = post_modal(
        modal_type="new",
        post_title="",
        post_body="",
        post_category="",
        post_id="",
    )
    assert modal == post_modal_new


def test_draft_post_modal(post_modal_draft):
    modal = post_modal(
        modal_type="draft",
        post_title="foo",
        post_body="bar",
        post_category="baz",
        post_id="asdf",
    )
    assert modal == post_modal_draft


def test_published_post_modal(post_modal_published):
    modal = post_modal(
        modal_type="published",
        post_title="foo",
        post_body="bar",
        post_category="baz",
        post_id="asdf",
    )
    assert modal == post_modal_published
