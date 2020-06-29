import hashlib
import hmac
import json

import requests

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from microblot.blogs.models import Blog

from .modals import NEW_POST


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


def slack_new(request):
    blog = Blog.objects.get(platform__team_id=request.POST["team_id"])
    views_open_url = f"{settings.SLACK_API_ROOT_URL}/views.open"
    new_modal_response = requests.post(
        views_open_url,
        data={
            "token": blog.platform["bot_access_token"],
            "trigger_id": request.POST["trigger_id"],
            "view": NEW_POST,
            "callback_id": "foobar",
        },
    )

    # TODO: switch to Slack Python SDK, maybe that'll help? #50

    return JsonResponse({"status_code": 200, "message": ""})
    # return HttpResponse("New post, got it!")  # TODO #19


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


def slack_info():
    return HttpResponse("info")  # TODO #32


@csrf_exempt
def dispatch(request):
    # TODO #25

    slack_signature = request.headers["X-Slack-Signature"]

    request_timestamp = request.headers["X-Slack-Request-Timestamp"]
    request_body = request.body.decode()
    message = f"v0:{request_timestamp}:{request_body}"
    hashed_message = hmac.new(
        bytes(settings.SLACK_SIGNING_SECRET, "utf-8"),
        bytes(message, "utf-8"),
        digestmod=hashlib.sha256,
    ).hexdigest()
    signature = f"v0={hashed_message}"

    signatures_match = hmac.compare_digest(slack_signature, signature)
    if not signatures_match:
        return HttpResponseForbidden

    text = request.POST.get("text")
    params = text.split(maxsplit=1)
    command = params[0]
    func = globals().get(f"slack_{command}")

    print(command)

    # TODO #24
    return func(request)
