from django.contrib import admin
from django.urls import include, path
from django.conf import settings

from microblot.cms.views import BlogHomeView
from microblot.core.views import dispatch
from microblot.main.views import MainHomeView
from microblot.shortener.views import ShortenerHomeRedirectView

urlpatterns = [
    path(
        "",
        dispatch,
        {
            "main_class": MainHomeView,
            "cms_class": BlogHomeView,
            "short_class": ShortenerHomeRedirectView,
        },
        name="dispatch-home",
    ),
    path("", include("microblot.cms.urls")),
    path("", include("microblot.shortener.urls")),
    path("api/slack/", include("microblot.slack.urls")),
]


if settings.DEBUG:
    urlpatterns += [
        path("admin/", admin.site.urls),
    ]
