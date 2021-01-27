from slack_sdk import WebClient

from django.http import HttpResponse

from .models import SlackWorkspace
from .modals import populate_post_modal


def command_new(team_id, user_id, token, response_url, trigger_id, params=None):
    workspace = SlackWorkspace.objects.get(slack_id=team_id)
    client = WebClient(token=workspace.bot_access_token)
    client.views_open(
        trigger_id=trigger_id,
        view=populate_post_modal(modal_type="new_post"),
    )


def command_list(team_id, user_id, token, response_url, trigger_id, params=None):
    ...  # TODO


def command_edit(team_id, user_id, token, response_url, trigger_id, params=None):
    ...  # TODO


def command_delete(team_id, user_id, token, response_url, trigger_id, params=None):
    ...  # TODO


def command_info(team_id, user_id, token, response_url, trigger_id, params=None):
    ...  # TODO


def command_help(*args, **kwargs):
    help_text = (
        "Hi, this is Microblot.\n\n"
        "There are several commands you can run:\n"
        "• `/microblot new` to create a new post\n"
        "• `/microblot list` to list posts\n"
        "• `/microblot edit <id>` to edit post\n"
        "• `/microblot delete <id>` to delete post\n"
        "• `/microblot info` to view blog information\n"
        "• `/microblot help` for this help message\n"
    )

    return HttpResponse(help_text)
