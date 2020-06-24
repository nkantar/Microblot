from django.urls import path

from . import views


urlpatterns = [
    path("", views.dispatch, name="slack-dispatch"),
    path("oauth/", views.slack_oauth, name="slack-oauth"),
    path("ping/", views.ping, name="slack-ping"),
]
