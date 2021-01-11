import json
from string import Template


POST_MODAL = Template(
    json.dumps(
        {
            "type": "modal",
            "callback_id": "modal-id",
            "title": {"type": "plain_text", "text": "Microblot: New Post"},
            "submit": {"type": "plain_text", "text": "Submit"},
            "close": {"type": "plain_text", "text": "Cancel"},
            "private_metadata": "$private_metadata",
            "blocks": [
                {
                    "type": "input",
                    "block_id": "post_title_id",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_title_action_id",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Witty title goes here",
                        },
                        "initial_value": "$post_title",
                    },
                    "label": {"type": "plain_text", "text": "Title"},
                },
                {
                    "type": "input",
                    "block_id": "post_body_md_id",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_body_md_action_id",
                        "multiline": True,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Mind blowing post goes here",
                        },
                        "initial_value": "$post_body_md",
                    },
                    "label": {"type": "plain_text", "text": "Body"},
                    "hint": {
                        "type": "plain_text",
                        "text": "GitHub Flavored Markdown supported",
                    },
                },
                {
                    "type": "input",
                    "block_id": "post_category_id",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_category_action_id",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Sensible category goes here",
                        },
                        "initial_value": "$post_category",
                    },
                    "label": {"type": "plain_text", "text": "Category"},
                },
            ],
        }
    )
)


def populate_post_modal(
    private_metadata="", post_title="", post_body_md="", post_category=""
):
    return POST_MODAL.substitute(
        private_metadata=private_metadata,
        post_title=post_title,
        post_body_md=post_body_md,
        post_category=post_category,
    )
