import json

import requests

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def ping(request):
    return HttpResponse("pong")


def slack_oauth(request):
    response = requests.post(
        settings.SLACK_OAUTH_ACCESS_URL,
        data={
            "client_id": settings.SLACK_CLIENT_ID,
            "client_secret": settings.SLACK_CLIENT_SECRET,
            "code": request.GET.get("code"),
            "redirect_uri": settings.SLACK_REDIRECT_URL,
        },
    )

    content = json.loads(response.content)

    bot_user_id = content["bot_user_id"]
    bot_access_token = content["access_token"]

    team_id = content["team"]["id"]
    team_name = content["team"]["name"]

    # TODO create relevant site once #41 is done

    return HttpResponse("oauth")  # TODO #19


def slack_new():
    return HttpResponse("new")  # TODO #20


def slack_list():
    return HttpResponse("list")  # TODO #21


def slack_edit(post_id):
    print(post_id)  # TODO
    return HttpResponse("edit")  # TODO #22


def slack_delete(post_id):
    print(post_id)  # TODO
    return HttpResponse("delete")  # TODO #23


def slack_help():
    return HttpResponse("help")  # TODO #30


def slack_uninstall():
    return HttpResponse("uninstall")  # TODO #31


def slack_download():
    return HttpResponse("download")  # TODO #32


@csrf_exempt
def dispatch(request):
    # TODO #25

    text = request.GET.get("text")
    params = text.split(maxsplit=1)
    command = params[0]
    func = globals().get(f"slack_{command}")

    # TODO #24
    return func(*(params[1:]))
