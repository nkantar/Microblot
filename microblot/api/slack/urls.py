from django.urls import path

from . import views


urlpatterns = [
    path("", views.dispatch, name="slack-dispatch"),
    path("ping", views.ping, name="slack-ping"),
]
