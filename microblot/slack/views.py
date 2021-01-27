from functools import wraps
import json

from slack_sdk.signature import SignatureVerifier

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from microblot.cms.models import Blog, Post

from . import actionables


def verify_slack_signature(func):
    @wraps(func)
    def wrapper_verify_slack_signature(*args, **kwargs):
        request = args[1]
        signature_verifier = SignatureVerifier(
            signing_secret=settings.SLACK_SIGNING_SECRET
        )
        if not signature_verifier.is_valid(
            body=request.body,
            timestamp=request.headers.get("X-Slack-Request-Timestamp"),
            signature=request.headers.get("X-Slack-Signature"),
        ):
            return HttpResponseForbidden()

        return func(*args, **kwargs)

    return wrapper_verify_slack_signature


def respond_to_challenge(func):
    @wraps(func)
    def wrapper_respond_to_challenge(*args, **kwargs):
        request = args[1]
        if "challenge" in request.POST:
            return HttpResponse(request.POST.get("challenge"))

        return func(*args, **kwargs)

    return wrapper_respond_to_challenge


class SlackCommandView(View):
    @csrf_exempt
    @verify_slack_signature
    def post(self, request, *args, **kwargs):
        command, *params = request.POST.get("text").split(maxsplit=1)

        actionable = getattr(actionables, f"command_{command}")

        actionable(
            team_id=request.POST.get("team_id"),
            user_id=request.POST.get("user_id"),
            action=command,
            params=params,
            token=request.POST.get("token"),
            response_url=request.POST.get("response_url"),
            trigger_id=request.POST.get("trigger_id"),
        )

        return HttpResponse()


class SlackEventView(View):
    @csrf_exempt
    @verify_slack_signature
    @respond_to_challenge
    def post(self, request, *args, **kwargs):
        ...  # TODO


class SlackInteractiveView(View):
    @csrf_exempt
    @verify_slack_signature
    def post(self, request, *args, **kwargs):
        print(request.POST)

        submissions = request.POST["payload"]

        for submission_str in submissions:
            submission = json.loads(submission_str)

            modal_data = {
                key: submission["view"]["state"]["values"]["key"]["value"]
                for key in submission["view"]["state"]["values"]
            }

            params = {
                "modal_type": submission["view"]["callback_id"],
                "private_metadata": submission["view"]["private_metadata"],
                "modal_data": modal_data,
            }

            interaction = SlackInteraction(
                team_id=submission["team"]["id"],
                user_id=submission["user"]["id"],
                action="new_post",
                params=params,
            )
            interaction.execute()
