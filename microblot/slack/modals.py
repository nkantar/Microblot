POST_ROW_MAX = 2

POST_MODAL_TYPE_TITLES = {
    "new": "New post",
    "draft": "Edit draft post",
    "published": "Edit published post",
}

MODAL_BASE = {
    "type": "modal",
    "title": {
        "type": "plain_text",
        "text": "Microblot",
        "emoji": True,
    },
}


def block_markdown(text):
    block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": text,
        },
    }
    return block


def block_secondary_button(text, action_id):
    block = {
        "type": "actions",
        "elements": [
            {
                "type": "button",
                "text": {
                    "type": "plain_text",
                    "text": text,
                    "emoji": True,
                },
                "value": "",
                "action_id": action_id,
            }
        ],
    }
    return block


def block_header(text):
    block = {
        "type": "header",
        "text": {
            "type": "plain_text",
            "text": text,
            "emoji": True,
        },
    }
    return block


def block_post_row(title, post_id):
    block = {
        "type": "section",
        "text": {
            "type": "mrkdwn",
            "text": title,
        },
        "accessory": {
            "type": "button",
            "text": {
                "type": "plain_text",
                "text": "Edit :pencil2:",
                "emoji": True,
            },
            "value": post_id,
            "action_id": "edit_post_button",
        },
    }
    return block


def group_posts(posts, noun, emoji, action_id):
    blocks = []
    blocks.append(block_header(text=f"Your {noun}s ({len(posts)})"))
    if len(posts):
        for post in posts[:POST_ROW_MAX]:
            blocks.append(
                block_post_row(
                    title=post.title,
                    post_id=post.id,
                )
            )
    else:
        blocks.append(block_markdown(text=f"You have no {noun}s."))
    if len(posts) > POST_ROW_MAX:
        blocks.append(
            block_secondary_button(
                text=f"See all your {noun}s :{emoji}:",
                action_id=action_id,
            )
        )
    return blocks


def block_post_input(initial_value, label, placeholder, action_id, multiline):
    block = {
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "action_id": action_id,
            "multiline": multiline,
            "placeholder": {
                "type": "plain_text",
                "text": placeholder,
            },
            "initial_value": initial_value,
        },
        "label": {
            "type": "plain_text",
            "text": label,
            "emoji": True,
        },
    }
    return block


def block_post_category(initial_value):
    block = {
        "dispatch_action": True,
        "type": "input",
        "element": {
            "type": "plain_text_input",
            "dispatch_action_config": {
                "trigger_actions_on": ["on_character_entered"],
            },
            "action_id": "post_category",
            "initial_value": initial_value,
        },
        "label": {
            "type": "plain_text",
            "text": "Category",
            "emoji": True,
        },
    }
    return block


def main_button(text):
    button = {
        "type": "plain_text",
        "text": text,
        "emoji": True,
    }
    return button


def main_modal(blog_name, blog_url, blog_domain, drafts, posts):
    blocks = []

    # top section
    blocks.append(block_markdown(text=f"{blog_name}: <{blog_url}|{blog_domain}>"))
    blocks.append(
        block_secondary_button(
            text="New post :page_facing_up:",
            action_id="new_post_button",
        )
    )

    # drafts
    blocks.extend(
        group_posts(
            posts=drafts,
            noun="unpublished draft",
            emoji="notebook",
            action_id="all_drafts_button",
        )
    )

    # posts
    blocks.extend(
        group_posts(
            posts=posts,
            noun="published post",
            emoji="notebook_with_decorative_cover",
            action_id="all_posts_button",
        )
    )

    modal = {
        **MODAL_BASE,
        "close": main_button("Close"),
        "blocks": blocks,
    }

    return modal


def post_modal(modal_type, post_title, post_body, post_category, post_id):
    blocks = []

    # header
    blocks.append(block_header(text=POST_MODAL_TYPE_TITLES[modal_type]))

    # title field
    blocks.append(
        block_post_input(
            initial_value=post_title,
            label="Title",
            placeholder="Hello, World!",
            action_id="post_title",
            multiline=False,
        )
    )

    # body field
    blocks.append(
        block_post_input(
            initial_value=post_body,
            label="Body (Markdown)",
            placeholder="Write something _amazing!_",
            action_id="post_body",
            multiline=True,
        )
    )

    # category field
    blocks.append(block_post_category(initial_value=post_category))

    # save draft button
    if modal_type in ["new", "draft"]:
        blocks.append(
            block_secondary_button(
                text="Save draft :floppy_disk:",
                action_id="save_draft_button",
            )
        )

    # delete button
    if modal_type in ["draft", "published"]:
        blocks.append(
            block_secondary_button(
                text="Delete :no_entry_sign:",
                action_id="delete_button",
            )
        )

    # entire modal
    modal = {
        **MODAL_BASE,
        "private_metadata": post_id,
        "close": main_button("Cancel"),
        "submit": main_button("Publish"),
        "blocks": blocks,
    }

    return modal


def confirm_deletion_modal(post_title, post_id):
    blocks = []

    # header
    blocks.append(block_header(text="Confirm post deletion"))

    # text
    blocks.append(
        block_markdown(text=f"Are you sure you want to delete *{post_title}*?")
    )
    blocks.append(block_markdown(text="This action is irreversible!"))

    modal = {
        **MODAL_BASE,
        "private_metadata": post_id,
        "close": main_button("Cancel"),
        "submit": main_button("Delete"),
        "blocks": blocks,
    }

    return modal
