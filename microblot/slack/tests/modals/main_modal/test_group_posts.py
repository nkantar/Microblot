from microblot.slack.modals import group_posts


def test_group_posts_empty(no_drafts_group):
    group = group_posts(
        posts=[],
        noun="unpublished draft",
        emoji="notebook",
        action_id="all_drafts_button",
    )
    assert group == no_drafts_group


def test_group_posts_one(one_post, one_draft_group):
    group = group_posts(
        posts=[one_post],
        noun="unpublished draft",
        emoji="notebook",
        action_id="all_drafts_button",
    )
    assert group == one_draft_group


def test_group_posts_max(max_posts, max_posts_group):
    group = group_posts(
        posts=max_posts,
        noun="published post",
        emoji="notebook_with_decorative_cover",
        action_id="all_posts_button",
    )
    assert group == max_posts_group


def test_group_posts_more(more_posts, more_posts_group):
    group = group_posts(
        posts=more_posts,
        noun="published post",
        emoji="notebook_with_decorative_cover",
        action_id="all_posts_button",
    )
    assert group == more_posts_group
