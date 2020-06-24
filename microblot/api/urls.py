from django.urls import include, path

# from .slack import urls as slack_urls

urlpatterns = [
    path("slack/", include("microblot.api.slack.urls")),
]
