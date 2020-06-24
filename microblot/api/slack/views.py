from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helpers import find_command


def ping(request):
    return HttpResponse("pong")


def slack_oauth(request):
    return HttpResponse("oauth")  # TODO #19


def slack_new():
    return HttpResponse("new")  # TODO #20


def slack_list():
    return HttpResponse("list")  # TODO #21


def slack_edit():
    return HttpResponse("edit")  # TODO #22


def slack_delete():
    return HttpResponse("delete")  # TODO #23


def slack_help():
    return HttpResponse("help")  # TODO #30


@csrf_exempt
def dispatch(request):
    # TODO #25
    command = find_command(request.body.decode("utf-8"))

    func = locals().get(f"slack_{command}")
    # TODO #24
    return func()
