import json

import requests

from django.conf import settings
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from microblot.blogs.models import Blog


def ping(request):
    return HttpResponse("pong")


def slack_oauth(request):
    oauth_response = requests.post(
        settings.SLACK_OAUTH_ACCESS_URL,
        data={
            "client_id": settings.SLACK_CLIENT_ID,
            "client_secret": settings.SLACK_CLIENT_SECRET,
            "code": request.GET.get("code"),
            "redirect_uri": settings.SLACK_REDIRECT_URL,
        },
    )
    oauth_content = json.loads(oauth_response.content)

    team_info_url = f"{settings.SLACK_API_ROOT_URL}/team.info"
    team_info_response = requests.get(
        team_info_url,
        headers={"content-type": "application/x-www-form-urlencoded"},
        params={
            "token": oauth_content["access_token"],
            "team": oauth_content["team"]["id"],
        },
    )
    team_info_content = json.loads(team_info_response.content)

    breakpoint()

    blog = Blog.objects.create(
        slug=team_info_content["team"]["domain"],
        name=team_info_content["team"]["name"],
        platform={
            "bot_user_id": oauth_content["bot_user_id"],
            "bot_access_token": oauth_content["access_token"],
            "team_id": oauth_content["team"]["id"],
        },
    )

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
