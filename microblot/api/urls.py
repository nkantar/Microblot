from django.urls import include, path


urlpatterns = [
    path("slack/", include("microblot.api.slack.urls")),
]
