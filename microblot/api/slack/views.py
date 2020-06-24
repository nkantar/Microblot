from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

from .helpers import find_command


def ping(request):
    return HttpResponse("pong")


def oauth(request):
    ...  # TODO #19


def new_post():
    return HttpResponse("new")  # TODO #20


def list_posts():
    return HttpResponse("list")  # TODO #21


def edit_post():
    return HttpResponse("edit")  # TODO #22


def delete_post():
    return HttpResponse("delete")  # TODO #23


def slack_help():
    return HttpResponse("help")  # TODO #30


@csrf_exempt
def dispatch(request):
    # TODO #25
    command = find_command(request.body.decode("utf-8"))

    func = locals().get(f"{command}_post")
    # TODO #24
    return func()
