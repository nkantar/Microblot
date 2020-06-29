import json


NEW_POST = json.dumps(
    {
        "type": "modal",
        "callback_id": "modal-id",
        "title": {"type": "plain_text", "text": "Microblot: New Post"},
        "submit": {"type": "plain_text", "text": "Submit"},
        "close": {"type": "plain_text", "text": "Cancel"},
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
                },
                "label": {"type": "plain_text", "text": "Category"},
            },
        ],
    }
)
