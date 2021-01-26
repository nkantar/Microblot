from django.urls import path

from microblot.core.views import dispatch
from .views import SlackCommandView, SlackEventView, SlackInteractiveView


urlpatterns = [
    path(
        "command/",
        dispatch,
        {
            "main_class": SlackCommandView,
        },
        name="dispatch-slack-command",
    ),
    path(
        "event/",
        dispatch,
        {
            "main_class": SlackEventView,
        },
        name="dispatch-slack-event",
    ),
    path(
        "interactive/",
        dispatch,
        {
            "main_class": SlackInteractiveView,
        },
        name="dispatch-slack-interactive",
    ),
]
