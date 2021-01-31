from microblot.slack.modals import main_modal


def test_main_modal_no_drafts_or_posts(main_modal_empty):
    modal = main_modal(
        blog_name="foo",
        blog_url="bar",
        blog_domain="baz",
        drafts=[],
        posts=[],
    )
    assert modal == main_modal_empty


def test_main_modal_up_to_max_drafts_and_posts(
    main_modal_up_to_max,
    one_post,
    max_posts,
):
    modal = main_modal(
        blog_name="foo",
        blog_url="bar",
        blog_domain="baz",
        drafts=[one_post],
        posts=max_posts,
    )
    assert modal == main_modal_up_to_max


def test_main_modal_more_drafts_and_posts(more_posts, main_modal_more):
    modal = main_modal(
        blog_name="foo",
        blog_url="bar",
        blog_domain="baz",
        drafts=more_posts,
        posts=more_posts,
    )
    assert modal == main_modal_more
