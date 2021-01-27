from functools import wraps
import json

from slack_sdk.signature import SignatureVerifier

from django.conf import settings
from django.http import HttpResponse, HttpResponseForbidden
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import View

from . import commands, interactions


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
        try:
            slack_command, *params = request.POST.get("text").split(maxsplit=1)
        except ValueError:
            slack_command = "help"
            params = []

        command = getattr(commands, f"command_{slack_command}", commands.command_help)

        response = command(
            team_id=request.POST.get("team_id"),
            user_id=request.POST.get("user_id"),
            token=request.POST.get("token"),
            response_url=request.POST.get("response_url"),
            trigger_id=request.POST.get("trigger_id"),
            params=params,
        )

        if response is not None:
            return response

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
        submission = json.loads(request.POST["payload"])
        modal_data = {
            key: submission["view"]["state"]["values"][key][f"{key}_action"]["value"]
            for key in submission["view"]["state"]["values"]
        }
        modal_callback_id = submission["view"]["callback_id"]
        interaction = getattr(interactions, modal_callback_id)
        interaction(
            team_id=submission["team"]["id"],
            user_id=submission["user"]["id"],
            modal_data=modal_data,
        )
        return HttpResponse()
