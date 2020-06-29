import hashlib
import hmac

import requests
from slack import WebClient
from slack.signature import SignatureVerifier

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from microblot.blogs.models import Blog

from .modals import NEW_POST


def ping(request):
    return HttpResponse("pong")


def slack_oauth(request):
    code = request.GET["code"]

    oauth_client = WebClient(token="")
    response = oauth_client.oauth_v2_access(
        client_id=settings.SLACK_CLIENT_ID,
        client_secret=settings.SLACK_CLIENT_SECRET,
        code=code,
    )

    bot_user_id = response.data["bot_user_id"]
    bot_access_token = response.data["access_token"]
    team_id = response.data["team"]["id"]

    authed_client = WebClient(token=bot_access_token)
    team_info = authed_client.team_info().data

    team_domain = team_info["team"]["domain"]
    team_name = team_info["team"]["name"]

    blog, unused_blog_created = Blog.objects.update_or_create(
        slack_id=team_id,
        defaults={
            "slug": team_domain,
            "name": team_name,
            "bot_user_id": bot_user_id,
            "bot_access_token": bot_access_token,
        },
    )

    return HttpResponse("oauth")  # TODO #19


def slack_new(request):
    trigger_id = request.POST["trigger_id"]
    team_id = request.POST["team_id"]

    blog = Blog.objects.get(slack_id=team_id)

    client = WebClient(token=blog.bot_access_token)

    response = client.views_open(trigger_id=trigger_id, view=NEW_POST)

    return JsonResponse({"status_code": 200, "message": ""})


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

    signature_verifier = SignatureVerifier(settings.SLACK_SIGNING_SECRET)

    if not signature_verifier.is_valid_request(request.body, request.headers):
        return HttpResponseForbidden

    text = request.POST.get("text")
    params = text.split(maxsplit=1)
    try:
        command = params[0]
    except IndexError:
        command = "help"
    func = globals().get(f"slack_{command}")

    print(command)

    # TODO #24
    return func(request)
