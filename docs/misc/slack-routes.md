# Slack Integration Routes

These routes are intended for the Slack integration.

| `/microblot` subcommand | API endpoint |
|:----------------------- |:------------ |
| `new` | `POST /slack/posts` |
| `list` | `GET /slack/posts` |
| `edit <id>` | `PUT /slack/posts/<id>` |
| `delete <id>` | `DELETE /slack/posts/<id>` |
| `info` | `GET /slack/info` |
| `help` | `GET /slack/help` |
