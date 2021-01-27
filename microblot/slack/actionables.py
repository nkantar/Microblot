from slack_sdk import WebClient

from .models import SlackWorkspace
from .modals import populate_post_modal


def command_new(team_id, user_id, action, params, token, response_url, trigger_id):
    workspace = SlackWorkspace.objects.get(slack_id=team_id)
    client = WebClient(token=workspace.bot_access_token)
    response = client.views_open(
        trigger_id=trigger_id,
        view=populate_post_modal(modal_type="new_post"),
    )
    ok = response.get("ok", False)
    return ok
