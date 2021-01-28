import json
from string import Template


POST_MODAL_TEMPLATE = Template(
    json.dumps(
        {
            "type": "modal",
            "callback_id": "$modal_type",
            "title": {
                "type": "plain_text",
                "text": "Microblot: New Post",
            },
            "submit": {
                "type": "plain_text",
                "text": "Submit",
            },
            "close": {
                "type": "plain_text",
                "text": "Cancel",
            },
            "private_metadata": "$private_metadata",
            "blocks": [
                {
                    "type": "input",
                    "block_id": "post_title",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_title_action",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Witty title goes here.",
                        },
                        "initial_value": "$post_title",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Title",
                    },
                },
                {
                    "type": "input",
                    "block_id": "post_body",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_body_action",
                        "multiline": True,
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Mind blowing post goes here. Markdown supported.",
                        },
                        "initial_value": "$post_body",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Body",
                    },
                    "hint": {
                        "type": "plain_text",
                        "text": "GitHub Flavored Markdown supported",
                    },
                },
                {
                    "type": "input",
                    "block_id": "post_category",
                    "element": {
                        "type": "plain_text_input",
                        "action_id": "post_category_action",
                        "placeholder": {
                            "type": "plain_text",
                            "text": "Sensible category goes here.",
                        },
                        "initial_value": "$post_category",
                    },
                    "label": {
                        "type": "plain_text",
                        "text": "Category",
                    },
                },
                {
                    "type": "actions",
                    "elements": [
                        {
                            "type": "button",
                            "text": {
                                "type": "plain_text",
                                "text": "Preview",
                                "emoji": True,
                            },
                            "value": "preview_post",
                            "action_id": "actionId-0",
                        }
                    ],
                },
            ],
        }
    )
)


def populate_post_modal(
    modal_type="",
    private_metadata="",
    post_title="",
    post_body="",
    post_category="",
):
    modal = POST_MODAL_TEMPLATE.substitute(
        modal_type=modal_type,
        private_metadata=private_metadata,
        post_title=post_title,
        post_body=post_body,
        post_category=post_category,
    )
    return modal
