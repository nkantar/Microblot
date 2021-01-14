# Slack Integration Routes

These routes are intended for the Slack integration.

| `/microblot` subcommand | API endpoint |
|:----------------------- |:------------ |
| `new` | `POST /api/slack/posts` |
| `list` | `GET /api/slack/posts` |
| `edit <id>` | `PUT /api/slack/posts/<id>` |
| `delete <id>` | `DELETE /api/slack/posts/<id>` |
| `info` | `GET /api/slack/info` |
| `help` | `GET /api/slack/help` |
