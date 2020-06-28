import json


NEW_POST = json.dumps(
    {
        "type": "modal",
        "title": {"type": "plain_text", "text": "Microblot: New Post"},
        "submit": {"type": "plain_text", "text": "Submit"},
        "blocks": [
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "post_title",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Witty title goes here",
                    },
                },
                "label": {"type": "plain_text", "text": "Title"},
            },
            {
                "type": "input",
                "element": {
                    "type": "plain_text_input",
                    "action_id": "post_body_md",
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
                "element": {
                    "type": "plain_text_input",
                    "action_id": "post_category",
                    "placeholder": {
                        "type": "plain_text",
                        "text": "Sensible category goes here",
                    },
                },
                "label": {"type": "plain_text", "text": "Category"},
            },
        ],
        "type": "modal",
    }
)
