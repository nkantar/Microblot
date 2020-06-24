from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt


def ping(request):
    return HttpResponse("pong")


def slack_oauth(request):
    print(request.GET)
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
